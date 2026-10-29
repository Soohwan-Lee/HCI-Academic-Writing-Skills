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

## Expansion gate F — intelligent interfaces and reusable resources
Parent reviewed P24–29, hashes/paths/unique identity checked; 45 integrated. SUPPLE's
optimality is relative to its model; UI X-Ray detection and historical effort are
not randomized productivity estimates; BINGO retains the unsupported exploration
hypothesis. Webzeitgeist scale is not representativeness; WebUI attributes gains
separately to architecture and pretraining; Prefab application demonstrations do
not inherit user benefits from earlier technique studies. Retained the late and
distributed related-work alternatives and P25's promotional language as a negative
example rather than imitating every feature of an award paper.

## Expansion gate G — further empirical and design breadth
Parent reviewed P35/P37–41; metadata, hashes and unique identities checked.
P35 is a documented replacement for an excluded anonymous draft. Retained limits
on causal motivation claims in P37; contextual and political readings in P38;
empirically grounded design knowledge rather than novel artifact coding in P39;
participant goals rather than automatic empowerment in P40; reported teaching
vs observed teaching/learning in P41. No single qualitative or DIS template fits
these cases. Integrated total 51.

## Scope review — 100-paper minimum
User raised the release floor from 60 to 100 and requested persistent process
records plus separate professional English/Korean READMEs. Updated PLAN and
SAMPLING-PLAN before assigning new IDs. Existing 51 reviewed papers remain the
verified count; pending 11 and reserved 42 are not reported as completed. Route
targets total 100; labels must follow actual knowledge claims, not quotas.

## Expansion gate H — conceptual disagreement and review architectures
Parent reviewed all P48–53 analytical notes; integration checks verified source
hashes, distinct DOI/IDs and analysis paths. Integrated total 57. Retained Dourish's
objection to mandatory product implications, Bardzell's agenda vs evaluated
outcomes, and Gaver's disagreement with universal RtD criteria. P51's citation
filters bound prevalence claims; P52's overlapping categories and single-classifier
process remain explicit. P53 is historical/conceptual synthesis, not interviews
or a systematic review; manuscript title/DOI-block and numbering caveats remain.
The added paragraph measurements are pending separate replay review and are not
used to claim norms. This is parent review of original single-analyst coding, not
independent recoding or researcher validation.

## Expansion gate I — review rigor and empirical scope
Root completed P60–64 with two rendered paragraph micro analyses per paper;
identity, local source hashes and uniqueness checked. Integrated 62. Corrected P61
award from an initial mistaken Best Paper reading to **Honorable Mention**, after
checking the enclosing heading on the official CHI 2021 list. Author-site evidence
supports P64 Honorable Mention. P63 DOI verified through Crossref.
Retained post-task trait measurement and exploratory analyses in P60, distinct
review denominators in P61/P62, descriptive rather than pooled causal synthesis
in P62, nonrandom browser assignment in P63, and observational/subsample limits
in P64. P59's attempted full-text URL returned 404; it remains excluded, not read.
Two short papers in the earlier root batch remain unsuitable as long-paper length
models. No historical analysis procedure is promoted into current methodological
requirements.

## Tool gate — read-only LaTeX audit
Parent inspected the parser and reran all nine isolated tests successfully. The
helper traverses literal project-local includes, checks bibliography/label keys
and surfaces TODOs without modifying manuscripts. Macro definitions, conditional
execution and external resources are explicitly uncertain; zero errors is not a
compile or semantic-validity claim. The implementation worker separately compiled
the valid ACM fixture with shell escape disabled, writing outputs only to ignored
.local. Fixture details and limitations are in tests/latex-audit/README.md.
The helper does not upload content, run builds or infer citation correctness.

## Expansion gate J — embodied systems and interaction infrastructure
Parent read P79–83 notes; hashes/paths/DOIs and unique IDs checked on integration.
Total 67. Preserved TapSense's eight-page analyzed version vs ten-page publisher
metadata, pooled vs held-out accuracy, inFORM informal vs formal evidence, PneUI
tested material combinations vs possibilities, Zooids scenarios vs deployment, and
ERICA breadth vs within-app coverage. None inherits user-performance benefits from
technical feasibility. Selected for specific writing/evidence contrasts, not fame.
Additional IUI work is prioritized after this deliberately UIST-heavy sub-batch.

## Expansion gate K — review warrants and conceptual constructions
Parent read P65–69 notes and checked source hashes, distinct IDs/DOIs and paths.
Total 72. Preserved selected influential vs exhaustive corpora (P65), unresolved
preprint count/date inconsistencies (P66), systematic selection vs reflexive
interpretation and reported vs actual practice (P67), purposive conceptual essay
vs systematic review (P68), and curated award-paper illustration vs representative
field evidence (P69). P68's argument-last definition and P69's concession after
rebuttal provide explicit alternatives to mandatory topic-first writing. These are
interpreted examples, not independently demonstrated reader-performance effects.

## Expansion gate L — stakeholder, diary and field evidence
Parent reviewed P93–97; hashes, identity uniqueness and analysis paths checked.
Total 77. Retained stakeholder disagreement and satisfaction/performance separation
(P93), attack-budget-dependent security/usability tradeoffs without current-policy
endorsement (P94), diary needs vs search-log coverage and source arithmetic caveat
(P95), perceived sensing errors vs classifier ground truth (P96), and network work
vs demonstrated health outcomes (P97). Historical platform settings remain bounded.
No source institution or influential status substitutes for the specific selection
rationales. Each note includes two complete rendered paragraph analyses.

## Expansion gate M — design methods, pedagogy and research agenda
Parent reviewed P70–74 and checked hashes/identities/paths. Total 82. Preserved
interpretive openness with evaluation responsibility, pedagogy's concept potential
vs fully realized experience, portfolio relations vs unperformed combined deployment,
partial experiential simulation vs becoming another person, and research agenda vs
validated intervention. P71 nomination remains distinct from an award. P74 repeated
local research-focus structures are followed by integration, a useful alternative
to disconnected literature catalogs. Four DIS papers broaden method/design coverage.

## Expansion gate N — five IUI contribution contrasts
Parent reviewed P84–88; source hashes, paths and unique identities checked. Total 87.
Retained terminology-based synthesis vs community-belief inference, feature-feedback
efficiency vs terminal accuracy, task-definition-specific screen metrics, authoring
examples vs comparative productivity, and processing-speed vs end-to-end latency.
P84/P86 version inconsistencies remain visible. P88's one-user benchmark is not
its earlier elicitation sample. Award evidence is independently recorded for
FrameKit and radar; neither award licenses copying overbroad result summaries.

## Expansion gate O — learning, uncertainty and accessibility in IUI
Parent reviewed P89–92; hashes/identities/paths pass integration. Total 91. Retained
delayed vs immediate recall and effort costs; benchmark-enabled teaching study with
mixed outcomes; R-squared change vs classification accuracy and collaborator users;
and best-performing stimulus selection vs representative accessibility performance.
P92 nonsignificant ratings remain distinct from qualitative preference accounts.
Best Paper evidence for P89/P90/P92 is recorded with its primary-source level.
The additional IUI papers span empirical, method, design and artifact claims.
