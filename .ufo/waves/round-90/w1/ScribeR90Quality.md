# ScribeR90Quality — round 90 w1 (revenger), drafts for r89 routed D1–D3

Freeze read first: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md`
(lane HEAD `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`). Nothing outside this dir and
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Quality.md` was written in the lane.

## Deliverables (all in `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Quality/`)

| file | content |
|---|---|
| `quality-row.md` | Q17 row (Q16 is the highest id, `corpus/QUALITY.md:28`; Q17 unused), clause→evidence table, red probe, proposed check contract |
| `checklist-correction.md` | line 67 quoted exactly; append-only `Correction (round 90, 2026-11-04):` paragraph naming `corpus/live/runs/round-89/` → `reports/round-89/rejected-android-record/` |
| `mistakes.md` | three `## Mistakes` rows (class · evidence pointer · captured-by · fix) for D1, D2, D3 |
| `sm2-receipt.log` | D3 receipt: two runs of `corpus/self_assessment_check.py` with commands, checker sha256, all SM values and exit codes |
| `d1-dead-path-probe.log` | scratch probe output + its source (red for Q17) |

## Measurements (exercised)

- D3: `git archive <rev> corpus SHONEN.md SCORECARD.md SKILL.md` extracted in scratch;
  `TMPDIR=… python3 -B corpus/self_assessment_check.py --root TREE --lane <lane>`:
  - `2b017fa3…` → `SM1=0 SM2=1 SM3=0 SM4=0 SM5=0 SM6=1 SELF_MISMATCH=2`, exit 1
  - `c8cc585c…` → `SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=1 SELF_MISMATCH=1`, exit 1
  - checker sha256 `82e59fce5647f27727644d121dd73641bc14a7bb3293d7e54f2070b0db0335cc` at HEAD and inside both archives. The r89 "SM2 1 → 0" holds.
- D1 probe (mine, not the named instrument): `SOURCE_PATH_DEAD_PROBE=2` — S481 `source` and anchor at `corpus/SOURCES.md:498`; 83 path tokens checked. Relocated receipt re-read: :6, :20, :31 match S481's quoted anchors.

## Findings for the L1

1. **`reports/round-90/source_path_check.py` is absent at the freeze.** Q17 as drafted names it;
   landing Q17 without that file would make the row's own pointer dead (Q17's own class). Either
   land the check (contract proposed in `quality-row.md`) or reword the clause. Not a frozen
   instrument for C1/C2, so adding it does not touch the claims.
2. D2's fix belongs in the round-90 lesson's `## Gate`: carry the source-opening table inline
   for every new row, including the S481-superseding row and the two C2 source rows that
   claims.md:90-95 promises.
3. Live old-path pointers: only SOURCES.md:498 (S481) and the checklist :67. Hits in
   `corpus/lessons/round-89-verifier-spotcheck.md` and `reports/round-89/*` are historical
   records of the move, so they are not sweep targets (my call, stated for the judge).
4. Probe limits: it reads only backticked `corpus/`/`reports/` tokens in S-row `source`/`anchor`
   cells; knowledge entries, LOG.md, lessons, unbackticked paths and `.ufo/` are not covered by it.

## Out of scope / not done

No lane file outside my dir was edited. No commit, no VCS mutation, no tool installs (none needed;
RULES.md not consulted for that reason). Scratch `/fast/scratch/hyaku/revenger-r90/ScribeR90Quality`
was deleted after the receipts were copied.
