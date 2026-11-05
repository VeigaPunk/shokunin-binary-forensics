#!/usr/bin/env python3
"""Attack A3 (shape c): C10 held with the exact entry fileset, but the SOURCES used-by
cell of the new rows names a DIFFERENT entry path that also exists — the superseded
2026-10-29 entry. Two modes:

  old  : used-by cell REPLACED by the superseded entry path  -> expect cite-back kill
  both : used-by cell names the superseded entry AND the real entry -> substring
         check `ENTRY_REL in r[10]` decides; if it passes, route as looseness.
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

OLD = "knowledge/2026-10-29-rea-evidence-ledger-discipline.md"


def failing_legs(stdout):
    return [ln.split("=", 1)[0] for ln in stdout.splitlines()
            if ln.startswith("C1_") and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]


def main():
    workroot = Path(sys.argv[1]).resolve()
    receipt_out = Path(sys.argv[2]).resolve()
    mode = sys.argv[3] if len(sys.argv) > 3 else "old"
    workroot.mkdir(parents=True, exist_ok=True)
    root, want = C._fixture(workroot)
    old_exists = (root / "corpus" / OLD).is_file()
    entry_exists = (root / "corpus" / C.ENTRY_REL).is_file()
    src_p = root / "corpus/SOURCES.md"
    text = src_p.read_text(encoding="utf-8")
    marker = f"| on-release | {C.ENTRY_REL} |"
    n = text.count(marker)
    assert n == 2, f"expected 2 new-row used-by cells, found {n}"
    if mode == "old":
        text = text.replace(marker, f"| on-release | {OLD} |")
    elif mode == "both":
        text = text.replace(marker, f"| on-release | {OLD} and {C.ENTRY_REL} |")
    else:
        raise SystemExit(f"unknown mode {mode}")
    src_p.write_text(text, encoding="utf-8")

    r = subprocess.run([sys.executable, "-B", str(COUNTER), "--tree", str(root)],
                       cwd=str(LANE), capture_output=True, text=True,
                       env={**os.environ, "HYAKU_SCRATCH": str(workroot)})
    legs = failing_legs(r.stdout)
    if r.returncode == 0:
        verdict = "SURVIVED"
    elif "C1_SOURCES" in legs:
        verdict = "killed"
    else:
        verdict = "killed-other-legs"
    receipt = {
        "attack": f"A3-usedby-redirect-{mode}",
        "shape": ("(c) new-row used-by cell names the superseded entry "
                  + ("ONLY" if mode == "old" else "AND the real entry")
                  + "; superseded path exists in the fixture corpus"),
        "superseded_path_exists": old_exists,
        "real_entry_exists": entry_exists,
        "used_by_cell_replaced": n,
        "rc": r.returncode, "verdict": verdict,
        "expected_leg": "C1_SOURCES" if mode == "old" else None,
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
                      "superseded_path_exists": old_exists}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
