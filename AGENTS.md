# Web Programming Course Book Instructions

## Project identity

- Book: *Web Programming: From the Platform to Production*
- Author: Dr. Mahyar Teymournezhad
- Audience: computer engineering students and university instructors
- Entry level: assume no prior knowledge unless a chapter states otherwise
- Teaching path: web platform, JavaScript in the browser, Node.js on the server,
  PostgreSQL, React, testing, deployment, and advanced web systems
- Continuing application: Campus Hub

Use the personal `$university-book-authoring` skill for book writing, chapter
review, laboratories, assessments, educational visuals, and publication work.

## Sources of truth

Read the files relevant to the task before editing:

- `docs/BOOK_ARCHITECTURE.md` for scope, dependencies, and chapter completion;
- `docs/EDITORIAL_STYLE.md` for voice, terminology, captions, and examples;
- `docs/PDF_BUILD.md` for publication commands and visual quality assurance;
- `docs/CURRICULUM_RESEARCH_2026.md` for the documented curriculum comparison;
- chapter release reviews in `docs/` when working on Chapters 1 or 2.

Editable sources and tested examples are authoritative. Files under `output/` are
generated deliverables and must not be edited directly.

## Authoring requirements

- Write in a natural, professional professor's voice and teach from concrete
  details toward the whole system.
- Expand an abbreviation at its first meaningful use in each chapter.
- Explain commands from the correct working directory and show the expected
  evidence. Do not assume a beginner knows how to identify a terminal, browser
  panel, file location, server process, or error message.
- Keep client-side and server-side responsibilities explicit while showing how
  they cooperate through HTTP.
- Use chapter-local numeric captions such as `Figure 2.1` and `Table 2.1`; never
  append alphabetic suffixes.
- Mention every figure and table by number in the prose. Label important objects,
  messages, and paths inside instructional visuals.
- Use real browser output for executable visual examples. Keep generated
  illustrations distinct from evidence screenshots.
- Give complete, reasoned answers for laboratories, exercises, and quizzes.

## Verification

After relevant changes, run the narrowest checks that cover the work. Before a
publication handoff, run all of the following from the repository root:

```powershell
npm test
npm run pdf
npm run pdf:verify
```

Render and inspect the complete PDF for overflow, clipping, collisions, captions,
tables, arrowheads, image quality, headers, footers, and section transitions.
Correct source files or the builder, rebuild, and verify again. Report the exact
current PDF path rather than referring to an older edition from memory.

## Change discipline

Preserve existing user changes and avoid unrelated rewrites. Do not change the
author, course language, framework sequence, chapter numbering, or assessment
policy without explicit direction. Research current official sources before
making update-sensitive technical claims.
