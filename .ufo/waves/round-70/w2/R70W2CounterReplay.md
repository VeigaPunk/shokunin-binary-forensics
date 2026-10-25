# R70W2CounterReplay — replay of frozen counters on landed tree 17ee7f8

VERDICT: **REPLAYS** — both frozen counters reproduce deterministically on the landed tree; A1 labels stable across six runs despite randomised C2 variants; exit contract verified (README deleted → exit 2 COUNTER_ERROR; checker `raise SystemExit(3)` → red labels; A1 missing v5 → A1_C1=no, exit 1). No deviation found.

## What was replayed

- Target bytes: `git archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md` extracted to scratch (`/tmp/revenger-r70-R70W2CounterReplay`, 523 files, deleted after).
- Pins verified with `sha256sum` (match claims.md / amendment A1, both untouched):
  - `reports/round-70/measure.py` = `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`
  - `reports/round-70/measure-a1.py` = `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191`

## measure.py (frozen counter) — 4 runs, all byte-identical

- Run 1, 2 from cwd `/`, run 3, 4 from cwd `/tmp`: `cmp` identical across all four (runs 3/4 identical to each other and to runs 1/2). Exit 0 every time.
- Replay label set (representative run):
  - `K_HELD_BACKED=8/14 score=5.7`, `K_HELD_BACKED_STRICT=8/14`, `C05_STATUS=uncovered`, `C05_KNOWLEDGE_COLUMN=-`, `C05_SINGLE_V5=no`, `V5_ENTRY_PRESENT=yes`, `V5_ADMITTED_MARKED=no` (landed candidate is deliberately `admission-status: candidate`, README unflipped — expected wave-2 state, C1 decided by Q01–Q15 seats)
  - `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`; `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`; `HOLDS_C1_V5=no`
  - `SM1=0 … SM6=0`, `SELF_MISMATCH=0 exit=0`, `SELF_CLEAN_FIXTURE=0`, `SELF_MUTANTS_KILLED=6/6`, `SHONEN_BOX_COUNT=4`, `README_ROWS=14`, `HOLDS_C2_V5=yes`
  - `EMB_R65=checked_blocks=15 problems=1 exit=1`; `EMB_R67=…17 problems=0 exit=0`; `EMB_R68=checked_blocks=17 problems=0 exit=0`; `EMB_R69=…17 problems=0 exit=0`; `EMB_PINNED_SCRIPT_IS_S046=yes`; `EMB_R68_BYTES_UNCHANGED=yes`; `EMB_R65_BYTES_UNCHANGED=yes`; `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`; `HOLDS_C3_V1=yes`
  - `HOLD_REPLAY=10/10`; `GATE_SELFTEST=exit 0`; `F_COVERAGE=5/8 score=6.2`; `FRESH_ROWS=18/18`; `HOLDS_OK_V7=yes`; exit 0.

## measure-a1.py (amendment counter) — 6 runs, labels stable

- Run 1–5 from cwd `/tmp`, run 6 from cwd `/`. All six print identical labels, exit 0:
  - `A1_C1=yes` (`distinct_commands=24 scripts_allowlisted=True readout_lines=15/15 source_rows_tier_a=7/7`)
  - `A1_C2=yes` (`base_vector=yes clean_variant=yes defect_variants=6/6`)
  - `A1_C3=yes` (`binds_s046=yes script_digest=yes script_prints_17_lines=yes`)
- C2 variants are randomised per run (random.H, random file names/sizes/ids) and no label flipped across six runs — satisfies "labels stable though variants differ".

## Exit contract

- measure.py, README deleted from tree → `FileNotFoundError … corpus/README.md`, prints `COUNTER_ERROR=uncaught exception (exit 2)`, exit **2** (never 1). Verified.
- measure.py, `corpus/self_assessment_check.py` replaced by `raise SystemExit(3)` → labels: `SELF_MISMATCH=n/a exit=3`, `SELF_CLEAN_FIXTURE=nonzero`, `SELF_MUTANTS_KILLED=0/6`, `HOLDS_C2_V5=no`; exit 0 (exit code reflects only the holds block, `measure.py:276-278`; C-labels are printed, not exit-coded — documented contract). Verified.
- measure-a1.py, v5 entry removed → `A1_C1=no` (detail `no v5 entry`), other labels yes, exit **1** (a named label red). Verified.
- measure-a1.py, README deleted → still exit 0 with all labels yes (A1 never reads the tree's README; `a1_c2` runs against `git archive 3f5edbc…`). Noted, not a deviation.

## Verdict

REPLAYS — deterministic identical replay across cwds, stable A1 labels with randomised variants, pins match, exit contract holds. No claim label deviates from the frozen/amended predicates on the landed bytes; C1's mechanical conjuncts read expected `no` because the wave's target state is candidate/unflipped (admission-stage), which is exactly the pre-registered landing order.

## Environment

No tools installed; no mutations to lane/fleet; scratch under `/tmp/revenger-r70-R70W2CounterReplay*` deleted. No blockers.
