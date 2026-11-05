#!/usr/bin/env python3
"""Attack A5 (shape e): SOURCES row S500 whose teaches cell contains an escaped pipe
(`\\|`). parse_sources splits cells naively on `|`, so the row grows to !=11 cells and is
silently dropped from the registry read; every sid check that needs S500 should then
fail. Records which legs actually fire.
"""
import importlib.util, json, os, subprocess, sys
from pathlib import Path

SCRIPT = Path(__file__).resolve()
LANE = SCRIPT.parent
while not (LANE / "corpus").is_dir():
    LANE = LANE.parent
assert (LANE / "corpus").is_dir(), LANE
COUNTER = LANE / "reports/round-95/c1_k_admit_counter4.py"
_spec = importlib.util.spec_from_file_location("c1v4counter", COUNTER)
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)


def failing_legs(stdout):
    return [ln.split("=", 1)[0] for ln in stdout.splitlines()
            if ln.startswith("C1_") and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]


def main():
    workroot = Path(sys.argv[1]).resolve()
    receipt_out = Path(sys.argv[2]).resolve()
    workroot.mkdir(parents=True, exist_ok=True)
    root, want = C._fixture(workroot)
    src_p = root / "corpus/SOURCES.md"
    text = src_p.read_text(encoding="utf-8")
    needle = "the confidence enum and authority vocabulary are unchanged"
    assert text.count(needle) == 1, "S500 teaches anchor not found"
    text = text.replace(needle, "the confidence enum \\| authority vocabulary are unchanged")
    src_p.write_text(text, encoding="utf-8")

    # what does the frozen strict reader make of the mutated row?
    try:
        rows = C.parse_sources(root)
        s500_seen = "S500" in rows
        s500_cells = len(rows.get("S500", []))
    except ValueError as e:
        s500_seen, s500_cells = f"ValueError: {e}", -1

    r = subprocess.run([sys.executable, "-B", str(COUNTER), "--tree", str(root)],
                       cwd=str(LANE), capture_output=True, text=True,
                       env={**os.environ, "HYAKU_SCRATCH": str(workroot)})
    legs = failing_legs(r.stdout)
    if r.returncode == 0:
        verdict = "SURVIVED"
    elif "C1_SOURCES" in legs or "C1_SIDS" in legs:
        verdict = "killed"
    else:
        verdict = "killed-other-legs"
    receipt = {
        "attack": "A5-escaped-pipe-sources-cell",
        "shape": "(e) S500 teaches cell carries an escaped `\\|` pipe; naive cell splitter widens the row",
        "parse_sources_after_mutation": {"s500_seen": s500_seen,
                                         "s500_cell_count": s500_cells},
        "rc": r.returncode, "verdict": verdict,
        "expected_leg": "C1_SOURCES or C1_SIDS",
        "failing_legs": legs,
        "why": [ln for ln in r.stdout.splitlines() if ln.startswith("C1_SOURCES_WHY")
                or ln.startswith("C1_SIDS_WHY")],
        "counter_stdout": r.stdout,
        "counter_stderr": r.stderr[-400:],
        "fixture_root": str(root),
    }
    receipt_out.write_text(json.dumps(receipt, indent=1), encoding="utf-8")
    print(json.dumps({"receipt": str(receipt_out), "rc": r.returncode,
                      "verdict": verdict, "failing_legs": legs,
                      "s500_seen": s500_seen, "s500_cells": s500_cells}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
