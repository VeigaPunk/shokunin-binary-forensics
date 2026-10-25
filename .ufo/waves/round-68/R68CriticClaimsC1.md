# R68CriticClaimsC1 — C1 claim shape (calibration)

**DEFECT** — the C1 predicate is falsifiable and its mutant/attribution text is exactly frozen, but the attributed conjunct is satisfiable by a marker tag on *any* failed self-test assertion while the round-67 shadowed control stays in place, C1's pass branch transitively reads the C2 artifact (so the claims.md "causally separable" sentence is false), and the kill rule does not close over the pass branch.

Seat: `L1Revenger68.R68CriticClaimsC1` · read-only · base `f165908aaffcf14798de53405fe788986bd33ff9`, build HEAD `4232235723cf8d4731a1e7e78ca098b8af953a57` · counter sha256 verified `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` (matches claims.md:4 and the pin).

## 1. What actually holds (checked, not assumed)

| check the brief asks | result | pointer |
|---|---|---|
| mutant is exactly the frozen one | **PASS** | `reports/round-68/measure.py:385` `C7_CLAUSE = re.compile(r"problems \+= drift\(lines, stdout_set, lineno\)")`, substitution `:392` `problems += []  # mutant: verbatim comparison removed` — byte-for-byte the text of `claims.md:60-62`; `:389-391` refuses (`evaluable=False`, exit 2) unless the clause matches exactly once |
| attribution rule is "last output line ends with the marker" | **PASS** | `measure.py:428` `c7_mut_attributed += rc != 0 and last.endswith(C7_MARKER)`; `C7_MARKER` `:384`; `last` = `tail[-1]` over `(stdout+stderr)` `:149-150` |
| negative control specified with expected values (1/1 killed, 0/1 attributed) | **PASS** | `claims.md:66-70`; implemented `measure.py:460-493` (mutant + spoofed `MARKER`, expects `KILLED=1/1`, `ATTRIBUTED=0/1`). Not trivially satisfied: `"…accepted (spoofed)"` does not `endswith` the registered marker, so the pair really pins the counter's operator |
| kill rule has no clause repairable after scoring | **PASS** for the clause itself | `claims.md:72-78` "honest stop, no re-target, no repaired acceptance condition" |
| do-nothing control genuinely cannot reach the target unchanged | **PASS** | base gate `git show f165908:corpus/check_embedded_outputs.py:133-134` raises `"self-test: drifted entry not caught"` before the marker `require(not ok(dproblems), MARKER)` at `:141`. Replayed independently: base tree + frozen mutant → `exit=1 attributed=0 last='self-test: drifted entry not caught'` (matches `measure-before.log` C7 block exactly) |
| landed build is at target today | **PASS** | counter on HEAD corpus: `C7_SELFTEST=pass`, `C7_CONTROL_PASS=1/1`, `C7_MUTANT_KILLED=1/1`, `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`, `C7_RED_ON_R65_CANDIDATE=yes`, `C7_V2_CLEAN=yes`, `C7_V3_CLEAN=yes`, `HOLDS_OK_V5=yes`, `HOLDS_OK_V6=yes`, exit `0` |

The predicate is therefore falsifiable: the base is genuinely red, and a repair that keeps the r67 shadowing reads red. The defect is not "unfalsifiable" — it is **too cheap to satisfy**.

## 2. DEFECT A (primary) — the attributed conjunct is self-fulfilling: any failed assertion stamps the marker

Clause: `claims.md:52` `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, defined as "the mutant must die *with the registered marker as the last output line*" (`:43`, `:63`).

There is exactly **one** frozen mutant, and it exercises the same leg whose failure the marker names. Nothing in the predicate binds the marker to *that* leg. Counterexample, 2 added lines on the **unrepaired round-67 gate**:

```diff
 def require(cond, msg):
     if not cond:
         print(msg)
+        print(MARKER)
         sys.exit(1)
```

Reproduction trees: `git archive f165908 corpus | tar -x -C /tmp/r68c1/base`, patch as above, then the pinned counting command. Actual counter output on that tree (`/tmp/r68c1/basecheat`):

```
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLDS_OK_V5=yes
HOLDS_OK_V6=no        <- only because C7_V3_CLEAN=n/a (see DEFECT B; base has no v3 file)
exit=0
```

Every C1 label that measures the *gate* is at target while `require(not ok(dproblems), MARKER)` at `f165908:141` remains shadowed dead code — i.e. the exact r67 defect C1 exists to repair is untouched, and the marker now fires on the clean-entry leg, the full-run leg, anything. The same patch applied to the HEAD gate yields byte-identical labels to the unpatched HEAD gate (verified on `/tmp/r68c1/cheat`: the label block above with `C7_V3_CLEAN=yes`, `HOLDS_OK_V6=yes`, exit 0). The counter cannot tell the landed repair from the fake, because `last.endswith(marker)` is a suffix test on a string the gate can print anywhere.

*Fairness note:* the **landed** build is honest — on HEAD, a drift-disjoint specificity mutant (below) reads `attributed=0/1`, so the shipped branch at `corpus/check_embedded_outputs.py:142-145` is causally tied to the drift leg. The defect is that C1's acceptance would not have established that; it certifies "a marker line appeared", not "the marker is bound to the removed comparison".

Smallest safe correction — add a **second frozen mutant on a disjoint leg** and require it *not* to be attributed:

```python
# measure.py, C7 block
C7_SPEC_CLAUSE = re.compile(r'json\.dumps\(\{"fact": "b", "v": 2\}, sort_keys=True\)')
# mutant: the full-run quoted output drifts -> the full-run require fails, not the drift leg
```

Measured discrimination (gate `--self-test`, one tree per variant):

| gate | frozen mutant | specificity mutant |
|---|---|---|
| HEAD (landed repair) | exit 1, attributed **1/1** | exit 1 `self-test: full-run entry not clean`, attributed **0/1** |
| base + marker-tag cheat | exit 1, attributed 1/1 | exit 1, attributed **1/1** ← caught |

So adding `C7_SPEC_MUTANT_KILLED=1/1 ∧ C7_SPEC_MUTANT_KILLED_ATTRIBUTED=0/1` to the pass branch kills the fake and passes the landed repair, unchanged.

## 3. DEFECT B — C1 imports the C2 artifact, so "causally separable" is false and the verdict can be undefined

Clauses: `claims.md:57` `HOLDS_OK_V5=yes` **and** `HOLDS_OK_V6=yes`; `claims.md:34-36` "The two claims are causally separable … Neither counter reads the other's artifact (C1's counter labels read the gate file; C2's aggregate reads the README row and the knowledge column)".

`measure.py:521-526`:

```python
c7_targets    = (c7_present and c7_selftest_ok and c7_control_ok == 1 and c7_mut_attributed == 1 and c7_red and c7_v2_clean)
holds_ok_v5   = (holds_ok_v4 and c7_targets)
holds_ok_v6   = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0 and c7_v3_clean)
```

`c7_v3_clean` (`measure.py:441-444`) is computed by running `--entry corpus/knowledge/round-68-apk-axml-byte-evidence.md` — **the C2 artifact**. C1's pass branch therefore cannot be satisfied without the C2 candidate file existing *and* being gate-clean. The separability sentence is textually wrong on the C1 side.

Actual evidence (`/tmp/r68c1/nov3` = HEAD corpus minus the round-68 knowledge entry):

```
C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
C7_V3_CLEAN=n/a (no v3 file)
HOLDS_OK_V5=yes
HOLDS_OK_V6=no
exit=0
```

Pass branch: unmet (`HOLDS_OK_V6` no). Kill rule (`claims.md:72-78`): no clause fires — self-test exits 0, mutant killed 1/1, attributed 1/1, neg `1/1`/`0/1`, `HOLDS_OK_V4=yes`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`. **Neither pass nor FALSIFIED** — an undefined state, triggered by a C2-side deletion. The same undefined state is what lets base+cheat (DEFECT A) sit at `HOLDS_OK_V5=yes` with only the C2 conjunct holding it back.

Smallest safe correction: C1's branch must be a C1-only composite —

```
HOLDS_OK_V5=yes ∧ C7_NEG_SPOOF_KILLED=1/1 ∧ C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
```

i.e. `HOLDS_OK_V6` minus `c7_v3_clean`. `C7_V3_CLEAN` already appears as C2's own conjunct (`claims.md:120`), so nothing is lost and the two claims become genuinely separable.

## 4. DEFECT C — the kill rule does not close over the pass branch

Pass branch conjuncts (`claims.md:47-58`): `C7_GATE_PRESENT`, `C7_SELFTEST`, `C7_CONTROL_PASS`, `C7_MUTANT_KILLED`, `C7_MUTANT_KILLED_ATTRIBUTED`, the neg pair, `C7_RED_ON_R65_CANDIDATE`, `HOLDS_OK_V5`, `HOLDS_OK_V6`, exit 0.
Kill rule (`claims.md:72-78`) enumerates only: self-test exit ≠ 0; mutant not killed; attributed ≠ 1/1; neg pair wrong; `HOLDS_OK_V4` no; `HOLD_CALIBRATION` < 4/4; `HOLD_REPLAY` < 10/10; `FRESH_ROWS` ≠ 18/18.

Missing: `C7_CONTROL_PASS`, `C7_RED_ON_R65_CANDIDATE`, `HOLDS_OK_V5`, `HOLDS_OK_V6`, `GATE_PRESENT`, exit 0. Concrete undefined-verdict tree (`/tmp/r68c1/redblind`: HEAD gate with `problems = []` inserted before the entry-mode print loop — self-test untouched, entry mode blind):

```
C7_SELFTEST=pass
C7_RED_ON_R65_CANDIDATE=no exit=0 :: checked_blocks=15 problems=0
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLD_CALIBRATION=4/4  HOLD_REPLAY=10/10  FRESH_ROWS=18/18
HOLDS_OK_V5=no
HOLDS_OK_V6=no
exit=0
```

Pass branch false; **every** enumerated kill clause satisfied. That is the round-67 failure mode in miniature: an asymmetric rule that invites a post-scoring re-reading ("the rule didn't say so, but obviously…").

Smallest safe correction: append one catch-all — "or any other conjunct of the pass branch is not met". No re-target, no threshold change, strictly a closure.

## 5. Bounded observations (not defects of the claim)

- `C7_CONTROL_PASS=1/1` is `selftest_ok ∧ C7_MARKER in gate_text` (`measure.py:408`) — a "the string exists" control, near-free. Not load-bearing for C1's force, because `C7_SELFTEST=pass` is separately required.
- `last` concatenates stdout then stderr (`measure.py:149-150`). A repair that emits any stderr line at exit would silently drop attribution to 0/1. Direction of risk is only anti-repair (it can make C1 harder, not easier), so I do not raise it.
- The negative control does not test instrument specificity, only the counter's `endswith`-vs-`in` choice; that is why it does not catch DEFECT A. Its stated purpose at `claims.md:68-70` is accurately narrower than "attribution", so this is a scope note, not a false claim.
- Tree hygiene: `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` (mtime 2026-10-25 03:29:00, untracked) appeared in the lane working tree during this wave. Not this seat's write (every invocation here used `python3 -B`, and the counter spawns the gate with `-B`), so it is another seat importing the gate as a module without bytecode suppression. It cannot affect the measured tree (`git archive` takes committed content only) and it is outside this seat's write scope — flagging for the ledger/L1 rather than deleting it. Left in place.

## 6. Impacted axes

- **calibration (C1)** — DEFECT A under-certifies the axis; DEFECT C leaves the axis's verdict open.
- **separability (C1×C2)** — DEFECT B: the frozen text asserts a property the counter contradicts (`measure.py:525-526`), and C1 can be blocked or un-blocked by C2's file alone.
- **coverage (C2)** — untouched by this seat; the C1-side use of `C7_V3_CLEAN` is the only coupling and it is removable from C1 without touching C2's own conjunct.

## 7. Reproduce (read-only, cwd `/`, no repo writes)

```sh
# trees
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
git archive 4232235 corpus | tar -x -C /tmp/r68c1/head
git archive f165908 corpus | tar -x -C /tmp/r68c1/base
# DEFECT A: 2 lines into base corpus/check_embedded_outputs.py -> print(MARKER) in require
# DEFECT B: rm /tmp/r68c1/head/corpus/knowledge/round-68-apk-axml-byte-evidence.md
# DEFECT C: insert `problems = []` before the entry-mode print loop in main()
cd / && TMPDIR=/tmp/r68c1/tmp python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py <tree>
```

All three trees and the gate-level variant matrix were executed; the outputs quoted above are verbatim.

## 8. Tooling

No installs or upgrades this seat (none needed; python3 + git archive sufficed). Every write stayed inside `/tmp/r68c1` and this report.
