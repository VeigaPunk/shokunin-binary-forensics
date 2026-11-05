# ExecBattery — round 94, wave 1 (frozen-instrument integrity + frozen C2 re-run)

Seat: ExecBattery (executor, leaf). Freeze rev audited: `060a8e87d6de6b31f91b58524ab0fcad88ae5431`.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. All commands run with `PYTHONUTF8=1 python3 -B`, cwd = my scratch (`/fast/scratch/hyaku/revenger-r94/ExecBattery`, deleted before this report). Full stdout/stderr/exit codes preserved verbatim in the sibling log files in this wave dir.

## 1. Immutability receipt — ALL FIVE IDENTICAL

Method: `sha256(git show 060a8e87…:<path>)` compared against `sha256(<worktree file>)`, byte-for-byte. Receipt: `freeze-integrity.txt` in this wave dir.

| path | frozen == worktree | sha256 (both sides) |
|---|---|---|
| reports/round-93/c1_k_admit_counter2.py | YES | `2a5132d0620aa9400a4025d8c0587fa095441af033d5e76a85e5969fe6ea9211` (21453 B) |
| reports/round-93/c2_legend_counter2.py | YES | `fba5a58a1d2b728be40b9da13671cc513c81998829ab19668bff5f1b89b41ca8` (11246 B) |
| reports/round-93/forge_battery.py | YES | `d6e70e52e8a9af6a8d559a820db0fd92093230c478d45fb4bedef104e51811f2` (16658 B) |
| reports/round-94/c1_k_admit_counter3.py | YES | `de2815be742737cb66ffc5249aa61b25173cec138b8e4b958eb2e171175d799e` (27785 B) |
| reports/round-94/forge_battery3.py | YES | `5a0d27dbcff27bfbfdcae4e522a7d3b0c64eb6194621e23ebffde471356a5d9e` (7948 B) |

`git show` returned rc=0 with empty stderr for all five; frozen byte counts equal worktree byte counts. No frozen instrument was modified on this host.

## 2. Re-runs — every frozen expectation met, zero deviations

### 2a. r93 battery, `--stage full` (`forge_battery_full.log`, exit 0)
- `V1_REACH_C2=5/5` — expected 5/5 ✔
- `V2_KILLS=9/9` (F1–F4 `v2c1=fail kill=yes`; F5–F9 `v2c2=fail kill=yes`) — expected 9/9 ✔
- `POS_C1V2=pass` ✔, `POS_C2V2=pass` ✔
- `DO_NOTHING_C2=fail` — expected fail (negative control) ✔
- `BATTERY_VERDICT=pass` ✔
- R92 receipt probes: `findings.md present=True marker=yes` for all four quoted markers.

### 2b. r93 battery, `--stage v1-only` (`forge_battery_v1only.log`, exit 0)
- `V1_REACH_C2=5/5` (F5–F9 `v1=pass rc=0 reach=yes`) — expected 5/5 ✔
- `BATTERY_VERDICT=pass` ✔

### 2c. r94 v3 battery, `--stage full` (`forge_battery3_full.log`, exit 0)
- V3 kills, each on its frozen expected leg: F10-dup-status→`C1_ADMITTED`, F11-forged-registry→`C1_VOTES`, F12-case-dup-seat→`C1_VOTES`, F13-role-mismatch→`C1_VOTES`, F14-empty-artifact→`C1_VOTES`, F15-traversal→`C1_VOTES`, F16-body-rejected-sid→`C1_SOURCES`, F17-vacuous-na→`C1_VOTES`, F18-ws-output→`C1_EMBED_NONVACUOUS`, F18b-tilde-fence→`C1_EMBED_NONVACUOUS`, F19-stale-new-row→`C1_SOURCES`, ONLY-C15-second-row→`C1_ONLY_C15`.
- `V3_KILLS=12/12` — expected 12/12 ✔
- `POS_C1V3=pass (real lint + real embedded checker, no stubs)` ✔
- `DO_NOTHING_C1V3=fail-as-required` — expected fail ✔
- R93 hold re-run inside battery3: `V2_KILLS=9/9`, `POS_C1V2=pass`, `POS_C2V2=pass`, `DO_NOTHING_C2=fail`, `BATTERY_VERDICT=pass` ⇒ `HOLD_R93_BATTERY=pass` ✔
- `BATTERY3_VERDICT=pass` ✔

### 2d. v3 counter self-test (`c1_counter3_selftest.log`, exit 0)
- `SELFTEST_C1V3=pass legs=14` — expected `pass legs=14` ✔

Deviation count: **0**. Every line above matches the frozen predicate sentences in `reports/round-94/claims.md` (C2 before→after and C1 self-test); nothing was fixed, patched or re-routed — logs are verbatim.

## 3. Environment notes (disclosed, no action taken beyond spec)
- The r93 battery itself pre-created its hardcoded `/fast/scratch/hyaku/revenger-r93/CriticR93` fixture subdirs; I did not touch anything outside `/fast/scratch/hyaku/revenger-r94/ExecBattery` (which was empty — batteries only used their hardcoded r93 roots — and was removed before this report).
- No tools installed; no network used; no git/jj write commands anywhere (`git show <rev>:<path>` and a `git -C` read only).

## 4. Calibration read-out (scoped finding)
On this host, at the freeze tip bytes: the frozen v2 counter still kills its nine frozen classes and passes its positives/do-nothing control (r93 hold intact), while the v3 counter kills all twelve routed forgery classes on their frozen expected legs, passes the honest positive with REAL `corpus/lint_entry.py` + REAL `corpus/check_embedded_outputs.py`, fails on the do-nothing base, and self-tests clean with 14 legs. This is exactly the frozen C2 predicate state (`BATTERY3_VERDICT=pass`, exit 0) plus the frozen C1 self-test predicate (`SELFTEST_C1V3=pass legs=14`).

## Artifacts (all under `.ufo/waves/round-94/w1/ExecBattery/`)
- `freeze-integrity.txt` — five-path immutability receipt
- `forge_battery_full.log` — r93 battery full stage stdout/stderr/exit
- `forge_battery_v1only.log` — r93 battery v1-only stage stdout/stderr/exit
- `forge_battery3_full.log` — r94 battery3 full stage stdout/stderr/exit
- `c1_counter3_selftest.log` — v3 counter self-test stdout/stderr/exit

No blockers.
