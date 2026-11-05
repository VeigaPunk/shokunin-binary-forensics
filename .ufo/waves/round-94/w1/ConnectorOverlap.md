# ConnectorOverlap — revenger round 94, attempt 1 (seat report)

Seat: `ConnectorOverlap-26` (connector, leaf, read-only on the lane). Lane tip at scan: `060a8e8` (round-94 freeze). Frozen claims read in full: `reports/round-94/claims.md` (unchanged; not edited). Deliverables are in `.ufo/waves/round-94/w1/ConnectorOverlap/`; this file is the scoped findings the task's `Report:` trailer names.

## 1. Sibling overlap scan — `ConnectorOverlap/overlap.md`

Scanned the fleet round-93 and round-94 reports (kaidoku, kake, lore, mori; revenger r93) and the 2026-11-05 MANIFEST closures. Overlap with revenger's province (saved-ledger evidence craft, source-registry discipline, admission gates):

- **kake** (r93 admitted; r94 honest stop): r94 built a strict successor counter with eight false-green routes (refused 8/8; frozen r93 counter admits 7/7). Quote-anchor defects (hyphenation breaks) corrected before landing. Merge package collides 8/129. → REPORT.
- **kaidoku** (r93 rejected; r94 admitted): r93 frozen v3 counter raised `TypeError` writing its receipt on the honest input; r94 successor v4 imports the frozen verdict code by sha pin and changes only the writer. Supersession by new row (S318, S319). → REPORT: positive controls should exercise the writer path.
- **mori** (r93 and r94 landed): r94 R02 — the v1 admission check `count-c1.py:141` used `ac[:7] in va` (substring); v2 requires a ≥7-char prefix of the admission `%h` as the first `verified-at` token. Registry debt: 31 prefix-only digest rows, S125 unpinned. → REPORT: candidate predicate, needs its own freeze.
- **lore** (r93, r94 admitted): `corpus/tools/map_obligations.py` checks map rows against source obligations one-to-one — the coverage-map ↔ record instrument family. → REPORT only.
- Method-only overlaps from the MANIFEST: kotodama r92 (named-counterfeit refusal battery), kotoba r90 (mutation battery over own gates). → REPORT.
- Standing, not re-read this round: tabi `adjacency.tsv:5` and tsukuroi `PROVINCE.md:150-152` (both contested-open on browser/CDP scope); carried from the r93 scan.

Nothing is absorbed. Revenger should report, not absorb, the five items listed in `overlap.md` §3.

## 2. considerthese proposal 2 re-measurement — `ConnectorOverlap/measurement-r94.tsv`

Methodology (also in the TSV header): r89–r92 carried from the r93 baseline; re-verified unchanged (`git diff --numstat 02050cb 060a8e8` over SCORECARD, lessons, reports/round-89..92: 233 insertions, 0 deletions). r93 read at the adjudication tip `28b5f99` (SCORECARD.md:1762–1763) and the spot-check at `9876cb3` (spotcheck:47, :60). r94 frozen at `060a8e8`, no landing → pending, counted 0.

| round | claims | verdict class of record | counted invalid |
|---|---|---|---|
| r89 | C1 MISS, C2 KILLED | failed / failed-killed | 2 |
| r90 | C1 met-contested, C2 met-not-verified | — | 2 |
| r91 | C1 met-contested, C2 met-not-verified | — | 2 |
| r92 | C1 met-contested, C2 met-contested | — | 2 |
| r93 | C1 met-contested, C2 met-contested | — | 2 |
| r94 | pending (frozen, no verdict) | — | not counted |

- Total: **10 of 10 invalid, running rate 100%**. Met-on-counter subset (r90–r93): 8 of 8 contested or not-verified.
- Sub-class: 2 outright counter-failures; 6 met-but-contested; 2 met-but-not-verified.
- Caveats recorded in the TSV: (C-spot) the r93 spot-check's own wording ("met — re-measured", "met on the frozen predicate — evidence-verified") would class both r93 rows as clean met, giving 8/10 = 80%; the headline follows the SCORECARD verdict cell, the verdict of record. (C-closure) the MANIFEST r93 closure marks calibration "improved"; axis-level closures are not counted. (C-post-fix) r93 is the first post-fix reading (successor counters); r94 has no reading yet.
- Report only. Adopting a criterion would need its own frozen predicate; the lane decides.

## 3. Shokuknow merge package — adoption state

`/home/vgpnk/Projects/shokuknow/merge/revenger/MERGE-REPORT.md` exists (155 accepted, 0 refused, 87 knowledge entries; nothing written to the lane). Adoption is closed on the 155/155 id collisions (r94 `ExecCensus/collision-run.log`) and the unanswered L0 line `.ufo/l0-questions.md:304`. Nothing adopted.

## 4. Verification exercised

- `measurement-commands-r94.sh` run once; output saved to `ConnectorOverlap/measurement-r94.receipt.txt` (exit 0). It covers the drift check, r93 verdict cells and lesson/spot-check anchors, r94 freeze state (claims present, no lesson, no `## Round 94` heading, 0 commits after freeze), MANIFEST revenger closures (r90–r93; none for r94), and the adoption-state lines.
- Not run: no frozen counter was executed (not assigned; the lane's own counters are for the L1 and the sentinel).

## 5. Bounds and host state

- Writes: only `.ufo/waves/round-94/w1/ConnectorOverlap/` and this file (path named by the task's `Report:` trailer, one level above my seat directory — written there as instructed).
- Scratch `/fast/scratch/hyaku/revenger-r94/ConnectorOverlap` used for extracted bytes and deleted by the script on exit (verified absent).
- No lane file, sibling file, fleet-root file, `.ufo/state`, watchdog log, or shokuknow file was written. No git write command was run. No network use. No tool installed; no sudo; no subagent spawned.
- No `__pycache__` created (no Python counter was imported; the MANIFEST read used `python3 -c` with `json` only).

## 6. Routed for the lane (not decided here)

- Decide whether mori's first-token admission rule and kake's false-green battery warrant a successor predicate of their own.
- Decide whether the r93 spot-check wording or the SCORECARD verdict cell governs the frozen-counter validity rate (80% vs 100%).
- Operator: the `revenger | round-91` L0 line remains the adoption blocker.
