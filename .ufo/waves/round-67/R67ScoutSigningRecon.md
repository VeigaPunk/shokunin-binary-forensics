PRESENT — official APK Signing Block spec located at source.android.com; magic "APK Sig Block 42" (16 bytes, hex `41504b2053696720426c6f636b203432`); block sits immediately before the ZIP Central Directory.

# R67ScoutSigningRecon — frontier recon only (no row, no claim)

Recon for a FUTURE round's C05 frontier claim. This round claims nothing from it; fetched bytes live under /tmp only.

## Located source

- URL: https://source.android.com/docs/security/features/apksigning/v2 ("APK signature scheme v2", AOSP, docs tier A per the corpus tiering used for S045)
- Fetched: `curl -sL --max-redirs 15 -o /tmp/r67-apksigning-v2.html` → 169,743 bytes, sha256 `b930f042b49f7b73d28fcb6b135181fa9d9c7acbde58ec75b8f536c5c61986a8`
- Tier note [INFERENCE]: same publisher/authority class as registry S045 (`/docs/core/runtime/dex-format`), so likely tier A docs if mined in a future round.

## Located constants and format (observed in fetched doc)

- Magic constant: `"APK Sig Block 42"` — 16 bytes, hex `41504b2053696720426c6f636b203432` (doc: 'magic "APK Sig Block 42" (16 bytes)').
- Block layout (all little-endian, per doc): `size of block (uint64)` → uint64-length-prefixed ID-value pairs (`ID uint32`, `value`) → `size of block again (uint64)` → `magic (16 bytes)`.
- v2 signature pair ID: `0x7109871a` (doc: "stored as an ID-value pair with ID 0x7109871a").
- Parse rule (doc): find ZIP End of Central Directory at file end → read Central Directory start offset → "The magic value provides a quick way to establish that what precedes Central Directory is likely the APK signing block".

## Placement quote (22 words, verbatim from doc)

> "Signing using APK signature scheme v2 inserts an APK signing block into the APK file immediately before the ZIP Central Directory section."

## What a minimal byte-level fixture check requires

Two honest directions, both grounded in the r65 fixture (sha256 `05d2280f…d03e`, 947 bytes, EOCD at 925, CD offset 737):

1. **Absence check (current fixture).** The fixture is unsigned: bytes at `cd_offset−16..cd_offset` are `b're generator\r\n\r\n'` (tail of the last local entry's content), not the magic; a byte scan finds zero occurrences of `APK Sig Block`. A future claim could assert "the last local entry ends exactly at the CD start (no signing block gap)" — a pure inert-byte fact, matching the r65/r67 house style.
2. **Presence check (future authored signed fixture).** Generator must emit a synthetic block between the last local entry and the CD: magic at `cd_offset−16`; `uint64` size at `cd_offset−24` equal to the head size; block start `cd_offset − 8 − size`; length-prefixed ID-value pairs terminating exactly at `cd_offset−24`; EOCD `cd_offset` field updated to point after the inserted block. Oracle/truth.json extends with `signing_block_size`, `magic_hex`, `id_list` (e.g. `0x7109871a`); readout recomputes each from raw bytes, same pattern as the dex-header check.

## Adjacency to current claims (observed)

- `corpus/knowledge/round-65-apk-axml-byte-evidence.md:127` and `round-67-apk-axml-byte-evidence.md:130`: "Unknown — nothing about install validity, signature blocks, dex program validity … is claimed" — so this ground is explicitly named uncovered in both candidates; the found spec directly addresses that named gap.
- `round-67-apk-axml-byte-evidence.md:7` coverage-map repeats "Not covered: install/signature verification".
- Kill-scope caution: a byte-level block-location check is still NOT signature *verification*; a future claim must keep the inert-byte framing or it collides with the same named-not-covered wall.

## Confidence and gaps

- Confidence: high — primary AOSP doc fetched and quoted verbatim; fixture gap bytes verified directly.
- Gap: doc describes v2 scheme page; a v3/v3.1/v4 pages exist as siblings (`/v3`, `/v4`) if a future round wants broader coverage (not fetched — out of this seat's scope).
- Gap: whether generator.py can be extended to emit a signed block without breaking the retained r65 fixture hash — future round's call; r65 fixture bytes are frozen.

No installs performed; no tool updates needed.
