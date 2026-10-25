REHEARSAL-GREEN — the planned admission edit, applied on a scratch copy of the landed candidate tree, turns every expected label green with counter exit 0; the only red found is in a deliberate negative control (the SCORECARD line omitted), and one residual prose staleness no label sees.

Seat: R70W2FlipRehearsal (wave 2, falsify; leaf). Lane read-only; nothing in the lane was written, edited, committed or checked out.

## Inputs verified

```
$ git -C <lane> log -1 --format='%H %s'
17ee7f87ea8ee72a427af0fd8e7586d09bad99cd round-70: wave-1 integration — v5.1 candidate (still candidate, README unflipped), ...

$ sha256sum reports/round-70/measure.py reports/round-70/measure-a1.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  .../measure.py
96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191  .../measure-a1.py
```
Both match the frozen digests in `claims.md` / `claims-amendment-A1.md`. Scratch trees: `/tmp/revenger-r70-R70W2FlipRehearsal/tree0` (verbatim `git archive 17ee7f87 corpus SHONEN.md SCORECARD.md SKILL.md`) and `.../tree` (same bytes + the three admission edits).

## The admission edit, applied exactly as planned

Three files differ between `tree0` and `tree`; `diff -rq` lists no other file.

1. `corpus/README.md:41` — knowledge cell `—` → `` `knowledge/round-70-apk-axml-byte-evidence.md` `` and status `uncovered` → `held`; every other cell of the row untouched:
```
| C05 | Android packages (APK) | `knowledge/round-70-apk-axml-byte-evidence.md` | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) | held |
```
2. `corpus/knowledge/round-70-apk-axml-byte-evidence.md:11` — `admission-status: candidate` → `admission-status: admitted` (one line; the file's only `admission-status` line).
3. `SCORECARD.md` — one appended final line `K_HELD_BACKED 8/14 -> 9/14` (now line 617).

sha256 before → after:
```
entry      819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31 -> 5f89432e2336ef0f25778d684fd2490a72c064c1fade87bbbd2bcda75b86b4c8
README.md  c7b24f907a0e3f8d60a07d1faef3f9283aca071df5a130c10b84136a45450406 -> 06f7d12869802669cb4d9b9b957c0033bc5451b75e9546d238a85255b5bb7733
SCORECARD  3f86dfdf87c4fb1e71e188d2320882ab1da697bc070b0e492f0373239c9caa90 -> 3ab848136c6e49e4f26fb8137ad0eced62535199f9516f4f6646b7577c911faa
```

## Labels — frozen counter (unflipped landed tree → after the edit)

`python3 -B <lane>/reports/round-70/measure.py <tree>`; unflipped run 3.28 s, flipped run 2.57 s, **both exit 0**.

| label | landed (unflipped) | after admission edit | expected | ok |
|---|---|---|---|---|
| `K_HELD_BACKED` | 8/14 score=5.7 | **9/14 score=6.4** | 9/14 | yes |
| `K_HELD_BACKED_STRICT` | 8/14 | **9/14** | 9/14 | yes |
| `C05_STATUS` | uncovered | **held** | held | yes |
| `C05_KNOWLEDGE_COLUMN` | `-` | **knowledge/round-70-apk-axml-byte-evidence.md** | exact | yes |
| `C05_SINGLE_V5` | no | **yes** | yes | yes |
| `V5_ENTRY_PRESENT` / `V5_ADMITTED_MARKED` | yes / no | yes / **yes** | yes/yes | yes |
| `C1_GATE` | checked_blocks=24 problems=0 exit=0 ok=yes | unchanged | >=17 / 0 | yes |
| `C1_LINT` | QMAP=0; Q14=0; Q15=0; HEADER=0 exit=0 | unchanged | exit 0 | yes |
| `HOLDS_C1_V5` | no | **yes** | yes | yes |
| `SM1..SM6` | 0 0 0 0 0 0 | 0 0 0 0 0 0 | 0 | yes |
| `SELF_MISMATCH` | 0 exit=0 | **0 exit=0** | 0 | yes |
| `SELF_CLEAN_FIXTURE` / `SELF_MUTANTS_KILLED` | 0 / 6/6 | unchanged | 0 / 6/6 | yes |
| `SHONEN_BOX_COUNT` / `README_ROWS` | 4 / 14 | unchanged | 4 / 14 | yes |
| `HOLDS_C2_V5` | yes | **yes** | yes | yes |
| `EMB_R65/R67/R68/R69` | 15/1, 16/0, 17/0, 17/0 | unchanged | 1,0,0,0 | yes |
| `EMB_PINNED_SCRIPT_IS_S046`, `EMB_R68_BYTES_UNCHANGED`, `EMB_R65_BYTES_UNCHANGED`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED` | yes, yes, yes, 1/1 | unchanged | same | yes |
| `HOLDS_C3_V1` | yes | **yes** | yes | yes |
| `HOLD_REPLAY` / `GATE_SELFTEST` | 10/10 / exit 0 | unchanged | 10/10 / 0 | yes |
| `F_COVERAGE` / `FRESH_ROWS` | 5/8 score=6.2 / 18/18 | unchanged | 5/8 / 18/18 | yes |
| `HOLDS_OK_V7` | yes | **yes** | yes | yes |
| counter exit | 0 | **0** | 0 | yes |

Only three labels move, all in the intended direction (K count, C05 row, admitted marker); nothing else regresses.

## Labels — A1 counter

`python3 -B <lane>/reports/round-70/measure-a1.py <tree>` — exit 0, identical before and after the edit (the A1 conjuncts read the entry's commands/sources, not the row):
```
A1_C1_DETAIL=distinct_commands=24 scripts_allowlisted=True readout_lines=15/15 source_rows_tier_a=7/7
A1_C2_DETAIL=base_vector=yes clean_variant=yes defect_variants=6/6
A1_C3_DETAIL=binds_s046=yes script_digest=yes script_prints_17_lines=yes
A1_C1=yes
A1_C2=yes
A1_C3=yes
```

## Standalone checker, lint and gate on the flipped tree

```
$ python3 -B <lane>/corpus/self_assessment_check.py --root .../tree --lane <lane>
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0
SELF_MISMATCH=0                       EXIT=0

$ python3 -B <lane>/corpus/lint_entry.py --entry .../tree/corpus/knowledge/round-70-apk-axml-byte-evidence.md
LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0        LINT_EXIT=0

$ python3 -B <lane>/corpus/check_embedded_outputs.py --entry .../tree/corpus/knowledge/round-70-apk-axml-byte-evidence.md
checked_blocks=24 problems=0          GATE_EXIT=0
```
(The gate also runs from a non-lane cwd because its commands are confined to the tree's own relative scripts.)

## Negative control — the SCORECARD line is load-bearing

Same flipped tree with only the appended `K_HELD_BACKED 8/14 -> 9/14` line removed (`tree-noscore`):
```
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=1
SELF_MISMATCH=1                       CHECKER_EXIT=1
K_HELD_BACKED=9/14 C05_STATUS=held C05_KNOWLEDGE_COLUMN=knowledge/round-70-apk-axml-byte-evidence.md
HOLDS_C1_V5=yes  HOLDS_C2_V5=no  HOLDS_C3_V1=yes  HOLDS_OK_V7=yes  (counter exit 0)
```
So a row flip without the SCORECARD line silently reds C2 (SM6 compares the last `N/14` on the last `K_HELD_BACKED` line — `corpus/self_assessment_check.py` docstring, SM6 — against the count of `held` rows). The rehearsal's step 3 is required, not cosmetic.

## Findings / risks for the L1 (none of them a red expected label)

1. **Residual stale prose after the flip, invisible to every label.** `corpus/README.md:77-82` still reads "C05 Android — … needs an authored APK fixture … the row is `uncovered`, the candidate retained rejected; a re-gate needs the corrected text, not new fixture bytes." After the admission edit that sentence contradicts line 41 (`held`). No mechanical conjunct sees it: the six SM classes cover the README index range (SM1), `corpus/*.py`/`corpus/*/` naming (SM2), SHONEN digests (SM3), SHONEN verifier authorship (SM4), SCORECARD commit ids (SM5) and the SCORECARD K statement (SM6) — none reads the §Frontier section. The frozen landing order ("flips README C05 → held naming only the v5 entry and sets the header admitted") does not require touching §Frontier, so this is a treatment decision, not a predicate change: the same admission revision can drop or rewrite the C05 bullet with no label moving (verified: only the three edits above change any label).
2. **Counter exit code is `HOLDS_OK_V7`-only.** `measure.py` returns `0 if holds_ok else 1` (`reports/round-70/measure.py`, `main` tail); a red claim label does not move the exit — the `tree-noscore` run printed `HOLDS_C2_V5=no` and still exited 0. This matches `claims.md`'s stated exit contract (0/1/2 are hold/crash codes), but the L1 must read labels, never the exit alone, when judging C1/C2/C3.
3. **Score moves 5.7 → 6.4** on the K ground (`K_HELD_BACKED` 9/14). No frozen predicate names the score, and no prose in the tree claims 5.7 as current: `SKILL.md:490` and `SKILL.md:493` quote `=8/14 score=5.7` under the column header "round-66 base value", so they are historical, not stale.
4. `C1_GATE` reads `checked_blocks=24 problems=0` — above the predicate's `>=17` floor; the flip does not change the block count.

## Scope and hygiene

- Lane writes: none. No mutating git/jj in the lane or fleet; lane HEAD read-only at `17ee7f8`.
- Only files written: this report and `/tmp/revenger-r70-R70W2FlipRehearsal/` (scratch trees + logs), deleted before return.
- Tools installed/updated: none (pacman paused host-wide; no `uv`/`npx` install was needed — python3 stdlib + the lane's own scripts sufficed).
