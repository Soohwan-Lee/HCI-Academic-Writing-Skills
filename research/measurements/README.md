# Length measurements: deliberately small, explicitly bounded

[counts.json](counts.json) contains reproducible measurements for **two** PDFs.
Run `python3 scripts/measure_corpus.py /path/to/reviewed/pdfs` from the repo root.
The script checks the corpus SHA-256, removes specified frontmatter/headers,
normalizes ligatures, joins line-end hyphens, removes numeric citation brackets
and counts regex tokens. Poppler `pdftotext` is required.

These are **extracted-body estimates**, including headings, captions, figure/table
labels, numerals and quoted material. They are not prose-only counts, official ACM
counts or measurements of scientific quality. P07's introduction includes a
caption placed before its continuation; its other main sections are intentionally
aggregated because column order complicates boundaries. P03's extended
individual-differences analysis includes figure/table text. Do not apply these
percentages mechanically to an 8,000-word manuscript.

| Paper | Extracted body | Introduction | Related work |
|---|---:|---:|---:|
| P03, empirical experiment | 9,307 | 1,157 / 12.43% | 965 / 10.37% |
| P07, conceptual framework | 7,009 | 597 / 8.52% | 1,358 / 19.38% |

The contrast demonstrates why a single universal allocation would be premature;
it does **not** estimate differences between contribution types.

## Visually verified prose-paragraph subsets
P03: five consecutive complete Introduction paragraphs on PDF p.2, paragraphs
2–6. Token counts **99, 147, 119, 36, 146**. P07: first three Introduction
paragraphs on PDF p.1, counts **77, 131, 101**. Total n=8, two papers, opening
sections only. This is a contiguous convenience subset, not a random sample.
The 36-token P03 paragraph states the proposed direction; neighboring paragraphs
supply the theoretical rationale. Shortness serves a specific argumentative role.

Ranges or individual counts describe only these eight paragraphs. They do not
support “HCI paragraphs should be X words,” a percentile chart or a detector of
AI prose. The sentence-role worked examples in the analyses are selected for
instruction and are a separate sample from these length measurements.

PDF reading-order errors were also found in P02 p.6 and P05 p.2, so they were
excluded from automatic length summaries. Full-corpus section and paragraph
measurements, prose/caption separation and native-source count comparisons remain
future validation work. A smaller transparent measurement is preferable to a
larger unreviewed set of precise-looking numbers.

## Replay all available measurements

Run the read-only checker from any working directory:

```sh
python3 scripts/verify_measurements.py .local/papers
python3 scripts/verify_measurements.py .local/papers --json
```

Paths in these examples assume the repository root. Python's standard library and
Poppler `pdftotext` are required. The checker does not download PDFs, modify files,
use private snippet caches, or emit source prose. Missing PDFs and mismatched
versions fail verification. Exit codes: 0 all records pass, 1 a record fails,
2 an input/schema/tool-level error prevents a complete run. JSON reports contain
record identifiers and verification status only, with counts/check names.

The replay covers the two pilot papers above plus eight selected paragraphs each
in [systems-paragraphs.json](systems-paragraphs.json),
[social-paragraphs.json](social-paragraphs.json), and
[design-paragraphs.json](design-paragraphs.json): **32 paragraphs across 14 papers**.
These remain purposive examples spanning several contribution types, not a
random sample. The existing pilot section counts retain their broader extracted
body definition; the newer files measure selected prose paragraphs only. Their
normalizations also differ: pilot counts remove numeric citation brackets;
paragraph JSON counts include citation numerals. Do not pool them as interchangeable
linguistic word counts.

For the pilot, replay reuses `measure_corpus.py`'s reviewed boundary specifications
without calling its writing entry point. It verifies PDF hashes, abstract/body/
section token counts, section proportions, and the eight paragraph token counts.
For the three newer files it verifies PDF hashes, normalized page hashes,
character spans (including multiple spans excluding interleaved headers), paragraph
hashes, opening locators, and token counts. The checker adapts the two selector
schemas and historical double-escaped regex strings internally; source records
are preserved.

**Not automated:** sentence counts, visual paragraph completeness, prose-versus-
caption judgments, rhetorical roles, and representativeness. Stored visual-check
flags document the original analyst's inspection; replay does not perform another
visual inspection. A matching hash proves extraction identity, not that the chosen
boundary or interpretation is correct. Poppler-version changes can alter extraction
and legitimately cause a replay failure; investigate before updating evidence.

Local replay on 2026-10-30 passed all **26 records** (two pilot paper records and
24 individually recorded paragraphs) against the reviewed PDFs. The pilot's eight
paragraphs are nested inside its two records. Deliberate token-count and PDF-hash
mutations in temporary local fixtures were rejected; they did not modify the
published measurements.

## Five additional body/section examples

The complete body/section subset is now **seven papers**: the two pilot examples
above plus the five below. The 32-paragraph/14-paper subset is unchanged. These
are extraction estimates, not prose-only manuscript counts or comparable venue
statistics. No distribution over all 107 analyses has been measured.

| Paper | Extracted body tokens | Main-section count | Extraction |
|---|---:|---:|---|
| P98-accessible-collaboration | 11,697 | 6 | PDF bounding boxes |
| P102-dance-physicalisations | 11,780 | 9 | PDF bounding boxes |
| P61-accessibility-review | 11,363 | 6 | Explicit normalized text spans |
| P64-typing | 8,514 | 5 | Explicit normalized text spans |
| P80-inform | 6,938 | 6 | Explicit normalized text spans |

[Empirical records](empirical-sections.json) retain headings, quotations, captions,
table/figure text and numeric citations, exclude front matter/acknowledgments/
references/appendices, and do not join line-end hyphens. Coordinates and main-section
starts/stops were inspected on rendered pages by an AI analyst. Floating captions
are assigned geometrically. [Additional records](additional-sections.json) disclose
explicit selectors and hashes; P64 aggregates interleaved adjacent sections and P80
aggregates Introduction + Contributions + Related Work. P61's introduction-linked
footnote falls into the extracted related-work interval. These differences prohibit
pooling raw counts as a single linguistic measure. The scripts check source hashes;
replay does not independently validate the original visual boundary judgments.

```sh
python3 scripts/measure_empirical_sections.py .local/papers
python3 scripts/measure_additional_sections.py .local/papers --check research/measurements/additional-sections.json
```

The first command prints JSON without writing; compare it with the empirical record.
The second compares the full generated metadata with the saved record. Both were
replayed successfully on 2026-10-30. Private PDFs are intentionally not distributed;
obtain the recorded source versions before replaying. Poppler changes may alter
extraction, requiring investigation rather than blind record replacement.
