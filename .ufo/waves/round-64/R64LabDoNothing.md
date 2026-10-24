# R64LabDoNothing — independent do-nothing re-derivation

Brief: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/briefs/R64LabDoNothing.md`
Contract: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md`
Base commit under test: `666ea84b6be2eec2b0359f556ba2429fc9044c36` (resolved via `git rev-parse 666ea84b6be2eec2b0359f556ba2429fc9044c36^{commit}`; READ-ONLY git, no mutation).
No lane file, index, jj state, `.ufo` spec/registry, MANIFEST or sibling lane was written. The only writes are this report and lane-owned scratch under `/tmp/revenger-r64-donothing/`. No tools installed (nothing needed; pacman untouched).

## Verdict

**PASS — the frozen counter on the base archive reproduces the committed red-before receipt byte-for-byte.**
`measure-after.log` sha256 `8116b216d543984bfb60c6331defae43f384f5c94904658afb8997b8692a1003` == committed `reports/round-64/measure-before.log` sha256 `8116b216d543984bfb60c6331defae43f384f5c94904658afb8997b8692a1003`. `cmp` → identical, 4116 bytes, both 47 newline-terminated lines. Label-line diff: **0 differences (46/46 label lines identical)**. Probe exit **0**.

Do-nothing meets no target, exactly as the contract states: K 7/14 < 8/14, `README_TOKEN_LEGEND_MISMATCH` 1 ≠ 0, `C4_RECEIPT_KILLED_ATTRIBUTED` 0/2 < 2/2.

## Commands executed (verbatim, absolute paths)

```
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse 666ea84b6be2eec2b0359f556ba2429fc9044c36^{commit}
rm -rf /tmp/revenger-r64-donothing && mkdir -p /tmp/revenger-r64-donothing
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus | tar -x -C /tmp/revenger-r64-donothing/
cd / && TMPDIR=/tmp/revenger-r64-donothing python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py /tmp/revenger-r64-donothing
```

Run captured stdout+stderr to `/tmp/revenger-r64-donothing/measure-after.log`; stderr was empty (0 bytes), stdout 4116 bytes.

## Frozen label values — expected vs observed

| Frozen label | Required (contract / before receipt) | Observed | Match |
|---|---|---|---|
| `K_HELD` | 7/14 | `K_HELD=7/14 score=5.0` | yes |
| `K_ROW C07` | `frontier` at base | `K_ROW C07 status=frontier` | yes |
| `K_HELD_BACKED` | 7/14 | `K_HELD_BACKED=7/14` | yes |
| `K_HELD_BACKED_STRICT` | 7/14 (must equal K_HELD_BACKED) | `K_HELD_BACKED_STRICT=7/14` | yes |
| `README_TOKEN_LEGEND_MISMATCH` | 1 (row `C07`) | `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']` | yes |
| `C4_RECEIPT_KILLED_ATTRIBUTED` | 0/2 | `C4_RECEIPT_KILLED_ATTRIBUTED=0/2` (both mutants exit 0, "pass") | yes |
| `C4_CONTROLS_PASS` | 2/2 | `2/2` | yes |
| `C2_CONTROLS_PASS` / `C2_RECEIPT_B_KILLED` / `C2_D2_KILLED` / `C2_RECEIPT_B_KILLED_ATTRIBUTED` | unchanged at base | `2/2`, `2/2`, `2/2`, `2/2` | yes |
| `C3_CONTROLS_PASS` / `C3_RECEIPT_KILLED_ATTRIBUTED` | unchanged at base | `2/2`, `2/2` | yes |
| `F_COVERAGE` / `F_FAMILIES` | 5/8, five families | `F_COVERAGE=5/8 score=6.2`, `['native-static', 'javascript', 'archives', 'firmware', 'evm']` | yes |
| `FRESH_ROWS` | 18/18 | `FRESH_ROWS=18/18` | yes |
| `HOLD_CALIBRATION` / `HOLD_REPLAY` | 4/4, 10/10 | `4/4`, `10/10`; all ten `HOLD` lines `exit=0` | yes |
| `HOLDS_OK` | `yes` (round-63 semantics) | `HOLDS_OK=yes` | yes |
| `HOLDS_OK_V2` | `no` at base by construction (mismatch 1, C4 0/2) | `HOLDS_OK_V2=no` | yes |
| probe exit | 0 | 0 (not 1, not 2) | yes |

`SAVED_RECORDS=59` and `ROW_OPS={'C03': ['inspect_managed_artifact'], 'C05': ['inspect_android_package'], 'C07': ['inspect_firmware_regions'], 'C08': ['capture_browser_scenario', 'inspect_web_page', 'observe_web_session']}` also reproduce exactly.

## Diff against the committed receipt

- `cmp -s /tmp/revenger-r64-donothing/measure-after.log /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log` → **identical** (no differing bytes).
- Label-line extraction (`^[A-Z][A-Z0-9_]*=`, `K_ROW `, `HOLD `, `MUTANT `): 46 lines in each; ordered comparison → **0 differences**. The per-mutant receipt lines (`MUTANT … control/b/d2/c3/c4`, incl. both `c4` survivors `exit=0 pass`) are identical too, so the red-before attribution state is reproducible, not just the totals.

## Independent cross-checks (not via measure.py)

1. **Tree identity.** All **486/486** files extracted from the archive hash to the exact blobs listed by `git ls-tree -r 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus` (`git hash-object --no-filters` per file; 0 mismatches). The probe ran on the declared base bytes, and re-hashing after the run still matched → the counter's temp-copy mutation strategy left corpus bytes untouched.
2. **Coverage map, independent parse.** 14 `| C.. |` rows, 7 `held`, C07 row literally `| C07 | firmware images | — | — | frontier |`; legend line contains "no knowledge and no saved record". Independent JSON walk: 106 files under `corpus/live/runs`, **59** are dicts with a truthy `operation` (47 are dicts without one — this is exactly why the label is 59, not 106), including exactly **1** `inspect_firmware_regions` record. So `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']` is independently the right observation.
3. **Counter identity.** `reports/round-64/measure.py` sha256 `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`; the run used that file from the lane working tree, not a copy.

## Notes / observations (not defects, no action requested)

- Lane HEAD at probe time was `a3d063f29b93ad1f0b7eab78652c552685b84d89` (other seats' integration), not `666ea84…`. The archive argument pins the base, so this does not affect the control; recorded so the 47-line receipt is not mistaken for a HEAD run.
- `HOLDS_OK_V2=no` with exit 0 is the frozen base state: the V2 predicate additionally requires `README_TOKEN_LEGEND_MISMATCH==0` and attributed C4 kills, while exit status stays on round-63 `HOLDS_OK` semantics. This is the red the round is meant to remove; it is consistent in both receipts.
- `/tmp/revenger-r64-donothing/` contains only `corpus/` and `measure-after.log`; the counter's `TMPDIR` temp dirs were cleaned up by the script (no residue). Scratch is lane-owned and to be removed on landing.

## Restoration

No mutation was made to `/home/vgpnk/Projects/shokunin/revenger-shokunin` (including lane jj state and Git index). Scratch evidence retained at `/tmp/revenger-r64-donothing/` (corpus extracted from the base archive, post-run tree re-verified 486/486), `measure-after.log` kept there as the reproduction receipt.
