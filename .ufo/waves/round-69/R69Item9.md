MATCH — the `dex_declared_header` fact re-derives byte-identically to the entry's embedded line (14/14 fields, 0 differing), the prose sentence claims nothing the output does not support, and every S045 quote it cites is present in the committed snapshot.

# R69Item9 — per-item re-derivation: dex_declared_header

Seat: leaf executor, C05 v4 candidate (C1 coverage claim). Scope of this item: one fact, its
entry block, and the prose sentence about it. No files were edited; no packages installed.

## 1. Command and actual output

From `/home/vgpnk/Projects/shokunin/revenger-shokunin`:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact dex_declared_header
{"checksum_matches": true, "checksum_recomputed": "0x3d120c30", "declared_checksum": "0x3d120c30", "endian_tag": "0x12345678", "fact": "dex_declared_header", "file_size": 112, "format_version": "035", "header_bytes": 112, "header_size": 112, "magic_ascii": "dex\n", "magic_hex": "6465780a30333500", "signature_matches": true, "signature_recomputed": "a5fc7bea8fa9ffaa52243540c8026066511b9fce", "signature_sha1": "a5fc7bea8fa9ffaa52243540c8026066511b9fce"}
```

Exit code **0**, 456 bytes stdout (single JSON line + `\n`).

## 2. Entry's embedded line

`corpus/knowledge/round-69-apk-axml-byte-evidence.md:113` — same 456-byte line, inside the fenced
block opened at entry:112 (`$ python3 -B corpus/fixtures/apk-r65/readout.py --fact dex_declared_header`).

Byte comparison (captured stdout vs `sed -n '113p'` of the entry):

```
diff -> no output (BYTE_IDENTICAL)
d93bfafb434757e991319ed15795527a9e0a14c007a24e5442c7a892025b4d81  /tmp/revenger-r69-item9-actual.json
d93bfafb434757e991319ed15795527a9e0a14c007a24e5442c7a892025b4d81  /tmp/revenger-r69-item9-embedded.json
```

JSON-level: `actual_keys 14`, `embedded_keys 14`, `same_keys_same_order True`, `same_values True`,
`differing_fields []`.

## 3. Field-by-field verdict (14 fields, all present in both)

| # | field | actual | embedded | verdict |
|---|---|---|---|---|
| 1 | `checksum_matches` | `true` | `true` | MATCH |
| 2 | `checksum_recomputed` | `0x3d120c30` | `0x3d120c30` | MATCH |
| 3 | `declared_checksum` | `0x3d120c30` | `0x3d120c30` | MATCH |
| 4 | `endian_tag` | `0x12345678` | `0x12345678` | MATCH |
| 5 | `fact` | `dex_declared_header` | `dex_declared_header` | MATCH |
| 6 | `file_size` | `112` | `112` | MATCH |
| 7 | `format_version` | `"035"` | `"035"` | MATCH |
| 8 | `header_bytes` | `112` | `112` | MATCH |
| 9 | `header_size` | `112` | `112` | MATCH |
| 10 | `magic_ascii` | `"dex\n"` | `"dex\n"` | MATCH |
| 11 | `magic_hex` | `6465780a30333500` | `6465780a30333500` | MATCH |
| 12 | `signature_matches` | `true` | `true` | MATCH |
| 13 | `signature_recomputed` | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | same | MATCH |
| 14 | `signature_sha1` | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | same | MATCH |

**Fields that differ: none.** No field is present in one side only.

## 4. Independent recomputation from the fixture bytes (not the readout)

Read `corpus/fixtures/apk-r65/fixture.apk` at the member payload (offset 506, length 112 — the
offset/width pair that entry:43's `member[classes.dex]` line declares) and recomputed in-process:

```
payload_len 112
magic 6465780a30333500 b'035'
decl_checksum 0x3d120c30
decl_signature a5fc7bea8fa9ffaa52243540c8026066511b9fce
adler_over_12on 0x3d120c30      adler_over_8on 0x74a70cbb      <- offset 12 uniquely determined
sha1_over_32on  a5fc7bea...      sha1_over_12on 92fbf950...     <- offset 32 uniquely determined
file_size 112 header_size 112   endian_tag 0x12345678
```

So `checksum_matches: true` and `signature_matches: true` are true of the committed bytes, and the
two offsets the prose names (12 and 32) are the ones that actually reproduce the declared values —
the neighbouring candidate offsets (8, 12 for SHA-1) do not. `header_bytes 112` equals the member
length, so the declared `file_size` equals the real payload length for this member.

Provenance of the bytes read: `fixture.apk` sha256
`05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` — identical to the S041 anchor
(entry:4); `readout.py` sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`.

## 5. Does the prose sentence (entry:109) state anything the output does not support?

Entry:109, clause by clause, against the 14 fields:

1. "The `classes.dex` payload's first eight bytes are `6465780a30333500`" → supported by
   `magic_hex` (8 bytes) and cross-supported by entry:43 `payload_first16_hex`
   `6465780a30333500300c123da5fc7bea` at `payload_offset` 506. SUPPORTED.
2. "the magic `dex\n035\0`" → supported jointly by `magic_hex` + `format_version: "035"`. NIT (not
   an overclaim): the field named `magic_ascii` carries only 4 chars — `readout.py:238` is
   `magic[:4].decode("ascii")` — so `magic_ascii` alone does not show `035\0`. The prose cites the
   hex, not the ascii field, so nothing is asserted beyond the output.
3. "declared checksum **`0x3d120c30`**" → `declared_checksum`. SUPPORTED.
4. "equals the Adler-32 recomputed over the bytes from offset 12 on" → `checksum_recomputed`
   `0x3d120c30` + `checksum_matches: true`; offset 12 confirmed independently in §4 and
   disambiguated from offset 8. SUPPORTED.
5. "declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on" →
   `signature_sha1` == `signature_recomputed` == `signature_matches: true`; "20-byte" is entailed by
   the 40-hex-char value (`sig_hex_len 40`, `sha1_bytes 20`); offset 32 confirmed. SUPPORTED.
6. "declared `file_size` and `header_size` are both 112" → `file_size: 112`, `header_size: 112`.
   SUPPORTED. (Under-claim, not over-claim: `header_bytes: 112` — the real member length — is not
   mentioned.)
7. "S045: `header_size` 'must be 0x70 (112) bytes (v40 or earlier)' for this `035` magic" → correct
   branch application: the snapshot's same sentence continues "must be 0x78 (120) bytes (v41 or
   later)", and `format_version: "035"` selects the v40-or-earlier branch. SUPPORTED.
8. "the endian tag is `0x12345678`, S045's `ENDIAN_CONSTANT`" → `endian_tag: "0x12345678"`; snapshot
   literal `uint ENDIAN_CONSTANT = 0x12345678;`. SUPPORTED.
9. "These are declared-header self-consistency facts about one inert member; dex validity is not
   claimed" → the output is exactly declared-vs-recomputed self-consistency on one 112-byte member
   and asserts nothing about program validity; consistent with entry:167 ("The dex member is a header
   only and is intentionally not a valid dex program"). SUPPORTED.

**Verdict on the prose: no unsupported statement.** The only mismatch-shaped thing in the sentence is
the 8-byte ascii rendering vs the 4-char `magic_ascii` field (item 2) — a field-scope nit, since the
prose quotes `magic_hex`.

## 6. Quote accuracy against the S045 snapshot (secondary, supports the prose's attributions)

`.ufo/waves/round-67/source-snapshots/dex-format.html`, sha256
`c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (matches the round-67 fetch
record). All four attributed strings are present in the flattened text:

```
FOUND   'adler32 checksum of the rest of the file (everything but magic and this field)'
FOUND   'SHA-1 signature (hash) of the rest of the file (everything but magic , checksum , and this field)'
FOUND   'must be 0x70 (112) bytes (v40 or earlier)'   (next: 'must be 0x78 (120) bytes (v41 or later)')
FOUND   'uint ENDIAN_CONSTANT = 0x12345678;'
```

The signature clause renders with spaces before the commas because each comma is a separate `<code>`
element in the HTML; the entry's "everything but magic, checksum, and this field" is a markup-space
normalization, not a misquote.

## 7. Corroboration of the entry's own recheck predicate (entry:9)

```
$ python3 -B corpus/fixtures/apk-r65/readout.py      -> exit 0, 15 lines
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

Identical to the SHA-256 the entry's `recheck:` line declares. The per-value form this item uses
also holds: exactly one JSON line, exit 0.

## 8. Retained evidence

- Captured stdout: byte-identical to entry:113; sha256 `d93bfafb434757e991319ed15795527a9e0a14c007a24e5442c7a892025b4d81` (456 B).
- Entry:113 embedded line: same sha256 `d93bfafb…b4d81` (456 B).
- Full-readout stdout sha256 `507d79f8…dad247`, 15 lines (entry:9 predicate).
- fixture.apk sha256 `05d2280f…afe7d03e` = S041 anchor (entry:4).
- Snapshot sha256 `c0428612…91d9f4` with all four S045 quote strings found.
- Independent adler32/SHA-1 recomputation showing offsets 12 and 32 are the reproducing ones.

## 9. Risks / findings for the wave

- N1 (cosmetic, no gate impact): `magic_ascii` is a 4-byte prefix by construction
  (`readout.py:238`). A future critic diffing the prose's `dex\n035\0` against that field name alone
  will see a truncation; the prose is nonetheless grounded in `magic_hex` + `format_version`.
- N2 (omission, no gate impact): the prose does not state that `header_bytes` (actual member length)
  equals the declared `file_size` — the output does show it, so this is a missed strengthening rather
  than a defect.
- No edit was made to the entry, the readout, the registry or any fixture; the entry stays a
  candidate and `corpus/README.md`'s C05 row is untouched by this seat.
