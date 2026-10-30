# S07 — Methodological criteria, empirical audit and secondary screening artifact

Source: [P121 ethics/openness/transparency audit](../analyses/P121-ethics-transparency.md),
CHI 2023, institutional PDF. Re-read main hierarchy, criteria-development subsection
and screening-design subsection 2026-10-31. Prior full-text and visual review is
recorded in P121. This is a hybrid with three distinct knowledge/evidence objects.

## 1. Actual hierarchy

| Section | Subsections | Dependency |
|---|---|---|
| Introduction | Value definitions, tensions, evidence gap, promised outputs | Readers need to know what is being assessed |
| Related work | ethics; openness; transparency, subdivided into methods/results/data/artifacts | Supplies distinctions and criteria sources |
| Criteria, §§3–3.2 | development process; insights about access, terminology and screening potential | Makes the instrument independently inspectable before applying it |
| Method, §4 | samples; coding procedure; analysis | Explains the two-snapshot audit, not criterion construction again |
| Results, §5 | ethics; openness; transparency; reporting-practice changes | Applies the instrument to published-paper evidence |
| Screening tool, §6 | design considerations; implementation (PDF processing, similarity, classifier); evaluation | A secondary feasibility branch motivated by using many criteria |
| Discussion, §7 | surveys versus observed reporting; awareness; progress; students; limitations | Interprets audit findings and proposes changes in practice |
| Conclusion, §8 | Recap | Reconciles the distinct contributions |

Criteria construction is not hidden as a minor coding detail. Tool evaluation is
not the audit's data-generation method. Combining both under one Methods heading
would risk obscuring that the manual results precede the screening prototype.
The paper explicitly distinguishes these roles; its architecture makes them legible.

## 2. Complete paragraph map: §3.1 development, p.5

1. Identify inherited and newly operationalized criteria, who developed/refined
   them, the instructions produced, and later collaborative refinement.
2. Explain preregistration and changes in the criteria set, applicability to subsets,
   coverage across research phases, and locations of reusable material.
3. Explain why criteria have rationales and demonstrate their function using two
   examples. This connects an assessment rule to the reason someone should use it.

The sequence is construction → version/applicability → rationale and reuse. It
answers different questions from the later sampling/coding method. Moving all
rationale into an appendix would leave the instrument looking like an arbitrary list.

## 3. Complete paragraph map: tool branch opening and §6.1, pp.14–15

The opening first describes a possible author/reviewer workflow and human judgment,
then narrows to the implemented detection component and its preliminary evaluation.
This distinguishes a future application from the delivered technical work.

§6.1 has two paragraphs:

1. Explain heterogeneous applicability, trade-offs among criteria and multiple
   studies within papers; derive independent, local criterion evaluation.
2. Explain classification trade-offs through a degenerate perfect-specificity
   example, connect errors to reader workload, then justify a sensitivity priority
   with user-controlled narrowing of results.

The goals are derived from task/criterion properties. No formative interview is
needed or reported for this derivation. Implementation follows the resulting
requirements; it is not a list of libraries preceding any explanation of purpose.

## 4. Sentence-level maps

**§3.1 first paragraph, seven sentences:** inherited criteria → other sources →
operationalization by two authors → wider refinement → instruction production →
concrete instruction components/figure → continued refinement and forward reference.
The repeated criterion/instruction entities connect stages. The final reference
places subsequent procedural detail where it belongs instead of duplicating it.

**§6.1 first paragraph, five sentences:** variable applicability → trade-off among
criteria → risk of one aggregate score → multiple-study heterogeneity → design
consequence of independent sentence-level assessment. The conclusion comes last
because the preceding constraints earn it. Front-loading a generic “our tool is
flexible” claim would lose the specific reason for this representation choice.

## 5. Conditional transfer

When a method/instrument is a contribution, give its construction and rationale
space distinct from an application study. When an application motivates automation,
explain the actual branch: human workflow/requirements → implemented component →
component evidence. Do not present the imagined end-to-end workflow as evaluated.

This differs from a paper merely using a standard questionnaire: such a paper may
need only a concise measure description. It also differs from a primary system
paper where the artifact's capability organizes the entire narrative. Hybrid
organization should follow dependence among knowledge objects, not the order in
which authors happened to write code or collect data.
