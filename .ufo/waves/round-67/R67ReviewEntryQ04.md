Q04 PASS — every scored output is attributed to the author's own hash-pinned stdlib script `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`, verified), the analysis is explicitly labeled manual, and no external tool is credited with a result it did not output.

# Criterion (QUALITY.md:16)

Q04: a tool claim names tool, version and function and scores the tool's own explicit output; manual analysis is labeled manual. Reject when a tool is credited with a result it did not output, or one version/function is generalized to the product (M02).

# Evidence

1. Manual analysis is labeled manual. Entry:12 — "The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` … Nothing is extracted to disk, nothing is executed, no producer is called, no network is used." Verified against the script: imports are `hashlib json struct sys zlib pathlib` only (`readout.py:13-18`), no `subprocess`/`os`/network/`zipfile`/`open(` writes; the only input is `APK.read_bytes()` (`readout.py:21,44`). `sha256sum` of committed bytes = `92e347c3…13976`, matching the pin at entry:166 and S041 at entry:4.

2. No external tool is credited. `inspect_android_package` (the only named tool) appears only as documentation scope: entry:2 (S043 doc quote), entry:7 ("Not covered: … provider (`inspect_android_package`) readiness or output"), entry:138 ("this lane ran no provider"). No provider output is scored anywhere. `aapt`/`apktool`/`jadx`/`dexdump`/`zipinfo`/`unzip`/`androguard` do not appear as producers.

3. Every embedded output line is the script's own stdout, verbatim. Re-ran `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root: exit 0, 15 lines, stdout SHA-256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the digest claimed at entry:6 and entry:166. Programmatic check: all 20 embedded `{"fact":…}` lines in the entry (items 1-10 blocks + Reproduce block) match the fresh stdout byte-for-byte ("NONE" missing). The repaired `member[META-INF/MANIFEST.MF]` line at entry:42 carries the script's actual `payload_first16_hex` `4d616e69666573742d56657273696f6e` (16 bytes), confirming the M39 drift repair.

4. Intra-entry pointers to script internals are accurate — the script actually emits what the entry credits it with:
   - `flags & 0x100` UTF-8 test → `readout.py:166` (`utf8=bool(flags & 0x100)`), cited at entry:67. ✓
   - attrExt-relative attribute offset `base + 16 + attribute_start + i*attribute_size` → `readout.py:199-203`, cited at entry:81 as "readout.py:200-203". ✓
   - `payload_offset = lh_off + 30 + lh_name_len + lh_extra_len` → `readout.py:99-105`, cited at entry:34 as "readout.py:99-105". ✓
   - `0xffffffff` treated as null → `NO_INDEX` at `readout.py:22`, used at :211/:213/:219, cited at entry:88 as "readout.py:22". ✓
   - Struct widths "computed by summing" → literal field-width lists summed at `readout.py:52-60,64`; the emitted `bytes_per_field`/`total_bytes` is the script's own output. ✓
   - Dex checksum/signature recomputation → `zlib.adler32`/`hashlib.sha1` inside the script (`readout.py:241-245`), so "the Adler-32/SHA-1 recomputed" (entry:106) attributes the math to the manual readout, not to an external verifier. ✓

5. No generalization of a tool's function. The interpreter is named only as `python3 -B`; the scored artifact is identified by pinned sha256 rather than version string — appropriate since Q04's reject clause targets crediting a tool with output it did not produce or generalizing one version/function to a product. Neither occurs; entry:134 explicitly fences generalization ("would need its own evidence").

# OFF-criterion defects (for the named Q01/Q02 seats)

- OFF entry:1 and entry:56 — the S038 anchor cites `RES_XML_START_NAMESPACE_TYPE` at snapshot line :244, but in the committed snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` line 244 is `RES_XML_FIRST_CHUNK_TYPE`; `RES_XML_START_NAMESPACE_TYPE` is at **line 245**. Span 237-253, `RES_XML_RESOURCE_MAP_TYPE` :253, END_NAMESPACE :246, START_ELEMENT :247, END_ELEMENT :248 all verified correct; only this one name→line pointer is off by one (the cited value 0x0100 is coincidentally identical). Anchor-precision defect, not a Q04 tool-credit failure.
- OFF — none other found in a spot sweep: truth.json sha256 `27303bae…f8173` matches entry:4; S043 snapshot sha256 `412d9cb4…74c` and dex-format.html sha256 `c0428612…d9f4` match entry:2/entry:3/claims.md; `struct ResXMLTree_attrExt` at snapshot :677 and the attributeStart comment at :685-687 match entry:81's provenance; S043 snapshot lines 7-8 carry the quoted route-scope sentence.

# Tools installed

None. Pacman paused per guard; no installs needed.

Report: .ufo/waves/round-67/R67ReviewEntryQ04.md
