"""Central configuration for the RAG system.

Every setting has a sensible default and can be overridden with an environment
variable (or a `.env` file in `source_code/`).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Root of the source code (the folder that contains `rag/`, `app.py`, ...).
SOURCE_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(SOURCE_ROOT / ".env")
# Also pick up docker/.env so local runs share the same settings (values above win).
load_dotenv(SOURCE_ROOT.parent / "docker" / ".env")


def _env(name: str, default: str) -> str:
    return os.getenv(name, default)


def _ollama_base_url() -> str:
    # The Ollama client uses the native /api routes, so drop an OpenAI-style "/v1" suffix.
    url = _env("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
    return url.removesuffix("/v1")


def _env_int(name: str, default: int) -> int:
    return int(os.getenv(name, default))


def _env_float(name: str, default: float) -> float:
    return float(os.getenv(name, default))


def _env_bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def _env_optional_float(name: str) -> Optional[float]:
    value = os.getenv(name, "").strip()
    return float(value) if value else None


def _env_path(name: str, default: Path) -> Path:
    value = Path(os.getenv(name, str(default)))
    return value if value.is_absolute() else (SOURCE_ROOT / value).resolve()

CALIBRATED_SCORE_THRESHOLDS = {"mxbai-embed-large": 0.55}
DEFAULT_SCORE_THRESHOLD = 0.3

@dataclass(frozen=True)
class Settings:
    # Documents & vector store
    data_dir: Path = field(default_factory=lambda: _env_path("RAG_DATA_DIR", SOURCE_ROOT / "data" / "docs"))
    vector_store_dir: Path = field(default_factory=lambda: _env_path("RAG_VECTOR_STORE_DIR", SOURCE_ROOT / "vector_store"))
    collection: str = field(default_factory=lambda: _env("RAG_COLLECTION", "rag_documents"))

    # Chunking
    chunk_size: int = field(default_factory=lambda: _env_int("RAG_CHUNK_SIZE", 1000))
    chunk_overlap: int = field(default_factory=lambda: _env_int("RAG_CHUNK_OVERLAP", 200))

    # Models (served by Ollama)
    ollama_base_url: str = field(default_factory=_ollama_base_url)
    # Bearer token for a protected Ollama server (empty = no auth header).
    api_key: str = field(default_factory=lambda: _env("OLLAMA_API_KEY", _env("LLM_API_KEY", "")).strip(), repr=False)
    embed_model: str = field(default_factory=lambda: _env("RAG_EMBED_MODEL", "nomic-embed-text"))
    llm_model: str = field(default_factory=lambda: _env("RAG_LLM_MODEL", "qwen2.5:0.5b"))
    temperature: float = field(default_factory=lambda: _env_float("RAG_TEMPERATURE", 0.2))
    # "Thinking" models (qwen3, qwen3.5, deepseek-r1, ...) reason before answering by default.
    # Small ones can reason for minutes and return an empty answer, so it is off unless asked for.
    think: bool = field(default_factory=lambda: _env_bool("RAG_THINK", False))
    # Upper bound on generated tokens, so one request can never run forever.
    max_tokens: int = field(default_factory=lambda: _env_int("RAG_MAX_TOKENS", 1024))
    # Context window requested from Ollama (some models default to 256k, which is slow and memory-hungry).
    num_ctx: int = field(default_factory=lambda: _env_int("RAG_NUM_CTX", 8192))
    # Seconds before an Ollama request is abandoned.
    request_timeout: float = field(default_factory=lambda: _env_float("RAG_REQUEST_TIMEOUT", 180))

    # Retrieval
    top_k: int = field(default_factory=lambda: _env_int("RAG_TOP_K", 5))
    # Minimum cosine similarity (0..1) for a chunk to be used. None = calibrated default for the
    # embedding model (see `min_score`).
    score_threshold: Optional[float] = field(default_factory=lambda: _env_optional_float("RAG_SCORE_THRESHOLD"))
    # If True the model may fall back to its own knowledge when retrieval is weak
    # (baseline behaviour). If False it must say it does not know.
    allow_general_knowledge: bool = field(default_factory=lambda: _env_bool("RAG_ALLOW_GENERAL_KNOWLEDGE", False))

    # Conversation
    history_turns: int = field(default_factory=lambda: _env_int("RAG_HISTORY_TURNS", 3))

    @property
    def min_score(self) -> float:
        """Similarity cut-off actually used: the explicit setting, else the model's calibrated value."""
        if self.score_threshold is not None:
            return self.score_threshold
        return CALIBRATED_SCORE_THRESHOLDS.get(self.embed_model.removesuffix(":latest"), DEFAULT_SCORE_THRESHOLD)

    def with_overrides(self, **overrides) -> "Settings":
        """Return a copy with some fields replaced (ignores `None` values)."""
        return replace(self, **{k: v for k, v in overrides.items() if v is not None})


def get_settings(**overrides) -> Settings:
    return Settings().with_overrides(**overrides)
