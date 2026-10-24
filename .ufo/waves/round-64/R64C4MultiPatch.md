# R64C4MultiPatch report

## Files changed
- `corpus/verify_multi_icon_states.py` — inserted the frozen stdout-forgery control immediately after the existing forged-command control; `receipt_ok` and all other lines were left unchanged.

## Behavior
The control deep-copies the valid receipt, changes `stdout_sha256` to `H(b'')`, and requires `receipt_ok(...)` to reject it with the prescribed attribution message.

## Exact diff
```diff
     forged = copy.deepcopy(receipt)
     forged['command'] += ' --forged'
     require(not receipt_ok(forged, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt command accepted')
+    forged_stdout = copy.deepcopy(receipt)
+    forged_stdout['stdout_sha256'] = H(b'')
+    require(not receipt_ok(forged_stdout, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt stdout accepted')
     return data, report, decoded, state
```

## Retained evidence
- Post-edit source read and targeted search showed the existing forged-command assertion at line 150, the new three-line control at lines 151–153, and `return` at line 154.
- The requested `python3 -B corpus/verify_multi_icon_states.py --self-test` was **not run**: the fleet executor policy prohibits tests while the editing wave is in flight; the parent owns post-integration verification. Therefore there is no observed self-test output or exit status to report.
- No tools were installed or updated.

## Risks and blockers
- Self-test outcome remains unverified pending the parent-owned post-integration gate.
