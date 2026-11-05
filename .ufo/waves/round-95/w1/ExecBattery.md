# ExecBattery — seat report (round-95 w1, attempt 1)

Seat: ExecBattery (executor). Task: reproduce the frozen round-95 battery4 end to end and
compare against the freeze receipts. Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin.

## Result: REPRODUCED — no verdict-line drift

Both stages of the frozen instrument were run from the lane root with
`python3 -B` and `HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r95/ExecBattery`:

- `--stage red-v3` → rc 0 (14:36:42–14:36:47 -0300), captured to
  `.ufo/waves/round-95/w1/ExecBattery/red-v3.log`.
- `--stage full` → rc 0 (14:37:08–14:37:41 -0300), captured to
  `.ufo/waves/round-95/w1/ExecBattery/full.log`.

Diff against the frozen controls (`reports/round-95/controls/battery4-red-v3.log`,
`battery4-full-at-freeze.log`): in both cases the only differing line is the control's
trailing `rc=0` capture line, which in my runs was captured separately (`RED_RC=0`,
`FULL_RC=0` — both matching). Every verdict line is byte-identical:

- red-v3: `V3_REACH_NEW=10/10`, `MUTANT_V3_REGISTRY_SURVIVES=pass`, `RED_V3_VERDICT=pass`;
  all 10 per-vector `v3 reach` lines identical.
- full: `SELFTEST_C1V4=pass`, `V4_KILLS=10/10`, `MUTANT_V4_REGISTRY_KILLED=pass`,
  `POS_C1V4=pass`, `DO_NOTHING_C1V4=fail-as-required`, `HOLD_R94_BATTERY=pass`,
  `BATTERY4_VERDICT=pass`; all 10 per-vector `v4 KILLED on <leg>` lines identical, same
  legs, same order.

So C2's frozen predicate `BATTERY4_VERDICT=pass` (exit 0) is independently reproduced, and
the committed red-before (`RED_V3_VERDICT=pass`) reproduces too. No scratch path appears
in any verdict line.

## Freeze integrity

Lane HEAD = `6e0bf15fed58f357b7fa0c881371ac7616a116f7` (freeze commit). Working-tree
entry bytes sha256 `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` ==
the freeze commit's blob. Frozen bytes untouched by this seat.

## Files written (all inside this seat's wave dir)

- `red-v3.log` — sha256 `54fd9885f242231b686bdebc64a1b4891114168705088613dc4c04cc5d45d3fd`
- `full.log` — sha256 `5b640281060356ddae6e326b21880cd3b3d0f3dcee938f415b8691c9d43f604a`
- `battery-repro.md` — full diff detail, rcs, token tables, environment notes.
- this file (`../ExecBattery.md` per rendered task trailer).

No lane file, sibling wave dir, `.ufo/state`, watchdog log, or fleet-repo path was
written. No git/jj write command was run anywhere (only read-only `git rev-parse`/`show`/
`status` inside the lane). No installs were performed.

## Findings for the sentinel / L1

1. **r94-M5-class pycache, pre-existing, other actor.**
   `reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc`, mtime 2026-11-05
   14:23:14 — 13 minutes BEFORE this seat's first battery invocation (14:36:42). Every
   Python invocation this seat made used `-B`, and both frozen batteries spawn every
   subprocess with `-B` (verified in forge_battery4.py run_counter/selftest_runner and
   forge_battery3.py lines 73/117/129/138/147), so this seat cannot have produced it.
   Corroboration: `/fast/scratch/hyaku/revenger-r94/c1v3` (mtime 14:27:56) sits at
   counter3's DEFAULT path, reachable only with `HYAKU_SCRATCH` unset — impossible for
   this seat's invocations (env exported; counter3 SCRATCH is env-aware, line 27).
   Some concurrent actor imported/ran counter3 without `-B` and without `HYAKU_SCRATCH`
   before ~14:28. Out of `C1_PYCACHE` scope (that leg checks corpus/, reports/round-95/,
   .ufo/waves/round-95/), so it does not trip the frozen C1 leg — but it is exactly the
   r94 lesson M5 defect class the sentinel audits. Not modified (frozen dir; not mine).
2. **HOLD provisioning root left in place, deliberately.** My full-stage HOLD leg
   created `/fast/scratch/hyaku/revenger-r94/battery3` (`forge_battery3.py`'s hardcoded
   SCRATCH constant; disclosed provisioning per claims §C2). Kept: r94 lesson M1 —
   removing it re-breaks direct frozen-battery3 runs, and battery4 re-pre-creates it
   every HOLD leg anyway. My own seat scratch
   (`/fast/scratch/hyaku/revenger-r95/ExecBattery`) was deleted on exit (verified empty
   of files before deletion; the batteries self-clean their mkdtemp work roots).

## Environment

Python 3.14.8; python3 -B everywhere; `HYAKU_SCRATCH` exported for both runs (battery4
nests `revenger-r95/battery4` under it — still inside the seat scratch). No provider
errors encountered; no network used; no sibling coordination needed.
