FAIL — entry contains one false-provenance cross-reference (item 8: `attributeCount=3` "all equal to the derived sizes of item 5"; item 5 derives {8,16,20,28}, no 3) and two undisclosed inter-item value dependencies (item 8 silently consumes item 6's string table and item 7's resource map; item 7 silently consumes item 6's strings). §Comparison-with-oracle survives falsification: every claimed shared field exists in truth.json.

# Scope
Attack `corpus/knowledge/round-65-apk-axml-byte-evidence.md` for dependency errors only (undeclared item→item value reliance; oracle-agreement claims on absent truth.json fields; item 5↔8 size cross-references). All paths under `/home/vgpnk/Projects/shokunin/revenger-shokunin/`.

# Ground truth established
- `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — matches entry `recheck:` (line 5) and §Reproduce (line 162). All 10 quoted `--fact` blocks match live output verbatim.
- `sha256sum`: fixture.apk `05d2280f…d03e` (947 B), truth.json `27303bae…8173`, generator.py `eaa9444c…7c1a`, readout.py `92e347c3…f76` — all match header S041 anchors (line 3).
- Item 5 emitted derived-size set: `{8, 16, 20, 28}` (`total_bytes` {ResChunk_header:8, ResStringPool_header:28, ResXMLTree_attrExt:20, ResXMLTree_attribute:20, ResXMLTree_node:16, Res_value:8}).

# Findings

## F1 — Broken link: item 8 claims `attributeCount` equals an item-5 derived size [defect]
`corpus/knowledge/round-65-apk-axml-byte-evidence.md:78`: "`attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3** — all equal to the derived sizes of item 5."
Item 5's emitted fact `spec_derived_struct_widths` (readout.py:61-68) contains exactly the values {8,16,20,28}. `attributeCount=3` is not among them and is a *count*, not a struct size — nothing in item 5 derives 3. The same-sentence "all equal" extends item-5 provenance to a value item 5 never produced: false provenance by over-grouping. The paired reverse link (line 62, item 5's prose → item 8's `attributeStart`/`attributeSize`) is sound; only the item-8 direction over-claims.
Smallest safe correction: "`attributeStart` **20** and `attributeSize` **20** — equal to the derived `ResXMLTree_attrExt`/`ResXMLTree_attribute` sizes of item 5 — with `attributeCount` **3** as stated by the chunk."

## F2 — Undisclosed dependency: item 8 values are computed from item 6's string table and item 7's resource map [defect]
In readout.py, `axml_start_element` resolves `name`/`ns`/`raw_value` via `strings[…]` (lines 211-213) — the item-6 string list — and `res_id` via `ids[aname]` (line 216) — the item-7 resource-map list. The entry's item-8 prose (line 78) names only item 5 as a dependency; it never says the resolved strings (`package`, `versionCode`, `versionName`, `android` ns) come from item 6's pool, nor that `res_id` 0x0101021b/0x0101021c comes from item 7's map. Item 8 therefore relies on two other items' values without saying so — exactly the failure mode this seat was asked to name. (Mitigation, not cure: the namespace prose at line 85 does cite the start-namespace chunk for `android` prefix resolution.)
Smallest safe correction: one clause in item 8 — "attribute names, namespaces and raw values resolve through item 6's string table; `res_id` values are item 7's resource-map entries at the same name index."

## F3 — Undisclosed dependency: item 7's `nonzero` keys are item 6's strings [minor defect]
readout.py:175 emits `"nonzero": {strings[i]: …}` — the keys `versionCode`/`versionName` are item-6 pool strings, but item 7's prose (lines 71-76) never cites item 6; a reader cannot tell whether `versionCode`/`versionName` are read from the pool or assumed. Same smallest-safe-correction pattern as F2.

## F4 — Item 4's headerSize attribution omits the resource map's 8 [minor]
Line 53: "The `headerSize` column — 28, 8, 16, 16, 16, 16 — equals the fixed struct sizes derived in item 5 **for the string pool and the XML node chunks**." The `8` belongs to the resource-map chunk (offset 204) and equals derived `ResChunk_header`=8 — an item-5 struct, but not "for the string pool or XML node chunks" as phrased. The value is in item 5's table, so the link resolves but under a mislabeled bucket. One-word-class fix.

## F5 — Item 3's cursor-equality claim depends on item 2's `eocd_offset` without naming it [minor]
Line 33: "the walk's end cursor equals the end-of-central-directory offset." `eocd_offset` is emitted only by item 2; item 3's member JSONs carry no field proving the equality (it holds via `assert cursor == eocd`, readout.py:119, i.e. exit-0 evidence only). Value-wise correct; pointer-wise the claim leans on item 2 silently and on an assertion no printed field shows.

## §Comparison-with-oracle — NOT falsified
Line 121 claims agreement on: image sha256+size (truth.json `image.sha256`/`image.size` — present, lines 69-73); members' local-header offsets, payload sizes, CRC-32 (`members[].local_header_offset`/`compressed_size`/`uncompressed_size`/`crc32` — present, lines 74-102); nine strings (`axml_declared.strings` — present, lines 37-47); three attribute rows (`axml_declared.attributes` — present, lines 3-25); two non-zero resource ids (`axml_declared.resource_ids` — present, lines 26-36). Every named shared field exists; no absent field is claimed. Spot-check: readout `member[AndroidManifest.xml]` crc32 `962d075f`, lh_off 0, sizes 416/416, sha256 `73d1e0f2…fae4` — all equal truth.json. Cosmetic: readout's `nonzero` formats ids as `0x101021b` (leading zero dropped by `f"0x{ids[i]: 08x}"`, readout.py:175) vs truth.json's `0x0101021b` — numerically equal, textually mismatched inside the emitted JSON.

## Independent items — clean
Items 1 (archive), 2 (EOCD), 5 (spec widths — S038 field lists, not item values), 9 (dex header), 10 (jar manifest) rely on no other item's output. Items 4 and 6 depend on item 3's member extraction, which both name in prose ("member's uncompressed size", "the string-pool chunk (offset 8, size 196)" restates item-4 table values in-line rather than silently).

# Impacted axes
- **Coverage (C1 admission surface):** F1 is a false-provenance link inside §Observation — the class of defect Q11's "carries its deriving command" basis (line 150) claims absent; F2/F3 leave item 8's provenance incomplete. Fixable defects, not value errors — every emitted number verified correct against live readout + truth.json.
- **Calibration:** not touched (entry-only findings).

# Verdict for adjudicator
Fail the entry's dependency hygiene as drafted: one over-claiming cross-reference (F1) and two silent value dependencies (F2, F3). All corrections are single-clause text edits; no readout, fixture, or truth.json byte needs to change. If the admission gate treats F1's provenance over-claim as blocking, the correction set above is the minimal repair; nothing here falsifies any emitted value.

Tooling: no installs needed (python3 3.14.8, coreutils sha256sum already present).
