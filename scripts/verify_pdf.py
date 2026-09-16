"""Verify the generated course-book PDF structurally and textually."""

from __future__ import annotations

from pathlib import Path

import pdfplumber
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "output" / "pdf" / "web-programming-from-platform-to-production-foundations-edition-revised-v10.pdf"


def main() -> None:
    if not PDF.exists():
        raise SystemExit(f"PDF does not exist: {PDF}")

    reader = PdfReader(PDF)
    failures: list[str] = []
    metadata = reader.metadata or {}
    title = metadata.get("/Title", "")
    author = metadata.get("/Author", "")
    if "Web Programming" not in title or "Revised Foundations Edition" not in title:
        failures.append("PDF title metadata is missing or incorrect")
    if author != "Dr. Mahyar Teymournezhad":
        failures.append("PDF author metadata is missing or incorrect")
    if len(reader.pages) < 30:
        failures.append(f"unexpectedly short PDF: {len(reader.pages)} pages")

    expected_width = 595.28
    expected_height = 841.89
    for number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - expected_width) > 1 or abs(height - expected_height) > 1:
            failures.append(f"page {number} is not A4: {width:.1f} x {height:.1f} points")

    with pdfplumber.open(PDF) as document:
        page_text = [(page.extract_text() or "").strip() for page in document.pages]
    combined = "\n".join(page_text)
    required_text = [
        "How the Web Works",
        "Prepare Your Web-Programming Workstation",
        "Table 0.6 - Student workstation readiness record",
        "Preface",
        "About the author",
        "Internet Protocol version 6",
        "Reading 2001:db8::40 as an IPv6 address",
        "Exercise 13 - Expand, compress, and interpret IPv6",
        "Table 1.4 - Common DNS resource record types",
        "Table 2.7 - Session 2 glossary",
        "Table 3.8 - Session 3 glossary",
        "Figure 0.2. The course workstation keeps editing",
        "Figure 0.3. npm searches for package.json",
        "Figure 0.4. JavaScript runs in browsers and Node.js",
        "Figure 0.5. A repository-first workflow",
        "Figure 0.6. The server and command terminals",
        "Figure 0.8. Network records requests",
        "Figure 0.9. The ENOENT path",
        "Figure 1.3. Client and server are roles within an exchange",
        "Figure 1.7. A page navigation coordinates naming",
        "Figure 1.14. Local development keeps the browser and development server",
        "Figure 2.1. An HTML element combines tags",
        "Figure 2.5. The browser output of the complete semantic form example",
        "Figure 2.7. Accessibility judgments combine automated",
        "Figure 3.1. A CSS rule connects a selector",
        "Figure 3.5. Logical inline and block axes",
        "Figure 3.10. At a narrow viewport",
        "Figure 3.11. One component can adapt",
        "Figure 3.12. CSS debugging traces evidence",
        "What DNS actually is",
        "The smallest useful HTML document",
        "Semantic HTML and Accessible Forms",
        "Cascading Style Sheets, Layout, and Responsive Design",
        "Guided laboratory",
        "Worked answers",
        "Retrieval quiz",
        "Answer 12",
        "Answer 14",
        "Answer 16",
        "Answer 10",
        "Dr. Mahyar Teymournezhad",
        "JavaScript is the course's primary programming language",
        "One language, two environments",
        "Appendix A - Tested laboratory reference solutions",
        "Appendix B - Quick commands",
    ]
    for text in required_text:
        if text not in combined:
            failures.append(f"required text not found: {text}")
    if "\ufffd" in combined:
        failures.append("replacement glyph found in extracted text")
    if "Text alternative:" in combined:
        failures.append("misleading visible Text alternative label found")
    if "Figure 0.1" in combined:
        failures.append("the author's photograph must not have a numbered caption")

    for number, text in enumerate(page_text[1:], start=2):
        if len(text) < 20:
            failures.append(f"page {number} appears blank or nearly blank")

    link_annotations = 0
    for page in reader.pages:
        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") == "/Link":
                link_annotations += 1
    if link_annotations < 5:
        failures.append(f"too few hyperlink annotations: {link_annotations}")

    if failures:
        print("PDF verification failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print(f"PDF verification passed: {len(reader.pages)} A4 pages")
    print(f"Hyperlink annotations: {link_annotations}")
    print(f"File size: {PDF.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
