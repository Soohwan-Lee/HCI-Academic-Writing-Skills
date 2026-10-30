<p align="left"><img src="assets/logo.svg" width="64" alt="Evidence paths joining a manuscript page"></p>

# HCI Academic Writing Skills

**Build the argument. Shape the paper. Revise the prose.**

A writing skill for AI coding agents working inside your HCI manuscript folder. It helps turn research materials into a contribution-specific outline, develop sections and paragraphs, and revise the actual LaTeX files you will upload to Overleaf.

For researchers writing **CHI, CSCW, UIST, DIS and IUI** papers, including systems, empirical studies, sociotechnical accounts, research through design, conceptual work and literature reviews.

[한국어](README.ko.md) · [Quick start](#quick-start) · [Writing examples](#try-it-on-your-manuscript) · [Evidence](#what-the-guidance-is-based-on) · [Development plan](docs/STRUCTURE-ANALYSIS-PLAN.md)

![Editorial illustration of manuscript pages, human interaction and connected evidence](assets/editorial-cover.png)

## What this skill helps you do

You supply the research, draft and task. The skill gives your agent instructions and selectively loaded writing references for the decisions between evidence and finished prose.

| Your task | What the agent is instructed to produce |
|---|---|
| “What is this paper's contribution?” | A clear knowledge claim, its supporting evidence and its boundaries |
| “How should this paper be organized?” | A section and subsection plan, with paragraph roles and logical transitions |
| “Draft this section from my notes.” | Manuscript text grounded in the supplied material, with missing facts left explicit |
| “My related work is a list of papers.” | A synthesis organized around the problem and the relationships among prior approaches |
| “These paragraphs do not flow.” | Revised paragraph order, sentence connections and referents |
| “Cut this to the word limit.” | A shorter passage that retains consequential claims, evidence and uncertainty |
| “Help address this review.” | An answer tied to evidence and concrete manuscript changes |

The deliverable is usually an edit to your manuscript, accompanied by a short explanation of what changed. A small wording task stays small; it does not require a full-paper planning exercise.

## The structure follows the contribution

An interview can inform a system, support a sociotechnical interpretation or help develop a concept. Those papers need different arguments even when they use similar methods or target the same venue.

The skill separates **contribution, method, topic, venue and manuscript form**. It then helps plan four connected levels:

> **Section:** What does the reader need to understand here?
>
> **Subsection:** Which questions must be answered, and in what order?
>
> **Paragraph:** What claim or question does this paragraph develop, with what material?
>
> **Sentence:** How does each sentence connect known information to the next inference?

Source-backed examples illustrate alternative structures:

| Kind of argument | One possible progression |
|---|---|
| New interaction capability | Capability overview → design rationale → implementation → capability-specific evaluation |
| System informed by formative inquiry | Formative findings → design commitments → system → distinct evaluation questions |
| Reflective design / pictorial | Situated practice → reflective lens → material or visual cases → cross-case interpretation |
| Sociotechnical understanding | Situated accounts → relationships or tensions → conceptual interpretation → implications |
| Historical inquiry | Period-specific accounts → cross-period analytical dimensions → implications and methodological reflection |
| Concept development | Conceptual lineage → illustrative design → participant interpretations → conceptual account |
| Dataset or research resource | Construction → characterization → task-specific utility → reuse conditions |
| Interpretive literature review | Selection and analysis → thematic findings → conceptual synthesis → research agenda |

These are conditional choices, not required templates for a venue. The [architecture guide](skills/hci-academic-writing/references/architectures.md) explains when each helps. The [contribution catalogue](skills/hci-academic-writing/references/contribution-catalogue.md) also covers participatory change, critique, methods, replication and hybrid contributions.

Shared references address abstracts, introductions, gap-driven related work, discussion, paragraph development and sentence flow. Topic-first paragraphs are useful when the claim is immediately intelligible; narrative or delayed interpretation can serve other purposes. An 8,000-word allocation is a planning aid, not a universal HCI convention.

## Quick start

You need an existing manuscript folder, a supported AI coding agent and **Python 3.9+** to run the installer. No third-party Python packages are required. The package provides a skill bundle; your agent supplies the model and editing tools.

### 1. Get the repository

```sh
git clone https://github.com/Soohwan-Lee/HCI-Academic-Writing-Skills.git
cd HCI-Academic-Writing-Skills
```

### 2. Install into your manuscript folder

Replace `/path/to/paper` with the folder containing your ACM project. Choose the host you use.

```sh
# Preview a Codex installation; writes nothing.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper

# Install for Codex.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper --apply

# Or install for Claude Code.
python3 scripts/install_skill.py --host claude-code --scope project --project-root /path/to/paper --apply
```

For Antigravity, select `--host antigravity-app`, `antigravity-ide` or `antigravity-cli`. Codex and Antigravity project installs use `.agents/skills/hci-academic-writing/`; Claude Code uses `.claude/skills/hci-academic-writing/`.

The installer previews changes by default and refuses conflicting files. To update an older copy, review and relocate it before reinstalling. See [installation and compatibility](docs/COMPATIBILITY.md) for personal installs, exact paths and tested behavior.

### 3. Open the paper folder and request the skill

Start a fresh agent session **in your manuscript project**, then name `hci-academic-writing` explicitly. Confirm that the intended `SKILL.md` is loaded. For example:

> Use hci-academic-writing. The root is main.tex. Read sections/related-work.tex and revise it around the unresolved problem. Preserve existing claims and citation attachments. Improve paragraph order and sentence connections, then edit the file and summarize the changes.

Your manuscript stays in its existing structure:

```text
my-paper/
├── main.tex
├── sections/
│   ├── introduction.tex
│   ├── related-work.tex
│   └── ...
├── references.bib
└── .claude/skills/hci-academic-writing/  # or .agents/skills/ for Codex
    ├── SKILL.md
    ├── references/
    └── scripts/
```

The installed bundle is self-contained. You do not need the full research corpus or Zotero library to use it. Compilation needs your TeX toolchain; uploading to Overleaf is a separate step. The skill does not include the ACM template.

## Try it on your manuscript

Give the agent the root file, edit scope, available evidence and any word limit. Include the venue/track and official requirements when the task concerns submission format.

### Plan a paper beyond generic headings

> Use hci-academic-writing. Read main.tex and my study notes. Identify the primary contribution and propose an outline suited to it. For every section, give its purpose and subsection order. For the central section, plan each paragraph's claim, supporting material and handoff to the next paragraph. Explain any consequential alternative structure before editing the outline.

### Turn findings into an interpretive discussion

> Use hci-academic-writing. Draft the discussion in sections/discussion.tex from the supplied interview findings. Explain how the observed relationships extend or complicate the concepts already introduced. Keep participant accounts, our interpretation and proposed implications distinguishable. Do not turn every finding into a system requirement.

### Develop a design argument

> Use hci-academic-writing. Read the design diary and annotated artifact images. Help organize the RtD argument around what making and reflection taught us. Propose subsections and paragraph roles that connect material encounters to design understanding, including tensions and unresolved interpretations.

### Write a literature synthesis

> Use hci-academic-writing. Use my review protocol and extraction table to plan the findings and synthesis sections. Distinguish what the corpus contains from the cross-paper interpretation. Choose a structure suited to the review's actual purpose and procedure; do not assume it is a systematic review.

### Revise or compress a passage

> Use hci-academic-writing. Edit the selected results paragraph in sections/results.tex to at most 150 words. Preserve estimates, uncertainty, null findings and analysis units. Report the counting convention and any material changes.

These are example requests, not measured performance claims. The agent should preserve bibliography keys, labels, macros and unrelated edits. Unknown facts belong in explicit draft comments such as `% HCI-TODO[evidence]: ...`, not plausible invented prose.

## What the guidance is based on

The repository contains **128 full-text analytical notes**: CHI 41, CSCW 25, UIST 18, DIS 21 and IUI 21, plus one COMPASS and one Findings of EMNLP paper. Sources include award-recognized work, established research lineages and contrasting forms of inquiry. Award evidence is recorded separately from writing analysis.

Within that collection, **12 deeper structure maps** trace actual section/subsection order and selected complete paragraph sequences, with sentence-level analysis. They connect observed writing choices to conditional drafting guidance. They do not mean that every paragraph of all 128 papers has been mapped.

| Evidence | Where to inspect it |
|---|---|
| Paper selection, sources and analytical notes | [Corpus](research/CORPUS.md) · [coverage audit](research/COVERAGE-AUDIT.md) |
| Hierarchy, paragraph roles and sentence flow | [Structure maps](research/structure-maps/README.md) |
| Cross-paper interpretation | [Synthesis](research/SYNTHESIS.md) · [portable corpus index](skills/hci-academic-writing/references/corpus-index.md) |
| Quantitative length observations | [Measurements](research/measurements/README.md): seven body/section examples and 32 selected paragraphs in 14 papers |
| Decisions and revisions | [Active plan](docs/STRUCTURE-ANALYSIS-PLAN.md) · [review log](docs/REVIEW-LOG.md) |

This is a purposive teaching collection, with AI-assisted analysis and integration review. It is not a representative sample or independently human-validated coding study. Paragraph lengths and section allocations are not established norms. New papers are added when they resolve a meaningful gap, not to reach a numerical target.

## What has been tested

| Layer | Current evidence |
|---|---|
| Installation and lexical LaTeX audit | 18 automated tests; isolated host-specific installation layouts |
| Claude Code file editing | Two scoped edits in a multi-file ACM fixture, with explicit skill loading and successful compilation |
| Codex / Antigravity live editing | Not yet tested |
| Automatic skill discovery | Not established by the restricted Claude test; explicit named requests were tested |
| Whole-paper architectural writing quality | Broader contribution-specific writing probes remain to be completed |

The [file-edit report](tests/behavior/README.md) records actual behavior. Other generation trials exposed unsupported claims; the [semantic report](tests/behavior/SEMANTIC-REPORT.md) records failures and revisions. Review the agent's changes as an author. No controlled study establishes publication benefits or overall writing-quality gains.

## Development priorities

The skill is usable now, with continuing work on depth and validation:

1. Compare more **within-family alternatives**, especially RtD, empirical organization and review structures.
2. Test outline selection, section drafting and paragraph restructuring in multi-file ACM projects.
3. Expand comparable length measurements before drawing stronger quantitative guidance.
4. Verify ordinary-session discovery and editing across hosts.

The [active plan](docs/STRUCTURE-ANALYSIS-PLAN.md) tracks these gates. Expanding from 128 to 200 papers is not a completion requirement.

## Contribute and reuse

Corrections, contrasting exemplars and real authoring failure cases are welcome. See [contribution guidelines](CONTRIBUTING.md).

Original project code and writing are [MIT licensed](LICENSE); linked papers retain their own rights. Source PDFs, private Zotero records and model transcripts are not distributed. [Visual provenance](assets/README.md) documents the cover and logo.

To run local checks:

```sh
python3 -m unittest discover -s tests/install -v
python3 -m unittest discover -s tests/latex-audit -v
python3 scripts/build_corpus_index.py --check
```
