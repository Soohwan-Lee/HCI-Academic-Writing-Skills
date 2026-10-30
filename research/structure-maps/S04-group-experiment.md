# S04 — Group experiment with designed conditions and exploratory interaction analysis

Source: [P103 LLM-powered Devil's Advocate](../analyses/P103-devils-advocate.md),
IUI 2024, 17-page published PDF. Re-read heading hierarchy, measurement/results
openings and discussion pp.8–14 on 2026-10-31. PDF pages differ from printed
pp.103–119. Prior visual paragraph inspection is recorded in P103. The source's
LLM conditions support an empirical comparison; their implementation does not
make this a system-first paper.

## 1. Actual hierarchy

| Section | Subsections | Why this organization matters |
|---|---|---|
| Introduction, pp.1–2 | Unnumbered paragraphs | Group decision stakes → reliance problem → dissent and its costs → LLM role → dimensions, study and contribution |
| Related work, pp.2–4 | group discussion → empirical AI-assisted decisions → LLM HCI | Supplies the social mechanism, outcome construct and candidate means |
| Study design, pp.4–8 | opening RQs → task → treatments → procedure → measurements | States questions after positioning, then makes the intervention and its observables recoverable |
| Results, pp.8–12 | overall comparison → two design factors → distribution-specific cases → process perceptions → exploratory deliberation analysis | Answers increasingly differentiated questions before examining interaction material |
| Discussion, pp.12–14 | interactive AI-target effects → limited majority-target effects → LLM collaboration challenges → limitations | Organizes around explanatory puzzles and implications, not a second listing of RQ answers |
| Conclusion, p.14 | Recap | Returns to the specific experiment and its mixed outcomes |

The five conditions belong inside Study Design's treatment explanation. There is
no required Design Goals or standalone System section. The four RQs appear at the
start of Study Design; their placement depends on the prior literature and concepts.
Recruitment phases are steps in one experiment, not two independently reported studies.

The results ordering is not simply “quantitative then qualitative”: it first moves
from a baseline contrast to factorial contrasts and conditional task cases, then
changes from group outcomes to individual perceptions, then investigates possible
interaction explanations. The latter is exploratory rather than a mediation test.

## 2. Complete local paragraph maps

### §4.1 overall comparison, PDF pp.8–9: two paragraphs

1. Define the comparison question, outcome models and reference condition; point
   to the coefficient figure. This lets readers interpret signs and comparisons.
2. Report the accuracy contrast, translate its meaning, then distinguish correct-
   and incorrect-AI reliance outcomes. The paragraph ends with a limit to what the
   intervention changed rather than presenting all metrics as the same success.

### §4.2 design factors, PDF p.9: two paragraphs

1. Restrict the analysis to four intervention conditions and identify the factors,
   outcomes and analysis. This makes the changed denominator/comparison explicit.
2. Walk through accuracy, factor interaction and the two reliance outcomes, then
   offer an interpretation. Marginal or non-significant findings should retain
   their uncertainty; the source's final implication is not a universal effect.

### §5.1 interpreting the interactive AI-target condition, PDF pp.12–13: three paragraphs

1. State the central outcome and develop an explanation involving amount and
   character of deliberation, drawing on logs. This changes from reporting to
   interpretation; the explanation was not isolated as a causal mediator.
2. Narrow by task distribution, consider information available to the advocate,
   and motivate future work. It qualifies the preceding general explanation.
3. Introduce the performance/experience puzzle, consider discord, abstract a
   design-goal tension and identify a research direction. This adds a different
   implication rather than repeating the first paragraph's performance claim.

### §5.2 majority-target condition, PDF p.13: two paragraphs

1. Present the limited-impact puzzle, connect it to authentic dissent literature,
   and propose an argument-quality explanation.
2. Offer a different confidence/climate explanation, relate it to discussion
   length, and propose design investigation. Keeping the explanations in separate
   paragraphs makes their different mechanisms inspectable.

## 3. Sentence-level maps

**§5.1 third paragraph, PDF p.13, six sentences:** objective/subjective performance
contrast → additional teamwork contrast → conjectured discord → why that conjecture
might be particularly relevant here → design-goal tension → future investigation.
The first two sentences establish a puzzle that the next two attempt to explain.
The fifth changes analytical level from condition-specific results to design goals.
The sixth follows from that tension. A rewrite that starts with a generic claim
about AI improving collaboration would erase the paragraph's purpose.

**§5.2 first paragraph, PDF p.13, four sentences:** unexpected limited effect →
possible inability to persuade the majority → prior distinction between assigned
advocacy and authentic dissent → proposed connection to LLM argument generation.
The paragraph is result → candidate account → conceptual precedent → application.
The final cross-human/LLM comparison must be checked for its actual evidence and
historical scope rather than adopted as a current universal capability claim.

## 4. Conditional transfer

Use task/treatments/procedure/measurement organization when the central product is
knowledge about intervention differences. Give implementation enough detail to
understand and reproduce the manipulated conditions; expand it into a separate
system section only if understanding the mechanism needs that space or the artifact
also has an independent capability contribution.

For group research, the outline must preserve levels of analysis. Group decisions,
individual ratings and conversation traces can have separate result subsections
and then meet in a discussion puzzle. That meeting is where the paper adds
interpretation; it should not silently turn traces into proof of a causal mechanism.

Compare S03: formative findings motivate building; here experimental outcomes
answer questions about alternatives. Compare S01: capability-specific studies warrant
an artifact; here the artifact configurations instantiate the comparison. The same
venue can contain all these forms.
