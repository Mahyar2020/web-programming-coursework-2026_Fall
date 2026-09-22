import { createReadStream } from "node:fs";
import { stat } from "node:fs/promises";
import http from "node:http";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const contentTypes = new Map([
  [".css", "text/css; charset=utf-8"],
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".txt", "text/plain; charset=utf-8"],
]);

function sendText(response, statusCode, message) {
  response.writeHead(statusCode, { "Content-Type": "text/plain; charset=utf-8" });
  response.end(message);
}

export function createStaticServer(rootDirectory) {
  const root = path.resolve(rootDirectory);

  return http.createServer(async (request, response) => {
    if (request.method !== "GET" && request.method !== "HEAD") {
      response.setHeader("Allow", "GET, HEAD");
      sendText(response, 405, "405 Method Not Allowed\n");
      return;
    }

    let pathname;
    try {
      pathname = decodeURIComponent(new URL(request.url, "http://localhost").pathname);
    } catch {
      sendText(response, 400, "400 Bad Request\n");
      return;
    }

    const requestedPath = path.resolve(root, `.${pathname}`);
    const isInsideRoot =
      requestedPath === root || requestedPath.startsWith(`${root}${path.sep}`);

    if (!isInsideRoot) {
      sendText(response, 403, "403 Forbidden\n");
      return;
    }

    let filePath = requestedPath;
    try {
      const fileStatus = await stat(filePath);
      if (fileStatus.isDirectory()) filePath = path.join(filePath, "index.html");
      const finalStatus = await stat(filePath);
      if (!finalStatus.isFile()) throw new Error("Not a regular file");
    } catch {
      sendText(response, 404, "404 Not Found\n");
      return;
    }

    const contentType = contentTypes.get(path.extname(filePath).toLowerCase()) ??
      "application/octet-stream";
    response.writeHead(200, { "Content-Type": contentType });
    if (request.method === "HEAD") {
      response.end();
      return;
    }

    createReadStream(filePath).pipe(response);
  });
}

const isCommandLineEntry =
  process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href;

if (isCommandLineEntry) {
  const rootDirectory = process.argv[2] ?? ".";
  const port = Number.parseInt(process.argv[3] ?? "8000", 10);

  if (!Number.isInteger(port) || port < 0 || port > 65535) {
    console.error("Port must be an integer from 0 through 65535.");
    process.exit(1);
  }

  const server = createStaticServer(rootDirectory);
  server.listen(port, "127.0.0.1", () => {
    const address = server.address();
    const actualPort = typeof address === "object" && address ? address.port : port;
    console.log(`Serving ${path.resolve(rootDirectory)}`);
    console.log(`Open http://localhost:${actualPort}/`);
    console.log("Press Ctrl+C to stop.");
  });
}
