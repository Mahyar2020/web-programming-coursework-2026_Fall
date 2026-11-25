# Chapter 5 Release Review

Review date: 25 November 2026  
Scope: *The Document Object Model, Events, and Forms* and Week 5 laboratory

## Coverage audit

The chapter follows the approved architecture in `docs/BOOK_ARCHITECTURE.md`.
It introduces the HTML-to-DOM parsing boundary; browser objects and document
readiness; scoped selectors and traversal; safe mutation; attributes versus live
properties; templates; state and rendering; event dispatch and listener
lifetime; event delegation; form controls and `FormData`; native and custom
validation; accessible feedback; and progressive enhancement. Asynchronous
requests, persistent storage, server-side routes, and React are intentionally
left to later chapters, where their prerequisites are taught.

The teaching path begins with a visible source fragment and builds toward the
Campus Hub event explorer. Figure references and captions are chapter-local.
Tables cover browser objects, form serialization, debugging evidence, and the
  glossary. The chapter includes 40 applied exercises with reasoned answers, a
  40-item retrieval quiz, instructor sequencing, and primary standards and
university reading.

## Research basis

- WHATWG DOM and HTML Living Standards define current browser behavior.
- MDN material supports detailed teaching explanations of DOM events, event
  bubbling, and constraint validation.
- W3C Web Accessibility Initiative guidance informs error and status feedback.
- Stanford CS142 and University of Washington CSE 154 materials provide
  university sequencing examples for DOM, events, forms, and validation.

Standards are the technical authority; course notes inform sequencing and
practice. The source chapter includes direct links and annotations.

## Laboratory and evidence

`labs/starters/week-05/` and `labs/solutions/week-05/` use the same Campus Hub
event data. The lab asks students to inspect the expected DOM contract, build a
pure filter model, render safe text, delegate save actions, preserve keyboard
focus, display an empty state, and collect browser evidence. The solution has a
readable static event list and an honest `<noscript>` explanation. Its empty
form action is explicitly described as a teaching limitation; the chapter does
not claim that the static file server performs server-side filtering.

The solution's pure model has eight automated tests. Figure 5.8 is a browser
output capture of the completed interface. Conceptual diagrams are generated
separately by the PDF builder.

The 25 November expansion adds evidence-led DOM read/decide/write batching,
`MutationObserver`, light and shadow DOM, event retargeting, custom-element
lifecycle, input-independent event choice, form ownership, reset and `formdata`
behavior, submission encodings, and file-input trust boundaries. Figures
5.9-5.11 and Table 5.4 make those relationships explicit. Asynchronous network
requests remain in Chapter 6.

## Publication checks

- `npm test`: passed on 25 November 2026.
- `npm run pdf`: passed; generated the current English edition.
- `npm run pdf:verify`: passed; 284 A4 pages, 1,405 hyperlink annotations.
- `npm run pdf:tr` and `npm run pdf:tr:verify`: passed; 247 A4 pages and 496
  hyperlink annotations.
- All 284 English pages and 247 Turkish pages were rendered after the final
  builder changes and inspected in
  page contact sheets. Chapter 5 pages were also rendered at print scale and
  inspected individually. The review found and corrected an overlong Figure
  5.3 caption and low-contrast table-header text. The final rebuild shows the
  caption within the figure margins and the table headings in high-contrast
  white on navy; no clipping or collision was visible in the reviewed pages.

## Turkish edition status

The editable Turkish Chapter 5 source mirrors the English chapter's sections,
figures, tables, laboratory, exercises, worked answers, quiz, and references.
`scripts/build_turkish_pdf.py` renders that source with Turkish figure labels,
adds a linked contents continuation and Chapter 5 bookmark, and assembles it
after the 214-page legacy translated checkpoint. Earlier translated pages still
predate the editable source workflow; Chapter 5 is now source-driven and
repeatable without editing the generated PDF directly.
