# Image-generation prompts for Foundations Edition v5

These prompts document the two generated educational illustrations added to the
revised PDF. Both were generated with the built-in image-generation workflow and
saved as project assets before publication.

## Figure 4 - Client and server software roles

```text
Use case: scientific-educational
Asset type: university textbook illustration for an A4 PDF
Primary request: Create a polished educational illustration explaining that
client and server are software roles, not permanent kinds of computers. Show a
student laptop on the left running a web browser. The browser sends a clearly
directed request arrow to a central application server. The application server
sends a response arrow back to the browser. The same application server also
sends a separate database query arrow to a database server on the right and
receives a result arrow back, demonstrating that the application server becomes
a client when it calls another service.
Scene/backdrop: clean modern computer-network teaching diagram on a pale warm
background, with subtle campus technology motifs and ample white space
Style/medium: high-quality editorial vector-style raster illustration, precise,
professional, friendly but not childish
Composition/framing: wide landscape, three evenly spaced groups, all boxes and
arrowheads comfortably inside the image boundary
Color palette: deep navy, teal, cyan, warm amber accents, high contrast
Text (verbatim): "STUDENT DEVICE", "Browser - client role", "HTTP request",
"HTTP response", "APPLICATION SERVER", "Server role for browser", "Client role
for database", "Database query", "Database result", "DATABASE SERVER", "Stores
trusted data"
Constraints: exact English labels; arrows must have unmistakable direction and
terminate cleanly before the target; no arrows crossing labels; equal visual
height for the three principal device groups; legible at textbook print size;
every label belongs beside the object or path it identifies; no logos; no
watermark
Avoid: decorative clouds that imply the Internet is one machine, random code
text, tiny illegible labels, cropped arrowheads, overlapping boxes, misleading
bidirectional single arrows
```

Final asset: `assets/images/client-server-software-roles-v1.png`

## Figure 15 - Local development and public deployment

```text
Use case: scientific-educational
Asset type: university textbook illustration for an A4 PDF
Primary request: Create an accurate educational network illustration comparing
local web development with public web deployment. LEFT ZONE: one student laptop
contains both a browser and a small development server. Draw a short internal
loopback request/response path labelled localhost. Clearly mark this setup Not
public and Same computer. RIGHT ZONE: show a browser device, a small DNS resolver
positioned above and to the side, several interconnected Internet routers, an
HTTPS gateway/reverse proxy, an application server, and a database. First show a
small separate two-arrow DNS lookup between the browser and DNS resolver, labelled
DNS lookup and Address answer. Then show a completely separate main request path
from browser through Internet routers to HTTPS gateway, then application server;
the database is accessible only from the application server. Show the response
returning along the main path. There must be NO path or arrow from DNS to the
HTTPS gateway, application server, or database.
Scene/backdrop: spacious clean network map on a light neutral background with
subtle university motifs
Style/medium: high-quality editorial vector-style raster illustration, precise,
professional, visually attractive but technically sober
Composition/framing: wide landscape with two clearly separated zones, all boxes,
labels, paths, and arrowheads fully inside the image boundary
Color palette: navy, teal, cyan, soft amber, high contrast
Text (verbatim): "LOCAL DEVELOPMENT", "Browser", "localhost", "Development
server", "Same computer", "Not public", "PUBLIC HTTPS DEPLOYMENT", "Browser
client", "DNS resolver", "DNS lookup", "Address answer", "Internet routers",
"HTTPS gateway", "Application server", "Database", "HTTPS request", "HTTPS
response"
Constraints: exact English labels; DNS arrows exist only between Browser client
and DNS resolver; HTTPS request and response bypass DNS and cross the Internet
routers; database has no public connection; distinct arrow colors and
unmistakable arrow direction; no arrows cross text; labels legible at textbook
print size; no logos; no watermark
Avoid: an Internet cloud as a single machine, DNS in the page-content path, DNS
arrow to gateway, direct browser-to-database connection, tiny labels, clipped
arrowheads, overlaps, random code
```

Final asset: `assets/images/local-and-public-server-deployment-v1.png`
