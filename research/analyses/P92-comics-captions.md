# P92 — Dense comic captioning

Single-analyst rhetorical coding of the 16-page author manuscript linked by the official IUI 2024 temporary proceedings. Page numbers refer to that version, whose DOI field is a placeholder; the published DOI is 10.1145/3640543.3645154. Full body and references read; both selected paragraphs rendered to check boundaries. Best Paper is independently recorded in the ACM SIGAI IUI 2024 conference report. This is evidence about one paper's writing, not a universal convention.

## Contribution and architecture

The knowledge object combines a caption-generation technique with accessibility design knowledge: grouping comic panels can support more coherent descriptions, but automatic realization remains uneven. Its methods include model adaptation, ablation, sighted assessment, and a study with visually impaired participants. Classifying it merely as “mixed methods” would conceal what each method warrants.

Actual order: abstract → Introduction → Related Work → Dense Comic Captioning → Preliminary Assessment with Sighted Evaluators → User Study → Discussions → Limitations → Conclusion → acknowledgments/references. Technical validation and two distinct populations receive separate sections. There is no need to manufacture an opening list of RQs or merge everything into one Methods–Results pair.

## Framing and literature logic

The abstract moves from existing image descriptions to a sequence-specific failure, grouping proposal, two evaluations, conditional findings, and recommendations. Its useful discipline is separating human-generated dense descriptions, which improve multiple ratings, from AI-generated ones, whose significant advantage is length. An abstract should preserve this interaction rather than report that “our AI outperformed the baseline.”

The introduction (pp. 2–3) begins with comics' popularity, narrows to exclusion and annotation cost, explains why isolated-image captioning mishandles sequences, and proposes a video-captioning analogy. Implementation, ablation, both assessments, and a contribution list follow. The analogy does argumentative work: it suggests a representation while exposing an empirical question about transferring video methods to discontinuous illustrations.

Related work separates accessibility-oriented description research from image/video captioning. The former supplies user needs and contextual requirements; the latter supplies technical possibilities. Their intersection motivates the gap. This is stronger than treating prior systems as a chronological inventory, although the eventual transfer still requires evidence about comics' distinctive visual grammar.

## Claims, evidence, and boundaries

The model adapts a video-captioning architecture, tests visual features and panel duration, and adds comic annotations. Automatic metrics establish technical comparisons, not accessibility. Three sighted evaluators assess 24 strips; the main study involves 12 visually impaired participants. Human dense descriptions score better across preliminary measures, whereas automatic dense descriptions improve significantly only on length. Main-study ratings do not differ significantly; qualitative accounts identify conciseness, stable references, detail, coherence, and reduced redundancy.

Several boundaries are essential to retain. The main study selects three strips with the highest automatic-caption accuracy, so it investigates favorable potential rather than representative performance. Baseline and proposed models use different training data. Three sighted evaluators generate many ratings but remain three people. Model-generated descriptions can misidentify scenes. Anticipated improvements from larger data or language-model refinement are proposals, not findings. Discussion language about preferences must be read alongside the nonsignificant main-study ratings; award status does not remove this interpretive obligation.

## Two complete paragraph micro-analyses

**A. p. 10, §5.2, entire paragraph; opening “Instead of presenting 24”.** Six sentences. S1 explicitly changes the stimulus set and justifies selecting best-performing examples. S2 points to descriptive stimulus statistics. S3 specifies remote delivery and the crossed set of audio materials. S4 controls speech synthesis voice and rate. S5 describes an ending cue. S6 records session capture. Relation: sampling decision → characterization → delivery → controls → analysis record. Entry follows participant recruitment; exit enables the next procedure paragraph. The opening is a methodological contrast, not a generic topic assertion. Its candid sampling rationale is highly transferable, provided later claims inherit its restricted scope.

**B. p. 11, §5.4, first paragraph; opening “Reflecting the findings from”.** Four sentences. S1 connects the descriptive ordering to the earlier assessment. S2 supplies endpoint means and scale direction. S3 blocks a significance inference. S4 redirects attention to thematic evidence and states coding/reliability details. Relation: cross-study pattern → numerical grounding → qualification → justified analytic shift. Entry follows study procedure; exit prepares the five thematic subsections and figure. The paragraph's pivotal sentence is the qualification, not its first sentence. Copying only its positive opening would distort the result.

## Transferable moves

Separate technique feasibility, population-specific judgment, and design recommendations. Use conditional result sentences when advantages depend on author type or metric. Locate an explicit sampling restriction beside the sampling decision, then carry it into discussion. Let qualitative findings supply explanations after an inconclusive quantitative comparison without recasting them as proof of a statistically superior system.
