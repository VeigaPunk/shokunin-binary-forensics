SOUND — all four assigned checks pass on committed evidence; one live observation (the package's staged-id space drifted mid-round, which strengthens rather than weakens the claims' by-document obligation) plus one cosmetic note (prose-row slice ids carry a trailing backtick).

Seat: R67CriticAssim · scope: item 10 wave-4 quarantine posture attack · contract read: reports/round-67/claims.md §Assimilation posture (lines 9-29), §Registered (line 148).

## Check 1 — slice re-derivation: byte-identical, 26 rows

Re-ran the frozen derivation verbatim from claims.md:18-19:

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin && awk -F'|' -v l='revenger' \
  '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md \
  > /tmp/r67-slice-readerive.txt
diff -u .ufo/waves/round-67/assimilation/quarantine-slice /tmp/r67-slice-readerive.txt
→ DIFF: IDENTICAL ; wc -l → 26
```

Composition verified: `grep -c 'payload-absent' quarantine-slice` → 24; rows 25-26 are the two prose rows S054/S099 with class text "the cited source could not be fetched, so no quote was checked" (quarantine-slice:25-26). Every line carries an S-id. Matches claims.md:22-23 exactly.

Cosmetic note (not a defect): the prose rows emit `S054`` / `S099`` with a trailing backtick (the register's pipe-split lands the closing backtick of the prose cell on $4). The id is still recoverable and `register-rows.json:170-183` keys them cleanly as `S054`/`S099`; seat verdicts are addressed by id, so no ambiguity results.

## Check 2 — nothing appended or copied: SOUND

- `git diff fa0eb3eb HEAD -- corpus/` → only `M corpus/SOURCES.md`, `A corpus/check_embedded_outputs.py`, `A corpus/knowledge/round-67-apk-axml-byte-evidence.md`. The SOURCES.md delta is exactly 2 insertions, 0 deletions: the new S045 row (sources table) and the round-67 search-log line — this lane's own row, not a package row.
- The lane S045 row text is independently worded (scope = "the declared `header_item` field semantics … of one authored `classes.dex` member"; snapshot sha256 `c0428612…`) vs the package's staged row S055 for the same URL (scope = "what the `.dex` format does not define", different anchors, dated 2026-10-23). Not a copy.
- Filename collision check: `LC_ALL=C comm -12` over `ls corpus/knowledge/` (14 files) vs package `knowledge/corpus/knowledge/` (83 files) → empty intersection. No package knowledge file copied.
- `git status --porcelain` → only untracked `.ufo/waves/round-67/*` wave scratch and `corpus/lessons/round-67.md` (the registered lesson file, claims.md:150); no modified tracked files beyond the committed build delta; nothing outside `.ufo/waves/round-67/` + `corpus/lessons/round-67.md` is dirty.
- Grep for `shokuknow|merge/revenger|SOURCES.append` inside corpus/ hits only `corpus/lessons/round-67.md:11` — the posture statement itself, not copied content.

## Check 3 — id-collision evidence: SOUND, with a mid-round package drift observation

- Files exist and are consistent: `reg-ids` (44 lines, S001–S044) re-derives byte-identically from the claim-base registry: `git show fa0eb3eb:corpus/SOURCES.md | grep -oE '\| S[0-9]+' | sort` diff → IDENTICAL. `staged-ids` (146 lines, S045–S190). `collisions` is a committed 0-byte file; independent recompute `comm -12 <(sort reg-ids) <(sort staged-ids) | wc -l` → 0. At capture, lane next-id S045 did collide with the staged id space — claims.md:25-27 correctly calls this a by-document renumber obligation ("URL/anchor is the evidence; the id follows it"), never arithmetic.
- Observation (evidence that the obligation is real, not a claims error): the committed `staged-ids` no longer re-derives from the CURRENT `SOURCES.append.md` — deriving now yields S046–S196 (151 rows), i.e. staged S045 is gone and S191–S196 were added. File mtimes: staged-ids committed 20:49; SOURCES.append.md mtime 21:17 — the package mutated after the evidence snapshot. `MERGE-REPORT.md:109` now records the durable fact the claims posture depends on: staged `S055` ↔ lane row S045 are the same document ("the lane's own row(s): S045" in the package's own overlap table). So the arithmetic view of the collision is already stale while the document-level obligation is confirmed by the packager's own tooling — exactly why "renumber by document" is the only safe rule. The committed evidence is labeled "pre-append" (claims.md:24) and is a correct point-in-time snapshot; adjudication should not treat `staged-ids` as re-derivable against the live package.
- S045 snapshot verified: `.ufo/waves/round-67/source-snapshots/dex-format.html`, 281157 bytes, sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` — matches claims.md:46-47.

## Check 4 — S054/S099 classification: correctly `unverifiable-unreachable`, not fabrication

- Register class (register-rows.json:172,179): "the cited source could not be fetched, so no quote was checked" — an unchecked-fetch state, not a checked-and-absent finding; the JSON notes mark both "prose-class row (register unchecked family; staged-row quote checked separately)". claims.md:22-23 carries the same reading.
- Both URLs are in fact currently reachable from this lane: S054's URL (`source.android.com/docs/core/runtime/dex-format`) is the very document this lane fetched as S045 (snapshot sha256 above); S099's seat fetch evidence already sits at `.ufo/waves/round-67/quarantine/S099/source.bin` (280121 bytes, HTML document). Reachability-now ≠ reachability-then, but it confirms the register's fetch failure was a fetch event, not a fabrication signal — the classification holds and the quote-check obligation stays open for the seat verdicts.

## Residual exposure (reported, not counted against the posture)

- Per-row verdicts are still in flight: only 9 of 26 seat directories exist under `.ufo/waves/round-67/quarantine/` and `corpus/lessons/round-67.md`'s Gate table is still the "(filled from wave reports at adjudication)" template — consistent with a live wave; the ≥1 admit + ≥1 reject spot-check surface (claims.md:148-149) is not yet populated, so that registered item remains unverifiable at this timestamp, not failed.
- Tooling: none installed (reused awk/diff/comm/git/sha256sum only); pacman untouched per the pause ruling.
