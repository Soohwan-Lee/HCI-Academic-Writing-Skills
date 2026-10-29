# P60 — Explaining Models

Dodge, Liao, Zhang, Bellamy and Dugan, IUI 2019; Oregon State University and IBM
Research. [Author PDF](https://qveraliao.com/iui19.pdf), DOI
10.1145/3301275.3302310. Full eleven-page paper read; PDF pp. 3 and 9 visually
checked. Award remains unverified in this record. Historical legal statements in
the introduction are not transferred as current legal guidance.

## Contribution and architecture
The central object is empirical knowledge about fairness judgments under different
explanation conditions. An implemented prediction/explanation pipeline supplies
controlled materials; it is not automatically the paper's artifact contribution.
The paper distinguishes perceived fairness from a prescriptively defined fairness
criterion. That distinction is necessary to understand what the study measures.

Order: Introduction → Background → Study Overview (questions, use case, explanation
styles, fairness issues, individual factors) → System Overview → Methodology →
Quantitative Results → Qualitative Results → Discussion → Conclusion. The study
overview establishes constructs before implementation explains how manipulations
are realized. Quantitative results address patterns and differences; qualitative
results examine reasoning and explanation-specific responses. Discussion combines
these into possible design directions. The architecture is more precise than a
single methods section that mixes construct selection, stimulus generation and
participant procedure without signposts.

The abstract moves from human scrutiny of fairness to explanation needs, study,
three findings and implications. Introduction builds societal stakes, the need for
human judgment, opacity and explanation research, then states the study's nuanced
scope. Formal RQs occur in Study Overview, after Background, not at a mandatory
position in Introduction. Background connects normative fairness methods with
descriptive judgments, then explanation taxonomies and individual differences.
The closest predecessor's hypothetical/incommensurate explanations motivate
comparable model-generated stimuli. This is a gap that directly shapes design.

## Evidence and caution
The authors use raw versus processed data, four explanation styles and cases with
or without a specified disparity. The system section reports construction and
oversampling decisions; the participant section reports an online experiment with
160 crowdworkers. Analyzed ratings concern the supplied predictions. They do not
establish what judges would do or whether a criminal-justice system is fair.
Open responses support interpretations of ratings, not independent causal tests
of the proposed psychological mechanisms.

The paper reports an initially nonsignificant three-way interaction, followed by
exploration of individual factors and model reduction. It also uses a marginal-
significance category and stronger summary language. A writing skill should retain
model sequence and uncertainty rather than imitate that rhetoric as a best practice.
Traits described as prior positions were measured after tasks; do not silently
rewrite them as a pre-exposure baseline or randomized influence. The abstract's
rounded recruitment description should not override the explicit methods count.
Personalized/hybrid explanations are proposed implications, not tested interfaces.
This exemplar is useful partly because careful editing must distinguish its
valuable argument structure from statements that require more qualification.

## Micro-analysis A: explain why a scenario is a probe
PDF p. 3, §3.1 second paragraph, locator “We chose a criminal”. Four sentences.
S1 justifies the domain's ability to elicit meaningful judgments. S2 disclaims a
study of the system's actual professional users. S3 restates the scenario's role
as an empirical probe. S4 cites precedent for that role. Flow: **selection rationale
→ population boundary → inferential purpose → methodological precedent**. The
previous paragraph describes the dataset; the next subsection defines explanation
conditions. The boundary appears where the domain is chosen rather than being
reserved for a final limitations paragraph.

## Micro-analysis B: evidence to a proposed workflow
PDF p. 9, §8.1 second paragraph, locator “Our results highlight”. Three sentences.
S1 states the design need inferred from differing judgment needs. S2 connects
local/global explanation patterns to that need. S3 proposes combining them in
a workflow. Flow: **implication → empirical rationale → possible design response**.
The preceding paragraph integrates quantitative and qualitative findings; the next
extends to fine-grained sampling. A writer must keep the last sentence prospective:
the observed comparison does not validate the combined workflow.

## Transfer and exception
Separate construct rationale, stimulus implementation and participant procedure
when their dependencies would otherwise be hard to follow. Connect mixed evidence
at the level of the question answered, while preserving disagreement and uncertainty.
Make an exploratory follow-up visible rather than rewriting it as a prior hypothesis.
Do not treat every quantitative paper as this architecture: a single manipulation
may need a much shorter setup, and qualitative inquiry may require a different
account of how interpretation is warranted.
