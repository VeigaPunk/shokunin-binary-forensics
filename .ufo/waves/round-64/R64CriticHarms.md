# R64CriticHarms — frozen-harms precheck

Seat: `revenger-r64.R64CriticHarms`. Review only; no production edits, admission, integration, git/jj mutations, or other runtime invocation. No tools installed.

## Axes and evidence scope

Axes checked: coverage K/F; calibration; operability/replay; freshness byte-survival; preservation of the existing quality/depth evidence. No adjacency move is assessed.

This is an in-wave **precheck**, not a final committed-tree receipt or canonical judgment. At `2026-10-24T04:17:38.164822+00:00`, I copied the working-tree `corpus/` to an isolated scratch tree and extracted the claim-base `666ea84b6be2eec2b0359f556ba2429fc9044c36` `corpus/` with read-only `git archive`. All counter variants ran on the copied tree, not the live working tree. Scratch was lane/round-owned and removed after evidence capture. Later production corrections are not tested by this report.

Frozen probe used: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py`, SHA-256 `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`.

## Strongest counterexample: C4 improves while an existing C2 guard disappears

**FAIL — fixable regression, not an admissible trade.** The snapshot reaches `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, but `C2_RECEIPT_B_KILLED_ATTRIBUTED` drops from the frozen red-before `2/2` to `1/2`. The languages command mutant survives with exit 0. All ten ordinary replay self-tests still pass, showing why ordinary green replay does not establish no harm.

Local cause: `corpus/verify_icon_languages.py` snapshot lines 149–153 creates the forged command receipt but no longer asserts its rejection. Claim-base line 151 contained this assertion:

```python
require(not receipt_ok(forged,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt command accepted')
```

The actual snapshot diff replaces that line with the new stdout control instead of retaining it and appending the control:

```diff
     forged=copy.deepcopy(receipt)
     forged['command']+=' --forged'
-    require(not receipt_ok(forged,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt command accepted')
+    forged_stdout=copy.deepcopy(receipt)
+    forged_stdout['stdout_sha256']=H(b'')
+    require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
```

Smallest safe correction: restore the one original `require` immediately after the forged-command mutation and before the separate stdout control. Keep both controls; do not weaken the frozen counter, attribution suffix, or holds. This violates the explicit existing-control preservation requirement in `claims.md:78–80` and the C2/probe-exit void conditions in `claims.md:119–120` until corrected. L1 and `R64C4LangPatch` were notified. I made no correction and did not rerun after notifying them.

Snapshot script SHA-256 values:

- languages: `2e9e56e8bd8d55ba56c91c87454c0768a66ac87cbe4ee02943cf1916a26d7d15`
- multi-icon: `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e`

## Per-condition results

PASS/FAIL below refers only to each exercised precheck, not to claim admission.

| Frozen condition / requested check | Result | Observed evidence |
|---|---|---|
| Preservation manifest exists and covers both `corpus/live` and `corpus/fixtures` | PASS | `.ufo/waves/round-64/preservation-base.sha256` appeared during the review; 452 lines and 452 unique paths, exactly the claim-base/live snapshot path set. No missing, extra, or mismatched base digests. |
| No changed existing live/fixture byte outside new round-64 paths | PASS | Base and snapshot: 351 live files + 101 fixture files = 452; zero changed, missing, or added files. `sha256sum --check --quiet` against the production tree exited 0. |
| No lost baseline held row | PASS | The same seven held row IDs remain: C01, C04, C06, C09, C11, C12, C13. |
| README status/change scope limited to C07 | PASS | Read-only diff against the claim base is empty for README; comparison after removing C07 is identical. No premature flip observed. |
| Denominators stay 14 rows / 8 families | PASS | Snapshot has exactly 14 C rows; frozen probe prints K `7/14` and F `5/8`. |
| Q01–Q13 not weakened / QUALITY untouched | PASS | Whole-file byte equality to claim base, with all 13 IDs present. SHA-256 `811ebf73179a86e0adff18874d0abf2d22e5161ac73c6a04ab3cf21fb51c45d1`. |
| C2 attributed command kills at least 2/2 | **FAIL** | `C2_RECEIPT_B_KILLED_ATTRIBUTED=1/2`; languages command mutant exits 0. |
| C2 d2 kills at least 2/2 | PASS | `C2_D2_KILLED=2/2`. |
| C3 attributed kills at least 2/2 | PASS | `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`. |
| C4 attributed kills at least 2/2 after patch | PASS | `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, both ending in the registered stdout assertion. |
| HOLD_CALIBRATION at least 4/4 | PASS | `HOLD_CALIBRATION=4/4`. |
| HOLD_REPLAY at least 10/10, ten scripts retained | PASS | Exactly ten `HOLD` lines, all exit 0; `HOLD_REPLAY=10/10`. |
| Probe exit 0 | **FAIL** | Exercised frozen probe exits **1**; `HOLDS_OK=no`, `HOLDS_OK_V2=no`. |
| Prior rejected candidates, historical counterexamples and lessons remain byte-preserved | PASS | All 11 baseline knowledge files and all 10 baseline lesson files are unchanged, with none missing. Read-only Git diff is also empty for `reports/round-63`. Existing live/fixture evidence is covered above. |
| Freshness byte-survival hold | PASS | `FRESH_ROWS=18/18`; this does not certify current-host truth. |
| Source census and validation run cleanly | PASS | Baseline and copied-current census each exit 0 at 35 rows; both validation runs exit 0, with only the four disclosed W04s S024/S028/S029/S034. This is not the still-unlanded final S036/S037 census. |
| C2/C3/C4 attributed labels are actually printed | PASS | All three labels were printed by the exercised frozen counter; printing does not imply their targets pass. |

C07 remains `frontier` in this pre-admission snapshot, so `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']` and K remains `7/14`. The candidate is not present in this snapshot. These are open C1/integration dependencies, not evidence that a final C1 decision occurred. The frozen contract requires the eventual C07-only flip to `held` on admission or `uncovered` on falsification.

## Preservation details

Manifest SHA-256: `b5c2c9ca64c65659f0f6e97749c8dc02f29aa776d65e8af82889613a35aa5035`.

The round-63 preservation manifest has 455 total lines, of which **443** cover live/fixture files; the remaining 12 cover README, SOURCES and ten verifiers. The round-64 live/fixture manifest is **452**, a legitimate +9 already present in the claim-base archive, not newly introduced round-64 evidence:

- `corpus/fixtures/firmware-r63/firmware-r63.bin`
- `corpus/fixtures/firmware-r63/generator.py`
- `corpus/fixtures/firmware-r63/truth.json`
- `corpus/live/runs/round-63/LEDGER.md`
- `corpus/live/runs/round-63/inspection.json`
- `corpus/live/runs/round-63/oracle_check.py`
- `corpus/live/runs/round-63/receipt.json`
- `corpus/live/runs/round-63/stderr.txt`
- `corpus/live/runs/round-63/stdout.raw`

All overlapping round-63/round-64 manifest digests match. The new manifest omits the old manifest's 12 non-live/fixture paths by its stated scope; quality/README/historical-content checks above are separate.

## Exercised counter receipt

Command (cwd `/`, lane-owned TMPDIR):

```text
env TMPDIR=/tmp/revenger-r64-harms-mknxdlfu python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py /tmp/revenger-r64-harms-mknxdlfu/working
```

Selected exact output, exit **1**:

```text
K_HELD=7/14 score=5.0
K_ROW C07 status=frontier
K_HELD_BACKED=7/14
K_HELD_BACKED_STRICT=7/14
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py b exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=1/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=1/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=no
HOLDS_OK_V2=no
```

Source checks exercised `sources-census.sh census` and `validate` with `--today 2026-10-24 --file` pointing separately to the claim-base and copied-current absolute SOURCES paths. Both produced 35 rows: tier A 33, tier C 2; mined 30, queued 1, rejected 4; missing 0. Both validations reported only the four registered W04 warnings.

## Closure boundary

The C2 control deletion is the concrete no-harm blocker demonstrated here. The smallest correction is one restored assertion, not a change of target. After that correction and C1 integration, L1 must obtain the final frozen-counter receipt on the contract-required committed archive and repeat the preservation/diff/census checks there; this precheck does not substitute for that receipt. The frozen probe deliberately retains old exit semantics (`measure.py:264–273`), so future exit 0 alone is not sufficient evidence for all attributed counts or `HOLDS_OK_V2`.

After this receipt was recorded, `revenger-r64.R64C4LangPatch` reported that the current verifier contains the command-rejection assertion immediately before the stdout control and that its ordinary self-test passes. This is a reported correction, not a new counter measurement by this critic. The captured failing version and its results remain the precheck evidence; only L1's final archived attributed-count receipt can establish that the calibration hold is restored.

Report: .ufo/waves/round-64/R64CriticHarms.md
