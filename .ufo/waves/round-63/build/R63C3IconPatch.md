# R63 C3 icon receipt fix

Axes: receipt-identity correctness; regression safety; scoped maintainability.

## Change

Changed only `corpus/verify_icon_states.py`. Moved the saved-receipt exit-code, fixture-SHA, stdout-SHA, and evidence-ID checks into `receipt_ok(receipt, expected_hash, evidence_id, raw_bytes, round_id)`. The byte-preserved fixture-SHA conjunct appears once, and the `if round_id != 36` evidence exemption remains unchanged. `check_saved()` deep-copies each receipt, forges `fixture_sha256` to `'0'*64`, and rejects acceptance with an `AssertionError` message containing `forged receipt`. The existing candidate-forgery control and other assertions were left unchanged.

The frozen receipt-identity regex matched exactly once in the final target (`corpus/verify_icon_states.py:120`).

## Verification transcripts

Lane-root self-test (exit 0):

```text
$ python3 -B corpus/verify_icon_states.py --self-test
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
```

Frozen mutant in `/tmp/revenger-r63-icon-mutant.kk71cb/corpus/verify_icon_states.py`: removed exactly ` and receipt['fixture_sha256'] == expected_hash`; mutant process exit 1. The shell wrapper recorded the exit status after the process output:

```text
$ python3 -B verify_icon_states.py --self-test; status=$?; printf 'EXIT=%s\\n' "$status"; test "$status" -ne 0
Traceback (most recent call last):
  File "/tmp/revenger-r63-icon-mutant.kk71cb/corpus/verify_icon_states.py", line 181, in <module>
    main()
    ~~~~^^
  File "/tmp/revenger-r63-icon-mutant.kk71cb/corpus/verify_icon_states.py", line 162, in main
    rows = {r: check_saved(r) for r in EXPECTED}
               ~~~~~~~~~~~^^^
  File "/tmp/revenger-r63-icon-mutant.kk71cb/corpus/verify_icon_states.py", line 158, in check_saved
    raise AssertionError(f'r{round_id}: forged receipt accepted')
AssertionError: r36: forged receipt accepted
EXIT=1
```

The mutant's final process-output line was `AssertionError: r36: forged receipt accepted`.

## Notes

No tools were installed or updated. LSP was unavailable in the exposed seat tool interface; no LSP operation could be issued. No other risks or blockers identified.
