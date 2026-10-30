# S10 — Resource construction, characterization and task-specific utility

Source: [P132 UICrit](../analyses/P132-uicrit.md), UIST 2024, author PDF.
Re-read hierarchy and mapped passages 2026-10-31. Prior main-text/appendix and
visual inspection are recorded in P132. The resource is the central reusable
object; downstream prompting is a distinct utility branch.

## 1. Actual hierarchy

| Section | Nested organization | Argumentative job |
|---|---|---|
| Introduction | Resource need, scope and contribution | Explain what missing feedback data prevents |
| Related work | UI datasets; automated evaluation; feedback frameworks/guidelines | Resource lineage, target task, annotation semantics |
| Data collection, §3 | Method; collection results | How the resource was produced and what records contain |
| Dataset analysis, §4 | critique topics; screen tasks; comment spatial scale; app-level rating relations/consistency | Characterize coverage and structure before claiming utility |
| Application, §5 | region-of-interest feedback; whole-screen feedback; final performance validation | Two enabled tasks and an expert-rated comparison |
| §5.1 region task | prompt → example selection → results | First task's dependency chain |
| §5.2 whole-screen task | prompt → example selection/results → visual prompting/results | Adds a localization problem and its technical branch |
| §5.3 validation | method → results | A separate comparison of the selected configuration |
| Discussion, §6 | observed utility; prospective applications; collection scalability | Distinguishes demonstrated use from possible reuse |
| Limitations, §7; Conclusion, §8 | Boundaries; recap | Scope and resulting resource |

The source does not have a single undifferentiated Evaluation section. Characterization,
task experiments and final judging answer different questions. A resource paper
can be damaged by moving all construction detail to an appendix before readers
understand its units, provenance and representation.

## 2. Complete local paragraph maps

### §3.2 collection results, p.5: one paragraph
Report effort, complete-record and critique totals, fields per screen, illustrative
records and a handoff to characterization. This closes construction by specifying
the delivered object, not by asserting every intended benefit.

### §4.1 critique topics, p.5: three prose paragraphs plus category list

1. Define the characterization purpose and computational grouping/visualization.
2. Explain interpretive coding and analyst roles, then introduce the named groups.
3. After the list, compare coverage with the annotation heuristics, distinguish
   missing or inapplicable concerns, and explain partial coverage.

The list's role is to expose the resulting taxonomy. The final paragraph makes
it useful: it interprets what the dataset can represent. Reported category totals
have an unresolved discrepancy recorded in P132; do not silently repair them.

### §4.2 screen tasks, pp.5–6: four prose paragraphs plus category list

1. Explain the analogous task analysis and why it matters for selecting examples.
2. Introduce the cluster visualization and task categories.
3. After the list, compare against an external task space and identify a gap.
4. Distinguish app category from the task of an individual screen, show the second
   distribution and identify underrepresented app categories.

The last paragraph adds another level of analysis; an app-category plot cannot
replace a task-category analysis. Their adjacency helps readers understand this.

### §6.1 utility, pp.12–13: two paragraphs

1. Interpret the targeted-sampling result and propose why the resource helps.
2. Relate expert judgment/preference to that result, retain the gap to human
   critiques and identify a prospective avenue. This is not an isolated data-only
   treatment effect; examples and visual prompting change together.

## 3. Sentence-level maps

**§3.2, five sentences:** collection effort → delivered totals → record schema →
concrete examples → next analysis. The noun chain moves from the collection to
records to examples; the final sentence hands off a new reader question rather
than adding generic importance. The schema sentence is long because it specifies
a reusable object; an agent can use a table if that improves legibility.

**§6.1 first paragraph, three sentences:** observed task contrast → probable
resource-related explanation → implication for feedback generation. The second
sentence is the inferential bridge. Keep it conditional unless separately tested;
otherwise the paragraph's fluency can conceal a change from result to explanation.

## 4. Conditional transfer

For resource contributions, consider construction → characterization → enabled
tasks → utility interpretation. Organize task branches with their own prompt/model,
selection and results when they solve different problems. Separate development
experiments from final judging and describe shared data/raters where relevant.

For a benchmark, add actual task definitions, splits and metrics; for a design
repository, retrieval/reuse workflows may be more central than model scores. Neither
variant should copy this exact hierarchy without checking the knowledge claim.
Compare S07, where criteria precede an audit and automation is secondary: the
presence of a resource and tool does not settle which object should organize the paper.
