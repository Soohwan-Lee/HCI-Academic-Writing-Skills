# Contributing

Use an issue or pull request to propose a correction, missing research tradition,
contrasting exemplar, or reproducible authoring failure. Explain which writing
decision it changes. Famous authors and awards can guide discovery; they are not
proof of a general rule or grounds for excluding less-visible research.

## Adding an exemplar

1. Check for duplicate title/DOI and fit with the coverage audit. Identify venue,
   contribution, method and form separately; retain substantive hybrids.
2. Read the full main text and inspect relevant rendered pages. Record exact
   source URL, version, date and SHA-256. Verify award claims independently.
3. Write original analysis of the contribution contract, section architecture,
   opening/positioning, evidence-to-claim links, paragraph and sentence functions,
   and a counterexample or limit. Give page/section locators. Do not redistribute
   full text or extensive excerpts.
4. Add the reviewed metadata and analysis, regenerate the corpus index with
   `python3 scripts/build_corpus_index.py`, and update coverage and relevant docs.
   The current generator's snapshot count must be updated when corpus size changes.
5. Record the review and sampling decision. Keep changes small and reviewable.

Numeric style claims require actual measurements with clear inclusion/exclusion,
source identity, extraction protocol and inspected boundaries. Rhetorical coding
is not a frequency measurement. Do not pool incompatible counting protocols.

## Changing the skill

Keep the entry short enough for selective loading. Put route-specific detail in
references, preserve portable relative links, and avoid machine-specific paths.
State whether advice is source-observed, editorial or a current submission rule.
Run installer/auditor tests and the index check listed in the README. For changed
behavior, test a realistic task and inspect semantic meaning, not only tokens.
Report failures and distinguish AI inspection from human evaluation. Live model
calls cost subscription usage; the opt-in behavior runner never uses API fallback.

## Source and privacy boundaries

Only public metadata and original analytical writing belong here. Do not commit
PDFs, publisher text caches, Zotero databases, account data, API keys, private
manuscripts or model transcripts. Synthetic fixtures must be marked synthetic.
Original contributions follow the repository license; cited papers retain their
own rights. An analysis note should not imply endorsement by its authors or venue.
