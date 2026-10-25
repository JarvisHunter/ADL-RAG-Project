import shutil

from rag.indexer import VectorIndex, split_documents
from rag.loaders import load_pdf

from .conftest import HANDBOOK_DIR


def test_split_keeps_page_metadata(settings):
    chunks = split_documents(load_pdf(HANDBOOK_DIR / "CS_MajorHandbook.pdf"), settings)
    assert all(len(c.page_content) <= settings.chunk_size for c in chunks)
    assert all("page" in c.metadata and "chunk_id" in c.metadata for c in chunks)
    assert len({c.metadata["chunk_id"] for c in chunks}) == len(chunks)


def test_build_is_cached_until_documents_change(settings, embeddings, tmp_path):
    data_dir = tmp_path / "docs"
    data_dir.mkdir()
    shutil.copy(HANDBOOK_DIR / "CS_MajorHandbook.pdf", data_dir)
    settings = settings.with_overrides(data_dir=data_dir)

    index = VectorIndex(settings, embeddings)
    first = index.build()
    assert first["rebuilt"] == 1 and first["chunks"] == index.count() > 0

    assert index.build()["rebuilt"] == 0  # unchanged -> reused

    (data_dir / "extra.txt").write_text("The CS club meets every Friday.", encoding="utf-8")
    third = index.build()
    assert third["rebuilt"] == 1 and third["files"] == 2
    assert index.indexed_files() == ["CS_MajorHandbook.pdf", "extra.txt"]


def test_add_files_is_incremental(settings, embeddings, tmp_path):
    index = VectorIndex(settings, embeddings)
    index.build()
    before = index.count()
    extra = tmp_path / "extra.txt"
    extra.write_text("Office hours are on Tuesdays.", encoding="utf-8")
    added = index.add_files([extra])
    assert added == 1 and index.count() == before + 1
    index.add_files([extra])  # re-adding replaces instead of duplicating
    assert index.count() == before + 1
