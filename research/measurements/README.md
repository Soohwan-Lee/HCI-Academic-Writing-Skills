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
