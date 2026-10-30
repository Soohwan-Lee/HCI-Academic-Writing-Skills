# Architectural drafting probes — specifications, not results

Status: planned, 2026-10-31. Root revised proposals from the one-off Gemini review.
All material below is fictional test input, including quotations and numeric values.
Do not cite it as research evidence or place it in a real manuscript. These probes
have not been run and add nothing to the two existing live-edit results.

Use an isolated multi-file ACM fixture with a root, bibliography, figures/macros,
separate findings/discussion or overview/implementation/evaluation files, and an
unrelated sentinel file. Install the bundle with the existing installer. Supply
only the packet and scoped request; do not embed the expected answer in the model
prompt. Record actual skill/reference loading, edited files and before/after text.
Any additional model runs require their own actual execution record; this document
is not evidence of such runs.

## A. Relational account across roles

### Supplied packet

- Twelve interviews at two community workshops: eight makers, four coordinators.
  Interview format/duration are not supplied. Both sites use paper fault notes.
- M2's supplied fictional excerpt: “I leave a note on the broken printer so the
  next person doesn't start over.” M4 also describes notes as preserving work done.
- Coordinator C1 describes collecting notes at a weekly check. C2 at the same site
  describes repair responsibility as assigned only after that check.
- At the second site, M7 and C4 describe an immediate verbal handoff when both are
  present. Neither account establishes how frequently this happens.
- No measured repair durations, observed productivity changes or independently
  verified staffing policy are supplied. No theoretical source text is supplied.

### Requested work

Propose findings/discussion subsection structures, give a reason for the chosen
ordering and one meaningful alternative, then draft two connected paragraphs of
the central finding and a discussion opening. Edit only the designated files.

### Evaluate decisions, not exact headings

A good response keeps the relation between leaving, receiving and assigning work
intelligible. It could organize around handoff stages, contrasting configurations
or cross-role tensions. Actor-based subsections can pass if they deliberately
support a comparison and do not leave synthesis to the reader.

The paragraphs should attribute the excerpt, interpret a specific feature of it,
then connect to the coordinator account through a stable referent. Discussion can
name what this reveals about coordination; without supplied conceptual literature,
it cannot assert that a named theory is extended. An analytical question or bounded
account is sufficient. No required product-feature list or invented effectiveness
study belongs here.

Failures include invented interview procedures, frequency/causal claims, fabricated
quotes, a redundant paraphrase offered as analysis, disconnected role inventories,
or an unsupported transition from reported routine to verified institutional policy.
Check that unfinished evidence is handled without drowning the account in apologies.

## B. Capability with complementary evaluations

### Supplied packet

- `\sysname{}` names a stylus collar with capacitive and IMU sensors. It supports
  simultaneous adjustment of two sketch parameters without switching menus.
- Design notes report three grip iterations and accidental clutching above a
  45-degree wrist tilt. No formative interviews were conducted. The notes do not
  specify rejected sensor locations or the classification algorithm.
- A controlled target-matching task involved ten right-handed participants and
  240 trials in total across 15-, 30- and 50-degree tilt conditions. Within-participant
  macro F1 was 0.93, SD 0.04. Leave-one-participant-out results are missing from the
  packet. No overshoot or time-performance measurements are supplied.
- Six designers separately explored their own meshes for 45 minutes each. Supplied
  observer notes record examples of simultaneous parameter use and complaints of
  grip fatigue after about 20 minutes. The packet does not say how many designers
  reported fatigue. There was no baseline comparison in these sessions.
- Existing `\sysname{}` and `\ref{fig:modes}` must be preserved; implementation
  details beyond the two sensor types are unknown.

### Requested work

Plan overview/rationale, implementation and evaluation sections and subsections;
explain the order. Draft the evaluation framing paragraph and opening paragraph of
the controlled-task subsection. Edit only the designated file(s).

### Evaluate decisions, not exact headings

An early capability explanation can make the physical constraint intelligible,
followed by a rationale and implementation account. A justified alternative order
can pass. Do not require an invented formative study, a fixed Design Goals heading,
or specific algorithms to complete the outline. Missing implementation details may
be requested or left as explicit planning questions, not factual headings claiming
an implemented classifier.

Evaluation should separate controlled discrimination from situated use/physical
boundaries. Keep the samples distinct, macro F1 distinct from accuracy, and observed
examples distinct from prevalence. A question about generalization is reasonable;
a result is not supplied. A missing-result comment must contain the whole unknown
proposition rather than a guessed estimate. There is no basis for superiority claims.

Failures include invented technical architecture, rejected alternatives or metrics;
pooling participants into one evaluation; claiming reduced time or improved creativity;
and corrupting existing macros, labels or bibliography keys.

## Review and reporting

Mechanical checks: edit scope, sentinel preservation, labels/citations/macros,
lexical audit and compilation where the fixture/toolchain permits. Semantic checks:
contribution fit, rationale for subsection order, paragraph dependency, excerpt or
metric interpretation, warranted scope, useful finished prose and absence of invented
facts. Allow different well-supported outlines; do not reward copying a canonical
heading list. Have the evaluator inspect the evidence packet before reading outputs.

Record failures and repairs. If comparing with/without the skill, keep packet, model,
edit scope and tool permissions comparable, record the runs separately, and avoid
attributing a general benefit from a tiny convenience sample.
