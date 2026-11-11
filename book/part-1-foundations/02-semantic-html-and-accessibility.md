# Session 2 - Semantic HTML and Accessible Forms

**Essential question:** How can one HyperText Markup Language (HTML) document
remain understandable to people, browsers, search engines, and assistive
technology before any Cascading Style Sheets (CSS) or JavaScript is added?

## Session map

Table 2.1 summarizes the preparation, teaching time, expected artifact, and
evidence for this session.

**Table 2.1 - Session scope, preparation, and evidence**

| Item | Plan |
|---|---|
| Audience | Students who completed Session 1; no prior accessibility experience is assumed |
| Preparation | Complete the workstation orientation; this session repeats the edit-save-serve-reload workflow before introducing HTML concepts |
| Contact time | Approximately 3 hours lecture/workshop plus a 2-hour laboratory |
| Independent work | Approximately 3 hours |
| Main artifact | An accessible event-submission page for Campus Hub |
| Assessment | Validator evidence, keyboard test, semantic rationale, exercises, and quiz |

## Learning outcomes

After this session, you should be able to:

1. locate the Campus Hub HTML source, edit and save it in a code editor, serve
   the correct directory, and verify the rendered output in a browser;
2. distinguish an element, tag, attribute, content, void element, Boolean
   attribute, and character reference in conforming HTML syntax;
3. explain why HTML communicates meaning rather than merely arranging boxes;
4. establish document language, direction, title, encoding, description, and
   viewport metadata;
5. choose headings and landmark elements from the document's information
   structure;
6. write useful text, links, images, lists, tables, dates, and media alternatives;
7. construct a form whose controls have names, labels, descriptions, groups, and
   appropriate native types;
8. predict which controls and values a form will submit with `get` or `post`,
   including the encoding required for a file upload;
9. distinguish native browser constraint validation from complete application
   validation;
10. design labels, instructions, error summaries, and field-level errors that
   support recovery;
11. describe how source HTML contributes to the DOM and accessibility tree;
12. operate and inspect a page using only a keyboard; and
13. combine conformance, automated, keyboard, zoom, assistive-technology, and
    user evidence when evaluating accessibility.

## Before the concepts: find, edit, and view Campus Hub

HTML does not require a special visual design program. An HTML document is a
plain-text file whose name normally ends in `.html`. You write the source in a
text editor, save the file, and ask a browser to load it. The browser reads the
markup and produces the visible page. The editor and browser therefore show two
views of the same work: the editor shows instructions; the browser shows the
result of interpreting those instructions.

### Find the correct Campus Hub file

Your personal repository, created from the
[Fall 2026 coursework template](https://github.com/Mahyar2020/web-programming-coursework-2026_Fall),
contains one student working file for each laboratory. In Session 2, edit
`labs/week-02/index.html`. It already contains the outer document and the heading
**Submit a campus event**, but its comments mark work that has not yet been
completed. The complete reference answer appears in Appendix A of this book; it
is intentionally absent from the private student repository.

The repeated filename `index.html` is intentional. Web servers commonly treat
`index.html` as the default document for a directory. The folders distinguish
the files. A tab that says only `index.html` is not enough evidence; read its
folder path in the Explorer panel or editor breadcrumb.

The PDF you are reading is not the website source. Editing the PDF cannot change
the Campus Hub page. The source to edit in this session is:

```text
web-programming-coursework-2026_Fall-YOUR_STUDENT_NUMBER
  labs
    week-02
      index.html       <- edit this file
```

### Use a plain-text code editor

Any plain-text editor can write HTML, including Notepad, but this course uses
Visual Studio Code (VS Code) because it shows folders, line numbers, syntax
coloring, an integrated terminal, and useful error indicators. Do not use a word
processor such as Microsoft Word: a word processor can add formatting data that
is not HTML source.

The tools have distinct jobs:

- **VS Code Explorer** shows the repository's folders and files.
- **VS Code editor** is where you type and save HTML source.
- **Terminal** runs the local server and other development commands.
- **Browser** requests the saved file and renders the page.
- **Browser developer tools** reveal the request, parsed Document Object Model
  (DOM), accessibility information, and other evidence.

Open the project and the correct file step by step:

1. Start VS Code.
2. Choose **File > Open Folder**.
3. Select your outer `web-programming-coursework-2026_Fall-...` folder, the one
   containing `package.json`, `labs`, and `scripts`.
4. In the Explorer panel, expand `labs`, then `week-02`.
5. Select `index.html`. Confirm that the breadcrumb or path includes
   `labs > week-02 > index.html`.
6. If the editor shows a preview rather than editable text, right-click the file,
   choose **Open With**, and select **Text Editor**.

### Make one visible change and save it

Find this heading in the starter:

```html
<h1>Submit a campus event</h1>
```

On the next line, add a paragraph:

```html
<p>This page is being edited in Visual Studio Code.</p>
```

The opening tag `<p>` begins a paragraph, the sentence is its text content, and
the closing tag `</p>` ends it. Indent the paragraph to the same level as the
nearby heading because both are children of `main`. Indentation helps people read
the source; the tags establish the actual structure.

Press `Ctrl+S` on Windows or Linux, or `Command+S` on macOS. The small unsaved
indicator on the editor tab should disappear. Saving writes the change to disk;
it does not automatically reload every browser.

### Start the local server and open the browser output

Open **Terminal > New Terminal** in VS Code. The prompt must be at the repository
root. On Windows Command Prompt, verify the location with:

```text
dir package.json
npm run serve:week02
```

On PowerShell, `Get-Item package.json` provides the same proof. On macOS or Linux,
use `ls -l package.json` before the npm command. A successful server prints lines
with this meaning:

```text
Serving ...\labs\week-02
Open http://localhost:8000/
Press Ctrl+C to stop.
```

Leave that terminal running. It is now the server terminal and will not display
a new prompt until the server stops. Open a browser, put the following plain
address in the address bar, and press Enter:

```text
http://localhost:8000/
```

Do not type the address into the terminal. In the browser, the starter should
show **Submit a campus event** and the paragraph you added. The page looks plain
because Session 2 intentionally uses no Cascading Style Sheets (CSS). Plain
presentation is not a failure; it lets you inspect the HTML structure before
styling is introduced.

Each time you change the source, repeat this short cycle:

1. edit `labs/week-02/index.html` in VS Code;
2. save the file;
3. return to the browser; and
4. reload with `Ctrl+R`, `F5`, or the browser's reload button.

Figure 2.1 shows the complete path. The arrows represent steps used together,
not alternative programs: VS Code saves the file, the Node.js server reads it
when the browser sends an HTTP request, and the browser parses and renders the
response.

<!-- figure:html-edit-preview-workflow -->

The supplied server does not provide automatic live reload. If the old page
remains visible, first confirm that the editor tab is saved, then reload the
browser. Also confirm that the server's `Serving` line ends in
`labs\week-02`. If you edit a different copy of `index.html`, reloading
this address cannot display that other file.

A real browser screenshot later in this session shows the completed Week 2
solution. Your starter will contain fewer controls until you build them during
the laboratory, so do not expect it to match that completed page immediately.

### Read the evidence when the result differs

A browser page and an error message are different kinds of evidence:

- If **Submit a campus event** appears, the browser reached the correct starter.
- If the page loads with status `200 OK` but your new paragraph is absent, the
  likely causes are an unsaved editor tab, a missing reload, or editing a
  different `index.html`.
- If the browser shows an almost empty page, open developer tools, inspect the
  `body`, and read the server's `Serving` path. You may be serving an intentionally
  incomplete starter from another week.
- If the browser says **This site can't be reached**, no server is responding at
  that address and port. Return to the server terminal.
- If the browser receives `404 Not Found`, the server responded, but the requested
  path did not identify an available file.

The browser's **Elements** or **Inspector** panel shows the parsed DOM, not an
editable replacement for the saved source file. Temporary edits made there are
useful experiments, but they disappear on reload. Make durable corrections in
the VS Code file and save them.

## 1. Begin with the user task

Imagine an event form that looks polished. Each field is represented by a pale
rectangle. Placeholder text says “Name,” “Date,” and “Email.” Clicking the final
rectangle submits the form. A mouse user with good vision may complete it. A
keyboard user cannot see where focus has moved. A screen-reader user hears “edit
text, blank” three times. When a value is rejected, the border becomes red but no
message explains why.

The page has a visual arrangement, but it does not yet have a reliable interface.
Accessibility is not an optional decoration for a completed design. It is the
quality of the relationships, names, states, and interactions that the system
offers to different users and technologies.

Before reading further, write a short prediction:

- Which information would remain if all CSS disappeared?
- Which operations can be completed without a mouse?
- What name would assistive technology announce for each control?
- How would a person know why submission failed?

These questions turn accessibility from a vague virtue into observable
engineering behavior.

## 2. HTML is a language of meaning

HTML elements describe what content is and how pieces relate. A heading introduces
a section. A list groups related items. A button represents an action. A link
navigates to a resource. A form control accepts input. Browsers attach behavior
and accessibility semantics to these elements.

It is technically possible to make a `div` look like a button. Appearance does
not give it keyboard behavior, an accessible role, a disabled state, or activation
semantics. Recreating all of that correctly is unnecessary when the native
`button` element already expresses the concept.

```html
<button type="submit">Publish event</button>
```

The principle is simple: use the element whose meaning matches the task. Use
generic containers such as `div` and `span` when no more specific element applies.
Figure 2.2 shows how semantic landmark elements identify regions by purpose.

<!-- figure:semantic-landmarks -->

The same semantic document should not become a separate “accessible version.”
As Figure 2.3 illustrates, its structure can support visual presentation,
keyboard operation, assistive technology, and different viewport sizes from one
shared source.

<!-- media:semantic-accessibility -->

### 2.1 Read the syntax before choosing the element

HTML is written as text, but its punctuation has grammatical meaning. Consider
one complete anchor element:

```html
<a class="event-link" href="/events/robotics">Robotics event</a>
```

The opening tag begins with `<a` and ends with `>`. The closing tag is `</a>`.
Together with the text between them, they form the **element**. `class` and
`href` are **attributes** in the opening tag. Each attribute has a name and a
quoted value. “Robotics event” is the element's text content. A tag is markup at
an element boundary; it is not a synonym for the complete element.

Figure 2.4 labels these parts and shows their contribution to the parsed element.
The browser does not display the tags as prose. It parses them into a Document
Object Model (DOM) node with properties, content, and relationships.

<!-- figure:html-anatomy -->

Most elements have an opening tag, content, and a closing tag. Elements must be
properly nested: close the most recently opened child before closing its parent.

```html
<!-- Conforming nesting -->
<p>Read the <strong>important guidance</strong> first.</p>

<!-- Overlapping elements: do not write this -->
<p>Read the <strong>important guidance</p></strong>
```

Browsers apply error-recovery rules to malformed HTML, but recovery is not proof
that the source expresses the intended tree. A different error or context can
produce a different DOM. Write conforming source, validate it, and inspect the
constructed DOM when the result is surprising.

**Void elements** cannot contain child content and do not have closing tags.
Common examples are `img`, `input`, `meta`, `link`, `br`, `hr`, and `source`.
Write `<img src="map.png" alt="Campus map">`, not
`<img>Campus map</img>`. A trailing slash in `<img ... />` is tolerated in HTML
syntax but does not close the element in the XML sense and is not required.

An attribute normally has a quoted value. Consistent double quotes prevent spaces
or punctuation from being misread as new attributes. A **Boolean attribute** is
true when present and false when absent. Therefore, `required="false"` still
makes a control required because the attribute is present. Write `required` to
turn it on and omit the attribute to turn it off.

Whitespace usually collapses in ordinary text, so several spaces do not create a
layout system. The `pre` element preserves relevant preformatted whitespace.
When `<`, `>`, or `&` must appear as text rather than markup, use a character
reference such as `&lt;`, `&gt;`, or `&amp;`. Comments use
`<!-- explanation -->`; comments are delivered to the client and must never
contain passwords, tokens, private notes, or server-only information.

Global attributes can occur on many elements, but they have different jobs:

- `id` is a document-wide unique identifier used by fragments, labels, scripts,
  and accessibility relationships;
- `class` assigns one or more reusable classifications for CSS and scripts; it
  supplies no user-facing semantics by itself;
- `data-*` stores application-specific data for scripts; it is not a substitute
  for visible content or a standard semantic attribute;
- `lang`, `dir`, `hidden`, `title`, and `tabindex` affect language, direction,
  exposure, advisory information, or focus behavior and must be used deliberately.

HTML also defines **content models**: rules about which children and descendants
are permitted. A `ul`, for example, represents a list whose direct children are
`li` elements. A `p` cannot contain another paragraph. A form must not contain a
nested form. Memorizing every rule is unnecessary; learn to consult the current
element reference and use the [W3C Nu HTML Checker](https://validator.w3.org/nu/)
as one source of conformance evidence. A validator can find a duplicate `id` or
forbidden child, but it cannot decide whether a heading or alternative text
communicates the correct meaning.

### 2.2 Document-wide meaning begins in `html` and `head`

Before the first visible heading, the document already communicates important
information. The `doctype` selects the modern HTML parsing mode. The `lang`
attribute identifies the document's human language so pronunciation, spelling,
translation, and other language-sensitive tools can behave appropriately. The
`title` names the page in browser tabs, history, bookmarks, and assistive
navigation. Character encoding tells the browser how bytes represent text.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Submit a student event to Campus Hub.">
    <title>Submit an event - Campus Hub</title>
  </head>
</html>
```

The viewport declaration asks mobile browsers to treat the layout viewport as
the device width. It does not make a page responsive by itself; the HTML and CSS
must still adapt. Do not disable zoom with values such as `user-scalable=no`.
People use zoom for many reasons, including low vision, fatigue, small screens,
and temporary environmental conditions.

The description metadata gives search, sharing, and indexing systems a concise
summary they may choose to use. It is not guaranteed display text and does not
replace a visible introduction. The `title` and visible `h1` have related but
different audiences: the title identifies the page in browser and navigation
contexts, while the `h1` identifies the main subject inside the document. Both
should be concise and specific, and they need not be character-for-character
identical.

Use a valid [BCP 47 language tag](https://www.rfc-editor.org/info/bcp47/), such as
`en`, `tr`, or `fa`, and mark a passage whose language changes with `lang` on the
nearest containing element. Writing direction is a separate property. Use
`dir="rtl"` for a right-to-left passage when its base direction requires it, and
prefer `dir="auto"` for user-generated text whose direction is not known in
advance. Language and direction metadata are functional information, not search
engine decoration.

When an inline user-supplied name may have an unknown writing direction, `bdi`
(Bidirectional Isolate) prevents that text's direction from unexpectedly
reordering surrounding punctuation:

```html
<p>Organizer: <bdi>مریم</bdi></p>
```

### 2.3 Structure follows the document, not its font size

A heading level expresses nesting. An `h1` names the document's main subject. An
`h2` begins a major subsection of that subject; an `h3` is subordinate to the
preceding `h2`. Choosing `h4` because its default font happens to be small confuses
presentation with structure. CSS controls appearance later.

Consider this outline:

```text
Campus Hub                           h1
  Upcoming events                   h2
    Robotics laboratory evening     h3
    Sustainable design workshop     h3
  Student communities               h2
```

The structure remains meaningful in a text-only view, a browser reader mode, a
search index, and assistive navigation. Do not choose levels merely to avoid a
large default heading.

### 2.4 Landmarks divide the page into navigable regions

Common structural elements are summarized in Table 2.2.

**Table 2.2 - Semantic elements for common document regions**

| Element | Appropriate use |
|---|---|
| `header` | Introductory material for a page or section |
| `nav` | A major group of navigation links |
| `main` | The page's unique primary content; normally one visible instance |
| `section` | A thematic grouping that usually has a heading |
| `article` | A self-contained composition that could stand independently |
| `aside` | Content indirectly related to the surrounding material |
| `footer` | Closing information for a page or section |

An element's name does not prescribe its screen position. A `nav` can appear at
the bottom; an `aside` need not be visually placed at the side. Semantics describe
purpose.

When a page contains more than one navigation region, give each a distinct name:

```html
<nav aria-label="Primary navigation">...</nav>
<nav aria-label="Event categories">...</nav>
```

A skip link is an ordinary link to the primary content, normally placed as the
first useful focusable item in `body`. It lets keyboard users bypass repeated
navigation:

```html
<a href="#main-content">Skip to main content</a>
<main id="main-content">...</main>
```

Mark the link for the current page or step with `aria-current="page"` or another
appropriate token. Do not remove its `href`; current-page information supplements
the link's native navigation semantics.

Use Accessible Rich Internet Applications (ARIA) features to fill a genuine
semantic gap or supply an accessible name. Do not add
redundant roles to native elements. `<button role="button">` says nothing that
the element does not already say.

An ARIA role is a promise about behavior. Adding `role="button"` to a `div` does
not make it focusable, activate it from the keyboard, submit a form, or supply a
disabled state. If native HTML can express the control, native HTML is normally
the more reliable starting point. ARIA is powerful when a real semantic gap
remains, but incorrect ARIA can override accurate native information.

## 3. Text content, links, and media

### 3.1 Text elements communicate rhetorical structure

Use `p` for a paragraph, `em` for stress emphasis that changes the intended
reading, and `strong` for strong importance or urgency. Use `blockquote` for an
extended quotation and `q` for a short inline quotation. The `cite` element names
a creative work, not the person who said a quotation. Use `code`, `kbd`, and
`samp` to distinguish source code, user input, and program output. Use `pre` when
line breaks and spaces are genuinely part of preformatted content, often with a
`code` child for a block of source code.

Several less frequent elements prevent generic markup from erasing meaning:

- `figure` groups self-contained content with an optional `figcaption`;
- `address` contains contact information for the nearest article or page, not an
  arbitrary postal address mentioned in prose;
- `mark` identifies text highlighted because it is relevant in the current
  context, such as a search match;
- `small` represents side comments such as legal or attribution text, not every
  sentence that should look visually small;
- `sub` and `sup` represent subscripts and superscripts when that position carries
  meaning, such as H<sub>2</sub>O or x<sup>2</sup>;
- `ins` and `del` represent inserted and deleted content; and
- `details` with `summary` provides a native disclosure when hiding the content
  does not prevent the user from discovering essential information.

`div` and `span` are neutral containers for grouping when no specific semantic
element fits. A meaningful `class` name such as `class="event-card"` helps authors
maintain code, but it does not create an article, button, heading, or landmark in
the accessibility tree.

Do not select these elements merely for their default appearance. For example,
`strong` is not a generic instruction to make arbitrary words bold, and `br` is
not a spacing tool. Meaning belongs in HTML; later CSS controls presentation.

### 3.2 Lists express grouping

Use `ul` when order is not essential, `ol` when sequence or ranking matters, and
`dl` for name-value groups. A row of navigation links is still conceptually a
list even if CSS later displays it horizontally.

### 3.3 Link text should make sense in context

“Click here” tells the reader how to operate a mouse but not where the link goes.
Prefer text that names the destination or action:

```html
<a href="/events/robotics-open-evening">Robotics open-evening details</a>
```

Do not use a link for an action that changes the current interface without
navigating. That is a button. Do not use a button merely to navigate. Correct
elements produce predictable keyboard, history, context-menu, and assistive
technology behavior.

If a link downloads a file, name the file type and, when useful, its approximate
size. If it opens a new browsing context, warn the reader before activation.
Avoid placing a URL itself in prose unless the literal address is what the reader
needs; descriptive link text is usually easier to understand and revisit.

### 3.4 Images require a purpose decision

The `alt` attribute supplies a text alternative for an image. Its content depends
on the image's purpose in this context, not only on what the pixels contain.

- An informative image needs concise equivalent information.
- A decorative image normally uses `alt=""` so it is ignored by screen readers.
- A linked image needs text that names the link's destination or action.
- A complex chart needs a short alternative and a nearby detailed explanation or
  data table.

Do not begin every alternative with “image of.” The software already identifies
the element as an image. Do not copy a caption into `alt` if that makes users hear
the same sentence twice.

```html
<figure>
  <img src="capacity.svg" width="640" height="360"
       alt="Registration rises from 20 to 48 students over four weeks">
  <figcaption>Workshop registration by week.</figcaption>
</figure>
```

The example is suitable only if that short trend is the important information.
If exact values matter, provide the underlying values as text or a table.

When the intrinsic image dimensions are known, `width` and `height` attributes
help the browser reserve the correct aspect-ratio space before the file arrives.
CSS can still scale the image responsively in Chapter 3. For an icon-only link or
button, the image alternative must identify the operation or destination, not the
icon's geometric appearance. Inline Scalable Vector Graphics (SVG) and images of
text require the same purpose analysis; using a different file format does not
remove the need for an accessible name or equivalent information.

### 3.5 Dates, abbreviations, and data can have machine-readable values

The `time` element lets visible wording and a machine-readable date or time
coexist. Its `datetime` value uses a standardized form that software can parse.

```html
<p>The workshop begins <time datetime="2026-10-14T18:30:00+03:00">14 October at 18:30</time>.</p>
```

The visible text is written for the reader; the attribute includes the year and
Coordinated Universal Time (UTC) offset needed to identify the instant. A local
event whose time zone is already unambiguous in context may use a local date or
time value, but software must not invent a time zone that the content did not
specify.

Use `abbr` when expanding an abbreviation genuinely helps, and expand uncommon
abbreviations in ordinary prose at first use. Do not put essential teaching in a
`title` tooltip: it is not consistently available to keyboard, touch, or
assistive-technology users.

### 3.6 Audio and video require equivalent access

Controls alone do not make recorded media accessible. Prerecorded video with
meaningful speech needs synchronized captions. Audio-only material needs a
transcript. Important visual information that is not conveyed in the soundtrack
may require audio description or an equivalent text account. Do not rely on
automatic captions without reviewing names, technical vocabulary, punctuation,
speaker changes, and timing.

The `track` element can associate caption files with `video`, but authoring the
media element and producing an accurate alternative are separate responsibilities.
Also provide a fallback link when a browser cannot play the chosen format.

### 3.7 Tables are for relationships in data

A data table represents relationships between headers and cells. It is not a
page-layout mechanism.

```html
<table>
  <caption>Remaining places by workshop</caption>
  <thead>
    <tr><th scope="col">Workshop</th><th scope="col">Places</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Robotics safety</th><td>12</td></tr>
    <tr><th scope="row">Accessible design</th><td>8</td></tr>
  </tbody>
</table>
```

The caption names the table. Header cells and `scope` expose row and column
relationships. Visual alignment alone cannot communicate those relationships to
software.

For a simple table, `scope="col"` and `scope="row"` are normally sufficient. A
multi-level table may use `scope="colgroup"` or `scope="rowgroup"` when its
structure genuinely contains those groups. When relationships cannot be expressed
clearly with scope, give each header a unique `id` and list the applicable header
IDs in a data cell's `headers` attribute. Complex tables impose cognitive and
testing costs, so first ask whether the data can be divided into several simpler
tables. Do not use an empty header cell merely to create visual spacing, and do
not rely on color or position alone to identify a total or category.

## 4. Forms are conversations with constraints

A form gathers values for an operation. Each successful control contributes a
name-value pair when the form is submitted. The `name` attribute supplies the
name used in that submission; `id` identifies an element within the document.
They often share a value but serve different purposes.

```html
<form action="/events" method="post">
  <label for="event-title">Event title</label>
  <input id="event-title" name="title" type="text" required>

  <button type="submit">Submit event</button>
</form>
```

The label's `for` value matches the control's `id`. Activating the label focuses
the input. Assistive technology can announce “Event title, edit text, required.”
The control's `name="title"` determines the submitted field name. The form's
`action` identifies the submission destination, while `method` selects the HTTP
method used by the browser's form-submission algorithm. Figure 2.5 follows these
relationships from the visible label to the submitted value and then to
server-side validation.

<!-- figure:form-data-flow -->

Figure 2.6 shows the browser output of the complete Week 2 form. It deliberately
uses native browser presentation so students can see what correct HTML provides
before custom CSS is introduced.

<!-- media:week-02-form-output -->

### 4.1 Choose the submission method from the operation

A `get` form represents retrieval. Its successful name-value pairs normally
become a query in the resulting URL, which makes a search easy to bookmark and
share. A `post` form sends form data in the request content and is suitable for an
operation that creates or changes server state. `post` does not encrypt data and
does not make an operation safe: use HTTPS, validate on the server, authorize the
operation, and avoid collecting information the service does not need.

The method is not merely a syntax preference. Refreshing, bookmarking, caching,
history, logs, and retries behave differently. A search form can use `get`; an
event-creation form should use `post`. Later server chapters add Cross-Site
Request Forgery protection and show how the application handles the submitted
data.

### 4.2 Labels and descriptions remain available

A placeholder is an example or hint, not a replacement for a label. It disappears
as the user types, is often displayed with weak contrast, and does not consistently
provide an accessible name. Keep a visible label. If format guidance matters,
associate permanent help text with the control:

```html
<label for="event-date">Event date</label>
<input id="event-date" name="date" type="date"
       aria-describedby="event-date-help" required>
<p id="event-date-help">Choose a date within the current semester.</p>
```

The connected `label` provides the **accessible name**: the short identity of the
control. `aria-describedby` contributes an **accessible description**: additional
instructions, format guidance, or context. A description does not replace a
name. Keep important instructions visible so people who do not use assistive
technology receive the same information.

### 4.3 Select the narrowest appropriate native control

Input types communicate intent and can provide mobile keyboards and built-in
checks. Examples include `email`, `url`, `date`, `time`, `number`, `search`, and
`password`. Use `textarea` for multi-line input, `select` for a constrained list,
checkboxes for independent choices, and radio buttons for one choice from a set.

Choose the type from the value's meaning, not from the characters it happens to
contain. A postal code, telephone number, student number, credit-card number, or
one-time code is an identifier, not a quantity on which arithmetic is performed.
It normally uses a text-like input with suitable `autocomplete` and `inputmode`
rather than `type="number"`. The `inputmode` attribute is a keyboard hint; it does
not validate the value. Table 2.3 summarizes common decisions.

**Table 2.3 - Choosing native form controls and supporting attributes**

| User task | Native starting point | Important considerations |
|---|---|---|
| Short general text | `input type="text"` | Add a visible label, useful `autocomplete`, and length constraints only when the task defines them. |
| Email address | `input type="email"` | The browser checks an email-shaped value, not whether the mailbox exists or belongs to the user. |
| Password | `input type="password"` | Use the correct `autocomplete` token; allow password managers and paste; never treat masking as encryption. |
| Search | `input type="search"` | Normally belongs in a GET form because it retrieves or filters information. |
| Quantity | `input type="number"` | Use for arithmetic quantities with meaningful `min`, `max`, and possibly `step`; not for digit-only identifiers. |
| Telephone or numeric identifier | `input type="tel"` or text with `inputmode="numeric"` | Preserve leading zeroes and formatting; validate according to the real domain rather than assuming one national pattern. |
| Date or time | `input type="date"` or `input type="time"` | Native presentation varies; state time zone and allowed range when they matter. |
| Several lines of text | `textarea` | Its initial value is text between the tags; provide rows as a useful starting size, not a content limit. |
| One option from a short visible set | Radio buttons in `fieldset` | A shared `name` forms the choice; the `legend` names the group. |
| Independent yes/no options | Checkboxes | Each choice needs a label and an explicit value; unchecked boxes are omitted from submission. |
| One option from a longer set | `select` with `option` | Use `optgroup` for meaningful groups; make any prompt option non-ambiguous. |
| Suggested values with free entry | `input` with `list` and `datalist` | Suggestions are not a closed constraint; server validation must accept or reject the actual value. |
| File selection | `input type="file"` | The POST form normally needs `enctype="multipart/form-data"`; `accept` is only a picker hint. |

Group related choices with `fieldset` and `legend`:

```html
<fieldset>
  <legend>Attendance mode</legend>
  <label><input type="radio" name="mode" value="campus" required> On campus</label>
  <label><input type="radio" name="mode" value="online"> Online</label>
</fieldset>
```

The shared `name` makes the radio buttons one submitted choice. The legend names
the group. A collection of visually adjacent controls without this relationship
is more difficult to interpret.

Button type also matters. Inside a form, a `button` defaults to submission.
Write `type="submit"` for the submitter and `type="button"` for a button that
performs only a client-side action. Avoid reset buttons in ordinary forms because
an accidental activation can erase substantial work.

Do not nest one form inside another; HTML does not support nested forms. A control
can be explicitly associated with a form through the `form` attribute, but
keeping controls visibly and structurally near their form is usually clearer.
Pressing Enter may submit some forms through the browser's implicit-submission
behavior, so every form must remain coherent without depending only on a pointer
click.

### 4.4 Predict which controls will be submitted

The browser does not submit every element inside `form`. Table 2.4 summarizes
the rules students most often need when debugging missing or surprising data.

**Table 2.4 - Common successful-control submission rules**

| Control condition | Submitted? | Reason or consequence |
|---|---|---|
| Enabled control with a `name` | Usually yes | Its current value is associated with that name. |
| Control without a `name` | No | An `id` can label or target the element but does not create a submitted field name. |
| Disabled control | No | Disabled controls are not successful controls and are normally not operable. |
| Read-only text control | Yes | The value cannot be edited through the control, but it can still be submitted and must not be trusted. |
| Unchecked checkbox or radio button | No | No name-value pair is contributed for that control. |
| Checked checkbox or radio button | Yes | Its explicit `value` is submitted; without one, a browser-defined default such as `on` can surprise the server. |
| Submit button that initiated submission | Yes | Its name and value can identify which submit action was chosen. Other submit buttons are omitted. |
| File input with no selected file | Browser-dependent empty file entry under multipart rules | The server must handle the no-file case explicitly rather than infer a usable upload. |

Submission rules explain transport, not trust. Hidden and read-only values can be
modified by a client. The server must derive security-sensitive facts, such as
the current user or an authorized price, from trusted server-side state.

### 4.5 Choose the encoding, especially for files

Form submission must represent names and values as bytes. With GET, form data is
encoded into the URL query. With an ordinary POST form, the default encoding is
`application/x-www-form-urlencoded`, which represents fields in a query-like
name-value form inside the request body. Spaces and reserved characters require
percent-encoding; the server framework later decodes them.

A file upload normally requires POST and `multipart/form-data`:

```html
<form action="/event-materials" method="post" enctype="multipart/form-data">
  <label for="agenda">Agenda document</label>
  <input id="agenda" name="agenda" type="file" accept=".pdf">
  <button type="submit">Upload agenda</button>
</form>
```

Multipart encoding separates fields into parts so file bytes and ordinary text
can travel in one request. `accept=".pdf"` helps a file picker present likely
choices; it is not a security boundary. The server must enforce allowed type,
size, content, authorization, storage name, malware policy, and retention. Do not
trust a client-supplied filename, extension, media type, or local path. The
`text/plain` encoding exists but is not a robust general application encoding.

### 4.6 Autocomplete, input purpose, and data minimization

The `autocomplete` attribute helps browsers and assistive technologies identify
the purpose of common personal-data fields. Tokens such as `name`, `email`,
`organization`, and `current-password` are more informative than arbitrary field
names. Autocomplete can reduce effort and errors, especially for people with
motor or cognitive disabilities. Do not disable it reflexively.

Choose fields from the task, not from curiosity. Explain why information is
required, avoid collecting secrets in examples, and do not place confidential
values in GET URLs. `readonly` and `disabled` are interface states, not privacy or
authorization mechanisms.

Attributes such as `inputmode`, `autocapitalize`, and `spellcheck` can reduce
entry effort, but they are hints rather than validation. Disable spell checking
for a value when sending it to a spelling service would be inappropriate, such as
a password or one-time code. Do not disable paste in password or confirmation
fields; password managers and assistive workflows depend on it.

### 4.7 Constraint validation is useful but incomplete

Attributes such as `required`, `min`, `max`, `minlength`, `maxlength`, and
`pattern` express constraints to the browser. They improve the experience and
reduce avoidable requests. They are not a security boundary. A client can disable
JavaScript, alter markup, or send a Hypertext Transfer Protocol (HTTP) request
directly. The server must
validate every untrusted value again.

Validation should answer three questions:

1. What is wrong?
2. Where is the problem?
3. How can the user correct it?

Color alone cannot answer them. Provide specific text, preserve valid values,
associate messages with controls, and move focus or an error summary appropriately
after a failed submission.

Mark required and optional status in words, preferably before the user begins the
form, and include the status in or programmatically with each relevant label.
An asterisk without an explanation is ambiguous. Native `required` already
exposes the required state; adding `aria-required="true"` to the same native
control is normally redundant.

### 4.8 Design error recovery before adding JavaScript

A server-rendered response can return the form with an error summary and
field-level messages without any JavaScript. The page title should announce the
failed state, the summary should appear before the form, and each message should
identify the problem and correction. Preserve valid values unless security makes
that unsafe.

```html
<title>2 errors - Submit an event - Campus Hub</title>

<div role="alert" tabindex="-1">
  <h2>There are 2 errors</h2>
  <ul>
    <li><a href="#event-title">Enter an event title.</a></li>
    <li><a href="#capacity">Enter a capacity from 1 to 300.</a></li>
  </ul>
</div>

<label for="capacity">Capacity (required)</label>
<input id="capacity" name="capacity" type="number"
       min="1" max="300" required aria-invalid="true"
       aria-describedby="capacity-error">
<p id="capacity-error">Enter a whole number from 1 to 300.</p>
```

`aria-invalid="true"` belongs on a control only while its current value is known
to be invalid. The description connects the specific correction. `tabindex="-1"`
allows a script or server-navigation enhancement to move focus to the summary
without adding it to the ordinary Tab sequence. A static server response is
already announced as a new page; `role="alert"` becomes especially relevant when
errors are inserted dynamically, which later JavaScript chapters treat carefully.

### Predict before running

Given this control:

```html
<input id="capacity" type="number" min="1" max="300" required>
```

Will a value be submitted under the name `capacity`? No. The control has an `id`
but no `name`, so it does not contribute that name-value pair. The browser can
still validate and display it. This distinction is a frequent source of missing
server data.

## 5. Three related representations

The browser maintains several related models:

1. Source HTML is the text received or read from a file.
2. The DOM is the parsed, live document tree.
3. The accessibility tree is a platform-oriented representation containing
   relevant roles, names, states, values, and relationships for assistive tools.

Figure 2.7 locates the accessibility tree between the live Document Object Model
(DOM) and the assistive technology that consumes the platform representation.

<!-- figure:accessibility-tree -->

These representations are not identical. CSS can hide content. The HTML parser
can repair omitted structure. JavaScript can alter the DOM. Some DOM nodes do not
need accessibility exposure, while one compound widget may create several
accessible relationships.

The HTML `hidden` attribute, CSS `display: none`, and the `hidden` state of a
closed disclosure normally remove descendant content from both visual rendering
and the accessibility tree. Visually hidden content intended only for assistive
technology requires a carefully tested CSS pattern introduced in Chapter 3; do
not use `hidden` for that purpose. Conversely, visually placing content off-screen
without understanding focus can create a focus target that the keyboard reaches
but a sighted user cannot see.

The accessibility tree is not “a screen reader version of the DOM.” It is a
semantic interface used through operating-system accessibility application
programming interfaces (APIs). Different
browsers and platforms can expose details differently, but good native HTML
provides a strong interoperable basis.

### 5.1 Accessible name, description, role, and state

Interactive controls need a name that identifies their purpose. A button's text
usually provides its name. An input normally obtains its name from a connected
`label`. An image can obtain a name from `alt`. `aria-label` can supply a name when
no visible text can do so, but visible text is usually preferable because all
users receive the same wording. A description supplies supporting information;
it should not repeat the name word for word. Role communicates what kind of
thing the object is, while state communicates information such as checked,
expanded, selected, invalid, or disabled.

For speech-input users, the words they can see should occur in the accessible
name. If the visible label says “Organizer email” while an `aria-label` silently
renames the control “Contact address,” a voice command based on the visible words
may fail. Prefer the connected visible label and use `aria-describedby` for extra
help rather than replacing good visible text.

Do not place important visible text in CSS-generated content and assume it will
be exposed consistently. Put meaningful content in HTML.

### 5.2 Keyboard operation is an engineering test

Use the Tab key to move through interactive elements. Use Shift+Tab to reverse
direction, Enter to activate links and many buttons, Space to activate buttons
and toggle checkboxes, and arrow keys within controls that define arrow-key
behavior.

A useful keyboard inspection asks:

- Is every operation reachable?
- Is the focus indicator visible against its surroundings?
- Does focus order follow the reading and task order?
- Can a user escape components such as dialogs and menus?
- Does focus move only when there is a clear reason?

Positive `tabindex` values create a separate focus order that becomes difficult
to maintain. Prefer logical source order and native elements. Use `tabindex="-1"`
when a normally non-focusable element must receive programmatic focus, such as an
error summary, not to insert it into ordinary Tab navigation.

## 6. Accessibility is broader than conformance

The Web Content Accessibility Guidelines (WCAG) 2.2 organize accessibility under
four principles. Content should be **perceivable**, **operable**,
**understandable**, and **robust**. The initials form the useful memory aid POUR.
Table 2.5 connects each principle to questions a student can ask of Campus Hub.

**Table 2.5 - WCAG principles as engineering questions**

| Principle | Engineering question |
|---|---|
| Perceivable | Can necessary information be obtained through more than one relevant sensory pathway, including text alternatives and captions? |
| Operable | Can people complete the task with keyboard, pointer, touch, zoom, and other supported input without traps or obscured focus? |
| Understandable | Are labels, instructions, navigation, errors, and changes predictable enough to act upon? |
| Robust | Do names, roles, states, values, and relationships remain available across supported browsers and assistive technologies? |

WCAG success criteria are assigned conformance levels A, AA, or AAA. Level AA is
a common organizational target, but conformance is evaluated against defined
criteria for complete pages and processes; it is not a general score produced by
one scanning tool. A product can meet a formal criterion and still impose a poor
experience, while an isolated automated warning may require human interpretation.

Standards provide testable requirements, but an automated checker cannot decide
whether alternative text communicates the correct purpose, whether instructions
are understandable, or whether a workflow places an unreasonable cognitive
burden on a user. Combine:

- valid semantic HTML;
- automated checks;
- keyboard testing;
- browser accessibility inspection;
- zoom and reflow testing;
- testing with assistive technology when possible; and
- feedback from disabled people and representative users.

Passing an automated scan is evidence, not proof of accessibility.

Figure 2.8 shows these evidence sources operating in parallel. Automated checks
find some programmatically detectable failures. Keyboard and zoom testing reveal
interaction and reflow problems. Accessibility-tree inspection and a screen
reader expose names, roles, states, and reading behavior. Representative users
show whether the real task is understandable and achievable. The conclusion is
based on the combined evidence; no station can replace all the others.

<!-- media:accessibility-combined-evidence -->

---

# Guided laboratory - Build an accessible event form

## Goal and acceptance criteria

Complete the Week 2 starter as a no-CSS, no-JavaScript event-submission page. The
page must remain understandable through structure alone.

Your result must contain:

- a useful title, language, encoding, description, and viewport declaration;
- a skip link whose target is the `main` element;
- one `h1` followed by logically nested headings;
- labeled primary navigation;
- a form using `post` with a meaningful `action`;
- visible labels for title, organizer email, date, start time, capacity, format,
  and description;
- native input types and reasonable constraints;
- appropriate autocomplete metadata for the organizer email;
- an `aria-current="page"` indication on the relevant navigation link;
- a `fieldset` and `legend` for the event format;
- persistent help text associated with the description;
- a submit button with an explicit type;
- no positive `tabindex`, ARIA role that duplicates a native role, inline event
  handler, secret, or real personal data; and
- at least three coherent Git commits.

## Step 1 - Read before editing

From the repository root, open
`labs/week-02/index.html` in the VS Code text editor. Verify the full
folder path rather than trusting an `index.html` tab name. In the SERVER terminal,
run `dir package.json` on Windows or `ls -l package.json` on macOS/Linux, followed
by `npm run serve:week02`. Leave that process running, open
`http://localhost:8000/`, and confirm that the baseline page displays **Submit a
campus event**. Keep a second terminal available for Git and tests.

Now identify every TODO in the source. Sketch the intended heading outline and
form data names on paper. Decide which information is instruction, which is a
label, and which is a constraint. Save each meaningful edit and reload the
browser; the local server displays saved files, not unsaved editor contents.

## Step 2 - Establish landmarks and navigation

Add a skip link as the first useful link in `body`, a page header, labeled
navigation, `main id="main-content"`, and a footer. Activate the skip link with a
keyboard and confirm that its target exists.

## Step 3 - Build the form from native controls

Use labels and native input types. Choose names that a server could interpret,
such as `title`, `organizerEmail`, `date`, `startTime`, `capacity`, `format`, and
`description`. Do not use placeholder text as the only instruction.

## Step 4 - Define the submission contract

Confirm that the form uses `post` because it creates an event. Write the expected
successful field names in order, and predict which controls disappear from the
submission when they are disabled or unchecked. Explain why no field is trusted
merely because it was read-only or hidden in the interface.

## Step 5 - Express constraints

Require all fields except the description. Set capacity to a reasonable range.
Set a useful maximum length for free text. Associate description help text with
`aria-describedby`.

## Step 6 - Test without a mouse

Reload at the top of the page, set the mouse aside, and complete the form. Record
the focus order. Trigger at least two native validation messages. At 200% zoom,
confirm that no information is lost.

## Step 7 - Validate the source and inspect the tree

Submit the source to the W3C Nu HTML Checker by direct input, or use an approved
local equivalent when the document is private. Correct every source error. Then
inspect the heading structure, landmarks, labels, and the capacity control's
name, role, value, description, and required state in browser accessibility tools.
Record one thing a validator can establish and one meaning it cannot judge.

## Step 8 - Verify, explain, and commit

Keep the server terminal running and open a second terminal with **Terminal > New
Terminal**. This second terminal is the commands terminal: it displays a prompt
and accepts new commands while the first terminal remains occupied by the
server. From the repository root, run:

```text
npm test
```

The final output should report `Coursework setup verification passed.` This
check proves that the supplied structure and server still operate; it does not
grade every semantic decision in the completed form. If it fails, read the first
reported check, correct the source or project location, save, and run the command
again. Then compare the page with every acceptance criterion and write a
five-sentence rationale explaining one native semantic choice, one keyboard
observation, one limitation of browser validation, one privacy decision, and one
improvement you would test with users. Review the
staged diff and create the final laboratory commit only after the browser,
accessibility inspection, validator, and automated check agree with the intended
source.

## Laboratory observation record

Table 2.6 is an evidence record, not a checklist to mark without observation.
Students should write what they saw and then explain what that observation means.

**Table 2.6 - Laboratory accessibility observation record**

| Check | Evidence and interpretation |
|---|---|
| Heading outline | |
| Skip-link target | |
| First five focus stops | |
| Accessible name of capacity control | |
| Method and action rationale | |
| Expected successful field names | |
| Two native validation results | |
| Data excluded for privacy | |
| Automated-check limitation | |
| Nu HTML Checker result and limitation | |
| Accessibility-tree name, role, state, and description | |

---

# Exercises

## Foundation

### Exercise 1 - Element choice

Choose the best native element for each item and explain why: a navigation
destination, an operation that opens a filter panel, a self-contained news item,
a set of event categories, and the page's unique content region.

### Exercise 2 - Label and name

Explain the independent purposes of `label[for]`, `id`, and `name` in a form.
What breaks if an input has only `id="email"`?

### Exercise 3 - Alternative text

An event card contains a decorative confetti pattern, a speaker portrait next to
the visible name “Dr. Ada Kaya,” and a chart of registration by faculty. Propose
an alternative-text strategy for each.

## Application

### Exercise 4 - Repair the outline

Repair this structure without selecting headings by desired size:

```html
<h3>Campus Hub</h3>
<h1>Events</h1>
<h4>Robotics evening</h4>
<h2>Communities</h2>
```

### Exercise 5 - Diagnose the inaccessible control

Why is this not an adequate button, and what is the smallest correct replacement?

```html
<div class="button" onclick="submitEvent()">Submit</div>
```

### Exercise 6 - Table relationships

Design semantic table markup for three rooms and their capacity, building, and
availability. Identify the caption, column headers, and row headers.

## Challenge

### Exercise 7 - Validation boundary

The browser rejects an empty title, but an attacker successfully submits an empty
title to the API. Explain how both observations can be true and specify validation
responsibilities at the browser, server boundary, and database.

### Exercise 8 - Accessibility-tree reasoning

A visually hidden checkbox remains in the DOM but is removed from the
accessibility tree with `display: none`. A styled `div` is visible and clickable
but has no role or keyboard behavior. Explain what different users and tools may
perceive, and propose native-HTML repairs.

### Exercise 9 - Predict the submitted data

Consider this form. Assume the user enters `Ada`, leaves the checkbox unchecked,
and activates the Save button. Write the name-value pairs the browser will submit
and explain why the other controls do or do not contribute data.

```html
<form action="/profiles" method="post">
  <input name="displayName" value="Ada">
  <input name="theme" value="dark" disabled>
  <input name="studentId" value="CE-104" readonly>
  <input type="checkbox" name="newsletter" value="yes">
  <button type="submit" name="intent" value="save">Save</button>
</form>
```

### Exercise 10 - Choose a testing strategy

A scanner reports no accessibility errors for a course-registration form. State
why that result is insufficient. Design a compact test plan that gathers at least
four different kinds of evidence, and identify one question each method can and
cannot answer reliably.

### Exercise 11 - Repair the syntax and semantics

Identify every independent problem in this fragment, write a conforming repair,
and explain what the browser cannot infer from the original source.

```html
<p class=event note>Register <strong>before Friday</p></strong>
<input id="email" type="email" required="false" placeholder="Email">
<p id="help">Use your university address & include the department.</p>
```

### Exercise 12 - Choose controls and encoding

Design the HTML form contract for an event search, a six-digit one-time code, a
seat quantity from 1 to 20, and an optional PDF agenda upload. Choose the method,
control types, keyboard hints, names, constraints, and encoding. Explain why one
form should not necessarily contain all four operations.

### Exercise 13 - Design error recovery

A server rejects `capacity=500` and returns the form. Specify the page title,
error summary, link target, field attributes, field-level message,
value-preservation decision, and focus plan. Explain what changes if JavaScript
inserts the error into the existing page instead of returning a new page.

### Exercise 14 - Model a complex table

A timetable has two column groups, Monday and Tuesday, each with Morning and
Afternoon columns. Every row begins with a room header. Design the header
relationships using `caption`, `thead`, `tbody`, `colgroup`, and appropriate
`scope` values. Then state when you would replace the table with two simpler
tables or use explicit `id` and `headers` associations.

---

# Worked answers

## Answer 1

Use `a` with an `href` for the navigation destination because it participates in
history, link menus, copying, and ordinary link keyboard behavior. Use `button`
for opening a filter panel because it performs an action in the current interface.
Use `article` for the self-contained news item, `ul` with `li` for categories when
order is unimportant, and `main` for the unique primary content. CSS can give any
of these the required appearance without erasing their meaning.

## Answer 2

`id` uniquely identifies the element in the document. `label for="email"` uses
that identifier to associate visible label text with the control. `name` supplies
the key used when the form constructs submitted data. With only `id="email"`, a
connected label can work, but the control does not submit a field named `email`.
The three attributes may share a value, yet they are not interchangeable.

## Answer 3

The decorative confetti should use an empty alternative, `alt=""`, because it
adds no information. The portrait can also use `alt=""` when the adjacent visible
name already provides all relevant identity; repeating the name would be noisy.
If the portrait communicates additional relevant information, include only that
information. The chart needs a concise summary of its important conclusion plus
nearby access to exact values, normally a table or textual description. “Chart”
alone is not an equivalent.

## Answer 4

A defensible repair is one `h1` for Campus Hub, `h2` for Events and Communities,
and `h3` for Robotics evening under Events. The original levels suggested that
Events was the document title and Campus Hub was deeply subordinate. Heading
appearance should be styled later with CSS.

```html
<h1>Campus Hub</h1>
<h2>Events</h2>
<h3>Robotics evening</h3>
<h2>Communities</h2>
```

## Answer 5

The `div` has no native button role, focusability, keyboard activation, disabled
state, or form semantics. An `onclick` handler supplies only one implementation
path. The smallest repair is `<button type="button">Submit</button>` with the
behavior attached separately. If it submits a form, use `type="submit"` and allow
the form's submit event and native behavior to coordinate the operation.

## Answer 6

Use a caption such as “Teaching-room availability.” Put Room, Capacity, Building,
and Availability in `th scope="col"` cells inside `thead`. In each body row, put
the room name in `th scope="row"` and the other values in `td` cells. This exposes
the same row-column relationships that visual alignment communicates to a sighted
reader. A layout made of generic elements would require software to guess.

## Answer 7

Browser validation is executed by a client under the user's control. An attacker
can modify the document, disable checks, or call the API directly. The browser
should provide immediate, accessible feedback for ordinary mistakes. The server
must treat every request as untrusted, normalize and validate the value, and
return a consistent error. The database should enforce durable invariants with
constraints such as `NOT NULL` and, when appropriate, a check on trimmed length.
No single layer replaces the others: they serve user experience, trust-boundary
protection, and persistent integrity respectively.

## Answer 8

`display: none` removes the checkbox from visual layout and normally from the
accessibility tree, so neither sighted users nor screen-reader users can operate
it even though a DOM node exists. The clickable `div` may be visible to a mouse
user, but it has no native control semantics and is not ordinarily in the Tab
order. Use a real checkbox with a connected visible label for a binary choice and
a real button for an action. If custom visuals are required, style the native
control or its label while preserving focus, name, state, and keyboard behavior.

## Answer 9

The submission contains `displayName=Ada`, `studentId=CE-104`, and
`intent=save`. The display-name control is enabled and named, so its current value
is successful. `readonly` prevents ordinary editing but does not prevent the
student identifier from being submitted. The disabled theme control is omitted.
The unchecked checkbox is also omitted; a checkbox contributes its configured
value only when checked. The activated submit button contributes its own
`name=value` pair, which lets the server distinguish Save from another possible
submission action. These browser rules describe data construction, not trust:
the server must still authorize and validate every received field.

## Answer 10

An error-free scan means only that the chosen tool did not detect a rule it knows
how to test in the page state it inspected. It does not prove that labels are
meaningful, keyboard order follows the task, reflow remains usable, screen-reader
feedback is understandable, or the overall registration journey can be completed.
A defensible plan combines: an automated standards check for detectable markup
errors; keyboard-only completion while observing focus order and visibility;
zoom and narrow-viewport reflow inspection; accessibility-tree and screen-reader
inspection of names, roles, states, errors, and status messages; and, where
possible, representative-user task testing. Automation can find a missing label
association but cannot reliably judge whether the wording explains the field.
Keyboard testing can expose unreachable actions but cannot establish spoken
output. Tree and screen-reader inspection can expose an incorrect name or state
but cannot by itself prove that the workflow suits real users. User testing
reveals task barriers in context but does not replace systematic conformance
checks. The methods answer different questions, so their evidence must be read
together.

## Answer 11

The unquoted class value stops at `event`; `note` is parsed as a separate Boolean
attribute rather than a second class token. The `p` and `strong` elements overlap
instead of nesting. `required="false"` still turns the Boolean required state on.
The input has no connected visible label and no `name`, so its value would not be
submitted. A placeholder is not a durable label. Finally, the literal ampersand
should be written as `&amp;` in conforming text where it could begin a character
reference. One repair is:

```html
<p class="event note">Register <strong>before Friday</strong>.</p>

<label for="email">University email</label>
<input id="email" name="email" type="email" aria-describedby="help">
<p id="help">Use your university address &amp; include the department.</p>
```

Whether the email is required is a product decision. The repair omits `required`
to match the literal false intention; if the field is required, add the bare
attribute and say so in the label or form instructions. Error recovery can create
a DOM, but the browser cannot infer the intended second class, business rule,
visible label, submitted field name, or authorial nesting with certainty.

## Answer 12

The event search is a retrieval operation and belongs in a GET form, commonly
with `<input type="search" name="q">`. Its value becomes a bookmarkable query.
The one-time code is an identifier rather than a quantity; use a text input such
as `<input name="code" inputmode="numeric" autocomplete="one-time-code"
pattern="[0-9]{6}" maxlength="6">`, while recognizing that the server must still
validate the exact six-digit policy. The seat count is a quantity and can use
`<input type="number" name="seats" min="1" max="20" step="1">`.

The agenda upload uses `<input type="file" name="agenda" accept=".pdf">` inside
a POST form with `enctype="multipart/form-data"`. The server must verify the
file's content, type, size, authorization, and storage policy. Search is safe,
shareable retrieval, while an upload changes server state and carries file bytes.
Putting both into one submission would blur method semantics and encoding, so
separate forms are clearer. The one-time code likely belongs to a separate
authentication workflow rather than an event search or upload.

## Answer 13

Use a specific title such as “1 error - Submit an event - Campus Hub.” Place a
summary before the form with a heading such as “There is 1 error” and a link to
`#capacity`. Keep `id="capacity"`, set `aria-invalid="true"`, and associate
`aria-describedby="capacity-error"`. The visible message should say what works,
for example, “Enter a whole number from 1 to 300.” Preserving `500` can help the
user understand and correct the mistake; preserve all other safe, valid fields as
well. Passwords and other security-sensitive values may need different handling.

For a new server-rendered page, move focus to the summary through normal page
navigation or a deliberate focus enhancement and ensure the title reports the
failure. If JavaScript inserts the error without navigation, the change needs an
appropriate live announcement, focus must be managed without creating a trap,
and repeated submissions must not produce duplicate IDs or stale messages.

## Answer 14

Give the table a caption that names the timetable. In `thead`, the first row has
a corner cell followed by `<th scope="colgroup" colspan="2">Monday</th>` and the
equivalent Tuesday header. The second header row contains Morning and Afternoon
as `<th scope="col">` cells under each day. Use two `colgroup` elements, each
spanning the relevant pair of day columns, after the room column. In `tbody`, each
room name is `<th scope="row">`, followed by four data cells.

Test the resulting associations in more than one accessibility combination.
Divide the table when users naturally compare one day at a time or when the
combined grid becomes difficult to understand at narrow widths. If header levels,
spans, or irregular cells cannot be represented unambiguously with scope, assign
unique IDs to header cells and list all applicable IDs in each data cell's
`headers` attribute. Visual position alone is not a sufficient relationship.

---

# Debugging clinic

A student reports, “The Email text is immediately above the field, so the field
is labeled.” Inspection shows `<p>Email</p><input type="email" name="email">`.

## Diagnosis

Visual proximity is not a programmatic relationship. The input has no accessible
name from a connected label. Replace the paragraph with
`<label for="email">Email</label>` and add `id="email"` to the input, or wrap the
input inside its label. Then inspect the accessibility tree and activate the
label to confirm that it focuses the control. Do not add `aria-label` merely to
avoid correcting the visible markup.

---

# Retrieval quiz

1. What does semantic HTML communicate?
2. Why should heading level not be chosen from default font size?
3. When is `article` more appropriate than `section`?
4. What is the difference between a link and a button?
5. Why is placeholder text not an adequate label?
6. What does a form control's `name` do?
7. Why must the server repeat validation performed by the browser?
8. What information belongs in an accessible name?
9. Why is `alt=""` sometimes correct?
10. What does the accessibility tree contain?
11. Name two limitations of automated accessibility testing.
12. Why should positive `tabindex` values usually be avoided?
13. What is the practical difference between `disabled` and `readonly` controls
    during form submission?
14. When is GET normally preferable to POST for an HTML form?
15. Name the four WCAG principles and explain why satisfying one does not imply
    satisfying the other three.
16. What is the difference between a tag and an element?
17. Why does `required="false"` still make a native control required?
18. Why is `type="number"` usually wrong for a student number or postal code?
19. Which form encoding is normally required for a file upload?
20. Name four parts of an accessible server-rendered validation failure.

## Quiz answers and misconception notes

1. It communicates the roles and relationships of content and controls. Semantics
   are not a promise about visual style.
2. Levels express document nesting. CSS, not an incorrect level, should change
   size and spacing.
3. Use `article` when the composition is independently meaningful or reusable,
   such as a news story or event card. A `section` is a thematic division of its
   surrounding document.
4. A link navigates to a resource; a button performs an action. Native behavior,
   not just appearance, follows that distinction.
5. A placeholder disappears, is not consistently an accessible name, and cannot
   remain as permanent instruction. Keep a visible connected label.
6. It supplies the key for that control's submitted value.
7. The client is outside the server's trust boundary and can be bypassed or
   modified. Server validation protects the operation.
8. A concise description of the control's purpose, normally derived from its
   visible label or text.
9. An empty alternative intentionally removes a decorative or redundant image
   from the accessibility experience.
10. Relevant roles, names, states, values, and relationships exposed through
    platform accessibility APIs.
11. Automated tools cannot reliably judge whether text alternatives convey the
    intended meaning or whether an entire workflow is understandable. Many other
    usability and assistive-technology interactions also require human testing.
12. They create a manually managed focus order that easily diverges from reading
    and source order. Prefer logical HTML order and native focusability.
13. A disabled control cannot ordinarily be operated and is omitted from submitted
    form data. A read-only text control cannot ordinarily be edited, but it remains
    focusable in common browsers and its named value is submitted. Neither makes a
    client-provided value trustworthy to the server.
14. Use GET when submission retrieves or filters information without requesting a
    state change and when a bookmarkable, shareable query is useful. Use POST when
    the request creates or changes server state, carries a larger body, or should
    not place ordinary field values in the URL. HTTPS is still required for
    confidentiality; POST alone is not encryption.
15. Perceivable, Operable, Understandable, and Robust. They address different
    failure modes: content may be perceivable but impossible to operate, operable
    but confusing, or understandable visually while exposing invalid semantics to
    assistive technology. Evidence is required across all applicable principles.
16. A tag is source markup at an element boundary, such as `<p>` or `</p>`. The
    element is the complete parsed object, including its tags when applicable,
    attributes, content, and relationships.
17. `required` is a Boolean attribute. Presence means true regardless of a string
    that looks like “false.” Omit it to turn the native required state off.
18. Those values are identifiers rather than arithmetic quantities. Numeric input
    can reject formatting or leading zeroes and implies quantity behavior. Use an
    appropriate text-like control with `inputmode` and domain validation.
19. `multipart/form-data` on a POST form. The picker and `accept` attribute do not
    remove the server's responsibility to validate the uploaded bytes.
20. A failure-specific page title, an error summary with links, field-level
    messages associated with their controls, and invalid-state/focus handling.
    Preserving safe valid values and explaining how to correct each error are also
    essential.

### Self-check scale

- **17-20:** ready to style the document without sacrificing its structure.
- **12-16:** revisit syntax, forms, and the accessibility-tree model, then repeat the
  keyboard test.
- **0-11:** rebuild the laboratory form from native elements and explain each
  choice to a peer or teaching assistant.

---

# Session summary

- The Session 2 working source is `labs/week-02/index.html`; VS Code
  edits it, the local Node.js server serves it, and the browser renders it.
- The basic feedback cycle is edit, save, reload, and inspect. An unsaved file or
  a different `index.html` cannot change the page currently being served.
- HTML describes structure, relationships, controls, and meaning.
- Conforming syntax distinguishes tags, elements, attributes, Boolean presence,
  void elements, nesting, and character references.
- The document language, title, character encoding, and viewport metadata provide
  meaning and operating assumptions for the whole page.
- Native elements provide tested semantics and behavior before customization.
- Headings form a hierarchy; landmarks divide the page into navigable regions.
- Links navigate and buttons act.
- Images need alternatives chosen from purpose, not a mechanical description.
- Data tables require captions and explicit header relationships.
- Simple tables use scope; genuinely complex tables may require row/column groups
  or explicit header IDs, and are often clearer when divided.
- Form labels, identifiers, and submitted names have different responsibilities.
- GET and POST express different request intentions, and successful-control rules
  determine which form fields become submitted data.
- Ordinary text fields and file bytes require different form encodings;
  multipart upload hints never replace server validation.
- Browser validation improves experience but never establishes server trust.
- Accessible error recovery combines a failure-specific title, summary, linked
  field messages, preserved safe values, state, and deliberate focus behavior.
- Accessible names identify controls; descriptions supply supporting instructions
  or constraints without replacing concise labels.
- The source, DOM, and accessibility tree are related but distinct.
- Accessibility work considers content that is Perceivable, Operable,
  Understandable, and Robust, and combines automated and human evidence.

## Glossary

Table 2.7 collects the terms that instructors can reuse for retrieval questions
and that students can revisit while explaining their laboratory evidence.

**Table 2.7 - Session 2 glossary**

| Term | Working definition |
|---|---|
| Accessibility tree | A semantic representation of relevant roles, names, states, values, and relationships exposed to assistive technologies. |
| Accessible name | Text by which software identifies an interface element to a user. |
| Accessible description | Supporting information associated with an element, such as a format hint or constraint; it supplements rather than replaces the accessible name. |
| ARIA | Accessible Rich Internet Applications specifications for adding accessibility semantics when native HTML cannot express a needed pattern. |
| Boolean attribute | An attribute whose presence represents true and whose absence represents false; the string `"false"` does not turn it off. |
| Character reference | HTML syntax such as `&amp;` or `&lt;` used to represent a character that would otherwise be interpreted as markup. |
| Content model | The HTML rules that define which kinds of content an element may contain. |
| Constraint validation | Browser mechanisms that evaluate form constraints such as required values and ranges. |
| Element | A parsed HTML component with a defined meaning, attributes, content when permitted, and relationships in the document tree. |
| Form encoding | The representation used to serialize successful controls, such as `application/x-www-form-urlencoded` or `multipart/form-data`. |
| Focus | The current destination for keyboard input. |
| Landmark | A major navigable page region such as navigation or main content. |
| Native semantics | Meaning and behavior supplied by a standard HTML element. |
| Tag | Source markup that begins or ends an HTML element; a tag is not the complete element. |
| Semantic HTML | Element selection based on the meaning and relationship of content. |
| Successful control | A form control whose name and current value are included in submitted form data under the form rules. |
| Text alternative | Text that communicates the relevant purpose or information of non-text content. |
| Void element | An HTML element such as `img` or `input` that cannot contain child content and has no closing tag. |
| WCAG | Web Content Accessibility Guidelines, organized around the principles Perceivable, Operable, Understandable, and Robust. |

## Primary references and further reading

1. WHATWG, [HTML Living Standard - Web developer edition](https://html.spec.whatwg.org/dev/).
2. W3C, [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/).
3. W3C, [WAI-ARIA Authoring Practices - Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/).
4. MDN, [HTML: A good basis for accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML).
5. MDN, [Web forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms).
6. MDN, [Core modules: Semantic HTML](https://developer.mozilla.org/en-US/curriculum/core/semantic-html/).
7. Manuel Matuzovic, [Web Accessibility Cookbook](https://accessibility-cookbook.com/).
8. MDN, [Basic HTML syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax).
9. W3C Web Accessibility Initiative, [Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/).
10. Jennifer Niederst Robbins, *Learning Web Design*, 6th edition, O'Reilly Media, 2025.
11. Adam Silver, *Form Design Patterns*, Smashing Media.
12. Heydon Pickering, *Inclusive Components*.

## What changes often?

HTML's central semantics and WCAG 2.2 requirements are stable. Browser validation
messages, accessibility-tree inspection panels, and assistive-technology details
vary by platform and version. Technical review date: **22 September 2026**.

## Session reflection

- Which native element prevented the most custom work in your form?
- Which keyboard observation changed your design?
- Which accessibility claim still requires evidence from a representative user?
