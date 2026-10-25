CLEAN — `validate` exits 0 with exactly the four disclosed W04s (S024/S028/S029/S034); the registry is 47 rows (S001–S047, contiguous), and the round-68→HEAD diff is purely additive: `+2 / -0`, the new S047 row plus its search-log entry, with S046 byte-identical.

seat: L1Revenger69.R69CensusReplay · date 2026-10-25 · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · axis: coverage (registry supports C1's S047 citation) + freshness (new row re-derivable today)
reads: `reports/round-69/claims.md` (frozen contract, §Registered "The new registry row S047"), `corpus/SOURCES.md`, `scripts/sources-census.sh`. Writes: this file only. No tool installed; no package transaction.

## 1. Full validate output and exit (the assigned command)

```sh
$ cd /home/vgpnk/Projects/shokunin && bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT_CODE=0
```

FULL output above: 5 stdout lines, no `E01`–`E12` finding, no `W01`/`W02`/`W03`, no `unlisted`. Exit **0**. Per the script header (`scripts/sources-census.sh:27-28`: "W-codes … never change status"; `:22` exit table) this is the clean-with-warnings branch. The four W04s are the same four the lane has disclosed since round 62 (`corpus/lessons/round-62.md:316`, `round-64.md:190`, `round-64-verifier-spotcheck.md:66`, `round-65-verifier-spotcheck.md:54`, `round-66.md:16`, `round-67.md:83`, `round-67-verifier-spotcheck.md:206-208`, `round-68.md:71-74,84`, `round-68-verifier-spotcheck.md:155`).

## 2. Row count

```sh
$ grep -cE '^\| S[0-9]+ ' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
47
$ bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin revenger
revenger	rows	47
revenger	tier.A	45
revenger	tier.C	2
revenger	status.mined	39
revenger	status.queued	4
revenger	status.rejected	4
FLEET	rows	47
EXIT=0
```

47 rows, both counters agree. IDs contiguous S001…S047, no gap and no duplicate id (no `E03` in the validate output; independent scan of `^\| S[0-9]+ ` found no repeated id). Histogram 39 mined / 4 queued / 4 rejected. pr65→now: 45 (r67) → 46 (r68, +S046) → 47 (r69, +S047), i.e. exactly one row added per round, matching `round-68.md`'s "Rows 45 → 46 (only S046 added)".

## 3. S046 / S047 status and used-by

Columns 8/9/10/11 of the 11-column row (`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`):

| row | status | opened | recheck | used-by | target exists |
|---|---|---|---|---|---|
| S046 (`corpus/SOURCES.md:60`) | `mined` | 2026-10-24 | on-release | `corpus/knowledge/round-68-apk-axml-byte-evidence.md` | yes — sha256 `ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e` |
| S047 (`corpus/SOURCES.md:61`) | `mined` | 2026-10-25 | on-release | `corpus/knowledge/round-69-apk-axml-byte-evidence.md` | yes — sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5` |

- Both used-by paths resolve, so no `E11`; both rows are mined with a non-`—` used-by, so no `W03` (which is why the round-69 run drops the `W03 S046 mined but unused` line that `round-68.md:76-84` shows at that round's start).
- S047's `teaches` opens "supersedes S046"; S047's `scope` is the round-69 v4 citation set ("every S038 line number and enum value the round-69 C05 v4 candidate cites, including the enum-block bounds"), S046's is the round-68 set — distinct scopes, so no same-URL/E04 interaction (both are `own-work` local artifacts, not URLs).
- S046 keeps `status=mined` and its round-68 used-by. This is not a deviation: the contract in `corpus/SOURCES.md:4-7` makes rows append-only and allows in-place change of only `status`/`recheck`/`used-by`. The lane's own precedent is identical — S039 stays `mined` (used-by `round-65-apk-axml-byte-evidence.md`) although S043 supersedes it, and S040 stays `queued` although S044 supersedes it. Supersession is recorded in the successor row + search log, never by demoting the predecessor.

S047's own stated facts re-derive (freshness, not taken on the row's word):

```sh
$ sha256sum corpus/derive_axml_anchors.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa   # == the S047 pin
$ sha256sum corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f   # == S047's snapshot copy pin
$ python3 -B corpus/derive_axml_anchors.py > /tmp/revenger-r69-derive.out; echo EXIT=$?; wc -l < /tmp/revenger-r69-derive.out
EXIT=0
20
```
20 output lines (== "20 output lines" in S047), exit 0, line 1 is `sha256 56b88bc4… ResourceTypes.h`, stdout sha256 `f90e342deb01ad384ed020702a7c543e755c107c15d8ace056294a0ef5fa3230`. The enum values the row quotes are printed verbatim (`enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100`, `enum block open : 237`, `enum block close : 263`, `enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180`). The entry cites the row: `corpus/knowledge/round-69-apk-axml-byte-evidence.md:6` = `source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened round 69 …)`, and `:11` still reads `admission-status: candidate` (README not flipped at build time, as C1 requires).

## 4. Diff against the committed round-68 bytes — no row other than S047 changed

```sh
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff refs/heads/main~2 -- \
    /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
diff --git c/corpus/SOURCES.md w/corpus/SOURCES.md
index 686e1cd..ca35952 100644
--- c/corpus/SOURCES.md
+++ w/corpus/SOURCES.md
@@ -58,6 +58,7 @@
 | S046 | AXML anchor derivation — …
+| S047 | AXML anchor derivation (extended) — …
@@ -88,6 +89,7 @@
+- 2026-10-25, round-69 C05 re-gate source opening (S047). Unit: one own-work artifact set — …
EXIT=0
$ git -C … diff --numstat refs/heads/main~2 -- corpus/SOURCES.md
2	0	corpus/SOURCES.md
```

`main~2` = `e1d22ca` (round-69 pre-registration; its SOURCES.md is untouched round-68 bytes — 46 rows, sha256 `3aa3808f011b481f46e15b808caf155c9aae4600249c693a290d6f7ae8c41ecf`). Working tree == HEAD for this file (`git diff --quiet HEAD -- corpus/SOURCES.md` silent), HEAD SOURCES.md sha256 `f562c9f858da3bf5b8f99712cf9c46c05246fd87cf4e8dd166affa1ac05c5b7f`, 100 lines.

**Answer: no.** 2 insertions, **0 deletions** — the added lines are the S047 registry row and the S047 `## Search log` entry (the census "identified 1, screened 1, included 1 row (S047 mined own-work, supersedes S046), excluded 0" record). S046 and every other row are byte-identical; no `status`/`recheck`/`used-by` cell was touched, so the append-only rule holds and no in-place change log was owed.

## 5. The four W04s are pre-existing, not introduced this round

Round-68 bytes validated through a lane mirror (`/tmp/revenger-r69-r68lane`, `corpus/` subdirs symlinked so `E11` resolves, `corpus/SOURCES.md` = `git show refs/heads/main~2:corpus/SOURCES.md`):

```sh
$ bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin /tmp/revenger-r69-r68lane
revenger-r69-r68lane	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger-r69-r68lane	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger-r69-r68lane	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger-r69-r68lane	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger-r69-r68lane	ok	/tmp/revenger-r69-r68lane/corpus/SOURCES.md
EXIT=0
```

Identical warning set, identical exit, 46 rows → the round-69 row addition changed neither the finding set nor the exit code. (Note for other seats: `validate --file PATH` resolves `used-by` against the *lane* root, so a `/tmp` file yields one spurious `E11` per used-by cell — use a lane mirror or the lane path as I did; this is a usage caveat, not a registry defect.)

## 6. Freshness (recheck) — nothing overdue

```sh
$ bash scripts/sources-census.sh overdue --root /home/vgpnk/Projects/shokunin --today 2026-10-25 revenger
revenger	cadence	S001 recheck=90d opened=2026-10-19
… 47 cadence lines, S001–S047 …
revenger	cadence	S047 recheck=on-release opened=2026-10-25
EXIT=0
```

47/47 rows reported under `cadence` (symbolic cadence or an `NNd` window that has not elapsed: S001 `90d` from 2026-10-19 is due 2027-01-17, S014/S015/S030/S031 likewise), so `overdue` finds none and exits 0. S047 opened today (`2026-10-25`) with `recheck=on-release`.

## Verdict

**CLEAN** — exit 0, only the four disclosed W04s; 47 contiguous rows (S001–S047); S046 `mined`/round-68 candidate (unchanged, per lane precedent) and S047 `mined`/round-69 candidate, both used-by targets present; the round-68→HEAD diff is `+2/-0` naming only S047, answered "no row other than S047 changed".

### Handoff notes (not defects, no action taken)
- `corpus/lessons/round-69.md` does not exist yet (`ls corpus/lessons/round-69*.md` → No such file). `claims.md:229` and §Frontier require the round-69 census before→after **with both outputs and exit codes** in that lesson; the closure seat owes that block, and can quote §1 + §5 above as the two receipts (r68 mirror `EXIT=0`, 4 W04s, 46 rows → r69 lane `EXIT=0`, same 4 W04s, 47 rows).
- `corpus/SOURCES.md:92` records S047 colliding with the shokuknow package's staged S047 space; adoption stays closed (wave-4), consistent with `claims.md` §Registered. Read-only campaign tree was not modified.
