<p align="left"><img src="assets/logo.svg" width="64" alt="Evidence paths joining a manuscript page"></p>

# HCI Academic Writing Skills

**Turn research evidence into a coherent HCI manuscript.**

A contribution-aware writing skill for AI coding agents working directly in an
existing ACM LaTeX project. Frame the argument, synthesize related work, connect
paragraphs and sentences, and revise without losing the evidence behind a claim.

[한국어](README.ko.md) · [Install](docs/COMPATIBILITY.md) · [Skill](skills/hci-academic-writing/SKILL.md) · [107-paper corpus](research/CORPUS.md) · [Development record](docs/REVIEW-LOG.md)

![Editorial illustration of manuscript pages, human interaction and connected evidence](assets/editorial-cover.png)

## Write for the contribution

CHI, CSCW, UIST, DIS and IUI contain many kinds of knowledge. The skill routes by
what a paper contributes, then adapts to its method, audience and manuscript form.

| Contribution | Writing focus |
|---|---|
| Quantitative findings | Constructs, comparisons, analysis units, uncertainty and bounded inference |
| Qualitative understanding | Situated accounts, interpretation, reflexivity and analytical contribution |
| Systems and interaction techniques | Capability, enabling mechanisms, evaluation questions and failure conditions |
| Design / research through design | Making, material encounters, reflection and transferable design understanding |
| Concepts and theory | Premises, distinctions, explanatory consequences and limits |
| Methods and instruments | Procedure, rationale, validity and conditions of use |
| Datasets and resources | Provenance, construction, characterization, reuse and stewardship |
| Reviews and synthesis | Selection, coding units, synthesis and appropriate review commitments |

Hybrid contributions can use multiple routes. Pictorials retain visual argument
and reading paths. Common modules cover abstracts, introductions, gap-driven related
work, paragraph jobs, sentence connections, discussion, compression and reviewer
responses. An 8,000-word planning table is an **editorial aid**, not a measured norm.

## Install in a paper project

Clone this repository and run from its root. Python 3.9+ is sufficient for installation.
Replace `/path/to/paper` with your existing manuscript directory.

```sh
git clone https://github.com/Soohwan-Lee/HCI-Academic-Writing-Skills.git
cd HCI-Academic-Writing-Skills

# Preview; no files are written.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper

# Copy the complete skill bundle.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper --apply
```

For Claude Code use `--host claude-code`; for Antigravity use
`--host antigravity-app`, `antigravity-ide` or `antigravity-cli`.
The installer refuses conflicting existing files. Updating an older installation
requires reviewing and relocating that copy first. It does not alter global settings.
See [personal installation, host paths and compatibility evidence](docs/COMPATIBILITY.md).

Start a new agent session in the manuscript project and explicitly request
`hci-academic-writing`. Confirm that it loads the intended `SKILL.md`. The core
bundle is self-contained; linked public paper analyses are optional further reading.
Codex and Antigravity paths/formats are documented and installation-tested; live
editing was tested with Claude Code. Automatic host discovery remains unverified.

## Start with a real writing task

Give the agent a scoped request and the evidence it needs. For example:

> Use hci-academic-writing. The root is chi26.tex. Revise sections/related-work.tex
> around the unresolved problem rather than one paragraph per author. Preserve
> existing claims and citation attachments. Improve paragraph transitions and
> sentence-to-sentence flow; flag only substantive evidence gaps.

> Use hci-academic-writing to frame this group-decision paper. Separate the system
> contribution from the group-level findings. Build an outline from the supplied
> results; do not turn group outcomes into claims about individual judgment.

> Use hci-academic-writing for this design study of domestic objects. Trace making
> and reflection into the design insight. Preserve ambiguity and conflicting
> interpretations; do not invent an effectiveness evaluation.

> Compress the results paragraph to 150 words while preserving effect estimates,
> uncertainty, null findings and the unit of analysis. Edit the existing .tex file
> and report the counting convention and material changes.

The workflow preserves project structure, macros, bibliography keys, labels and
unrelated edits. A bundled read-only LaTeX auditor checks lexical dependencies;
actual compilation requires your TeX toolchain. Overleaf upload and submission
remain separate actions. The package does not include or replace the ACM template.

## Evidence you can inspect

**107 full-text analytical notes:** 105 papers from CHI (34), CSCW (21), UIST (15),
DIS (18) and IUI (17), plus COMPASS and Findings of EMNLP supplements. The corpus
includes decorated exemplars, established research lineages and methodological
contrasts. Award evidence is checked separately; reputation is not a writing rule.

The scope includes collaboration, human–AI interaction, dissent and reflection,
alongside accessibility, privacy, care, education, craft, physical interaction and
situated social research. This is a purposive teaching collection, not a representative
sample. Artifact papers remain more numerous; some routes need further expansion.

- [Corpus and source provenance](research/CORPUS.md) · [coverage audit](research/COVERAGE-AUDIT.md)
- [Cross-paper synthesis](research/SYNTHESIS.md) · [portable evidence index](skills/hci-academic-writing/references/corpus-index.md)
- [Length measurements](research/measurements/README.md): seven body/section examples; 32 selected paragraphs across 14 papers
- [Plan](docs/PLAN.md) · [sampling decisions](docs/SAMPLING-PLAN.md) · [stage reviews](docs/REVIEW-LOG.md)

Analyses were produced with AI agents and reviewed during integration. There is no
independent human coding validation. Only the stated subsets have numeric length
measurements; no universal paragraph length or section ratio is claimed.

## Validation and limits

18 automated installer/auditor tests pass. Measurement replay passed on the recorded
local source versions. Two actual Claude Code edits loaded the installed skill,
preserved unrelated files and supplied evidence, and compiled as ACM LaTeX.
[File-edit evidence](tests/behavior/README.md) documents the tested configuration.

Generation trials also exposed unsupported temporal, coding-unit and research-gap
claims despite explicit instructions. [Failures and revisions](tests/behavior/SEMANTIC-REPORT.md)
are recorded openly. This toolkit supports authoring; it does not establish factual
correctness, methodological validity or better publication outcomes. No controlled
comparison or independent author-usage evaluation has been conducted.

```sh
python3 -m unittest discover -s tests/install -v
python3 -m unittest discover -s tests/latex-audit -v
python3 scripts/build_corpus_index.py --check
```

## Contribute and reuse

Corrections, contrasting exemplars and real authoring failure cases are welcome.
See [contribution guidelines](CONTRIBUTING.md). Original project code and writing
are [MIT licensed](LICENSE); linked papers remain under their own rights. Source
PDFs, private Zotero records and model transcripts are not distributed.
[Visual provenance](assets/README.md) documents the generated cover and original logo.
