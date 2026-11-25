import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createStaticServer } from "./serve-static.mjs";

const repositoryRoot = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "..",
);

const requiredFiles = [
  "book/part-0-orientation/00-development-environment-setup.md",
  "book/part-1-foundations/01-how-the-web-works.md",
  "labs/starters/week-01/index.html",
  "labs/solutions/week-01/index.html",
  "assessment/public-practice/week-01.md",
];

const failures = [];

async function load(relativePath) {
  try {
    return await readFile(path.join(repositoryRoot, relativePath), "utf8");
  } catch (error) {
    failures.push(`${relativePath}: ${error.message}`);
    return "";
  }
}

for (const requiredFile of requiredFiles) {
  await load(requiredFile);
}

const solutionPath = "labs/solutions/week-01/index.html";
const html = await load(solutionPath);
const starter = await load("labs/starters/week-01/index.html");

if (!/<h1>Campus Hub setup check<\/h1>/i.test(starter)) {
  failures.push("labs/starters/week-01/index.html: missing visible setup-check heading");
}
if (!/received the Week 1 starter through the local web server/i.test(starter)) {
  failures.push("labs/starters/week-01/index.html: missing local-server success message");
}

const requiredPatterns = [
  [/^<!doctype html>/i, "modern HTML doctype"],
  [/<html\s+lang="en">/i, "document language"],
  [/<meta\s+charset="utf-8">/i, "UTF-8 declaration"],
  [/<meta\s+name="viewport"\s+content="width=device-width, initial-scale=1">/i, "viewport declaration"],
  [/<title>[^<]+<\/title>/i, "non-empty title"],
  [/<header>/i, "header landmark"],
  [/<nav\s+aria-label="[^"]+">/i, "labeled navigation"],
  [/<main>/i, "main landmark"],
  [/<h1>[^<]+<\/h1>/i, "main heading"],
  [/<section\s+id="events">/i, "events section target"],
  [/<section\s+id="communities">/i, "communities section target"],
  [/<a\s+href="#events">/i, "relative events fragment link"],
  [/<a\s+href="#communities">/i, "relative communities fragment link"],
  [/<footer>/i, "footer landmark"],
];

for (const [pattern, description] of requiredPatterns) {
  if (!pattern.test(html)) {
    failures.push(`${solutionPath}: missing ${description}`);
  }
}

const forbiddenPatterns = [
  [/<style(?:\s|>)/i, "embedded CSS"],
  [/\sstyle="/i, "inline CSS"],
  [/<script(?:\s|>)/i, "JavaScript"],
  [/<link[^>]+rel="stylesheet"/i, "external CSS"],
  [/\son\w+="/i, "inline event handler"],
];

for (const [pattern, description] of forbiddenPatterns) {
  if (pattern.test(html)) {
    failures.push(`${solutionPath}: Week 1 solution must not contain ${description}`);
  }
}

const ids = [...html.matchAll(/\sid="([^"]+)"/gi)].map((match) => match[1]);
const duplicateIds = ids.filter((id, index) => ids.indexOf(id) !== index);
if (duplicateIds.length > 0) {
  failures.push(`${solutionPath}: duplicate id values: ${[...new Set(duplicateIds)].join(", ")}`);
}

const chapter = await load("book/part-1-foundations/01-how-the-web-works.md");
const setup = await load("book/part-0-orientation/00-development-environment-setup.md");
for (const [pattern, description] of [
  [/Prepare Your Web-Programming Workstation/i, "setup orientation"],
  [/development-workstation-evidence-loop/i, "workstation evidence-loop visual"],
  [/node --version[\s\S]+npm --version[\s\S]+git --version[\s\S]+npm test/i, "readiness command sequence"],
  [/Windows[\s\S]+macOS[\s\S]+Linux/i, "cross-platform installation guidance"],
  [/Student workstation readiness record/i, "readiness evidence record"],
  [/Orientation worked answers/i, "orientation worked answers"],
  [/terminal-directory-rescue/i, "wrong-directory ENOENT visual"],
  [/repository-first-workflow/i, "repository-first workflow visual"],
  [/Git hosting service\*\* is a website[\s\S]+This course uses \*\*GitHub\*\*/i, "Git hosting service explanation"],
  [/web-programming-coursework-2026_Fall[\s\S]+learning management system \(LMS\)/i, "Fall 2026 template address and LMS responsibility"],
  [/Multi-factor authentication \(MFA\)[\s\S]+two-factor authentication[\s\S]+recovery codes/i, "step-by-step GitHub MFA guidance"],
  [/Use this template[\s\S]+Create a new repository[\s\S]+Create repository from template/i, "GitHub template creation sequence"],
  [/Accept invitation[\s\S]+Include all branches[\s\S]+checkbox \*\*unchecked\*\*/i, "invitation and unchecked-branch instructions"],
  [/Add people[\s\S]+Mahyar2020[\s\S]+instructor must accept/i, "instructor collaborator instructions"],
  [/git remote -v[\s\S]+origin[\s\S]+fetch and push/i, "remote verification evidence"],
  [/two-terminal-model/i, "two-terminal explanation"],
  [/npm run serve:week01[\s\S]+does not produce an unexplained white page[\s\S]+Campus Hub setup check/i, "student-template server command and visible setup-check explanation"],
  [/network-panel/i, "Network-panel procedure and visual"],
  [/C:\\Users\\Student\\Documents\\GitHub\\web-programming-coursework-2026_Fall-12345678/i, "generic Windows-path recovery example"],
  [/does not explain a white page/i, "separation of ENOENT from the blank starter result"],
  [/git commit[\s\S]+git push/i, "commit-and-push workflow"],
  [/Request method[\s\S]+GET[\s\S]+200 OK[\s\S]+text\/html; charset=utf-8/i, "expected localhost Network evidence"],
  [/JavaScript is the course's primary programming language/i, "JavaScript course-language orientation"],
  [/javascript-runtime-map/i, "browser-versus-Node JavaScript visual"],
  [/typeof document[\s\S]+undefined/i, "browser and Node runtime verification"],
  [/client-side and server-side programming are taught separately first/i, "client/server teaching sequence"],
]) {
  if (!pattern.test(setup)) failures.push(`setup: missing ${description}`);
}
const requiredChapterSections = [
  "# Session 1 — How the Web Works",
  "# Guided laboratory",
  "# Exercises",
  "# Worked answers",
  "# Debugging clinic",
  "# Retrieval quiz",
  "# Session summary",
  "## Primary references and further reading",
];

for (const heading of requiredChapterSections) {
  if (!chapter.includes(heading)) {
    failures.push(`chapter: missing required section containing “${heading}”`);
  }
}

for (const [pattern, description] of [
  [/Fall 2026 coursework template[\s\S]+labs\/week-01\/index\.html[\s\S]+npm run serve:week01/i, "student coursework repository path and Week 1 server command"],
  [/Reading `2001:db8::40` as an IPv6 address/i, "detailed IPv6 section"],
  [/exactly 128 bits/i, "IPv6 bit length"],
  [/eight 16-bit groups/i, "IPv6 group structure"],
  [/2001:db8::40]:8443/i, "bracketed IPv6 URL example"],
  [/Exercise 13 - Expand, compress, and interpret IPv6/i, "IPv6 transfer exercise"],
  [/## Answer 13/i, "IPv6 worked answer"],
]) {
  if (!pattern.test(chapter)) failures.push(`chapter: missing ${description}`);
}

const server = createStaticServer(path.join(repositoryRoot, "labs/solutions/week-01"));
await new Promise((resolve, reject) => {
  server.once("error", reject);
  server.listen(0, "127.0.0.1", resolve);
});

try {
  const address = server.address();
  const port = typeof address === "object" && address ? address.port : 0;
  const successfulResponse = await fetch(`http://127.0.0.1:${port}/#events`);
  if (successfulResponse.status !== 200) {
    failures.push(`server: expected / to return 200, received ${successfulResponse.status}`);
  }
  if (successfulResponse.headers.get("content-type") !== "text/html; charset=utf-8") {
    failures.push("server: expected the HTML response to declare UTF-8 content");
  }

  const missingResponse = await fetch(`http://127.0.0.1:${port}/missing.html`);
  if (missingResponse.status !== 404) {
    failures.push(`server: expected /missing.html to return 404, received ${missingResponse.status}`);
  }
} finally {
  await new Promise((resolve, reject) => {
    server.close((error) => error ? reject(error) : resolve());
  });
}

if (failures.length > 0) {
  console.error("Week 1 verification failed:\n");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log("Week 1 verification passed.");
  console.log(
    `Checked ${requiredFiles.length} required files, ${requiredPatterns.length} HTML requirements, and HTTP 200/404 behavior.`,
  );
}
