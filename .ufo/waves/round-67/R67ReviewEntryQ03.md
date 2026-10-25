Q03 PASS — every expected value class in `corpus/knowledge/round-67-apk-axml-byte-evidence.md` derives from a pin fixed outside the record under test (the authored oracle `truth.json` sha256-pinned separately, spec text S032/S034/S038/S045 snapshots), or is recomputed from the bytes by a spec-named algorithm; no expected value is copied from `fixture.apk` itself, and no saved path serves as both identity and locator (paths are locators; sha256 digests are identity — all pins verified byte-for-byte below).

# Scope

Criterion Q03 (corpus/QUALITY.md: "Expected values are derived independently: from bytes, a specification, or a pin fixed outside the record under test"; reject when "the expected value is copied from the record being checked, or a saved path is used as both identity and locator"). Record under test: `corpus/fixtures/apk-r65/fixture.apk` and its declared-header/container values, as analyzed by `corpus/fixtures/apk-r65/readout.py`. Fresh-seat decision on the landed v2 bytes; I am not the author.

# Evidence — each expected-value class maps to an external pin

## 1. Identity pins verified on committed bytes (no path-as-identity)

```
$ sha256sum corpus/fixtures/apk-r65/{fixture.apk,truth.json,readout.py,generator.py}
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk   (entry pins 05d2280f… — match)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json    (entry pins 27303bae… — match)
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py    (entry pins 92e347c3… — match)
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a19…           generator.py  (S041 row pins eaa9444c… — match)
```
`fixture.apk` is 947 bytes (`ls -la`), matching item 1. The M14 failure shape (path doubling as identity) is absent: every `corpus/fixtures/…` string in the entry is a locator paired with a digest identity.

## 2. Readout reproduces — observed side is derived from bytes, not restated

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r67q03-readout.out; echo "exit=$?"; wc -l …; sha256sum …
exit=0
15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247   (entry's pinned stdout digest — match)
```
The observed side of every comparison is recomputed at run time; `readout.py` contains no copy of `truth.json` (`grep -n 'truth' readout.py` → no hits) and no hardcoded expected table — its `==` sites are spec constants and cross-field checks (readout.py:85 `cd_off + cd_size == eocd`, :116 stated CRC vs `zlib.crc32(payload)` recomputation, :242 declared adler32 vs `zlib.adler32(dex[12:])`, :245 declared signature vs `hashlib.sha1` recomputation).

## 3. The authored oracle is a separate pinned record, not the record under test

`truth.json:69-73` declares `image.sha256`/`size` matching item 1; `:74-102` declares the three members' `local_header_offset`, `compressed_size`, `uncompressed_size`, `crc32`, `sha256` matching item 3 (0/465/618, 416/112/69, `962d075f`/`2635c82a`/`e948d738`); `:26-36` declares `resource_ids` with `0x0101021b`/`0x0101021c` at indices 5-6 matching item 7's nonzero map; `:4-24` declares `name_idx`/`raw_value_idx`/`data_type`/`ns_idx` matching item 8's three attribute rows. The comparison direction is readout(bytes) → oracle(pinned record); the expected side never reads the APK. truth.json's own identity is fixed by digest `27303bae…` outside fixture.apk. [INFERENCE: oracle and fixture share a generator (truth.json:49-67 `build_recipe`), so the oracle is an authored expectation written ahead of the artifact — the lane's declared own-work design (S041 scope "byte/oracle correspondence"), which is exactly the "pin fixed outside the record under test" shape, not an expectation harvested from the record.]

## 4. Spec-derived expectations resolve to committed snapshot text

- S038 enum anchor :237-253 verified — `sed -n '237,253p' .ufo/waves/round-65/source-snapshots/ResourceTypes.h` prints the `enum` block ending `RES_XML_RESOURCE_MAP_TYPE = 0x0180` at :253; `struct ResChunk_header` at :218; `struct ResXMLTree_attrExt` at :677 with `attributeStart` and its "Byte offset from the start of this structure" comment in the :685-687 span. Item 5's struct widths and item 8's attrExt-relative attribute location are spec-derived expectations, not byte-copied.
- S045 snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (match; 281157 bytes). `grep -o 'adler32 checksum[^<]*'` → "adler32 checksum of the rest of the file (everything but"; `grep -o 'SHA-1 signature[^<]*'` → "SHA-1 signature (hash) of the rest of the file (everything but" (the full quoted strings are HTML-tag-broken but verbatim); `must be 0x70` and `ENDIAN_CONSTANT = 0x12345678` present verbatim. Item 9's expected semantics (checksum/signature coverage, header_size 112, endian tag) come from this spec text.
- S032/S034 APPNOTE rows exist in SOURCES.md (:46,:48, tier A) for the 46/30-byte container record widths behind items 2-3.

## 5. Internal-consistency fields are spec-algorithm recomputations, not copies

`crc32_matches`, `checksum_matches`, `signature_matches`, `cd_end_equals_eocd_offset`, `xml_total_size_equals_member` each compare a record field against an independent recomputation over different bytes of the same record — both sides derived from bytes via distinct paths. No field is "expected = stated" tautology.

# Fail-branch check

Neither Q03 reject condition is met: (a) no expected value is copied from the record being checked — the expectation side is always oracle/spec/recompute; (b) no saved path is used as both identity and locator — digest pins carry identity everywhere a path appears.

# OFF-criterion findings

- OFF-none: none observed in scope-relevant read. (Long lines 1,3,81,85,106 display-truncated in tooling only — raw tails verified complete, e.g. line 1 ends "86255 bytes"; the only literal `…` in the file, line 45, is an intentional elision quoting the r65 defect.)

# Residual risk / verification gaps

- Q03 attests independence of the expectation source, not fidelity of the author's transcription: whether `readout.py`'s `bytes_per_field` lists correctly transcribe S038's struct fields (28/20/20/16/8 widths) is a spec-fidelity question for Q01/Q11 seats, not a Q03 circularity.
- truth.json's correctness relative to generator.py output is round-65 evidence (S041) not re-run by this entry — the entry states this; a wrong-but-consistent oracle would pass Q03 while failing elsewhere.
- Verification basis: `readout.py` executed read-only (exit 0, 15 lines, stdout sha256 match); `truth.json` read fully; S038/S045 snapshots grepped at cited anchors; SOURCES.md rows S032/S034/S038/S041/S043/S045 confirmed present. No sub-check was skipped for time.
