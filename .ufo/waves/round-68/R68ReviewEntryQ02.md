PASS — Q02 PASS on `corpus/knowledge/round-68-apk-axml-byte-evidence.md` as committed: the entry opens with five `source:` rows (S038/S043/S045/S046/S041), carries `verified-at:` (2026-10-24) and `recheck:` (two runnable commands), names coverage row C05, and every anchor value it states re-derives to the cited line/value in the cited document — with one non-blocking range-wording defect recorded in §Defect (no stated line number is wrong).

criterion: Q02 only (QUALITY.md:14 — `source:` + `verified-at:` + `recheck:` + coverage-map row; "every anchor it states is the right line of the cited document").
seat: L1Revenger68.R68ReviewEntryQ02 · witness: L1Revenger68.R68ReviewEntryQ02 · author: not this seat (fresh, non-author) · date 2026-10-25
target bytes: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md` (216 lines, `admission-status: candidate`)
read-only seat: no file edited; this report is the only write.

## 1. Header presence and precedence (Q02 clause 1)

Entry lines 1-9, verbatim head (from `python3` numbered read of the first 10 lines):

```
1 source: S038 — AOSP `ResourceTypes.h` … https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h …
2 source: S043 — supersedes S039 — REA reverse-engineer-anything skill reference, "Android application artifacts" … anchor: snapshot `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` **lines 7-8** …
3 source: S045 — Android DEX format specification … https://source.android.com/docs/core/runtime/dex-format … snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256 `c0428612…9d9f4`, 281157 bytes
4 source: S046 — AXML anchor derivation (own-work, tier A; row opened round 68 …) — anchor: `corpus/derive_axml_anchors.py` sha256 `bce497d6…f1e249`, 17 output lines over `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4…8957c56f`
5 source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `truth.json`, `generator.py`, `readout.py` … fixture sha256 `05d2280f…afe7d03e` (947 bytes) …
6 verified-at: 2026-10-24 (round-68 re-derivation; … unchanged since `c7b7cf98`; …)
7 recheck: `python3 -B corpus/derive_axml_anchors.py` from the lane root … and `python3 -B corpus/fixtures/apk-r65/readout.py` … exits 0 and prints 15 stdout lines whose SHA-256 is `507d79f8…6dad247` …
8 coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture …
9 admission-status: candidate — … It is NOT admitted: the README C05 row stays `uncovered` …
```

- `source:` is the FIRST line, not merely present: all five `S###` rows precede `verified-at:`/`recheck:`/`coverage-map:`. PASS.
- Every `source:` row carries an identifier that resolves: S038/S045 are URLs; S043/S046/S041 are repo paths (snapshot + script + fixture members). No anchor is a bare homepage. PASS.
- `verified-at:` carries an exact date (`2026-10-24`). PASS.
- `recheck:` carries runnable commands, not a citation alone. PASS.

`S046` row exists in the registry and its recorded digests agree with the entry:

```
$ grep -n 'S046' corpus/SOURCES.md
61:| S046 | AXML anchor derivation — `corpus/derive_axml_anchors.py` over `corpus/snapshots/ResourceTypes.h` | own-work | A | … script sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`, 17 output lines; snapshot copy sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (86255 bytes …) …
```

## 2. Coverage-map row named and still unflipped (Q02 clause 2)

Entry:8 names `coverage-map: C05 (`corpus/README.md`, Android packages (APK))`. The named row exists with that exact label:

```
$ python3 (numbered read of corpus/README.md)
34 | | C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` … | uncovered |
coverage rows: 14
```

The row's status is `uncovered`, which is consistent with entry:9 `admission-status: candidate` and with the frozen C2 admission order (no flip at build time). PASS.

## 3. Every stated anchor re-derived against the cited document (Q02 clause 3)

### 3a. S038 `ResourceTypes.h` — 16 symbol anchors, byte-checked line by line

Entry:1 states: `struct ResChunk_header` 218; enum block 237-253 with `RES_STRING_POOL_TYPE` :239, `RES_XML_TYPE` :241, `RES_XML_START_NAMESPACE_TYPE` **:245**, `RES_XML_END_NAMESPACE_TYPE` :246, `RES_XML_START_ELEMENT_TYPE` :247, `RES_XML_END_ELEMENT_TYPE` :248, `RES_XML_RESOURCE_MAP_TYPE` :253; `struct ResStringPool_header` 461; `struct ResXMLTree_header` 612; `struct ResXMLTree_node` 621; `struct ResXMLTree_attrExt` 677 with comment at 686 and field at 687; `struct ResXMLTree_attribute` 707; `struct Res_value` 287.

Independent check (numbered print of the snapshot, not the entry's script):

```
$ python3 - <<'EOF'   # prints L[n-1] of corpus/snapshots/ResourceTypes.h
218 | struct ResChunk_header
239 |     RES_STRING_POOL_TYPE              = 0x0001,
241 |     RES_XML_TYPE                      = 0x0003,
244 |     RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245 |     RES_XML_START_NAMESPACE_TYPE      = 0x0100,
246 |     RES_XML_END_NAMESPACE_TYPE        = 0x0101,
247 |     RES_XML_START_ELEMENT_TYPE        = 0x0102,
248 |     RES_XML_END_ELEMENT_TYPE          = 0x0103,
253 |     RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
287 | struct Res_value
461 | struct ResStringPool_header
612 | struct ResXMLTree_header
621 | struct ResXMLTree_node
677 | struct ResXMLTree_attrExt
686 |     // Byte offset from the start of this structure where the attributes start.
687 |     uint16_t attributeStart;
707 | struct ResXMLTree_attribute
```

16/16 anchors exact, including the load-bearing repair: `:245` is `RES_XML_START_NAMESPACE_TYPE` and `:244` is `RES_XML_FIRST_CHUNK_TYPE`, exactly as entry:148 asserts after the derivation block. The 686/687 pair matches entry:82 verbatim (comment text and `uint16_t attributeStart;`).

Entry's own derivation command reproduces its embedded block (item 11) exactly:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py; echo "EXIT=$?"
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
EXIT=0
```

17 lines, exit 0: matches entry:4 ("17 output lines") and item 11 byte for byte (every printed line equals the embedded line; verified by set comparison of the 17 outputs against the entry's code block).

Snapshot pin agrees in both places the entry names:

```
$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
$ stat -c '%s %n' corpus/snapshots/ResourceTypes.h
86255 corpus/snapshots/ResourceTypes.h
```

Entry:1 states 86255 bytes and that digest for the pinned snapshot, and the same digest for the committed copy; both hold. PASS.

### 3b. S043 `rea-android-applications.md` — "lines 7-8" and the "line 5" claim

```
$ python3 (numbered print of .ufo/waves/round-65/source-snapshots/rea-android-applications.md)
  1|# Android application artifacts
  2|
  3|Use the connected server's advertised Android tools. Repository main and npm
  4|4.1.0 include this family. A skill installation alone cannot add it to an
  5|older server.
  6|
  7|Start with `inspect_android_package` on the caller's APK path for package
  8|identity, manifest declarations, coverage, and inline Evidence. Use
```

Entry:2 quotes exactly the text at lines 7-8 and says the round-65 draft's "line 5" is `older server.` — both true (line 7 = "Start with `inspect_android_package` on the caller's APK path for package", line 8 = "identity, manifest declarations, coverage, and inline Evidence."). The snapshot digest the entry states also holds:

```
$ sha256sum .ufo/waves/round-65/source-snapshots/rea-android-applications.md
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  .ufo/waves/round-65/source-snapshots/rea-android-applications.md
```

PASS.

### 3c. S045 `dex-format.html` — four quoted clauses

Entry:3 quotes the `header_item` table clauses. Raw HTML splits them across tags, so an exact-substring search over the raw file reports MISSING; over tag-stripped, entity-decoded text every clause is present verbatim:

```
$ python3 (strip tags, unescape, collapse whitespace)
'adler32 checksum': hits=1
   … checksum uint adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption …
'SHA-1 signature': hits=1
   … signature ubyte[20] SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field); used to uniquely identify files …
'0x70': hits=2
   … must be 0x70 (112) bytes (v40 or earlier) must be 0x78 (120) bytes (v41 or later) endian_tag uint = ENDIAN_CONSTANT …
ENDIAN_CONSTANT literal:
   … uint ENDIAN_CONSTANT = 0x12345678; uint REVERSE_ENDIAN_CONSTANT …
```

All four anchors named in entry:3 are the right text of the cited document, including `ENDIAN_CONSTANT = 0x12345678`. Snapshot digest holds:

```
$ sha256sum .ufo/waves/round-67/source-snapshots/dex-format.html
c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4  .ufo/waves/round-67/source-snapshots/dex-format.html
$ stat -c '%s' …                                              281157
```

PASS.

### 3d. S041 / S046 digests and the `recheck:` values

```
$ sha256sum corpus/fixtures/apk-r65/fixture.apk corpus/fixtures/apk-r65/truth.json corpus/fixtures/apk-r65/readout.py corpus/derive_axml_anchors.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py
```

All four equal the values stated at entry:4, entry:5 and in item 1. The fixture-size claim "947 bytes" holds (entry:1/5; readout `--fact archive` prints `"bytes": 947`).

The `recheck:` contract value (15 stdout lines, SHA-256 `507d79f8…6dad247`, exit 0) reproduces:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py | tee /tmp/r68_q02_out.txt | wc -l
15
$ sha256sum /tmp/r68_q02_out.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r68_q02_out.txt
EXIT=0
```

Every embedded output line in the entry is a real stdout line — no value is printed that the command does not emit:

```
$ python3 (compare entry lines starting '{"' against the 15 real stdout lines)
real stdout json lines 15 entry embedded json lines 30
(<no "NOT EXACT" lines: all 30 embedded JSON lines — the 15 per-item blocks plus the 15-line §Reproduce block — equal a real stdout line)
```

PASS for Q02: no anchor value in the header is unproduced, transcribed, or wrong.

## 4. Defect found — non-blocking for Q02, named with the exact fix

**Entry lines 1, 57, 148, 157 state the chunk-type enum block's extent as `lines 237-253`.** The enum block opens at 237 (`enum {`) but does **not** close at 253; it continues through the `RES_TABLE_*` group and closes at **263**:

```
$ python3 (snapshot line print)
236 |
237 | enum {
250 |     RES_XML_LAST_CHUNK_TYPE           = 0x017f,
251 |     // This contains a uint32_t array mapping strings in the string
252 |     // pool back to resource identifiers.  It is optional.
253 |     RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
254 |
255 |     // Chunk types in RES_TABLE_TYPE
256 |     RES_TABLE_PACKAGE_TYPE            = 0x0200,
…
enum closes at 263
```

Why this is not a Q02 FAIL, stated explicitly so adjudication can overrule if it disagrees:

1. Q02's reject triggers (QUALITY.md:14) are a missing header or a bare-homepage anchor; neither occurs.
2. The criterion's anchor test is "every anchor it states is the right line of the cited document". Every line the range 237-253 names **is** a line of that enum block (237 `enum {`; 239-253 enum members and their comments), so no stated anchor points at a line that belongs to something else. Contrast the defect this round repairs: `:244` named `RES_XML_FIRST_CHUNK_TYPE` where the entry cited `RES_XML_START_NAMESPACE_TYPE` — a line that is *not* the cited thing. That defect is gone.
3. The statement the range supports is true and is the load-bearing correction: `RES_XML_RESOURCE_MAP_TYPE` is at 253 with value `0x0180` and **is inside the enum block**, unlike the round-65 draft's `:239-250` (entry:1, entry:57).

The defect is a range *under-bound* on a correct subset: the range delimits the AXML chunk-type group, not the block's span. Item 11's word "spans" (entry:148) is the imprecise part. Smallest safe correction, no anchor value changes:

- entry:1 `chunk-type enum block **lines 237-253**` → `chunk-type enum block (opens line 237; the AXML chunk-type group is **lines 239-253**, and the block closes at line 263)`
- entry:57 and entry:157 `lines 237-253` → `lines 239-253 (AXML chunk-type group inside the enum block that opens at 237)`
- entry:148 `The chunk-type enum block spans lines 237-253` → `The AXML chunk-type group spans lines 239-253 inside the enum block that opens at 237 and closes at 263`

A second, smaller precision note (not a wrong line number, no fix required): entry:82 attributes the doc-comment sentence "Appears header.headerSize bytes after a `ResXMLTree_node`." to `struct ResXMLTree_attrExt` "(line 677)". Line 677 is the struct declaration, correctly anchored; that sentence literally sits at line 675 inside the struct's doc block 672-676. Stating it as `(struct at line 677; the sentence is at line 675)` would remove the last one-line ambiguity from the attrExt provenance.

## 5. What this seat did not decide

- Q01, Q03-Q13 are other seats' criteria; the §Q-map row for Q02 was read only as data and was not used as evidence for this verdict.
- No gate, counter, README or fixture byte was re-run for admission purposes beyond the two `recheck:` commands and the digest checks above; those belong to other seats.
- No file outside this report was written; no git/jj mutation; no message to another seat; no subagent dispatched.
- Tooling: no install or upgrade performed (nothing was needed).

Verdict: **Q02 PASS** on these bytes, with the §4 range-wording defect recorded as a precision item (fixable in three text spans, changes no anchor value).
