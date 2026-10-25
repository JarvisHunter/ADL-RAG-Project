import sys
from pathlib import Path

import pytest
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_core.language_models.fake_chat_models import FakeListChatModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.config import SOURCE_ROOT, get_settings  # noqa: E402

HANDBOOK_DIR = SOURCE_ROOT / "data" / "handbook"


@pytest.fixture
def settings(tmp_path):
    """Settings pointing at a temporary vector store; no Ollama needed."""
    return get_settings(
        data_dir=HANDBOOK_DIR,
        vector_store_dir=tmp_path / "vector_store",
        collection="test",
        score_threshold=-1.0,  # fake embeddings are random, keep every hit
    )


@pytest.fixture
def embeddings():
    return DeterministicFakeEmbedding(size=64)


@pytest.fixture
def llm():
    return FakeListChatModel(responses=["The major requires 56 credits [CS_MajorHandbook.pdf p.7]."])
