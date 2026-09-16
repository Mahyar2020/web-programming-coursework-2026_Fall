# Image-generation record for PDF v9

## Figure 0.4 - repository-first student workflow

Saved asset: `assets/images/repository-first-workflow-v1.png`

Tool mode: built-in image generation, new raster asset followed by one targeted
text correction.

### Generation prompt

```text
Use case: scientific-educational
Asset type: wide landscape illustration for a university web-programming textbook
Primary request: Explain a repository-first student workflow. Show a university student creating a private remote coursework repository, cloning it to one clearly bounded local project folder on a laptop, editing files only inside that folder, verifying changes, committing a checkpoint, and pushing the commit back to the remote repository. Use clean directional arrows and make local versus remote locations unmistakable.
Scene/backdrop: modern university study desk with a laptop; remote repository represented as a secure hosted storage panel, not as an atmospheric cloud
Style/medium: polished editorial vector-style raster illustration, rigorous but welcoming, high print quality
Composition/framing: wide horizontal layout with five evenly spaced stages; every box, label, connector, and arrowhead fully inside the canvas; no crossed arrows
Color palette: deep navy, teal, cyan, and restrained warm amber accents on a light neutral background
Text (verbatim): "1 CREATE PRIVATE REPOSITORY", "2 CLONE", "3 EDIT INSIDE PROJECT", "4 COMMIT", "5 PUSH", "REMOTE REPOSITORY", "LOCAL PROJECT FOLDER", "package.json"
Constraints: exact English labels; show package.json visibly inside LOCAL PROJECT FOLDER; distinguish commit as local history and push as remote synchronization; no product logos; no terminal commands; no watermark
Avoid: suggesting that Git automatically uploads every saved file, direct editing in remote storage, nested repositories, cropped text, cropped arrowheads, overlapping labels, decorative clutter
```

### Targeted correction prompt

```text
Use case: precise-object-edit
Asset type: university textbook repository-first workflow illustration
Primary request: Correct only the heading in the lower history panel of stage 5. Replace the misspelled text with exactly "REMOTE HISTORY (COMMITS)".
Text (verbatim): "REMOTE HISTORY (COMMITS)"
Constraints: change only that one heading; preserve every stage, number, arrow, box, student, laptop, repository, folder, commit entry, color, spacing, and all other text exactly as shown; keep the corrected heading fully inside its panel
Avoid: changing layout, changing any other label, adding objects, cropped text, watermark
```

The exact terminal, localhost, and Network-panel figures in this edition are
code-native textbook facsimiles produced by the PDF builder. Their interface
labels, commands, paths, status codes, and headers therefore remain deterministic
and testable rather than depending on generative rendering.
