n/a (criterion does not apply) — the entry writes no rejected-sources row and cites no registry-rejected row, so no reject reason or `flip` is owed; **but** the entry carries no Q12 decision at all (`| Q12 |` count = 0), which is an admission-blocking finding under `claims.md` §C1's "n/a only with the entry's named reason" — see §Adjacent finding, which is outside my verdict.

seat: L1Revenger69.R69ReviewEntryQ12 · criterion: **Q12 only** · target bytes:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`
sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`, 35113 bytes, 215 lines
(lane HEAD at review time `35e12584d37434632fa06a6c2975ab55f29a8d3f`; read-only — nothing edited, no
git/jj mutation, nothing written outside this report).

## Criterion as frozen

`corpus/QUALITY.md:24` (Q12):

> A rejected source row states a reject reason grounded in a located quote, and its `flip` names a
> change to the source (a successor or revision) or a scope the reject reason does not exclude.
> — reject when: "the flip asks for content the row already credits the source with, so it can never
> change the verdict (S008, superseded by S024)"; lesson M21 (`corpus/lessons/round-61.md:37`).

My assignment states the applicability rule as "n/a if the entry writes no rejected-sources row".
`corpus/QUALITY.md` admission step 1 adds: "A criterion marked `n/a` names why it cannot apply."
The registry format that makes a row "rejected" is fixed by
`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:34-37`:

```
34: - `teaches` — one grounded learner benefit. Rejected rows read
35:   `REJECTED: <reason>; flip: <what would change the verdict>`.
36: - `status` — `queued` (opened, worth mining) · `mined` (cited by ≥1 path in `used-by`) ·
37:   `rejected` (kept — a rejection is evidence of taste).
```

So the applicability test has two branches, and I checked both: **written** (does the entry author a
rejected row / carry a `flip`) and **cited** (does the entry rest support on a `status=rejected`
row — the stricter reading used by the r64 precedent,
`corpus/knowledge/round-64-firmware-region-byte-evidence.md:220`).

## Evidence — commands and their actual stdout

### 1. Written branch — no rejected row exists in the entry's bytes

Exhaustive reject/refusal/exclusion vocabulary over the whole 215-line file:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && grep -n -i -E \
  "reject|refus|exclud|declin|discard|dropped|withdraw|retired|deprecat|not admitted|non-admitted|stale row|unsuitable|insufficient|supersed|replaced" \
  corpus/knowledge/round-69-apk-axml-byte-evidence.md
2:source: S043 — supersedes S039 — REA reverse-engineer-anything skill reference, "Android application artifacts" (docs, tier A; row mined round 66) — route-scope sentences only: …
6:source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened round 69 by this entry's author) — scope: the machine derivation of every S038 line number and enum value …
127:11. Every S038 line number and enum value this entry states in items 4, 8 and 11 is printed by a committed derivation script … The script refuses to print a line it did not find …
184:| Q14 | pass | … hex without a count clause is excluded. |
```

Four matches, none a rejected source row: `:2`/`:6` are *supersedes* relations inside `source:`
lines (dismissed in §Entry lines at issue), `:127` is the sentence "The script **refuses** to print a
line it did not find", `:184` is "hex without a count clause is **excluded**". There is no `flip`
token and no `rejected:` key anywhere:

```
$ grep -c -i 'flip' corpus/knowledge/round-69-apk-axml-byte-evidence.md
0
$ awk 'NR<=12' corpus/knowledge/round-69-apk-axml-byte-evidence.md | grep -oE "^[a-z-]+:" | sort | uniq -c
      1 admission-status:
      1 coverage-map:
      1 recheck:
      7 source:
      1 verified-at:
$ grep -n -E "^(source|rejected|excluded|flip|admission-status|coverage-map|verified-at|recheck):" \
  corpus/knowledge/round-69-apk-axml-byte-evidence.md | wc -l
11
```

Header is exactly 7×`source:` + `verified-at:` + `recheck:` + `coverage-map:` + `admission-status:`
= 11 keyed lines. No rejected row, no `flip` field — the M21 defect (a flip asking for content the
row already credits) has no surface in these bytes.

### 2. Cited branch — every `S###` the entry names is `mined` or `queued`, none `rejected`

Cited ids in the entry vs registry status (field 9 of the 13-field row, parsed not eyeballed):

```
$ for id in S032 S034 S038 S039 S041 S043 S045 S046 S047; do printf "%s: " "$id"; \
  grep -E "^\| $id \|" corpus/SOURCES.md | awk -F'|' '{print "fields="NF-1" status="$9}'; done
S032: fields=13 status= mined
S034: fields=13 status= mined
S038: fields=13 status= mined
S039: fields=13 status= mined
S041: fields=13 status= mined
S043: fields=13 status= queued
S045: fields=13 status= mined
S046: fields=13 status= mined
S047: fields=13 status= mined
```

The registry holds exactly four `status=rejected` rows, and the entry mentions none of them:

```
$ awk -F'|' '/^\| S[0-9]/ {s=$9; gsub(/^ +| +$/,"",s); if (s=="rejected") print $2"s="$9}' corpus/SOURCES.md
 S008s=rejected
 S012s=rejected
 S024s=rejected
 S025s=rejected
$ for id in S008 S012 S015 S024 S025 S044; do printf "%s mentions=" "$id"; \
  grep -c "$id" corpus/knowledge/round-69-apk-axml-byte-evidence.md; done
S008 mentions=0
S012 mentions=0
S015 mentions=0
S024 mentions=0
S025 mentions=0
S044 mentions=0
```

(`S015`/`S044` are `queued`, not rejected — included only to close the alphabet of "reject-shaped"
ids the earlier grep surfaced.) So even the strict cited branch is clean: the entry neither writes
nor leans on any rejected row.

### 3. The two supersedes relations are not rejections

```
$ awk -F'|' '/^\| S0(39|46) / {printf "%s status=%s teaches: %.200s\n", $2, $9, $8}' corpus/SOURCES.md
 S039 status= mined teaches: That the Android route is documented as taking the caller's APK path for package identity and manifest declarations with a separately supplied JADX prerequisite, so a fixture-only round makes no provider-readiness claim.
 S046 status= mined teaches: Turns the transcribed spec line numbers into a re-derivable command: every anchor is searched in the pinned bytes and a missing or ambiguous symbol is exit 2 — the capture for the M40/M44 anchor class
```

Both superseded rows are `mined`, neither carries a `REJECTED:` teaches cell, and neither is named
in the entry's `used-by`. On the contract's vocabulary (`SOURCES-CONTRACT-v1.md:36-37`) supersession
is a successor relation, not a rejection: `rejected` is a distinct status these rows do not have.

### 4. The entry's own commands re-run (read-only) — no rejected row appears at runtime either

```
$ python3 -B corpus/derive_axml_anchors.py ; echo derive_exit=$?
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum block open : 237
enum RES_STRING_POOL_TYPE : 239 = 0x0001
enum RES_XML_TYPE : 241 = 0x0003
enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
enum RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101
enum RES_XML_START_ELEMENT_TYPE : 247 = 0x0102
enum RES_XML_END_ELEMENT_TYPE : 248 = 0x0103
enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
derive_exit=0
$ python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum ; echo readout_exit=${PIPESTATUS[0]}
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
readout_exit=0
$ python3 -B corpus/fixtures/apk-r65/readout.py | wc -l
15
```

20 derivation lines / exit 0 and 15 readout lines / `507d79f8…` / exit 0 both match the entry's
`recheck:` line (`:9`) and §Reproduce (`:190-192`). Neither output contains a source row, a
`REJECTED:` token or a `flip`, so live re-execution creates no rejected row that the entry would
owe a reason and flip for. (Values are quoted here only to show the commands behave as the entry
says; I scored no other criterion and rely on none of these numbers for my verdict.)

## Entry lines at issue

- `:2` — `source: S043 — supersedes S039 — … — the round-65 draft cited "line 5", which is
  `older server.``. Closest thing in the file to a rejection record, examined and dismissed: the
  located quote (`older server.`) grounds the correction of the *round-65 draft's citation*, not a
  rejection of a source row; S039 and S043 are both non-rejected in the registry
  (`SOURCES.md:53` mined, `:57` queued); it states no `flip`. Nothing is being rejected here, so
  Q12 owes nothing. **Correct as written.**
- `:6` — `source: S047 — supersedes S046 — …`. Same shape: S046 is `mined` (`SOURCES.md:60`), no
  `REJECTED:` cell, no `flip`. **Correct as written.**
- `:175-184` — the §Q-map. **No Q12 row exists** (`grep -c '^| Q12 '` → `0`). This is the only
  place the entry could name an n/a reason and it names none; see §Adjacent finding. Not scored as
  a Q12 violation — Q12's reject condition is a defective `flip`, which is absent — but it is the
  reason this seat's n/a cannot by itself satisfy the frozen §C1 predicate.

There is no line in these bytes that states a wrong Q12 value; the correct Q12 decision is `n/a`
with the reason "no rejected source row is written by this entry", which is exactly the wording the
r68 candidate carried at `corpus/knowledge/round-68-apk-axml-byte-evidence.md:183`.

## Adjacent finding (outside my criterion's verdict — for adjudication)

The §Q-map is materially shorter than the v3 candidate's, and the Q12 decision row is among the
dropped rows. Row-id diff, v3 → v4:

```
$ diff <(grep -oE "^\| Q[0-9]+" corpus/knowledge/round-68-apk-axml-byte-evidence.md) \
       <(grep -oE "^\| Q[0-9]+" corpus/knowledge/round-69-apk-axml-byte-evidence.md)
3d2
< | Q03
6d4
< | Q06
8,10d5
< | Q08
< | Q09
< | Q10
12d6
< | Q12
13a8
> | Q14
$ grep -n "^| Q12 " corpus/knowledge/round-68-apk-axml-byte-evidence.md
183:| Q12 | n/a | no rejected source row is written by this entry. |
$ grep -c "^| Q12 " corpus/knowledge/round-69-apk-axml-byte-evidence.md
0
```

Consequences I can state from the frozen text alone:

1. `reports/round-69/claims.md` §C1 pass branch: "every applicable Q01–Q15 decision of the
   dispatched wave on the landed v4 bytes is **PASS (n/a only with the entry's named reason)**".
   The v4 entry names no Q12 reason, so a wave-recorded Q12 n/a is not entry-backed; the entry's
   own `:11` advertises "a fresh-seat Q01–Q15 all-pass flip" while its map carries 8 rows
   (Q01, Q02, Q04, Q05, Q07, Q11, Q13, Q14).
2. §C1 also defines the candidate as "the round-68 v3 candidate's bytes with **exactly the deltas
   above**" (nine items listed). Dropping six decision rows (Q03, Q06, Q08, Q09, Q10, Q12) is not
   among the nine deltas, so it is an undeclared delta — the same accounting class the round-68
   wave mined as "Q-map not re-derived against the deltas"
   (`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/R68QmapSelfCheck.md`,
   Finding 4).
3. Adjudication options, stated without recommending an edit to landed bytes: either the entry is
   amended to carry `| Q12 | n/a | no rejected source row is written by this entry. |` before the
   final measurement (v3 wording, one line), or §C1's parenthetical is read as satisfied by the
   wave seat's named reason rather than the entry's. My seat's n/a is issued on the substance of
   Q12 and must not be read as satisfying the entry-named-reason clause.

The lane's adjudicated vocabulary for this exact shape is `PASS (correctly n/a)` (r65 round lesson
table: `| Q12 | PASS (correctly n/a) | R65ReviewEntryQ12 | consistent — entry writes no rejected
row |`), but that label was available only because r65/r67/r68 each named the reason at their
`| Q12 |` row. On the v4 bytes there is no such row to affirm.

## Residual risk

1. **Verdict scope.** n/a is correct for Q12's content. It is not a statement that the entry passes
   admission; the Q-map gap above is a different criterion's ground (map completeness / §C1
   predicate), and I have deliberately not converted it into a Q12 FAIL because Q12's frozen reject
   condition — "the flip asks for content the row already credits the source with" — has no surface
   in these bytes (`flip` count = 0).
2. **Registry state read from the working tree.** Statuses were read from `corpus/SOURCES.md` in the
   lane working tree at `35e1258`, not from an archived-tree extraction. A rejected row would have
   to appear in the measured tree to matter, and no cited id is rejected in either state I observed.
3. **Q12's known weak branch.** `corpus/lessons/round-61.md:117` and `corpus/lessons/round-62.md:22`
   record the successor-flip weakness as unresolved criterion debt; it can only reach rows that are
   rejected, and this entry writes none.

## Verification gaps (stated, not filled)

- I scored **Q12 only**. I did not adjudicate Q01–Q11 or Q13–Q15 on these bytes; in particular I did
  not re-verify the item-11 anchor claims, the Q14 hex lengths, or Q15's tree-identity sentence.
- I did not run `corpus/check_embedded_outputs.py` (the C7 gate) on the v4 — the C7 decision belongs
  to the wave's registered gate seats.
- I did not attempt to determine whether the missing six Q-map rows are an intentional freeze-time
  reduction; §C1's nine-item delta list contains no such item, which is all I can assert.

## Tooling

No install or upgrade was made (no pacman/uv/npm/cargo transaction was run — the host's pacman
transactions are paused and none was needed). Only already-present binaries were used: `grep`,
`sed`, `awk`, `diff`, `sha256sum`, `wc`, `sort`, `uniq`, `printf`, `python3 -B`. No `/tmp` scratch
was created, so nothing was left behind; no peer message was sent.

## Report

`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-69/R69ReviewEntryQ12.md`
