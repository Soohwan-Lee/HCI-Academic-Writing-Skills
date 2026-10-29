# P55 — Understanding Touch

Holz and Baudisch, CHI 2011. [Author-lab PDF](https://static.siplab.org/papers/chi2011-understanding_touch.pdf).
Full text read; paragraph examples checked on rendered pages 4 and 8. Hasso
Plattner Institute. Award unverified. This analysis concerns argumentation, not
current recommendations for touch hardware or statistical modeling.

## Contribution and architecture
The central object is an explanatory account of how users aim with their fingers.
Interviews, candidate models, controlled comparisons and engineering implications
serve that account; neither an interview dataset nor a new sensor is the principal
claimed contribution. The paper explicitly distinguishes scientific understanding
from engineering improvements. Its quantitative studies are organized as an
inference chain rather than one interchangeable Method–Results block.

Sequence: Introduction → Understanding Touch (proposed explanatory problem and
approach) → Related Work → Step 1 interviews → Step 2 candidate models → Step 3
eliminating models (finger posture, then head parallax) → Step 4 evaluating the
survivors → engineering implications → Conclusions. Each step changes what the
next step can legitimately assume. This is a strong precedent for naming sections
by their inferential job when several studies build on one another.

The abstract moves from the familiar contact-area explanation to a distinction
between random error and systematic offsets, then to an alternative account,
evidence and engineering consequences. The introduction uses the conventional
account as an apparently reasonable baseline, then uses systematic offsets to
expose what it cannot explain. It previews an account based on what people see,
not only what the sensor detects. A visual comparison makes the difference
concrete before the detailed empirical argument.

## Related work and evidence chain
Related work covers sensing and contact-point computation, techniques that aid
selection, and models of pointing. These are different levels of explanation:
a useful interface technique does not itself settle the user's targeting model.
The paper positions prior posture-dependent corrections as motivation for asking
why the offsets occur. The gap is explanatory inadequacy, not a claim that nobody
has improved touch accuracy.

Interviews generate plausible candidate models while acknowledging limits of
introspection. They do not validate unconscious perceptual processes. Subsequent
studies eliminate candidates against measured offsets. A fresh participant sample
and more repetitions in the final study address reuse of selection data and the
separation of systematic offsets from noise. The engineering discussion translates
model errors into possible target-size consequences, keeping that application
separate from the explanatory model comparison. Individual variation and remaining
models prevent a claim that one model describes every person in every posture.

## Micro-analysis 1: purpose with an epistemic boundary
Page 4, Step 1 opening paragraph, locator “The purpose of this study”. Three
sentences. S1 identifies the interview's learning goal. S2 immediately qualifies
introspective access and narrows the output to potentially relevant candidates.
S3 explains why incorrect candidates are acceptable at this stage: later steps
will eliminate them. Flow: **purpose → bounded evidence role → downstream check**.
The preceding material demonstrates unexplained offsets; the following Task and
Procedure explains how the interviews make targeting salient. The paragraph is
deductive, but its main value is an explicit limit on what that method can prove.
It prevents a reader from interpreting every participant explanation as ground
truth about perception.

## Micro-analysis 2: motivate a new study instead of repeating a method
Page 8, Step 4 opening paragraph, same opening locator under a different heading.
Three sentences. S1 states the remaining evaluation task. S2 explains why earlier
data cannot be reused after selecting models with them. S3 adds a measurement
problem: too few trials to distinguish systematic offsets from random noise.
Flow: **new purpose → independence requirement → precision requirement**. The
preceding discussion selects surviving models; the following paragraph increases
repetitions and explains the aggregation. Local cohesion comes from carrying
“remaining models” forward and turning each identified deficiency into a design
choice. A new study earns its place rather than appearing as a second study with
an unrelated question.

## Transfer and exceptions
For a multi-study manuscript, write the output and unresolved uncertainty of each
study, then justify the next design against that uncertainty. Preserve the
exploratory role of interviews and model selection. Separate descriptive fit,
explanation and downstream engineering benefit. This stepwise architecture is
unsuitable when studies are independent replications or when iterative design
knowledge does not depend on eliminating competing predictive models. Do not
force those papers into this sequence merely because they contain several studies.
