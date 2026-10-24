# R64ExecSkillRun transcript

## Checklist availability

Initially requested checklist: `/tmp/revenger-r64-skill/SKILL.md`.

- `read` result: `Path '/tmp/revenger-r64-skill/SKILL.md' not found`
- `glob` result for `/tmp/revenger-r64-skill/`: `Path not found: /tmp/revenger-r64-skill`

The later instruction identified the landed checklist at `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md`. It was read there and the runnable checklist commands were executed as recorded below.

## Frozen reference evidence (read only)

`reports/round-64/measure-before.log` records the pre-wave counter results:

- `K_HELD_BACKED=7/14`; `K_HELD_BACKED_STRICT=7/14`
- `K_ROW C07 status=frontier`
- `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`
- `C4_CONTROLS_PASS=2/2`
- `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`
- `HOLD_CALIBRATION=4/4`; `HOLD_REPLAY=10/10`; `HOLDS_OK=yes`; `HOLDS_OK_V2=no`

Initial attempt only: no tool was installed and no checklist commands had yet been run. The checks were executed after the checklist became available; see below. No build, lint, or formatter was run, and no repository state mutation was performed.

## Checklist execution

Checklist source: `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md` (sections 6.1–6.3, lines 284–395). Commands ran in the specified lane-root or `/` working directory. For the verifier census and firmware oracle, a second invocation added only a shell status print because the first tool result showed stdout without an explicit shell exit code; the outputs matched.

### 1. Verifier census

Observed: ten verifier rows in name order, all constituent exits `0`; `CALIBRATION 4 / 4 score= 10.0`; `REPLAY 10 / 10`; wrapper exit `0`. This matches the checklist's ten-verifier, calibration 4/4, replay 10/10 promise.

```text
verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
CALIBRATION 4 / 4 score= 10.0
REPLAY 10 / 10
VERIFIER_CENSUS_EXIT=0
```

### 2. Firmware oracle

Observed five `REGION` lines (two zlib members and three padding spans), final line `ORACLE OK`, exit `0`; this matches the promised outcome.

```text
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
ORACLE OK
FIRMWARE_ORACLE_EXIT=0
```

### 3. Frozen counter

Used committed archive `8c27f1b2018dc5ea284d3dbd2c5ecaa6e86b4661`, extracted with `git archive ... corpus` into `/tmp/revenger-r64-counter-2TnbVB`; ran the frozen counter from `cwd=/` with `TMPDIR` set to that same scratch directory. Counter exit `0`; its final output line was `HOLDS_OK_V2=no` (the wrapper then printed `COUNTER_EXIT=0`). Scratch was removed after the run.

Observed versus the checklist's recorded base values: K and C07 remain `7/14` and `frontier`; strict and ordinary backed counts agree at `7/14`; the legend mismatch remains `1` for C07. C4 attributed kills are `2/2` in this archive, versus the saved red-before base `0/2`. `HOLDS_OK=yes` but `HOLDS_OK_V2=no`; the counter's exit `0` is not evidence that round claims are met. Full relevant output:

```text
K_HELD=7/14 score=5.0
K_ROW C07 status=frontier
K_HELD_BACKED=7/14
K_HELD_BACKED_STRICT=7/14
SAVED_RECORDS=59
ROW_OPS={'C03': ['inspect_managed_artifact'], 'C05': ['inspect_android_package'], 'C07': ['inspect_firmware_regions'], 'C08': ['capture_browser_scenario', 'inspect_web_page', 'observe_web_session']}
README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=no
COUNTER_EXIT=0
```