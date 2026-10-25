NEGATIVE-CONTROL-AS-SPECIFIED — the assigned mutant+spoof copy exits 1 and its LAST line is `drifted entry output accepted (spoofed)`, which does NOT end with the registered marker; the same-provenance unspoofed mutant exits 1 ending exactly with the marker and the pristine copy exits 0, so the kill is attributable and the marker is load-bearing. Two independent frozen-instrument defects were also observed (counter crash on the after-tree; `C7_V3_CLEAN=no` on the round-69 build tree) — recorded as findings, not as a change to this probe's verdict.

# R69MutC7Spoof — C7 negative-spoof control (round 69)

seat: L1Revenger69.R69MutC7Spoof (leaf, mutation-tester) · date: 2026-10-25
scope: read-only on the lane; every mutation in `/tmp/revenger-r69-*` scratch copies of `corpus/`.

## Surface under attack

| artifact | sha256 | bytes |
|---|---|---|
| lane `corpus/check_embedded_outputs.py` | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` | 6791 |
| frozen counter `reports/round-69/measure.py` | `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` (== `reports/round-69/claims.md` pin) | — |
| lane tree measured | `35e1258` (`git status --porcelain -- corpus reports LOG.md SCORECARD.md SHONEN.md` empty before and after) | — |

Clause counts in the pristine gate (asserted before any write):

```
LANE_DRIFT_CLAUSE_COUNT 1      # "problems += drift(lines, stdout_set, lineno)"   (:105)
LANE_SPOOF_CLAUSE_COUNT 1      # 'MARKER = "drifted entry output accepted"'         (:36)
LANE_MARKER_SUBSTRING_COUNT 2  # :21 docstring mention + :36 assignment
```

The gate file is byte-identical to the round-68 surface, so the round-68 negative-control numbers reproduce exactly (mutated sha below is identical to `R68MutC7Spoof.md`'s).

## Cell A — the assigned negative control (frozen mutant + marker spoof)

Scratch: `/tmp/revenger-r69-mutc7spoof-hk4fpt4a/A_neg_mutant_plus_spoof` (`shutil.copytree(..., symlinks=True)` of `corpus/`).
Copy provenance: `sha256(copy) == sha256(lane) == b89183be…` (printed `pristine_match=True`).

Both edits applied with `count == 1` guards:

```
@@ :105  -        problems += drift(lines, stdout_set, lineno)
         +        problems += []  # mutant: verbatim comparison removed
@@ :36   -MARKER = "drifted entry output accepted"
         +MARKER = "drifted entry output accepted (spoofed)"
```

Post-write assertions: `drift_clause=0 spoof_clause=0 spoof_text=1 mutant_text=1`.
Mutated sha256: `862dd687638d0ac4747ca846faaad89c06273dbf5a7877d35891453347365823`

### Run — `python3 -B corpus/check_embedded_outputs.py --self-test`, cwd = scratch root

```
EXIT=1
STDOUT_REPR='self-test: drifted entry not caught\ndrifted entry output accepted (spoofed)\n'
STDERR_REPR=''
LAST_LINE='drifted entry output accepted (spoofed)'
LAST_ENDSWITH_MARKER=False        # last.endswith("drifted entry output accepted")
LAST_ENDSWITH_SPOOFED=True
LAST_CONTAINS_MARKER=True         # substring only — see load-bearing note
```

Emission path: `corpus/check_embedded_outputs.py:141-146` — `caught` is False, `print("self-test: drifted entry not caught")`, `print(MARKER)` (the spoofed value), `sys.exit(1)`. The marker is the final emitted line, exactly as the contract requires.

Assigned-probe result: exit != 0 AND last line does not end with the registered marker → **NEGATIVE-CONTROL-AS-SPECIFIED**.

## Contrast cells (same provenance, discriminative not tautological)

| cell | edit | exit | last line | ends with marker |
|---|---|---|---|---|
| A mutant+spoof | both | 1 | `drifted entry output accepted (spoofed)` | **False** |
| B plain mutant | drift clause only (`d67d9b12…`) | 1 | `drifted entry output accepted` | **True** |
| C pristine | none (`b89183be…`) | 0 | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` | False |
| D spoof only | marker only (`974c3c5d…`) | 0 | `SELFTEST OK: …` | False |

A and B differ by exactly one literal (the marker) and flip attribution False→True. C green rules out an environmental/baseline failure ("baseline failure ⇒ inconclusive" does not apply). D shows the spoof alone cannot manufacture a kill. The 2×2 reads (mutant,spoof) = (no,no)→green, (yes,no)→kill+ATTRIBUTED, (yes,yes)→kill+NOT-ATTRIBUTED; the fourth cell is unreachable for a passing gate. All four cells' outputs were captured with full stdout/stderr reprs in the probe transcript (`/tmp/revenger-r69-mutc7spoof-hk4fpt4a` before cleanup).

## Load-bearing detail: `endswith`, not substring

On cell A's last line `MARKER in last` is True while `last.endswith(MARKER)` is False. The frozen counter uses the strict `last.endswith(C7_MARKER)` (`reports/round-69/measure.py:428` region and the `c7neg` cell at `:461-494`; `HOLDS_OK_V6` requires `c7_neg_attributed == 0` at `:573-575`). A substring rule would have scored cell A as attributed and the negative control would be vacuous. Observation only — the contract is untouched.

## Counter replay — the registered control reads as specified, but only on a tree without the Q15 checker

```
git archive HEAD corpus | tar -x -C /tmp/revenger-r69-spoof-counter/tree   # gate sha b89183be… matches
cd / && TMPDIR=… python3 -B reports/round-69/measure.py <tree>
```

On the **HEAD tree as committed** the counter aborts:

```
FRESH_ROWS=18/18
Q15_PRESENT=yes
Traceback (most recent call last):
  File ".../reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
EXIT=1
```

Cause: the Q15 block is module-level code at `measure.py:151-182` and calls `run(...)` at `:158`; `def run` is not bound until `measure.py:187`. Any tree containing `corpus/q15_tree_id_check.py` (the after-tree C2 requires) crashes before the C7 block at `:425+` — so `Q15_SELFTEST`/`Q15_FALSE_KILLED`/`Q15_RESTATE_OK` are unreachable in a completed run and the counter's exit is 1.

Control run (same archived tree, `corpus/q15_tree_id_check.py` deleted in scratch only) completes:

```
Q15_PRESENT=yes
Q15_SELFTEST=n/a (no checker)
C7_SELFTEST=pass
MUTANT check_embedded_outputs.py control exit=0 pass
MUTANT check_embedded_outputs.py c7 exit=1 killed :: drifted entry output accepted
MUTANT check_embedded_outputs.py c7neg exit=1 killed :: drifted entry output accepted (spoofed)
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLDS_OK_V4=yes HOLDS_OK_V5=yes HOLDS_OK_V6=no
COUNTER_EXIT=0
```

So the frozen instrument's own `c7neg` cell reproduces my manual probe byte-for-byte — the negative control is as specified **where the counter can run**. `measure-before.log` shows the same `C7_NEG_SPOOF=1/1 / 0/1` lines because the base tree `222a7a7` had no checker, so the Q15 block printed `n/a` and execution continued.

## Finding 1 (calibration, blocking for C1/C2 measurement) — frozen counter cannot evaluate the after-tree

`measure.py:158` calls `run` before `measure.py:187` defines it. Consequence: with `corpus/q15_tree_id_check.py` present (HEAD), the counter exits 1 with a traceback; `reports/round-69/claims.md` void condition "counter exit non-zero at final" is therefore hit by construction, and C2's `Q15_SELFTEST`/`Q15_FALSE_KILLED`/`Q15_RESTATE_OK` predicates cannot be printed by the pinned counter at all. The counter is pinned (`bca74e6d…`) and claims.md forbids editing it after the claims revision, so this is a frozen-instrument defect, not a seat error. `measure-before.log` masks it because the base tree lacked the checker — and that same fact contradicts claims.md's C2 "Red-before (committed history)" sentence "`Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes`" (the committed receipt actually reads `Q15_SELFTEST=n/a (no checker)` / `Q15_FALSE_KILLED=n/a (no checker)` at `measure-before.log:23-24`). That is the D1-class "stated identity contradicted by the committed receipt" defect class re-occurring inside the same round that adds Q15.

## Finding 2 (calibration, voids both claims on build state) — `C7_V3_CLEAN=no`, `HOLDS_OK_V6=no`

On the round-69 build tree (HEAD `35e1258`, checker removed only to let the counter finish):

```
C7_V3_CLEAN=no exit=1 :: checked_blocks=17 problems=7
C7_V4_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
HOLDS_OK_V6=no
```

The seven problems, enumerated by calling the archived gate's own `evaluate()` on the unchanged v3 bytes:

```
drift entry:137 embedded output line not in recheck stdout: enum RES_STRING_POOL_TYPE : 239
drift entry:138 … enum RES_XML_TYPE : 241
drift entry:139 … enum RES_XML_START_NAMESPACE_TYPE : 245
drift entry:140 … enum RES_XML_END_NAMESPACE_TYPE : 246
drift entry:141 … enum RES_XML_START_ELEMENT_TYPE : 247
drift entry:142 … enum RES_XML_END_ELEMENT_TYPE : 248
drift entry:143 … enum RES_XML_RESOURCE_MAP_TYPE : 253
```

Cause is the C05 repair bundle, not a candidate byte change:

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md` sha256 is `ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e` at **both** `222a7a7` and HEAD (unmodified, as the claims require).
- `corpus/derive_axml_anchors.py` sha256 changed `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` (base) → `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa` (HEAD) — C05 repair item 1.
- The extended script now prints the enum values, so the v3 embedded lines no longer match verbatim:

```
v3 embedded (round-68):     enum RES_STRING_POOL_TYPE : 239
current derivation output:  enum RES_STRING_POOL_TYPE : 239 = 0x0001
                            enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
                            enum block open : 237 / enum block close : 263
```

`HOLDS_OK_V6 = HOLDS_OK_V5 ∧ c7_neg_killed == 1 ∧ c7_neg_attributed == 0 ∧ c7_v3_clean` (`measure.py:573-575`). Since item 1 of the C05 repair set necessarily changes the derivation output, and the v3 candidate is forbidden to change (void condition "prior rejected candidates altered"), `c7_v3_clean` is False on every admissible round-69 tree — this is the D5 `HOLDS_OK_V6`/`c7_v3_clean` separability coupling firing for real. The claims list "`HOLDS_OK_V4`/`HOLDS_OK_V5`/`HOLDS_OK_V6` not yes" as a void condition, so the build as committed is void before any Q adjudication. Not adjudicated here (other seats own C1/C2); recorded with pointers so it is not lost.

Two side observations, not adjudicated:
- `C7_V4_CLEAN=yes :: checked_blocks=17` — identical block count to v3, while `claims.md` C1 item 2 says the v4 entry re-embeds a 20-line derivation. The gate counts fenced command blocks, not output lines, so this is not by itself a contradiction; flagging only so the Q-side seats compare block counts deliberately.
- `K_HELD_BACKED=8/14` and `C05_SINGLE_V4=no` on HEAD are expected build-state values (README not flipped), consistent with the milestone.

## Restoration evidence

- The lane gate was never written: sha256 before `b89183be…`, after `b89183be…`; `git status --porcelain -- corpus reports LOG.md SCORECARD.md SHONEN.md` empty before and after all runs.
- Every mutated scratch was restored to the pristine lane bytes and re-run:

```
A_SHA 862dd687…  →  RESTORED_SHA b89183be…  equals_lane=True  RESTORED_EXIT 0  RESTORED_LAST 'SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired'
B_SHA d67d9b12…  →  RESTORED_SHA b89183be…  equals_lane=True  RESTORED_EXIT 0
C/D (unmutated / spoof-only)  RESTORED_SHA b89183be…  equals_lane=True  RESTORED_EXIT 0
```

- Scratch roots (disposable, `/tmp`, deleted on return): `revenger-r69-mutc7spoof-hk4fpt4a`, `revenger-r69-spoof-counter`, `revenger-r69-spoof-counter2`.

## Verdict

**NEGATIVE-CONTROL-AS-SPECIFIED** for the assigned probe: exit 1, last line `drifted entry output accepted (spoofed)`, `last.endswith("drifted entry output accepted") == False` — the registered marker is not the last line, and the attribution rule (`endswith`) is what makes that observable. The control is discriminative (B attributed, C/D green), not tautological. Mutant KILLED; no survivor; no inconclusive cell.

## Bounds compliance

Wrote only this report. No lane edit, no git/jj mutation, no write into `corpus/`, `reports/`, `corpus/live/`, `corpus/fixtures/`, or `/home/vgpnk/Projects/shokuknow`. No subagents. No tool installs or upgrades were needed (Python stdlib + coreutils + git read-only only).
