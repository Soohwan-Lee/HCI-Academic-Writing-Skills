# P82 — Zooids

**Provenance.** Le Goc, Kim, Parsaei, Fekete, Dragicevic, and Follmer, UIST 2016, DOI [10.1145/2984511.2984547](https://doi.org/10.1145/2984511.2984547). Full author-hosted manuscript from Stanford's Shape Lab, explicitly named `SwarmUIs_no_copyright.pdf`; this version retains an incomplete ISBN placeholder. Full substantive text read, two complete paragraphs rendered and visually checked. Single-analyst, version-dependent coding; award unverified. Selected for the separation of a platform, a proposed interface category, and design principles.

## Contribution and architecture

The primary objects are an open hardware/software platform and a conceptual definition of swarm interfaces. Technical implementation and scenarios substantiate these objects; they are not evidence of a general user-performance advantage.

Actual sequence: **Introduction → Background → Swarm UI Examples with Zooids → Zooids Hardware and Software Design → Swarm UIs: Design Principles and Challenges → Limitations and Future Work → Conclusion → Acknowledgments → References**. Background culminates in a definition of swarm interfaces. Examples precede engineering detail, while design principles follow both. The abstract similarly moves from interface class to platform, enumerates its components, then promises scenarios and design considerations rather than experiment results.

The introduction (pp. 1–2) invokes programmable-matter visions, identifies limits of actuated tangibles and shape displays, introduces the small robot, explains input/output possibilities, and lists contributions separately from benefits. This separation is useful: the reusable platform is a deliverable, whereas claims about physical manipulation and cost are properties that still require qualification.

## Related work and conceptual gap

Background compares tabletop tangibles, shape displays/programmed matter, swarm robotics, and data physicalization. Each contributes one part of the argument: synchronization, topology, collective actuation, or representational use. The proposed definition then makes membership criteria explicit—independence, self-propulsion, collective movement, and input responsiveness—and provides exclusions and ambiguous cases. The distinction from robotics concerns direct interaction and interface applications, not an assertion that collective motion is new. Its definition is a proposal for organizing research, not a discovered natural boundary.

## Claim–support–warrant–limit

Working drawing, visualization, and animation applications show how multiple small objects can act as representations and controls. Hardware dimensions, tracking resolution, communication testing, and controller descriptions support implementation feasibility. The warrant is that detached, mobile elements permit configurations and direct manipulations unavailable to a fixed pin array.

No controlled user-benefit evaluation is reported; comparative studies remain future work. “In-the-wild” scenarios are explicitly not implemented applications, so they must not be described as field deployments. Collision avoidance does not guarantee collision-free operation. Wheel geometry, tracking occlusion, ambient light, charging, cost, and flat-surface requirements constrain the generality of early claims about operating on arbitrary horizontal surfaces. The price at larger manufacturing scale is projected. A nuanced synthesis retains both useful design principles and unresolved engineering constraints.

## Micro-analysis 1: bounded algorithm rationale

**PDF p. 6, Hardware and Software Design / Software; opening “After the goal assignment step”.** Six sentences: **S1** states the motion-and-collision objective; **S2** selects HRVO for real-time planning; **S3** describes normal motion; **S4** explains the exceptional collision-response mechanism; **S5** qualifies the absence of guarantees while arguing its practical advantage; **S6** identifies the reused implementation. Relation: **requirement → choice → normal case → exception → bounded warrant → provenance**. Entry follows goal assignment; exit explains local PID execution. The paragraph makes the borrowed algorithm's role visible without falsely claiming its invention.

## Micro-analysis 2: when an optimization changes meaning

**PDF p. 8, Design Principles / Elements with an Identity vs. Interchangeable Elements; opening “One important distinction to be”.** Eight sentences: **S1** introduces the distinction; **S2** maps it to the prior things/stuff concepts; **S3** supplies a drawing example; **S4** explains the optimization benefit; **S5** gives a counterexample involving a graspable control; **S6** extends the risk to stable data identities; **S7** derives a design decision; **S8** states an implemented safeguard for manipulated elements. Relation: **distinction → examples → benefit → semantic cost → prescription → safeguard**. Entry follows physical persistence; exit turns to manipulation. The paragraph's principle emerges through contrasting cases rather than a claim followed by supporting citations.

## Transfer and exceptions

Define a new category using inclusions, exclusions, and border cases. Follow demonstrations with principles that explain why engineering decisions affect interaction meaning. Label scenarios, implementations, and future studies separately. This paper needs neither a conventional Results chapter nor invented RQs; its validation burden concerns an enabling platform and design repertoire. It does not license converting technical possibility into universal interaction superiority.
