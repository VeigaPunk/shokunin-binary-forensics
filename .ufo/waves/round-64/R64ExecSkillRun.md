# R64ExecSkillRun

- **Files changed:** `.ufo/waves/round-64/exec-skill-run.md` (probe transcript), `.ufo/waves/round-64/R64ExecSkillRun.md` (this report).
- **Behavior:** Probe stopped before checklist execution because `/tmp/revenger-r64-skill/SKILL.md` was unavailable. Its required runnable commands were not guessed or substituted; no commands were executed, so there are no probe exit codes/last lines.
- **Exact retained evidence:** `read` returned `Path '/tmp/revenger-r64-skill/SKILL.md' not found`; `glob` returned `Path not found: /tmp/revenger-r64-skill`. The saved baseline in `reports/round-64/measure-before.log` states `K_HELD_BACKED=7/14`, `K_HELD_BACKED_STRICT=7/14`, `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `HOLDS_OK_V2=no`.
- **Risks/blockers:** Missing checklist prevents verbatim execution and outcome comparison; this is the sole blocker. Frozen baseline lines are reference data, not results of this probe.
- **Tooling:** No installs or updates.

Report: `.ufo/waves/round-64/R64ExecSkillRun.md`