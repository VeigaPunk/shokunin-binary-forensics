MATCH — the `axml_string_pool` fact re-derives byte-identically to both embedded copies (`round-68-apk-axml-byte-evidence.md:72` and `:207`) on all 11 fields, the prose sentence states nothing the output does not support, and the pool independently decodes from the fixture's raw bytes to the same values.

Seat: L1Revenger68.R68Item6 (leaf, read-only). Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`. No edits made outside this report. No tools installed or upgraded.

## 1. Command and actual output (item 6 fact)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool
{"fact": "axml_string_pool", "flags": "0x00000100", "offset": 8, "offsets": [0, 10, 55, 66, 76, 94, 108, 122, 126], "sorted_flag": false, "stringCount": 9, "strings": ["android", "http://schemas.android.com/apk/res/android", "manifest", "package", "com.example.r65", "versionCode", "versionName", "1", "1.0"], "stringsStart": 64, "styleCount": 0, "stylesStart": 0, "utf8": true}
EXIT=0
```

Entry's embedded line, byte-for-byte the same JSON:

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:72` (item 6 block)
- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:207` (the §Reproduce full-stdout block; the entry claims at `:196` that "every line also appears in the per-item blocks above")

Equality was tested as `entry_line.strip() == json.dumps(live, sort_keys=True)` — not by eye, and `True` for both (`:72` and `:207`).

## 2. Member fact runs (requested alongside)

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

Each of these is also an exact match to the two places the entry embeds it (same `sort_keys` equality test): `AndroidManifest.xml` → `:39`, `:203`; `classes.dex` → `:41`, `:204`; `MANIFEST.MF` → `:43`, `:205`.

Full-run cross-check of the entry's §Reproduce receipt (`:194`): `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, **15** stdout lines, `sha256(stdout + "\n") = 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — matches the claimed digest exactly.

## 3. Field-by-field verdict (live vs entry line 72 / line 207)

All 11 emitted fields compared programmatically; key sets identical (no field added, dropped or renamed in the entry):

| field | live | entry `:72` and `:207` | verdict |
|---|---|---|---|
| `fact` | `"axml_string_pool"` | same | equal |
| `flags` | `"0x00000100"` | same | equal |
| `offset` | `8` | same | equal |
| `offsets` | `[0, 10, 55, 66, 76, 94, 108, 122, 126]` | same | equal |
| `sorted_flag` | `false` | same | equal |
| `stringCount` | `9` | same | equal |
| `strings` | 9 items, `android` … `1.0` | same, same order | equal |
| `stringsStart` | `64` | same | equal |
| `styleCount` | `0` | same | equal |
| `stylesStart` | `0` | same | equal |
| `utf8` | `true` | same | equal |

Differing fields: **none** (0/11). `exact_string_equal: True` for both lines, so serialization order/spacing also matches the readout's `json.dumps(..., sort_keys=True)` output.

## 4. Independent re-derivation from the fixture bytes (not via readout.py)

Raw `struct` walk over `zipfile.ZipFile("corpus/fixtures/apk-r65/fixture.apk").read("AndroidManifest.xml")` (416 bytes), reading the pool header at absolute offset 8 with S038's field order (header, stringCount, styleCount, flags, stringsStart, stylesStart — snapshot `corpus/snapshots/ResourceTypes.h:461-488`):

```
chunk type/hs/size 0x1 28 196
stringCount 9 styleCount 0 flags 0x100 stringsStart 64 stylesStart 0
offsets [0, 10, 55, 66, 76, 94, 108, 122, 126]
strings ["android","http://schemas.android.com/apk/res/android","manifest","package","com.example.r65","versionCode","versionName","1","1.0"]
```

Every value equals the readout's. Additional arithmetic checks, all consistent:

- Per-string prefix bytes (abs = 8 + 64 + rel): `(0,7,7) (10,42,42) (55,8,8) (66,7,7) (76,15,15) (94,11,11) (108,11,11) (122,1,1) (126,3,3)` — for each string, `start + 2 + u8len + 1` (NUL) lands exactly on the next offset, and the last one lands at abs **204** = chunk offset 8 + size 196 = the resource-map chunk's offset. So the string data fills the chunk with no padding and the offsets are self-consistent.
- `sorted_flag=false` is consistent with `flags=0x00000100` (bit 0 clear) and with S038 `SORTED_FLAG = 1<<0` (`snapshots/ResourceTypes.h:477`); `utf8=true` is consistent with `UTF8_FLAG = 1<<8` (`:480`), so `0x100` is indeed the UTF-8 flag.
- The agent-claimed `readout.py:166` anchor is exact: `166:         utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),`; the fact is emitted at `readout.py:164`.
- The authored oracle `corpus/fixtures/apk-r65/truth.json` → `axml_declared.strings` is the identical 9-string list in the same order — an expected value fixed outside the record under test (supports the entry's Q03 basis for this fact).

## 5. Prose judgement (`:68`)

Sentence under test: *"The string-pool chunk (offset 8, size 196) declares **9** strings, **0** styles, flags **`0x00000100`** — bit `0x100` set, the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166) — with string data starting 64 bytes into the chunk. The nine strings, decoded as length-prefixed UTF-8 from the offsets the pool states, are:"*

Clause-by-clause, does the output support it?

| clause | supported? | basis |
|---|---|---|
| offset 8 | yes | output `offset: 8` |
| size 196 | yes, but **not from this fact's output** | from the entry's own item-4 block `:60` (`{"headerSize": 28, "offset": 8, "size": 196, "type": 1}`), which I re-ran (exit 0) and confirmed by raw parse (type `0x1`, size 196, end 204). Traceability nit only: the sentence's size rests on the adjacent fact, and the entry does not claim the string-pool command emits `size`. |
| 9 strings | yes | `stringCount: 9` and `len(strings) == 9` |
| 0 styles | yes | `styleCount: 0` (and `stylesStart: 0`) |
| flags `0x00000100` | yes | `flags: "0x00000100"` |
| bit `0x100` set = UTF-8 flag, tested at readout.py:166 | yes | `utf8: true`; `readout.py:166` text verified; `UTF8_FLAG = 1<<8` at `snapshots/ResourceTypes.h:480` |
| string data starts 64 bytes into the chunk | yes | `stringsStart: 64`, chunk-relative (first string decodes at abs 8+64=72) |
| "length-prefixed UTF-8 from the offsets the pool states" | yes | `offsets` come from the pool's own uint32 index array; strings decode as UTF-8; `utf8: true` |

Unsupported statements: **none found**. The sentence makes no claim about `sorted_flag`, about general AXML pools, or about varint decoding — it stays inside the observed fields.

One depth note, not a defect: the readout reads the UTF-8 length prefix as a fixed 2-byte pair (`u16len = axml[base]; u8len = axml[base+1]`, `readout.py:158-160`, with `assert len(s) == u16len`) rather than the spec's 1–2 byte varint. This is harmless for this fixture — every prefix byte for all nine strings has its high bit clear (`hi_bit_any=False` for all nine; max length 42) — and the entry makes no varint claim and fences to "UTF-8 string pool only" in §Limitations (`:156`). It is a robustness boundary of the reader, not a mismatch of the record.

## 6. Cross-round copy census (drift attribution for this fact)

All copies of this fact across the three retained candidate generations are byte-identical to live stdout, i.e. the string-pool claim was never the drifted value:

```
round-65:68 exact=True
round-67:71 exact=True
round-67:179 exact=True
round-68:72 exact=True
round-68:207 exact=True
```

So the M39 drift the round-68 entry repairs (`entry:41` in the r65 draft) is elsewhere; this fact contributes no drift and no new delta relative to r67.

## 7. Risks / blockers

- Risk (scoped): if the string pool's `size` were ever re-derived from a different chunk than the one this fact reads, the sentence's "size 196" would silently lean on item 4. It is currently correct and independently confirmed; no action needed for these bytes.
- Observation for the L1 (not mine, not caused by this seat): `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` appeared at 2026-10-25T03:29:00-03:00 while this seat was running — a sibling's C1 gate execution, untracked. It cannot pollute the C2 count (`git archive <commit> corpus | tar -x` ships tracked files only), but it must not be `git add`-ed at cutover.
- No blocker. Nothing was written outside this report; `corpus/` (tracked files), `reports/`, `README.md`, `.git`/jj state untouched. No mutation guessing: this seat made no production edits, so the C2/C7 predicates are unchanged by it.

Report: `.ufo/waves/round-68/R68Item6.md`
