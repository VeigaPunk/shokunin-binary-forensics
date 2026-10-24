# R64C4LangPatch

## Axes
- C4 attribution: reject a receipt whose `stdout_sha256` is forged.
- Scope preservation: change only the assigned verifier behavior; retain `receipt_ok` and all existing checks.

## Files changed
- `corpus/verify_icon_languages.py` — in `check(r)`, preserved the existing forged-command control and added the stdout-digest forgery control immediately after it. It runs for each `r` in `EXPECTED` (47, 48, 49); `receipt_ok` is unchanged.

Exact added diff:
```diff
+    forged_stdout=copy.deepcopy(receipt)
+    forged_stdout['stdout_sha256']=H(b'')
+    require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
```

## Retained evidence
Ran the assigned command:
`cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/verify_icon_languages.py --self-test`

It exited successfully and printed exactly:
```text
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
```

## Risks and blockers
- No additional checks were run; the parent owns post-integration verification.
- A peer reported a working-tree counter result (C2 raw kills 2/2, C4 attributed 2/2); I did not run it. This is not committed-archive evidence and does not establish C2 attributed 2/2; L1 owns that verification.
- No tools for LSP symbol operations are exposed in this session; this was a literal in-function insertion and no symbol refactor was needed.
- No tools were installed or updated.
