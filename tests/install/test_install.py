import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts/install_skill.py'
spec = importlib.util.spec_from_file_location('install_skill', SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()

    def test_default_dry_run_creates_nothing(self):
        proc = subprocess.run([sys.executable, str(SCRIPT), '--host', 'codex',
                               '--scope', 'project', '--project-root', str(self.root)],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertIn('would-install', proc.stdout)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_all_hosts_project_and_global_self_contained_idempotent(self):
        expected = installer.snapshot(installer.SOURCE)
        for host in installer.HOSTS:
            for scope in ('project', 'global'):
                with self.subTest(host=host, scope=scope):
                    base = self.root / (host + '-' + scope)
                    base.mkdir()
                    result = installer.install(host, scope, base, True)
                    dest = Path(result['destination'])
                    self.assertEqual(installer.snapshot(dest), expected)
                    self.assertGreater(installer.check_bundle(installer.snapshot(dest)), 0)
                    before = {p: p.stat().st_mtime_ns for p in dest.rglob('*')}
                    self.assertEqual(installer.install(host, scope, base, True)['status'], 'identical')
                    self.assertEqual(before, {p: p.stat().st_mtime_ns for p in dest.rglob('*')})

    def test_different_and_extra_files_preserved(self):
        dest = Path(installer.install('codex', 'project', self.root, True)['destination'])
        (dest / 'user-note.txt').write_text('preserve')
        before = installer.snapshot(dest)
        for apply in (False, True):
            with self.assertRaisesRegex(ValueError, 'no overwrite'):
                installer.install('codex', 'project', self.root, apply)
        self.assertEqual(before, installer.snapshot(dest))

    def test_file_conflict(self):
        (self.root / '.agents').write_text('user settings')
        with self.assertRaises(ValueError):
            installer.install('codex', 'project', self.root, True)
        self.assertEqual((self.root / '.agents').read_text(), 'user settings')

    def test_symlink_ancestor_and_broken_destination(self):
        outside = self.root / 'outside'
        outside.mkdir()
        link = self.root / '.agents'
        link.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            installer.install('codex', 'project', self.root, True)
        link.unlink()
        (self.root / '.agents/skills').mkdir(parents=True)
        (self.root / '.agents/skills' / installer.NAME).symlink_to(self.root / 'missing')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            installer.install('codex', 'project', self.root, True)
        self.assertEqual(list(outside.iterdir()), [])

    def test_source_symlink_rejected(self):
        source = self.root / 'source'
        source.mkdir()
        (source / 'SKILL.md').symlink_to(installer.SOURCE / 'SKILL.md')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            installer.install('codex', 'project', self.root, True, source)

    def test_outside_or_missing_link_rejected(self):
        files = installer.snapshot(installer.SOURCE)
        for link in ('../../outside.md', 'missing.md'):
            with self.subTest(link=link):
                changed = dict(files)
                body, mode = changed['SKILL.md']
                changed['SKILL.md'] = (body + f'\n[bad]({link})\n'.encode(), mode)
                with self.assertRaisesRegex(ValueError, 'Non-self-contained'):
                    installer.check_bundle(changed)

    def test_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError, 'overlap'):
            installer.install('codex', 'project', self.root, True, self.root)

    def test_missing_project_argument(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--host', 'codex',
                                 '--scope', 'project', '--apply'], capture_output=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
