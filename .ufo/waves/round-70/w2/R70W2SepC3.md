# R70W2SepC3 — C3 (freshness) separability, round 70 wave 2

**SEPARABLE** — a tree carrying only C3's change moves exactly C3's labels to their target values
(`EMB_R68` 17/7 → 17/0, `EMB_PINNED_SCRIPT_IS_S046` no → yes, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED` n/a → 1/1,
`HOLDS_C3_V1` no → yes, `A1_C3` no → yes) and leaves **every** label of C1 and C2 at its base value; no label
of any claim is worse than base. One cross-claim *coverage* coupling exists and is reported below (§4): C2's
`SM2` counts the file C3 introduces, so the final tree only keeps `SM2=0` if C3's own README line lands with it.

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Target bytes: lane commit
`17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`; base: `3f5edbc206351232a3d2d801334dd930499ccaf5`.
Counters used unmodified: `reports/round-70/measure.py` sha256
`488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`, `reports/round-70/measure-a1.py` sha256
`96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191` (both re-hashed in this seat before use).
Scratch trees: `/tmp/revenger-r70-R70W2SepC3/{base,c3,target,...}` (deleted after this report).

## 1. Trees built

```
git -C <lane> archive 3f5edbc… corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C $S/base
git -C <lane> archive 3f5edbc… … | tar -x -C $S/c3        # then overlay ONLY C3's files
git -C <lane> archive 17ee7f87… … | tar -x -C $S/target
```

C3-only overlay (files C3's claim text names, taken byte-exact from the target commit):

| file | sha256 in C3 tree | = target? |
|---|---|---|
| `corpus/check_embedded_outputs.py` | `5f42415bd4124cf916ecfd9b745d030254a29d299afbe8061a89b784e0d9e879` | yes |
| `corpus/embedded_output_pins.json` | `34c400c4721408a1ae485e8d6895ebb93e2744cdeeeefa0954c3c3176c0e4efd` | yes |
| `corpus/derive_axml_anchors_r68.py` | `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` (= S046) | yes |

README: base file plus only the two index lines naming those files (`diff -u base/corpus/README.md
c3/corpus/README.md` shows exactly `+` for the `check_embedded_outputs.py` line and the
`derive_axml_anchors_r68.py` line, nothing else). `c3_strict` repeats it with **only** the
`derive_axml_anchors_r68.py` line, i.e. the literal ownership split in `reports/round-70/claims.md:131-134`
(C3 names `derive_axml_anchors_r68.py`; the `check_embedded_outputs.py` line belongs to C2's "four old files").
Both variants produce identical labels (below), so the split does not change the verdict.

The retained entries are byte-identical to base in every tree:
`round-68-apk-axml-byte-evidence.md` sha256 `ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e`,
`round-65-apk-axml-byte-evidence.md` sha256 `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a`
(both match the counter's pins at `measure.py:20-21`).

## 2. Label table (base / C3-only / target), commands

```
cd / && python3 -B <lane>/reports/round-70/measure.py   $S/<tree>
cd / && python3 -B <lane>/reports/round-70/measure-a1.py $S/<tree>
python3 -B <lane>/corpus/self_assessment_check.py --root $S/<tree> --lane <lane>
```

| label | base | C3-only | target | note |
|---|---|---|---|---|
| `K_HELD_BACKED` | 8/14 score=5.7 | 8/14 score=5.7 | 8/14 score=5.7 | unchanged |
| `K_HELD_BACKED_STRICT` | 8/14 | 8/14 | 8/14 | unchanged |
| `C05_STATUS` | uncovered | uncovered | uncovered | unchanged (C1 not flipped at this commit) |
| `C05_KNOWLEDGE_COLUMN` | - | - | - | unchanged |
| `C05_SINGLE_V5` | no | no | no | unchanged |
| `V5_ENTRY_PRESENT` | no | no | yes | target-only (C1) |
| `C1_GATE` | n/a | n/a | checked_blocks=24 problems=0 exit=0 | target-only (C1) |
| `C1_LINT` | n/a | n/a | LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0 | target-only (C1) |
| `HOLDS_C1_V5` | no | no | no | unchanged |
| `SELF_MISMATCH` | n/a (no checker) | n/a (no checker) | 0 exit=0 | C3 tree at base |
| `SELF_CLEAN_FIXTURE` | n/a | n/a | 0 | C3 tree at base |
| `SELF_MUTANTS_KILLED` | n/a | n/a | 6/6 | C3 tree at base |
| `SHONEN_BOX_COUNT` | 4 | 4 | 4 | unchanged |
| `README_ROWS` | 14 | 14 | 14 | unchanged |
| `HOLDS_C2_V5` | no | no | yes | C3 tree at base |
| `EMB_R65` | 15/1 exit=1 | 15/1 exit=1 | 15/1 exit=1 | unchanged (legit M39 drift retained) |
| `EMB_R67` | 16/0 exit=0 | 16/0 exit=0 | 16/0 exit=0 | unchanged |
| **`EMB_R68`** | **17/7 exit=1** | **17/0 exit=0** | **17/0 exit=0** | C3 moves to target |
| `EMB_R69` | 17/0 exit=0 | 17/0 exit=0 | 17/0 exit=0 | unchanged |
| **`EMB_PINNED_SCRIPT_IS_S046`** | no | yes | yes | C3 moves to target |
| `EMB_R68_BYTES_UNCHANGED` | yes | yes | yes | unchanged |
| `EMB_R65_BYTES_UNCHANGED` | yes | yes | yes | unchanged |
| **`EMB_PIN_MUTANT_KILLED_ATTRIBUTED`** | n/a | 1/1 | 1/1 | C3 moves to target |
| **`HOLDS_C3_V1`** | no | yes | yes | C3 moves to target |
| `HOLD_REPLAY` | 10/10 | 10/10 | 10/10 | unchanged |
| `GATE_SELFTEST` | exit 0 | exit 0 | exit 0 | unchanged |
| `F_COVERAGE` | 5/8 | 5/8 | 5/8 | unchanged |
| `FRESH_ROWS` | 18/18 | 18/18 | 18/18 | unchanged |
| `HOLDS_OK_V7` | yes | yes | yes | unchanged |
| `A1_C1` | no | no | yes | C3 tree at base |
| `A1_C2` | no | no | yes | C3 tree at base |
| **`A1_C3`** | **no** | **yes** (`binds_s046=yes script_digest=yes script_prints_17_lines=yes`) | yes | C3 moves to target |

Counter exits: base `measure.py` 0, C3-only 0, target 0; `measure-a1.py` base 1 (all three A1 false), C3-only 1
(`A1_C3=yes`, `A1_C1/A1_C2=no`), target 0 — i.e. the C3-only tree's A1 exit is exactly the base exit plus C3's
own label, no other A1 label moves. `c3_strict` (C3-owned README line only) reproduces every C3-only row
verbatim: `EMB_R68=checked_blocks=17 problems=0 exit=0`, `HOLDS_C3_V1=yes`, `GATE_SELFTEST=exit 0`,
`HOLDS_OK_V7=yes`.

Base reproduction of the documented before-vector (lane checker run against the untouched base archive):
`SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0`, `SELF_MISMATCH=9` — identical to `reports/round-70/claims.md` §C2
"Before".

## 3. Falsification attempts on C3's own axis (all fail closed)

The pin must not be a way to stop checking, so three attacks on copies:

1. **Drift with the pin active** — append ` TAMPERED` to the first quoted output line of the r68 entry
   (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:25`, block `$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive`):
   `drift entry:25 embedded output line not in recheck stdout: …TAMPERED` / `checked_blocks=17 problems=1` / exit 1.
   The pin does not suppress drift detection (`problems += drift(...)` is live at
   `corpus/check_embedded_outputs.py:178`).
2. **Pin path escape** — set the pin's `use` to `../outside.py`:
   `drift entry:128 pinned historical script digest mismatch: ../outside.py (path escapes the tree)` / exit 1
   (`check_embedded_outputs.py:136`).
3. **Pin removal** — `target` minus `embedded_output_pins.json` + `derive_axml_anchors_r68.py` (i.e. C3's change
   reverted from the landed tree) reads `EMB_R68=checked_blocks=17 problems=7 exit=1`,
   `EMB_PINNED_SCRIPT_IS_S046=no`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=n/a`, `HOLDS_C3_V1=no`, `A1_C3=no`,
   while `C1_GATE=checked_blocks=24 problems=0`, `C1_LINT` exit 0 and `SELF_MISMATCH=0 … SELF_MUTANTS_KILLED=6/6`
   stay at target. So C3's five labels are attributable to C3's three files alone, and C1's/C2's labels do not
   depend on them. No silent fallback to the current script.

The pin's digest is named by the entry's own text, not assigned for free:
`round-68-apk-axml-byte-evidence.md:4` carries `sha256 bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`.

## 4. The one cross-claim coupling (finding, not entanglement)

`SM2` counts every top-level `corpus/*.py` file that the README does not name
(`corpus/self_assessment_check.py:66-81`). C3 introduces `corpus/derive_axml_anchors_r68.py`, so the final tree
keeps `SM2=0` only if C3's README line naming it is present:

- `target` minus **only** the `derive_axml_anchors_r68.py` index line → `SM2=1`, `SELF_MISMATCH=1` (C2 red).
- `target` minus **only** the `check_embedded_outputs.py` index line → `SM2=1` (that line is C2-owned per
  `claims.md:131-134`).
- C3-only tree with the lane's checker and C2's own `self_assessment_check.py` line overlaid:
  `SM1=1 SM2=3 SM3=2 SM4=1 SM5=1 SM6=0 SELF_MISMATCH=8` (better than base 9) — with the C3-owned line only
  (`c3_strict`): `SM2=4`, `SELF_MISMATCH=9` (exactly base). So C3's bytes never raise C2's count above base.

Under the frozen definition (`claims.md:129-135`) this is **not** entanglement: C3's own tree carries no checker
(C2 labels n/a = base), and C2's own tree carries no `derive_axml_anchors_r68.py` (its four base-present files
plus `self_assessment_check.py` are enough for `SM2=0`). It is a landing-coherence requirement: **C3's
`derive_axml_anchors_r68.py` index line must land with C3's file**, or the combined tree falsifies C2 with a
located `SM2=1`. Both lines are present in the landed candidate bytes
(`corpus/README.md:21-22` at `17ee7f87`).

## 5. Residual risks

- The verdict is on the landed candidate bytes only; the final flip revision must not edit `corpus/README.md`
  beyond the C05 row (C1) — editing the C3/C2 index lines there would move `SM2` without any claim owning the move.
- `EMB_R68_BYTES_UNCHANGED=yes` is checked against the counter's hard pin; an admission-time edit of the r68 entry
  would falsify C3 regardless of the gate (control G already models this).
- No tooling installed or upgraded in this seat (pacman paused; nothing needed beyond Python 3 stdlib and git).

Blockers: none. No lane file was written or edited; only this report and the deleted `/tmp/revenger-r70-R70W2SepC3*`
scratch were touched.
