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
| New full-text batches | 9 / 100 accepted | E01 four + E02 five; 117 total; 91 additions remain |
| Skill synthesis and tests | Pending | Review after each 20 additions and final integration |
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
