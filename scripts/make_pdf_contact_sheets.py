"""Create compact page-contact sheets from a numbered PNG render directory."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def page_number(path: Path) -> int:
    return int(path.stem.split("-")[-1])


def build(source: Path, destination: Path) -> None:
    pages = sorted(source.glob("page-*.png"), key=page_number)
    if not pages:
        raise FileNotFoundError(f"No page PNG files found in {source}")
    destination.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(pages), 16):
        sheet = Image.new("RGB", (1360, 2000), (238, 242, 246))
        draw = ImageDraw.Draw(sheet)
        for index, page_path in enumerate(pages[start : start + 16]):
            number = page_number(page_path)
            with Image.open(page_path) as opened:
                page = opened.convert("RGB")
            page.thumbnail((330, 470))
            x = (index % 4) * 340 + 5
            y = (index // 4) * 500 + 20
            sheet.paste(page, (x, y))
            draw.text((x, y - 16), f"Page {number}", fill=(25, 35, 55))
        sheet.save(destination / f"sheet-{start // 16 + 1:02}.jpg", quality=88)
    print(f"Created {len(list(destination.glob('sheet-*.jpg')))} contact sheets from {len(pages)} pages")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    arguments = parser.parse_args()
    build(arguments.source, arguments.destination)
