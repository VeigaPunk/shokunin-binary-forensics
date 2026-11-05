# MutationR93 — report (round 93, wave 1)

Lane commit: `02050cb2a6758e3bd9cec696ff0e42df6f23511a`.
Full per-mutant table, diff lines, deciding trees and proofs: `.ufo/waves/round-93/w1/MutationR93/mutants.md`.

## Outcome

- Mutants: 21 = 13 C1 legs + C1 gate + 6 C2 legs + C2 gate.
- **KILLED 20/21**, **EQUIVALENT 1/21** (`C2_NO_NEW`), **SURVIVED 0/21**.
- Every kill is single-leg isolated: the pristine counter's only failing leg on the deciding
  tree is the mutated leg (plus the verdict echo), and each mutant still passes the honest
  positive fixture.
- Equivalence (`C2_NO_NEW`): proved from `ROWS_TOTAL` + `ONLY_C08` + the base status set
  (no `frontier` cell at base) + `C08_TOKEN`; the probe flags a row only when it is `frontier`,
  so no tree flips the verdict through this leg. Three trees show the mutant fails wherever the
  pristine fails. Same class as the r92 n03 precedent.
- Verdict-gate mutants (`all(legs.values())` → `True`): the do-nothing tree kills both
  (C1: 11 legs fail plus the verdict echo; C2: `C2_C08_TOKEN`).

## Defects found

- None in the frozen counters: no leg is dead, no leg is redundant except the proven-equivalent
  `C2_NO_NEW`, and both positive fixtures and both do-nothing controls reproduce.
- Coverage note, not a counter defect: `C2_NO_NEW` is verdict-redundant at this base. Keep it
  as defense-in-depth; the routed kill tree (for a future round) is a frontier row with a planted
  matching record while `ONLY_C08` is loosened.

## Integrity

- Frozen sha256 before = after for `c1_k_admit_counter2.py`, `c2_legend_counter2.py`,
  `forge_battery.py`, `claims.md` (`logs/frozen-before.sha256` vs `logs/frozen-after.sha256`).
- `git status --porcelain` before and after: `?? .ufo/waves/round-93/` only.
- Mutants and trees lived in scratch only; scratch removed after copying. No lane path was written.
- No tools installed or upgraded.

## Artifacts (wave dir)

- `MutationR93/mutants.md` — per-mutant table and NO_NEW proof.
- `MutationR93/harness.py` — the harness that produced every outcome.
- `MutationR93/results.json` — 23 result rows (21 mutants, plus extra NO_NEW demonstration trees).
- `MutationR93/logs/` — original, mutant and positive-mutant logs for every row, plus hashes.
