# P26 — BINGO / Reason Bins

**Provenance.** Beltran, Huang, Abouzied, and Nandi, *Don’t Just Swipe Left, Tell Me Why: Enhancing Gesture-based Feedback with Reason Bins*, IUI 2017, DOI 10.1145/3025171.3025212. Full author-hosted PDF: <https://arnab.org/files/bingo_iui17.pdf>. Best Paper Honourable Mention verified by the [official awards page](https://iui.acm.org/2017/awards.html). Single-analyst coding of this twelve-page version; micro passages on PDF pp.5 and 9–10 visually checked. Do not treat award status as validation of every claim.

## Architecture and entry

The primary object is a gestural query-refinement technique with a bin-generation mechanism. Main sequence: **Introduction → Motivating Use Cases → Related Work → Overview of the BINGO System → Evaluation → Conclusion → Future Work**, then acknowledgments/references. Evaluation is organized by targeted search, survey search, and exploration; each needs different evidence. System description separately motivates interface choices and explains database, bin generation, and ranking.

The abstract moves from the persistence of query-specification difficulty to keyboardless interaction constraints, the richer swipe mechanism, efficient bin generation, design rationale, and evaluation-based claims. The introduction uses mobile search context, gesture affordances, then a document-review scenario whose binary feedback cannot express a reason (pp.1–2). The proposed reason bins resolve that specific ambiguity. Two subsequent use cases derive requirements for refinement, vocabulary discovery, changing intent, and exploration (pp.2–3). This extra motivating section supplies design criteria without forcing a formal RQ list.

## Positioning

Related Work (pp.3–4) covers reformulation/autocompletion, faceted exploration, recommendation algorithms, visual querying, and touch interfaces. The crucial boundary is explicit: the contribution is query specification, not a superior underlying document-retrieval model. The review connects suggestion presentation to distraction and compares expressiveness with interaction effort. Some prior-work discussion already previews outcomes; a new manuscript should ensure this does not obscure which claims are literature-grounded and which arise from its own evaluation.

## Claims, support, and limits

The balance claim is supported by different comparisons: graph/simulation analysis for targeted retrieval, a 20-person study of survey tasks against keyword-only and pure-swipe interfaces, and a 21-person between-groups exploration study. Controls retain similar visual appearance and underlying retrieval. The warrant is that richer feedback can occupy a useful point between free-form keyword expressiveness and fast binary decisions.

The evidence does not establish dominance on every task. Survey results expose speed/precision tradeoffs, and the exploration hypothesis is not supported by games-saved counts (p.10). Targeted-search simulations make assumptions about available target terms and user choice, so their interaction counts are not observed human search behavior. Precision is operationalized through users' saved documents, not independent relevance judgments. The evaluated datasets are domain-specific, and general web search is expressly outside scope. Do not convert a nonsignificant difference into equivalence or the use of swipe interactions into demonstrated benefit on every device form factor.

## Micro-analysis 1: local design rationale

**p.5, Interface Design Considerations, item 6; opening “An earlier BINGO prototype”.** Three sentences after the item label:

- **S1:** Describes an earlier scroll-dependent bin policy.
- **S2:** Reports the confusion associated with changing bins.
- **S3:** States the resulting tradeoff and stable-bin design decision.

Relation: **prior design → experienced problem → revised constraint**. It enters within a list of independently motivated interface choices and exits to a different choice about display counts. This local, chronological explanation is more informative than simply declaring the final feature intuitive. The source does not provide a fully specified study for that formative observation, so do not upgrade it to controlled evidence.

## Micro-analysis 2: preserving a failed hypothesis

**pp.9–10, Evaluation / Exploration / Games Saved; opening “Figure 7 illustrates the number”.** The paragraph begins on p.9 and continues on p.10; both text and page layout were checked. Eight sentences: **S1** points to the games-saved figure; **S2** states the expected advantage; **S3** reports that the data do not support it; **S4** introduces the survey as explanatory follow-up; **S5** specifies a keyword-group rating question; **S6** reports agreement; **S7** adds perceived ease; **S8** supplies the BINGO counterpart. Relation: **expectation → contrary result → follow-up evidence → comparative description**. It follows the participant/method paragraph and precedes additional dimensions of exploratory behavior. The survey contextualizes the null result; it does not erase it.

## Transfer and exception

For intelligent interaction artifacts, separate algorithm novelty from interaction novelty and align each task type with its evaluation. Explain deliberate tradeoffs, including choices that sacrifice algorithmic freedom for interaction stability. Preserve unsuccessful hypotheses in the results narrative. This paper demonstrates why a single undifferentiated claim of “better search” and a single generic Results template would misrepresent the contribution.
