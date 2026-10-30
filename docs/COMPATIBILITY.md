# Installation and host compatibility

This package uses a `SKILL.md` file with `name` and `description` frontmatter,
relative Markdown references, and a bundled Python audit script. It does not need
host-specific settings, hooks, credentials, or plugins. Its references and script
are copied together; the research corpus and private PDFs are not required to
load the skill.

## Official locations

Verified against official documentation on **2026-10-30**. Append
`hci-academic-writing/` to each directory below.

| Installer host | Project directory | Personal/global directory |
|---|---|---|
| `codex` | `.agents/skills/` | `~/.agents/skills/` |
| `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| `antigravity-app` | `.agents/skills/` | `~/.gemini/config/skills/` |
| `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| `antigravity-ide` | `.agents/skills/` | `~/.gemini/config/skills/` |

Codex's official documentation identifies repository and personal `.agents/skills`
locations. Its installed CLI README was checked first but did not document skill
search paths; the official web documentation supplied these locations. This
installer targets the current documented paths, not every legacy location a host
might still recognize. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)

Claude Code documents project and personal `.claude/skills` bundles and explicit
invocation with `/hci-academic-writing`. Local filesystem installation is distinct
from claude.ai account synchronization and cloud/Cowork availability. This installer
only manages local files. [Claude Code: Skills](https://code.claude.com/docs/en/skills)

Antigravity documents `.agents/skills` for project discovery, with separate global
locations for App/IDE and CLI. Its `.agent/skills` project path and IDE's older
`~/.gemini/antigravity/skills` remain documented compatibility paths, but the
installer writes the current paths in the table. Select the actual surface rather
than assuming one global folder serves all products.
[Google Antigravity: Agent skills](https://antigravity.google/docs/skills)

Codex and Antigravity project installations share the same destination. Installing
for both is an identical-content no-op after the first copy. Claude Code needs its
own `.claude` copy. This does not synchronize later edits between copies.

## Preview and install

Python 3.9 or later is sufficient; no third-party Python packages are needed.
Run from this repository, supplying the existing target project explicitly:

```sh
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper
python3 scripts/install_skill.py --host codex --scope project --project-root /path/to/paper --apply
python3 scripts/install_skill.py --host claude-code --scope project --project-root /path/to/paper --apply
python3 scripts/install_skill.py --host antigravity-ide --scope project --project-root /path/to/paper --apply
```

Every command without `--apply` is a dry run. It validates the source, checks for
conflicts, and prints the destination without creating directories. For a personal
installation, select global scope explicitly:

```sh
python3 scripts/install_skill.py --host claude-code --scope global
python3 scripts/install_skill.py --host claude-code --scope global --apply
```

`--home-root /path/to/isolated/home` selects an alternative existing home root,
primarily for fixtures or explicitly managed environments. It does not change any
environment variables. Global scope otherwise uses the current user's home.

The installer refuses a different existing destination, including extra files,
and does not merge or overwrite it. A destination with matching file bytes and
permission modes is an idempotent no-op. Review and relocate an old installation
outside every host skill-search directory before installing an updated copy.
Renaming a backup inside a scanned skills directory can leave multiple discoverable
bundles; retain backups elsewhere. Source/destination overlap, symlinked
paths or entries, and special files are rejected. On systems with symlinked temp
paths, supply the resolved real path. No global settings are edited.

Copies use exclusive destination creation and verify copied bytes/modes. On a
copy failure, the newly created destination is removed; newly created empty parent
directories may remain. This is a local installer, not a security boundary against
another process concurrently replacing filesystem paths. Do not run simultaneous
installations into the same tree.

## What has actually been tested

| Evidence | Status |
|---|---|
| Official `SKILL.md` format and locations | Documentation verified for the hosts above |
| Copy into each project/global layout | Tested in isolated temporary directories |
| Relative links and complete bundle | All current inline Markdown file links resolve within each copied bundle |
| Dry run, idempotence, conflicting files, symlinks, overlap | Automated tests pass |
| Real global installation | Not performed |
| Host discovery/menu visibility for this installed package | Not tested by these installer tests |
| End-to-end manuscript editing in each host | Not established by installer tests |

Run the tests with:

```sh
python3 -m unittest discover -s tests/install -v
```

The local link checker supports this bundle's simple inline Markdown links and
frontmatter; it is not a general Markdown/YAML validator. It checks file targets,
not heading-anchor validity or remote URL availability. The bundled LaTeX auditor
uses Python; compiling a manuscript separately requires the user's TeX toolchain.

After installation, start a fresh host session in the target project, inspect its
available skills, and request `hci-academic-writing` for a small scoped edit. Check
that the intended bundle and references were loaded before attributing behavior to
it. Discovery and task performance are separate tests: a visible skill name alone
does not establish writing quality. No Claude invocation or credential changes
are needed to run the installer or its tests.

## Subsequent live Claude Code evidence

Two isolated ACM editing tasks loaded the installed skill and relevant references
through explicit named requests and file reads. Both edits passed scope/evidence
inspection, lexical audit and compilation. The initialization skill catalogs did
**not** list the package, so automatic discovery and slash invocation remain
unverified in that restricted configuration. Codex and Antigravity live discovery/
editing have not been tested. See [file-edit results](../tests/behavior/README.md)
and [semantic failures](../tests/behavior/SEMANTIC-REPORT.md). Documentation and
filesystem layout compatibility should not be read as equal behavioral validation.
