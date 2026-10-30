# Artifact, system and interaction-technique writing

Use when the contribution is a new capability, algorithmic/interaction technique,
architecture or implemented design space. The manuscript should make readers
understand **what becomes possible, why existing approaches do not already provide
it, how it works, and what evidence establishes its operating scope**. User studies
are one possible warrant, not a replacement for explaining the invention.

## Establish the capability contract

Write a working sentence: “The artifact enables [action/capability] under [conditions]
through [distinctive mechanism], compared with [nearest alternatives].” Then map
claims to evidence: implementation→feasibility, benchmark→measured technical
performance, user comparison→measured task outcome, deployment→situated use,
design examples→range of expressible possibilities. Do not let one evidence type
silently stand in for all the others.

A software implementation used as an experimental stimulus may not itself be a
research contribution. Conversely, a hardware platform can make a substantive
capability contribution without a controlled user-performance claim. [P80, inFORM](https://doi.org/10.1145/2501988.2502032)
explicitly distinguishes its platform/dynamic-affordance exploration from its
unevaluated user-benefit possibilities.

## Choose an architecture that explains dependencies

A practical sequence is problem and positioning → requirements/design rationale →
interaction concept or walkthrough → mechanism/implementation → evaluation →
limitations and implications. Adapt it to the invention:

- Concept-led hardware: introduce the vocabulary and demonstrate its categories
  before implementation, as in P80.
- Material/fabrication technique: organize around layers, processes and primitives,
  connecting each choice to behavior, as [P81, PneUI](https://doi.org/10.1145/2501988.2502037).
- Infrastructure/resource pipeline: explain requirements, representation, capture,
  and downstream use, as [P83, ERICA](https://doi.org/10.1145/2984511.2984581).
- Optimization: define the objective, representation and constraints before showing
  results; optimality is relative to that model, as [P24, SUPPLE](https://doi.org/10.1145/964442.964461).

Give figures a clear job: interaction sequence, architecture, mechanism, parameter
space, result or failure boundary. Reference the relevant figure where readers
need it. A teaser illustrates the contribution but is not evidence of effectiveness.

## Opening and related work

A capability-led abstract can name the problem, new capability, mechanism,
implementation scope and decisive evidence. Replace “novel framework” with what
is actually different. In the introduction, move from a consequential limitation
to the enabling idea, then preview evidence and contributions. Formal RQs may be
unnecessary when engineering questions are precise elsewhere.

Compare related work on dimensions that matter to the capability: input assumptions,
instrumentation, interaction semantics, operating environment, construction effort,
latency, precision or extensibility. Credit borrowed components. A matrix helps only
when its cells are verified and the dimensions actually explain the gap. Avoid
selecting dimensions merely to make every predecessor look inferior.

Late related work can work when the new mechanism must be understood first; provide
enough early positioning to make the contribution assessable. [P29, Prefab](https://doi.org/10.1145/1753326.1753554)
is a useful contrast to a mandatory early literature block. Never delay credit in
order to imply that borrowed ideas are new.

## Evaluation as an argument

For each claimed property, identify the comparison, workload, operating conditions,
measure and remaining uncertainty. Separate representative cases from stress tests,
ablations from baseline comparisons, personalized from held-out-user models, and
actual end-to-end operation from substituted components. [P79, TapSense](https://doi.org/10.1145/2047196.2047279)
explicitly explains why pooled classification and held-out-user performance answer
different questions. [P22, WirePrint](https://doi.org/10.1145/2642918.2647359)
uses an intermediate comparison to separate mechanisms behind an advantage.

Separate favorable-case selection from representative sampling. [P92, Comic
Captioning](https://doi.org/10.1145/3640543.3645154) selects the three highest-accuracy
strips for its main study; this examines potential under favorable conditions,
not average deployment performance.

Report failures where they explain design constraints. If a demo depends on manual
steps, state them near the workflow. A successful task under researcher operation
is not independent participant usability. Informal enthusiasm does not establish
learnability or adoption. State what the evaluations enable readers to conclude,
then reserve untested applications for prospects.

## Paragraph pattern and original illustration

For learned sensing techniques, make **training population, training environment,
test split, metric and prototype hardware** recoverable where the result is first
reported in detail. In compressed claims, retain conditions that change the conclusion.
[P120, EarHover](https://doi.org/10.1145/3654777.3676367) (author manuscript, implementation §4 p.5; evaluations and discussion §§5–7 pp.6–11) illustrates why:
user-independent detection and user-specific classification have different
generalization boundaries, and environment-specific training changes the result.
Its prototype uses added recording hardware; compatibility with ordinary hearables
remains prospective, not demonstrated for unmodified devices. Do not compress those distinctions into
“works on commodity devices” or one unqualified recognition percentage.

Its discussion (§7, p.11) offers one possible paragraph move: **error type → interaction
consequence → relative cost → design priority → unresolved evaluation**. A false
activation and a missed gesture need different remedies. Ground those consequences
in the manuscript; possible harms or benefits are not automatically measured
outcomes. As a general check, when a confusion matrix motivates pruning a gesture
set, identify that selection step and whether the revised set received fresh
evaluation. P120 reports a post-hoc five-gesture subset in §7.2; distinguish that
reanalysis from a newly collected validation.

A useful engineering paragraph is **requirement → choice → mechanism → trade-off
→ scope or next component**. P81's portable actuation discussion connects an
implemented alternative to speed/noise costs and a prospective mitigation. [P82,
Zooids](https://doi.org/10.1145/2984511.2984547) uses a contrasting-case paragraph
to explain why computationally interchangeable elements can have stable interaction
identities. The principle is earned through examples, not just asserted first.

**Hypothetical revision:** “Our system enables seamless collaboration” becomes
“The prototype synchronizes the displayed annotations across the two connected
clients. The timing test characterizes update delay under the tested network
conditions; collaboration quality remains to be evaluated.” Use actual measured
values if supplied. This distinguishes a technical capability from a social effect.

## Execute

Outline claims and evidence first; draft the walkthrough and mechanism in the order
readers need; write evaluation results from verified outputs; use discussion to
explain trade-offs and transferable capability. Revise introduction/abstract against
that evidence. Compress repeated application descriptions before removing operating
conditions or construction detail needed to understand the contribution. In `.tex`,
preserve figure/label relationships and check moved references. Ask whether each
benefit is implemented, measured, inferred or merely envisioned.

## Creative authoring and accessibility conversion

For creative tools, distinguish **expressible capability, authoring activity, live
performance and creative outcomes**. [P133, SoundToons](https://doi.org/10.1145/3581641.3584047)
(author draft, workflow pp.5–10, live study pp.14–18, design discussion pp.18–20)
shows why a performance-input comparison does not automatically establish an
advantage over programming or keyframing. Author examples can demonstrate
possibilities; a creativity claim needs appropriate evidence about the particular
creative process, experience or output. Do not prescribe one universal scale.
When study details are in an unavailable supplement, mark the access limit rather
than state that no study occurred.

Its paragraph after Equation 3 (p.12) connects **objective → interpretation →
smoothing choice → solver → rendered update**. Keep properties directly optimized
separate from those encouraged by preprocessing or interaction design. Its
sound–motion paragraph (§7.1, p.20) uses **condition → failed apparent match →
mechanism → contrasting case** to produce useful design knowledge. A failure can
refine the capability contract without becoming a generic limitations list.

For accessibility authoring, identify **creator, recipient and produced artifact**.
[P134, Chart4Blind](https://doi.org/10.1145/3640543.3645175) (arXiv v2, formative
requirements pp.5–6, novice evaluation pp.11–14, recipient feedback pp.14–15)
separates these perspectives. Creator usability, converted-data correctness,
guideline-informed rendering and recipient comprehension need distinct warrants.
Retain training, manual calibration and correction work when interpreting time.
An informal expert estimate is contextual evidence, not a controlled baseline.

Use **reported output problem → possible cause → implemented response → remaining
check** when writing iterations, keeping uncertainty where the cause is unresolved.
Do not describe a revision as validated unless its outcome was checked. These
checks belong in the working claim ledger; final prose should foreground what the
artifact contributes and include only qualifications that change its interpretation.
