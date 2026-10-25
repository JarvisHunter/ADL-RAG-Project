"""Central configuration for the RAG system.

Every setting has a sensible default and can be overridden with an environment
variable (or a `.env` file in `source_code/`). This keeps the same code usable
locally, inside Docker, and in evaluation scripts.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, replace
from pathlib import Path

from dotenv import load_dotenv

# Root of the source code (the folder that contains `rag/`, `app.py`, ...).
SOURCE_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(SOURCE_ROOT / ".env")


def _env(name: str, default: str) -> str:
    return os.getenv(name, default)


def _env_int(name: str, default: int) -> int:
    return int(os.getenv(name, default))


def _env_float(name: str, default: float) -> float:
    return float(os.getenv(name, default))


def _env_bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def _env_path(name: str, default: Path) -> Path:
    value = Path(os.getenv(name, str(default)))
    return value if value.is_absolute() else (SOURCE_ROOT / value).resolve()


@dataclass(frozen=True)
class Settings:
    # Documents & vector store
    data_dir: Path = field(default_factory=lambda: _env_path("RAG_DATA_DIR", SOURCE_ROOT / "data" / "handbook"))
    vector_store_dir: Path = field(default_factory=lambda: _env_path("RAG_VECTOR_STORE_DIR", SOURCE_ROOT / "vector_store"))
    collection: str = field(default_factory=lambda: _env("RAG_COLLECTION", "rag_documents"))

    # Chunking
    chunk_size: int = field(default_factory=lambda: _env_int("RAG_CHUNK_SIZE", 1000))
    chunk_overlap: int = field(default_factory=lambda: _env_int("RAG_CHUNK_OVERLAP", 200))

    # Models (served by Ollama)
    ollama_base_url: str = field(default_factory=lambda: _env("OLLAMA_BASE_URL", "http://127.0.0.1:11434"))
    embed_model: str = field(default_factory=lambda: _env("RAG_EMBED_MODEL", "nomic-embed-text"))
    llm_model: str = field(default_factory=lambda: _env("RAG_LLM_MODEL", "qwen2.5:0.5b"))
    temperature: float = field(default_factory=lambda: _env_float("RAG_TEMPERATURE", 0.2))

    # Retrieval
    top_k: int = field(default_factory=lambda: _env_int("RAG_TOP_K", 5))
    # Minimum cosine similarity (0..1) of the best chunk before the context is trusted.
    score_threshold: float = field(default_factory=lambda: _env_float("RAG_SCORE_THRESHOLD", 0.3))
    # If True the model may fall back to its own knowledge when retrieval is weak
    # (baseline behaviour). If False it must say it does not know.
    allow_general_knowledge: bool = field(default_factory=lambda: _env_bool("RAG_ALLOW_GENERAL_KNOWLEDGE", False))

    # Conversation
    history_turns: int = field(default_factory=lambda: _env_int("RAG_HISTORY_TURNS", 3))

    def with_overrides(self, **overrides) -> "Settings":
        """Return a copy with some fields replaced (ignores `None` values)."""
        return replace(self, **{k: v for k, v in overrides.items() if v is not None})


def get_settings(**overrides) -> Settings:
    return Settings().with_overrides(**overrides)
