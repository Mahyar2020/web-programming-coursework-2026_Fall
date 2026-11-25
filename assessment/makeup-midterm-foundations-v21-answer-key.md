# Makeup Midterm Examination - Instructor Answer Key

**Scope:** Sessions 0-3 of *Web Programming: From the Platform to Production*, Foundations Edition v21  
**Questions:** 40  
**Scoring:** 2.5 points each; 100 points total

## Assessment blueprint

| Content area | Questions | Count |
|---|---:|---:|
| Workstation and development workflow | 1-4 | 4 |
| How the Web works | 5-16 | 12 |
| Semantic HTML and accessible forms | 17-28 | 12 |
| CSS, layout, and responsive design | 29-40 | 12 |

Correct positions are balanced: A, B, C, D, and E each occur exactly eight times.

## Key and rationales

| Q | Key | Rationale |
|---:|:---:|---|
| 1 | C | Saving, served-directory identity, and a fresh Network request test the actual edit-to-browser path without unrelated changes. |
| 2 | A | The server terminal must remain occupied; a second terminal at the repository root can run tests concurrently. |
| 3 | E | Inspection, intentional staging, a coherent commit, and push preserve a reviewable local and remote history. |
| 4 | B | Since `package.json` is present, its `scripts` object is the authoritative evidence for the exact available command name. |
| 5 | D | `/calendar` is the path and `labs` is the fragment; `week=4` is the query. |
| 6 | B | An address answer proves name resolution completed; timeout points to a later reachability or connection boundary. |
| 7 | A | IPv4 dotted-decimal notation has four decimal octets, each from 0 through 255. |
| 8 | E | IPv6 permits one `::` to compress consecutive zero-valued 16-bit groups. |
| 9 | C | Status 301 and `Location` express redirection and commonly cause a follow-up request. |
| 10 | D | IP, transport, and HTTP cooperate with distinct network, end-to-end, and application responsibilities. |
| 11 | B | HTTPS with omitted port uses effective port 443, so scheme, host, and effective port match. |
| 12 | D | Resource requests have independent outcomes: the document succeeded while the stylesheet was not found. |
| 13 | A | `localhost` denotes the requesting host, but a process must still listen on the requested port. |
| 14 | C | Headers describe/control the response; the optional body carries its representation. |
| 15 | E | Origin uses scheme, host, and effective port; the different hosts make these origins different. |
| 16 | B | The sequence correctly orders name resolution, secure connection establishment, HTTP exchange, parsing, and rendering. |
| 17 | C | One `h1` states the page topic and peer `h2` headings express equal subsections. |
| 18 | E | A native button represents an in-page action and already supplies keyboard activation semantics. |
| 19 | E | Matching `for` and `id` associate the visible label, while `name` supports form data. |
| 20 | A | For a linked functional image, alternative text should express the link's purpose rather than visual decoration or filename. |
| 21 | D | `main` identifies the document's dominant, non-repeated content. |
| 22 | C | Header cells and appropriate scope relationships expose table structure instead of relying on visual bolding. |
| 23 | B | GET form data is ordinarily encoded into the URL query as successful-control name-value pairs. |
| 24 | E | A fieldset and legend name the group; one shared name gives radio buttons mutually exclusive form behavior. |
| 25 | C | Declared document and passage languages support pronunciation, processing, and language-aware behavior. |
| 26 | A | Complex instructional meaning needs concise identification plus a nearby detailed equivalent, not a vague filename or color-only code. |
| 27 | D | Native types improve input and basic validation, but they do not prove real-world truth or server authorization. |
| 28 | B | Clearing work and giving only a distant color-coded generic error provides neither identification nor an efficient recovery path. |
| 29 | B | With other cascade factors equal, the selector containing a type plus class is more specific than one class. |
| 30 | D | `color` is inherited by default, unlike many box and layout properties. |
| 31 | A | Auto inline margins share remaining inline space and therefore center a constrained block. |
| 32 | C | A flex item's automatic minimum can preserve long content; `min-width: 0` permits intended shrinking. |
| 33 | E | `auto-fit` creates available tracks and `minmax` combines a safe minimum with flexible `1fr` growth. |
| 34 | A | Absolutely positioned offsets resolve against the applicable containing block, often made by the nearest positioned ancestor. |
| 35 | D | The media feature respects a user preference to reduce nonessential motion and possible discomfort. |
| 36 | C | Container queries respond to allocated component space rather than only the global viewport. |
| 37 | E | A rigid viewport height can conflict with content growth and changing mobile viewport chrome; the alternative must match the layout need. |
| 38 | A | `:focus-visible` targets focus when the browser determines a visible indicator is appropriate, commonly for keyboard interaction. |
| 39 | D | A `rem` uses the root font size: 2 × 18 pixels equals 36 pixels. |
| 40 | B | Evidence-led debugging identifies the overflowing element and cause before applying a targeted, testable repair. |

## Compact key

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | E | B | D | B | A | E | C | D |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | E | B | C | E | E | A |

| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | C | B | E | C | A | D | B | B | D |

| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | E | A | D | C | E | A | D | B |

## Instructor notes

- Keep this file separate from student distribution.
- The English and Turkish examinations are aligned item by item; do not combine both languages into one paper unless bilingual presentation is an approved accommodation.
- Questions 6, 10-12, 15-16, 26-28, 32-37, and 40 particularly assess reasoning rather than isolated recall.
- The makeup form is equivalent in scope and scoring to the original midterm but uses new scenarios and wording.
