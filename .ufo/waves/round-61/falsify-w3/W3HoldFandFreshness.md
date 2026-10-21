GRADE: HOLDS — coverage F and freshness-proxy holds, ab58069 vs base cf02419 (K hold count also intact)

Seat RevengerR61-2.W3HoldFandFreshness, leaf, no delegation. Archives: `git archive --format=tar <commit> | tar -x` into /tmp/revenger-r61w3-W3HoldFandFreshness/{base,landed}; `rev-parse` printed cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 and ab580698212258a55e43e9bb9bf6ac78c91eae2a. Live lane read-only; every run happened in the extracted trees. No REA device, no bytecode or JavaScript execution, no network fetch.

## F — SCORECARD.md:45-57 (observation)
Command at SCORECARD.md:45-57 run verbatim with cwd = each tree root.
- base: `{"analyze_javascript_application": 6, "compare_application_versions": 1, "compare_javascript_export_shapes": 3, "extract_artifact": 2, "inspect_analysis_view": 1, "inspect_artifact": 4, "inspect_evm_interface": 7, "inspect_pe_resources": 30, "trace_application_feature": 2, "trace_javascript_semantics": 2}`
  `COVERAGE 4 / 8 score= 5.0 families= ['native-static', 'javascript', 'archives', 'evm']`
- landed: identical operation counter, identical line `COVERAGE 4 / 8 score= 5.0 families= ['native-static', 'javascript', 'archives', 'evm']`
No drop (5.0 -> 5.0). Mechanical cause: `git diff --stat cf02419 ab58069 -- corpus/live corpus/fixtures` prints nothing, rc 0 — no saved record entered. Same line is recorded at `reports/round-61/measure-after.log:40`.

## Freshness — SCORECARD.md:134 (observation)
Command: `grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)' corpus/knowledge/{seed.md,2026-10-12-rea-readiness-checklist.md}`
- base: `corpus/knowledge/seed.md:12` / `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:6`
- landed: `corpus/knowledge/seed.md:12` / `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:6`
No drop (18 -> 18). Both files are byte-identical across the commits: sha256 `d1d31602f2b667d6c9406743f06dd2f14030cf1fdf477b1da251f2682d7d7534` (seed.md) and `561327faf39fdc9221c3ebc1b2f9e5175a466ca39fb2c37d119be594f085b6e0` (checklist); neither is in the landed diff (8 files under `corpus/`). `measure-after.log:41-42` records the same 12/6. [INFERENCE] the freshness score is therefore unchanged at 18/18; round 61 cannot move this axis because it touches neither counted file.

## Holds — K (observation)
- Amended probe `reports/round-61/measure.py` run by me on both archives, exit 0 both. Base: `K_HELD=4/14 score=2.9`, `K_HELD_BACKED=4/14`, `HOLDS_OK=yes`. Landed: `K_HELD=6/14 score=4.3`, `K_HELD_BACKED=6/14`, `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`. Matches `measure-before.log:37` and `measure-after.log:5,55`.
- Status compare by script over both READMEs: 14 rows each; 12 statuses identical; only C04 and C09 changed `uncovered` -> `held`; base held set {C01, C11, C12, C13} all still `held`; every named `knowledge/*.md` exists in landed. No lost hold.
- All 10 `HOLD` script lines (names, exit codes, tails) are identical between base and landed; only the mutant-b control differs (0/2 base, 2/2 landed), which is C2's measured change, not a hold.
- Harm void `changed saved record or fixture`: `git diff --stat cf02419 ab58069 -- corpus/live corpus/fixtures` empty, rc 0.
- Sources cited by the two entries (S016-S023, S026, S027) are registry-marked `opened 2026-10-21`; tier A except rejected S024/S025 (S025 tier C, rejected). `lessons/round-61.md` `### Sources opened this round` carries the access date and <=25-word located quotes.

## Entry-evidence spot check on my axes (observation)
- Both `## Reproduce` blocks extracted verbatim and run with `python3 -B` from the landed archive root: exit 0; EVM 14 stdout lines, JS 29; `difflib` vs each `## Provenance (Q11)` fence = 0 diff lines. The derivation layer behind both holds reproduces exactly.
- Non-voiding precision notes (not my grade target; reported for the entry seats): (a) `evm-saved-interface-candidates.md:40` "each record's subject digest equals the fixture bytes' SHA-256" is literally true, but for r19 the subject digest `294e6fd2…` is sha256 of `fixture.hex` text, not the decoded 18 bytes (measured `eq_raw=True, eq_decoded=False`); the block's `subject_eq_bytes` is a disjunction, so its printed `True` does not show which carrier matched. (b) `commonjs-destructured-require-edges.md:39` "a single exposed export named `default`" understates the edge count: each graph has 2 `exposes` edges (its own Provenance at :162/:172 prints `'exposes': 2`); sibling W3JsLabelsDefault graded this PARTIAL. Neither changes F, freshness or the K mechanics.

## Unknown
- S016-S023/S024/S025 were not re-fetched by me; tier A "for its scope" there is registry + L1 gate observation, not my independent re-open. Those rows belong to sibling seats (W3EvmSelectorConstants, W3JsQTable).
- Freshness currency beyond the counted rows was spot-checked only at S002: `/home/vgpnk/.agents/skills/reverse-engineer-anything/SKILL.md` (mtime 2026-10-20) still has `metadata.version: "42"`, `tool_count: 207` and `rea-agents@6.7.0` at lines 37-56, so both entries' "host skill now names 6.7.0" limitation is current.
- I did not re-adjudicate Q01-Q13 admission; the probe, F and freshness are the only measurements I own here.

VERDICT: F holds at 4/8 = 5.0 on both sides; freshness holds at 12+6 = 18 on both sides with byte-identical files; K moves 4/14 -> 6/14 with no lost hold, probe exit 0 and HOLDS_OK=yes on both. No drop and no harm on the assigned axes.
Installs: none.
