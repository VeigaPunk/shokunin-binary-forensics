#!/usr/bin/env python3
"""Attack A6 (extra): duplicate JSON keys inside a NEW-ROW receipt. The frozen eleven
cover dup-keys for the registry (V03) and a vote (V04); this probes whether the receipts
leg reads receipts with the same strict reader. Expects C1_RECEIPTS to fail on the
strict-JSON hook; if it survives, route to r96.
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
    rec_p = root / C.RECEIPTS_DIR / "S500.receipt.json"
    raw = rec_p.read_text(encoding="utf-8")
    needle = '"fetched_at": "2026-11-05"'
    assert needle in raw, "receipt field anchor not found"
    raw2 = raw.replace(needle, needle + ', "fetched_at": "2026-11-05"', 1)
    rec_p.write_text(raw2, encoding="utf-8")

    # direct probe: does the strict reader reject it while plain json.loads would not?
    plain_ok = True
    try:
        json.loads(raw2)
    except ValueError:
        plain_ok = False
    strict_ok, strict_why = True, ""
    try:
        C.strict_json(raw2)
    except ValueError as e:
        strict_ok, strict_why = False, str(e)

    r = subprocess.run([sys.executable, "-B", str(COUNTER), "--tree", str(root)],
                       cwd=str(LANE), capture_output=True, text=True,
                       env={**os.environ, "HYAKU_SCRATCH": str(workroot)})
    legs = failing_legs(r.stdout)
    if r.returncode == 0:
        verdict = "SURVIVED"
    elif "C1_RECEIPTS" in legs:
        verdict = "killed"
    else:
        verdict = "killed-other-legs"
    receipt = {
        "attack": "A6-receipt-dup-json-keys",
        "shape": "(extra) S500.receipt.json carries a literal duplicate fetched_at key",
        "plain_json_loads_ok": plain_ok,
        "strict_json_rejects": not strict_ok,
        "strict_why": strict_why,
        "rc": r.returncode, "verdict": verdict, "expected_leg": "C1_RECEIPTS",
        "failing_legs": legs,
        "why": [ln for ln in r.stdout.splitlines() if ln.startswith("C1_RECEIPTS_WHY")],
        "counter_stdout": r.stdout,
        "counter_stderr": r.stderr[-400:],
        "fixture_root": str(root),
    }
    receipt_out.write_text(json.dumps(receipt, indent=1), encoding="utf-8")
    print(json.dumps({"receipt": str(receipt_out), "rc": r.returncode,
                      "verdict": verdict, "failing_legs": legs}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
