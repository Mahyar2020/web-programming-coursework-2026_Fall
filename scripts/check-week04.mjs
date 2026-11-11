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
  "labs/solutions/week-04/index.html",
  "labs/solutions/week-04/styles.css",
  "labs/solutions/week-04/events.js",
  "labs/solutions/week-04/events.test.js",
  "labs/solutions/week-04/hello.js",
  "labs/solutions/week-04/hello-browser.html",
  "labs/solutions/week-04/hello-browser.js",
];

for (const file of required) await readFile(path.join(root, file), "utf8");

const solution = await readFile(path.join(root, "labs/solutions/week-04/events.js"), "utf8");
for (const pattern of [/export function seatsRemaining/, /Array\.isArray/, /\.filter\(/, /\.map\(/, /throw new TypeError/, /textContent/]) {
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
  [/Table 4\.4 - First-run symptoms/i, "beginner troubleshooting table"],
  [/figure:javascript-first-run-workflow/i, "first-run workflow visual"],
  [/figure:browser-javascript-load-path/i, "browser loading visual"],
  [/seven primitive types/i, "complete primitive-type introduction"],
  [/`const` and `let`/i, "binding guidance"],
  [/Strict comparison/i, "strict equality lesson"],
  [/Functions give a calculation a name and boundary/i, "function contract lesson"],
  [/Arrays model ordered collections/i, "array lesson"],
  [/Objects model named facts/i, "object lesson"],
  [/figure:javascript-host-boundary/i, "runtime boundary visual"],
  [/figure:value-reference-identity/i, "identity visual"],
  [/media:week-04-browser-output/i, "authentic browser output"],
  [/# Guided laboratory/i, "guided laboratory"],
  [/# Worked answers/i, "worked answers"],
  [/Exercise 15 - Trace browser script loading/i, "environment-diagnosis exercises"],
  [/## Answer 15/i, "complete environment-diagnosis answers"],
  [/# Retrieval quiz/i, "retrieval quiz"],
  [/20\. Which browser panel proves/i, "twenty-question retrieval quiz"],
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

console.log("Week 4 JavaScript verification passed.");
