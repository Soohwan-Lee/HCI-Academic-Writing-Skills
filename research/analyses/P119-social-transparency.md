# P119 — Expanding Explainability: Towards Social Transparency in AI systems

## Source and review scope
arXiv 2101.04719v1, 12 January 2021, 29 pages; not compared with proceedings version. [Source](https://arxiv.org/pdf/2101.04719v1); [publication DOI](https://doi.org/10.1145/3411764.3445188). Claude Opus 5.5 medium analyzed the full text via the existing Claude Code subscription. Root independently read the main text through page 24 and inspected rendered pages 7, 9, 12, including both micro-analysis passages. Other figures were consulted through captions and adjacent text. No independent human coding, numerical length measurement, or study replication is claimed. Reviewed 2026-10-30.

## Contribution contract
**Promised:** (1) naming an epistemic blind spot in XAI; (2) Social Transparency (ST) as a concept, embodied in a speculative design with What/Why/Who/When (4W) features; (3) a formative framework of technological, decision, and organizational context; (4) design insights and tensions.

**Not promised:** a built system, an effect evaluation, or a complete account of socially situated XAI.

**Methods:** four workshops (21 people), four pilots, and 29 semi-structured scenario interviews analyzed through open coding, thematic clustering, and grounded-theory-informed comparison.

**Form:** a critical-reflective argument, framed by Critical Technical Practice (CTP), wrapped around a conventional CHI empirical report.

## Section architecture
1 Introduction (pp. 1–3). 2 Related Work (pp. 3–7): 2.1 XAI; 2.2 sociotechnical approaches; 2.3 social transparency and related concepts. 3 Scenario-Based Design Exploration (pp. 7–8). 4 Study Methods (pp. 8–10): 4.1 Recruitment; 4.2 Procedure; 4.3 Analysis. 5 Findings (pp. 11–21): 5.1 technical transparency's insufficiency; 5.2–5.4 the three contexts; 5.5 4W (5.5.1–5.5.4); 5.6 transferability (5.6.1–5.6.2); 5.7 challenges. 6 Discussion (pp. 21–24): 6.1 holistic explainability; 6.2 human-AI assemblage; 6.3 socially situated XAI. 7 Limitations (p. 24). 8 Conclusion (p. 24). Acknowledgments and references follow (pp. 25–29).

## Abstract and introduction moves
The nine-sentence abstract moves through stakes (S1), paired premises about situated explanation and embedded AI (S2–3), the algorithm-centered gap (S4), the concept (S5), method (S6), products (S7), hedged potential effects (S8), and field contribution (S9).

The introduction moves from why explanations matter to evidence that XAI techniques disappoint, then uses CTP to convert that shortfall into an assumption problem. A broad definition of explanation as an answer to a why-question matters structurally: it lets non-model information qualify as explanatory. A pricing vignette then dramatizes the gap. It is a constructed illustration whose cause is stipulated, not a case finding. The aims, a scope disclaimer, and four contributions close the section.

## Related-work jobs
- **2.1 establishes inadequacy.** Its three issues are mixed empirical performance, product versus process views of explanation, and absent sociotechnical perspectives. Hong et al. serve as the closest precedent.
- **2.2 borrows legitimacy.** Critical and fairness scholarship supports widening the analytic boundary, and the section ends by claiming the operational step that follows.
- **2.3 supplies genealogy and mechanisms.** Translucence, awareness, and Stuart et al.'s ST provide the design lineage. Transactive memory and heuristics provide interpretive resources that return in Findings.

## Evidence, warrant, limits
**Evidence:** participant accounts of their own AI work; think-aloud reactions to a scenario; before/after price and confidence reports; 4W rankings; transfer brainstorming.

**Warrant:** if practitioners locate why-answers outside the model, both in their own work and when reacting to a concrete ST probe, then socio-organizational context belongs inside explainability's design space.

**Limits:** there was no control condition, reveal order was fixed, comments were researcher-authored, and no pricing ground truth exists. Lower prices and higher confidence therefore cannot establish better decisions. Participants' accounts describe perceived or anticipated value, not observed organizational behavior. Transfer discussion followed researchers' conceptual debriefing, so 'holistic' explainability may be partly prompted. The authors call the insights formative and acknowledge scenario-data dependency.

## Findings-to-discussion transitions
Section 5 progresses from need (5.1), to contextual effects (5.2–5.4), features (5.5), transfer (5.6), and risks (5.7). Section 6 elevates rather than repeats these results. 6.1 turns participant surprise into a claim about the field's narrow boundary, but it also adds new debrief quotations, so Discussion partly carries evidence. It then extends to developers, auditors, and automated systems, none of which the study examined. 6.2 extrapolates from organizational meta-knowledge to transactive memory and possible collective mind; this is theoretical projection. 6.3 converts reported needs into unbuilt requirements, such as summarization, quality control, and ingesting social data. These are design implications, not validated capabilities.

## Paragraph micro-analysis 1: §2.3, final paragraph, p. 7 (4 sentences)
1. Marks inherited concepts, then pivots to the distinguishing center: explainability in AI-mediated decisions. Its plural 'distinctions' is not itemized.
2. Narrows the object from visibility of others' activity to the bearing of their AI interactions on explainability.
3. Licenses conceptual transfer: the assemblage view treats people and AI as decision agents, so human-human lenses can be borrowed.
4. Sets the study's first-order scope (sense-making and decisions) while conceding organizational spillover.

**Function:** a differentiation paragraph that moves from inheritance through boundary and warrant to scope.

## Paragraph micro-analysis 2: §5.1, p. 12 (7 authorial sentences plus a 5-sentence block quotation)
1. Restates the thematic claim: needed knowledge may lie outside the machine.
2. Ties it to participants' repeated requests for context.
3. Reframes the 4W scenario as an intended response, marking design intent rather than result.
4. Reports price movement after ST exposure against the $100 recommendation.
5. Reports parallel confidence movement.
6. Interprets both as cautious, more confident judgment, supported by a participant phrase. This is the paragraph's main inferential leap.
7. Introduces the quotation as a summary.

Block quotation:
- Q1 asserts data incompleteness.
- Q2 generalizes it to how the world works.
- Q3 challenges machine-only sense-making rhetorically.
- Q4 states context as the condition for holistic trust judgment.
- Q5 positions ST as completing explainability.

**Function:** the paragraph moves from theme to participant demand, design intent, descriptive numbers, interpretation, and voiced conclusion. The numbers illustrate the qualitative claim; §4.2 explicitly disclaims quantitative evaluation.

## Cross-paragraph connections
The why-question definition (p. 2) underwrites Paragraph 2's claim about knowledge outside the model. Paragraph 1's scope predicts the emphasis on decisions in 5.1–5.3, while its concession about organizational behavior reappears as 5.4. Paragraph 2's vague 'context' is immediately resolved by the three-level roadmap on p. 13. The vignette's pandemic example recurs in participant reasoning (p. 14) and the When feature (p. 19), giving the paper continuity. The opening pain point returns in 6.1 as a field-level reframing.

## Transferable lessons and counterexamples
- **Define the construct to expose a boundary choice.** Counterexample: an overbroad definition can make the thesis nearly definitional. Show what the definition excludes.
- **Use a speculative artifact as a probe when the concept has no deployed instance.** Counterexample: when feasibility or effect is the claim, a probe cannot substitute for a system evaluation.
- **Pair each contribution with a later section.** Here, the blind spot maps to §§1–2, 4W to §3, the framework to §§5.2–5.4, and tensions to §§5.5, 5.7, and 6.3. Counterexample: interpretive essays may need a developing argument rather than a checklist.
- **Separate effect-of-context from effect-of-feature.** Tables 2 and 3 do this cleanly. Counterexample: their 'effects' labels invite causal reading, so qualitative work should prefer 'anticipated' or 'perceived' effects.
- **Report descriptive numbers as prompts for interpretation.** Counterexample: 'helped' after an uncontrolled before/after change overstates what such numbers can show.
- **Give risks their own section.** Counterexample: when harms are central to the argument, a late section can make them seem peripheral.

## Root integration review
Primary routing is conceptual with qualitative/formative warrants; use the qualitative guide for how accounts and scenario responses warrant the framework. Existing social-transparency, awareness and transactive-memory concepts are explicit antecedents. Naming ST in AI does not erase that lineage. The design space and framework are the knowledge objects, not demonstrated improvements in trust, decisions or organizational performance. Root checked the four-sentence differentiation paragraph, the seven authorial sentences with a separate five-sentence block quotation, and the scenario illustration. The illustration supplies selected histories and outcomes; before/after judgments cannot establish actual decision quality.

The source reports eight sellers, but its participant table marks nine IDs with -S; retain this source inconsistency rather than invent a corrected sample split. Recruitment spans six companies and is not a representative cross-industry sample. Discussion projections to auditors, model development and collective mind need to retain their prospective status. Numeric details in formative work do not automatically turn it into an effect-evaluation contribution.
