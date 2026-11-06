# ExecCounterV9 — findings (revenger round 100, wave w1), revision 2

Artifact: `reports/round-100/c1_k_admit_counter9.py`
sha256 (final bytes): `8e2eafc80726789aafa2ee491123de8b46ac63945692edaed6c474540e9885e8`
Base: byte copy of frozen v8 (`reports/round-99/c1_k_admit_counter8.py`, sha256 `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581`, unchanged).
Frozen builder used as a scratch copy, sha256 `22dddf3d683719c38772f7f65716196f2eabd641e8368791e9575430e79984ec` (verified).

## Revision 2 (RevengerR100 decision, pre-freeze)

Revision 1 failed no-regression conjunct 2 (forge_reach8 c14 control `control-BROKEN`): the r98 Amendment C candidate (`1b76b4d`) fails the lane's own `deriv_check.py` (8 of 17 rows), so the strict DERIV leg refused it. The L1 decided: `C1_DERIV_RERUN` applies only when the entry declares a verbatim stdout cell rule (a preamble line in the derivation section, outside table rows and before the next `## ` heading, containing both `stdout` and `verbatim`). An entry with no such declaration passes the leg with `no verbatim cell rule declared`. The 0350014d and 9ddd38ac entries declare it (line 66); 1b76b4d does not.

Revision 1 results, superseded (receipts removed; recorded here): 12/12 green refused; `C2_ACCEPTED=0/12`, `C2_CONTROL_C02=control-ok`, `C2_CONTROL_C14=control-BROKEN` (only failing leg on that tree: `C1_DERIV_RERUN`, `DERIV_ROWS=17 DERIV_MISMATCH=8`); v8 on that tree `C1_VERDICT=pass`.

## Results, revision 2 (the four L1-requested checks)

| Check | Command | Result |
|---|---|---|
| Self-test | `python3 -B reports/round-100/c1_k_admit_counter9.py --self-test --receipts-dir <scratch>/selftest-receipts --work <scratch>/stwork` | rc 0; `SELFTEST_C1V9=OK legs=128` (126 rev 1 + declared-rule delta + undeclared-rule delta on c14 and c14r99) |
| 12 r99 vectors, v9 | `build_fresh99.py --counter reports/round-100/c1_k_admit_counter9.py --profile {c02,c14} --lane <lane>` | rc 0 both. c02: control-ok, `HOLDOUT99 accepted=0/6`. c14: control-ok, `HOLDOUT99 accepted=0/6`. All 12 `refused`. |
| forge_reach8, v9 | `python3 -B reports/round-99/forge_reach8.py --counter reports/round-100/c1_k_admit_counter9.py --work <scratch>/forge8b/work` | rc 0; `C2_ACCEPTED=0/12`; `C2_CONTROL_C02=control-ok`; `C2_CONTROL_C14=control-ok` |
| c14r99 real tree | `python3 -B reports/round-100/c1_k_admit_counter9.py --profile c14r99 --tree <scratch>/data` (`data` = `git archive 0350014d`) | rc 0; `C1_K_HELD_BACKED=14/15`; `C1_DERIV_RERUN_WHY=DERIV_ROWS=29 DERIV_MISMATCH=0`; `C1_VERDICT=pass` |

Red-before (frozen v8) receipts from revision 1 are unchanged and still in the wave dir: 12/12 ACCEPTED (`HOLDOUT99 accepted=6/6` each profile, both controls control-ok).

## Leg list (name → vector class → rule)

"all" = c02, c14, c14r99; "C14" = c14 and c14r99; legs outside their profile print `pass` with `not applicable to profile`.

| Leg | Profiles | Vector class (builder) | Rule |
|---|---|---|---|
| `C1_PASS_NOTE_FLOOR` | all | c02 N1 one-token PASS note | every PASS decision has a note of ≥6 whitespace tokens |
| `C1_VOTER_PRESENT` | all | c02 N2 pinned vote omitted | every pinned reviewer/critic whose `WAVE_DIR/w1/<seat>/` tree holds a file naming the candidate digest has a vote |
| `C1_QMAP_POINTER` | all | c02 N3 Q-map PASS over n/a | no Q-map row with decision PASS carries the `see Qnn in corpus/QUALITY.md` pointer (text rule) |
| `C1_EVIDENCE_RESOLVES` | all | c02 N4 identifier in derivation row replaced | every `ev_<64 hex>` in the entry occurs in a file under `corpus/live/runs/`; at least one cited |
| `C1_SECTIONS` | c02 | c02 N5 observation/limitations cut | `## Observation, inference, unknown` and `## Limitations` each appear once with a non-blank body |
| `C1_SURFACE_TEXT` | all | c02 N6 surface text asserts replication | target row's surface cell contains no PASS/FAIL/replicat*/seat(s)/vote(s) token (text rule) |
| `C1_NA_SHARE` | C14 | c14 N1 n/a inflation | each voter's n/a count ≤ 8 of 17 |
| `C1_ARTIFACT_COPY` | C14 | c14 N2 artifact renamed to other seat | no two vote artifacts of different roles equal after the owning seat's name is replaced by `<SEAT>` |
| `C1_DERIV_RERUN` | C14 | c14 N3 derivation count edited | IF the entry declares a verbatim stdout cell rule: every derivation row re-runs (bash, cwd=tree) to its printed value, `DERIV_MISMATCH=0`, `DERIV_ROWS>0`. ELSE pass (`no verbatim cell rule declared`). |
| `C1_RECORD_PINNED` | C14 | c14 N4 record appended | `ROUND_RECORD_DIR` holds exactly the three pinned round-98 record files with pinned sha256 |
| `C1_BODY_DIGEST` | C14 | c14 N5 S506 body rebuilt | every SOURCES cell citing `body N bytes sha256 H committed at P` has `P` present with that length and sha256 |
| `C1_ANCHOR_VERBATIM` | C14 | c14 N6 S507 anchor relabelled | each new own-work anchored row (`(1-based bytes …)`): every backticked quoted segment after the byte range occurs verbatim in the citing entry |

Green vector → refusing leg (revision 2; each vector refused by its class leg plus `C1_VERDICT`):
C02-N1 → C1_PASS_NOTE_FLOOR; C02-N2 → C1_VOTER_PRESENT; C02-N3 → C1_QMAP_POINTER; C02-N4 → C1_EVIDENCE_RESOLVES; C02-N5 → C1_SECTIONS; C02-N6 → C1_SURFACE_TEXT; C14-N1 → C1_NA_SHARE; C14-N2 → C1_ARTIFACT_COPY; C14-N3 → C1_DERIV_RERUN (declaration present in the forged entry, so the rule applies); C14-N4 → C1_RECORD_PINNED; C14-N5 → C1_BODY_DIGEST; C14-N6 → C1_ANCHOR_VERBATIM.

Honest controls: builder c02 `control-ok`; builder c14 `control-ok`; c14r99 real tree pass (K 14/15); self-test honest fixtures pass for c02, c14, c14r99.

## Known evasion and limits (disclosed)

- **Declaration evasion (new with revision 2):** an author can remove the verbatim stdout declaration from an entry and then edit a derivation cell, and `C1_DERIV_RERUN` passes. The self-test covers this exact case as a documented pass (`C1_DERIV_RERUN-undeclared`), so the gate is visible in the receipts. The leg does not detect a stripped declaration by any other means.
- `C1_ARTIFACT_COPY` catches cross-role copies only. The honest builder's reviewer artifacts are template-identical after normalization, so a reviewer-to-reviewer copy passes.
- `C1_QMAP_POINTER` and `C1_SURFACE_TEXT` are text-pattern rules, not vote-consistency checks. Vote-to-Q-map consistency cannot be a rule here: the honest c02 fixture's votes say n/a on Q03, Q04, Q05, Q06, Q11, Q14 and Q16 while the r96 entry Q-map marks them PASS. The honest c02 control is itself Q-map/vote inconsistent; the L1 should know this.
- `C1_RECORD_PINNED` pins lane bytes of the round-98 record (identical at `0350014d` and `9ddd38a`, verified by sha256sum). It is a constant set, not a builder fingerprint.
- `C1_ANCHOR_VERBATIM` relies on verbatim quotes in the entry; passes the landing entry and the honest fixtures.
- `C1_EVIDENCE_RESOLVES` checks the ID exists in any saved record, not that it sits in the row's cited file.

## Changes to v8 bytes (disclosed)

v8 is kept byte-for-byte for every leg and constant. Edits: (1) module docstring first line (version string); (2) `self_test` summary print renamed `SELFTEST_C1V9`; (3) one self-test fixture artifact line in `_fixture`: `"{seat} fixture evidence"` → `"{seat} ({role}) fixture evidence"` (accepted by the L1; self-test only). Reason: the three template-identical honest artifacts collided across the reviewer/critic boundary under `C1_ARTIFACT_COPY`; the role marker keeps the honest fixture distinct, and the copy delta still collides.

## Commands and exit codes (revision 2)

1. `python3 -B -c "ast.parse(...)"` → AST_OK.
2. Self-test (above) → rc 0, `SELFTEST_C1V9=OK legs=128`.
3. c14r99 real tree (above) → rc 0, `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`.
4. `build_fresh99.py --counter <v9> --profile c02` → rc 0; control-ok; accepted 0/6.
5. `build_fresh99.py --counter <v9> --profile c14` → rc 0; control-ok; accepted 0/6.
6. `forge_reach8.py --counter <v9>` → rc 0; `C2_ACCEPTED=0/12`; `C2_CONTROL_C02=control-ok`; `C2_CONTROL_C14=control-ok`.
7. `sha256sum` on the lane file → `8e2eafc8…e885e8`; v8 `620dfca9…3581` (matches frozen); builder `22dddf3d…84ec` (matches frozen).

Earlier, revision 1 (superseded): self-test rc 0 `legs=126`; builder c02 and c14 runs rc 0 (green); c14r99 rc 0 K 14/15; forge8 rc 0 with `C2_CONTROL_C14=control-BROKEN`; v9 on the staged c14 control tree rc 1 (only `C1_DERIV_RERUN`); v8 on that tree rc 0 (`C1_VERDICT=pass`); lane `deriv_check.py` on `1b76b4d` `DERIV_MISMATCH=8`, on `0350014d` `DERIV_MISMATCH=0`.

## Receipts

Wave dir `.ufo/waves/round-100/w1/ExecCounterV9/`: `red-v8/` (frozen v8, revision-independent: run logs, rc, per-vector counter.log, vector.json, results), `build-only/` (builder build-only logs, rc), `rev2/` (revision 2: `selftest-v9-rev2.out`, `selftest-receipts/`, `realtree-c14r99-rev2.out`, `run-c02.log`, `run-c14.log`, `rc.txt`, `forge8-v9-rev2.out`, `forge8-v9-rev2.rc`, per-vector counter logs and results).

## Tooling

No installs. No pacman or git mutations. Git used read-only (`archive`, `show`) into scratch. Scratch removed after this report.

## Open questions for the L1

None on the instrument. Gate decisions to record: the declaration-evasion limit above, and the honest c02 Q-map/vote inconsistency.
