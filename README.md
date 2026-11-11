# Web Programming: From the Platform to Production

An open course book for a university-level web programming course in a computer
engineering program.

## Current status

The curriculum is approved and the book is in active production. Part I and
Chapter 4 are complete and verified; the remaining chapters in Parts II-IV complete the core semester and Part V forms
the advanced reference. See the [research-based curriculum
proposal](CURRICULUM_PROPOSAL.md), [2026 comparative research
review](docs/CURRICULUM_RESEARCH_2026.md), and [complete book
architecture](docs/BOOK_ARCHITECTURE.md) for the evidence, teaching approach,
chapter dependencies, assessment model, and release standard.

## Foundations chapters

- [Orientation - Prepare Your Web-Programming Workstation](book/part-0-orientation/00-development-environment-setup.md)
- [Session 1 - How the Web Works](book/part-1-foundations/01-how-the-web-works.md)
- [Session 2 - Semantic HTML and Accessible Forms](book/part-1-foundations/02-semantic-html-and-accessibility.md)
- [Session 3 - CSS, Layout, and Responsive Design](book/part-1-foundations/03-css-cascade-layout-and-responsive-design.md)
- [Session 4 - JavaScript from First Principles](book/part-2-browser-programming/04-javascript-from-first-principles.md)
- [Laboratory assets](labs/README.md)

Run `npm test` with Node.js 24 LTS to verify the current book assets.

## Course repositories

- [Course-book source](https://github.com/Mahyar2020/web-programming-course-book)
  - used by the author and instructors to build the book and verify reference
  solutions.
- [Fall 2026 student coursework template](https://github.com/Mahyar2020/web-programming-coursework-2026_Fall)
  - used by each student to create a separate private coursework repository.

Both repositories are private. GitHub may display `404` until the signed-in
account has accepted the appropriate invitation. Student laboratory commands in
the book assume the personal repository created from the coursework template,
not the course-book source repository.

## PDF edition

- [Download the revised Foundations Edition (v21, latest)](output/pdf/web-programming-from-platform-to-production-foundations-edition-revised-v21.pdf)

Author: **Dr. Mahyar Teymournezhad**

- [PDF build and publication guide](docs/PDF_BUILD.md)
- [Editorial and teaching style](docs/EDITORIAL_STYLE.md)

Run `npm run pdf` to rebuild the edition from the Markdown chapters and tested
source files, then run `npm run pdf:verify` before publication.
