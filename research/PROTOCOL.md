# Corpus and analysis protocol v1

## Axes
Record separately: knowledge contribution; research method; rhetorical strategy;
venue/year/track; verified award; author affiliation stated in the paper.
Prestige is a sampling signal, not evidence that a writing device causes success.
CHI subcommittees are topic/reviewer contexts, not mutually exclusive knowledge types.

## Contribution routes (working taxonomy)
- Empirical / quantitative: an estimate, comparison, relationship or prediction.
- Empirical / qualitative: an interpretation of practice, experience or social process.
- Artifact / system: a capability, interaction technique, architecture or toolkit.
- Design / research through design: generative knowledge through situated making,
  reflection, annotated artifacts or design inquiry, not just an evaluated UI.
- Theory / conceptual: constructs, explanatory relations or a reframing.
- Method / resource: a reusable procedure, instrument, dataset or benchmark.
- Synthesis / review: an accountable synthesis of a defined literature corpus.
Hybrids have one primary claim and one or more secondary claims. Quantitative and
qualitative are empirical subroutes; design is an operational writing route that
can overlap artifact/theory, not a claim to supersede published taxonomies.

## Sampling
Initial purposive sample: aim for 10–15 full papers across CHI, CSCW, UIST, DIS,
IUI, with variation in contribution and rhetorical structure. Start with the
user's Zotero interests (human–AI interaction, collaboration, design), then fill
coverage gaps from author/institutional open copies. Record actual coverage;
do not silently call unfilled categories analyzed. Prefer award-verified work
where available; include contrasts. Affiliation is recorded, not ranked.
The corpus intentionally cannot establish field-wide averages or causal effects.

## Provenance
Each paper: ID, title, authors, venue/year, DOI, full-text source/version,
access date, checksum when locally available, contribution labels, award status
and source. `unverified` does not mean `no award`. Author-page award evidence
must be distinguished from official conference evidence.
Local Zotero keys and paths stay in ignored .local; public metadata is sufficient
for reproducibility without publishing the user's library or attachments.

## Coding
Read full text and inspect original page layout for measurements. Code:
1. Abstract: stakes/problem, gap, approach, evidence, finding, implication.
2. Introduction: paragraph-level moves and order; merged/repeated/absent moves.
3. Related work: organizing question, comparison axes, boundary of novelty,
   synthesis-to-study transition, treatment of nearest competing work.
4. Main body: actual top-level section sequence, study/design logic,
   claim–evidence–warrant mapping, limits and discussion moves.
5. Style: paragraph jobs, concrete subjects, calibrated verbs, transitions,
   evidence-bearing detail; never diagnose AI authorship from style.
6. Alternatives: identify when the apparent recipe fails or changes.
Notes are original paraphrases and locators, not copied paper text.

## Measurements
Count English tokens with a documented regex; do not equate this to ACM counts.
Body excludes title/authors, abstract, references, acknowledgments and appendices.
Report separately abstract and section word counts, denominator and extraction
version. For PDF-derived counts, record reading order, ligature/hyphen handling,
caption/table/header exclusions and reviewed section boundaries. Do not report
paragraph distributions from layout blocks as though they were true paragraphs.
Manually reviewed paragraph subsets must state section, n and selection rule.
Small strata get descriptive examples only, never population percentile claims.

## Evidence labels
- Official guidance: normative only for the named venue/year/source.
- Practitioner advice: attributed, optional, not a universal rule.
- Corpus observation: named paper(s), location, extraction/coding limits.
- Editorial heuristic: our adjustable advice, not measured prevalence.
- Untested hypothesis: a proposed pattern awaiting more evidence.

## Review gate
Verify identity, contribution/method distinction, full-text access, award source,
claim locations, extraction quality and permitted redistribution before synthesis.
A single analyst's coding is not inter-rater reliability. A model critique is not
an independent human validation or empirical evaluation of writing effectiveness.
