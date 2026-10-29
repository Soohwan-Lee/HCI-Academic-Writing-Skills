# P17 — ProtoAI

Hariharan Subramonyam, Colleen Seifert, and Eytan Adar. IUI 2021, pp. 48–58.
[Publication](https://doi.org/10.1145/3397481.3450640) · [Analyzed author PDF](https://cond.org/iui2021protoai.pdf).

## Selection and contribution

Selected as an IUI contrast to P04's evaluation-method critique: this paper proposes a
prototyping workflow, implements a tool, and evaluates designers' initial engagement.
Its primary knowledge object is a reusable design workflow embodied in a system.
The preliminary user study provides a warrant for feasibility and perceived utility;
its presence does not automatically create a separate general empirical contribution.
The [conference host's report](https://ieei.tamu.edu/26th-annual-acm-iui-conference-hosted-by-texas-am/)
identifies it as IUI 2021 Best Paper. The analyzed copy is an 11-page proceedings-layout
PDF, not the separately available 17-page manuscript-layout version.

## Observed structure

Introduction → related work → design considerations → model-informed prototyping → design
scenarios → preliminary evaluation → discussion/future work → conclusion. Related work
uses the design, test, and analysis phases as its organizing structure. Design considerations
precede the system narrative and supply five explicit requirements. The system is explained
through a recurring designer scenario, with features connected back to those requirements.
Three additional scenarios demonstrate possible application breadth. A designer study
then examines actual use. These are different forms of evidence and should remain distinct.

## Abstract and introduction flow

The abstract establishes the prototyping activity, explains AI-specific difficulty,
identifies tool fragmentation, proposes the workflow, describes the system's capabilities,
and reports preliminary designer engagement. It compresses solution and evaluation without
claiming a controlled productivity advantage.

The introduction (PDF pp. 1–2; proceedings pp. 48–49) first explains conventional
prototyping through a phone-unlock example. It shows how dynamic AI behavior complicates
this activity, identifies missing tool support, and develops the resulting practical
friction. A motivating design question precedes the proposed workflow. Guideline analysis
and derived needs lead to the approach; a concrete walkthrough shows what designers can
do before the closing contribution statement. This is a capability argument made legible
through an example, not an experimental introduction ending in statistical hypotheses.

## Related-work positioning

The opening of Section 2 distinguishes horizontal interface prototyping from vertical
access to AI behavior. Its three subsections organize previous work by the tasks a designer
must perform. Prior systems provide precedents and partial capabilities, while the present
system's relationship to them is stated locally. The section thus predicts the later
workflow instead of cataloguing adjacent algorithms. Section 3 separately reports an
analysis of design guidelines; it should not be mistaken for the same activity as the
selective positioning in Section 2.

## Two paragraph micro-analyses

**Introduction, proceedings p. 49, locator “AI-powered applications bring”.** S1 states
the general prototyping challenge; S2 explains sources of dynamic behavior; S3 derives
the need to connect user tasks and AI capabilities; S4 specifies interface adaptations;
S5 extends the obligation across users and contexts. Topic claim → mechanism → consequence
→ concrete requirements → scope. This is deductive development of a problem claim, not
a results-first paragraph. The previous paragraph demonstrates the limits of conventional
prototyping; the next tests current tools against the requirements just established.

**Related-work opening, proceedings p. 49, locator “The user interface design”.** S1 frames
design as a transformation; S2 characterizes existing tools; S3 contrasts AI-specific
requirements; S4 derives vertical prototyping; S5 locates ProtoAI in that space; S6 names
the workflow phases; S7 acknowledges existing tools sharing them; S8 announces the review
organization. Context → contrast → requirement → positioning → organizing framework →
roadmap. The paragraph begins with a conceptual premise, not its main novelty claim.
It follows the introduction's contributions and makes the upcoming three subsections
predictable. Its similarity acknowledgment keeps the distinction precise rather than
implying that every component of the workflow is unprecedented. Both boundaries were
checked against the rendered page.

## Claim, warrant, and limits

The implementation and walkthrough establish how model outputs, interface states,
data previews, and repairs connect. Section 5's illustrative scenarios demonstrate
possible uses; they are not field deployments. Section 6 reports a preliminary study with
ten designers, a supplied task/data setup, think-aloud activity, interview feedback,
and questionnaires. Observed designs and comments support initial usability and engagement
claims. Without a comparison condition or assessment of downstream end-user outcomes,
they do not establish superiority over commercial tools or improved fairness.

Discussion identifies unexamined data-generation needs, the early-stage scope, and failures
that designers may not detect through previews. It proposes later-stage usability testing,
additional collaboration, and educational support. The paper explicitly places comparative
evaluation in future work. A writing skill must preserve these limits even where the
introduction summarizes the tool confidently. The PDF extractor interleaves columns and
figure text in places; section ordering and selected paragraphs were checked visually,
so raw extraction order should not drive sentence-flow or word-share estimates.

## Transferable writing decisions

Maintain a traceable chain from guideline-derived need to feature to demonstrated use.
Introduce a recurring example early enough that later technical detail has a purpose.
Label scenarios and preliminary observations by their actual evidential status. Let the
contribution determine the section sequence rather than imposing a single IUI template.
These are single-analyst, version-specific observations, not general frequency estimates
or validated prescriptions for successful writing.
