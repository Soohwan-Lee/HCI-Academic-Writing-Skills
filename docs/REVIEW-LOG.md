# Review log

## Gate 1 — protocol (2026-10-30)
Initial protocol committed as d5e94db. Claude Code was authenticated through
`claude.ai` (Pro), with API/provider overrides removed from the child environment.
A tool-free critique completed; runtime reported `claude-opus-5-5`. This is
advisory model review, not human inter-rater validation. Raw CLI output stays local.

Accepted revisions before corpus synthesis:
- Separate knowledge-object labels from methodological writing routes.
- Treat artifact evaluation as warrant unless it supports an independent claim.
- Retain author-stated claims separately from analyst-assigned labels in notes.
- Treat conceptual arguments and design knowledge as first-class outcomes.
- Avoid claims of route-level frequency from 1–2 exemplars.
- Use self-contained skill references and contribution-specific precedence.
- Add paragraph and sentence-level flow coding following user clarification.

Not adopted as a v1 claim: randomized sampling, matched award/non-award pairs,
representative statistics, comprehensive coverage or independent human coding.
These require a larger study. The purposive selection is documented as such.

Zotero: app launched; API status successful (Zotero 9.0.4). Item queries timed
out (helper timeout and a 45-second direct read). No library items were exported
or modified. Public full texts are used for this release; no claim of Zotero-based
personalization is made. Awards were checked independently of PDF availability.

## Gate 2 — corpus
Ten full texts obtained and PDF signatures checked; SHA-256 recorded. All five
venues represented. Six award labels have explicit evidence levels (four directly
read conference lists, one ACM certificate index corroborated by lab, one author
institution). No unverified paper is labeled non-awarded. Version differences,
selection bias, missing contribution types and Zotero timeout are recorded.
Gate outcome: suitable for exploratory exemplars, unsuitable for HCI-wide norms.

## Gate 3 — analysis and measurement
Ten full-text notes reviewed for structure, claim/evidence distinctions and a
selected sentence-by-sentence paragraph example each. Separate analysts produced
three batches; this is division of work, not independent double-coding or IRR.
Corrected P01's evaluation label to warrant; clarified P05's design knowledge vs
RtD method. P06 explicitly uses the revised 2021 arXiv version of a 2020 paper.
Two PDFs have reproducible extraction estimates and eight visual-checked prose
paragraphs. Column-order problems in other PDFs are documented, not hidden by
averaging. The short P03 bridge and P07's inductive paragraph contradict a uniform
length or always-deductive requirement. Gate outcome: proceed with examples and
clearly labeled heuristics; no statistical norms claimed.

## Workflow consultation — scope refinement
Second tool-free Claude consultation completed via verified claude.ai Pro;
runtime claude-opus-5-5, CLI 2.1.312. Prioritize claim alignment, finding-to-
implication warrants, reviewer response, scope-controlled editing, compression,
and citation-support checks. Keep one discoverable entrypoint and load routes on
demand; do not make researchers complete a taxonomy quiz before getting help.

Accepted: build-if-available, citation-movement review, no ungrounded numerical
or quoted additions, minimal diffs, scope-aware context, concrete fixture tests.
Modified: no automatic approval gate for every deletion, no mandatory claim-lock
file, and no invariant that forbids authorized label/citation changes. Preserve
existing claims by default, but let the user request substantive revisions. Static
checks are limited evidence, not a substitute for a successful build. Corpus and
coverage remain transparent in project docs even if normal editing responses stay
brief. A small optional state note is appropriate for sustained drafting, not a
mandatory new artifact for every paragraph edit.

## Expansion gate A — six papers
Parent reviewed all six notes P12–P17 and matched metadata, local PDF hashes and
analysis paths. Integrated 16 total. Retained method vs artifact distinctions,
Rico's bounded coverage and maintenance claim, the embodied narrative exception
to compulsory topic-first paragraphs, documentation vs actual practice in P16,
and scenario vs observed use in ProtoAI. These are reviewed interpretations, not
independent recoding or human validation. Toolkit/RtD papers are calibration
sources; their publication does not establish universal methodological standards.

## Expansion gate B — six system papers
Parent reviewed P18–P23, checked metadata, local hashes and unique identities;
22 papers integrated. Main safeguards: VizWiz response correctness differs from
task success; LightSpace attendance is not study N; Sauron participants did not
operate the complete plugin; Printed Optics includes manual/substituted parts;
OmniTouch error supports interface-size constraints; WirePrint's intermediate
control separates material reduction from path changes. Their varied architectures
are retained rather than normalized into IMRaD. No award inferred from reputation.

## Expansion gate C — six social/interpretive papers
Parent reviewed P30–34/P36; hashes, analysis paths and identities checked. Retained
distinctions between applying a framework and contributing one (P36 vs P30),
method as a separate contribution when explicitly defended (P34), and participant
aspirations vs critical interpretation (P33). P31's historical reanalysis is not
present-day practice; P32's care preferences are not population-wide cultural rules.
P35's anonymous draft was excluded pending an accessible replacement, not silently
treated as the final award paper. Integrated total 28; no independent double coding.

## Expansion gate D — design and conceptual synthesis
Parent reviewed P42–47, checked unique identities, hashes and notes; 34 integrated.
Preserved construction vs deployment evidence in Photobox; retrospective rather
than intended qualities in Mechanical Sympathy; expert co-speculation and priming
boundaries in Morse Things; contextual confounds in Undertable; purposive portfolio
vs systematic review in P46; missing historical voices and manuscript version in
Core Memory. P46 remains conceptual/methodological synthesis, not relabeled to fill
a design quota. Five design cases substantially widen the non-AI sample.

## Expansion gate E — input, attention and method contrasts
Root read P54–58 fully, checked two micro passages per paper against rendered
pages, and self-reviewed notes against the text. Hashes and unique IDs/DOIs pass.
Retained speed–stress trade-offs, candidate-model generation vs validation,
model fit vs performance advantage, elicitation agreement vs tested usability,
and methodological utility vs mathematical proof. P57 is coded from its actual
empirical/vocabulary claims, not as inventing elicitation. Four-page P54/P58 are
explicitly excluded from long-paper allocation models. Historical statistical
practices are not current recommendations. Crossref title search returned an
unrelated Beam Cursor record; rejected it and used an institutional bibliography
for Bubble Cursor identity instead. Integrated total 39.
