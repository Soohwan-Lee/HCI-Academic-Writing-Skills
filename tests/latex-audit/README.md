# Read-only LaTeX audit verification

Run from the repository root:

```sh
python3 -m unittest discover -s tests/latex-audit -v
python3 skills/hci-academic-writing/scripts/latex_audit.py tests/latex-audit/fixtures/valid/main.tex
python3 skills/hci-academic-writing/scripts/latex_audit.py tests/latex-audit/fixtures/broken/main.tex --json
```

The audit requires only Python 3.9+ standard-library modules. It prints to stdout and does not write files, compile, run shell commands, contact services, or upload manuscript content. Exit 1 means static errors were found; warnings alone exit 0. Argument usage errors follow argparse's exit 2 convention. Paths resolve from `--project-dir`, which defaults to the root file's parent and should match the compilation working directory. Outside-project files and symlinks resolving outside that directory are not read.

The valid fixture is an ACM manuscript with two section files, a real cited publication, references, masked literal examples, and one scoped authoring TODO in a comment. It makes no invented study-result claims. The broken fixture deliberately includes a missing file, include cycle, duplicate label, duplicate bibliography key, unknown citation, and unresolved reference. Unit tests also cover no mutation, CLI exits, BibTeX comments and parentheses, optional citation arguments, inline/environment literals, dynamic paths, conditionals, external references, root-relative include resolution, path boundaries, and post-document content.

The parser does not expand TeX, read packages, implement custom commands, infer generated labels, honor conditional branches or `includeonly`, resolve import-package directory state, or validate full BibTeX grammar. Recognized macro/conditional/import constructs produce warnings and downgrade potentially execution-dependent errors. Unrecognized custom macros and custom verbatim environments may be missed. Repeated includes are inspected once and reported; repeated expansion is not modeled. Bibliographic correctness, factual attribution, semantic reference intent, and actual TeX correctness require separate review. TODO detection includes ordinary comments but excludes supported literal environments; TODOs after the document terminator remain authoring reminders. A zero-error report is not proof of successful compilation.

A separate fixture build was run on 2026-10-30 with latexmk 4.86a, pdfTeX from TeX Live 2025, and acmart 2.12. It completed with citation/reference resolution; the final log had only the expected disabled-shell-escape warning. The audit itself never invokes this command. To reproduce the fixture-only build, create an output directory under `.local`, enter `fixtures/valid`, and use an absolute output path:

```sh
latexmk -norc -pdf -interaction=nonstopmode -halt-on-error \
  -latexoption=-no-shell-escape -outdir=/absolute/repo/.local/latex-audit main.tex
```

`-norc` disables latexmk configuration loading; outputs belong in ignored `.local`, not in the fixture directory. The compilation check is appropriate for this inspected fixture, not an instruction to compile arbitrary user projects automatically.
