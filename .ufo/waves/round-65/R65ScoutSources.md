PASS — every data-type and chunk-type name the entry uses matches S038's enum members verbatim at the cited snapshot; no typo found (one line-range drift noted: `RES_XML_RESOURCE_MAP_TYPE` sits at :253, outside the cited "lines 239-250").

# Scope

Seat brief: re-open S038's chunk-type enum and `Res_value` Type enum in the snapshot `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/ResourceTypes.h`; confirm the entry `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md`'s 0x03/0x10 data-type names and chunk-type names match the enum member names at the cited lines (typo-level check, cf. S038's own 'occurrance' spelling preserved verbatim).

# Snapshot integrity

- `sha256sum` → `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, `wc -c` → 86255 bytes. Matches the digest/length cited at entry line 1 and `corpus/SOURCES.md:52` (S038 row).

# Chunk-type enum (snapshot :237-263)

Observed members (snapshot `ResourceTypes.h`):

| line | member | value |
|---|---|---|
| 239 | `RES_STRING_POOL_TYPE` | 0x0001 |
| 241 | `RES_XML_TYPE` | 0x0003 |
| 244 | `RES_XML_FIRST_CHUNK_TYPE` | 0x0100 |
| 245 | `RES_XML_START_NAMESPACE_TYPE` | 0x0100 |
| 246 | `RES_XML_END_NAMESPACE_TYPE` | 0x0101 |
| 247 | `RES_XML_START_ELEMENT_TYPE` | 0x0102 |
| 248 | `RES_XML_END_ELEMENT_TYPE` | 0x0103 |
| 249 | `RES_XML_CDATA_TYPE` | 0x0104 |
| 253 | `RES_XML_RESOURCE_MAP_TYPE` | 0x0180 |

Entry usage checked verbatim:

- Entry :46 — `0x0003` named `RES_XML_TYPE` → exact member name at :241. ✓
- Entry :1 (`source:` line) — names `RES_XML_TYPE`/`RES_XML_START_NAMESPACE_TYPE`/`RES_XML_START_ELEMENT_TYPE`/`RES_XML_END_ELEMENT_TYPE`/`RES_XML_END_NAMESPACE_TYPE`/`RES_XML_RESOURCE_MAP_TYPE` — all six spelled exactly as :241/:245/:247/:248/:246/:253. ✓
- Entry :53 — "six chunk types — `0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace" — value↔member mapping all correct (RES_STRING_POOL_TYPE, RES_XML_RESOURCE_MAP_TYPE, RES_XML_START_NAMESPACE_TYPE, RES_XML_START_ELEMENT_TYPE, RES_XML_END_ELEMENT_TYPE, RES_XML_END_NAMESPACE_TYPE). ✓
- `readout.py:127` comment and :129 assert name `RES_XML_TYPE`; :146 comment names `RES_STRING_POOL_TYPE`; :170 comment names `RES_XML_RESOURCE_MAP_TYPE` — all verbatim. ✓

# `Res_value` Type enum (snapshot :287-351)

`struct Res_value` opens at :287 (entry-cited anchor exact). Nested `enum : uint8_t` at :296; members include `TYPE_STRING = 0x03` (:307) and `TYPE_INT_DEC = 0x10` (:327). Note :324 `TYPE_FIRST_INT = 0x10` shares the value — 0x10 has two member names; the entry picks the semantically correct `TYPE_INT_DEC` (a raw decimal integer), not the sentinel.

Entry usage:

- Entry :78 — attributes "typed `0x03` string" (×2, package + versionName) and "typed `0x10` int" (versionCode) — value↔member mapping correct for `TYPE_STRING`/`TYPE_INT_DEC`. ✓
- `readout.py:215` — emits JSON key `data_type_string` when `vtype == 0x03`, else `data_type_int_dec` — verbatim lowercase echoes of `TYPE_STRING`/`TYPE_INT_DEC`; in this fixture only 0x03 and 0x10 occur (`truth.json:6,13,20` data_type 3/16/3), so no key is misapplied in emitted output. ✓

# 'occurrance' (brief's verbatim-typo flag)

- Snapshot :609 (doc comment on `ResXMLTree_header`, :612): "is described by the **occurrance** of RES_XML_START_ELEMENT_TYPE" — upstream misspelling confirmed present.
- `grep occurr?a?nce` over the entry file: zero hits — the entry does not quote or paraphrase that comment, so nothing propagates the typo and nothing "corrects" it inside a quote. No action needed.

# Other cited names spot-checked

- `UTF8_FLAG = 1<<8` (:480) inside `ResStringPool_header` flags enum — entry :64's `0x00000100` = `UTF8_FLAG` claim matches; `SORTED_FLAG = 1<<0` (:477) consistent with `sorted_flag: false`.
- `ResXMLTree::getAttributeNameResID` — method declared at :792; entry :71's semantic citation ("0 = no resource id") is a behavior claim, not a name typo.
- Struct anchors all exact: `ResChunk_header` :218, `ResStringPool_header` :461, `ResXMLTree_header` :612, `ResXMLTree_node` :621, `ResXMLTree_attrExt` :677, `ResXMLTree_attribute` :707, `Res_value` :287.
- `RES_XML_CDATA_TYPE` (0x0104, :249) correctly absent — no CDATA chunk in the fixture.

# Drift found (not a name typo — flagged for Q02/Q11 reviewers)

Entry :1 and :53 cite the chunk-type enum as "lines 239-250", but `RES_XML_RESOURCE_MAP_TYPE` — one of the six members the entry names and one of the six observed chunks — is defined at snapshot :253 (after the :250 `RES_XML_LAST_CHUNK_TYPE` member and a two-line comment). The named members are all correct; only the inclusive line range under-covers the enum by 3 lines.

# Confidence / remaining unknowns

Confidence: high — all checks performed directly on the pinned snapshot bytes whose digest matches the citation. Remaining unknowns: none within seat scope; the line-range drift is left for the fresh-seat Q reviewers to weigh.
