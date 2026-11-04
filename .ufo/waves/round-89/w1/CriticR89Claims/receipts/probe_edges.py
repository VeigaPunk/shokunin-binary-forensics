#!/usr/bin/env python3
"""Supplement exact commands and counterexamples; writes only own scratch."""
import concurrent.futures
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
os.environ.update({key: ENV[key] for key in ('TMPDIR', 'PYTHONUTF8', 'PYTHONDONTWRITEBYTECODE')})
R = json.loads((S / 'results.json').read_text())
CENSUS = S / 'freeze/corpus/census_reprobe.py'
F4 = S / 'freeze/reports/round-81/f_probe4.py'
SEED = Path('corpus/knowledge/seed.md')
CHECK = Path('corpus/knowledge/2026-10-12-rea-readiness-checklist.md')
P = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ExecR89Record')


def census(tree):
    return ['python3', '-B', str(CENSUS), '--root', str(tree)]


def run(item):
    name, argv = item
    done = subprocess.run(argv, cwd=S, env=ENV, capture_output=True, text=True, timeout=180)
    result = {'command': 'env TMPDIR=' + str(S) + ' PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 ' + shlex.join(map(str, argv)), 'stdout': done.stdout, 'stderr': done.stderr, 'exit': done.returncode}
    return name, result


# Cheap lies accepted by substring matching; K04 alone remains unsatisfiable.
for name, k04 in [('k04-minimum', '| K04 | mint | ghidra present; ida off PATH | reverified |'), ('negated-presence', '| K04 | mint | ghidra present; ida off PATH | reverified |')]:
    tree = S / name
    for rel in (SEED, CHECK):
        target = tree / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(S / 'c1-only' / rel, target)
    with (tree / CHECK).open('a') as file:
        file.write(k04 + '\n')
    if name == 'negated-presence':
        with (tree / SEED).open('a') as file:
            file.write('| F04 | mint | probe | rea is NOT present | holds |\n')

# ROWS file-key is ignored: every F row may disappear from seed yet be scored.
relocated = S / 'relocated-rows'
for rel in (SEED, CHECK):
    (relocated / rel).parent.mkdir(parents=True, exist_ok=True)
seed = (S / 'k04-minimum' / SEED).read_text().splitlines()
(relocated / SEED).write_text('\n'.join(line for line in seed if not re.match(r'^\|\s*F\d{2}\s*\|', line)) + '\n')
(relocated / CHECK).write_text((S / 'k04-minimum' / CHECK).read_text() + '\n' + '\n'.join(line for line in seed if re.match(r'^\|\s*F\d{2}\s*\|', line)) + '\n')

# A contradictory manifest (not merely missing attributes) is still accepted.
comment_record = S / 'comment-lie/corpus/live/runs/round-89/forged.json'
record = json.loads(comment_record.read_text())
record['normalized_result']['manifest']['text'] = '<manifest package="com.example.wrong" versionCode="999" versionName="999"><!-- versionCode="1" versionName="1.0" --></manifest>'
comment_record.write_text(json.dumps(record))

jobs = [
    ('k04_minimum', census(S / 'k04-minimum')),
    ('negated_presence', census(S / 'negated-presence')),
    ('relocated_rows', census(relocated)),
    ('comment_lie_strong_oracle', ['python3', '-B', str(S / 'comment-lie/corpus/fixtures/apk-r65/oracle_check.py'), str(S / 'comment-lie/corpus/fixtures/apk-r65/truth.json'), str(comment_record)]),
    ('comment_lie_f4', ['python3', '-B', str(F4), str(S / 'comment-lie/corpus')]),
    ('fixture_axml_bytes', ['python3', '-B', str(S / 'base/corpus/fixtures/apk-r65/readout.py'), '--fact', 'axml_string_pool']),
    ('producer_cmp', ['cmp', str(P / 'run1.json'), str(P / 'run2.json')]),
    ('producer_hashes', ['sha256sum', str(P / 'run1.json'), str(P / 'run2.json')]),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for name, result in pool.map(run, jobs):
        R[name] = result
        print('=== ' + name + ' ===\n$ ' + result['command'] + '\n' + result['stdout'] + result['stderr'] + 'EXIT=' + str(result['exit']), flush=True)
R['producer_receipt'] = json.loads((P / 'receipt.json').read_text())
R['producer_raw_sha256'] = {name: hashlib.sha256((P / name).read_bytes()).hexdigest() for name in ('run1.json', 'run2.json')}
R['strong_comment_record'] = record
(S / 'results.json').write_text(json.dumps(R, indent=2) + '\n')
