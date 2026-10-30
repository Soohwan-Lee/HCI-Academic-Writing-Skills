# Quantitative empirical writing

Use this module when the central contribution is a measured relationship, comparison, distribution, explanatory model, or critique of what an evaluation can establish. Route by the knowledge claim, not by the presence of numbers. An experiment evaluating a novel artifact may primarily support an artifact claim; interviews generating candidate models may belong inside a quantitative explanatory argument. For multiple independently substantive outputs, consult [hybrids](hybrids.md).

The source examples below are selected, version-specific observations. They are neither universal venue conventions nor evidence that an award proves a writing strategy effective.

## Establish the inferential contract

Before changing an existing ACM `.tex` manuscript, locate the actual study design, analysis outputs, figures, hypotheses/questions, and contribution statements. Preserve citation keys, labels, numerical values, and distinctions between planned and exploratory analyses. Draft a working alignment table:

| Question or claim | Evidence needed in this manuscript | Boundary to retain |
| --- | --- | --- |
| Does an intervention change an outcome? | Implemented comparison, assignment/procedure, operational outcome, estimated contrast and uncertainty | Population, task, exposure, comparison and design's causal assumptions |
| How are two characteristics related? | Observational measurement, sampling, adjustment/model assumptions and reported association | Confounding, selection and temporal ordering |
| Which explanatory model accounts for behavior? | Candidate derivation, discriminatory evidence, evaluation and unresolved alternatives | Fit versus explanation; selection versus independent assessment |
| Does an evaluation proxy support the intended inference? | Explicit target construct, proxy and comparable evidence about their relationship | A mismatch does not make every use of the proxy invalid |

Write the contribution at the strongest level supported by that table. If essential evidence is missing, use a visible working placeholder or editorial comment; do not manufacture results to complete the narrative. Discuss analyses the manuscript actually reports. Statistical test selection requires the study's analytical expertise and assumptions; this module does not prescribe a test from a paper genre.

## Choose a section spine

For a focused comparison, a useful starting sequence is motivation/positioning → study rationale and questions → method → results by question → discussion and boundaries → conclusion. Put hypotheses where their rationale is understandable. They need not appear in the introduction: [P03, To Trust or to Think](https://doi.org/10.1145/3449287) develops them in the experiment section after motivating cognitive mechanisms.

For dependent studies, give each study a purpose, evidence output, and unresolved issue that earns the next study. [P55, Understanding Touch](https://doi.org/10.1145/1978942.1979308) proceeds from interviews to candidate models, elimination, and evaluation of survivors. That architecture suits an inference chain. Independent replications may instead share a method section and use parallel study sections followed by a synthesis; do not imply that the second study was designed in response to the first without evidence of that chronology.

Separate construct rationale, stimulus implementation, and participant procedure when combining them obscures dependencies. [P60, Explaining Models](https://doi.org/10.1145/3301275.3302310) uses a study overview, system overview, and methodology before quantitative and qualitative findings. A simple manipulation rarely needs this many headings. Give a consequential subgroup, robustness, or ethical analysis its own section only when it materially changes the argument, as P03's individual-differences audit does.

## Draft the opening and literature argument

An abstract can state the phenomenon or question directly, identify the unresolved explanation or comparison, describe the study sufficiently to identify its warrant, report the central pattern with uncertainty, and state its bounded consequence. Include a null outcome, cost, or trade-off when it changes what readers should conclude. Avoid a positive headline that is repaired only by the final limitations paragraph.

For the introduction, build a sequence of reasons rather than filling mandatory slots: why the phenomenon matters → what current explanations or interventions establish → what remains uncertain → why the chosen comparison can resolve part of it → what was learned → what knowledge is contributed. Use an explicit RQ when it sharpens this sequence. A study can instead center motivated hypotheses or competing explanatory accounts. State the actual comparator; “improves decision making” is incomplete without an outcome, baseline, and setting.

Organize related work around premises needed for the study: competing mechanisms, operational definitions, prior outcome patterns, and evaluation choices. Each cluster should explain a design or inferential decision. [P04, Proxy Tasks](https://doi.org/10.1145/3377325.3377498) distinguishes what proxy and decision tasks require people to do, making the literature a validity argument. [P54, Interrupted Work](https://doi.org/10.1145/1357054.1357072) uses conflicting accounts of interruption context rather than a generic absence-of-research gap. Credit the nearest predecessor and state the specific unresolved comparison.

## Turn results into warranted discussion

Organize results by the question answered, not the order of software output. A useful local sequence is outcome/comparison → reported estimate or pattern and uncertainty → relevant qualification → answer at the supported level. Point to a table or figure for detail without repeating every cell. Keep denominators, analysis units, aggregation and condition names consistent. Separate observed ratings from the latent or normative construct they might imperfectly represent: perceived fairness is not demonstrated institutional fairness.

In discussion, first answer the question using the actual outcome scope. Then relate the pattern to competing explanations, identify what evidence supports the interpretation, and state what remains untested. Proposed mechanisms, personalization, and combined workflows must retain prospective or interpretive wording. P04's think-aloud follow-up complicates its explanation; it does not isolate verbalization as the cause. P03's conditional improvement should not become a claim of improvement across every trial and measure.

For uncertain or null results, report what the analysis can and cannot distinguish. Nonsignificance alone does not establish equivalence or absence. Preserve exploratory model changes and post-task measurement timing. When subgroup evidence is discussed, do not infer a difference between groups solely because one within-group result passes a threshold and another does not. Pair benefits with measured costs; P54's speed and workload pattern is a useful rhetorical example, not a statistical reporting template to inherit unchanged.

## Build paragraph progression

Choose an opening that performs the paragraph's job. Use conclusion-first writing when the result is already established; use a question, contrast, or purpose when readers need the warrant first.

- **Mechanism to prediction:** proposed mechanism → literature-based reason → testable consequence. P04, introduction p. 1, develops a concern about attention in proxy tasks this way. The next paragraph addresses a distinct measurement concern, avoiding repetition.
- **Purpose to next study:** learning goal → current method's evidence limit → later check. P55, Step 1 p. 4, bounds what interviews can establish; Step 4 p. 8 explains why fresh evaluation is needed after selection.
- **Observation to interpretation:** measured pattern → explicit interpretive transition → plausible explanation → observed counterweight → bounded takeaway. P54, discussion p. 4, then follows with alternative explanations and missing measurements.

These are expandable sentence roles, not mandatory sentence counts. Carry a specific unresolved concept from the preceding paragraph into the next; delete generic transitional promises when the content already provides continuity.

### Preserve the comparison while compressing

Before rewriting a results paragraph or abstract, retain four linked elements:
**what varied or was compared → what was measured → what analysis supports the
statement → what remains unresolved when that uncertainty changes the claim**. If the sentence names a psychological construct, check
whether it reports a rating, behavior, inferred process, or directly assessed
construct. Do not silently upgrade one to another.

[P117, Are Explanations Helpful?](https://doi.org/10.1145/3397481.3450650)
(author manuscript, §§2–5; discussion pp.9–10) threads the same three desiderata through literature, RQs, measures and results.
This is a useful alignment strategy. Its two domains, however, do not isolate
expertise as a causal moderator. A task-specific contrast should retain the task
names rather than become a universal novice/expert claim. Its tables also distinguish
untested, unsupported and partially supported criteria; preserve that distinction
when compressing a mixed result into a sentence or table symbol.

[P116, Illusion of Explanatory Depth](https://doi.org/10.1145/3397481.3450644)
(author manuscript, introduction pp.1–2; research questions §3 and study procedure §5) connects
overestimated understanding to the limits of self-reported understanding, then
compares understanding ratings before and after explanatory tasks and feedback. In adapting that structure, keep the sequence and
intervening feedback visible: a post-feedback rating decline is not by itself
an isolated effect of explanation format. Different recruitment and procedures
also constrain comparisons between moderated and unmoderated samples.

For a proposed explanation of results, use **pattern → explicitly tentative account
→ reason or relevant theory → unresolved alternative → bounded implication**.
P117's expertise discussion illustrates this move, while also showing how a firm
phrase later in the paragraph can undo an initial hedge. Read the full paragraph,
abstract and conclusion for changes in certainty; one early “may” does not qualify
every subsequent sentence. These cases illustrate reporting choices, not advice
to inherit their statistical procedures.

## Original hypothetical revision

**Hypothetical scenario, not a source finding:** suppose supplied results show shorter completion time, greater reported workload, and an inconclusive error comparison.

Before: “Our interface significantly improves productivity and validates our design.”

After: “Participants completed the task sooner with the interface, while reporting greater workload. The error comparison remained inconclusive. The results suggest a speed–effort trade-off in this task; whether that trade-off remains acceptable during sustained use requires further study.”

Insert the manuscript's actual estimates, uncertainty and references only after checking its outputs. The revision improves the inference without inventing an effect size or a causal mechanism.

## Execute and review

**Outline:** make the alignment table; assign one evidence job to each section; mark dependencies between studies. **Draft:** write results from verified outputs first, then discussion warrants, then revise introduction and abstract to promise exactly that contribution. **Revise:** trace every abstract/contribution claim to evidence and inspect constructs, comparison scope and epistemic verbs. **Compress:** remove duplicated table narration and broad background before deleting operational definitions, adverse outcomes, or qualifications that change the claim.

Reviewer checks: Is the unit of analysis clear? Can readers distinguish planned tests from exploration? Does the claimed outcome match its measure? Is an observational association being written causally? Is model fit mistaken for explanatory truth? Are null results or costs omitted from the headline? Does each extra study resolve an identified uncertainty? Could a proposed design implication be mistaken for a tested intervention? If the answer exposes a gap in evidence, flag it while completing all supported prose edits.
