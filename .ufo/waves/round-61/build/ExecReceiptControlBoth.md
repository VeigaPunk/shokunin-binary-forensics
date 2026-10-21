# ExecReceiptControlBoth - round 61, C2 competing design (both verifiers)

Seat CloseChousa26.ExecReceiptControlBoth-10 (executor, leaf; no subagents). Scope: C2 only; C1 (C04/C09) and sources untouched.
Base e0a4b0c4348ef1fade46539f520e94fa140c4d8a. `git diff --stat cf02419 e0a4b0c -- corpus` printed nothing, so `measure-before.log` applies unchanged.
Clone /tmp/revenger-r61-ExecReceiptControlBoth (branch r61-ExecReceiptControlBoth, uncommitted). Axes: kill power, holds, saved-record integrity, churn, kill-message diagnosability.

## Design: one predicate, one control pattern in both files
- `receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes)`: identical text in both scripts, returns bool. The only `receipt['command']==command` conjunct lives there.
- verify_icon_languages.py:118-120 helper; :147-151 in `check`: saved `require(receipt_ok(...))` at :148; in-memory `copy.deepcopy` + `['command']+=' --forged'` at :149-150; `require(not receipt_ok(forged,...))` at :151.
- verify_multi_icon_states.py:121-123 helper; :146-150 same pattern.
- PASS print lines unchanged. Saved records quote them verbatim: corpus/live/runs/round-46/{LEDGER.md:4,reviewer.md:14,verifier-receipt.json:4} and round-50/{LEDGER.md:4,reviewer.md:9,verifier-receipt.json:4}.

## Probe on /tmp copy (after): `python3 -B reports/round-61/measure.py /tmp/revenger-r61-ExecReceiptControlBoth-after`
```
K_HELD=4/14 score=2.9
K_ROW C04 status=uncovered
K_ROW C09 status=uncovered
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
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
```
Same probe on the pre-change /tmp copy (`-base`) reproduces the C2 and HOLD values of measure-before.log (lines 11-25): C2_RECEIPT_B_KILLED=0/2, C2_CONTROLS_PASS=2/2, C2_D2_KILLED=2/2, HOLD_CALIBRATION=4/4, HOLD_REPLAY=10/10, K_HELD=4/14. No non-zero probe exit was reported by the shell.

## Diff size
- Competing (delivered): `git diff --numstat e0a4b0c` gives icon +9/-3, multi +8/-2; total +17/-5 (churn 22).
- Per-file comparison (scratch only, `-perfile`): `check(r, forged=None)` plus a main() control that re-reads the saved receipt, re-runs the whole check on a forged copy, and hard-codes round 48/45. Icon +10/-2, multi +10/-2; total +20/-4 (churn 24). Probe: b killed 2/2, but the kill line is bare `AssertionError: forged receipt command accepted`; holds identical.

## Simpler than per-file? Only marginally.
- Simpler: one predicate serves saved and forged input; no second file read; no hard-coded round; the kill names the round; the forged verdict depends only on `receipt_ok`, while the per-file control accepts any AssertionError from the whole check.
- Not materially: churn 22 vs 24. The one-conjunct rule (exactly one `receipt['command']==` match, probe CLAUSE regex) forbids duplicating the expression, so any in-memory forged control needs a predicate (this design) or a re-entrant check (per-file). Each costs about 20 lines.
- Considered, not built: a loop over (saved, forged) pairs. The probe regex requires the literal name `receipt`, so the loop variable would shadow the saved receipt. Rejected on readability.

## Integrity
- `git diff --quiet e0a4b0c -- corpus/live corpus/fixtures` -> exit 0 (LIVE_AND_FIXTURES_DIFF_EMPTY).
- `grep receipt\['command'\]==` -> one match per file (icon :119, multi :122).
- Mutant b dies on the new control, not a SyntaxError: last lines `r47: forged receipt command accepted` and `r42: forged receipt command accepted`.
- Not run: kaika mutants a/c/d1/d3 (not in probe); no builds or lint; no REA or producer calls.
- Residual: deleting the forged-control `require(not ...)` line itself is not measured; no kaika mutant or probe site covers it.

## Files written
- clone corpus/verify_icon_languages.py sha256 0f781c6a216bfdaa9cc1ab9b9fe8ae3ab9cb8a79d00ed56c4f94282c80a8efbd
- clone corpus/verify_multi_icon_states.py sha256 0179e93f8bec17d5f4b60047f167ad26aa803a84440e98329fd8a8f2ea7a176d
- patch /tmp/revenger-r61-ExecReceiptControlBoth/r61-ExecReceiptControlBoth.patch sha256 0c21e899f333294962a8892f3ac73d26676119c0b8036745881061dc65922cbb (`git -C <clone> diff e0a4b0c4348ef1fade46539f520e94fa140c4d8a`)
- scratch, not delivered: /tmp/revenger-r61-ExecReceiptControlBoth-{base,after,perfile}/corpus
- this report (lane path, own file only)

Installs: none (git, python3, sha256sum, cp, tar were already present; no pacman, uv or npm).
VERDICT: competing C2 design kills mutant b in both scripts (0/2 -> 2/2) with holds and saved bytes intact; churn +17/-5 vs per-file +20/-4, so only marginally simpler.
