# S03 — Formative-first system with creator and recipient evaluations

Source: [P134 Chart4Blind](../analyses/P134-chart4blind.md), IUI 2024, arXiv v2.
Re-read hierarchy and mapped passages 2026-10-31. Source main text and selected
renders were previously reviewed; heading descriptions below are normalized.
This is a formative-first example from IUI, not evidence that this form belongs
exclusively to UIST or that every system paper requires interviews.

## 1. Actual nested architecture

| Section | Subsection sequence | What it establishes |
|---|---|---|
| 1 Introduction, pp.2–3 | Three prose paragraphs and contributions | Conversion problem, proposed scope and evidence preview |
| 2 Related work, pp.3–4 | accessible representations → image/vector conversion → user experience | Output possibilities, technical lineage, workflow gap |
| 3 Need-finding, pp.4–7 | participants → procedure → findings → principles | Which work is difficult and how the authors translate it into design commitments |
| 3.3 Findings, pp.6–7 | streamlined process → intelligent features → accessible output | Workflow, operation and output requirements at different scales |
| 3.4 Principles, p.7 | Progress; consistent steps; input; selection assistance; exports | Five design commitments, not another set of empirical themes |
| 4 System, pp.7–11 | extraction (segmentation, OCR) → rendering → interface (selection, tutorials/guidelines) | Pipeline internals and interaction that enact the commitments |
| 5 Usability study, pp.11–14 | participants → study design → procedure → results/discussion | Sighted novice authoring experience |
| 5.4 Results/discussion | task performance → interaction patterns → feedback | From completion behavior to its distribution across the interface and reported experience |
| 6 Output-accessibility exploration, pp.14–15 | Study setup and recipient feedback without numbered subsections | A different user perspective on produced outputs |
| 7 Limitations/future work, pp.15–16 | Constraints and prospective extensions | Operating boundaries and further questions |
| 8 Conclusion, p.16 | Contribution recap | Reconnect workflow and studied use |

The formative section carries its own participants, procedure and findings. The
later authoring study has another method/results sequence. Section 6 introduces
another perspective. Flattening all three into a single Methods and Results pair
would hide which study generated goals and which examined the built artifact.

The system section is organized by modules then interaction, whereas S01 is
organized first by user-visible modes and later by hardware/electronics/firmware.
These are different explanatory dependencies, not different names for the same
fixed system template.

## 2. Complete paragraph map of §3.3, pp.6–7

The opening sentence introduces findings and requirements. Three subsections then
perform a discovery-to-design translation:

| Unit | Paragraph role | Handoff |
|---|---|---|
| Streamlined process ¶1 | Compare existing tools and establish manual work/time burden | Creates a need to identify what can be unified |
| Streamlined process ¶2 | Find shared steps, explain novice-assistance and parallel-work obstacles, formulate workflow/parallelization requirements | Converts the observed workflow into design scope |
| Intelligent features, sole ¶ | Identify costly operations, provide participant-specific examples, select OCR/segmentation and semi-automation | Narrows from workflow to operations the implementation must support |
| Accessible output ¶1 | Credit SVG's appeal, then distinguish missing data semantics and further accessible-format processing | Explains why simply exporting a vector image is insufficient |
| Accessible output ¶2, p.7 | State the combined output gap, name CSV/SVG requirement, connect it to assistive use | Closes the needs sequence at the output boundary |

§3.4 is an orientation plus five bullets, not five body paragraphs. Its principles
are a normative/design translation from the findings. Preserve that role: the
interviews did not empirically prove every selected technical solution or feature.
The source's participant/tool attribution and broad novelty language have issues
recorded in P134; do not carry those forward as unquestioned facts.

## 3. Transition into the system: two opening paragraphs, p.7

The first paragraph states the system's purpose, ties it to the principles and
names two modules. The second walks through upload, extraction, calibration,
rendering, session handling and export, then announces module detail. The reader
gets an end-to-end dependency before the component subsections.

This changes the question from “what should be addressed?” to “how does the user
move through the response?” An agent drafting from this pattern should attach
concrete goals to features, while avoiding repetition of every formative finding.

## 4. Sentence maps

**§3.3.2 sole paragraph, p.6, six sentences:** costly text/line operations → tick
example → complex-line example → parameter-tuning example → technical requirements
chosen from those insights → semi-automatic scope decision. Each example elaborates
an operation, and the last two sentences change from participant evidence to author
design action. Preserve the change of agency. In a draft, explain why the selected
mechanism fits rather than imply the participants prescribed that mechanism.

**§3.3.3 second paragraph, p.7, three sentences:** combined capability gap →
requirement for two representations given varied needs → support from assistive
technology compatibility. This is gap → design response → reason for the response.
The opening novelty claim needs a verified comparison; the structural pattern does
not license copying its breadth into another manuscript.

## 5. Conditional transfer and contrasting alternatives

Use a formative-first spine when discovering the problem and selecting its design
scope are essential parts of the argument. Give formative findings enough room to
explain requirements, but distinguish findings from chosen principles. Group them
by consequential work, not interview-question order unless that order is analytical.

A concept-first artifact can instead introduce the interaction and later explain
its origins (S01). A reflective design inquiry can repeatedly pair emergence and
interpretation (S02). If the formative work produces a substantial sociotechnical
account beyond requirements, give that account its own argumentative treatment;
forcing every theme into a feature can erase its contribution.

For two-sided systems, separate authoring/use and consequences for recipients when
they require different participants or evidence. Do not let a later evaluation
retroactively supply missing formative data or let a good usability score substitute
for output interpretation. These are structural decisions as well as claim checks.
