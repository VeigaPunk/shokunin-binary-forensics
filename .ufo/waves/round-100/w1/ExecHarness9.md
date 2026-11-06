# ExecHarness9 — findings (round 100, wave w1)

## Deliverable
- `reports/round-100/forge_reach9.py`
- sha256 `3acdd3a98b5dcdbdc3534f32c9be52f990da7f2994b498f6a107cc5678bdd362` (final bytes; no edit after the final v8 run)
- Not edited: `reports/round-99/forge_reach8.py` (sha256 `0a393136…`, untouched).

## What it does
- Pins the frozen builder `.ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py` by working-tree sha256 `22dddf3d…84ec`. Mismatch → rc 2. The file is tracked in the lane (`git ls-files --error-unmatch` rc 0).
- Stages a byte copy at `<work>/forge9/stage-<tag>/nest×4/build_fresh99.py` and runs it per profile with `--counter <given> --profile {c02,c14} --work <run> --lane <lane>` (lane passed explicitly).
- Parses the builder table rows (`name | cls | rc= | verdict | K= | legs | expected | outcome`), the `HOLDOUT99_CONTROL=` line and the `HOLDOUT99 accepted=` summary.
- Vector names are fixed in the harness (C02-N1..N6, C14-N1..N6). A missing, duplicated, unparseable or unclean row (anything other than verdict `fail` + outcome `refused`, or verdict `pass` + outcome `ACCEPTED`) counts as **accepted** and is named in `R100_REASON`. A builder that times out, crashes or prints nothing leaves all its rows missing, so those vectors count as accepted.
- `C1_VERDICT` is excluded from the failing-leg list (the builder's leg column also matches the `C1_VERDICT=fail` line).
- Stub self-test, per profile, on the same built trees (honest tree and each vector's changed/removed sets with per-file sha256 compared with the main run):
  - stub-pass (always `C1_VERDICT=pass`): every row clean-accepted, control-ok;
  - stub-fail (always `C1_VERDICT=fail`): every row refused, control-bad.
- Prints the contract: `R100_VECTOR <name> accepted|refused legs=…` ×12, `R100_ACCEPTED=n/12`, `R100_CONTROL_C02`, `R100_CONTROL_C14`, `R100_STUB_SELFTEST=ok|bad`, `R100_REASON=…` (not-met only), last `R100_VERDICT=met|not-met`. rc 0 met / 1 not-met / 2 usage or pin error.
- Honours `--work`, else `$HYAKU_SCRATCH/forge9-work`, else `$TMPDIR/forge9-work`. Writes only under `<work>/forge9/`. No `/tmp` literal.

## Fixes made during development (disclosed)
1. First run: the c02 fingerprint walked `honest/` and saw the random `fx-<rand>/t/` prefix; a fail-closed normaliser then raised. Fixed by keying the c02 manifest on the builder's own root `honest/fx-*/t` (the builder's `manifest_of(honest)` is rooted there). Verified: two build-only c02 runs gave byte-identical `vectors/c02` trees; only the random prefix differed.
2. Stub-fail message text cleaned; `C1_VERDICT` removed from legs.
3. A bad bulk edit of mine briefly broke the file; repaired and re-parsed (`ast.parse` ok) before any scored run.

## Runs (scratch under /fast/scratch/hyaku/revenger-r100/ExecHarness9, removed on exit)

### 1. Frozen v8 — acceptance run  → `v8.log`
Command:
`PYTHONUTF8=1 python3 -B reports/round-100/forge_reach9.py --counter reports/round-99/c1_k_admit_counter8.py --work <scratch>`
- counter sha256 `620dfca9…3581` (matches the frozen v8 digest in claims.md)
- output: `R100_ACCEPTED=12/12`, `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`, `R100_STUB_SELFTEST=ok`, `R100_VERDICT=not-met`
- rc **1** (expected for the v8 development baseline; met would require 0/12)
- all twelve `R100_VECTOR … accepted` lines present, names in r99 order, no missing rows; stderr empty.
- Consistent with the r99 receipts (`holdout99-v8-c02.log`, `holdout99-v8-c14.log`: 6/6 + 6/6, control-ok).

### 2. Negative: silent counter (`import sys` only, prints nothing)  → `silent-counter-negative.log`
- `R100_ACCEPTED=12/12`, `R100_CONTROL_C02=control-bad`, `R100_CONTROL_C14=control-bad`, `R100_STUB_SELFTEST=ok`, `R100_VERDICT=not-met`; harness rc **1**.
- Confirms fail-closed: no-verdict rows count as accepted, never refused.

### 3. Negative: tampered builder copy in a fake lane  → `pin-mismatch-negative.log`
- stderr `forge_reach9 error: builder sha256 4aefe48a… != pinned 22dddf3d…`; harness rc **2**.

## Not done
- **v9 development run: not performed.** `reports/round-100/c1_k_admit_counter9.py` did not exist at the time of the runs (`ls` rc 2). When ExecCounterV9 lands it, the same command with `--counter reports/round-100/c1_k_admit_counter9.py` should be run; no log exists yet.
- The stub self-test on v8 is ok, so a v9 run is the first place the refusal legs (`legs=`) will be non-empty; the leg parse is exercised only by the builder's `C1_*=fail` lines, which have not been observed on a refusal yet.

## Tooling
- Nothing installed or upgraded. Python 3 standard library only.

## Open questions / risks for the L1
- The builder must be run against lane commit `9ddd38ac…` (`--rev` default, c14 landing) and needs `reports/round-97/c1_k_admit_counter6.py` in the lane. Both are present in the lane at the time of the run; the harness does not pin them.
- The harness pins the builder by working-tree sha256, not by a committed blob (the r98 harness pinned a blob at a freeze rev). The file is tracked; the L1 may add a blob pin if wanted.
- Harness rc 1 on v8 is the correct not-met result; no harness change is needed for the target run.

## Exit codes observed
- v8 run: 1 · silent-counter run: 1 · pin-mismatch run: 2 · `ast.parse` on final bytes: ok.
