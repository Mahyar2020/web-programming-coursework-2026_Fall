# Image-generation record for PDF v8

## Figure 2 - development workstation evidence loop

Saved asset: `assets/images/development-workstation-evidence-loop-v1.png`

Tool mode: built-in image generation, new raster asset followed by one targeted
label correction.

### Generation prompt

```text
Use case: scientific-educational
Asset type: wide university textbook illustration for an A4 PDF
Primary request: Create a polished instructional illustration that explains a beginner web-programming workstation and the evidence loop used in this course. Show one adult university student at a desk with a laptop. On and around the laptop, depict clearly separated labelled stations connected by clean directional arrows: a code editor where the student edits project files; a terminal that runs commands; Node.js and npm supplying the runtime and course scripts; a local web server; a browser requesting localhost; browser developer tools inspecting the response; automated tests checking the project; and Git recording a commit in repository history. Make the sequence and tool relationships visually unmistakable without suggesting that all tools are one program.
Scene/backdrop: modern university computer laboratory, light neutral background, subtle network and file motifs
Style/medium: high-quality editorial vector-style raster illustration, precise, professional, welcoming, suitable for a rigorous computer engineering textbook
Composition/framing: wide landscape; student and laptop centered; stations arranged in a spacious clockwise loop; every box, label, connector, endpoint, and arrowhead fully inside the image; no overlapping arrows or labels
Color palette: deep navy, teal, cyan, warm amber accents, high contrast
Text (verbatim): "STUDENT WORKSTATION", "CODE EDITOR", "PROJECT FILES", "TERMINAL", "NODE.JS + NPM", "LOCAL WEB SERVER", "BROWSER + DEVTOOLS", "AUTOMATED TESTS", "GIT HISTORY", "edit", "run", "request localhost", "inspect", "test", "commit"
Constraints: exact English labels; adult university student shown respectfully; indicate CODE EDITOR and TERMINAL as separate applications; LOCAL WEB SERVER runs through NODE.JS + NPM; BROWSER + DEVTOOLS requests localhost from the server; AUTOMATED TESTS inspect the project; GIT HISTORY records commits; all text legible at textbook print size; no product logos; no watermark
Avoid: installation wizard screenshots, command output too small to read, cloud deployment, database, crossed connectors, cropped labels, cropped arrowheads, misleading direct browser-to-Git path, random code, decorative clutter
```

### Targeted correction prompt

```text
Use case: precise-object-edit
Asset type: university textbook workstation illustration
Primary request: Correct only the labels and meaning of the two bottom horizontal arrows in the supplied image. The arrow traveling from "BROWSER + DEVTOOLS" toward "AUTOMATED TESTS" must be labelled exactly "test". The arrow traveling from "AUTOMATED TESTS" toward "GIT HISTORY" must be labelled exactly "commit". Add the small verb "inspect" inside the "BROWSER + DEVTOOLS" panel near the DevTools area, without covering existing content. Keep the overall clockwise loop and every other box, label, person, background, color, connector, arrowhead, and layout unchanged.
Text (verbatim): "test", "commit", "inspect"
Constraints: change only those lower action labels; retain "edit", "run", and "request localhost" exactly; all labels and arrowheads fully inside the canvas and legible at textbook size
Avoid: moving panels, redrawing the student, changing code, changing URLs, adding arrows, crossed connectors, cropped text, watermark
```
