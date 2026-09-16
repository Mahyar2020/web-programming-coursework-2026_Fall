# University Book Project Instructions

## Project identity

Read `BOOK_PROFILE.md` before making content or design decisions. Use the personal
`$university-book-authoring` skill for textbook writing, chapter review,
laboratories, assessments, educational visuals, and publication work.

## Sources of truth

- `BOOK_PROFILE.md` defines the audience, author, scope, technical choices, and
  publication identity.
- `docs/EDITORIAL_STYLE.md` defines the teaching and visual language.
- `docs/PUBLICATION_WORKFLOW.md` defines builds, verification, and release output.
- Editable source files and tested examples are authoritative. Generated PDFs
  must not be edited directly.

## Chapter requirements

For each substantial chapter, provide the elements that serve its learning
outcomes: motivation, prerequisites, beginner-accessible narrative, verified
examples, instructional visuals and tables, guided practice, exercises, complete
worked answers, quiz explanations, summary, glossary, annotated sources, and
instructor guidance when it is in scope.

Explain new concepts from observable details toward terminology, mechanism, and
the whole system. Expand abbreviations on first meaningful use in each chapter.
Do not assume that beginners recognize tools, interfaces, commands, directories,
or expected output without guidance.

## Figures, tables, and output

- Number figures and tables independently within each chapter, beginning at 1.
- Use numeric captions only; do not add alphabetic suffixes.
- Mention each figure and table by number in the prose and explain what to notice.
- Label significant components and paths inside instructional diagrams.
- Keep all labels, boxes, connectors, and arrowheads inside the visual boundary.
- Use authentic output captures for executable examples; generated illustrations
  must not be presented as proof that code ran.

## Verification and change discipline

Run the commands documented in `docs/PUBLICATION_WORKFLOW.md`. For a release,
test examples, build the PDF, run structural checks, render every page, and inspect
the complete result visually. Fix source defects and repeat verification.

Preserve existing user changes. Do not change the book's author, audience,
language, framework, course sequence, visual identity, or assessment policy
without explicit direction. Research current authoritative sources for
update-sensitive claims.
