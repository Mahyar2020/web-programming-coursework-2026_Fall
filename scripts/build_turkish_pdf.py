"""Append the source-driven Turkish Chapter 5 to the translated checkpoint PDF.

The first 214 Turkish pages predate the editable translation-source workflow.
They remain the legacy base. This builder renders the new chapter from Markdown,
adds a linked continuation of the contents, and assembles a stable Turkish PDF.
"""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import AnchorFlowable, Frame, PageBreak, PageTemplate, Paragraph, Spacer

import build_pdf as book


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output" / "pdf" / "web-programming-from-platform-to-production-foundations-edition-revised-v21-tr.pdf"
CHAPTER = ROOT / "translations" / "tr" / "chapter-05-dom-events-and-forms.md"
TEMP_DIR = ROOT / "tmp" / "pdfs"
CHAPTER_PDF = TEMP_DIR / "chapter-05-tr-source-build.pdf"
ASSEMBLED = TEMP_DIR / "web-programming-v21-tr-assembled.pdf"
LEGACY_BASE_PAGES = 214


def draw_turkish_body_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setStrokeColor(book.RULE)
    canvas.setLineWidth(0.5)
    canvas.line(book.LEFT_MARGIN, A4[1] - 15 * mm, A4[0] - book.RIGHT_MARGIN, A4[1] - 15 * mm)
    canvas.line(book.LEFT_MARGIN, 14 * mm, A4[0] - book.RIGHT_MARGIN, 14 * mm)
    canvas.setFillColor(book.MUTED)
    canvas.setFont("BookSans", 6.8)
    canvas.drawString(book.LEFT_MARGIN, A4[1] - 11.5 * mm, "WEB PROGRAMLAMA - PLATFORMDAN ÜRETİME")
    canvas.drawRightString(A4[0] - book.RIGHT_MARGIN, A4[1] - 11.5 * mm, "TEMELLER BASKISI")
    canvas.drawString(book.LEFT_MARGIN, 9.5 * mm, "Bilgisayar Mühendisliği Programı")
    canvas.drawRightString(A4[0] - book.RIGHT_MARGIN, 9.5 * mm, str(LEGACY_BASE_PAGES + doc.page))
    canvas.restoreState()


def continuation_page(styles) -> list:
    return [
        Paragraph("İçindekiler - devam", styles["h1"]),
        Spacer(1, 7 * mm),
        Paragraph(
            '<a href="#chapter5-tr"><b>Oturum 5 - Belge Nesne Modeli, Olaylar ve Formlar</b></a>'
            ' ........................................................................ 216',
            styles["body"],
        ),
        Spacer(1, 4 * mm),
        Paragraph(
            "Canlı DOM ağacı; güvenli seçim ve değişiklik; uygulama durumu ve çizim; "
            "olay yayılması ve devri; form verisi ve erişilebilir doğrulama; performans "
            "ölçümü; MutationObserver; shadow DOM; özel öğeler; laboratuvar; alıştırmalar, "
            "gerekçeli yanıtlar ve kısa sınav.",
            styles["body"],
        ),
        Spacer(1, 8 * mm),
        Paragraph(
            "Bu sayfa, kaynak tabanlı Türkçe yayın iş akışına eklenen yeni bölüm için "
            "içindekiler devamıdır. Yukarıdaki bölüm başlığı PDF içinde tıklanabilir.",
            styles["small"],
        ),
        PageBreak(),
        AnchorFlowable("chapter5-tr"),
    ]


def build_chapter_pdf() -> Path:
    if not CHAPTER.exists():
        raise FileNotFoundError(f"Turkish Chapter 5 source not found: {CHAPTER}")
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    book.register_fonts()
    styles = book.make_styles()
    frame = Frame(
        book.LEFT_MARGIN,
        book.BOTTOM_MARGIN,
        book.CONTENT_WIDTH,
        book.PAGE_HEIGHT - book.TOP_MARGIN - book.BOTTOM_MARGIN,
        id="turkish-body-frame",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc = book.BookDocTemplate(
        CHAPTER_PDF,
        pagesize=A4,
        leftMargin=book.LEFT_MARGIN,
        rightMargin=book.RIGHT_MARGIN,
        topMargin=book.TOP_MARGIN,
        bottomMargin=book.BOTTOM_MARGIN,
        title="Web Programlama: Platformdan Üretime - Gözden Geçirilmiş Temeller Baskısı",
        author=book.AUTHOR,
        subject="Üniversite web programlama ders kitabı - Türkçe kaynak tabanlı bölüm",
        creator="Reproducible ReportLab Turkish chapter build pipeline",
    )
    doc.addPageTemplates([PageTemplate(id="body", frames=[frame], onPage=draw_turkish_body_page)])
    story = continuation_page(styles)
    story.extend(book.markdown_to_flowables(CHAPTER.read_text(encoding="utf-8"), styles, language="tr"))
    doc.multiBuild(story)
    return CHAPTER_PDF


def assemble() -> Path:
    chapter_pdf = build_chapter_pdf()
    base = PdfReader(str(OUTPUT))
    if len(base.pages) < LEGACY_BASE_PAGES:
        raise ValueError(f"Turkish base has {len(base.pages)} pages; expected at least {LEGACY_BASE_PAGES}.")

    writer = PdfWriter()
    writer.append(base, pages=(0, LEGACY_BASE_PAGES), import_outline=True)
    writer.append(PdfReader(str(chapter_pdf)), import_outline=True)
    writer.add_metadata(
        {
            "/Title": "Web Programlama: Platformdan Üretime - Gözden Geçirilmiş Temeller Baskısı",
            "/Author": book.AUTHOR,
            "/Subject": "Üniversite web programlama ders kitabı - Türkçe baskı",
            "/Creator": "Reproducible ReportLab Turkish assembly pipeline",
        }
    )
    with ASSEMBLED.open("wb") as stream:
        writer.write(stream)
    ASSEMBLED.replace(OUTPUT)
    return OUTPUT


if __name__ == "__main__":
    result = assemble()
    print(f"Created {result}")
