#!/usr/bin/env python3
"""Read two reviewed local PDFs and print descriptive section counts; write only with --out."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET

TOKEN = r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*"
# Coordinates are PDF points, top-left origin. Starts include numbered headings.
# Each tuple is (section name, PDF page, column: 0 left/single or 1 right, yMin).
SPECS = {
    'P98-accessible-collaboration': {
        'columns': 1, 'body_y': [90, 670],
        'abstract_box': [1, 0, 176, 486, 280],
        'first_page_body_stop_y': 537,
        'starts': [
            ['Introduction', 1, 0, 395.6],
            ['Related work', 2, 0, 614.7],
            ['Method', 5, 0, 147.9],
            ['Findings', 6, 0, 265.8],
            ['Discussion', 16, 0, 357.1],
            ['Conclusion', 19, 0, 505.4],
            ['STOP: acknowledgments', 20, 0, 97.1],
        ],
        'selection': 'Qualitative collaborative-accessibility study; six conventional main sections, long findings and theory-building discussion.',
    },
    'P102-dance-physicalisations': {
        'columns': 2, 'body_y': [85, 715],
        'abstract_box': [1, 0, 305, 306, 490],
        'starts': [
            ['Introduction', 1, 1, 332.5],
            ['The origin of the project', 2, 0, 319.2],
            ['Related work', 2, 1, 661.3],
            ['Methods', 4, 0, 540.7],
            ['Learning the Duncan dance repertoire and collecting data', 5, 0, 282.2],
            ['Designing the artefacts', 5, 1, 499.3],
            ['Interacting with the data', 11, 0, 194.8],
            ['Discussion', 13, 1, 282.2],
            ['Conclusion', 15, 1, 336.5],
            ['STOP: acknowledgments', 15, 1, 603.5],
        ],
        'selection': 'Retrospective autoethnography and design practice; preserves contextual, making and reflective sections rather than forcing IMRaD.',
    },
}


def tokens(words):
    # Keep extraction word boundaries: no speculative dehyphenation or prose repair.
    return len(re.findall(TOKEN, ' '.join(unicodedata.normalize('NFKC', w).replace('\u00ad', '') for w in words)))


def measure(pdf_dir, manifest_path):
    manifest = {r['id']: r for r in json.loads(manifest_path.read_text())}
    rows = []
    for paper_id, spec in SPECS.items():
        pdf = pdf_dir / (paper_id + '.pdf')
        checksum = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if checksum != manifest[paper_id]['sha256']:
            raise ValueError(f'{paper_id}: PDF checksum differs from reviewed version')
        raw = subprocess.check_output(['pdftotext', '-bbox', str(pdf), '-'])
        pages = ET.fromstring(raw).findall('.//{*}page')
        words, abstract = [], []
        ap, ax0, ay0, ax1, ay1 = spec['abstract_box']
        for page_number, page in enumerate(pages, 1):
            for w in page.findall('.//{*}word'):
                x, y = float(w.attrib['xMin']), float(w.attrib['yMin'])
                text = w.text or ''
                if page_number == ap and ax0 <= x < ax1 and ay0 <= y < ay1:
                    abstract.append(text)
                if not spec['body_y'][0] <= y < spec['body_y'][1]:
                    continue
                if page_number == 1 and y >= spec.get('first_page_body_stop_y', 10000):
                    continue
                column = int(spec['columns'] == 2 and x >= 306)
                # Full-width Figure 14 caption precedes §7 in both columns.
                if paper_id.startswith('P102') and page_number == 11 and y < 194.8:
                    column = 0
                words.append(((page_number, column, y), text))
        sections = []
        for start, stop in zip(spec['starts'], spec['starts'][1:]):
            selected = [t for key, t in words if tuple(start[1:]) <= key < tuple(stop[1:])]
            sections.append(dict(section=start[0], tokens=tokens(selected),
                                 start=dict(pdf_page=start[1], column=start[2], y_min=start[3]),
                                 end_exclusive=dict(pdf_page=stop[1], column=stop[2], y_min=stop[3]),
                                 opening_locator=start[0], end_locator=stop[0]))
        total = sum(s['tokens'] for s in sections)
        independent = tokens([t for key, t in words if tuple(spec['starts'][0][1:]) <= key < tuple(spec['starts'][-1][1:])])
        assert total == independent
        for s in sections:
            s['percent_of_extracted_body'] = round(100 * s['tokens'] / total, 2)
        rows.append(dict(id=paper_id, doi=manifest[paper_id]['doi'], sha256=checksum,
                         pdf_pages=len(pages), analyzed_version=manifest[paper_id]['analyzed_version'],
                         selection_reason=spec['selection'], abstract_tokens=tokens(abstract),
                         abstract_box=dict(pdf_page=ap, x_min=ax0, y_min=ay0, x_max=ax1, y_max=ay1),
                         extracted_body_tokens=total, sections=sections,
                         visual_boundary_verified=True,
                         visual_audit='All main-section starts and stops checked on rendered pages; single analyst, 2026-10-30.'))
    return dict(status='Two purposively selected descriptive extraction estimates; not population norms or prose-only budgets.',
                extraction_command='pdftotext -bbox SOURCE.pdf -',
                poppler_version=subprocess.check_output(['pdftotext', '-v'], stderr=subprocess.STDOUT, text=True).splitlines()[0],
                token_regex=TOKEN,
                normalization='Unicode NFKC per extracted word; remove soft hyphen; join words with spaces. No dehyphenation. Numeric citation tokens retained.',
                boundary_rule='Lexicographic (PDF page, column, yMin), half-open intervals. P98 single column; P102 split at xMin=306 PDF points. Coordinates in script and records.',
                includes='Main-section and subsection headings, prose, quotations, numeric citations, extractable captions, table/figure text, footnotes and their URLs.',
                excludes='Title/authors, abstract from body denominator, front matter and rights notices, running headers/footers, acknowledgments, references and appendices.',
                limitations='Line-end hyphenation may count as two tokens; PDF glyph fusion may count as one. Floating captions belong to the geometric section interval, not necessarily the section discussing them. P102 full-width Figure 14 caption explicitly assigned before §7. Counts cannot be treated as prose-only ACM word counts or universal 8000-word ratios. Different extraction protocols should not be pooled without harmonization.',
                papers=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf_dir', type=Path)
    parser.add_argument('--manifest', type=Path, default=Path('research/corpus.json'))
    parser.add_argument('--out', type=Path, help='Optional explicit JSON output; otherwise read-only and stdout only')
    args = parser.parse_args()
    result = json.dumps(measure(args.pdf_dir, args.manifest), ensure_ascii=False, indent=2) + '\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result)
    else:
        print(result, end='')


if __name__ == '__main__':
    main()
