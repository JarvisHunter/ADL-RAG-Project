from pathlib import Path

from rag.loaders import clean_text, find_files, load_documents, load_pdf, load_txt

from .conftest import HANDBOOK_DIR


def test_clean_text_fixes_ligatures_and_hyphenation():
    raw = "ﬁrst  eﬀective\nmeta -\nprogramming\n\n\n\nMission ........ 2"
    cleaned = clean_text(raw)
    assert "first effective" in cleaned
    assert "metaprogramming" in cleaned
    assert "...." not in cleaned
    assert "\n\n\n" not in cleaned


def test_load_pdf_returns_one_document_per_text_page():
    docs = load_pdf(HANDBOOK_DIR / "CS_MajorHandbook.pdf")
    pages = [d.metadata["page"] for d in docs]
    assert len(docs) >= 15
    assert pages == sorted(pages)
    assert all(d.metadata["source"] == "CS_MajorHandbook.pdf" for d in docs)
    assert any("56 credits" in d.page_content for d in docs)


def test_load_txt(tmp_path: Path):
    path = tmp_path / "note.txt"
    path.write_text("Hello   world\n\n\n\nBye", encoding="utf-8")
    [doc] = load_txt(path)
    assert doc.page_content == "Hello world\n\nBye"
    assert doc.metadata == {"source": "note.txt", "file_type": "txt"}


def test_find_files_skips_hidden_and_unsupported(tmp_path: Path):
    for name in ["a.pdf", "b.txt", "c.docx", ".hidden.txt", "~$lock.pdf"]:
        (tmp_path / name).write_text("x")
    assert [p.name for p in find_files(tmp_path)] == ["a.pdf", "b.txt"]


def test_broken_file_does_not_stop_loading(tmp_path: Path):
    (tmp_path / "broken.pdf").write_text("not a pdf")
    (tmp_path / "ok.txt").write_text("some content here")
    docs = load_documents(find_files(tmp_path))
    assert [d.metadata["source"] for d in docs] == ["ok.txt"]
