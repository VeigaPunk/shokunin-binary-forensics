# R64ReviewC4Lang — C4 patch review (verify_icon_languages.py)

Seat: reviewer (independent leaf). Round: 64 (hyaku). Lane:
`/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Reviewed snapshot (working tree, uncommitted): `corpus/verify_icon_languages.py`
sha256 `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3`,
blob `37601cb4e1e1d6f0115b069321db64df0b821949` (base blob `ffb907cb735a0c03725f125100e9d2ca93c92be6`).
Contract base: `666ea84b6be2eec2b0359f556ba2429fc9044c36` (ancestor of HEAD `a3d063f`).
Frozen sources read: `reports/round-64/claims.md`, `reports/round-64/measure.py`,
`reports/round-64/measure-before.log`. No git/jj mutation was run (read-only
`git diff/status/hash-object/rev-parse/merge-base` only); no lane file edited.

## Verdicts

| Point | Verdict | Evidence |
|---|---|---|
| (1) frozen conjunct appears exactly once | **PASS** | line 120, regex count = 1 |
| (2) added control matches frozen shape and placement | **PASS** | lines 152–154, after line 151, inside `check(r)` |
| (3) no other line changed (diff vs `666ea84b`) | **PASS** | `3 0 corpus/verify_icon_languages.py` |
| (4) self-test exit 0 | **PASS** | exit 0, line `PASS: 3/3 group-language states, …` |

Cross-check against the frozen counter (own copy of the current tree,
`TMPDIR` under `/tmp/revenger-r64-c4final-*`, cwd `/`): **counter exit 0**,
`C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`,
`C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`,
`C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`,
`HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`,
`K_HELD_BACKED=7/14`, `K_ROW C07 status=frontier`,
`README_TOKEN_LEGEND_MISMATCH=1`, `HOLDS_OK_V2=no`.

## Point evidence

### (1) Exactly one frozen conjunct — PASS

`corpus/verify_icon_languages.py:118-120`:

```
118: def receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes):
119:     return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
120:             receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))
```

The frozen `C4_CLAUSE = re.compile(r"receipt\['stdout_sha256'\]\s*==\s*H\(raw_bytes\)")`
matches exactly once (`len(findall)=1`, both scripts). The counter's
`mutate_c4` was therefore evaluable — its output shows a real `c4` mutant line,
not `could-not-evaluate`. The added control writes
`forged_stdout['stdout_sha256']` (line 153), a different token that the frozen
regex does not match; the count is not inflated and the mutation target stays
unambiguous.

### (2) Frozen shape and placement — PASS

`corpus/verify_icon_languages.py:148-155`:

```
148:     require(receipt_ok(receipt,command,expected_hash,eid,raw_bytes),f'r{r}: receipt')
149:     forged=copy.deepcopy(receipt)
150:     forged['command']+=' --forged'
151:     require(not receipt_ok(forged,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt command accepted')
152:     forged_stdout=copy.deepcopy(receipt)
153:     forged_stdout['stdout_sha256']=H(b'')
154:     require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
155:     return data,record,decoded
```

- Shape matches claims.md C2 verbatim: deep-copies the receipt (line 152), sets
  `forged['stdout_sha256'] = H(b'')` (line 153), requires rejection with a
  message ending `forged receipt stdout accepted` (line 154).
- The forged-command control survives intact at line 151 and the new control is
  placed after it (line 152 > 151).
- Inside `check(r)` (line 122), which is the only `check` definition and is
  invoked for every `EXPECTED` round via `rows={r:check(r) for r in EXPECTED}`
  (line 158; keys 47, 48, 49). So the control runs in every check round, not
  once globally.
- The copy is independent: `receipt` and `raw_bytes` are untouched; the
  variable is not referenced after line 154; `EXPECTED`/`main()` unchanged.
- The frozen mutation is what makes the control load-bearing: deleting
  ` and receipt['stdout_sha256']==H(raw_bytes)` from line 120 leaves lines
  152–154 rejecting, so the mutant dies with exactly the registered message.

### (3) No other line changed — PASS

`git diff --numstat 666ea84b -- corpus/` → `3 0 corpus/verify_icon_languages.py`,
`3 0 corpus/verify_multi_icon_states.py`; `git diff --name-only` lists only
those two paths. `git diff -U0` for the reviewed file is a single hunk
`@@ -151,0 +152,3 @@` — three pure insertions, no deletion, no reformat. The
red-before receipt is untouched (`git status --porcelain -- reports/round-64/`
is empty). Verifier census still 10 (`ls corpus/verify_*.py | wc -l` = 10);
`HOLD_REPLAY=10/10`.

### (4) Self-test — PASS

`python3 -B corpus/verify_icon_languages.py --self-test` → exit 0, last line:

```
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
```

## Independent attribution reproduction

On a `/tmp` copy of `corpus/`, I re-ran the frozen mutation myself (delete
`\s*and\s+receipt\['stdout_sha256'\]\s*==\s*H\(raw_bytes\)`, first-match) for
both scripts:

```
verify_icon_languages.py   hits_before=1 hits_after=0 exit=1 last=AssertionError: r47: forged receipt stdout accepted  endswith=yes
verify_multi_icon_states.py hits_before=1 hits_after=0 exit=1 last=AssertionError: r42: forged receipt stdout accepted  endswith=yes
```

Both kills are attributed by the registered `endswith` rule, not substring and
not a crash. The frozen counter agrees (`C4_RECEIPT_KILLED_ATTRIBUTED=2/2`,
controls 2/2).

## Finding F1 (resolved, integration hazard) — observed contract-violating intermediate state

Severity: low now (current snapshot passes), but it is a real concurrency
hazard for landing. At 2026-10-24 01:17:08 -0300 the working-tree file was
sha256 `2e9e56e8bd8d55ba56c91c87454c0768a66ac87cbe4ee02943cf1916a26d7d15` and
its diff vs base was **3 insertions, 1 deletion**: the new block had replaced
the forged-command `require(...)` line instead of being added after it
(`forged` / `forged['command']` left as dead code). The self-test still exited 0
in that state, but the frozen counter on that snapshot measured:

```
C2_RECEIPT_B_KILLED=1/2   C2_RECEIPT_B_KILLED_ATTRIBUTED=1/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2   HOLDS_OK=no   counter exit 1
MUTANT verify_icon_languages.py b exit=0 pass
```

i.e. it would have met the C4 target while regressing C2 to 1/2 — a void
condition of this round — and `--self-test` alone would not have caught it.
The state persisted across a 2 s resample and was the state the counter was run
against, so it was not a torn read; it was repaired later, to the reviewed
snapshot `a2fd347e…`. Integration guidance: L1 should gate landing on a fresh
counter run against the final integrated tree (and pin the file sha), not on an
earlier observed PASS of this seat or of a patch seat.

## Residual risk

- Attribution depends on the `AssertionError:` message being the last combined
  output line; measured so on both scripts and both mutant variants. A future
  change that prints after the failing `require` inside `check()` would break
  `endswith` — not currently the case.
- Control efficacy relies on `H(b'') != H(raw_bytes)`; the raw inputs are
  3976–4390 bytes, so the forged value is always wrong. No edge case.
- The new control only proves rejection, not which conjunct rejected: it is
  specifically the stdout conjunct only because `forged_stdout` differs from
  the valid receipt in that field alone and the frozen mutant kills it. Verified
  behaviorally by mutation; no residue.
- `HOLDS_OK_V2=no` on this snapshot is caused solely by
  `README_TOKEN_LEGEND_MISMATCH=1` (C07 still `frontier`). Every other
  `HOLDS_OK_V2` conjunct (controls, d2, attributed b/c3/c4, calibration 4/4,
  replay 10/10, fresh 18/18) is satisfied. This is C1 scope, not a C4 defect.
- The reviewed file is uncommitted working-tree state; commit provenance is L1's
  integration step and was not reviewable here.

## Verification gaps

- **No LSP device in this runtime**: `read xd://lsp` returned
  `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` Caller/definition/
  diagnostics checks were therefore done by direct line-anchored reads plus
  execution (self-test and frozen counter), not by semantic LSP queries. No
  empty-result inference was drawn from any text search.
- I did not independently re-run the eight non-calibration verifiers beyond the
  counter's replay; `HOLD_REPLAY=10/10` covers them.

## Tooling / scratch

No installs or upgrades (no pacman, no uv/npx use). Scratch was lane-owned under
`/tmp/revenger-r64-c4*` and removed after inlining the evidence above; no lane
bytes other than this report were written.

Report: .ufo/waves/round-64/R64ReviewC4Lang.md
