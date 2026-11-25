# Publication Workflow

Replace bracketed placeholders after choosing the book's source and PDF toolchain.
Do not edit generated PDFs directly.

## Environment

- Required runtime and version: [RUNTIME]
- Required packages: [DEPENDENCY FILE OR INSTALL COMMAND]
- Required fonts: [FONTS]
- PDF renderer or inspection tools: [TOOLS]

## Commands

Run commands from the repository root.

```powershell
[TEST COMMAND]
[PDF BUILD COMMAND]
[PDF VERIFICATION COMMAND]
```

The current release PDF must be written to the path declared in
`BOOK_PROFILE.md`. Temporary page renderings belong outside the release directory.

## Release sequence

1. Confirm title, author, edition, date, rights text, and table of contents.
2. Test executable examples, links, references, captions, and required assets.
3. Build the PDF from editable sources.
4. Verify metadata, page count, fonts, links, and embedded images when supported.
5. Render every PDF page to an image.
6. Inspect every page for overflow, clipping, collisions, weak contrast, broken
   glyphs, unreadable tables, poor page breaks, caption errors, and malformed
   connectors or arrowheads.
7. Correct source files or the generator and repeat the build and review.
8. Report the exact delivered PDF path, completed checks, and known limitations.

A successful build command is necessary but does not establish publication
quality. Release readiness requires structural checks and complete visual review.
