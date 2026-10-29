# Hybrid contribution and evidence routes

Use this module when a manuscript combines claims, methods, or outputs that a single route does not adequately explain. First distinguish **multiple methods supporting one claim** from **multiple independently substantive contributions**. An interface used as experimental material, a workshop creating research access, or a publicly released codebook is not automatically a second contribution. Start with [quantitative empirical](empirical-quantitative.md) or [qualitative empirical](empirical-qualitative.md) when one clearly dominates.

## Negotiate the contribution contract

Write one row per proposed contribution: knowledge/output → intended reader use → evidence → validation boundary → section where the inference is made. Test independence: if the other output were removed, would this still offer a distinct, evidenced advance? Retain secondary contributions only when the answer is substantive; otherwise describe them as method, setting, instrument, or support.

[P57, User-Defined Gestures](https://doi.org/10.1145/1518701.1518866) offers both empirical characterization and a constructed gesture vocabulary. The paper explains how observations become the vocabulary, but independent guessability and recognizer testing remain future work. Elicitation agreement must not become a claim of demonstrated usability. By contrast, the experimental interfaces in [P03, To Trust or to Think](https://doi.org/10.1145/3449287) support the behavioral comparison; implementation alone does not establish an artifact contribution.

## Choose an integration architecture

For an inference chain, give each study an output and unresolved issue that motivates the next. For complementary evidence, organize around common questions, with distinct method accounts and an explicit synthesis. For genuinely distinct outputs, introduce a shared problem, develop each contribution with its own warrant, and explain their relationship in discussion. Avoid two disconnected miniature papers joined only by a generic introduction.

Use a working integration table: question → quantitative observation → qualitative interpretation → convergence/disagreement → justified combined inference. Qualitative accounts can illuminate what a rating meant without proving its cause. Quantitative prevalence within a sample can locate a theme without invalidating rare, consequential experiences. [P60, Explaining Models](https://doi.org/10.1145/3301275.3302310) separates the two results strands and combines them in discussion. [P04, Proxy Tasks](https://doi.org/10.1145/3377325.3377498) uses a follow-up that complicates the proposed explanation; integration need not manufacture agreement.

## Resolve common boundary cases

**Making and design knowledge.** Ask what is new: a functioning capability, or a way of understanding and conducting design? [P39, Woodshop](https://doi.org/10.1145/3173574.3174159) derives lessons and design orientations from apprenticeship-led ethnography. Building houses is part of its warrant, not evidence of a new interactive artifact. [P40, DIY Empowerment](https://doi.org/10.1145/3064663.3064674) uses workshops to investigate experience; the workshop setting is not a validated general curriculum. Explain the transition from episode to interpretation to proposed design orientation.

**Empirical account and resource.** Separate the instrument entering a study from the resource revised through it. [P06, Questioning the AI](https://doi.org/10.1145/3313831.3376590) uses a question bank to support practitioner inquiry and develops a reusable output. State what its construction establishes and what subsequent effectiveness evaluation would still need to show.

**Review and documentary analysis.** Papers can be evidence objects rather than sources whose findings are synthesized. [P16, Dataset Politics](https://doi.org/10.1145/3476058) examines documentation as disciplinary practice. [P41, Design in the HCI Classroom](https://doi.org/10.1145/3322276.3322381) combines textbook analysis and instructor survey to support an agenda. Neither should be relabeled a systematic review without a corresponding retrieval, eligibility and synthesis design. Conversely, a review does not become ethnography because its interpretation concerns social values.

## Draft and revise the joint argument

In the abstract, name the primary knowledge claim, the complementary evidence and any independently usable output. In the introduction, explain why one evidence source is insufficient for the intended question. Organize related work around the distinct intellectual needs, then connect them; do not repeat a separate generic gap for every method.

Within a transition paragraph, use **established result → unresolved issue → next inquiry's purpose → evidence limit**. In synthesis, use **convergence or discrepancy → interpretation → alternative account → bounded consequence**. These are editable role sequences, not required sentence counts.

**Original hypothetical example:** before, “The survey and interviews validate our tool.” After, “The survey characterizes reported adoption, while interviews examine how participants describe incorporating the tool into existing work. Together they support an account of use in this setting; they do not establish improved performance.” This illustration supplies no actual study finding.

For existing ACM `.tex`, preserve distinct samples, study timelines, measures, labels and citation keys while improving the connections. Outline contribution rows first; draft each evidence chain; revise the synthesis against both; compress duplicate motivation and repeated methods without deleting integration. Final checks: Are different populations being silently pooled? Is a proposed resource treated as evaluated? Does the combined inference exceed either design? Are disagreements retained? Can readers identify what each method adds? Selected source architectures illustrate possibilities, not award-proven templates or universal length norms.
