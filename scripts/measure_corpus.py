#!/usr/bin/env python3
"""Reproduce explicitly bounded PDF token counts. Requires Poppler pdftotext.
Full text is read locally and never emitted into committed results.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata

TOKEN = re.compile(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*")


def count(text):
    # Numerals in citations are removed; numerals in prose/tables remain.
    text = re.sub(r"\[[\d\s,–—-]+\]", "", text)
    return len(TOKEN.findall(text))


def between(text, start, end):
    assert text.count(start) == 1, (start, text.count(start))
    assert text.count(end) == 1, (end, text.count(end))
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[a:b]


def clean(text, paper):
    text = unicodedata.normalize('NFKC', text).replace('\f', '\n')
    if paper == 'P03-trust-think':
        text = re.sub(r"Authors’ addresses:.*?Publication date: April 2021\.", '', text, flags=re.S)
        text = re.sub(r'^Proc\. ACM Hum\.-Comput\. Interact\..*$', '', text, flags=re.M)
        text = re.sub(r'^(?:188(?::\d+)?|To Trust or to Think|Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z\. Gajos)\s*$', '', text, flags=re.M)
    else:
        text = re.sub(r'Permission to make digital.*?http://dx\.doi\.org/10\.1145/3313831\.3376301', '', text, flags=re.S)
        text = re.sub(r'^(?:CHI 2020 Paper|CHI 2020, April 25–30, 2020, Honolulu, HI, USA|Paper 174|Page \d+)\s*$', '', text, flags=re.M)
    # Join line-end hyphenation. Ambiguous compound hyphens are a known limitation.
    text = re.sub(r'(?<=\w)-\n(?=\w)', '', text)
    return text


SPECS = {
    'P03-trust-think': {
        'abstract': ('People supported by AI-powered', 'CCS Concepts:'),
        'body': ('From loan approval', 'ACKNOWLEDGMENTS'),
        'sections': [('Introduction', 'From loan approval', 'RELATED WORK'),
                     ('Related work', 'RELATED WORK', 'EXPERIMENT'),
                     ('Experiment', 'EXPERIMENT', 'RESULTS'),
                     ('Results', 'RESULTS', 'ETHICAL CONSIDERATIONS: INDIVIDUAL DIFFERENCES IN COGNITIVE'),
                     ('Individual-differences analysis', 'ETHICAL CONSIDERATIONS: INDIVIDUAL DIFFERENCES IN COGNITIVE', 'DISCUSSION'),
                     ('Discussion', 'DISCUSSION', 'CONCLUSION'),
                     ('Conclusion', 'CONCLUSION', 'ACKNOWLEDGMENTS')],
        'paragraphs': [('Explainable AI (XAI),', 'We posit that'),
                       ('We posit that', 'In the context of explainable AI,'),
                       ('In the context of explainable AI,', 'We argue that to reduce'),
                       ('We argue that to reduce', 'A number of approaches'),
                       ('A number of approaches', 'We conducted an experiment with 199')],
        'paragraph_selection': 'Five consecutive complete introduction paragraphs on PDF p.2 (paragraphs 2–6); visual boundary check. Cross-page paragraphs excluded from this subset.',
    },
    'P07-reexamining': {
        'abstract': ('Artificial Intelligence (AI) plays', 'Author Keywords'),
        'body': ('Advances in Artificial Intelligence', 'The contents of this paper'),
        'sections': [('Introduction', 'Advances in Artificial Intelligence', 'RELATED WORK'),
                     ('Related work', 'RELATED WORK', 'THREE QUESTIONS FOR PROVOCATION'),
                     ('Remaining argument including conclusion', 'THREE QUESTIONS FOR PROVOCATION', 'The contents of this paper')],
        'paragraphs': [('Advances in Artificial Intelligence', 'The growing interest'),
                       ('The growing interest', 'Existing research frequently'),
                       ('Existing research frequently', 'The goal of this paper')],
        'paragraph_selection': 'First three consecutive prose paragraphs of Introduction, PDF p.1; visual boundary and column-order check.',
    },
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf_dir', type=Path)
    parser.add_argument('--out', type=Path, default=Path('research/measurements/counts.json'))
    args = parser.parse_args()
    manifest = {x['id']: x for x in json.loads(Path('research/corpus.json').read_text())}
    rows = []
    for key, spec in SPECS.items():
        path = args.pdf_dir / (key + '.pdf')
        checksum = hashlib.sha256(path.read_bytes()).hexdigest()
        if checksum != manifest[key]['sha256']:
            raise ValueError(f'{key}: PDF version differs from reviewed checksum')
        raw = subprocess.check_output(['pdftotext', str(path), '-'], text=True)
        text = clean(raw, key)
        total = count(between(text, *spec['body']))
        sections = [{'section': name, 'tokens': count(between(text, a, b))}
                    for name, a, b in spec['sections']]
        assert sum(s['tokens'] for s in sections) == total
        for section in sections:
            section['percent_of_extracted_body'] = round(100 * section['tokens']/total, 2)
        paras = [count(between(text, a, b)) for a, b in spec['paragraphs']]
        rows.append(dict(id=key, sha256=checksum, abstract_tokens=count(between(text, *spec['abstract'])), extracted_body_tokens=total,
                         sections=sections, paragraph_tokens=paras,
                         paragraph_selection=spec['paragraph_selection']))
    result = dict(status='descriptive extraction estimates, not prose-only or ACM counts',
                  tokenizer=TOKEN.pattern, extraction='pdftotext default; Unicode NFKC; specified header/frontmatter removal; numeric citations removed; line-end hyphens joined',
                  includes='body headings, figure/table captions, extractable figure/table labels and numerals, quoted material',
                  excludes='title/authors, abstract, rights notice, running headers/footers, acknowledgments, references and appendices',
                  limitations='Figure/table text is not separately counted; column flow and broken glyphs can alter counts. P07 p2 figure caption falls within extracted Introduction. Do not compare to prose-only word budgets or infer population norms.',
                  papers=rows)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(rows, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
