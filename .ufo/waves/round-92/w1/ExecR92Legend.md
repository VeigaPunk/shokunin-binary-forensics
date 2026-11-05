# Report — ExecR92Legend (round 92, w1): independent C2 legend cross-check

Lane HEAD at check time: `9402183a9492428fa0064d250746c62a0a2d9ca5` (freeze commit).
Output file: `.ufo/waves/round-92/w1/ExecR92Legend/legend-crosscheck.md`.

## What was done

1. **Record census.** Parsed all 135 `*.json` under `corpus/live/runs/`; 78 carry a
   truthy top-level `operation` — matches the frozen probe's `SAVED_RECORDS=78`
   (0 parse failures). Eight records carry one of the six in-scope ops; full table
   (path, operation, sibling-receipt exit_code, oracle result) in
   `legend-crosscheck.md` §1. Highlights: `round-76/inspection.json`
   (`inspect_managed_artifact`, exit 0, no oracle block in receipt);
   `round-77/inspection.json` (`inspect_web_page`, exit 0, no oracle block in
   receipt); six round-85 records (managed artifact/members/native-boundaries,
   exit 0, receipts state `ORACLE OK (20/20|47/47|39/39 checks)`).
   `capture_browser_scenario` / `observe_web_session`: zero records.
2. **C08 determination.** The round-77 CDP records carry `confidence="observed"`,
   `evidence_id`, populated `normalized_result`, passing receipts, and **zero**
   rejected/quarantine/admission-status markers (byte-level scan). They are **work
   evidence**, not rejected candidates and not quarantined material — and not
   admitted knowledge either (no admitted entry covers the browser surface; only
   `candidate`-status files mention adjacent tools). Legend-correct C08 token:
   `uncovered`.
3. **Frozen probe reproduced independently** (git archive HEAD corpus → scratch,
   `cd /`, TMPDIR under scratch, `reports/round-66/measure.py` unmodified):
   `K_HELD=8/15 score=5.3`, `K_HELD_BACKED=8/15`,
   `README_TOKEN_LEGEND_MISMATCH=2 rows=['C03', 'C08']`.
4. **Frozen counter run** (`c2_legend_counter.py --rev HEAD`): `C2_LEGEND_MISMATCH=2
   rows=['C03', 'C08']`, `C2_ROWS_COUNT=15`, `C2_K_HELD=8/15 C2_K_HELD_BACKED=8/15`,
   `C2_ROWS_TOTAL=pass`, `C2_C08_CLEAR=fail`, `C2_NO_NEW=fail`,
   `C2_NO_UNBACKED=pass`, `C2_VERDICT=fail`, exit 1 (do-nothing base state,
   matching `controls/c2-do-nothing.log`).

## Agreement

Probe and counter agree exactly on the mismatch rows (`['C03', 'C08']`) and held
counts (8/15, 8/15). Per-row verdicts: C03 should read `uncovered` on the
committed tree (managed records exist, no admitted entry; `held` only if the C1
entry lands admitted); C08 should read `uncovered` (round-77 CDP record exists,
no entry claimed).

## Defects

None in the frozen counter or probe. Notes: working tree at check time had
`M SKILL.md` and untracked `.ufo/waves/round-92/` (other seats'/L1 activity, not
touched); the frozen counter uses its own scratch `$HYAKU_SCRATCH/revenger-r92/c2/`
by its frozen code.

## Bounds

Read-only over the lane (git rev-parse/status/log/archive only); writes confined
to `.ufo/waves/round-92/w1/ExecR92Legend{,.md,/}` and scratch
`/fast/scratch/hyaku/revenger-r92/ExecR92Legend` (deleted before yield). No tool
installs; no subagents; no mutating git/jj; no frozen file modified.
