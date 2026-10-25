# R69SpotcheckDiscern — outside-discernment spot-check (adjudication aid, not a verdict)

**AGREE (both checks) — the S047 row's anchor re-derives verbatim from the bytes it names, and the tier-A enum line facts (244/245, 237–263) match the snapshot bytes.** No edits made; one source row + one tier-A claim set checked.

- seat: `L1Revenger69.R69SpotcheckDiscern` (independent leaf, no subagent dispatch)
- date: 2026-10-25 · lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
- contract read first: `reports/round-69/claims.md` (sha pinned counter `bca74e6d…`; not re-derived here — out of this seat's scope)
- tools installed/updated: **none** (used standing `python3`/`sha256sum`/`awk`/`grep`; pacman paused host-wide, no transaction attempted)

## Check 1 — S047 row: located quote vs actual stdout, and both pinned digests vs disk — **AGREE**

Target row: `corpus/SOURCES.md:61` (`| S047 | AXML anchor derivation (extended) … own-work | A | …`).

Command (read-only; `cwd` = lane root, matching the script's usage header):

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py
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
EXIT=0
```

Byte-exact quote test (not a substring-of-eyeball test):

```
$ grep -Fx 'enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100' <stdout>
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
EXACT_QUOTE_PRESENT=yes
$ wc -l < <stdout>   →  stdout_lines=20
$ wc -c < <stderr>   →  stderr_bytes=0
```

The row's recorded located quote — `enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100` (`corpus/SOURCES.md:61`) — is present verbatim in the actual stdout. The row's `20 output lines` claim matches the observed 20 stdout lines.

Digests, row vs disk (both tokens extracted programmatically from the row; the row carries exactly two 64-hex tokens):

```
row S047: script sha256   74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa
          snapshot sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f

$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
```

Both match disk exactly (`matches disk` ×2). The script's own stdout `sha256` line also prints the same snapshot digest, i.e. the pin inside the script and the row agree with the bytes read.

Corroborating: the row is genuinely the frontier row this round claims — row is `own-work`, tier `| A |`, opens as `S047` and self-describes as superseding `S046` (`corpus/SOURCES.md:60` = S046, `:61` = S047, both present; no key collision), and the v4 candidate cites it in its header: `corpus/knowledge/round-69-apk-axml-byte-evidence.md:6` carries the identical script sha `74d4c0d9…`, the identical snapshot sha `56b88bc4…`, and `20 output lines`.

## Check 2 — tier-A enum line facts in the entry vs the wave-65 snapshot bytes — **AGREE**

Source of truth named by the case: `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`.

```
$ awk 'NR>=237 && NR<=245 || NR==263 {printf "%d: %s\n", NR, $0}' ResourceTypes.h
237: enum {
238:     RES_NULL_TYPE                     = 0x0000,
239:     RES_STRING_POOL_TYPE              = 0x0001,
240:     RES_TABLE_TYPE                    = 0x0002,
241:     RES_XML_TYPE                      = 0x0003,
242:
243:     // Chunk types in RES_XML_TYPE
244:     RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:     RES_XML_START_NAMESPACE_TYPE      = 0x0100,
263: };
```

Per-fact result:

| fact asserted | bytes at that line | result |
|---|---|---|
| :245 is `RES_XML_START_NAMESPACE_TYPE` | `RES_XML_START_NAMESPACE_TYPE      = 0x0100,` | **AGREE** |
| :244 is `RES_XML_FIRST_CHUNK_TYPE` | `RES_XML_FIRST_CHUNK_TYPE          = 0x0100,` | **AGREE** |
| enum opens at :237 | `enum {` | **AGREE** |
| enum closes at :263 | `};` | **AGREE** |

The entry states exactly these (`corpus/knowledge/round-69-apk-axml-byte-evidence.md:1`, `:153`): block `237-263` with `enum {` :237 / `};` :263, `:244` = `RES_XML_FIRST_CHUNK_TYPE` (0x0100), `:245` = `RES_XML_START_NAMESPACE_TYPE`. The v3 number-drift `237-253` range is not present in the v4 entry; the only `237-263` readings are the corrected bounds, and the :253 line the entry names is `RES_XML_RESOURCE_MAP_TYPE` (0x0180), consistent with the derivation's `:253 = 0x0180`.

Transfer audit (why this snapshot may stand in for the script's input): the two files are identical by digest and size, verified, not assumed —

```
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
86255 .ufo/waves/round-65/source-snapshots/ResourceTypes.h
86255 corpus/snapshots/ResourceTypes.h
```

## Limits of this spot-check

- Two artifacts only: source row **S047** and the tier-A enum line-fact subset of the C05 v4 entry. This is **not** an adjudication of Q01–Q15, the counter labels (`K_HELD_BACKED`, `C05_SINGLE_V4`, `HOLDS_C2_V4`, `C7_V4_CLEAN`, `Q15_*`), or C1/C2. No counter run, no C7 gate run, no Q15 checker run.
- Only the enum-block and struct-anchor lines the derivation prints were compared; struct *widths* (item 5's manual table) and the readout/oracle/fixture bytes were not re-derived here.
- Both files were read at working-tree state; nothing was compared against a git object id at an archived commit (tree-identity is C2/Q15's ground, not this seat's).
- No writes outside this report; nothing edited in `corpus/`, no git mutation, no subagent dispatch, no peer messaging.

## Cleanup

`/tmp/revenger-r69-discern.out`, `/tmp/revenger-r69-discern.err` removed. Remaining `/tmp/revenger-r69-*` entries belong to sibling seats and were left untouched.

## Artifact paths

- this report: `.ufo/waves/round-69/R69SpotcheckDiscern.md`
- evidence read: `corpus/SOURCES.md:60-61`, `corpus/derive_axml_anchors.py`, `corpus/snapshots/ResourceTypes.h`, `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`, `corpus/knowledge/round-69-apk-axml-byte-evidence.md:1,6,59,153,177-178`, `reports/round-69/claims.md`
