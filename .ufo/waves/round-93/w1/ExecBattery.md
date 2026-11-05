# ExecBattery — round 93 w1, frozen-instrument integrity (C2 support)

Seat: ExecBattery (leaf, no dispatches). Date: 2026-11-05. Lane:
`revenger-shokunin`, HEAD at run time `02050cb2a6758e3bd9cec696ff0e42df6f23511a`
(= the freeze commit; `reports/round-93` was clean before and after every run).

## 1. Instrument integrity (integrity.tsv)

Working-tree bytes vs `git show 02050cb2…:reports/round-93/<name> | sha256sum` — all match:

| file | sha256 (both sides) |
|---|---|
| c1_k_admit_counter2.py | `2a5132d0620aa9400a4025d8c0587fa095441af033d5e76a85e5969fe6ea9211` |
| c2_legend_counter2.py | `fba5a58a1d2b728be40b9da13671cc513c81998829ab19668bff5f1b89b41ca8` |
| forge_battery.py | `d6e70e52e8a9af6a8d559a820db0fd92093230c478d45fb4bedef104e51811f2` |

No frozen file was edited; `git status --porcelain -- reports/round-92
reports/round-93` is empty after all runs.

## 2. Re-runs (reproduce.tsv)

From lane root, `HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r93/ExecBattery`,
`PYTHONUTF8=1`:

- `forge_battery.py --stage v1-only` — rc=0, `V1_REACH_C2=5/5`, `BATTERY_VERDICT=pass`
- `forge_battery.py --stage full` — rc=0, `V2_KILLS=9/9`, `POS_C1V2=pass`,
  `POS_C2V2=pass`, `DO_NOTHING_C2=fail`, 4/4 R92 receipts resolved, `BATTERY_VERDICT=pass`
- `c1_k_admit_counter2.py --self-test` — rc=0, `SELFTEST_C1V2=pass kills=registry,artifact-sha,all-na,na-reason cases=none`
- `c2_legend_counter2.py --self-test` — rc=0, `SELFTEST_C2V2=pass kills=record-sha,trailing-cell cases=0open`

Reproduction: each rerun log is byte-identical to its committed control
(`diff -u` empty against `controls/battery-v1-only.log`, `controls/battery-full.log`,
`controls/selftest-c1v2.log`, `controls/selftest-c2v2.log`); every
VERDICT/REACH/KILLS/SELFTEST/POS/DO_NOTHING line equals the committed line.
Verdict-carrying lines and per-log diffs recorded in `reproduce.tsv`.

## 3. Mutation probe (canfail.log)

Pre-registered: one-constant mutant of `c2_legend_counter2.py`
(`RECORD_SHA` last char `…868 → …869`), run over a `git archive 281a5bad…corpus`
copy in scratch. Result: frozen counter over the same tree `C2_C08_RECORD=pass`,
mutant `C2_C08_RECORD=fail`; both `C2_VERDICT=fail` rc=1 on the uncovered base.
The record leg flips pass→fail from the single flipped character — the
instrument can fail. Mutant deleted.

Execution note (recorded honestly in canfail.log): a mutant staged directly in
scratch fails early with `probe-archive-failed` because the counter resolves
LANE from its own script path (archive-isolation design); to exercise the
record leg the mutant was staged two levels deep inside a scratch-local
`git clone --local --no-hardlinks` of the lane. No mutating git command was
run anywhere; the clone's `status --porcelain` was 0 lines after the run.

## 4. Defects, risks

- No defect: both frozen stages, both self-tests and all four control-log
  diffs reproduce byte-identically at the freeze commit.
- Observation, not a defect: the LANE-from-script-path resolution (attempt 1
  above) means any counter copy outside a repo-shaped tree fails closed before
  verdict legs — consistent with the archive-isolation close, worth knowing
  when staging mutants.
- Tooling: installed nothing (no pacman, no uv, no binaries).

## Deliverables

- `.ufo/waves/round-93/w1/ExecBattery/integrity.tsv`
- `.ufo/waves/round-93/w1/ExecBattery/reproduce.tsv`
- `.ufo/waves/round-93/w1/ExecBattery/canfail.log`
- Scratch `/fast/scratch/hyaku/revenger-r93/ExecBattery` removed before yield.
