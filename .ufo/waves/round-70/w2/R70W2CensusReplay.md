CENSUS-CLEAN — live lane validate exits 0, rows 47→49 (S048, S049 only), W03 clear, no E-code at base or tip; the single new W04 (S048 vs S045) is honest and independently substantiated.

seat: R70W2CensusReplay · round 70 / wave 2 (falsify) · target commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`)
base: `3f5edbc206351232a3d2d801334dd930499ccaf5`
script under test: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`
tools: GNU Awk 5.4.1 (pre-existing), curl 8.23.0 (pre-existing) — no installs, no pacman transactions.

## 1. Live lane (expected exit 0) — PASS

```
$ cd /home/vgpnk/Projects/shokunin && ./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	W04	S048 duplicate url source.android.com/docs/core/runtime/dex-format across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT=0
```

`census` mode on the live lane root: `revenger rows 49 | tier.A 47 | tier.C 2 | status.mined 41 | status.queued 4 | status.rejected 4`, `FLEET missing 0`, EXIT=0.

Script selftest (operability of the instrument, not of the lane): `./scripts/sources-census.sh selftest` → every mutant `killed`, final line `selftest ok`, EXIT=0.

Live lane `corpus/SOURCES.md` sha256 `a1ba476e47afba33ad0b018e54acb7349bb33c73c95be1c30e2fc8d50c206523` — byte-identical to the tip archive extraction, so the working tree's registry is the landed registry (the only uncommitted lane edits are `SCORECARD.md`, `SHONEN.md`, `corpus/lessons/round-70.md`, `.ufo/` wave files).

## 2. Base vs tip, from `git archive` extractions

Extraction roots (`--file <tree>/corpus/SOURCES.md`, so the script resolves `dir = <tree>`):
- base `/tmp/revenger-r70-CensusReplay/base` ← `git -C … archive 3f5edbc… corpus`; SOURCES.md sha256 `f562c9f858da3bf5b8f99712cf9c46c05246fd87cf4e8dd166affa1ac05c5b7f`
- tip `/tmp/revenger-r70-CensusReplay/tip` ← `git -C … archive 17ee7f8… corpus`; SOURCES.md sha256 `a1ba476e47afba33ad0b018e54acb7349bb33c73c95be1c30e2fc8d50c206523`

| metric | base | tip | delta |
|---|---|---|---|
| rows | 47 | 49 | +2 (S048, S049) |
| tier.A | 45 | 47 | +2 |
| tier.B | 0 | 0 | 0 |
| tier.C | 2 (S012, S025) | 2 (S012, S025) | 0 |
| tier.invalid | 0 | 0 | 0 |
| status.mined | 39 | 41 | +2 |
| status.queued | 4 (S007, S040, S043, S044) | 4 (same ids) | 0 |
| status.rejected | 4 (S008, S012, S024, S025) | 4 (same ids) | 0 |
| status.invalid | 0 | 0 | 0 |
| malformed rows (NF≠13) | 0 | 0 | 0 |
| duplicate ids | none | none | — |
| id sequence | S001…S047 contiguous | S001…S049 contiguous, no gap | +2 |
| `validate` exit | 0 | 0 | — |

`validate` output diff base→tip is exactly one added line (the S048 W04); no E-code, no W01, no W02, **no W03** at either end.

W04 set, with the row it collides with (tip): S024↔S008 (rejected), S028↔S016, S029↔S022, S034↔S032, **S048↔S045**. Only S048 is new; S049's URL (`raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/…/android-applications.md`) collides with nothing. Correction to the brief: the new duplicate-URL warning is **S048-vs-S045 only** — there is no S049 duplicate.

## 3. W03 clear — confirmed two ways

- `sources-census.sh validate` prints no `W03` for base, tip, or live lane.
- Independent recomputation over the tip table (`status=mined` and `used-by ∈ {—, empty}`) prints **nothing**; both new rows carry a real `used-by`: S048 and S049 → `corpus/knowledge/round-70-apk-axml-byte-evidence.md`, which exists at the tip (`git cat-file -e 17ee7f8:corpus/knowledge/round-70-apk-axml-byte-evidence.md` → exists), so E11 is also clear.

## 4. Is the new W04 honest? — YES

The warning is factually correct: S045 and S048 both carry `https://source.android.com/docs/core/runtime/dex-format`, at *different scopes*, and S048 declares `supersedes S045` in its `teaches` cell (so E04's same-scope/no-supersedes condition does not apply — W04 is the right class). Two independent tests of whether the supersede is substantive rather than bookkeeping:

(a) **S045's locator is wrong, S048's is right** — checked against the committed snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` (sha256 `c0428612…`, 281157 bytes) and against my own live fetch:

```
$ grep -nE '<h2 id=' <snapshot> | (4700<n<6000)
4825:<h2 id="file-layout" …>File layout</h2>
4964:<h2 id="definitions" …>Bitfield, string, and constant definitions</h2>
5580:<h2 id="string-syntax" …>String syntax</h2>
5921:<h2 id="items" …>Items and related structures</h2>
$ sed -n '5926p;5035p' <snapshot>
5926: <h3 id="header-item" data-text="header_item" …>header_item</h3>      ← enclosing h2 = 5921 "Items and related structures"
5035: uint ENDIAN_CONSTANT = 0x12345678;                                  ← enclosing h2 = 4964 "Bitfield, string, and constant definitions"
```
S045 says the table is under `"File layout" → header_item`; the `header_item` table is not under `File layout` (h2 at 4825) but under `Items and related structures` (h2 at 5921). S048's stated correction is exactly right, and the four quoted phrase rows (5949 checksum, 5956 signature, 5981 header_size, plus 5035 ENDIAN_CONSTANT) resolve verbatim at the cited lines in **both** the committed snapshot and my live fetch.

(b) **S048's live-vs-snapshot claim reproduces** — `curl` fetch on 2026-10-25:

```
dex_http=200 size=281161          # S048 claims 281161 bytes  → exact
$ diff live-dex.html <committed snapshot>
8946c8946  <script nonce="Cahh2tivBKDRLG1bVQxMNvr9Dtl/3L">   vs  nonce="R1GN4pA7+nDrYJ/dulpbEJ8pQlLBzr">
8951c8951  … devrel-devsite/prod/v5a0f9ff8… app_loader.js …   (same URL, loader line)
```
Only two lines differ, i.e. "differs from the committed snapshot only in the per-request CSP nonce and one devsite loader line" holds; the 4-byte size delta is the nonce-length delta.

(c) **S049's supersede of S043 reproduces** — the reason given ("S043 names a repo path `skills/...` that returns HTTP 404 at the tag") is true:
```
new path .agents/skills/…/android-applications.md → http=200 size=1992 sha256 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c
old path skills/…/android-applications.md        → http=404
```
1992 bytes / `412d9cb4…` are byte-identical to the committed snapshot `corpus/snapshots/rea-android-applications.md` in the tip tree and in the live lane — so the row's "byte-identical to the committed snapshot" claim is literally true, not asserted.

(d) **Scope discipline is honest, not widened to hide the duplicate.** S048's scope cell deliberately drops `magic` and `file_size` (S045's scope had both), and the entry fences itself the same way — `round-70-apk-axml-byte-evidence.md:101` states the four fields S048 covers "checksum, signature, header_size and endian_tag" and explicitly excludes `magic`, `format…`; `:292`/`:302` fence the provider route to S049's documented scope. Tier A for both new rows is defensible (first-party AOSP spec page; the tool's own reference doc for what it documents) and consistent with the pre-existing S043/S045 rows' tiers.

(e) **Row hygiene of the two additions:** S048 `docs/A/mined/2026-10-25/180d`, S049 `docs/A/mined/2026-10-25/on-release`, both `used-by` the new entry; `opened` is today (not future → no E08), `recheck` valid (no E09), inside `## Registry` (no E12), `used-by` path exists (no E11). Snapshot anchors named by the rows all exist at the tip with the digests the rows print: `corpus/snapshots/dex-format.html` `c0428612…` (281157), `corpus/snapshots/rea-android-applications.md` `412d9cb4…` (1992), `corpus/snapshots/APPNOTE.TXT` `0b993022…`, `corpus/snapshots/ResourceTypes.h` `56b88bc4…`.

S045's `used-by` is unchanged base→tip (`corpus/knowledge/round-67-apk-axml-byte-evidence.md`), which matches claims.md's frozen landing order — the S045→round-70 re-point happens at admission (step 4), not at the candidate landing. Not a defect at this tip.

## 5. Frozen manual census, run from the lane root

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
### rows
49
### malformed (must be 0)
0
### tier histogram
A=47 C=2 
### status histogram
mined=41 queued=4 rejected=4 
### duplicate ids (must be empty)
### enum violations (must be empty)
### missing used-by paths (must be empty)
### sha256 lane SOURCES.md
a1ba476e47afba33ad0b018e54acb7349bb33c73c95be1c30e2fc8d50c206523  corpus/SOURCES.md
```

Same seven commands replayed inside each extraction (`cd $D/base`, `cd $D/tip`, relative `corpus/SOURCES.md`): base → `47 / 0 / A=45 C=2 / mined=39 queued=4 rejected=4 / (empty) / (empty) / (empty)`; tip → `49 / 0 / A=47 C=2 / mined=41 queued=4 rejected=4 / (empty) / (empty) / (empty)`. Manual and maintained-parser numbers agree at both ends, so the maintained parser is not masking a row the frozen awk misses.

## 6. Observations (non-blocking, no kill)

- **O1 — S048's pinned live digest is not reproducible by design.** My independent fetch returned the same size (281161) but sha256 `dde39228c5624e272b2d4ad888da8781f44d99c8a412a60a062ffbdbf0660aa9`, not the row's `d72efc55…`, because the CSP nonce is per-request. The row discloses exactly this cause and the substantive content (size, the two differing lines, every cited line number) reproduced, so the row is honest; but any future reader who treats `d72efc55…` as a re-derivable pin will "fail" it spuriously. A snapshot-anchored digest (the committed `c0428612…`, which *is* stable) is the re-derivable one, and S048 does carry it too.
- **O2 — brief correction.** The wave brief describes an "S048/S049-vs-S045 duplicate-URL warning"; the registry actually emits one new W04, S048-vs-S045. S049 shares no URL with any row. Recording this so the L1's report does not cite a warning that the script never printed.

## 7. Verdict

**CENSUS-CLEAN.** Base 47 rows (A45/C2; mined39/queued4/rejected4) → tip 49 rows (A47/C2; mined41/queued4/rejected4); the two additions are S048 and S049, both `mined`, tier A, with existing `used-by` and resolving snapshot anchors; W03 clear at base, tip and live lane; every W04 accounted for (four pre-existing + S048, all cross-scope, all with a real same-URL partner row); no E-code and exit 0 on the live lane, on the tip extraction, and on the base extraction; frozen manual census outputs agree with the maintained parser and print nothing on the three must-be-empty checks. The new S048 warning is honest — its supersede of S045 corrects a real mislocated quote (field table is under "Items and related structures", not "File layout"), its live-vs-snapshot diff claim reproduces, and S049's supersede of S043 reproduces as a 404→200 with a byte-identical snapshot.

Caveat on scope of this verdict: it is a registry/census-axis result only. It does not decide Q01–Q15 on the landed candidate and cannot raise or lower C1; C1's kill rule is judged on the wave-2 Q decisions on the entry bytes.
