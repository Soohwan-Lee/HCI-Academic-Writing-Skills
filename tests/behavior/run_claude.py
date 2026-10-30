#!/usr/bin/env python3
"""Opt-in live subscription test. Outputs stay under ignored .local/behavior.
Requires --run; never falls back to API billing. No global configuration edits.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
COMMON = '''Use the installed hci-academic-writing skill explicitly; locate and read its SKILL.md and relevant local references. Do not treat this prompt as the skill contents. Work only in this isolated project. The root is chi26.tex, not main.tex. Use only Read/Edit/Glob/Grep. Do not use network, shell, builds, or other tools. Change only the requested paragraph in the specified file; preserve its section, label, comment, all other files, and every unrelated macro. This is an actual edit task, not a request for advice. End with a short change report.'''
CASES = {
 'existing-citations': ('sections/rw.tex', '''Revise the existing related-work paragraph for better sentence-to-sentence flow. Preserve the author-owned claims, their citation keys and attachments, and the scoped research gap. Source full texts are intentionally unavailable; do not add verification TODOs merely for unchanged cited claims. Do not strengthen claims or invent new evidence.'''),
 'compress-results': ('sections/results.tex', '''Compress the existing results paragraph to at most 90 prose words. Preserve the sample, both condition score means, the nonsignificant result and exact p value, both median times, both effort ratings and scale, and the absence of an established score benefit. Values are supplied synthetic test data. Do not invent effects, significance, explanation, or findings.'''),
}


def clean_env():
    return {k: v for k, v in os.environ.items()
            if not k.startswith(('ANTHROPIC_', 'CLAUDE_CODE_USE_'))
            and k not in ('CLAUDE_CODE_OAUTH_TOKEN', 'CLAUDECODE')}


def tree(path):
    return {str(p.relative_to(path)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in path.rglob('*') if p.is_file() and '.git' not in p.parts}


def run(base):
    env = clean_env()
    summary = []
    for case, (target, instruction) in CASES.items():
        project = base / case
        shutil.copytree(ROOT / 'tests/behavior/fixture', project)
        subprocess.run(['git', 'init', '-q', str(project)], check=True)
        subprocess.run([sys.executable, str(ROOT / 'scripts/install_skill.py'), '--host',
                        'claude-code', '--scope', 'project', '--project-root', str(project),
                        '--apply'], check=True, capture_output=True)
        # Fresh authentication check immediately before each model request.
        status = subprocess.run(['claude', 'auth', 'status'], env=env, cwd=project,
                                capture_output=True, text=True, check=True)
        auth = json.loads(status.stdout)
        if auth.get('authMethod') != 'claude.ai' or not auth.get('subscriptionType'):
            raise RuntimeError('Subscription authentication unavailable; no API fallback')
        before = tree(project)
        original = (project / target).read_text()
        command = ['claude', '-p', '--output-format', 'stream-json', '--verbose',
                   '--restricted', '--permission-mode', 'acceptEdits', '--permission-prompts', 'none',
                   '--tools', 'Read,Edit,Glob,Grep', '--strict-mcp-config',
                   '--mcp-config', '{"mcpServers":{}}', '--setting-sources', '',
                   '--no-session-persistence', COMMON + '\nTarget: ' + target + '\n' + instruction]
        with (base / (case + '.stream.jsonl')).open('w') as out, (base / (case + '.stderr.txt')).open('w') as err:
            proc = subprocess.run(command, cwd=project, env=env, stdout=out, stderr=err, timeout=240)
        after = tree(project)
        changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
        events = []
        for line in (base / (case + '.stream.jsonl')).read_text().splitlines():
            try: events.append(json.loads(line))
            except ValueError: pass
        models, reads, catalog = set(), [], []
        for event in events:
            if event.get('model'): models.add(event['model'])
            if event.get('type') == 'system' and event.get('subtype') == 'init':
                catalog = event.get('skills', [])
            message = event.get('message', {})
            if message.get('model'): models.add(message['model'])
            for part in message.get('content', []) if isinstance(message, dict) else []:
                if isinstance(part, dict) and part.get('type') == 'tool_use' and part.get('name') == 'Read':
                    reads.append(part.get('input', {}).get('file_path', ''))
        edited = (project / target).read_text()
        (base / (case + '.before.tex')).write_text(original)
        (base / (case + '.after.tex')).write_text(edited)
        row = dict(case=case, returncode=proc.returncode, authMethod=auth['authMethod'],
                   subscriptionType=auth['subscriptionType'], models=sorted(models), changed=changed,
                   skill_catalog_observed='hci-academic-writing' in catalog,
                   skill_read_observed=any('.claude/skills/hci-academic-writing/SKILL.md' in p for p in reads),
                   citations_preserved=re.findall(r'\\cite\{[^}]+\}', original)==re.findall(r'\\cite\{[^}]+\}', edited),
                   numeric_tokens_preserved=re.findall(r'\d+(?:\.\d+)?', original)==re.findall(r'\d+(?:\.\d+)?', edited),
                   no_added_todo=edited.count('TODO') <= original.count('TODO'))
        row['scope_preserved'] = changed == [target]
        row['structural_lines_preserved'] = [x for x in original.splitlines() if x.startswith(('\\section', '%'))] == [x for x in edited.splitlines() if x.startswith(('\\section', '%'))]
        prose = '\n'.join(x for x in edited.splitlines() if not x.startswith(('\\section', '%')))
        row['prose_tokens'] = len(re.findall(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*", prose))
        row['length_pass'] = case != 'compress-results' or row['prose_tokens'] <= 90
        row['mechanical_pass'] = proc.returncode == 0 and all(row[k] for k in ('scope_preserved', 'structural_lines_preserved', 'citations_preserved', 'numeric_tokens_preserved', 'no_added_todo', 'length_pass', 'skill_read_observed'))
        summary.append(row)
        (base / 'summary.json').write_text(json.dumps(summary, indent=2))
        print(json.dumps(row), flush=True)
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true', help='make two real subscription model requests')
    args = parser.parse_args()
    if not args.run:
        parser.error('Live requests require explicit --run')
    base = ROOT / '.local/behavior' / time.strftime('%Y%m%d-%H%M%S')
    base.mkdir(parents=True)
    results = run(base)
    raise SystemExit(0 if all(r['mechanical_pass'] for r in results) else 1)
