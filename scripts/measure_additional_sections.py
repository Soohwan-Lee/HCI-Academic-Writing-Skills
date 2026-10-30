#!/usr/bin/env python3
"""Read-only, version-bound section estimates for three reviewed PDFs.
Print metadata/counts to stdout; never emit or write extracted source text.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata

TOKEN = re.compile(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*")
ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def normalize(text, key, page):
    text = unicodedata.normalize('NFKC', text).replace('\u00ad', '')
    if key == 'P61-accessibility-review':
        text = re.sub(r'\n' + str(page) + r'\s*$', '', text)
    text = re.sub(r'(?<=[A-Za-z])-\s*\n\s*(?=[a-z])', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def locate(page, marker):
    if marker is None:
        return 0
    if page.count(marker) != 1:
        raise ValueError('Non-unique section marker; inspect extraction version')
    return page.index(marker)


def measure(pdf_dir):
    corpus = {x['id']: x for x in json.loads((ROOT / 'research/corpus.json').read_text())}
    output = []
    for key in ('P61-accessibility-review', 'P64-typing', 'P80-inform'):
        path = pdf_dir / (key + '.pdf')
        checksum = sha(path.read_bytes())
        if checksum != corpus[key]['sha256']:
            raise ValueError(key + ': PDF differs from reviewed corpus hash')
        proc = subprocess.run(['pdftotext', str(path), '-'], capture_output=True, text=True)
        if proc.returncode:
            raise ValueError(key + ': extraction failed')
        pages = [normalize(s, key, i) for i, s in enumerate(proc.stdout.split('\f'), 1)]
        sections, used = [], []

        def section(name, spans, note=None):
            pieces, selectors = [], []
            for page_number, start, end in spans:
                page = pages[page_number - 1]
                a = locate(page, start)
                b = len(page) if end is None else locate(page, end)
                if not 0 <= a < b <= len(page):
                    raise ValueError('Invalid section span')
                for prior_page, prior_a, prior_b in used:
                    if page_number == prior_page and max(a, prior_a) < min(b, prior_b):
                        raise ValueError('Overlapping section spans')
                used.append((page_number, a, b))
                part = page[a:b].strip()
                pieces.append(part)
                selectors.append(dict(pdf_page=page_number, normalized_page_sha256=sha(page),
                                      start_character_inclusive=a, end_character_exclusive=b,
                                      selected_text_sha256=sha(part)))
            text = ' '.join(pieces)
            row = dict(section=name, tokens=len(TOKEN.findall(text)), selectors=selectors,
                       normalized_section_sha256=sha(text))
            if note:
                row['boundary_note'] = note
            sections.append(row)

        def span_range(first, start, last, end):
            return [(p, start if p == first else None, end if p == last else None)
                    for p in range(first, last + 1)]

        if key == 'P61-accessibility-review':
            bounds = [(1, '1 INTRODUCTION'), (2, '2 BACKGROUND AND RELATED WORK'),
                      (5, '3 METHOD'), (9, '4 RESULTS'), (17, '5 DISCUSSION'),
                      (20, '6 CONCLUSION'), (21, '7 ACKNOWLEDGMENTS')]
            names = ['Introduction', 'Background and Related Work', 'Method', 'Results', 'Discussion', 'Conclusion']
            for name, (first, start), (last, end) in zip(names, bounds, bounds[1:]):
                section(name, span_range(first, start, last, end))
            note = ('Single-column manuscript permits main-section boundaries. Footnotes remain at extracted page positions: '
                    'the introduction-linked data-access footnote on p.2 falls inside the extracted related-work span. '
                    'These are layout-based section estimates, not exact rhetorical allocations.')
            checked = [1, 2, 5, 9, 17, 20, 21]
        elif key == 'P64-typing':
            section('Introduction', [(1, 'INTRODUCTION', 'Permission to make digital'),
                                     (1, 'This paper presents new data', None),
                                     (2, None, 'BACKGROUND AND RELATED WORK')])
            section('Background and Related Work', [(2, 'BACKGROUND AND RELATED WORK', None)])
            section('Data Collection + Preprocessing and Data Analysis', [(3, None, None), (4, None, None)],
                    'Aggregate avoids assigning the p.4 floated bigram table to Data Collection merely because it precedes the Preprocessing heading. Includes p.3 collection figure/table.')
            section('Results + Keystroke-Level Clustering + Summary', span_range(5, None, 10, 'THE 136M KEYSTROKES DATASET'),
                    'Aggregate includes p.5 results table/figure before RESULTS; p.8 clustering figure before its heading; p.9 summary content interleaved before SUMMARY. No separate result/discussion percentages are asserted.')
            section('The 136M Keystrokes Dataset', [(10, 'THE 136M KEYSTROKES DATASET', 'ACKNOWLEDGEMENTS')])
            note = 'Two-column extraction interleaves floats and prose; ambiguous adjacent main sections are deliberately aggregated.'
            checked = [1, 2, 3, 4, 5, 8, 9, 10]
        else:
            section('Introduction + Contributions + Related Work',
                    [(1, 'INTRODUCTION', 'Past research on shape displays'),
                     (1, 'The rich variety of physical', 'Author Keywords'),
                     (1, 'To overcome these limitations', None)] +
                    span_range(2, None, 3, 'DYNAMIC AFFORDANCES AND CONSTRAINTS'),
                    'P.1 INTRODUCTION is extracted before abstract prose; select its heading and two prose spans separately. P.2 contribution bullets appear after RELATED WORK in extraction, so the adjacent sections are aggregated. Front-page teaser caption excluded.')
            section('Dynamic Affordances and Constraints', span_range(3, 'DYNAMIC AFFORDANCES AND CONSTRAINTS', 6, 'DEMONSTRATION APPLICATIONS'))
            section('Demonstration Applications', span_range(6, 'DEMONSTRATION APPLICATIONS', 7, 'IMPLEMENTATION'))
            section('Implementation', span_range(7, 'IMPLEMENTATION', 9, 'DISCUSSION AND FUTURE WORK'))
            section('Discussion and Future Work', [(9, 'DISCUSSION AND FUTURE WORK', 'CONCLUSIONS')])
            section('Conclusions', [(9, 'CONCLUSIONS', 'ACKNOWLEDGMENTS')])
            note = 'Front-page abstract/keywords/rights and teaser are excluded by explicit disjoint spans; later captions and figure text remain.'
            checked = [1, 2, 3, 6, 7, 9]
        total = sum(s['tokens'] for s in sections)
        for s in sections:
            s['percent_of_extracted_body'] = round(100 * s['tokens'] / total, 2)
        output.append(dict(id=key, pdf_sha256=checksum, analyzed_version=corpus[key]['analyzed_version'],
                           extracted_body_tokens=total, sections=sections, boundary_note=note,
                           visually_checked_boundary_pages=checked,
                           visual_verification='Single analyst inspected rendered boundary pages; replay does not reperform visual judgment'))
    return dict(status='Three purposive extracted-body examples; not prose-only counts, ACM counts, target allocations or venue/type norms',
                extraction=dict(tool=subprocess.run(['pdftotext', '-v'], capture_output=True, text=True).stderr.splitlines()[0], command='pdftotext SOURCE.pdf -', page_split='form feed, one-based pages',
                                normalization=['Unicode NFKC', 'remove soft hyphens',
                                               'P61 only: remove trailing standalone page number matching PDF page',
                                               'join hyphen + line break between ASCII letter and lowercase ASCII letter',
                                               'collapse whitespace; strip; join selected spans with one space'],
                                dehyphenation_regex=r'(?<=[A-Za-z])-\s*\n\s*(?=[a-z])', token_regex=TOKEN.pattern,
                                includes='headings, numeric citations, captions, table/figure labels and numbers, footnotes at extracted positions',
                                excludes='abstract, authors/title/keywords, rights notices, acknowledgments, references, appendices; P80 front-page teaser',
                                offsets='Python Unicode character offsets in normalized page; end exclusive'), papers=output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf_dir', type=Path)
    parser.add_argument('--check', type=Path, help='compare generated JSON to saved metadata; no writes')
    args = parser.parse_args()
    try:
        result = measure(args.pdf_dir)
        if args.check:
            if result != json.loads(args.check.read_text()):
                raise ValueError('Saved measurements differ from replay')
            print(json.dumps(dict(status='pass', papers=len(result['papers']))))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps(dict(status='error', reason=str(exc))))
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
