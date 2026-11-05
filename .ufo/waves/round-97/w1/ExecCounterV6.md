# ExecCounterV6 — v6 admission counter + red-before controls (wave w1)

## Axis claims (C1=C1, C2=C2)
- C1 (coverage, row C02 partial->held through v6): NOT SCORED this wave (freeze order binds; L1 scores the landing tree after this wave returns). This seat builds the counter and its red-before fixtures only.
- C2 (calibration, 19 frozen forgery vectors): v6 refuses 19/19 of the CriticR96 deltas (FG01-FG20 minus FG17) with a named failing leg each, and still accepts the honest fixture (positive control). The battery in claims.md (`forge_reach6.py`) is scored by the L1 afterwards; this seat ran v6 against the same 19 deltas rebuilt via the v5 generator + `drv.py` forge functions.

## Files written
- `reports/round-97/c1_k_admit_counter6.py` (new; `python3 -B -m py_compile` exit 0)
- `reports/round-97/controls/red-v5-corpus-prefix.log` (rc=1, `C1_SOURCES=fail`)
- `reports/round-97/controls/green-v6-corpus-prefix.log` (rc=0, `C1_SOURCES=pass`)
- `reports/round-97/controls/red-v5-decorated.log` (rc=0, `C1_ADMITTED_UNION=pass`)
- `reports/round-97/controls/green-v6-decorated.log` (rc=1, `C1_ADMITTED_UNION=fail`)
- `reports/round-97/controls/base-v6.log` (rc=1, `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15`)
- `reports/round-97/controls/selftest-v6.log` (rc=0, `SELFTEST... legs=34`)
- `.ufo/waves/round-97/w1/ExecCounterV6/v5-v6.diff` (265 lines, diff rc=1 = files differ)
- `.ufo/waves/round-97/w1/ExecCounterV6/vector-table.txt` (per-vector refusing leg)
- `.ufo/waves/round-97/w1/ExecCounterV6.md` (this file)

## Changed legs (tied to M5/M6/M7/scratch/vector)
1. M5 — `check_sources` used-by: strip a leading `corpus/` from each cell entry before the exact `[ENTRY_REL]` comparison, so both `corpus/knowledge/<f>` (census) and `knowledge/<f>` (fixture) pass exactly once; no other part of the leg changes.
2. M6 — `check_admitted_union`: admission-status regex anchor dropped from `admitted\s*$` to `admitted`, so `admission-status: admitted (...)` is detected as admitted and refused unless named in the coverage union. New self-test delta `DECOR-shadow-admitted` (expected `C1_ADMITTED_UNION`, passing).
3. M7 — self-test label: `total = 1 + len(EXPECT_FAIL) + 1` (positive + per-delta + do-nothing) instead of `len(EXPECT_FAIL)+2` (off by one once EXPECT_FAIL grew); prints `legs=34` for 34 executed legs.
4. Scratch — `_scratch()` honours `HYAKU_SCRATCH` else `tempfile.gettempdir()` (TMPDIR); new global `WORK_ARG` set by a top-level `--work` flag; `main()` and `self_test()` both place temp work under `Path(WORK_ARG)` when given. No hardcoded `/tmp` writes; no `revenger-r96` hardcoded path beyond the retained workdir name `c1v5` (scratch root still resolved from the env).
5. Vector hardening (minimal, byte rules only, no vector/file/digest special-casing):
   - FG01 M6 (above); FG02 recursive `rglob` of `corpus/knowledge`; FG03 suffix case-fold (`.MD`); FG04 decode `errors="replace"` instead of skipping undecodable files.
   - FG05 strip `<!--...-->` HTML comments before seat/digest checks; empty visible content fails.
   - FG06 reject any symlink component in the artifact path; require the resolved artifact under the seat's own dir (not just the wave dir).
   - FG07 widen SID collection to `[Ss]\s*\d{2,}` with full whitespace removal + upper-case normalisation, so `S  0999` / `s0888` normalise to `S0999`/`S0888` and fail C1_SIDS/C1_SOURCES.
   - FG08 also fail on any loose `*.pyc` file under the surfaced dirs (not only `__pycache__`).
   - FG09 require each receipt's `quote` to contain the pinned reference substring for its sid (S502 decompile route; S503 shipped-artifact evidence sentence).
   - FG10 require each RECEIPT_ROW_IDS row's `fetch_url` to appear in the SOURCES row URL (url-drift).
   - FG11/FG15 new leg `C1_DERIV_TABLE`: a 64-hex token on a row naming the fixture path must equal the actual committed fixture sha256; derivation-row Q-tags must lie in the pinned Q01-Q17 set. (FG15 previously passed v5; now refused here.)
   - FG12/FG16 new leg `C1_ADMITTED_WS`: any admission-status line's leading whitespace must be ASCII spaces only (no tabs) and no U+00A0 anywhere in the status line.
   - FG19 require a per-sid `-`-prefixed fetch-log line containing sid+sha; a merged `S502 S503` line is rejected.
   - FG13, FG14, FG18, FG20 already refused by v5 legs (C1_ADMITTED, C1_TRIO, C1_SOURCES, C1_ADMITTED) — kept as regression guards (observed failing).

## Per-vector table (v6 refuses all 19; honest fixture passes)
See `.ufo/waves/round-97/w1/ExecCounterV6/vector-table.txt`. Summary (vector -> refusing leg, observed rc):
FG01->C1_ADMITTED_UNION rc1; FG02->C1_ADMITTED_UNION rc1; FG03->C1_ADMITTED_UNION rc1; FG04->C1_ADMITTED_UNION rc1; FG05->C1_VOTES rc1; FG06->C1_VOTES rc1; FG07->C1_SIDS rc1; FG08->C1_PYCACHE rc1; FG09->C1_RECEIPTS rc1; FG10->C1_SOURCES rc1; FG11->C1_DERIV_TABLE rc1; FG12->C1_ADMITTED_WS rc1; FG13->C1_ADMITTED rc1; FG14->C1_TRIO rc1; FG15->C1_DERIV_TABLE rc1; FG16->C1_ADMITTED_WS rc1; FG18->C1_SOURCES rc1; FG19->C1_RECEIPTS rc1; FG20->C1_ADMITTED rc1. Honest fixture: C1_VERDICT=pass rc0.

## Exact counting-command outputs (observed)
- `python3 -B -m py_compile reports/round-97/c1_k_admit_counter6.py` -> COMPILE_OK (rc 0)
- v5 on corpus-prefix fixture: `C1_SOURCES=fail`, `C1_VERDICT=fail` (rc 1, red-v5-corpus-prefix.log)
- v6 on corpus-prefix fixture: `C1_SOURCES=pass`, `C1_VERDICT=pass` (rc 0, green-v6-corpus-prefix.log)
- v5 on decorated fixture: `C1_ADMITTED_UNION=pass`, `C1_VERDICT=pass` (rc 0, red-v5-decorated.log)
- v6 on decorated fixture: `C1_ADMITTED_UNION=fail`, `C1_VERDICT=fail` (rc 1, green-v6-decorated.log)
- v6 on base archive 7d380ce: `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15` (rc 1, base-v6.log)
- v6 --self-test --work <scratch>: `SELFTEST_C1V5=pass legs=34` (rc 0, selftest-v6.log)
- diff v5->v6: rc 1 (265 lines)

## Risks / blockers / open questions
- Two new legs (`C1_DERIV_TABLE`, `C1_ADMITTED_WS`) enlarge the leg set beyond v5's printed names; the brief says to keep every v5 leg name "except where item 1-4 require a change" — these two are required to refuse FG11/FG15/FG12/FG16. Flag for L1 to confirm the verdict-line format tolerance (`C1_<LEG>=pass|fail` one per leg still holds).
- `check_sources` now also enforces the per-sid URL match (FG10) and receipt quote pinning (FG09); both were verified not to break the honest fixture, but the L1's landing tree must pass them too.
- Retain-workdir name `c1v5` kept inside `SCRATCH` for continuity; scratch root is env-driven. If the L1 wants `c1v6`, that is a one-token change.
- No candidate scoring was run; the landing tree was not touched. No commits made.
- Tools: only python3 stdlib (no installs).

