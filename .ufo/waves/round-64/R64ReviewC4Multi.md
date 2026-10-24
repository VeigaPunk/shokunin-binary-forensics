# R64ReviewC4Multi — C4 patch review: `corpus/verify_multi_icon_states.py`

Verdict on the assigned file: **PASS** (all four required points). Snapshot reviewed:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_multi_icon_states.py`,
175 lines, sha256 `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e`.

A C2-wide regression found in `corpus/verify_icon_languages.py` mid-review (the existing
forged-command assertion had been deleted) was corrected by that file's owner before this
report closed; the current working tree passes the frozen counter with exit 0. Both states
are recorded below so integration does not inherit the broken snapshot.

## Required points

### 1. Frozen conjunct appears exactly once — PASS

- `receipt_ok` is at `corpus/verify_multi_icon_states.py:121-123`; the frozen conjunct
  `receipt['stdout_sha256']==H(raw_bytes)` is line 123 and is its only occurrence in the file.
- The counter's frozen mutation regex (`reports/round-64/measure.py:212`) matches exactly 1
  hit in both the patched file and base `666ea84b`, so `mutate_c4`
  (`measure.py:216-224`) evaluates rather than returning `could-not-evaluate`.
- The diff adds no second copy of the conjunct: the only other `stdout_sha256` line is the
  forged-control assignment at line 152.

### 2. Control shape and placement — PASS

- Inserted at lines 151-153, inside `check(round_id)` (`:125-154`), immediately **after** the
  existing forged-command control (`:148-150`) and **before** `return` (`:154`) — exactly the
  frozen placement at `reports/round-64/claims.md:70-71`.
- Shape matches claims.md:70-76 verbatim: `forged_stdout = copy.deepcopy(receipt)` (line 151),
  `forged_stdout['stdout_sha256'] = H(b'')` (line 152), rejection require with message
  `f'r{round_id}: forged receipt stdout accepted'` (line 153), which ends with the registered
  attribution phrase used by `measure.py:247` (`last.endswith("forged receipt stdout accepted")`).
- Non-vacuous: `H(b'')` = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`,
  while the four receipts 42-45 store `7163c758…4b9c`, `d84d8db6…8d49`, `2a14dc2a…2e19`,
  `20fd361d…1ec7` respectively — all differ, so the control can fail.
- Covers rounds 42-45: `main()` at `:157` runs `check(r)` for every key of `EXPECTED`
  (`:106-119` = 42,43,44,45). Because the self-test passes, all four executions clear the new
  require; a mutation of the conjunct breaks at the first one (r42, EXPECTED insertion order).

### 3. Diff vs base `666ea84b` shows only added lines — PASS

`git diff --numstat 666ea84b -- corpus/verify_multi_icon_states.py` → `3 0`. One hunk,
`@@ -148,6 +148,9 @@`, three added lines and zero deletions; `receipt_ok`, every saved-input
assertion and the forged-command control are byte-unchanged. `git diff --stat 666ea84b HEAD --
corpus/verify_multi_icon_states.py` is empty, so no committed intermediate change exists.

### 4. Self-test exit 0 — PASS

Both invocations on the working tree exit 0:
`python3 -B corpus/verify_multi_icon_states.py` and the counter's exact invocation
`python3 -B corpus/verify_multi_icon_states.py --self-test` (`measure.py:109-114`), printing
`PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED`.
The frozen counter's own control variant on a scratch copy also reports
`MUTANT verify_multi_icon_states.py control exit=0 pass`.

## Independent mutation reproduction (assigned file)

Scratch copy under `/tmp/revenger-r64-review-c4multi` (lane-owned prefix), corpus copied,
then the counter's exact frozen regex deletion applied to `receipt_ok` (leaving
`command and exit_code and fixture_sha256 and evidence_id`):

- control (unmutated copy): exit 0, PASS line above;
- mutant: exit 1, final line exactly `AssertionError: r42: forged receipt stdout accepted`,
  `endswith('forged receipt stdout accepted') == True` → **attributed kill**.

So the assigned file satisfies C2's mechanism on its own.

## In-wave finding — sibling file regression, now corrected

While the wave was live, `corpus/verify_icon_languages.py` carried numstat `3 1`: base line 151
`require(not receipt_ok(forged,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt command accepted')`
was deleted and `forged['command']+=' --forged'` was left with no consumer — the new
`forged_stdout` block had replaced the command control rather than following it. That
contradicts `reports/round-64/claims.md:78-80` ("Unchanged scripts otherwise … the existing
forged-command controls stay") and `claims.md:70`. Frozen counter on that snapshot:

```
MUTANT verify_icon_languages.py b exit=0 pass :: PASS: ... forged selection REJECTED
C2_RECEIPT_B_KILLED=1/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=1/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLDS_OK=no
HOLDS_OK_V2=no
COUNTER_EXIT=1
```

(red-before: lang `b` killed 2/2; exit-1 hits the void condition at `claims.md:120`).
After I reported it, the owner restored the command assertion. Current bytes:
numstat `3 0`, sha256 `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3`,
control at lines 150-154 in order `forged --forged` → require command → `forged_stdout` →
require stdout. Re-run of the unmodified counter on the current working-tree copy:

```
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
FRESH_ROWS=18/18
K_HELD=7/14   K_ROW C07 status=frontier   K_HELD_BACKED=7/14   K_HELD_BACKED_STRICT=7/14
README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']
HOLDS_OK=yes
HOLDS_OK_V2=no
COUNTER_EXIT=0
```

`HOLDS_OK_V2=no` is the expected pre-C1 state only (`.ufo/waves/round-64/` README token still
`frontier`; `holds_ok_v2` at `measure.py:268-271` requires `len(mismatch)==0`), not a C4 defect.
C2 end-state 2/2 and C4 2/2 both hold on current bytes; `holds_ok` (`measure.py:264-266`) is
`yes` and exit (`:273`) is 0.

## Residual risk

- **Patch is uncommitted** (lane status `M corpus/verify_multi_icon_states.py` and
  `M corpus/verify_icon_languages.py`). The frozen counter measures a committed `git archive`
  tree; if L1 integrates without committing, every C2/C4 label stays at red-before and this
  PASS does not transfer.
- The lang regression was transient and is fixed in current bytes, but the same replacement
  mistake can recur if that file is touched again; the guard is the frozen `b` mutant showing
  `exit=1 killed :: ... forged receipt command accepted`, which must stay in the final receipt.
- Attribution depends on Python emitting the assertion message as the final output line.
  Verified on Python 3.14.8; the counter also guards with `endswith`, so a wrapped or prefixed
  message would simply not count (fail-closed, not a false pass).
- The control runs four times; only the first failure is attributed (r42). This satisfies the
  per-script criterion, and since the unmutated self-test passes, all four rounds reach the
  control.
- `README_TOKEN_LEGEND_MISMATCH=1` in this run reflects the pre-flip working tree; C1's
  admission/flip is another seat's scope.

## Verification gaps

- No committed-archive counter run (no commit exists in this wave; L1 owns integration). Both
  runs above used frozen `reports/round-64/measure.py` unchanged against a byte copy of the
  working-tree corpus, cwd `/`, `TMPDIR` under lane scratch.
- C1/README flip and non-C2 criteria are outside this seat.
- Not run: other verifiers' semantics, live/fixtures byte preservation (other seats).

## Bounds and tooling

Read-only on the lane; writes were this report and peer messages. Scratch stayed under
`/tmp/revenger-r64-review-c4multi` and was removed after the runs. No git/jj mutations, no
commits, no installs or upgrades (no tool installation performed).

Report: .ufo/waves/round-64/R64ReviewC4Multi.md
