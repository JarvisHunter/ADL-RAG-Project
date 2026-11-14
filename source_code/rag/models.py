"""Model factories.

All model construction lives here so the rest of the code never imports a
provider directly. Swapping Ollama for another backend (or for a fake model in
tests) only requires changing this module or injecting objects into
`RAGPipeline`.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Dict, List

from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel

from .config import Settings


def auth_headers(api_key: str) -> Dict[str, str]:
    """HTTP headers for a protected Ollama server (empty when no key is set)."""
    return {"Authorization": f"Bearer {api_key}"} if api_key else {}


def _client_kwargs(settings: Settings) -> dict:
    return {"headers": auth_headers(settings.api_key), "timeout": settings.request_timeout}


def get_embeddings(settings: Settings) -> Embeddings:
    from langchain_ollama import OllamaEmbeddings

    return OllamaEmbeddings(
        model=settings.embed_model,
        base_url=settings.ollama_base_url,
        client_kwargs=_client_kwargs(settings),
    )


def get_chat_model(settings: Settings) -> BaseChatModel:
    from langchain_ollama import ChatOllama

    return ChatOllama(
        model=settings.llm_model,
        base_url=settings.ollama_base_url,
        temperature=settings.temperature,
        # think=False makes reasoning models answer directly (ignored by other models).
        reasoning=settings.think,
        num_predict=settings.max_tokens,
        num_ctx=settings.num_ctx,
        client_kwargs=_client_kwargs(settings),
    )


def list_ollama_models(base_url: str, api_key: str = "", timeout: float = 3.0) -> List[str]:
    """Names of the models pulled on the Ollama server. Raises if unreachable."""
    request = urllib.request.Request(base_url.rstrip("/") + "/api/tags", headers=auth_headers(api_key))
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.load(response)
    return sorted(model["name"] for model in payload.get("models", []))


def check_ollama(settings: Settings) -> dict:
    """Health check used by the CLI and the web UI."""
    status = {"reachable": False, "models": [], "missing": [], "error": None}
    try:
        models = list_ollama_models(settings.ollama_base_url, settings.api_key)
    except (urllib.error.URLError, OSError, ValueError) as exc:
        status["error"] = f"Cannot reach Ollama at {settings.ollama_base_url}: {exc}"
        return status
    status["reachable"] = True
    status["models"] = models
    # Ollama reports "nomic-embed-text:latest" for a model pulled as "nomic-embed-text".
    available = set(models) | {m.removesuffix(":latest") for m in models}
    status["missing"] = [m for m in (settings.embed_model, settings.llm_model) if m not in available]
    return status
