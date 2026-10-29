# P08 — Guidelines for Human–AI Interaction

**Source:** Amershi et al., CHI 2019, [DOI](https://doi.org/10.1145/3290605.3300233), [Microsoft author copy](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf). Single-analyst rhetorical coding of this PDF; not a claim about all CHI papers. Page-one layout was visually checked. Award verification belongs in the corpus manifest, not inferred from the paper.

## Contribution and architecture

Primary contribution: a reusable design-guidance resource. Secondary contribution: empirical evidence about its relevance and interpretability. The four-stage construction and evaluation process is the method; having a user study does not make an experiment the paper's primary knowledge contribution.

The actual top-level sequence, with long labels paraphrased, is §1 Introduction → §2 Related Work → §3 initial guideline consolidation → §4 adapted heuristic assessment → §5 practitioner study → §6 expert assessment of revisions → §7 Discussion/Future Work → §8 Conclusion. Methods and results appear inside stages rather than as one global pair. Table 1 exposes the resulting resource before the complete derivation.

## Abstract and introduction moves

The abstract on p. 1 moves from technological opportunity/challenge to the need to revisit earlier guidance, then names the resource, describes validation, reports relevance and remaining gaps, and identifies intended beneficiaries. Its result is a validated resource with qualified applicability, not a performance increase.

The introduction (§1, pp. 1–2) first makes a capability-to-risk transition with concrete interface examples. Its second paragraph explains why familiar usability principles become difficult under probabilistic behavior. The next paragraph acknowledges two decades of prior guidance, then contrasts that accumulated knowledge with continuing design failures. The final move names the synthesis and gives two contribution bullets: codification and validation. It ends with intended use. There is no numbered RQ list that needs to be imitated or retrofitted.

## Positioning and evidence

Related work (§2) groups earlier work into general principles, deeply studied issues, and specific interaction settings. It then diagnoses a discoverability and transfer problem: guidance is dispersed, sometimes implicit, and may not travel between settings. The closest predecessor is explicitly acknowledged, including overlap. Novelty therefore rests on consolidation plus systematic examination, not on pretending no previous guidelines exist.

The central evidence chain is source recommendations → selection and clustering → initial guidelines → observed ambiguity/application → revision → further assessment (§§3–6). The warrant is that practitioners can recognize and distinguish the guidelines across varied products. The discussion (§7) keeps this apart from the stronger, still prospective claim that applying them improves downstream user outcomes. It also identifies interface observability, specialization, guideline conflicts, and ethics as boundaries.

## Transferable writing decisions

For a resource paper, show the deliverable early, then make each transformation accountable. A stage should explain what changed and why; process chronology alone is insufficient. Distinguish evidence of clarity, relevance, adoption, and effectiveness in contribution statements. Acknowledge inherited ideas before specifying the added work. Treat ambiguous or inapplicable cases as informative limits rather than cleaning them out of the narrative.

These are editorial adaptations from one case. The structure is useful when intermediate revisions matter to credibility; it is not a requirement that every guideline paper use four phases, contribution bullets, or the same validation methods. No paragraph-length or section-ratio norm is inferred here.

## Paragraph micro-analysis

**Locator:** §1, p. 1, opening “Advances in artificial intelligence”. Five sentences in the first introduction paragraph (visually checked): **S1** establishes the new interface capability space (topic-setting claim); **S2** gives concrete examples of capabilities and adoption pressure (elaboration); **S3** pivots from capability to uncertainty and harmful behavior (contrast plus stakes); **S4** expands the setting from explicit interaction to background services (scope expansion); **S5** contrasts useful personalization with hidden information and misaligned actions (qualification and problem sharpening). This is topic-first, but not conclusion-first: the paragraph does not yet state the guideline contribution. There is no previous introduction paragraph. The next paragraph converts these concrete risks into a conflict with established usability principles, supplying the conceptual warrant for revisiting guidance. A transferable pattern is capability → examples → failure mechanism → scope → consequence; it should not be mistaken for five mandatory sentence slots.
