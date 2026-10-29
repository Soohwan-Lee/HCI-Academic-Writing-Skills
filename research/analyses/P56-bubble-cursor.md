# P56 — The Bubble Cursor

Grossman and Balakrishnan, CHI 2005, University of Toronto.
[Institution-hosted PDF](https://www.dgp.toronto.edu/papers/tgrossman_CHI2005.pdf).
Full text read; PDF p. 6 (printed p. 286) rendered for paragraph boundaries.
Award unverified. Historical interaction-technique exemplar, not a contemporary
statistical-method prescription.

## Contribution and architecture
The primary contribution is a target-acquisition technique. Controlled experiments
and modeling support its performance claims; they are not automatically a second,
independent empirical contribution. The technique increases effective target
width through an adaptive activation region while preserving target appearance.
The paper separates that mechanism from observed selection performance.

Order: Introduction → Related Work → Bubble Cursor Design and Implementation →
Experiment 1 → Experiment 2 → Discussion → Future Work. Each experiment reports
its own rationale, apparatus, participants, procedure, design and results. The
second study does not merely add participants: it tests a more complex two-
dimensional setting after the first isolates fundamental modeling questions.
There is no separately titled Conclusion. Discussion summarizes the established
capability and then examines modeling, design simplifications and deployment.

The abstract starts with the technique, explains the distinguishing mechanism,
states two experiments and their task conditions, and previews comparative and
model-fit results. The introduction motivates pointing, identifies degradation
of earlier techniques under dense layouts, introduces the adaptive alternative,
and gives a roadmap. No formal RQ is necessary for a clear evaluative argument.
The initial dense-layout claim must be read together with the actual tested
conditions; a skill should not preserve the paper's broadest generalizations
without also carrying its later qualifications.

## Related work and evaluation logic
Related work begins with the predictive model, then groups techniques by whether
they decrease movement amplitude, increase effective width, or do both. This is
a mechanism-based synthesis. Each branch explains both the prior benefit and a
failure condition relevant to dense targets. The closest area-cursor predecessor
is credited as inspiration. Design then addresses two explicit shortcomings:
shape-dependent capture and the trade-off between a fixed region being too large
or too small. The gap therefore constrains the implementation rather than serving
as a ceremonial sentence at the end of the literature section.

Experiment 1 asks separately whether a model predicts performance and whether
users exploit the enlarged effective width. Good model fit alone would not show
a useful performance advantage. Experiment 2 varies surrounding space and
intermediate-target density, reports both speed and error, and explains deviations
from a comparison technique's earlier results. Discussion examines an alternative
time definition to check that counting until successful selection did not create
the main pattern. It also acknowledges layout simplifications and tunable baseline
parameters. Application proposals and 3D extensions remain future work.

## Micro-analysis A: make a second experiment necessary
PDF p. 6, Experiment 2 opening, locator “In experiment 1”. Four sentences, visually
checked. S1 states what the first study established. S2 explains why its simplified
task suited those initial questions. S3 identifies the remaining transfer limit.
S4 introduces the new task conditions. Flow: **prior result → design rationale →
boundary → next inquiry**. The previous section finishes error reporting; the
following paragraph spells out the boundary conditions and comparator choice.
The paragraph creates continuity without pretending the earlier study was flawed.

## Micro-analysis B: operationalize an apparently contradictory outcome
Same page, Error Rate opening, locator “Recall that the experiment design”. Three
sentences. S1 recalls the requirement to succeed before advancing. S2 draws its
consequence: every completed trial ultimately succeeds. S3 distinguishes first-
click failures as the operational error measure. Flow: **procedure → apparent
measurement problem → operational resolution**. It follows movement-time results
and precedes the actual error analysis. The useful lesson is to resolve a likely
reader misunderstanding before presenting a number, not to prescribe this exact
error definition for every pointing study.

## Transfer and limits
Organize prior work by mechanisms that predict the proposed intervention's
strengths and limits. Keep mathematical capability, fitted behavior, measured
benefit and deployment feasibility distinct. Give each study a different inferential
job. Avoid inheriting historical claims that tested parameter variation establishes
performance in every real interface. A nonexperimental design inquiry or a resource
paper needs different warrants and should not adopt this architecture wholesale.
