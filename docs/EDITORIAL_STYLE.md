# Editorial and Teaching Style

This guide applies to every student-book chapter and instructor resource.

## Explain from the detail to the whole

1. Begin with a concrete situation, observable failure, or user task.
2. Describe what the learner can see before introducing a formal name.
3. Introduce one term and its purpose in plain English.
4. Show a minimal example and explain every meaningful part.
5. Connect the example to the larger system and its boundaries.
6. Ask the learner to predict, observe, and explain.

Do not begin a novice section with a dense list of technologies. Build the list
only after each item has a role in the learner's mental model.

## Abbreviations

- At the first meaningful use in each chapter, write the full form followed by
  the abbreviation in parentheses.
- Use the abbreviation alone afterward when it improves readability.
- Do not expand an established protocol name inaccurately. Explain its history
  separately when necessary.
- Repeat the full form when many pages have passed or when a table must stand on
  its own.

## Punctuation and code notation

- Avoid a bare colon immediately before a URL or code sample when a novice could
  mistake it for part of the value. Prefer “Consider the following URL.”
- Put URLs, addresses, header fields, commands, and code punctuation in code
  formatting.
- When a punctuation mark has technical meaning, name that meaning explicitly.
  For example, explain the colon after a URL scheme separately from the colon
  before a port.
- Use ASCII hyphens in PDF source text.

## Human, professional voice

- Address the learner as an intelligent beginner, not as an expert and not as a
  child.
- Prefer direct sentences and concrete verbs.
- Explain why a distinction matters before presenting exceptions.
- Avoid filler such as “simply,” “obviously,” and “just.” These words can hide a
  missing explanation.
- State the limits of a teaching model without making the model sound useless.
- Use examples from the continuing Campus Hub application so teachers can connect
  one session to the next.

## Tables and figures

- Number every instructional table and figure and give it a descriptive caption.
  Use chapter-local decimal numbering: Figure 0.1 for preliminary/orientation
  material, Figure 1.1 for the first figure in Chapter 1, Figure 2.1 for the first
  figure in Chapter 2, and so forth. Restart the local figure number at 1 in each
  numbered chapter; never append alphabetic suffixes.
- Mention the table or figure by number in the surrounding prose before or after
  it appears, and explain what relationship the learner should notice.
- State whether boxes operate together, sequentially, alternatively, or
  independently.
- Communicate the visual's essential relationship naturally in the surrounding
  explanation. Do not print a detached paragraph labelled “Text alternative:”
  as though it were another caption.
- Keep every object, label, and arrowhead inside the figure boundary.

## Code and rendered output

- Treat short snippets as parts of one named, cumulative example whenever
  possible; avoid a parade of unrelated fragments.
- Show a browser screenshot for each complete HTML/CSS example and refer to it
  by figure number. If several snippets modify the same cumulative page, state
  which final output figures demonstrate their combined result.
- Use browser-produced screenshots, not invented interface mockups, when the
  purpose is to demonstrate executable code output.
- Distinguish source code, browser output, protocol messages, and terminal output.
  Not every code fence has a visual browser result.

## Answers and teaching support

- A worked answer must explain the reasoning, the relevant boundary, and at least
  one common misconception.
- Laboratory checkpoints should give instructors natural places to pause for a
  prediction, demonstration, or quick formative assessment.
- When several answers are defensible, name the decision criteria instead of
  presenting one preference as universal law.

## Sources and technical currency

- Use a standards document or official project documentation as the authority for
  behavior that can change. Use university materials and books to improve
  pedagogy, sequencing, examples, and exercises.
- Paraphrase sources in the author's own teaching voice. Quote only when the exact
  wording matters and identify the source beside the quotation.
- Every chapter ends with a short annotated reading list. Explain what each source
  helps the reader learn; do not present an unexplained wall of links.
- Put the last technical-review date and update-sensitive topics in every chapter.
  Keep tool versions in the tested project configuration whenever possible.
- Prefer terms that remain true across products. When a framework-specific term is
  necessary, distinguish it from the underlying web-platform concept.
