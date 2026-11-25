# Web Programming: From the Platform to Production

## Makeup Midterm Examination - Foundations Edition (v21)

**Name and surname:** ____________________________________  
**Student number:** ______________________________________  
**Date:** ____________________  
**Duration:** 80 minutes  
**Total:** 100 points

### Instructions

- This examination contains 40 multiple-choice questions worth 2.5 points each.
- Select the single best answer. Every question has five choices (A-E) and only one correct answer.
- Unless stated otherwise, assume standards-conforming modern browsers and the course environment described in Sessions 0-3.

---

## Part I - Workstation and Development Workflow

### 1.

A student changes `index.html`, refreshes the browser, and still sees the old page. Which sequence supplies the most useful first evidence?

A. Reinstall Git, then rename the repository.  
B. Add `!important` to every CSS declaration.  
C. Confirm the file was saved, the server is serving that same folder, and Network shows a fresh document request.  
D. Create an empty `package.json` beside the HTML file.  
E. Push the unverified change to GitHub.

### 2.

The local server occupies one terminal and continues printing request records. Where should the student run `npm test` without stopping that server?

A. In a second terminal opened at the same repository root  
B. In the browser address bar  
C. In the CSS file  
D. In a terminal opened in `C:\Users\Student`, regardless of the project location  
E. Tests cannot run while a local server is active.

### 3.

Which Git sequence most responsibly records a completed lab?

A. Push first, then edit, then save.  
B. Commit every file on the computer without inspection.  
C. Delete `.git`, recreate it, and force-push.  
D. Rename the project after each change.  
E. Inspect changes, stage the intended files, commit a meaningful unit, and push the commit.

### 4.

`npm run serve:week03:starter` reports that the script does not exist, although `package.json` is visible in the current directory. What is the best next check?

A. Whether the monitor is connected  
B. Open `package.json` and verify the exact script name under `scripts`  
C. Whether the HTML contains an `<npm>` element  
D. Reinstall the browser  
E. Change the page URL to a GitHub address

---

## Part II - How the Web Works

### 5.

For `https://events.example.edu:443/calendar?week=4#labs`, which pair is correct?

A. Host is `/calendar`; path is `events.example.edu`.  
B. Scheme is `events`; query is `#labs`.  
C. Port is `4`; fragment is `443`.  
D. Path is `/calendar`; fragment is `labs`.  
E. Query is `https`; host is `week=4`.

### 6.

A DNS lookup has returned an IP address, but the browser then reports a connection timeout. What does the evidence support?

A. HTML parsing failed before DNS.  
B. Name resolution succeeded; a later connection or reachability step failed.  
C. The CSS cascade rejected the address.  
D. The URL fragment caused DNS to time out.  
E. Git did not contain the server.

### 7.

Which value is a syntactically valid Internet Protocol version 4 (IPv4) address?

A. `192.168.1.42`  
B. `192.168.1.300`  
C. `192.168.1`  
D. `192:168:1:42`  
E. `campus.192.1.42`

### 8.

Why can `2001:db8::40` contain two adjacent colons?

A. They separate a URL scheme from its path.  
B. They mark an encrypted port number.  
C. They convert the value to IPv4.  
D. They indicate an invalid empty field.  
E. In IPv6 notation, one `::` can compress one or more consecutive all-zero groups.

### 9.

A browser requests `/events` and receives status `301` with a `Location: /calendar` header. What should this response be understood to mean?

A. The server could not resolve its own DNS name.  
B. The browser must render an empty page permanently.  
C. The resource is being redirected, and the client may make another request to `/calendar`.  
D. The response proves `/calendar` has the same content forever.  
E. The CSS file moved the page.

### 10.

Which exchange correctly places responsibilities?

A. HTTP chooses physical Wi-Fi frequencies; CSS routes packets.  
B. DNS renders HTML; TCP selects heading levels.  
C. HTML encrypts the transport; Git authenticates the certificate.  
D. IP addresses and routes packets; transport supports end-to-end delivery; HTTP expresses Web requests and responses.  
E. JavaScript must replace all network layers.

### 11.

Which two URLs are normally same-origin?

A. `https://hub.example.edu/events` and `http://hub.example.edu/events`  
B. `https://hub.example.edu/events` and `https://hub.example.edu:443/news`  
C. `https://hub.example.edu` and `https://api.example.edu`  
D. `https://hub.example.edu:8443` and `https://hub.example.edu`  
E. `https://hub.example.edu` and `file:///hub.html`

### 12.

The Network panel shows the document as `200`, but `styles.css` as `404`. Which conclusion is best?

A. DNS failed for the whole page.  
B. The document and stylesheet are necessarily identical.  
C. HTTPS forbids CSS.  
D. The HTML request succeeded, while the requested stylesheet resource was not found.  
E. The stylesheet loaded but lost the cascade.

### 13.

Which statement about `localhost` is correct?

A. It refers back to the same computer from which the request is made; a local server must still be listening on the selected port.  
B. It is a public university domain available to everyone.  
C. It always maps to the course GitHub repository.  
D. It means the browser opened a file without HTTP.  
E. It guarantees that port 8000 is active.

### 14.

Why is an HTTP response header different from its body?

A. Headers are CSS and the body is DNS.  
B. Headers are visible pixels; the body is a Git commit.  
C. Headers carry response metadata and control information; the body carries the representation, when one is present.  
D. Headers exist only for errors.  
E. A response cannot contain both.

### 15.

A page at `https://hub.example.edu` requests data from `https://api.example.edu`. Why may the browser apply cross-origin controls?

A. The paths are too short.  
B. Both addresses use HTTPS.  
C. The response is JavaScript Object Notation.  
D. The page contains a form.  
E. The hosts differ, so the origins differ even though the scheme is the same.

### 16.

Which ordered description best represents a first navigation to a named HTTPS site?

A. Render pixels, commit Git, then resolve DNS.  
B. Resolve the name, establish the required connection/security, exchange HTTP messages, parse resources, and render.  
C. Run CSS, assign an IPv4 address, then create the URL.  
D. Send the fragment to DNS, then download the browser.  
E. Open the database before contacting any server.

---

## Part III - Semantic HTML and Accessible Forms

### 17.

Which document outline is most coherent for a page with one main title and two peer sections?

A. `<h3>Campus Hub</h3><h1>Events</h1><h5>News</h5>`  
B. `<div>Campus Hub</div><b>Events</b><b>News</b>`  
C. `<h1>Campus Hub</h1><h2>Events</h2><h2>News</h2>`  
D. `<h1>Events</h1><h1>News</h1><h4>Campus Hub</h4>`  
E. Heading levels should be chosen only from their default font sizes.

### 18.

A control performs “Save event” without navigating. Which element provides the most appropriate native semantics?

A. `<a>Save event</a>` without `href`  
B. `<input type="text" value="Save event">`  
C. `<span onclick="save()">Save event</span>`  
D. `<div role="presentation">Save event</div>`  
E. `<button type="button">Save event</button>`

### 19.

Which markup gives a text input a visible and programmatically associated label?

A. `<span>Email</span><input placeholder="Email">`  
B. `<input name="email"><p>Email</p>`  
C. `<label>Email</label><div contenteditable>`  
D. `<input id="email"><label for="mail">Email</label>`  
E. `<label for="email">Email</label><input id="email" name="email" type="email">`

### 20.

What is the best alternative text for a linked image containing the Campus Hub logo when the link returns to the Campus Hub home page?

A. `alt="Campus Hub home"`  
B. `alt="blue and orange rectangular image"`  
C. `alt="logo.png"`  
D. No `alt` attribute  
E. `alt="image link graphic"`

### 21.

Which element is intended for the page's dominant content, excluding repeated site navigation and footer material?

A. `<aside>`  
B. `<nav>`  
C. `<header>`  
D. `<main>`  
E. `<small>`

### 22.

A table lists event, date, and venue. What is the best treatment of its header cells?

A. Use ordinary `<td>` cells and bold them only with CSS.  
B. Use empty cells so screen readers infer the labels.  
C. Use appropriate `<th>` cells, with scope relationships where needed.  
D. Replace the table with spaces and line breaks.  
E. Put the entire table inside an image.

### 23.

A form uses `method="get"` for a public event search. Where are its successful controls ordinarily represented?

A. Only in browser memory  
B. In the URL query component as name-value pairs  
C. In the fragment after `#`  
D. In the CSS stylesheet  
E. In a Git commit message

### 24.

Which field grouping is most appropriate for three mutually exclusive attendance choices?

A. Three unrelated text inputs  
B. A heading followed by three links  
C. A `<div>` whose meaning is supplied only by color  
D. One checkbox with three values  
E. A `<fieldset>` with a `<legend>` and radio buttons sharing one `name`

### 25.

Which statement about document language is correct?

A. `lang` is needed only when CSS uses colors.  
B. The browser always infers language perfectly from the filename.  
C. The document's primary language should be declared, and language changes in passages can be marked locally.  
D. `lang` replaces character encoding.  
E. A page may declare language only on headings.

### 26.

An instructional diagram explains a network path not otherwise described in the prose. What accessibility treatment is strongest?

A. Provide concise `alt` identifying the diagram and an adjacent detailed explanation of the meaningful relationships.  
B. Use `alt="diagram"` and supply no other information.  
C. Hide the diagram from all users.  
D. Put all explanation in the filename.  
E. Use color alone to distinguish every path.

### 27.

Which statement about native form types is correct?

A. `type="email"` proves that the address exists.  
B. `type="date"` guarantees identical visual presentation in every browser.  
C. `type="number"` is ideal for every digit sequence.  
D. Appropriate types can provide input affordances and constraint checks, but the server must still validate meaning and authority.  
E. Native types eliminate the need for labels.

### 28.

After an invalid submission, which response is least helpful and least accessible?

A. Preserve valid values and identify each correction.  
B. Clear the entire form and display only “Error” in red at the page bottom.  
C. Provide a linked summary and field-level messages.  
D. Use text in addition to visual styling.  
E. Move focus predictably to useful error information when appropriate.

---

## Part IV - CSS, Layout, and Responsive Design

### 29.

Given `.card { color: navy; }` and `main .card { color: teal; }` in the same layer and origin, both matching the same element, which color normally wins?

A. Navy, because the shorter selector is faster  
B. Teal, because `main .card` has greater specificity  
C. Both colors are averaged  
D. The declaration with fewer characters wins  
E. Neither declaration is valid

### 30.

A child paragraph has no `color` declaration, while its parent has `color: #12355b`. What normally happens?

A. The paragraph becomes transparent.  
B. Every property from the parent is copied.  
C. The paragraph must use black.  
D. `color` is inherited, so the paragraph normally uses `#12355b`.  
E. The paragraph is removed from normal flow.

### 31.

What does `margin-inline: auto` commonly accomplish on a block with a constrained inline size and available horizontal space?

A. It centers the block in the inline direction.  
B. It makes the block a grid container.  
C. It vertically aligns text.  
D. It removes the block's padding.  
E. It forces right-to-left writing.

### 32.

Why can `min-width: 0` be necessary on a flex item containing a long unbroken string?

A. It enlarges the font automatically.  
B. It changes the flex axis.  
C. It permits the item to shrink below its automatic minimum, allowing intended wrapping or overflow handling.  
D. It disables the cascade.  
E. It converts the string to an image.

### 33.

Which declaration creates responsive Grid columns that remain at least `16rem` wide and share extra space?

A. `grid-template-columns: 16rem 16rem 16rem;`  
B. `display: flex-column;`  
C. `columns: auto;`  
D. `position: grid;`  
E. `grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));`

### 34.

An element has `position: absolute`. Relative to what is it normally positioned?

A. Its containing block, commonly established by the nearest positioned ancestor  
B. Always the physical screen  
C. The last CSS rule in the file  
D. The Git repository root  
E. The browser's Network panel

### 35.

What is the main accessibility purpose of `@media (prefers-reduced-motion: reduce)`?

A. Increase animation speed for all users.  
B. Remove semantic HTML.  
C. Disable keyboard input.  
D. Provide a reduced-motion experience for users who express that preference.  
E. Make the page print in grayscale.

### 36.

A component must adapt to the width of the article column that contains it, not to the whole viewport. Which tool best expresses that dependency?

A. A viewport media query only  
B. A fixed pixel width  
C. A container query  
D. An HTML table  
E. A browser-brand selector

### 37.

Why is `height: 100vh` sometimes fragile for a content page?

A. It always disables scrolling.  
B. It converts all lengths to pixels.  
C. It works only in print.  
D. It prevents inherited color.  
E. Content or dynamic mobile viewport controls can make a rigid height clip or overflow; a minimum height or dynamic viewport unit may fit the requirement better.

### 38.

Which selector is best for showing a focus ring primarily during keyboard-style focus interaction?

A. `:focus-visible`  
B. `:hover-only`  
C. `:visited-focus`  
D. `::keyboard`  
E. `[focus=mouse]`

### 39.

If the root font size is `18px`, what computed length is `2rem`?

A. `2px`  
B. `18px`  
C. `20px`  
D. `36px`  
E. It depends only on the element's own font size.

### 40.

At `320px` width, a page has horizontal scrolling. Which debugging action is most disciplined?

A. Hide all overflow immediately.  
B. Inspect which element exceeds the viewport, identify the responsible computed size or unbreakable content, then repair that constraint and retest.  
C. Add a second viewport meta element.  
D. Scale the entire page to 50 percent.  
E. Remove all semantic elements.

---

## Answer Sheet

| Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---:|:---:|---:|:---:|---:|:---:|---:|:---:|
| 1 |  | 11 |  | 21 |  | 31 |  |
| 2 |  | 12 |  | 22 |  | 32 |  |
| 3 |  | 13 |  | 23 |  | 33 |  |
| 4 |  | 14 |  | 24 |  | 34 |  |
| 5 |  | 15 |  | 25 |  | 35 |  |
| 6 |  | 16 |  | 26 |  | 36 |  |
| 7 |  | 17 |  | 27 |  | 37 |  |
| 8 |  | 18 |  | 28 |  | 38 |  |
| 9 |  | 19 |  | 29 |  | 39 |  |
| 10 |  | 20 |  | 30 |  | 40 |  |
