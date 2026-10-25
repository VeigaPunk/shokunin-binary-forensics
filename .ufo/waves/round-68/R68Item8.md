MATCH — the entry's embedded `axml_start_element` line is byte-identical to the command's actual stdout on this tree (all 44 scalar positions agree; the two wording nits below are prose quantifier/citation imprecision, not differing fields).

Seat: L1Revenger68.R68Item8 (independent re-derivation, leaf; no edits performed).

# Command and actual output

Run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element
```

Exit code **0**, stderr empty, stdout is exactly one line of **890 characters + trailing newline (891 bytes)**, sha256 of the whole stdout (newline included) = `66cc5f92479d8ef18c7d80fc8fd5b346e228d688d8af7e6f69ba46d7c41b9c09`.

Actual output (single line, reproduced verbatim; sorted keys):

```json
{"attributeCount": 3, "attributeSize": 20, "attributeStart": 20, "attributes": [{"data_type": "0x03", "data_type_string": 4, "name": "package", "name_index": 3, "ns": null, "ns_index": 4294967295, "raw_value": "com.example.r65", "raw_value_index": 4, "res_id": 0, "value_size": 8}, {"data_type": "0x10", "data_type_int_dec": 1, "name": "versionCode", "name_index": 5, "ns": "android", "ns_index": 0, "raw_value": "1", "raw_value_index": 7, "res_id": 16843291, "value_size": 8}, {"data_type": "0x03", "data_type_string": 8, "name": "versionName", "name_index": 6, "ns": "android", "ns_index": 0, "raw_value": "1.0", "raw_value_index": 8, "res_id": 16843292, "value_size": 8}], "classIndex": 0, "element_name": "manifest", "element_name_index": 2, "element_ns": null, "element_ns_index": 4294967295, "fact": "axml_start_element", "idIndex": 0, "lineNumber": 1, "offset": 272, "styleIndex": 0}
```

Member invocations as briefed (three runs, one per member, `--fact 'member[...]'`): each exit **0**, one stdout line, and each line is byte-identical to the entry's item-3 block and to the corresponding line of the full-stdout block:

| member fact | stdout len | sha256 (first 16) | entry lines with byte-identical copy |
|---|---|---|---|
| `member[AndroidManifest.xml]` | 365 | `d475f62a5988bc19` | entry:39, entry:203 |
| `member[classes.dex]` | 360 | `76aa7a9d5bd1b967` | entry:41, entry:204 |
| `member[META-INF/MANIFEST.MF]` | 367 | `598d9999a254a9dc` | entry:43, entry:205 |

Provenance note on my own first three calls: I invoked the bare arg `readout.py "member[...]"` without the `--fact` flag, which correctly prints all 15 lines (no filter); with `--fact` the filter works. The `--fact=<id>` equals-form is likewise unparsed and prints all 15 lines (main() only reads the space-separated form). Neither is an entry defect — the entry always uses the space form.

# Entry's embedded line and byte-equality proof

The block claiming this fact is **entry:82** (item 8, heading sentence) with the embedded output line at **entry:86**, and the same line duplicated inside the "Full stdout as printed at this entry's build" block at **entry:211**.

Programmatic comparison (`readout.py --fact axml_start_element` stdout, newline-stripped, vs. the raw markdown line at that line number):

```
--- md line 86:  len 890 sha 4ad2e59802cab7642af547c1cd53938e4340d2b8059f98a62f65fc3d572fc648 equals_actual=True
--- md line 211: len 890 sha 4ad2e59802cab7642af547c1cd53938e4340d2b8059f98a62f65fc3d572fc648 equals_actual=True
act: exit 0  len 890  sha 66cc5f92479d8ef18c7d80fc8fd5b346e228d688d8af7e6f69ba46d7c41b9c09 (890 chars, +"\n" = 891 bytes)
full[11] contains start_element: True  full[11] len 890  full[11]==act: True
```

(sha differs only because `act` above included the trailing newline; the character-for-character comparison `md_line == act_line` returned `True` for both 86 and 211, and line 12 of the 15-line full stdout is identical to the single-fact line.)

Also verified: the entry's `recheck:`/§Reproduce claim "exit 0 and prints 15 stdout lines whose SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`" — actual bare run: exit 0, 15 lines, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`. Pins re-hashed: readout.py `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`, fixture.apk `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, truth.json `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` — all equal the entry's stated digests.

# Field-by-field verdict

Top level (14 keys, alphabetical as emitted):

| field | actual | entry:86 | verdict |
|---|---|---|---|
| `attributeCount` | `3` | `3` | MATCH |
| `attributeSize` | `20` | `20` | MATCH |
| `attributeStart` | `20` | `20` | MATCH |
| `classIndex` | `0` | `0` | MATCH |
| `element_name` | `"manifest"` | `"manifest"` | MATCH |
| `element_name_index` | `2` | `2` | MATCH |
| `element_ns` | `null` | `null` | MATCH |
| `element_ns_index` | `4294967295` | `4294967295` | MATCH |
| `fact` | `"axml_start_element"` | same | MATCH |
| `idIndex` | `0` | `0` | MATCH |
| `lineNumber` | `1` | `1` | MATCH |
| `offset` | `272` | `272` | MATCH |
| `styleIndex` | `0` | `0` | MATCH |
| `attributes` | 3 objects | same 3 objects | MATCH |

`attributes[0]` (`package`): `data_type 0x03` / `data_type_string 4` / `name "package"` / `name_index 3` / `ns null` / `ns_index 4294967295` / `raw_value "com.example.r65"` / `raw_value_index 4` / `res_id 0` / `value_size 8` — all MATCH.
`attributes[1]` (`versionCode`): `data_type 0x10` / `data_type_int_dec 1` / `name "versionCode"` / `name_index 5` / `ns "android"` / `ns_index 0` / `raw_value "1"` / `raw_value_index 7` / `res_id 16843291` / `value_size 8` — all MATCH.
`attributes[2]` (`versionName`): `data_type 0x03` / `data_type_string 8` / `name "versionName"` / `name_index 6` / `ns "android"` / `ns_index 0` / `raw_value "1.0"` / `raw_value_index 8` / `res_id 16843292` / `value_size 8` — all MATCH.

44 scalar positions, 0 differing fields.

Independent arithmetic/oracle corroboration of values (not needed for the equality verdict, but it shows the numbers are real):
- `res_id 16843291 == 0x0101021b`, `16843292 == 0x0101021c` (matches the entry's item-7 resource-map ids and `truth.json` `axml_declared.resource_ids`).
- Chunk internal consistency: start-element chunk spans 272..368 (96 bytes, entry:206 chunk table); `node header 16 + attrExt 20 + 3 × attributeSize 20 = 96` — so `attributeStart 20`/`attributeSize 20`/`attributeCount 3` are mutually consistent with the declared chunk size.
- `truth.json` `axml_declared.attributes` agrees with all three rows on `name_idx` 3/5/6, `ns_idx` 4294967295/0/0, `data_type` 3/16/3, `raw_value_idx` 4/7/8; `data` 4/1/8 decode to `com.example.r65`/`1`/`1.0` through the pool.

# Prose judgement on item 8 (entry:82 and entry:89)

Supported by the actual output, with the cited provenance verified:

- "The start-element chunk at offset 272 names the element `manifest` with no namespace" — supported (`offset 272`, `element_name "manifest"`, `element_ns null`).
- "`attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3**" — supported exactly.
- "so attribute *i* is at `chunk_base + 16 + attributeStart + i * attributeSize` — the readout's own derivation (readout.py:200-203)" — the citation resolves: readout.py:200-203 is exactly the comment plus `aoff = base + 16 + attribute_start + i * attribute_size` (readout.py:203), and the 16-byte node header comes from `ResXMLTree_node` = `[2,2,4,4,4]` in item 5's output.
- "S038's `struct ResXMLTree_attrExt` (line 677) "Appears header.headerSize bytes after a `ResXMLTree_node`"" — snapshot lines 675 (`* Appears header.headerSize bytes after a ResXMLTree_node.`) and 677 (`struct ResXMLTree_attrExt`) verified, and both are printed by `python3 -B corpus/derive_axml_anchors.py` (exit 0).
- "`attributeStart` field is "Byte offset from the start of this structure where the attributes start" (snapshot line 686; the field declaration `uint16_t attributeStart;` at line 687)" — verified at `corpus/snapshots/ResourceTypes.h:686` (comment) and `:687` (declaration); both derived by the same script.
- "The three attributes read there are `package="com.example.r65"` (typed `0x03` string), `android:versionCode=1` (typed `0x10` int, resource id `0x0101021b`) and `android:versionName="1.0"` (typed `0x03` string, resource id `0x0101021c`)" — every clause supported (`ns "android"`, `data_type`, `data_type_int_dec 1`, `res_id` values as hex-checked above).
- entry:89 "The `0xffffffff` namespace index on `package` and the element itself is recorded as observed and treated as null by the readout (readout.py:22); the same constant on `android`-carrying attributes resolves instead through the start-namespace chunk at offset 248, which states prefix index 0 (`android`) and URI index 1 …" — supported: output keeps `4294967295` in `ns_index`/`element_ns_index` while `ns`/`element_ns` are `null`; readout.py:22 is `NO_INDEX = 0xFFFFFFFF`; the start-namespace chunk is at offset 248 with `prefix_index 0` (`android`) and `uri_index 1`; `ns_index 0` resolves to `strings[0] == "android"` in the same run's string pool (entry:207).

Two prose imprecisions (no field differs; recorded because this seat checks the prose, not just the numbers):

1. entry:82 "`attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3** — all equal to the derived sizes of item 5." Item 5's output derives `attr_ext_attribute_start 20` and `attribute_size 20` only; there is no derived value `3` in item 5, so the universal "all" quantifies over three values while only two have a counterpart. The intended reading (start/size equal the two derived widths; count is independent) is supported, but the sentence as written asserts an equality for `attributeCount` that item 5 does not supply. This is the only statement in the fact's prose that the outputs do not literally support.
2. entry:89 cites `readout.py:22` for the readout *treating* `0xffffffff` as null; line 22 is the constant definition, while the treatment itself is the conditional at `readout.py:211` (`"ns": None if ans == NO_INDEX else strings[ans]`, with the sibling `element_ns` mapping at readout.py:219). The citation is to the right mechanism but not the mapping statement.

Neither imprecision changes any value, field, offset, type, id or digest in the block, and neither is a minted fact: the entry's `## §Q-map` Q11 stance ("every count, offset, identifier and digest carries its deriving command and output") is satisfied for this fact by entry:86/211, which are byte-exact.

# Things checked and not found

- No field value differs; no field is present in one and absent in the other; key set and ordering match exactly (both `sort_keys=True` output of the same script, verified by `json.loads(...) == json.loads(...)` and by raw string equality).
- No hidden transformation: the embedded line is not reordered, re-quoted or re-spaced; raw equality on 890 characters passed.
- No stale-bytes suspicion: the entry's three hashes for readout.py / fixture.apk / truth.json and its 15-line stdout sha256 (`507d79f8…`) all re-computed equal on this tree.

# Files

None modified. Report written at `.ufo/waves/round-68/R68Item8.md` (this file). No tools installed or upgraded.
