# Web Programming: From the Platform to Production

The canonical repository for the university Web Programming course taught by
Dr. Mahyar Teymournezhad in the Computer Engineering program. It combines the
course book, bilingual editions, student laboratories, instructor solutions,
assessments, publication tooling, and verification checks in one maintained
course directory.

## Current status

The curriculum is approved and the book is in active production. Part I and
Chapters 4-5 are complete and verified. The remaining chapters in Parts II-IV
complete the core semester, while Part V forms the advanced reference. See the
[research-based curriculum proposal](CURRICULUM_PROPOSAL.md),
[2026 comparative research review](docs/CURRICULUM_RESEARCH_2026.md), and
[complete book architecture](docs/BOOK_ARCHITECTURE.md) for the teaching path,
dependencies, assessment model, and chapter release standard.

## Published sessions

- [Orientation - Prepare Your Web-Programming Workstation](book/part-0-orientation/00-development-environment-setup.md)
- [Session 1 - How the Web Works](book/part-1-foundations/01-how-the-web-works.md)
- [Session 2 - Semantic HTML and Accessible Forms](book/part-1-foundations/02-semantic-html-and-accessibility.md)
- [Session 3 - CSS, Layout, and Responsive Design](book/part-1-foundations/03-css-cascade-layout-and-responsive-design.md)
- [Session 4 - JavaScript from First Principles](book/part-2-browser-programming/04-javascript-from-first-principles.md)
- [Session 5 - The DOM, Events, and Forms](book/part-2-browser-programming/05-dom-events-and-forms.md)
- [Laboratory index](labs/README.md)

## Canonical GitHub repository

[Mahyar2020/web-programming-coursework-2026_Fall](https://github.com/Mahyar2020/web-programming-coursework-2026_Fall)
is the main course repository. It contains the editable sources, English and
Turkish PDF editions, direct student laboratories, instructor reference
solutions, assessments, and publication tools.

Students should create their own private repository through the workflow
authorized by the instructor and work in the direct `labs/week-NN` folders.
The `labs/solutions` tree is intended for instructor review and guided feedback,
not for submission as student work.

## Current PDF editions

- [English Foundations Edition v21](output/pdf/web-programming-from-platform-to-production-foundations-edition-revised-v21.pdf)
- [Turkish Foundations Edition v21](output/pdf/web-programming-from-platform-to-production-foundations-edition-revised-v21-tr.pdf)
- [PDF build and publication guide](docs/PDF_BUILD.md)
- [Editorial and teaching style](docs/EDITORIAL_STYLE.md)

Run `npm run pdf` to rebuild the English edition and `npm run pdf:verify` before
publication. The Turkish build and verification commands are `npm run pdf:tr`
and `npm run pdf:tr:verify`.

## Prepare and verify the repository

Open a terminal in the repository root. Before running a project command, make
sure the prompt ends with `web-programming-coursework-2026_Fall`.

Windows Command Prompt:

```text
cd C:\Users\Mahyar\Documents\GitHub\web-programming-coursework-2026_Fall
dir package.json
node --version
npm --version
npm test
```

PowerShell:

```text
Set-Location C:\Users\Mahyar\Documents\GitHub\web-programming-coursework-2026_Fall
Get-Item package.json
node --version
npm --version
npm test
```

The Node.js version must begin with `v26.`. The final command should report that
all link, laboratory, and foundations checks passed.

## Repository map

```text
web-programming-coursework-2026_Fall/
  book/                 editable English chapters
  translations/tr/      aligned Turkish chapter sources
  course-book/          current distributable PDF copies
  output/pdf/           generated PDF editions and translation state
  docs/                 architecture, research, editorial, and build guidance
  assets/images/        illustrations and evidence screenshots
  assessment/           current assessment packages
  labs/
    week-01/ ... week-05/      direct student activities
    starters/week-01/ ...      maintainer starter sources
    solutions/week-01/ ...     tested instructor references
  scripts/              tests, local server, assessment, and PDF tooling
  package.json          commands and Node.js requirements
```

Each direct `labs/week-NN` folder is a student activity. Read the matching book
session and guided-laboratory section before changing its files.

## View a laboratory in the browser

Run only one server command at a time:

```text
npm run serve:week01
npm run serve:week02
npm run serve:week03
npm run serve:week04
npm run serve:week05
```

After the command prints `Open http://localhost:8000/`, leave that terminal
running and open `http://localhost:8000/` in a browser. Stop the server with
`Ctrl+C` before starting another week. Keep a second terminal available for
`git status`, `npm test`, and other commands.

Maintainers can preview a separated starter or solution with commands such as
`npm run serve:week05:starter` and `npm run serve:week05:solution`.

## Save work and send it to GitHub

Saving, committing, and pushing are separate actions:

```text
git status
git diff
git add path-to-the-file-you-changed
git diff --staged
git commit -m "Describe the completed change"
git push
```

Review paths before staging. Never commit passwords, access tokens, private
keys, recovery codes, `.env` files, or private student information. After
pushing, refresh GitHub and confirm that the latest commit is visible.

## Getting help

When reporting a problem, include the operating system, exact command, terminal
working directory, and complete error text. Remove credentials and unrelated
personal information before sharing screenshots or logs.
