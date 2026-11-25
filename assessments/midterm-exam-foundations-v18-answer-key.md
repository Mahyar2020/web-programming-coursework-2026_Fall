# Midterm Examination - Instructor Answer Key

**Source scope:** *Web Programming: From the Platform to Production - Foundations Edition, Revised v18*  
**Questions:** 40  
**Scoring:** 2.5 points each; 100 points total

## Assessment Blueprint

| Content area | Questions | Count |
|---|---:|---:|
| Workstation and development workflow | 1-4 | 4 |
| How the Web works | 5-16 | 12 |
| Semantic HTML and accessible forms | 17-28 | 12 |
| CSS, layout, and responsive design | 29-40 | 12 |

| Cognitive demand | Questions | Count |
|---|---|---:|
| Foundational understanding | 1, 3, 5, 6, 8, 17, 19, 22, 29, 33 | 10 |
| Applied understanding | 2, 4, 7, 9, 11, 13, 14, 18, 20, 21, 23, 24, 26, 27, 30, 31, 32, 35, 36, 38 | 20 |
| Analysis and diagnostic reasoning | 10, 12, 15, 16, 25, 28, 34, 37, 39, 40 | 10 |

The difficulty mix is 25% foundational, 50% applied, and 25% analysis/diagnosis. Correct answer positions are balanced: A, B, C, D, and E each occur eight times.

## Key and Rationales

| Q | Key | Rationale |
|---:|:---:|---|
| 1 | B | Readiness needs executable version evidence and successful use in the actual course workflow; an installer or shortcut proves little. |
| 2 | D | The error path shows where npm looked. Project commands must run from the repository root that contains `package.json`. |
| 3 | A | Save writes the working file, commit records selected content locally, and push transfers commits to the configured remote. |
| 4 | E | Network may be empty because recording began after the request. Reloading while the panel is open captures the exchange. |
| 5 | C | The Internet is the underlying network of networks; the Web is an application that uses it. |
| 6 | A | The fragment is interpreted by the client and is not normally included in the HTTP request target. |
| 7 | D | An origin is the tuple of scheme, host, and effective port; path, query, and fragment do not define it. |
| 8 | B | DNS supplies address information for a hostname; it does not fetch, render, encrypt, or certify the page. |
| 9 | E | A visible error body and a `404` status are both parts of a server response. |
| 10 | C | HTTPS protects data in transit and authenticates the certified endpoint, not the truth or defect-free quality of the application. |
| 11 | A | The initial HTML can reference multiple resources, each potentially requiring a separate request. |
| 12 | D | `200 OK` is protocol evidence about one request; it does not establish semantic, accessibility, data, or interface correctness. |
| 13 | B | HTTP does not inherently retain conversational state between requests; applications add continuity with mechanisms such as cookies or tokens. |
| 14 | E | An HTTP URL and a Network entry containing method, status, and response fields distinguish HTTP serving from a direct `file:` load. |
| 15 | C | The DOM is the live tree produced by parsing and can include repairs and script-driven changes not present in the source text. |
| 16 | A | `<h1>` supplies the requested level-one heading, while `<a href="events.html">` creates a functioning native link to the resource. |
| 17 | D | Semantic HTML communicates roles and relationships, independently of visual styling. |
| 18 | B | Heading levels express structural hierarchy; CSS controls visual size and spacing. |
| 19 | E | An `article` is suitable for a composition that remains independently meaningful or reusable. |
| 20 | C | A link navigates to a resource; a button performs an action. Appearance does not determine semantics. |
| 21 | A | Placeholder text disappears and is not a dependable persistent label or accessible name. |
| 22 | D | A successful named control contributes a key-value pair in submitted form data; `name` supplies the key. |
| 23 | B | The client is outside the server's trust boundary and can be bypassed or modified. |
| 24 | E | An empty alternative intentionally prevents a decorative or redundant image from adding noise to the accessibility experience. |
| 25 | C | `required` is Boolean: its presence means true, even when its written value is the string `false`. |
| 26 | A | Student numbers and postal codes are identifiers, so quantity semantics and numeric normalization can damage valid formatting. |
| 27 | D | Disabled controls are ordinarily omitted; a named read-only text control is ordinarily still submitted. |
| 28 | B | Accessible recovery combines a failure-specific title, navigable summary, field associations, state/focus management, and preservation of safe valid input. |
| 29 | E | The cascade uses an ordered decision process involving origin, importance, layers, specificity, and source order. |
| 30 | C | Under `content-box`, the outer size is 300 + 40 padding + 4 border = 344 pixels. |
| 31 | A | `border-box` includes padding and border inside the declared dimensions; it improves predictability but does not prevent every overflow. |
| 32 | D | Flexbox models one primary axis and `flex-wrap` supports resilient wrapping of navigation items. |
| 33 | B | Grid coordinates rows and columns, making it appropriate for two-dimensional card layouts. |
| 34 | E | A container query responds to the space allocated by a component's container rather than the overall viewport. |
| 35 | C | Content-driven breakpoints respond to the space a real layout relationship needs, not to a transient device catalogue. |
| 36 | A | Visual reordering does not necessarily change DOM-based reading and keyboard focus sequences. |
| 37 | D | `opacity: 0` hides pixels but can leave the element in layout and potentially focusable or interactive. |
| 38 | B | Focus must be visibly indicated and remain unobscured under actual keyboard navigation and responsive conditions. |
| 39 | E | `min(100%, 20rem)` lets the card fit a narrower container while retaining the intended maximum. |
| 40 | C | The evidence-led sequence checks loading, matching, cascade/computation, and layout assumptions before changing code. |

## Compact Key

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | E | C | A | D | B | E | C |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | B | E | C | A | D | B | E | C |

| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | B | E | C | A | D | B | E | C |

| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | B | E | C | A | D | B | E | C |

## Instructor Notes

- Questions 10, 12, 15, 25, 28, 34, 37, and 40 are especially useful for distinguishing memorized terminology from operational understanding.
- Accept only one response per question unless the institution's standard examination policy states otherwise.
- Keep the answer-key file out of student-facing distribution channels.
- If the taught scope excluded workstation orientation, Questions 1-4 can be removed and the remaining 36 questions rescaled. The current version intentionally assesses the complete content of revised v18.
