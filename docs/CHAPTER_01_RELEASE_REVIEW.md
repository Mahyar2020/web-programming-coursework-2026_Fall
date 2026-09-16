# Chapter 1 Release Review

Review date: **1 September 2026**  
Decision: **PASS — ready as the prerequisite for Chapter 2**

## Release judgment

Chapter 1 now provides the conceptual and practical foundation needed before a
student writes a substantial page. It begins with the distinction between the
Internet and the Web, then builds outward through client and server roles,
resource identification, name resolution, secure transport, HTTP exchanges,
browser processing, local and public web servers, evidence-led debugging, a
minimal HTML document, and a small Git workflow. Every major model is reinforced
by a labelled figure, a prediction or observation activity, assessed practice,
and a fully explained answer.

## Comparison basis

The release gate compared the chapter with the introductory sequence and stated
learning outcomes in Harvard CS50 Web Programming, the University of Washington
CSE 154 curriculum, current MDN learning modules, the WHATWG HTML standard, and
the relevant IETF descriptions of URLs, DNS, HTTP, and TLS. The comparison asked
whether a novice can explain a page navigation as one cooperating system rather
than memorize disconnected vocabulary.

## Coverage matrix

| Area | Evidence in Chapter 1 | Decision |
|---|---|---|
| Internet and Web | Packet-network infrastructure is distinguished from the Web application layer. | Complete for entry level |
| Client and server | Roles are explained as exchange-specific; one process may be a server in one exchange and a client in another. | Complete |
| URL and origin | Scheme, authority, host, port, path, query, fragment, and same-origin reasoning are introduced with examples. | Complete for prerequisites |
| Navigation and DNS | The request journey, resolver hierarchy, record types, IPv4 dotted-decimal notation, IPv6 purpose, caching, and diagnostic observations are connected. | Complete for prerequisites |
| Protocol cooperation | Application, security, transport, network, and link responsibilities are shown as simultaneous layers rather than competing alternatives. | Complete |
| TLS and HTTP | HTTPS purpose, request methods, response status, headers, content, caching, and safe/idempotent distinctions are introduced. | Complete for prerequisites |
| Browser pipeline | Fetching, parsing, DOM construction, dependent resources, rendering, and interaction are presented as a causal pipeline. | Complete |
| Web-server setup | Local development and public deployment are distinguished, with a tested local-server laboratory. | Complete for the first session |
| Engineering practice | DevTools, command-line evidence, prediction, debugging, minimal HTML, Git snapshots, exercises, answers, and quiz checks are included. | Complete |

## Deliberate later placement

The chapter does not attempt to teach every downstream implementation detail.
DOM programming belongs in the JavaScript chapters; request handlers and server
frameworks belong in the server-side chapters; cookies, sessions, authentication,
and Cross-Site Request Forgery defenses belong with state and security; reverse
proxies, process supervision, deployment automation, observability, and scaling
belong in the production chapters. Chapter 1 names these boundaries without
prematurely duplicating their later treatment.

## Maintenance conditions

The conceptual release is approved. Future maintenance should still review dated
tool screenshots, browser-specific developer-tool labels, supported protocol
versions, and external links before each academic year. Passing this gate means
the chapter is ready to teach; it does not mean the Web platform will never
change.
