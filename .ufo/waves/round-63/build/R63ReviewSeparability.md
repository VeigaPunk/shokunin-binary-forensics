# Round 63 — separability review (R63ReviewSeparability, 2026-10-23)

## Verdict: SEPARABLE

The three claims move three independent counters under the frozen probe
`reports/round-63/measure.py` (frozen at 54ab973c021cc62ca65dcbe2cbfabe3235d5ee38).
Each tree changed exactly one axis; no tree moved another claim's counter; all
frozen holds stayed green in every tree and every probe exited 0.

| tree | delta over base 55bcb6e | K_HELD_BACKED | F_COVERAGE | C3_RECEIPT_KILLED_ATTRIBUTED | expectation |
|---|---|---|---|---|---|
| A | C06 row `partial → held` naming `knowledge/round-63-zip-central-directory-evidence.md` + that entry file | **7/14** | 4/8 | 0/2 | 7/14, 4/8, 0/2 ✓ |
| B | `corpus/live/runs/round-63/{inspection.json,receipt.json}` only | 6/14 | **5/8** (`firmware` via `inspect_firmware_regions: 1`) | 0/2 | 6/14, 5/8, 0/2 ✓ |
| C | patched `verify_named_multi_icon_states.py` + `verify_icon_states.py` only | 6/14 | 4/8 | **2/2 attributed** | 6/14, 4/8, 2/2 ✓ |

FRESH_ROWS 18/18, HOLD_CALIBRATION 4/4, HOLD_REPLAY 10/10, C2 block 2/2×3 in
all three trees; `HOLDS_OK=yes`, probe exit 0 in all three. No pacman, no tool
installs (none needed).

## Construction

- Base: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 55bcb6e corpus | tar -x`
  into `/tmp/revenger-r63-sep/{a,b,c}`. Base scripts at 55bcb6e confirmed to
  lack `receipt_ok`/in-script forged controls (red-before C3 0/2 consistent).
- Tree A: C06 row flipped in scratch README (status cell → `held `, entry path
  appended to the knowledge cell, i.e. `split("|")[3]` — the cell the
  K_HELD_BACKED check reads); entry file created at
  `corpus/knowledge/round-63-zip-central-directory-evidence.md`. The entry file
  in tree A is a **labeled scratch stub** (probe measures existence only,
  per claims.md "the K probe measures existence, never quality"); candidate
  content quality is not this review's scope.
- Tree B: byte-for-byte copies of the sibling-produced working-tree artifacts
  `corpus/live/runs/round-63/inspection.json` (has top-level `evidence_id`,
  `normalized_result`, `operation="inspect_firmware_regions"`) and
  `receipt.json`. receipt.json carries no `normalized_result`, so it adds no
  counter entry — no false F inflation.
- Tree C: byte-for-byte copies of the sibling-patched working-tree verifiers.
  Each frozen C3 clause matches exactly once (`receipt['command']==command` in
  named; `receipt['fixture_sha256'] == expected_hash` in icon_states), so
  `mutate_c3` evaluated both sites.

## Probe outputs (frozen command `python3 -B reports/round-63/measure.py TREE`, cwd lane root)

### Tree A — claim-relevant lines

```
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
F_COVERAGE=4/8 score=5.0
F_FAMILIES=['native-static', 'javascript', 'archives', 'evm']
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
PROBE_A_EXIT=0
```

### Tree B — claim-relevant lines

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
PROBE_B_EXIT=0
```

### Tree C — claim-relevant lines

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
F_COVERAGE=4/8 score=5.0
MUTANT verify_named_multi_icon_states.py control exit=0 pass
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
PROBE_C_EXIT=0
```

Both C3 kills are attributed per the frozen sentence: non-zero exit, last
output line contains `forged receipt`. Full logs preserved during review at
`/tmp/revenger-r63-sep/probe-{a,b,c}.log` (scratch removed after this report).

## Findings

1. **None blocking.** All nine frozen expectations printed exactly.
2. Flip contract detail for L1's C06 flip: `K_HELD_BACKED` reads README cell
   index 3 (`split("|")[3]`) and requires every `knowledge/*.md` path in that
   cell to exist. The landed flip must (a) end the line with `| held |`,
   (b) name `knowledge/round-63-zip-central-directory-evidence.md` inside the
   knowledge-entries cell, and (c) land the entry file in the same commit.
   A path named only in the work-evidence cell would not back the row.
3. Tree C control output shifts are limited to the frozen fix shape: named
   verifier self-test count 139 → 142 positive checks (the added forged-receipt
   controls); all existing assertions and messages unchanged; replay census
   stays 10/10 in every tree.

## Residual risk / verification gaps

- Tree A exercises counter mechanics with a stub entry and a scratch-authored
  flip row; it does not judge candidate content or gate decisions (Q01–Q13,
  README flip ordering remain L1/falsify-wave scope).
- Trees B/C bytes were snapshotted from sibling working-tree state at
  2026-10-23 ~23:25; if the landed bytes differ, the probe must be re-run on
  the final tip (`measure-after.log` is committed with the report claim
  regardless, per routed debt).
- `C3_RECEIPT_KILLED_ATTRIBUTED` is not part of the probe's `holds_ok`
  expression, so probe exit 0 alone would not prove C3; the printed value was
  compared directly (2/2 in tree C).
