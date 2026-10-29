# Writing inside an ACM LaTeX project

Use this when modifying manuscript files. The goal is a useful, reviewable change
in the existing project, ready for the researcher's normal Overleaf workflow.
Uploading, submitting or changing external projects requires corresponding user
instructions; local editing does not imply those actions.

## Locate the manuscript with minimal inspection

Read applicable project instructions and the working-tree state. Identify the root
file from the build configuration, editor magic comment or documentclass/include
structure; do not assume the file named main.tex is active. Follow relevant
`\input`/`\include` files and locate the bibliography. Read the requested section,
adjacent transitions, referenced tables/figures and evidence needed for its claims.
For a paragraph edit, avoid loading the entire corpus or unrelated project files.

Respect existing class/options, macros, packages, citation style, anonymization,
labels, figure paths and author edits. Change them when the task requires it, not
as incidental cleanup. Do not replace an existing ACM template with a newer one
merely because a writing task is underway. Follow the user's actual venue/track and
submission stage, including whether anonymous or camera-ready metadata applies.

## Edit the smallest coherent scope

Keep prose in its existing section file. Reuse semantic macros and citation keys.
When moving text, move a citation only if it still supports the resulting claim;
recheck attachment after merging sentences. If a label or reference must change,
update its dependents within authorized scope. Do not globally rename keys or
reformat whole files for a local prose revision.

Preserve numerical values, units, condition names, participant quotations and
pseudonyms unless the task or verified evidence calls for correction. Separate
corrections to factual claims from stylistic edits in the short change report.
Missing evidence can be marked in a native comment:

```tex
% HCI-TODO[evidence]: confirm the analysis unit before finalizing this claim.
```

Default to source comments; use visible markers only through the project's existing
draft convention, and identify unresolved markers in the final report.
Use comments sparingly, where the author can resolve a specific question. A TODO
must not conceal a polished unsupported result in the visible manuscript. When
necessary, leave a clearly marked draft placeholder or omit the unsupported
assertion while completing surrounding supported text. Ask a focused question only
when its answer is necessary for the next dependent edit.

## Work from evidence, not bibliography presence

For wording-only revision, retain the author's existing claims and citation scope
without demanding a new source audit. Recheck when introducing a claim, changing
what a citation supports, strengthening the inference, or noticing a contradiction.
Do not create TODOs merely because unchanged sources were not reopened.

A `.bib` record proves only that a reference is available. Read the relevant source
passage or use supplied verified notes before assigning a substantive claim. Keep
metadata verification, full-text reading and interpretation distinguishable. If a
source is inaccessible, narrow to what is verified or mark the unresolved citation.
Do not invent BibTeX metadata, page numbers, quotes or source-specific findings.
Use the author's established keys where possible; add verified entries only when
needed for the requested writing task.

When supplied outputs and manuscript numbers disagree, inspect provenance before
choosing one. Do not silently re-run analyses, select favorable models or convert
an exploratory observation into a planned hypothesis to improve narrative flow.
Writing can clarify an inference; it cannot supply absent empirical evidence.

## Check and deliver

Inspect the diff for accidental edits, lost qualifiers, changed citation scope and
broken math/escaping. Run the bundled read-only helper when structural changes,
new citations or labels make it useful:

```sh
python3 /path/to/hci-academic-writing/scripts/latex_audit.py paper.tex --json
```

Pass `--project-dir` when the compilation working directory differs from the root
file's parent. The helper reads literal local includes and bibliography entries,
reports TODOs, and checks reference/key consistency. It does not expand TeX or
judge factual citation support. Dynamic macros/conditionals can downgrade findings
to warnings. A clean report is not proof of compilation or correct scholarship.

Use an existing, understood local build when appropriate. Inspect unfamiliar build
configuration before execution; keep generated files in the project's intended
output directory and preserve unrelated files. If compilation is unavailable,
report that specifically while still checking the text and diff. Do not claim an
Overleaf build from a local build. For substantial structural changes, inspect the
resulting PDF for heading flow, floats, references and accidental layout damage.
A reversible wording-only edit does not require inventing a new test suite.

Finish with the files/sections changed, the substantive improvement, checks actually
performed and essential unresolved author decisions. Keep the report shorter than
the manuscript edit. A long drafting task may benefit from a compact state note
tracking claims/evidence/open items; a single paragraph should not trigger a new
mandatory planning artifact.
