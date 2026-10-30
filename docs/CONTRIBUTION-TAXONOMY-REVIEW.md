# Contribution taxonomy review

Status: first implementation reviewed; corpus expansion in progress, 2026-10-30. This records an audit of the first
package, not a claim to have validated a complete HCI taxonomy.

## Review material and procedure

Read the full CHI 2026 God-Saeng preprint and inspect its paragraph examples
([P110 analysis](../research/analyses/P110-godsaeng.md)). Conducted two no-tool
Claude Code consultations through `claude.ai` Pro authentication. Both returned
`claude-opus-5-5`; the second explicitly requested medium effort and that model.
The first received the core router, qualitative/conceptual modules, coverage and
God-Saeng full text. The second received all nine route modules and a request to
challenge the first review, including its treatment of probes and theory.
Private prompts/transcripts remain local. Root makes acceptance decisions.

## Findings accepted

- Existing modules already discuss situated practice, interpretation, theory roles,
  normative commitments and participatory examples. Claiming these were entirely
  absent would be inaccurate. Discovery and subtype-specific obligations are weak.
- The route table mixes knowledge contributions with evidence methods. Introduce
  a contribution selection layer; retain useful method guidance beneath it.
- Distinguish characterization, sociotechnical configuration, theory application,
  conceptual development, critique and normative proposals. A new term alone does
  not establish theory generation; interpretive understanding need not generate theory.
- Historical, participatory/action, computational observation, replication and
  measurement claims need clearer boundaries and more direct exemplars.
- Preserve different analytical levels. A participant account cannot silently become
  a population, institutional or historical causal claim.

## Advice corrected or declined

The first review's suggestion that a probe is not an intervention is too absolute.
Probes can intervene in practices and relationships. The defensible distinction is
between intervening and establishing an effectiveness claim with suitable evidence.
The second review explicitly corrected this. God-Saeng's missions shaped the data;
they are not a demonstrated treatment for improved well-being.

Neither conceptual work nor interpretive research must produce a general theory.
Distinctions, sensitizing concepts and frameworks can contribute at their stated
scope. Do not impose causal prediction on every interpretive account.

Do not promote Claude's recalled landmark titles into analyzed exemplars. They are
search candidates until identity, full text and fit are verified. Do not infer
shared governance from workshop participation or empowerment from tool deployment.
Do not mechanically relabel all legacy corpus records from titles or methods.

## Pending gates

Implement and source-review the selection layer, add focused writing guidance,
run bounded behavior probes, reconcile bilingual documentation and expand weak
subtypes through the [second expansion](EXPANSION-200.md). P110 raises the completed
corpus to 108; other downloaded historical candidates have not yet been counted.

## Concrete-draft review and behavior gate
A third Opus review received the proposed catalogue, sociotechnical guide and notes
P33/P36/P98/P110. Root reread those notes and accepted corrections: P98 already
provides theory extension; P36 is explicit theory application; P110 is not safely
classified as formal theory application merely because it draws on perspectives.
Separated structural critique from standpoint epistemology, added a short entry
path, clarified routing by evidence, and preserved absent-party perspective limits.
Did not treat the review's every wording preference as a source-derived rule.

Eight bounded behavior cases were reviewed in full. Most intended distinctions
were preserved, but T1 invented variation and T6 imposed overly broad measurement
requirements. See [behavior report](../tests/behavior/TAXONOMY-REPORT.md). The new
guidance is available; reliable semantic behavior and full subtype exemplar coverage
remain unproven. No additional corpus analyses are counted at this gate.
