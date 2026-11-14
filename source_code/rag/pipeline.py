"""The RAG pipeline: retrieve relevant chunks, build a prompt, generate an answer."""

from __future__ import annotations

import time
from dataclasses import asdict, dataclass, field
from typing import Dict, Iterator, List, Optional, Sequence

from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

from . import models, prompts
from .config import Settings, get_settings
from .indexer import VectorIndex

# A conversation turn as stored by the UI/CLI: {"role": "user"|"assistant", "content": "..."}
Turn = Dict[str, str]


@dataclass
class RetrievedChunk:
    content: str
    source: str
    page: Optional[int]
    score: float  # cosine similarity in [0, 1], higher is better

    @property
    def label(self) -> str:
        return prompts.format_source_label({"source": self.source, "page": self.page})


@dataclass
class RAGResponse:
    question: str
    answer: str
    sources: List[RetrievedChunk] = field(default_factory=list)
    used_fallback: bool = False
    latency_s: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)


class RAGPipeline:
    def __init__(
        self,
        settings: Optional[Settings] = None,
        embeddings: Optional[Embeddings] = None,
        llm: Optional[BaseChatModel] = None,
        index: Optional[VectorIndex] = None,
    ):
        self.settings = settings or get_settings()
        self.embeddings = embeddings or models.get_embeddings(self.settings)
        self.llm = llm or models.get_chat_model(self.settings)
        self.index = index or VectorIndex(self.settings, self.embeddings)

    # -------------------------------------------------------------- indexing
    def ensure_index(self, force: bool = False) -> Dict[str, int]:
        return self.index.build(force=force)

    # ------------------------------------------------------------- retrieval
    def _search(self, query: str, k: int) -> List[RetrievedChunk]:
        results = models.with_retries(lambda: self.index.store.similarity_search_with_score(query, k=k))
        return [
            RetrievedChunk(
                content=doc.page_content,
                source=str(doc.metadata.get("source", "unknown")),
                page=doc.metadata.get("page"),
                score=round(1.0 - float(distance), 4),
            )
            for doc, distance in results
        ]

    def retrieve(self, question: str, history: Sequence[Turn] = ()) -> List[RetrievedChunk]:
        """Top-k chunks for the question.

        For follow-up questions ("what are its prerequisites?") the previous
        user question is also used as a query and the results are merged, so
        the retriever still knows what "its" refers to.
        """
        k = self.settings.top_k
        chunks = self._search(question, k)
        previous = [t["content"] for t in history if t.get("role") == "user"]
        if previous:
            chunks += self._search(f"{previous[-1]} {question}", k)

        best: Dict[str, RetrievedChunk] = {}
        for chunk in chunks:
            key = f"{chunk.label}|{chunk.content[:80]}"
            if key not in best or chunk.score > best[key].score:
                best[key] = chunk
        ranked = sorted(best.values(), key=lambda c: c.score, reverse=True)[:k]
        return [c for c in ranked if c.score >= self.settings.min_score]

    # ------------------------------------------------------------ generation
    def build_messages(
        self, question: str, chunks: List[RetrievedChunk], history: Sequence[Turn] = ()
    ) -> List[BaseMessage]:
        context = prompts.format_context(chunks)
        example = chunks[0].label if chunks else "handbook.pdf p.7"
        messages: List[BaseMessage] = [
            SystemMessage(prompts.system_prompt(context, self.settings.allow_general_knowledge, example))
        ]
        recent = list(history)[-2 * self.settings.history_turns :] if self.settings.history_turns > 0 else []
        for turn in recent:
            cls = HumanMessage if turn.get("role") == "user" else AIMessage
            messages.append(cls(turn.get("content", "")))
        messages.append(HumanMessage(prompts.question_message(question, self.settings.allow_general_knowledge)))
        return messages

    def _refuse_without_llm(self, chunks: List[RetrievedChunk]) -> bool:
        """In strict mode with nothing relevant retrieved, the answer is known: don't ask the model.

        Small models often answer from memory anyway, so this makes the refusal deterministic
        (and instant).
        """
        return not chunks and not self.settings.allow_general_knowledge

    def ask(self, question: str, history: Sequence[Turn] = ()) -> RAGResponse:
        start = time.perf_counter()
        chunks = self.retrieve(question, history)
        if self._refuse_without_llm(chunks):
            answer = prompts.NOT_FOUND
        else:
            messages = self.build_messages(question, chunks, history)
            answer = str(models.with_retries(lambda: self.llm.invoke(messages)).content).strip()
        return RAGResponse(
            question=question,
            answer=answer,
            sources=chunks,
            used_fallback=not chunks,
            latency_s=round(time.perf_counter() - start, 2),
        )

    def stream(self, question: str, history: Sequence[Turn] = ()):
        """Like `ask`, but returns (sources, token_iterator) for streaming UIs."""
        chunks = self.retrieve(question, history)
        if self._refuse_without_llm(chunks):
            return chunks, iter([prompts.NOT_FOUND])
        messages = self.build_messages(question, chunks, history)

        def tokens() -> Iterator[str]:
            # Retry only while nothing has been shown yet; a half-streamed answer is not restarted.
            for attempt in range(1, 4):
                started = False
                try:
                    for piece in self.llm.stream(messages):
                        started = True
                        yield str(piece.content)
                    return
                except Exception as exc:
                    if started or attempt == 3 or not models.is_transient(exc):
                        raise
                    time.sleep(attempt)

        return chunks, tokens()
