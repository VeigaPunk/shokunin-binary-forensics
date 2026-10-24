# R64SimplifierDrift — minimality review of the two C4 patches (2026-10-24)

Verdict: **PASS — both C4 patches are minimal.** 6 insertions, 0 deletions total; no non-minimal hunk at final state.

## Diff line count and purity

`git diff 666ea84b -- corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py` (final state):

- `--numstat`: `3 0 corpus/verify_icon_languages.py`, `3 0 corpus/verify_multi_icon_states.py` — **6 insertions(+), 0 deletions(-)**.
- verify_icon_languages.py `check()` — added at lines 152-154, immediately after the existing forged-command control (lines 149-151):
  ```python
  forged_stdout=copy.deepcopy(receipt)
  forged_stdout['stdout_sha256']=H(b'')
  require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
  ```
- verify_multi_icon_states.py `check(round_id)` — added at lines 151-153, immediately after the existing forged-command control (lines 148-150): same three lines in that file's spaced style.
- No refactors, no moved code, no whitespace churn: each file's added lines match its own local convention (icon file compact `x=y`, multi file spaced `x = y`), and nothing else in either hunk changed.

## Frozen conjunct byte-identity to base

- `receipt['stdout_sha256']==H(raw_bytes)` occurs **exactly once** per file (verify_icon_languages.py:120, verify_multi_icon_states.py:123).
- sha256 of the `receipt_ok` region (base `git show 666ea84b` lines 117-121 / 120-124 vs working tree same ranges): all four digests identical — `396f45c786bb599e16d37202ee803c1eaa4820837489ed14b2e98aff89383ecc`. **Byte-identical to base.**

## Minimality of the added lines

- 3 added lines per file = exactly the frozen fix shape in reports/round-64/claims.md (C2): deep-copy the receipt, set `forged['stdout_sha256'] = H(b'')`, require rejection with a message ending `forged receipt stdout accepted`. No smaller shape is compatible with the frozen shape: a 2-line variant reusing the existing `forged` object would overwrite/edit existing control lines (forbidden — "existing forged-command controls stay") and would deviate from the registered deep-copy-of-the-pristine-receipt form.
- Placement inside `check()` after the forged-command control gives one control per round (icon r47-49, multi r42-45), matching the owning briefs (R64C4LangPatch / R64C4MultiPatch) verbatim.
- Attribution is exact: both kill messages end `forged receipt stdout accepted`, matching the registered `last.endswith(...)` attribution in the frozen counter.

## End-state proof (frozen counter on the working tree)

`python3 -B reports/round-64/measure.py <lane>` (all mutant runs on temp copytrees; read-only against the repo):

- `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2` (red-before: 0/2) — kills at `r47: forged receipt stdout accepted` and `r42: forged receipt stdout accepted`.
- No harm: `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` (`r47`/`r42: forged receipt command accepted` intact), `C2_D2_KILLED=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, probe exit 0. K rows and `README_TOKEN_LEGEND_MISMATCH=1` unchanged (C1 landing pending — outside this seat's scope; `HOLDS_OK_V2=no` for the same pending reason).

## Non-minimal hunk / process finding (no action required, FYI landing checks)

Mid-flight transient observed: at my first read, verify_icon_languages.py briefly had the existing `require(...,'r{r}: forged receipt command accepted')` line **replaced** by the new control (diff showed `1 deletions(+)`); the owning seat restored it within minutes and the final state is a pure 3-line addition. Had it persisted, mutant b's killer line would have been gone (`C2_RECEIPT_B_KILLED` would regress below 2/2). Flag for R64SnapshotManifest: hash these two files only at final state, and for L1: the landing-time tamper check should re-run this same diff expecting exactly 6 insertions / 0 deletions.

## Scope and hygiene

- Wrote only `.ufo/waves/round-64/R64SimplifierDrift.md`; no git/jj mutations; no edits to corpus files (findings routed via this report); scratch `/tmp/revenger-r64-simplifier` removed. No tool installs performed (pacman untouched).
