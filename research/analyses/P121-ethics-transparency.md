# P121 — Changes in Research Ethics, Openness, and Transparency in Empirical Studies between CHI 2017 and CHI 2022

## Source and review scope
CHI 2023, Salehzadeh Niksirat and colleagues; [DOI](https://doi.org/10.1145/3544548.3580848). Analyzed the 23-page institutional-repository PDF from [HES-SO](https://arodes.hes-so.ch/record/13311/), main text pp.1–20. Opus 5.5 medium supplied a text analysis through subscription authentication; root read the main text and inspected rendered pp.2, 8, 14, 19. Supplementary protocols and raw coding were not independently reanalyzed. Reviewed 2026-10-30. Citation lookup returned HTTP 429; recognition remains unverified.

## Contribution contract and review subtype
This is a methodological audit of published research, with reusable assessment criteria and a secondary screening prototype. It combines operationalization, a two-snapshot empirical comparison and technical feasibility. It is not a meta-analysis or a narrative topic survey. The 45 criteria are an assessment instrument, not an explanatory theory. Presence of a criterion in a paper is not proof of correct execution, ethical adequacy or research quality.

The paper samples 118 CHI 2017 and 127 CHI 2022 papers with empirical contributions. Sampling selects sessions and then papers, replacing nonempirical entries. Papers are the analysis unit: any constituent study can satisfy a criterion. Applicable denominators vary by criterion. Forty-five criteria were defined, but 41 compared; three had only one applicable paper and sketches lacked a defensible comparison denominator. Keep these distinctions in a compressed abstract or results sentence.

## Architecture and opening
Introduction → related work → criteria development and insights → sampling/coding/analysis → four results groups → screening tool design/implementation/evaluation → discussion and limitations → conclusion. Giving criteria their own section makes operationalization independently inspectable before its application. The prototype follows the manually coded findings; the authors explicitly state that automatic screening did not generate those findings.

The introduction establishes empirical research and three values, defines each, introduces tensions among them, distinguishes fragmented/direct and self-report evidence, then promises criteria, snapshots and a tool. Its gap is the combined assessment and comparison, not the invention of studying published papers. The abstract compresses sampling and criteria alongside improvement and tool results, but its assertion of no improvement in remaining criteria loses uncertainty and the distinction between assessed and untested criteria.

## Related-work argument
The three value headings prepare the instrument. Transparency is further divided into methods, results, data and artifacts. Prior audits, surveys and guidelines perform different evidentiary jobs. The qualitative discussion distinguishes disclosure from an ideal of a researcher becoming invisible; this prevents a term shared across traditions from silently imposing one epistemology. Production transparency is set aside because the proposed paper-level audit cannot assess it. This is a reasoned scope boundary, not a claim that it is unimportant.

## Evidence and interpretation
Manual codes and interval estimates support statements about reported/shared practices in the sampled papers. They do not establish why practices changed. Page limits, time since publication, selection and methodological composition complicate comparisons. The paper acknowledges that qualitative criteria emphasize interviews and do not capture all interpretive analysis artifacts.

The screening system evaluates eight criteria using similarity and classification. Threshold selection and evaluation independence are insufficiently clear in the main text to claim held-out generalization. SciScore numbers are imported from another domain/corpus, not a controlled head-to-head baseline. An implemented detector does not demonstrate reduced reviewer workload or better review decisions.

## Micro-analysis 1 — p.2, introduction, transparency paragraph
Six sentences: (1) acknowledge that openness and transparency are often coupled; (2) declare a distinction; (3) define the operational target; (4) state that neither guarantees the other; (5) provide a paywall counterexample; (6) connect the definition to HCI activity. The paragraph earns its definition through a discriminating example. The previous openness paragraph explicitly points forward; the following paragraph complicates both desirable values with practical tensions. This is conceptual continuity across paragraphs, not a generic transition phrase.

## Micro-analysis 2 — p.19, §7.5, second paragraph
Four sentences: (1) recall the assessed domain of desirable practices; (2) distinguish desirable from correct; (3) name correctness checks outside scope, with examples; (4) defend consistent application as a basis for year comparison. The last sentence is the authors' warrant, not proof that all biases cancel. A useful repair retains the distinction while qualifying comparison limits. This paragraph narrows the evaluation target after recommendations have expanded its possible use.

## Cross-section and sentence-level lessons
The same definitions recur in the criteria, figures and discussion, allowing readers to trace a claim. Figure denominators prevent a percentage of applicable papers from becoming a percentage of all studies. Discussion moves from remaining low rates to proposals for submission guidance, review processes and education; these proposals need prospective verbs. The tool section makes the user a decision-maker, not an automatic pass/fail recipient. Its warning about superficial keyword compliance also applies to AI writing assistants: adding an ethics sentence cannot establish the procedure occurred.

## Counterexamples retained after root review
- Several zero-crossing intervals are described as negligible or no change. Preserve inconclusiveness unless equivalence is actually established.
- Similar award proportions do not demonstrate absence of selection bias, and awards are an incomplete proxy for quality.
- A reported ethics–transparency pattern does not isolate vulnerability as its cause; the authors' later causal-sounding language needs restraint.
- Figure 3 visibly labels 139 CHI 2022 sessions but 146 screened sessions. This source inconsistency remains unresolved; do not silently correct it.
- The proposed power-analysis sample and selection procedures require supplementary verification before reuse. Claude's suggested numerical recalculation was not accepted as a verified result.
- The paper's 2023 access-policy statements are historical observations, not current ACM policy guidance.

Use this exemplar to construct auditable methodological arguments, not a universal checklist or a benchmark claiming all research should expose identical materials.
