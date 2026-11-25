"""Validate bilingual makeup-midterm structure and answer balance."""

from collections import Counter
from pathlib import Path
import re

from docx import Document


ROOT = Path(__file__).resolve().parent.parent
ASSESSMENT = ROOT / "assessment"
EXAMS = [
    ASSESSMENT / "makeup-midterm-foundations-v21.md",
    ASSESSMENT / "makeup-midterm-foundations-v21-tr.md",
]
KEYS = [
    ASSESSMENT / "makeup-midterm-foundations-v21-answer-key.md",
    ASSESSMENT / "makeup-midterm-foundations-v21-answer-key-tr.md",
]
EXPECTED = "C A E B D B A E C D B D A C E B C E E A D C B E C A D B B D A C E A D C E A D B".split()


def exam_blocks(text: str) -> list[str]:
    matches = list(re.finditer(r"^### (\d+)\.\s*$", text, re.MULTILINE))
    assert [int(match.group(1)) for match in matches] == list(range(1, 41))
    blocks = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else text.index("## Answer", match.end()) if "## Answer" in text[match.end():] else text.index("## Cevap", match.end())
        blocks.append(text[match.end():end])
    return blocks


for exam in EXAMS:
    text = exam.read_text(encoding="utf-8")
    blocks = exam_blocks(text)
    for number, block in enumerate(blocks, 1):
        options = re.findall(r"^[A-E]\. ", block, re.MULTILINE)
        assert len(options) == 5, f"{exam.name} question {number} has {len(options)} options"
    docx = Document(exam.with_suffix(".docx"))
    numbered = [p.text for p in docx.paragraphs if re.fullmatch(r"\d+\.", p.text.strip())]
    assert len(numbered) == 40, f"{exam.with_suffix('.docx').name} has {len(numbered)} question headings"

for key in KEYS:
    text = key.read_text(encoding="utf-8")
    found = [(int(q), answer) for q, answer in re.findall(r"^\| (\d+) \| ([A-E]) \|", text, re.MULTILINE)]
    assert [q for q, _ in found] == list(range(1, 41))
    assert [answer for _, answer in found] == EXPECTED

assert Counter(EXPECTED) == Counter({letter: 8 for letter in "ABCDE"})
print("Makeup midterm verification passed: 40 aligned questions, five options each, balanced key, four DOCX files.")
