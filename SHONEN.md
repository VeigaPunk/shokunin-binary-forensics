# revenger-shokunin — Promotion checklist

Promotion to shokunin requires all of:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  Lane attestation, not a non-author check: the named verifier `revenger-r64.R64ReviewSkill` is a
  seat this lane dispatched (`.ufo/waves/round-64/R64ReviewSkill.md`), and it re-stated
  `[x]`-ready = YES on the round-64 bytes of `SKILL.md`, which resolve with
  `git show cab8085a5fe4e222090edb223755ac1d747386db:SKILL.md` (size and digest are derived by
  piping that command to `wc -c` and `sha256sum`; none is quoted here, so none can drift).
  The current `SKILL.md` has no outside confirmation; routed need: a non-lane reviewer
  re-confirming the CURRENT bytes (round-69 verifier spot-check V7,
  `corpus/lessons/round-69-verifier-spotcheck.md`). Citation sweep 0 phantoms
  (`R64ReviewSkillCites`); checklists executed verbatim with observed exits matching promises
  (`R64ExecSkillRun` transcript). Historical checks in `corpus/live/runs/promotion-review-r5.md`
  remain narrower history only.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  Fixture-scoped saved-ledger replay + real producer record verification:
  `reports/round-64/measure-after.log` (frozen counter over archived corpus),
  `corpus/live/runs/round-63/` record verified (Evidence ID re-derived from the
  shipped package by `R64ReviewRecord`); no producer rerun this round.
- [~] Instructions executable by an agent without oral context
  `SKILL.md` runnable sections executed by `R64ExecSkillRun` (census 4/4, replay 10/10,
  oracle ORACLE OK, counter exit 0); no independent outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  Entry `## Cross-lane scope note (Q10)` + README C07 parenthetical report-not-absorb
  ADJ-06 (fleet `.ufo/l0-questions.md:42` open); connector scan `R64ConnectorOverlap`;
  no province sentence edited; no outside verifier this round.
