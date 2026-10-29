# Dataset, benchmark and reusable-resource writing

Use when the central knowledge product is something other researchers can reuse:
a dataset, benchmark, corpus, annotation scheme, design repository or comparable
resource. Public release alone does not establish a contribution. Explain **what
research becomes possible, how the resource was constructed, what it represents,
and what its evidence and use conditions permit**.

## Decide whether the resource is primary

Ask whether the resource's coverage, representation or reuse affordance supplies an
independent advance. A dataset released with an empirical paper can be a secondary
output, as in [P64, Typing](https://doi.org/10.1145/3173574.3174220). A dataset-first
paper must give construction and fitness for use enough space to support its own
claim. A collection pipeline may instead be the main artifact contribution; consult
[artifact](artifact.md) and [hybrids](hybrids.md).

Write a resource contract: intended users/tasks → unit of data → source population
or collection boundary → representation/annotations → supported uses → known gaps.
Keep coverage, scale, quality, representativeness and usefulness separate. Large
counts do not substitute for meaningful provenance or sampling.

## Section architecture

A useful sequence is research need and alternatives → resource requirements →
collection/construction → representation and quality checks → characterization →
example tasks/baselines → access, maintenance and limitations. Move tasks earlier
when they explain otherwise obscure representation choices. A benchmark additionally
needs task definitions, splits, metrics and evaluation protocol. A design repository
may foreground search and reuse workflows rather than model scores.

[P14, Rico](https://doi.org/10.1145/3126594.3126651) connects mobile-interface scale
to data-driven design applications. [P27, Webzeitgeist](https://doi.org/10.1145/2470654.2466420)
combines a platform and repository; the corpus is not a representative sample of
all web design. [P28, WebUI](https://doi.org/10.1145/3544548.3581158) distinguishes
resource/transfer utility from gains due to model architecture. These are different
ways to warrant reuse, not interchangeable evidence for universal generalization.

## Opening and positioning

In the abstract, state the research bottleneck, resource contents and scope,
construction approach, most informative quality/use evidence and access status.
Avoid using scale as the only result. In the introduction, explain which questions
existing resources cannot answer and why the new representation or coverage matters.
Related work should compare source domains, units, collection methods, annotation
semantics, licensing/access and supported tasks where relevant. A comparison table
is useful only if these attributes are verified and comparable.

A statement that a resource is “open” needs the actual access/license conditions.
Do not invent permission, perpetual hosting or future maintenance. Report what the
authors supplied, including restrictions and versioning. Current availability may
need verification separately from what the paper reported at publication.

## Construction and evidence

Explain selection, exclusions, duplicates, processing, annotation provenance and
quality checks. Define whether counts refer to people, applications, screens,
sessions, records or annotations. If only a subset receives detailed validation,
state its selection and denominator. Keep missingness and skew visible in the
characterization rather than burying them after reuse claims.

For benchmark results, explain the split and what independence it tests. Distinguish
within-source from cross-domain evaluation and held-out identities from random
records. Attribute gains to the tested intervention: new architecture, extra data,
pretraining, annotation or task formulation can be different factors. Illustrative
applications demonstrate possibility; they do not prove researcher productivity or
coverage across all intended use cases.

[P83, ERICA](https://doi.org/10.1145/2984511.2984581) distinguishes more applications
from deeper coverage within each application. Its three-app coverage comparison
does not establish a universal participant-count rule. This distinction helps a
resource discussion explain what expansion would actually improve.

## Paragraph and drafting example

A construction paragraph can use **coverage goal → collection choice → consequence
for included material → quality check → residual gap**. A use paragraph can use
**task enabled → representation consumed → observed result → transfer boundary**.
Where a resource is itself the product, enough concrete representation detail is
essential evidence, not an implementation appendix to remove automatically.

**Original hypothetical revision:** “Our diverse dataset generalizes to all group
interactions” becomes “The corpus contains discussions from the three recruited
settings. Its speaker and turn annotations support analysis of participation in
those settings; performance on other group types has not been assessed.” Add the
actual verified counts and distributions rather than filling in plausible numbers.

## Execute and review

Outline the use contract and construction chain. Draft the resource specification
and characterization before broad reuse claims. Revise every summary count against
its unit and subset. Compress repeated examples while protecting provenance,
annotation definitions, exclusions and use conditions. In `.tex`, keep schema
notation, tables and data-access links consistent. Ask whether a reader can identify
what is available, reconstruct its boundaries, choose an appropriate use and avoid
unsupported generalization.
