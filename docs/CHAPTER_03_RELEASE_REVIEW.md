# Chapter 3 Release Review

Review date: **2 September 2026**  
Decision: **PASS - ready to support Chapter 4**

## Release judgment

Chapter 3 now supplies the Cascading Style Sheets (CSS) knowledge that Chapter 4
may safely assume before introducing browser programming with JavaScript. A
student who completes the reading, guided laboratory, exercises, and retrieval
quiz has encountered CSS syntax and loading; selector matching; the complete
practical cascade; inheritance and custom properties; value processing; color
and typography; the box model, intrinsic sizing, normal flow, overflow,
positioning, and stacking; Flexbox and Grid; viewport and container queries;
responsive media; preference-sensitive and accessible presentation; maintainable
stylesheet architecture; and evidence-driven debugging with browser developer
tools.

The gate does not claim that one chapter replaces the CSS specifications or a
living browser-compatibility reference. It means that no unresolved foundation
should force Chapter 4 to repair missing CSS concepts while students are learning
JavaScript values, control flow, functions, events, and Document Object Model
(DOM) interaction.

## Comparison basis

The audit compared this chapter with the W3C CSS Snapshot 2026; MDN's current CSS
fundamentals, text styling, and layout curricula; the W3C CSS Cascading and
Inheritance, Selectors, Flexbox, Grid, and Containment specifications; Web Content
Accessibility Guidelines (WCAG) 2.2; Harvard CS50 Web Programming; Stanford
CS142; Jennifer Niederst Robbins's 2025 sixth edition of *Learning Web Design*;
and Keith J. Grant's second edition of *CSS in Depth*. The external materials
were used to test scope, sequencing, terminology, misconceptions, and practice
coverage rather than to imitate their prose.

## Coverage matrix

| Area | Evidence in Chapter 3 | Decision |
|---|---|---|
| Language and loading | Rule anatomy, declarations, parsing recovery, at-rules, shorthands, external/internal/inline CSS, resolved stylesheet requests, user-agent styles, and restrained resets | Complete for foundation work |
| Selectors and cascade | Type, class, ID, attribute, combinator, pseudo-class, pseudo-element, functional selector, relevance, origin and importance, layers, specificity, scoping proximity, and order | Complete practical model with advanced signposts |
| Inheritance and reusable values | Inherited versus non-inherited properties, `initial`, `inherit`, `unset`, `revert`, `revert-layer`, custom-property scope, fallback, and invalid-value behavior | Complete for maintainable introductory systems |
| Values and presentation | Specified/computed/used values, absolute and relative units, viewport units, `min()`, `max()`, `clamp()`, color and contrast, typography, web-font resilience, backgrounds, borders, shadows, and form controls | Complete for the chapter's page shell |
| Boxes and flow | Content, padding, border, margin, `box-sizing`, normal flow, intrinsic contributions, minimum and maximum constraints, replaced elements, aspect ratio, logical axes, margin collapse, and overflow diagnosis | Complete foundation and intermediate model |
| Positioning and depth | Static, relative, absolute, fixed, sticky, containing blocks, `z-index`, stacking contexts, and common trapping conditions | Complete prerequisite model |
| Layout systems | Layout-choice criteria, Flexbox axes and sizing, Grid tracks and placement, explicit/implicit grids, auto-placement, subgrid signpost, gaps, and source-order preservation | Complete for responsive component and page layout |
| Responsive design | Viewport metadata dependency, content-driven breakpoints, media queries, container queries, query units, responsive media, reduced motion, color preferences, forced colors, zoom, and reflow | Complete for a robust responsive shell |
| Accessible presentation | Visible focus, target size and spacing, text spacing, contrast, non-color cues, hiding mechanisms, preferences, logical order, and keyboard verification | Complete for CSS responsibilities |
| Architecture and compatibility | Tokens, cascade layers, low-specificity composition, nesting boundaries, progressive enhancement, and `@supports` | Complete for maintainable course-scale work |
| Debugging evidence | Network, Elements/Inspector, matched rules, cascade winner, Computed values, box model, Flexbox/Grid overlays, exact viewport tests, long content, direction, zoom, and overflow tracing | Complete repeatable workflow |
| Practice and assessment | Tested Campus Hub laboratory, authentic wide and narrow output screenshots, observation record, sixteen transfer exercises with fully reasoned answers, debugging clinic, twenty-question retrieval quiz with explanations, glossary, and instructor guide | Release-ready |

## Deliberate later placement

- JavaScript-driven class changes, inline-style APIs, the CSS Object Model
  (CSSOM), event-responsive styling, and live interface state belong in the
  browser-programming chapters, after students understand JavaScript and the DOM.
- Transforms, transitions, keyframe animation, animation performance, and
  view-transition orchestration deserve a later interaction and performance
  treatment; Chapter 3 establishes reduced-motion policy and cascade placement.
- Large-scale design systems, theming pipelines, CSS Modules, CSS-in-JS, utility
  frameworks, and component-library governance belong after students can judge
  the platform features those abstractions organize.
- Rendering-pipeline internals, containment for performance, critical CSS,
  font-loading optimization, and Core Web Vitals belong in the browser and
  production-performance sequence.
- Print styles, paged media, and specialized publication CSS belong in an
  appendix or elective extension rather than blocking ordinary screen layout.

These are sequencing decisions, not unexplained omissions. Chapter 3 introduces
the relevant boundary wherever a novice might otherwise confuse static CSS with
JavaScript behavior or production optimization.

## Readiness condition for Chapter 4

Chapter 4 may now assume that students can connect and verify a stylesheet,
predict which declaration wins, reason about generated boxes and constraints,
choose Flexbox or Grid from the relationship being expressed, produce an
accessible responsive page shell, and use developer tools to distinguish a
loading failure from a matching, cascade, computed-value, or layout failure.
Students who cannot yet produce the laboratory evidence should repeat the
specific checkpoint before adding JavaScript, because scripting an unexplained
layout defect usually makes diagnosis harder.

## Maintenance conditions

Before each academic year, maintainers should check the current W3C CSS snapshot,
the maturity and interoperability of the modules used in examples, MDN browser
compatibility data, WCAG errata and supporting techniques, operating-system
preference modes, and browser developer-tool interfaces. The responsive output
screenshots and automated foundation checks should be regenerated with the
course's supported browser and Node.js versions. Release approval describes this
reviewed edition; CSS remains a living platform.
