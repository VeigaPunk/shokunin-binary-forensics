MATCH — the v3 entry's oracle-comparison paragraph claims nothing the oracle and the readout disagree on: 49/49 shared value fields agree, 0 mismatches.

# R68OracleCorrespondence — v3 entry vs authored oracle (round 68)

Every shared field in `corpus/knowledge/round-68-apk-axml-byte-evidence.md ## Comparison with the authored oracle` agrees with the oracle: 49/49 value-level comparisons match, 0 mismatches, over the readout's actual 15-line stdout (sha256 `507d79f8…dad247`, exit 0); the only divergences found are notation-only and neither is claimed in that paragraph.

Seat: read-only oracle-correspondence reviewer. No file in `corpus/`, `reports/`, or the lane git/jj state was modified; no tool was installed or upgraded (none needed). No writes outside this report; scratch files in `/tmp` only.

## 1. Reproduced input (the readout's actual stdout, not a quoted copy)

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68oc.log        # exit 0
sha256sum /tmp/r68oc.log                                              # 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
wc -l /tmp/r68oc.log                                                  # 15
```

- stdout digest equals the digest the entry claims at `corpus/knowledge/round-68-apk-axml-byte-evidence.md:194` (`507d79f8…dad247`, 15 lines, exit 0) — the entry's §Reproduce receipt is faithful on this host.
- 15 fact lines, in order: `archive, spec_derived_struct_widths, eocd, member[AndroidManifest.xml], member[classes.dex], member[META-INF/MANIFEST.MF], axml_chunk_table, axml_string_pool, axml_resource_map, axml_start_namespace, axml_end_namespace, axml_start_element, axml_end_element, dex_declared_header, jar_manifest`.
- Input files, hashed here: `fixture.apk` `05d2280f…f7d03e` (947 bytes), `readout.py` `92e347c3…8ef8c13976` (equals the entry's :194 claim), `truth.json` `27303bae…5b4f8173`, `generator.py` `eaa9444c…930c27c1a` (equals the prefix pinned in `corpus/SOURCES.md:55`, S041).
- Non-circularity: `grep -n "open(\|truth\|json.load\|read_bytes\|Path(" corpus/fixtures/apk-r65/readout.py` → `20:ROOT = Path(__file__).resolve().parent` and `44: apk = APK.read_bytes()`; the readout never opens `truth.json`. The comparison is therefore readout-vs-oracle, not oracle-echoed-as-readout.

## 2. Field-by-field: oracle value (truth.json) vs readout value (actual stdout)

Oracle pointers are `corpus/fixtures/apk-r65/truth.json`; readout pointers are fact name in `/tmp/r68oc.log` (reproduced by `python3 -B corpus/fixtures/apk-r65/readout.py --fact <name>`).

### 2.1 Image digest and size

| field | oracle (truth.json) | readout (`archive`) | verdict |
|---|---|---|---|
| `image.sha256` | `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (truth.json:71) | `05d2280f…f7d03e` (`archive.sha256`) | MATCH |
| `image.size` | `947` (truth.json:72) | `947` (`archive.bytes`); `stat -c %s` = 947 | MATCH |

### 2.2 Three members — offsets / sizes / CRC-32 (plus the members' sha256, which the paragraph does not even claim)

| member | field | oracle | readout | verdict |
|---|---|---|---|---|
| AndroidManifest.xml | `local_header_offset` | 0 (:78) | 0 | MATCH |
| AndroidManifest.xml | `compressed_size` | 416 | 416 | MATCH |
| AndroidManifest.xml | `uncompressed_size` | 416 | 416 | MATCH |
| AndroidManifest.xml | `crc32` | `962d075f` (:77) | `962d075f` (`crc32`, `crc32_matches:true`, `crc32_recomputed:962d075f`) | MATCH |
| AndroidManifest.xml | `sha256` | `73d1e0f2…afe9fae4` (:81) | `73d1e0f2…afe9fae4` | MATCH |
| classes.dex | `local_header_offset` | 465 (:87) | 465 | MATCH |
| classes.dex | `compressed_size` | 112 | 112 | MATCH |
| classes.dex | `uncompressed_size` | 112 | 112 | MATCH |
| classes.dex | `crc32` | `2635c82a` (:86) | `2635c82a` | MATCH |
| classes.dex | `sha256` | `57cfe887…f8d548c2` (:90) | `57cfe887…f8d548c2` | MATCH |
| META-INF/MANIFEST.MF | `local_header_offset` | 618 (:96) | 618 | MATCH |
| META-INF/MANIFEST.MF | `compressed_size` | 69 | 69 | MATCH |
| META-INF/MANIFEST.MF | `uncompressed_size` | 69 | 69 | MATCH |
| META-INF/MANIFEST.MF | `crc32` | `e948d738` (:95) | `e948d738` | MATCH |
| META-INF/MANIFEST.MF | `sha256` | `2e5da249…03c0a49` (:99) | `2e5da249…03c0a49` | MATCH |

### 2.3 The nine strings

| field | oracle | readout (`axml_string_pool`) | verdict |
|---|---|---|---|
| `stringCount` | 9 (len of `strings`, :37) | 9 | MATCH |
| `strings[0..8]` | `android`, `http://schemas.android.com/apk/res/android`, `manifest`, `package`, `com.example.r65`, `versionCode`, `versionName`, `1`, `1.0` | identical, same order | MATCH ×9 |

### 2.4 The three attribute rows

Oracle keys are `name_idx / ns_idx / raw_value_idx / data_type / data`; readout keys are `name_index / ns_index / raw_value_index / data_type (hex string) / data_type_string|data_type_int_dec` (the readout renames the Res_value `data` field by its interpretation: string index vs integer). `data_type` was compared after `int(x,16)` on the readout's hex form.

| attr | field | oracle | readout | verdict |
|---|---|---|---|---|
| 0 `package` | `name_idx` | 3 (:7) | 3 | MATCH |
| 0 | `ns_idx` | 4294967295 | 4294967295 (`ns:null`) | MATCH |
| 0 | `raw_value_idx` | 4 | 4 (`raw_value:"com.example.r65"`) | MATCH |
| 0 | `data_type` | 3 | `0x03` → 3 | MATCH |
| 0 | `data` | 4 | `data_type_string`=4 | MATCH |
| 1 `versionCode` | `name_idx` | 5 (:14) | 5 | MATCH |
| 1 | `ns_idx` | 0 | 0 (`ns:"android"`) | MATCH |
| 1 | `raw_value_idx` | 7 | 7 (`raw_value:"1"`) | MATCH |
| 1 | `data_type` | 16 | `0x10` → 16 | MATCH |
| 1 | `data` | 1 | `data_type_int_dec`=1 | MATCH |
| 2 `versionName` | `name_idx` | 6 (:21) | 6 | MATCH |
| 2 | `ns_idx` | 0 | 0 | MATCH |
| 2 | `raw_value_idx` | 8 | 8 (`raw_value:"1.0"`) | MATCH |
| 2 | `data_type` | 3 | `0x03` → 3 | MATCH |
| 2 | `data` | 8 | `data_type_string`=8 | MATCH |

### 2.5 The two non-zero resource ids

| field | oracle | readout (`axml_resource_map`) | verdict |
|---|---|---|---|
| `resource_ids` (9 entries) | `0,0,0,0,0,0x0101021b,0x0101021c,0,0` (:26) | identical 9-entry `ids` array | MATCH |
| non-zero pair, by value | `0x0101021b`, `0x0101021c` | `0x101021b`, `0x101021c` — `int(...)` = 16843291 / 16843292, equal to the oracle's | MATCH (value) |
| non-zero pair, names | `versionCode`, `versionName` | `nonzero: {versionCode, versionName}` | MATCH |
| attr[1] res_id cross-check | `0x0101021b` = 16843291 | `attributes[1].res_id` = 16843291 | MATCH |
| attr[2] res_id cross-check | `0x0101021c` = 16843292 | `attributes[2].res_id` = 16843292 | MATCH |

Notation-only divergence (not a value disagreement, and not a field the paragraph claims): the readout prints the *secondary* `nonzero` map unpadded (`0x101021b`) while the oracle and the readout's own `ids` array print `0x0101021b`. `python3 -c "print(hex(int('0x101021b',16)), int('0x101021b',16)==16843291)"` → `0x101021b True`. Entry item 7 (`…:75`) quotes the padded form `0x0101021b`, which the readout does print in `ids`, so the entry's printed value is not a silent normalisation.

### 2.6 Build recipe (declared by the oracle; not a readout field)

| field | oracle | readout | verdict |
|---|---|---|---|
| `build_recipe.members[].name` | `AndroidManifest.xml`, `classes.dex`, `META-INF/MANIFEST.MF` | same three (`member[*]` facts) | MATCH |
| `build_recipe.members[].bytes` | 416, 112, 69 | `uncompressed_size` 416, 112, 69 | MATCH |
| `build_recipe.command/container/determinism/python_version` | `python3 -B generator.py`; ZIP_STORED + fixed DOS date_time; `3.14.8` | readout emits nothing for these | oracle-only, not comparable |

## 3. One-sided fields (deliberately outside the comparison, recorded so "every shared field" is auditable)

Oracle-only: `image.path` (`fixture.apk`, resolved beside truth.json), `members[].method` (all 0), `build_recipe.*` prose. Readout-only: `payload_offset` (49/506/668), `payload_first16_hex`, `cd_index`, `crc32_matches`, `spec_derived_struct_widths`, `axml_chunk_table`, `axml_string_pool.offsets/flags/utf8`, `axml_start_element.attributeStart/attributeSize/attributeCount/classIndex/idIndex/styleIndex/lineNumber/offset`, `dex_declared_header`, `jar_manifest`. None of these is asserted by the paragraph as agreeing.

`image.path` is the one field both sides report in different notation (oracle `fixture.apk` vs readout `corpus/fixtures/apk-r65/fixture.apk`); same file, proven by the equal `05d2280f…` digest, and the paragraph does not list path among the agreed fields.

## 4. Independent cross-check that the oracle itself is right (not just mutually consistent)

Read the container with the standard library instead of the readout (`zipfile.ZipFile('corpus/fixtures/apk-r65/fixture.apk')`, `zf.read()`, `zlib.crc32`, `hashlib.sha256`), 18 oracle fields checked: `uncompressed_size`, `compressed_size`, `crc32`, `sha256`, `method`, `local_header_offset` for all three members → **0 MISMATCH**; image sha256 and size re-derived from the raw bytes → both true. So the oracle's member values are container facts, not artefacts of the readout's parse.

## 5. Does the paragraph claim anything the two disagree on?

`corpus/knowledge/round-68-apk-axml-byte-evidence.md:150-152`, sentence by sentence:

1. "The oracle declares the image digest and size, the three members with their measured offsets, sizes and CRC-32 values, the declared AXML string table, attribute table and resource-map ids, and the build recipe." — TRUE. `truth.json` keys are exactly `image`, `members`, `axml_declared{strings,attributes,resource_ids}`, `build_recipe`; each named datum exists at the pointers in §2.
2. "The readout values agree with it on every shared field: image sha256 and size (item 1), the three members' local-header offsets, payload sizes and CRC-32 values (item 3), the nine strings, the three attribute rows and the two non-zero resource ids (items 6-8)." — TRUE, and the item cross-references resolve: item 1 at `:21`, item 3 at `:35`, item 6 at `:68`, item 7 at `:75`, item 8 at `:82`. 49/49 shared values match. The claim is conservative in two directions: per-member `sha256` and `method` also match but are not claimed, and readout-only fields are not claimed as agreed.
3. "Regenerating the fixture from generator.py in a scratch directory on this host was round-65 evidence (S041) and is not re-run by this entry; the committed bytes are hash-pinned above." — the non-re-run disclaimer is honest and matches the entry's Q06 wording (`:177`). The cited row exists: `corpus/SOURCES.md:55` (S041, tier A) pins `fixture.apk 05d2280f…`, `truth.json 27303bae…`, `generator.py eaa9444c…`; the local hashes in §1 reproduce all three. **Wording nit (not a disagreement):** "the committed bytes are hash-pinned above" — the *oracle* file's own digest (`27303bae…`) is pinned in SOURCES.md S041 but **not** in the entry; `grep -n "27303bae"` over the entry returns nothing, so a reader of the entry alone cannot verify the bytes it compares against. Same for `generator.py`. Both are reachable through the cited S041 row, so this is a support-strength note, not an overclaim.
4. Nothing in the paragraph asserts that the oracle validates install validity, dex program validity, provider behaviour, or cross-fixture generality; §Limitations (`:160-162`) and §Cross-lane scope note (`:164`) hold that fence.

**Conclusion: the paragraph claims nothing the two disagree on. Verdict MATCH.**

## 6. Embedded-output fidelity (adjacent C7 surface, checked because the paragraph's evidence is embedded stdout)

All readout command blocks in the entry (13 fences, 15 command invocations including the three `member[...]` facts and the full run) were re-executed and compared byte-for-byte: **15/15 exact, 0 drift**. The full-run fence at `:198-215` is byte-identical to `/tmp/r68oc.log`. No `…` ellipsis exists in the file — the truncations seen during this review were my shell's display limit, not the entry's content.

## 7. Residual risk and verification gaps

- **Determinism of `generator.py` is not re-verified here.** Neither the entry nor this seat re-runs it (entry says so explicitly; I did not run it either). Host `python3 -V` = `3.14.8`, equal to the oracle's declared `build_recipe.python_version`, which supports but does not prove byte-for-byte reproducibility. If a later seat re-runs it, do it in a scratch dir and compare `05d2280f…`.
- **Oracle self-consistency is verified only against the container** (§4). The AXML/dex *semantics* the oracle's numbers are supposed to mean are out of this seat's scope (items 4-5, 9-11) and were not judged.
- **`image.path` and the `nonzero` hex form differ in notation only**; both are benign, and neither is claimed as character-identical anywhere in the entry.
- **This seat used no language server**: the check is byte/value comparison of committed files, where text extraction (not symbol resolution) is the correct instrument; `lsp` semantic queries would add nothing to a hex/JSON equality claim.
- No tool install or upgrade was needed; no pacman/uv channels touched.
