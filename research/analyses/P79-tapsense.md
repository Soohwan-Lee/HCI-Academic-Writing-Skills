# P79 — TapSense

**Provenance.** Harrison, Schwarz, and Hudson, UIST 2011, DOI [10.1145/2047196.2047279](https://doi.org/10.1145/2047196.2047279). Read the complete author-hosted PDF from chrisharrison.net. This file has **eight PDF pages**, whereas publisher metadata specifies ten proceedings pages; all locators refer to the analyzed file, not assumed proceedings pagination. Both selected complete paragraphs were rendered and visually checked. Single-analyst, version-dependent coding; award unverified.

## Object, architecture, and opening

The contribution is an acoustic input-discrimination technique integrated with existing touch localization, not a general-purpose classifier or a behavioral theory. The actual sequence is **Introduction → Related Approaches → Sensing and Processing → Proof-of-Concept Setups → Fingers → Pens, Pointers, Stamps and Tools → Evaluation → Results → Conclusion → Acknowledgements → References**. Hardware configurations and application possibilities precede evaluation. Results distinguish pooled, personalized, and held-out-user classification, followed by training-volume analysis.

The abstract starts with the artifact capability, explains its acoustic mechanism, gives anatomically meaningful examples, motivates touch-interaction possibilities, extends to passive tools, and previews accuracy/training evidence. The introduction (p. 1) moves from widespread touch use to impoverished coordinate-only input, contrasts this with finger capabilities, and introduces recognition without user instrumentation. It uses a concrete alternate-click example instead of a long numbered-RQ sequence. Evaluation questions appear later, at the start of Results, because they concern the artifact's operating envelope.

Related Approaches (pp. 1–2) organizes active versus passive sensing, with intermediate electromagnetic approaches. Its comparisons track instrumentation, object identity, marker size, cost, and classification evidence. Acoustic predecessors are acknowledged explicitly; the argument narrows to discriminating input types without instrumenting users and reporting training/accuracy detail. This is a constraint-based comparison rather than an author-by-author list, although its strongest judgments about earlier systems should be treated as the authors' positioning.

## Claim, support, warrant, and boundary

The core warrant is that different contacting materials produce distinguishable acoustic signatures that can be paired with location events. Two physical setups and interface demonstrations establish implementation possibility. Data from 18 participants support classification analyses, not demonstrated typing-speed improvements or lower cognitive burden. High accuracy depends on input-set size and training regime: post-hoc removal of confused classes changes what the system recognizes. Pooled cross-validation can share participants across train/test sets, while held-out-user results test a different deployment question. Personalization matters more for fingers than manufactured tools.

The distinction between measured and prospective claims is crucial. Timing collisions limit simultaneous inputs; the mobile prototype processes audio on an external computer. Suggested built-in-microphone use and accuracy with much larger training sets are projections. Describing collected-data results as a lower bound because additional training might help is not a guaranteed statistical bound. The conclusion's compact accuracy claim should therefore be read through the detailed conditions rather than copied as an unconditional benchmark.

## Micro-analysis 1: a local failure mechanism

**PDF p. 3, Sensing and Processing; opening “In practice, this method appears”.** Three sentences: **S1** offers a qualified practical-success observation; **S2** introduces timing collisions as an unresolved exception; **S3** explains how near-simultaneous impacts defeat segmentation and classification. Relation: **qualified capability → exception → causal mechanism**. It follows event matching and latency, then leads into factors determining the collision window. The paragraph puts a limitation beside the mechanism it qualifies, rather than deferring all uncertainty to the end.

## Micro-analysis 2: interpreting a metric

**PDF p. 6, Results / Ten-Fold Cross Validation; opening “To get a general sense”.** Three sentences: **S1** names the pooled evaluation and its data; **S2** explains why shared users and temporal proximity can inflate this statistic; **S3** retains its limited role as a baseline and points to the figure. Relation: **measurement → validity qualification → bounded use**. Entry follows input-set pruning; exit introduces per-user classifiers. The same figure can support several deployment interpretations only if the prose explains the split assumptions.

## Transfer and exception

Separate sensing, applications, and validation obligations. Use result subsections to distinguish deployment regimes rather than presenting one headline accuracy. Put failure mechanisms near the relevant implementation. This artifact paper combines a capability-led abstract with later evaluation questions; neither mandatory early RQs nor a single generic “user study proves utility” template captures its argument. Its optimistic extrapolations are counterexamples to imitate cautiously, not universal style rules.
