Q06 PASS — every fixture premise in `corpus/knowledge/round-68-apk-axml-byte-evidence.md` is printed from the built fixture by the entry's own command, reproduced byte-identically on re-run today, and independently re-derived by this seat from the APK bytes (103 fields / 14 facts, 0 value mismatches); no producer is called; the rejected r65/r67 candidates are retained byte-preserved.

Seat: `L1Revenger68.R68ReviewEntryQ06` (round 68, revenger-shokunin). Criterion: **Q06 only** — "Fixture premises are byte-verified against the built fixture after every edit and before any producer call; failed inputs are retained" (`corpus/QUALITY.md:20`), reject when "an offset, operand, size or count is stated from intent rather than from the built bytes" (lesson M04/M05). Read-only: nothing written outside this report. No tool installs or upgrades were performed (none needed).

Target bytes: `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`, 33442 bytes (`admission-status: candidate`, line 8).

## 1. The entry's own command, re-run (premise source)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/fixtures/apk-r65/readout.py
exit=0
15            # stdout line count
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/q06_readout.txt
stderr: (empty)
```

Both numbers the entry pins in `recheck:` (line 7) and §Reproduce (`:194`) reproduce exactly: exit 0, 15 stdout lines, stdout SHA-256 `507d79f8…` — the value the entry states. `--fact` form also works as claimed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
exit=0
```

`$ python3 -B corpus/derive_axml_anchors.py` → `derive_exit=0`, 17 stdout lines, including `enum RES_XML_START_NAMESPACE_TYPE : 245`, `comment attributeStart : 686`, `field attributeStart : 687`, `sha256 56b88bc4…f56f ResourceTypes.h` — matches item 11 (`:131-148`) line for line, and the corrected S038 anchor at `:245` in both places (line 1, line 57).

## 2. Byte comparison: entry text vs actual stdout

Extracted every line of the entry starting with `{"` (30 occurrences: 15 per-item blocks + the 15-line §Reproduce dump) and diffed against the real stdout:

```
embedded JSON-looking lines: 30
non-matching embedded lines: 0
actual stdout facts not embedded verbatim: 0
```

No truncated, hand-edited or invented output line is present; every one of the 15 facts appears verbatim.

## 3. Independent re-derivation of every fixture premise (not the entry's readout)

This seat wrote its own ZIP/AXML/dex parser (positional `struct` reads, its own CD walk from `cd_off`, its own attrExt offset taken from the *observed* chunk `headerSize`, not the readout's constants) and diffed it field-by-field against each embedded fact:

```
facts compared: 14 fields compared: 103
DIFFS: 1
('axml_resource_map', 'nonzero', {'versionCode': '0x0101021b', 'versionName': '0x0101021c'},
                                  {'versionCode': '0x101021b',  'versionName': '0x101021c'})
```

The single "diff" is not a value error: `readout.py:146` formats `f"0x{ids[i]: 08x}".replace(" ","")`, which drops the leading zero (`0x101021b`); the prose at `:70` states the id as `0x0101021b`. Same integer. Independent facts (all equal to the entry's embedded values):

```
size 947 sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
eocd_offset 925 comment_len 0 eocd_end 947 eof 947
n_tot 3 cd_sz 188 cd_off 737 cd_off+cd_sz 925   cd_walk_end 925 cd_end_equals_eocd True
AndroidManifest.xml lho=0   payload_off=49  csz=416 usz=416 crc=962d075f sha=73d1e0f2… first16=03000800a001000001001c00c4000000
classes.dex         lho=465 payload_off=506 csz=112 usz=112 crc=2635c82a sha=57cfe887… first16=6465780a30333500300c123da5fc7bea
META-INF/MANIFEST.MF lho=618 payload_off=668 csz=69 usz=69 crc=e948d738 sha=2e5da249… first16=4d616e69666573742d56657273696f6e
chunks [(8,1,28,196),(204,384,8,44),(248,256,16,24),(272,258,16,96),(368,259,16,24),(392,257,16,24)] walk_end 416 ==total True
pool cnt=9 styleCount=0 flags=0x00000100 utf8=True stringsStart=64 stylesStart=0 offsets=[0,10,55,66,76,94,108,122,126]
resource_map offset=204 entry_count=9 ids=[0×5 zeros,0x0101021b,0x0101021c,0,0]
start_ns offset=248 prefix_index=0 prefix='android' uri_index=1
start_element offset=272 node_hs=16 attrExt_at=288 attributeStart=20 attributeSize=20 attributeCount=3 idIndex=0 classIndex=0 styleIndex=0
  attr0 off=308 ns=0xffffffff name='package'     raw='com.example.r65' value_size=8 data_type=0x03 data=4 res_id=0
  attr1 off=328 ns='android'  name='versionCode' raw='1'             value_size=8 data_type=0x10 data=1 res_id=16843291
  attr2 off=348 ns='android'  name='versionName' raw='1.0'           value_size=8 data_type=0x03 data=8 res_id=16843292
  attr_span_end 368 == chunk_end 368
end_element offset=368 name='manifest'
dex magic=6465780a30333500 declared_checksum=0x3d120c30 adler=0x3d120c30 sig==sha1=a5fc7bea8fa9ffaa52243540c8026066511b9fce file_size=112 header_size=112 endian=0x12345678 len=112
jar bytes=69 first_line='Manifest-Version: 1.0' section_count=1 first16_hex=4d616e69666573742d56657273696f6e first16_ascii=b'Manifest-Version'
```

Cross-checks that close the byte-arithmetic the entry asserts: `payload_offset = lho + 30 + name_len + extra_len` holds on the built bytes for all three members (0+30+15+4=49; 465+30+11+0=506; 618+30+20+0=668); the chunk walk (`8+196=204`, `204+44=248`, `248+24=272`, `272+96=368`, `368+24=392`, `392+24=416`) closes exactly on the member length; and the observed `headerSize`/`attributeStart`/`attributeSize`/`value_size` values (28/8/16/16/16/16, 20, 20, 8) match the struct widths the readout hardcodes — I re-read the snapshot declarations myself (`ResourceTypes.h:218` ResChunk_header, `:287` Res_value, `:461` ResStringPool_header, `:621` ResXMLTree_node, `:677` ResXMLTree_attrExt, `:707` ResXMLTree_attribute) and the summed widths 8/8/28/16/20/20 are correct.

## 4. "Before any producer call" — the premise source is producer-free

`readout.py` imports only stdlib (`hashlib`, `json`, `struct`, `sys`, `zlib`, `pathlib`; `readout.py:13-18`), reads exactly one path (`APK = ROOT / "fixture.apk"`, `readout.py:21`; `apk = APK.read_bytes()`, `:44`), and emits no `method`/`flags`/subprocess/network call. No provider (`inspect_android_package`) is invoked anywhere in the entry's evidence path; the entry states this at `:17` ("no producer is called") and §Observation `:24`.

## 5. "After every edit" — fixture identity is real, and the re-verification is post-edit

```
$ git log --oneline --follow -- corpus/fixtures/apk-r65/fixture.apk
c7b7cf9 round-65: candidates — apk-r65 fixture+readout, C05 candidate entry, … (no README flip)

$ git show c7b7cf98:corpus/fixtures/apk-r65/fixture.apk | sha256sum
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  -
$ git show c7b7cf98:corpus/fixtures/apk-r65/truth.json  | sha256sum
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  -
$ git show c7b7cf98:corpus/fixtures/apk-r65/readout.py | sha256sum
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  -
$ git status --porcelain -- corpus/fixtures/apk-r65/ corpus/knowledge/round-65-apk-axml-byte-evidence.md corpus/knowledge/round-67-apk-axml-byte-evidence.md
(empty)
```

The fixture, oracle and readout bytes are byte-identical to the round-65 claim tree — the entry's `verified-at:` lineage claim (`:6`) is true, and the r68 edits (this entry) were followed by the verification the entry embeds (today's byte-identical stdout). The fixture's own build path measures the finished archive rather than asserting intent: `generator.py:175` `parse_members()` reads offsets/sizes/CRC from the completed zip, and `generator.py:196/204` writes those measurements into `truth.json`.

## 6. "Failed inputs are retained"

This entry's own inputs produced no failure (readout exit 0; every `assert` inside it passed, including CD/local-header signatures, local/CD name equality, `cursor == eocd`, root `RES_XML_TYPE`, string-length equality, non-zero chunk size). The retention requirement is met materially by the retained *failed candidates*:

```
corpus/knowledge/round-65-apk-axml-byte-evidence.md   21166 bytes  (amended only by a4c712a, round-66 header repairs)
corpus/knowledge/round-67-apk-axml-byte-evidence.md   30583 bytes  worktree sha == HEAD sha 057a1826…
r67 :244 drift still present and untouched at the red-before surface:
  round-67-…:1  … `RES_XML_START_NAMESPACE_TYPE` :244 …
  round-67-…:56 … start/end namespace :244/:246 …
```

and by the declared retention posture at entry line 8 ("on a fail the row stays `uncovered` and this file is marked `rejected`"). This matches `reports/round-68/claims.md` §Void conditions ("prior rejected candidates altered … they are the red-before surface"): the prior candidates are unaltered in this revision.

## 7. Findings

**P3 — Q06-scope gap (named, not a reject; the premise is true on the bytes but carries no in-entry derivation).** Entry `:162`: "The container is ZIP_STORED with no data descriptors, so the byte walk does not exercise split archives, spanned records or compression." `readout.py` never emits the compression method or the general-purpose flag word (verified: `grep -n "method\|flags" corpus/fixtures/apk-r65/readout.py` → only `:166` `flags & 0x100`, which is the *string-pool* flags), so this container operand is stated from the generator's intent (`generator.py:167` `ZIP_STORED`, `:171` `info.compress_type = ZIP_STORED`) rather than from a printed fixture field. It *is* true on the built bytes — I measured, for all three members, CD `method=0`, CD `flags=0x0000`, local-header `flags=0x0000`, bit 3 (data descriptor) clear, `compressed_size == uncompressed_size` — and `truth.json` `members[].method` is `0`. Remediation: emit `method` and the general-purpose `flags` in the member facts (or cite `truth.json members[].method` and print the `flags` word), so the limitation rests on the built bytes.

**P2 — adjacent, Q11 scope (`:148`, `:157`, `:1`, `:57`).** "The chunk-type enum block spans lines 237-253" is wrong as a block bound: the enum opens at `ResourceTypes.h:237` (`enum {`) and closes at **`:263`** (`};`); `:253` is `RES_XML_RESOURCE_MAP_TYPE`, one member inside it. Correct statement: the cited chunk-type members occupy 239-253 and the enclosing enum closes at 263. The derive command prints neither 237 nor 263, so the span bound is un-derived. Related: item 11 also asserts "line 244 is `RES_XML_FIRST_CHUNK_TYPE`" (`:148`) — true (`ResourceTypes.h:244`), but `derive_axml_anchors.py` does not search that symbol (its 16 symbol lines omit `RES_XML_FIRST_CHUNK_TYPE`), so the sentence that characterises the repaired off-by-one is not carried by the embedded capture.

**P2 — adjacent, Q03 scope (`:152`, `:174`).** The §Comparison agreement for the container metadata is self-comparison: `truth.json members[]` is produced by `generator.py:175-196` `parse_members()` from the same finished archive (`generator.py:204` `"members": measured`), so "the three members' local-header offsets, payload sizes and CRC-32 values" cannot serve as independent ground truth for those fields. Independent declared expectation exists only for the AXML tables (`STRINGS` `:37`, `ATTRIBUTES` `:53`, `RESOURCE_IDS` `:61`, written as `axml_declared` at `:205`), which do give a genuine external check for items 6-8. `:152` does say "their measured offsets", a partial disclosure, but the Q03 row's "fixed outside the record under test" (`:174`) overstates independence for the container fields. Reported, not absorbed; the Q03 seat owns the verdict.

**P4 — nit (`:194`).** "exit 0, 17 lines, one per cited symbol": the command does print 17 lines, but line 1 is the `sha256 …ResourceTypes.h` header and only 16 are symbol lines. The count 17 is right; the gloss "one per cited symbol" is off by one.

**P4 — observation, working-tree hygiene (not this entry's bytes, not mine).** The lane worktree now carries an untracked `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` (9356 bytes, mtime `2026-10-25 03:29:00`), i.e. `corpus/check_embedded_outputs.py` was executed without `-B` by some other seat during the wave. This seat never ran that gate and did not create or remove the file. It cannot reach the frozen counter (which measures `git archive <commit> corpus`), but it is untracked pollution under `corpus/` in a round whose void conditions are written around corpus byte discipline, and it should not be swept into a commit at the measured tip. `git status --porcelain -- corpus/` otherwise empty; `git diff --stat -- corpus/` empty.

**Not a defect (checked, correct as written).** Entry `:46` — the printed field `4d616e69666573742d56657273696f6e` is 16 bytes = ASCII `Manifest-Version`, and the entry's "the 16-byte prefix of `Manifest-Version: 1.0`" is exactly right; the appositive "ASCII `Manifest-`" names the first 9 bytes of the same value. The round-65 drift it contrasts against (`4d616e696673742d…`, decodes to `Manifist-`) is genuinely the M39 class, and the value quoted for it is 9 bytes though the prose calls it a "15-byte pair" — a wording slip in a comparison to a superseded candidate, not a premise about the built bytes.

## 8. Robustness against the criterion's own adversarial shapes

- *Offset/size/count stated from intent:* none found. Every one of the 103 fixture-derived fields the entry prints equals my parser's independent value; the payload-offset formula and the chunk walk re-close arithmetically on the bytes.
- *Stale verification after an edit:* none. Fixture bytes unchanged since `c7b7cf9` (blob hashes above), and the verification reproduces today, so the captured outputs are of these bytes, not of an earlier build.
- *Producer contamination:* none. Stdlib-only reader, one input file, no network, no provider.
- *Retention:* prior failed inputs preserved and readable, with the actual falsifying anchors (`:244`) still in place.

## 9. Residual risk / verification gaps

- I did not re-run `generator.py` (the entry says it is round-65 evidence and not re-run, `:152`); my check is that the committed bytes are the built bytes and every premise matches them. Reproducibility of the *build* is therefore outside this seat's evidence.
- I verified the readout is producer-free by reading its imports and file reads, not by syscall tracing.
- Q06 admits one premise (ZIP_STORED / no data descriptors, P3) whose byte grounding is not in the entry's own output. It is true on the bytes and no measured value depends on it, which is why this is a PASS with a required repair rather than a FAIL; if the wave's bar is that *every* stated fixture operand be printed, add the `method`/`flags` fields and this gap closes.
- Adjacent P2 items (enum span 237-263, un-derived `RES_XML_FIRST_CHUNK_TYPE`, circular container oracle) belong to Q11/Q03 seats; they are reported with exact pointers and not scored here.
