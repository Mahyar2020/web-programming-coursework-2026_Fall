import { readFile } from "node:fs/promises";
import { spawn } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const required = [
  "labs/starters/week-04/index.html",
  "labs/starters/week-04/styles.css",
  "labs/starters/week-04/events.js",
  "labs/starters/week-04/hello.js",
  "labs/starters/week-04/hello-browser.html",
  "labs/starters/week-04/hello-browser.js",
  "labs/starters/week-04/language-evidence.html",
  "labs/starters/week-04/language-evidence.js",
  "labs/starters/week-04/language-examples.js",
  "labs/solutions/week-04/index.html",
  "labs/solutions/week-04/styles.css",
  "labs/solutions/week-04/events.js",
  "labs/solutions/week-04/events.test.js",
  "labs/solutions/week-04/hello.js",
  "labs/solutions/week-04/hello-browser.html",
  "labs/solutions/week-04/hello-browser.js",
  "labs/solutions/week-04/language-evidence.html",
  "labs/solutions/week-04/language-evidence.js",
  "labs/solutions/week-04/language-examples.js",
  "labs/solutions/week-04/language-examples.test.js",
];

for (const file of required) await readFile(path.join(root, file), "utf8");

const solution = await readFile(path.join(root, "labs/solutions/week-04/events.js"), "utf8");
for (const pattern of [/export function seatsRemaining/, /Array\.isArray/, /\.filter\(/, /\.map\(/, /new Map\(/, /createEventRegistry/, /Object\.freeze/, /throw new TypeError/, /textContent/]) {
  if (!pattern.test(solution)) throw new Error(`Week 4 solution is missing ${pattern}`);
}

const hello = await readFile(path.join(root, "labs/starters/week-04/hello.js"), "utf8");
for (const expected of ["const courseName", "const sum", "console.log"]) {
  if (!hello.includes(expected)) throw new Error(`First program is missing ${expected}`);
}

const helloHtml = await readFile(path.join(root, "labs/starters/week-04/hello-browser.html"), "utf8");
if (!/<script src="hello-browser\.js"><\/script>/.test(helloHtml)) {
  throw new Error("First browser page must load hello-browser.js with a script element");
}

const chapter = await readFile(path.join(root, "book/part-2-browser-programming/04-javascript-from-first-principles.md"), "utf8");
for (const [pattern, description] of [
  [/ECMAScript and JavaScript/i, "language and host boundary"],
  [/Install Node\.js on Windows, step by step/i, "zero-start Node.js installation"],
  [/Create and run the first Node\.js program/i, "first-program walkthrough"],
  [/Run JavaScript in a browser/i, "first browser-program walkthrough"],
  [/Table 4\.4 - Responsibilities of the Week 4 entry/i, "four-file responsibility table"],
  [/Table 4\.5 - First-run symptoms/i, "beginner troubleshooting table"],
  [/figure:javascript-first-run-workflow/i, "first-run workflow visual"],
  [/figure:browser-javascript-load-path/i, "browser loading visual"],
  [/figure:javascript-four-file-map/i, "four-file architecture visual"],
  [/seven primitive types/i, "complete primitive-type introduction"],
  [/`const`,? (?:and )?`let`/i, "binding guidance"],
  [/Why `var` exists/i, "var scope and hoisting lesson"],
  [/Table 4\.8 - JavaScript loop forms/i, "complete loop selection table"],
  [/Strict comparison/i, "strict equality lesson"],
  [/Functions give a calculation a name and boundary/i, "function contract lesson"],
  [/A call returns one JavaScript value/i, "return-value lesson"],
  [/Common function call forms/i, "function call-form lesson"],
  [/Arrays model ordered collections/i, "array lesson"],
  [/figure:javascript-array-indexes/i, "array index visual"],
  [/figure:javascript-array-pipeline/i, "array transformation visual"],
  [/media:week-04-language-evidence/i, "tested loop function and array screenshot"],
  [/Objects model named facts/i, "object lesson"],
  [/Execution has preparation, calls, and returns/i, "execution model"],
  [/Closures preserve lexical access/i, "closure lesson"],
  [/Objects delegate through prototypes/i, "prototype lesson"],
  [/Choose a collection by the question/i, "Map and Set collection lesson"],
  [/Standard built-ins define common data boundaries/i, "standard built-in boundaries"],
  [/Modules make dependencies explicit/i, "module lesson"],
  [/figure:javascript-host-boundary/i, "runtime boundary visual"],
  [/figure:value-reference-identity/i, "identity visual"],
  [/figure:javascript-call-stack-closure/i, "call stack and closure visual"],
  [/figure:javascript-prototype-chain/i, "prototype visual"],
  [/figure:javascript-module-graph/i, "module graph visual"],
  [/media:week-04-browser-output/i, "authentic browser output"],
  [/# Guided laboratory/i, "guided laboratory"],
  [/# Worked answers/i, "worked answers"],
  [/Exercise 15 - Trace browser script loading/i, "environment-diagnosis exercises"],
  [/## Answer 15/i, "complete environment-diagnosis answers"],
  [/Answer 36/i, "complete advanced-language loop function and array answers"],
  [/# Retrieval quiz/i, "retrieval quiz"],
  [/40\. Which array operations/i, "forty-question retrieval quiz"],
  [/Instructor teaching guide/i, "instructor guidance"],
  [/Technical review\s+date:/i, "technical review date"],
]) {
  if (!pattern.test(chapter)) throw new Error(`Chapter 4 is missing ${description}`);
}

const helloOutput = await new Promise((resolve, reject) => {
  const child = spawn(process.execPath, ["labs/starters/week-04/hello.js"], {
    cwd: root,
    stdio: ["ignore", "pipe", "pipe"],
  });
  let stdout = "";
  let stderr = "";
  child.stdout.on("data", (chunk) => { stdout += chunk; });
  child.stderr.on("data", (chunk) => { stderr += chunk; });
  child.on("error", reject);
  child.on("exit", (code) => code === 0
    ? resolve(stdout.trim())
    : reject(new Error(`First program exited with ${code}: ${stderr}`)));
});
if (helloOutput !== "Hello from Web Programming!\nTwo plus three is 5.") {
  throw new Error(`Unexpected first-program output: ${JSON.stringify(helloOutput)}`);
}

await new Promise((resolve, reject) => {
  const child = spawn(process.execPath, ["--test", "labs/solutions/week-04/events.test.js"], { cwd: root, stdio: "inherit" });
  child.on("exit", (code) => code === 0 ? resolve() : reject(new Error(`Week 4 tests exited with ${code}`)));
});

await new Promise((resolve, reject) => {
  const child = spawn(process.execPath, ["--test", "labs/solutions/week-04/language-examples.test.js"], { cwd: root, stdio: "inherit" });
  child.on("exit", (code) => code === 0 ? resolve() : reject(new Error(`Language-evidence tests exited with ${code}`)));
});

console.log("Week 4 JavaScript verification passed.");
