# Complete Book Architecture

This document is the production map for *Web Programming: From the Platform to
Production*. It turns the semester syllabus into a complete reference-book
structure while keeping the core course teachable in fifteen weeks.

## Part I — The Web Platform

0. **Programming Foundations Bridge** — expressions, values, variables,
   selection, repetition, functions, collections, files, errors, tracing, and
   systematic debugging. A diagnostic routes experienced students past material
   they already know; first-time programmers complete it before Chapter 4.
1. **How the Web Works** — Internet and Web, clients and servers, URLs, Domain
   Name System, Internet Protocol addresses, transport, Transport Layer Security,
   HTTP, browser rendering, caches, developer tools, and evidence-led debugging.
2. **Semantic HTML and Accessible Forms** — document structure, text, links,
   media, tables, forms, native validation, accessibility tree, keyboard use, and
   responsible content structure.
3. **CSS, Layout, and Responsive Design** — cascade, inheritance, specificity,
   box model, units, typography, color, Flexbox, Grid, media/container queries,
   logical properties, and responsive images.

## Part II — Programming in the Browser

4. **JavaScript from First Principles** — values, types, variables, control flow,
   functions, scope, arrays, objects, mutation, equality, errors, debugging, and
   small tests.
5. **The Document Object Model, Events, and Forms** — parsing, the document tree,
   selecting and changing nodes, event propagation, default actions, form data,
   client validation, state, rendering, and progressive enhancement.
6. **Asynchronous JavaScript and Web APIs** — call stack, task and microtask
   queues, promises, `async`/`await`, `fetch`, JSON, HTTP failures, cancellation,
   Cross-Origin Resource Sharing, storage, and resilient loading/empty/error
   states.
7. **Modules, Tooling, and TypeScript** — ECMAScript modules, npm, dependency
   trust, package metadata, Vite, linting, formatting, source maps, strict
   TypeScript, narrowing, interfaces, generics, and typed browser boundaries.

## Part III — Programming on the Server and with Data

8. **From an HTTP Listener to an Express API** — the Node runtime, environment
   and process, a minimal native server, routing, middleware, request parsing,
   validation, structured errors, logs, REST semantics, and OpenAPI contracts.
9. **Relational Data and PostgreSQL** — entities and relationships, keys,
   constraints, normalization, SQL create/read/update/delete operations, joins,
   parameterized queries, migrations, indexes, and query inspection.
10. **Application Architecture and Reliable Data Changes** — routes, controllers,
    services, repositories, dependency direction, transactions, isolation,
    concurrency, idempotency, file handling, pagination, filtering, sorting, and
    server-rendered HTML as an architectural alternative.
11. **Identity, Sessions, Authorization, and Web Security** — trust boundaries,
    password hashing, cookies, sessions, authentication, authorization, least
    privilege, Cross-Site Request Forgery, Cross-Site Scripting, injection,
    security headers, rate limits, OAuth 2.0/OpenID Connect concepts, and secure
    failure.

## Part IV — Application and Production Engineering

12. **React as a User-Interface Model** — why components exist, JSX, props,
    state, events, composition, controlled forms, identity/keys, accessibility,
    and comparison with direct Document Object Model programming.
13. **Data-Driven React Applications** — routing, effects and their alternatives,
    server state, caching, optimistic interaction, errors, suspense concepts,
    rendering performance, and component/integration tests.
14. **Testing, Review, and Continuous Integration** — test strategy, unit,
    integration, contract, and end-to-end tests; test doubles; static analysis;
    accessibility testing; security testing; review; refactoring; and continuous
    integration gates.
15. **Deployment and Operations** — build artifacts, environments, configuration,
    secrets, containers, Domain Name System and HTTPS in deployment, application
    server versus reverse proxy, processes, graceful shutdown, health/readiness,
    logs, metrics, tracing concepts, caching, performance budgets, backups,
    rollback, and incident learning.

## Part V — Advanced Web Systems

16. Browser internals, critical rendering path, performance, workers, and memory.
17. Real-time communication with WebSockets and Server-Sent Events.
18. GraphQL and API-design tradeoffs.
19. Server-side rendering, static generation, hydration, streaming, and React
    Server Components.
20. Advanced PostgreSQL: plans, locks, isolation, full-text search, and JSON.
21. Distributed systems: caches, queues, retries, idempotency, consistency,
    horizontal scale, and failure modes.
22. Internationalization, localization, Unicode, time zones, and bidirectional
    interfaces.
23. Progressive Web Applications, service workers, and offline-first design.
24. Privacy engineering, analytics, consent, retention, and responsible data use.
25. Secure software supply chains, provenance, Software Bills of Materials, and
    secrets management.
26. Graphics, media, device APIs, and WebAssembly.
27. Cloud architecture and infrastructure as code without vendor lock-in.

## Appendices

A. The published orientation provides zero-start setup for Windows, macOS, and Linux.  
B. Command line and Git field guide.  
C. HTML, CSS, JavaScript, HTTP, SQL, and accessibility quick references.  
D. Debugging decision trees and error-message reading.  
E. Glossary with first-use expansion of abbreviations.  
F. Complete formative answer key and solution index.  
G. Instructor lesson plans, rubrics, accommodations, and private-assessment model.  
H. Version ledger, errata, migrations, and technical-review history.

## Learning dependency map

```text
web request and browser model
        |
        +--> semantic HTML --> accessible forms --------+
        |                                                |
        +--> CSS and responsive layout ------------------+--> browser application
        |                                                |          |
        +--> JavaScript --> DOM/events --> async/API -----+          |
                                                                   HTTP contract
                                                                        |
JavaScript --> Node listener --> Express --> validation ----------------+
                                      |                                 |
SQL --> relational model --> transactions ------------------------------+
                                                                        |
                                             authentication/authorization
                                                                        |
                                              integrated application
                                                       |
                                         tests --> CI --> deployment
                                                       |
                                              operations and scale
```

The arrows express prerequisites, not a production network diagram. The browser
and server are learned independently, connected by an HTTP contract, and then
tested together.

## Chapter release definition

A chapter is complete only when all of these artifacts exist and agree:

- reader-facing narrative from concrete detail to whole-system model;
- measurable learning outcomes and explicit prerequisites;
- original diagrams with numbered captions and references in the prose;
- runnable concept examples and a tested Campus Hub feature;
- an output capture or deterministic output transcript for every example whose
  purpose is visible behavior;
- guided laboratory, checkpoints, accessibility/security criteria, and cleanup;
- foundation, application, and challenge exercises with fully reasoned answers;
- debugging clinic with diagnosis, evidence, repair, and prevention;
- quiz with explanations for correct and incorrect choices;
- summary, glossary, primary references, and update-sensitive note;
- instructor timing, misconceptions, demonstration plan, rubric, and
  accommodations;
- automated build/test checks and a visual PDF review.

## Stable core and changing layer

Concept chapters explain standards and mechanisms without unnecessary product
versions. A machine-readable version ledger pins the runtime and dependencies used
to test code. Framework chapters state their technical-review date and isolate
version-specific syntax in clearly marked implementation notes. Each academic
year, maintainers review supported Node releases, browser baselines, WCAG/ARIA,
OWASP guidance, TypeScript, React, Express, PostgreSQL, Vite, testing tools, and
deployment instructions before issuing a new edition.

## Maintenance calendar

- **Before every semester:** run all automated checks, validate links, rebuild and
  inspect the PDF, review security advisories, and test setup instructions on a
  clean Windows, macOS, and Linux environment.
- **Every six months:** review runtime and dependency support status, browser
  baseline changes, OWASP guidance, accessibility guidance, and screenshots.
- **Every year:** obtain independent reviews from at least one instructor, one
  subject specialist, and novice readers; revise misconceptions, examples,
  assessment validity, and the index.
- **At each major standards or framework change:** issue a dated compatibility
  note immediately, then decide whether a new edition is required. Never silently
  rewrite a result that a current cohort is being graded against.
- **For every release:** publish the technical-review date, tested versions,
  errata status, and a concise migration note from the previous edition.
