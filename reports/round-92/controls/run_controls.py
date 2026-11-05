#!/usr/bin/env python3
"""Round-92 pre-freeze control runner (committed before any scoring).

Builds scratch copies of the lane's corpus/ and reports/round-92/ and runs the two
frozen counters over: the do-nothing base, skip-work/junk variants that must FAIL,
and one positive control that performs only the intended real move and must PASS.
Writes one receipt per control under reports/round-92/controls/ and prints a summary.

  C2 positive: row C08 frontier -> uncovered only (its record exists; no knowledge claimed)
  C2 junk A  : C08 -> held with no backing file (token without backing)
  C2 junk B  : row C08 deleted (denominator games)
  C1 junk    : stub entry with admitted line, C03 -> held, no votes, S999 unknown source
Usage: run_controls.py   (cwd irrelevant; writes into the lane)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
R92 = LANE / "reports/round-92"
OUT = R92 / "controls"
C2 = R92 / "c2_legend_counter.py"
C1 = R92 / "c1_k_admit_counter.py"
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r92" / "controls"


def build(name, edit):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    d = Path(tempfile.mkdtemp(prefix=f"{name}-", dir=str(SCRATCH)))
    shutil.copytree(LANE / "corpus", d / "corpus")
    (d / "reports/round-92").mkdir(parents=True)
    if (R92 / "votes").is_dir():
        shutil.copytree(R92 / "votes", d / "reports/round-92/votes")
    edit(d)
    return d


def sub_row(d, cid, new_line_fn):
    p = d / "corpus/README.md"
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    for ln in lines:
        if re.match(rf"^\| {cid} ", ln):
            r = new_line_fn(ln)
            if r is not None:
                out.append(r)
        else:
            out.append(ln)
    p.write_text("".join(out), encoding="utf-8")


def c08_held(ln):
    return ln.replace("| frontier |", "| held |")


def c08_uncovered(ln):
    return ln.replace("| frontier |", "| uncovered |")


def c08_deleted(ln):
    return None


def c03_held_stub(d):
    sub_row(d, "C03", lambda ln: ln.replace(
        "| — | — | frontier |",
        "| `knowledge/round-92-managed-assembly-metadata-evidence.md` | — | held |"))
    (d / "corpus/knowledge").mkdir(exist_ok=True)
    (d / "corpus/knowledge/round-92-managed-assembly-metadata-evidence.md").write_text(
        "source: S999 (not in registry)\nverified-at: test\nrecheck: test\n"
        "admission-status: admitted\n\nStub body without votes or embedded outputs.\n",
        encoding="utf-8")


def run(counter, tree, label, log_name):
    pr = subprocess.run([sys.executable, "-B", str(counter), "--tree", str(tree)],
                        capture_output=True, text=True)
    txt = pr.stdout + pr.stderr
    (OUT / log_name).write_text(f"# {label}\n# counter exit={pr.returncode}\n{txt}", encoding="utf-8")
    verdict = re.search(r"(C[12])_VERDICT=(\w+)", txt)
    return (verdict.group(2) if verdict else "none"), pr.returncode


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    results = []
    cases = [
        ("c2-do-nothing", C2, lambda d: None, "C2 do-nothing (base tree)", "c2-do-nothing.log", "pass-required:no"),
        ("c2-positive", C2, lambda d: sub_row(d, "C08", c08_uncovered), "C2 positive: C08 frontier->uncovered only", "c2-positive.log", "pass-required:yes"),
        ("c2-junk-held", C2, lambda d: sub_row(d, "C08", c08_held), "C2 junk A: C08 held with no backing file", "c2-junk-held.log", "pass-required:no"),
        ("c2-junk-deleted", C2, lambda d: sub_row(d, "C08", c08_deleted), "C2 junk B: C08 row deleted", "c2-junk-deleted.log", "pass-required:no"),
        ("c1-do-nothing", C1, lambda d: None, "C1 do-nothing (base tree)", "c1-do-nothing.log", "pass-required:no"),
        ("c1-junk-stub", C1, c03_held_stub, "C1 junk: stub entry, C03 held, no votes, S999", "c1-junk-stub.log", "pass-required:no"),
    ]
    for name, counter, edit, label, log, want in cases:
        d = build(name, edit)
        try:
            verdict, code = run(counter, d, label, log)
        finally:
            shutil.rmtree(d, ignore_errors=True)
        expect = "pass" if want.endswith("yes") else "fail"
        results.append((name, verdict, code, "OK" if verdict == expect else "UNEXPECTED"))
        print(f"{name}\tverdict={verdict}\texit={code}\texpected={expect}\t{results[-1][3]}")
    bad = [r for r in results if r[3] != "OK"]
    print(f"CONTROLS_UNEXPECTED={len(bad)}/{len(results)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
