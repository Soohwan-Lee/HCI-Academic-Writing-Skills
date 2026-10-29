#!/usr/bin/env python3
"""Read-only replay of reviewed PDF measurements; never emits source prose."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata

import measure_corpus as pilot

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*")


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def normalize(page):
    page = unicodedata.normalize('NFKC', page).replace('\u00ad', '')
    page = re.sub(r'(?<=[A-Za-z])-\s*\n\s*(?=[a-z])', '', page)
    return re.sub(r'\s+', ' ', page).strip()


def replay(pdf_dir, measurements):
    results, cache = [], {}

    def raw(key, checksum):
        if key not in cache:
            path = pdf_dir / (key + '.pdf')
            actual = digest(path.read_bytes())
            # Do not invoke external extraction on a mismatched version.
            if actual != checksum:
                raise ValueError('PDF checksum mismatch')
            proc = subprocess.run(['pdftotext', str(path), '-'], capture_output=True,
                                  text=True, check=False)
            if proc.returncode:
                raise ValueError('pdftotext failed (source output withheld)')
            cache[key] = (actual, proc.stdout)
        if cache[key][0] != checksum:
            raise ValueError('conflicting recorded PDF checksum')
        return cache[key][1]

    def check(label, action):
        try:
            details = action()
            results.append(dict(record=label, status='pass', **details))
        except (OSError, ValueError, KeyError, IndexError, AssertionError) as exc:
            # Assertion messages from pilot boundary code contain source locators;
            # only class is emitted, never arbitrary source/extractor content.
            results.append(dict(record=label, status='fail', reason=type(exc).__name__))

    counts = json.loads((measurements / 'counts.json').read_text())
    for row in counts['papers']:
        def verify_pilot(row=row):
            key = row['id']
            text = pilot.clean(raw(key, row['sha256']), key)
            spec = pilot.SPECS[key]
            total = pilot.count(pilot.between(text, *spec['body']))
            sections = [dict(section=name, tokens=pilot.count(pilot.between(text, a, b)))
                        for name, a, b in spec['sections']]
            if total <= 0:
                raise ValueError('empty body')
            for section in sections:
                section['percent_of_extracted_body'] = round(100 * section['tokens'] / total, 2)
            actual = dict(abstract_tokens=pilot.count(pilot.between(text, *spec['abstract'])),
                          extracted_body_tokens=total, sections=sections,
                          paragraph_tokens=[pilot.count(pilot.between(text, a, b))
                                            for a, b in spec['paragraphs']])
            if any(row[k] != v for k, v in actual.items()) or sum(s['tokens'] for s in sections) != total:
                raise ValueError('pilot numeric mismatch')
            return dict(kind='pilot', paragraphs=len(actual['paragraph_tokens']),
                        checks=['PDF hash', 'abstract/body/section tokens', 'section proportions', 'paragraph tokens'])
        check('counts.json:' + row['id'], verify_pilot)

    for name in ('systems-paragraphs.json', 'social-paragraphs.json', 'design-paragraphs.json'):
        data = json.loads((measurements / name).read_text())
        # Existing JSON documents double-escape backslashes in regex values.
        # Decode just this historical representation, not arbitrary escape sequences.
        pattern = data['extraction']['token_regex'].replace('\\\\', '\\')
        if pattern != TOKEN.pattern:
            raise ValueError('unsupported token specification in ' + name)
        for i, row in enumerate(data['records'], 1):
            def verify_paragraph(row=row):
                selector = row['extraction_selector']
                page_number = selector['page_one_based']
                if page_number < 1 or page_number != row['pdf_page']:
                    raise ValueError('invalid page selector')
                page = normalize(raw(row['paper_id'], row['pdf_sha256']).split('\f')[page_number - 1])
                if digest(page) != selector['normalized_page_sha256']:
                    raise ValueError('normalized page mismatch')
                spans = selector.get('segments', [selector])
                pieces, previous = [], -1
                for span in spans:
                    a, b = span['start_character_inclusive'], span['end_character_exclusive']
                    if not 0 <= a < b <= len(page) or a < previous:
                        raise ValueError('invalid character selector')
                    pieces.append(page[a:b].strip())
                    previous = b
                paragraph = ' '.join(pieces)
                if digest(paragraph) != row['normalized_paragraph_sha256']:
                    raise ValueError('paragraph hash mismatch')
                if len(TOKEN.findall(paragraph)) != row['word_count']:
                    raise ValueError('token mismatch')
                if not paragraph.startswith(row['opening_locator']):
                    raise ValueError('opening locator mismatch')
                return dict(kind='paragraph', tokens=row['word_count'],
                            checks=['PDF hash', 'normalized page hash', 'character spans', 'paragraph hash', 'tokens', 'opening locator'],
                            sentence_count='manual; not recomputed', visual_boundaries='manual; not reverified')
            check(f'{name}:{row["paper_id"]}:{i}', verify_paragraph)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf_dir', type=Path)
    parser.add_argument('--measurements', type=Path, default=ROOT / 'research/measurements')
    parser.add_argument('--json', action='store_true', help='emit metadata-only JSON to stdout')
    args = parser.parse_args()
    try:
        results = replay(args.pdf_dir, args.measurements)
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps(dict(status='error', reason=type(exc).__name__)))
        return 2
    failed = sum(r['status'] != 'pass' for r in results)
    if args.json:
        print(json.dumps(dict(passed=len(results)-failed, failed=failed, results=results), indent=2))
    else:
        for row in results:
            print(f'{row["status"].upper()}: {row["record"]}')
        print(f'{len(results)-failed} passed; {failed} failed. Sentence counts and visual boundaries remain manual evidence.')
    return int(bool(failed))


if __name__ == '__main__':
    raise SystemExit(main())
