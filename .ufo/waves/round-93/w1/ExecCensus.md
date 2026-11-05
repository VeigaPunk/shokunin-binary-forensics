# ExecCensus — round 93 w1, round-mechanics receipts (mid-round; L1 re-runs the census at round end)

Seat: ExecCensus (leaf; no subagents spawned, no mutating git/jj, nothing installed).
All receipts live in `.ufo/waves/round-93/w1/ExecCensus/`. Checked 2026-11-05 ~14:52 UTC.

## 1. Census receipts (census-mid.log, counts.txt)
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → **EXIT=0**, final line `ok`; **33 warnings = 21× W01 + 12× W04, 0× E** — exactly the disclosed warning classes, no error class. (r79's L0 line noted 31 W then; +2 since is consistent with this round's rows not yet landed.)
- Manual census (fleet CORPUS.md census block): **rows 494**, **malformed 0** (the block's `NF!=13` check prints 0 as required).

## 2. No-harm receipt (noharm.log)
- Lane HEAD = `02050cb2a6758e3bd9cec696ff0e42df6f23511a` (the freeze commit itself).
- `git diff --stat 02050cb…` → **empty output, exit 0**; `git status --porcelain` → only `?? .ufo/waves/round-93/`.
- Verdict: **no-harm HOLDS** — zero tracked modifications anywhere; frozen files under reports/round-93/ byte-untouched. No defect.

## 3. Assimilation collision count (collisions.txt)
- Frozen r67/r70/r91 method (`comm -12` of sorted unique row ids) over lane `corpus/SOURCES.md` vs `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md` (READ-ONLY; no shokuknow script run).
- lane_rows=494, staged_rows=155, **COLLISION_COUNT=155 — matches the expected 155**; ids are S047–S201 contiguous, i.e. every staged id collides (mass id drift). Nothing adopted; supports claims.md's "Assimilation: expected none" posture and the still-open L0 r91 (:304).

## 4. L0 inventory (l0-open.txt)
- 7 open `revenger |` lines in `/home/vgpnk/.ufo`→`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`: rounds **67 (:146), 68 (:156), 69 (:160), 73 (:221), 74 (:233), 79 (:248), 91 (:304)**, openings quoted in l0-open.txt. Nothing appended.

## 5. Scratch discipline observation
- `ls /fast/scratch/hyaku/revenger-r93/` (run twice, 11:49 and 11:52 ls-local): 19 dirs, all created 2026-11-05 11:40–11:52 (same clock) → **none older than 90 minutes; no defect observation**. Other seats' dirs left untouched; my own (empty) `ExecCensus/` scratch dir deleted before yielding.

## Defects
None observed. (Mid-round snapshot: the L1's round-end census re-run is the authoritative before→after.)
