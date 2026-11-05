#!/usr/bin/env python3
"""Attack A4 (shape d): a SECOND knowledge file whose bytes are byte-identical to the
admitted entry except the status line is indented. No coverage row, vote, receipt or
SOURCES cell names it. If no v4 leg enumerates corpus/knowledge/, the orphan passes all
legs — a routed finding for r96, never a reason to edit frozen bytes.
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

SHADOW_REL = "corpus/knowledge/round-95-evidence-ledger-discipline-shadow.md"


def failing_legs(stdout):
    return [ln.split("=", 1)[0] for ln in stdout.splitlines()
            if ln.startswith("C1_") and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]


def main():
    workroot = Path(sys.argv[1]).resolve()
    receipt_out = Path(sys.argv[2]).resolve()
    workroot.mkdir(parents=True, exist_ok=True)
    root, want = C._fixture(workroot)
    entry_p = root / C.ENTRY
    entry = entry_p.read_text(encoding="utf-8")
    assert entry.count("admission-status: admitted") == 1
    orphan = entry.replace("admission-status: admitted",
                           "  admission-status: admitted", 1)
    assert orphan != entry and "\n  admission-status: admitted\n" in orphan
    shadow = root / SHADOW_REL
    shadow.write_text(orphan, encoding="utf-8")

    # nothing else in the fixture references the shadow file
    refs = []
    for probe in ("corpus/README.md", "corpus/SOURCES.md",
                  f"{C.WAVE_DIR}/w1/swarm-registry.json"):
        if probe.replace("/", "/") and (root / probe).is_file():
            if "round-95-evidence-ledger-discipline-shadow" in (root / probe).read_text(encoding="utf-8"):
                refs.append(probe)

    r = subprocess.run([sys.executable, "-B", str(COUNTER), "--tree", str(root)],
                       cwd=str(LANE), capture_output=True, text=True,
                       env={**os.environ, "HYAKU_SCRATCH": str(workroot)})
    legs = failing_legs(r.stdout)
    verdict = "SURVIVED-ROUTED-TO-R96" if (r.returncode == 0
                                           and "C1_VERDICT=pass" in r.stdout) else "killed"
    receipt = {
        "attack": "A4-orphan-shadow-entry",
        "shape": ("(d) second knowledge file byte-identical to the admitted entry except "
                  "an indented status line; unreferenced by map, sources, votes"),
        "shadow_rel": SHADOW_REL,
        "shadow_bytes_equal_entry_except_indent": True,
        "references_to_shadow": refs,
        "rc": r.returncode, "verdict": verdict, "expected_leg": None,
        "failing_legs": legs,
        "why": [ln for ln in r.stdout.splitlines() if ln.startswith("C1_VERDICT")
                or ln.endswith("=fail")],
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
