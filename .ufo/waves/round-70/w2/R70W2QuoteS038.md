# R70W2QuoteS038 — source freshness re-open of S038 / S032 / S034

**Verdict: OPENED-AND-IDENTICAL** — live S038 (AOSP ResourceTypes.h @ android-15.0.0_r1) and live S032/S034 (PKWARE APPNOTE.TXT 6.3.10) are byte-identical to the committed lane snapshots; every anchor entry items 11 and 12 rest on checks out at the same line numbers in the live bytes.

## Fetch receipts

- Fetch time: 2026-10-25T21:49:37Z (UTC).
- Live source 1: `https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h?format=TEXT` (gitiles base64), decoded with `base64 -d`.
  - Served size 86255 bytes; sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`.
  - `cmp -s` vs `corpus/snapshots/ResourceTypes.h` (landed 17ee7f8 and working tree identical): exit 0. Byte-identical.
- Live source 2: `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT`.
  - Served size 174585 bytes; sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`.
  - `cmp -s` vs `corpus/snapshots/APPNOTE.TXT` (landed and working tree identical): exit 0. Byte-identical.
- Both hashes/sizes equal the registry rows: S038 (56b88bc…, 86255), S032/S034 (0b993022…, 174585). First raw-URL attempt (`/raw/refs/tags/…`) returned HTTP 404; the gitiles `?format=TEXT` form succeeded (recorded because the registry text suggests both forms).

## Item 11 anchors (in live ResourceTypes.h)

Entry `corpus/knowledge/round-70-apk-axml-byte-evidence.md` item 11 says the derivation prints every cited S038 line number and the spec-quote locator prints the `attributeStart` comment line. Live grep results:

```
686:    // Byte offset from the start of this structure where the attributes start.
687:    uint16_t attributeStart;
237:enum {
244:    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
263:};
```

- attributeStart comment: line 686, quote (12 words): "Byte offset from the start of this structure where the attributes start." — field declaration `uint16_t attributeStart;` at line 687. Matches entry output lines `comment attributeStart : 686`, `field attributeStart : 687` and `MATCH ResourceTypes.h: first line 686` (entry:141, :142, :149).
- Chunk-type enum block: opens line 237 (`enum {`), closes line 263 (`};`) — no other `enum {`/`};` lies between 237 and 263 (adjacent closes at 235 and 263). `RES_XML_FIRST_CHUNK_TYPE` line 244, `RES_XML_START_NAMESPACE_TYPE` line 245 (0x0100). Matches entry `enum block open : 237`, `enum block close : 263`, `enum RES_XML_FIRST_CHUNK_TYPE : 244`, `enum RES_XML_START_NAMESPACE_TYPE : 245` (entry:131, :134, :135, :140).

## Item 12 anchors (in live APPNOTE.TXT)

Entry item 12 prints where each ZIP record layout sits in the snapshot. Live grep results:

```
387:   4.3.7  Local file header:
511:   4.3.12  Central directory structure:
632:   4.3.16  End of central directory record:
```

- §4.3.7 heading line 387; transcribed field lines 389–399 (local file header signature 0x04034b50 … extra field length 2 bytes). Matches entry `MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399` (entry:171).
- §4.3.12 heading line 511; transcribed field lines 522–538 (central file header signature 0x02014b50 … relative offset of local header 4 bytes). Matches `MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538` (entry:172).
- §4.3.16 heading line 632; transcribed field lines 634–646 (end of central dir signature 0x06054b50 … .ZIP file comment length 2 bytes). Matches `MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646` (entry:173).

## Conclusion

Live bytes at fetch time are byte-identical to the committed snapshots for all three registry rows (S038; S032/S034 share the APPNOTE.TXT document). No staleness, no drift. All anchors item 11 and item 12 rest on are present at the exact printed line numbers in the live sources. Freshness holds; no DIFFERS or UNREACHABLE conditions.
