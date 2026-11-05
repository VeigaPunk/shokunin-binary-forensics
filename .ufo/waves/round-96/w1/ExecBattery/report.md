# ExecBattery — round 96 reproduction report

Seat: ExecBattery (executor). Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin
Freeze commit: ff767436feed32cf2f4074f05f938f8cea98e69a
Env: PYTHONUTF8=1, HYAKU_SCRATCH=/fast/scratch/hyaku, `python3 -B` everywhere (no --receipts-out, no lane writes).
Scratch receipts used: /fast/scratch/hyaku/revenger-r96/ExecBattery/per-delta/ (31 JSON files, deleted after copy).

## Instrument bytes (step 4)

| Instrument | Check | Verdict |
|---|---|---|
| reports/round-96/c1_k_admit_counter5.py | `git show <freeze>:reports/round-96/c1_k_admit_counter5.py \| cmp - reports/round-96/c1_k_admit_counter5.py` | BYTE-IDENTICAL (cmp rc 0, no output) |
| reports/round-96/forge_battery5.py | `git show <freeze>:reports/round-96/forge_battery5.py \| cmp - reports/round-96/forge_battery5.py` | BYTE-IDENTICAL (cmp rc 0, no output) |

## 1. Self-test — `c1_k_admit_counter5.py --self-test --receipts-dir <scratch>/per-delta`

Command rc = 0. Output (selftest.log, 1 line) vs controls/selftest-c1v5.log:

| Line | Expected control | Observed | Verdict |
|---|---|---|---|
| 1 | `SELFTEST_C1V5=pass legs=33` | `SELFTEST_C1V5=pass legs=33` | MATCH — `diff` clean (DIFF_CLEAN) |

- sha256 selftest.log = c5e65f7bc68a8948eb9a1c3024a445b498158f2b45325480d4bccac655fdad05, equal to sha256 of controls/selftest-c1v5.log.
- Per-delta receipts generated in scratch: 31 files (A3-usedby-extra, A4-shadow-admitted, EMBEDDED-fake-fence, F10-dup-status-fenced, F12-case-dup-seat, F13-role-mismatch, F15-traversal, F16-unresolved-body-sid, F17-vacuous-na, F18-ws-output, F18b-tilde-fence, F19-stale-new-row, F20-foreign-artifact-dir, H1-indent-dup-status, KHELDBACK-broken-cell, LINT-qmap-missing-row, M5-pycache-planted, M6-forged-registry-seat, M8-pycache-frozen-dir, ONLY-C10-second-row, QUOTES-mutated-body, ROWS-total-extra-row, TRIO-missing-recheck, V03-dup-json-keys-registry, V04-dup-json-keys-vote, V07-legacy-path, V08-entry-pending, V10-stale-fetched-at, V18-na-letter-flood, V19-sid-suffix-spaced, V27-fabricated-body-foreign-host). All 31 byte-compared against reports/round-96/controls/per-delta/<name>.json — all identical (no DIFFERS output).

## 2. Red-v4 — `forge_battery5.py --stage red-v4`

Command rc = 0. Output (red.log) vs controls/battery5-red-v4.log:

| Line | Expected control | Observed | Verdict |
|---|---|---|---|
| 1 | `V4_REACH_NEW=3/3` | `V4_REACH_NEW=3/3` | MATCH |
| 2 | `  A4-shadow-admitted: v4 reach` | `  A4-shadow-admitted: v4 reach` | MATCH |
| 3 | `  A3-usedby-extra: v4 reach` | `  A3-usedby-extra: v4 reach` | MATCH |
| 4 | `  M8-pycache-frozen-dir: v4 reach` | `  M8-pycache-frozen-dir: v4 reach` | MATCH |
| 5 | `V4_SELFTEST_UNCOVERED_LEGS=C1_ROWS_TOTAL,C1_TRIO,C1_LINT,C1_EMBEDDED,C1_QUOTES,C1_K_HELD_BACKED` | `V4_SELFTEST_UNCOVERED_LEGS=C1_ROWS_TOTAL,C1_TRIO,C1_LINT,C1_EMBEDDED,C1_QUOTES,C1_K_HELD_BACKED` | MATCH |
| 6 | `V4_SELFTEST_UNCOVERED=6/6` | `V4_SELFTEST_UNCOVERED=6/6` | MATCH |
| 7 | `RED_V4_VERDICT=pass` | `RED_V4_VERDICT=pass` | MATCH |

- `diff` clean (DIFF_CLEAN). sha256 red.log = 1c4884587ee963c19fa5d8e504daa4ddfdb6b0a2adb83a2e28499967f39e05e0, equal to controls/battery5-red-v4.log.
- Expected values confirmed: V4_REACH_NEW=3/3, V4_SELFTEST_UNCOVERED=6/6, RED_V4_VERDICT=pass.

## 3. Full — `forge_battery5.py --stage full`

Command rc = 0. Output (full.log) vs controls/battery5-full.log:

| Line | Expected control | Observed | Verdict |
|---|---|---|---|
| 1 | `SELFTEST_C1V5=pass (POS + 31 deltas + do-nothing)` | `SELFTEST_C1V5=pass (POS + 31 deltas + do-nothing)` | MATCH |
| 2 | `DELTA_RECEIPTS=31/31` | `DELTA_RECEIPTS=31/31` | MATCH |
| 3 | `A4-shadow-admitted: v5 KILLED on C1_ADMITTED_UNION` | `A4-shadow-admitted: v5 KILLED on C1_ADMITTED_UNION` | MATCH — killed on C1_ADMITTED_UNION as required |
| 4 | `A3-usedby-extra: v5 KILLED on C1_SOURCES` | `A3-usedby-extra: v5 KILLED on C1_SOURCES` | MATCH — killed on C1_SOURCES as required |
| 5 | `M8-pycache-frozen-dir: v5 KILLED on C1_PYCACHE` | `M8-pycache-frozen-dir: v5 KILLED on C1_PYCACHE` | MATCH — killed on C1_PYCACHE as required |
| 6 | `V5_KILLS=3/3` | `V5_KILLS=3/3` | MATCH |
| 7 | `MUTANT_V5_REGISTRY_KILLED=pass` | `MUTANT_V5_REGISTRY_KILLED=pass` | MATCH |
| 8 | `POS_C1V5=pass` | `POS_C1V5=pass` | MATCH |
| 9 | `DO_NOTHING_C1V5=fail-as-required` | `DO_NOTHING_C1V5=fail-as-required` | MATCH |
| 10 | `STUB_REJECTED=pass (stub prints pass; no discriminating leg line, so the kill check fails)` | `STUB_REJECTED=pass (stub prints pass; no discriminating leg line, so the kill check fails)` | MATCH |
| 11 | `HOLD_R95_BATTERY=pass` | `HOLD_R95_BATTERY=pass` | MATCH |
| 12 | `BATTERY5_VERDICT=pass` | `BATTERY5_VERDICT=pass` | MATCH |

- `diff` clean (DIFF_CLEAN). sha256 full.log = 15e6a9fc72ccadee2e3dce183b1b3649c956ed90cc9d47df946bd94b4e94d5e8, equal to controls/battery5-full.log.
- All expected full-stage markers present: SELFTEST_C1V5=pass (POS+31+do-nothing), DELTA_RECEIPTS=31/31, V5_KILLS=3/3 on C1_ADMITTED_UNION/C1_SOURCES/C1_PYCACHE, MUTANT_V5_REGISTRY_KILLED=pass, POS_C1V5=pass, DO_NOTHING_C1V5=fail-as-required, STUB_REJECTED=pass, HOLD_R95_BATTERY=pass, BATTERY5_VERDICT=pass.

## Artifacts copied into wave dir

- .ufo/waves/round-96/w1/ExecBattery/selftest.log (sha256 c5e65f7b...)
- .ufo/waves/round-96/w1/ExecBattery/red.log (sha256 1c488458...)
- .ufo/waves/round-96/w1/ExecBattery/full.log (sha256 15e6a9fc...)
- .ufo/waves/round-96/w1/ExecBattery/per-delta/ — 31 receipt JSONs copied from scratch, each identical to controls/per-delta/
- .ufo/waves/round-96/w1/ExecBattery/report.md (this file)

Notes: No tools installed. No lane files edited. No git writes. Scratch deleted before yield.
