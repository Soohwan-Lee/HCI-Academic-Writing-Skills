# P87 — FrameKit: A Tool for Authoring Adaptive User Interfaces Using Keyframes

Single-analyst coding of the author-hosted 15-page IUI 2024 proceedings PDF. All substantive sections and technical appendices were read; two complete paragraph boundaries were verified on rendered pages. Locators use PDF pages. The knowledge object is an authoring workflow and computational technique realized in a tool, supported by demonstrations and a preliminary developer study.

## Architecture and opening logic

The sequence is Abstract → Introduction → Related Work → FrameKit: An AUI Authoring Tool → Computational Approach for UI Adaptation → System Implementation → Example Applications → Evaluation → Discussion → Conclusion → Acknowledgments → References → Appendix A: Participant-Authored Examples → Appendix B: Heuristics for Optimizing Edit Sequences. The interface and walkthrough precede the algorithm, so readers understand the interaction that the technical mechanism must support.

The abstract (pp. 1–2) moves from adaptive interfaces’ utility to authoring complexity, a generalized interpolation approach, the tool’s control–effort balance, varied demonstrations, and a ten-developer evaluation. Introduction (p. 2) builds a tradeoff: manually authoring variants is expensive; abstract objectives reduce work but distance authors from concrete designs. Domain-specific toolkits add a second constraint. The keyframe metaphor then makes the proposed workflow tangible before computational detail, evidence summary, and three contributions. The contribution list names approach, tool, and examples; it does not inflate the evaluation into an independent contribution by default.

Related work (pp. 2–3) separates adaptive interfaces, computational design tools, and programming by example. Each section identifies a different dependency: the adaptation problem, generation/control strategies, and example-driven specification with correction. Comparisons concern what authors specify and control. The closest keyframe precedent is acknowledged, then distinguished through structural changes, modular behavior, and multidimensional context. This supplies an argument for the new combination rather than claiming keyframes themselves are unprecedented.

## Evidence, warrants, and qualifications

The example suite tests expressive range across responsive design, ability-based adaptation, and spatial context. It is distinct from the user study, where ten front-end developers recreate simplified responsive and ability-based examples after a tutorial. Successful recreation means reaching the supplied screenshot states through parameter settings. This warrants a bounded feasibility and learnability claim, not faster production work than alternative tools. No comparative authoring baseline was tested.

Four participants used blending, whereas nine nested widgets; success with the tool therefore cannot be equated with widespread use or validation of its central generation feature. Participants’ perceived usefulness and workflow expectations are evidence of perceptions, not observed long-term adoption. The AR example uses simulated sensor values. The ability-based example manually encodes designs rather than reproducing SUPPLE’s optimization or validating accessibility outcomes. Limitations separate tree representation, generation, and study scope. Multidimensional generation is demonstrated but the study uses one-dimensional contexts; instability beyond three parameters also bounds generality.

## Two complete paragraph micro-analyses

**§6.2, p. 7, final paragraph, opening “Our re-implementation differs from”.** S1 flags a functional difference from the reference system. S2 contrasts automatic generation from abstract specifications with manual keyframes informed by user groups. S3 acknowledges the generative-control tradeoff and proposes complementary uses in refinement or prototyping. Relation: caveat → operational distinction → bounded opportunity. It follows the construction of the ability-based example and ends before the AR case. Putting the qualification beside the demonstration prevents a visually similar reproduction from implying equivalent capability.

**§8.2, p. 11, final paragraph, opening “Overall, our user evaluation”.** S1 states the limited empirical support for the context-based model and ties it to task success and participants’ familiar-software analogies. S2 retains the authoring-effort/control tradeoff. S3 frames the contribution as expanding available choices so authors can select an appropriate tradeoff. Relation: evidence-bounded synthesis → qualification → pluralistic implication. It follows comparison with rule-, task-, and objective-based models, then leads into explicit limitations. Its ending offers additional design options, not a claim that one model should replace every alternative.

## Transferable moves

Introduce a workflow through concrete interaction before unpacking its algorithm. Separate breadth demonstrations from novice-use evidence. Define task success precisely and disclose when participants bypass a feature. Keep a reference implementation’s capabilities distinct from a recreated appearance. Let discussion identify a useful alternative within a tradeoff space; a systems paper need not claim universal superiority or force a hypothesis-testing introduction to establish its contribution.
