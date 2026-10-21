# ExecReceiptControlLang — round 61 C2 (receipt-command kill), verify_icon_languages.py

Seat: CloseChousa26.ExecReceiptControlLang-10 (executor, WRITER+RUNS). Subagents spawned: none.
Base: e0a4b0c4348ef1fade46539f520e94fa140c4d8a (observed clone HEAD; `git status` clean before edit).
Clone: /tmp/revenger-r61-ExecReceiptControlLang, branch r61-ExecReceiptControlLang.
Probe tree: /tmp/revenger-r61-ExecReceiptControlLang-tree (`cp -a` of clone corpus/, includes the edit).
Toolchain: Python 3.14.8 (`python3 --version`). Installs/updates: none.

## Change (only file touched: corpus/verify_icon_languages.py; 12 insertions, 3 deletions)
- L118 `def check(r,receipt=None):` takes an optional in-memory receipt; L126-127 loads the saved `live/runs/round-{r}/producer-receipt.json` only when none is given.
- L144-146 keeps the one conjunct `receipt['command']==f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'`, text unchanged, `and`-chained so mutant b is evaluable.
- L157-164 in-memory control: copy of the saved r48 receipt with `command` + ` --forged` (dict only, never written). `check(48,forged_receipt)` must raise with message exactly `r48: receipt`; acceptance raises `forged receipt command accepted` (exit 1); any other rejection reason exits 1.
- L170 PASS text also reports `forged receipt command REJECTED`.
- `git diff e0a4b0c4348ef1fade46539f520e94fa140c4d8a -- corpus/live corpus/fixtures` = 0 bytes. `git status --short` = ` M corpus/verify_icon_languages.py` only.

## Probe
$ cd /tmp/revenger-r61-ExecReceiptControlLang && python3 -B reports/round-61/measure.py /tmp/revenger-r61-ExecReceiptControlLang-tree; echo measure_exit=$?
```
== python: Python 3.14.8
K_HELD=4/14 score=2.9
K_ROW C04 status=uncovered
K_ROW C09 status=uncovered
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED, forged receipt command REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=1/2
C2_D2_KILLED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED, forged receipt command REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
measure_exit=0
```

## Findings (this file)
- Mutant b (conjunct and its `and` deleted): exit 1, last line `AssertionError: forged receipt command accepted`. The mutant parses and reaches the control, so the kill is not a syntax failure. Killed: 1/1 for this file.
- Control: exit 0 with the PASS line. d2 (saved r47 receipt command forged): exit 1, `AssertionError: r47: receipt`.
- `C2_RECEIPT_B_KILLED=1/2` is the two-file aggregate; the 1 is this file. `verify_multi_icon_states.py` is unchanged in this clone and its b survives (exit 0), as expected for this item.
- Holds: C2_CONTROLS_PASS=2/2, C2_D2_KILLED=2/2, HOLD_CALIBRATION=4/4, HOLD_REPLAY=10/10; no could-not-evaluate line, so exactly one receipt-command conjunct matched.
- The kill is specific: the forged receipt differs from the saved r48 receipt only in `command`, so with the conjunct deleted nothing else rejects it.

## Files written (clone)
- corpus/verify_icon_languages.py  sha256 51a7f56c382f14be787c8c2ae7fdfc24f5917e26611def027a1b0834a21b7af1  (175 lines; base file content sha256 at e0a4b0c, from `git show e0a4b0c:corpus/verify_icon_languages.py | sha256sum`: ed0ad16655e3e3c8989c80fb92c0fc35bf35dbb7dd1007f2b9d4be1d84c6bd95)
- r61-ExecReceiptControlLang.patch  sha256 1fc73e311d9e55d8093cf7cddf3255a51d210277dc7a0273d87d0404c5cdd622  (45 lines)
  Patch path: /tmp/revenger-r61-ExecReceiptControlLang/r61-ExecReceiptControlLang.patch, made with `git -C /tmp/revenger-r61-ExecReceiptControlLang diff e0a4b0c4348ef1fade46539f520e94fa140c4d8a > /tmp/revenger-r61-ExecReceiptControlLang/r61-ExecReceiptControlLang.patch`
- Scratch only, not in patch: /tmp/revenger-r61-ExecReceiptControlLang-tree
- Live lane: this report file only.

## Not done
- verify_multi_icon_states.py (different item; its control is needed for C2_RECEIPT_B_KILLED=2/2).
- No REA, no bytecode execution, no network, no lint/format/build. Live-lane corpus/live, corpus/fixtures, MANIFEST.json, .ufo/state, .ufo/watchdog.log untouched.

VERDICT: verify_icon_languages.py C2 done in clone: b killed, control/d2/holds pass, patch 1fc73e31; aggregate stays 1/2 until verify_multi_icon_states.py gets the same control.
