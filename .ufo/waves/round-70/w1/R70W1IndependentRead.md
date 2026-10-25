INDEPENDENT-AGREE — all 15 facts `readout.py` prints for items 1-3 and the AXML/dex/manifest blocks reproduce under four implementations that share no code with it (python `zipfile` 3.14.8, Info-ZIP `unzip` 6.00, 7-Zip 26.04, androguard 4.1.4 / apktool 3.0.3 for the AXML); one fixture-fidelity divergence (attribute namespace indices bind to the *prefix* string, not the declared namespace URI) and two advisory prose gaps, no numeric divergence.

Seat R70W1IndependentRead (revenger, leaf) · round 70 wave 1 · Q03 independent derivation + Q04 tool record · read-only on the lane, nothing edited.

## 1. Bytes under test

Extracted from the candidate commit into scratch, never from the working tree:

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive aa1842f corpus/fixtures/apk-r65 | tar -x -C $S/tree
$ sha256sum $S/tree/corpus/fixtures/apk-r65/fixture.apk ; sha256sum <lane>/corpus/fixtures/apk-r65/fixture.apk
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  .../tree/.../fixture.apk
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  .../corpus/fixtures/apk-r65/fixture.apk
$ wc -c < fixture.apk   -> 947
```

Bundle digests, recomputed (compare entry item 14, which prints all four):

```
$ sha256sum fixture.apk truth.json generator.py readout.py ; wc -c fixture.apk truth.json generator.py readout.py
05d2280f…afe7d03e  fixture.apk          947
27303bae…5b4f8173  truth.json          2466
eaa9444c…930c27c1a generator.py        9599
92e347c3…ef8c13976  readout.py        11236
```
Item 14's four bundle rows match byte for byte. Readout stdout, recomputed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py | wc -l      -> 15
$ python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum  -> 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
$ cmp -s readout.out run2.out && echo DETERMINISTIC   -> DETERMINISTIC: two runs byte-identical
```
Item 15's `15 lines, sha256 507d79f8…` matches. Each of the 15 fact ids is reachable by `--fact <id>` and returns exactly 1 line (all 15 checked, `lines=1` each), so item 1-15's `$ … --fact X` commands are honest selectors, not re-derivations.

## 2. Tools exercised (Q04 record)

| tool | version (`cmd`) | function exercised | exit | used for |
|---|---|---|---|---|
| python `zipfile` | 3.14.8, `/usr/lib/python3.14/zipfile/__init__.py` | `ZipFile.testzip`, `infolist`, `read` (name, `header_offset`, `CRC`, `compress_size`, `file_size`, `flag_bits`, `date_time`) | 0 | items 2-3 |
| Info-ZIP `unzip` | 6.00 of 20 Apr 2009 (`unzip -v`) | `-lv` listing, `-t` CRC verification | 0 / 0 | items 2-3 |
| `zipinfo` | 6.00 | `-v` (EOCD offset, CD offset/size/count, per-entry local-header offset, CRC, sizes) | 0 | item 2-3 |
| 7-Zip `7z` | 26.04 x64 | `l -slt` (CRC, `Offset`, sizes), `t` (integrity) | 0 / 0 | items 2-3 |
| `binwalk` | host `/usr/bin/binwalk` | default scan | 0 | item 1 cross-check |
| androguard | 4.1.4 (`androguard --version`; installed this seat by `uv tool install androguard`) | `AXMLPrinter` (chunk walk, namespace map, START_TAG line, attribute name/ns/value resolution), `DEX` (header load) | 0 / 0 | items 4-9 |
| apktool | 3.0.3 (`apktool --version`) | `apktool d -f -o out2 fixture.apk` → `AndroidManifest.xml` | **1** (manifest decoded, dex step throws; see §5) | items 4-8 |
| jadx | 1.5.6 (`jadx --version`) | `jadx -e --no-res --no-src` | **2** (refuses the fixture; see §5) | attempted items 4-9 |
| `file` | host | magic on extracted members | 0 | item 3/9 |
| `sha1sum`, `dd`, `xxd` | coreutils/binutils | raw slices at printed offsets | 0 | items 3, 9, 12 |
| aapt2 / aapt / apkanalyzer | **absent** (`command -v` → MISSING) | — | — | not available on the host |
| manual walks (§4, §5) | — | own `struct` readers written for this seat | 0 | labelled **manual**, never counted as a tool |

`readout.py` writes nothing: `grep -nE "open\(|write|mkdir|extract|subprocess|os\." readout.py` returns only line 5's docstring sentence — the "nothing is extracted to disk" claim (item 3 preamble, `readout.py:2-11`) holds; it uses `Path.read_bytes()` only.

## 3. Fact-by-fact comparison (readout printed value vs independent implementation)

| # | fact (entry item) | readout prints | independent result | verdict |
|---|---|---|---|---|
| 1 | `archive` (1) | 947 / `05d2280f…` | `wc -c` 947, `sha256sum` `05d2280f…`, binwalk "ZIP archive, file count: 3, total size: 947 bytes" | **MATCH** |
| 2 | `spec_derived_struct_widths` (5) | node 16, sp-hdr 28, attrExt 20, attribute 20, Res_value 8 | arithmetic of the declared lists re-summed; corroborated by the bytes: string-pool chunk `headerSize` = 28 (`xxd -s 8`), node `headerSize` = 16, `attributeStart` = `attributeSize` = 20 — and by a real aapt2 manifest, whose `attributeStart`/`attributeSize` are also 20 (§5) | **MATCH** |
| 3 | `eocd` (2) | eocd 925, 3 entries, CD 188 @ 737, `cd_end_equals_eocd_offset: true` | `zipinfo -v`: "Actual end-cent-dir record offset: 925", "central directory contains 3 entries", "188 … bytes long", "offset … is 737"; 737+188=925 | **MATCH** |
| 4 | `member[AndroidManifest.xml]` (3) | lh 0, payload 49, 416/416, crc `962d075f`, sha `73d1e0f2…`, first16 `03000800a001000001001c00c4000000` | `zipfile`: `header_offset=0`, `CRC=962d075f`, `data_sha256=73d1e0f2…`; `dd skip=49 count=416 \| sha256sum` → `73d1e0f2…` (so payload_offset 49 is right, 0+30+19+0); `unzip -t` OK, `7z t` "Everything is Ok" | **MATCH** |
| 5 | `member[classes.dex]` (3) | lh 465, payload 506, 112/112, crc `2635c82a`, sha `57cfe887…`, first16 `6465780a30333500300c123da5fc7bea` | `zipfile` same four values; `dd skip=506 count=112 \| sha256sum` → `57cfe887…` (465+30+11); first16 identical to the `xxd -l 48` header | **MATCH** |
| 6 | `member[META-INF/MANIFEST.MF]` (3) | lh 618, payload 668, 69/69, crc `e948d738`, sha `2e5da249…`, first16 `4d616e69666573742d56657273696f6e` | `zipfile` same; `dd skip=668 count=69 \| sha256sum` → `2e5da249…` (618+30+20); first16 = `Manifest-Version` | **MATCH** |
| 7 | `axml_chunk_table` (4) | 6 chunks: 8/0x0001/28/196, 204/0x0180/8/44, 248/0x0100/16/24, 272/0x0102/16/96, 368/0x0103/16/24, 392/0x0101/16/24; total 416 | `xxd` at 0/8/204/248/272/368/392 confirms every type/headerSize/size; androguard's own walk prints `idx=0xcc type=384 hs=8 size=44`, `0xf8/256/16/24`, `0x110/258/16/96`, `0x170/259/16/24`, `0x188/257/16/24`; 8+196+44+24+96+24+24 = 416 | **MATCH** |
| 8 | `axml_string_pool` (6) | count 9, style 0, flags `0x00000100`, stringsStart 64, stylesStart 0, offsets `[0,10,55,66,76,94,108,122,126]`, 9 strings | manual decode of the raw pool (**manual**) reproduces all nine offsets and all nine strings with `u16len == u8len` (`android`, `http://schemas.android.com/apk/res/android`, `manifest`, `package`, `com.example.r65`, `versionCode`, `versionName`, `1`, `1.0`); androguard emits the same attribute values | **MATCH** |
| 9 | `axml_resource_map` (7) | 9 ids, non-zero at 5/6 = `0x0101021b`/`0x0101021c` | `xxd -s 204 -l 44`: `8001 0800 2c00 0000` + 9 u32, `1b020101` at byte 232 (index 5) and `1c020101` at 236 (index 6); a real aapt2 manifest maps string `versionCode`→`0x0101021b`, `versionName`→`0x0101021c` (§5), matching strings[5]/[6] here | **MATCH** |
| 10 | `axml_start_namespace` (8) | offset 248, line 1, prefix 0 = `android`, uri 1 = the URL | `xxd -s 248`: `0001 1000 1800 0000 0100 0000 ffff ffff 0000 0000 0100 0000`; androguard: "Start of Namespace mapping: prefix 0: 'android' --> uri 1: 'http://schemas.android.com/apk/res/android'" | **MATCH** |
| 11 | `axml_end_namespace` (8) | offset 392, line 1, 0 / 1 | `xxd -s 392`: `0101 1000 1800 0000 0100 0000 ffff ffff 0000 0000 0100 0000` | **MATCH** |
| 12 | `axml_start_element` (8) | offset 272, line 1, ns `NO_INDEX`, name 2 `manifest`, aStart/aSize/count 20/20/3, id/class/style 0; attrs `package`=str"com.example.r65", `versionCode`=int 1 (res 16843291), `versionName`=str"1.0" (res 16843292) | `xxd -s 272 -l 96` confirms every field at its printed offset (attr 0 at 308, attr 1 at 328, attr 2 at 348); androguard: `START_TAG: manifest (line=1)`, `package='b'com.example.r65''`, `{android}versionCode='b'1''`, `{android}versionName='b'1.0''`; apktool decodes `<manifest package="com.example.r65" n0:versionCode="1" n0:versionName="1.0" …/>` | **MATCH** (values), see D1 for the `ns` field |
| 13 | `axml_end_element` (8) | offset 368, line 1, ns `NO_INDEX`, name 2 `manifest` | `xxd -s 368`: `0301 1000 1800 0000 0100 0000 ffff ffff ffff ffff 0200 0000` | **MATCH** |
| 14 | `dex_declared_header` (9) | magic `6465780a30333500`, `dex\n`, `035`, checksum `0x3d120c30` = recomputed, sha1 `a5fc7bea…` = recomputed, file/header 112, endian `0x12345678` | `dd skip=32 \| sha1sum` → `a5fc7bea8fa9ffaa52243540c8026066511b9fce`; **manual** adler32 over `dex[12:]` (no `zlib`) → `0x3d120c30` = declared bytes `300c123d`; `xxd -l 48` gives file_size 0x70=112, header_size 0x70=112, endian `78563412`; `file` → "Dalvik dex file version 035"; androguard `DEX` loads it but warns "no map list! This DEX file is probably empty" (consistent with item 9's "nothing about dex program validity follows") | **MATCH** |
| 15 | `jar_manifest` (10) | 69 bytes, first line `Manifest-Version: 1.0`, section_count 1 | `cat -A`: `Manifest-Version: 1.0^M$` / `Created-By: revenger-r65 fixture generator^M$` / `^M$` → exactly one `\r\n\r\n`; `file` → "JAR Manifest, ASCII text, with CRLF line terminators" | **MATCH** |

**Zero numeric divergences.** Every value readout prints for items 1-3 and for the AXML, dex and manifest blocks is reproduced by at least one implementation that does not import or copy `readout.py`.

## 4. Divergences

### D1 — fixture fidelity: the two namespaced attributes bind to the *prefix* string, not the namespace URI (advisory; fixture is frozen, prose repair only)

The bytes: `xxd -s 272` shows attribute 1 ns = `0000 0000` and attribute 2 ns = `0000 0000`, i.e. `ns_index = 0` = string `android`; the declared namespace is `prefix_index 0 / uri_index 1`. A real aapt2-produced manifest on this host (`~/.local/share/apktool/framework/1.apk:AndroidManifest.xml`, 395168 bytes) does the opposite:

```
$ (manual UTF-16 pool decode + namespace chunk walk, labelled manual)
REAL pool: count=2043 flags=0x0 utf8=False
  [85] = 'android'
  [2027] = 'http://schemas.android.com/apk/res/android'
REAL START_NAMESPACE @194780 line=20 prefix_index=85('android') uri_index=2027('http://…/android')
REAL attribute ns_idx = 2027  (every namespaced attribute; e.g. @194804 attr0 ns_idx=2027)
$ androguard AXMLPrinter(framework manifest)
Start of Namespace mapping: prefix 85: 'android' --> uri 2027: 'http://schemas.android.com/apk/res/android'
```

Both third-party decoders therefore have to *invent* a prefix for the fixture's attributes — this is the observable consequence, and it is not something either tool does on real output:

```
$ apktool d -f -o out2 fixture.apk   (exit 1, manifest written)
<manifest package="com.example.r65" n0:versionCode="1" n0:versionName="1.0"
  xmlns:android="http://schemas.android.com/apk/res/android" xmlns:n0="android" />
$ androguard 4.1.4 AXMLPrinter(fixture)
<manifest xmlns:android="http://schemas.android.com/apk/res/android" xmlns:ns0="android"
          package="com.example.r65" ns0:versionCode="1" ns0:versionName="1.0"/>
```

Scope of the finding: it is **not** a readout error. `readout.py:211` prints the raw `ns_index` and the string at that index, and entry item 8 states the method exactly ("indexing the string pool directly with the attribute's own `ns_index` … does not consult [the start-namespace chunk] when resolving attribute namespaces") — so the printed `"ns": "android"` is true of the bytes. What the entry does not record is that the fixture's `ns_index` resolves to the *prefix* string rather than the declared URI, i.e. that this AXML is not aapt2-conforming and that both independent decoders synthesize a namespace for it. Advisory repair (prose, no fixture change): one sentence in item 8 or in the limits section naming `ns_index 0 → strings[0] = "android"` (the prefix), with the apktool/androguard observation. Without it a wave-2 reader can read `"ns": "android"` as a namespace binding the bytes do not establish. **No kill-rule input** (wave 1 is advisory; the fixture is frozen and item 8's sentence is true as written).

### D2 — `data_type_string` carries the string-pool index, not a string (advisory, naming)

`readout.py:215` emits key `data_type_string` with the raw `data` word when `data_type == 0x03`, so the fixture prints `"data_type_string": 4` (index of `com.example.r65`) and `"data_type_string": 8`. The resolved text appears separately as `raw_value`. Nothing false is printed (the key is `data_type_string`, the value is an int), but the key reads as "the string", and entry item 8's paragraph does not disambiguate it. Advisory: one clause, or a rename of the key, when the entry is repaired for other reasons. Not a numeric divergence.

## 5. Tools that refuse the fixture (findings about inertness, not about the readout)

- **jadx 1.5.6 — exit 2**: `ERROR - Failed to read zip entry: fixture.apk:classes.dex` / `ERROR - Load failed! No classes for decompile!`. The 112-byte `classes.dex` is a declared header only (`androguard`: "no map list! This DEX file is probably empty"), which is exactly what item 9 says it analyses; jadx needs a program body. Consistent with the entry's scope sentence ("not dex validity or execution").
- **apktool 3.0.3 — exit 1**: decodes `AndroidManifest.xml` first (log line 3, `Decoding AndroidManifest.xml with only framework resources…`), then `brut.androlib.exceptions.AndrolibException: Could not find file: classes.dex` from the baksmali step. Two runs produced byte-identical manifests (`4c2e924dba638c8faea5e48413812da6c49f936eded74026a7ed61222619bc87`), so the manifest decode is deterministic.
- **aapt2 / aapt / apkanalyzer**: not installed (`command -v` → MISSING); `binwalk` sees only "ZIP archive, file count: 3, total size: 947 bytes" and does not descend into AXML.
- No tool refused the **manifest**; every AXML reader that ran produced the same element, the same three attribute names and the same three values as `readout.py`.

## 6. What this does not establish

- It does not establish that `truth.json` is independent of `readout.py` in authorship (both are S041 own-work); it establishes that every printed value is reproducible from the bytes by foreign code, so the readout is not merely agreeing with its own oracle.
- It does not test dex program validity, APK signature/install, or any parser's general behaviour — outside item 3/9's scope and outside this seat.
- D1 is a statement about AXML *convention* (real aapt2 output vs this fixture), not about any spec line; it is labelled as such and rests on the framework manifest comparison above.

## 7. Housekeeping

- Tools installed this seat: **androguard 4.1.4**, channel `uv tool install androguard` (no pacman; host transactions paused), reason: an AXML/DEX parser independent of `readout.py` — exercised as recorded in §2.
- Scratch `/tmp/revenger-r70-IndependentRead` (git-archive extraction, apktool/jadx/androguard outputs, manual walkers) deleted before return.
- No lane file was written, edited, staged or committed; the only lane write is this report.
