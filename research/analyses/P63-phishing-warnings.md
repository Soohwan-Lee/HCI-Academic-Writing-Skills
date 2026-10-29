# P63 — You've Been Warned

Egelman, Cranor and Hong, CHI 2008, Carnegie Mellon University. DOI
10.1145/1357054.1357219. [Institutionally hosted teaching copy](https://css.csail.mit.edu/6.566/2012/readings/youve-been-warned.pdf).
Full substantive text read; PDF pp. 5 and 7 rendered for paragraph verification.
Award unverified. The browser versions and interface details are historical, not
current browser-security recommendations.

## Contribution and architecture
The central contribution is empirical knowledge about responses to browser
phishing warnings, with theory-informed explanation and design recommendations.
The researchers create attack scenarios as experimental materials; this does not
make a new anti-phishing system the principal contribution. They apply the existing
Communication–Human Information Processing model rather than introduce that model.

Order: Introduction → Background → A Model for Warnings → Methodology → Results
and Analysis → Discussion → Conclusion. Background explains phishing, defenses and
prior warning studies. A separate model section defines stages of attention,
comprehension, attitudes, motivation and behavior before the study operationalizes
them. Results revisit these stages rather than following questionnaire order.
Discussion changes from diagnosing observed failures to proposing interface
responses. The theory therefore connects motivation, measurement, interpretation
and implications across the whole paper.

The abstract describes active/passive warnings, the empirical question, simulated
attack, headline behavioral results, and the explanatory framework. Introduction
establishes the problem, distinguishes technical detection from effective user
response, identifies evidence lacking for newer warnings, then previews the study
and findings. Previous work does more than establish popularity: earlier passive
indicators and study contexts establish the relevant contrast. The gap concerns
how and why warnings succeed or fail, not simply whether a particular browser has
been studied before.

## Evidence and inferential boundaries
Sixty participants contribute to analysis after ten arrivals were excluded because
the emails did not arrive. Participants are assigned by their existing browser
preferences, not randomly to browsers. Purchase order is randomized; these are
different design decisions. Comparisons of reported experience and demographics
cannot establish absence of selection bias merely because tests are nonsignificant.
Warning notice, reading, understanding, following a link and submitting information
are separate outcomes with different denominators. Some questions were introduced
partway through collection; their smaller sample must remain visible.

The attack is deliberately timed to purchases in a laboratory task. Its high email
response rate is not a population estimate of everyday phishing susceptibility.
Observations, think-aloud comments and exit responses help interpret behavior, but
proposed habituation mechanisms are not isolated by randomized manipulation of
warning history. Likewise, a nonsignificant passive-warning comparison does not
prove equivalence or universal uselessness. These are useful negative examples of
claims an editing assistant should qualify, even in an influential paper.

Discussion recommendations follow identifiable observed problems: ignored passive
messages, unclear choices, repeated dismissal, misplaced trust, and familiarity
with other warnings. However, the combined redesigned interface is not evaluated.
Keep a recommendation distinct from a demonstrated intervention effect. No actual
credentials were collected; do not turn the study description into an account of
retaining participants' sensitive account data.

## Micro-analysis A: a qualification that does not remove confounding
PDF p. 5, Participants, locator “We were initially concerned”. Four sentences.
S1 identifies self-selection as a validity concern. S2 reports nonsignificant
experience comparisons. S3 gives equal novice counts in the active conditions.
S4 restates that equality. Flow: **concern → diagnostic comparison → concrete
balance information → local conclusion**. The preceding paragraph defines groups;
the next subsection describes scenarios. This placement makes a design limitation
visible, but a stronger rewrite should not treat these diagnostics as randomization.
The last sentence also repeats rather than substantially advances S3.

## Micro-analysis B: observed episode to bounded design interpretation
PDF p. 7, Attention, locator “Upon seeing the warnings”. Six sentences.
S1 gives two participants' immediate behavior. S2 follows their return and repeated
dismissal. S3 extends the sequence until abandonment. S4 supplies their explanation.
S5 reinterprets the episode as protection despite failed comprehension. S6 derives
a possible design principle. Flow: **episode → repetition → outcome → participant
account → analyst interpretation → implication**. It follows aggregate reading
results and precedes habituation analysis. Argument-last structure is productive:
the surprising interpretation becomes understandable through the preceding episode.

## Transfer and exception
When a framework genuinely guides an empirical study, carry its constructs through
measurement and analysis, while distinguishing the borrowed framework from the new
findings. Pair aggregate patterns with explanatory observations without promoting
those accounts into proven mechanisms. Preserve denominator shifts and assignment
limitations during compression. This architecture is less suitable when exploratory
interpretation develops the framework only after data collection; report that
sequence honestly instead of manufacturing an a priori theoretical design.
