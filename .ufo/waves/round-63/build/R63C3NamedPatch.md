# R63 C3 named-receipt patch

## Files changed
- `corpus/verify_named_multi_icon_states.py`
- `.ufo/waves/round-63/build/R63C3NamedPatch.md` (this report)

## Behavior
Moved the complete existing receipt predicate into `receipt_ok(receipt, command, digest, eid, raw)`, preserving its conjunct text and order, including `receipt['command']==command`. `check()` now deep-copies the receipt, appends ` --forged` to the copied command, and requires `receipt_ok` to reject it with `r{r}: forged receipt accepted`. The saved-input assertions, EXPECT table, and PASS print statement were not changed. The probe-clause search found exactly one `receipt['command']==command` occurrence in the verifier.

## Verification transcripts
Control run, from `/home/vgpnk/Projects/shokunin/revenger-shokunin`:
```text
$ python3 -B corpus/verify_named_multi_icon_states.py --self-test
PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
EXIT=0
```
Exit status: 0.

Frozen mutant run, from `/tmp/revenger-r63-c3namedpatch.T31NlC`. In the copied corpus verifier, removed exactly `receipt['command']==command and ` from the helper predicate; no lane source was mutated for this run:
```text
$ python3 -B corpus/verify_named_multi_icon_states.py --self-test
Traceback (most recent call last):
  File "/tmp/revenger-r63-c3namedpatch.T31NlC/corpus/verify_named_multi_icon_states.py", line 106, in <module>
    if __name__=='__main__': main()
                             ~~~~^^
  File "/tmp/revenger-r63-c3namedpatch.T31NlC/corpus/verify_named_multi_icon_states.py", line 84, in main
    rows={r:check(r) for r in EXPECT}; base=rows[55][0]
            ~~~~~^^^
  File "/tmp/revenger-r63-c3namedpatch.T31NlC/corpus/verify_named_multi_icon_states.py", line 78, in check
    req(not receipt_ok(forged, command, digest, eid, raw), f'r{r}: forged receipt accepted')
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/revenger-r63-c3namedpatch.T31NlC/corpus/verify_named_multi_icon_states.py", line 14, in req
    if not ok: raise AssertionError(msg)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: r55: forged receipt accepted
EXIT_STATUS=1
```
The mutant process exited 1; its final application-output line contains `forged receipt`, attributing the kill to the in-script control.

## Risks / blockers
None observed. No tools were installed or updated.
