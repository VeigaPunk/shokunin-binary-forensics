# ExecControls — findings (round 97 w1, C1 coverage / C2 calibration)

## Files created
- `reports/round-97/controls/skip-work/stub_always_pass.py` (S-B)
- `reports/round-97/controls/skip-work/stub_always_fail.py` (S-C)
- `reports/round-97/controls/skip-work/count_summary.py` (S-F)
- `reports/round-97/controls/c2-count-audit.log` (S-F log with rc)
- `reports/round-97/controls/skip-work-table.md` (paper table, 6 rows)

## Observed runs (PYTHONUTF8=1 python3 -B)
- S-B stub_always_pass.py: `C1_VERDICT=pass`, `C1_K_HELD_BACKED=13/15`, rc=0
- S-C stub_always_fail.py: `C1_VERDICT=fail`, rc=0
- S-F count_summary.py: `accepted 14/19`, accepted_list FG01,FG02,FG03,FG04,FG05,FG06,FG07,FG08,FG09,FG10,FG11,FG12,FG15,FG19, rc=0 (logged to c2-count-audit.log)
- S-A do-nothing: observed v5 copied from committed `reports/round-97/controls/c1-do-nothing-v5.log` (`C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15`, only failing leg `C1_SOURCES=fail`); expected v6 same.
- S-D id-edited copy: applied `admission-status: candidate -> admitted` in scratch copy of base archive (flip rc=0, line 8); README C02 still `partial` and SOURCES used-by unchanged; expected v6 failing legs `C1_C02_HELD`, `C1_ONLY_C02`; v6 not run per freeze order.
- S-E hand-fit lookup table: recorded in table; frozen predicate is a rule about bytes, not names (claims.md §C2 and §C1), so a name table must not be accepted.

## Notes
- Scratch at /fast/scratch/hyaku/revenger-r97/ExecControls removed (rc=0) after use.
- No git mutations; `git status --short` shows only the new files above as untracked.

## Checks for main agent
- Re-run the three scripts with `PYTHONUTF8=1 python3 -B` and confirm rc=0 and outputs above.
- Score S-A/S-D/S-B/S-C/S-E with the committed v6 counter + forge_reach6 battery after the freeze.
