---
name: hci-academic-writing
description: Draft and revise HCI research manuscripts in existing ACM LaTeX projects. Use for contribution framing, abstracts, introductions, related-work synthesis, paragraph and sentence flow, evidence-aligned discussion, review papers, compression, and reviewer responses across CHI, CSCW, UIST, DIS and IUI. Routes by knowledge contribution rather than venue or method alone.
---

# HCI academic writing

Help the researcher produce useful manuscript text, not only an editorial report.
For a scoped request, read the relevant section and its dependencies, make the
requested changes, and explain material unresolved issues briefly. For a full
paper, establish the contribution and evidence before expanding prose.

## Start from the actual task

Identify the requested output, target venue/track, study stage, available evidence,
root `.tex` and edit scope from the conversation and project. Ask only for missing
information that changes the argument; continue supported work meanwhile. If the
user requests one paragraph, do not require a project-wide intake or new ledger.

Find the paper's knowledge contribution: what should readers understand, build,
do or reconsider after reading it, and what evidence supports that change? Treat
venue, contribution, method and manuscript form as separate choices. A study used
to evaluate a system does not automatically make the paper empirical-first.

For sentence/paragraph polish, load paragraph flow only; add a route if the edit
changes the kind or scope of a claim. For section drafting, load section guidance
and the relevant route. For whole-paper framing, load the route and section guide;
add budgets only when length matters. A system evaluation usually remains inside
the artifact route; use hybrids when two substantive claims need distinct warrants.

For contribution framing or claim-changing edits, use the
[contribution catalogue](references/contribution-catalogue.md) to distinguish finer
claims: characterization, sociotechnical explanation, theory application/revision,
critique, historical inquiry, participatory change, replication and others. The
following routes provide writing/evidence support; they are not an exhaustive
classification of contributions. HCAI is a topic, and an interview is a method.
For sociotechnical relations, also consult the focused
[sociotechnical guide](references/sociotechnical.md).

Load only the matching support route(s):

| Main knowledge claim | Reference |
|---|---|
| Measured comparison, relationship or explanatory account | [Quantitative](references/routes/empirical-quantitative.md) |
| Situated social account or interpretive understanding | [Qualitative](references/routes/empirical-qualitative.md) |
| New system, interaction capability or technique | [Artifact](references/routes/artifact.md) |
| Design understanding through making and reflection | [Design / RtD](references/routes/design.md) |
| Concept, theory, framework or critical argument | [Conceptual](references/routes/conceptual.md) |
| Method, instrument or evaluation procedure | [Method](references/routes/method.md) |
| Dataset, benchmark, corpus or reusable research resource | [Resource](references/routes/resource.md) |
| Synthesis of a research literature | [Review](references/routes/review.md) |
| Multiple substantive claims or complementary evidence | [Hybrids](references/routes/hybrids.md) |

## Choose the shortest useful workflow

- **Frame/outline:** state the claim, its support and boundary; assign each section
  a job; give paragraphs working claims or questions. Resolve duplicated jobs.
- **Before results exist:** draft motivation, related work and the actual method.
  Keep result-dependent abstract/contribution slots in explicit draft comments;
  record which promises need reconciliation after analysis. Do not write imagined
  findings or conditional success stories as visible finished prose. Keep the visible
  wording explicitly planned; even a scaffold should not say "we report a study"
  when collection has not begun.
- **Draft:** turn supplied evidence into paragraphs. For empirical work, verified
  findings often provide the strongest starting point; for conceptual/design work,
  start with the central argument or annotated cases. Reconcile openings afterward.
- **Revise:** diagnose the specific break in inference, positioning or flow, then
  edit the prose. Offer an alternative only when it changes a consequential choice.
- **Compress:** protect claims, evidence, uncertainty and construct definitions;
  remove repetition and nonessential background. Use an explicit target and report
  the counting convention if giving word counts.
- **Respond to review:** map each comment to an answer, supporting evidence and
  manuscript change. Complete supported edits; separate new-analysis/study requests
  from changes that writing can honestly resolve. Use [review responses](references/review-responses.md)
  for substantive rebuttal or revision tasks.

Read [section architecture](references/sections.md) for abstract/intro/RW/discussion
work, [paragraph flow](references/paragraphs.md) for local revision, [word budgets](references/word-budgets.md)
for length planning, and [LaTeX workflow](references/latex-workflow.md) before file edits.

## Maintain the evidence contract

For evidence-sensitive drafting, briefly identify supplied facts and missing facts
in your working reasoning. Do not complete missing details with familiar defaults:
interviews need not be semi-structured, a literature review need not be systematic,
and a sample of eight does not mean all eight showed the reported behavior.
When a fact is unknown, omit it or place the **whole missing proposition** in a
draft comment. Do not assert a plausible fact and append “verify this” as a repair.
Optional methodological suggestions must remain separate from manuscript facts.

Keep observed findings, interpretation, proposed mechanisms and future possibilities
distinguishable. Never invent studies, participants, quotations, statistics,
references or claims of having read a source. During wording-only revision, preserve existing author-owned claims and citation
attachments without requiring every source to be reread. Verify new claims, changed
citation scope, strengthened wording and apparent contradictions; do not add TODOs
solely because an unchanged cited source was not opened.

A BibTeX entry verifies neither its
content nor the claim attached to it. Mark missing substantive evidence with a
concise comment, such as `% HCI-TODO[evidence]: verify the condition contrast`.
Do not leave unsupported factual assertions polished into apparently final prose.

Preserve the author's terminology and epistemological commitments where coherent.
Prefer clear subjects, specific verbs, connected reasoning and varied paragraph
structures over stock enthusiasm or rigid sentence counts. Topic-first writing is
useful when readers can understand the claim immediately; it is not mandatory.

Throughout the references, P-ID examples identify purposive, version-specific analyses;
“hypothetical” examples assume their stated evidence and are structural illustrations.
Neither supplies findings to insert into another manuscript. Source examples are not universal conventions
or proof that awards validate a writing style. Planning allocations are editorial
heuristics. Complete edits within scope, check the diff and relevant references,
and report what changed, what was checked and any evidence still needed.

## Select evidence and manuscript form

Use the [corpus index](references/corpus-index.md) when an exemplar would resolve
an architectural decision; retrieve only the relevant one or two analyses. Cite
an exemplar's source/version and explain its fit, rather than borrowing its prose.
For a pictorial, route by contribution **and** visual form: images, captions,
annotations and reading paths may carry the argument. P109 is a resource/method
pictorial, not a conventional linear 8,000-word manuscript. Do not force it into
IMRaD or apply prose budgets to a visual submission. Confirm current venue/track
requirements from the author's template or official call before changing format.
