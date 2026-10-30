# Live file-edit behavior checks

These are two small, synthetic authoring tasks in an existing multi-file ACM
project, not a benchmark of HCI writing quality. The root is `chi26.tex`, which
includes separate related-work and results files. Unrelated macros, labels,
references and bibliography entries act as preservation sentinels. Numeric results
are explicit test inputs, not findings from a real study.

## Reproduce deliberately

```sh
python3 tests/behavior/run_claude.py --run
```

This makes **two real Claude Code subscription requests**. It requires an existing
subscription login and stops if authentication is not `claude.ai` with a subscription.
There is no API fallback. The child environment excludes every `ANTHROPIC_*` and
`CLAUDE_CODE_USE_*` variable, plus an externally supplied OAuth token override.
The parent's environment and authentication files are unchanged. The runner checks
authentication separately immediately before each request; it stores only the
method and subscription type in summaries, not account details or credentials.

Each task gets an isolated project under ignored `.local/behavior/`, a Git root,
and a project-local skill installed using the repository installer. No global
skill is installed. The prompt names the skill but does not embed its contents.
Claude receives only Read, Edit, Glob and Grep, with `--restricted`,
`acceptEdits`, no permission prompts, an empty strict MCP configuration, and no
user/project/local settings sources. Restricted mode confines file tools to the
working directory. The prompt additionally limits changes to one paragraph and
forbids builds, network and other files. Do not use `--bare`: in the tested CLI,
that mode bypasses subscription/keychain authentication.

Private stream logs, before/after paragraphs and metadata summaries remain under
`.local`. The runner reports file scope, citation/numeric preservation, structural
lines, absence of added TODOs, operational token count and observed SKILL.md reads.
It exits unsuccessfully if those mechanical criteria fail. A separate semantic review must inspect meaning, citation attachments, null-result interpretation and prose flow;
matching tokens alone cannot prove those properties. See
[expected-checks.json](expected-checks.json).

## Observed run: 2026-10-30

Claude Code **2.1.312** reported runtime model **claude-opus-5-5**. Both requests
verified **claude.ai / Pro** before launch; initialization reported no API-key
source. The model was read from runtime events, not inferred from a requested alias.

| Check | Existing-citation revision | Results compression |
|---|---|---|
| Actual edit completed | Yes | Yes |
| Only requested section file changed | Yes | Yes |
| Root, bibliography and other section preserved | Yes | Yes |
| Citation keys / numerical token sequence preserved | Yes | Yes |
| Added TODOs | None | None |
| Installed SKILL.md read observed | Yes | Yes |
| Entry present in initialization skill catalog | **No** | **No** |
| Local lexical audit | 0 errors; expected macro-expansion warning | Same |
| Actual ACM LaTeX compile | Passed | Passed |

The related-work revision moved a synthesis sentence before the two cited examples,
connected their different roles, and kept the workflow-specific gap. AI evaluator inspection
found the original claims and citation attachments intact, with no unsupported
strengthening or unnecessary verification TODO. It was a flow task, so its small
length increase is not a failure.

Results compression reduced the operational prose count from **119 to 78 tokens**
(limit 90). AI evaluator inspection confirmed the 24-person sample, both means, exact p value,
non-significance, both median times, both effort ratings, seven-point scale and
absence of an established score benefit. It introduced no mechanism or new finding.
Counts exclude the section/label line and comment; regex tokens include numerals
and treat internal apostrophes/hyphens as part of a token. This is not an ACM count.

After the model finished, the evaluator ran the bundled auditor and `latexmk`
with shell escape disabled, placing build outputs under `.local`. The auditor's
warning concerns the intentionally preserved macro definition; it is not a
compilation error. These checks were evaluator actions, not tools exposed to Claude.

## Interpretation and limits

This run demonstrates explicit named-skill **file loading and application**: logs
show Glob/Read access to the installed SKILL.md and relevant reference files.
It does **not** demonstrate automatic discovery or slash-command activation. The
initialization catalogs omitted this skill under the restricted configuration.
That observation is recorded without assuming why the host omitted it.

Two successful edits do not establish performance on whole papers, other research
traditions, different models, or future CLI versions. No no-skill control was run,
so the improvement cannot be causally attributed to the package. Host discovery
should be tested separately in an ordinary user session. Full model transcripts
and local account/path details are intentionally not published.

Semantic generation failures and iteration history: [report](SEMANTIC-REPORT.md). No independent human evaluation was performed.
