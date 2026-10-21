# ExecReceiptControlMulti — round 61 C2 (corpus/verify_multi_icon_states.py)

Seat CloseChousa26.ExecReceiptControlMulti-10 (executor; writer+runs in private clone). Base observed e0a4b0c4348ef1fade46539f520e94fa140c4d8a (clone HEAD; `git status` clean before edit). Clone /tmp/revenger-r61-ExecReceiptControlMulti, branch r61-ExecReceiptControlMulti. Labrat probes: 0. Installs: none.

## 1. Change (one file, uncommitted)
`corpus/verify_multi_icon_states.py`: `git diff --stat` → 1 file, 13 insertions(+), 2 deletions(-).
- L121 `def check(round_id, receipt=None):`; L127-128 read the saved producer receipt only when none is passed. Grep of the clone for importers of this module: no matches.
- L144 clause unchanged: `require(receipt['command']==command and ...`. Grep: exactly one `receipt['command']==` match in the file.
- main() L156-165 (new): for each round in EXPECTED, load the saved receipt, forge `command` in memory (`forged_receipt['command'] += ' --forged'`), run `check(r, forged_receipt)`. Must raise `r{r}: receipt`; if accepted, raises `r{r}: forged receipt command accepted` (exit 1).
- No printed output added: saved records quote the PASS line verbatim (`corpus/live/runs/round-46/verifier-receipt.json:4`, `reviewer.md:14`).

## 2. Checks run
- Real run, cwd=/tmp: `python3 -B <clone>/corpus/verify_multi_icon_states.py --self-test` → `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED`, `real_run_exit=0`.
- Saved records: `git diff --stat e0a4b0c4…` lists only the verifier; `git diff e0a4b0c4… -- corpus/live corpus/fixtures | wc -l` → `0`.
- Probe file identical in lane and clone: sha256 7879ec49284923e6fbd67fd6209bbfc2821777c73ebd13c57304901fab919c05 (both).
- Probe tree: `cp -a <clone>/corpus /tmp/revenger-r61-ExecReceiptControlMulti-tree/`; `cmp` of the verifier identical.

## 3. Probe output, full
Command: `python3 -B /tmp/revenger-r61-ExecReceiptControlMulti/reports/round-61/measure.py /tmp/revenger-r61-ExecReceiptControlMulti-tree` (cwd=/tmp)
```text
K_HELD=4/14 score=2.9
K_ROW C04 status=uncovered
K_ROW C09 status=uncovered
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=1/2
C2_D2_KILLED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
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
probe_exit=0
```

## 4. Reading
- Before (reports/round-61/measure-before.log:9,12): multi `b` exit=0 (survived); C2_RECEIPT_B_KILLED=0/2.
- After (this clone): multi `b` killed (exit=1, `AssertionError: r42: forged receipt command accepted`); CONTROLS 2/2; D2 2/2; HOLD_CALIBRATION 4/4; HOLD_REPLAY 10/10; probe_exit 0; saved-record diff empty.
- C2_RECEIPT_B_KILLED=1/2 here by scope: verify_icon_languages.py is unchanged in this clone (its `b` still exit=0). The predicted 2/2 needs the sibling icon_languages patch in the same tree; not tested here.
- K_HELD=4/14 unchanged (knowledge map is C1, outside this item).

## 5. Patch and files written
Patch: /tmp/revenger-r61-ExecReceiptControlMulti/r61-ExecReceiptControlMulti.patch (38 lines; `git -C <clone> diff e0a4b0c4…`), sha256 b5f4619b49501022031d3976db13f589efce4ed94f2b2531cbff1fa78b767142
- /tmp/revenger-r61-ExecReceiptControlMulti/corpus/verify_multi_icon_states.py, sha256 79fbd2a4ee9d09063123bbf91a84a7167924b388048aa3e8ea12df29878dfd93 (edited, uncommitted)
- /tmp/revenger-r61-ExecReceiptControlMulti/r61-ExecReceiptControlMulti.patch (above)
- /tmp/revenger-r61-ExecReceiptControlMulti-tree/corpus/ (probe scratch copy; not part of the change)
- /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-61/build/ExecReceiptControlMulti.md (this report; the only lane write)

## 6. Notes for integration
- The control covers all four rounds (42-45); each forged copy must fail with its own `r{r}: receipt`, so an unrelated failure cannot mask the kill.
- D2 stays killed by the saved-receipt path (`r42: receipt`), independent of the new control.
- After merging both C2 patches, the integrator should re-run the probe (expect C2_RECEIPT_B_KILLED=2/2, holds unchanged) and `git diff e0a4b0c4… -- corpus/live corpus/fixtures` (expect empty).

VERDICT: multi-file C2 done — mutant b now killed (exit 1); controls, D2, HOLD_CALIBRATION and HOLD_REPLAY intact; saved records untouched; combined C2_RECEIPT_B_KILLED=2/2 awaits the sibling verify_icon_languages.py patch.
Installs: none.
