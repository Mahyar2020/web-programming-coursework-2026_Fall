# Chapter 2 Release Review

Review date: **18 November 2026**  
Decision: **PASS - ready to support Chapter 3**

## Release judgment

The November 2026 cross-chapter audit rechecked the HTML, form, and accessibility
dependencies used by Chapters 3 and 4. The semantic document and browser parsing
model remains complete for the JavaScript transition; dynamic DOM behavior stays
in Chapter 5 where it can be taught with events and state.

Chapter 2 now supplies the HTML and accessibility knowledge that Chapter 3 may
safely assume. A student who completes the reading, laboratory, exercises, and
retrieval quiz has encountered basic HTML syntax; document metadata; text,
landmark, link, image, media, and table semantics; native form controls; GET and
POST meaning; successful-control rules; URL-encoded and multipart submission;
browser and server validation boundaries; accessible names, descriptions, roles,
states, keyboard operation, error recovery, and layered accessibility evidence.

The gate does not claim that a single chapter replaces the living HTML element
reference or the complete Web Content Accessibility Guidelines (WCAG). It means
that no unresolved prerequisite should force Chapter 3 to teach missing HTML
syntax or semantic structure while explaining Cascading Style Sheets (CSS).

## Comparison basis

The audit compared this chapter with the current WHATWG HTML Living Standard,
MDN's core semantic-HTML and structuring-content curriculum, WCAG 2.2, the W3C
Web Accessibility Initiative forms tutorial and evaluation guidance, Harvard
CS50 Web Programming, University of Washington CSE 154, Stanford CS142, and the
2025 sixth edition of Jennifer Niederst Robbins's *Learning Web Design*. Form
design and component decisions were also checked against *Form Design Patterns*,
*Inclusive Components*, and *Web Accessibility Cookbook*.

## Coverage matrix

| Area | Evidence in Chapter 2 | Decision |
|---|---|---|
| HTML syntax | Tags versus elements, attributes, quoted values, Boolean presence, void elements, nesting, whitespace, character references, comments, content models, and validation | Complete for the foundation sequence |
| Document metadata | Doctype, language, direction, encoding, viewport, description, title, visible heading, language changes, and bidirectional isolation | Complete |
| Document structure | Heading hierarchy, landmarks, multiple-region names, skip links, current-page state, native-first ARIA policy | Complete |
| Text and embedded content | Rhetorical text, lists, quotations, code, figures, dates, abbreviations, images, audio/video alternatives, and intrinsic image dimensions | Complete for prerequisites |
| Data tables | Captions, row/column headers, scope, groups, explicit header associations, simplification decision | Complete for foundation and intermediate tables |
| Form controls | Labels, names, descriptions, grouping, input-type decisions, mobile hints, datalist, select, textarea, button types, and non-nesting rule | Complete for native HTML forms |
| Submission contract | Action, GET/POST meaning, successful controls, disabled/readonly behavior, URL encoding, multipart file upload, and trust boundary | Complete for client markup |
| Validation and recovery | Native constraints, server repetition, required/optional communication, failure title, summary, linked field errors, invalid state, preserved values, and focus plan | Complete for pre-JavaScript forms |
| Accessibility model | Source, DOM, accessibility tree, name/description/role/state, label in name, keyboard operation, hiding behavior, WCAG POUR, conformance levels | Complete for prerequisites |
| Evaluation | Source validation, automated checks, keyboard, zoom/reflow, accessibility-tree inspection, assistive technology, and representative-user evidence | Complete as an introductory layered method |
| Practice and assessment | Tested laboratory, observation record, fourteen transfer exercises, fully reasoned answers, debugging clinic, and twenty-question retrieval quiz | Release-ready |

## Deliberate later placement

- Visual focus indicators, target sizing, layout, typography, responsive images,
  and reflow implementation belong in Chapter 3 because they require CSS.
- Dynamic form events, live validation, DOM mutation, and status announcements
  belong in the browser-programming chapters because they require JavaScript.
- Request parsing, storage, file scanning, database constraints, and durable error
  responses belong in the server and data chapters.
- Cross-Site Request Forgery protection, authentication, authorization, content
  security policy, upload isolation, and session security belong in the security
  sequence, where the complete threat model can be taught.
- Custom composite widgets belong after students understand events, state, focus
  management, and the relevant ARIA Authoring Practices pattern.

These are prerequisite boundaries, not omissions. Chapter 2 states each boundary
where a novice might otherwise mistake client markup for complete application
behavior.

## Readiness condition for Chapter 3

Chapter 3 may now assume that students can construct and validate a meaningful
un-styled document, identify the native behavior that CSS must preserve, navigate
the page with a keyboard, and explain the accessibility evidence. If a student
cannot pass the Chapter 2 self-check or laboratory evidence review, the correct
remedy is targeted Chapter 2 practice before layout work begins.

## Maintenance conditions

Before each academic year, maintainers should check the HTML Living Standard,
MDN curriculum, WCAG errata, WAI tutorials, browser accessibility-tree tooling,
and form-control interoperability. Examples should be retested in the course's
supported browser and Node.js versions. Release approval describes the reviewed
edition; it is not a promise that a living platform can never change.
