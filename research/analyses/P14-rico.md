# P14 — Rico

**Source:** Deka, Huang, Franzen, Hibschman, Afergan, Li, Nichols, and Kumar, UIST 2017, [DOI](https://doi.org/10.1145/3126594.3126651), [author-hosted full text](https://ranjithakumar.net/resources/rico.pdf). The analyzed PDF is a 10-page author-hosted proceedings-format version. Affiliations stated in it are University of Illinois at Urbana-Champaign, Northwestern University, and Google Inc. Award status remains unverified; inclusion does not imply an award.

**Contribution coding:** primary knowledge object: dataset/resource. Supporting objects: data-collection infrastructure, UI-state similarity heuristic, and example downstream application. These are related but have different evidential obligations. Calling this only a system paper would obscure its intended reusable resource.

**Evidence status:** single-analyst interpretation of the downloaded full text. PDF pp. 1 and 7 were visually inspected. Page numbers refer to the analyzed PDF. On p. 7, default text extraction inserts a later-column example and future-work heading before completing the embedding subsection; visual reading order governs the analysis. No statistical writing norm or user-benefit claim is inferred.

## Section architecture

The main sequence is introduction → Android app datasets → data-driven design applications → mining app designs → the Rico dataset → future work. Acknowledgments and references follow; a full-page retrieval figure appears after references begin because of figure placement. There is no separately titled conclusion, related-work section, or all-purpose results section.

The dataset-comparison section performs related-work positioning. The application section supplies requirements for the resource. Mining explains how collection works and contains the coverage comparison. The resource section reports composition, collection, organization, and a learned representation. This arrangement makes the chain **intended reuse → necessary data → collection mechanism → resulting resource → demonstrated use** inspectable. It should not be flattened into a conventional experiment template.

## Abstract and introduction

The abstract (p. 1) moves from the value of data-driven design to the named resource and intended applications, then collection approach, scale, exposed data properties, and a concrete learned-embedding demonstration. The size numbers characterize a deliverable. They are not experimental effects or sufficient evidence of quality by themselves.

The introduction (pp. 1–2) comprises four main prose paragraphs. The first establishes the promise of data-driven design and ends with the prerequisite of suitable datasets. The second presents Rico and identifies intended application classes. The third summarizes the hybrid collection pipeline and its relationship to ERICA. The fourth describes resource contents and the layout embedding. The contribution is legible through the object and its properties without a numbered contribution list or numbered RQs. The explicit comparison with existing datasets is developed immediately afterward, rather than completing a long prior-work survey before introducing the resource.

## Related-work positioning and paragraph bridges

The dataset section (p. 2, Figure 2) distinguishes app-store metadata, software/security information, and design data. It then explains how screenshots, hierarchies, and interaction traces expose different aspects of design. Static versus dynamic mining becomes a consequential comparison because runtime behavior determines which information is obtainable. ERICA is treated as the closest predecessor: Rico inherits its dynamic approach while expanding scale, aggregation into unique UIs, and layout representations. Thus the novelty claim is not simply “a larger dataset.”

The application section (pp. 2–3, Figure 3) connects each downstream task to specific fields or representations. Literature from other design domains motivates a use case, followed by what Rico exposes to support it. These bridges keep citations tied to resource requirements. However, intended applications remain distinct from evaluated applications: the paper does not empirically validate every proposed use case.

## Evidence, warrant, and scope

Three layers support the contribution. First, collection and composition details establish what the resource contains and how it was obtained (pp. 5–6). Second, comparison against human-only and automated-only exploration supports the hybrid collection mechanism (p. 5, Figure 8). Third, training an embedding and showing retrieved neighbors provides a downstream feasibility demonstration (pp. 7–8, Figures 11–12).

The coverage measure is the number of unique UIs under the paper's similarity heuristic, rather than a known fraction of all possible app states. The heuristic itself has separately reported error rates on labeled UI pairs. Consequently, better observed coverage does not mean exhaustive or error-free app coverage. Retrieval examples demonstrate plausible layout organization, not a comprehensive retrieval benchmark or a designer study. The corpus is limited to collected free Android apps, excludes specified app categories, and reflects a historical snapshot. App ratings are proposed as proxies for design quality; they should not be promoted to validated measures of usability. Future work explicitly identifies obsolescence and sustainable collection as concerns. The manuscript's promised hosting period is historical, not a verified present-day availability guarantee.

## Paragraph micro-analysis A: creating a resource requirement

**Locator:** introduction, p. 1, first paragraph; opening “Data-driven models of design can”. Four sentences:

| Sentence | Rhetorical role | Connection |
|---|---|---|
| S1 | States the general capability that motivates the paper. | Topic-setting claim. |
| S2 | Grounds one immediate benefit in example-based design practice and citations. | Elaboration with support. |
| S3 | Extends the ambition to prospective prediction and personalization. | Future-facing expansion, not a reported result. |
| S4 | States the data prerequisite for building such models. | Dependency that motivates the next paragraph. |

The paragraph moves **capability → established use → prospective ambition → enabling requirement**. It begins deductively, but its final sentence carries the crucial transition: the next paragraph names the resource that addresses that prerequisite. A revision that retained the first sentence but deleted the final dependency would weaken the argument despite preserving a topic sentence.

## Paragraph micro-analysis B: limitation to maintenance agenda

**Locator:** future work, p. 7, second paragraph; opening “Unlike static research datasets”. Three sentences:

| Sentence | Rhetorical role | Connection |
|---|---|---|
| S1 | Identifies temporal decay if new apps are not collected. | Contrast that introduces a durability limitation. |
| S2 | Converts that limitation into a sustainability research need. | Explicit consequence. |
| S3 | Offers community-contributed traces as one candidate approach. | Bounded proposal, not demonstrated resolution. |

The preceding paragraph proposes richer annotations; this one changes the axis from informational richness to continued relevance. The following access statement directs readers to the resource. Its useful pattern is **failure condition → maintenance obligation → possible mechanism**, not a generic list of future features.

## Transfer and counterexample

A resource paper should make units, fields, provenance, coverage, errors, access, and intended reuse legible. Validation may combine construction checks and bounded downstream demonstrations, each attached to its own claim. Rico supplies a concrete alternative to a universal section recipe. It also shows why a celebrated or widely used resource should not make every historical assertion in its paper a current best practice.
