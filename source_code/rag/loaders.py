"""Document loaders: turn files on disk into LangChain `Document` objects.

Task 1 (PDF support): PDFs are read page by page with `pypdf`. Each page becomes
one Document whose metadata records the source file and the 1-based page
number, so answers can cite "CS_MajorHandbook.pdf p.7".
"""

from __future__ import annotations

import logging
import re
import unicodedata
from pathlib import Path
from typing import Callable, Dict, Iterable, List

from langchain_core.documents import Document
from pypdf import PdfReader

logger = logging.getLogger(__name__)


def clean_text(text: str) -> str:
    """Normalise text extracted from PDFs/TXT.

    - NFKC folds typographic ligatures ("ﬁ" -> "fi", "ﬀ" -> "ff").
    - Re-joins words hyphenated across line breaks ("meta -\\nprogramming").
    - Collapses runs of spaces and blank lines.
    - Drops dot leaders from tables of contents ("Mission ....... 2").
    """
    text = unicodedata.normalize("NFKC", text)
    text = text.replace(" ", " ")
    text = re.sub(r"(\w) ?-\n(\w)", r"\1\2", text)
    text = re.sub(r"\.{4,}", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_txt(path: Path) -> List[Document]:
    content = clean_text(path.read_text(encoding="utf-8", errors="ignore"))
    if not content:
        return []
    return [Document(page_content=content, metadata={"source": path.name, "file_type": "txt"})]


def load_pdf(path: Path) -> List[Document]:
    """Extract selectable text from every page of a PDF.

    Pages with no extractable text (scanned pages, images, diagrams) are
    skipped with a warning; they would need OCR to be searchable.
    """
    reader = PdfReader(str(path))
    documents: List[Document] = []
    empty_pages = []
    for index, page in enumerate(reader.pages, start=1):
        text = clean_text(page.extract_text() or "")
        if len(text) < 20:
            empty_pages.append(index)
            continue
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": path.name,
                    "file_type": "pdf",
                    "page": index,
                    "total_pages": len(reader.pages),
                },
            )
        )
    if empty_pages:
        logger.warning("%s: no extractable text on page(s) %s (image-only? needs OCR)", path.name, empty_pages)
    return documents


LOADERS: Dict[str, Callable[[Path], List[Document]]] = {
    ".txt": load_txt,
    ".md": load_txt,
    ".pdf": load_pdf,
}

SUPPORTED_EXTENSIONS = tuple(LOADERS)


def find_files(directory: Path) -> List[Path]:
    """All supported files under `directory` (recursive, sorted, hidden/temp files ignored)."""
    if not directory.exists():
        return []
    return sorted(
        p
        for p in directory.rglob("*")
        if p.is_file() and p.suffix.lower() in LOADERS and not p.name.startswith((".", "~$"))
    )


def load_file(path: Path) -> List[Document]:
    loader = LOADERS.get(path.suffix.lower())
    if loader is None:
        raise ValueError(f"Unsupported file type: {path.suffix} (supported: {', '.join(SUPPORTED_EXTENSIONS)})")
    return loader(path)


def load_documents(paths: Iterable[Path]) -> List[Document]:
    documents: List[Document] = []
    for path in paths:
        try:
            docs = load_file(path)
        except Exception as exc:  # a single broken file should not stop indexing
            logger.error("Failed to load %s: %s", path, exc)
            continue
        logger.info("Loaded %s (%d section(s))", path.name, len(docs))
        documents.extend(docs)
    return documents
