# P116 — I Think I Get Your Point, AI! The Illusion of Explanatory Depth in Explainable AI

## Source and review scope
ACM-formatted author copy, 11 pages; no version comparison. [Source](https://www.mmi.ifi.lmu.de/pubdb/publications/pub/chromik2021iui/chromik2021iui.pdf); [publication DOI](https://doi.org/10.1145/3397481.3450644). Claude Opus 5.5 medium analyzed the full text via the existing Claude Code subscription. Root independently read the main text through page 10 and inspected rendered pages 1, 2, 10, including both micro-analysis passages. Other figures were consulted through captions and adjacent text. No independent human coding, numerical length measurement, or study replication is claimed. Reviewed 2026-10-30.

## 2. Contribution contract
**Contract:** for non-technical users, felt global understanding gained from local additive explanations may not survive examination, so explanation and evaluation should not rest on one-shot self-report. The introduction announces three contributions but enumerates two: SHAPTable and the IOED result. The conclusion implies a third: described reasoning strategies and design starting points.

**Method, separately:** staged within-subjects procedure, repeated self-ratings, simulation test, think-aloud coding. **Form, separately:** hypothesis-led empirical paper with a dedicated apparatus section. SHAPTable is claimed as a contribution but functions as apparatus; no comparative interface evaluation appears.

## 3. Exact section architecture
Abstract; CCS Concepts; Keywords; 1 Introduction; 2 Background and Related Work (2.1 Explanations from Intelligent Systems; 2.2 Illusion of Explanatory Depth; 2.3 IOED and Cognitive Biases in XAI and IS); 3 Research Questions and Hypotheses; 4 SHAPTable (4.1 Scenario, Data Set, and ML Model; 4.2 Explanation Facility); 5 Methods (5.1 Participants, with 5.1.1 Moderated and 5.1.2 Unmoderated; 5.2 Procedure; 5.3 Dependent Variables; 5.4 Design and Analysis); 6 Results (6.1 Robustness of Perceived Understanding; 6.2 How Users Formed Their Understanding); 7 Discussion (run-ins: Calibrating Understanding; Forming Rationales; Limitations); 8 Conclusion; References.

## 4. Abstract and introduction moves
The five-sentence abstract moves from societal pressure, to a local-to-global burden on users, to the question, to the method, to the observed outcomes. It withholds effect sizes, test scores, and design implications.

The introduction has four paragraphs: (1) stakes and the operator audience; (2) a double critique of local-only studies and one-shot ratings, resolved by importing overconfidence research; (3) thesis, gap, and study outline; (4) audience gap and contributions. The critique of measurement is the hinge: the paper's own repeated measurement becomes the answer to it.

## 5. Related work's argumentative jobs
- **2.1 fixes the vocabulary:** black-box, post-hoc, fidelity, local versus global. Simplification thereby becomes a known risk.
- **2.2 imports the theory:** it establishes explanatory versus descriptive knowledge, domain extension, and four candidate causes.
- **2.3 builds the bridge and gap:** mental models link IOED to HCI; prior speculation shows plausibility without systematic study; neighbouring biases situate the claim; Dunning-Kruger is distinguished by scope.
- **Section 3 selects:** only two of the four causes become mechanisms for this context. They are stated as hypothesized routes, not tested variables.

## 6. Evidence, warrant, limits
- **H1 (explanations raise perceived understanding).** Evidence: unmoderated T1 mean 4.33 to T2 mean 4.75; 53 of 107 rose. Warrant: the T1–T2 gain reflects explanation exposure. Limits: fixed order, no separate control, and no T1 in the moderated study. The baseline was already fairly high.
- **H2 (IOED applies).** Evidence: T5 below T2 in both studies; 63% and 72% lowered ratings. Warrant: post-examination decline indicates prior inflation. Limits: T5 follows personalized score feedback and re-examination, so calibration, discouragement, or demand cannot be separated. Unmoderated verbalization, the classic trigger, produced no significant drop. No black-box arm completed the examination, so a Shapley-specific effect is not isolated. A rating decline is an indirect indicator, not a directly observed illusion.
- **Objective understanding.** Means of 2.85 and 2.66 of 8 exceed the 1.86 chance estimate. This shows above-chance simulation on eight items, not an accurate global model.
- **RQ2.** Evidence comes from six think-aloud protocols, recordings, and open coding. These are participants' accounts and observed interaction, from which mental models are inferred; they do not expose those models directly. 'All participants' should be read cautiously, since the section's stated base is six.
- **Moderated versus unmoderated contrast.** Moderation is confounded with recruitment, sample, procedure length, and Task 1. The System 1/System 2 reading is an assumption, then an interpretation; it was not measured.

## 7. Findings-to-discussion transitions
The discussion restates the decline, then pivots to where the drops occurred: two moderated drops versus one late unmoderated drop. It marks interpretation ('we interpret', 'we believe') before a normative step: systems should guide interaction and expose complexity. Two conversions follow. The measurement procedure becomes a candidate onboarding intervention, though only perceived helpfulness (85% and 69% agreement) supports it, and no onboarding effect was tested. Abstraction difficulty becomes a proposal to condense local explanations, which is future work and not a validated capability. The conclusion hardens the language by saying users overestimate 'because of' the IOED, which is stronger than the design licenses.

## 8. Paragraph micro-analysis A
**Section 1, third paragraph, pp. 1–2. Twelve sentences.** A page break splits S2.
- S1: states the thesis, with hedged risk.
- S2: sharpens the risk by contrasting assumed gains with false or incomplete beliefs.
- S3: credits prior speculation.
- S4: declares the gap, qualified by the authors' knowledge.
- S5: states the study aim.
- S6: narrows to local post-hoc Shapley explanations.
- S7: names evaluation type, domain, and data.
- S8: specifies model and explanation generator; a footnote gives the repository.
- S9: labels the approach.
- S10: gives Study 1 size and observational role.
- S11: assigns Study 2 the hypothesis-verifying role.
- S12: reports ethics approval.

The paragraph funnels from risk to procedure in one block. Its weakness is S11: 'verified' overstates the unmoderated study's role, and H1 is testable only there.

## 9. Paragraph micro-analysis B
**Section 7, run-in 'Forming (Global) Rationales from Local Explanations', p. 10. Seven sentences, excluding the run-in heading.**
- S1: states the finding and aligns it with one prior study.
- S2: specifies the difficulty: local justifications seemed understood, representativeness did not. No separate local-comprehension measure is reported in the text.
- S3: pivots from finding to technical possibility, hedged by 'might'.
- S4: proposes future research on condensation.
- S5: ties that idea back to observed strategies.
- S6: links it to rationales.
- S7: defines rationales.

The paragraph's order, from finding to affordance to concept, makes a design hypothesis feel grounded. S5's 'in our studies' blurs the fact that strategy evidence comes from six protocols.

## 10. Cross-paragraph connections
The four IOED causes in 2.2 narrow to two in Section 3. Label/mechanism confusion resurfaces when users under- or overestimate interactions; representation/recovery resurfaces in memory aids during verbalization. These are thematic echoes, not mechanism tests. The introduction's complaint about self-report returns as repeated self-rating, and later as the calibration implication. 'Local-to-global' threads the abstract, RQ2, Abstraction codes, and paragraph B.

## 11. Transferable lessons and counterexamples
- Pair a substantive gap with a measurement gap. *Counterexample:* unnecessary where established measures are not contested.
- Import a theory, then state which mechanisms apply and why. *Counterexample:* inventorying all four causes without selecting would add nothing.
- Stage a procedure so each rating has a rhetorical and analytic meaning. *Counterexample:* without counterbalancing or control, staged order weakens causal language.
- Report where results diverge from the expected pattern. Here, the rise at T4 is disclosed. *Counterexample:* do not then explain subgroup differences causally when groups were not randomized.
- Keep hedges stable from results to conclusion. This paper shows the failure case: 'may', 'indicate', then 'because of'.
- Convert instruments into design ideas only as hypotheses. *Counterexample:* 'playful' extension of cognitive forcing is asserted, not evidenced.

## Root integration review
Primary route is quantitative evidence, with a methodological critique and qualitative interaction account. Applying IOED in a new context is not automatically revising its theory. Keep moderator presence, recruitment and task differences separate; neither cognitive-processing mode nor an isolated effect of Shapley values was identified. The twelve-sentence introduction paragraph and seven-sentence implication paragraph are visually confirmed, including their page/column continuations. They illustrate rhetorical choices, not recommended paragraph lengths. The source's three-contributions/two-items mismatch is retained as a caution rather than silently repaired in its description.
