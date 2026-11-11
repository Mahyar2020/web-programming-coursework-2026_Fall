# Session 3 - Cascading Style Sheets, Layout, and Responsive Design

**Essential question:** How can Cascading Style Sheets (CSS) help one semantic
document adapt to different screens, preferences, languages, and amounts of
content without becoming fragile?

A browser can display the Chapter 2 document without any author-written CSS. Its
headings are large, paragraphs form blocks, links are recognizable, and form
controls use platform conventions. Those defaults are intentionally modest, but
they reveal an important starting point: CSS does not create the document's
meaning. It participates in how that meaningful document is presented.

This chapter begins at the first character in a stylesheet and continues through
the cascade, typography, color, boxes, positioning, Flexbox, Grid, media queries,
container queries, accessibility preferences, and browser debugging. The live
session should emphasize the core path marked in Table 3.1; the additional
sections make the chapter useful later as a reference instead of forcing a
beginner to search for missing foundations in unrelated tutorials.

## Session map

Table 3.1 summarizes the prerequisites, expected work, and evidence for this
session.

**Table 3.1 - Session scope, preparation, and evidence**

| Item | Plan |
|---|---|
| Prerequisites | Sessions 1-2; semantic Campus Hub HyperText Markup Language (HTML) |
| Contact time | Approximately 3 hours workshop plus a 2-hour laboratory |
| Independent work | Approximately 5 hours, including reference sections and exercises |
| Main artifact | A responsive, accessible Campus Hub shell |
| Assessment | Three viewport checks, keyboard evidence, overflow audit, exercises, and quiz |

The recommended teaching route is CSS syntax and loading, selector matching, the
cascade, the box model, normal flow, Flexbox, Grid, responsive constraints, and
the guided laboratory. Typography, color, positioning, container queries, and
the expanded debugging material can be assigned before or after the workshop and
revisited in later chapters. They are not optional professional knowledge; the
separation protects the pace of the first encounter.

## Learning outcomes

After this session, you should be able to:

1. connect an external stylesheet and explain CSS rule, selector, declaration,
   property, value, at-rule, and error-recovery syntax;
2. use type, class, attribute, state, relationship, and pseudo-element selectors
   without coupling presentation to accidental document nesting;
3. explain how relevance, origin, importance, cascade layers, specificity,
   scoping proximity, and order of appearance choose a declared value;
4. distinguish inheritance from selector matching and use custom properties and
   CSS-wide keywords deliberately;
5. reason about display, the box model, intrinsic sizing, containing blocks,
   overflow, positioning, stacking, and logical axes;
6. choose units, colors, typography, backgrounds, borders, and form styles that
   remain readable and adaptable;
7. create robust one-dimensional layouts with Flexible Box Layout (Flexbox) and
   two-dimensional layouts with Grid;
8. design mobile-first media queries and component-level container queries from
   content constraints rather than named devices;
9. preserve focus visibility, contrast, target size, source order, zoom, reflow,
   forced colors, and reduced-motion preferences;
10. diagnose missing declarations, cascade conflicts, overflow, and layout
    failures with browser developer tools; and
11. organize CSS so that later changes remain local and predictable.

## 1. CSS is a language for presentation and constraints

CSS does not paint a fixed screenshot. It is a declarative language: an author
describes desired relationships, and the browser determines the resulting
presentation for the current conditions. The browser combines CSS rules with
document structure, fonts, available space, user preferences, writing direction,
zoom, and actual content.

A design that works only for one exact viewport and one exact paragraph is not
responsive. It is a picture of a single test case. Professional CSS establishes
constraints under which many valid cases can be laid out.

Before adding CSS, test the Chapter 2 page at narrow width, 200% zoom, with a long
event title, and with keyboard focus. Record what already works because of normal
HyperText Markup Language (HTML) flow. CSS should improve that behavior without
destroying it.

The short code examples in this chapter build one cumulative page rather than a
series of unrelated demonstrations. Figures 3.9 and 3.10 show the completed page
at wide and narrow viewports, so every rule that affects this example can be
connected to visible output.

### 1.1 Read a CSS rule as a complete sentence

Consider the first rule added to `styles.css`.

```css
.event-card {
  border: 1px solid #cad4df;
  padding: 1rem;
}
```

The selector `.event-card` identifies which elements the rule can match. The
curly braces contain a declaration block. Each declaration contains a property,
a colon, a value, and normally a terminating semicolon. In
`padding: 1rem;`, `padding` is the property and `1rem` is the value. The colon
belongs to CSS syntax; it is not part of either name. Figure 3.1 labels these
parts and shows the path from a matched element to proposed presentation values.

<!-- figure:css-rule-anatomy -->

A property describes the aspect being controlled. A value uses the grammar that
the property accepts. `padding: teal` is not meaningful merely because `teal` is
a valid CSS color: the `padding` property expects lengths, percentages, or
related keywords. Browser developer tools usually cross out or omit a declaration
whose value cannot be parsed for that property.

A semicolon separates declarations. The final semicolon is technically optional
in a block, but keeping it makes later additions safer. CSS comments begin with
`/*` and end with `*/`. The `//` notation used for comments in some programming
languages is not a CSS comment.

CSS is designed to recover from many errors. If a browser does not understand one
declaration, it normally ignores that declaration and continues with the rest of
the rule. This resilience supports progressive enhancement, but it can also make
a spelling error look silent. `colr: navy` does not stop the entire stylesheet;
it simply does not set `color`.

### 1.2 Rules, at-rules, and shorthands are different structures

An **at-rule** begins with `@` and controls a larger condition or operation.
Examples in this chapter include `@layer`, `@media`, `@container`, and
`@supports`. Some at-rules end with a semicolon; others contain a block. Read the
particular at-rule's grammar instead of assuming every `@` construct behaves the
same way.

A shorthand property sets several related longhand properties together. For
example, this declaration proposes width, style, and color for all four borders.

```css
.event-card {
  border: 1px solid #cad4df;
}
```

Shorthands are concise, but they also reset omitted longhands to their initial
values. Use them when that reset is intended. During debugging, the Computed
panel can reveal the resulting longhand values.

### 1.3 Connect CSS to HTML deliberately

The preferred connection for this project is an external stylesheet referenced
from the document `head`.

```html
<link rel="stylesheet" href="styles.css">
```

`rel="stylesheet"` identifies the relationship, and `href="styles.css"`
resolves relative to the HTML document's address. The browser requests the CSS
resource, parses it, and applies applicable rules. The Network panel should show
a successful request whose response has a CSS media type. A `404 Not Found`
response, a misspelled filename, or a path relative to the wrong document can
leave the page unstyled even when the CSS itself is correct.

CSS can also appear in a `style` element or a `style` attribute. A `style`
element can be useful for a self-contained demonstration. A style attribute is
occasionally generated by applications, but widespread inline styling duplicates
decisions, bypasses selectors, and makes maintenance difficult. The project uses
an external stylesheet so one tested file can serve multiple documents and be
cached independently.

The `@import` at-rule can load another stylesheet, but it may create additional
serial discovery and makes dependency order less visible. Prefer HTML `link`
elements for major stylesheets unless the project's architecture justifies an
import.

### 1.4 The browser already has a stylesheet

Browsers apply a **user-agent stylesheet** before the author's stylesheet. It is
why an unstyled heading appears bold and why a button resembles a platform
control. Users may also provide their own preferences or styles. The cascade is
designed to reconcile these sources; author CSS is not the only participant.

A reset should remove only defaults the design is prepared to replace. Erasing
all margins, focus indicators, list markers, and control appearance can destroy
useful affordances. This project uses a small baseline: predictable box sizing,
responsive media, and a few intentional spacing decisions. It does not attempt to
make every element visually blank.

## 2. Selectors match; the cascade decides

A selector answers one question: which elements does this rule target? It does
not traverse the document and change HTML. The browser evaluates the selector
against the Document Object Model (DOM), creates a set of matches, and considers
the declarations for each matched element. Figure 3.2 separates selector matching
from the later cascade decision.

<!-- figure:selector-matching -->

### 2.1 Build selector literacy before composing long selectors

Table 3.2 introduces the selector families that a beginning web programmer must
be able to read. The examples assume the semantic Campus Hub document.

**Table 3.2 - CSS selector families and the relationships they express**

| Selector family | Example | Meaning |
|---|---|---|
| Type | `article` | Every `article` element |
| Class | `.event-card` | Elements whose `class` list contains `event-card` |
| ID | `#events` | The element whose document ID is `events` |
| Attribute | `input[required]` | `input` elements with a `required` attribute |
| Attribute value | `input[type="email"]` | `input` elements whose `type` value is `email` |
| Pseudo-class | `a:hover`, `:focus-visible` | Elements in a state or structural condition |
| Pseudo-element | `.event-card::before` | A stylable generated box associated with a matched element |
| Descendant combinator | `.event-card h3` | Matching `h3` elements anywhere inside an event card |
| Child combinator | `.site-navigation > ul` | Matching `ul` elements that are direct children |
| Next-sibling combinator | `h2 + p` | A matching paragraph immediately after an `h2` |
| Subsequent-sibling combinator | `h2 ~ p` | Matching later sibling paragraphs after an `h2` |
| Selector list | `h1, h2, h3` | The union of several selectors; each item is evaluated separately |

Whitespace around `>` or `+` improves readability, but the space between
`.event-card` and `h3` is itself the descendant combinator. By contrast,
`.event-card.featured` contains no space and matches one element that has both
classes.

Classes are normally the most reusable styling hooks. IDs are valid selectors,
but their high specificity and one-document identity make them better suited to
fragment targets, labels, and scripting identities than routine component
styling. Attribute selectors are valuable when presentation genuinely follows a
semantic attribute or state.

Pseudo-classes such as `:hover`, `:focus-visible`, `:checked`, `:disabled`,
`:valid`, and `:invalid` describe conditions. Hover must never be the only way to
reveal essential information because touch, keyboard, and assistive input may not
produce it. Pseudo-elements such as `::before` and `::after` can add decorative
boxes, but generated content is not a reliable home for essential text.

Modern functional pseudo-classes make selectors more expressive. `:where()`
always contributes zero specificity, which is useful for low-priority defaults.
`:is()`, `:not()`, and `:has()` take the specificity of their most specific
selector argument rather than contributing an extra pseudo-class unit of their
own. Use `:has()` for relationships that CSS could not previously express, but do
not hide an unclear document model behind a difficult selector.

### 2.2 The cascade resolves competing declarations

When more than one declaration proposes a value for the same property on the
same element, the cascade resolves the conflict. Figure 3.3 turns that decision
into an ordered path rather than the misleading rule “the last declaration
wins.”

<!-- figure:css-cascade -->

At a practical introductory level, ask these questions in order:

1. Is the declaration relevant to this element, document, condition, and medium?
2. Which origin and importance level has precedence?
3. Within that origin and importance level, which cascade layer has precedence?
4. Which selector has greater specificity?
5. If the rules use `@scope` and specificity ties, which scope root is nearer?
6. If the earlier dimensions tie, which declaration comes later in the style
   order?

The full cascade also gives running transitions and animations special positions.
Table 3.3 records the parts that most often surprise authors. It is a reasoning
guide, not an invitation to override user needs.

**Table 3.3 - Practical cascade precedence and important qualifications**

| Situation | What to remember |
|---|---|
| Normal author declarations | Unlayered author rules outrank normal author rules inside layers; among normal layers, later declared layers outrank earlier layers. |
| Important declarations | `!important` reverses layer precedence; important declarations in earlier layers protect foundational constraints. |
| User important declarations | Important user preferences outrank important author declarations so users can override author presentation. |
| Keyframe animations | Animated values outrank normal declarations but not important declarations. |
| Running transitions | A property currently transitioning has the highest cascade precedence for its duration. |
| Inline style | A style attribute participates as author styling with special precedence in specificity comparisons; avoid treating it as a routine architecture. |
| Source order | Later wins only after relevance, origin, importance, layer, specificity, and scoping proximity fail to distinguish candidates. |

Do not memorize the table as a license to use `!important`. First inspect which
declaration won and why. The browser Styles panel normally shows losing
declarations crossed out and identifies their source files and line numbers.

### 2.3 Specificity is a comparison, not a score to maximize

Specificity is compared as three categories: ID selectors; class, attribute, and
pseudo-class selectors; and type and pseudo-element selectors. Compare the ID
category first. If it ties, compare the class-like category; if that ties, compare
the type-like category. Do not interpret `1-0-0` and `0-12-0` as decimal values:
one ID category still wins the first comparison.

```css
/* Specificity 0-1-0: reusable component hook */
.event-card__title { color: var(--color-heading); }

/* Specificity 1-2-3: coupled to one location and difficult to override */
#main-content section.events article.event-card h3 { color: navy; }
```

Prefer shallow class selectors for component styling. Use source order and
explicit cascade layers intentionally. Avoid `!important` as a routine escape;
it changes the conflict level and tends to create an escalating override contest.
When third-party CSS must be controlled, place it in a deliberately low-priority
layer rather than fighting every selector.

### 2.4 Inheritance is not selector matching

Properties such as `color` and `font-family` normally inherit. Properties such as
`margin`, `border`, and `width` normally do not. A directly targeted declaration
on a child wins over an inherited value even when the ancestor's selector has
greater specificity, because specificity is not compared between direct and
inherited declarations.

```css
body {
  color: #172033;
  font-family: system-ui, sans-serif;
}
```

Descendant text normally inherits these values. A card does not inherit the
body's margin because margin is not inherited.

CSS-wide keywords make the decision explicit:

- `inherit` takes the parent's computed value even for a property that does not
  normally inherit;
- `initial` uses the property's specification-defined initial value, which is not
  necessarily the browser's element default;
- `unset` behaves like `inherit` for inherited properties and `initial` for the
  others;
- `revert` rolls back the current origin's contribution; and
- `revert-layer` rolls back the current cascade layer's contribution.

These keywords are precise tools. A global `all: unset` can remove display and
interaction affordances that a component still needs.

### 2.5 Custom properties carry decisions through the cascade

Custom properties can represent repeated decisions:

```css
:root {
  --color-ink: #172033;
  --color-accent: #146c94;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --radius: 0.5rem;
}

.event-card {
  color: var(--color-ink);
  border-radius: var(--radius);
}
```

Custom property names begin with two hyphens, are case-sensitive, participate in
the cascade, and inherit by default. The `var()` function substitutes their
value where a property's grammar permits it. A fallback such as
`var(--card-surface, white)` is used when the referenced custom property is
missing or invalid at substitution time; it is not a compatibility fallback for
an arbitrary unsupported value.

A token name should express purpose when possible. `--color-accent` survives a
palette change better than `--blue`. Tokens centralize decisions, but they do not
automatically create a coherent design system; document their purpose and test
every combination in which they are used.

## 3. Boxes turn declared values into geometry

Most visible layout questions eventually become box questions: which box is this,
how large is it allowed to become, which containing block supplies its reference,
and does it remain in normal flow?

### 3.1 `display` establishes outer and inner behavior

An element's `display` value controls how its principal box participates in its
parent's layout and, for layout containers, how its children are arranged.

- `display: block` normally creates a block-level box that takes the available
  inline space and begins on a new line.
- `display: inline` participates in line layout; ordinary inline boxes do not use
  `width` and `height` like block boxes.
- `display: inline-block` participates inline while its inside behaves as a block
  container.
- `display: flex` and `display: grid` create block-level layout containers for
  their children.
- `display: none` removes the element's generated boxes and normally removes it
  from the accessibility tree. It is not merely visual transparency.

HTML semantics and CSS display are related only through browser defaults. A
`nav` element can be laid out with Grid, and a `span` can be displayed as a block,
without changing what those elements mean.

### 3.2 Content, padding, border, and margin form the box model

The standard box model consists of content, padding, border, and margin. Figure
3.4 nests the four regions so their boundaries are easier to distinguish.

<!-- figure:box-model -->

With the default `box-sizing: content-box`, a declared `width` or `inline-size`
applies to the content box. Padding and borders are added outside it. A common
project baseline is:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

Now a declared size includes content, padding, and border. Margin remains outside.
This does not make every box fit: a fixed `20rem` border box still cannot fit a
`17rem` container, and an unbreakable string can still impose a larger minimum.

Padding belongs inside the border and inherits the element's background. Margin
is transparent space outside the border. Borders contribute size and can convey
boundaries, but a difference that exists only in a faint border may not be
perceivable. `outline` differs from `border`: an outline does not occupy box-model
space, which makes it useful for focus indicators that should not shift layout.

### 3.3 Normal flow is a resilient default

Block content ordinarily follows document order and expands in the block
direction to contain its content. Inline content participates in line layout.
Normal flow handles unknown text length, font substitution, translation, and many
zoom cases well. Removing an element from flow means its size no longer reserves
ordinary space for neighbors.

An absolutely positioned card with fixed coordinates may overlap when text grows.
A normally flowing card contributes its size to surrounding layout. Begin with
flow, then introduce a different layout model because a real relationship demands
it.

### 3.4 Sizing begins with intrinsic content

An **intrinsic size** comes from the content itself. A word has an unbroken
minimum contribution; an image has intrinsic dimensions; a paragraph has a
preferred width at which its lines would not wrap. CSS sizing combines these
contributions with available space and author constraints.

`min-inline-size`, `max-inline-size`, `min-block-size`, and `max-block-size`
express boundaries without forcing one exact size. The following page shell can
shrink with its container but stops growing at `72rem`.

```css
.page-shell {
  inline-size: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

`min-content`, `max-content`, and `fit-content()` expose useful intrinsic sizing
ideas, but they are not synonyms for small, large, and responsive. Test them with
real content. Flex and Grid items also have an automatic minimum size that can
surprise authors. `min-inline-size: 0` allows a particular item to shrink below
its min-content contribution when wrapping or clipping behavior makes that safe.

Replaced elements such as images and video bring intrinsic dimensions and aspect
ratios from outside ordinary text layout. Width and height attributes in HTML can
reserve the correct ratio before a resource loads. CSS can then constrain the
rendered box. The `aspect-ratio` property is useful when the ratio is part of the
design, while `object-fit: cover` or `contain` controls how replaced content fits
inside a deliberately sized box. Cropping with `cover` must not remove information
that users need.

### 3.5 Logical properties follow the writing system

`left`, `right`, `top`, and `bottom` are physical directions. CSS also defines
logical directions relative to the writing mode. The **inline axis** follows a
line of text; the **block axis** follows the direction in which lines and blocks
accumulate. In English the inline axis is normally horizontal and begins on the
left. In Arabic or Persian it normally begins on the right. Some writing systems
can use vertical flow.

Figure 3.5 shows why `margin-inline`, `padding-block`, `inline-size`, and
`inset-inline-start` are more adaptable than assumptions about left, right,
width, and top.

<!-- figure:logical-axes -->

```css
.event-card {
  padding-block: 1.5rem;
  padding-inline: 1rem;
  border-inline-start: 0.25rem solid var(--color-accent);
}
```

This border follows the inline start edge when direction changes. Logical
properties do not translate content or correct an incorrect HTML `dir` value;
they allow layout to respect direction information already present.

### 3.6 Margin collapse and overflow provide evidence

Adjacent block-axis margins in normal flow can collapse under defined conditions,
so the resulting separation may equal the larger margin instead of their sum.
Padding, a border, a new formatting context, or a layout container changes those
conditions. If spacing appears to disappear, inspect the boxes instead of adding
larger and larger margins.

Overflow often reveals an incorrect constraint:

- a fixed size wider than the available inline size;
- unbreakable content such as a long Uniform Resource Locator (URL);
- a Flex or Grid item whose automatic minimum prevents shrinking;
- an image without a responsive maximum;
- a child sized to `100vw` inside a page that also has padding or a scrollbar; or
- a transformed or positioned object extending beyond the scrollable area.

Choose overflow behavior locally. `overflow: auto` can create a scroll container
where two-dimensional content genuinely needs it, such as a wide data table.
`overflow: clip` or `hidden` may be correct for deliberate visual effects, but
clipping must not make focused or essential content unreachable. Do not hide a
page-wide symptom with `overflow-x: hidden`; find the box that exceeds its
container and correct the cause.

### 3.7 Positioned layout changes reference and flow

Positioning is useful when an object must be anchored to a box or viewport, but
each mode has a different reference:

- `static` is the normal positioned state; inset properties do not reposition it;
- `relative` keeps the box's normal-flow space and offsets its visual position;
  it can also establish the containing block for positioned descendants;
- `absolute` removes the box from normal flow and positions it relative to an
  appropriate containing block;
- `fixed` is generally positioned relative to the viewport; and
- `sticky` behaves in flow until a scroll threshold is reached within its scroll
  container.

Sticky and fixed headers can obscure headings, skip-link targets, or keyboard
focus. Test them at high zoom and with `scroll-margin-block-start` where anchored
content needs clearance.

`z-index` participates in **stacking contexts**; it is not one global number line
for the whole page. Positioning, opacity, transforms, isolation, and other
properties can create separate contexts. If `z-index: 9999` appears ineffective,
inspect the ancestor stacking contexts rather than choosing a still larger
number. Transforms also change geometry visually without reserving new normal-flow
space, so they are not a substitute for layout.

## 4. Values express type, scale, color, and visual hierarchy

CSS values are typed. A property may accept a keyword, number, length,
percentage, color, image, position, function, or a combination defined by its
grammar. Browsers move values through several stages: a declaration supplies a
specified value; the cascade and inheritance contribute a computed value; layout
resolves a used value; rendering may finally round it to device pixels. This is
why the Computed panel can show something different from the text originally
written in the stylesheet.

### 4.1 Units communicate relationships

Table 3.4 compares units and functions by the relationship they express rather
than treating them as interchangeable ways to write a number.

**Table 3.4 - CSS units and responsive sizing functions**

| Unit or function | Relationship and useful role |
|---|---|
| `px` | A CSS reference pixel, not necessarily one physical screen pixel; useful for fine borders and precise thresholds |
| `rem` | A root-em length: `1rem` equals the computed `font-size` of the root `html` element; useful when many elements should share one scale |
| `em` | A local font-relative length: for most properties, `1em` equals the element's own computed font size; in a `font-size` declaration, it is resolved from the inherited parent size |
| `%` | Relative to a property-specific reference; inspect the property's definition instead of assuming it always means parent width |
| `vw`, `vh` | One percent of the viewport width or height; useful carefully because browser UI and extreme aspect ratios change the result |
| `svh`, `lvh`, `dvh` | Small, large, and dynamic viewport heights; useful when mobile browser interfaces change the visible viewport |
| `ch` | The advance measure of the `0` glyph; a practical approximation for readable line-length constraints |
| `fr` | A fraction of remaining space in Grid after non-flexible track sizing is considered |
| `min()`, `max()` | Choose a boundary from comparable values at used-value time |
| `clamp(min, preferred, max)` | Bound a preferred fluid value between a minimum and maximum |

#### What `rem` means

The name `rem` is short for **root em**. In an HTML document, the root element is
`html`. A length written in `rem` therefore asks the browser to begin with the
computed `font-size` of `html` and multiply it by the number before the unit. If
the root size is represented by *R*, the calculation is:

```text
x rem = x × R
```

Many browsers, with their ordinary settings unchanged, compute the initial root
font size as `16px`. That is a useful classroom example, not a promise made by
CSS. A user can select a larger default text size, a browser or operating system
can use another setting, and an author can change the root size. Always reason
from the **computed root font size**, not from a memorized assumption that
`1rem` must equal 16 pixels.

With a computed root size of `16px`, the arithmetic is direct:

```text
0.5rem = 0.5 × 16px = 8px
1rem   = 1   × 16px = 16px
1.5rem = 1.5 × 16px = 24px
2rem   = 2   × 16px = 32px
```

If the root size becomes `20px`, the same declarations resolve to `10px`,
`20px`, `30px`, and `40px`. The stylesheet has not changed; the common reference
has changed. Figure 3.6 follows that one root reference into several declarations
and contrasts it with the local chain used by `em`.

<!-- figure:rem-em-scale -->

The most important relationship in Figure 3.6 is not the particular number
`16px`. It is that every `rem` length points back to the same root. This makes a
spacing and type scale easier to reason about across nested components.

#### Read a `rem` declaration as a calculation

Consider a small part of the Campus Hub stylesheet.

```css
body {
  font-size: 1rem;
}

.event-card {
  padding: 1rem;
  gap: 0.75rem;
}

.event-card__title {
  font-size: 1.5rem;
}
```

If the computed root font size is `16px`, the body text is `16px`, the card
padding is `16px`, the gap is `12px`, and the title is `24px`. Nesting the title
inside the card does not change those calculations because every value still
uses the root. In developer tools, the rule may remain visible as `1.5rem` in the
Styles panel while the Computed panel reports the resolved size, such as `24px`.
The authored value communicates the relationship; the computed value supplies
evidence of what the browser is using now.

Do not mentally replace every `rem` with pixels while designing. Write the
relationship first, then use the current root size when a concrete measurement
is needed for debugging. The conversion changes if the root changes.

#### `rem` and `em` answer different questions

Both units are font-relative, but they do not normally consult the same element.
`rem` asks, “How large is this compared with the document's root text size?”
`em` usually asks, “How large is this compared with this component's text?”

One detail deserves careful attention. In a `font-size` declaration, an `em`
value is resolved from the font size inherited from the parent because the
element's own new font size has not yet been established. For most other
properties, such as `padding`, `gap`, or `border-radius`, `em` is resolved from
the element's computed font size.

```css
.event-card {
  font-size: 1.25em;
  padding: 1em;
}

.event-card__tag {
  font-size: 0.8em;
}
```

Suppose the card's parent has a computed font size of `16px`. The card's
`font-size: 1.25em` becomes `20px`. Its `padding: 1em` then becomes `20px`
because padding uses the card's computed font size. The tag inherits `20px` from
the card, so `0.8em` becomes `16px`. This local scaling can be exactly what a
self-contained badge, icon, or button needs. It can also surprise you when
nested components multiply sizes repeatedly. Using `rem` avoids that accidental
compounding when the intended reference is the document-wide scale.

A practical starting policy is:

- use `rem` for the main type scale, page and component spacing, and dimensions
  that should follow the user's root text setting consistently;
- use `em` when a detail should deliberately scale with the text of its own
  component, such as an icon, badge padding, or a button's internal spacing;
- use `px` where a CSS reference pixel expresses the intended relationship well,
  such as a thin border; and
- choose percentages, viewport units, container units, `ch`, Grid fractions, or
  sizing functions when their different reference is the relationship you need.

This is a design policy, not a rule that makes one unit universally superior.
For example, browser zoom enlarges content written in pixels too. The benefit of
`rem` is the explicit connection to the root font setting; accessibility still
requires rendered testing.

#### Preserve the user's starting point

You may encounter the following shortcut in existing stylesheets.

```css
html {
  font-size: 62.5%;
}
```

When the browser's starting size happens to be `16px`, `62.5%` produces `10px`,
which makes decimal conversion to pixels look convenient. The result is not
guaranteed to be `10px`, however, because the user's starting size may differ.
It also makes the document's normal text smaller unless later rules enlarge it.
This course does not change the root merely to make mental arithmetic resemble
decimal notation. Leave the user's root setting intact unless the design has a
well-tested reason to change it, and never treat `62.5%` as required boilerplate.

Relative units reduce some rigid relationships, but they cannot prevent clipped
text, fixed-height controls, or layouts that fail under enlargement. Verify the
rendered page at 200% text enlargement or the applicable browser test, at browser
zoom, and at narrow reflow widths. The goal is not the presence of `rem`; the
goal is content and functionality that remain available.

#### Checkpoint - calculate before opening developer tools

The root computed font size is `18px`. A card has `padding: 1.25rem`; its title
has `font-size: 1.5rem`. The card also has `font-size: 1.1em` inside a parent
whose computed font size is `20px`, and a local badge uses `padding-inline:
0.5em`. What values should you predict?

**Answer:** the card padding is `22.5px` because `1.25 × 18 = 22.5`; the title is
`27px` because `1.5 × 18 = 27`. The card's own font size is `22px` because
`1.1 × 20 = 22`. If the badge inherits that `22px` font size and does not set a
different one, each inline padding is `11px` because `0.5 × 22 = 11`. The common
mistake is to calculate every value from `18px`: only the `rem` values use the
root; these `em` values follow the local font-size chain.

Physical units such as `cm`, `mm`, `in`, and `pt` are anchored to CSS reference
units on screens and do not promise an accurate physical ruler. They are most
appropriate when print output has a real physical design requirement.

Avoid setting ordinary paragraph text in viewport units alone; extreme viewport
dimensions can make it unreadably small or large and can resist effective text
scaling. A bounded fluid size is safer:

```css
h1 {
  font-size: clamp(2rem, 1.4rem + 3vw, 4rem);
}
```

This rule contributes to the heading visible in Figures 3.10 and 3.11. The
minimum and maximum protect extremes; the middle term allows gradual change.
Always test zoom and user font settings rather than assuming a formula is
accessible.

### 4.2 Color notation is separate from color usability

CSS accepts named colors, hexadecimal notation, `rgb()`, `hsl()`, and newer color
functions. The Campus Hub palette uses hexadecimal values because they are
compact and familiar, but the notation does not determine quality. `#146c94` and
an equivalent `rgb()` value describe the same sRGB color.

Alpha controls transparency. Semi-transparent foregrounds blend with whatever is
behind them, so their final contrast depends on the complete stack. The
`currentColor` keyword reuses an element's computed `color`, which can keep icons
and borders coordinated. System color keywords can cooperate with forced-color
modes where author colors may be replaced.

Table 3.5 connects visual decisions with their accessibility implications.

**Table 3.5 - Color, contrast, and non-color evidence**

| Decision | Required reasoning |
|---|---|
| Ordinary text contrast | Web Content Accessibility Guidelines (WCAG) 2.2 Level AA normally requires at least 4.5:1 against the actual background. |
| Large text contrast | Qualifying large text normally requires at least 3:1; do not enlarge text merely to obtain the lower threshold. |
| User-interface and graphical boundaries | Meaningful visual information normally needs at least 3:1 contrast against adjacent colors under the relevant criterion. |
| Error, status, or selection | Color may reinforce the state but cannot be its only cue; include text, shape, iconography, or another perceivable difference. |
| Focus indicator | It must remain visible against the component and surrounding surface; test actual colors and states rather than trusting the palette name. |

Contrast ratios are measurements, not aesthetic judgments. A compliant pair can
still be tiring at small sizes, and a strong-looking pair may fail when opacity or
a background image changes. Measure the rendered combination and test high
contrast or forced-color settings.

### 4.3 Typography controls reading, not merely decoration

A font stack provides ordered alternatives:

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 1rem;
  line-height: 1.6;
}
```

The browser chooses the first available face capable of representing the text.
Generic families such as `sans-serif` provide a final category rather than a
specific file. Font availability, glyph coverage, weight synthesis, and metrics
can change line breaks and component height, so test more than one platform and
include the languages the course supports.

Use unitless `line-height` for ordinary text when descendants should scale the
ratio with their own font sizes. Very tight line height can cause lines to collide;
excessive line height separates related text. A useful body-text starting point
is often between 1.4 and 1.7, followed by testing with the actual typeface,
language, width, and user overrides.

Readable paragraphs also need a controlled measure. Approximately 45-75
characters per line is a useful starting range, not a conformance rule. The
project uses `max-inline-size: 68ch` and tests actual content. Avoid justified
alignment in narrow digital columns when it creates disruptive gaps. Preserve
link underlines unless another strong, non-color affordance makes links evident.

Web fonts can strengthen identity, but they add network requests and may cause
late metric changes. Use only needed weights and styles, choose appropriate
fallbacks, and evaluate performance and layout movement. The `font-display`
descriptor belongs inside `@font-face`; its choice trades immediate fallback
text against the timing of the downloaded face.

### 4.4 Backgrounds, borders, and shadows must support content

`background-color` paints beneath content and padding. Background images can be
positioned, sized, and repeated, while CSS gradients are generated images. They
are presentation: essential content and alternative text still belong in HTML.

```css
.event-card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  box-shadow: 0 0.25rem 1rem rgb(18 53 91 / 8%);
}
```

The completed rule appears in the cards shown in Figures 3.9 and 3.10. The border
supplies a dependable boundary; the subtle shadow adds depth but is not the only
separation. Large blurred shadows and full-page background images can increase
paint cost and reduce text contrast.

### 4.5 Form controls retain platform behavior

Form controls do not all inherit typography consistently, and their internal
rendering varies across operating systems and browsers. Begin with a small,
testable baseline rather than removing every native feature.

```css
button,
input,
select,
textarea {
  font: inherit;
}

button,
select {
  min-block-size: 2.75rem;
  padding-block: 0.6rem;
  padding-inline: 0.9rem;
}
```

The filter controls in Figures 3.9 and 3.10 use this rule. The minimum block size
creates a comfortable target under the tested font settings, but a CSS declaration
alone does not prove WCAG target-size conformance: measure the rendered target and
its spacing. Preserve recognizable states, keyboard operation, labels, and native
semantics. `appearance: none` transfers more responsibility to the author and
should be used only when every required affordance is rebuilt and tested.

## 5. Choose a layout model from the relationship

Normal flow, Flexbox, and Grid are cooperating tools, not successive generations
where the newest replaces everything before it. Table 3.6 begins with the content
relationship and then selects the smallest model that expresses it.

**Table 3.6 - Choosing a CSS layout model**

| Relationship | Likely starting model | Reason |
|---|---|---|
| Headings and paragraphs in reading order | Normal flow | Content naturally stacks and expands without explicit tracks. |
| Navigation, toolbar, button group, or aligned row/column | Flexbox | One primary axis controls distribution and alignment. |
| Card gallery, page regions, or timetable | Grid | Rows and columns or repeated tracks must coordinate. |
| Image with surrounding prose | Float, used narrowly | Float remains appropriate for content wrapping around an item, not for whole-page layout. |
| Genuine tabular data | Semantic HTML table | Data relationships require table semantics; changing CSS display does not create them. |

Figure 3.7 contrasts Flexbox's primary-axis coordination with Grid's
row-and-column coordination.

<!-- figure:layout-systems -->

### 5.1 Flexbox distributes items along a main axis

Setting `display: flex` creates a flex container. Its direct children become flex
items. The **main axis** follows `flex-direction`; the **cross axis** is
perpendicular. In the default horizontal writing mode, `row` follows the inline
axis, but “row” should not be memorized as “left to right” because direction and
writing mode affect it.

```css
.site-navigation ul {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1rem;
}
```

Wrapping is a resilience decision. Without it, translated labels, user font
settings, or zoom can force horizontal overflow. `justify-content` distributes
free space along the main axis. `align-items` aligns items on the cross axis.
These properties align boxes; they do not replace padding within a control.

Each flex item has grow, shrink, and basis components. The shorthand
`flex: 1 1 16rem` means the item may grow, may shrink, and begins flexing from a
`16rem` basis. Avoid using `flex: 1` without understanding its expanded values.
A long word or intrinsically wide child may still resist shrinking because of the
automatic minimum; inspect the item and use wrapping or `min-inline-size: 0` when
that is the correct content policy.

Auto margins can absorb available main-axis space for a specific relationship.
They are often clearer than adding an empty spacer element. `gap` belongs to the
container and creates consistent separation without special first/last-child
margin rules.

### 5.2 Grid coordinates tracks in two dimensions

Setting `display: grid` creates a grid container. Its direct children become grid
items. Rows and columns are **tracks**; the boundaries are **grid lines**; and the
space between tracks is the gap.

```css
.event-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 1rem;
}
```

The inner `min(100%, 17rem)` permits a track to shrink when the container itself
is narrower than `17rem`. `minmax()` sets the track's lower and upper bounds.
`auto-fit` creates as many repeated tracks as fit and collapses empty ones.
`1fr` shares remaining track space after fixed and intrinsic contributions have
been considered. This rule produces the one- and three-column arrangements in
Figures 3.9 and 3.10 without naming phones, tablets, or laptops.

The explicitly declared tracks form the **explicit grid**. Auto-placement can
create rows or columns in the **implicit grid** when more items exist. Use
`grid-auto-rows` or `grid-auto-columns` when those tracks need a deliberate
policy. Items can be placed by line numbers or named areas, but auto-placement is
often more resilient for collections whose item count changes.

`subgrid` allows a nested grid to use track sizing from its parent along a chosen
axis. It is useful when internal labels or actions across several cards must align,
but it should solve a real shared-track relationship rather than compensate for
unnecessary nesting.

### 5.3 Alignment is not ordering

Flexbox and Grid can change visual placement with `order`, explicit grid lines, or
named areas. The DOM order still governs important sequential experiences such as
reading and keyboard focus. Do not use visual reordering to repair incorrect HTML
order. Choose a coherent source order first, then place it responsibly and test
the linearized page.

Alignment also has a vocabulary. `justify-*` and `align-*` act on different axes,
and the exact effect depends on the layout method. When a property seems to do
nothing, ask whether free space exists on that axis and whether the property
applies to the container or the item.

## 6. Responsive design treats context as an input

Responsive design is not a list of device sizes. A page must work in resized
windows, split-screen views, embedded panels, browser zoom, different font
settings, portrait and landscape orientations, and devices that did not exist
when the stylesheet was written. Begin with flexible content and narrow
constraints, then enhance when a real relationship has room.

### 6.1 Viewport behavior begins in HTML

Chapter 2 supplied this metadata in the document `head`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

It asks a mobile browser to make the layout viewport correspond to the device's
CSS-pixel width at the initial scale. It does not make a fixed layout responsive.
Never disable user scaling with `user-scalable=no` or a restrictive maximum
scale; zoom is an essential user capability.

### 6.2 Media queries respond to the environment

Start with a useful single-column layout. Add a media query when the content has
enough space to support an enhancement:

```css
.page-shell {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}

@media (min-width: 48rem) {
  .dashboard {
    grid-template-columns: minmax(0, 2fr) minmax(16rem, 1fr);
  }
}
```

The breakpoint is justified by the layout's content, not by a specific device
model. New devices and split-screen windows need not match a familiar label.
Figure 3.8 compares the same card content under narrow and wide constraints.

<!-- figure:responsive-reflow -->

Figure 3.9 provides a more concrete view of that principle across a desktop,
tablet, and phone. The content remains recognizably the same; only its layout
adapts to the available space.

<!-- media:responsive-layout -->

The complete example produces the wide browser output in Figure 3.10. When the
viewport narrows, the same source produces Figure 3.11 without a separate mobile
document or duplicated content.

<!-- media:week-03-output-desktop -->

<!-- media:week-03-output-narrow -->

Use range syntax or the established `min-width`/`max-width` syntax consistently.
Width queries describe the viewport, not the screen hardware. Media features can
also describe orientation, hover capability, pointer precision, color scheme,
contrast preference, forced colors, and motion preference. Avoid inferring a
person or device class from one feature; a laptop may have both touch and a mouse.

### 6.3 Container queries make components context-aware

A media query knows about the viewport. A reusable component often needs to know
about the space its parent gives it. The same event card may appear wide in a
main region and narrow in a sidebar at the same viewport width.

```css
.event-card {
  container-name: event-card;
  container-type: inline-size;
}

@container event-card (min-width: 20rem) {
  .event-card__content {
    grid-template-columns: 1fr auto;
    align-items: end;
  }
}
```

`container-type: inline-size` establishes size containment needed for inline-size
queries. The named query applies to descendants of the container, not the
container box itself. Figure 3.12 shows two instances of one component responding
differently because their containers provide different inline sizes.

<!-- figure:container-query -->

Container queries complement media queries. Use media queries for page-level
environment changes and user preferences; use container queries when a component's
own allocated space should govern its internal arrangement. Container query units
such as `cqi` are relative to a query container, but ordinary `rem`, percentages,
and intrinsic sizing often remain easier to reason about.

### 6.4 Images and embedded media

Prevent ordinary images from exceeding their containers:

```css
img,
svg,
video {
  max-inline-size: 100%;
  block-size: auto;
}
```

Reserve aspect ratio or dimensions when possible so late-loading media does not
cause avoidable layout movement.

CSS constrains how an image's box is presented; HTML chooses which image resource
best matches content and loading conditions. The `srcset` and `sizes` attributes
support resolution switching, while the `picture` element supports art direction
when crops or compositions genuinely change. Do not use CSS background images for
content that needs alternative text or document meaning.

### 6.5 User preferences are responsive inputs

Respect reduced-motion preferences for non-essential animation:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto;
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
  }
}
```

This example is a broad project policy and should be adapted if an animation
communicates essential state. Also consider color-scheme preferences and forced
colors. Do not make interaction depend on motion, hover, or color alone.

`prefers-color-scheme` can select a light or dark palette, but every resulting
token combination still needs contrast testing. The `color-scheme` property tells
the browser which schemes a component supports so built-in controls and scrollbars
can cooperate. In `forced-colors: active`, user-agent colors may replace author
colors. Preserve borders, focus, and state with system color keywords or other
forced-color-aware techniques instead of fighting the mode.

Do not use `prefers-reduced-motion` to remove essential feedback. Replace
non-essential movement with an immediate state change and ensure that progress,
errors, and completion remain perceivable.

## 7. Accessible presentation survives real user conditions

Accessibility is not a theme added after layout. CSS can make semantic content
unreadable, unreachable, misleading, or motion-sensitive, so every presentation
decision must be tested against the ways people actually perceive and operate it.

### 7.1 Interaction states must remain perceivable

Links and controls need distinguishable hover, focus, active, disabled, valid,
and invalid states where relevant. Never remove the focus outline without a
replacement that is at least as visible across every surface.

```css
:focus-visible {
  outline: 3px solid #f0a202;
  outline-offset: 3px;
}
```

Use `:focus-visible` to emphasize keyboard-style focus while allowing the browser
to decide when that indicator is appropriate. Test it rather than assuming every
browser interaction follows the same heuristic.

Focus must also remain unobscured. Sticky headers, cookie panels, and fixed
toolbars can cover the focused control even when its outline is technically
rendered. Tab through the page at narrow width and high zoom. For a robust focus
indicator across varying surfaces, a two-color indicator or separated outline
can maintain contrast where one color cannot.

Disabled controls should look unavailable without becoming unreadable. Validation
states must not rely on red and green alone. Hover styling must be accompanied by
focus behavior where the same information or action matters to keyboard users.

### 7.2 Target size is measured after layout

WCAG 2.2 Level AA generally requires pointer targets to be at least 24 by 24 CSS
pixels or to satisfy one of the criterion's spacing or contextual exceptions.
That is a minimum conformance threshold, not necessarily a comfortable design
target. The Campus Hub controls aim for a `2.75rem` minimum block size under the
tested root settings and retain space between adjacent targets.

Inline links inside sentences have a specific exception, and browser-provided
controls can have another. Do not quote “24 pixels” without the criterion's
conditions, and do not assume declared CSS dimensions equal the final clickable
area. Inspect the rendered box and test touch or imprecise pointer use.

### 7.3 Zoom, text spacing, and reflow are layout tests

At 400% browser zoom, a page initially 1280 CSS pixels wide commonly presents a
layout viewport close to 320 CSS pixels wide. WCAG reflow expects most content to
remain readable without two-dimensional scrolling at the specified equivalent
dimensions, with exceptions for content such as data tables that genuinely needs
two dimensions. Test both narrow width and zoom because they expose related but
not identical failures.

Users may override line height, paragraph spacing, letter spacing, and word
spacing. Avoid fixed heights and clipped text. A card that works only with its
original copy, font, and spacing is not a robust card.

### 7.4 Hiding and visual order can change access

`display: none` and the HTML `hidden` attribute normally remove content from both
visual layout and the accessibility tree. `visibility: hidden` preserves layout
space while hiding the element and its descendants. `opacity: 0` can leave an
invisible control present and focusable. Off-screen positioning can also create
unexpected scrolling. Choose a hiding mechanism from the intended state rather
than copying a “hide element” recipe.

CSS-generated content, background images, and visual reordering do not repair
missing semantic order. Test the page without CSS, with keyboard focus, and in a
linearized reading sequence.

### 7.5 Motion, contrast, and forced colors require combined evidence

Measure text and non-text contrast for every state, including hover, focus,
disabled, and invalid conditions. Verify meaning without color. Emulate reduced
motion and forced colors, then use a real operating-system mode where possible.
Automated checks can find some contrast and target problems, but keyboard,
zoom/reflow, preference, and human reading tests remain necessary.

### Predict before running

What happens when this card is placed in a 280px-wide container?

```css
.card { width: 20rem; padding: 2rem; }
```

With a typical 16px root size, 20rem is 320px before considering the containing
space. Under `border-box`, padding is included in that 320px; under `content-box`,
it increases the outer box further. Either way, a fixed width can overflow the
280px container. A resilient alternative is `width: min(100%, 20rem)`.

## 8. CSS architecture should make change inexpensive

CSS is global by default: a selector can match anywhere in the document, and a
custom property can flow through many descendants. Maintainability comes from
controlling that power, not from pretending the cascade does not exist.

A maintainable small project can use this explicit layer order:

```css
@layer reset, base, layout, components, utilities;
```

1. `reset` contains the small interoperability baseline the project intentionally
   owns;
2. `base` contains tokens and low-specificity element defaults;
3. `layout` contains page shells and reusable spatial relationships;
4. `components` contains cohesive interface objects such as event cards; and
5. `utilities` contains narrow, documented single-purpose exceptions.

Normal declarations in a later layer outrank normal declarations in an earlier
layer without requiring higher specificity. Declare the order before loading
layer contents. Remember that unlayered normal author rules outrank layered normal
author rules, so an accidental unlayered file can bypass the architecture.

Names should communicate purpose and ownership. `.event-card` is more durable
than `.blue-box-left`. Avoid encoding one page's entire nesting into every
selector. A component may use a naming convention such as
`.event-card__title`, but the convention is a team tool rather than CSS syntax.

Native CSS nesting can group related selectors, but deep nesting recreates the
same coupling as long descendant selectors. Keep the resulting selector clear and
understand how functional pseudo-classes affect specificity. Comments should
explain a non-obvious decision, compatibility boundary, or constraint, not
translate obvious syntax into English.

Use `@supports` for progressive enhancement when a feature needs a guarded
fallback:

```css
.dashboard {
  display: block;
}

@supports (display: grid) {
  .dashboard {
    display: grid;
  }
}
```

Modern Flexbox and Grid do not normally require this particular fallback in the
course's supported browsers; the example demonstrates the decision pattern.
Check current compatibility and audience requirements before shipping a newer
feature. A declaration that an older browser ignores can be a safe enhancement
only when the earlier presentation remains usable.

## 9. Debug CSS by tracing evidence, not by guessing values

When a page looks wrong, separate four possible questions:

1. Did the stylesheet load?
2. Did the selector match the intended element?
3. Did the declaration win the cascade and compute to a valid value?
4. Did layout have the space and content assumptions the author expected?

Figure 3.13 maps those questions to browser evidence.

<!-- figure:css-devtools-evidence -->

### 9.1 Open the correct browser panels

1. Open the Campus Hub page in the browser.
2. Press `F12`, or press `Ctrl+Shift+I` on Windows and Linux. On macOS, press
   `Command+Option+I`. Browser and keyboard settings can change these shortcuts;
   the browser menu normally contains **Developer tools** when a shortcut is not
   available.
3. Select the **Network** panel and reload. Filter for `CSS` or find
   `styles.css`. A successful status and CSS response establish that the file was
   requested. If no row appears, inspect the HTML `link`; if the status is `404`,
   inspect the resolved request address and filename.
4. Select the **Elements** or **Inspector** panel and activate the element picker.
   Click the visible card or control whose presentation is unexpected.
5. In **Styles** or **Rules**, examine matched selectors. A crossed-out property
   lost the cascade or was overridden by a shorthand. A warning icon or missing
   value can indicate invalid syntax.
6. In **Computed**, search for the property and expand it to trace the winning
   declaration. Inspect the box-model visualization for content, padding, border,
   and margin.
7. Open the Flexbox or Grid overlay in the **Layout** panel. Turn on line numbers,
   track sizes, gaps, and item overlays where the browser supports them.
8. Use responsive-design mode to set an exact CSS-pixel viewport. Test zoom in
   the ordinary page as well; responsive emulation and browser zoom are related
   but not interchangeable evidence.

Edits made inside developer tools are temporary experiments. Once an experiment
explains the failure, reproduce the minimal correction in `styles.css`, save it,
reload, and confirm the evidence again.

### 9.2 Trace horizontal overflow systematically

Start at the page's horizontal scrollbar and inspect outward evidence:

1. Record the viewport width and zoom level.
2. Temporarily outline candidate boxes in developer tools.
3. Find the first box whose right or inline-end edge extends beyond its containing
   block.
4. Inspect its declared size, intrinsic minimum, margins, transforms, positioned
   offsets, and unbreakable descendants.
5. Correct the cause locally, then test long text, another language direction,
   and every required viewport again.

Do not keep a global diagnostic outline in the production stylesheet. Do not
declare success because the scrollbar disappeared after clipping; confirm that
all content and focus indicators remain reachable.

---

# Guided laboratory - Build the responsive Campus Hub shell

## Before you begin

Work in your personal repository created from the
[Fall 2026 coursework template](https://github.com/Mahyar2020/web-programming-coursework-2026_Fall).
Its root is the folder that contains `package.json`, `labs`, and `scripts`. In
Visual Studio Code, open **Terminal > New Terminal** and run the command below in
PowerShell to display the current location.

```powershell
Get-Location
```

If the path is not your cloned
`web-programming-coursework-2026_Fall-YOUR_STUDENT_NUMBER` folder, change to the
repository using its actual path. Replace the placeholder with your own student
number; do not copy this example literally.

```powershell
cd "C:\path\to\web-programming-coursework-2026_Fall-YOUR_STUDENT_NUMBER"
```

Confirm that the project manifest is visible before running an npm command.

```powershell
Get-Item package.json
```

Create a working branch and commit the untouched starting point only if your
course workflow asks for that baseline. Otherwise, begin from the instructor's
provided starter commit.

```powershell
git switch -c chapter-03-responsive-campus-hub
```

Open two ordinary terminal tabs. The first becomes the **server terminal** only
because it runs the long-lived server process. The second remains available for
tests and Git commands. Their windows are not different kinds of software; their
current jobs are different.

In the first terminal, run:

```powershell
npm run serve:week03
```

Leave that process running. Open the address printed by the command, normally
`http://localhost:8000/`, in the browser. If npm reports that it cannot find
`package.json`, the terminal is in the wrong directory. If the browser cannot
connect, confirm that the server terminal is still running and that the port in
the browser matches the printed address.

## Goal and acceptance criteria

Style the supplied semantic Campus Hub page without changing its meaning. Your
result must:

- use an external stylesheet;
- define a small token set for color, spacing, radius, and readable width;
- apply `border-box` consistently;
- preserve logical source and focus order;
- use Grid for the event collection and Flexbox for navigation/actions;
- style the semantic filter form without removing its native keyboard behavior;
- demonstrate one component-level container query;
- work without horizontal scrolling at 320, 768, and 1440 CSS pixels;
- remain usable at 200% zoom;
- show a strong keyboard focus indicator;
- provide comfortably sized, separated pointer targets;
- wrap long titles and navigation labels;
- respect reduced motion;
- remain understandable with forced colors and without color cues;
- avoid `!important`, ID selectors, positive `tabindex`, and fixed page heights;
- pass the supplied repository check and every manual acceptance check; and
- contain at least three meaningful commits.

## Step 1 - Inspect the unstyled document

Open `labs/week-03/index.html` and read the heading, landmark, event-card,
and filter-form structure. In the browser, press `Tab` repeatedly and write down
the focus order. Narrow the viewport to 320 CSS pixels in responsive-design mode.
Do not change HTML merely to make a selector convenient.

Expected evidence: the content remains in a meaningful order, the form has visible
labels, and the page uses browser defaults. It does not yet resemble Figures 3.9
and 3.10 because the starter stylesheet contains only its assignment comment.

## Step 2 - Establish tokens and global constraints

Open `labs/week-03/styles.css`. Add the layer declaration, purpose-named
custom properties, inherited body typography, the universal `border-box`
baseline, responsive media sizing, a centered page shell, and a visible
`:focus-visible` rule. Save the file and reload.

In developer tools, select one event card and confirm that the Computed box model
reports `border-box`. Select a link with the keyboard and confirm that the focus
outline is visible against its actual background. Commit the completed baseline.

```powershell
git add labs/week-03
git commit -m "Establish CSS tokens and resilient baseline"
```

## Step 3 - Build component layouts

Use a wrapping Flexbox list for navigation. Use responsive Grid tracks for event
cards. Give cards internal spacing and a subtle boundary while preserving their
article semantics. Style the filter with wrapping Flexbox and allow its controls
to inherit typography. Do not remove native select or button appearance.

Turn on Flexbox and Grid overlays. Explain which axis Flexbox controls in the
navigation and which tracks Grid creates in the event collection. Make the second
commit after the page relationships work at narrow and wide sizes.

## Step 4 - Add a content-driven enhancement

At a breakpoint justified by the content, allow the page header or dashboard to
use additional columns. Record why that width supports the enhancement. Then make
each event card an inline-size query container. At a threshold justified by the
card's own content, align its details link beside the metadata while preserving
the card's logical reading order.

Resize the page until one card crosses the container threshold. Record the card's
container width before and after the rule activates. Figure 3.12 explains why the
component responds to its container rather than a device name.

## Step 5 - Conduct an overflow audit

Test 320, 768, and 1440 CSS pixel widths and 200% zoom. Insert a deliberately long
event title. If horizontal scrolling appears, use the layout inspector to identify
the exact box before changing CSS. Also paste one long unbroken URL into a card,
switch the document direction temporarily to `rtl`, and check that logical
spacing follows the new inline start and end.

Remove temporary test content only after recording the cause and correction. Make
the third commit when the audited layout is stable.

## Step 6 - Verify preferences and interaction

Tab through the page and capture evidence of visible, unobscured focus. Measure
the rendered filter targets. Emulate reduced motion and forced colors in browser
tools, then verify an actual operating-system high-contrast mode if available.
Check that every state remains understandable without color alone.

In the second terminal, run the supplied coursework check from the repository
root.

```powershell
npm test
```

A passing command reports `Coursework setup verification passed.` It confirms
that the repository structure, Node.js version, starter documents, and local
servers remain usable; it does not grade every CSS decision. If it fails, read
the reported file or environment problem before editing. Then evaluate every
acceptance criterion manually and compare your committed attempt with the tested
reference solution in Appendix A.

Finally, compare the completed page with the wide output in Figure 3.10 and the
narrow output in Figure 3.11. Differences in exact font rendering are expected
across operating systems; the relationships, states, and responsive behavior must
agree.

Use Table 3.7 to record visible evidence at every required viewport and user
preference rather than writing “works” without a reproducible observation.

**Table 3.7 - Responsive-layout laboratory observation record**

| Check | Evidence and interpretation |
|---|---|
| Stylesheet request | |
| Matched selector and computed value | |
| 320px overflow | |
| 768px layout | |
| 1440px readable line length | |
| 200% zoom | |
| Long-title wrapping | |
| Right-to-left logical spacing | |
| Container-query threshold | |
| Focus visibility | |
| Target dimensions and spacing | |
| Reduced-motion behavior | |
| Forced-color behavior | |

---

# Exercises

## Foundation

### Exercise 1 - Cascade decision

Given `.card p { color: navy; }`, `.message { color: teal; }`, and an element
`<p class="message">`, which declaration wins in the same layer and origin? Show
the specificity comparison.

### Exercise 2 - Box calculation

Under `content-box`, calculate the outer inline size of an element with
`width: 240px`, 16px padding on each side, 2px borders, and 12px margins. Repeat
for `border-box`.

### Exercise 3 - Calculate and choose font-relative units

The root computed font size is `20px`. A card uses `padding: 1.25rem` and its
heading uses `font-size: 1.6rem`. Calculate both values. Then choose and justify a
unit or function for body line length, component padding, a badge whose padding
must scale with its own text, full-width media, and a fluid but bounded title.

## Application

### Exercise 4 - Repair overflow

Explain why `width: 100vw; padding: 2rem` can create horizontal scrolling inside
a page and propose a robust alternative.

### Exercise 5 - Flexbox or Grid

Choose a layout system for a wrapping navigation bar, a two-dimensional timetable,
a vertical button group, and a responsive card gallery. Explain each choice.

### Exercise 6 - Focus regression

A reset contains `*:focus { outline: none; }`. Explain the failure and provide a
repair that does not depend on color change alone.

## Challenge

### Exercise 7 - Source order

A designer asks you to display the event sidebar before the main event list on
wide screens but after it on narrow screens. Explain how to choose a DOM order and
CSS strategy without producing a confusing focus or reading sequence.

### Exercise 8 - Responsive reasoning

Design a Grid declaration that produces as many cards as fit, prefers a 17rem
minimum, never exceeds the container, and shares remaining space evenly. Explain
every function and unit.

### Exercise 9 - Diagnose an unstyled page

The HTML contains `<link rel="stylesheet" href="styles.css">`, but the Network
panel shows `404 Not Found` for
`http://localhost:8000/pages/styles.css`. The actual file is
`http://localhost:8000/assets/styles.css`. Explain why no CSS rule can apply and
give two correct repairs, assuming the HTML document is in `/pages/index.html`.

### Exercise 10 - Match selectors deliberately

For `<article class="event-card featured"><h3>Robotics night</h3></article>`,
state whether each selector matches an element and identify that element:
`.event-card`, `.event-card.featured`, `.event-card .featured`,
`article > h3`, and `article::before`.

### Exercise 11 - Inheritance and CSS-wide keywords

A card inherits `color: navy` from `body`, but a component rule directly sets
`.event-card { color: teal; }`. What color does ordinary card text inherit? What
would `color: inherit`, `color: initial`, and `color: unset` mean on the card?

### Exercise 12 - Positioning and stacking

A modal child has `z-index: 9999`, but it still appears below a transformed
sidebar. Explain why increasing the number may not help and describe the developer
tools evidence you would inspect before changing the architecture.

### Exercise 13 - Media or container query

The same event card is 25rem wide in the main area and 15rem wide in a sidebar,
both while the viewport is 1200px wide. Choose a media query or a container query
for changing the card's internal layout. Provide a minimal rule and explain the
containment requirement.

### Exercise 14 - Accessible control styling

A design removes the select arrow with `appearance: none`, removes the focus
outline, uses pale gray text, and gives the control a 16px-high click target.
Identify the separate usability and accessibility risks. Propose a safer baseline
without claiming that CSS alone proves conformance.

### Exercise 15 - Developer-tools evidence plan

A student's `padding-inline: 1rem` appears crossed out. Write an evidence sequence
that determines whether the file loaded, the selector matched, the declaration
was valid, which declaration won, and what used padding the browser produced.

### Exercise 16 - Architecture review

Review this selector and repair strategy:

```css
#main-content section.events article.event-card h3.title {
  color: purple !important;
}
```

Explain the maintenance costs and propose a layered, low-specificity alternative
that still allows a featured card to vary its title color.

---

# Worked answers

## Answer 1

`.card p` contains one class selector and one type selector. `.message` contains
one class selector and no type selector. Their class category ties, and the type
category breaks the tie, so `.card p` is more specific and its navy value wins if
all earlier cascade dimensions are equal. Later source order would not defeat the
higher specificity in this case.

## Answer 2

With `content-box`, the outer size including margins is `240 + 32 + 4 + 24 =
300px`. Without margins, the border box is 276px. With `border-box`, the declared
240px already includes padding and borders, so the outer size including margins
is `240 + 24 = 264px`. Margins never become part of the declared border-box width.

## Answer 3

`1.25rem` resolves to `25px` because `1.25 × 20 = 25`; `1.6rem` resolves to
`32px` because `1.6 × 20 = 32`. Use a `ch`-based maximum such as
`max-inline-size: 68ch` for body line length and `rem` for component padding that
should follow the user's root text size consistently. Use `em` for the badge's
internal padding because that spacing is intentionally local to the badge's own
computed text size. Use `max-inline-size: 100%` for media containment and
`clamp()` combining `rem` and a fluid term for a bounded title. These are
starting decisions that require testing with actual content, fonts, user text
settings, zoom, and reflow. The common mistake is to call every relative unit
interchangeable; each unit encodes a different reference relationship.

## Answer 4

`100vw` describes the viewport width, not the remaining content width inside a
parent. With `content-box`, padding is added outside that width, and a vertical
scrollbar can also make viewport units differ from the document's available
inline size. Prefer normal block sizing or `width: 100%` within the containing
block, use `border-box`, and let the parent provide page padding.

## Answer 5

Use Flexbox for wrapping navigation because its primary relationship is one row
that may wrap. Use Grid for the timetable because rows and columns must align.
Use Flexbox with a column direction for the button group. Use Grid with responsive
tracks for the card gallery because both track creation and column alignment
matter. These are reasoned defaults, not laws; content relationships decide.

## Answer 6

The reset removes the primary visible indication of keyboard location. Users can
reach controls but may not know which one will receive input. Remove the rule and
style `:focus-visible` with a sufficiently thick outline and offset that contrasts
with adjacent colors, for example a 3px amber outline plus spacing. Test on every
surface; a single color may not contrast with all backgrounds.

## Answer 7

Choose the DOM order that makes the most coherent reading and keyboard sequence,
usually main content followed by complementary content. On wide screens, place
the regions into named Grid areas without changing their logical sequence. A
visual left-right arrangement need not dictate DOM order. Test linearized reading
and Tab order at both widths. If the sidebar must logically precede the main list,
use that order consistently rather than creating breakpoint-dependent meaning.

## Answer 8

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 1rem;
}
```

`repeat()` defines recurring tracks. `auto-fit` creates as many as fit and
collapses unused tracks. `minmax()` provides minimum and maximum track sizes.
The inner `min()` prevents the preferred 17rem minimum from overflowing a
narrower container. `1fr` shares remaining track space evenly.

## Answer 9

The `href` is resolved relative to `/pages/index.html`, so `styles.css` becomes
`/pages/styles.css`. The server's `404` response means the browser did not receive
the stylesheet at that address; correct CSS in another file cannot participate in
matching or the cascade.

One repair is to use a root-relative address:

```html
<link rel="stylesheet" href="/assets/styles.css">
```

Another is the correct document-relative address:

```html
<link rel="stylesheet" href="../assets/styles.css">
```

Which form is preferable depends on the deployment's URL structure. The common
misconception is to edit selector specificity while the resource itself never
loaded. Reload with the Network panel open and require a successful CSS response
before investigating rules.

## Answer 10

- `.event-card` matches the `article` because its class list contains that token.
- `.event-card.featured` also matches the same `article`; no space means the one
  element must have both classes.
- `.event-card .featured` does not match anything in the supplied fragment. The
  space asks for a descendant with class `featured`, not the card itself.
- `article > h3` matches the `h3` because it is a direct child of the article.
- `article::before` selects a generated pseudo-element associated with the
  article. It does not match an HTML child, and it generates no visible box unless
  applicable declarations, often including `content`, cause one to be rendered.

The important misconception is that punctuation is cosmetic. A space changes the
relationship being selected.

## Answer 11

The card's directly declared `teal` value wins for the card. Descendant text that
has no direct color declaration normally inherits teal from the card. The body's
selector specificity is irrelevant to that direct-versus-inherited distinction.

On `.event-card`, `color: inherit` explicitly takes the parent's computed color,
so it would normally take navy. `color: initial` uses the specification's initial
color value, commonly represented by the user-agent canvas text color rather than
the author's body navy. Because `color` is normally inherited, `color: unset`
behaves like `inherit` here and also takes the parent value. A common misconception
is that `initial` means “the browser's normal style for this HTML element”; it
means the property's defined initial value.

## Answer 12

`z-index` compares boxes within stacking contexts. A transformed ancestor can
create a context, so a child with `z-index: 9999` may still be trapped beneath a
sibling context whose entire stack is above it. Larger numbers do not allow the
child to escape its ancestor's context.

Inspect the modal and sidebar ancestors in the Elements panel. Identify which
properties create stacking contexts—such as transforms, positioned elements with
non-auto `z-index`, opacity, or isolation—and inspect the browser's stacking or
layers visualization if available. Then decide whether the modal belongs higher
in the DOM or whether an unnecessary ancestor context should be removed. The
misconception is that `z-index` is one global ranking shared by every element.

## Answer 13

Use a container query because both cards share one viewport but receive different
component space.

```css
.event-card {
  container-type: inline-size;
}

@container (min-width: 20rem) {
  .event-card__content {
    grid-template-columns: 1fr auto;
  }
}
```

The card establishes an inline-size query container, and the rule styles its
descendant when that container reaches `20rem`. A media query at the 1200px
viewport would affect both cards and therefore cannot express the actual
relationship. The queried container cannot ordinarily style itself through that
same size query; the query applies to descendants.

## Answer 14

Removing native appearance removes a familiar affordance and makes the author
responsible for recreating the select indicator across states and platforms.
Removing focus styling hides keyboard location. Pale text may fail text contrast,
and a 16px-high target can be difficult to activate and may fail the WCAG 2.2
target-size criterion unless a stated exception or spacing condition applies.

A safer baseline keeps native appearance, uses `font: inherit`, supplies readable
foreground and background colors, preserves or strengthens `:focus-visible`, and
adds padding with a comfortable tested minimum block size. Measure the rendered
target, spacing, text contrast, non-text boundaries, focus contrast, and forced
colors. CSS declarations are implementation choices; conformance is established
from the resulting behavior and measurements.

## Answer 15

First, reload with the Network panel open and confirm that the intended stylesheet
returned successfully. Second, select the element and find the rule in the Styles
panel; absence suggests that the selector did not match or the conditional rule
was inactive. Third, check for a warning or invalid value. Fourth, expand the
crossed-out declaration or search `padding-inline` in the Computed panel to find
the winning shorthand or longhand and its source. Finally, inspect the box-model
diagram or computed `padding-inline-start` and `padding-inline-end` values to see
the resolved result.

Make a temporary developer-tools change only to test the hypothesis, then fix the
source file and reload. The common mistake is to add `!important` before learning
whether the declaration was valid, relevant, or loaded.

## Answer 16

The selector couples the title to an ID, several ancestors, element names, and two
classes. Its high specificity makes reuse and later variation expensive, while
`!important` moves the declaration into a different precedence level and invites
more important overrides.

A low-specificity component layer can express the default and a modifier:

```css
@layer components {
  .event-card__title {
    color: var(--event-title-color, var(--color-heading));
  }

  .event-card--featured {
    --event-title-color: var(--color-accent-strong);
  }
}
```

The title rule remains reusable, while the featured card changes a documented
component decision through the cascade. Another class-based modifier could be
valid; the important principle is to express ownership and variation without
encoding accidental page nesting. The misconception is that a selector becomes
safer when it names more ancestors. It actually becomes more coupled.

---

# Debugging clinic

At 400% zoom, an event card overlaps the footer. The card has `height: 18rem` and
its description has `overflow: hidden`.

## Diagnosis

The fixed height assumes a particular text size and amount. Zoom increases text
space requirements, but the card is forbidden to grow and the description is
clipped. Remove the fixed height, allow normal block growth, and use `min-height`
only if a minimum visual rhythm is needed. Retest with long content and zoom. Do
not conceal the failure with additional clipping.

---

# Retrieval quiz

1. What are the selector, declaration block, property, and value in a CSS rule?
2. Why can one invalid declaration fail without stopping the complete stylesheet?
3. How does an external stylesheet address resolve, and which browser panel proves
   that the file loaded?
4. What is the difference between `.card.featured` and `.card .featured`?
5. What does a selector do, and what does the cascade do?
6. When does source order decide a conflict?
7. Why is specificity not an ordinary decimal score?
8. How does inheritance differ from a selector directly matching a child?
9. What changes when `box-sizing` becomes `border-box`?
10. Why are normal flow and intrinsic sizing valuable?
11. What do the inline and block axes represent?
12. Why can a very large `z-index` still appear below another component?
13. When is Flexbox usually preferable to Grid?
14. What does `minmax(min(100%, 17rem), 1fr)` protect against?
15. When should a component use a container query instead of a media query?
16. Why is visual reordering risky?
17. Why is `overflow-x: hidden` a poor first repair?
18. What must a focus design provide beyond declaring `:focus-visible`?
19. How do zoom, reflow, and target-size tests contribute different evidence?
20. How should reduced-motion and forced-color preferences affect design?

## Quiz answers and misconception notes

1. In `.card { padding: 1rem; }`, `.card` is the selector, the braces contain the
   declaration block, `padding` is the property, and `1rem` is the value. The
   colon separates property from value; the semicolon terminates the declaration.
2. CSS has error-recovery rules so an unsupported or malformed declaration can be
   ignored while later valid material remains usable. The misconception is that
   resilience makes errors harmless; a misspelled property can silently remove an
   essential visual state.
3. A relative `href` resolves from the HTML document's address. Reload with the
   Network panel open and verify the requested URL, response status, and CSS
   response. The Styles panel cannot prove that an absent resource loaded.
4. `.card.featured` matches one element with both classes. `.card .featured`
   matches a descendant with class `featured` inside an ancestor with class
   `card`. The space expresses a relationship.
5. A selector identifies matching elements; the cascade resolves competing
   property declarations for each matched element and property.
6. Source order decides only after relevance, origin and importance, layer,
   specificity, and scoping proximity no longer distinguish the declarations.
   “Last always wins” is therefore incomplete.
7. Specificity compares ordered categories—ID, class-like, and type-like—not one
   base-ten number. Many class selectors do not carry into the ID category.
8. A directly matched declaration participates in the cascade for the child.
   Inheritance supplies a value only through the parent relationship when the
   child does not otherwise establish one. High ancestor specificity does not
   defeat a directly targeted child declaration.
9. Declared width and height include content, padding, and border. Margin remains
   outside, and intrinsic minimums or fixed sizes can still cause overflow.
10. Normal flow reserves space and accommodates changing content; intrinsic sizing
    lets content contribute real constraints. Removing both too early replaces
    adaptable behavior with assumptions about text, fonts, and viewport size.
11. The inline axis follows text within a line, while the block axis follows the
    direction in which lines and blocks accumulate. Logical properties adapt those
    relationships to writing direction and mode.
12. `z-index` is compared inside stacking contexts. A child cannot escape an
    ancestor context merely by using a larger number, so the ancestor structure
    and context-creating properties must be inspected.
13. Flexbox is usually preferable when one main axis governs a row or column of
    items. Grid is preferable when rows and columns or repeated tracks must
    coordinate. Neither choice changes source semantics.
14. The inner `min()` lets a preferred `17rem` minimum yield to a container that
    is even narrower. `minmax()` then allows growth to `1fr`, and repeated tracks
    share remaining space instead of overflowing.
15. Use a container query when a component's allocated space—not the viewport—
    determines its internal layout. Establish an appropriate query container and
    remember that the size query styles descendants, not the queried container
    itself.
16. Visual order can diverge from DOM reading and keyboard order, producing a
    page that looks coherent but is sequentially confusing.
17. Global clipping hides the evidence and can make content or focus indicators
    unreachable. Identify the first oversized box and correct its local constraint.
18. The focus indicator must be visible, sufficiently contrasting, and not
    obscured on every relevant surface. It must also follow a meaningful focus
    order. A selector alone proves none of those rendered outcomes.
19. Zoom tests text enlargement and can activate responsive conditions; reflow
    tests whether content remains readable without unnecessary two-dimensional
    scrolling; target testing measures the final interactive area and spacing.
    Together they reveal different failures.
20. Reduce or replace non-essential motion while preserving understandable state.
    In forced colors, allow user-agent colors to replace author colors and retain
    boundaries, focus, and state through compatible cues rather than color alone.

### Self-check scale

- **17-20:** ready to add behavior to a resilient interface.
- **13-16:** revisit the answers you could not explain without notes.
- **8-12:** repeat the cascade, sizing, and responsive investigations.
- **0-7:** rebuild the shell from normal flow, then add Flexbox and Grid one
  decision at a time.

---

# Session summary

- CSS supplies adaptable constraints rather than fixed screenshot coordinates.
- CSS syntax connects selectors with typed property values, while error recovery
  allows unsupported declarations to fail locally.
- A stylesheet must load and a selector must match before the cascade can matter.
- The cascade considers origin, importance, layers, specificity, scope, and order.
- Low-specificity component rules are easier to maintain.
- Inheritance and custom properties carry decisions through the document tree.
- Display, intrinsic sizing, the box model, and containing blocks explain most
  apparent size and spacing surprises.
- Normal flow should be preserved unless a real relationship requires otherwise.
- Logical properties follow writing direction and improve international resilience.
- `rem` lengths share the root element's computed font size, while `em` lengths
  can express deliberate component-local scaling.
- Typography, color, controls, backgrounds, and borders must be tested as rendered
  combinations rather than judged from declarations alone.
- Flexbox coordinates one primary axis; Grid coordinates rows and columns.
- Media queries respond to the environment; container queries respond to a
  component's allocated space.
- Logical DOM order must remain coherent regardless of visual placement.
- Focus, target size, zoom, reflow, long content, direction, reduced motion, and
  forced colors are required test inputs.
- Browser developer tools connect a visible failure to loading, matching, cascade,
  computed values, boxes, and layout.
- Overflow is diagnostic evidence, not something to hide globally.

## Glossary

Table 3.8 consolidates the vocabulary needed to explain cascade and layout
decisions during review.

**Table 3.8 - Session 3 glossary**

| Term | Working definition |
|---|---|
| Box model | Content, padding, border, and margin regions generated for an element. |
| At-rule | A CSS construct beginning with `@` that defines a condition, grouping, or operation, such as `@media` or `@layer`. |
| Cascade | The algorithm that resolves competing CSS declarations. |
| Cascade layer | An author-defined precedence group that organizes declarations independently of selector specificity. |
| Computed value | A property's value after cascade and much of value processing, before final layout use. |
| Containing block | The reference box used to resolve sizes or positions for another box. |
| Container query | A conditional rule based on a query container, commonly its inline size, rather than the viewport. |
| Custom property | A cascading author-defined property such as `--color-accent`, commonly used as a design token. |
| Declaration | A property-and-value proposal such as `padding: 1rem`. |
| `em` | A font-relative CSS length unit. In a `font-size` declaration it refers to the inherited parent size; for most other properties it refers to the element's computed font size. |
| Flexbox | A layout model for distributing and aligning items primarily along one axis. |
| Grid | A layout model that coordinates rows and columns. |
| Inheritance | Transfer of selected property values from an element to its descendants. |
| Intrinsic size | A size contribution derived from an element's content rather than only an author-declared external dimension. |
| Logical property | A property expressed relative to block and inline flow rather than fixed physical directions. |
| Media query | A conditional block based on characteristics such as available width or user preference. |
| Normal flow | The default system by which block and inline boxes participate in document layout. |
| Pseudo-class | A selector component representing a state or structural condition, such as `:focus-visible`. |
| Pseudo-element | A selector component representing a stylable generated or abstract part, such as `::before`. |
| `rem` | Root em, a CSS length unit equal to the computed font size of the document's root element. |
| Selector | A pattern that identifies elements to which a rule may apply. |
| Stacking context | A local three-dimensional painting context within which `z-index` values are compared. |
| Specificity | The selector comparison used within the relevant cascade level to resolve conflicts. |

## Primary references and further reading

1. World Wide Web Consortium (W3C), [CSS Snapshot 2026](https://www.w3.org/TR/css-2026/). Use the snapshot to understand that modern CSS is a family of coordinated modules, not one numbered “CSS3” specification.
2. MDN, [CSS fundamentals curriculum](https://developer.mozilla.org/en-US/curriculum/core/css-fundamentals/). Use its outcomes to review syntax, selectors, boxes, conflicts, values, forms, and debugging.
3. MDN, [CSS text styling curriculum](https://developer.mozilla.org/en-US/curriculum/core/css-text-styling/). Use it for deeper typography, links, lists, and web-font study.
4. MDN, [CSS layout curriculum](https://developer.mozilla.org/en-US/curriculum/core/css-layout/). Use it to extend normal flow, positioning, Flexbox, Grid, and responsive-design practice.
5. W3C, [CSS Cascading and Inheritance Level 5](https://www.w3.org/TR/css-cascade-5/). Use it when the introductory cascade model needs normative detail about layers and value processing.
6. W3C, [Selectors Level 4](https://www.w3.org/TR/selectors-4/). Use it to verify selector grammar and modern functional pseudo-classes.
7. W3C, [CSS Flexible Box Layout](https://www.w3.org/TR/css-flexbox-1/). Use it to resolve precise flex sizing and alignment questions.
8. W3C, [CSS Grid Layout Level 2](https://www.w3.org/TR/css-grid-2/). Use it for track sizing, placement, auto-placement, and subgrid behavior.
9. W3C, [CSS Containment Level 3](https://www.w3.org/TR/css-contain-3/). Use it for normative container-query and containment behavior.
10. W3C Web Accessibility Initiative, [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/). Use it to evaluate contrast, reflow, focus, target size, and preference-sensitive presentation as outcomes rather than isolated declarations.
11. Harvard University, [CS50 Web Week 0: HTML and CSS](https://cs50.harvard.edu/web/weeks/0/). Compare its concise lecture-and-project progression with this chapter's slower novice reference path.
12. Stanford University, [CS142 CSS lecture notes](https://web.stanford.edu/class/cs142/lectures/CSS.pdf). Use the rule-anatomy, selector, color, box, positioning, display, and layout outline as a compact university-level review.
13. Jennifer Niederst Robbins, *Learning Web Design*, 6th edition (O'Reilly, 2025). Use Chapters 11-17 for an extended beginner-to-intermediate treatment of CSS, typography, color, boxes, responsive layout, and transitions.
14. Keith J. Grant, *CSS in Depth*, 2nd edition (Manning). Use its treatment of the cascade, relative units, flow, boxes, layout, and maintainable component systems for instructor enrichment.
15. W3C, [CSS Values and Units Module Level 4](https://www.w3.org/TR/css-values/). Use its definitions of root-relative and local font-relative length units to verify `rem` and `em` calculations.
16. W3C Web Accessibility Initiative, [Understanding Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html). Use it to connect relative sizing decisions with the required rendered outcome: enlarged text without loss of content or functionality.

## What changes often?

Cascade, flow, Flexbox, and Grid principles are stable. Selectors, container
queries, nesting, color spaces, viewport units, preference media features, and
browser developer tools continue to evolve. Compatibility decisions must use the
project's tested browser policy and current support data rather than a remembered
label such as “CSS3.” Technical review date: **21 October 2026**.

## Session reflection

- Which CSS declaration removed the most special cases?
- Which overflow diagnosis changed your mental model?
- Which constraint would make this layout safer under translation or user zoom?

## Instructor teaching guide

### Suggested five-hour sequence

1. **Opening evidence, 20 minutes:** compare the unstyled Chapter 2 document with
   the completed page. Ask which meaning remains when CSS is disabled.
2. **Language and cascade, 50 minutes:** annotate Figure 3.1, live-edit selector
   matches, and trace one conflict through Figure 3.3 and developer tools.
3. **Boxes and values, 55 minutes:** measure one card under both box-sizing models,
   calculate `rem` and `em` from inspected computed font sizes, then demonstrate
   intrinsic overflow and logical axes.
4. **Break, 10 minutes.**
5. **Layout and responsive systems, 55 minutes:** build navigation with Flexbox,
   cards with Grid, and one container-query enhancement. Require students to
   predict each change before resizing.
6. **Accessible presentation, 30 minutes:** test focus, target size, 200% zoom,
   320 CSS pixels, reduced motion, and forced colors.
7. **Laboratory, 120 minutes:** use the six checkpoints and Table 3.7 as formative
   evidence. Reserve the final 15 minutes for peer explanation and commit review.

### Demonstrations that expose misconceptions

- Break the stylesheet path before discussing specificity. Students must use the
  Network panel and learn that an unloaded rule cannot lose the cascade.
- Compare `.card.featured` with `.card .featured` on Figure 3.2's document tree.
- Give a low-specificity rule a later layer and a high-specificity rule an earlier
  layer so students see that specificity is not the first cascade dimension.
- Put a long unbroken string in a Flex or Grid item and inspect its automatic
  minimum before adding `min-inline-size: 0`.
- Change the browser's default font size, inspect the computed root size, and ask
  students to predict which `rem` and `em` measurements will change before
  reloading the Campus Hub page.
- Place the same card in wide and narrow containers at one viewport to distinguish
  a container query from a media query.
- Temporarily remove focus styling and enable forced colors; ask students to
  describe evidence rather than say that the design “looks accessible.”

### Common misconceptions to listen for

- “CSS3 is the current single version of CSS.” Modern CSS consists of modules with
  independent levels and maturity.
- “The last declaration wins.” It wins only after earlier cascade dimensions tie.
- “Inheritance means a selector matched every descendant.” Inheritance and direct
  matching are different value paths.
- “`border-box` prevents overflow.” It changes size accounting but cannot override
  every fixed or intrinsic minimum.
- “`1rem` always equals `16px`.” Sixteen pixels is a common starting value, but
  the unit follows the computed root font size, which can reflect user and author
  settings.
- “`rem` automatically makes a page accessible.” A relative unit can preserve a
  useful relationship, but only resizing, zoom, and reflow tests reveal clipping
  or loss of functionality.
- “Flexbox is old Grid” or “Grid replaces Flexbox.” They express different
  dimensional relationships and cooperate with normal flow.
- “Responsive means phone, tablet, desktop.” Content, containers, zoom, input,
  preferences, and window configuration are the real inputs.
- “A high `z-index` is globally on top.” Stacking contexts are local.
- “Passing an automated accessibility checker proves the CSS is accessible.” It
  supplies partial evidence only.

### Accommodations and alternatives

Provide completed source files to students whose assistive workflow makes timed
typing an irrelevant barrier; assess their explanation, diagnosis, and adaptation
instead. Supply textual descriptions of every diagram through the surrounding
prose, allow browser zoom and personal styles, and avoid grading pixel-identical
rendering across platforms. A learner who cannot use a pointing device must be
able to complete every required task by keyboard or an equivalent input method.

### Formative rubric

- **Conceptual reasoning, 30%:** explains matching, cascade, boxes, and layout
  choices with correct boundaries.
- **Responsive resilience, 25%:** passes required widths, zoom, long-content,
  direction, and container tests without concealing overflow.
- **Accessible presentation, 20%:** preserves focus, contrast, target usability,
  source order, preferences, and perceivable states.
- **Engineering evidence, 15%:** uses Network, Styles, Computed, box, and layout
  tools and records reproducible observations.
- **Maintainability, 10%:** uses purposeful names, low specificity, documented
  layers, cohesive commits, and no forbidden repair shortcuts.
