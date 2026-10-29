# P58 — The Aligned Rank Transform

Wobbrock, Findlater, Gergle and Higgins, CHI 2011.
[Author-hosted PDF](https://faculty.washington.edu/wobbrock/pubs/chi-11.06.pdf).
Full four-page text read; printed p. 145 rendered. University of Washington,
Northwestern University and Kansas State University. Award unverified. A short
method-paper example, excluded from long-paper allocation guidance.

## Contribution and structure
The paper adapts and generalizes a statistical procedure for HCI researchers,
provides tools, and illustrates use by reexamining published data. Its primary
knowledge object is a method, with implementation enabling adoption. It does not
claim to invent rank transformation itself. Its three contributions explicitly
separate generalization, software and reanalysis.

Structure: Introduction → Aligned Rank Transform for N Factors (background,
procedure, correctness checks) → ARTool and ARTweb → Re-examination of Data
(three cases, limitations) → Conclusion. Related literature is integrated into
the problem statement and methodological background. There is no generic user
study evaluating whether researchers like the tool. The warrant instead concerns
methodological antecedents, specified operations, checkable intermediate outputs
and illustrative utility. Each kind supports a different claim.

The abstract begins with a recurrent analytical difficulty, explains why familiar
alternatives cannot answer the targeted question, identifies availability and
complexity barriers, introduces the procedure, explains its practical entry point,
and states generalization, tools and reanalysis. Introduction follows the same
problem-to-method logic with a comparison table. The table supplies dimensions
relevant to method choice rather than a catalogue of software features. Its
historical comparisons are not a current inventory of statistical practice.

## What the examples establish
Background credits the existing aligned-rank literature and distinguishes it from
ordinary rank transformation. The procedure is written as ordered operations,
with notation, an example table and explicit instructions about which transformed
outcome corresponds to which effect. Correctness checks are placed next to the
procedure. Tool outputs expose intermediate aligned data as well as ranks, so
users can inspect the operation instead of receiving only a final statistic.

The reanalysis introduction explicitly says these examples show utility and
relevance; mathematical correctness is not being proven by three favorable
examples. Cases illustrate different analytical needs rather than three arbitrary
applications. The limitations paragraph identifies tied values, meaningful skew
and design-dependent alignment concerns. A writing assistant should preserve this
separation of scope, procedural auditability and illustrative demonstration.
It should not recommend choosing an analysis because it produces significance.

## Micro-analysis A: give each demonstration an evidential job
Printed p. 145, Re-examination of Data opening, locator “In this section”. Five
sentences, visually checked. S1 announces reanalysis of published data. S2 narrows
the purpose to utility and relevance while attributing prior methodological
validation. S3 assigns the first case an interaction-analysis role. S4 assigns the
second a distributional-assumption role. S5 assigns the third a repeated-measures
role. Flow: **activity → warrant boundary → three distinct demonstrations**.
The prior section describes software; the next subsection supplies the first case.
The roadmap is informative because the cases answer different objections, not
because it enumerates everything the paper contains.

## Micro-analysis B: turn validation requirements into tool design
Same page, Ensuring Correctness paragraph, locator “ART users have”. Five
sentences (including the parenthesized sentence), visually checked. S1 announces
two checks. S2 describes the first and its tool support. S3 describes the second.
S4 qualifies which intermediate form makes that check clearer. S5 explains why
the software exposes both forms. Flow: **checkability claim → operation → second
operation → technical qualification → interface consequence**. It follows the
procedure and precedes software description. Thus the implementation is motivated
by the methodological need rather than appearing as an unrelated artifact.

## Transfer and exception
For a method contribution, state what is inherited, what is generalized, what
inputs and assumptions are required, how the procedure works, what checks users
can perform, and what demonstration does or does not establish. Keep a usable
explanation alongside formal notation. This is a rhetorical exemplar, not a
statistical cookbook: historical post-hoc advice and assumptions must not be
copied into a new analysis without current methodological verification. A skill
must never silently change the user's statistical analysis on the strength of
this writing example. Empirical treatment papers and critical essays require
different evidence and need not reproduce its procedural architecture.
