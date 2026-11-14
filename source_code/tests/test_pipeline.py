from dataclasses import replace

from rag import prompts
from rag.config import get_settings
from rag.pipeline import RAGPipeline


def make_pipeline(settings, embeddings, llm):
    pipeline = RAGPipeline(settings, embeddings=embeddings, llm=llm)
    pipeline.ensure_index()
    return pipeline


def test_ask_returns_answer_and_sources(settings, embeddings, llm):
    pipeline = make_pipeline(settings, embeddings, llm)
    response = pipeline.ask("How many credits are required?")
    assert "56" in response.answer
    assert len(response.sources) == settings.top_k
    assert not response.used_fallback
    assert all(s.source == "CS_MajorHandbook.pdf" and s.page for s in response.sources)


def test_prompt_contains_context_history_and_question(settings, embeddings, llm):
    pipeline = make_pipeline(settings, embeddings, llm)
    history = [{"role": "user", "content": "Tell me about CS 201"}, {"role": "assistant", "content": "It is DSA."}]
    chunks = pipeline.retrieve("What are its prerequisites?", history)
    messages = pipeline.build_messages("What are its prerequisites?", chunks, history)
    assert messages[0].type == "system" and "CS_MajorHandbook.pdf p." in messages[0].content
    assert [m.type for m in messages[1:]] == ["human", "ai", "human"]
    assert messages[-1].content.startswith("What are its prerequisites?")
    # strict mode repeats the grounding rule next to the question (small models forget it)
    assert prompts.NOT_FOUND in messages[-1].content


def test_low_scores_trigger_fallback(settings, embeddings, llm):
    pipeline = make_pipeline(settings.with_overrides(score_threshold=1.01), embeddings, llm)
    response = pipeline.ask("What is the tuition fee?")
    assert response.used_fallback and response.sources == []
    # strict mode refuses without calling the model
    assert response.answer == prompts.NOT_FOUND
    system = pipeline.build_messages("q", [])[0].content
    assert "No sufficiently relevant passages" in system


def test_stream_yields_tokens(settings, embeddings, llm):
    pipeline = make_pipeline(settings, embeddings, llm)
    sources, tokens = pipeline.stream("How many credits?")
    assert sources
    assert "56" in "".join(tokens)


def test_strict_stream_refuses_when_nothing_retrieved(settings, embeddings, llm):
    pipeline = make_pipeline(settings.with_overrides(score_threshold=1.01), embeddings, llm)
    sources, tokens = pipeline.stream("Who won the 2022 World Cup?")
    assert sources == [] and "".join(tokens) == prompts.NOT_FOUND


def test_general_knowledge_mode_still_asks_the_model(settings, embeddings, llm):
    pipeline = make_pipeline(
        settings.with_overrides(score_threshold=1.01, allow_general_knowledge=True), embeddings, llm
    )
    response = pipeline.ask("Who won the 2022 World Cup?")
    assert response.used_fallback and "56" in response.answer  # the fake LLM's reply
    assert pipeline.build_messages("q", [])[-1].content == "q"  # no strict reminder


def test_score_threshold_is_calibrated_per_embedding_model():
    def min_score(embed_model, threshold=None):
        return replace(get_settings(), embed_model=embed_model, score_threshold=threshold).min_score

    assert min_score("mxbai-embed-large") == 0.55
    assert min_score("mxbai-embed-large:latest") == 0.55
    assert min_score("nomic-embed-text") == 0.3
    assert min_score("mxbai-embed-large", 0.42) == 0.42  # an explicit setting wins


def test_citation_example_uses_a_retrieved_label(settings, embeddings, llm):
    pipeline = make_pipeline(settings, embeddings, llm)
    chunks = pipeline.retrieve("How many credits?")
    system = pipeline.build_messages("How many credits?", chunks)[0].content
    assert f"e.g. [{chunks[0].label}]" in system


class FlakyLLM:
    """Fails like a dropped connection a given number of times, then delegates to a real fake model."""

    def __init__(self, inner, failures):
        self.inner, self.failures = inner, failures

    def _maybe_fail(self):
        if self.failures:
            self.failures -= 1
            raise ConnectionError("Failed to connect to Ollama")

    def invoke(self, messages):
        self._maybe_fail()
        return self.inner.invoke(messages)

    def stream(self, messages):
        self._maybe_fail()
        return self.inner.stream(messages)


def test_transient_errors_are_retried(settings, embeddings, llm, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda s: None)
    pipeline = make_pipeline(settings, embeddings, llm)
    pipeline.llm = FlakyLLM(llm, failures=2)
    assert "56" in pipeline.ask("How many credits?").answer
    pipeline.llm = FlakyLLM(llm, failures=1)
    _, tokens = pipeline.stream("How many credits?")
    assert "56" in "".join(tokens)


def test_non_transient_errors_are_not_retried(settings, embeddings, llm):
    pipeline = make_pipeline(settings, embeddings, llm)

    class Broken:
        calls = 0

        def invoke(self, messages):
            Broken.calls += 1
            raise ValueError("bad request")

    pipeline.llm = Broken()
    try:
        pipeline.ask("How many credits?")
    except ValueError:
        pass
    assert Broken.calls == 1
