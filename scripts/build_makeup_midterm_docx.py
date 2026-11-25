"""Build print-ready English and Turkish makeup-midterm DOCX files."""

from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parent.parent
ASSESSMENT = ROOT / "assessment"
FILES = [
    "makeup-midterm-foundations-v21.md",
    "makeup-midterm-foundations-v21-tr.md",
    "makeup-midterm-foundations-v21-answer-key.md",
    "makeup-midterm-foundations-v21-answer-key-tr.md",
]


def set_cell_shading(cell, fill: str) -> None:
    props = cell._tc.get_or_add_tcPr()
    shading = props.find(qn("w:shd"))
    if shading is None:
        shading = OxmlElement("w:shd")
        props.append(shading)
    shading.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=90, start=100, bottom=90, end=100) -> None:
    tc = cell._tc
    props = tc.get_or_add_tcPr()
    margins = props.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        props.append(margins)
    for name, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = margins.find(qn(f"w:{name}"))
        if node is None:
            node = OxmlElement(f"w:{name}")
            margins.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row) -> None:
    tr_props = row._tr.get_or_add_trPr()
    repeat = OxmlElement("w:tblHeader")
    repeat.set(qn("w:val"), "true")
    tr_props.append(repeat)


def add_inline(paragraph, text: str, *, bold=False) -> None:
    parts = re.split(r"(`[^`]+`|\*\*[^*]+\*\*)", text)
    for part in parts:
        if part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(9.3)
        elif part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        else:
            run = paragraph.add_run(part)
            run.bold = bold


def configure(doc: Document, is_key: bool, is_turkish: bool) -> None:
    section = doc.sections[0]
    section.top_margin = Cm(1.7)
    section.bottom_margin = Cm(1.6)
    section.left_margin = Cm(1.9)
    section.right_margin = Cm(1.9)

    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10.5 if not is_key else 9.5)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.08

    for style_name, size, before, after in [
        ("Title", 19, 0, 7), ("Heading 1", 15, 12, 6),
        ("Heading 2", 12.5, 10, 5), ("Heading 3", 10.8, 8, 3),
    ]:
        style = doc.styles[style_name]
        style.font.name = "Arial"
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.font.size = Pt(size)
        style.font.bold = True
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True
    title_props = doc.styles["Title"]._element.get_or_add_pPr()
    borders = title_props.find(qn("w:pBdr"))
    if borders is not None:
        title_props.remove(borders)

    header = section.header.paragraphs[0]
    if is_turkish:
        header.text = "VİZE MAZERET SINAVI" if not is_key else "CEVAP ANAHTARI"
    else:
        header.text = "MAKEUP MIDTERM" if not is_key else "INSTRUCTOR ANSWER KEY"
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header.runs[0].font.name = "Arial"
    header.runs[0].font.size = Pt(8)
    header.runs[0].font.color.rgb = RGBColor(85, 85, 85)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run("Dr. Mahyar Teymournezhad  |  Web Programming")
    run.font.name = "Arial"
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(85, 85, 85)


def parse_table(lines: list[str], start: int, doc: Document) -> int:
    raw = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        raw.append(lines[index].strip())
        index += 1
    rows = []
    for line_no, line in enumerate(raw):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if line_no == 1 and all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append(cells)
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    table.autofit = True
    if len(rows[0]) == 3 and rows[0][0] in {"Q", "Soru"}:
        widths = [Cm(1.2), Cm(1.3), Cm(13.5)]
        table.autofit = False
    elif len(rows[0]) == 3:
        widths = [Cm(10), Cm(3), Cm(3)]
        table.autofit = False
    elif len(rows[0]) >= 8:
        widths = [Cm(2.0)] * len(rows[0])
    else:
        widths = None
    for r_index, values in enumerate(rows):
        row_props = table.rows[r_index]._tr.get_or_add_trPr()
        cant_split = OxmlElement("w:cantSplit")
        row_props.append(cant_split)
        for c_index, value in enumerate(values):
            cell = table.cell(r_index, c_index)
            if widths:
                cell.width = widths[c_index]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if r_index == 0:
                set_cell_shading(cell, "17365D")
            paragraph = cell.paragraphs[0]
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_index < 2 or len(values) > 3 else WD_ALIGN_PARAGRAPH.LEFT
            add_inline(paragraph, value, bold=r_index == 0)
            for run in paragraph.runs:
                run.font.color.rgb = RGBColor(255, 255, 255) if r_index == 0 else RGBColor(0, 0, 0)
                run.font.size = Pt(8.3 if len(values) <= 3 else 8.8)
        if r_index == 0:
            set_repeat_table_header(table.rows[0])
    doc.add_paragraph().paragraph_format.space_after = Pt(1)
    return index


def build(source: Path) -> Path:
    is_key = "answer-key" in source.stem
    is_turkish = source.stem.endswith("-tr")
    doc = Document()
    configure(doc, is_key, is_turkish)
    lines = source.read_text(encoding="utf-8").splitlines()
    index = 0
    first_heading = True
    in_code = False
    inside_numbered_question = False
    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()
        if not stripped or stripped == "---":
            index += 1
            continue
        if stripped.startswith("|"):
            index = parse_table(lines, index, doc)
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            index += 1
            continue
        if in_code:
            p = doc.add_paragraph()
            r = p.add_run(line)
            r.font.name = "Consolas"
            r.font.size = Pt(9)
            index += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if heading:
            level = len(heading.group(1))
            text = heading.group(2)
            if text in {"Answer Sheet", "Cevap Kâğıdı", "Instructor notes", "Öğretim elemanı notları"}:
                doc.add_page_break()
            if level == 1 and first_heading:
                p = doc.add_paragraph(style="Title")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_inline(p, text)
                first_heading = False
            else:
                p = doc.add_heading(text, level=min(level, 3))
                if re.fullmatch(r"\d+\.", text):
                    inside_numbered_question = True
                    p.paragraph_format.space_before = Pt(8)
                    p.paragraph_format.space_after = Pt(3)
                    p.paragraph_format.keep_with_next = True
            index += 1
            continue
        bullet = re.match(r"^-\s+(.*)$", stripped)
        if bullet:
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, bullet.group(1))
            index += 1
            continue
        option = re.match(r"^[A-E]\.\s+", stripped)
        p = doc.add_paragraph()
        add_inline(p, stripped)
        if option:
            p.paragraph_format.left_indent = Cm(0.45)
            p.paragraph_format.first_line_indent = Cm(-0.35)
            p.paragraph_format.space_after = Pt(1.3)
            p.paragraph_format.keep_together = True
            p.paragraph_format.keep_with_next = not stripped.startswith("E. ")
            if stripped.startswith("E. "):
                inside_numbered_question = False
        elif stripped.startswith("**"):
            p.paragraph_format.space_after = Pt(2)
        else:
            p.paragraph_format.keep_together = True
            if inside_numbered_question:
                p.paragraph_format.keep_with_next = True
        index += 1

    output = source.with_suffix(".docx")
    doc.core_properties.title = source.stem.replace("-", " ").title()
    doc.core_properties.author = "Dr. Mahyar Teymournezhad"
    doc.save(output)
    return output


if __name__ == "__main__":
    for name in FILES:
        output = build(ASSESSMENT / name)
        print(output)
