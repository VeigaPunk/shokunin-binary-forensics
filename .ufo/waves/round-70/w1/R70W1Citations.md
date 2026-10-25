FAIL — 21 citations resolve, 3 located citation defects (APPNOTE ranges 387-398 and 511-531 do not contain the fields the entry attributes to them; "five derivation flags" lists six) plus 1 range-precision defect at `readout.py:164-168`.

Target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `aa1842fac199aa524930e5565ed3715de5f84c6d`, `admission-status: candidate` (line 12). Working-tree bytes equal that commit for this file and for every file it cites (verified by digest: item 14 pins all match, below). Every command was run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Defects (each with path:line + the command output that shows it)

### D1 — entry:4 and entry:152, APPNOTE §4.3.12 cited as `lines 511-531`: the range stops 7 lines before the four offsets item 12 attributes to the spec

Entry line 4: `scope: the record layouts of §4.3.7 local file header (snapshot lines 387-398), §4.3.12 central directory file header (lines 511-531) and §4.3.16 end of central directory record (lines 632-646)`.
Entry line 152 repeats: `the layouts are APPNOTE snapshot lines 387-398, 511-531 and 632-646`.

```
$ awk 'NR>=511 && NR<=538{printf "%d: %s\n", NR, $0}' corpus/snapshots/APPNOTE.TXT
511:    4.3.12  Central directory structure:
...
522:         central file header signature   4 bytes  (0x02014b50)
...
531:         uncompressed size               4 bytes
532:         file name length                2 bytes
533:         extra field length              2 bytes
534:         file comment length             2 bytes
...
538:         relative offset of local header 4 bytes
```

The fixed part of the record is lines 522-538 (17 fields, 46 bytes). The four offsets item 12 prints as spec-derived — `central.name_length: spec offset 28`, `central.extra_length: spec offset 30`, `central.comment_length: spec offset 32`, `central.local_header_offset: spec offset 42` — sit on lines 532, 533, 534 and 538, all outside `511-531`. A reader who follows the citation to check any of those MATCH lines cannot find the field. Same wrong range is hard-coded in the transcription the entry names as its source: `corpus/fixtures/apk-r65/entry_checks.py:47` `# (snapshot lines 387-398 section 4.3.7, 511-531 section 4.3.12, 632-646 section 4.3.16).`, while `CENTRAL_HEADER` (`entry_checks.py:51-55`) lists all 17 fields. Repair: `511-538` (or `522-538` for the fixed part) in both places.

### D2 — entry:4 and entry:152, APPNOTE §4.3.7 cited as `snapshot lines 387-398`: the range omits `extra field length` (line 399), which the 30-byte fixed part and the S034 scope sentence both require

```
$ awk 'NR>=387 && NR<=400{printf "%d: %s\n", NR, $0}' corpus/snapshots/APPNOTE.TXT
387:    4.3.7  Local file header:
389:       local file header signature     4 bytes  (0x04034b50)
...
398:       file name length                2 bytes
399:       extra field length              2 bytes
```

`entry_checks.py:48-50` transcribes 11 fields including `("extra_length", 2)`; their sum is the printed `local fixed part: 30 bytes`. Lines 389-398 hold only 10 fields (28 bytes). The S034 header line (entry:5) explicitly scopes the row to "the file-name and extra-field length offsets", and the extra-field length offset is on line 399. Repair: `387-399` in entry:4, entry:152 and `entry_checks.py:47`.

### D3 — entry:273, "The five derivation flags" lists six flags

```
$ awk 'NR==273{print NR": "$0}' corpus/knowledge/round-70-apk-axml-byte-evidence.md
273: ... The five derivation flags are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--spec-quotes` and `--stdout-digest` of `corpus/fixtures/apk-r65/entry_checks.py`.
$ grep -n 'cmds = ' corpus/fixtures/apk-r65/entry_checks.py
195:    cmds = {"--pins": pins, "--eocd": eocd, "--oracle": oracle, "--zip-layout": zip_layout,
196:            "--stdout-digest": stdout_digest, "--spec-quotes": spec_quotes}
```

Six names, six flags. (Entry:9's `the five entry_checks.py flags named in items 11-15` is correct — items 11-15 name exactly five, `--eocd` is in item 2.) Repair: "six" at entry:273, or drop `--eocd` from that sentence. This is a prose count, the class the Q14 lint reads.

### D4 (minor) — entry:72, `readout.py:164-168` cited for "the strings the readout decodes from the offsets the pool states": 164-168 is the `emit` call, the decode loop is 157-163

```
$ awk 'NR>=155 && NR<=168{printf "%d: %s\n", NR, $0}' corpus/fixtures/apk-r65/readout.py
155:     offsets = [u32(axml, so + sp["headerSize"] + 4 * i) for i in range(string_count)]
156:     strings = []
157:     for rel in offsets:
158:         base = so + strings_start + rel
159:         u16len = axml[base]
160:         u8len = axml[base + 1]
161:         s = axml[base + 2:base + 2 + u8len].decode("utf-8")
162:         assert len(s) == u16len
163:         strings.append(s)
164:     emit("axml_string_pool", offset=so, stringCount=string_count,
...
168:          offsets=offsets, strings=strings)
```

The sentence's own second citation (`readout.py:166`, `flags & 0x100`) is inside the cited range and TRUE; only the range start is short. Repair: `readout.py:155-168`.

## Full resolution table

| entry line | citation | what the cited file says there | verdict |
|---|---|---|---|
| 2 | `rea-android-applications.md` "first line 7" | `7: Start with \`inspect_android_package\` on the caller's APK path for package` / `8: identity, manifest declarations, coverage, and inline Evidence.` — folded phrase starts on 7 | TRUE |
| 4 | APPNOTE "snapshot lines 387-398" (§4.3.7) | 387 heading, 389-399 the 11 fields, 399 = `extra field length 2 bytes` outside the range | **FALSE (D2)** |
| 4 | APPNOTE "(lines 511-531)" (§4.3.12) | 511 heading, 522-538 the 17 fields, 532/533/534/538 = name/extra/comment length and relative offset of local header outside the range | **FALSE (D1)** |
| 4 | APPNOTE "(lines 632-646)" (§4.3.16) | 632 heading, 634-646 the 8 fields, 646 = `.ZIP file comment length 2 bytes` — fixed part complete | TRUE |
| 30 | `readout.py:76`, constant `b"PK\x05\x06"` | `76: sig_eocd = b"PK\x05\x06"` (the `rfind` using it is 77) | TRUE |
| 39 | `readout.py:105` `payload_offset = local_header_offset + 30 + name_length + extra_length` | `105: payload_off = lh_off + 30 + lh_name_len + lh_extra_len` | TRUE |
| 63 | `readout.py:51-58` (manual width transcription) | 51 `w8, w16, w32 = 1, 2, 4`, 52 `widths = {`, 53-58 the six struct rows ending `"Res_value": [w16, w8, w8, w32]` | TRUE |
| 72 | `readout.py:164-168` (decode from pool offsets) | 164-168 is `emit("axml_string_pool", ... offsets=offsets, strings=strings)`; decode is 157-163 | **FALSE (D4, minor)** |
| 72 | `readout.py:166`, `flags & 0x100` | `166: utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),` | TRUE |
| 86 | `readout.py:203` `aoff = base + 16 + attribute_start + i * attribute_size` | `203: aoff = base + 16 + attribute_start + i * attribute_size` | TRUE |
| 86 | `readout.py:211`, `strings[ans]` | `211: "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],` | TRUE |
| 86 | `NO_INDEX` 0xFFFFFFFF at `readout.py:22` | `22: NO_INDEX = 0xFFFFFFFF` | TRUE |
| 101 | `readout.py:233-248` (dex declared header) | 233 `magic = dex[:8]` … 248 `header_bytes=len(dex))` — the whole `dex_declared_header` emit | TRUE |
| 152 | `387-398`, `511-531`, `632-646` | as rows 2-4 | **FALSE, FALSE, TRUE** |
| 234 | `readout.py:203`, literal 16 = chunk `headerSize` | item 4 start-element chunk `{"headerSize": 16, "offset": 272, ...}`, item 5 `node_header_size: 16` | TRUE |
| 239 | `readout.py:49-50` comments widths "computed here ... not assumed" | `49: # Every fixed offset the readout uses is computed here from the field` / `50: # widths in ResourceTypes.h's own struct definitions, not assumed.` | TRUE |
| 273 | "The five derivation flags" | six flags named; `entry_checks.py:195-196` defines six | **FALSE (D3)** |
| 144-149 (embedded `--spec-quotes` output) | `first line 7 / 5949 / 5956 / 5981 / 5035 / 686` | 5949 `adler32 checksum of the rest of the file (everything but`; 5956 `SHA-1 signature (hash) of the rest of the file (everything but`; 5981 `<p>must be 0x70 (112) bytes` + 5982 `(v40 or earlier)`; 5035 `uint ENDIAN_CONSTANT = 0x12345678;`; 686 `// Byte offset from the start of this structure where the attributes start.` | TRUE (all six) |
| item 11 block (S038 anchors) | 218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263, 287, 461, 612, 621, 677, 686, 687 | each line matches the printed symbol/value (`RES_XML_FIRST_CHUNK_TYPE = 0x0100` at 244 and `RES_XML_START_NAMESPACE_TYPE = 0x0100` at 245 both exist; 687 `uint16_t attributeStart;`) | TRUE (all 18) |

## Re-derivations that back the table (commands + actual output)

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/...; wc -l; sha256sum
exit=0 / 15 / 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```
matches item 15 (`readout stdout: 15 lines, sha256 507d79f8…`) byte for byte.

```
$ python3 -B corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218 ... field attributeStart : 687
```
identical to item 11's block (19 lines), exit 0.

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout   # exit 0, 17 lines, identical to item 12
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes  # exit 0, 6 MATCH lines, identical to item 11
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd
eocd signature bytes at offset 925: 504b0506 (4 bytes)
```
`entry_checks.py:109-113` really does `apk.rfind(b"PK\x05\x06")` then `apk[pos:pos+4].hex()`, so entry:30's "reads those four bytes back from the archive at the printed offset" is TRUE as written.

Item 14 pins re-hashed, all nine identical to the printed digests and sizes: fixture.apk `05d2280f…` 947; truth.json `27303bae…` 2466; generator.py `eaa9444c…` 9599; readout.py `92e347c3…` 11236; derive_axml_anchors.py `74d4c0d9…` 4979; ResourceTypes.h `56b88bc4…` 86255; APPNOTE.TXT `0b993022…` 174585; dex-format.html `c0428612…` 281157; rea-android-applications.md `412d9cb4…` 1992.

Q14 spot-check on the one prose byte count: `4d616e69666573742d56657273696f6e` = 32 hex chars = 16 bytes (`len=32, bytes=16`), so entry:47's "a 32-hex-character run, which is 16 bytes" is TRUE; item 2's "four signature bytes" is a count on the `b"PK\x05\x06"` literal (exactly 4 bytes), not on a hex run.

## Notes, not findings

- `readout.py:49-50` says the widths are "computed here from the field widths in ResourceTypes.h's own struct definitions, not assumed", while the entry labels them a manual transcription (item 5, Q04). The entry discloses this at entry:239 and does not credit the comment as evidence; no citation defect, but the comment is the one place a reader could mistake transcription for runtime derivation.
- Entry:4's "fetched and committed byte-for-byte as `corpus/snapshots/APPNOTE.TXT`" cannot be resolved from the tree (no upstream fetch; network not used). Digest identity of the committed file is verified; upstream byte-identity is not, and the entry's Unknown section already fences it ("whether the upstream document has since changed is not checked").
- D1/D2 are advisory wave-1 findings under the frozen contract; they are not kill-rule inputs, and fixing them touches only prose ranges in entry:4, entry:152 and the comment at `entry_checks.py:47` — no printed output, pin or predicate changes.

Scratch deleted (`/tmp/revenger-r70-R70W1Citations*`); no lane file was modified. No tool installed.
