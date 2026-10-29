# P83 — ERICA

**Provenance.** Deka, Huang, and Kumar, UIST 2016, DOI [10.1145/2984511.2984581](https://doi.org/10.1145/2984511.2984581). Full ten-page author-hosted PDF read, including the flow figures that occupy entire pages; selected complete paragraphs on pp. 3 and 9 were rendered and checked. Single-analyst, PDF-version-dependent coding; award unverified. Selected as a resource-enabling infrastructure paper whose coverage argument differs from classifier or user-performance validation.

## Object and actual sequence

The contribution is an interaction-mining system and representation, with a collected repository and a semantic-flow search application demonstrating utility. Human exploration, instrumentation, clustering, and rule/classifier construction are methods serving that object.

Actual order: **Introduction → Background and Related Work → Interaction Mining → ERICA: Interaction Mining for Android Apps → Collecting User Interaction Traces → Extracting Semantic User Flows at Scale → Discussion and Future Work → Acknowledgments → References**. Requirements precede architecture; collection precedes an application built from the data. Flow detection and search are subsections, not a generic participant-study Results chapter. No separate Conclusion appears.

The abstract follows design complexity → interaction mining → human/computer capture system → collection scale → flow detectors → search repository. Its introduction (pp. 1–2) expands the different design activities, explains what static and dynamic information can support, assigns human and machine roles, reports resource scale, and previews downstream applications. The rhetorical center is a new capability and reusable representation, not a numbered hypothesis sequence.

## Literature and gap

The short Background and Related Work section explicitly extends Webzeitgeist's static design mining to connected app states and interactions. Static app extraction misses dynamic information; automated runtime exploration may reach states without producing meaningful human task sequences. Human-driven exploration is introduced to address that semantic limitation. The next requirements section turns this comparison into capture, meaningful-state coverage, and scalability obligations. Thus the gap is operationalized in architecture rather than repeated as a vague absence of research.

## Claim, support, warrant, and limits

ERICA joins screenshots, UI hierarchy, and events into traces without modifying individual app source or binaries. Its Android operating system is modified: “no app modification” must not become “no instrumentation anywhere.” The 28 recruited participants supply 1,065 retained sessions over 1,011 apps after filtering. Those numbers establish a collected resource, not a representative sample of normal mobile behavior. Participants were instructed to use fake personal data.

Semantic cues and observed interactions motivate flow detectors. Example figures and the search application show utility, but the paper does not report a comprehensive precision/recall benchmark or a designer-productivity experiment. The viewer gives neighboring screens and navigation rather than validated exact flow boundaries. Coverage analysis on three apps demonstrates diminishing returns under that collection procedure; it cannot establish a universal optimal participant count. Possible usability testing, code regeneration, and large-scale streaming applications have different evidential status from the implemented repository.

## Micro-analysis 1: an architecture choice with two reasons

**PDF p. 3, ERICA / Design Choices / Web-Based Interaction Interface; opening “ERICA users interact with Android”.** Five sentences: **S1** states the mediated-access design; **S2** announces two reasons; **S3** explains remote crowdsourcing; **S4** details the reduced device/install requirements; **S5** supplies the server-compute rationale. Relation: **choice → reason structure → first reason → consequence → second reason**. Entry follows why humans drive exploration; exit argues that mediation can still resemble native use. This is an explicit design-rationale paragraph, not a result that participants preferred the web interface.

## Micro-analysis 2: scope of a coverage inference

**PDF p. 9, Discussion and Future Work; opening “Another way to improve the”.** Six sentences: **S1** proposes improving within-app coverage; **S2** suggests combining traces; **S3** describes the three-app comparison; **S4** interprets the observed plateau by analogy to heuristic evaluation; **S5** qualifies coverage for complex apps; **S6** proposes automated exploration for unvisited states. Relation: **goal → strategy → evidence → interpretation → boundary → complementary method**. Entry follows increasing the number of apps; exit moves to other design activities. Its two scale dimensions—more apps and deeper coverage—should remain separate. The analogy in S4 is a claim to scrutinize, not a reusable five-to-eight-user rule.

## Transfer and exception

Translate a literature gap into capture and coverage requirements. Explain what human participation contributes to a technical pipeline. Separate resource size, semantic validity, and downstream benefit. This paper demonstrates a requirements–infrastructure–resource–application argument that a fixed IMRaD template would flatten. Its strongest writing lesson is making each data representation useful to the next stage while keeping future applications from masquerading as evaluated outcomes.
