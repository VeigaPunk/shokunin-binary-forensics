# ExecHarness8 — findings (round 99, wave w1, milestone: C2 forge harness)

Deliverable: `reports/round-99/forge_reach8.py`
sha256 (final bytes, unchanged since the last run below): `0a393136509478866090d97e25ba35ed31e2db24512363462b9bdec564c4bb67`

## Files written
- `reports/round-99/forge_reach8.py` (new, executable mode from the write tool; no `__pycache__`, `-B` used throughout).
- Receipts in this wave dir:
  - `ExecHarness8/forge_reach8.sha256` — sha256 line for the harness.
  - `ExecHarness8/c2-forge-v7-frozen.log` / `.stderr` — frozen v7 run (acceptance receipt).
  - `ExecHarness8/c2-forge-v8wip-development.log` / `.stderr` — WIP v8 development run (not a frozen result).

## What the harness does (one run)
- Pins the builder (`.ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py`, sha `82347899…38cd`) and the parity patch (`…/L1-holdout-v7/parity-patch.diff`, sha `1dfcb155…2572`) to the blobs committed at `7e6edd4d` and to pinned constants. Mismatch → exit 2. The committed builder is never edited or run in place.
- Stages a byte copy four directories deep under the scratch root, applies the one-hunk add patch with a strict applier (anchor line 189 verified, already-applied input refused, patched source compiled), runs the copy for `--profile c02` and `--profile c14` with `--lane` explicit.
- Parses the builder table and checks it against its own summary line and control line; missing, empty or inconsistent output → exit 2 (never 0 accepted).
- Stub self-test: always-pass stub must score every vector accepted, always-fail stub 0; both are run per profile and the built trees must match the main run (persisted honest-tree manifest plus per-vector changed-file hashes and removed sets).
- Prints `C2_VECTOR <profile>-<id> accepted|refused legs=…` (one per vector), `C2_ACCEPTED=n/12`, `C2_CONTROL_C02=`, `C2_CONTROL_C14=`, `C2_STUB_SELFTEST=`, `C2_REASON=` (whenever not-met), `C2_VERDICT=met|not-met`. Met only if exactly 12 vectors, 0 accepted, both controls `control-ok`, stub ok, every vector has a verdict. Per RevengerR99 amendment A3, fewer than 12 lines forces not-met.

## Deviations from the spec text, stated plainly
- The builder deletes each vector tree after scoring it, so "same fully built trees" is checked by fingerprint (honest manifest and per-vector changed/removed hashes) across the main and stub runs, not by re-scoring the stored trees.
- Fixture paths: the frozen v6 `_fixture` roots the c02 honest tree under a random `fx-<rand>/t/`; the harness strips that prefix from honest manifest keys only (fail closed if absent). Vector paths are already root-relative.
- `NO-VERDICT` vector rows make the verdict not-met.

## Counting command outputs
Frozen v7 (`reports/round-98/c1_k_admit_counter7.py`, sha `59c9930a…8548`), `PYTHONUTF8=1 python3 -B reports/round-99/forge_reach8.py --counter reports/round-98/c1_k_admit_counter7.py --work <scratch>`, rc=0, wall 79.7 s:
```
C2_VECTOR c02-V01 accepted legs=
C2_VECTOR c02-V02 accepted legs=
C2_VECTOR c02-E01 accepted legs=
C2_VECTOR c02-E02 accepted legs=
C2_VECTOR c02-E03 accepted legs=
C2_VECTOR c02-R01 refused legs=C1_ONLY_TARGET,C1_ADMITTED_UNION,C1_VERDICT
C2_VECTOR c14-R01 accepted legs=
C2_VECTOR c14-V01 refused legs=C1_VOTE_NOTES,C1_VERDICT
C2_VECTOR c14-V02 accepted legs=
C2_VECTOR c14-Q01 refused legs=C1_QUOTES,C1_VERDICT
C2_VECTOR c14-O01 accepted legs=
C2_VECTOR c14-L01 accepted legs=
C2_ACCEPTED=9/12
C2_CONTROL_C02=control-ok
C2_CONTROL_C14=control-ok
C2_STUB_SELFTEST=ok
C2_REASON=counter accepts 9 of 12 vectors
C2_VERDICT=not-met
```
Per-vector outcomes match `reports/round-99/controls/c2-do-nothing-v7-holdout98-c02.log` (5 accepted, R01 refused) and `…-c14.log` (R01, V02, O01, L01 accepted; V01, Q01 refused), and the `legs` column matches the logs' failing-leg column.

WIP v8 (`reports/round-99/c1_k_admit_counter8.py`, sha `6db14795…e1a6b`), development only, rc=0, wall 46.9 s: identical to the frozen v7 output above (`C2_ACCEPTED=9/12`, both controls `control-ok`, stub ok, `C2_VERDICT=not-met`). The WIP declares each of the nine new leg names exactly once (`grep -c`: 1 each). It does not yet refuse any of the twelve vectors, so C2 is not met at this WIP stage; that is the counter seat's open work, not a harness fault.

Negative checks (exit codes observed):
- `--lane` pointing at a tree without the pinned builder → `forge_reach8 error: frozen builder missing …`, rc=2.
- Missing counter path → `counter not found`, rc=2.
- In-process `apply_add_patch` checks: patch applied once → 460 → 465 lines, compiles; second application → `already applied` refused; anchor drift → `anchor line 189 drifted` refused.

## Freeze-order disclosure (for RevengerR99)
- The c14 profile's builder constructs a landing-shaped holdout fixture from `1b76b4d` with the README C14 cell set to `held` and the entry set to `admitted` (the builder's `build_c14_honest`). Frozen v7 and the WIP v8 counter were both run on it in this step (development on fixtures, as the claims allow). The freeze-order text says no counter may run on a C14-held tree; I read these as holdout fixtures, not the landing tree, but the L1 should rule on that reading before the v8 freeze. No counter was run on the landing archive or on any `7e6edd4d` tree.
- Tooling: no installs or upgrades were made. Read-only git only (`cat-file blob`).

## Open questions
- The WIP v8 accepts 9/12 today; C2 cannot be met until ExecCounterV8 refuses the twelve vectors. The harness will report that honestly on each run.
- Whether the c14 fixture counts as a C14-held tree under freeze order (see disclosure).

## Addendum: re-run against final v8 bytes (supersedes the WIP result above)

Counter: `reports/round-99/c1_k_admit_counter8.py`, sha256 `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581`. Command: `PYTHONUTF8=1 python3 -B reports/round-99/forge_reach8.py --counter reports/round-99/c1_k_admit_counter8.py --work <scratch>`, rc=0, wall 42.5 s. Receipt: `ExecHarness8/c2-forge-v8-final-620dfca9.log` (+ `.stderr`, empty).

```
C2_VECTOR c02-V01 refused legs=C1_VOTES_GLOB,C1_VERDICT
C2_VECTOR c02-V02 refused legs=C1_NA_REASON,C1_VERDICT
C2_VECTOR c02-E01 refused legs=C1_RECHECK_CMD,C1_VERDICT
C2_VECTOR c02-E02 refused legs=C1_HEX_CLAUSES,C1_VERDICT
C2_VECTOR c02-E03 refused legs=C1_COVMAP_ROW,C1_VERDICT
C2_VECTOR c02-R01 refused legs=C1_ONLY_TARGET,C1_ADMITTED_UNION,C1_VERDICT
C2_VECTOR c14-R01 refused legs=C1_ROW_IDS,C1_VERDICT
C2_VECTOR c14-V01 refused legs=C1_VOTE_NOTES,C1_VERDICT
C2_VECTOR c14-V02 refused legs=C1_DECISION_KEYS,C1_VERDICT
C2_VECTOR c14-Q01 refused legs=C1_QUOTES,C1_VERDICT
C2_VECTOR c14-O01 refused legs=C1_OWNWORK_ROUND,C1_VERDICT
C2_VECTOR c14-L01 refused legs=C1_FETCHLOG_DATE,C1_VERDICT
C2_ACCEPTED=0/12
C2_CONTROL_C02=control-ok
C2_CONTROL_C14=control-ok
C2_STUB_SELFTEST=ok
C2_VERDICT=met
```

Each of the twelve vectors is refused by exactly the leg its class targets, plus `C1_VERDICT`. The c02 R01 vector also fails `C1_ONLY_TARGET` and `C1_ADMITTED_UNION`, as in v7. Harness unchanged (sha `0a39…c4bb67`). Scratch removed. This is a development-set result on the twelve r98 vectors (not a fresh holdout); the L1 should run the calibration on the committed v8 freeze as the claims require.
