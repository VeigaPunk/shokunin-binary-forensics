#!/usr/bin/env python3
"""Round-92 C2 frozen counter (calibration): coverage-map token vs saved records.

Measures the README coverage map against the saved-record evidence with the
frozen round-66 legend probe (`reports/round-66/measure.py`, run unmodified, cwd=/,
TMPDIR under lane scratch) and adds three checks the probe does not make:

  C2_ROWS_TOTAL   the coverage map keeps 15 rows (no row deleted to clear a flag)
  C2_C08_CLEAR    row C08 is not flagged by the legend probe
  C2_NO_NEW       every flagged row is C03 (the round's other claim owns C03)
  C2_NO_UNBACKED  K_HELD == K_HELD_BACKED: no `held` token without a backing file

Usage:
  c2_legend_counter.py --rev REV       committed tree (git archive of corpus/ + reports/round-92/)
  c2_legend_counter.py --tree DIR      a directory containing corpus/ (controls only)

Prints C2_* lines and C2_VERDICT=pass|fail; exit 0 iff pass, 1 otherwise, 64 usage.
"""
import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
PROBE = LANE / "reports/round-66/measure.py"
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r92" / "c2"


def main(argv):
    rev = tree = None
    i = 0
    while i < len(argv):
        if argv[i] == "--rev":
            rev = argv[i + 1]; i += 2
        elif argv[i] == "--tree":
            tree = Path(argv[i + 1]); i += 2
        else:
            print(__doc__, file=sys.stderr); return 64
    if bool(rev) == bool(tree):
        print(__doc__, file=sys.stderr); return 64

    SCRATCH.mkdir(parents=True, exist_ok=True)
    d = Path(tempfile.mkdtemp(prefix="c2-", dir=str(SCRATCH)))
    try:
        if rev:
            ar = subprocess.run(["git", "-C", str(LANE), "archive", rev, "corpus"],
                                capture_output=True)
            if ar.returncode != 0:
                print(f"C2_VERDICT=fail reason=archive-failed {ar.stderr.decode()[:200]}")
                return 1
            subprocess.run(["tar", "-x", "-C", str(d)], input=ar.stdout, check=True)
        else:
            shutil.copytree(tree / "corpus", d / "corpus")
        (d / "tmp").mkdir()
        pr = subprocess.run([sys.executable, "-B", str(PROBE), str(d)], cwd="/",
                            env={**os.environ, "TMPDIR": str(d / "tmp")},
                            capture_output=True, text=True)
        out = pr.stdout + pr.stderr
        m = re.search(r"README_TOKEN_LEGEND_MISMATCH=(\d+) rows=(\[.*?\])", out)
        kh = re.search(r"^K_HELD=(\d+)/(\d+)", out, re.M)
        khb = re.search(r"^K_HELD_BACKED=(\d+)/(\d+)", out, re.M)
        if not (m and kh and khb):
            print(f"C2_VERDICT=fail reason=probe-labels-missing probe_exit={pr.returncode}")
            return 1
        rows = ast.literal_eval(m.group(2))
        held_tok, held_backed = int(kh.group(1)), int(khb.group(1))
        n_rows = sum(1 for ln in (d / "corpus/README.md").read_text(encoding="utf-8").splitlines()
                     if re.match(r"^\| C[0-9]+ ", ln))
        legs = {
            "C2_ROWS_TOTAL": n_rows == 15,
            "C2_C08_CLEAR": "C08" not in rows,
            "C2_NO_NEW": set(rows) <= {"C03"},
            "C2_NO_UNBACKED": held_tok == held_backed,
        }
        print(f"C2_PROBE_EXIT={pr.returncode} (probe exit is not the claim verdict)")
        print(f"C2_LEGEND_MISMATCH={len(rows)} rows={rows}")
        print(f"C2_ROWS_COUNT={n_rows}")
        print(f"C2_K_HELD={held_tok}/{kh.group(2)} C2_K_HELD_BACKED={held_backed}/{khb.group(2)}")
        for k, v in legs.items():
            print(f"{k}={'pass' if v else 'fail'}")
        ok = all(legs.values())
        print(f"C2_VERDICT={'pass' if ok else 'fail'}")
        return 0 if ok else 1
    finally:
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
