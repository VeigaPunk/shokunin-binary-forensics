#!/usr/bin/env python3
r"""Held-out SM6 probe for round-91 C1 — seat ReviewerR91C1 (attack: calibration).

22 fresh real-format cases (H01–H22) in the lane's own SCORECARD row shape
(`| axis | before → after | counter | commits | verdict |`), NONE of them in
the frozen battery `reports/round-91/sm6_battery_v3.py` (B01–B12 are bare
lines; R01–R09 are single-row cases without these mechanisms). Labels are
hand-derived from the frozen rule in `reports/round-91/claims.md` §C1, with
the rule steps named per case:

  S1  take the LAST SCORECARD line containing `K_HELD_BACKED`
  S2  if that line is a `|`-delimited row with >= 5 cells (naive split),
      stated region = cell index 2; otherwise the whole line (S2b)
  S3  truncate the stated region at the first `K_HELD_BACKED_STRICT`
  S4a if the region contains `K_HELD_BACKED`: first `N/D` group immediately
      following the (first) token occurrence — skipping non-digits, an
      optional parenthesised score, taking the right side of `→`/`->`
      (one arrow step only)
  S4b otherwise (when S4a yields no group): the LAST `N/D` group in the
      region under the same right-side preference
  S5  if neither yields a group: SM6 = 1 (row does not state the quantity)
  S6  SM6 = 0 iff N = README rows whose status is `held` and D = README
      coverage-map rows (`^| C<n> `)

The rule-step chain for each label is printed by `--derive` and embedded per
case below. Two cases are flagged AMBIGUOUS (the rule does not decide them;
the label follows the literal reading and the divergence is disclosed):
  H19 en-dash `–>` arrow — rule names only `→`/`->`
  H20 escaped `\|` inside the axis cell — naive split vs markdown cell

Mandated shapes covered: two arrows (H01, H02); token after the numbers
(H03, H04); axis label carrying an `N/D` (H05, H06, H07); `K_HELD_BACKED_
STRICT` mention (H08, H09) and escaped pipe (H20, H21); map with a `partial`
status row (H10, H11); N/D in code-fence context in/around the stated cell
(H12 file-level fence; H13 inline code span inside the stated cell — a
multi-line fence cannot live inside a single table row, disclosed); and two
genuinely ambiguous cases (H19, H20).

Erratum (label provenance): the first derivation pass carried three seat
errors — H10/H11 built 8 held rows where the labels assumed 7, and H15
misread the frozen `cell index 2` as the third visible column (index 2 of a
naive `split("|")` is the second visible column). The frozen reference
(`reports/round-91/mutants.py::reference`) caught all three BEFORE any
implementation result was accepted; the corrections follow the frozen rule's
own split semantics, and the corrected label set scores 0/22 against the
reference. The implementation was never the arbiter of a label.

Usage:
    python3 -B heldout_sm6_probe.py --impl <checker.py> [--fn sm6] [--derive]

Prints `CASE <id> label=<l> got=<g> ok|MISCLASS` per case (ambiguous cases
carry `label=<l>AMBIG`), then `HELDOUT_MISCLASS=<n>/<M>`. Exit 0 iff n == 0,
1 otherwise, 64 on usage. Read-only over the lane; writes only inside its own
temp dirs.
"""
import importlib.util
import sys
import tempfile
from pathlib import Path

# (id, statuses for map rows (len = D; "*" suffix = two trailing spaces on
#  that row), SCORECARD lines, hand label, rule-step chain, ambiguity note)
CASES = [
    ("H01", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 4/14 (2.9) → 8/15 (5.3) → 9/16 (5.6); "
      "C04 held → C16 proposed | probe `K_HELD_BACKED` | `aaaaaaa` → `bbbbbbb` | improved |"],
     0,
     "S1; S2 row→cells[2]; S4a first token-adjacent group takes ONE arrow step → (8,15); "
     "S6 8==held 15==rows",
     None),
    ("H02", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 6/14 (4.3) → 7/14 (5.0) → 8/15 (5.3); "
      "C04 held | probe `K_HELD_BACKED` | `aaaaaaa` → `bbbbbbb` | improved |"],
     1,
     "S1; S2; S4a single arrow step from the token → (7,14) ≠ (8,15); S6 mismatch "
     "(the trailing 8/15 is past the one judged arrow step)",
     None),
    ("H03", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | 8/14 (5.7) → 8/15 (5.3) at round close; "
      "`K_HELD_BACKED` restated below | probe `K_HELD_BACKED` | `aaaaaaa` → `bbbbbbb` | unchanged |"],
     0,
     "S1; S2; S4a fails (token carries no following digits in the region); S4b last N/D = (8,15); "
     "S6 8==held 15==rows",
     None),
    ("H04", ["held"] * 9 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | 9/16 (5.6) → 10/16 (6.2) at round close; "
      "`K_HELD_BACKED` restated below | probe `K_HELD_BACKED` | `aaaaaaa` → `bbbbbbb` | improved |"],
     1,
     "S1; S2; S4a fails; S4b last N/D = (10,16) ≠ (held 9, rows 16); S6 mismatch",
     None),
    ("H05", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K (`K_HELD_BACKED` 4/14 (2.9) → 8/14 (5.7) at r90) | "
      "8/15 (5.3) → 8/15 (5.3); `K_HELD_BACKED` unchanged at the round close | probe | same | "
      "unchanged |"],
     0,
     "S1; S2 (the axis cell's token+4/14→8/14 decoy is OUTSIDE cells[2]); S4a fails (stated-cell "
     "token has no digits after it); S4b last N/D in stated cell = (8,15); S6 8==held 15==rows",
     None),
    ("H06", ["held"] * 8 + ["frontier"] * 6,
     ["| coverage — knowledge-map ground K (map grew 4/13 → 5/14 this round) | "
      "`K_HELD_BACKED` 7/14 (5.0) → 8/14 (5.7); C05 uncovered | probe | `aaaaaaa` → `bbbbbbb` | "
      "improved |"],
     0,
     "S1; S2 (axis N/D decoy 4/13→5/14 is outside cells[2] and carries no token); "
     "S4a → (8,14); S6 8==held 14==rows",
     None),
    ("H07", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K (map grew 8/14 → 8/15 this round) | "
      "`K_HELD_BACKED` 8/14 (5.7) → 9/15 (6.0); C05 uncovered | probe | `aaaaaaa` → `bbbbbbb` | "
      "improved |"],
     1,
     "S1; S2; S4a → (9,15) ≠ (8,15); S6 mismatch (the axis decoy must not rescue anything)",
     None),
    ("H08", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3) · "
      "`K_HELD_BACKED_STRICT` 7/15 (4.7) | probe both | same | unchanged |"],
     0,
     "S1; S2; S3 truncate at K_HELD_BACKED_STRICT (7/15 discarded); S4a → (8,15); "
     "S6 8==held 15==rows",
     None),
    ("H09", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 9/15 (6.0) → 9/15 (6.0) · "
      "`K_HELD_BACKED_STRICT` 8/15 (5.3) | probe both | same | improved |"],
     1,
     "S1; S2; S3 truncate (the agreeing STRICT 8/15 must be discarded); S4a → (9,15) ≠ (8,15); "
     "S6 mismatch",
     None),
    ("H10", ["held"] * 6 + ["held*"] + ["partial"] + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 6/14 (4.3) → 7/15 (4.7); C10 partial | "
      "probe | `aaaaaaa` → `bbbbbbb` | improved |"],
     0,
     "S1; S2; S4a → (7,15); S6 held=7 (6 plain + 1 trailing-space held row, which still counts) "
     "and rows=15 (the `partial` row counts in D only)",
     None),
    ("H11", ["held"] * 6 + ["held*"] + ["partial"] + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 7/15 (4.7) → 8/15 (5.3); "
      "C10 partial now held | probe | `aaaaaaa` → `bbbbbbb` | improved |"],
     1,
     "S1; S2; S4a → (8,15) ≠ (held 7, rows 15); S6 mismatch (a `partial` row is not held)",
     None),
    ("H12", ["held"] * 8 + ["frontier"] * 7,
     ["## Round 91", "", "```", "K_HELD_BACKED 4/14 (2.9) → 9/15 (6.0)", "```", "",
      "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3); C05 uncovered | "
      "probe | same | unchanged |"],
     0,
     "S1 the fenced line above the row also names the token but the ROW is the LAST K line; "
     "S2; S4a → (8,15); S6 8==held 15==rows",
     None),
    ("H13", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | r91 probe: `K_HELD_BACKED=9/16` then real "
      "`K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3) | probe | same | unchanged |"],
     1,
     "S1; S2; S4a the FIRST token occurrence (inside the inline code span in the stated cell) → "
     "(9,16) ≠ (8,15); S6 mismatch",
     None),
    ("H14", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3) | "
      "pointer `K_HELD_BACKED=9/15` | unchanged |"],
     0,
     "S1; S2 four visible columns → naive split len 6 ≥ 5, cells[2] = 2nd visible column = the "
     "stated cell; S4a → (8,15); S6 8==held 15==rows (the pointer decoy in the 4th column is "
     "outside the region)",
     None),
    ("H15", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3) | verdict 9/15 |"],
     0,
     "S1; S2 three visible columns → naive split len 5 ≥ 5, cells[2] = 2nd visible column = the "
     "stated cell; S4a → (8,15); S6 8==held 15==rows (the 3rd-column verdict decoy 9/15 is "
     "outside the region)",
     None),
    ("H16", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | preamble only | probe `K_HELD_BACKED` 8/15 (5.3) → "
      "8/15 (5.3) | same"],
     0,
     "S1; S2b row does not end with `|` → whole line is the region; S4a → (8,15); "
     "S6 8==held 15==rows",
     None),
    ("H17", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3) | probe | "
      "same | unchanged |",
      "| coverage — knowledge-map ground K (recount) | `K_HELD_BACKED` 8/15 (5.3) → 9/15 (6.0) | "
      "probe | same | improved |"],
     1,
     "S1 the LAST K row (recount) is judged, not the first; S2; S4a → (9,15) ≠ (8,15); S6 mismatch",
     None),
    ("H18", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 9/15 (6.0) | probe | "
      "same | improved |",
      "| coverage — knowledge-map ground K (erratum) | `K_HELD_BACKED` 9/15 (6.0) → 8/15 (5.3) | "
      "probe | same | corrected |"],
     0,
     "S1 the LAST K row (erratum) is judged; S2; S4a → (8,15); S6 8==held 15==rows",
     None),
    ("H19", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/14 (5.7) –> 8/15 (5.3); "
      "C05 uncovered | probe | `aaaaaaa` → `bbbbbbb` | improved |"],
     1,
     "S1; S2; S4a the arrow class is `→`/`->` only; `–>` (en dash) is not an arrow → group is "
     "(8,14) ≠ (8,15); S6 mismatch under the literal reading",
     "AMBIGUOUS: a human reads `–>` as an arrow (current side 8/15 → label 0); the rule names "
     "only `→`/`->`. Label follows the literal rule."),
    ("H20", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K \\| K map | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3) | "
      "probe | same | unchanged |"],
     1,
     "S1; S2 naive split on `|` — the escaped `\\|` in the axis cell splits into an extra cell, so "
     "cells[2] = ' K map ' (no token, no N/D); S5 neither read yields a group → 1",
     "AMBIGUOUS: a markdown-aware reader sees cells[2] as the true stated cell (label 0); the "
     "rule's `cell index 2` is undecided on escapes. Label follows the literal naive split."),
    ("H21", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3) | probe | "
      "same | unchanged \\| held |"],
     0,
     "S1; S2 the escaped pipe sits AFTER cell 2, so cells[2] stays the stated cell; "
     "S4a → (8,15); S6 8==held 15==rows",
     None),
    ("H22", ["held"] * 8 + ["frontier"] * 7,
     ["| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3) |"],
     0,
     "S1; S2b two visible columns → naive split len 4 < 5 → whole line is the region; "
     "S4a → (8,15); S6 8==held 15==rows",
     None),
]


def load(path, name="heldout_impl"):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build(root, statuses, sc_lines):
    (root / "corpus").mkdir(parents=True)
    body = ""
    for i, st in enumerate(statuses, 1):
        trail = ""
        if st.endswith("*"):
            st = st[:-1]
            trail = "  "
        body += f"| C{i:02d} | s | k | w | {st} |{trail}\n"
    (root / "corpus/README.md").write_text(body, encoding="utf-8")
    (root / "SCORECARD.md").write_text("## Round 91\n" + "\n".join(sc_lines) + "\n",
                                       encoding="utf-8")


def main(argv):
    impl = fn = None
    derive = False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--impl":
            impl = Path(argv[i + 1]); i += 2
        elif a == "--fn":
            fn = argv[i + 1]; i += 2
        elif a == "--derive":
            derive = True; i += 1
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: {a}", file=sys.stderr); return 64
    if impl is None:
        print(__doc__, file=sys.stderr)
        return 64
    fn = fn or "sm6"
    mod = load(impl)
    score = getattr(mod, fn)
    bad = 0
    amb_div = 0
    total = 0
    with tempfile.TemporaryDirectory(prefix="rev-r91-heldout-") as d:
        d = Path(d)
        for cid, statuses, sc_lines, label, steps, amb in CASES:
            root = d / cid
            build(root, statuses, sc_lines)
            got = score(root)
            total += 1
            ok = (got == 0 and label == 0) or (got == 1 and label == 1)
            if not ok:
                bad += 1
                if amb:
                    amb_div += 1
            tag = f" label={label}{'AMBIG' if amb else ''}"
            verdict = "ok" if ok else "MISCLASS"
            extra = "" if (ok or not amb) else " DIVERGES-AMBIGUOUS(rule-interpretation)"
            print(f"CASE {cid}{tag} got={got} {verdict}{extra}")
            if derive:
                print(f"DERIVE {cid} {steps}")
                if amb:
                    print(f"AMBIGUITY {cid} {amb}")
    print(f"HELDOUT_MISCLASS={bad}/{total}")
    print(f"AMBIGUOUS_DIVERGENCE={amb_div}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
