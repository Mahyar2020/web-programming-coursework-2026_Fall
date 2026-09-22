# Building the PDF Edition

The PDF edition is generated from the Markdown chapters and tested source files.
Do not edit the PDF directly.

## Requirements

- Python 3.11 or later
- The packages pinned in `requirements-pdf.txt`
- DejaVu Sans, DejaVu Serif, and DejaVu Sans Mono fonts
- Poppler (`pdftoppm` and `pdfinfo`) for visual quality assurance

Install the Python dependencies in a virtual environment:

```powershell
python -m pip install -r requirements-pdf.txt
```

The builder searches common Windows, TeX Live, Linux, and macOS font locations.
Set `COURSE_BOOK_FONT_DIR` to a directory containing the DejaVu TTF files when
they are installed elsewhere.

## Build and verify

```powershell
npm run pdf
npm run pdf:verify
```

The final artifact is written to:

```text
output/pdf/web-programming-from-platform-to-production-foundations-edition-revised-v13.pdf
```

Intermediate rendered pages used for visual review belong in `tmp/pdfs/` and are
ignored by Git.

## Publication workflow

1. Update Markdown chapters and tested code assets.
2. Run `npm test`.
3. Run `npm run pdf` and `npm run pdf:verify`.
4. Render every PDF page with Poppler.
5. Inspect all rendered pages for overflow, collisions, broken glyphs, table
   readability, headers, footers, and section transitions.
6. Correct the source or builder and repeat until no defects remain.

The PDF builder appends every tested laboratory solution automatically so printed
code cannot drift from repository code.
