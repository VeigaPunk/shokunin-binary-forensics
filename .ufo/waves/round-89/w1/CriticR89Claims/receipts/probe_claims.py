#!/usr/bin/env python3
"""Read-only lane review; all trees and controls are created in own scratch."""
import concurrent.futures
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess

S = Path('/fast/scratch/hyaku/revenger-r89/CriticR89Claims')
ENV = dict(os.environ, TMPDIR=str(S), PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
os.environ.update({k: ENV[k] for k in ('TMPDIR', 'PYTHONUTF8', 'PYTHONDONTWRITEBYTECODE')})
BASE = S / 'base'
FREEZE = S / 'freeze'
CENSUS = FREEZE / 'corpus/census_reprobe.py'
F4 = FREEZE / 'reports/round-81/f_probe4.py'
ORACLE = FREEZE / 'corpus/fixtures/apk-r65/oracle_check.py'
FIXTURE = Path('corpus/fixtures/apk-r65')
SEED = Path('corpus/knowledge/seed.md')
CHECK = Path('corpus/knowledge/2026-10-12-rea-readiness-checklist.md')
RUNS = Path('corpus/live/runs/round-89')
results = {}


def command(name, argv):
    result = subprocess.run(argv, cwd=S, env=ENV, capture_output=True, text=True, timeout=180)
    return name, {
        'command': 'env TMPDIR=' + str(S) + ' PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 ' + shlex.join(map(str, argv)),
        'stdout': result.stdout, 'stderr': result.stderr, 'exit': result.returncode,
    }


def score_census(tree):
    return ['python3', '-B', str(CENSUS), '--root', str(tree)]


def score_f4(tree):
    return ['python3', '-B', str(F4), str(tree / 'corpus')]


def score_oracle(tree, record):
    return ['python3', '-B', str(tree / FIXTURE / 'oracle_check.py'), str(tree / FIXTURE / 'truth.json'), str(record)]


spec = importlib.util.spec_from_file_location('frozen_census', CENSUS)
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)
live_values = {rid: [census.live(item) for item in specs] for rid, (_, specs) in census.ROWS.items()}
results['live_values'] = live_values

# Freshness-only: immutable full base, with only the two census files appended.
c1 = S / 'c1-only'
shutil.copytree(BASE, c1)
for file_key, rel in (('seed', SEED), ('check', CHECK)):
    rows = []
    for rid, (key, specs) in census.ROWS.items():
        if key != file_key:
            continue
        observations = []
        for (kind, arg), (_, _, tokens, _) in zip(specs, live_values[rid]):
            observations.append(f'{kind}:{arg}: ' + ', '.join(tokens))
        observed = '; '.join(observations)
        cells = f'| {rid} | unchanged historical mint | '
        if key == 'seed':
            cells += 'same frozen probes | '
        rows.append(cells + observed + ' | reverified |')
    with (c1 / rel).open('a', encoding='utf-8') as file:
        file.write('\n## Re-verification 2026-11-04 — truthful critic control\n\n' + '\n'.join(rows) + '\n')

# Coverage-only: immutable full base, adding only frozen oracle and raw run1.
c2 = S / 'c2-only'
shutil.copytree(BASE, c2)
(c2 / RUNS).mkdir(parents=True)
record = c2 / RUNS / 'android.json'
source = Path('/fast/scratch/hyaku/revenger-r89/ExecR89Record/run1.json')
shutil.copyfile(source, record)
shutil.copyfile(ORACLE, c2 / FIXTURE / 'oracle_check.py')
results['candidate_sha256'] = hashlib.sha256(record.read_bytes()).hexdigest()

# Kill deletion controls: no rows and no census files cannot score zero.
deleted_rows = S / 'deleted-rows'
for rel in (SEED, CHECK):
    target = deleted_rows / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(line for line in (BASE / rel).read_text().splitlines() if not re.match(r'^\|\s*[FK]\d{2}\s*\|', line)) + '\n')
missing_files = S / 'missing-files'
missing_files.mkdir()

# A 19-check record-shaped forgery: no raw_result/engine/session/provider run.
forged = S / 'forged'
shutil.copytree(BASE, forged)
(forged / RUNS).mkdir(parents=True)
shutil.copyfile(ORACLE, forged / FIXTURE / 'oracle_check.py')
truth = json.loads((forged / FIXTURE / 'truth.json').read_text())
minimal = {
    'operation': 'inspect_android_package', 'evidence_id': 'ev_' + '0' * 64,
    'provider': {'id': 'jadx', 'version': '0.0.0'},
    'subject': {'digest': {'sha256': truth['image']['sha256']}, 'format': 'apk'},
    'normalized_result': {
        'package_name': 'com.example.r65', 'manifest': {'status': 'complete', 'text': 'versionCode="1" versionName="1.0"'},
        'class_count': 0, 'resource_count': 3, 'permissions': [], 'signature_verification': 'not_performed',
    },
}
forged_record = forged / RUNS / 'forged.json'
forged_record.write_text(json.dumps(minimal))
results['forged_record'] = minimal

# Unvalidated truth metadata acts as a second authority, independent of bytes.
truth_lie = S / 'truth-lie'
shutil.copytree(forged, truth_lie)
lie_truth = copy.deepcopy(truth)
lie_truth['axml_declared']['strings'][4] = 'com.example.not_in_apk'
lie_truth['axml_declared']['strings'][7] = '999'
lie_truth['axml_declared']['strings'][8] = '9.9'
(truth_lie / FIXTURE / 'truth.json').write_text(json.dumps(lie_truth))
lie_record = copy.deepcopy(minimal)
lie_record['normalized_result']['package_name'] = 'com.example.not_in_apk'
lie_record['normalized_result']['manifest']['text'] = 'versionCode="999" versionName="9.9"'
(truth_lie / RUNS / 'forged.json').write_text(json.dumps(lie_record))
results['truth_lie_apk_unchanged'] = hashlib.sha256((truth_lie / FIXTURE / 'fixture.apk').read_bytes()).hexdigest()

# Even a false manifest package plus attributes inside an XML comment passes.
comment_lie = S / 'comment-lie'
shutil.copytree(forged, comment_lie)
comment_record = copy.deepcopy(minimal)
comment_record['normalized_result']['manifest']['text'] = '<manifest package="com.example.wrong"/><!-- versionCode="1" versionName="1.0" -->'
(comment_lie / RUNS / 'forged.json').write_text(json.dumps(comment_record))

# Current-run weakening can retain current id/version/identity yet discard real evidence.
weakened = S / 'weakened-current'
shutil.copytree(forged, weakened)
weak_record = json.loads(record.read_text())
weak_record.pop('raw_result', None)
weak_record['normalized_result'].pop('engine', None)
weak_record['normalized_result']['manifest']['text'] = 'versionCode="1" versionName="1.0"'
(weakened / RUNS / 'forged.json').write_text(json.dumps(weak_record))

jobs = [
    ('base_census', score_census(BASE)), ('base_f4', score_f4(BASE)),
    ('c1_census', score_census(c1)), ('c1_f4', score_f4(c1)),
    ('c2_census', score_census(c2)), ('c2_f4', score_f4(c2)),
    ('c2_oracle', score_oracle(c2, record)),
    ('selftest', ['python3', '-B', str(CENSUS), '--selftest']),
    ('deleted_rows_census', score_census(deleted_rows)), ('missing_files_census', score_census(missing_files)),
    ('forged_oracle', score_oracle(forged, forged_record)), ('forged_f4', score_f4(forged)),
    ('truth_lie_oracle', score_oracle(truth_lie, truth_lie / RUNS / 'forged.json')),
    ('comment_lie_oracle', score_oracle(comment_lie, comment_lie / RUNS / 'forged.json')),
    ('weakened_oracle', score_oracle(weakened, weakened / RUNS / 'forged.json')),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for name, result in pool.map(lambda item: command(*item), jobs):
        results[name] = result
        print('=== ' + name + ' ===\n$ ' + result['command'] + '\n' + result['stdout'] + result['stderr'] + 'EXIT=' + str(result['exit']), flush=True)
(S / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
print('LIVE_K04=' + json.dumps(live_values['K04']))
print('FORGED_RECORD=' + json.dumps(minimal, sort_keys=True))
