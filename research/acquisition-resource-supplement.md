# Resource supplement acquisition and reading log

Access date: 2026-10-30. Scope: P107–P109 only. PDFs, extracted text, and rendered images stay in ignored `.local`; public records contain original analysis and source locators. Single analyst; neither awards nor lab reputation substitute for evidence quality. No new length measurements were collected.

| ID | Acquisition and identity | Reading/visual verification | Selection boundary |
| --- | --- | --- | --- |
| P107 | Author-hosted `https://www.dgp.toronto.edu/~bryanw/pdf/screen2words.pdf`; title, authors, UIST 2021, DOI 10.1145/3472749.3474765 and pp. 498–510 in PDF front matter. | Complete main text §§1–9, dataset/model tables and examples; rendered PDF pp. 7 and 10 verify complete §5.1 and §6.2 paragraph boundaries. | Task/resource/model hybrid; not relabeled as a pure resource-first paper. |
| P108 | Official `https://aclanthology.org/2025.findings-emnlp.781.pdf`; DOI, authors, pages and year verified against official ACL record. | Complete main text, limitations/ethics, appendices A–C; rendered PDF pp. 3 and 9 verify §2.2 and conclusion paragraphs, including column-spanning conclusion. | Genuine dataset/task-first contract; **Findings of EMNLP**, supplementary outside requested five venues. |
| P109 | `https://pure.tue.nl/ws/portalfiles/portal/358323352/3532106.3533495.pdf`; repository cover declares publisher version of record and gives DIS 2022 DOI 10.1145/3532106.3533495. | Complete main text. Rendered PDF pp. 3–13 inspected for substantive pictorial layout, including image-only landscape and case annotations; micro paragraphs on PDF pp. 7 and 12 (printed562 and567). | Fourteen-page DIS pictorial; toolkit resource and design-method hybrid. One added repository cover makes15PDFpages. |

SHA-256 and byte sizes are in `additions-resource-supplement.json`. No source PDFs are redistributed. P109 produced a recoverable xref reconstruction warning in Poppler; extraction and rendered substantive pages were readable. An initial overlarge image batch was not counted as inspection; pages were subsequently viewed in individual/two-image calls.

## Screened alternatives and failures

- Screen2Words guessed author URL `/~bryanw/assets/pdf/screen2words.pdf` returned404; author `/~bryanw/pdf/screen2words.pdf` succeeded.
- Enrico: genuine UI dataset, but MobileHCI2020 Extended Abstract/companion four-page format was excluded from this full-paper supplement.
- Original Envisioning Cards CHI2012 four-page paper: useful resource precedent, but the fuller DIS2022 pictorial was selected to inspect construction, case demonstrations, and extensibility reasoning.
- Large typing-study dataset releases were considered as discovery leads but not substituted without a demonstrable resource-primary contract.
- Existing Rico, WebUI, Webzeitgeist, and ERICA were excluded as duplicates already represented elsewhere in the corpus.

## Review findings for synthesis

1. A resource route needs distinct contracts for dataset-first, benchmark/task hybrid, and reusable design toolkit. These are not interchangeable evidence requirements.
2. P108 explicitly treats a familiar computational method as a useful baseline rather than algorithmic novelty. It also exposes the need to distinguish elicited original stimuli from generated variations and minority descriptions from noise.
3. P107 distinguishes annotation quality, generalization split design, automatic metrics, human judgments, and potential applications. The gap between those warrants should survive compression.
4. P109 is a counterexample to linear section templates. Caption sequences and spatially parallel heuristics require visual reading; their evidence cannot be recovered from prose headings alone.
5. None of these three are award-verified exemplars. Selection rests on explicit contribution contracts and inspectable evidence, not prestige inference.
