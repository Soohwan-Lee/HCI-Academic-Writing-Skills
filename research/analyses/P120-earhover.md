# P120 — EarHover: Mid-Air Gesture Recognition for Hearables Using Sound Leakage Signals

## Source and review scope
ACM-formatted author-lab copy, 13 pages; no version comparison. [Source](https://www.iplab.cs.tsukuba.ac.jp/paper/international/suzuki_uist2024.pdf); [publication DOI](https://doi.org/10.1145/3654777.3676367). Claude Opus 5.5 medium analyzed the full text via the existing Claude Code subscription. Root independently read the main text through page 11 and inspected rendered pages 3, 10, 11, including both micro-analysis passages. Other figures were consulted through captions and adjacent text. No independent human coding, numerical length measurement, or study replication is claimed. Reviewed 2026-10-30.

## Contribution contract
**Promise:** a new sensing technique that repurposes leaked playback for mid-air hearable input, plus an initial gesture set and feasibility evidence across two device forms.

**Method:** Doppler spectrograms, a CNN detection-classification cascade, gesture screening, a listening study, and offline detection and classification experiments.

**Form:** a UIST-style systems paper moving from problem to artifact, evaluation, and limitations.

The evidence supports feasibility with an added microphone and amplifier, external power, and user-specific classifiers. It does not establish deployment on commercial built-in hardware, despite the paper's practical framing.

## Section architecture
1 Introduction; 2 Related Work (2.1 Input with Hearables: 2.1.1 Hand Input, 2.1.2 Hands-Free Input; 2.2 Acoustic-Based Recognition); 3 EarHover (3.1 Device Insights; 3.2 System; 3.3 Gesture Detection Model: 3.3.1 Preprocessing and Spectrogram Image Generation, 3.3.2 Model Training; 3.4 Gesture Classification Model: 3.4.1 Data Augmentation, 3.4.2 Model Training); 4 Implementation; 5 Gesture Selection Experiment (5.1 Mid-Air Gesture Design; 5.2 Procedure; 5.3 Gesture Selection: 5.3.1 Doppler Shift Magnitude, 5.3.2 Doppler Shift Similarity, 5.3.3 Usability); 6 System Evaluation (6.1 Auditory Impact on User; 6.2 Gesture Detection Performance: 6.2.1 Experimental Setup, 6.2.2 Data Collection, 6.2.3 Detection Performance; 6.3 Gesture Classification Performance: 6.3.1 Classification Performance in Other Measurement Environments, 6.3.2 Five types of gesture classification performance); 7 Discussion (7.1 System Performance: 7.1.1 Gesture Detection Performance, 7.1.2 Gesture Classification Performance; 7.2 Limitations; 7.3 Future Works); 8 Conclusion; Acknowledgments; References [1-58].

## Abstract and introduction moves
The abstract moves from artifact to benefit, gap, mechanism, gesture filtering, and evaluation, but gives no results. The introduction narrows from hearable growth to control problems: voice has social and noise limits, while touch brings strain, noise, and hygiene problems. Mid-air input becomes the answer, and sensor cost becomes the gap. The system is then introduced, followed by separate results and contributions lists. That duplication lets performance figures appear before their conditions are explained.

## Related-work jobs
- **2.1.1** creates the opening by contrasting contact burdens with added-sensor burdens.
- **2.1.2** keeps hands-free input as a situational complement, not a rival to defeat.
- **2.2** establishes acoustic plausibility, then differentiates by challenge: leakage is attenuated and limited by safe volume, unlike a directly aimed signal.
- **Yang et al. [55]** forces a narrower novelty claim centered on air-conducted in-ear and open-ear devices.

## Evidence, warrant, and limits
- **Device fit:** A hand-movement demonstration warrants excluding canal devices. The 332-person survey reports usage, which supports a possible audience but not adoption intent.
- **Gesture set:** Eleven participants informed threshold-based filtering. The 27-to-7 reduction is arithmetically consistent, but the thresholds receive no justification and confusion was not tested directly.
- **Auditory impact:** Half of participants perceived a difference, and those participants showed no significant preference difference. 'Minimal' influence therefore outruns the evidence, because nonsignificance does not show equivalence.
- **Detection:** Models excluded the test user. Scripted activities and annotated gestures yielded false-detection rates of about 2% and 10%.
- **Classification:** Stable within-user F-scores were 79.7% and 85.9%. Without test-environment training data, means were 64.3% and 67.6%; with it, 86.3% and 86.8%. Leave-one-subject-out performance, about 48%, appears only in the Discussion.
- **Five-gesture result:** The 90.1% and 90.9% scores follow removals guided by observed confusion and are not independent validation. Music and video-call mappings remain conceptual illustrations, not tested capabilities.
- **Not reported:** real-time end-to-end recognition, latency, power use, or a field deployment.

## Findings-to-discussion transitions
The strongest transition converts error rates into asymmetric consequences: false activation is treated as disruptive and potentially unsafe, whereas a missed gesture costs repetition. Confusion between Twist variants becomes an explicit admission that the selection process was flawed. Weaker transitions turn untested mechanisms into explanations, including Neighbor hand proximity and feedback-related instability. These are interpretations, not measured causes.

## Paragraph micro-analyses
### 1. Page 3, section 2.1.1, paragraph beginning 'Touch gesture input, which requires contact' (6 sentences; boundaries clear)
1. Reasserts the contact burden as the alternative's weakness.
2. Frames prior mid-air sensing as costly and privacy-limited.
3. Presents EarHover's components as the resolution through compatibility and cost.
4. Concedes the closest prior principle.
5. Pivots to a device-class distinction.
6. Adds evaluation scope as further differentiation.

**Effect:** The paragraph builds a gap, then protects it from the nearest competitor. Sentence 3 claims more than the evaluated prototype supports, a tension the next subsection partly resolves by conceding that EarHover is not yet compatible with commercial hearables.

### 2. Page 11, section 7.1.2, paragraph beginning 'In this study, we evaluated gesture classification' (6 sentences; boundaries clear)
1. Identifies individual models as the evaluation basis.
2. Reveals the much lower cross-user result.
3. Offers a tentative explanation through user variation in execution and anatomy.
4. Reports that individual models remained stronger, without giving a value.
5. Shifts from limitation to a future training goal.
6. Proposes selecting similar data from other users and hedges the possible benefit.

**Effect:** The paragraph discloses a major generalization limit, yet converts it into a personalization agenda. The transparency is useful, but the position after the headline claims reduces its rhetorical force.

## Cross-paragraph connections
The introduction's 'low cost' claim is carried by the 2.1.1 gap paragraph, conditioned by the 2.2 compatibility concession and Section 4 hardware, then restated strongly in the Conclusion. The gesture path runs from 5.3.2's 0.60 threshold to Figure 14's confusion and 7.1.2's process critique. Likewise, individual-model headline results connect to the later cross-user limit. A reader must assemble these links to recover the actual claim boundary.

## Transferable lessons
- State the phenomenon, then explain how the artifact operationalizes it.
- Use the closest prior work to sharpen novelty instead of hiding it.
- Translate errors into interaction consequences.
- Admit when a selection procedure failed its downstream purpose.

## Counterexamples
- Do not write 'real-world' for scripted or synthesized conditions.
- Do not call a null preference test proof of minimal impact.
- Do not place a headline range ahead of its training assumptions.
- Do not reserve the key generalization limit for late Discussion.
- Do not let an unqualified 'first' exceed the novelty boundary defended in related work.

## Root integration review
Root visually verified both six-sentence micro-examples and the classification figures on page 10. The actual Figure 15 includes open-ear Neighbor TDA 89.3%; the introduction's 79.7–88.8% range is not an exhaustive range across those conditions. Stray overlapping extraction strings do not appear as additional results in the rendered figure and were excluded. Preserve F-score as the named metric rather than silently calling it accuracy. Detection excludes the held-out user, whereas the headline classification uses each user's own training data; those protocols must not be collapsed.

An external microphone, amplifier and power supply were used. Integration into ordinary commercial hardware and a deployed application remain future work. The no-significant-preference result is not an equivalence test, and half of participants perceived an audio difference. Cross-user classification around 48% is a material boundary. The narrower novelty distinction concerns air-conducted in-ear/open-ear devices; prior sound-leakage work is acknowledged. This analysis concerns writing and evidential scope, not an independent replication or acoustic-safety assessment.
