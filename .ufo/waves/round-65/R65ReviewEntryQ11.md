FAIL (Q11) — item 3's `member[META-INF/MANIFEST.MF]` output line in the entry is not what its stated deriving command prints (15-byte `Manifst-Version` hex vs the real 16-byte `Manifest-Version`), so the entry's promise "the output it printed" is falsified at one line; every other count/offset/identifier/digest in items 1–10 re-derives clean and item 5's constants are genuinely derived.

# Q11 review — `corpus/knowledge/round-65-apk-axml-byte-evidence.md`

Reviewed tree: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, tree clean for the entry (entry added by `c7b7cf9`, unchanged since). Entry sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`, 162 lines. Read-only seat: no production edits, no git/jj mutation, no tool installs.

## Finding 1 — HIGH, fails Q11: recorded output line does not match the deriving command

`corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` (item 3) records:

```
{"cd_index": 2, ... "payload_first16_hex": "4d616e696673742d56657273696f6e", ...}
```

The deriving command the entry names in that item prints:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, ... "payload_first16_hex": "4d616e69666573742d56657273696f6e", ...}
```

Byte-level difference (both fields parsed from the committed entry and from live stdout):

```
entry  hex_len 30 hex bytes 15 ascii b'Manifst-Version'
stdout hex_len 32 hex bytes 16 ascii b'Manifest-Version'
```

The recorded value is 15 bytes, so it does not even satisfy the field name `payload_first16_hex`; it drops byte `0x65` (`e`) after `Manif`. It also contradicts the entry's own item 10 (`entry:118`-block, `first_line: "Manifest-Version: 1.0"`). `readout.py:118` emits `payload[:16].hex()` from the committed fixture, and the fixture digest the entry claims (`05d2280f…`, item 1) matches the file on disk, so this is a transcription/paste error in the entry, not a changed fixture.

Exhaustive check: comparing every JSON output line pasted in the entry against the live 15-line stdout (`sort_keys` JSON text comparison) yields exactly one diff — this line:

```
TEXT-DIFF member[META-INF/MANIFEST.MF]
```

Fix: replace line 41 with the readout's real line (or regenerate all output blocks mechanically from `readout.py`). After that fix the entry's output blocks are verbatim — my re-run of the full stdout is 15 lines with SHA-256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, exactly the digest claimed at `entry:5` and `entry:162`.

Admission consequence: the round's gate is all-criteria Q01–Q13; a Q11 FAIL blocks C05 `frontier → held` until this line is corrected and re-reviewed. The defect is mechanical, not architectural.

## Finding 2 — LOW: EOCD signature hex has no printed output

`entry:26` states the signature `504b0506` sits at offset 925. The `eocd` fact prints `eocd_offset: 925` but no signature bytes; the literal exists only in the cited script (`readout.py:76-77`, `apk.rfind(b"PK\x05\x06")`). The derivation is reproducible from the committed script (S041), but the command output shown in the entry does not itself carry the hex. Suggest adding `eocd_signature_hex` (or accepting the script literal as the anchor).

## Finding 3 — LOW: header/S041 digests carry no deriving command inside the entry

`entry:3` lists sha256 for `truth.json`, `generator.py`, `readout.py`; the §Reproduce prose (`entry:161`) repeats the `readout.py` digest. Only the fixture digest is re-derived by a shown command (item 1). The §Q-map Q11 basis ("every count, offset, identifier and digest carries its deriving command and output in §Observation (items 1-10)") is scoped to items 1–10, so it is not self-contradictory, but the header digests are values without an in-entry `sha256sum` command+output. I verified all four against the committed files (below), so the values are correct — presentation gap only.

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
```

## Finding 4 — INFO, cross-criterion (Q03/Q06 owners, not scored here)

`entry:121` asserts oracle agreement "on every shared field" and byte-for-byte regeneration of `fixture.apk`/`truth.json`, but quotes no oracle values and shows no comparison/regeneration command. Both assertions are true — I reproduced them independently:

```
$ cd /tmp/q11regen && cp …/generator.py . && python3 -B generator.py   # Python 3.14.8
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json
```

and `truth.json` contains exactly the values the readout prints for image sha/size, the three members' `local_header_offset` (0/465/618), sizes, CRC-32 (`962d075f`/`2635c82a`/`e948d738`), the 9 strings, the 3 attribute rows (`name_idx` 3/5/6, `data_type` 3/16/3) and the 2 non-zero resource ids. This is a presentation gap in the comparison section, not a wrong value.

## Re-derivations I ran (10 independent commands)

1. **Archive** — `hasattr` independent `hashlib`: `len 947`, `sha256 05d2280f…` ✓ item 1.
2. **EOCD/CD** — independent struct parse: `eocd_off 925`, `cd_size 188`, `cd_off 737`, `cdoff+size 925`, CD walk end `925` ✓ item 2.
3. **Members** — local headers walked independently (30-byte fixed part + name): payload offsets `49/506/668`, sizes `416/112/69`, `zlib.crc32` over each payload slice = `962d075f/2635c82a/e948d738` ✓ item 3.
4. **AXML chunk table** — script output: six chunks at `8(28/196),204(8/44),248(16/24),272(16/96),368(16/24),392(16/24)`, last end `392+24=416`; script also asserts `cursor==eocd` (`readout.py:119`) ✓ item 4.
5. **Struct widths** — `readout.py:52-60` builds the field-width lists and computes `sizes = {name: sum(w)}` (not hardcoded); output shows both `bytes_per_field` and `total_bytes`: `ResChunk_header 8`, `ResStringPool_header 28`, `ResXMLTree_node 16`, `ResXMLTree_attrExt 20`, `ResXMLTree_attribute 20`, `Res_value 8`. Cross-checked against `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`: `struct ResChunk_header` 218 (u16,u16,u32), `ResStringPool_header` 461 (chunk header + 5×u32), `ResXMLTree_node` 621 (8+u32+u32), `ResXMLTree_attrExt` 677 (2×u32+6×u16), `ResXMLTree_attribute` 707 (3×u32+Res_value), `Res_value` 287 (u16,u8,u8,u32) — all sums match ✓ item 5 derived, not assumed.
6. **String pool** — script output: `stringCount 9`, `styleCount 0`, `flags 0x00000100` (= `UTF8_FLAG`, snapshot 1<<8), `stringsStart 64`, offsets `[0,10,55,66,76,94,108,122,126]`, 9 decoded strings ✓ item 6.
7. **Resource map** — `entry_count 9`, seven zeros, `0x0101021b`/`0x0101021c` at indexes 5/6; start-element `res_id` decimals `16843291`/`16843292` equal those hex values ✓ items 7–8.
8. **DEX** — independent: magic `6465780a30333500`, `zlib.adler32(dex[12:]) = 3d120c30` = declared, `hashlib.sha1(dex[32:]) = a5fc7bea8fa9ffaa52243540c8026066511b9fce` = declared, `file_size/header_size 112`, `endian_tag 0x12345678` ✓ item 9.
9. **JAR manifest** — payload bytes `b'Manifest-Version: 1.0\r\nCreated-By: revenger-r65 fixture generator\r\n\r\n'`, 69 bytes, one `\r\n\r\n` ✓ item 10 (and it is the ground truth against which line 41 is wrong).
10. **Stdout digest** — `python3 -B corpus/fixtures/apk-r65/readout.py | wc -l` = 15, `sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, exit 0; per-fact form `--fact eocd` / `--fact axml_string_pool` prints single lines ✓ `entry:5`, `entry:154-162`.

## Checklist

| Q11 requirement | result |
|---|---|
| every count/offset/identifier/digest carries its deriving command + output inside the entry | **FAIL** — item 3's MANIFEST payload hex (`entry:41`) is not the command's output; item 2 signature hex not printed (LOW); header S041 digests lack command (LOW) |
| output blocks verbatim vs deriving command | 14/15 lines byte-identical; 1 line false (`member[META-INF/MANIFEST.MF]`) |
| constants derived, not assumed (item 5) | **PASS** — summed from S038 field lists at `readout.py:52-60`, cross-checked against the snapshot structs; observed `headerSize`/`attributeStart`/`attributeSize` (28/16/20/20) equal the derived widths |
| no recorded value presented as re-derived | **PASS** in items 1–10 apart from line 41; §Comparison's oracle/regeneration assertions are true but unshown (INFO) |
| tests/checks not credited as coverage | entry credits no verifier; `recheck:` is the same readout command (Q13 owner's decision, not mine) |

## Residual risk

- The single wrong line is the only false value I found; because it sits in an output block that the entry presents as verbatim command output, a reader cannot distinguish it from a fixture change without running the command — exactly what Q11 exists to prevent. Treat the output blocks as unverified until regenerated.
- The fixture, oracle, script and container arithmetic all agree with the committed bytes, and regeneration is deterministic on this host (Python 3.14.8, matching the oracle's `python_version`), so the underlying C05 evidence is sound; the Q11 failure is documentary and mechanically fixable.
- Confidence in the rest of Q11: high (10 independent re-derivations, full 15-line textual diff).

## Verification gaps

- I did not score Q01's S038 line-anchor accuracy beyond the struct/enum anchors used by item 5 (lines 218, 241-246, 287, 461, 612, 621, 677, 707 all resolve in the snapshot).
- I did not run `reports/round-65/measure.py` (out of my lane; C1/C2 counter seats own it).
- I did not assess the S039/rea row or the README flip (other criteria/seats).

No tool installs or upgrades were performed.
