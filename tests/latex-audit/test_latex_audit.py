"""Isolated lexical fixtures; no user manuscript changes or network access."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parents[1] / 'skills/hci-academic-writing/scripts/latex_audit.py'
spec = importlib.util.spec_from_file_location('latex_audit', SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class AuditTests(unittest.TestCase):
    def temporary(self, content, files=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        (root / 'main.tex').write_text(content)
        for name, value in (files or {}).items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(value)
        return mod.audit(root / 'main.tex')

    def test_valid_acm_and_no_mutation(self):
        fixture = HERE / 'fixtures/valid'
        before = {str(p): p.read_bytes() for p in fixture.rglob('*') if p.is_file()}
        result = mod.audit(fixture / 'main.tex')
        self.assertEqual(result['errors'], 0)
        self.assertEqual(len(result['files']), 3)
        self.assertEqual([i['code'] for i in result['issues']], ['todo'])
        self.assertEqual(before, {str(p): p.read_bytes() for p in fixture.rglob('*') if p.is_file()})

    def test_broken_static_errors(self):
        result = mod.audit(HERE / 'fixtures/broken/main.tex')
        self.assertEqual({i['code'] for i in result['issues']}, {
            'duplicate_label', 'missing_tex', 'cyclic_include', 'duplicate_bib_key',
            'unresolved_citation', 'unresolved_reference'})
        self.assertEqual(result['errors'], 6)

    def test_literal_content_and_comments_are_ignored(self):
        result = self.temporary(r'''% \ref{bad}
\begin{minted}{tex}
\cite{bad}\input{bad} TODO
\end{minted}
\verb|\label{x}| \verb*+\cite{bad}+
\label{good}\ref{good} \\ref{not-a-command}
''')
        self.assertEqual(result['issues'], [])

    def test_bib_comments_and_optional_citations(self):
        result = self.temporary(r'\addbibresource[location=local]{r.bib}\parencite[see][p. 2]{a,b}\nocite{*}',
          {'r.bib': '% @article{fake,}\n@comment{ @book{nested,} }\n@string{x="foo"}\n@book{a,title={nested {braces}}}\n@article(b,title={Parentheses})'})
        self.assertEqual(result['issues'], [])
        keys = list(mod.bib_keys('@comment{@book{fake,}}\n@book{real,title={x}}'))
        self.assertEqual([x[0] for x in keys], ['real'])

    def test_dynamic_paths_and_conditional_code_warn(self):
        result = self.temporary(r'\input{\chapterfile}\ifdefined\draft\input{draft}\fi\ref{generated}')
        self.assertEqual(result['errors'], 0)
        self.assertIn('unsupported_dynamic_include', [x['code'] for x in result['issues']])
        self.assertTrue(all(x['severity'] == 'warning' for x in result['issues']))

    def test_paths_resolve_from_project_and_do_not_escape(self):
        result = self.temporary(r'\input{sections/a}', {'sections/a.tex': r'\input{sections/b}', 'sections/b.tex': r'\label{x}\ref{x}'})
        self.assertEqual(result['errors'], 0)
        self.assertEqual(len(result['files']), 3)
        escaped = self.temporary(r'\input{../outside}\ref{unknown}')
        self.assertEqual(escaped['errors'], 0)
        self.assertIn('outside_project', [x['code'] for x in escaped['issues']])

    def test_bibitem_and_external_labels(self):
        result = self.temporary(r'\bibitem[Author]{a}\cite{a}\externaldocument{elsewhere}\ref{external}')
        self.assertEqual(result['errors'], 0)
        self.assertIn('unresolved_reference', [x['code'] for x in result['issues']])

    def test_after_document_end_and_import_uncertainty(self):
        result = self.temporary(r'\label{a}\ref{a}\end{document}\input{draft}\cite{bad}')
        self.assertEqual(result['issues'], [])
        result = self.temporary(r'\import{sections/}{chapter.tex}\ref{imported}')
        self.assertEqual(result['errors'], 0)
        self.assertIn('unsupported_execution', [x['code'] for x in result['issues']])

    def test_missing_root_and_cli_exit_status(self):
        with tempfile.TemporaryDirectory() as directory:
            result = mod.audit(Path(directory) / 'missing.tex')
            self.assertEqual(result['errors'], 1)
        for name, code in [('valid', 0), ('broken', 1)]:
            run = subprocess.run([sys.executable, str(SCRIPT), str(HERE / 'fixtures' / name / 'main.tex'), '--json'], capture_output=True, text=True)
            self.assertEqual(run.returncode, code)
            self.assertIn('scope', json.loads(run.stdout))


if __name__ == '__main__':
    unittest.main()
