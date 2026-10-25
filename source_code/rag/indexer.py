"""Indexing: load documents, split them into chunks, embed and store in Chroma.

A small `manifest.json` is saved next to the vector store. It records which
files (and which chunking / embedding settings) produced the index, so the
index is rebuilt automatically when documents or settings change instead of
silently serving stale vectors.
"""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import Settings
from .loaders import find_files, load_documents

logger = logging.getLogger(__name__)

MANIFEST_NAME = "manifest.json"
BATCH_SIZE = 64


def file_fingerprint(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def split_documents(documents: List[Document], settings: Settings) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
        add_start_index=True,
    )
    chunks = splitter.split_documents(documents)
    for chunk in chunks:
        meta = chunk.metadata
        key = f"{meta.get('source')}|{meta.get('page', 0)}|{meta.get('start_index', 0)}"
        meta["chunk_id"] = hashlib.md5(key.encode("utf-8")).hexdigest()
    return chunks


class VectorIndex:
    """Thin wrapper around a persistent Chroma collection."""

    def __init__(self, settings: Settings, embeddings: Embeddings):
        self.settings = settings
        self.embeddings = embeddings
        self.settings.vector_store_dir.mkdir(parents=True, exist_ok=True)
        self.store = self._open_store()

    # ------------------------------------------------------------------ store
    def _open_store(self) -> Chroma:
        return Chroma(
            collection_name=self.settings.collection,
            embedding_function=self.embeddings,
            persist_directory=str(self.settings.vector_store_dir),
            # Cosine distance makes `1 - distance` a similarity in [0, 1].
            collection_metadata={"hnsw:space": "cosine"},
        )

    def count(self) -> int:
        return self.store._collection.count()

    def reset(self) -> None:
        self.store.delete_collection()
        self.store = self._open_store()
        self.manifest_path.unlink(missing_ok=True)

    # --------------------------------------------------------------- manifest
    @property
    def manifest_path(self) -> Path:
        return self.settings.vector_store_dir / MANIFEST_NAME

    def _settings_signature(self) -> Dict[str, object]:
        return {
            "embed_model": self.settings.embed_model,
            "chunk_size": self.settings.chunk_size,
            "chunk_overlap": self.settings.chunk_overlap,
        }

    def load_manifest(self) -> Dict[str, object]:
        if not self.manifest_path.exists():
            return {}
        return json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def _save_manifest(self, files: Dict[str, str]) -> None:
        manifest = {"settings": self._settings_signature(), "files": files}
        self.manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    def indexed_files(self) -> List[str]:
        return sorted(self.load_manifest().get("files", {}))

    def is_up_to_date(self, files: Dict[str, str]) -> bool:
        manifest = self.load_manifest()
        return (
            self.count() > 0
            and manifest.get("settings") == self._settings_signature()
            and manifest.get("files") == files
        )

    # --------------------------------------------------------------- indexing
    def _add_chunks(self, chunks: List[Document]) -> None:
        for start in range(0, len(chunks), BATCH_SIZE):
            batch = chunks[start : start + BATCH_SIZE]
            self.store.add_documents(batch, ids=[c.metadata["chunk_id"] for c in batch])
            logger.info("Embedded %d/%d chunks", min(start + BATCH_SIZE, len(chunks)), len(chunks))

    def build(self, data_dir: Optional[Path] = None, force: bool = False) -> Dict[str, int]:
        """(Re)build the index from every supported file in `data_dir`.

        Skips work when the manifest shows nothing changed, unless `force`.
        """
        data_dir = data_dir or self.settings.data_dir
        paths = find_files(data_dir)
        if not paths:
            raise FileNotFoundError(f"No .pdf/.txt/.md files found in {data_dir}")

        fingerprints = {str(p.relative_to(data_dir)): file_fingerprint(p) for p in paths}
        if not force and self.is_up_to_date(fingerprints):
            logger.info("Vector store is up to date (%d chunks)", self.count())
            return {"files": len(paths), "chunks": self.count(), "rebuilt": 0}

        logger.info("Indexing %d file(s) from %s", len(paths), data_dir)
        self.reset()
        documents = load_documents(paths)
        chunks = split_documents(documents, self.settings)
        self._add_chunks(chunks)
        self._save_manifest(fingerprints)
        return {"files": len(paths), "chunks": len(chunks), "rebuilt": 1}

    def add_files(self, paths: Iterable[Path], data_dir: Optional[Path] = None) -> int:
        """Incrementally index extra files (e.g. uploaded from the web UI)."""
        data_dir = data_dir or self.settings.data_dir
        paths = list(paths)
        chunks = split_documents(load_documents(paths), self.settings)
        if chunks:
            # Remove stale chunks of the same files before re-adding them.
            for name in {c.metadata["source"] for c in chunks}:
                self.store._collection.delete(where={"source": name})
            self._add_chunks(chunks)
        files = dict(self.load_manifest().get("files", {}))
        for path in paths:
            try:
                key = str(path.relative_to(data_dir))
            except ValueError:
                key = path.name
            files[key] = file_fingerprint(path)
        self._save_manifest(files)
        return len(chunks)
