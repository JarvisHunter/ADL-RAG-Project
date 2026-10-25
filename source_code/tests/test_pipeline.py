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
    assert messages[-1].content == "What are its prerequisites?"


def test_low_scores_trigger_fallback(settings, embeddings, llm):
    pipeline = make_pipeline(settings.with_overrides(score_threshold=1.01), embeddings, llm)
    response = pipeline.ask("What is the tuition fee?")
    assert response.used_fallback and response.sources == []
    system = pipeline.build_messages("q", [])[0].content
    assert "No sufficiently relevant passages" in system


def test_stream_yields_tokens(settings, embeddings, llm):
    pipeline = make_pipeline(settings, embeddings, llm)
    sources, tokens = pipeline.stream("How many credits?")
    assert sources
    assert "56" in "".join(tokens)
