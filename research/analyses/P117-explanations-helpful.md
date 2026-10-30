# P117 — Are Explanations Helpful? A Comparative Study of the Effects of Explanations in AI-Assisted Decision-Making

## Source and review scope
ACM-formatted author copy, 11 pages; no version comparison. [Source](https://mingyin.org/paper/IUI-21/iui21.pdf); [publication DOI](https://doi.org/10.1145/3397481.3450650). Claude Opus 5.5 medium analyzed the full text via the existing Claude Code subscription. Root independently read the main text through page 10 and inspected rendered pages 3, 9, 10, including both micro-analysis passages. Other figures were consulted through captions and adjacent text. No independent human coding, numerical length measurement, or study replication is claimed. Reviewed 2026-10-30.

## Contribution contract
The paper promises: (1) three posited, explicitly non-comprehensive desiderata for helpful explanations: understanding, uncertainty awareness, and trust calibration; (2) a comparison of four established model-agnostic explanation types against them; (3) evidence that outcomes differ between tasks associated with different perceived expertise; (4) implications for selecting explanations and reporting evaluations.

Method is separate: between-subject MTurk experiments with five treatments per task. Form is also separate: an RQ-structured empirical report. The experiment does not validate the desiderata; it applies them.

## Section architecture
Abstract; CCS Concepts; Keywords; 1 Introduction; 2 Literature Review (run-in heads: Overview of AI explanation methods; Desiderata of AI explanations; Empirical Studies on the Effectiveness of AI explanations); 3 Study Design (RQ1–3), with 3.1 Decision Making Tasks, 3.2 Experimental Design (3.2.1 Experimental Treatments; 3.2.2 Selection of task instances), 3.3 Experimental Procedure, 3.4 Analysis Methods (3.4.1 Independent variables; 3.4.2 Dependent variables; 3.4.3 Statistical methods); 4 Results (4.1 RQ1; 4.2 RQ2; 4.3 RQ3; 4.4 Summary of results); 5 Conclusion and Discussion (run-in heads: The role of domain expertise; Implications for designing and selecting XAI methods; Limitations); Acknowledgments; References.

## Abstract and introduction moves
The abstract states its contribution first, then criteria, method, three findings, and implications. The introduction moves from proliferating aids and XAI techniques, through contrasting technical and social-science rationales, to three stacked questions. It then cites the call for human evaluation, names an unarticulated-principles gap, states the contribution, and previews procedure, findings, and implications. The title's question is answered conditionally rather than yes or no.

## Related-work jobs
- **Overview** defines the design space and positions model-agnostic methods without evaluating them.
- **Desiderata** moves from taxonomy to evaluation criteria. Two scope filters justify extraction, and each desideratum is then given a rationale. This subsection also separates accuracy gains from calibrated trust.
- **Empirical studies** uses Table 1 to expose thin coverage and mixed results, licensing a systematic comparison and a task moderator.

## Evidence, warrant, limits
- **Understanding:** Measured by nine objective items and two self-report items. Recidivism: feature importance and counterfactuals raised objective scores, and all four types raised subjective scores in aggregate and regression analyses. Forest cover: only feature importance (objective) and feature contribution (subjective) showed conclusive gains.
- **Uncertainty awareness:** The warrant is behavioral. Reliance is expected to rise on high-confidence cases. Positive confidence-by-explanation regression terms appeared for recidivism, although the aggregate difference-in-difference interval was [-0.02, 0.42]. Participants 'might have' inferred uncertainty; that process was not observed.
- **Trust calibration:** Feature contribution received the sole positive mark, on recidivism. Its appropriate-trust coefficient interval includes zero (0.01 [-0.003, 0.03]), while its undertrust reduction excludes zero. The prose claim that it 'increases' appropriate trust therefore exceeds that interval.
- **Expertise:** This is perceived expertise from a 98-person pilot, not a manipulated or measured skill variable. Expertise is bundled with task domain, and forest participants alone received an introduction and 10 training tasks. The supplied text reports no between-task interaction test, so 'dramatically different' is a descriptive contrast.
- **Generalization:** Limited by MTurk laypeople, logistic regression, about 69% model accuracy, selected prototype instances, and specific explanation formats. The authors caution against over-generalizing.
- **Null handling:** Negative table marks mean no supportive evidence was found, not demonstrated failure. Phrases such as 'do not satisfy' can read more strongly than 'inconclusive' intervals warrant.

## Findings-to-discussion transitions
Section 4.4 compresses the matrix into four findings. Section 5 recasts the forest-task pattern as 'ineffectiveness', which poses a why-question. The answer is labeled conjecture, not a tested mechanism. It then moves to design and selection advice, cross-desideratum independence, limitations, and a reporting recommendation. Cognitive load was not measured, and the proposed non-expert heuristics (summing contributions, counting counterfactuals) were not tested. These are hypotheses, not validated capabilities.

## Micro-analysis A: p. 3, §2, 'Empirical Studies' (8 sentences)
1. Establishes a small but growing research line.
2. Hands synthesis to Table 1.
3. Gap one: Desideratum 2 is rarely examined and Desideratum 3 is often assessed through accuracy alone.
4. Gap two: mixed results, with causes left open.
5. First cause, yielding the need for systematic comparison.
6. Second cause: task properties may moderate effects.
7. Exemplifies with expertise and a speculative causal chain.
8. Converts both gaps into the study's design.

The paragraph turns literature into design requirements. Its modals ('may', 'could') keep moderation hypothetical.

## Micro-analysis B: pp. 9–10, §5, 'The role of domain expertise' (8 sentences)
1. Reframes the null-heavy pattern as a why-question.
2. Declares conjectural status.
3. Mechanism one: unfamiliar explanations burden consumption.
4. Grounds this in tacit knowledge and working memory.
5. Applies it to forest participants, who may not know some feature meanings. 'Particularly true' is firmer than the unmeasured evidence allows.
6. Mechanism two: expertise may support inference about uncertainty and correctness.
7. Illustrates plausible strategies with feature contribution.
8. Closes with the implied failure when expertise is absent.

The paragraph is a labeled explanatory bridge, not a finding. Every mechanism depends on participants' unobserved cognition.

## Cross-paragraph connections
The triplet runs through the whole paper: introduction questions, desiderata, RQs, 3.4.2 measures, 4.1–4.3, and Table 2 columns. Paragraph A's accuracy critique motivates overtrust and undertrust, yet appropriate trust is defined as effectively final accuracy, which creates a tension. Paragraph A's expertise moderator leads to the 3.1 pilot, 4.4, and Paragraph B. Paragraph B then supports the design implications, which depend on its conjectural premise.

## Transferable lessons and counterexamples
- **Fix criteria before comparing.** Counterexample: exploratory qualitative work may need criteria to emerge from data.
- **Use a coded synthesis table to reveal absences.** Counterexample: Table 2's marks flatten effect sizes and interval uncertainty, and its positive mark can outrun the intervals.
- **Thread one conceptual structure from questions to discussion.** Counterexample: strong unanticipated findings may justify breaking the structure.
- **Separate proxy from construct.** Counterexample: this paper warns against accuracy as sufficient evidence while building accuracy into one calibration metric. Pair such a metric with error-type measures, as this paper does.
- **Label explanatory speculation.** Counterexample: a later phrase like 'particularly true' can undo the hedge.
- **Treat a two-task comparison as a contrast.** Do not imply a moderator effect unless a design and test support it.

## Root integration review
Root checked both complete eight-sentence paragraphs and the table symbols in rendered pages. Table 1 distinguishes absent examination from absent supportive evidence, and Table 2 also marks partial understanding evidence. Preserve those distinctions when writing a synthesis table. The source's trust-calibration verdict needs qualification because some reported intervals include zero. Task differences do not isolate expertise as the moderator. The recidivism task measures participants' predictions against dataset labels; it does not establish justice, fairness, or suitability for real sentencing. This note does not endorse that application. Main studies retain 782 and 561 participants after filtering; the 98-person pilot is separate.
