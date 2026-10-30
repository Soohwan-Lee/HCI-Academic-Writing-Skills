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
| Taxonomy review | In progress | Two completed Opus consultations; recommendations need integration |
| Library inventory | In progress | Local read-only collection and item inventory; no public raw export |
| Candidate screening | Pending | DOI/title deduplication and balanced shortlist |
| New full-text batches | 0 / 100 accepted | Earlier downloaded historical candidates are not yet counted |
| Skill synthesis and tests | Pending | Review after each 20 additions and final integration |
| README revision | Pending | Claude draft, root factual and usability review |

## Release gate

Count only completed source-reviewed notes. Synchronize English/Korean guides,
corpus/index, coverage and limitations. Re-run relevant tests; explicitly distinguish
installation, live discovery, compile success and semantic behavior. Confirm remote
HEAD after each push. Do not describe this expansion as complete while any required
batch or review remains outstanding.
