# P132 — UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset

## Source and review scope
Peitong Duan, Chin-Yi Chen, Gang Li, Björn Hartmann and Yang Li, UIST 2024; [DOI](https://doi.org/10.1145/3654777.3676381). Reviewed 2026-10-30 using the [author-hosted PDF](https://people.eecs.berkeley.edu/~bjoern/papers/duan-uicrit-uist2024.pdf): 17 pages, main text through p.14 and appendices through p.17. Root read both and inspected rendered pp.4, 5, 11, 12 and 13. Claude Opus 5.5 medium provided a text-based critique; root adjudicated it against the source. No award or citation-count claim is made. The associated repository was not independently audited.

## Contribution contract
The primary contribution is a critique resource with spatial annotations and ratings, accompanied by descriptive analysis and a demonstration of its utility for prompting. Treat the dataset, the prompting configuration and the downstream evaluation as related but distinct objects. The paper does not establish that the dataset alone causes every reported improvement.

The sampling chain runs from RICO through CLAY to 1,000 selected screens and 983 complete records. Seven contracted designers supplied annotations; six had at most two years of experience. Each screen had one annotator. The resulting 3,059 critiques include 2,283 human-only, 256 Gemini-only critiques validated by annotators, and 520 overlapping critiques. A resource description should preserve these origins rather than label the entire collection independently human-authored. Annotator coverage, annotation protocol and label reliability answer different questions.

## Architecture and opening
Introduction → related work → dataset construction → dataset analysis → automated critique approach → evaluation → discussion and limitations → conclusion, with additional statistical and protocol details in appendices. The ordering lets the reader inspect what the resource contains before judging its utility.

The introduction's five prose paragraphs establish the value of critique; distinguish model limitations from a lack of suitable data; introduce the resource and its scope; preview utility in two tasks; and identify prospective applications. A contribution list then separates the delivered objects. The abstract similarly moves from value and current promise to a data gap, the resource, analysis, task results and prospective use. Future uses should stay prospective.

Related work has three jobs: situate the resource among interface datasets, distinguish critique from narrower automation tasks, and identify frameworks used to structure evaluative feedback. The dataset lineage explains what can be reused and what is missing. Evaluation frameworks motivate annotation instructions; they do not independently validate every annotation. This is stronger positioning than a list of datasets ordered by publication year.

## Method and evidence dependencies
The annotation procedure combines designer critiques, generated suggestions, validation, bounding boxes and ratings. Instructions specify an expected standard, a current discrepancy and a possible correction. These are useful operational definitions for a resource paper, but their presence should not be rewritten as measured accuracy.

Clustering combines sentence embeddings and K-means with interpretation of the resulting groups. The visualization helps inspect distributions; it does not prove the categories' semantic validity. Root visually confirmed that the five critique-category counts printed on p.5 sum to 3,144 rather than 3,059. Retain this unresolved reporting discrepancy instead of silently repairing it. Near-zero correlations with app ratings and lower within-app variation do not establish independent annotator agreement. The rating correlation reported in Appendix A is on PDF p.15.

The downstream pipeline includes example retrieval, visual prompting and a two-call critique/localization sequence. A localization choice with lower aggregate IoU is justified by the behavior of irregular boxes, showing how a technical decision can balance metrics and interaction requirements. Report the criterion actually used rather than select the largest number retrospectively.

The final comparison uses six interfaces and six expert judges. One judge also took part in prompt tuning; the evaluated interface overlap with tuning and same-app/self-retrieval exclusion are not fully specified. These are dependency questions, not proof of leakage. The partial-credit critique score rises from .31 to .48: an absolute .17 and a relative improvement of about 55%. The comparison bundles examples with visual prompting. Human critiques score .75. Scores per critique do not establish completeness of critique coverage, and preference does not establish that designers subsequently produce better interfaces.

## Micro-analysis 1 — dataset provenance, PDF p.5
The provenance passage moves from the overall critique total to origin-specific subsets and the relationship between human and generated material. Its rhetorical work is to decompose a headline quantity into interpretable components. Repeated references to critiques keep the unit stable while origin labels introduce the new information. A resource-writing assistant should preserve that sequence: total and unit → origin distinctions → overlap rule → implications for reuse. Avoid replacing it with a single impressive count that erases supervision or validation dependencies.

## Micro-analysis 2 — discussion §6.1 opening, PDF p.12
Three sentences move from observed task performance to a proposed explanation involving examples, then toward an implication for automated evaluation. The middle sentence is the inferential hinge. Preserve the distinction between a plausible mechanism and a separately tested mechanism; the final implication should inherit the scope of the actual tasks. The paragraph is useful as result → explanation → significance, provided the explanation is calibrated rather than asserted as an isolated causal finding.

## Transfer to writing assistance
For resource contributions, build a provenance ledger before drafting the contribution statement: source population, selection, annotation unit, annotator roles, generated material, validation, missing records and intended use. Connect construction decisions to downstream affordances. Keep dataset characterization separate from utility demonstrations, and distinguish prompt components, tuning evidence and final evaluation. Preserve practical applications as opportunities when no deployment or design-revision study was performed. Resource quality cannot be inferred from author affiliation, a compelling demonstration, or an aggregate corpus size.
