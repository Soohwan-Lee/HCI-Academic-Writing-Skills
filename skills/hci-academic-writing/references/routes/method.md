# Method, instrument and evaluation-framework writing

Use when the contribution changes **how researchers or practitioners conduct an
inquiry, measurement, analysis or design activity**. Distinguish using a method from
contributing one. A novel application, a toolkit implementation and a validated
measurement instrument have different knowledge claims even when all include code.

## Define the methodological advance

Identify the prior practice, its consequential limitation, the proposed change,
the assumptions under which it works, and the evidence for its usefulness or
validity. Ask what a reader could do differently after reading the paper. Specify
whether the output is a procedure, measurement scale, analytical technique,
evaluation framework, design guideline set or invitation to a research approach.

The warrant depends on the claim. An instrument may need evidence about the
constructs it measures; an algorithmic procedure may need correctness/performance
arguments; a framework synthesized from practice needs transparent derivation and
application boundaries. Do not attach a generic “user study” to all of them.
[P12, Evaluation Strategies for HCI Toolkit Research](https://doi.org/10.1145/3173574.3173610)
organizes evaluation options around the knowledge a toolkit claims. [P09, Time for
Historicism](https://doi.org/10.1145/3479603) is a methodological invitation supported
through argument and examples, not a validated scale.

## Adapt the section spine

A procedural method can use motivation/nearest approaches → requirements and
assumptions → procedure with worked example → validation → application guidance
and limits. A synthesis-derived framework can use problem → scope/derivation →
framework → demonstrations or assessment → discussion. A conceptual methodological
proposal may develop an argument and objections throughout instead of presenting
an empirical Results section.

A practice-refined method can describe selected applications before deriving
cross-case lessons. Explain what changed from the earlier method and which failed
assumption or encounter motivated it. [P77, User Enactments](https://doi.org/10.1145/2317956.2318008)
abandons its original matrix after emergent issues challenged it: refinement is
the advance, not reinvention. Its provocations reveal experiences without necessarily
endorsing the eliciting product concept.

Keep derivation, specification and validation distinguishable. A reader needs to
know where a rule came from, how to apply it and what evidence supports it. In
[P08, Guidelines for Human-AI Interaction](https://doi.org/10.1145/3290605.3300233),
iteration and evaluation are part of the account; do not reduce the contribution
to an unsupported list of recommendations. [P58, Aligned Rank Transform](https://doi.org/10.1145/1978942.1978963)
provides an accessible procedure and worked reanalyses. Its historical statistical
choices are not blanket current advice: verify relevant assumptions and current
methodological documentation before advising a particular analysis.

## Abstract, introduction and related work

The abstract should identify the methodological problem, proposed operation,
validation/argument and supported benefit. A concise statement of scope is more
useful than claiming the method is universally rigorous or easy. In the introduction,
show what existing practice prevents readers from learning or doing, not simply
that tools are inconvenient. Explain the consequence of the limitation and what
your method changes.

Related work should distinguish competing assumptions, intended outputs, evidence
requirements and practical constraints. Compare like with like: a method aiming to
interpret experience is not deficient because it does not estimate a population
prevalence. When adapting a method from another field, credit its origin and state
the substantive modification. Specify what is inherited, generalized, operationalized
or newly supported rather than claiming the entire procedure is invented here.

## Explain and evaluate the method

Use a small worked example to show inputs, decisions, intermediate representations
and outputs. Include failure conditions and ambiguous cases where they determine
correct use. Keep implementation instructions separate from the conceptual reason
for each operation, but connect them where an arbitrary-looking step needs a warrant.
A diagram can expose dependencies that a list of steps hides.

Validation should test the claim being made. Reproducing known cases tests something
different from outperforming a comparator, transferring across contexts, or enabling
novices to apply a method. Make those distinctions visible. If the method is a
proposal with illustrative applications, say so and explain why the illustrations
are informative. Avoid “validated” without naming what was examined and what
remains uncertain.

## Paragraph logic and an original illustration

A method-rationale paragraph can progress **goal → obstacle → operation → reason
it addresses the obstacle → remaining assumption**. A validation paragraph can
progress **property tested → evidence → interpretation → scope**. P58's worked
reanalysis connects a reproducibility task to intermediate checks; P12 connects
an evaluation strategy to the kind of toolkit claim it can support. These examples
illustrate reasoning, not a universal requirement to use their procedures.

**Hypothetical revision:** “Our coding framework ensures reliable assessment of
collaboration” becomes “The framework distinguishes turn-taking, uptake and
resolution in the analyzed transcripts. The worked examples show how the categories
can be applied; they do not establish independent coding consistency or predict
collaboration quality.” Replace the illustrative categories and evidence with the
actual manuscript's material.

## Workflow and review

Outline the change in practice and the evidence chain. Draft the specification and
worked example before writing a broad benefit claim. Revise each guideline or step
against its derivation and intended use. Compress repeated rationale while retaining
assumptions and decision rules. For an existing `.tex` project, preserve notation
and cross-references between steps, algorithms and examples.

Check that using the proposed method is possible from the description; that the
validation matches the promise; that inherited ideas are credited; and that
limitations help readers decide when not to apply it. Do not convert a corpus's
most common method into the recommended method merely because it is common.

## Reporting audits and metaresearch hybrids

When publications serve as data, separate the reusable assessment criteria from
findings about a sampled research community. [P121, Research Ethics, Openness and
Transparency](https://doi.org/10.1145/3544548.3580848) specifies criteria, applies a
manual audit and then examines a screening prototype. Keep these claims
separate: a screening tool evaluated against manual labels inherits their limits.
Its performance does not validate the manual audit, and manual
coding does not establish the tool's usefulness in researchers' actual workflows.

State whether a criterion concerns disclosure, availability, conduct or correctness.
If any study meeting a criterion makes its paper count as meeting it, explain that
aggregation before comparing percentages. Retain applicability denominators and
unassessable or noncomparable items. Changes across publication years may reflect reporting space,
access time, methodological composition and sampling as well as practice. A confidence interval crossing zero
is not proof of negligible change. Do not treat transparent qualitative inquiry as
requiring an invisible researcher; interview-focused criteria may also miss other
interpretive analysis materials. Report n/N_applicable and the aggregation unit
where applicability differs. Pair this with the [review route](review.md) when
the contribution includes a synthesis of publication practices.
