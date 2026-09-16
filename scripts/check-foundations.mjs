import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const failures = [];

async function load(relativePath) {
  try {
    return await readFile(path.join(root, relativePath), "utf8");
  } catch (error) {
    failures.push(`${relativePath}: ${error.message}`);
    return "";
  }
}

function requirePatterns(text, file, checks) {
  for (const [pattern, description] of checks) {
    if (!pattern.test(text)) failures.push(`${file}: missing ${description}`);
  }
}

const week2File = "labs/solutions/week-02/index.html";
const week2 = await load(week2File);
requirePatterns(week2, week2File, [
  [/<a href="#main-content">[^<]+<\/a>/i, "skip link"],
  [/<main id="main-content">/i, "skip-link target"],
  [/<nav aria-label="[^"]+">/i, "named navigation"],
  [/<a href="\/events" aria-current="page">/i, "current-page navigation state"],
  [/<meta name="description" content="[^"]+">/i, "page description metadata"],
  [/<form action="\/events" method="post">/i, "POST event form"],
  [/<label for="event-title">/i, "visible title label"],
  [/<input id="event-title" name="title"[^>]+required/i, "required named title"],
  [/<input id="organizer-email" name="organizerEmail" type="email"/i, "email input"],
  [/<input id="organizer-email"[^>]+autocomplete="email"/i, "email autocomplete purpose"],
  [/<input id="capacity" name="capacity" type="number" min="1" max="300" required/i, "bounded capacity"],
  [/<fieldset>[\s\S]*<legend>Event format \(required\)<\/legend>/i, "format fieldset and legend"],
  [/aria-describedby="description-help"/i, "associated description help"],
  [/<button type="submit">/i, "explicit submit button"],
]);
for (const [pattern, description] of [
  [/\stabindex="[1-9]/i, "positive tabindex"],
  [/<style(?:\s|>)/i, "embedded CSS"],
  [/<script(?:\s|>)/i, "JavaScript"],
  [/\son\w+="/i, "inline event handler"],
]) {
  if (pattern.test(week2)) failures.push(`${week2File}: contains forbidden ${description}`);
}

const week3HtmlFile = "labs/solutions/week-03/index.html";
const week3CssFile = "labs/solutions/week-03/styles.css";
const week3Html = await load(week3HtmlFile);
const week3Css = await load(week3CssFile);
requirePatterns(week3Html, week3HtmlFile, [
  [/<link rel="stylesheet" href="styles\.css">/i, "external stylesheet"],
  [/<form class="event-filter" action="\/" method="get">/i, "semantic event filter form"],
  [/<label for="event-type">/i, "visible event-type label"],
  [/<select id="event-type" name="type">/i, "named event-type select"],
  [/<button type="submit">/i, "explicit filter submit button"],
  [/class="event-grid"/i, "event grid hook"],
  [/class="event-card"/i, "event card components"],
  [/class="event-card__content"/i, "container-query content hook"],
]);
requirePatterns(week3Css, week3CssFile, [
  [/@layer\s+reset,\s*base,\s*layout,\s*components/i, "declared cascade layers"],
  [/box-sizing:\s*border-box/i, "border-box baseline"],
  [/display:\s*flex/i, "Flexbox layout"],
  [/display:\s*grid/i, "Grid layout"],
  [/repeat\(auto-fit,\s*minmax\(min\(100%,\s*17rem\),\s*1fr\)\)/i, "overflow-safe responsive tracks"],
  [/:focus-visible/i, "visible focus rule"],
  [/@media\s*\(min-width:\s*48rem\)/i, "content breakpoint"],
  [/@media\s*\(prefers-reduced-motion:\s*reduce\)/i, "reduced-motion policy"],
  [/@media\s*\(forced-colors:\s*active\)/i, "forced-colors policy"],
  [/container-type:\s*inline-size/i, "inline-size query container"],
  [/@container\s+event-card\s*\(min-width:\s*20rem\)/i, "component container query"],
  [/min-block-size:\s*2\.75rem/i, "comfortable control target baseline"],
  [/padding-inline:/i, "logical inline spacing"],
  [/padding-block:/i, "logical block spacing"],
  [/overflow-wrap:\s*anywhere/i, "long-title wrapping"],
]);
for (const [pattern, description] of [
  [/!important/i, "!important"],
  [/#(?:[a-z_-][\w-]*)\s*\{/i, "ID selector"],
  [/height:\s*100vh/i, "fixed viewport height"],
  [/overflow-x:\s*hidden/i, "global overflow concealment"],
]) {
  if (pattern.test(week3Css)) failures.push(`${week3CssFile}: contains forbidden ${description}`);
}

for (const [week, chapter] of [[2, "book/part-1-foundations/02-semantic-html-and-accessibility.md"], [3, "book/part-1-foundations/03-css-cascade-layout-and-responsive-design.md"]]) {
  const text = await load(chapter);
  for (const heading of ["# Guided laboratory", "# Exercises", "# Worked answers", "# Debugging clinic", "# Retrieval quiz", "# Session summary"]) {
    if (!text.includes(heading)) failures.push(`${chapter}: missing ${heading}`);
  }
  if (!text.includes(`Technical review date:`)) failures.push(`${chapter}: missing technical review date`);
}

const chapter2 = await load("book/part-1-foundations/02-semantic-html-and-accessibility.md");
requirePatterns(chapter2, "book/part-1-foundations/02-semantic-html-and-accessibility.md", [
  [/Document-wide meaning begins in `html` and `head`/i, "document metadata lesson"],
  [/Choose the submission method from the operation/i, "GET and POST lesson"],
  [/Successful-control submission rules/i, "successful-control rules"],
  [/Perceivable[\s\S]+Operable[\s\S]+Understandable[\s\S]+Robust/i, "WCAG POUR principles"],
  [/media:accessibility-combined-evidence/i, "combined accessibility evidence figure"],
  [/figure:html-anatomy/i, "HTML anatomy figure"],
  [/Choose the encoding, especially for files/i, "form encoding lesson"],
  [/Design error recovery before adding JavaScript/i, "accessible error-recovery lesson"],
  [/Exercise 14 - Model a complex table/i, "complex-table transfer exercise"],
  [/Exercise 10 - Choose a testing strategy/i, "multi-method accessibility exercise"],
]);

const chapter3 = await load("book/part-1-foundations/03-css-cascade-layout-and-responsive-design.md");
requirePatterns(chapter3, "book/part-1-foundations/03-css-cascade-layout-and-responsive-design.md", [
  [/Read a CSS rule as a complete sentence/i, "CSS syntax lesson"],
  [/Build selector literacy/i, "selector-family lesson"],
  [/CSS-wide keywords/i, "inheritance keyword lesson"],
  [/Logical properties follow the writing system/i, "logical-properties lesson"],
  [/Positioned layout changes reference and flow/i, "positioning and stacking lesson"],
  [/Form controls retain platform behavior/i, "form-control styling lesson"],
  [/Container queries make components context-aware/i, "container-query lesson"],
  [/Debug CSS by tracing evidence/i, "developer-tools workflow"],
  [/figure:css-rule-anatomy/i, "CSS rule anatomy figure"],
  [/figure:logical-axes/i, "logical axes figure"],
  [/figure:container-query/i, "container-query figure"],
  [/figure:css-devtools-evidence/i, "CSS debugging evidence figure"],
  [/Exercise 16 - Architecture review/i, "architecture transfer exercise"],
  [/Instructor teaching guide/i, "instructor teaching support"],
  [/CSS Snapshot 2026/i, "current CSS snapshot reference"],
]);

if (failures.length) {
  console.error("Foundation verification failed:\n");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log("Foundation verification passed.");
  console.log("Checked Week 2 semantic-form and Week 3 responsive-CSS artifacts.");
}
