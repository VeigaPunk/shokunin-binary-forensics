#!/usr/bin/env python3
"""Round-91 attack seat MutR91Sm6 — attributed mutants of
corpus/self_assessment_check3.py (C1 calibration).

Detector = the FROZEN battery reports/round-91/sm6_battery_v3.py (21 labelled
cases), imported; each case is built in its own temp dir with battery.build().

Every mutant is one textual transformation of the v3 source, named by the exact
matched text it replaces (recorded verbatim in mutants.json). A pattern that
does not match exactly once is recorded UNAPPLIED, never as a survivor. The
pristine impl is scored first: a nonzero baseline makes every mutant
INCONCLUSIVE (a baseline failure is not a kill).

Supplementary probes S01-S05 are rule-derived scenarios the frozen battery does
not contain (two K lines; STRICT before K; a `partial` map row; a missing
README; a missing SCORECARD). They are attack-seat probes, NOT frozen truth:
they exist only to explain whether a survivor is a false green.

Usage:
    python3 -B mutate_sm6.py --impl <v3.py> --battery <sm6_battery_v3.py> \
        --out <dir> [--real <TREE>]

Always exits 0: this is a measurement, not a gate.
"""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True


def load_from_path(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------- mutants
# id, description, rule element broken, regex (count=1), replacement
MUTANTS = [
    ("M01", "stated-region cell index 2 -> 3 (the evidence-pointer cell)",
     "rule 2: stated region = cell index 2",
     "return cells[2]", "return cells[3]"),
    ("M02", "stated-region cell index 2 -> 1 (the axis-name cell)",
     "rule 2: stated region = cell index 2",
     "return cells[2]", "return cells[1]"),
    ("M03", "table-row threshold: >= 5 cells -> >= 6",
     "rule 2: table row iff at least 5 cells",
     "if len(cells) >= 5:", "if len(cells) >= 6:"),
    ("M04", "strip the K_HELD_BACKED_STRICT truncation",
     "rule 3: truncate the stated region at the first K_HELD_BACKED_STRICT",
     'region = stated_region(last[-1]).split("K_HELD_BACKED_STRICT")[0]',
     "region = stated_region(last[-1])"),
    ("M05", "table rows fall back to the whole line (step 2 skipped)",
     "rule 2: table row => stated region is cell index 2",
     "if len(cells) >= 5:\n            return cells[2]",
     "if len(cells) >= 5:\n            return s"),
    ("M06", "take the FIRST K_HELD_BACKED line, not the last",
     "rule 1: the LAST SCORECARD line containing K_HELD_BACKED",
     "last[-1]", "last[0]"),
    ("M07", "coverage-map denominator excludes `partial` rows",
     "rule 6: D = every `^| C<n> ` map row",
     're.match(r"^\\| C[0-9]+ ", l)]',
     're.match(r"^\\| C[0-9]+ ", l) and "partial" not in l]'),
    ("M08", "read `held` from cell index 4 (the `w` column) instead of the status column",
     "rule 6: N = README rows whose status is held",
     'if re.search(r"\\|\\s*held\\s*\\|\\s*$", l)',
     'if l.split("|")[4].strip() == "held"'),
    ("M09", "a missing corpus/README.md is accepted as 0 rows",
     "rule 6: N/D are read from the README (absence must fail closed)",
     'readme = txt(root / "corpus/README.md")\n    rows = [l for l in readme.splitlines()',
     'readme = txt(root / "corpus/README.md") if (root / "corpus/README.md").is_file() else ""\n    rows = [l for l in readme.splitlines()'),
    ("M10", "numerator check `==` -> `>=`",
     "rule 6: SM6 = 0 iff N equals the held rows",
     "return 0 if got == (held, len(rows)) else 1",
     "return 0 if got[0] >= held and got[1] == len(rows) else 1"),
    ("M11", "denominator off-by-one: len(rows) -> len(rows) + 1",
     "rule 6: D = the number of map rows",
     "return 0 if got == (held, len(rows)) else 1",
     "return 0 if got == (held, len(rows) + 1) else 1"),
    ("M12", "take the LAST N/D group instead of the first after the token",
     "rule 4: the FIRST N/D group immediately following the token",
     "if mm:\n            got = (int(mm.group(3)",
     "if False:\n            got = (int(mm.group(3)"),
    ("M13", "no right-side-of-arrow preference (the left side wins)",
     "rule 4: prefer the right side of -> when the group carries one",
     "got = (int(mm.group(3) or mm.group(1)), int(mm.group(4) or mm.group(2)))",
     "got = (int(mm.group(1)), int(mm.group(2)))"),
    ("M14", "no parenthesised-score skip: the arrow must follow the pair directly",
     "rule 4: skip an optional parenthesised score such as (5.7)",
     "(?:\\s*(?:\\(\\s*[\\d.]+\\s*\\))?\\s*(?:→|->)\\s*(\\d+)\\s*/\\s*(\\d+))?",
     "(?:\\s*(?:→|->)\\s*(\\d+)\\s*/\\s*(\\d+))?"),
    ("M15", "no N/D found in the region -> 0 (pass) instead of 1",
     "rule 5: no group => SM6 = 1",
     "if not nums:\n            return 1", "if not nums:\n            return 0"),
    ("M16", "the K line must also mention K_HELD_BACKED_STRICT",
     "rule 1: any SCORECARD line containing K_HELD_BACKED",
     'if "K_HELD_BACKED" in l]',
     'if "K_HELD_BACKED" in l and "K_HELD_BACKED_STRICT" in l]'),
    ("M17", "`held` counted as a substring anywhere on the map row",
     "rule 6: N = rows whose status is held (status column only)",
     'if re.search(r"\\|\\s*held\\s*\\|\\s*$", l)',
     'if "held" in l'),
]


def apply_mutant(src, old, new):
    """Literal, attributed replacement: `old` must occur exactly once."""
    n = src.count(old)
    if n != 1:
        return None, None, None, f"literal matched {n} times (need exactly 1)"
    out = src.replace(old, new, 1)
    if out == src:
        return None, None, None, "replacement is a no-op"
    return out, old, new, None


def run_battery(bat, mod, cases, d):
    res = {}
    for cid, rows, held, k_line, label in cases:
        root = d / cid
        bat.build(root, rows, held, k_line)
        try:
            got = mod.sm6(root)
        except Exception as e:  # noqa: BLE001
            got = f"EXC:{type(e).__name__}"
        res[cid] = (label, got)
    return res


def killed_by(res):
    return [cid for cid, (lab, got) in res.items() if got != lab]


# ------------------------------------------------------- supplementary probes
def probe_roots(d):
    """Rule-derived scenarios absent from the frozen battery. Expected values are
    read off the frozen rule (claims.md §C1), not off any implementation."""
    out = []

    def mk(name, nrows, held, sc_text, expect, why):
        root = d / name
        (root / "corpus").mkdir(parents=True)
        body = "".join(
            f"| C{i:02d} | s | k | w | {'held' if i <= held else 'frontier'} |\n"
            for i in range(1, nrows + 1))
        (root / "corpus/README.md").write_text(body, encoding="utf-8")
        (root / "SCORECARD.md").write_text(sc_text, encoding="utf-8")
        out.append((name, root, expect, why))

    mk("S01", 15, 8, "K_HELD_BACKED 8/15\nK_HELD_BACKED 9/15\n", 1,
       "rule 1: the LAST K line is the statement")
    mk("S02", 15, 8, "K_HELD_BACKED_STRICT 8/15 · K_HELD_BACKED 9/15\n", 1,
       "rule 3: the region truncates at STRICT, leaving no stated N/D")

    root = d / "S03"
    (root / "corpus").mkdir(parents=True)
    rows = "".join(
        f"| C{i:02d} | s | k | w | {'held' if i <= 8 else ('partial' if i == 9 else 'frontier')} |\n"
        for i in range(1, 16))
    (root / "corpus/README.md").write_text(rows, encoding="utf-8")
    (root / "SCORECARD.md").write_text("K_HELD_BACKED 8/15\n", encoding="utf-8")
    out.append(("S03", root, 0, "rule 6: D counts `partial` rows too"))

    root = d / "S04"
    root.mkdir(parents=True)
    (root / "SCORECARD.md").write_text("K_HELD_BACKED 0/0\n", encoding="utf-8")
    out.append(("S04", root, 1, "rule 6 undefined without a README => fail closed"))

    root = d / "S05"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | w | held |\n" for i in range(1, 16)),
        encoding="utf-8")
    out.append(("S05", root, 1, "rule 1: no K line => 1"))

    # S06: the word `held` sits in a NOTE cell; the status cell is `frontier`.
    root = d / "S06"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | {'held-out probe' if i == 1 else 'w'} | frontier |\n"
                for i in range(1, 16)),
        encoding="utf-8")
    (root / "SCORECARD.md").write_text("K_HELD_BACKED 0/15\n", encoding="utf-8")
    out.append(("S06", root, 0, "rule 6: only the status column counts as held"))

    # S07 (differential only, expect=None): a SCORECARD row with exactly three
    # content cells. The rule's phrase "at least 5 cells" does not pin whether
    # the two empty split parts count, so no truth label is assigned.
    root = d / "S07"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | w | {'held' if i <= 8 else 'frontier'} |\n"
                for i in range(1, 16)),
        encoding="utf-8")
    (root / "SCORECARD.md").write_text("| K_HELD_BACKED 8/15 | note | x |\n", encoding="utf-8")
    out.append(("S07", root, None, "threshold boundary: 3 content cells (differential only)"))

    # S08: the threshold boundary with a decoy, under the held-out probe's own
    # S2 convention ("naive split len >= 5"). A 3-visible-column row IS a table
    # row there, so cells[2] is the stated region and the token in the axis
    # cell must be ignored.
    root = d / "S08"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | w | {'held' if i <= 8 else 'frontier'} |\n"
                for i in range(1, 16)),
        encoding="utf-8")
    (root / "SCORECARD.md").write_text(
        "| coverage — knowledge-map ground K: K_HELD_BACKED 9/15 | 8/15 (5.3) → 8/15 (5.3) | "
        "verdict 8/15 |\n", encoding="utf-8")
    out.append(("S08", root, 0,
                "threshold boundary: 3 visible columns are a table row (naive-split convention)"))

    # S09: same boundary, FALSE-GREEN direction — the stated cell is false and
    # the axis-cell token is true; a whole-line read rescues the false row.
    root = d / "S09"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | w | {'held' if i <= 8 else 'frontier'} |\n"
                for i in range(1, 16)),
        encoding="utf-8")
    (root / "SCORECARD.md").write_text(
        "| coverage — knowledge-map ground K: K_HELD_BACKED 8/15 | 9/15 (6.0) → 9/15 (6.0) | "
        "verdict 9/15 |\n", encoding="utf-8")
    out.append(("S09", root, 1, "threshold boundary: a false stated cell must be flagged"))

    # S10: FALSE-GREEN direction for a `held` mention outside the status column.
    root = d / "S10"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | {'held-out probe' if i == 1 else 'w'} | frontier |\n"
                for i in range(1, 16)),
        encoding="utf-8")
    (root / "SCORECARD.md").write_text("K_HELD_BACKED 1/15\n", encoding="utf-8")
    out.append(("S10", root, 1, "rule 6: a note-cell `held` must not count (false statement)"))

    # S11: FALSE-GREEN direction for excluding `partial` rows from D.
    root = d / "S11"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus/README.md").write_text(
        "".join(f"| C{i:02d} | s | k | w | {'held' if i <= 8 else ('partial' if i == 9 else 'frontier')} |\n"
                for i in range(1, 16)),
        encoding="utf-8")
    (root / "SCORECARD.md").write_text("K_HELD_BACKED 8/14\n", encoding="utf-8")
    out.append(("S11", root, 1, "rule 6: D counts the `partial` row, so 8/14 is false"))
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--impl", required=True)
    ap.add_argument("--battery", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--real")
    ap.add_argument("--heldout", help="reviewer held-out probe (optional detector)")
    args = ap.parse_args(argv)

    impl_path = Path(args.impl).resolve()
    src = impl_path.read_text(encoding="utf-8")
    bat = load_from_path(Path(args.battery).resolve(), "frozen_battery")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "mutants").mkdir(exist_ok=True)
    real = Path(args.real).resolve() if args.real else None
    heldout = Path(args.heldout).resolve() if args.heldout else None

    def run_heldout(path):
        import subprocess
        st = subprocess.run([sys.executable, "-B", str(heldout), "--impl", str(path)],
                            capture_output=True, text=True)
        out = st.stdout + st.stderr
        mis = re.findall(r"^CASE (H\d+) label=\S+ got=\S+ MISCLASS", out, re.M)
        summ = re.search(r"HELDOUT_MISCLASS=(\d+)/(\d+)", out)
        return {"exit": st.returncode,
                "summary": summ.group(0) if summ else "none",
                "misclass": mis}

    rows = []
    with tempfile.TemporaryDirectory(prefix="mut-sm6-") as td:
        td = Path(td)
        base_file = td / "m_base.py"
        base_file.write_text(src, encoding="utf-8")
        base_mod = load_from_path(base_file, "m_base")
        bdir = td / "base"
        bdir.mkdir()
        base = run_battery(bat, base_mod, bat.CASES, bdir)
        base_bad = killed_by(base)
        base_heldout = run_heldout(impl_path) if heldout else None
        base_real = None
        if real:
            try:
                base_real = base_mod.sm6(real)
            except Exception as e:  # noqa: BLE001
                base_real = f"EXC:{type(e).__name__}"
        probes = probe_roots(td)
        base_probe = {}
        for n, root, exp, _ in probes:
            try:
                base_probe[n] = base_mod.sm6(root)
            except Exception as e:  # noqa: BLE001
                base_probe[n] = f"EXC:{type(e).__name__}"

        for mid, desc, rule, old_txt, new_txt in MUTANTS:
            msrc, old, new, err = apply_mutant(src, old_txt, new_txt)
            row = {"id": mid, "desc": desc, "rule": rule, "replaced": old,
                   "replacement": new, "killing_cases": [], "real": None,
                   "probe_fail": []}
            if msrc is None:
                row.update(status="UNAPPLIED", reason=err)
                rows.append(row)
                continue
            mp = out / "mutants" / f"{mid}.py"
            mp.write_text(msrc, encoding="utf-8")
            try:
                mod = load_from_path(mp, f"m_{mid}")
            except Exception as e:  # noqa: BLE001
                row.update(status="UNAPPLIED", reason=f"import error: {e}")
                rows.append(row)
                continue
            mdir = td / mid
            mdir.mkdir()
            res = run_battery(bat, mod, bat.CASES, mdir)
            kb = killed_by(res)
            if base_bad:
                row.update(status="INCONCLUSIVE", reason=f"baseline mismatch {base_bad}",
                           killing_cases=kb)
            else:
                row.update(status="killed" if kb else "SURVIVED", killing_cases=kb)
            row["heldout"] = run_heldout(mp) if heldout else None
            if real:
                try:
                    row["real"] = mod.sm6(real)
                except Exception as e:  # noqa: BLE001
                    row["real"] = f"EXC:{type(e).__name__}"
            row["probe_all"] = {}
            for n, root, exp, why in probes:
                try:
                    got = mod.sm6(root)
                except Exception as e:  # noqa: BLE001
                    got = f"EXC:{type(e).__name__}"
                row["probe_all"][n] = got
                if exp is not None and got != exp and got != base_probe[n]:
                    row["probe_fail"].append(
                        {"probe": n, "expect": exp, "got": got,
                         "baseline": base_probe[n], "why": why})
            rows.append(row)

    survivors = [r["id"] for r in rows if r["status"] == "SURVIVED"]
    payload = {
        "impl": str(impl_path),
        "impl_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "battery": str(Path(args.battery).resolve()),
        "cases": [c[0] for c in bat.CASES],
        "baseline_mismatch": base_bad,
        "baseline_real": base_real,
        "heldout": str(heldout) if heldout else None,
        "baseline_heldout": base_heldout,
        "baseline_probes": base_probe,
        "mutants": rows,
        "survivors": survivors,
        "SURVIVORS": len(survivors),
    }
    (out / "mutants.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"IMPL {impl_path}")
    print(f"IMPL_SHA256={payload['impl_sha256']}")
    print(f"BASELINE_MISMATCH={len(base_bad)} {base_bad}  REAL={base_real}")
    print(f"BASELINE_PROBES={base_probe}")
    if heldout:
        print(f"BASELINE_HELDOUT={base_heldout}")
    print(f"{'ID':<4} {'STATUS':<13} {'KILLED_BY':<34} {'SUP_FAILS':<12} {'HELDOUT':<12} DESC")
    for r in rows:
        print(f"{r['id']:<4} {r['status']:<13} "
              f"{(','.join(r['killing_cases']) or '-'):<34} "
              f"{(','.join(p['probe'] for p in r['probe_fail']) or '-'):<12} "
              f"HOUT={(','.join((r.get('heldout') or {}).get('misclass', [])) or '-'):<12} {r['desc']}")
    print(f"SURVIVORS={len(survivors)} {survivors}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
