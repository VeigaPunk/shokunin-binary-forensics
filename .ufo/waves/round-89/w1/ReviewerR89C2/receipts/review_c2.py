#!/usr/bin/env python3
"""Read-only lane review; generated inputs and subprocess outputs stay in scratch."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import shlex
import shutil
import struct
import subprocess
import sys
import tarfile
from concurrent.futures import ThreadPoolExecutor

REPO = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin')
SCRATCH = Path('/fast/scratch/hyaku/revenger-r89/ReviewerR89C2')
OUT = SCRATCH / 'receipts'
BASE = '2b017fa3c616a84b7b491e3312029fa8a8c076e6'
FREEZE = 'c84339c'
ENV = {**os.environ, 'TMPDIR': str(SCRATCH), 'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
FIXTURE = REPO / 'corpus/fixtures/apk-r65'
ORACLE = FIXTURE / 'oracle_check.py'
F4 = REPO / 'reports/round-81/f_probe4.py'
TRUTH = FIXTURE / 'truth.json'
OUT.mkdir(parents=True, exist_ok=True)


def command(name, args):
    completed = subprocess.run([str(a) for a in args], env=ENV, cwd=SCRATCH,
                               capture_output=True, timeout=90, check=False)
    prefix = 'env TMPDIR=' + str(SCRATCH) + ' PYTHONUTF8=1 '
    text = ('$ ' + prefix + shlex.join([str(a) for a in args]) + '\n'
            + completed.stdout.decode('utf-8', 'replace')
            + ('STDERR:\n' + completed.stderr.decode('utf-8', 'replace') if completed.stderr else '')
            + f'EXIT={completed.returncode}\n')
    (OUT / (name + '.log')).write_text(text)
    return {'name': name, 'command': prefix + shlex.join([str(a) for a in args]),
            'exit': completed.returncode, 'stdout': completed.stdout.decode('utf-8', 'replace'),
            'stderr': completed.stderr.decode('utf-8', 'replace')}


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


archive = subprocess.run(['git', '-C', str(REPO), 'archive', BASE, 'corpus'],
                         env=ENV, cwd=SCRATCH, capture_output=True, check=True, timeout=90)
with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tf:
    tf.extractall(SCRATCH / 'base', filter='data')
base_corpus = SCRATCH / 'base/corpus'
red = command('base-f4', [sys.executable, '-B', F4, base_corpus])
assert red['exit'] == 0 and 'F4_COVERAGE=10/11' in red['stdout']
assert 'inspect_android_package' not in red['stdout']
readout = command('fixture-byte-readout', [sys.executable, '-B', FIXTURE / 'readout.py'])
assert readout['exit'] == 0
facts = {r['fact']: r for line in readout['stdout'].splitlines() if (r := json.loads(line))}
truth = json.loads(TRUTH.read_bytes())
assert facts['axml_string_pool']['strings'] == truth['axml_declared']['strings']
attrs = {a['name']: a['raw_value'] for a in facts['axml_start_element']['attributes']}
assert attrs == {'package': 'com.example.r65', 'versionCode': '1', 'versionName': '1.0'}
from zipfile import ZipFile
with ZipFile(FIXTURE / 'fixture.apk') as z:
    dex = z.read('classes.dex')
    classes = struct.unpack_from('<I', dex, 0x60)[0]
    resource_count = len(z.infolist())
assert classes == 0 and resource_count == 3

pins = {}
for name in ('reports/round-81/f_probe4.py', 'corpus/fixtures/apk-r65/oracle_check.py',
             'corpus/fixtures/apk-r65/fixture.apk', 'corpus/fixtures/apk-r65/truth.json'):
    current = (REPO / name).read_bytes()
    at_freeze = subprocess.run(['git', '-C', str(REPO), 'show', FREEZE + ':' + name],
                               env=ENV, cwd=SCRATCH, capture_output=True, timeout=30, check=True).stdout
    item = {'working_sha256': hashlib.sha256(current).hexdigest(),
            'freeze_sha256': hashlib.sha256(at_freeze).hexdigest(),
            'working_equal_freeze': current == at_freeze}
    at_base = subprocess.run(['git', '-C', str(REPO), 'show', BASE + ':' + name],
                             env=ENV, cwd=SCRATCH, capture_output=True, timeout=30)
    item['base_exists'] = at_base.returncode == 0
    if at_base.returncode == 0:
        item['base_sha256'] = hashlib.sha256(at_base.stdout).hexdigest()
        item['working_equal_base'] = current == at_base.stdout
    pins[name] = item

# Hand-authored from known byte facts, not copied from any producer record.
handwritten = {
    'operation': 'inspect_android_package',
    'provider': {'id': 'jadx', 'version': '0.7.1'},
    'evidence_id': 'ev_' + '0' * 64,
    'subject': {'format': 'apk', 'digest': {'sha256': facts['archive']['sha256']}},
    'normalized_result': {
        'package_name': attrs['package'],
        'manifest': {'status': 'complete', 'text': '<manifest package="com.example.r65" versionCode="1" versionName="1.0" />'},
        'class_count': classes, 'resource_count': resource_count,
        'permissions': [], 'signature_verification': 'not_performed'
    }
}
cases = {}
cases['handwritten'] = (handwritten, TRUTH)
for name, path, value in (
    ('package-name', ('normalized_result', 'package_name'), 'com.example.fabricated'),
    ('class-count', ('normalized_result', 'class_count'), 1),
    ('subject-digest', ('subject', 'digest', 'sha256'), 'f' * 64),
    ('provider-version', ('provider', 'version'), '9.9.9'),
    ('evidence-id', ('evidence_id',), 'ev_' + 'f' * 64),
    ('manifest-contradiction', ('normalized_result', 'manifest', 'text'),
     '<manifest package="com.attacker.fabricated" versionCode="999" versionName="999"><!-- versionCode="1" versionName="1.0" --></manifest>'),
):
    mutated = copy.deepcopy(handwritten)
    cursor = mutated
    for field in path[:-1]:
        cursor = cursor[field]
    cursor[path[-1]] = value
    cases[name] = (mutated, TRUTH)
false_truth = copy.deepcopy(truth)
false_truth['axml_declared']['strings'][4] = 'com.example.fabricated'
false_truth_path = OUT / 'truth-metadata-only-mutated.json'
save_json(false_truth_path, false_truth)
metadata_record = copy.deepcopy(handwritten)
metadata_record['normalized_result']['package_name'] = 'com.example.fabricated'
cases['truth-metadata-mismatch'] = (metadata_record, false_truth_path)


def run_case(item):
    name, (record, truth_path) = item
    root = SCRATCH / 'cases' / name / 'corpus'
    shutil.copytree(base_corpus / 'live/runs', root / 'live/runs')
    record_path = root / 'live/runs/round-89/reviewer-forgery.json'
    save_json(record_path, record)
    save_json(OUT / ('input-' + name + '.json'), record)
    f4 = command(name + '-f4', [sys.executable, '-B', F4, root])
    oracle = command(name + '-oracle', [sys.executable, '-B', ORACLE, truth_path, record_path])
    return {'name': name, 'record': str(record_path), 'f4': f4, 'oracle': oracle}

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(run_case, cases.items()))
for r in results:
    assert r['f4']['exit'] == 0 and 'F4_COVERAGE=11/11' in r['f4']['stdout']
    expected = 1 if r['name'] in {'package-name', 'class-count', 'subject-digest'} else 0
    assert r['oracle']['exit'] == expected, r
    if expected:
        assert 'ORACLE FAIL (18/19 checks)' in r['oracle']['stdout']
    else:
        assert 'ORACLE OK (19/19 checks)' in r['oracle']['stdout']
summary = {
    'axes': ['coverage', 'calibration'],
    'base': BASE, 'freeze': FREEZE, 'base_f4': red,
    'lsp': 'xd://lsp absent; read and status dispatch both returned No such tool. Text fallback is not semantic evidence.',
    'pins': pins, 'byte_derived_attributes': attrs, 'truth_strings_equal_actual_bytes': True,
    'dex_class_defs_size': classes, 'zip_member_count': resource_count,
    'cases': results, 'tools_installed_or_updated': []
}
save_json(OUT / 'review-summary.json', summary)
print(json.dumps({
    'base': 'F4_COVERAGE=10/11', 'truth_strings_match_actual_bytes': True,
    'pins': pins,
    'cases': [{'name': r['name'], 'f4': '11/11', 'oracle_exit': r['oracle']['exit'],
               'oracle_verdict': r['oracle']['stdout'].splitlines()[-1]} for r in results]
}, indent=2))
