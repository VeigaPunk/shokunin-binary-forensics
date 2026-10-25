NEGATIVE-CONTROL-AS-SPECIFIED — mutant+spoof exits 1 with last line `drifted entry output accepted (spoofed)` (does NOT end with the registered marker); the unspoofed mutant in the same scratch provenance exits 1 ending exactly with the marker, and the pristine baseline is green (exit 0), so the kill is attributed and the attribution is marker-load-bearing.

# R68MutC7Spoof — C1 negative-spoof control

seat: L1Revenger68.R68MutC7Spoof (leaf, mutation-tester) · date: 2026-10-25
scope: read-only on the lane; all mutation in `/tmp` scratch copies of `corpus/`.

## Surface under attack

| artifact | sha256 | bytes |
|---|---|---|
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py` | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` | 6791 |
| frozen counter `reports/round-68/measure.py` | `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` (== claims.md pin) | — |
| build tip measured | `4232235` (working `corpus/` is clean vs tip: `git status --porcelain -- corpus …` printed nothing) | — |

Clause match counts in the pristine file (asserted before any write):

```
LANE_DRIFT_CLAUSE_COUNT 1      # "problems += drift(lines, stdout_set, lineno)"  (:105)
LANE_SPOOF_CLAUSE_COUNT 1      # 'MARKER = "drifted entry output accepted"'       (:36)
LANE_MARKER_SUBSTRING_COUNT 2  # :21 docstring mention + :36 assignment
```

## Mutation applied (scratch A — the assigned negative control)

Scratch: `/tmp/revenger-r68-spoof-neg-_0l4d6wm`, copy of `corpus/` via `shutil.copytree(..., symlinks=True)`.
Copy provenance verified: `sha256(copy) == sha256(lane) == b89183be…`.

Both frozen edits applied programmatically with `count == 1` assertions:

```
@@ -35,3 +35,3 @@
-MARKER = "drifted entry output accepted"
+MARKER = "drifted entry output accepted (spoofed)"
@@ -104,3 +104,3 @@
-        problems += drift(lines, stdout_set, lineno)
+        problems += []  # mutant: verbatim comparison removed
```

Mutated sha256: `862dd687638d0ac4747ca846faaad89c06273dbf5a7877d35891453347365823`
Post-write assertions: drift clause count 0 / mutant text 1; spoof clause count 0 / spoof text 1.

### Run — `python3 -B corpus/check_embedded_outputs.py --self-test`, cwd = scratch root

```
exit code: 1
stdout (repr): 'self-test: drifted entry not caught\ndrifted entry output accepted (spoofed)\n'
stderr (repr): ''
last line:    'drifted entry output accepted (spoofed)'
last.endswith("drifted entry output accepted") -> False
last.endswith("drifted entry output accepted (spoofed)") -> True
```

Landed code path: `corpus/check_embedded_outputs.py:141-146` — `caught` is False, `print("self-test: drifted entry not caught")` then `print(MARKER)` (the spoofed value) then `sys.exit(1)`; the marker is the last emitted line, exactly as the contract requires.

Verdict on the assigned probe: **NEGATIVE-CONTROL-AS-SPECIFIED** (exit != 0 AND last line does not end with the marker).

## Contrast cell B — unspoofed frozen mutant, same provenance

Scratch `/tmp/revenger-r68-spoof-plain-tq5ttm7_`, only the `problems += drift(...)` → `problems += []` edit (match count 1, mutation sha256 `d67d9b121389e922f7a64fafb9bad08ba530691dc68ddb5759ae0d9535f5c2ba`).

```
exit code: 1
stdout (repr): 'self-test: drifted entry not caught\ndrifted entry output accepted\n'
stderr (repr): ''
last line:    'drifted entry output accepted'
last.endswith("drifted entry output accepted") -> True
```

A and B differ by exactly one line (the marker literal) and flip the attribution reading `False` → `True`. The kill is therefore attributable to the registered marker, not to "any non-zero exit".

## Baseline cell C — pristine copy in the same scratch provenance (pairing / no-baseline-failure check)

Scratch `/tmp/revenger-r68-spoof-pristine-m17ufzp0`, byte-identical gate (`sha == b89183be…`).

```
exit code: 0
stdout (repr): 'SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired\n'
stderr (repr): ''
```

Baseline green ⇒ the A/B non-zero exits are caused by the mutations, not by the host/scratch environment. No "baseline failure ⇒ inconclusive" applies.

## Isolation cell D — spoof only, mutant absent

Scratch `/tmp/revenger-r68-spoof-only-msdagll4`, only the `MARKER = "…(spoofed)"` edit (match count 1).

```
exit code: 0
last line: 'SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired'
```

So the spoof alone does not kill; the exit 1 in cell A is caused by the mutant, and the attribution miss in cell A is caused by the spoof. The 2×2 (mutant × spoof) reads killed/attributed = (no,no)→green, (yes,no)→kill+ATTRIBUTED, (yes,yes)→kill+NOT-ATTRIBUTED, and the fourth cell is not reachable for a passing gate.

## Load-bearing detail: `endswith` vs substring

On cell A's last line, `MARKER in last` is **True** while `last.endswith(MARKER)` is **False**. The frozen counter uses `last.endswith(C7_MARKER)` (`reports/round-68/measure.py:428`, `:492`), which is what makes the spoofed suffix fail attribution. An attribution rule written as a substring test would have scored cell A as attributed and the negative control would be vacuous. This is a defended boundary, recorded as an observation — not a request to change the contract.

## Frozen-instrument parity — counter replay on the committed build tree

```
git archive 4232235 corpus | tar -x -C /tmp/revenger-r68-spoof-counter-6SK1
cd / && TMPDIR=/tmp/revenger-r68-counter-spoof python3 -B \
  reports/round-68/measure.py /tmp/revenger-r68-spoof-counter-6SK1
```

Archived gate sha256 `b89183be…` (matches the working file). C7/C05/HOLD labels and exit:

```
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLDS_OK=yes HOLDS_OK_V2=yes HOLDS_OK_V3=yes HOLDS_OK_V4=yes HOLDS_OK_V5=yes HOLDS_OK_V6=yes
K_HELD=8/14 score=5.7 · K_HELD_BACKED=8/14 · K_HELD_BACKED_STRICT=8/14 · C05_STATUS=uncovered · C05_SINGLE_V3=no · HOLDS_C2_V3=no
COUNTER_EXIT=0
```

My independent manual probe reproduces the counter's `c7neg` cell exactly (`measure.py:461-494` uses the same two patterns with `findall(...) != 1` guards). The C2-side labels (`K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`, `C7_V3_CLEAN` on 17 blocks) are observed side-evidence only — C2 is another seat's axis and is not adjudicated here.

## Restoration evidence

- The lane gate was never written: `sha256` before `b89183be…` and after `b89183be…`; `git status --porcelain -- corpus reports LOG.md SCORECARD.md SHONEN.md` returned empty.
- The mutated scratch gate was restored to the pristine lane bytes and re-run:

```
A_SHA_BEFORE_RESTORE 862dd687…   A_SHA_AFTER_RESTORE b89183be…   == lane True
A_RESTORED_EXIT 0   A_RESTORED_LAST 'SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired'
LANE_GATE_SHA_NOW b89183be… unchanged True
```

- Scratch roots (disposable, `/tmp`, outside the lane): `revenger-r68-spoof-neg-_0l4d6wm`, `revenger-r68-spoof-plain-tq5ttm7_`, `revenger-r68-spoof-pristine-m17ufzp0`, `revenger-r68-spoof-only-msdagll4`, `revenger-r68-spoof-counter-6SK1`.

## Findings

1. **MUTANT KILLED, ATTRIBUTION SOUND (cell A).** The frozen negative control reads exactly as claims.md C1 specifies: killed (`exit 1`) and not attributable (last line = spoofed text). Pointer: `corpus/check_embedded_outputs.py:141-146`.
2. **Discriminative, not tautological (cells B/C/D).** The only delta between the attributed cell B and the non-attributed cell A is the marker literal; a green pristine cell C rules out environmental failure; a spoof-only cell D stays green, so the spoof cannot manufacture a kill. Verdicts: killed / survived-neutral / inconclusive = killed, killed, killed; no survivors, no inconclusive cells.
3. **The counter's attribution predicate is the strict one.** `endswith`, not substring (`measure.py:428`, `:492`); cell A demonstrates a substring rule would have mis-scored it (observation only — contract untouched).
4. **Residual note (not a defect for this claim).** The file contains the marker string twice (`:21` docstring, `:36` assignment). The counter's `C7_CONTROL_PASS` conjunct (`measure.py:408`) is a presence check on the file text, so it would also pass with only the docstring mention present. That conjunct is not the attribution rule — attribution is the `endswith` check measured above — so C1's predicate is unaffected; flagged so a future round does not mistake file presence for self-attribution.

## Bounds compliance

Wrote only this report. No lane edit, no git/jj mutation, no write into `corpus/`, `reports/`, `corpus/live/`, `corpus/fixtures/`, or `/home/vgpnk/Projects/shokuknow`. No subagents. No tool installs or upgrades were needed.
