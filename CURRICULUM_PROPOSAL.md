# Web Programming: From the Platform to Production

## Research-Based Curriculum Proposal

**Status:** Draft for faculty decision  
**Research reviewed:** 29 August 2026  
**Default format:** 15 teaching weeks, adaptable to 14 or 16 weeks  
**Audience:** Computer engineering undergraduates with no assumed web-development
knowledge. One introductory programming course is recommended; a programming
foundations bridge supports readers who need it.

## 1. Executive decision

The book should teach enduring web concepts first and contemporary tools second.
Students should begin with the browser, HTML, CSS, JavaScript, URLs, HTTP, and the
request-response model. Only after they can build and debug a small application
without a framework should they move to TypeScript, React, Node.js, Express, and
PostgreSQL.

The recommended application stack is:

| Layer | Core choice | Reason |
|---|---|---|
| Web platform | Semantic HTML, modern CSS, browser JavaScript | Standards outlive frameworks and make framework behavior understandable. |
| Language progression | JavaScript first, then TypeScript in strict mode | One language spans browser and server; delaying types avoids teaching syntax, the DOM, and a type system simultaneously. |
| Front end | React with Vite, after vanilla DOM programming | React is useful and widely taught, but it should be presented as one UI model rather than “the web.” |
| Server | Node.js 24 LTS and Express 5 | A single-language full stack reduces accidental complexity; use an LTS runtime rather than the current non-LTS release. |
| Data | PostgreSQL and SQL | Relational modeling, constraints, joins, indexes, and transactions are core computer-engineering knowledge. |
| API | HTTP/JSON REST as the core; GraphQL as an extension | REST exposes the Web's native semantics and is easier to reason about, test, and secure in a first course. |
| Authentication | Server-side sessions first; token and OAuth/OIDC concepts second | Sessions make cookies, state, CSRF, and revocation concrete before more complex distributed identity. |
| Quality | ESLint, formatter, unit/integration/E2E tests, accessibility and performance audits | Quality practices must accompany construction, not appear only at the end. |
| Delivery | Git/GitHub, CI, containers, and one cloud deployment | Students should finish with a reproducible, deployed system and an observable delivery pipeline. |

### The client and server are taught separately, then joined deliberately

Client-side and server-side programming are different responsibilities, even
when both are written in JavaScript. The browser owns presentation, interaction,
local interface state, and calls to remote services. The server owns trusted
validation, authorization, business rules, persistence, and the HTTP response.
Students therefore learn each environment in isolation before they build a
feature that crosses the boundary.

The course introduces a web server in four passes:

1. **Week 1 — observe a server:** run a tiny static development server and inspect
   its HTTP responses. At this stage, “server” means a program that listens for a
   request and returns a response; no server-side application code is required.
2. **Week 6 — use a server:** call a supplied Application Programming Interface
   (API) from the browser and handle latency, malformed data, and failure.
3. **Week 8 — build a server:** first implement one route with Node's native HTTP
   facilities, then use Express. This order makes routing and middleware
   conveniences intelligible instead of magical.
4. **Week 15 — operate a server:** deploy behind HTTPS, separate configuration
   from code, manage processes and graceful shutdown, expose health checks, and
   interpret logs and metrics. A reverse proxy is explained as an optional
   production component, not confused with the application server itself.

The first full-stack feature is taught as a traceable round trip: a user action
in the browser creates an HTTP request; routing, validation, authorization, and a
database operation occur on the server; a response crosses the network; then the
browser updates the interface. Every later feature keeps this responsibility
boundary visible in diagrams, code organization, tests, and debugging exercises.

Do **not** make Bootstrap, Tailwind, Next.js, MongoDB, GraphQL, or a cloud vendor
the spine of the book. They are valuable comparisons or extensions, but each
would consume time better spent on transferable foundations. Next.js and React
Server Components should be an advanced survey, not required infrastructure for
the first complete application.

## 2. What the research says

This proposal compares official university materials and authoritative standards;
it does not copy their text or exercises.

### Current university course patterns

- [Stanford CS142](https://bulletin.stanford.edu/courses/2085161) covers browser
  facilities, JavaScript frameworks, server-side JavaScript, sessions, databases,
  security, scalability, and deployment. Its public lecture sequence moves from
  HTML/CSS and JavaScript through React, HTTP, Node/Express, data, sessions,
  validation, security, and scale.
- [Harvard CS50 Web](https://cs50.harvard.edu/web/) uses a project-centered
  sequence spanning HTML/CSS, Git, Python/Django, SQL, JavaScript, UI, testing,
  CI/CD, scalability, and security. The important lesson is the breadth and
  project structure, not the necessity of Django for this book.
- [Carnegie Mellon 17-437/637](https://www.cmu-webapps.org/static/index/syllabus.pdf)
  has a particularly balanced 2026 schedule: HTML/CSS, DOM JavaScript, HTTP,
  Django, sessions, responsive design, forms, authentication, models, files,
  AJAX, WebSockets, cloud deployment, software engineering, HTTPS, OAuth, React,
  transactions, scalability, REST, internationalization, and testing.
- [Cornell INFO 2300](https://classes.cornell.edu/browse/roster/FA25/class/INFO/2300)
  emphasizes HTTP, server-rendered HTML, relational SQL, accessible forms,
  cookies, secure sessions, Git, development containers, documentation, and
  responsible use of generative AI. Its learning outcomes are unusually clear
  and directly useful for this book.
- [University of Washington CSE154](https://courses.cs.washington.edu/courses/cse154/)
  organizes the subject around HTML/CSS, client-side scripting, APIs, server-side
  scripting, databases, and security. Its materials explicitly recommend MDN as
  the principal reference rather than depending on a conventional textbook.
- [University of Helsinki Full Stack Open](https://fullstackopen.com/en/part0/general_info/)
  demonstrates the value of a large, exercise-driven application that grows in
  small steps. Its current coverage includes React, Node, testing, TypeScript,
  CI/CD, containers, relational databases, GraphQL, and Next.js. It assumes prior
  programming, web, database, and Git knowledge, so its sequence is too abrupt
  for a true zero-to-advanced book but excellent for the second half.
- [MIT web.lab](https://webdevelopment.mit.edu/) uses HTML, CSS, JavaScript,
  Node, and a database to produce a dynamic server-backed site through an
  intensive build-and-iterate format. MIT's
  [Design for the Web](https://designftw.mit.edu/) reinforces teaching the core
  languages and the design rationale behind them.

### Standards and professional baseline

- The [MDN Curriculum](https://developer.mozilla.org/en-US/curriculum/), updated
  in October 2025, defines semantic HTML, CSS, JavaScript, accessibility,
  responsive design, testing, frameworks, version control, and tooling as the
  essential front-end baseline. MDN explicitly warns that new developers often
  learn frameworks without understanding the underlying platform.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the current W3C accessibility
  Recommendation. Accessibility must therefore be a design constraint in every
  relevant chapter, not a final-week checklist.
- [OWASP Top 10:2025](https://owasp.org/Top10/) updates the security baseline to
  include broken access control, misconfiguration, supply-chain failures,
  cryptographic failures, injection, insecure design, authentication failures,
  integrity failures, logging/alerting failures, and exceptional-condition
  handling.
- [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/) supports a competency-based
  design that integrates software development, security, ethics, and professional
  practice rather than treating the course as a tour of syntax.
- As of the research date, [Node.js 24 is LTS while Node.js 26 is Current](https://nodejs.org/en/about/previous-releases),
  [Express 5 is released](https://expressjs.com/en/guide/migrating-5.html),
  and [React documentation targets 19.2](https://react.dev/versions). The book
  should pin tested versions in a machine-readable file and keep prose
  version-light so routine upgrades do not invalidate the concepts.

### Course-book conclusion

Several leading courses require no conventional textbook and instead use course
notes plus primary documentation. The older *Web Programming Step by Step* was
formerly used at Washington, but its PHP/Ajax-era stack is no longer an
appropriate technical spine. Our book should combine the coherence of a textbook
with the updateability of living documentation: original explanations, tested
code, labs, and assessments, with curated links to MDN, WHATWG/W3C, ECMAScript,
Node, PostgreSQL, React, and OWASP documentation.

## 3. Learning outcomes

By the end of the core course, a successful student will be able to:

1. Explain how a URL becomes a rendered page, including DNS, TCP/IP at a useful
   abstraction level, TLS, HTTP requests, responses, caching, and browser work.
2. Build semantic, responsive, accessible interfaces using HTML and CSS without
   depending on a component or CSS framework.
3. Write, debug, and test modern JavaScript and TypeScript; use modules,
   asynchronous operations, browser APIs, and event-driven programming.
4. Design client-server interfaces using HTTP semantics, JSON, validation,
   consistent errors, pagination, and an OpenAPI description.
5. Build a layered Node/Express application and explain its control flow.
6. Model relational data; write parameterized SQL; use constraints, joins,
   transactions, migrations, and indexes; recognize ORM tradeoffs.
7. Implement authentication and authorization safely using password hashing,
   secure cookies, sessions, CSRF defenses, and least privilege.
8. Build a React interface using components, state, effects only when appropriate,
   forms, routing, and server-state patterns, while explaining what React
   abstracts.
9. Apply unit, integration, and end-to-end testing; use static analysis, code
   review, CI, and reproducible environments.
10. Threat-model, deploy, observe, measure, and improve a web application for
    security, accessibility, performance, reliability, and scalability.
11. Read primary documentation, evaluate unfamiliar tools, and justify technical
    decisions rather than following tutorials mechanically.
12. Use AI assistance transparently and critically, validate its output, cite its
    contribution, and remain able to explain and modify submitted work.

“Advanced” should mean that students can reason about and extend a production-like
system—not that every current framework has been mentioned. The core semester can
take a novice from zero web knowledge to competent full-stack practice. Specialist
topics belong in extension chapters.

## 4. Pedagogical and programming approach

### One evolving reference application

Use one accessible, multilingual **Campus Hub** throughout the book: announcements,
events, clubs, registrations, comments, search, moderation, and notifications.
Each chapter adds a vertical capability. Students repeatedly see the same concept
at a larger scale instead of discarding a toy project every week.

Alongside it, use tiny “concept programs” that isolate one idea. This combination
avoids both extremes: a monolith that hides the lesson and disconnected snippets
that never become software.

### The recurring learning cycle

Every session follows the same structure:

1. **Before class:** short diagnostic and 10–20 minutes of reading.
2. **Concept model:** diagrams and executable examples explain why the mechanism
   exists before introducing an API.
3. **Predict:** students predict output, network traffic, layout, state changes,
   or failure modes before running code.
4. **Guided lab:** a partially scaffolded feature with checkpoints.
5. **Independent exercise:** a transfer problem with different surface details.
6. **Debugging clinic:** one realistic broken implementation.
7. **Retrieval quiz:** 6–10 short questions, including code reading and design
   judgment rather than vocabulary alone.
8. **Reflection:** students explain one decision, one bug, and one remaining risk.

### Complexity staircase

- Provide a pre-course programming bridge covering expressions, variables,
  selection, repetition, functions, collections, files, errors, and systematic
  debugging. It is required for true first-time programmers and diagnostic-based
  review for everyone else; it does not displace the web-focused semester.
- Begin with files that run directly in the browser.
- Add the command line and Git before package management.
- Add npm and Vite only when modules and a development server solve a problem the
  students have already experienced.
- Teach JavaScript before TypeScript; then migrate a small working module to strict
  TypeScript so types have an observable purpose.
- Teach the DOM before React; then rebuild one feature in React and compare the
  state model, accessibility, network behavior, and testing cost.
- Teach SQL before an ORM/query builder; all generated database behavior must
  remain inspectable.
- Teach server sessions before token-based authentication and OAuth/OIDC.
- Teach deployment only after automated tests and configuration separation exist.
- Teach browser code and server code in separate directories and processes before
  introducing an integrated development workflow. The same language must never
  be allowed to blur the security boundary between an untrusted client and a
  trusted server.

### Accessibility, security, and ethics are cross-cutting

Every lab has explicit accessibility and security acceptance criteria. Examples:
keyboard navigation begins with the first form; injection is discussed with the
first untrusted input; secrets are addressed with the first API; authorization is
checked with the first protected record; dependency risk begins with the first
`npm install`; privacy and data minimization begin with the first database table.

### AI-use policy

Teach AI as a fallible engineering tool, not as a substitute author.

- Allowed for explanation, brainstorming, test-case suggestions, documentation
  lookup, and critique, with disclosure.
- Allowed for code only when the task permits it, the prompt/output is logged, the
  student tests it, and the student can explain and modify it in a short oral or
  live-code check.
- Not allowed during closed quizzes or practical competency checks.
- Never enter secrets, personal student data, unpublished assessment banks, or
  proprietary code into an external model.
- Grade the evidence: commits, tests, design notes, debugging record, and oral
  defense—not merely the final repository state.

## 5. Proposed 15-week semester

The default assumes one lecture/workshop and one laboratory block per week. For a
14-week semester, combine Weeks 14 and 15. For two meetings per week, divide each
row into concepts and application.

| Week | Concepts and book chapter | Required laboratory | Evidence of mastery |
|---:|---|---|---|
| 1 | Course workflow; files, terminal, editor, Git; Internet vs Web; URL, DNS, TCP/TLS, HTTP; browser pipeline | Inspect a real request in DevTools; build and publish the first static Campus Hub page | Annotated request/response and first Git commits |
| 2 | Semantic HTML; document structure; links, media, tables, forms; validation; accessibility tree | Build an accessible event-submission form using only HTML | Validator report, keyboard test, semantic rationale |
| 3 | CSS cascade, inheritance, specificity, box model, units, typography, Flexbox, Grid, responsive design | Implement the responsive Campus Hub shell from a supplied design | Three viewport checks and no horizontal overflow |
| 4 | JavaScript values, control flow, functions, arrays/objects, scope, errors, modules, debugging | Build and test a data-transformation module for events | Console/debugger trace and unit tests |
| 5 | DOM, events, forms, client validation, state, rendering, progressive enhancement, storage | Add event filtering, accessible dialog behavior, and saved preferences | Keyboard flow and DOM/state explanation |
| 6 | Asynchrony, event loop, promises, `async`/`await`, `fetch`, JSON, failures, cancellation, CORS | Consume a supplied API with loading, empty, success, and error states | Network trace and resilient UI |
| 7 | npm, dependency trust, ESM, Vite, linting/formatting; TypeScript types, narrowing, interfaces, generics at a practical level | Migrate the Week 6 client to strict TypeScript | Zero type errors; dependency and build explanation |
| 8 | Server runtime; Node; Express 5; routing, middleware, request validation, errors, logs; REST and OpenAPI | Implement read/write event endpoints with consistent errors | API tests and OpenAPI document |
| 9 | Relational modeling; keys, constraints, normalization, SQL CRUD, joins, parameterization, migrations | Model and implement events, users, registrations, and capacity rules in PostgreSQL | ER model, migration, and query set |
| 10 | Layered architecture; transactions; concurrency; files; pagination, filtering, sorting; server-rendered HTML comparison | Connect API to PostgreSQL and make registration atomic | Integration tests including race/error cases |
| 11 | Cookies, sessions, password hashing, authentication vs authorization, CSRF, CORS, OAuth/OIDC concepts | Add login/logout and owner/moderator authorization | Negative authorization tests and threat model |
| 12 | React mental model; components, JSX, props, state, events, controlled forms, composition, accessibility | Rebuild the events interface in React with Vite | Behavior parity plus component rationale |
| 13 | React data flow; routing; effects; server state; optimistic UI; error boundaries; performance basics | Add routing and registration UX without duplicating server state | Component/integration tests and render analysis |
| 14 | Test strategy; unit/integration/E2E; test doubles; CI; code review; refactoring; OWASP Top 10:2025 | Security review and Playwright user journey; configure CI quality gates | Passing pipeline, review report, fixed vulnerabilities |
| 15 | Containers, configuration/secrets, deployment, HTTPS, logging, monitoring, caching, load and graceful failure; WebSockets/GraphQL/SSR survey | Deploy the capstone, run accessibility/performance/security checks, and conduct demo/defense | Live system, operations runbook, retrospective |

## 6. Per-session book contract

Every chapter must contain all of the following. This is a publishing contract,
not an aspiration:

1. Session title, duration, prerequisites, and measurable learning outcomes.
2. A motivating failure or user need.
3. A precise conceptual explanation with diagrams where relationships matter.
4. Minimal runnable examples and a larger reference-application example.
5. “Predict before running” questions with immediate explanations.
6. A guided lab with setup, checkpoints, tests, accessibility/security criteria,
   common failures, cleanup, and a completed reference solution.
7. Independent exercises at three levels: foundation, application, and challenge.
8. Full worked answers that explain reasoning and alternatives, not just final code.
9. A debugging exercise and diagnosis.
10. A 6–10 item quiz with answer explanations and misconception notes.
11. A one-page summary, glossary, primary-source reading list, and “what changes
    often” update note.
12. Instructor notes: timing, live-demo plan, likely misconceptions, optional
    extensions, grading rubric, and accommodations.

All code solutions must be executable and automatically tested. Code blocks in the
manuscript should be extracted from tested source files during the build rather
than maintained as unverified copies.

## 7. Assessment and answer strategy

Putting every answer beside every graded question would make the book useful for
self-study but unusable for secure assessment. Use three layers:

### Student book

- Full answers to all formative exercises and labs, placed after a deliberate
  attempt boundary.
- Complete quiz answers and explanations for self-study.
- Rubrics and sample high-quality reasoning.

### Public practice bank

- Parameterized variants of each exercise and quiz.
- Automated feedback for objective checks.
- No claim that these questions are secure summative assessments.

### Private instructor supplement

- Isomorphic quiz and practical-test variants with solutions.
- Oral-defense prompts and grading anchors.
- Misconception-based distractor rationales.
- Versioned release each semester.

Recommended course weighting:

| Component | Weight |
|---|---:|
| Weekly labs and engineering journal | 20% |
| Three individual milestone projects | 30% |
| Quizzes and concept checks | 10% |
| Midterm practical | 15% |
| Team capstone, individual contribution, demo, and defense | 25% |

Projects should be graded on correctness, design, code quality, testing,
accessibility, security, documentation, and explanation. A working page alone is
not sufficient evidence of mastery.

## 8. Capstone progression

The Campus Hub capstone grows through graded milestones:

- **Milestone A — Inclusive interface (Weeks 1–5):** semantic, responsive,
  keyboard-accessible static and interactive client.
- **Milestone B — Data service (Weeks 6–10):** typed client, REST API, relational
  schema, validation, migrations, and integration tests.
- **Milestone C — Trustworthy application (Weeks 11–14):** authentication,
  authorization, React UI, security review, E2E tests, and CI.
- **Release — Production rehearsal (Week 15):** deployment, observability,
  performance budget, accessibility report, threat model, runbook, and defense.

Students may choose another problem domain, but it must meet the same technical,
accessibility, security, testing, and operational requirements.

## 9. Advanced extension chapters

These chapters make the book genuinely “zero to advanced” without pretending all
of them fit in one semester:

1. Browser internals, rendering performance, Web Workers, and service workers.
2. Real-time systems with WebSockets and Server-Sent Events.
3. GraphQL design and comparison with REST.
4. Server-side rendering, hydration, React Server Components, and meta-frameworks.
5. Advanced PostgreSQL: query plans, isolation, locks, full-text search, and JSON.
6. Distributed systems: caching, queues, idempotency, rate limits, horizontal
   scaling, consistency, and failure modes.
7. Secure software supply chains, dependency provenance, SBOMs, and secret
   management.
8. Internationalization, localization, time zones, Unicode, and bidirectional UI.
9. Progressive Web Apps and offline-first design.
10. Web APIs for graphics, media, devices, and WebAssembly.
11. Cloud architecture and infrastructure as code, taught vendor-neutrally.
12. Privacy engineering, analytics, consent, and responsible data design.

## 10. Book engineering and quality gates

Recommended repository design:

```text
book/
  part-1-foundations/
  part-2-browser-programming/
  part-3-server-and-data/
  part-4-production-engineering/
  part-5-advanced-topics/
labs/
  starters/
  solutions/
reference-app/
assessment/
  public-practice/
instructor/                 # private distribution or separate private repository
scripts/
```

Before a chapter is released:

- All example and solution code builds and tests on Windows, macOS, and Linux.
- Links are checked; dependency and runtime versions are recorded.
- HTML validates; keyboard operation and automated accessibility checks pass.
- Lint, type-check, unit, integration, and relevant E2E tests pass in CI.
- Security-sensitive examples are reviewed against OWASP guidance.
- At least one novice and one instructor perform a clarity review.
- Diagrams have text alternatives; screenshots are never the sole instruction.
- The chapter states its last technical review date and update-sensitive sections.

## 11. Adopted production assumptions

The author has authorized the following default decisions so drafting can proceed
without leaving the course architecture ambiguous:

1. The core uses fifteen teaching weeks and includes lecture/workshop and
   laboratory work. A documented mapping will support fourteen- and sixteen-week
   calendars.
2. The book assumes no web knowledge. A diagnostic programming bridge supports
   readers without a prior programming course, while the core JavaScript chapter
   still teaches the language from first principles.
3. The main edition is written in professional international English. Code,
   commands, protocol fields, and technical identifiers remain in English in any
   later translation.
4. PostgreSQL uses a reproducible development-container path plus a documented
   native installation alternative.
5. Formative exercises and their complete answers belong in the student book.
   Secure variants and grading anchors belong in a separately distributed
   instructor supplement.
6. AI tools are treated as fallible, disclosed engineering aids. Local university
   policy takes precedence where it is stricter.
7. Campus Hub remains the reference application; alternative capstones must
   satisfy the same outcomes and acceptance criteria.

The next production stage is Part II, beginning with Chapter 4 and its tested lab,
worked answers, quiz explanations, output evidence, instructor notes, and PDF
review. Chapters are released sequentially because later examples depend on the
tested behavior and vocabulary established earlier.
