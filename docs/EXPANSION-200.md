# Second corpus expansion

Status: active; started 2026-10-30. Baseline: 108 distinct full-text analyses,
including the newly read God-Saeng paper. Target: **100 additional analyses (208 total)**.
This target is a work commitment, not a claim that 208 papers have been read.

## Selection design

Use contribution as the primary sampling axis. Venue, publication year, topic,
evidence method, manuscript form and source of discovery are separate dimensions.
The initial venue allocation is CHI 30, CSCW 25, UIST 15, DIS 15 and IUI 15.
Adjust with a recorded rationale when a contribution needs a cross-venue supplement;
retain at least 15 new papers per requested venue before declaring balanced expansion.

Aim for at least 80 of the 100 additions from 2018–2026, with at least 40 from
2022–2026. Older landmark contrasts may occupy up to 20 slots. These are sampling
targets, not population estimates. Recent papers cannot yet have the citation
histories of older work. Use verified awards, documented uptake, citation snapshots,
and contribution relevance as complementary signals. Never call a paper highly cited
without a dated source and a clear database. Lab reputation alone is insufficient.

Review multiple Zotero collections: HCAI and human–AI collaboration, but also
sociotechnical/CSCW, participatory and critical design, RtD, methods/reviews,
accessibility, sustainability, health, embodied interaction and visualization.
Collection names describe interests, not contribution classes. Independently search
conference programs, ACM proceedings and public author/preprint copies. Aim for at
least half the additions discovered independently of the library and no more than
35 additions primarily about AI. Overlapping discovery paths are recorded, not
counted as independent evidence of importance. Keep library membership private.

## Contribution coverage priorities

1. Situated characterization and sociotechnical configurations; interpretive depth,
   relations, practices, institutions, power and cultural context.
2. Comparative/causal evidence versus descriptive computational observation and audits.
3. Conceptual distinctions, sensitizing concepts, frameworks, theory use and revision.
4. Critical/normative arguments, non-design, historical accounts and genealogy.
5. Participatory/action research, partnerships, infrastructuring and maintenance.
6. Systems, interaction techniques, toolkits, algorithms and physical fabrication.
7. RtD, portfolios, material exploration, speculative and pictorial argument.
8. Measurement/method contributions, datasets/resources, replication and null evidence.
9. Systematic, scoping, critical, methodological and quantitative research synthesis.

One paper can substantiate several priorities, but has one identity in the corpus.
Do not pad a weak subtype with papers merely using its method or vocabulary.

## Batch protocol

For each batch of 5–10 papers:

1. Screen identity, duplication, version, relevance and full-text availability.
2. Record selection rationale and verify any award/citation signal independently.
3. Read the full main text, necessary appendices, figures and tables. Record access
   limits; inaccessible or abstract-only items remain candidates outside the corpus.
4. Write original notes: contribution contract, evidence warrant, section sequence,
   introduction/RW logic, results-to-discussion transition, paragraph jobs and at
   least two source-located sentence-flow examples. Record counterexamples/limits.
5. Root reviews source alignment and compares papers; Claude output alone is not
   final verification. Reject invented metadata, unsupported generalization and
   taxonomy forced by method labels.
6. Update metadata/index/counts and batch review record. Commit and push scoped files.
7. Update skill guidance only when the evidence supports the change; distinguish a
   single-paper illustration from a cross-paper pattern and an editorial heuristic.

After each 20 additions, audit venue/year/topic/contribution balance and reallocate
remaining slots. Expand numerical measurements separately: consistent main-text
boundaries, excluded references/captions, extraction quality, paragraph definitions,
and sample size per subtype. No universal word quota follows from corpus size.

## Work ledger

| Stage | State | Evidence / next gate |
|---|---|---|
| Baseline | 108 analyses | 107 first-release papers plus P110 God-Saeng |
| Taxonomy review | First implementation reviewed | Catalogue and sociotechnical guide shipped; eight-case behavior report retains two failures/limitations |
| Library inventory | Partially blocked | Collection names retrieved; item API repeatedly timed out and active database was locked; no raw export published |
| Candidate screening | In progress | 30 recent official-award candidates independently sourced and title-deduplicated; IUI and other strata pending |
| New full-text batches | 19 / 100 accepted | E01 four + E02 five + E03 five + E04 five; 127 total; 81 additions remain |
| Skill synthesis and tests | E02/E03 integrations reviewed | Four E03 behavior probes retained limitations; next cumulative review after 20 additions |
| README revision | First revision reviewed | Opus drafted both guides; root checked every section, counts, links and scope; update after each accepted batch |

## Release gate

Count only completed source-reviewed notes. Synchronize English/Korean guides,
corpus/index, coverage and limitations. Re-run relevant tests; explicitly distinguish
installation, live discovery, compile success and semantic behavior. Confirm remote
HEAD after each push. Do not describe this expansion as complete while any required
batch or review remains outstanding.

## E01 gate — focused taxonomy contrasts
A four-paper exception to the normal 5–10-paper batch closes three carried-over
historical reads and a directly relevant recent genealogy. Root read every main
text and inspected paragraph renders; Opus assisted three analyses. P114 remains
unread/unaccepted because its eight-page scan needs OCR or visual reading. No
additional numeric length measurements were added. Next batches must prioritize
2018–2026 sources to meet the 80/100 recent target. The separate 30-title queue is
not included in the analyzed count.

## E02 gate — recent empirical, conceptual, ecological and sensing contrasts
Five additions from 2021–2025: two IUI experiments, CHI Social Transparency,
DIS domestic plant-care ethnography, and UIST EarHover. Root read all five main
texts and inspected 17 rendered pages, including ten complete paragraph examples.
Opus 5.5 medium assisted all five through subscription authentication. The plant
study is an explicitly identified March 2025 OSF preprint; its published version
was inaccessible and is not claimed identical. Official Best Paper records were
checked for plant care and EarHover. Four Crossref snapshots succeeded; EarHover
returned HTTP 429 and has no inferred citation count.

Cumulative expansion: 9/100, with 6/9 from 2018–2026 and 3/9 from 2022–2026.
Current additions by venue: CHI 4, CSCW 1, IUI 2, DIS 1, UIST 1. Three E02 papers
primarily concern AI; the sensing classifier serves a physical-interaction claim.
These small batches are not individually representative. Next acquisition must
prioritize CSCW/DIS/UIST, resources, review/measurement and non-AI contrasts before
adding another XAI cluster. Two of the 30 award-queue papers are now accepted;
28 remain candidates. Other Zotero collections remain part of the acquisition plan.

## E03 gate — reviews, metaresearch and accessible input
Five source-reviewed additions: CHI reporting-practice audit, CHI queer literature
mapping/critique, CSCW digital-legacy conceptual synthesis, UIST Wheeler and CSCW
moderation-experience synthesis. Root read all main texts, read Wheeler appendices,
and inspected 22 rendered pages across the five papers. Opus 5.5 medium assisted
all five; root adjudicated scope, extraction omissions and selected microanalyses.
The Crip Reflections download duplicated P15: excluded, with P124 left unused.
Wheeler's Honorable Mention was verified on the official conference page. Two
Crossref snapshots succeeded, one was rate-limited, and two were not requested.

Cumulative expansion: 14/100; 11/14 from 2018–2026 and 8/14 from 2022–2026.
Additions by venue: CHI 6, CSCW 3, IUI 2, DIS 1, UIST 2. Three primarily AI
additions remain from E02; E03's moderation focus concerns governance and lived
experience across moderation arrangements. Counts do not establish topic balance.
Zotero item retrieval remains blocked; broader collections remain acquisition
priorities, not completed coverage. Next: translate E03 contrasts into review
instructions, then prioritize DIS, resource/method and non-AI design exemplars.
No new numerical paragraph-length or section-proportion measurements were added.

## E04 acquisition and reading — in progress
P128 Design Bookkeeping and P129 Porous by Design have completed root main-text
reading, visual inspection and Opus-assisted analysis. Their notes are staged
research artifacts; neither is yet included in the accepted corpus count.
Together they contrast reflective material practice and sociotechnical conceptual
extension within DIS. P127 Participation in Data Donation remains an acquisition
candidate after repository timeouts and a publisher-mirror HTTP 403; it is not read
or counted. Seek additional participatory/method/resource contrasts and then
return to UIST, CSCW and IUI; a convenient award cohort must not become the whole
expansion. Zotero collection inventory remains a sampling guide, not evidence of
item-level coverage. Remote HEAD was confirmed after the E03 correction push.

## E04 acceptance gate — 2026-10-30
Accepted P128, P129 and P132–134 after complete main-text reading, selected
render inspection and root adjudication of subscription Opus 5.5 medium critiques.
The earlier acquisition status above is historical; P128/P129 are now accepted.
UICrit appendices were read; SoundToons supplement/video were not inspected and
are explicitly outside the evidence claim. Thirty-three rendered pages were
inspected across the five papers, including the full pictorial main argument.
Published-version and author-draft differences are recorded rather than hidden.

Cumulative additions: CHI 6, CSCW 3, UIST 3, DIS 3, IUI 4; 19/100 complete.
Recent 2018–2026: 16/19; 2022–2026: 13/19. UICrit adds a primarily AI resource
case; SoundToons and Chart4Blind use learned components for creative/accessibility
workflows. Track that distinction when auditing the AI-topic cap; do not exclude
AI-enabled artifacts merely to improve a balance statistic. The next checkpoint
will define and apply the same primary-topic criterion to all accepted additions.

P127, P130 and P131 remain inaccessible candidates, not analyses. Other Zotero
collections remain active selection priorities; no item-level coverage inferred.
Next: integrate E04 lessons, acquire CSCW contrasts, and perform the 20-addition
balance review before continuing the next large block.
