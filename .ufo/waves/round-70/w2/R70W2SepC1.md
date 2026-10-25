SEPARABLE — with the C1 change set as assigned (README C05 flip + `snapshots/`/`lint_entry.py` index lines + entry header `admitted` + one SCORECARD `K_HELD_BACKED 8/14 -> 9/14` line), no other claim's label rises above base; the frozen `claims.md` §Separability enumeration OMITS that SCORECARD line and without it C2's `SM6` goes 0 → 1 (that one-label variant is ENTANGLED, file responsible `corpus/README.md` C05 row).

# R70W2SepC1 — separability of claim C1 (coverage), wave 2 (falsify)

Seat: fresh wave-2 seat, no wave-1 report read before this verdict. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Target bytes: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`, README C05 `uncovered`).
Base: `3f5edbc206351232a3d2d801334dd930499ccaf5`. Counters verified before use:

```
$ sha256sum reports/round-70/measure.py reports/round-70/measure-a1.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  reports/round-70/measure.py
96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191  reports/round-70/measure-a1.py
```

Scratch trees (all under `/tmp/revenger-r70-R70W2SepC1`, deleted at exit):

| tree | construction |
|---|---|
| `base` | `git archive 3f5edbc… corpus SHONEN.md SCORECARD.md SKILL.md` — untouched |
| `tree` | `git archive 17ee7f8… corpus SHONEN.md SCORECARD.md SKILL.md` — the landed candidate, untouched |
| `c1` | `base` + C1's files only (`knowledge/round-70-apk-axml-byte-evidence.md`, `lint_entry.py`, `fixtures/apk-r65/entry_checks.py`, the three new `snapshots/` files; `snapshots/ResourceTypes.h` unchanged base→target), the whole `corpus/SOURCES.md` diff (S032/S034/S038/S041 re-opens + S047 `used-by` + new S048/S049 rows — `grep -n 'derive_axml_anchors_r68\|self_assessment_check\|embedded_output_pins' corpus/SOURCES.md` at the target: **no match**, so the SOURCES diff carries no C2/C3 artifact), README `snapshots/`+`lint_entry.py` index lines, README C05 row flipped to `held`, entry header `candidate` → `admitted` |
| `c1b` | `c1` + one appended SCORECARD line `K_HELD_BACKED 8/14 -> 9/14` (the variant the assignment specifies) |
| `tip` | `tree` + the three admission edits only (README C05 flip, header `admitted`, SCORECARD K line) — final-tip rehearsal on the landed bytes |

No lane file was read from the mutable worktree for any judged value (all from `git archive`); no lane file was written; `git -C <lane> status --porcelain` shows only other seats'/L1's entries (`M SCORECARD.md`, `M SHONEN.md`, `.ufo/…`), none mine.

## Label table — base value first, then each tree

| label (owner) | base `3f5edbc` | `c1` (literal §Separability, no K line) | `c1b` (assigned C1 set) | landed `17ee7f8` | `tip` (admission rehearsal) |
|---|---|---|---|---|---|
| `K_HELD_BACKED` (C1) | 8/14 score=5.7 | 9/14 score=6.4 | 9/14 score=6.4 | 8/14 score=5.7 | 9/14 score=6.4 |
| `K_HELD_BACKED_STRICT` (C1) | 8/14 | 9/14 | 9/14 | 8/14 | 9/14 |
| `C05_STATUS` (C1) | uncovered | held | held | uncovered | held |
| `C05_KNOWLEDGE_COLUMN` (C1) | `-` | `knowledge/round-70-apk-axml-byte-evidence.md` | same | `-` | same |
| `C05_SINGLE_V5` (C1) | no | yes | yes | no | yes |
| `V5_ENTRY_PRESENT` (C1) | no | yes | yes | yes | yes |
| `V5_ADMITTED_MARKED` (C1) | no | yes | yes | **no** (candidate) | yes |
| `C1_GATE` (C1) | n/a | checked_blocks=24 problems=0 exit=0 | same | checked_blocks=24 problems=0 exit=0 | same |
| `C1_LINT` (C1) | n/a | QMAP=0; Q14=0; Q15=0; HEADER=0 exit=0 | same | same | same |
| `HOLDS_C1_V5` (C1) | no | **yes** | **yes** | no | **yes** |
| `A1_C1` (C1) | no (no v5 entry) | — | **yes** (distinct_commands=24 scripts_allowlisted=True readout_lines=15/15 source_rows_tier_a=7/7) | — | **yes** |
| lane checker `SM1..SM6` (C2) | 1,4,2,1,1,0 | 1,**3**,2,1,1,**1** | 1,**3**,2,1,1,**0** | 0,0,0,0,0,0 | 0,0,0,0,0,0 |
| `SELF_MISMATCH` (C2, lane checker) | 9 (exit 1) | 9 (exit 1) | **8** (exit 1) | 0 (exit 0) | 0 (exit 0) |
| `SELF_MISMATCH` / `SELF_CLEAN_FIXTURE` / `SELF_MUTANTS_KILLED` (C2, in-counter) | n/a / n/a / n/a (no checker) | n/a / n/a / n/a | n/a / n/a / n/a | 0 / 0 / 6/6 | 0 / 0 / 6/6 |
| `SHONEN_BOX_COUNT` / `README_ROWS` (C2) | 4 / 14 | 4 / 14 | 4 / 14 | 4 / 14 | 4 / 14 |
| `HOLDS_C2_V5` (C2) | no | no | no (checker absent, as base) | yes | **yes** |
| `EMB_R65` (C3) | 15 blocks / 1 problem | 15 / 1 | 15 / 1 | 15 / 1 | 15 / 1 |
| `EMB_R67` (C3) | 16 / 0 | 16 / 0 | 16 / 0 | 16 / 0 | 16 / 0 |
| `EMB_R68` (C3) | 17 / **7** | 17 / **7** | 17 / **7** | 17 / 0 | 17 / 0 |
| `EMB_R69` (C3) | 17 / 0 | 17 / 0 | 17 / 0 | 17 / 0 | 17 / 0 |
| `EMB_PINNED_SCRIPT_IS_S046` (C3) | no | no | no | yes | yes |
| `EMB_R68_BYTES_UNCHANGED` / `EMB_R65_BYTES_UNCHANGED` (C3) | yes / yes | yes / yes | yes / yes | yes / yes | yes / yes |
| `EMB_PIN_MUTANT_KILLED_ATTRIBUTED` (C3) | n/a (no pin) | n/a | n/a | 1/1 | 1/1 |
| `HOLDS_C3_V1` (C3) | no | no | no | yes | **yes** |
| `A1_C2` / `A1_C3` | no / no | no / no | no / no (tool absent, = base) | yes / yes | **yes / yes** |
| `HOLD_REPLAY` / `GATE_SELFTEST` / `F_COVERAGE` / `FRESH_ROWS` (holds) | 10/10 · exit 0 · 5/8 · 18/18 | same | same | same | same |
| `HOLDS_OK_V7` · `measure.py` exit | yes · 0 | yes · 0 | yes · 0 | yes · 0 | yes · 0 |

Commands (each run from `/tmp/revenger-r70-R70W2SepC1`):

```
$ python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py {base,c1,c1b,tree,tip}
$ python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure-a1.py {base,c1b,tip}
$ python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/self_assessment_check.py --root {base,c1,c1b,tip} \
      --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
```

Exit codes: `measure.py` 0 on all five trees; `measure-a1.py` exit 0 on `tip`, exit 1 on `c1b` **only because** `A1_C2`/`A1_C3` are `no` there (the checker and the pin are C2's/C3's files and are absent in a C1-only tree) — the same `no`/`no` the base tree reads, so this is equality with base, not a regression.

## Verdict derivation

1. **C1's own labels move to target in C1's own tree.** `c1b` reads `HOLDS_C1_V5=yes` and `A1_C1=yes` with the same values as the landed bytes reach at `tip` (`C1_GATE=checked_blocks=24 problems=0`, `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0`). The v5 entry's blocks (24) are accepted by the **base** round-69 gate as well as the round-70 gate — so C1's gate conjunct does **not** depend on C3's `corpus/check_embedded_outputs.py` bytes, i.e. no C1↔C3 file entanglement through the gate.
2. **No other claim's label is raised above base by the assigned C1 set.** C2: `SM6` 0 → 0, `SM2` 4 → 3 (better; `snapshots/` becomes named), `SM1/SM3/SM4/SM5` unchanged, `SELF_MISMATCH` 9 → 8 (better), boxes/rows 4/14 unchanged. C3: every `EMB_*`, `EMB_PIN*`, `EMB_*_BYTES_UNCHANGED` label is byte-identical to base. Holds: `HOLDS_OK_V7=yes` on every tree.
3. **The literal `claims.md` §Separability file list is not sufficient.** With C1's declared change set as enumerated there (README index lines + C05 flip; no SCORECARD line), `c1` reads `SM6=1` where base reads `SM6=0`:

```
$ python3 -B …/corpus/self_assessment_check.py --root c1 --lane …/revenger-shokunin
SM1=1  SM2=3  SM3=2  SM4=1  SM5=1  SM6=1   SELF_MISMATCH=9  exit=1
$ … --root c1b
SM1=1  SM2=3  SM3=2  SM4=1  SM5=1  SM6=0   SELF_MISMATCH=8  exit=1
$ … --root base
SM1=1  SM2=4  SM3=2  SM4=1  SM5=1  SM6=0   SELF_MISMATCH=9  exit=1
```

Mechanism (located): `corpus/self_assessment_check.py:175` `sm6()` takes the **last** SCORECARD line naming `K_HELD_BACKED` and requires its `N/14` (arrow target preferred) to equal the README `held` rows; the README flip takes `held` 8 → 9 while the last such SCORECARD line stays `K_HELD_BACKED=8/14` (`base/SCORECARD.md:612`), so `SM6=1`. Appending `K_HELD_BACKED 8/14 -> 9/14` (arrow form is matched by `(?:→|->)`) restores `SM6=0`. This independently confirms the wave-1 connector finding mechanically.
4. **Final-tip rehearsal is green on all three claims simultaneously.** `tip` (landed bytes + exactly the three admission edits) reads `HOLDS_C1_V5=yes`, `HOLDS_C2_V5=yes`, `HOLDS_C3_V1=yes`, `A1_C1=A1_C2=A1_C3=yes`, `SELF_MISMATCH=0 exit=0`, `HOLDS_OK_V7=yes`, `measure.py` exit 0. So the admission revision does not have to trade one claim for another: the single added SCORECARD line is what keeps C2's `SM6` clean while C1's row flips.

## Findings

- **F1 (calibration, confirmed; severity: text-of-contract, not bytes).** `claims.md` §Separability (`reports/round-70/claims.md:129-135`) enumerates C1's change set as "names `lint_entry.py` and flips the C05 row" and does not claim the SCORECARD `K_HELD_BACKED 8/14 -> 9/14` line. Taken literally that change set raises C2's `SM6` from 0 to 1 (`c1` run above), contradicting the same section's conclusion "no claim's tree raises another claim's label above its base value". The assignment's change set (which includes the line) is separable; the frozen sentence is not true of the literal enumeration. Repair is textual and belongs to the L1 (the admission revision already needs the line to keep `SELF_MISMATCH=0` at the final tip — `tip` run).
- **F2 (landing constraint on the flip, from `measure.py:149`).** `c05_single` requires the C05 **knowledge column** to hold exactly one `knowledge/*.md` token. My flip puts the retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` in the tools column (same shape as the C04 and C09 rows) and reads `C05_SINGLE_V5=yes`. If the admission flip names the rejected candidate in the knowledge column, `C05_SINGLE_V5=no` and `HOLDS_C1_V5=no` — a one-line trap for whoever writes the flip.
- **F3 (coverage, positive).** C1's own labels at the landed bytes are already green apart from the three admission edits: `tree` reads `C1_GATE=checked_blocks=24 problems=0 exit=0`, `C1_LINT=… all 0`, `V5_ENTRY_PRESENT=yes`, with only `V5_ADMITTED_MARKED=no` / `C05_STATUS=uncovered` outstanding — exactly the landing order's step-1 state. Nothing in C1's predicate needs bytes from C2 or C3.
- **F4 (calibration, positive).** The lane checker reproduces the documented before-vector exactly on the untouched base archive: `SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0`, `SELF_MISMATCH=9` — identical to `claims.md` §C2 "Before" and to `measure-a1.py`'s frozen `A1_C2` expectation.
- **F5 (source digests, positive).** C1's `corpus/snapshots/` files carry the digests their SOURCES rows name: `APPNOTE.TXT` `0b993022…` (S034), `ResourceTypes.h` `56b88bc4…` (S038), `dex-format.html` `c0428612…` (S045), `rea-android-applications.md` `412d9cb4…` (S039/S043/S049).

## Artifact digests (reproducibility of the constructed trees)

```
041c4878f1121913c4dc2dfff254b78ba43a8713c00ef4873497bc6db2980c69  c1b/corpus/README.md
a1ba476e47afba33ad0b018e54acb7349bb33c73c95be1c30e2fc8d50c206523  c1b/corpus/SOURCES.md
29671cbe8692a1a990a4c6d10fe597a635acc77f74feebdf6f4c80f347eadecf  c1b/SCORECARD.md
5f89432e2336ef0f25778d684fd2490a72c064c1fade87bbbd2bcda75b86b4c8  c1b/corpus/knowledge/round-70-apk-axml-byte-evidence.md  (admitted variant)
819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31  tree/corpus/knowledge/round-70-apk-axml-byte-evidence.md (landed, candidate)
3ef6c7b119b2a5003afdf38ed7981d445565d7575e9aa437e60147393183d76b  c1b/corpus/lint_entry.py
2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9  c1b/corpus/fixtures/apk-r65/entry_checks.py
```

The admitted entry differs from the landed candidate only in the header line (`diff <(sed 's/^admission-status: .*//' …)` → identical), i.e. the admission edit is one line.

## Risks / blockers

- The flip text I exercised is my construction, not a frozen artifact; the labels I report hold for any flip that (a) puts exactly the v5 path in the knowledge column, (b) ends in `| held |`, and (c) is accompanied by the SCORECARD K line. F2 is the failure mode if (a) is violated.
- `c1`/`c1b` cannot show C2's in-counter labels (`SELF_MISMATCH`/`SELF_CLEAN_FIXTURE`/`SELF_MUTANTS_KILLED`) because the checker is C2's file; I used the lane's checker directly on each tree for those labels, which is the same instrument `measure.py` drives.
- No blockers. No package was installed or updated (pacman paused; no `uv tool`/`npx` install was needed). Scratch `/tmp/revenger-r70-R70W2SepC1` removed before returning.
