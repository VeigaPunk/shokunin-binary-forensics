# R61 baseline census — ScoutCensusBaseline-10 (read-only)

Extraction root `/tmp/revenger-r61-ScoutCensusBaseline-10-base`, built with
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar e0a4b0c4348ef1fade46539f520e94fa140c4d8a corpus | tar -x -C /tmp/revenger-r61-ScoutCensusBaseline-10-base`
→ base hash `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`, equal to live `git rev-parse HEAD`; `jj bookmark list` shows `main: umxqnzkr e0a4b0c4`, `jj status` work copy `b1924489 (empty)`, only untracked `.ufo/waves/round-61/`. `git status --porcelain corpus` empty.
Corpus tree id `7404111557505c03bdc6fa526a9fb18669bc45c6` at both claim base `cf02419` and `e0a4b0c`, so `reports/round-61/measure-before.log` is corpus-current for this base.
Live corpus files byte-identical to extraction (sha256): `SOURCES.md c1573b2fbc284493096ddb20af506122aea0bcf7bc6b5a037b7dc31988f55f30`, `README.md 98738c2b16de9d848f55e003907aec9f365294b4dd95f58e487d00e7cf3d4c78`, `QUALITY.md 2072be286a3556559e86e3310fcfc4d025d64210ae40ccd0e8a98152f97ca33b`.

## Seven frozen census commands (run from the extraction root; exact output)

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
15
```
```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0
```
```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
A=14 C=1 
```
```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
mined=12 queued=1 rejected=2 
```
```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# (no output; rc=0)
```
```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; ...enum checks...}' corpus/SOURCES.md
# (no output; rc=0)
```
```sh
awk -F'|' '...mined used-by paths...' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
# (no output; rc=0)
```
Command 6/7 bodies are the CORPUS.md §Census text verbatim; the only abbreviation here is this report's ellipsis, and both printed nothing.
Seventh-command caveat: the extraction holds only `corpus/`. All 12 mined used-by cells point inside it (`corpus/knowledge/...`), so no non-corpus path is silently skipped (checked with awk on column 12).

## Maintained parser

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT=0
```
Same parser on the extracted registry: `file	ok	/tmp/revenger-r61-ScoutCensusBaseline-10-base/corpus/SOURCES.md`, EXIT=0. `census` mode: rows 15, tier.A 14, tier.C 1, status.mined 12, status.queued 1, status.rejected 2, missing 0. `overdue --today 2026-10-21`: all 15 rows are symbolic cadences (`90d`/`180d`/`on-release`), opened 2026-10-19, none overdue; EXIT=0.

## Cross-check: counting probe on this tree

`python3 -B reports/round-61/measure.py /tmp/revenger-r61-ScoutCensusBaseline-10-base` → exit 0; `K_HELD=4/14 score=2.9`, `K_ROW C04 status=uncovered`, `K_ROW C09 status=uncovered`, `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=0/2`, `C2_D2_KILLED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10` — identical to `measure-before.log`.

## Baseline facts C1 must move

- Coverage map: 14 rows (`corpus/README.md:26-40`), statuses held=4 (C01, C11, C12, C13), partial=4, frontier=4, uncovered=2 (C04 `README.md:30`, C09 `README.md:35`). `grep -cE '^\| C[0-9]+ ' = 14`, `... '| held |$' = 4`; no `corpus/knowledge/*.md` mentions C04 or C09 (`grep -ln` → none), matching `uncovered`.
- Registry: 15 rows, S001–S015; only non-mined are S007 queued, S008 rejected, S012 (tier C) rejected. Every row's opened column is `2026-10-19`; nothing was opened 2026-10-21, so a round-61 Q01 citation requires a new row dated this round.
- `QUALITY.md` has Q01–Q11 (`QUALITY.md:23` defines Q11), but `corpus/README.md:9` still says "admission criteria Q01–Q10" — stale index line C1's gate should not rely on (authority: `README.md:3` points at QUALITY.md).
- `corpus/README.md:44-45` says statuses "before this round's admissions are frozen at `a7acc20`". Observed `git show a7acc20:corpus/README.md`: held=0, partial=6, uncovered=4 (C04 and C09 uncovered). The operative pre-round baseline is the `e0a4b0c` state, held=4/14; a7acc20 would read 0/14. Pre-registration uses the correct 4/14.
- `git rev-parse --abbrev-ref HEAD` prints `HEAD` (detached at e0a4b0c; jj colocated). `git log -1 main` = `e0a4b0c`, matching the stated branch.

## Unknowns

- C2 mutant behaviour was not re-adjudicated (out of my read-only census remit); the probe reproduction above is the only C2 evidence I observed.
- Nothing outside `corpus/` was extracted (no `LOG.md`, `.ufo/`, `reports/`); used-by is corpus-internal, so command 7 is not weakened. Installs: none (no tool installed or upgraded).

Report: .ufo/waves/round-61/build/ScoutCensusBaseline.md

VERDICT: Baseline is exactly the pre-registered one — 15 registry rows (A=14/C=1, mined=12), K_HELD 4/14 with C04/C09 uncovered, receipt-mutant b 0/2, all census and validate checks clean at e0a4b0c; two pre-existing doc drifts (README Q10 count, a7acc20 status pointer) are recorded but do not alter the measured baseline.
