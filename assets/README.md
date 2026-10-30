# Visual identity

`logo.svg` is original code-authored vector artwork: three evidence paths join a
manuscript page. It uses charcoal/teal, warm paper and muted vermilion. It is not
an ACM or conference mark. The SVG includes an accessible title and description.

`editorial-cover.png` is an AI-generated decorative cover created on 2026-10-30
using the built-in OpenAI image-generation tool, fresh-image mode with an opaque
background. It was visually inspected at full width. It is not a scientific figure,
data visualization or depiction of actual study evidence. No third-party reference
image was supplied. Exact generation prompt:

> Create a refined editorial illustration for the README cover of an open-source academic writing toolkit called HCI Academic Writing Skills. Wide landscape composition, sophisticated academic journal visual identity. Off-white archival paper background, charcoal ink, restrained deep teal and muted vermilion accents. A beautifully composed abstract arrangement of manuscript pages: some have fine typographic rule-like lines, others show small branching argument diagrams, a miniature human interaction schematic, annotations and linking threads. The visual metaphor is diverse research evidence becoming a coherent scholarly argument. Precise geometry combined with subtle printed-paper texture, generous whitespace, professional understated design, no futuristic robots, no circuit-brain imagery, no gradients, no glossy 3D. Do not render any readable text, letters, numbers, labels, publisher logos or fake charts. This is a decorative editorial cover, not a scientific data figure. Make the composition work at GitHub README width.

## README explanation diagrams

`writing-levels-en.svg` and `writing-levels-ko.svg` are original, code-authored
vector diagrams showing how the skill separates a paper's contribution from
method, topic, venue and format before connecting section, subsection, paragraph
and sentence planning in a stepped cascade. Their `-mobile.svg` counterparts
arrange the same anchor and cascade vertically for narrow screens. They are
instructional diagrams, not measured results or source-paper figures. Each has an
accessible title/description; README images also have alt text. The fixed
paper/teal/vermilion palette remains legible against light and dark page
backgrounds.

Regenerate all four diagrams with the standard-library-only script:

```sh
python3 scripts/assets/build_readme_diagrams.py
```

The original cover is retained unchanged as the sole decorative illustration.
The additional diagram explains the workflow; it does not imply four mandatory
sections or sentence-count rules. Header badges use Shields.io for descriptive
skill, Python-version and license labels, not CI status or endorsement claims.
