# R69HoldSweep — prior-hold regression sweep (leaf, read-only)

REGRESSION — `C7_V3_CLEAN` yes→**no** (exit 1, `problems=7`) and `HOLDS_OK_V6` yes→**no** on the
round-69 build tree, plus the frozen counter crashing (`COUNTER_EXIT=1`,
`NameError: name 'run' is not defined`, `measure.py:158`). All ten verifier self-tests, all
C2–C6 attribution holds and `HOLDS_OK_V4`/`V5` still hold.

## Tree under test

| item | value |
|---|---|
| lane | `/home/vgpnk/Projects/shokunin/revenger-shokunin` |
| tree | `git archive refs/heads/main corpus` → `/tmp/revenger-r69-holdsweep/corpus-tree` |
| `refs/heads/main` / `HEAD` | `35e12584d37434632fa06a6c2975ab55f29a8d3f` |
| base (red-before) | `222a7a7` (round-68 tip) |
| counter | `reports/round-69/measure.py` sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` — **matches** the pinned sha in `claims.md` |
| receipt | `reports/round-69/measure-before.log` sha256 `e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29` |
| claims | `reports/round-69/claims.md` sha256 `a007710bd63c676b0c52777d944b70cc1d5172d5f1a5387fdc2ffaa065b9ba46` |

Counter reproducibility on the base tree: `archive 222a7a7 corpus` → `measure.py` → exit **0**,
output `diff`-identical to the committed `measure-before.log` (`BEFORE_LOG_BYTE_IDENTICAL`).
The counter is sound on `222a7a7` and broken on `35e12584`; the only new code between them is the
round-69 Q15 block.

## Ten `verify_*.py` self-tests (cwd = tree, `python3 -B corpus/<f> --self-test`)

| script | exit | last line |
|---|---|---|
| `verify_evm_evidence.py` | 0 | `NEGATIVE REJECTED candidate destination mismatch` |
| `verify_icon_languages.py` | 0 | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` |
| `verify_icon_states.py` | 0 | `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED` |
| `verify_js_graph_delta.py` | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` |
| `verify_multi_icon_states.py` | 0 | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` |
| `verify_named_multi_icon_states.py` | 0 | `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not …` |
| `verify_pe_resources.py` | 0 | `NEGATIVE REJECTED payload relation mismatch` |
| `verify_saved_evidence.py` | 0 | `NEGATIVE JS REJECTED: JS: wrong package-main mapping` |
| `verify_semantic_trace.py` | 0 | `NEGATIVE REJECTED relation differs from source parent` |
| `verify_shape_evidence.py` | 0 | `NEGATIVE REJECTED changed-property evidence mismatch` |

10/10 exit 0 → `HOLD_REPLAY=10/10`, `HOLD_CALIBRATION=4/4` (the four calibrated names are all
present and pass).

## Counter as invoked by the frozen contract — **exit 1, crash**

```
cd / && TMPDIR=/tmp/revenger-r69-holdsweep/tmpd python3 -B \
  .../reports/round-69/measure.py /tmp/revenger-r69-holdsweep/corpus-tree
→ Q15_PRESENT=yes
→ Traceback (most recent call last):
    File ".../reports/round-69/measure.py", line 158, in <module>
      rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
  NameError: name 'run' is not defined
→ COUNTER_EXIT=1
```

Root cause (`reports/round-69/measure.py`): the Q15 block at `:150-183` calls `run()` at `:158`,
`:163`, `:172`; `def run` is at `:187`, after `evaluable = True` at `:184`. The round-68 counter
had `def run` at `:146`, before all its call sites — the round-69 insert put the new block above
the definition. Because `run()` is only reached when `corpus/q15_tree_id_check.py` exists, the
defect is invisible on base `222a7a7` (checker absent → `else` branch prints three `n/a` lines) and
fires exactly on the build tree that ships the checker (`git cat-file -e 35e12584:corpus/q15_tree_id_check.py`
→ present; `222a7a7` → ABSENT).

Consequences, both contract-level:

1. **Exit-code contract broken.** `claims.md` says `1 = a hold failed`; a `NameError` also exits 1,
   so an instrument crash is indistinguishable from a real failed hold, and `2 = not evaluable` is
   never used. `claims.md` void condition “counter exit non-zero at final” therefore fires on any
   final run over a checker-carrying tree, independent of the wave.
2. **Every label after `:158` is unreachable**: `C2_*`, `C3_*`, `C4_*`, `C5_*`, `C6_*`, `C7_*`,
   `HOLD_CALIBRATION`, `HOLD_REPLAY`, `HOLDS_OK*` never print.

### Labels recovered by a no-edit diagnostic

`/tmp/revenger-r69-holdsweep/hoist_run.py` injects the module's own `run` body into `builtins`
(so the forward reference at `:158` resolves; the later `def run` at `:187` still shadows it for
every other call site). No lane byte is modified; `measure.py` is consumed unchanged via
`runpy.run_path`. Exit 0.

| label | value |
|---|---|
| `HOLD_CALIBRATION` | 4/4 |
| `HOLD_REPLAY` | 10/10 |
| `FRESH_ROWS` | 18/18 |
| `F_COVERAGE` | 5/8 score=6.2 (`native-static, javascript, archives, firmware, evm`) |
| `README_TOKEN_LEGEND_MISMATCH` | 0 (rows=[]) |
| `STRICT_REJECT_WINDOW_SELFTEST` | pass (old_window_miss=True) |
| `C2_CONTROLS_PASS` / `C2_RECEIPT_B_KILLED` / `C2_D2_KILLED` / `C2_RECEIPT_B_KILLED_ATTRIBUTED` | 2/2 · 2/2 · 2/2 · 2/2 |
| `C3_CONTROLS_PASS` / `C3_RECEIPT_KILLED_ATTRIBUTED` | 2/2 · 2/2 |
| `C4_CONTROLS_PASS` / `C4_RECEIPT_KILLED_ATTRIBUTED` | 2/2 · 2/2 |
| `C5_CONTROL_PRESENT` / `C5_CONTROLS_PASS` / `C5_RECEIPT_KILLED` / `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` | 2/2 · 2/2 · 2/2 · 2/2 |
| `C6_CONTROL_PRESENT` / `C6_CONTROLS_PASS` / `C6_RECEIPT_KILLED` / `C6_RECEIPT_KILLED_ATTRIBUTED` | 4/4 · 4/4 · 4/4 · 4/4 |
| `C7_GATE_PRESENT` / `C7_SELFTEST` / `C7_RED_ON_R65_CANDIDATE` | yes · pass · yes (exit 1, problems=1) |
| `C7_V2_CLEAN` | yes (exit 0, checked_blocks=16 problems=0) |
| **`C7_V3_CLEAN`** | **no** (exit 1, checked_blocks=17 **problems=7**) |
| `C7_V4_CLEAN` | yes (exit 0, checked_blocks=17 problems=0) |
| `C7_CONTROL_PASS` / `C7_MUTANT_KILLED` / `C7_MUTANT_KILLED_ATTRIBUTED` | 1/1 · 1/1 · 1/1 |
| `C7_NEG_SPOOF_KILLED` / `C7_NEG_SPOOF_KILLED_ATTRIBUTED` | 1/1 · 0/1 |
| `HOLDS_OK` / `_V2` / `_V3` / `_V4` / `_V5` | yes · yes · yes · yes · yes |
| **`HOLDS_OK_V6`** | **no** |

Build state (not scored as regressions): `K_HELD=8/14`, `K_HELD_BACKED`/`_STRICT`=8/14,
`K_ROW C05 status=uncovered`, `C05_SINGLE_V2/V3/V4=no`, `HOLDS_C2_V3=no`, `HOLDS_C2_V4=no`,
`C05_REJECTED_MARKED=yes` — matches the frozen “no README flip” milestone and the claims'
red-before values exactly.

## Regression 1 — `C7_V3_CLEAN`: yes → no (`problems=0` → `problems=7`)

Prior held value: `reports/round-68/measure-after.log` → `C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0`,
and on base `222a7a7` the committed receipt reads the same `yes exit=0 problems=0`.

Blame isolated by blob ids across `222a7a7` → `35e12584`:

| path | 222a7a7 blob | 35e12584 blob |
|---|---|---|
| `corpus/knowledge/round-65-apk-axml-byte-evidence.md` | `d68e21b23a12` | `d68e21b23a12` (unchanged) |
| `corpus/knowledge/round-67-apk-axml-byte-evidence.md` | `be6de1b124b1` | `be6de1b124b1` (unchanged) |
| `corpus/knowledge/round-68-apk-axml-byte-evidence.md` | `8b95fd136d84` | `8b95fd136d84` (unchanged) |
| `corpus/check_embedded_outputs.py` (gate) | `294b7871a4f0` | `294b7871a4f0` (unchanged) |
| **`corpus/derive_axml_anchors.py`** | `0aa7b4329a34` | **`ec424adfe908` (changed)** |

The three prior candidates keep every byte (void condition satisfied) and the gate is untouched;
the C1 repair item 1 — “extend `derive_axml_anchors.py` … and the enum values” — changed the
command the frozen v3 entry embeds. Gate run on the frozen v3 entry, cwd = tree:

```
python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
drift entry:137 … enum RES_STRING_POOL_TYPE : 239
drift entry:138 … enum RES_XML_TYPE : 241
drift entry:139 … enum RES_XML_START_NAMESPACE_TYPE : 245
drift entry:140 … enum RES_XML_END_NAMESPACE_TYPE : 246
drift entry:141 … enum RES_XML_START_ELEMENT_TYPE : 247
drift entry:142 … enum RES_XML_END_ELEMENT_TYPE : 248
drift entry:143 … enum RES_XML_RESOURCE_MAP_TYPE : 253
checked_blocks=17 problems=7      (exit 1)
```

`python3 -B corpus/derive_axml_anchors.py` now prints 20 lines, each enum line carrying a value
(`enum RES_STRING_POOL_TYPE : 239 = 0x0001`, `enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100`, …,
`enum block close : 263`). The frozen v3 entry embeds the 17-line form without `= 0x…`, so its
seven enum lines no longer appear verbatim in stdout. The v3 entry's own `source: S046` also pins
the pre-extension script (`sha256 bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`,
“17 output lines”); the tree now holds `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`.
So the frozen r68 entry is no longer internally re-derivable on the measured tree even though its
bytes are intact.

Round-69 contract impact: `claims.md` §Void lists “`HOLDS_OK_V4`/`HOLDS_OK_V5`/`HOLDS_OK_V6` not
yes” as a void condition; `HOLDS_OK_V6=no` at the build tree, so a final measure at this instrument
state voids the round regardless of the wave verdicts. Note the C1 predicate itself is not
violated — `C7_V4_CLEAN=yes`, i.e. the v4 candidate is clean under the extended script; it is the
**prior** candidate's cleanliness that the repair traded away.

Design note for the L1 (not a fix, no edit made): the gate is applied to frozen superseded
candidates whose embedded output depends on a script the round deliberately extends. Either the
gate must be pinned per-entry to the script revision the entry names, or `C7_V3_CLEAN` must be
scoped to the round that owns the entry — as written, every future derivation extension
mechanically flips `HOLDS_OK_V6` to `no` and voids the round.

## Regression 2 — counter instrument, `exit 0` → `exit 1`

Covered above. Reproducible in one line; the only state it needs is the checker's presence:
`git cat-file -e 35e12584:corpus/q15_tree_id_check.py` → present. The counter's own docstring
promises “Exit semantics identical: 2 = not evaluable, 0 = holds_ok, 1 = a hold failed” — the Q15
block breaks that promise for the whole file.

## C2 predicate reachability defects (independent of the crash)

1. **`Q15_FALSE_KILLED` cannot be `yes` under the documented invocation.** The counter resolves
   the fixture as `TREE / "reports/round-69/d1-false-sentence.md"` (`measure.py:160`), but
   `claims.md` §Frozen counter prescribes `git archive <commit> corpus`, which produces a tree with
   no `reports/`. Observed on the prescribed tree: `Q15_FALSE_KILLED=n/a (no d1 fixture)`. The
   fixture is committed (`git ls-files | grep d1-false` → `reports/round-69/d1-false-sentence.md`),
   so this is a path-scope bug, not a missing artifact. Under the frozen predicate
   (`Q15_FALSE_KILLED=yes`) C2 is unreachable as written.
2. **`Q15_RESTATE_OK` is `n/a` at this build HEAD.** `corpus/lessons/round-69.md` is ABSENT at both
   `222a7a7` and `35e12584`, so the counter reads `Q15_RESTATE_OK=n/a (no round-69 lesson)`.
   `corpus/QUALITY.md:27` already cites the lesson as the criterion's capture —
   `M48 (`lessons/round-69.md`)` — a dangling pointer at `35e12584`. If the lesson is a wave
   output this is expected build-state, but C2's predicate is then not evaluable at the measured
   commit the claims call “after”.
3. **This round's own claims contradict their receipt (Q15-class).** `claims.md:138-139` states the
   red-before reads `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes`, “the checker ships with the
   claims revision”. The committed `measure-before.log` reads
   `Q15_SELFTEST=n/a (no checker)` / `Q15_FALSE_KILLED=n/a (no checker)`, and
   `git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → ABSENT (added in `e1d22ca`, which is
   *after* the `222a7a7` base the receipt was run on). This is exactly Q15's defect class — a
   stated state asserted against contradicting bytes — inside the criterion's own claim text.

## Q15 checker behaviour (C2 ability-to-fail, run directly)

```
python3 -B corpus/q15_tree_id_check.py --self-test
→ Q15_SELFTEST=pass (true sentence verified; false sentence killed)          exit 0
python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md --lane <lane>
→ Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)         exit 1
```

The checker itself works and kills the committed D1 fixture when given the real path. The defect
is only the counter's fixture path (item 1 above).

## Held, unchanged (no regression)

Ten verifier self-tests 10/10 exit 0 · `HOLD_CALIBRATION=4/4` · `HOLD_REPLAY=10/10` ·
`FRESH_ROWS=18/18` · `F_COVERAGE=5/8` · `README_TOKEN_LEGEND_MISMATCH=0` ·
`STRICT_REJECT_WINDOW_SELFTEST=pass` · C2 2/2+2/2+2/2+2/2 · C3 2/2+2/2 · C4 2/2+2/2 ·
C5 2/2+2/2+2/2+2/2 · C6 4/4+4/4+4/4+4/4 · C7 gate present/selftest pass/red 1/1/v2 clean/v4
clean/control 1/1/mutant attributed 1/1/spoof killed 1/1 attributed 0/1 · `HOLDS_OK`…`V5`=yes ·
prior candidate bytes identical (`round-65/67/68` blob ids unchanged) · `K_HELD=8/14` unchanged.

## Risks / blockers for the L1

- The wave's final measurement cannot produce a valid verdict until `def run` is hoisted above the
  Q15 block and the d1 fixture is resolved outside `TREE` (or the extraction contract changes to
  archive `corpus reports`). The counter is pinned by sha in `claims.md` and must not be edited
  after that revision — this is a claims-revision defect, and the round needs an explicit L1
  decision (void + re-pin, or an L0 question), not a silent patch.
- `C7_V3_CLEAN=no` is not repairable by editing the r68 entry (void condition: prior candidates keep
  every byte). The instrument/gate scoping decision above is the only route.
- `HOLDS_OK_V6=no` voids the round at final measurement under `claims.md` §Void unless the L1
  re-scopes `C7_V3_CLEAN` in a new claims revision.

## Peer cross-check (why the crash escaped the wave)

- `R69CounterIntegrity.md` → `INTACT` (pinned sha at every commit) — a *static* integrity result;
  the crash is a runtime forward-reference, invisible to blob identity.
- `R69CounterReplay.md` → `MATCH` on the base tree `222a7a7` only, which takes the Q15 `else`
  branch and never calls `run()`. My replay reproduces the same `BEFORE_LOG_BYTE_IDENTICAL`
  result, so the two findings are consistent — the defect exists exclusively on a tree that
  carries `corpus/q15_tree_id_check.py`, i.e. the build tree and the eventual final tree.
- `R69CensusReplay.md` → `CLEAN` (47 rows, additive S047) — independent of this instrument path.

Neither peer seat ran the counter on a checker-carrying tree; that is the only configuration in
which `exit 1` appears, and it is the configuration the round will measure.

## Method / hygiene

- Read-only: no write inside the lane, the fleet repo, `corpus/`, or `shokuknow`; no mutating
  git/jj command. The only lane writes are this report.
- No lane file was edited. The one diagnostic uses `builtins.run` injection via
  `runpy.run_path`; `measure.py` bytes are unmodified (sha re-checked before and after:
  `bca74e6d…`).
- Scratch (`/tmp/revenger-r69-holdsweep/`) deleted before returning.
- No tool installed or upgraded (pacman paused; not needed).
