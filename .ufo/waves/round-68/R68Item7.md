MATCH — `axml_resource_map` reproduces field-for-field (embedded line byte-identical to stdout, sha256 `630855d74045e698548cdb52f315e6301edd5862ef2a3a6126562f4af9da8134`), the two non-zero ids equal `truth.json` `axml_declared.resource_ids` exactly, and every numeric assertion in item 7's prose is supported; one prose adjective ("framework") is unanchored and two low-severity evidence-hygiene defects are recorded below.

# R68Item7 — independent re-derivation, item 7 (`axml_resource_map`)

Seat: leaf reviewer, round 68 / lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Read-only: nothing edited; only this file written.
Entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md` (215 lines).

## 1. Commands and actual output

### 1.1 The claimed fact

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map
{"entry_count": 9, "fact": "axml_resource_map", "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
EXIT=0
```
stderr: 0 bytes (`wc -c` on the redirect).

### 1.2 The three members (as briefed)

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[AndroidManifest.xml]'
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
EXIT=0

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[classes.dex]'
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
EXIT=0

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
EXIT=0
```

The three member lines are also what the entry embeds at its item 3 (entry:66-68): each value there is identical to the stdout above, including the 16-byte `payload_first16_hex` `4d616e69666573742d56657273696f6e` (the round-65 15-byte drift the entry says it repaired, entry:70 — repaired in the bytes I see).

### 1.3 Whole-run hash and byte pins

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68i7_all.txt 2>&1 ; EXIT=0 ; LINES=15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r68i7_all.txt
# entry:8 (recheck) and entry:203 (Reproduce) claim exactly this sha256 and 15 lines — CONFIRMED

92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py   # = entry:3, entry:50
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk   # = entry:3, entry:52
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json    # = entry:3
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h       # = entry:1, entry:4, S046 stated sha256
```

## 2. The entry's embedded line, and byte-level identity

Entry:75 is item 7's prose; its embedded block is entry:78-79:

```
78: $ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map
79: {"entry_count": 9, "fact": "axml_resource_map", "ids": [...], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
```

Entry:208 carries the same fact line a second time inside the §Reproduce full-stdout dump.

```
$ sed -n '79p' entry > /tmp/r68i7_emb.txt
$ diff -u /tmp/r68i7_emb.txt /tmp/r68i7_rm.txt && echo BYTE_IDENTICAL
BYTE_IDENTICAL
630855d74045e698548cdb52f315e6301edd5862ef2a3a6126562f4af9da8134  /tmp/r68i7_rm.txt
630855d74045e698548cdb52f315e6301edd5862ef2a3a6126562f4af9da8134  /tmp/r68i7_emb.txt
$ sed -n '79p;208p' entry | sort -u | wc -l
1                      # both occurrences identical, and both identical to stdout
```

No transcription drift in this block: the embedded text is the command's stdout byte for byte, including the readout's own `nonzero` rendering quirk (finding F2).

## 3. Independent byte re-derivation of the chunk itself

I did not take `readout.py`'s word: I read the member bytes from the archive and parsed the resource-map chunk header directly (`zipfile` + `struct`, read-only, temp dir under `/tmp`):

```
member_bytes 416 sha256 73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4
member_sha_matches_entry True
chunk@204: type=0x0180 headerSize=8 size_field=44 first_payload_word=0
body_bytes 36  n_uint32 9  remainder 0
ids_hex ['0x00000000','0x00000000','0x00000000','0x00000000','0x00000000','0x0101021b','0x0101021c','0x00000000','0x00000000']
zeros 7   nonzero_count 2
next_chunk@248 type=0x0100 size=24
entry_xml_total 416
```

So the chunk at offset 204 is `RES_XML_RESOURCE_MAP_TYPE` (`0x0180`), headerSize 8, declared size 44, and `44 - 8 = 36 = 9 x uint32` with zero remainder — the nine ids sit exactly inside the declared chunk and the next chunk (start-namespace `0x0100`) begins at 248, matching the entry's item 4 table (entry:55-57). The nine values equal the readout's `ids` array element for element.

## 4. Field-by-field verdict against the entry's embedded line

Every field present in the output is compared; the entry embeds the whole line, so the comparison is exhaustive by construction.

| field | actual stdout | embedded (entry:79) | verdict |
|---|---|---|---|
| `fact` | `"axml_resource_map"` | `"axml_resource_map"` | MATCH |
| `offset` | `204` | `204` | MATCH (independently confirmed: chunk header read at payload offset 204, entry:55 chunk table agrees) |
| `entry_count` | `9` | `9` | MATCH (equals string-pool `stringCount` 9, entry:63) |
| `ids` length | 9 | 9 | MATCH (no truncation, no elision in this line) |
| `ids[0..4]` | `0x00000000` x5 | same | MATCH |
| `ids[5]` | `0x0101021b` | `0x0101021b` | MATCH; equals start-element `res_id` 16843291 (entry:82 attributes[1]) |
| `ids[6]` | `0x0101021c` | `0x0101021c` | MATCH; equals `res_id` 16843292 (entry:82 attributes[2]) |
| `ids[7..8]` | `0x00000000` x2 | same | MATCH |
| `nonzero` keys | `versionCode`, `versionName` | same | MATCH; keys resolve to indices 5 and 6 of the string pool (entry:63: `strings[5]="versionCode"`, `strings[6]="versionName"`) |
| `nonzero` values | `0x101021b`, `0x101021c` | same | MATCH as text and as integers (`int(...,16)` == 16843291 / 16843292); textual form differs from `ids` — finding F2 |
| extra/missing fields | none | none | MATCH |

Oracle correspondence (the entry's own claimed correspondence, entry:75):

```
$ python3 -c "... ids == truth.json['axml_declared']['resource_ids'] ..."
ids==oracle.resource_ids: True
entry_count==stringCount: True 9 9
zeros: 7
key maps to index: [(5, 16843291), (6, 16843292)]
```

`truth.json` `axml_declared.resource_ids` is the identical nine-element list (`corpus/fixtures/apk-r65/truth.json:26-35`), and its `attributes` rows (same file, `:3-25`) carry `data=1`/`data=8` for the two version attributes with `ns_idx 0` — consistent with entry:82.

**Verdict: MATCH.** No differing field, in either direction (observed-but-not-embedded or embedded-but-not-observed).

## 5. Judgment of item 7's prose sentence (entry:75)

Sentence: *"The resource-map chunk (offset 204, size 44) holds one `uint32` per string. Seven entries are `0x00000000` and the entries for `versionCode` and `versionName` are **`0x0101021b`** and **`0x0101021c`** — exactly the two framework attribute ids the fixture's authored oracle declares for those strings (`truth.json` `axml_declared.resource_ids`), which is the correspondence this entry claims; the all-zero entries are recorded as observed, and no framework-wide semantics for a zero entry is claimed from this fixture."*

| assertion | supported? | evidence |
|---|---|---|
| chunk at offset 204 | yes | output field `offset=204`; my independent parse |
| size 44 | yes, but not by this fact's output | the `axml_resource_map` JSON has **no size field**; 44 comes from the item 4 embedded `axml_chunk_table` line (entry:56) and my independent parse (`size_field=44`). Traceability nit F1. |
| "holds one `uint32` per string" | yes, jointly | 36 body bytes / 4 = 9 = `stringCount` (entry:63), remainder 0; and S038 states it in words: snapshot lines 251-252 *"This contains a uint32_t array mapping strings in the string pool back to resource identifiers. It is optional."* — item 7 does not quote this. |
| "Seven entries are `0x00000000`" | yes | 7 zeros counted programmatically and by my parse |
| "entries for versionCode and versionName are 0x0101021b / 0x0101021c" | yes | index↔name mapping verified against the string pool |
| "exactly the two … ids the fixture's authored oracle declares for those strings" | yes | exact list equality with `truth.json` `axml_declared.resource_ids` |
| "the all-zero entries are recorded as observed" | yes | output records them, no semantics attached |
| "no framework-wide semantics for a zero entry is claimed" | yes — and conservative | indeed nothing is claimed; note the generator (own code) goes further at `generator.py:58-61` citing `ResXMLTree::getAttributeNameResID` ("returns the entry or 0"); the entry correctly does **not** import that |
| "**framework** attribute ids" | **no** | see F3 |

Nothing in the sentence contradicts the output. The one phrase the output cannot support is the adjective "framework", which asserts an external fact (that these integers are the platform `android.R.attr.versionCode`/`versionName` ids) rather than the observed authored value.

## 6. Findings by severity

**F3 (low, prose provenance) — "framework attribute ids" is unanchored.** The entry attributes framework identity to `0x0101021b`/`0x0101021c` in two places: item 7 (entry:75) and the Inference bullet (entry:157, *"the two non-zero resource-map entries are the framework versionCode/versionName ids the fixture generator declared"*). No registry row backs that identity: `grep -rn "android.R\|public.xml\|attrs_manifest\|0x0101021" corpus/SOURCES.md SKILL.md corpus/README.md corpus/fixtures/apk-r65/generator.py` returns only `generator.py:59-60` (a comment inside the own-work bundle, S041) and `:61` (`RESOURCE_IDS = [0,0,0,0,0,0x0101021B,0x0101021C,0,0]`). S038 is `ResourceTypes.h` format structures — it explains what a resource-map entry *is*, not which integer is which framework attribute. So "framework" is inherited from authored intent, exactly the class of unregistered claim the entry otherwise fences (its own Q01/Q09 language: the oracle "declares" them; a declaration is not a framework anchor). The value is in reality correct (`android.R.attr.versionCode == 0x0101021b`), but the entry must either drop "framework" (say "the two attribute ids the oracle declares") or register a row for the platform attr-id table (`attrs_manifest.xml`/`public.xml` at the pinned tag). Recommended: drop the adjective — cheapest, and the sentence keeps all its load-bearing content.

**F1 (low, traceability) — item 7's own block carries `offset` but not `size 44`.** `axml_resource_map` emits no `size` field (`readout.py:173-175`). A reader checking item 7 in isolation cannot derive "size 44" from the block beneath it; the derivation lives in item 4 (entry:55-57 `axml_chunk_table`, `{"headerSize": 8, "offset": 204, "size": 44, "type": 384}`). Q11 at entry granularity still holds (item 4 is inside §Observation), so this is not a Q11 FAIL — but item 7 would be self-contained if it either quoted item 4's chunk row or added `rm["size"]` to the fact.

**F2 (low, evidence formatting) — the same integer is printed two ways inside one output line.** `ids[5] = "0x0101021b"` but `nonzero.versionCode = "0x101021b"`. Cause: `readout.py:175` uses `f"0x{ids[i]: 08x}".replace(" ", "")`; the spec `" 08x"` is a *sign-space* plus width 8, so the padded field renders `" 101021b"` and the `replace` strips the sign-space, losing the leading zero. Verified:

```
$ python3 -c "i=0x0101021b; print('0x%08x'%i, f'0x{i: 08x}'.replace(' ',''), f'0x{i:08x}')"
0x0101021b 0x101021b 0x0101021b
$ string equal? False False ; integer equal? True True   (both ids)
```

The entry reproduces stdout faithfully and its prose uses the 8-digit `ids` form, so the entry is not wrong — but any consumer (or mutant harness) that string-compares `nonzero` against `ids` sees inequality for equal values. This is a spoof-shaped hazard in the review surface, not in the entry's claims.

**F4 (low, registry hygiene) — S038's recorded anchor span stops short of the anchor this item leans on.** `corpus/SOURCES.md:52` records the chunk-type enum as `:239-250`; the entry cites the enum block as **237-253** and derives `RES_XML_RESOURCE_MAP_TYPE` at **:253** (entry:1, entry:57; snapshot line 253 verified: `RES_XML_RESOURCE_MAP_TYPE = 0x0180`). Scope text still covers the chunk family, but the row's anchor list omits :253, the one line that licenses the resource-map chunk type. Extending the row's anchor list to :253 (S046 derives it, `enum RES_XML_RESOURCE_MAP_TYPE : 253`) closes the gap.

**[INFERENCE] F5 (low, readout robustness) — the fact cannot detect a count mismatch.** `readout.py:172` builds the id list as `[u32(axml, rm["offset"] + 8 + 4*i) for i in range(string_count)]`, taking the count from the string pool and ignoring the resource-map chunk's own `size` field. A resource map declaring fewer entries than the string pool would be read straight through into the following chunk's bytes while still reporting `entry_count: 9` — so "one uint32 per string" is the code's assumption, not something this fact can falsify. In this fixture no over-read occurs (independent parse: body 36 = 9x4, remainder 0, next chunk `0x0100` at 248), so no observed value is affected; the residual risk is a mutant that changes the map header count. Not exploitable from the entry as written; noted for the C7/C2 mutant seats.

**No entry-drift class present here.** Unlike the round-65/r67 `:244` and 15-byte-hex classes, item 7 contains no hand-transcribed spec line number and no hand-copied hex: its only numbers (204, 9, the nine ids, 7 zeros) come from the one embedded stdout line, and that line is byte-identical to the command's output.

## 7. Residual risk and verification gaps

- **Not verified by this seat:** the round-67 v2 candidate file and the `:244`→`:245` / `685-687` deltas, the `557d...`-class stdout hash history, `corpus/derive_axml_anchors.py` end-to-end (`:253` verified directly in the snapshot instead — 253 is `RES_XML_RESOURCE_MAP_TYPE`, 244 is `RES_XML_FIRST_CHUNK_TYPE`, 245 is `RES_XML_START_NAMESPACE_TYPE`, matching item 11's table), the C7 gate over the entry (`C7_V3_CLEAN`), and the README/`K_HELD_BACKED` counters. Those belong to sibling seats; no claim here depends on them.
- **Item 7's verdict in isolation:** MATCH, and it does not by itself threaten the C2 pass branch. F3 is the only finding that could move a Q decision (Q01 source-tier / Q09 overclaim) if the adjudicating seat treats "framework attribute ids" as a load-bearing provenance assertion; my read is that it is a prose qualifier over an own-work oracle and should be fixed by deletion, not by rejecting the candidate.
- **Scope honesty:** one fixtured fixture, one resource map, no general AXML/ZIP behavior inferred. The parenthetical "optional" in S038 :252 (the map chunk may be absent) is not exercised by this fixture.

## 8. Tooling

No installs or upgrades were performed; no package manager was invoked (host-wide pacman pause respected). Tools used: system `python3` (3.x, stdlib `zipfile`/`struct`/`json`/`hashlib`), `sha256sum`, `diff`, `sed`/`awk` for line addressing only — all read-only.
