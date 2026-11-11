# Laboratories

This course-book source repository contains both student starters and tested
reference solutions. Students work instead in the personal private repository
they create from the
[Fall 2026 coursework template](https://github.com/Mahyar2020/web-programming-coursework-2026_Fall).
That repository uses `labs/week-01` through `labs/week-04` and does
not contain solutions or book-production files.

The solutions are formative learning resources. Instructors should use fresh
private variants for graded practical assessments.

## Student coursework commands

From the root of the student's personal coursework repository, run one of these
commands and then visit `http://localhost:8000/`:

```text
npm run serve:week01
npm run serve:week02
npm run serve:week03
npm run serve:week04
```

Run only one server command at a time. Use `Ctrl+C` to stop it before serving a
different week. Run `npm test` to verify the student repository structure and
local servers.

## Course-book maintainer commands

The commands below work only in the course-book source repository because its
`package.json` deliberately exposes separate starter and solution scripts.

## Week 1

- [Starter](starters/week-01/index.html)
- [Reference solution](solutions/week-01/index.html)
- Verification: run `npm test` from the course-book repository root with Node.js
  24 LTS.
- Local preview: run `npm run serve:week01:starter` or
  `npm run serve:week01:solution`, then visit `http://localhost:8000/`.

## Week 2

- [Starter](starters/week-02/index.html)
- [Reference solution](solutions/week-02/index.html)
- Focus: semantic landmarks, accessible forms, native validation, and keyboard
  evidence.
- Local preview: run `npm run serve:week02:starter` or
  `npm run serve:week02:solution`.

## Week 3

- [Starter HTML](starters/week-03/index.html) and [starter CSS](starters/week-03/styles.css)
- [Reference HTML](solutions/week-03/index.html) and [reference CSS](solutions/week-03/styles.css)
- Focus: cascade layers, resilient sizing, Flexbox, Grid, responsive reflow,
  focus visibility, and reduced motion.
- Local preview: run `npm run serve:week03:starter` or
  `npm run serve:week03:solution`.

## Week 4

- The zero-start examples provide [a first Node.js file](starters/week-04/hello.js),
  [a first browser page](starters/week-04/hello-browser.html), and
  [its external JavaScript](starters/week-04/hello-browser.js).
- The cumulative laboratory provides [starter HTML](starters/week-04/index.html),
  [starter CSS](starters/week-04/styles.css), and
  [starter JavaScript](starters/week-04/events.js).
- The reference version provides [solution HTML](solutions/week-04/index.html),
  [solution CSS](solutions/week-04/styles.css),
  [solution JavaScript](solutions/week-04/events.js), and
  [automated tests](solutions/week-04/events.test.js).
- Focus: installation evidence, first execution in Node.js and a browser, values,
  bindings, explicit conversion, control flow, functions, arrays, objects,
  validation, errors, and small automated tests.
- Local preview: run `npm run serve:week04:starter` or
  `npm run serve:week04:solution`.
