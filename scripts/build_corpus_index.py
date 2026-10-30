#!/usr/bin/env python3
"""Build the portable evidence index from reviewed public corpus metadata."""
import argparse
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'skills/hci-academic-writing/references/corpus-index.md'

def render():
    rows = json.loads((ROOT / 'research/corpus.json').read_text())
    assert len({r['id'] for r in rows}) == len(rows)
    text = '# Evidence lookup by contribution\n\n'
    text += ('107 purposively selected full-text rhetorical analyses, not 107 quantitative style measurements. '
             'Choose one or two cases matching the knowledge claim and writing problem. '
             'These links lead to public analytical notes; loading this index does not mean you have read those notes or the papers. '
             'The installed core skill works offline; linked evidence requires repository access or a network. '
             'Primary routes are navigation aids; the knowledge objects below preserve hybrids.\n\n'
             'Section/body estimates: P03, P07, P61, P64, P80, P98, P102. '
             'Paragraph-length subset: 32 paragraphs in 14 papers; no universal paragraph target follows. '
             'See the [measurement protocols](https://github.com/Soohwan-Lee/HCI-Academic-Writing-Skills/blob/main/research/measurements/README.md).\n\n')
    for route in sorted({r['primary_writing_route'] for r in rows}):
        text += f'## {route.capitalize()}\n\n| Analysis | Venue/year | Knowledge object | Source |\n|---|---|---|---|\n'
        for r in rows:
            if r['primary_writing_route'] != route: continue
            assert (ROOT / 'research' / r['analysis']).is_file()
            source = 'https://doi.org/' + r['doi'] if r.get('doi') else r['url']
            label = (r['id'].split('-')[0] + ' — ' + r['title']).replace('|','/')
            text += f"| [{label}](https://github.com/Soohwan-Lee/HCI-Academic-Writing-Skills/blob/main/research/{r['analysis']}) | {r['venue']} {r['publication_year']} | {r['primary_knowledge_object'].replace('|','/')} | [source]({source}) |\n"
        text += '\n'
    return text

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true');args=parser.parse_args()
    result=render()
    if args.check:
        if TARGET.read_text()!=result: raise SystemExit('Corpus index is stale')
        print('Corpus index matches 107 reviewed records')
    else: TARGET.write_text(result)
