#!/usr/bin/env python3
"""Read-only lexical audit of literal multi-file LaTeX projects (not a TeX engine)."""
import argparse
import json
from pathlib import Path
import re
import sys

COMMAND = re.compile(r'\\([A-Za-z]+)\*?')
VERBATIM = re.compile(r'\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|comment)\}')
DYNAMIC = re.compile(r'[\\#$~{}]')


def masked(text, comments=True):
    """Mask comments and common literal environments, preserving source offsets."""
    chars = list(text)
    i = 0
    def erase(a, b):
        for k in range(a, b):
            if chars[k] != '\n':
                chars[k] = ' '
    while i < len(text):
        if comments and text[i] == '%' and (len(text[:i]) - len(text[:i].rstrip('\\'))) % 2 == 0:
            end = text.find('\n', i)
            end = len(text) if end < 0 else end
            erase(i, end); i = end
            continue
        env = VERBATIM.match(text, i)
        if env:
            endmark = '\\end{' + env.group(1) + '}'
            end = text.find(endmark, env.end())
            end = len(text) if end < 0 else end + len(endmark)
            erase(i, end); i = end
            continue
        verb = re.match(r'\\verb\*?(?![A-Za-z])', text[i:])
        if verb:
            delimiter = i + verb.end()
            if delimiter < len(text) and not text[delimiter].isspace():
                end = text.find(text[delimiter], delimiter + 1)
                if end >= 0:
                    erase(i, end + 1); i = end + 1
                    continue
        # Skip escaped control symbols, notably \\% and \\\\.
        if text[i] == '\\' and i + 1 < len(text) and not text[i + 1].isalpha():
            i += 2
        else:
            i += 1
    return ''.join(chars)


def group(text, position, opener='{', closer='}'):
    while position < len(text) and text[position].isspace():
        position += 1
    if position >= len(text) or text[position] != opener:
        return None, position
    start = position + 1
    depth = 1
    position += 1
    while position < len(text):
        c = text[position]
        if c == '\\':
            position += 2; continue
        if c == opener:
            depth += 1
        elif c == closer:
            depth -= 1
            if depth == 0:
                return text[start:position], position + 1
        position += 1
    return None, position


def commands(text):
    for match in COMMAND.finditer(text):
        # A command after an escaped backslash is not an invocation.
        n = len(text[:match.start()]) - len(text[:match.start()].rstrip('\\'))
        if n % 2:
            continue
        pos = match.end()
        for _ in range(2):
            value, end = group(text, pos, '[', ']')
            if value is None:
                break
            pos = end
        value, end = group(text, pos)
        yield match.group(1), value, match.start(), end


def bib_keys(text):
    """Scan whole BibTeX entries so @comment bodies cannot invent entries."""
    clean = masked(text)
    cursor = 0
    while True:
        match = re.search(r'@([A-Za-z]+)\s*([{(])', clean[cursor:])
        if not match:
            return
        start = cursor + match.start()
        opening = cursor + match.end() - 1
        op = clean[opening]
        body, end = group(clean, opening, op, '}' if op == '{' else ')')
        if body is None:
            return
        cursor = end
        if match.group(1).lower() in {'comment', 'preamble', 'string'}:
            continue
        key = body.split(',', 1)[0].strip()
        if key:
            yield key, start


def audit(root, project_dir=None):
    root = Path(root).resolve()
    project = Path(project_dir).resolve() if project_dir else root.parent
    issues, files, bibliographies = [], [], []
    labels, references, citations, entries = {}, [], [], {}
    seen, active, bib_seen = set(), [], set()
    uncertain = {'bibliography': False, 'references': False, 'execution': False}

    def issue(level, code, path, text, offset, message):
        try:
            name = str(path.relative_to(project))
        except ValueError:
            name = str(path)
        issues.append(dict(severity=level, code=code, file=name,
                           line=text.count('\n', 0, offset) + 1, message=message))

    def literal(value, path, text, offset, kind):
        if value is None or not value.strip() or DYNAMIC.search(value):
            issue('warning', 'unsupported_dynamic_' + kind, path, text, offset,
                  'Cannot statically interpret this ' + kind + ' argument.')
            if kind in uncertain:
                uncertain[kind] = True
            if kind == 'include':
                uncertain['execution'] = True
            return False
        return True

    def locate(value, suffix, path, text, offset):
        candidate = Path(value.strip())
        if not candidate.suffix:
            candidate = candidate.with_suffix(suffix)
        # TeX resolves relative paths from the compile working directory.
        resolved = (project / candidate).resolve()
        if not resolved.is_relative_to(project):
            issue('warning', 'outside_project', path, text, offset,
                  'Skipped path outside project: ' + value)
            uncertain['execution'] = True
            return None
        return resolved

    def read(path, kind, source=None, text='', offset=0):
        if not path.is_file():
            issue('error', 'missing_' + kind, source or path, text, offset,
                  'Missing file: ' + str(path))
            return None
        try:
            return path.read_text(encoding='utf-8-sig')
        except (OSError, UnicodeError) as exc:
            issue('warning', 'unreadable_' + kind, path, '', 0, str(exc))
            uncertain['execution'] = True
            return None

    def visit(path, source=None, source_text='', source_offset=0):
        if path in active:
            issue('error', 'cyclic_include', source or path, source_text, source_offset,
                  'Literal include cycle: ' + ' -> '.join(p.name for p in active + [path]))
            return
        if path in seen:
            issue('warning', 'repeated_include', source or path, source_text, source_offset,
                  'File already inspected; repeated expansion is not modeled.')
            return
        raw = read(path, 'tex', source, source_text, source_offset)
        if raw is None:
            return
        seen.add(path); active.append(path); files.append(str(path.relative_to(project)))
        clean = masked(raw)
        document_end = re.search(r'\\end\s*\{document\}', clean)
        if document_end:
            clean = clean[:document_end.end()]
        # TODOs in ordinary comments are useful authoring reminders; exclude literal environments.
        for match in re.finditer(r'\b(?:TODO|FIXME|TBD|XXX)\b', masked(raw, comments=False)):
            issue('warning', 'todo', path, raw, match.start(), 'Authoring marker: ' + match.group())
        for name, value, offset, _ in commands(clean):
            if name in {'newcommand', 'renewcommand', 'def', 'gdef', 'edef', 'newenvironment', 'includeonly', 'IfFileExists', 'import', 'subimport', 'inputfrom', 'subinputfrom', 'if', 'ifdefined', 'iffalse', 'iftrue'} or name.startswith('if'):
                uncertain['execution'] = True
                issue('warning', 'unsupported_execution', path, raw, offset,
                      'Macro definitions, conditionals, or import-package paths are not expanded; lexical findings need review.')
            if name == 'externaldocument':
                uncertain['references'] = True
                issue('warning', 'external_references', path, raw, offset, 'External labels are not loaded.')
            if name in {'input', 'include', 'subfile'}:
                if literal(value, path, raw, offset, 'include'):
                    child = locate(value, '.tex', path, raw, offset)
                    if child:
                        visit(child, path, raw, offset)
            elif name in {'bibliography', 'addbibresource'}:
                if literal(value, path, raw, offset, 'bibliography'):
                    for item in value.split(','):
                        bib = locate(item, '.bib', path, raw, offset)
                        if bib is None:
                            uncertain['bibliography'] = True
                        elif bib not in bib_seen:
                            bib_seen.add(bib)
                            content = read(bib, 'bibliography', path, raw, offset)
                            if content is None:
                                uncertain['bibliography'] = True
                                continue
                            bibliographies.append(str(bib.relative_to(project)))
                            for key, position in bib_keys(content):
                                if key in entries:
                                    issue('error', 'duplicate_bib_key', bib, content, position, 'Duplicate bibliography key: ' + key)
                                entries[key] = str(bib)
            elif name == 'bibitem' and literal(value, path, raw, offset, 'citation'):
                if value in entries:
                    issue('error', 'duplicate_bib_key', path, raw, offset, 'Duplicate bibliography key: ' + value)
                entries[value] = str(path)
            elif name == 'label' and literal(value, path, raw, offset, 'references'):
                if value in labels:
                    issue('error', 'duplicate_label', path, raw, offset, 'Duplicate label: ' + value)
                labels[value] = str(path)
            elif name in {'ref', 'pageref', 'eqref', 'autoref', 'cref', 'Cref', 'vref', 'nameref'}:
                if literal(value, path, raw, offset, 'references'):
                    references.extend((key.strip(), path, raw, offset) for key in value.split(','))
            elif name in {'cite', 'citep', 'citet', 'citealt', 'citealp', 'citeauthor', 'citeyear', 'citeyearpar', 'autocite', 'parencite', 'textcite', 'nocite', 'Cite', 'Citep', 'Citet'}:
                if literal(value, path, raw, offset, 'citation'):
                    citations.extend((key.strip(), path, raw, offset) for key in value.split(',') if key.strip() != '*')
            elif name in {'todo', 'missingfigure'}:
                issue('warning', 'todo_command', path, raw, offset, 'Unresolved authoring command: \\' + name)
        active.pop()

    if not root.is_relative_to(project):
        issue('error', 'root_outside_project', root, '', 0, 'Root must be within the project directory.')
    else:
        visit(root)
    for key, path, raw, offset in references:
        if key not in labels:
            level = 'warning' if uncertain['references'] or uncertain['execution'] else 'error'
            issue(level, 'unresolved_reference', path, raw, offset, 'No literal label found: ' + key)
    for key, path, raw, offset in citations:
        if key not in entries:
            level = 'warning' if uncertain['bibliography'] or uncertain['execution'] else 'error'
            issue(level, 'unresolved_citation', path, raw, offset, 'No bibliography entry found: ' + key)
    # Definitions/conditionals can contain dormant commands; do not assert execution errors.
    if uncertain['execution']:
        for item in issues:
            if item['code'] in {'missing_tex', 'missing_bibliography', 'cyclic_include', 'duplicate_label', 'duplicate_bib_key'}:
                item['severity'] = 'warning'
    return dict(root=str(root), project_dir=str(project), files=files, bibliographies=bibliographies,
                scope='Conservative lexical audit, not TeX correctness or compilation validation. No macro expansion, package loading, custom command interpretation, or build execution.',
                issues=issues, errors=sum(i['severity'] == 'error' for i in issues),
                warnings=sum(i['severity'] == 'warning' for i in issues))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', help='Explicit root .tex file')
    parser.add_argument('--project-dir', help='Compile working directory; defaults to root parent')
    parser.add_argument('--json', action='store_true', help='Print JSON instead of concise text')
    args = parser.parse_args()
    result = audit(args.root, args.project_dir)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Lexical audit: {len(result['files'])} TeX files; {result['errors']} errors, {result['warnings']} warnings")
        for item in result['issues']:
            print(f"{item['severity'].upper()} {item['file']}:{item['line']} [{item['code']}] {item['message']}")
        print(result['scope'])
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
