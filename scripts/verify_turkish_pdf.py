"""Verify the source-driven Turkish Chapter 5 publication assembly."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "output" / "pdf" / "web-programming-from-platform-to-production-foundations-edition-revised-v21-tr.pdf"
LEGACY_BASE_PAGES = 214


def flatten_outline(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten_outline(item)
        else:
            yield item


def verify() -> None:
    if not PDF.exists():
        raise FileNotFoundError(PDF)
    reader = PdfReader(str(PDF))
    if len(reader.pages) <= LEGACY_BASE_PAGES + 20:
        raise AssertionError(f"Turkish PDF is unexpectedly short: {len(reader.pages)} pages")

    page_width = float(reader.pages[0].mediabox.width)
    page_height = float(reader.pages[0].mediabox.height)
    if not (594 < page_width < 596 and 841 < page_height < 843):
        raise AssertionError(f"Expected A4 pages, got {page_width} x {page_height}")

    chapter_text = "\n".join((page.extract_text() or "") for page in reader.pages[LEGACY_BASE_PAGES:])
    required = [
        "Oturum 5 - Belge Nesne Modeli, Olaylar ve Formlar",
        "MutationObserver",
        "Shadow DOM",
        "multipart/form-data",
        "Yanıt 40",
        "Şekil 5.11",
        "Tablo 5.6",
    ]
    missing = [value for value in required if value not in chapter_text]
    if missing:
        raise AssertionError(f"Turkish Chapter 5 evidence missing: {missing}")

    outline_titles = [getattr(item, "title", str(item)) for item in flatten_outline(reader.outline)]
    chapter_outlines = [title for title in outline_titles if "Oturum 5" in title]
    if len(chapter_outlines) != 1:
        raise AssertionError(f"Expected one Turkish Chapter 5 bookmark, found {len(chapter_outlines)}")

    annotations = sum(len(page.get("/Annots", [])) for page in reader.pages)
    if annotations < 1:
        raise AssertionError("Expected hyperlinks in the Turkish PDF")

    print(
        f"Turkish PDF verification passed: {len(reader.pages)} A4 pages; "
        f"hyperlink annotations {annotations}; file size {PDF.stat().st_size:,} bytes"
    )


if __name__ == "__main__":
    verify()
