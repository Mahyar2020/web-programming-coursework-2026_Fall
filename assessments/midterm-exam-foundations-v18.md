# Web Programming: From the Platform to Production

## Midterm Examination - Foundations Edition (Revised v18)

**Name and surname:** ____________________________________  
**Student number:** ______________________________________  
**Date:** ____________________  
**Duration:** 80 minutes  
**Total:** 100 points

### Instructions

- This examination contains 40 multiple-choice questions.
- Each question is worth 2.5 points.
- Select the single best answer for each question.
- Each question has exactly five choices (A-E) and only one correct answer.
- Unless a question states otherwise, assume standards-conforming modern browsers and the course environment described in the book.

---

## Part I - Workstation and Development Workflow

### 1.

A student has installed Node.js, but has not yet run any course command. Which evidence best demonstrates that the installation is ready for the course workflow?

A. The installer file is present in the Downloads folder.  
B. `node --version` reports the required version and the repository's verification script completes successfully.  
C. The Node.js website opens in a browser.  
D. A desktop shortcut for Node.js exists.  
E. The student can open an HTML file by double-clicking it.

### 2.

Running `npm test` produces an `ENOENT` error whose path ends with `C:\Users\Student\package.json`. The actual repository is inside `C:\Users\Student\Documents\GitHub\coursework`. What is the most appropriate first action?

A. Reinstall npm globally.  
B. Create a new empty `package.json` in `C:\Users\Student`.  
C. Delete the repository and clone it again.  
D. Change to the repository root, confirm that `package.json` is present, and rerun the command.  
E. Open the page with a `file:` URL instead.

### 3.

Which statement correctly distinguishes saving, committing, and pushing?

A. Saving writes file changes; committing records selected content in local Git history; pushing transfers commits to a remote.  
B. Saving and committing both upload changes, while pushing publishes a website.  
C. Saving stages files, committing runs tests, and pushing creates a branch.  
D. Saving writes only to browser storage, committing writes to disk, and pushing writes to Git.  
E. Saving creates a local snapshot, committing sends it to GitHub, and pushing merges it into `main`.

### 4.

The Campus Hub page is visible, but the Network panel is empty. Which action provides the most direct useful evidence without changing the project?

A. Install a browser extension that records traffic.  
B. Restart the computer and reinstall the browser.  
C. Add a new `<script>` element to the page.  
D. Commit the current files before continuing.  
E. Keep the Network panel open and reload the page so the request is recorded.

---

## Part II - How the Web Works

### 5.

Which statement most accurately describes the relationship between the Internet and the Web?

A. They are two names for the same protocol.  
B. The Internet is a browser feature implemented by the Web.  
C. The Internet is the network infrastructure; the Web is an application that uses it to exchange linked resources.  
D. The Web is the physical network, while the Internet is its HTML content.  
E. The Internet handles only email, while the Web handles only websites.

### 6.

In `https://hub.campus.example:8443/events?day=monday#details`, which component is normally retained and interpreted by the client rather than sent as part of the HTTP request target?

A. `#details`  
B. `day=monday`  
C. `/events`  
D. `8443`  
E. `hub.campus.example`

### 7.

Which three values determine a Web origin?

A. Host, path, and query  
B. Scheme, path, and fragment  
C. Scheme, query, and port  
D. Scheme, host, and effective port  
E. Host, query, and fragment

### 8.

What is DNS's primary contribution during an ordinary navigation to a named website?

A. It encrypts the HTTP response body.  
B. It resolves the hostname to address information used to contact a service.  
C. It converts HTML into the DOM.  
D. It verifies that the site's information is truthful.  
E. It selects which CSS rules win the cascade.

### 9.

A browser receives a styled HTML error page together with HTTP status `404`. Which conclusion is correct?

A. No server was contacted because only `200` responses come from servers.  
B. DNS necessarily failed before the browser could send a request.  
C. The browser generated the HTML without receiving a response.  
D. HTTPS converted a successful response into an error.  
E. The server responded, and the response reported that the requested resource was not found.

### 10.

Which claim about HTTPS is correct?

A. It proves that all information presented by the site is accurate.  
B. It guarantees that the application contains no security defects.  
C. It protects the connection and authenticates the certified server identity, but it does not guarantee that the application is honest or correct.  
D. It prevents the server from returning `4xx` or `5xx` responses.  
E. It causes all resources to share the same origin.

### 11.

Why can displaying one Web page result in many HTTP requests?

A. Parsing the document can reveal separate stylesheets, scripts, images, fonts, and data that must also be retrieved.  
B. HTTP requires every HTML element to be requested separately.  
C. DNS repeats the complete page request for every element.  
D. Git creates a request for every committed file.  
E. The browser must contact a different server for every CSS declaration.

### 12.

A Network panel shows `200 OK` for a document request. What can be concluded from that evidence alone?

A. The page is accessible to every user.  
B. The HTML is valid and the displayed information is accurate.  
C. Every subresource also loaded successfully.  
D. The server successfully handled that HTTP request under its semantics, but application correctness still requires other evidence.  
E. The response came from the same origin as every script on the page.

### 13.

Which statement best explains why HTTP is described as stateless?

A. Servers are forbidden from storing application data.  
B. HTTP does not inherently remember a conversation between independent requests; applications add continuity explicitly.  
C. Browsers cannot send cookies or authorization information.  
D. Each response must contain an empty body.  
E. A client may send only one request per connection.

### 14.

Which observation most clearly distinguishes an HTTP-served page from a directly opened local file?

A. The document contains an `<html>` element.  
B. The page is displayed in a browser window.  
C. The source file has an `.html` extension.  
D. The page includes a relative hyperlink.  
E. The address uses `http:` or `https:`, and Network shows a document exchange with a method and status.

### 15.

Which statement correctly distinguishes HTML source from the DOM?

A. The DOM is the original file, while HTML is a screenshot of it.  
B. HTML exists only after JavaScript runs, while the DOM exists before parsing.  
C. HTML is source markup; the DOM is the browser's live parsed tree and may include parser repairs or later script changes.  
D. HTML stores styles, while the DOM stores only network headers.  
E. They must always be character-for-character identical.

### 16.

Which HTML fragment correctly creates a level-one heading followed by a functioning link to `events.html`?

A. `<h1>Campus Events</h1><a href="events.html">View events</a>`  
B. `<h1>Campus Events</h1><a>View events</a>`  
C. `<h2>Campus Events</h2><a href="events.html">View events</a>`  
D. `<h1>Campus Events</h1><button href="events.html">View events</button>`  
E. `<heading>Campus Events</heading><a src="events.html">View events</a>`

---

## Part III - Semantic HTML and Accessible Forms

### 17.

What is the main purpose of semantic HTML?

A. To define the exact colors and spacing of every element  
B. To guarantee that no CSS will be needed  
C. To make every document look the same in all browsers  
D. To communicate the roles and relationships of content and controls  
E. To replace all accessibility testing

### 18.

A designer wants a subsection heading to appear smaller. What is the best implementation?

A. Choose `<h5>` because its default font is smaller, regardless of hierarchy.  
B. Keep the heading level that represents the document hierarchy and change its appearance with CSS.  
C. Replace the heading with a `<div>` and bold text.  
D. Use a placeholder instead of a heading.  
E. Put the subsection inside `<footer>` to reduce its visual importance.

### 19.

When is `<article>` generally more appropriate than `<section>`?

A. Whenever the content needs a border  
B. Whenever the element is the first child of `<main>`  
C. Whenever the content contains a heading  
D. Whenever JavaScript will update the content  
E. When the composition is independently meaningful or reusable, such as a news story or event card

### 20.

A control styled as a blue rectangle opens a details page. Which native element best matches the behavior?

A. `<button type="button">` because all blue controls are buttons  
B. `<div tabindex="0">` because styling determines semantics  
C. `<a href="details.html">` because the control navigates to a resource  
D. `<input type="submit">` because all user actions submit forms  
E. `<span role="presentation">` because navigation is only visual

### 21.

Why is placeholder text not an adequate replacement for a visible, programmatically connected form label?

A. It disappears during entry and does not reliably provide the persistent accessible name and instruction users need.  
B. It is always submitted as the control's value.  
C. It prevents keyboard focus.  
D. It automatically disables browser validation.  
E. It can be used only with `<textarea>`.

### 22.

What is the form-related purpose of a control's `name` attribute?

A. It sets the text shown in the page title.  
B. It determines the control's CSS specificity.  
C. It supplies the control's visible label.  
D. It supplies the key associated with that control's submitted value.  
E. It forces the control to be included even when disabled.

### 23.

Why must a server repeat validation that the browser already performs?

A. Browser validation runs only after the server has accepted the data.  
B. Client-side checks can be bypassed or modified, so the server must protect the operation at its trust boundary.  
C. HTML controls never validate required values.  
D. Server validation is needed only to improve CSS styling.  
E. Repeating validation automatically encrypts the submission.

### 24.

An image is purely decorative and repeats no information needed to understand or operate the page. Which markup is generally appropriate?

A. Omit the `alt` attribute so the browser invents a description.  
B. Use the filename as the alternative text.  
C. Put the image inside a heading.  
D. Set `alt="decorative image"`.  
E. Use `alt=""` so the redundant image is excluded from the accessibility experience.

### 25.

A form contains `<input required="false">`. How will a conforming browser interpret the `required` attribute?

A. The control is optional because the string value is `false`.  
B. The attribute is ignored because it has an invalid value.  
C. The control is required because Boolean attributes are true when present.  
D. The control becomes read-only.  
E. The form can be submitted only with JavaScript.

### 26.

Why is `type="number"` usually a poor choice for a student number or postal code?

A. These are identifiers rather than quantities; number controls can imply arithmetic behavior and can mishandle formatting such as leading zeroes.  
B. Number controls cannot have labels.  
C. Number controls are never keyboard accessible.  
D. These identifiers must always be hidden from users.  
E. A number control sends no value to the server.

### 27.

Which statement correctly compares `disabled` and `readonly` text controls in ordinary form behavior?

A. Both are always excluded from submission.  
B. Both remain editable but cannot receive focus.  
C. `disabled` values are submitted, while `readonly` values are omitted.  
D. A disabled control is ordinarily omitted from submission; a named read-only text control is ordinarily submitted.  
E. `readonly` automatically makes a value trustworthy to the server.

### 28.

A server rejects a submitted form because two fields are invalid. Which response provides the strongest accessible recovery experience?

A. Clear all fields and show only a red border around the form.  
B. Provide a failure-specific page title, a linked error summary, associated field-level messages, appropriate invalid-state/focus handling, and preserve safe valid values.  
C. Show an alert that says only “Invalid input.”  
D. Disable every control and ask the user to reload.  
E. Return `200 OK` with no visible explanation.

---

## Part IV - CSS, Layout, and Responsive Design

### 29.

Which statement best describes the cascade?

A. It selects the first declaration written in the stylesheet.  
B. It applies only to inherited properties.  
C. It always gives inline styles priority over every possible declaration.  
D. It sorts rules only by selector length.  
E. It resolves competing declarations using factors such as origin, importance, layer, specificity, and source order.

### 30.

With the default `content-box` model, an element has `width: 300px`, `padding: 20px` on both sides, and a `2px` border on both sides. What is its outer inline size, excluding margins?

A. `300px`  
B. `322px`  
C. `344px`  
D. `340px`  
E. `384px`

### 31.

Why is the following rule commonly used in a project baseline?

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

A. It makes declared width and height include the element's padding and border, making box sizing easier to reason about.  
B. It forces all elements to have equal dimensions.  
C. It removes all browser default styles.  
D. It changes every element into a flex container.  
E. It prevents content from ever overflowing.

### 32.

Which layout choice best fits a one-dimensional navigation list whose items should wrap when space becomes limited?

A. Absolute positioning  
B. Multi-column layout  
C. A table with one row  
D. Flexbox with wrapping enabled  
E. Floats with fixed widths

### 33.

Which layout choice is most appropriate for a collection of cards that must coordinate rows and columns in two dimensions?

A. Normal inline flow only  
B. CSS Grid  
C. Text alignment  
D. Relative positioning on every card  
E. A sequence of `<br>` elements

### 34.

An event card should change its internal arrangement when the sidebar containing it becomes wider than `20rem`, regardless of the viewport width. Which mechanism best expresses this requirement?

A. A `screen` media query based on device model  
B. JavaScript that checks the operating-system name  
C. A print stylesheet  
D. A fixed width on the card  
E. A container query based on the card container's inline size

### 35.

What is the best principle for choosing a responsive breakpoint?

A. Use only the dimensions of the newest phone.  
B. Add a breakpoint every 100 pixels.  
C. Add it where the content and layout need enough space for a meaningful enhancement.  
D. Use the same breakpoint for every project.  
E. Base it on the user's browser brand.

### 36.

Why can using CSS `order` to repair incorrect HTML source order create an accessibility problem?

A. Visual order can change while reading and keyboard focus order still follows the DOM.  
B. The property removes all elements from the accessibility tree.  
C. The property works only in print media.  
D. It prevents Grid and Flexbox from wrapping.  
E. It automatically changes links into buttons.

### 37.

Which hiding technique can leave an element invisible while it may still occupy its usual layout box and remain available for interaction or focus, depending on the element?

A. `display: none`  
B. The HTML `hidden` attribute  
C. Removing the element from the DOM  
D. `opacity: 0`  
E. Setting its text to an empty string

### 38.

Which focus treatment is most appropriate for keyboard accessibility?

A. Remove every outline because focus is visible from context.  
B. Provide a clearly visible `:focus-visible` indicator and test that fixed or sticky content does not obscure it.  
C. Show focus only when the pointer hovers over the control.  
D. Indicate focus using color alone and only on wide screens.  
E. Move focused elements to the beginning of the DOM.

### 39.

A card uses `width: 20rem` inside a `280px`-wide container, with a typical `16px` root font size. Which revision is most likely to prevent horizontal overflow while retaining a `20rem` preferred maximum?

A. `width: 20rem !important;`  
B. `min-width: 20rem;`  
C. `width: 280rem;`  
D. `position: absolute;`  
E. `width: min(100%, 20rem);`

### 40.

A CSS declaration appears crossed out in developer tools and the expected layout is absent. Which investigation sequence is most disciplined?

A. Add several `!important` declarations, then reload until the page looks correct.  
B. Rewrite the HTML before checking whether the stylesheet loaded.  
C. Verify that the stylesheet loaded, the selector matched, the declaration won and computed validly, and the layout had the expected space and content.  
D. Change the browser and assume the original browser is defective.  
E. Delete all other stylesheets to remove the cascade.

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
