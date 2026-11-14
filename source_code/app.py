"""Streamlit web UI for the handbook RAG chatbot (Task 4).

Run locally:  streamlit run app.py
"""

from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import streamlit as st

from rag import RAGPipeline, get_settings
from rag.loaders import SUPPORTED_EXTENSIONS
from rag.models import check_ollama

EXAMPLE_QUESTIONS = [
    "How many credits are required for the Computer Science major?",
    "What are the prerequisites for CS 302?",
    "What GPA do I need to enroll in the Capstone?",
    "What are the major learning outcomes of the program?",
]

st.set_page_config(page_title="Handbook Chatbot", page_icon="🎓", layout="wide")


# --------------------------------------------------------------------- state
def init_state() -> None:
    st.session_state.setdefault("messages", [])  # [{role, content, sources, latency}]
    st.session_state.setdefault("uploaded", set())
    st.session_state.setdefault("pending_question", None)


@st.cache_resource(show_spinner=False)
def load_pipeline(settings) -> RAGPipeline:
    pipeline = RAGPipeline(settings)
    pipeline.ensure_index()
    return pipeline


def history_for_model():
    return [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]


def chat_as_markdown() -> str:
    lines = [f"# Chat export ({datetime.now():%Y-%m-%d %H:%M})\n"]
    for message in st.session_state.messages:
        who = "**You**" if message["role"] == "user" else "**Assistant**"
        lines.append(f"{who}: {message['content']}\n")
        for src in message.get("sources", []):
            lines.append(f"> source: {src['label']} (score {src['score']:.2f})")
        lines.append("")
    return "\n".join(lines)


# ------------------------------------------------------------------- sidebar
def sidebar():
    base = get_settings()
    st.sidebar.title("⚙️ Settings")

    status = check_ollama(base)
    if status["reachable"]:
        st.sidebar.success(f"Ollama connected · {len(status['models'])} model(s)")
    else:
        st.sidebar.error(status["error"])

    models = status["models"] or [base.llm_model]
    chat_models = [m for m in models if "embed" not in m] or [base.llm_model]
    default_idx = next((i for i, m in enumerate(chat_models) if m.startswith(base.llm_model)), 0)
    llm_model = st.sidebar.selectbox("Language model", chat_models, index=default_idx)
    top_k = st.sidebar.slider("Chunks to retrieve (top-k)", 1, 15, base.top_k)
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, base.temperature, 0.05)
    strict = st.sidebar.toggle(
        "Answer only from documents",
        value=not base.allow_general_knowledge,
        help="When off, the model may fall back to its own knowledge if nothing relevant is retrieved.",
    )
    show_sources = st.sidebar.toggle("Show sources", value=True)

    settings = base.with_overrides(
        llm_model=llm_model, top_k=top_k, temperature=temperature, allow_general_knowledge=not strict
    )
    return settings, status, show_sources


def knowledge_base_panel(pipeline: RAGPipeline):
    settings = pipeline.settings
    st.sidebar.divider()
    st.sidebar.subheader("📚 Knowledge base")
    # Filled in after uploads/rebuilds below so the counts include them in the same run.
    summary = st.sidebar.empty()
    file_list = st.sidebar.expander("Indexed files")

    uploads = st.sidebar.file_uploader(
        "Add documents", type=[ext.lstrip(".") for ext in SUPPORTED_EXTENSIONS], accept_multiple_files=True
    )
    for upload in uploads or []:
        if upload.name in st.session_state.uploaded:
            continue
        target = Path(settings.data_dir) / upload.name
        target.write_bytes(upload.getbuffer())
        with st.sidebar.status(f"Indexing {upload.name}..."):
            n_chunks = pipeline.index.add_files([target])
        st.session_state.uploaded.add(upload.name)
        st.sidebar.success(f"Indexed {upload.name} ({n_chunks} chunks)")

    if st.sidebar.button("Rebuild index", use_container_width=True):
        with st.sidebar.status("Rebuilding vector store..."):
            stats = pipeline.ensure_index(force=True)
        st.sidebar.success(f"{stats['files']} file(s), {stats['chunks']} chunks")

    files = pipeline.index.indexed_files()
    summary.caption(f"{len(files)} file(s) · {pipeline.index.count()} chunks · `{settings.data_dir.name}/`")
    with file_list:
        for name in files:
            st.write(f"- {name}")

    st.sidebar.divider()
    # Filled by chat_actions() at the end of the run, once this turn's answer is in the history.
    return st.sidebar.container()


def chat_actions(slot) -> None:
    col1, col2 = slot.columns(2)
    if col1.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    # The export text is fixed when the button is drawn, so draw it after the newest answer.
    col2.download_button(
        "Export chat", chat_as_markdown(), file_name="chat.md", mime="text/markdown", use_container_width=True
    )


# ---------------------------------------------------------------------- chat
def render_sources(sources) -> None:
    if not sources:
        st.caption("No relevant passages retrieved.")
        return
    with st.expander(f"Sources ({len(sources)})"):
        for src in sources:
            st.markdown(f"**{src['label']}** · similarity `{src['score']:.2f}`")
            st.caption(src["content"][:600] + ("…" if len(src["content"]) > 600 else ""))


def render_history(show_sources: bool) -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant":
                if show_sources and (message.get("sources") or not message.get("failed")):
                    render_sources(message.get("sources", []))
                if message.get("latency") is not None:
                    st.caption(f"⏱ {message['latency']:.1f}s")


def answer(pipeline: RAGPipeline, question: str, show_sources: bool) -> None:
    history = history_for_model()
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        start = time.perf_counter()
        chunks, failed = [], False
        try:
            with st.spinner("Searching the handbook..."):
                chunks, tokens = pipeline.stream(question, history)
            text = st.write_stream(tokens)
        except Exception as exc:  # surface model/connection errors in the chat
            text = f"⚠️ Error while generating the answer: {exc}"
            failed = True
            st.error(text)
        latency = time.perf_counter() - start
        sources = [{"label": c.label, "score": c.score, "content": c.content} for c in chunks]
        # After an error "no relevant passages" would be misleading, so only list what was retrieved.
        if show_sources and (sources or not failed):
            render_sources(sources)
        st.caption(f"⏱ {latency:.1f}s")

    st.session_state.messages.append(
        {"role": "assistant", "content": text, "sources": sources, "latency": latency, "failed": failed}
    )


def main() -> None:
    init_state()
    settings, status, show_sources = sidebar()

    st.title("🎓 Major Handbook Chatbot")
    st.caption(f"Local RAG · {settings.llm_model} + {settings.embed_model} via Ollama · ChromaDB")

    if not status["reachable"]:
        st.warning("The Ollama server is not reachable. Start it (`ollama serve`) and set `OLLAMA_BASE_URL`.")
        st.stop()
    if status["missing"]:
        st.warning("Missing model(s): " + ", ".join(f"`ollama pull {m}`" for m in status["missing"]))
        st.stop()

    try:
        with st.spinner("Loading the vector store (first run embeds all documents)..."):
            pipeline = load_pipeline(settings)
    except FileNotFoundError as exc:
        st.error(str(exc))
        st.stop()

    actions_slot = knowledge_base_panel(pipeline)

    # Read the input first (it is pinned to the bottom wherever it is called) so the example
    # buttons are hidden in the same run that answers the first question.
    question = st.chat_input("Ask about the handbook...") or st.session_state.pending_question
    if not st.session_state.messages and not question:
        st.markdown("**Try one of these:**")
        cols = st.columns(len(EXAMPLE_QUESTIONS))
        for col, example in zip(cols, EXAMPLE_QUESTIONS):
            if col.button(example, use_container_width=True):
                # Rerun so the buttons disappear before the answer is drawn below them.
                st.session_state.pending_question = example
                st.rerun()

    render_history(show_sources)

    if question:
        st.session_state.pending_question = None
        answer(pipeline, question, show_sources)

    chat_actions(actions_slot)


main()
