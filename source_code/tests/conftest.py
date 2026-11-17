import shutil
import sys
from pathlib import Path

import pytest
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_core.language_models.fake_chat_models import FakeListChatModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.config import SOURCE_ROOT, get_settings  # noqa: E402

HANDBOOK_DIR = SOURCE_ROOT / "data" / "docs"


@pytest.fixture
def settings(tmp_path):
    """Settings indexing only the CS handbook into a temporary vector store; no Ollama needed."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    shutil.copy(HANDBOOK_DIR / "CS_MajorHandbook.pdf", data_dir)
    return get_settings(
        data_dir=data_dir,
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
