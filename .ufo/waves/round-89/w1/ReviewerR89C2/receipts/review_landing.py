#!/usr/bin/env python3
"""Inspect a landed record without modifying its lane; args are explicit observed paths."""
import ast
import copy
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

REPO = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin')
SCRATCH = Path('/fast/scratch/hyaku/revenger-r89/ReviewerR89C2')
OUT = SCRATCH / 'receipts'
ENV = {**os.environ, 'TMPDIR': str(SCRATCH), 'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
F4 = REPO / 'reports/round-81/f_probe4.py'
ORACLE = REPO / 'corpus/fixtures/apk-r65/oracle_check.py'
TRUTH = REPO / 'corpus/fixtures/apk-r65/truth.json'
record_path = Path(sys.argv[1]).resolve()
assert record_path.is_relative_to(REPO / 'corpus/live/runs/round-89')
OUT.mkdir(parents=True, exist_ok=True)


def command(name, args):
    args = [str(a) for a in args]
    p = subprocess.run(args, env=ENV, cwd=SCRATCH, capture_output=True, timeout=90, check=False)
    text = ('$ env TMPDIR=' + str(SCRATCH) + ' PYTHONUTF8=1 ' + shlex.join(args) + '\n'
            + p.stdout.decode('utf-8', 'replace')
            + ('STDERR:\n' + p.stderr.decode('utf-8', 'replace') if p.stderr else '')
            + f'EXIT={p.returncode}\n')
    (OUT / (name + '.log')).write_text(text)
    return {'name': name, 'exit': p.returncode, 'stdout': p.stdout.decode('utf-8', 'replace')}


def sha(data):
    return hashlib.sha256(data).hexdigest()


record_bytes = record_path.read_bytes()
record = json.loads(record_bytes)
(OUT / 'producer-record-reviewed.json').write_bytes(record_bytes)
current_root = REPO / 'corpus/live/runs'
base_root = SCRATCH / 'base/corpus/live/runs'
old_files = {str(p.relative_to(base_root)): sha(p.read_bytes()) for p in base_root.rglob('*') if p.is_file()}
new_files = {str(p.relative_to(current_root)): sha(p.read_bytes()) for p in current_root.rglob('*') if p.is_file()}
added = sorted(new_files.keys() - old_files.keys())
removed = sorted(old_files.keys() - new_files.keys())
modified = sorted(p for p in old_files.keys() & new_files.keys() if old_files[p] != new_files[p])
families = next(ast.literal_eval(n.value) for n in ast.walk(ast.parse(F4.read_text()))
                if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'families' for t in n.targets))
added_details = []
for p in added:
    data = (current_root / p).read_bytes()
    detail = {'path': str(current_root / p), 'sha256': sha(data), 'counted_record': False}
    if p.endswith('.json'):
        try:
            value = json.loads(data)
        except (ValueError, UnicodeError):
            value = None
        if isinstance(value, dict) and value.get('evidence_id') and value.get('normalized_result') is not None:
            operation = value.get('operation', 'unknown')
            detail.update(counted_record=True, operation=operation,
                          families=sorted(k for k, v in families.items() if operation in v))
    added_details.append(detail)

land_f4 = command('landing-f4', [sys.executable, '-B', F4, REPO / 'corpus'])
land_oracle = command('landing-oracle', [sys.executable, '-B', ORACLE, TRUTH, record_path])
assert land_f4['exit'] == 0
assert land_oracle['exit'] == 0
assert 'ORACLE OK (19/19 checks)' in land_oracle['stdout']
xml = ET.fromstring(record['normalized_result']['manifest']['text'])
xml_facts = {'tag': xml.tag, 'attributes': xml.attrib}
mutations = []
for name, path, value in (
    ('package-name', ('normalized_result', 'package_name'), 'com.example.fabricated'),
    ('class-count', ('normalized_result', 'class_count'), 1),
    ('subject-digest', ('subject', 'digest', 'sha256'), 'f' * 64),
    ('manifest-contradiction', ('normalized_result', 'manifest', 'text'),
     '<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.attacker.fabricated" android:versionCode="999" android:versionName="999"><!-- android:versionCode="1" android:versionName="1.0" --></manifest>')
):
    mutated = copy.deepcopy(record)
    cursor = mutated
    for field in path[:-1]:
        cursor = cursor[field]
    cursor[path[-1]] = value
    root = SCRATCH / 'landing-cases' / name / 'corpus'
    shutil.copytree(SCRATCH / 'base/corpus/live/runs', root / 'live/runs')
    p = root / 'live/runs/round-89/mutated-producer-record.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    serialized = (json.dumps(mutated, sort_keys=True, indent=2) + '\n').encode()
    p.write_bytes(serialized)
    (OUT / ('producer-input-' + name + '.json')).write_bytes(serialized)
    f4 = command('producer-' + name + '-f4', [sys.executable, '-B', F4, root])
    oracle = command('producer-' + name + '-oracle', [sys.executable, '-B', ORACLE, TRUTH, p])
    expected = 0 if name == 'manifest-contradiction' else 1
    assert f4['exit'] == 0 and 'F4_COVERAGE=11/11' in f4['stdout']
    assert oracle['exit'] == expected
    mutation = {'name': name, 'f4': f4, 'oracle': oracle}
    if name == 'manifest-contradiction':
        parsed = ET.fromstring(mutated['normalized_result']['manifest']['text'])
        mutation['parsed_actual_attributes'] = parsed.attrib
        assert parsed.attrib['{http://schemas.android.com/apk/res/android}versionCode'] == '999'
        assert parsed.attrib['{http://schemas.android.com/apk/res/android}versionName'] == '999'
    mutations.append(mutation)
summary = {
    'record_path': str(record_path), 'record_sha256': sha(record_bytes),
    'old_run_files': len(old_files), 'working_run_files': len(new_files),
    'removed_old_files': removed, 'modified_old_files': modified, 'added_files': added_details,
    'land_f4': land_f4, 'land_oracle': land_oracle,
    'producer_manifest_parsed': xml_facts,
    'mutations_from_actual_producer_record': mutations,
}
(OUT / 'landing-review-summary.json').write_text(json.dumps(summary, sort_keys=True, indent=2) + '\n')
print(json.dumps(summary, sort_keys=True, indent=2))
