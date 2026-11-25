"""Combine page-contact sheets into overview images for whole-book QA."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def build(source: Path, destination: Path) -> None:
    sheets = sorted(source.glob("sheet-*.jpg"))
    if not sheets:
        raise FileNotFoundError(source)
    destination.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(sheets), 4):
        canvas = Image.new("RGB", (1200, 1800), "white")
        draw = ImageDraw.Draw(canvas)
        for index, sheet_path in enumerate(sheets[start : start + 4]):
            with Image.open(sheet_path) as opened:
                sheet = opened.convert("RGB")
            sheet.thumbnail((580, 850))
            x = 10 + (index % 2) * 600
            y = 35 + (index // 2) * 880
            canvas.paste(sheet, (x, y))
            draw.text((x, 10 + (index // 2) * 880), sheet_path.stem, fill=(25, 35, 55))
        canvas.save(destination / f"overview-{start // 4 + 1:02}.jpg", quality=90)
    print(f"Created {len(list(destination.glob('overview-*.jpg')))} overview images")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    build(args.source, args.destination)
