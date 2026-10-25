NO-SILENT-DEPS — every constant the v2 entry uses is derived in its own text, stated by a cited source's anchored scope, or observed output of the cited own-work readout (S041); three honest attribution gaps found (fixable hardening, none fatal under the assigned test).

# Silent-dependency attack — round-67 C05 candidate

Target: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md` (v2, `admission-status: candidate`).
Test applied (per brief): a value is SILENT iff the entry's own text does not derive it AND no cited source states it. Cited sources tested: S038 (snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`, sha256 `56b88bc4…`), S032/S034 (APPNOTE snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt`, sha256 `0b993022…`), S045 (snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html`), S041 (`corpus/fixtures/apk-r65/` bundle), S043.

Readout re-run (read-only verification, lane root): `python3 -B corpus/fixtures/apk-r65/readout.py` → 15 stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — byte-matches the entry's pinned recheck digest (entry:6). Pinned file digests confirmed: fixture `05d2280f…03e`, readout.py `92e347c3…976`, truth.json `27303bae…173`.

## Assigned candidates

**1. EOCD signature `504b0506` — DERIVED (cited source states it), with attribution gap N1.**
`readout.py:76-77` locates it via `apk.rfind(b"PK\x05\x06")`. APPNOTE snapshot :634 (S032's anchored §4.3.16): "end of central dir signature 4 bytes (0x06054b50)"; registry `SOURCES.md:46` scopes S032 to "central directory file header **and end-of-central-directory record** field layout… signature values". The same row covers the EOCD field offsets the readout uses (+10 total-entries, +12 cd-size, +16 cd-offset — `readout.py:78-80`, matching appnote.txt:634-642). **Gap N1:** entry:2 never cites S032, and entry:12's scope sentence credits S032 for "(central directory header)" only — the EOCD coverage is implicit in the registry row, not stated in the entry. Stated by the cited source → not silent. Smallest fix: extend entry:12's parenthetical to "central directory and end-of-central-directory records".

**2. 46/30-byte fixed parts — DERIVED.**
Entry:34 explicitly attributes "(46-byte fixed part per S032 §4.3.12)" and "(30-byte fixed part per S034 §4.3.7)"; `readout.py:71-75` carries the same comment plus the per-field offsets (crc +14, sizes +18/+22, name/extra len +26/+28, cd local-header offset +42), all inside the cited APPNOTE field tables (appnote.txt:522-534, :389-400). The `PK\x01\x02`/`PK\x03\x04` signature asserts (`readout.py:90,98`) are S032's `0x02014b50` (:522) and S034's `0x04034b50` (:389) little-endian per §4.3.3.

**3. `0x100` UTF-8 flag bit — DERIVED (twice); the re-attribution is honest.**
Entry:67 now says "the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166)". Verified: `readout.py:166` emits `utf8=bool(flags & 0x100)` — the sentence is literally true and grounded in cited own-work S041. It does not deny S038: S038's anchored `struct ResStringPool_header` (:461, in the header's anchor list) contains `UTF8_FLAG = 1<<8` at snapshot :479-480, and the r65 draft's stronger phrasing ("the `UTF8_FLAG` of S038's flags enum") was equally valid — the enum is inside the anchored struct, so both citations resolve. Honest, slightly weaker; optional hardening: name S038:480 alongside the readout line. `SORTED_FLAG = 1<<0` (:477) likewise grounds the readout's `sorted_flag` bit (0x1).

**4. Resource-map entry width "one `uint32` per string" — DERIVED, with observation note N3.**
S038's anchored enum block contains the comment at snapshot :251-252: "This contains a uint32_t array mapping strings in the string pool back to resource identifiers." — width and per-string indexing are stated by the cited source; observed chunk size 44 = 8-byte header + 9×4 confirms (entry:74, `readout.py:171-175`). Note: `readout.py:172` bounds the entry loop by `string_count`, not by `(size-8)/4` — consistent only because observed entry_count == stringCount == 9; a chunk whose count differed would silently under-read. Non-fatal for this fixture (oracle `truth.json` `resource_ids` cross-verifies all 9). Item 7 does not quote :251-252 in text — suggest quoting it inline.

**5. `737 + 188 == 925` — DERIVED.**
Arithmetic over three observed fields of the `eocd` fact JSON (entry:31: `eocd_offset` 925, `offset_of_start_of_cd` 737, `size_of_central_directory` 188, `cd_end_equals_eocd_offset` true — `readout.py:85`); the entry states the equality and the observed terms.

## Beyond the assigned list (swept all readout constants)

- `payload_offset` formula (`lh_off + 30 + name_len + extra_len`, `readout.py:105`): entry:34 now derives it explicitly with the S034 field-list citation — the routed repair holds. Observed 49/506/668 consistent.
- attrExt-relative `attributeStart` provenance: entry:81 quotes snapshot :675 ("Appears header.headerSize bytes after a `ResXMLTree_node`") and :686 ("Byte offset from the start of this structure where the attributes start") with derived sizes (item 5) — repaired and DERIVED.
- `0xffffffff` null index: v2 attributes it to `readout.py:22` (`NO_INDEX = 0xFFFFFFFF`, S041) as observed treatment, no longer inferred from S038 — improved.
- Struct field offsets used but not in entry text (idIndex/classIndex/styleIndex at +30/+32/+34, `Res_value` dataType at +15/data at +16, lineNumber at +8): all fall out of item 5's derived field-width lists (`readout.py:52-58` vs. `readout.py:192-209`). DERIVED by the same item-5 derivation.
- dex offsets +8/+12/+32/+36/+40 (`readout.py:234-247`): S045's `header_item` table (snapshot :5940-5994) states field order and widths (magic `ubyte[8]`, checksum `uint`, signature `ubyte[20]`, file_size `uint`, header_size `uint`, endian_tag `uint = ENDIAN_CONSTANT`); the entry quotes those semantics (entry:106). DERIVED — implicitly (entry never spells out the offset arithmetic, same pattern as the ZIP offsets it does spell out; minor asymmetry only).
- Typed values `0x03`/`0x10` (entry:81 "typed `0x03` string"/"typed `0x10` int"): S038 `Res_value` (anchored :287) type semantics + oracle-declared `data_type` 3/16 (`truth.json:6,13,20`) + readout key names (`readout.py:215`). DERIVED.
- Namespace/end-element ext offsets (+16/+20 for prefix/uri and ns/name): `ResXMLTree_namespaceExt`/`endElementExt` are **not** in item 5's derived-width list; the entry treats the emitted indices as observed values resolving through the string pool (entry:88-95), corroborated by truth.json's declared strings. DERIVED-by-observation; optional hardening to add the ext structs to item 5's list.
- JAR-manifest split constants `\r\n`/`\r\n\r\n` (`readout.py:251-252`): own-work observation only; item 10 claims observed values ("first line … one blank-line-separated section"), no spec claim. DERIVED via S041.
- **ZIP_STORED / "no data descriptors" (entry:134) — note N4:** the readout never parses `compression method` or general-purpose-bit fields; the claim rests on oracle-declared `method: 0` for all three members (`truth.json:79,88,97`, S041) plus the contiguous walk (each payload ends exactly at the next stated `local_header_offset`, readout-observed). Grounded in a cited source, stated provenance adequate; flag for Q-review awareness that the method byte is oracle-declared, not field-parsed.
- Entry:45's "16-byte prefix of `Manifest-Version: 1.0`": `4d616e69666573742d56657273696f6e` decodes to `Manifest-Version` (16 chars), matching item 10's observed `first_line`. DERIVED.

## Impacted axes

None falsified. Q01 (source support): every load-bearing constant resolves to a cited anchored source or observed output. Q11 (derivation): the routed repairs (payload_offset, attrExt provenance, 0x100, NO_INDEX) all carry entry-level derivations now. No kill-rule trigger; C1's pass branch is not threatened by this attack surface.

## Smallest safe corrections (optional hardening, not admission blockers)

1. Entry:12 — widen the S032 parenthetical to name the EOCD record (its signature and field offsets are used at `readout.py:76-80`; S032's mined scope already covers them).
2. Entry:67 — cite S038:480 (`UTF8_FLAG = 1<<8`, inside anchored struct :461) next to the readout-test pointer.
3. Entry:74 — quote S038 :251-252 ("uint32_t array mapping strings in the string pool back to resource identifiers") as the stated basis for one-uint32-per-string.

No tooling installs performed; no files outside this report written; no git/jj mutations.
Report: .ufo/waves/round-67/R67CriticEntryDeps.md
