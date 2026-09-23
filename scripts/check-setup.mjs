import { access, readFile } from "node:fs/promises";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createStaticServer } from "./serve-static.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const failures = [];

const requiredFiles = [
  ".editorconfig",
  ".gitignore",
  ".nvmrc",
  "README.md",
  "SECURITY.md",
  "package.json",
  "labs/week-01/index.html",
  "labs/week-02/index.html",
  "labs/week-03/index.html",
  "labs/week-03/styles.css",
  "scripts/serve-static.mjs",
];

for (const relativePath of requiredFiles) {
  try {
    await access(path.join(root, relativePath));
  } catch {
    failures.push(`Missing required file: ${relativePath}`);
  }
}

const forbiddenPaths = ["labs/solutions", "instructor", "answer-key"];
for (const relativePath of forbiddenPaths) {
  try {
    await access(path.join(root, relativePath));
    failures.push(`Student template must not contain: ${relativePath}`);
  } catch {
    // Absence is the expected result.
  }
}

const majorVersion = Number.parseInt(process.versions.node.split(".")[0], 10);
if (majorVersion !== 24) {
  failures.push(`Node.js 24 is required; this terminal is using ${process.version}.`);
}

for (const week of ["week-01", "week-02", "week-03"]) {
  const relativePath = `labs/${week}/index.html`;
  try {
    const source = await readFile(path.join(root, relativePath), "utf8");
    if (!/^<!doctype html>/i.test(source)) {
      failures.push(`${relativePath} must begin with the HTML doctype.`);
    }
    if (!/<html\s+lang="en">/i.test(source)) {
      failures.push(`${relativePath} must declare the document language.`);
    }
    if (!/<title>[^<]+<\/title>/i.test(source)) {
      failures.push(`${relativePath} must contain a non-empty title.`);
    }
    if (week === "week-01" && !/<h1>Campus Hub setup check<\/h1>/i.test(source)) {
      failures.push(`${relativePath} must display the orientation setup-check heading.`);
    }
  } catch {
    // A missing file has already been reported above.
  }
}

async function verifyServer(week) {
  const server = createStaticServer(path.join(root, "labs", week));
  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", resolve);
  });

  try {
    const address = server.address();
    const port = typeof address === "object" && address ? address.port : 0;
    const response = await fetch(`http://127.0.0.1:${port}/`);
    if (response.status !== 200) {
      failures.push(`${week} server returned ${response.status}, not 200.`);
    }
    const contentType = response.headers.get("content-type") ?? "";
    if (!contentType.startsWith("text/html")) {
      failures.push(`${week} server did not return HTML.`);
    }
  } finally {
    await new Promise((resolve, reject) => {
      server.close((error) => error ? reject(error) : resolve());
    });
  }
}

for (const week of ["week-01", "week-02", "week-03"]) {
  await verifyServer(week);
}

if (failures.length > 0) {
  console.error("Coursework setup verification failed:\n");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log("Coursework setup verification passed.");
  console.log("Checked required files, starter HTML, and Week 1-3 HTTP responses.");
}
