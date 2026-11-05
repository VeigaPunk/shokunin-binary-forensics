#!/usr/bin/env python3
"""Attack A1 (shape a): committed receipt body swapped AFTER the fetch-log was written.

The competent-forger variant: the receipt is re-bound to the swapped body (so
body-rehash passes, host/fetched_at/http_status stay honest); only the committed
fetch-log line still names the OLD sha, because it was written before the swap.
Runs the frozen v4 counter end-to-end with --tree and records rc + failing legs.
"""
import hashlib, importlib.util, json, os, subprocess, sys
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
    sid = "S500"
    body_p = root / C.RECEIPTS_DIR / "raw" / f"{sid}.body"
    rec_p = root / C.RECEIPTS_DIR / f"{sid}.receipt.json"
    log_p = root / C.FETCH_LOG_REL
    old_body = body_p.read_text(encoding="utf-8")
    old_sha = hashlib.sha256(old_body.encode("utf-8")).hexdigest()
    # swap the committed body after the fetch-log was written: append post-hoc content
    # (append keeps the audited quote/span intact so C1_QUOTES stays green and the
    # failure attributes cleanly to the receipt leg)
    new_body = old_body + ("Post-fetch swap: this tail was appended after the fetch-log "
                           "line had already been committed with the old sha.\n")
    body_p.write_text(new_body, encoding="utf-8")
    new_sha = hashlib.sha256(new_body.encode("utf-8")).hexdigest()
    rec = json.loads(rec_p.read_text(encoding="utf-8"))
    assert rec["fetch_sha256"] == old_sha
    rec["fetch_sha256"] = new_sha          # forger re-binds the receipt to the new body
    rec["length"] = len(new_body.encode("utf-8"))
    rec_p.write_text(json.dumps(rec, indent=1), encoding="utf-8")
    # fetch-log.md deliberately left as committed: its S500 line still names old_sha
    log_has_new = any(sid in ln and new_sha in ln for ln in log_p.read_text(encoding="utf-8").splitlines())
    assert not log_has_new

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
        "attack": "A1-body-swap-stale-log",
        "shape": "(a) S500 body appended after fetch-log commit; receipt re-bound to new body; log line still names the old sha",
        "old_body_sha256": old_sha, "new_body_sha256": new_sha,
        "rc": r.returncode, "verdict": verdict, "expected_leg": "C1_RECEIPTS",
        "failing_legs": legs,
        "why": [ln for ln in r.stdout.splitlines() if ln.startswith("C1_RECEIPTS_WHY")
                or ln.startswith("C1_QUOTES_WHY")],
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
