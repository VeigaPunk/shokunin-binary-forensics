# MutR91Sm6 — mutation test of `corpus/self_assessment_check3.py` (round-91 C1)

Seat: mutation-tester (attack, calibration). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Read-only over the lane; every artefact below is written inside
`.ufo/waves/round-91/w1/MutR91Sm6/`.

## What was measured

- **Impl under test:** `corpus/self_assessment_check3.py`, sha256
  `7f2b8e836cbd7fcb47de2d36343c339d7dbdb1787ae924fe5a15287914630791` (unchanged across every run in this seat; not edited by me).
- **Frozen detector:** `reports/round-91/sm6_battery_v3.py`, 21 labelled cases,
  imported and each case built in its own temp dir with `battery.build()`.
  Pristine baseline: `SM6_MISCLASS=0/21`, real-tree `sm6(.) = 0` — a
  green baseline, so a mismatch under a mutant is attributable to the mutant.
- **Second detector (when present):** the reviewer's held-out probe
  `.ufo/waves/round-91/w1/ReviewerR91C1/heldout_sm6_probe.py`, baseline
  `HELDOUT_MISCLASS=0/22`, exit 0.
- **Supplementary probes S01–S11** (attack-seat, hand-derived from
  `claims.md` §C1, **not** frozen truth): only used to say whether a survivor is
  a real divergence from the frozen rule. Baseline values
  `{'S01': 1, 'S02': 1, 'S03': 0, 'S04': 'EXC:FileNotFoundError', 'S05': 'EXC:FileNotFoundError', 'S06': 0, 'S07': 1, 'S08': 0, 'S09': 1, 'S10': 1, 'S11': 1}`.
- **Mutants:** 17 literal, attributed single-hunk textual
  transformations of the v3 source; each row names the exact replaced text. No
  pattern failed to apply (`UNAPPLIED=0`), none was inconclusive.
- **Reproduction:** two independent runs produced byte-identical `mutants.json`
  (sha256 `60a583853e243ad7da912a60f2da73d1f53732a9112a03761567df0855f12679`).

## Table — 11 killed / 6 survived

| id | transformation | rule element broken | battery | killing case ids | held-out (22) | held-out ids |
|---|---|---|---|---|---|---|
| M01 | stated-region cell index 2 -> 3 (the evidence-pointer cell) | rule 2: stated region = cell index 2 | **KILLED** | R02, R03, R04, R05, R06, R07, R08 | killed (12/22) | H01, H03, H05, H06, H08, H10, H12, H14, H15, H18, H20, H21 |
| M02 | stated-region cell index 2 -> 1 (the axis-name cell) | rule 2: stated region = cell index 2 | **KILLED** | R01, R02, R04, R07, R09 | killed (12/22) | H01, H03, H05, H06, H07, H08, H10, H12, H14, H15, H18, H21 |
| M03 | table-row threshold: >= 5 cells -> >= 6 | rule 2: table row iff at least 5 cells | **SURVIVED** | — | survived (0/22) | — |
| M04 | strip the K_HELD_BACKED_STRICT truncation | rule 3: truncate the stated region at the first K_HELD_BACKED_STRICT | **SURVIVED** | — | survived (0/22) | — |
| M05 | table rows fall back to the whole line (step 2 skipped) | rule 2: table row => stated region is cell index 2 | **KILLED** | R06 | killed (2/22) | H05, H20 |
| M06 | take the FIRST K_HELD_BACKED line, not the last | rule 1: the LAST SCORECARD line containing K_HELD_BACKED | **SURVIVED** | — | killed (3/22) | H12, H17, H18 |
| M07 | coverage-map denominator excludes `partial` rows | rule 6: D = every `^| C<n> ` map row | **SURVIVED** | — | killed (1/22) | H10 |
| M08 | read `held` from cell index 4 (the `w` column) instead of the status column | rule 6: N = README rows whose status is held | **KILLED** | B01, B04, B06, B08, B10, B11, R01, R02, R04, R07, R09 | killed (13/22) | H01, H03, H05, H06, H08, H10, H12, H14, H15, H16, H18, H21, H22 |
| M09 | a missing corpus/README.md is accepted as 0 rows | rule 6: N/D are read from the README (absence must fail closed) | **SURVIVED** | — | survived (0/22) | — |
| M10 | numerator check `==` -> `>=` | rule 6: SM6 = 0 iff N equals the held rows | **KILLED** | B03, B12, R03, R08 | killed (5/22) | H04, H07, H09, H11, H17 |
| M11 | denominator off-by-one: len(rows) -> len(rows) + 1 | rule 6: D = the number of map rows | **KILLED** | B01, B04, B06, B07, B08, B10, B11, R01, R02, R04, R07, R09 | killed (13/22) | H01, H03, H05, H06, H08, H10, H12, H14, H15, H16, H18, H21, H22 |
| M12 | take the LAST N/D group instead of the first after the token | rule 4: the FIRST N/D group immediately following the token | **KILLED** | R02 | killed (4/22) | H01, H02, H13, H19 |
| M13 | no right-side-of-arrow preference (the left side wins) | rule 4: prefer the right side of -> when the group carries one | **KILLED** | B04, B05, B07, B08, R02, R03, R05, R07, R09 | killed (8/22) | H01, H06, H10, H11, H14, H17, H18, H22 |
| M14 | no parenthesised-score skip: the arrow must follow the pair directly | rule 4: skip an optional parenthesised score such as (5.7) | **KILLED** | B07, B08, R02, R03, R05, R07, R09 | killed (8/22) | H01, H06, H10, H11, H14, H17, H18, H22 |
| M15 | no N/D found in the region -> 0 (pass) instead of 1 | rule 5: no group => SM6 = 1 | **KILLED** | R06 | killed (1/22) | H20 |
| M16 | the K line must also mention K_HELD_BACKED_STRICT | rule 1: any SCORECARD line containing K_HELD_BACKED | **KILLED** | B01, B04, B06, B08, B10, R01, R02, R04, R07, R09 | killed (12/22) | H01, H03, H05, H06, H10, H12, H14, H15, H16, H18, H21, H22 |
| M17 | `held` counted as a substring anywhere on the map row | rule 6: N = rows whose status is held (status column only) | **SURVIVED** | — | survived (0/22) | — |

**SURVIVORS=6** — M03, M04, M06, M07, M09, M17.

Exact replaced text for every row, the probe definitions and the reproduce
command are in `table.md`; the generator is `mutate_sm6.py`; the mutants are
`mutants/M01.py … M17.py`; the raw detector output is `mutation-run.log`.

## Survivors — the rule element each breaks, and whether it is a false green the battery cannot see

| id | rule element broken | does the frozen battery see it? | does the reviewer held-out probe see it? | demonstrated divergence |
|---|---|---|---|---|
| **M03** | rule 2 boundary: "table row with at least 5 cells" (`>= 5` → `>= 6`) | **no** — every battery row splits into ≥ 7 parts, so the boundary is never exercised | **no** — H15 is a 3-visible-column row but its whole-line read coincides with the cell read | **yes**: S08 (true stated cell → mutant flags it, false red) and S09 (false stated cell → mutant passes it, **false green**) |
| **M04** | rule 3: truncate the stated region at the first `K_HELD_BACKED_STRICT` | **no** — B11 is the only STRICT case and places STRICT *after* the K group, so the cut is inert | **no** — H08/H09 likewise put STRICT after the K group | **yes**: S02 (`K_HELD_BACKED_STRICT 8/15 · K_HELD_BACKED 9/15`) — rule ⇒ 1, mutant ⇒ 0, **false green** |
| **M06** | rule 1: the **last** SCORECARD line containing `K_HELD_BACKED` | **no** — every battery case has exactly one K line | **yes** — H12, H17, H18 | S01 — last line false, first true: mutant passes it, **false green** |
| **M07** | rule 6: D = **every** `^| C<n> ` map row (mutant drops `partial`) | **no** — battery map rows are only `held`/`frontier` | **yes** — H10 | S03 (false red) and S11 (false green: stated 8/14 passes) |
| **M09** | rule 6: N/D come from the README; absence must fail closed (mutant treats a missing README as 0 rows) | **no** — `battery.build` always writes a README | **no** — the probe always writes a README | **yes**: S04 (no README, statement `0/0`) — rule ⇒ 1, mutant ⇒ 0, **false green**; v3 itself raises `FileNotFoundError` there |
| **M17** | rule 6: only the **status** column decides `held` (mutant accepts the substring anywhere on the row) | **no** — no battery row mentions `held` outside the status cell | **no** — no held-out row does either | **yes**: S06 (false red) and S10 (false green: statement `1/15` with zero held rows passes) |

So: **four of six survivors (M03, M04, M09, M17) are false greens that neither
the frozen battery nor the reviewer's held-out probe can see**; the other two
(M06, M07) are false greens of the battery that the held-out probe does catch.
No survivor contradicts the frozen predicate as written — they are coverage
findings about the detectors, not permission to change the contract.

## Killed mutants (for the record)

- **M01** — stated-region cell index 2 -> 3 (the evidence-pointer cell) — killed by R02, R03, R04, R05, R06, R07, R08
- **M02** — stated-region cell index 2 -> 1 (the axis-name cell) — killed by R01, R02, R04, R07, R09
- **M05** — table rows fall back to the whole line (step 2 skipped) — killed by R06
- **M08** — read `held` from cell index 4 (the `w` column) instead of the status column — killed by B01, B04, B06, B08, B10, B11, R01, R02, R04, R07, R09
- **M10** — numerator check `==` -> `>=` — killed by B03, B12, R03, R08
- **M11** — denominator off-by-one: len(rows) -> len(rows) + 1 — killed by B01, B04, B06, B07, B08, B10, B11, R01, R02, R04, R07, R09
- **M12** — take the LAST N/D group instead of the first after the token — killed by R02
- **M13** — no right-side-of-arrow preference (the left side wins) — killed by B04, B05, B07, B08, R02, R03, R05, R07, R09
- **M14** — no parenthesised-score skip: the arrow must follow the pair directly — killed by B07, B08, R02, R03, R05, R07, R09
- **M15** — no N/D found in the region -> 0 (pass) instead of 1 — killed by R06
- **M16** — the K line must also mention K_HELD_BACKED_STRICT — killed by B01, B04, B06, B08, B10, R01, R02, R04, R07, R09

The eleven kills include every rule element the battery was designed to pin:
the stated cell vs the pointer cell (M01, M05), the axis cell (M02), the
first-after-token vs last-group read (M12), the arrow right-side preference
(M13), the parenthesised-score skip (M14), `==` vs `>=` on N (M10), the
denominator (M11), the held-column read (M08), and rule 5's fail-closed
no-group case (M15). Single-case kills are real but thin: M05 and M15 rest on
R06 alone, M12 on R02 alone.

## Observations, disclosed

- **v3 raises on absent inputs.** With no `corpus/README.md` (S04) or no
  `SCORECARD.md` (S05) `sm6` raises `FileNotFoundError` instead of returning 1.
  That is fail-closed in effect (the counter's `--self-test`/real legs would see
  a nonzero exit), but it is an exception, not a scored mismatch. The battery
  cannot see it either way; recorded here as an observation, not a claim.
- **Threshold convention is under-specified in the frozen rule.** "at least 5
  cells" is implemented as `len(s.split("|")) >= 5` (so 3 visible columns count
  as a table row). The battery never pins this; the held-out probe adopts the
  same convention in its H15 label. S08/S09 use that convention to expose M03.
- **Baseline context (one read-only run, not my deliverable):** the frozen
  counter `reports/round-91/c1_counter.py --impl corpus/self_assessment_check3.py
  --real . --lane .` reported `SM6_MISCLASS=0/22`, `MUTANTS_KILLED=11/11`,
  `IMPL_SELFTEST exit=0`, `REAL_SELF_MISMATCH=0`, `C1_VERDICT=pass` at my run
  time. The executor's earlier `counter.log` shows `REAL_SELF_MISMATCH=1` /
  `C1_VERDICT=fail`; I did not investigate that discrepancy (not my seat) and I
  do not claim anything about it beyond recording both observations.

## Hygiene

- No mutating git/jj command was run in the lane; no fixture repo was created
  (the battery's own `build()` writes plain files under `tempfile` dirs).
- Frozen files (`claims.md`, `sm6_battery_v3.py`, `mutants.py`, `c1_counter.py`,
  `cap_probe.py`) were read only; `corpus/self_assessment_check3.py` was not
  edited (sha256 unchanged).
- Tooling: nothing installed or upgraded.
- Scratch `$HYAKU_SCRATCH/revenger-r91/MutR91Sm6/` removed before yield.
