<p align="left"><img src="assets/logo.svg" width="64" alt="Evidence paths joining a manuscript page"></p>

# HCI Academic Writing Skills

**Turn research evidence into a coherent HCI manuscript.**

An agent skill for researchers writing HCI papers in an existing ACM LaTeX project. Give an AI coding agent a writing task and your evidence. The skill guides it to identify what the paper contributes, edit the relevant `.tex` files in place, and report what changed and what evidence is still missing.

[한국어](README.ko.md) · [Install](docs/COMPATIBILITY.md) · [Skill](skills/hci-academic-writing/SKILL.md) · [122-paper corpus](research/CORPUS.md) · [Development record](docs/REVIEW-LOG.md)

![Editorial illustration of manuscript pages, human interaction and connected evidence](assets/editorial-cover.png)

## What it does in your paper folder

The installer copies a skill folder into your project. It contains instructions, writing references and a read-only LaTeX audit script. Your manuscript stays where it is. A multi-file project might look like this:

```text
my-paper/
├── chi26.tex                          # root file
├── sections/related-work.tex          # file you ask the agent to revise
├── sections/...                       # other sections
└── .claude/skills/hci-academic-writing/   # installed skill (Claude Code)
```

For a scoped request, the skill directs the agent to:

1. **Establish the task:** the requested output, target venue or track, study stage, available evidence, root `.tex` file and edit scope. It asks only for missing information that changes the argument and continues supported work meanwhile.
2. **Read what matters:** the relevant section, its dependencies and only the guidance the task needs. Polishing one paragraph does not require a project-wide intake.
3. **Edit the manuscript:** make the requested changes in the existing files, along with a concise account of material changes.
4. **Mark evidence gaps:** omit unknown facts or place the whole missing proposition in a comment, such as `% HCI-TODO[evidence]: verify the condition contrast`.
5. **Check and report:** review the diff and relevant references, then state what changed, what was checked and what evidence is still needed.

### What to include in your request

- The root `.tex` file and the file, section or paragraph to work on
- The task and any limit, such as a target word count
- Your evidence: results, analysis notes, study details or design documentation
- For venue-specific work, the target venue or track and its template/official requirements
- A TeX toolchain, if you want the manuscript compiled

### What gets edited

The agent edits manuscript text within the scope you set. The workflow preserves project structure, macros, bibliography keys, labels and unrelated edits. During wording-only revision, it keeps your existing claims and citation attachments.

The skill instructs the agent never to invent studies, participants, quotations, statistics, references or claims of having read a source. Instructions do not guarantee behavior, so review every change (see [Validation and limits](#validation-and-limits)).

The bundled auditor checks lexical LaTeX dependencies and does not change files. Actual compilation requires your TeX toolchain. Overleaf upload and submission remain separate actions. The package does not include or replace the ACM template.

## Example task outcomes

These examples show what each request asks for. They are not measured improvements.

| Before | Requested outcome |
|---|---|
| Related work runs one paragraph per author | The section is organized around the unresolved problem, with existing claims and citation attachments preserved and substantive evidence gaps flagged |
| A group-decision paper blurs its system contribution and findings | An outline built from supplied results separates the two, without turning group outcomes into claims about individual judgment |
| A design study of domestic objects lists activities | The text traces making and reflection into the design insight, keeps ambiguity and conflicting interpretations, and invents no effectiveness evaluation |
| A results paragraph is over length | The existing `.tex` is compressed to 150 words, keeping effect estimates, uncertainty, null findings and the unit of analysis, with the counting convention and material changes reported |
| Data collection has not begun | Motivation, related work and the actual method are drafted, wording stays explicitly planned, and result-dependent slots stay in draft comments rather than imagined findings |

## How to start

**1. Install into your paper project.** Python 3.9+ is sufficient, with no third-party packages. Run from this repository's root and replace `/path/to/paper` with your manuscript directory.

```sh
git clone https://github.com/Soohwan-Lee/HCI-Academic-Writing-Skills.git
cd HCI-Academic-Writing-Skills

# Preview; no files are written.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper

# Copy the complete skill bundle.
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper --apply
```

For Claude Code use `--host claude-code`. For Antigravity use `--host antigravity-app`, `antigravity-ide` or `antigravity-cli`.

The installer refuses conflicting existing files. Updating an older installation requires reviewing and relocating that copy first. It does not alter global settings. See [personal installation, host paths and compatibility evidence](docs/COMPATIBILITY.md).

**2. Start a new agent session in the manuscript project.** Explicitly request `hci-academic-writing` and confirm that the agent loads the intended `SKILL.md`. The core bundle is self-contained; linked public paper analyses are optional further reading.

**3. Begin with a small, scoped task.** For example:

> Use hci-academic-writing. The root is chi26.tex. Revise sections/related-work.tex
> around the unresolved problem rather than one paragraph per author. Preserve
> existing claims and citation attachments. Improve paragraph transitions and
> sentence-to-sentence flow; flag only substantive evidence gaps.

> Use hci-academic-writing to compress the results paragraph to 150 words while
> preserving effect estimates, uncertainty, null findings and the unit of analysis.
> Edit the existing .tex file and report the counting convention and material changes.

### Host compatibility

| Host | Documented paths and format | Installation | Live manuscript editing |
|---|---|---|---|
| Claude Code | Verified | Tested in isolated temporary directories | Two isolated ACM editing tasks, loaded by explicit named request |
| Codex | Verified | Tested in isolated temporary directories | Not tested |
| Antigravity | Verified | Tested in isolated temporary directories | Not tested |

Automatic host discovery remains unverified. Slash invocation also remains unverified in the restricted Claude Code configuration tested.

## Contribution is different from method, topic and venue

A contribution is the change in knowledge a paper offers: what should readers understand, build, do or reconsider after reading it, and what evidence supports that change? The skill treats these as separate choices:

| Choice | Question it answers | Hypothetical example |
|---|---|---|
| Contribution | What should readers take away, and why should they accept it? | A new interaction capability |
| Method | How was the evidence produced? | A user study |
| Topic | What is the paper about? | Group decisions |
| Venue | Where will it be submitted? | CHI |
| Manuscript form | How is the argument presented? | Paper or pictorial |

A study used to evaluate a system does not automatically make a paper empirical-first. That evaluation usually stays inside the artifact route. A hybrid route applies when two substantive claims need distinct warrants.

The skill provides these support routes, selected after identifying the knowledge claim:

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

Hybrid contributions can use multiple routes. Pictorials retain visual argument and reading paths. Common modules cover abstracts, introductions, gap-driven related work, paragraph jobs, sentence connections, discussion, compression and reviewer responses. An 8,000-word planning table is an **editorial aid**, not a measured norm.

The [contribution catalogue](skills/hci-academic-writing/references/contribution-catalogue.md) distinguishes finer claims, including sociotechnical understanding, theory use and revision, critique, participatory change, historical inquiry and replication. It links these to evidence-specific support. Dedicated [sociotechnical guidance](skills/hci-academic-writing/references/sociotechnical.md) covers relationships, analytical levels and interpretive paragraph flow. Some subtypes still lack direct indexed exemplars; the expansion targets those gaps.

## Evidence you can inspect

**122 full-text analytical notes:** 120 papers from CHI (41), CSCW (24), UIST (17), DIS (19) and IUI (19), plus COMPASS and Findings of EMNLP supplements. The corpus includes decorated exemplars, established research lineages and methodological contrasts. Award evidence is checked separately; reputation is not a writing rule.

The scope includes collaboration, human–AI interaction, dissent and reflection, alongside accessibility, privacy, care, education, craft, physical interaction and situated social research. This is a purposive teaching collection, not a representative sample. Artifact papers remain more numerous, and some routes need further expansion.

**Planned, not completed:** [100 additional analyses](docs/EXPANSION-200.md) are planned, for a target of 208. Fourteen additions have passed source review (122 total); 86 remain. This README counts only completed analyses.

- [Corpus and source provenance](research/CORPUS.md) · [coverage audit](research/COVERAGE-AUDIT.md)
- [Cross-paper synthesis](research/SYNTHESIS.md) · [portable evidence index](skills/hci-academic-writing/references/corpus-index.md)
- [Length measurements](research/measurements/README.md): seven body/section examples; 32 selected paragraphs across 14 papers
- [Plan](docs/PLAN.md) · [sampling decisions](docs/SAMPLING-PLAN.md) · [stage reviews](docs/REVIEW-LOG.md)

Analyses were produced with AI agents and reviewed during integration. There is no independent human coding validation. Only the stated subsets have numeric length measurements; no universal paragraph length or section ratio is claimed.

## Validation and limits

18 automated installer/auditor tests pass. Measurement replay passed on the recorded local source versions. Two actual Claude Code edits loaded the installed skill, preserved unrelated files and supplied evidence, and compiled as ACM LaTeX. [File-edit evidence](tests/behavior/README.md) documents the tested configuration.

Generation trials also exposed unsupported temporal, coding-unit and research-gap claims despite explicit instructions. [Failures and revisions](tests/behavior/SEMANTIC-REPORT.md) are recorded openly. This toolkit supports authoring; it does not establish factual correctness, methodological validity or better publication outcomes. No controlled comparison or independent author-usage evaluation has been conducted.

```sh
python3 -m unittest discover -s tests/install -v
python3 -m unittest discover -s tests/latex-audit -v
python3 scripts/build_corpus_index.py --check
```

## Contribute and reuse

Corrections, contrasting exemplars and real authoring failure cases are welcome. See [contribution guidelines](CONTRIBUTING.md). Original project code and writing are [MIT licensed](LICENSE); linked papers remain under their own rights. Source PDFs, private Zotero records and model transcripts are not distributed. [Visual provenance](assets/README.md) documents the generated cover and original logo.
