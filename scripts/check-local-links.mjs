import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ignoredDirectories = new Set([".git", "instructor-private", "node_modules", "reports"]);
const failures = [];

async function collectMarkdown(directory) {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (entry.isDirectory() && ignoredDirectories.has(entry.name)) continue;
    const entryPath = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await collectMarkdown(entryPath));
    if (entry.isFile() && entry.name.endsWith(".md")) files.push(entryPath);
  }
  return files;
}

for (const markdownPath of await collectMarkdown(repositoryRoot)) {
  const markdown = await readFile(markdownPath, "utf8");
  const links = [...markdown.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)];

  for (const match of links) {
    const rawTarget = match[1].trim().replace(/^<|>$/g, "");
    if (/^(?:https?:|mailto:|#)/i.test(rawTarget)) continue;

    const withoutFragment = rawTarget.split("#", 1)[0];
    if (!withoutFragment) continue;

    const decodedTarget = decodeURIComponent(withoutFragment);
    const absoluteTarget = path.resolve(path.dirname(markdownPath), decodedTarget);
    try {
      await stat(absoluteTarget);
    } catch {
      const relativeSource = path.relative(repositoryRoot, markdownPath);
      failures.push(`${relativeSource}: broken local link ${rawTarget}`);
    }
  }
}

if (failures.length > 0) {
  console.error("Local link verification failed:\n");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log("Local Markdown link verification passed.");
}
