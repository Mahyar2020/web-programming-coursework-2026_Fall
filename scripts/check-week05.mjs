import { access, readFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";

const requiredFiles = [
  "labs/week-05/index.html",
  "labs/week-05/app.js",
  "labs/week-05/model.js",
  "labs/week-05/styles.css",
  "labs/starters/week-05/index.html",
  "labs/starters/week-05/app.js",
  "labs/starters/week-05/model.js",
  "labs/starters/week-05/styles.css",
  "labs/solutions/week-05/index.html",
  "labs/solutions/week-05/app.js",
  "labs/solutions/week-05/model.js",
  "labs/solutions/week-05/model.test.js",
  "labs/solutions/week-05/styles.css",
  "book/part-2-browser-programming/05-dom-events-and-forms.md",
];

for (const path of requiredFiles) await access(path);

const app = await readFile("labs/solutions/week-05/app.js", "utf8");
const html = await readFile("labs/solutions/week-05/index.html", "utf8");
const starterHtml = await readFile("labs/starters/week-05/index.html", "utf8");
const chapter = await readFile("book/part-2-browser-programming/05-dom-events-and-forms.md", "utf8");

const evidence = [
  [app, "querySelector"], [app, "textContent"], [app, "replaceChildren"],
  [app, "addEventListener"], [app, "closest"], [app, "FormData"],
  [app, "preventDefault"], [app, "aria-pressed"], [html, 'role="status"'],
  [chapter, "event.target"], [chapter, "event.currentTarget"],
  [chapter, "checkValidity()"], [chapter, "setCustomValidity"],
  [chapter, "progressive enhancement"],
  [app, "focusedEventId"], [app, "focus({ preventScroll: true })"],
  [app, "No events match these filters"], [html, "Robotics night"],
  [html, "<noscript>"], [starterHtml, "Robotics night"], [starterHtml, "<noscript>"],
  [chapter, "Table 5.3 - Common form controls"], [chapter, "Answer 40"],
  [chapter, "MutationObserver"], [chapter, "shadow DOM"],
  [chapter, "Figure 5.11"], [chapter, "Table 5.6 - Session 5 glossary"],
];

for (const [source, expected] of evidence) {
  if (!source.includes(expected)) throw new Error(`Week 5 evidence missing: ${expected}`);
}

const tests = spawnSync(process.execPath, ["--test", "labs/solutions/week-05/model.test.js"], {
  stdio: "inherit",
});
if (tests.status !== 0) process.exit(tests.status ?? 1);
console.log("Week 5 DOM, events, forms, and model checks passed.");
