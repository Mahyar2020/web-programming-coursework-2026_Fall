# Curriculum Research Review, 2026

**Review date:** 29 August 2026  
**Purpose:** document the evidence behind the course-book architecture  
**Scope:** official university materials, standards, primary documentation, and
selected books that offer a useful pedagogical or professional model

## 1. Method and limits

This review asks a practical question: what should a computer-engineering student
be able to explain and build after one university course in web programming?
Ranking alone is not a sound curriculum method. Public materials differ in age,
prerequisites, semester length, and institutional purpose. The review therefore
uses highly regarded university courses as comparative cases and checks their
technical claims against standards and official documentation.

Four tests were applied to every proposed topic:

1. **Durability:** will the underlying knowledge remain useful when a library
   changes?
2. **Explanatory power:** does it help a student predict behavior and diagnose a
   failure?
3. **Professional necessity:** is it required to build a secure, accessible,
   maintainable application rather than only a demonstration?
4. **Teachability:** can a novice encounter it in a coherent dependency order and
   demonstrate mastery through an authentic task?

The result is not a collage of other syllabi. It is an original course design
whose breadth is externally checked and whose implementation choices are stated
explicitly.

## 2. Comparative university evidence

**Table 1. Comparative evidence from university courses and curricula.**

| Course or curriculum | Characteristic emphasis | What this book adopts | What this book changes |
|---|---|---|---|
| Stanford CS142, *Web Applications* | Browser facilities, JavaScript frameworks, server-side JavaScript, sessions, data, security, scalability, and deployment | A genuine full-stack arc and production concerns | More introductory networking, accessibility, and guided practice for readers starting with no web knowledge |
| Harvard CS50 Web | Project sequence across HTML/CSS, Git, Python/Django, SQL, JavaScript, testing, continuous integration and continuous delivery, scalability, and security | Milestone projects and assessment of design and style as well as correctness | JavaScript/TypeScript and Node keep one language across the stack; the underlying concepts, not Django, are transferred |
| Carnegie Mellon 17-437/637 | Server programming, Django, increasingly sophisticated individual applications, and a substantial team project | Server-side depth, software-engineering habits, authentication, transactions, deployment, and team delivery | A slower browser-first opening and a standards-based accessibility thread |
| Cornell INFO 2300 | Server-rendered sites, HTTP, relational Structured Query Language, forms, cookies, sessions, Git, containers, and professional documentation | Server-rendered comparison, relational reasoning, secure sessions, accessible forms, and professional evidence | A later single-page application path so students can compare architectures rather than inherit one by default |
| University of Washington CSE154 | Explicit modules for HTML/CSS, Document Object Model JavaScript, consuming APIs, writing services, and databases | A clear client/server separation followed by integration | PostgreSQL replaces a lightweight teaching database in the main path; testing and operations receive more depth |
| University of Helsinki Full Stack Open | Exercise-rich React, Node, testing, TypeScript, continuous integration, containers, relational databases, GraphQL, and current frameworks | Incremental exercises, automated feedback, and a growing reference application | Foundations precede React because this book does not assume prior web, database, and Git knowledge |
| MIT web.lab | Intensive build-and-iterate work with HTML, CSS, JavaScript, React, Node, databases, design, and team projects | Rapid prototype/review cycles and attention to user-interface design | A full semester supplies more conceptual explanation, explicit security, and systematic assessment |
| MDN Curriculum | A vendor-neutral baseline for semantic HTML, CSS, JavaScript, accessibility, responsive design, tools, testing, and frameworks | The front-end competency baseline and platform-first order | Server, database, authentication, operations, and computer-engineering depth are added |

The comparison reveals a stable common core: HTML, CSS, JavaScript, HTTP,
client-side interaction, server-side programming, persistent data, security, and
project work. The differences are mainly language/framework choices and assumed
prerequisites. That is why this book treats the common core as durable and the
chosen stack as a replaceable implementation of it.

## 3. Standards and professional baseline

The standards hierarchy prevents tutorial folklore from becoming textbook fact.

**Table 2. Authority hierarchy used for technical claims.**

| Authority | Role in the book |
|---|---|
| WHATWG HTML and URL standards; IETF HTTP, TLS, DNS, and QUIC specifications | Normative definitions for platform and protocol behavior |
| ECMAScript specification and MDN Web Docs | JavaScript language and browser API behavior, with MDN used for approachable explanations and compatibility context |
| W3C Web Content Accessibility Guidelines (WCAG) 2.2 and WAI-ARIA Authoring Practices | Accessibility outcomes, patterns, testing, and terminology |
| OWASP Top 10:2025, Application Security Verification Standard 5.0, and Web Security Testing Guide | Threat awareness, verifiable security requirements, and testing practice |
| Official Node.js, Express, TypeScript, React, Vite, and PostgreSQL documentation | Version-sensitive implementation guidance |
| ACM/IEEE-CS/AAAI CS2023 | Competency-based outcomes, ethics, security, and professional practice |

Accessibility and security are not chapters that repair an otherwise finished
application. Keyboard use begins with the first link and form. Trust boundaries
begin with the first browser/server diagram. Injection begins with the first
untrusted value. Dependency risk begins with the first package installation.
Authorization begins with the first protected record.

## 4. Evaluation of books and long-form teaching resources

No single commercial book is current and complete enough to serve as the source
of truth for this course. Each of the following has a narrower role.

**Table 3. Roles and limitations of selected long-form resources.**

| Resource | Best use | Editorial caution |
|---|---|---|
| Marijn Haverbeke, *Eloquent JavaScript*, 4th ed. (2024) | Free companion for language, asynchronous programming, browser programming, Node, and substantial exercises | It is a programming book, not a complete accessibility, database, security, or production course |
| Axel Rauschmayer, *Exploring JavaScript (ES2025)* | Precise modern-language reference and optional advanced reading | Too language-focused to define the whole course sequence |
| David Flanagan, *JavaScript: The Definitive Guide*, 7th ed. (2020) | Detailed language, browser, and Node reference for instructors and advanced students | Its edition date requires checking changing APIs against primary documentation |
| Andrew Hoffman, *Web Application Security*, 2nd ed. (2024) | Threat modeling, offense/defense relationships, and advanced security extensions | Security labs must remain ethical, isolated, and mapped to current OWASP requirements |
| Martin Kleppmann and Chris Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (2026) | Advanced reliability, scalability, consistency, and distributed-data reading | Appropriate for extension chapters, not novice database instruction |
| University of Helsinki, *Full Stack Open* | Current exercise design and second-half enrichment | Assumes foundations that this book must teach explicitly |
| Kansas State University, CIS 526 open textbook | A useful Node/SQL/Linux full-stack comparison and openly inspectable teaching model | Its local course choices should be evaluated, not copied wholesale |

Older books can still explain enduring ideas, but code that depends on an
unsupported runtime or obsolete browser practice must never be reproduced merely
because it appears in a respected title. Primary documentation wins any technical
disagreement.

## 5. Essential improvements adopted

The audit resulted in the following non-negotiable improvements:

1. Split the complete book into five parts: foundations, browser programming,
   server and data, production engineering, and advanced systems.
2. Teach the client and server separately before tracing complete full-stack
   features across their trust boundary.
3. Introduce web servers in four passes: observe, consume, build, and operate.
4. Teach native browser and Node mechanisms immediately before the abstraction
   that simplifies them. The student should know what React, Express, and an
   object-relational mapper are doing on the student's behalf.
5. Teach JavaScript before TypeScript, the Document Object Model before React,
   SQL before a query builder or object-relational mapper, and sessions before
   token-based identity.
6. Require accessible, secure, tested behavior in every relevant laboratory.
7. Add server-rendered HTML as an explicit architecture comparison rather than
   implying that every modern application must be a single-page application.
8. Include failure as curriculum: timeouts, malformed responses, race conditions,
   unavailable dependencies, unauthorized requests, broken deployments, and
   recovery evidence.
9. Require output evidence for executable examples. Prefer generated browser
   captures or deterministic textual output, never a decorative screenshot that
   can drift from the code.
10. Keep concepts version-light, pin tested tool versions in configuration, and
    place a technical-review date beside update-sensitive material.
11. Add a diagnostic programming foundations bridge. “Web development from zero”
    and “programming from zero” are different promises; the bridge makes both
    routes honest without sacrificing the computer-engineering depth of the core.

## 6. Gap analysis of the current repository

**Table 4. Gap analysis of the current repository.**

| Area | Current evidence | Required next state |
|---|---|---|
| Web/platform foundations | Chapters 1-3, labs, solutions, quizzes, and figures are present | Preserve and periodically validate; add cross-chapter glossary/index later |
| Browser programming | Chapter 4 and its tested JavaScript laboratory are published | Continue with the Document Object Model, events/forms, asynchronous work, APIs, storage, modules, tooling, and TypeScript |
| Server and APIs | Not yet published | Native Node server concept, Express routing/middleware, validation, error contracts, logs, REST, and OpenAPI |
| Relational data | Not yet published | Modeling, constraints, SQL, joins, parameterization, migrations, transactions, indexes, concurrency, and query plans |
| Identity and security | Mentioned in the roadmap only | Password storage, sessions/cookies, Cross-Site Request Forgery, authorization, OAuth/OpenID Connect concepts, threat models, and negative tests |
| React/application architecture | Not yet published | Components, state, forms, routing, server state, accessibility, performance, and comparison with native/browser and server-rendered approaches |
| Quality and delivery | Build checks exist for the foundation volume | Unit/integration/end-to-end testing, continuous integration, containers, deployment, HTTPS, configuration, observability, and operations runbook |
| Advanced reference | Roadmap only | Clearly optional chapters on real time, server-side rendering, GraphQL, distributed systems, internationalization, progressive web apps, privacy, and WebAssembly |

The current foundation volume is therefore a sound beginning, not yet the complete
reference promised by the final title. Publishing thin placeholder chapters would
hide that fact and reduce quality. Each remaining chapter should be released only
when its prose, lab, complete answers, quiz explanations, code tests, output
evidence, figures, tables, references, and instructor material satisfy the same
contract.

## 7. Source links reviewed

- [Stanford CS142 course description](https://bulletin.stanford.edu/courses/2085161)
- [Harvard CS50 Web](https://cs50.harvard.edu/web/)
- [Carnegie Mellon 17-437/637 syllabus](https://www.cmu-webapps.org/static/index/syllabus.pdf)
- [Cornell INFO 2300, Fall 2025](https://classes.cornell.edu/browse/roster/FA25/class/INFO/2300)
- [University of Washington CSE154](https://courses.cs.washington.edu/courses/cse154/)
- [University of Helsinki Full Stack Open](https://fullstackopen.com/en/)
- [MIT web.lab](https://webdevelopment.mit.edu/schedule/)
- [MDN Curriculum](https://developer.mozilla.org/en-US/curriculum/)
- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/)
- [WHATWG URL Living Standard](https://url.spec.whatwg.org/)
- [IETF HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)
- [IETF TLS 1.3, RFC 9846](https://www.rfc-editor.org/rfc/rfc9846.html)
- [IETF DNS concepts and facilities, RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP ASVS](https://owasp.org/projects/asvs)
- [OWASP Web Security Testing Guide](https://wstg.owasp.org/latest/)
- [Node.js releases](https://nodejs.org/en/about/previous-releases)
- [Express 5 migration guide](https://expressjs.com/en/guide/migrating-5.html)
- [React versions](https://react.dev/versions)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [PostgreSQL transactions tutorial](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [Eloquent JavaScript, 4th edition](https://eloquentjavascript.net/)
- [Kansas State CIS 526 open textbook](https://textbooks.cs.ksu.edu/cis526/index.print.html)

## 8. Editorial conclusion

The promise should not be “complete forever,” because web standards, runtimes,
security threats, and teaching practice continue to change. The defensible promise
is stronger: a comprehensive living reference whose durable explanations remain
stable, whose changing examples are tested and dated, and whose maintenance
process makes obsolescence visible and correctable.
