#!/usr/bin/env python3
"""Score an apk-r65 oracle over the ForgeryR90Probe 40-case set (round 90, unclaimed).
Usage: python3 -B reports/round-90/score_oracle_probe.py <oracle.py>
Labels come from the seat's results.tsv column 2 (yes/strict = misstates -> must REJECT; no -> must ACCEPT)."""
import csv, glob, subprocess, sys
L = __file__.rsplit('/reports/', 1)[0]
D = L + '/.ufo/waves/round-90/w1/ForgeryR90Probe'
oracle = sys.argv[1]
print(f'# oracle {oracle} over the 40 ForgeryR90Probe cases; columns: case | label | v2 verdict (seat) | verdict | class')
c = {}
for r in csv.reader(open(D + '/results.tsv'), delimiter='\t'):
    cid, lab, v2 = r[0], r[1], r[2]
    rc = subprocess.run([sys.executable, '-B', oracle, L + '/corpus/fixtures/apk-r65/truth.json', D + f'/cases/{cid}.json'],
                        capture_output=True, text=True).returncode
    v = {0: 'ACCEPT', 1: 'REJECT'}.get(rc, f'rc{rc}')
    cls = 'ok' if (lab in ('yes', 'strict')) == (v == 'REJECT') else ('FALSE-GREEN' if v == 'ACCEPT' else 'false-red')
    c[cls] = c.get(cls, 0) + 1
    print(f'{cid} | {lab} | {v2} | {v} | {cls}')
print('TOTALS', dict(sorted(c.items())))
print(f"FALSE_GREEN={c.get('FALSE-GREEN', 0)}")
