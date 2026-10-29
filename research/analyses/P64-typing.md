# P64 — Observations on Typing from 136 Million Keystrokes

Dhakal, Feit, Kristensson and Oulasvirta, CHI 2018, Aalto University and University
of Cambridge. DOI 10.1145/3173574.3174220. [Author project PDF](https://userinterfaces.aalto.fi/136Mkeystrokes/resources/chi-18-analysis.pdf).
Full substantive text read; PDF pp. 3 and 8 rendered. Author-project Honorable
Mention evidence is recorded separately in metadata. Single-analyst writing coding.

## Contribution and architecture
The principal contribution is empirical characterization of modern typing, with a
released dataset and test code as reusable secondary outputs. An online collection
platform supports the evidence; implementing it is not by itself a system research
claim. The paper combines descriptive distributions, associations, comparisons and
exploratory clustering. Those operations answer different questions and must not
be compressed into a causal explanation of typing performance.

Order: Introduction → Background and Related Work → Data Collection → Preprocessing
and Data Analysis → Results → Keystroke-Level Clustering of Participants → Summary
(with implications and limitations/future work) → The 136M Keystrokes Dataset.
The main results contain subsections on performance, errors, hands, predictors and
rollover. Clustering receives its own methodological and interpretive sequence.
This accommodates a second analytical contribution without pretending that all
analyses share one inference procedure. The closing resource section makes reuse
concrete without replacing empirical interpretation with a download announcement.

The abstract states scale, previously supported findings, new associations, the
clustering result and availability. Introduction contrasts historical professional
typewriting with contemporary heterogeneous practice, recognizes small modern
studies, explains what larger data can address, previews analyses and enumerates
outputs. Related Work distinguishes historical evidence, modern keyboards, touch
input, measurement tasks and authentication. Each strand prepares a different
choice or use: transcription isolates aspects of motor performance; authentication
shows another potential use of keystroke patterns. It is a structured comparison of
contexts and assumptions, not a claim that scale alone creates novelty.

## Evidence, units and limits
The final analysis includes 168,960 volunteers and 136,857,600 keystrokes. People,
keystrokes and bigrams are not interchangeable sample units. The commercial typing
site's self-selected users skew young, U.S.-based and interested in typing; a large
sample does not establish population representativeness. Completion and exclusion
rules are explicit. Transcribing supplied English sentences also differs from
composing original text or everyday multilingual work.

The paper defines metrics, preprocessing, selected bigrams and grouping rules
before reporting patterns. Hand categories draw on an external motion dataset;
actual finger movements are not observed for every online participant. Detailed
error analysis uses 783 participants near cluster centers, not all 168,960. The
measurement precision caveat specifically challenges the smallest hand difference,
which is more informative than a generic limitations statement.

Clustering uses normalized inter-key intervals and an isolation criterion, without
external ground-truth typing categories. Its eight interpretable groups are an
exploratory representation, not proven natural classes. Associations between
rollover and speed do not show that training rollover will improve performance.
The discussion's personalized-training proposals therefore remain hypotheses.
Some captions and interpretive sentences use stronger causal language than the
observational design warrants. Historical test terminology is also inconsistent
between a table caption and prose; this is not a statistical-method template.
Useful writing features and inferential weaknesses coexist in the same exemplar.

## Micro-analysis A: specify who a large sample represents
PDF p. 3, Sampling and Participants, locator “Table 1 summarises”. Six sentences. S1 identifies the final sample and completion
requirements. S2 compares its demographics to the recruiting company's user base.
S3 adds training history. S4 states the population actually represented. S5 gives
start/completion attrition. S6 states the subsequent exclusion percentage and points
to the procedure. Flow: **sample identification → recruitment context → experience
→ scope → attrition → exclusion bridge**. The previous paragraph explains recruitment;
the next subsection describes the task. The large number is immediately accompanied
by selection information, not left to imply universal coverage.

## Micro-analysis B: declare an exploratory analytical warrant
PDF p. 8, Clustering opening, locator “Our goal is to summarise”. Five sentences.
S1 states the analytical purpose. S2 defines clustering in the chosen feature space.
S3 identifies absent ground truth. S4 explains the exploratory use and separation
criterion. S5 supplies interpretability as a further criterion. Flow: **purpose →
operation → validation limit → available criterion → interpretation requirement**.
The preceding paragraph motivates looking for shared strategies; the following
reports the eight-group result. The limit is part of the method's justification,
not an afterthought following an apparently definitive taxonomy.

## Transfer and exception
For large observational papers, connect scale to specific analytical affordances
while keeping recruitment, exclusions, proxy measures and subsample denominators
visible. Give an exploratory analysis its own question and criterion. Distinguish
empirical associations, proposed explanations, prospective interventions and
released resources. A confirmatory experiment or a dataset-first paper would need
a different emphasis; neither should inherit this paper's entire section order.
