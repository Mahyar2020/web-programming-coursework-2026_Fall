# Image-generation prompts for revised edition v4

All assets were produced with the built-in image-generation tool.

## Figure 3 - labeled request journey

Use case: precise-object-edit. Add the exact labels `Browser`, `Wi-Fi access
point`, `Campus router`, `Internet routers`, `TLS protection`, `Web server`,
`HTTP request`, `HTTP response`, and `Rendered page` to the existing request
journey. Place object labels with restrained leader lines, put request and
response labels beside their respective paths, preserve every object and route,
and keep every label readable and inside the canvas.

## Figure 4 - HTML, CSS, and JavaScript

Use case: precise-object-edit. Add the exact labels `HTML`, `Structure and
meaning`, `CSS`, `Presentation and layout`, `JavaScript`, `Behavior and state`,
`Same document`, `Style applied`, and `Interaction changes state` to the existing
three-stage browser illustration. Preserve the three panels, transformation
arrows, interface details, colors, and composition.

## Figure 5 - website, web application, and API

Use case: precise-object-edit. Add the exact labels `Website`, `Linked documents`,
`Web application`, `Interactive state`, `API`, `Software-to-software interface`,
`HTTP requests`, `HTTP responses`, and `Shared Web infrastructure` to the existing
three-panel illustration. Keep labels within their corresponding panels and
preserve every device, connector, server, and arrow.

## Figure 8 - campus-to-data-center network

Use case: precise-object-edit. Make the `Local network`, `Transit networks`, and
`Data-center network` containers equal in top position, bottom position, and
height. Add the exact labels `Student browser`, `Wi-Fi access point`, `Campus
switches`, `Campus border router`, `DNS resolver`, `Web server`, `HTTP request`,
`HTTP response`, and `Packets forwarded hop by hop`. Preserve the campus scene,
router topology, geographic cutaway, and request and response paths. The final
refinement removed an incorrect duplicate `DNS resolver` label from the server
rack and added the missing `Student browser` label to the laptop.

## Figure 10 - protocol cooperation across a network

Use case: scientific-educational. Visualize an HTTPS page request from a campus
browser through an access point and multiple routers to a web server. Show sender
encapsulation, hop-by-hop forwarding with changing link frames, and the response
path. Use the exact labels `Page resource`, `HTTP request`, `TLS protection`,
`TCP byte stream`, `IP packet`, `Wi-Fi frame`, `Ethernet frame`, `Router`, `Link
frame changes at every hop`, `IP packet continues toward the destination`, `HTTP
response`, and `Browser renders the page`. Do not imply that routers read HTML or
HTTP.

## Figure 11 - DNS name resolution and IPv4

Use case: scientific-educational. Explain DNS as a distributed hierarchical
naming system and show how the browser obtains the A-record answer
`192.0.2.40`. Show Browser -> Stub resolver -> Recursive resolver, followed by
Root DNS server -> `.edu` DNS server -> Authoritative DNS server, with the answer
returned to the recursive resolver and cached until its time to live expires.
Alongside it, divide `192.0.2.40` into four octets and label every octet as `8
bits` with the allowed range `0-255`; label the whole address `32 bits total` and
state `Dots separate four octets` and `Documentation address - not a real Campus
Hub server`. The final refinements removed the misleading browser-to-root arrow
and placed the query arrow from the recursive resolver to the root server.

For every prompt: use premium university-textbook illustration quality; keep all
text exactly spelled, large enough for reproduction, and inside the canvas; use
no logos, brands, watermarks, or decorative text.
