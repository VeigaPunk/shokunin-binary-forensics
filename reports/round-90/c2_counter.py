#!/usr/bin/env python3
"""Round-90 C2 counter: six frozen conjuncts over a lane TREE.

Usage:
    python3 -B reports/round-90/c2_counter.py --tree TREE

TREE is a `git archive <rev> corpus reports` extraction (or the lane root).
Conjuncts (all must hold; the predicate is their conjunction):
  K1 `reports/round-81/f_probe4.py TREE/corpus` prints `F4_COVERAGE=11/11`.
  K2 `corpus/fixtures/apk-r65/oracle_check2.py` accepts
     TREE/corpus/live/runs/round-90/inspection.json (exit 0, `ORACLE OK`).
  K3 `reports/round-90/oracle_battery.py --oracle <TREE oracle_check2.py>`
     prints `ORACLE_MISCLASS=0/9`.
  K4 `reports/round-90/norm_eq.py` over run1 (the landed inspection.json) and
     run2 (TREE/reports/round-90/android-run2.json) prints `NORM_EQ=identical`.
  K5 TREE/reports/round-90/android-receipt.json `runs[0].stdout_sha256` and
     `runs[1].stdout_sha256` equal the sha256 of run1 and run2 bytes.
  K6 the two runs carry distinct `evidence_id`s, neither equal to the
     round-89 record's `ev_387c9e9c…a588e4` (a copied or duplicated record
     cannot pass; hand-edited ids can — provenance is not machine-provable,
     Q09, and the claim does not assert it).
Prints `K<n>=pass|FAIL <detail>` lines and `C2_CONJUNCTS=<k>/6`.
Exit 0 iff 6/6, 1 otherwise, 64 on usage. Read-only.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

R89_ID = "ev_387c9e9c410dc40fb6a19524fcdda49a3186c4597c20e9c4a9625b3b99a588e4"


def run(*cmd):
    p = subprocess.run([sys.executable, "-B", *map(str, cmd)], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def main(argv):
    if "--tree" not in argv:
        print(__doc__, file=sys.stderr)
        return 64
    t = Path(argv[argv.index("--tree") + 1]).resolve()
    r1 = t / "corpus/live/runs/round-90/inspection.json"
    r2 = t / "reports/round-90/android-run2.json"
    rc_p = t / "reports/round-90/android-receipt.json"
    oracle = t / "corpus/fixtures/apk-r65/oracle_check2.py"
    res = {}
    _, out = run(t / "reports/round-81/f_probe4.py", t / "corpus")
    res["K1"] = ("F4_COVERAGE=11/11" in out, [l for l in out.splitlines() if l.startswith("F4_COVERAGE")])
    rc, out = run(oracle, t / "corpus/fixtures/apk-r65/truth.json", r1)
    res["K2"] = (rc == 0 and "ORACLE OK" in out, out.strip().splitlines()[-1:] if out.strip() else [])
    _, out = run(t / "reports/round-90/oracle_battery.py", "--oracle", oracle)
    res["K3"] = ("ORACLE_MISCLASS=0/9" in out, [l for l in out.splitlines() if l.startswith("ORACLE_MISCLASS")])
    rc, out = run(t / "reports/round-90/norm_eq.py", r1, r2)
    res["K4"] = (rc == 0 and "NORM_EQ=identical" in out, out.strip().splitlines()[:6])
    try:
        rec = json.loads(rc_p.read_text(encoding="utf-8"))
        s1, s2 = (hashlib.sha256(p.read_bytes()).hexdigest() for p in (r1, r2))
        want = [rec["runs"][0]["stdout_sha256"], rec["runs"][1]["stdout_sha256"]]
        res["K5"] = ([s1, s2] == want, [s1[:16], s2[:16]])
    except (OSError, ValueError, KeyError, IndexError) as e:
        res["K5"] = (False, [repr(e)])
    try:
        i1, i2 = (json.loads(p.read_text(encoding="utf-8")).get("evidence_id") for p in (r1, r2))
        res["K6"] = (bool(i1) and bool(i2) and i1 != i2 and R89_ID not in (i1, i2), [str(i1)[:20], str(i2)[:20]])
    except (OSError, ValueError) as e:
        res["K6"] = (False, [repr(e)])
    for k in sorted(res):
        print(f"{k}={'pass' if res[k][0] else 'FAIL'} {res[k][1]}")
    n = sum(1 for v in res.values() if v[0])
    print(f"C2_CONJUNCTS={n}/6")
    return 0 if n == 6 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
