# P108 — HapticCap

## Source and status

Hu, Hershcovich, and Seifi, *Findings of EMNLP* 2025, pp. 14473–14489, DOI [10.18653/v1/2025.findings-emnlp.781](https://doi.org/10.18653/v1/2025.findings-emnlp.781). The [official ACL record and PDF](https://aclanthology.org/2025.findings-emnlp.781/) establish identity and proceedings version. Read the complete main text and appendices A–C; visually inspected both complete micro-analysis paragraphs. Awards are unverified. This is a **supplementary cross-venue resource exemplar**, not CHI, CSCW, UIST, DIS, or IUI evidence. Coding is single-analyst and version-dependent.

## Contribution and architecture

The conclusion expressly locates the primary contribution in the dataset and task; contrastive learning supplies an established feasibility baseline. This is a strong example of a resource claim that does not require pretending to invent its evaluation algorithm. HapticCap links vibration signals to sensory, emotional, and associative descriptions. Controlled laboratory elicitation is the collection method, not a separate claim of discovering universal haptic experience.

Actual sequence: Abstract; 1 Introduction; 2 Related Work (haptic experience, touch datasets, multimodal captioning); 3 HapticCap Dataset (signal sources, descriptions, validation/diversity); 4 Retrieval Task (formalization, encoders, contrastive framework); 5 Experiments; 6 Results; unnumbered Conclusion, Limitations, Ethical Considerations, Acknowledgement; references; appendices on experiments, dataset analysis, collection/compensation. The paper distinguishes resource construction from benchmark formalization before reporting model performance.

## Framing and related-work argument

The abstract moves from meaningful haptic design to two obstacles, introduces the dataset, defines retrieval, reports the strongest model pairing, and provides access. The introduction (§1, pp. 14473–14474) moves through application relevance, underrepresented vibration–language relations, descriptive dimensions, and collection difficulty. It then motivates retrieval instead of generation under data scarcity. This feasibility constraint is part of the problem formulation, not a generic future-work apology.

Related work differentiates superficially similar resources by **physical signal, perceiver, and annotation provenance**. Tactile-image corpora for robot perception do not directly solve vibration description for people. Haptic experience research motivates the vocabulary dimensions; multimodal captioning locates the computational task. These comparisons create a resource need more precisely than simply counting existing datasets.

## Claim–support–warrant and limitations

The resource account traces 304 initial signals, generated variations, laboratory descriptions, validation, and agreement-based subsets. The expanded 2,736-signal corpus should not be described as 2,736 independently elicited original stimuli: signal generation is part of its provenance. Signal-wise train/test separation supports a benchmark claim, although independent validation of the released implementation was outside this reading.

Results support feasibility under the stated retrieval setup, not practical benefit in accessibility or human–robot interaction. Agreement filtering improves measured performance but also changes which subjective descriptions remain. Minority experiences should not automatically be treated as errors in a different research contract. Limitations address English-only descriptions, collection in Denmark and the United States, overlapping description categories, and limited algorithmic novelty. These restrictions clarify appropriate reuse rather than negate the resource contribution.

## Two rendered paragraph analyses

**p. 14475, §2.2, opening “Touch is one” (eight sentences).** S1 supplies a broad sensory frame. S2 characterizes prior tactile-image datasets. S3 identifies captured properties and partly automated annotation. S4 states their robot-perception use. S5 contrasts human-perceived vibration signals. S6 explains their temporal physical difference. S7 specifies human annotation and three description dimensions. S8 closes with the intended human-facing use. The preceding subsection establishes experiential vocabulary; the next shifts to captioning models. The paragraph develops its differentiating claim late: a topic opening is not necessarily a conclusion-first opening. For expert readers, its broad first sentence may be dispensable; observed style is not automatically advice.

**p. 14481, Conclusion, opening “In this paper” (eight sentences, crossing columns).** S1 restates the task; S2 introduces its dataset support. S3 explicitly identifies primary novelty. S4 summarizes benchmark evidence. S5 justifies using an established method in an emerging domain. S6 acknowledges task difficulty. S7 positions the resource as a future baseline. S8 separates ongoing generative work from the present result. The preceding results explain encoder performance; the following limitations narrow interpretation. The sequence protects the contribution contract instead of inflating algorithmic novelty.

## Transfer conditions

For dataset papers, distinguish elicited originals, derived examples, annotation, filtering, and evaluation units. State exactly what reuse is enabled and where the baseline's novelty ends. Keep representation choices visible: optimizing agreement is not a neutral replacement for studying variation. This supplementary paper calibrates resource writing; its NLP section conventions are not universal HCI requirements.
