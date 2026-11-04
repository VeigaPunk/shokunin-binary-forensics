# MutR90SM6 — mutation test of the C1 instrument (SM6 v2), round 90 w1

Seat MutR90SM6 (mutation-tester, leaf). Frozen at `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`; claims read from
`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md`.

## Setup

- Subject: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/self_assessment_check2.py`, sha256
  `0e73a90b2de99a1a8de40b59dfd75c48ce4a6bbb3243d4d93be78e31028d0227`. It was copied into scratch
  (`/fast/scratch/hyaku/revenger-r90/MutR90SM6/check2.py`, since deleted). The lane file was never written, and its
  sha256 after the run is identical.
- Real tree: `git archive c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9 corpus SHONEN.md SCORECARD.md SKILL.md`,
  extracted into scratch. Its README has 15 `| C<n> ` rows; `grep -c '^| C'` also gives 15.
- Detectors, run with `TMPDIR=` set to scratch:
  - Battery leg: `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/sm6_battery.py --impl <mutant> --real <tree>`
  - Selftest leg: `python3 -B <mutant> --self-test`
  - A mutant is killed if either leg exits non-zero.
- Driver: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/MutR90SM6/drive.py`. Each mutation
  is an exact single-occurrence string replacement, and the driver asserts that `count == 1`.
- Full output: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/MutR90SM6/driver-run.log`.
  Each mutant also has its own `<mutant>.diff`, `<mutant>.battery.log` and `<mutant>.selftest.log`.

## Controls

| leg | sha256 | battery | selftest |
|---|---|---|---|
| pristine | 0e73a90b…0227 | SM6_MISCLASS=0/14 exit 0 | SELFTEST OK exit 0 |
| restored (after all mutants) | 0e73a90b…0227 | SM6_MISCLASS=0/14 exit 0 | SELFTEST OK exit 0 |

Both baselines are green, so every verdict below is conclusive. After each mutant the scratch copy was restored, and
its hash matched the pristine one 11/11 times (`True` in the last column of `driver-run.log`).

## Mutants

| mutant | battery result | selftest result | killed? (leg) |
|---|---|---|---|
| M1 drop denominator check | 4/14 [B02,B05,B07,R2] | FAIL probe "fifteen rows, stale 8/14" | **killed** (battery+selftest) |
| M2 drop numerator check | 2/14 [B03,B12] | FAIL SM6 planted defect | **killed** (battery+selftest) |
| M3 left side instead of right | 4/14 [B04,B05,B07,B08] | FAIL SM6 planted defect | **killed** (battery+selftest) |
| M4 drop parenthesised-score allowance | 2/14 [B07,B08] | FAIL probe "scores between sides" | **killed** (battery+selftest) |
| M5 count all `\| C` rows, not `\| C<n> ` | 0/14 | OK | **SURVIVED** |
| M6a first statement (`stmts[0]`) | 0/14 | OK | **SURVIVED** |
| M6b first K line (`last[0]`) | 1/14 [R1-real-tree] | OK | **killed** (battery only, R1) |
| M7 drop `K_HELD_BACKED_STRICT` split | 1/14 [B11] | FAIL probe "two K statements, the first wrong" | **killed** (battery+selftest) |
| M8a return 0 when no N/D statement | 0/14 | OK | **SURVIVED** |
| M8b return 0 when no K line | 1/14 [B09] | OK | **killed** (battery only, B09) |
| M9 (extra) held = `"held" in l`, unanchored | 0/14 | OK | **SURVIVED** |

Score: **7 of 11 mutants killed; 4 survived.** Of the 8 mutant classes the seat assigned, 5 were killed outright. The
"first statement" class was split in two: M6b (first K line) was killed, M6a (first statement on the line) survived.
M5 and M8a survived.

## Survivors (coverage findings — not contract changes)

None of the survivors is equivalent to the original. For each one,
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/MutR90SM6/survivor-witness.log` records an
input where pristine v2 gets the truth label right and the mutant gets it wrong:

| witness | input | label | pristine | mutant |
|---|---|---|---|---|
| W1 → M5 | README has a `\| Criterion \|` header row above 15 map rows; K line `8/15` | 0 | 0 | 1 |
| W2 → M6a | `K_HELD_BACKED 9/15 · corrected K_HELD_BACKED 8/15` (15 rows, 8 held) | 0 | 0 | 1 |
| W3 → M8a | `K_HELD_BACKED unchanged (see r73)` (no N/D) | 1 | 1 | 0 |
| W4 → M9 | the C09 row has `held-out set` in another column and status `frontier`; K line `9/15` | 1 | 1 | 0 |

The W2 label follows v2's own docstring ("last `N/D` statement on the last … line"). The other three labels follow the
battery predicate directly.

## Leg-specific blind spots

- **Selftest only, no battery:** none.
- **Battery only:** M6b (real-tree R1 only) and M8b (synthetic B09 only).
  - The selftest is blind to "first K line" because every selftest fixture has only one K line.
  - It is blind to "no K line returns 0" because no selftest probe removes the K line.

## Proposals (report only; the frozen battery/instrument stays untouched)

A future battery or selftest revision could kill the four survivors by adding:

1. A README with a non-map `| C…` row, such as a table header.
2. Two `K_HELD_BACKED` ratios on one line, with the last one true.
3. A K line that names `K_HELD_BACKED` but has no ratio (label 1).
4. A non-held row that has `held` in a non-status column.

A selftest probe that drops the K line would also close the gap behind M8b.

## Assessment for C1

The frozen battery plus the selftest catches every mutant on the axes C1 claims to fix: the denominator, the
numerator, the right-side choice, the parenthesised score and the STRICT split. It also catches the R2 forgery under
M1. The surviving mutants are about parsing robustness: the row selector, the held matcher, the choice between
statements on one line, and a K line with no ratio. Over the frozen 14 cases all four survivors behave the same as v2,
so they do not change the C1 counter result. They do show that `SM6_MISCLASS=0/14` under-constrains those four code
paths.

## Tooling

No tools were installed or upgraded. The probe used only the system `python3`, `git archive` and `tar`. The only git
command was the read-only `git archive`.

## Scratch

`/fast/scratch/hyaku/revenger-r90/MutR90SM6` was deleted after the receipts were copied here.
