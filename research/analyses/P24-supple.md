# P24 — SUPPLE

**Provenance.** Gajos and Weld, *SUPPLE: Automatically Generating User Interfaces*, IUI 2004. Full author-hosted PDF: <https://kgajos.seas.harvard.edu/papers/supple-iui04.pdf>. Single-analyst coding of this eight-page conference version, not later SUPPLE studies. Locators use PDF positions. The selected p.7 paragraph was visually inspected. No award is asserted.

## Architecture and object

The primary object is an optimization formulation and interface-generation algorithm, realized in a system. Its order is **1 Introduction → 2 Interfaces, Devices & Users → 3 Rendering as Optimization → 4 Rendering Algorithm → 5 Evaluation → 6 Related Work → 7 Conclusions and Future Work → 8 Acknowledgments → 9 References**. The explanatory progression is definitions, formal objective, solver, then evidence. Evaluation separates runtime, device adaptation, usage adaptation, interactive application behavior, and a conceptual design comparison.

The abstract (p.1) states a ubiquitous-access goal, identifies shortcomings in previous solutions, introduces optimization, explains the search objective, and lists four contribution objects. It contains no participant count or headline user-performance result. The introduction moves from a future-use scenario to device/user variability, argues manual design cannot scale to all combinations, compares specific preceding approaches, and proposes constrained optimization. “Optimal” is explicitly relative to a cost function and models (pp.1–2); it must not become universally best UI quality when paraphrased.

## Related-work function

Positioning happens twice. The introduction motivates limitations relevant to the objective. The later review (p.7) situates the fully explained system among model-based interface generation, decision-tree selection, and optimization-based layout. This placement lets the review compare specific representations and algorithmic choices rather than previewing unexplained machinery. It recognizes existing optimization research while distinguishing joint widget selection and navigationally complex interfaces. Delaying Related Work does not mean delaying every comparison with prior work.

## Claim and evidence boundaries

Formal definitions and the search algorithm support the claim of optimizing the specified cost under constraints. Runtime comparisons test tractability on examples, including the effects of propagation and variable ordering. Rendered interfaces demonstrate controlled changes in device model or user trace. The conceptual study compares four HCI-trained graduate students' paper-widget designs with the system's choices; one participant's rationale is converted into a trace and produces a corresponding rendering.

The warrant connecting these pieces is coherent behavior under changed model inputs, not demonstrated superiority for real users. Device/interaction costs estimate effort; they do not measure all dimensions of usability. The examples are relatively simple, the representation assumes a tree, and broader adaptation effects remain future work (pp.7–8). The paper explicitly anticipates designer skepticism and calls for fuller user evaluation. Later SUPPLE accessibility results must not be back-projected into this 2004 paper.

## Paragraph micro-analysis

**p.7, §5.5 Conceptual User Study, paragraph opening “One subject came up”.** The visually confirmed paragraph contains six sentences:

- **S1:** Reports a design close to the empty-trace output.
- **S2:** Introduces another participant's grouping preference.
- **S3:** Describes the concrete widget/layout choice that implements it.
- **S4:** Explains the expected usage tradeoff motivating that choice.
- **S5:** Describes the authors' follow-up simulation and recorded trace.
- **S6:** Reports that the altered trace yields a corresponding system rendering.

Relation: **contrasting observations → participant rationale → diagnostic intervention → model-consistent output**. It follows study setup and precedes Related Work. The opening is an empirical case, not a deductive generalization; the argument emerges through the contrast. The last sentence closes a demonstration of representational capacity, not proof that the resulting interface optimizes human performance in practice.

## Transfer and exception

Introduce formal objects in the order readers need to understand the optimization target. Distinguish solver correctness, computational efficiency, output plausibility, and actual user benefit. Use controlled input changes to make system behavior legible. A late related-work section and a case-based empirical paragraph can serve a precise argument; neither must be rewritten into a rigid early-review or topic-sentence formula. Retain the qualifier attached to “optimal” wherever the claim travels.
