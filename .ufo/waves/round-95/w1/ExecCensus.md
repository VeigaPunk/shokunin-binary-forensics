# ExecCensus — round 95 wave 1 findings

Seat: ExecCensus (executor, leaf, read-only). Lane: revenger. Assignment: census validate
plus the frozen §10 assimilation collision check. Full detail:
`.ufo/waves/round-95/w1/ExecCensus/census-assimilation.md`.

## Results

1. **Census validate** (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`):
   - settled runs: **rc 0**, 0 E, 21 × W01 and 13 × W04 (expected shape). Default locale
     and LC_ALL=C give byte-identical output.
   - one transient run returned **rc 1** with `E01 S500 fields=10` and `E01 S501 fields=10`.
     `corpus/SOURCES.md` was modified (mtime 14:36:41) while that run was in progress.
     Re-runs on the settled file show S500/S501 with the full 11 columns and pass.
2. **Assimilation collision check** (frozen §10 block, greps and comm rc 0):
   - `reg-ids` = 501 lines, `staged-ids` = 155 lines, `collisions` = **155**.
   - A fresh re-run gives the same counts.

## What the count means

Nonzero, so **adopt nothing**. All 155 staged ids already exist in the lane registry.
L0 `revenger | round-91` stays open. This matches the round claims' expectation.

## Disclosures

- The census rc 1 in one run was a transient read of a file another writer was changing.
  Reported, not hidden: raw outputs for all three runs are in the wave dir.
- I made a bad edit to my own output file (`census-assimilation.md`) mid-run: a mistyped
  path plus a `PUT 1*:` that replaced the first block with `x`. I rewrote the whole file
  from the verified results. The lane is untouched; only my wave-dir file was affected.
- Scratch `/fast/scratch/hyaku/revenger-r95/ExecCensus/` removed. Nothing written to
  shokuknow, the fleet root, or any lane file.
- Installs: none.
- No sub-spawns; no labrat probe used (none needed).

## Files written (all under the wave dir)

- `ExecCensus.md` (this report)
- `ExecCensus/census-assimilation.md`
- `ExecCensus/census-validate.tsv` (settled run, rc 0)
- `ExecCensus/census-validate-LC_ALL-C.tsv` (settled run, rc 0)
- `ExecCensus/census-validate-run1-transient.tsv` + `.stderr` (rc 1, transient)
- `ExecCensus/assimilation/{reg-ids,staged-ids,collisions}`

## Checks for the main agent to run

- Re-run the census validate against the landed `corpus/SOURCES.md` (expect rc 0, 0 E).
- Re-run the §10 collision check on the landed file (expect `collisions` = 155 unless the
  lane registry changes).
