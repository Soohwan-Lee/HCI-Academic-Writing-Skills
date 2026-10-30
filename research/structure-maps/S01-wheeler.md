# S01 — Capability-led artifact with participatory refinement

Source: [P125 Wheeler](../analyses/P125-wheeler.md), UIST 2024, author PDF.
Structural re-reading: 2026-10-31. Main-text heading hierarchy recovered from the
PDF; §4 paragraphs re-read in layout extraction. Previously inspected page renders
are recorded in P125. Heading descriptions below are normalized/paraphrased. This
is an observed case, not the default structure of every UIST paper.

## 1. Actual hierarchy and dependency

| Section | Subsections in source order | Argumentative output |
|---|---|---|
| 1 Introduction, p.2 | No named subsections | Navigation cost → early artifact preview → predecessor limitation → capabilities and evidence |
| 2 Background/related work, pp.3–4 | 2.1 UI trees; 2.2 pointing devices (performance, comfort); 2.3 nonvisual adaptation; 2.4 rotary interaction; 2.5 mouse/virtual-cursor accommodations | Vocabulary, evaluation constructs and nearest capabilities needed to understand the mappings |
| 3 Overview, pp.4–6 | 3.1 hierarchical mode (keyboard comparison; deeper trees); 3.2 spatial mode (teleport variant); 3.3 switching modes | What the controls let a user do, before explaining how the device was developed |
| 4 Ideation, pp.6–8 | 4.1 three rotary inputs; 4.2 flat spatial navigation; 4.3 initial participatory design; 4.4 iterations | Different origins of mapping, form-factor and refinement decisions |
| 5 Implementation, pp.8–9 | 5.1 physical components; 5.2 electronics; 5.3 firmware | How the capability is realized across physical and software layers |
| 6 Evaluation, pp.9–14 | 6.1 participants; 6.2 shared procedure; 6.3 hierarchy study (design, specific procedure); 6.4 spatial study (design, specific procedure); 6.5 measured findings; 6.6 observations/subjective feedback | Separate warrants for the two capabilities, shared setup reported once |
| 6.5 Measured findings, pp.12–13 | hierarchy time; spatial target time; learning; movement trajectories | Outcome organization partly follows capability, partly repeated-use mechanism |
| 6.6 Observations, pp.13–14 | comfort; device design; relation between modes | Experience and redesign knowledge alongside performance |
| 7 Diary, p.14 | Situated use episodes rather than a second generic Results section | Insider longitudinal experience and contexts not covered by lab tasks |
| 8 Discussion, pp.14–16 | need; complementary role; productivity prospects; enabling prospects; VR; visualization; limitations/future work | Capability interpretation expands to prospective contexts and then explicit boundaries |
| 9 Conclusion, p.16 | No subsections | Recap of capability and evidence |

The source does **not** use formative study → design goals → system as its top-level
spine. It explains the finished interaction first, then reconstructs ideation.
The initial mapping is literature-informed; four participants refine embodiments.
A blind co-author contributes to iteration and later diary evidence. These are
connected roles but not interchangeable samples or independent validation stages.

Why this order works: readers can understand what a three-level control mapping is
before evaluating why three wheels and a particular enclosure were selected. An
alternative formative-first manuscript would need an early illustration or concise
capability preview to make those design choices intelligible.

## 2. Complete paragraph map of the ideation subsections

§4 has a two-sentence orientation: the design is informed by literature and the
section will explain that relationship. It changes the reader's question from
“how do I use this?” to “why is it like this?”

| Passage | Paragraph job | Relation to previous / handoff |
|---|---|---|
| §4.1 ¶1, p.6 | Explain tree navigation and the cost of moving between subtrees; derive independent traversal | Reuses §3's demonstrated action to name the problem that motivated it |
| §4.1 ¶2 | Credit rotary precedent, locate its residual cost, propose level-specific controls, justify three levels with application organization | Changes from problem to candidate mechanism and its coverage rationale |
| §4.1 ¶3 | Admit deeper hierarchies, consider another wheel, explain the rejected embodiment and retained allocation | Tests the preceding choice against a countercondition |
| §4.1 ¶4 | Explain wheel orientation through movement demands | Narrows from number/allocation to physical arrangement |
| §4.2 sole ¶, p.6 | Connect flat navigation and insider mouse-key experience to a second mode | Adds a complementary problem requiring another mapping, not another wheel-count rationale |
| §4.3 ¶1, p.8 | Establish participatory session, purpose and candidate embodiments | Moves from conceptual rationale to how the physical design was explored |
| §4.3 ¶2 | Compare participant responses, identify palm support, combine promising forms and explain a rejected alternative | Turns feedback into discriminating constraints rather than a preference list |
| §4.3 ¶3 | Resolve button placement and summarize the chosen embodiment | Closes a remaining component-level decision before iteration |
| §4.4 sole ¶, p.8 | Explain repeated refinement, insider involvement and return of the same four participants | Establishes process continuity and sends implementation detail to §5 / iteration detail to appendix |

This is a full map of these four selected subsections, not a full map of every
paragraph in the paper. It does not establish that this number of paragraphs is
optimal. The discussion subsections include prospects stronger than the direct
study evidence; P125 records those limits separately.

## 3. Sentence map — §4.3 second paragraph, p.8

Eight sentences: (1) state the elicitation action; (2) report an attractive form
and a simultaneous-control difficulty; (3) identify the preferred alternative and
its bodily affordance; (4) introduce missing palm support; (5) present a participant's
combination that addresses it; (6) introduce rejection of a touchpad alternative;
(7) explain the coordination difficulty; (8) connect that difficulty to conflict
with the intended independent-cursor mapping.

The chain is **elicitation → contrasted alternatives → unresolved constraint →
proposed combination → rejected alternative → interaction-level reason**. Devices
and fingers remain recognizable referents. Sentence 8 returns physical feedback to
the interaction concept introduced earlier. A generic “participants liked our
design” paragraph would erase the reasoning that makes the choice credible.

## 4. Sentence map — §4.4 sole paragraph, p.8

Four sentences: (1) state three major iterations; (2) identify insider involvement
and its role in smaller updates; (3) explain repeated consultation and continuity
with prior feedback; (4) direct the reader to the appendix. The paragraph allocates
process detail instead of repeating every iteration. It follows the initial-design
account and prepares the final implementation. Do not rewrite this as independent
validation or pretend the earlier concept came from these sessions.

## 5. Conditional transfer

For a capability-led artifact with multiple modes, one useful option is:
interaction overview → mode-specific rationale → embodiment refinement → layered
implementation → capability-specific evaluation → situated-use extension.

Choose it when the interaction must be legible before readers can assess rationale.
Choose a formative-first structure when the empirical discovery itself motivates
which capability should exist. A named Design Goals section is optional: goals
can be explicit within rationale paragraphs if their origins and consequences are
recoverable. The agent must select an ordering based on the manuscript's actual
research history and reader dependencies, not manufacture a formative study.
