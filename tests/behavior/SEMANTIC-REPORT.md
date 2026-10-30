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
