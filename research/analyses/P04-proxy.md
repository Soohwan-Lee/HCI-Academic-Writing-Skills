# P04 — Proxy Tasks and Subjective Measures

Buçinca, Lin, Gajos, and Glassman. IUI 2020.
[Paper](https://doi.org/10.1145/3377325.3377498) · [Analyzed author PDF](https://kgajos.seas.harvard.edu/papers/bucinca20proxy.pdf).

## Contribution and evidence

Primary route: methodological critique supported by empirical comparison. The quantitative experiments
and qualitative follow-up are its evidential methods, not automatically independent
secondary contributions. The contribution is not a new
explanation algorithm: it challenges whether common evaluation choices justify claims
about human–AI decision performance. Two online experiments contrast task framing and
explanation types, followed by a small in-person think-aloud study. Thus the method used
(experiment) and the contribution offered (evaluation validity) need separate labels.

## Observed architecture

Introduction → related work → experiments → results → qualitative study → discussion
→ conclusion. The qualitative study contains its own task, procedure, participants,
analysis, and results. It is not squeezed into the earlier results section. The discussion
revisits the two hypotheses before integrating the studies and explaining implications.
There is no separate top-level limitations section in this version.

## Opening moves

The abstract identifies a sociotechnical unit of evaluation, exposes a mismatch in
existing evaluation practice, specifies the studies and two targets of critique, reports
contradictory evaluation outcomes, and states the consequence for research progress.

The introduction (pp. 1–2) opens with the expected benefit of complementary human and
AI strengths, immediately followed by evidence of disappointing team performance. It
proposes two methodological explanations, then develops each in a separate paragraph.
Only after motivating both hypotheses does it describe the studies. It previews findings
and an unexpected concern about think-aloud methods, then closes on the implications
for evaluating the joint human–AI system. This is a problem–diagnosis–test argument,
not an exhaustive background followed by a late novelty announcement.

## Paragraph and sentence flow

Introduction, p. 1, opening locator **“First, evaluations that use”**: S1 asserts that
proxy tasks direct attention differently from decision tasks; S2 uses cognitive-effort
research to explain why voluntary attention may differ; S3 derives a hypothesis that
proxy outcomes may not predict decision-task outcomes. This is claim → theoretical
warrant → testable consequence. The opening is deductive about the proposed mechanism,
while the experimental conclusion has not yet been established. The preceding paragraph
announces two methodological concerns; the following paragraph develops the second,
subjective measurement. This parallelism is useful because the paper has two actual
arguments, not because every introduction needs a fixed number of balanced paragraphs.

## Related-work positioning

Section 2.1 connects decision support to cognition and effort. Section 2.2 distinguishes
evaluation taxonomies, explains how this paper's task definitions relate to them, and
contrasts objective performance with subjective assessments. The authors do not merely
claim that earlier work overlooked users: they identify which activity an evaluation
makes the user perform and which inference its measurements can support. This yields
comparison axes that recur in the experiments. Related work is therefore a validity
argument as well as a literature synthesis.

## Claim, warrant, and boundary

Sections 3–4 hold a nutrition domain and explanation families sufficiently similar to
compare evaluation outcomes across task framings. Preference reversals and a divergence
between preference and error detection undermine the assumption that one evaluation
predicts another. Importantly, the result is not that subjective measures are useless:
Section 6 recommends combining them with performance measures.

The qualitative study (Section 5) unexpectedly resembles the proxy-task pattern. The
authors suggest that verbalization changes cognitive engagement. That explanation is
plausible interpretation, not an isolated causal test of thinking aloud: recruitment,
setting, and sample also differ. A writing skill should preserve this evidential boundary.
The simulated AI and nutrition task also limit extrapolation to deployed expert work.

## Writing moves worth transferring

- Make the unit of the desired claim explicit before criticizing a measurement proxy.
- Align two concerns, two hypotheses, and two discussion threads.
- Use a follow-up study to complicate an explanation, not simply certify it.
- State what remains useful about a criticized method.
- Preserve differences between observed mismatch and its proposed mechanism.

These notes are original, single-analyst interpretations of the linked author PDF.
Section order is observed; recommendations are editorial transfer judgments. No award
claim or paragraph-length norm is inferred from the text.
