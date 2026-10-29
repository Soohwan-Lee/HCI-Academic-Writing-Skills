#!/usr/bin/env python3
"""Copy this repository's self-contained skill. Dry run unless --apply is given."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import stat
from urllib.parse import unquote, urlsplit

NAME = 'hci-academic-writing'
SOURCE = Path(__file__).resolve().parents[1] / 'skills' / NAME
HOSTS = {
    'codex': ('.agents/skills', '.agents/skills'),
    'claude-code': ('.claude/skills', '.claude/skills'),
    'antigravity-app': ('.agents/skills', '.gemini/config/skills'),
    'antigravity-cli': ('.agents/skills', '.gemini/antigravity-cli/skills'),
    'antigravity-ide': ('.agents/skills', '.gemini/config/skills'),
}


def check_path(path):
    """Reject symlinks, including broken ones, and non-directory ancestors."""
    for part in reversed((path, *path.parents)):
        if part.is_symlink():
            raise ValueError(f'Symlink path refused: {part}')
        if part != path and part.exists() and not part.is_dir():
            raise ValueError(f'Ancestor is not a directory: {part}')


def snapshot(root):
    check_path(root)
    if not root.is_dir():
        raise ValueError(f'Not a directory: {root}')
    files = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlink entry refused: {path}')
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError(f'Special file refused: {path}')
        files[path.relative_to(root).as_posix()] = (path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
    return files


def check_bundle(files):
    """Validate this bundle's simple frontmatter and inline Markdown file links.

    This deliberately isn't a general Markdown/YAML parser. The repository uses
    simple name/description fields and inline links; URLs and local anchors skip.
    """
    skill = files.get('SKILL.md', (b'', 0))[0].decode('utf-8')
    if not skill.startswith('---\n') or '\n---\n' not in skill[4:]:
        raise ValueError('Missing SKILL.md frontmatter')
    front = skill.split('\n---\n', 1)[0]
    if not re.search(r'^name:\s*' + re.escape(NAME) + r'\s*$', front, re.M):
        raise ValueError('Unexpected skill name')
    if not re.search(r'^description:\s*\S.+$', front, re.M):
        raise ValueError('Missing skill description')
    links = 0
    for name, (content, _) in files.items():
        if not name.endswith('.md'):
            continue
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', content.decode('utf-8')):
            target = target.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            # Normalize lexically without consulting anything outside the bundle.
            path = Path(os.path.normpath(str(Path(name).parent / unquote(parsed.path))))
            if path.is_absolute() or '..' in path.parts or path.as_posix() not in files:
                raise ValueError(f'Non-self-contained link in {name}: {target}')
            links += 1
    return links


def install(host, scope, base, apply=False, source=SOURCE):
    base = Path(os.path.abspath(Path(base).expanduser()))
    check_path(base)
    if not base.is_dir():
        raise ValueError('Explicit project/home root must be an existing directory')
    destination = base / HOSTS[host][scope == 'global'] / NAME
    check_path(destination)
    source = Path(os.path.abspath(source))
    if destination == source or source in destination.parents or destination in source.parents:
        raise ValueError('Source and destination overlap')
    files = snapshot(source)
    links = check_bundle(files)
    report = dict(host=host, scope=scope, source=str(source), destination=str(destination),
                  files=len(files), relative_links_checked=links, applied=False)
    if destination.exists():
        existing = snapshot(destination)
        if existing != files:
            raise ValueError(f'Existing destination differs; no overwrite: {destination}')
        return dict(report, status='identical')
    if not apply:
        return dict(report, status='would-install')
    destination.parent.mkdir(parents=True, exist_ok=True)
    check_path(destination)
    destination.mkdir()  # Exclusive: never merge with a concurrently created tree.
    try:
        for name, (data, mode) in files.items():
            path = destination / name
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('xb') as handle:
                handle.write(data)
            path.chmod(mode)
        if snapshot(destination) != files:
            raise ValueError('Copy verification failed')
    except BaseException:
        # This process created the destination exclusively; preserve all siblings.
        shutil.rmtree(destination)
        raise
    return dict(report, status='installed', applied=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', required=True, choices=HOSTS)
    parser.add_argument('--scope', required=True, choices=['project', 'global'])
    parser.add_argument('--project-root', type=Path, help='existing target project; required for project scope')
    parser.add_argument('--home-root', type=Path, help='global home root (default: current user home); useful for isolated tests')
    parser.add_argument('--apply', action='store_true', help='perform the displayed installation; otherwise dry run')
    args = parser.parse_args()
    if args.scope == 'project' and (args.project_root is None or args.home_root is not None):
        parser.error('project scope requires --project-root and disallows --home-root')
    if args.scope == 'global' and args.project_root is not None:
        parser.error('global scope disallows --project-root')
    base = args.project_root if args.scope == 'project' else (args.home_root or Path.home())
    try:
        print(json.dumps(install(args.host, args.scope, base, args.apply), indent=2))
    except (OSError, ValueError, UnicodeError) as exc:
        print(json.dumps(dict(status='error', message=str(exc))))
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
