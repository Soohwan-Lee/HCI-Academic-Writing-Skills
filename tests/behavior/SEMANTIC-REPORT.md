# Evidence-sensitive generation trials

Observed 2026-10-30 with Claude Code subscription authentication (`claude.ai`, Pro),
runtime `claude-opus-5-5`. These are development cases and two small held-out prompts,
not a writing benchmark or independent human evaluation. The model received selected
skill instructions and task text without expected checks. Tool-free calls could not
inspect or edit a manuscript. AI evaluator inspection assessed meaning; full transcripts
remain private. CLI-reported price estimates are not evidence of API billing.

## Iteration and observed outcomes

The six [development cases](semantic-cases.json) cover RtD, reviewer responses,
unsupported corpus frequencies, group-level inference, review units and pre-results
drafting. The historical corpus-count prompt deliberately describes its own smaller
measurement snapshot; it is test input, not the current repository's status.

| Case | Initial outcome | Revision / final observed limitation |
|---|---|---|
| RtD | Produced design insight and bounded reflection without inventing a participant experiment | No comparative effectiveness claim; one small case only |
| Corpus frequency | Declined an unsupported percentage and still revised the sentence | No empirical frequency inferred from corpus size |
| Group unit | Flagged group/individual inference mismatch without inventing reanalysis | Statistical correction still needs actual data/analysis |
| Reviewer response | Claimed edits already completed in a tool-free task | Prospective wording improved, but final proposed claim still said use “throughout” the period when only use “during” it was supplied |
| Review counts | Corrected publication/study counts but supplied unverified coding detail | Final response avoided systematic/meta-analysis labels but still asserted coding each study rather than preserving uncertainty about coding unit |
| Pre-results | Some wording implied an existing study; a later draft supplied semi-structured interviews | Final draft kept interviews planned and omitted the format, but still asserted “little is known” without supplied literature evidence |

After the first pass, instructions were strengthened about prospective revisions,
planned studies, review terminology, whole-proposition evidence gaps and familiar
methodological defaults. Three difficult cases were rerun twice. We do not report
a pass rate: revised prompts, repeated cases and qualitative judgments are not an
independent comparable test set. Notes saying “verify this” did not repair unsupported
assertions already present in visible prose; these remain failures.

Two [held-out prompts](heldout-cases.json), introduced for the last round, produced
bounded descriptive-review wording and a prospective ten-day pilot response without
claiming all nine recruited people used the system. This small success does not
erase the persistent failures above or establish generalization.

## Practical implication

Use the skill to help structure and revise supported material. Check every newly
introduced method, quantifier, temporal claim and research-gap statement against
source evidence, especially in generative drafting. “During” and “throughout,” or
“publications” and “studies,” can change the claim while retaining fluent prose.
An instruction-only guard is insufficient. A finished-looking abstract requires
researcher review; the package does not guarantee hallucination-free text.

Separate [live file-edit trials](README.md) test installed-file loading and actual
ACM edits. Both succeeded on supplied evidence, preserved unrelated files, and
compiled, but there was no no-skill control and no human author-usage study.

## E02: comparison scope and interpretive warrants

Four [synthetic cases](e02-cases.json) were run once with Claude Opus 5.5 medium
(subscription), supplied the four revised reference modules, with tools disabled.
Root reviewed outputs before integrating the subsequent critique. This is not a
full installed-skill test, independent benchmark or measured improvement.

| Case | Observed response | Root assessment |
|---|---|---|
| E02-Q | Retained within-task randomization and declined an equal novice/expert effect claim | Supported; no interaction/equivalence analysis invented |
| E02-S | Preserved external microphone/amplifier, within-user versus held-out-user F-score and offline scope | Supported; did not call F-score accuracy or claim deployment |
| E02-P | Wrote a qualitative explanatory contribution with configurations and supplied case reasoning | Supported facts, but unnecessary negative contrasts burdened the short contribution sentence |
| E02-C | Credited antecedent concepts and separated scenario work from deployment | Kept effect limits, but “framework remains formative” unnecessarily weakened the conceptual output |

Root's editorial repairs for the last two are a direct contribution sentence naming
the account and its material, and a conceptual-extension sentence followed by a
separate statement that effects were not evaluated. The final sociotechnical module
now explicitly distinguishes conceptual validity from deployment evidence. These
repairs were not rerun; no all-cases-pass claim is made.

A separate Opus critique identified camera-as-ground-truth implications, generic
bias-removal language, misplaced headings, missing locators and overly rigid claim
compression. Root accepted these concerns, checked source sections and revised the
modules. Qualitative interpretation is assessed within its analytical tradition;
research relationships can constitute the material rather than merely contaminate it.

## E03 — review and metaresearch probes, 2026-10-30
Four supplied-context prose cases in `e03-cases.json`, one Claude subscription
request, runtime `claude-opus-5-5`, medium effort. No tools, installation discovery,
LaTeX mutation or compilation exercised. Root reviewed the actual responses.

- R1 preserved 1,000 records versus 40 papers, category overlap and conceptual
  value. Its causal disclaimer tied the limitation too directly to absence of
  longitudinal data; the actual inferential design matters. Root added that rule.
- R2 distinguished the nearby review's analytical object and avoided an absence
  claim. It unnecessarily recited rejected alternatives and slightly exceeded the
  90-word request (about 91 whitespace-separated words). Not an unqualified pass.
- M preserved reporting/conduct, aggregation, uncertainty and separate tool claims,
  but packed them into two unwieldy sentences. Root added instructions to prioritize
  central prose and flag incompatible constraints rather than produce a checklist.
- C retained political commitments and avoided demanding an intervention study.
  It also used unnecessary defensive contrasts. The prose-quality correction applies.

The final instruction refinements were root-reviewed, not rerun through these
cases. Four responses are not a reliability estimate. Both actual wins and remaining
style failures are retained; no new host compatibility claim follows.
