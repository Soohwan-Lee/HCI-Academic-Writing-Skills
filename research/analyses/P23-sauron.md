# P23 — Sauron

**Provenance.** Savage, Chang, and Hartmann, *Sauron: Embedded Single-Camera Sensing of Printed Physical User Interfaces*, UIST 2013, DOI 10.1145/2501988.2501992. Full author-hosted conference PDF: <https://valkyriesavage.com/papers/sauron.pdf>. Single-analyst coding of this ten-page version, distinct from the earlier Berkeley technical report. PDF page numbers are one-based; p.8 micro passage visually inspected. Award not verified.

## Object and architecture

The primary object is a fabrication/sensing design tool combining camera-based input with geometry modification. Its main sequence is **Introduction → Related Work → Designing with Sauron → Implementation → Evaluation → Limitations → Future Work → Conclusion**, followed by acknowledgments/references. Evaluation has three strands: designing with the approach, suitability of existing models, and fabricated examples. A running game-controller workflow precedes implementation, making the system's abstractions intelligible before the algorithms appear.

The abstract (p.1) moves from a fabrication capability to passive-prototype limitations, states the design goal, presents the sensing approach, explains an occlusion problem and algorithmic answer, then previews evaluation forms and a qualified expressivity claim. This is a nested problem–solution sequence inside the abstract. The introduction similarly moves from physical interaction's value to assembly burdens, proposes a tool, explains its visibility mechanism, and explicitly lists assumptions and limitations before the evidence preview and contribution list (pp.1–2). Restrictions are part of the contribution's definition from the outset.

## Positioning

Related Work (pp.2–3) organizes electronic prototyping tools, computer vision, and CAD/digital fabrication. The contrast is about integration labor, environmental instrumentation, and design-time support. It identifies the closest camera-in-mockup predecessor and explains the additional analysis/modification capability. Printed Optics is treated as an inspirational design-space precedent that lacks the same tool support; Midas is complementary because it concerns a different sensing mechanism. These distinctions offer more precise positioning than declaring previous work generally inadequate.

## Evidence and boundaries

The claim is feasible, expressive construction with single-camera sensing. Algorithms and examples substantiate mechanics; three experienced CAD users expose design implications; analysis of ten pre-existing models probes applicability beyond deliberately favorable demonstrations. The latter is a geometry analysis with estimated shells and candidate camera placements, not a successful fabrication test of all ten objects.

Crucially, the three participants did not run the plug-in during modeling because of time constraints (p.7). The authors subsequently processed their designs and fabricated one. Therefore the study supports reasoning about designing under sensing constraints, not a validated claim that users independently mastered the whole software pipeline. Prototype reports retain oscillation, calibration, and tracking problems. The system remains tethered, requires registration and some manual assembly, and cannot handle arbitrary chained modifications. The belief that assembly is faster than wiring is not a timed comparative result. These distinctions should accompany any summary of ease, speed, or generality.

## Paragraph micro-analysis

**p.8, Evaluation / Modeling with Sauron, opening “One user wished”.** Visually one paragraph with three sentences:

- **S1:** Reports a participant's desire for iterative visibility checking.
- **S2:** Explains the current full-pass delay and its API-related cause.
- **S3:** Connects that feedback to a newly implemented lightweight checking feature, specifying what it omits.

Relation: **observed need → technical reason → responsive design change**. Entry follows accounts of differing camera-placement strategies; exit describes component customization and documentation needs. The paragraph is neither merely a testimonial nor a feature list: the intervening mechanism makes the redesign accountable. It also reveals chronology, so the later feature should not be retroactively counted as evaluated in the preceding sessions.

## Transfer and exception

Use a workflow to connect representations, algorithms, fabrication, and application events. Match each evaluation strand to the uncertainty it addresses. Include negative model cases to define the design space. Place assumptions early when they delimit what the system can plausibly do. Avoid a generic “user study validates system” conclusion: tool use, conceptual design, applicability analysis, and author-built artifacts offer different evidence. The paper's local observation-to-redesign paragraph is a useful alternative to forcing every paragraph into a universal claim–evidence–implication formula.
