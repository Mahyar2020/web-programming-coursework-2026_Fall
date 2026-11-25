# Session 5 - The Document Object Model, Events, and Forms

Chapter 4 taught the JavaScript language without pretending that JavaScript and
the browser are the same thing. We can now cross that boundary deliberately.
The browser gives JavaScript a live representation of the page, reports user and
system activity as events, and implements the behavior of forms. Together these
facilities turn the Campus Hub document into an interactive application.

This chapter starts with one visible paragraph and one button, then develops the
same ideas into a searchable event explorer. The progression matters. A student
who can explain each small boundary—source markup to live document, event to state,
state to rendering, and form control to validated data—can later reason about a
framework such as React instead of merely memorizing its syntax.

## Session map

Table 5.1 moves from observation to a tested feature. Each phase asks students
to state what they expect before using the browser to gather evidence.

**Table 5.1 - Session 5 learning sequence and inspectable evidence**

| Phase | Central question | Evidence |
|---|---|---|
| Observe | What page does JavaScript actually interact with? | Source HTML is compared with the live Document Object Model |
| Select and change | How does code find and update the intended element? | A selector, null check, and safe mutation produce a visible result |
| Model | Where should application state live? | One state object is transformed into a repeatable rendering |
| Respond | How does the browser report interaction? | Event properties and the propagation path are inspected |
| Collect | How does a form become structured data? | Named controls appear in `FormData` |
| Validate | How are useful and accessible errors reported? | Native constraints and custom messages are tested with keyboard and screen-reader-oriented evidence |
| Engineer | How do larger interfaces remain predictable and efficient? | DOM work is batched, observed, and contained behind explicit component boundaries |
| Verify | How do we know behavior remains correct? | Pure model tests pass and browser output is inspected |

## Prerequisites

Complete Chapters 2–4 or be able to read semantic HyperText Markup Language
(HTML), elementary Cascading Style Sheets (CSS), and JavaScript functions,
arrays, objects, modules, and tests. Work from the
repository root—the folder that contains `package.json`. Chapter 0 explains how
to find that folder and how to distinguish a server terminal from an ordinary
command terminal.

## Learning outcomes

After this chapter, you should be able to:

1. distinguish HTML source text from the browser's live Document Object Model (DOM);
2. explain the roles of `window`, `document`, nodes, elements, and text nodes;
3. select elements with CSS selectors and handle a missing result safely;
4. traverse nearby elements without depending on a fragile page shape;
5. update text, attributes, properties, classes, and data attributes deliberately;
6. create, clone, insert, replace, and remove nodes;
7. choose `textContent` instead of `innerHTML` for untrusted plain text;
8. keep application state separate from its rendered representation;
9. explain event dispatch, capture, target, and bubble phases;
10. distinguish `event.target` from `event.currentTarget`;
11. use default prevention and propagation control only for their actual purposes;
12. apply event delegation to dynamic collections;
13. remove listeners or use an abort signal when their lifetime ends;
14. read form controls with `FormData` and interpret successful controls;
15. use native constraint validation and add custom validation accessibly;
16. preserve server-side validation as the final trust boundary;
17. provide visible, programmatic, and focus-aware feedback;
18. explain progressive enhancement and the consequences of disabled JavaScript;
19. debug DOM and event behavior with browser developer tools; and
20. build and test the interactive Campus Hub event explorer;
21. separate DOM reads from writes to avoid repeated synchronous layout work;
22. use `MutationObserver` when code must observe changes made outside its own state model;
23. explain light DOM, shadow DOM, event retargeting, and the purpose of custom elements;
24. choose events that preserve native keyboard, pointer, form, and assistive-technology behavior; and
25. explain form ownership, reset, serialization encoding, and file-input boundaries.

---

# 1. From HTML source to a live document

Consider this source file:

```html
<p id="status">Three events are available.</p>
```

On disk it is a sequence of characters written in **HyperText Markup Language
(HTML)**. The browser parses those characters and creates objects connected as a
tree. JavaScript interacts with those objects, not directly with the bytes in
the file. This object system is the **Document Object Model (DOM)**. “Document”
refers to the loaded page; “object model” means that its parts are exposed as
objects with properties and methods. A browser application programming
interface (API) is the set of properties and methods that browser objects make
available to JavaScript.

Figure 5.1 follows one source fragment into its live representation and then
back to pixels. A DOM change can alter what the user sees, but it does not rewrite
the original HTML file on disk.

<!-- figure:dom-source-live-tree -->

## 1.1 The important browser objects

The browser exposes several related objects. They are not interchangeable.
Table 5.2 shows both what each object represents and the work it supports.

**Table 5.2 - Browser objects and their responsibilities**

| Name | Meaning | Example responsibility |
|---|---|---|
| `window` | The browsing context's global object | viewport, timers, location, global events |
| `document` | The loaded HTML document | select and create document nodes |
| `Node` | The general tree-object interface | parent/child relationships, removal |
| `Element` | A node created from an element such as `<button>` | attributes, classes, selector matching |
| `HTMLElement` | HTML-specific element behavior | `hidden`, `dataset`, focus behavior |
| `Text` | Character data inside an element | the words displayed inside a paragraph |

The rows also express an inheritance relationship: an
`HTMLElement` is an `Element`, and an `Element` is a `Node`; a `Text` object is
also a `Node`, but it is not an element.

An element is a node, but not every node is an element. Text and comments are
nodes too. This explains why `childNodes` may include whitespace text nodes while
`children` contains only element children. Figure 5.2 shows the useful
specialization rather than suggesting that these are unrelated object types.

<!-- figure:dom-interface-map -->

## 1.2 Source, DOM, and rendered page can differ

The parser may repair invalid nesting. Browser extensions may insert nodes.
JavaScript may change the tree after loading. Therefore:

- **View page source** shows the received source text;
- the **Elements** panel shows the current DOM; and
- the page viewport shows the current visual rendering.

When debugging, first decide which of these three kinds of evidence answers your
question. Looking only at source cannot explain a node created later by
JavaScript.

## 1.3 What the parser does, and when the document is ready

The browser reads HTML in order. It recognizes a start tag, creates an element
object, attaches it at the correct point in the tree, and continues through the
document. Text between tags becomes text nodes. A closing tag changes where new
nodes will be attached. This is why the page source is not a screenshot: it is
input to a parsing process that produces a structured tree.

The parser also encounters other resources. A stylesheet may affect when the
browser can paint useful output; an ordinary script can pause parsing while it
is fetched and run. A script marked `defer` waits until parsing is complete,
then runs before the `DOMContentLoaded` event. A module script is deferred by
default. The `load` event waits for more dependent resources, such as images, so
it is later than needed for ordinary DOM selection.

## 1.4 When can a script safely select the document?

This book loads application modules in the document head with `type="module"`:

```html
<script type="module" src="app.js"></script>
```

Module scripts are deferred: the browser finishes parsing the document before
executing them. The elements in the body therefore exist when `app.js` runs. A
classic script loaded in the head without `defer` can run before later elements
exist. Another valid option is to register a `DOMContentLoaded` listener when a
script may be loaded at different points. Do not add both a defer strategy and
a readiness listener without a reason; one clear loading contract is easier to
understand.

---

# 2. Select and traverse elements

`document.querySelector()` accepts a CSS selector and returns the first matching
element, or `null` when no match exists.

```js
const status = document.querySelector("#status");

if (!status) {
  throw new Error("Expected #status in the document.");
}
```

The check is not ceremonial. A renamed `id`, wrong page, or script-loading error
can produce `null`; the explicit error identifies the broken HTML–JavaScript
contract close to its cause. Optional chaining such as `status?.remove()` is
appropriate only when absence is genuinely acceptable.

`document.querySelectorAll()` returns a static `NodeList` of all current matches.
“Static” means that a later matching element is not silently added to that
already returned list. Convert only when an array operation is needed:

```js
const cards = [...document.querySelectorAll(".event-card")];
const fullCards = cards.filter((card) => card.dataset.remaining === "0");
```

`getElementById("status")` is also clear for one identifier. Consistency and
readability matter more than inventing a performance competition for a small
page.

Selectors can be scoped to an element instead of the whole document:

```js
const cards = eventList.querySelectorAll(".event-card");
```

This searches descendants of `eventList`, which reduces accidental matches in
another part of the page. A selector is a contract with the markup. If the HTML
class is renamed, the JavaScript selector must be reviewed. Prefer a stable
identifier or data attribute when it better describes the behavior than a class
whose name exists only for visual styling.

## 2.1 Move through a local relationship

Selectors find elements from a root. Traversal moves from an element already in
hand:

- `closest(selector)` searches the element and then its ancestors;
- `matches(selector)` asks whether the element itself matches;
- `parentElement`, `children`, `firstElementChild`, `nextElementSibling`, and
  `previousElementSibling` express structural relationships.

Prefer a relationship that states intent:

```js
const card = saveButton.closest("[data-event-id]");
```

Avoid brittle chains such as `parentElement.parentElement.children[1]`. A small
HTML wrapper change would break that chain even though the meaningful
“containing event card” relationship remained intact.

For a one-time lookup, `querySelectorAll()` is often preferable to a live
collection because the result is a stable snapshot. If the interface changes,
query again when you need current matches. This distinction matters when you
loop over elements while adding or removing them: a live collection can change
under the loop, while a static list retains the matches it captured.

---

# 3. Read and change the DOM safely

Finding an object does nothing visible by itself. A program must read or change
the appropriate interface.

## 3.1 Text, HTML, and security

Use `textContent` for plain text:

```js
status.textContent = "Showing 2 matching events.";
```

The browser treats the assigned characters as text. By contrast, `innerHTML`
parses a string as markup. If that string contains untrusted data, an attacker
may introduce dangerous elements or attributes; this is a common route to
Document Object Model cross-site scripting (DOM XSS), a form of cross-site
scripting (XSS). Figure 5.3 contrasts the two data paths.

<!-- figure:safe-dom-content -->

Use `innerHTML` only when HTML parsing is genuinely required and the markup is
trusted or correctly sanitized with a reviewed sanitizer. Escaping one or two
characters by hand is not a general sanitizer.

## 3.2 Attributes and properties are related, not identical

HTML attributes provide initial declarative information. DOM properties expose
current object state. For a checkbox, `getAttribute("checked")` describes whether
the attribute exists in markup, while `checkbox.checked` reports the current
checked state after user interaction.

```js
checkbox.checked = true;                 // current state
button.setAttribute("aria-pressed", "true"); // expose the current pressed state
```

Use dedicated properties when they express the state accurately. Use
`setAttribute`, `getAttribute`, `hasAttribute`, and `removeAttribute` when the
attribute itself is the intended interface. The `aria-pressed` attribute is
part of Accessible Rich Internet Applications (ARIA), which provides
accessibility semantics when native HTML alone does not express a control's
state.

## 3.3 Classes, visibility, and data attributes

`classList` changes named presentation states without rebuilding the entire
class string:

```js
card.classList.toggle("event-card--saved", isSaved);
panel.hidden = !isOpen;
card.dataset.eventId = event.id;
```

`dataset.eventId` corresponds to `data-event-id`. Data attributes are useful for
stable identifiers or small declarative metadata. They are strings, visible to
the client, and not secure storage. Do not put secrets or authoritative prices
in them.

Direct `style` assignments create inline styles and are appropriate for values
that are truly calculated at runtime. Prefer classes for named visual states so
CSS retains responsibility for presentation.

## 3.4 Create, clone, insert, replace, and remove

The browser can construct nodes one at a time:

```js
const item = document.createElement("li");
item.textContent = "Robotics night";
eventList.append(item);
```

For repeated, semantically rich markup, an HTML `<template>` keeps the structure
readable and inert until cloned:

```js
const fragment = cardTemplate.content.cloneNode(true);
fragment.querySelector(".event-card__title").textContent = event.title;
eventList.append(fragment);
```

`append` adds content, `prepend` adds it first, `before` and `after` place
siblings, `replaceChildren` deliberately replaces a container's content, and
`remove` detaches a node. A `DocumentFragment` groups work without introducing
an unwanted wrapper element.

Moving an existing element with `append()` moves that same object; it does not
make a copy. Use `cloneNode(true)` when a deep copy is intended, and remember
that copying an `id` can create duplicate identifiers. A `<template>` avoids
showing its contents before cloning. When populating a clone, check that the
expected descendants exist just as you would for elements in the main document.

## 3.5 Attributes, properties, and form-control state in practice

The attribute/property distinction becomes especially visible in controls. A
text input's `value` property is its current value, while its markup attribute
supplies the initial value. After a user types, reading the attribute may still
return the old text. Read the property for current input.

Likewise, `disabled` and `readOnly` are not interchangeable. A disabled control
cannot be interacted with and is generally omitted from form submission. A
read-only text control can still receive focus and its value can be submitted.
Use the state that matches the interaction you intend, not merely the one that
looks convenient.

---

# 4. State first, rendering second

An interactive application needs to remember facts that are not merely visual:
the current search query, selected category, availability filter, and saved
event identifiers. These facts form **application state**.

```js
let state = {
  query: "",
  category: "all",
  availableOnly: false,
  savedIds: new Set(),
};
```

The page is a representation of that state. Treating CSS classes or displayed
words as the only source of truth makes behavior hard to predict. Instead, an
event produces new state and `render()` makes the DOM agree with it. Figure 5.4
shows the loop. All arrows are used together; they are not alternative modes.

<!-- figure:state-render-loop -->

```js
function render() {
  const visible = deriveVisibleEvents(events, state);
  eventList.replaceChildren(...visible.map(createEventCard));
  savedCount.textContent = String(state.savedIds.size);
}
```

An effective render is **idempotent** for the same state: calling it twice should
not duplicate cards or invent new state. Pure functions such as
`deriveVisibleEvents(events, state)` are especially testable because they do not
need a browser.

Rebuilding a short teaching list is clear and acceptable. Very large interfaces
may preserve and update identified nodes to reduce work and protect focus,
selection, and media state. Frameworks automate parts of that reconciliation;
they do not remove the underlying state-and-render reasoning.

This model separates three questions. The **event handler** identifies what
happened, the **state transition** records the new fact, and the **rendering
function** derives what should be visible. Saving an event changes the saved
identifier set; filtering asks whether an event belongs in the current results;
rendering creates the cards and count. Keeping these jobs distinct makes the
application easier to test and prevents a CSS class from becoming the only
record of important application data.

---

# 5. Events: how the browser reports activity

An **event** is an object describing an occurrence: a pointer activation, key
press, changed form value, submitted form, completed resource, or many other
conditions. Code registers a listener rather than repeatedly asking whether the
occurrence happened.

```js
saveButton.addEventListener("click", (event) => {
  console.log(event.type);
});
```

The browser calls the listener later and supplies the event object. This is
event-driven execution: registration happens now; invocation happens when the
event is dispatched.

## 5.1 Target, current target, and propagation

When a user activates a button nested inside a card, the event is dispatched
along a path. It travels down in the **capture phase**, reaches the **target
phase**, and normally travels back up in the **bubble phase**. Figure 5.5 follows
one click; it is a single dispatch with phases, not three separate clicks.

<!-- figure:event-propagation -->

- `event.target` is the deepest object from which the event was dispatched.
- `event.currentTarget` is the object whose listener is currently running.

The two can differ when an ancestor listens for bubbled events. Prefer
`currentTarget` in a listener attached directly to the intended control; use
`target` carefully when implementing delegation.

Some events do not bubble in the same way. `focus` and `blur`, for example, have
bubbling alternatives `focusin` and `focusout`. A shadow tree can also retarget
events; `event.composedPath()` exposes the propagation path permitted across
that boundary.

## 5.2 Listener options and lifetime

The third argument to `addEventListener` can be an options object:

```js
const controller = new AbortController();

window.addEventListener("resize", updateLayout, {
  passive: true,
  signal: controller.signal,
});

controller.abort(); // removes listeners using this signal
```

- `capture: true` listens during capture;
- `once: true` removes the listener after its first invocation;
- `passive: true` promises not to call `preventDefault()` in that listener;
- `signal` ties listener lifetime to an `AbortController`.

Alternatively, call `removeEventListener` with the same event type, function
reference, and capture setting. Removing obsolete listeners avoids duplicated
behavior and prevents detached interface objects from being retained needlessly.

## 5.3 Three methods that solve different problems

`event.preventDefault()` cancels a cancelable browser default, such as form
navigation. It does not stop bubbling. `event.stopPropagation()` stops the event
from continuing along the propagation path. `event.stopImmediatePropagation()`
also prevents later listeners on the same object from running. Broad propagation
stops can hide events from other components and analytics; use them only when
the interaction contract requires it.

## 5.4 Event delegation

Cards can be replaced during every render. Attaching a listener to every new
button would require repeated setup. Instead, attach one listener to their
stable container and identify the relevant bubbled event.

```js
eventList.addEventListener("click", (event) => {
  const button = event.target.closest(".event-card__save");
  if (!button || !eventList.contains(button)) return;

  const card = button.closest("[data-event-id]");
  if (!card) return;
  save(card.dataset.eventId);
});
```

Figure 5.6 shows that delegation uses propagation plus a selector; it is not a
special browser event type.

<!-- figure:event-delegation -->

The containment check matters when a listener can observe a match nested inside
another component. Delegation works best for a collection with shared behavior.
Direct listeners remain simpler for one stable control.

## 5.5 Choose the event that represents the user's intent

`click` represents activation and works for a native button with pointer and
keyboard input. Do not recreate button keyboard behavior on a `<div>`.
`input` reports value changes as they occur; `change` usually reports a committed
change. `submit` belongs on the form and covers button activation and Enter-key
submission. Pointer events unify mouse, pen, and touch input where coordinates or
gestures are genuinely needed. Keyboard listeners are appropriate for
keyboard-specific commands, not as a substitute for semantic controls.

For text input, `input` usually fires as the value changes. `change` generally
fires when a value is committed, which can be later for text fields. A user
typing with an input method editor (IME) may produce composition events while
forming one character. Avoid treating every intermediate composition string as
a finished search if that would disrupt the user. For ordinary small filters,
`input` is appropriate, but test the expected interaction with the input
methods your audience uses.

JavaScript can also dispatch a `CustomEvent` to communicate a meaningful
application event between components. A custom event is not a substitute for a
native `submit` or `click` when one already describes the user action. When you
create a custom event, decide whether it should bubble and what data belongs in
its `detail` field. Document event names and payload shapes as carefully as any
other interface.

---

# 6. Forms turn controls into data

A form is more than a visual grouping. It defines controls, names, values,
validation constraints, and a submission contract. JavaScript should cooperate
with this native model.

```html
<form id="event-filter">
  <label for="query">Search events</label>
  <input id="query" name="query" type="search">

  <label>
    <input name="availableOnly" type="checkbox">
    Show events with seats
  </label>
  <button type="submit">Apply filters</button>
</form>
```

The `id` connects the label to the input. The `name` identifies submitted data.
An input without a name can still appear on screen but normally contributes no
entry to form submission.

The label relationship is functional, not decorative. Clicking a label usually
focuses its control, and assistive technology can announce the control's name.
For related choices, use `<fieldset>` with a `<legend>` so the group has a
programmatic name. A placeholder is not a replacement for a visible label: it
can disappear while the user types and may have insufficient contrast.

## 6.1 Read successful controls with FormData

```js
const data = new FormData(filterForm);
const query = String(data.get("query") ?? "");
const availableOnly = data.get("availableOnly") === "on";
```

`FormData` follows the browser's form rules. Generally, enabled named controls
are **successful controls**. An unchecked checkbox contributes no entry; controls
inside a disabled fieldset generally do not contribute; multiple controls may
share a name, so use `getAll()` where multiple values are expected. File inputs
produce `File` objects rather than ordinary strings.

The submit button used to submit a form can contribute its own name and value.
Modern event handling can construct `new FormData(form, event.submitter)` when
that distinction matters.

**Table 5.3 - Common form controls and the entries they contribute**

| Markup and current state | Typical `FormData` result | Teaching point |
|---|---|---|
| `<input name="query" value="robot">` | `query` -> `"robot"` | A text value is serialized as text. |
| Checked checkbox named `availableOnly` | `availableOnly` -> `"on"`, unless a `value` is specified | A checkbox contributes only when checked. |
| Unchecked checkbox with the same name | No `availableOnly` entry | Absence is not an empty string; interpret it deliberately. |
| Two checked controls named `topic` | Two `topic` entries | Use `getAll("topic")` to retain both. |
| `<select name="category">` | `category` -> selected option's value | The value can differ from the visible option label. |
| Disabled named control | Normally no entry | Disabled controls are not successful controls. |
| `<input type="file" name="poster">` | `poster` -> a `File` object | File data is not an ordinary text value. |

Table 5.3 describes common cases, not every rule in the HTML Standard. A form's
`method` and `action` define the normal submission destination and request
method. A `GET` form places successful values in the URL query, which is useful
for shareable searches and filters. A `POST` form sends values in the request
body and is normally used when an operation changes server state. `POST` is not
automatically private or secure; HTTPS and appropriate server controls still
matter. Do not put passwords, tokens, or private data in a `GET` query string,
where values can appear in history, logs, and copied URLs.

## 6.2 Handle submission at the form boundary

```js
filterForm.addEventListener("submit", (event) => {
  event.preventDefault();
  state = readFilterState();
  render();
});
```

Listening for the button's click would miss some submissions. The form's
`submit` event expresses the actual operation. Calling `form.requestSubmit()`
behaves like a user submission, including validation and the submit event.
Calling `form.submit()` directly bypasses those steps and is rarely the desired
choice.

Inside a form, a `<button>` defaults to submit behavior unless its type is
specified. Write `type="submit"` for the form's main action and
`type="button"` for a control that should only perform a local action. This
small declaration prevents a save or expand button from unexpectedly
submitting the form.

Figure 5.7 shows the complete boundary. Native validation occurs before an
ordinary submit event. JavaScript may enhance the response, but the server must
validate again because clients can be modified or bypassed.

<!-- figure:form-submit-validation -->

---

# 7. Validation that helps rather than punishes

HTML provides useful constraints: `required`, appropriate input types, `min`,
`max`, `minlength`, `maxlength`, `step`, and `pattern`. Use them when they express
the real rule.

```html
<label for="email">University email</label>
<input id="email" name="email" type="email" required
       aria-describedby="email-help email-error">
<p id="email-help">Use the address where confirmations should arrive.</p>
<p id="email-error"></p>
```

The Constraint Validation API exposes the result:

```js
if (!form.checkValidity()) {
  form.reportValidity();
}
```

`checkValidity()` checks and returns a Boolean. `reportValidity()` also asks the
browser to present its native feedback. Each control has `validity` flags such
as `valueMissing`, `typeMismatch`, `patternMismatch`, `tooShort`, and
`rangeOverflow`, plus a localized `validationMessage`.

## 7.1 Custom rules

Use `setCustomValidity(message)` when a real rule cannot be represented by
attributes. An empty string clears the custom error.

```js
function validateDateRange() {
  endDate.setCustomValidity("");
  if (startDate.value && endDate.value && endDate.value < startDate.value) {
    endDate.setCustomValidity("End date must not be earlier than start date.");
  }
}
```

Revalidate when either related value changes and before submission. Never leave
an obsolete custom message set after the user corrects the value.

Native constraints communicate common rules without requiring custom code.
`required` checks that a value is present; `type="email"` checks a
browser-defined email-like syntax, not whether an address exists or belongs to
the person. `min` and `max` constrain numeric or date values, while `step`
limits allowed increments. `pattern` uses a regular expression for a value's
expected shape. Choose constraints that describe the real rule, and explain any
rule the browser cannot infer.

When a control is invalid, inspect `validity.valid` and the specific flags
before choosing a message. The `invalid` event fires on invalid controls and
does not bubble in the ordinary way. During an attempted submission, the browser
may focus an invalid field and show native feedback before it dispatches the
form's `submit` event. If native messages are replaced, the application becomes
responsible for clear, accessible error text and predictable focus management.

## 7.2 Accessible error and status feedback

Color alone does not identify an error. Provide text that states what happened
and how to correct it. Associate field-specific help and errors with the control,
for example through `aria-describedby`. After an invalid submission, an error
summary can link to affected controls, and focus can move to the summary or first
invalid control when that movement is predictable and useful.

For results that update without navigation, a stable `role="status"` region can
announce a concise outcome:

```html
<p id="filter-status" role="status" aria-live="polite"></p>
```

Create the live region before the update and change its text afterward. Do not
announce every keystroke with a long message. Preserve the user's entered values
after an error. These practices support everyone, including keyboard users,
screen-reader users, people with low vision, and people correcting a simple typo.

Avoid moving focus after every live filter update. The status message can report
the result count while focus remains in the search field. When submission fails,
moving focus to an error summary can be useful because the user explicitly asked
to submit. These are different moments and deserve different focus behavior.

Client-side validation improves feedback; it is not a security boundary. The
server must validate authorization, data types, lengths, ranges, relationships,
and business rules using data it receives.

---

# 8. Progressive enhancement and failure boundaries

**Progressive enhancement** begins with meaningful HTML and adds CSS and
JavaScript without making the underlying task unnecessarily dependent on them.
A real search form can submit to a server when JavaScript is unavailable, while
JavaScript can intercept the same submission for a faster in-page experience.
That baseline works only when the server's `action` actually implements the
search. An empty action on a static teaching server reloads the current document
with query parameters; it does not filter records by itself.

The Campus Hub teaching lab uses in-memory sample data, so interactive filtering
requires JavaScript. The solution includes a `<noscript>` explanation and
meaningful page structure, but this is a graceful explanation rather than a
fully working no-JavaScript search. A production version should either render
the initial events on the server and give the form a functioning server action,
or clearly state which feature requires scripting. In a production application,
decide explicitly which operations must work without client scripting and
design the server contract accordingly.

Treat the following as separate failure boundaries:

1. the HTML or JavaScript resource may fail to load;
2. a selector contract may no longer match;
3. data may have an unexpected shape;
4. a listener may run twice or not at all;
5. rendering may destroy focus or stale state may overwrite new state;
6. validation may reject valid input or accept unsafe input; and
7. an accessibility announcement may be absent or excessively noisy.

Specific boundaries lead to specific evidence and useful error messages.

---

# 9. Guided laboratory: Campus Hub event explorer

The laboratory integrates DOM selection, state, rendering, delegation, forms,
accessibility, and pure-model tests. Figure 5.8 shows the completed browser
output. It is an evidence screenshot, not a conceptual illustration.

<!-- media:week-05-browser-output -->

## 9.1 Start from the correct directory

Open VS Code with the repository folder, then open **Terminal > New Terminal**.
In Windows Command Prompt, verify the project marker:

```text
dir package.json
```

In PowerShell, the equivalent is:

```powershell
Get-Item package.json
```

The command must show the repository's `package.json`. If it does not, do not run
the npm command yet; use `cd` to enter the cloned repository folder.

## 9.2 Run the starter

In the first terminal—the **server terminal**—run:

```text
npm run serve:week05:starter
```

Leave this terminal running. Open `http://localhost:8000/` in the browser. The
server terminal is not a special application; it is simply the terminal whose
current job is the local server. Open a second terminal for tests and Git
commands.

## 9.3 Inspect the four files

The starter contains:

- `index.html`, which declares the form, status region, result container, and
  reusable template;
- `styles.css`, which presents the interface;
- `model.js`, which holds sample data and pure state transformations; and
- `app.js`, which connects browser events to state and rendering.

Follow imports from `app.js` into `model.js`. Then locate each selected `id` in
`index.html`. This establishes the contract before editing.

## 9.4 Complete the model

Implement `seatsRemaining`, `deriveVisibleEvents`, and `toggleSaved`. Do not
mutate the incoming `Set`; return a new one so a state change remains observable.
In the second terminal run:

```text
npm run test:week05
```

Expected evidence ends with `Week 5 DOM, events, forms, and model checks passed.`
If a test fails, read its expected and actual values before changing code.

## 9.5 Complete browser rendering

Select the five required elements and fail clearly if any is missing. Clone the
template for each event. Fill text with `textContent`, store the event identifier
in `data-event-id`, reflect saved state with `aria-pressed`, and replace the
result container's children in one deliberate render. When no event matches,
render a readable empty-state message rather than leaving a large blank area.
Because rendering replaces card nodes, preserve keyboard focus on the same
event's replacement Save button after the user activates it. The tested solution
shows one way to do that; updating only the changed card is another valid design.

## 9.6 Connect events

On the form's `input` event, construct `FormData`, create updated filter state,
and render. On `submit`, prevent navigation and render the same state. On the
result container's `click`, use delegation and `closest()` to find a save button
and its card.

## 9.7 Verify behavior, accessibility, and evidence

Test all of the following:

1. typing `robot` leaves one matching card;
2. selecting Arts shows the orchestra;
3. “Show events with seats” removes the full orchestra;
4. a saved button changes its text and `aria-pressed` value;
5. the saved count changes;
6. saving with the keyboard returns focus to the updated Save button;
7. a search with no matches displays a useful empty-state message;
8. Tab reaches every control in a logical order;
9. Enter submits the form without a page navigation; and
10. the status region reports the result count.

Open Developer Tools with `F12` or `Ctrl+Shift+I`, choose **Elements**, and find
the event card. Confirm its `data-event-id` and the button's `aria-pressed` state.
Choose **Console** and confirm there are no red errors. Choose **Network**, reload,
and confirm `index.html`, `styles.css`, `app.js`, and `model.js` returned successful
status codes.

## 9.8 Compare with the tested solution

Stop the server with `Ctrl+C`, then run:

```text
npm run serve:week05:solution
```

Comparison is for explanation, not blind copying. For every difference, state
which contract it satisfies. Finally commit your work with a message such as
`Complete Week 5 DOM event explorer` and push to your coursework repository.

---

## 9.9 Advanced investigation: measure before optimizing

The basic laboratory deliberately redraws a short list because the code is easy
to inspect. Now collect evidence about that design rather than guessing about
performance. Open the **Performance** panel, record one filter operation, and
look for the script work followed by style, layout, and paint. Repeat with the
CPU throttling option if the work is too short to see clearly. Record the number
of visible cards, the interaction performed, and the longest task you observed.
This is a comparison exercise, not a benchmark that proves the application will
behave identically on every computer.

Then perform two controlled investigations:

1. save a card and verify that focus returns to the replacement button; and
2. temporarily add a `MutationObserver` to `#event-list`, save or filter once,
   and inspect the delivered mutation records.

Disconnect the observer after the experiment. The application already knows
when its own `render()` changes the list, so keeping an observer permanently
would duplicate its state model. The experiment exists to reveal the boundary,
not to prescribe an observer for every interface.

---

# 10. Advanced DOM engineering: scale without losing the model

The APIs introduced so far are enough to build a real interface. Larger pages
add two pressures: more work can occur in one interaction, and independently
authored components can share one document. The solution is not to abandon the
DOM. It is to make ownership, timing, and evidence explicit.

## 10.1 Read, decide, then write

Changing a class or inserting a node does not necessarily cause an immediate
paint. The browser can defer and combine visual work. Some DOM reads, however,
need current geometry. A call such as `getBoundingClientRect()` may require the
browser to bring style and layout information up to date before returning an
answer. Repeatedly alternating a geometry read with a style write can therefore
force repeated layout work.

```js
// Harder for the browser to batch: read, write, read, write.
for (const card of cards) {
  const width = card.getBoundingClientRect().width;
  card.classList.toggle("event-card--compact", width < 320);
}
```

When the design genuinely needs measurements, collect them first, make the
decision in JavaScript data, and then perform the writes:

```js
const measurements = cards.map((card) => ({
  card,
  width: card.getBoundingClientRect().width,
}));

for (const { card, width } of measurements) {
  card.classList.toggle("event-card--compact", width < 320);
}
```

Figure 5.9 shows the three-stage discipline. This is a reasoning model, not a
claim that every DOM write is expensive. Measure an actual interaction before
adding caches, partial rendering, or scheduling machinery. For responsive
presentation, CSS media and container queries are usually better than measuring
width in JavaScript.

<!-- figure:dom-read-decide-write -->

A `DocumentFragment` or detached template clone can collect several new nodes
before one insertion. That reduces intermediate document changes and keeps
construction code coherent. It does not make inefficient algorithms disappear:
creating ten thousand unnecessary cards is still unnecessary work.

## 10.2 Observe changes made outside your state model

A `MutationObserver` reports batches of DOM changes after they occur. It is
useful when code must respond to changes it did not initiate directly, such as a
third-party widget, an editor, or a custom element observing assigned content.

```js
const observer = new MutationObserver((records) => {
  for (const record of records) {
    console.log(record.type, record.addedNodes.length);
  }
});

observer.observe(eventList, {
  childList: true,
  subtree: true,
});

// Later, when the observing responsibility ends:
observer.disconnect();
```

Figure 5.10 distinguishes an event from a mutation record. An event reports an
occurrence through a propagation path. A mutation observer receives a later
batch describing tree, attribute, or text changes in its observed scope. It does
not explain the user's intention and should not replace the application's own
state transition. Observe the narrowest useful root and options; observing the
entire document for every possible mutation creates noise and unnecessary work.

<!-- figure:mutation-observer-batch -->

The older mutation events are deprecated. Use `MutationObserver` when mutation
observation is the real requirement. If your own function performed the change,
call the next application step directly instead of waiting to rediscover your
own work through an observer.

## 10.3 Light DOM, shadow DOM, and custom elements

Most elements in this book belong to the document's ordinary tree, often called
the **light DOM** when it is contrasted with a component's shadow tree. A
**shadow root** gives a component an internal DOM subtree with style and selector
encapsulation. The page can place light-DOM children into named or default
`<slot>` positions, but the component retains an internal implementation
boundary.

Figure 5.11 shows these cooperating trees. The shadow tree is not a security
boundary: open shadow roots are inspectable, browser developer tools expose the
structure, and component inputs remain untrusted data. The boundary protects
component structure and styling contracts from accidental coupling.

<!-- figure:shadow-dom-boundary -->

Events may cross a shadow boundary when their `composed` behavior permits it.
Outside the component, the event target can be **retargeted** to preserve the
component boundary; `event.composedPath()` reveals the permitted dispatch path.
This is why code outside a component should listen for a documented public event
instead of depending on an internal button.

A **custom element** is a registered HTML element whose name contains a hyphen,
such as `<campus-event-card>`. Its class can use lifecycle callbacks:

```js
class CampusEventCard extends HTMLElement {
  connectedCallback() {
    if (this.dataset.ready === "true") return;
    this.dataset.ready = "true";
    this.textContent = this.getAttribute("title") ?? "Untitled event";
  }
}

customElements.define("campus-event-card", CampusEventCard);
```

`connectedCallback()` may run more than once when an element is moved or
reconnected, so setup must be repeatable or guarded and cleanup must accompany
long-lived resources. Rich components may use shadow DOM, observed attributes,
slots, and custom events, but none is mandatory for a custom element. Autonomous
custom elements and form-associated custom elements have additional contracts;
they are extension material, not a reason to replace native `<button>`,
`<input>`, or `<form>` behavior.

## 10.4 Choose events by meaning and input independence

Table 5.4 compares common choices. Select the event that represents the task,
then use semantic HTML so browsers supply keyboard and accessibility behavior.

**Table 5.4 - Event choice by user intention and evidence**

| Intention | Prefer | Avoid as the only mechanism | Reason |
|---|---|---|---|
| Activate a native button | `click` | `mousedown` or `keydown` | native activation covers pointer and keyboard behavior |
| React while a form value changes | `input` | polling the value | the event reports user-caused value changes |
| React after a value is committed | `change` | assuming every keystroke is final | commitment timing differs by control type |
| Submit a form | `submit` on the form | only the button's `click` | Enter, assistive technology, and `requestSubmit()` can submit |
| Implement pointer geometry or a gesture | pointer events | mouse-only events | pointer events describe mouse, touch, and pen input |
| Implement a keyboard-specific command | `keydown` with `event.key` | numeric key codes | the command is genuinely keyboard-specific |
| Track focus moving within a component | `focusin` / `focusout` | assuming `focus` bubbles | the bubbling variants support delegation |

Keyboard commands need restraint. Do not override browser, operating-system, or
assistive-technology shortcuts. Respect `event.repeat` when holding a key should
not repeat an action, and avoid interpreting unfinished Input Method Editor
(IME) composition as a completed command. Pointer gestures need a cancellation
path such as `pointercancel`; a user can change direction, the browser can take
over scrolling, or the device can lose contact.

`isTrusted` distinguishes events dispatched by the user agent from events sent
by script, but it is not an authorization mechanism. A genuine click still
comes from an untrusted client. Security decisions remain on the server.

## 10.5 Form ownership, reset, encoding, and files

A control normally belongs to its nearest ancestor `<form>`. The `form`
attribute can associate it with a form elsewhere in the same document:

```html
<form id="event-search" action="/events" method="get"></form>

<label for="query">Search events</label>
<input id="query" name="query" form="event-search">
<button type="submit" form="event-search">Search</button>
```

Use this feature when layout requires separation; keeping controls inside the
form is easier to read when no such constraint exists. `form.elements` exposes
the owned controls, and `control.form` identifies the owner.

Reset is also a contract. A reset returns controls toward their initial values;
it does not automatically reset a separate JavaScript state object. Listen for
`reset` when application state must be synchronized, preferably allowing the
browser's default reset and then deriving state from the resulting controls.
Avoid using reset as a generic “clear” button without explaining its effect.

The `formdata` event permits a program to inspect or add entries after a
`FormData` object is constructed for the form. It is useful for derived values
that truly belong to submission, but hidden inputs are often clearer when the
value is declarative. Never add an authoritative price, role, or permission and
expect the server to trust it.

For a normal navigation, the form's method and encoding determine how entries
cross the network:

- `GET` represents them in the Uniform Resource Locator (URL) query;
- `POST` with the default `application/x-www-form-urlencoded` encoding sends
  name-value data in the request body; and
- a form containing file uploads normally uses `multipart/form-data`.

The `accept` attribute on a file input is a user-interface hint, not proof of a
file's content or safety. Browsers do not reveal an arbitrary local path to
JavaScript. Treat selected files as untrusted data; the server must enforce
size, type, authorization, storage, and malware-handling policy. This chapter
stops at the form boundary. Chapter 6 will send requests programmatically, and
later server chapters will validate and store received data.

---

# 11. Debugging clinic

Table 5.5 pairs a visible symptom with the first piece of evidence to inspect.

**Table 5.5 - Symptoms, likely meanings, and first evidence**

| Symptom | Likely meaning | First evidence to inspect |
|---|---|---|
| White page | script error or hidden/empty content | Console error and Network response |
| `Cannot set properties of null` | selector found no element | selector spelling and live Elements panel |
| Click appears twice | duplicate listeners or nested activation | Event Listener Breakpoints and call stack |
| Click on icon is ignored | code compared `target` only with the button | inspect `target`, then use `closest()` |
| Form reloads the page | submit default was not prevented | submit listener and Console logging |
| Checkbox value seems missing | unchecked checkboxes are not successful controls | inspect `FormData` entries |
| Error remains after correction | custom validity was not cleared | `validationMessage` and validation handler |
| New cards do not respond | listeners were attached only to old children | delegation boundary or listener setup |
| Focus jumps while typing | rendering replaced the focused element | active element before and after render |
| Scrolling feels delayed | a wheel or touch listener may block the default | listener options and Performance recording |
| Observer callback floods the Console | scope or options are too broad, or the callback mutates what it observes | observer root, options, and callback writes |
| A component click has an unexpected target | a shadow boundary retargeted the event | `target`, `currentTarget`, and `composedPath()` |
| Reset changes controls but not results | JavaScript state did not follow the form reset | `reset` listener and post-reset state derivation |

Use breakpoints instead of inserting many guesses. In the **Sources** panel, add
an Event Listener Breakpoint for `click` or `submit`. When execution pauses,
inspect the call stack, `event.target`, `event.currentTarget`, state, and selected
elements. In **Elements**, the Event Listeners view reveals registered listeners.
The goal is to identify the violated contract, not merely make the symptom vanish.

---

# 12. Exercises

1. Draw the DOM tree for `<main><h1>Hub</h1><p>Open</p></main>`, including text nodes.
2. Explain why changing `textContent` does not rewrite `index.html` on disk.
3. Write a safe selection and failure check for `#saved-count`.
4. Compare `children` with `childNodes`.
5. Predict whether a previously stored `querySelectorAll(".card")` result grows
   after another card is appended.
6. Replace unsafe `panel.innerHTML = userName` with the appropriate operation.
7. Explain the difference between the `checked` attribute and property.
8. Write code that adds `event-card--full` only when `remaining === 0`.
9. Explain why `data-event-id` is useful but cannot securely hold a secret.
10. Create an `<li>` containing the text “Web seminar” and append it to `list`.
11. State the invariant that an idempotent `render()` should satisfy.
12. For a click on a `<span>` inside a button whose ancestor list has the
    listener, identify `target` and `currentTarget`.
13. Put capture, target, and bubble in dispatch order.
14. Explain why `preventDefault()` does not stop propagation.
15. Implement a one-use listener.
16. Explain when delegation is preferable to one listener per child.
17. Read all values named `topic` from `FormData`.
18. Explain why an unchecked checkbox may not appear in `FormData`.
19. Compare `requestSubmit()` and `submit()`.
20. Add a custom rule that rejects an end date earlier than a start date and
    clears the message after correction.
21. Design accessible feedback for three invalid fields.
22. Explain why client-side validation cannot authorize a student enrollment.
23. State one progressively enhanced alternative for event search.
24. Design one pure unit test and one browser interaction test for saving an event.
25. Given a checked checkbox with `name="availableOnly"` and `value="yes"`,
    what should `FormData.get("availableOnly")` return? What happens when it is
    unchecked?
26. Explain why `type="email"` cannot prove that an address exists.
27. Choose `disabled` or `readOnly` for a control whose value should still be
    submitted but should not be edited. Explain the keyboard consequence.
28. A render replaces the Save button currently focused by the keyboard user.
    Describe the failure and one safe repair.
29. A static server receives a GET query from the lab's empty form action. Why
    does that not implement search, and what would a production baseline need?
30. Explain how an input method editor can affect live filtering and name one
    way to avoid disrupting composition.
31. Give one suitable use for a bubbling `CustomEvent` and one reason not to
    replace the native `submit` event with a custom event.
32. A loop reads `getBoundingClientRect()` and then changes a class on each card.
    Rewrite its plan so geometry reads occur before DOM writes. Explain what
    evidence would justify the change.
33. Design a narrowly scoped `MutationObserver` that reports cards added to
    `#event-list`, and state when it must be disconnected.
34. Compare a user event with a mutation record. Which one should represent the
    intention “save this event,” and why?
35. Explain light DOM, shadow DOM, event retargeting, and the role of
    `composedPath()` in one component interaction.
36. A custom element attaches a listener in `connectedCallback()`. Explain why
    reconnecting it can duplicate behavior and give one safe design.
37. Choose the event for each task: activating a native button, live text
    filtering, committed selection, form submission, and a pen-drawing gesture.
38. Explain why `event.isTrusted === true` cannot authorize deletion of a
    university record.
39. Build a form whose search control and submit button are outside the `<form>`
    element but owned by it. State when this structure is justified.
40. Compare URL-encoded and multipart form submission. Explain why `accept` on a
    file input does not validate the uploaded file.

# 13. Worked answers

## Answer 1

`main` is the root element in the fragment. It has `h1` and `p` element
children. `h1` contains a text node `Hub`; `p` contains a text node `Open`.
Whitespace between tags may also become text nodes, which is why element-only
traversal is often clearer for structural work.

## Answer 2

The browser parsed the file into in-memory objects. Assigning `textContent`
changes one of those live objects and therefore its rendering. Browsers do not
silently edit a developer's source file; reloading can restore the server's
original document unless the state is stored elsewhere.

## Answer 3

```js
const savedCount = document.querySelector("#saved-count");
if (!savedCount) throw new Error("Expected #saved-count in index.html.");
```

The error identifies both the missing contract and the file to inspect.

## Answer 4

`children` contains element children only. `childNodes` can also contain text,
comment, and other node types. Source indentation can therefore change
`childNodes` without changing the meaningful element structure.

## Answer 5

It does not grow. `querySelectorAll()` returns a static `NodeList` representing
the matches at selection time. Run the selector again to obtain the new card.

## Answer 6

```js
panel.textContent = userName;
```

This displays the characters as text instead of parsing them as potentially
dangerous markup.

## Answer 7

The attribute describes the markup's initial/default declaration. The property
reports and controls the live checked state, including user changes. Interactive
logic normally reads `checkbox.checked`.

## Answer 8

```js
card.classList.toggle("event-card--full", remaining === 0);
```

The second argument makes the intended Boolean rule explicit.

## Answer 9

The attribute keeps a stable event identifier near its rendered card and is easy
to read during delegated handling. It is visible in developer tools and can be
changed by the client, so a server must not trust it as a secret or authority.

## Answer 10

```js
const item = document.createElement("li");
item.textContent = "Web seminar";
list.append(item);
```

## Answer 11

Given the same state and data, repeated rendering should produce the same
observable interface without duplicate content or additional state changes.

## Answer 12

`target` is the nested `span`, the deepest dispatch target. `currentTarget` is
the ancestor list while its delegated listener is running. `closest("button")`
can move from the span to the activated control.

## Answer 13

Capture travels from ancestors toward the target, target processing occurs at
the target, and bubble normally travels back through ancestors.

## Answer 14

Default action and propagation are separate mechanisms. `preventDefault()`
cancels a cancelable browser action; the event can still reach ancestor
listeners unless propagation is separately stopped.

## Answer 15

```js
button.addEventListener("click", initializeOnce, { once: true });
```

The browser removes this registration after its first invocation.

## Answer 16

Delegation is useful when many current or future children share behavior and
their events bubble to one stable container. A direct listener is simpler for a
single stable control or for behavior that does not propagate appropriately.

## Answer 17

```js
const topics = new FormData(form).getAll("topic").map(String);
```

`getAll()` preserves multiple successful controls with the same name.

## Answer 18

Successful-control rules omit an unchecked checkbox, so no entry is produced.
Code must interpret absence deliberately, commonly as `false` for a Boolean
checkbox.

## Answer 19

`requestSubmit()` follows interactive submission: it performs constraint
validation and dispatches `submit`. `submit()` directly initiates submission and
bypasses those important steps.

## Answer 20

```js
function validateRange() {
  end.setCustomValidity("");
  if (start.value && end.value && end.value < start.value) {
    end.setCustomValidity("End date must not be earlier than start date.");
  }
}
start.addEventListener("input", validateRange);
end.addEventListener("input", validateRange);
```

Clearing first ensures that a corrected range can become valid.

## Answer 21

Place a concise error summary near the form heading, link each item to its
control, associate a specific message with each field using `aria-describedby`,
mark invalid state where appropriate, retain entered values, and move focus to a
predictable correction point after the failed submission. Do not rely on red
borders alone.

## Answer 22

The browser is controlled by the user; scripts and requests can be changed or
bypassed. The server must authenticate the student, check authorization and
capacity, validate the request, and enforce the final enrollment rule.

## Answer 23

Give the form a real server `action` and `method`. Without JavaScript it can
navigate to a server-rendered results page; with JavaScript it can update the
current result region while retaining the same request semantics.

## Answer 24

A pure unit test passes a `Set` and identifier to `toggleSaved` and verifies that
the returned set contains the identifier while the original remains unchanged.
A browser test activates a rendered Save button and verifies its text,
`aria-pressed`, visual class, and saved count. The tests cover different
boundaries and complement rather than replace each other.

## Answer 25

The checked control contributes `"yes"` because an explicit `value` replaces
the default checkbox value `"on"`. When unchecked, it contributes no entry at
all. Code should translate that absence into `false` deliberately rather than
mistaking it for an empty string.

## Answer 26

The browser checks a format that resembles an email address. It does not
contact the mail system or establish that the mailbox exists, that the user can
receive messages there, or that the address belongs to the person completing
the form. Verifying ownership requires an appropriate server-side process, such
as sending a confirmation link.

## Answer 27

Use `readOnly` for a text value that should remain focusable and be included in
ordinary form submission. A disabled control cannot be edited, is normally
skipped in keyboard navigation, and is omitted from form data. The server must
still decide whether the submitted value is authoritative.

## Answer 28

Replacing the whole list removes the focused button from the document. Keyboard
focus may fall back to the document body, so the next Tab can move to an
unexpected location. A clear repair is to remember the focused event ID before
rendering and focus the replacement button for that same event afterward, if
it remains visible. For a larger interface, update only the changed card or
use keyed reconciliation instead of rebuilding every node.

## Answer 29

The empty action resubmits to the current URL, but the static file server does
not interpret query parameters as filter instructions. The address changes;
the displayed event data does not. A production baseline needs a server route
that reads, validates, and applies the query, or a server-rendered initial page
that already contains the relevant results. Client-side filtering can then
enhance that functioning baseline.

## Answer 30

An input method editor may emit intermediate values while the user composes a
character or word. Filtering on each intermediate value can make results jump
before composition is complete. Listen for composition events and defer the
filter until composition ends, or inspect `isComposing` and skip intermediate
updates. Test with the writing systems and input methods students use.

## Answer 31

A reusable date-range component might dispatch a bubbling `date-range-change`
event with normalized start and end values in `detail`, allowing an ancestor to
respond without knowing the component's internal controls. Form submission
already has a native event, default action, validation behavior, and keyboard
semantics. Replacing it with a custom event would force the application to
recreate those contracts.

## Answer 32

First collect every required rectangle into ordinary data, then compute the
compact/not-compact decisions, and finally change classes in a second pass. This
removes the repeated read-after-write pattern that can force layout information
to be recomputed. The change is justified when a Performance recording shows
that layout work is material to a real interaction on representative content
and devices. A short list that already responds promptly does not need elaborate
optimization, and CSS container queries may remove the JavaScript measurement
altogether.

## Answer 33

```js
const list = document.querySelector("#event-list");
if (!list) throw new Error("Expected #event-list.");

const observer = new MutationObserver((records) => {
  for (const record of records) {
    for (const node of record.addedNodes) {
      if (node instanceof Element && node.matches(".event-card")) {
        console.log("Card added:", node.dataset.eventId);
      }
    }
  }
});

observer.observe(list, { childList: true });
// observer.disconnect() when this observing responsibility ends.
```

The root is the event list and the options request only direct child-list
changes. Add `subtree: true` only if descendant changes are part of the stated
contract. Disconnect when the view is destroyed, the experiment ends, or the
owner no longer needs notifications.

## Answer 34

A click or a documented custom event expresses an occurrence or intention and
travels through an event path. A mutation record describes a DOM change after
it happened and may be delivered in a batch. “Save this event” should be handled
from the native button activation or a domain-level custom event, because that
is where intention is known. Observing the later text or class mutation would
confuse a rendered consequence with the action that caused it.

## Answer 35

Light DOM is the ordinary page content, including children supplied to a
component. A shadow root owns an internal subtree and can place supplied light
content through slots. When a composed event crosses the shadow boundary, code
outside can see a retargeted target that protects internal structure.
`composedPath()` exposes the propagation path that the platform permits. An
outside listener should depend on the component's public event contract, not an
internal selector revealed by developer tools.

## Answer 36

An element can be removed and inserted again, so `connectedCallback()` can run
more than once. Adding the same logical behavior with a new anonymous listener
on every connection can produce duplicate calls. A safe design can guard
one-time setup, use an `AbortController` per connection and abort it in
`disconnectedCallback()`, or attach stable internal listeners once in the
constructor when the relevant nodes already exist. The choice must match the
resource lifetime.

## Answer 37

Use `click` for native-button activation, `input` for live filtering, `change`
for a committed selection, `submit` on the form for submission, and pointer
events for a pen gesture. These choices follow the meaning of the task. The
button and form choices retain keyboard and assistive-technology paths; pointer
events provide pressure, contact, and cancellation information without assuming
a mouse.

## Answer 38

`isTrusted` says that the user agent dispatched the event rather than the page
calling `dispatchEvent()`. It does not establish the user's identity,
authorization, current role, ownership of the record, or integrity of the
request sent over the network. A client can still construct a different HTTP
request. The server must authenticate the user and enforce authorization for
the specific record and operation.

## Answer 39

```html
<form id="event-search" action="/events" method="get"></form>
<label for="query">Search events</label>
<input id="query" name="query" form="event-search">
<button type="submit" form="event-search">Search</button>
```

Both controls name the form owner with `form="event-search"`, so they participate
in its submission despite not being descendants. This is justified when a real
layout or component boundary prevents nesting. Ordinary descendant markup is
easier to understand and should remain the default.

## Answer 40

The default URL-encoded form format represents ordinary name-value pairs compactly
in a request body. `multipart/form-data` separates entries into parts and can
carry file content and metadata. The `accept` attribute helps a file picker show
suitable choices, but extensions and reported media types can be misleading and
client rules can be bypassed. The server must enforce size, recognized content
type, authorization, storage location, and security scanning policy.

---

# 14. Retrieval quiz

1. What does DOM stand for? **Document Object Model.**
2. Does a DOM mutation normally edit the source file? **No; it changes the live
   in-memory document.**
3. What does `querySelector` return when no element matches? **`null`.**
4. Is the result of `querySelectorAll` live? **No; it is a static `NodeList`.**
5. Which property should display untrusted plain text? **`textContent`.**
6. What does `classList.toggle(name, condition)` do? **It adds the class when the
   condition is true and removes it when false.**
7. What is `dataset.eventId` backed by? **The `data-event-id` attribute.**
8. Why use a `<template>`? **It stores inert reusable structure that can be
   cloned and populated.**
9. What is application state? **The facts the interface must remember in order
   to determine its behavior and rendering.**
10. What is the event phase order? **Capture, target, bubble.**
11. What is `event.target`? **The deepest dispatch target.**
12. What is `event.currentTarget`? **The object whose listener is currently
    running.**
13. Does `preventDefault` stop bubbling? **No.**
14. What listener option removes a listener after one call? **`once: true`.**
15. What is event delegation? **Handling shared child behavior at a stable
    ancestor by using propagation and target matching.**
16. Which event represents form submission? **`submit` on the form.**
17. Why does a form control need a `name`? **The name identifies its submitted
    data entry.**
18. Which `FormData` method retrieves repeated values? **`getAll()`.**
19. What does `checkValidity()` return? **A Boolean result of constraint
    validation.**
20. How is a custom validity error cleared? **Call `setCustomValidity("")`.**
21. Why must a server validate again? **The client can be altered or bypassed.**
22. What is progressive enhancement? **Starting with a meaningful baseline and
    adding capabilities without unnecessarily destroying that baseline.**
23. Which developer-tools panel shows the live DOM? **Elements.**
24. What does an event-listener breakpoint provide? **Paused execution at event
    handling with the call stack and runtime values available for inspection.**
25. Does a checked checkbox always contribute the string `"on"`? **No; an
   explicit `value` attribute supplies its submitted value.**
26. Does `type="email"` verify mailbox ownership? **No; it checks only an
   email-like syntax.**
27. Does a disabled named input contribute to `FormData`? **Normally no.**
28. Why might rendering move focus unexpectedly? **Replacing a focused node
   removes that node from the document.**
29. Does a static file server apply a GET query as an application filter? **No;
   a server route must implement that behavior.**
30. Why consider composition events for live search? **An input method editor
   can produce temporary text while a character is being composed.**
31. What belongs in `CustomEvent.detail`? **Small, documented data that
   listeners need from the event.**
32. Why group geometry reads before DOM writes? **To avoid a repeated
   read-after-write pattern that can force synchronous layout work.**
33. When should a `MutationObserver` be disconnected? **When its observing
   responsibility or owning component lifetime ends.**
34. Does a mutation record express user intention? **No; it describes a DOM
   change after it occurred.**
35. Is shadow DOM a security boundary? **No; it is an encapsulation boundary.**
36. Which method reveals the permitted event path across component boundaries?
   **`event.composedPath()`.**
37. Which event normally represents native-button activation? **`click`.**
38. Can `event.isTrusted` replace server authorization? **No.**
39. Which attribute associates an external control with its form owner?
   **`form`.**
40. Which form encoding normally carries file uploads? **`multipart/form-data`.**

---

# 15. Summary and glossary

The DOM is the browser's live object tree, not the HTML file itself. JavaScript
selects and safely changes that tree, while explicit application state makes
rendering repeatable. Events arrive along a propagation path; understanding
target and current target makes direct handling and delegation predictable.
Forms already provide names, values, submission, and constraint validation.
Professional JavaScript enhances those semantics, gives accessible feedback,
and preserves server validation as the final trust boundary. At larger scales,
read-decide-write batching prevents accidental layout churn, mutation observers
watch changes outside an application's own state path, and shadow DOM plus custom
elements establish explicit component contracts without replacing native
semantics.

Table 5.6 gathers the terms used throughout this session.

**Table 5.6 - Session 5 glossary**

| Term | Meaning |
|---|---|
| DOM | Live object representation of a loaded document |
| node | General object in the document tree |
| element | Node produced from an HTML element |
| state | Facts an application remembers to determine behavior and output |
| render | Make the interface represent current state |
| event | Object describing an occurrence dispatched by the browser or code |
| propagation | Event movement through capture, target, and usually bubble phases |
| delegation | Ancestor handling of matching descendant events |
| default action | Browser behavior associated with an event, such as form navigation |
| successful control | Form control whose name and value contribute to submitted data |
| constraint validation | Browser model for checking declared form requirements |
| progressive enhancement | Adding capabilities to a meaningful baseline experience |
| mutation observer | API that delivers batches describing changes in an observed DOM scope |
| light DOM | Ordinary document children supplied outside a shadow tree |
| shadow DOM | Encapsulated component subtree attached to a shadow host |
| event retargeting | Adjustment of an exposed event target across a component boundary |
| custom element | Registered HTML element with a hyphenated name and defined lifecycle |
| form owner | Form associated with a control by ancestry or the `form` attribute |

## Instructor guide

Allow 12–14 contact hours plus independent laboratory time. Use the first meeting
for source-versus-DOM inspection and safe mutation, the second for state,
rendering, and propagation, and the third for forms, validation, accessibility,
and the integrated lab. Ask students to predict `target`, `currentTarget`, and
`FormData` entries before running code. Grade the laboratory from browser
behavior, model tests, keyboard evidence, and an explanation of the contracts—not
from a screenshot alone. Treat Section 10 as an advanced reference workshop:
profile the small application before discussing optimization, demonstrate one
mutation batch, and inspect a shadow-root event path without requiring every
student to build a component library.

## Standards and further study

The standards below define browser behavior. The teaching resources show useful
ways to sequence the same ideas in university courses. Use standards and current
browser documentation for precise behavior; lecture notes are valuable for
explanation and practice, not as a replacement for the standard.

- WHATWG, [*DOM Living Standard*](https://dom.spec.whatwg.org/). The authoritative
  model for document nodes, event dispatch, and related interfaces.
- WHATWG, [*HTML Living Standard: Forms and form-control infrastructure*](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html).
  The detailed rules for form submission, successful controls, and constraint
  validation.
- WHATWG, [*HTML Living Standard: Custom elements*](https://html.spec.whatwg.org/multipage/custom-elements.html)
  and [*Shadow trees*](https://dom.spec.whatwg.org/#shadow-trees). The normative
  component lifecycle, tree boundary, event-path, and retargeting models.
- W3C, [*Pointer Events*](https://www.w3.org/TR/pointerevents3/). The unified
  pointer model for mouse, pen, and touch input, including cancellation.
- MDN, [*Document Object Model events*](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events)
  and [*Event bubbling*](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling).
  Accessible explanations of registration, propagation, and delegation.
- MDN, [*Using HTML form validation and the Constraint Validation API*](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
  and [*Client-side form validation*](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation).
  Practical examples of native constraints, custom rules, and the server-side
  validation boundary.
- W3C Web Accessibility Initiative, [*Form validation*](https://www.w3.org/WAI/tutorials/forms/validation/)
  and [*User notifications*](https://www.w3.org/WAI/tutorials/forms/notifications/).
  Guidance for labels, error messages, and outcome announcements.
- Stanford CS142, [*DOM and Events lecture collection*](https://web.stanford.edu/class/cs142/lectures.html).
  A university sequence that separates the DOM model from event behavior before
  students build browser applications.
- University of Washington CSE 154, [*JavaScript and the DOM*](https://courses.cs.washington.edu/courses/cse154/20su/lectures/lec06-dom-events/index.html),
  [*More events and DOM manipulation*](https://courses.cs.washington.edu/courses/cse154/20sp/lectures/lec07-js-events-styles/index.html),
  and [*POST, form submission, and validation*](https://courses.cs.washington.edu/courses/cse154/20sp/lectures/lec15-post-form/index.html).
  Examples of lecture-and-laboratory sequencing across DOM, events, and forms.

Technical review date: 25 November 2026. Standards are living documents;
recheck browser behavior and accessibility guidance before a new academic-year
release.
