MATCH — the `axml_start_element` fact re-derives byte-identically to the entry's embedded line (all 14 top-level fields and all 3 attributes, 0 differing fields); the entry's item-8 prose, however, contains two clauses the output does not support (P2, P2) and one imprecise code pointer (P3).

Seat: R69Item8 (reviewer, leaf). Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin.
Entry under test: `corpus/knowledge/round-69-apk-axml-byte-evidence.md`, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`.
Fixture: `corpus/fixtures/apk-r65/fixture.apk`, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (= `axml_start_element`'s own member digest, unchanged).
Readout: `corpus/fixtures/apk-r65/readout.py`, sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` (matches the entry's line 194 claim).

## 1. Command, exit status, actual output

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element
{"attributeCount": 3, "attributeSize": 20, "attributeStart": 20, "attributes": [{"data_type": "0x03", "data_type_string": 4, "name": "package", "name_index": 3, "ns": null, "ns_index": 4294967295, "raw_value": "com.example.r65", "raw_value_index": 4, "res_id": 0, "value_size": 8}, {"data_type": "0x10", "data_type_int_dec": 1, "name": "versionCode", "name_index": 5, "ns": "android", "ns_index": 0, "raw_value": "1", "raw_value_index": 7, "res_id": 16843291, "value_size": 8}, {"data_type": "0x03", "data_type_string": 8, "name": "versionName", "name_index": 6, "ns": "android", "ns_index": 0, "raw_value": "1.0", "raw_value_index": 8, "res_id": 16843292, "value_size": 8}], "classIndex": 0, "element_name": "manifest", "element_name_index": 2, "element_ns": null, "element_ns_index": 4294967295, "fact": "axml_start_element", "idIndex": 0, "lineNumber": 1, "offset": 272, "styleIndex": 0}
EXIT=0
```

- stdout is 891 bytes, one line, valid JSON (`json.loads` succeeds).
- sha256 of the single stdout line: `66cc5f92479d8ef18c7d80fc8fd5b346e228d688d8af7e6f69ba46d7c41b9c09`.
- Determinism: three consecutive runs gave the identical digest `66cc5f92…9c09` (same bytes, exit 0 each time).

## 2. Entry's embedded line(s)

- Narrative block: entry **line 88** (command at line 87, fence at 86/89), sha256 `66cc5f92479d8ef18c7d80fc8fd5b346e228d688d8af7e6f69ba46d7c41b9c09`, 891 bytes.
- Replay copy in §Observation: entry **line 211**, sha256 `66cc5f92…9c09`, 891 bytes (`cmp` reports identity with line 88 and with the actual output).
- Verbatim comparison: `cmp actual.json embedded.json` → identical; `a == b` on raw bytes → `True`; both parse as JSON with the same 14 keys.

## 3. Field-by-field verdict (every field, actual vs. embedded, plus independent byte derivation)

Independent derivation was not taken from the readout: a throwaway `struct` walk in `/tmp` parsed `AndroidManifest.xml` inside `fixture.apk` itself (chunk table → chunk at 272, node at base+8, attrExt at base+16, attribute *i* at `base+16+attributeStart+i*attributeSize`) and read the string pool (index → string) and resource map.

| # | field (path) | actual | embedded (line 88) | independent bytes | verdict |
|---|---|---|---|---|---|
|1|`attributeCount`|3|3|attrExt `uint16` @ base+24 = 3|same|
|2|`attributeSize`|20|20|attrExt `uint16` @ base+26 = 20|same|
|3|`attributeStart`|20|20|attrExt `uint16` @ base+28 = 20|same|
|4|`attributes[0].data_type`|`0x03`|`0x03`|value byte @ 308+15 = 0x03|same|
|5|`attributes[0].data_type_string`|4|4|value data u32 @ 308+16 = 4 → pool[4]=`com.example.r65`|same|
|6|`attributes[0].name`|`package`|`package`|name_index 3 → pool[3]=`package`|same|
|7|`attributes[0].name_index`|3|3|u32 @ 308+4 = 3|same|
|8|`attributes[0].ns`|null|null|ns u32 @ 308 = `0xffffffff`|same|
|9|`attributes[0].ns_index`|4294967295|4294967295|u32 @ 308 = 4294967295|same|
|10|`attributes[0].raw_value`|`com.example.r65`|`com.example.r65`|raw u32 @ 308+8 = 4 → pool[4]|same|
|11|`attributes[0].raw_value_index`|4|4|u32 @ 308+8 = 4|same|
|12|`attributes[0].res_id`|0|0|ids[3]=`0x00000000` (resource map @204)|same|
|13|`attributes[0].value_size`|8|8|u16 @ 308+12 = 8|same|
|14|`attributes[1].data_type`|`0x10`|`0x10`|value byte @ 328+15 = 0x10|same|
|15|`attributes[1].data_type_int_dec`|1|1|value data u32 @ 328+16 = 1|same|
|16|`attributes[1].name`|`versionCode`|`versionCode`|name_index 5 → pool[5]|same|
|17|`attributes[1].name_index`|5|5|u32 @ 328+4 = 5|same|
|18|`attributes[1].ns`|`android`|`android`|ns u32 @ 328 = 0 → pool[0]=`android`|same|
|19|`attributes[1].ns_index`|0|0|u32 @ 328 = 0|same|
|20|`attributes[1].raw_value`|`1`|`1`|raw u32 @ 328+8 = 7 → pool[7]=`1`|same|
|21|`attributes[1].raw_value_index`|7|7|u32 @ 328+8 = 7|same|
|22|`attributes[1].res_id`|16843291|16843291|ids[5]=`0x0101021b` → 16843291|same|
|23|`attributes[1].value_size`|8|8|u16 @ 328+12 = 8|same|
|24|`attributes[2].data_type`|`0x03`|`0x03`|value byte @ 348+15 = 0x03|same|
|25|`attributes[2].data_type_string`|8|8|value data u32 @ 348+16 = 8 → pool[8]=`1.0`|same|
|26|`attributes[2].name`|`versionName`|`versionName`|name_index 6 → pool[6]|same|
|27|`attributes[2].name_index`|6|6|u32 @ 348+4 = 6|same|
|28|`attributes[2].ns`|`android`|`android`|ns u32 @ 348 = 0 → pool[0]|same|
|29|`attributes[2].ns_index`|0|0|u32 @ 348 = 0|same|
|30|`attributes[2].raw_value`|`1.0`|`1.0`|raw u32 @ 348+8 = 8 → pool[8]|same|
|31|`attributes[2].raw_value_index`|8|8|u32 @ 348+8 = 8|same|
|32|`attributes[2].res_id`|16843292|16843292|ids[6]=`0x0101021c` → 16843292|same|
|33|`attributes[2].value_size`|8|8|u16 @ 348+12 = 8|same|
|34|`classIndex`|0|0|attrExt u16 @ base+30 = 0|same|
|35|`element_name`|`manifest`|`manifest`|name_index 2 → pool[2]=`manifest`|same|
|36|`element_name_index`|2|2|u32 @ base+20 = 2|same|
|37|`element_ns`|null|null|ns u32 @ base+16 = `0xffffffff`|same|
|38|`element_ns_index`|4294967295|4294967295|u32 @ base+16 = 4294967295|same|
|39|`fact`|`axml_start_element`|`axml_start_element`|emitter label (readout.py:218)|same|
|40|`idIndex`|0|0|attrExt u16 @ base+32 = 0|same|
|41|`lineNumber`|1|1|u32 @ base+8 = 1|same|
|42|`offset`|272|272|chunk table: type `0x0102` at 272|same|
|43|`styleIndex`|0|0|attrExt u16 @ base+34 = 0|same|

Differences: **none**. Zero fields differ.

Corroborating arithmetic and anchors:
- chunk table (`--fact axml_chunk_table`): `{"headerSize": 16, "offset": 272, "size": 96, "type": 258}` → 258 = 0x0102 = `RES_XML_START_ELEMENT_TYPE`; `headerSize 16` matches `node_header_size: 16` from `spec_derived_struct_widths`.
- chunk size closes exactly: `16 (node) + 20 (attrExt) + 3×20 (attributes) = 96` = declared size at 272.
- `attributeStart` is relative to the attrExt, i.e. attribute 0 at `272+16+20 = 308`, then 328 and 348 — exactly the offsets whose bytes produced the three rows above (readout.py:199-209 implements the same formula, with `aoff` at :203).
- string pool index 2/3/4/5/6/7/8 = `manifest`/`package`/`com.example.r65`/`versionCode`/`versionName`/`1`/`1.0` (`--fact axml_string_pool`), so every `name`/`raw_value`/`data_type_string` string is the declared index, not a guess.
- start-namespace chunk at 248 states prefix_index 0, uri_index 1 (`--fact axml_start_namespace`, byte-verified: `nsExt prefix_index 0 uri_index 1`), and pool[0]=`android`.
- snapshot anchors cited by the block are correct in `corpus/snapshots/ResourceTypes.h`: `struct ResXMLTree_attrExt` = line 677, "Byte offset from the start of this structure where the attributes start." = line 686, `uint16_t attributeStart;` = line 687.
- whole-run invariant: `python3 -B corpus/fixtures/apk-r65/readout.py` → 15 lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, matching entry line 194 (re-derived here).

## 4. Prose judgement — does item 8's sentence state anything the output does not support?

**Yes: two clauses.**

**P2-a — "all equal to the derived sizes of item 5" (entry line 84), applied to `attributeCount` 3.**

> "The start-element chunk at offset 272 names the element `manifest` with no namespace, `attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3** — all equal to the derived sizes of item 5."

The universal covers three values; item 5's own output (`spec_derived_struct_widths`, entry line 65) offers `total_bytes` = 8, 28, 20, 20, 16, 8 and `node_header_size` 16 — there is no derived width equal to 3. Only `attributeStart` (20 = `ResXMLTree_attrExt`) and `attributeSize` (20 = `ResXMLTree_attribute`) are equalities, and that is exactly how item 5's own line 68 words it. `attributeCount` 3 is an observed count, closed by the size identity `16+20+3×20 = 96` (chunk size), not by any derived struct width. The output does not support "all".
Correct phrasing: "…`attributeStart` **20** and `attributeSize` **20** — equal to the derived `ResXMLTree_attrExt` and `ResXMLTree_attribute` widths of item 5 — and `attributeCount` **3**, which closes the chunk size: `16 + 20 + 3×20 = 96`."

**P2-b — "the same constant on `android`-carrying attributes" and "resolved … through the start-namespace chunk at offset 248" (entry line 91).**

> "The `0xffffffff` namespace index on `package` and the element itself is recorded as observed and treated as null by the readout (readout.py:22); the same constant on `android`-carrying attributes is resolved by this readout through the start-namespace chunk at offset 248, which states prefix index 0 (`android`) and URI index 1…"

Two unsupported assertions:
1. "the same constant on `android`-carrying attributes" — the actual output says `"ns_index": 0` for both `versionCode` and `versionName`; `0xffffffff` occurs only on `package` (`attributes[0].ns_index`) and on the element (`element_ns_index`). Independently: bytes at 328 and 348 carry `ns = 0`. The "same constant" is not on the android attributes.
2. "resolved by this readout through the start-namespace chunk at offset 248" — the readout resolves the attribute namespace as `strings[ans]` directly off the **string pool** (`readout.py:211`, `"ns": None if ans == NO_INDEX else strings[ans]`); the start-namespace handler at `readout.py:178-183` only *emits* prefix/uri as its own fact and is never consulted by the start-element path. Pool[0] happens to be `android`, which is what the chunk at 248 also declares as prefix index 0 — agreement between two observations, not a resolution path through chunk 248.
Correct phrasing: "the android attributes carry `ns_index` **0**, which this readout resolves to pool string 0 = `android` (`readout.py:211`); the start-namespace chunk at offset 248 independently declares prefix index 0 = `android` with URI index 1, i.e. the same binding observed twice, not resolved once from the other."

**P3 — pointer imprecision, same sentence.** "treated as null by the readout (readout.py:22)" points at the constant definition `NO_INDEX = 0xFFFFFFFF`; the null mapping that the sentence describes is executed at `readout.py:211` (`"ns_index": ans, "ns": None if ans == NO_INDEX …`) and `readout.py:219` (`element_ns=None if ns_idx == NO_INDEX …`). Cite :211/:219 (the constant may be added as :22), otherwise a reader landing on :22 sees no null treatment.

Consequence for the entry's own quality table: row **Q07** (entry line 181) answers pass because "the namespace-resolution sentence is explicitly scoped to how this readout resolves this fixture (item 8)" — the scope caveat fences *prediction*, but P2-b is a statement about *this* readout's own mechanism and is wrong about that mechanism, so Q07's pass rests on a sentence whose two factual clauses do not hold. The fact itself (item 8's JSON) is unaffected.

## 5. Residual risk / verification gaps

- `null` for `0xffffffff` is an AOSP `ResStringPool_ref`-sentinel reading, not a byte-level fact; the entry scopes this to the readout's own convention (supported), and the readout does emit both the raw index and the null, so the interpretation is auditable.
- `data_type_string` / `data_type_int_dec` are alternate keys chosen by value type (`readout.py:215`); both branches appear in this fact and both agree with the value bytes.
- I did not re-run `corpus/derive_axml_anchors.py` (item 11's instrument) — out of this item's scope; snapshot lines 677/686/687 were checked directly instead.
- My judgement covers item 8 and its two prose sentences only; the other items' prose and the Q-table rows for Q03/Q06/Q08/Q09/Q10/Q12/Q15 belong to their own seats.

## 6. Scope, tooling, cleanup

- Files written: this report only. No edit to `corpus/`, no git/jj mutation, no other repo touched.
- Tooling: none installed or upgraded (no need; Python stdlib sufficed). All reads used `python3 -B` and read-only git-free commands.
- Scratch: `/tmp/revenger-r69-item8/` removed after this report was written.
