# P20 — OmniTouch

**Source and coding.** Harrison, Benko, and Wilson, *OmniTouch: Wearable Multitouch Interaction Everywhere*, UIST 2011. Full author-hosted PDF: <https://chrisharrison.net/projects/omnitouch/omnitouch.pdf>. Single-analyst interpretive coding of this ten-page version; PDF pages below are one-based. The p.5 micro passage was visually inspected. No paragraph-length norm or award inference is made.

## Contribution and architecture

The primary object is an interaction/sensing artifact, with a quantitative feasibility characterization. Its order is **Introduction → Related Work → Hardware → Multitouch Finger Tracking → On-Demand Projected Interfaces → Example Applications → User Study → Results & Discussion → Future Work → Conclusion** (then acknowledgments/references). Hardware, algorithms, interface placement, and application demonstrations occupy distinct argumentative roles. The study does not replace these sections: it characterizes whether the infrastructure achieves usable touch detection and localization.

The abstract starts with the artifact and capability, then states the instrumentation boundary, expands the surface repertoire, explains input semantics, provides a concrete button-size constraint, and ends with an application vision (p.1). Thus, a useful limitation appears inside the sales pitch. The introduction instead moves from mobile computing's value to small-interface constraints, appropriable physical area, the sensing/wearability challenge, and the proposed system and tracking contribution. Formal numbered RQs and a contributions bullet list are absent. Questions become explicit when the user-study section needs operational criteria (p.7), rather than being mechanically placed in the introduction.

## Related-work reasoning

Related Work (p.2) groups neighboring approaches around the requirements they satisfy: projection placement, body-worn sensing, computer-vision tracking, and depth sensing. Comparisons repeatedly distinguish calibration, instrumentation, actual contact versus hovering, movable surfaces, and multitouch. This is a requirements-based contrast, not a chronological inventory. Prior work is not dismissed wholesale: each design supplies a capability that motivates the remaining combination. The writing makes the gap operational enough that later implementation and tests can answer it.

## Claim, support, warrant, boundary

The central claim is feasible touch-like interaction across everyday surfaces. Support comprises a working shoulder-mounted prototype, explicit tracking algorithms, diverse demonstration applications, and 12 participants performing controlled clicking and drawing tasks (pp.7–9). The warrant connects detected events and spatial precision to the interface element sizes required for reliable operation. This is stronger than counting demos alone because the system's error is translated into a design consequence.

However, the tests combine human and sensing error, use selected surfaces and right-handed participants, and compare some results with literature rather than a new concurrent touchscreen condition. The spatial analysis applies post-hoc offset corrections and removes stated outliers; reproduce these qualifications when carrying the numerical claims forward. A projected keyboard demonstrates implementability, not validated fast text entry. The desktop-tethered prototype and miniature wearable forecast also belong to different evidential levels. Future Work leaves social comfort and interpersonal body interaction as questions, not established acceptance findings.

## Paragraph micro-analysis

**p.5, On-Demand Projected Interfaces / One Size Fits All, paragraph opening “OmniTouch can use”.** Visually one paragraph, five sentences:

- **S1:** Establishes the baseline placement mechanism and its capability.
- **S2:** Introduces unknown surface extent as a constraint, deriving a conservative interface size.
- **S3:** Makes that consequence concrete on a large table.
- **S4:** Adds a separate centering limitation for asymmetric surfaces.
- **S5:** Converts the limitations into a reason to explore alternatives.

The relation is **baseline → causal constraint → example → additional cost → design transition**. It enters from a sentence announcing three placement approaches and exits into classification-driven placement. The paragraph's purpose is to make a design decision intelligible, not to deliver a standalone empirical finding. Repeated terms for surface/interface size maintain topical continuity; the final sentence creates demand for the next subsection.

## Transfer and exception

For technique papers, separate what is sensed, how interface behavior is composed, what applications become possible, and what has actually been measured. Translate technical accuracy into a user-facing constraint. Build related work from those same requirements. Conversely, do not force a generic methods/results split or interpret every application illustration as evaluation. This paper supports multiple placement options with local tradeoffs, demonstrating why an artifact narrative can need intermediate problem–solution cycles after the introduction.
