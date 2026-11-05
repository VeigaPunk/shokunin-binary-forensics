# ExecCensus — census validate + assimilation collision check (round 95, wave 1)

Read-only over the registry. Lane: revenger (`corpus/SOURCES.md`). No lane file, no git
write, no write into /home/vgpnk/Projects/shokuknow (its file was read only).

## 1. Census validate

Command: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`

| run | locale | rc | findings |
|---|---|---|---|
| run 1 (transient) | default | **1** | `E01 S500 fields=10`, `E01 S501 fields=10` (+ the W01/W04 set) |
| run 2 (settled) | default (en_US.UTF-8) | **0** | `ok` line, 21 × W01, 13 × W04, 0 E |
| run 3 (settled) | LC_ALL=C | **0** | byte-identical TSV to run 2 (`diff` of sorted output: SAME) |

Settled result, matching the expected shape: rc 0, 0 E, W01 and W04 warnings present.

Run 1 was a transient state, not a registry defect. `corpus/SOURCES.md` had mtime
2026-11-05 14:36:41, while run 1 was in progress. In the same window my own inspection
showed S500 (line 517) and S501 (line 518) with 11 columns (awk NF=13 with -F'|'), the
same field count the census gawk applies. Runs 2 and 3 saw the settled file and pass. Raw
outputs are kept in the wave dir:
- `census-validate.tsv` (run 2, the settled result, 35 lines)
- `census-validate-LC_ALL-C.tsv` (run 3, identical)
- `census-validate-run1-transient.tsv` + `.stderr` (run 1, rc 1)

Disclosed: a second writer touched `corpus/SOURCES.md` during this seat's run. The census
rc on the settled file is 0. The lane owner should confirm the final SOURCES.md bytes at
landing. The census gate is not affected either way (E01 only appears in the transient
run).

## 2. Assimilation collision check (frozen §10 block)

| step | rc |
|---|---|
| grep registry ids (`corpus/SOURCES.md`) | 0 |
| grep staged ids (`shokuknow/merge/revenger/SOURCES.append.md`, read only) | 0 |
| `comm -12` collisions | 0 |

`wc -l` of the three files (in the assimilation dir):

- `reg-ids`: **501**
- `staged-ids`: **155**
- `collisions`: **155**

A fresh re-run on the settled SOURCES.md gives the same reg-ids and collisions (`cmp`
identical to the first run). The staged file has no mtime change since 2026-10-24, so the
staged side is stable.

**Collision count: 155 (nonzero).** Every staged id collides: the 155 collisions equal the
155 staged ids.

## 3. What it means for this round

Nonzero means: adopt nothing. All 155 staged ids (the collision list runs S047 through
S201) are already registry ids in this lane, so no staged row is admissible under the
collision rule. L0 `revenger | round-91` stays open. This matches the round claims'
expectation ("none", 155/155 staged-id collisions, L0 unanswered).

Disclosed: the census run-1 E01 (transient) is not a collision or an adoption signal. The
collision count itself was stable across both checks.
