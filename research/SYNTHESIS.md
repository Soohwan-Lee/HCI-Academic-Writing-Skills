# From paper observations to writing decisions

This original synthesis draws on **112 purposive full-text analytical notes**.
It is a teaching corpus, not a systematic review, a study of acceptance predictors,
or a claim that famous labs share an optimal style. [Coverage](COVERAGE-AUDIT.md)
and [source records](CORPUS.md) make selection and version limitations explicit.
The P-IDs below link through the corpus. Rules are editorial interpretations of
named examples; only the separately documented length subset is measured.

## The contribution determines what must be warranted

| Contribution | Useful pattern and examples | Boundary or contrasting case |
|---|---|---|
| Quantitative finding | Align construct, contrast, unit and uncertainty (P03, P54, P64, P103) | P101/P103 group outcomes cannot become individual-level benefit; P105 conditional findings resist a global winner |
| Qualitative understanding | Link situated accounts to analytical claims and interpretations (P30, P33, P98–100) | P106 probes generate accounts, not an intervention-efficacy estimate; P99 context cannot be erased for generality |
| Artifact/capability | Make capability, enabling mechanism and evaluation questions distinct (P01, P19, P26, P80–82) | Application demonstrations do not establish situated user value; P56's measured comparison supports an interaction technique |
| Design knowledge | Trace making, material encounters and reflection into an insight (P05, P42–45, P102) | Neither a prototype nor the absence of an experiment defines RtD; P102 embodied experience resists generic effectiveness framing |
| Conceptual argument | Expose the premise, distinction, explanatory consequence and limit (P07, P48–50, P68–70, P75–76) | P09 and P46 integrate literature into argument; a standalone related-work section is not mandatory |
| Method | Explain the inference or practice improved, operational steps and evidential scope (P08, P12–13, P58, P71–73, P77) | Teaching/use cases and statistical validation warrant different claims; a checklist does not validate itself |
| Resource | Establish provenance, construction, scope, reuse and validation (P14, P28, P107–109) | P107 is task–resource–model hybrid; P108 is an NLP supplement; P109 is a resource/method pictorial |
| Review/synthesis | Make selection, analytical unit and synthesis traceable (P11, P51–52, P61–62, P65–67, P78) | Critical/conceptual synthesis and meta-analysis have different commitments; document counts are not study counts |

These are eight navigational routes, with justified hybrids. Venue and method are
separate attributes. CHI subcommittees help locate audiences; they cannot substitute
for deciding what a particular paper contributes.

## Openings answer dependent reader questions

An introduction often establishes context and stakes, explains a problem, positions
prior responses, identifies a gap or tension, and introduces a warranted response.
The order and amount depend on what the reader must know first. P03 moves from
expectations and failure to explanation and intervention; P04 diagnoses a mismatch
between intended knowledge and measurement. P07 tests prevailing explanations;
P09 states a methodological position early. P80 motivates a capability before
showing its mechanisms. P102 makes the project's origin part of its interpretive
account; P109 provides alternative visual reading paths.

Smit Desai's [six-part introduction advice](https://thesmitdesai5.medium.com/how-to-write-an-hci-introduction-a-six-part-recipe-0a4972dd05b5)
is practitioner advice, not an empirically established mandatory sequence. The
skill uses reader questions, not copied prose or a required eight-paragraph recipe.
An explicit RQ is useful when it sharpens the inquiry; an artifact or conceptual
paper need not invent an experimental RQ merely to match a template. Abstracts
must reconcile the actual claim, approach, evidence and contribution. Before data
exist, future/planned wording and draft result slots preserve that contract.

## Related work makes a distinction the paper needs

P01 compares mechanisms against a missing capability; P04 compares evaluation
practices against intended inference; P06 links XAI traditions and design practice.
P98 positions access as collaborative work; P99 makes social context consequential.
P107 separates summarization, screen understanding and GUI datasets so each strand
supplies a different prerequisite. P109 distributes prior work across conceptual
and visual landscapes. These are examples of synthesis by explanatory role, not
proof that every paper needs three themed subsections.

Choose comparison axes that expose what remains unresolved. A gap may be conflicting
findings, a neglected standpoint, a faulty construct, a reuse limitation or an
unexplained mechanism. Do not manufacture novelty with “no prior work” or treat all
precedents as deficient. In a review paper, the literature may itself be the data;
a background section should not duplicate the actual synthesis.

## Paragraphs carry local inferences; sentences supply their dependencies

A topic sentence identifies a subject; a claim sentence specifies an inference.
They may coincide. P07 builds its central inference after paired counterarguments;
P04 starts with a mechanism and derives a testable consequence. P26–29 explain
capabilities by connecting inputs, mechanisms and consequences. P33 and P98 link
accounts to interpretation without turning a quotation into self-evident proof.
P42's material encounters support reflective interpretation; P109's caption begins
with a design event, describes a representational failure, and explains conceptual
revision. Its neighboring columns are parallel arguments rather than sequential
prose paragraphs.

For revision, identify each sentence's function: context, claim, evidence, warrant,
qualification or transition. Follow recurring entities and given-to-new information;
make pronouns, causal agents and comparison baselines unambiguous. A paragraph's
ending should leave a reason to read the next one, not repeat a stock mini-conclusion.
Split when the inferential job changes; merge when two fragments jointly make one
claim. Claim-first is useful when the claim is already interpretable, not compulsory.

The sentence-role examples are selected teaching cases, coded by AI analysts and
reviewed during integration. They are not a frequency study of paragraph structures.
Avoid formulaic symmetry because it conceals reasoning, not because it proves AI
origin. The skill offers concrete local repairs rather than an authorship detector.

## Length evidence has a smaller denominator

Seven papers have version-bound extracted-body/section estimates; 32 selected
paragraphs across 14 papers have reproducible length records. Captions, numerals,
heading treatment and normalization vary by disclosed protocol. Ambiguous PDF
sections are aggregated rather than assigned false precision. See
[measurement methods and replay](measurements/README.md).

The skill's route-specific 8,000-word allocations are **editorial planning aids**,
not corpus averages. No optimal paragraph length, venue percentage, lab effect or
prestige advantage has been estimated. Existing manuscript counts and the current
submission rules take priority. Pictorials require visual/page planning.

## From evidence to an authoring assistant

The package separates fast paragraph repair from whole-paper framing, preserves
existing author-owned citations during wording-only edits, and checks changed claim
scope. It supplies routes for negative/null results, reviews, pre-results drafting,
compression and reviewer responses. Its LaTeX helper checks lexical dependencies;
compilation and semantic review remain different tasks. Two real file-edit trials
succeeded, while evidence-poor generative trials retained unsupported details.
The [behavior report](../tests/behavior/SEMANTIC-REPORT.md) records those failures;
the corpus and prompts cannot guarantee factual writing or replace author judgment.

## Contribution taxonomy correction
The original eight navigation routes mixed claim categories with method-oriented
labels. P110's sociotechnical account makes this limitation concrete: a probe and
qualitative analysis are its access/analytic approach, while the contribution is
an account of relations among practice, technology, cultural expectations and
well-being. Its implications are not an evaluated system or necessarily a new
general theory. See [taxonomy review](../docs/CONTRIBUTION-TAXONOMY-REVIEW.md).

## New contrasts: non-design, activist systems and genealogy
P111 builds a normative argument from questions and illustrative cases rather than
an empirical IMRaD sequence. P112 interleaves deployed-system choices with activist
interpretation; maintenance and ambivalent success are part of its contribution.
P113 separates critique from anticipatory reconstruction while explicitly denying
that written order is necessarily research chronology. P115 first makes eras legible
and then crosses them to construct analytical dimensions. Its sources include
research, journalism and legal documents; documentary synthesis does not erase its
primary genealogical claim. These are four contrasting examples, not a new universal
structure. See the source notes for rhetorical limits and version-specific tensions.

## E02: preserve the warrant through sentence-level revision
P116 and P117 show how repeated ratings, task contrasts and discussion mechanisms
can be made fluent while losing their inferential limits. Preserve the measured
construct and comparison through abstract and conclusion; a hedge early in a
paragraph does not qualify every later sentence. P120 makes the analogous systems
problem concrete: personalized classification, held-out-user detection and added
prototype hardware cannot collapse into one deployable-recognition claim.

P118 adds configurations and explanatory relationships rather than an interface
feature list. Triangulated sources can complicate each other; recordings do not
automatically overrule accounts, and reflexive presence is not always a removable
bias. P119 shows an inheritance–difference–transfer argument for extending a
concept. Scenario evidence bounds effects claims without making conceptual value
conditional on a deployment. These five papers supplied ten selected paragraph
analyses, not new paragraph-length distributions.

## E03 — review forms and evidence levels
P121 separates reusable reporting criteria, a manual metaresearch audit and an
assisting tool. P122 combines involvement mapping with a politically situated
reading of scholarly genres. P123 moves from themes to lifecycle relationships.
P126 separates experiences from scholarly perspectives before arguing for a
stakeholder agenda. These are different contributions within literature-based
research; selection procedures alone do not prescribe their section or paragraph
sequence. Interpretive models retain value without being recast as causal tests.
P125 adds an artifact contrast: comparative tasks, repeated sessions and an author
diary support different capabilities and interpretations. None is a universal
validation template. Selected paragraph-role sequences are qualitative examples;
no new length distribution or 8,000-word allocation was estimated in this batch.

## E04: carry the knowledge object through the argument
P128 and P129 demonstrate different conceptual work within the same venue: a
reflective account makes managerial practice legible; an interview-based account
extends a relational lens to platform labor. Neither should be reduced to feature
requirements. Their paragraphs earn concepts through encounters and contrasts,
including productive ambiguity and uneven consequences.

P132 separates resource provenance, characterization and downstream utility.
P133 and P134 separate authoring, performance and recipient evidence. Across these
three artifact/resource cases, a polished abstract can lose the distinctions that
make the detailed evidence interpretable. The writing aid should retain a working
claim ledger and then write readable prose, not expose the whole ledger as caveats.

Paragraph alternatives include equation-to-interaction explanation, a failed match
that earns a design condition, and feedback-to-revision across adjacent paragraphs.
These are source-located examples, not population frequencies or universal recipes.
P128's visual argument also shows why numeric prose budgets cannot describe every
manuscript form. Source versions and inaccessible supplements are recorded in the
individual notes. No numeric section/paragraph sample was expanded in E04.
