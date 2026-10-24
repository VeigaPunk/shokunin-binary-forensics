source: S036 — REA firmware-analysis guide, `docs/firmware-analysis.md`, at pinned tag `rea-agents-6.5.0` — https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md (docs, tier A for route-scope sentences only; registry id assigned by L1 at the round-64 append) — scope: what the `inspect-firmware-regions` route does per the version that produced the round-63 record, not evidence of local provider execution and not evidence about any fixture byte — anchors: tag object `refs/tags/rea-agents-6.5.0` → commit `3b79af28e80785afce9f5998d8f03289402a1847`, file blob `152819177f8dce2124dea2a6a541e701cee227ed`; line 3 "REA accepts **Binwalk 3.1.x** for region inspection"; line 56 `rea inspect-firmware-regions /path/to/firmware.bin`; §"Interpret the results" lines 91-96 "Region offsets refer to bytes in the original firmware. `reported_size` preserves Binwalk's output" and "Neither a signature nor its confidence byte proves a valid partition, encryption or runtime behavior."; lines 83-85 "Both return Evidence with the original path and SHA-256, raw producer reports"; snapshot `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`, 10695 bytes, sha256 `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`, HTTP 200, opened 2026-10-24 (provenance sidecar `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json`)
source: S037 — Authored firmware fixture, its generator and oracle, and the saved round-63 record bundle — `corpus/fixtures/firmware-r63/firmware-r63.bin`, `corpus/fixtures/firmware-r63/generator.py`, `corpus/fixtures/firmware-r63/truth.json`, `corpus/live/runs/round-63/inspection.json`, `corpus/live/runs/round-63/receipt.json`, `corpus/live/runs/round-63/LEDGER.md` (own-work, tier A for byte/record correspondence; registry id assigned by L1 at the round-64 append) — scope: the byte content of that one fixture and of that one oracle, and the literal saved fields of that one record and its receipt at claim base commit `666ea84b6be2eec2b0359f556ba2429fc9044c36` — anchors: fixture sha256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` (2048 bytes), generator.py sha256 `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` (5532 bytes), truth.json sha256 `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` (1933 bytes), inspection.json sha256 `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` (3904 bytes), receipt.json sha256 `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` (492 bytes), LEDGER.md sha256 `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6` (22671 bytes)
verified-at: 2026-10-24 (round-64 work commit pending; the fixture, generator, oracle, record, receipt and ledger bytes read here are byte-identical at claim base commit `666ea84b6be2eec2b0359f556ba2429fc9044c36` and in the working tree, verified by `git show <base>:<path> | sha256sum` against `sha256sum <path>` — item 2 below)
recheck: `python3 -B readout.py <repo-root>` — the script is the `### Code` block in §Reproduce, saved verbatim as `readout.py`; it is Python standard library only (`hashlib`, `json`, `zlib`, `sys`), exits 0, and prints 7 JSON lines whose SHA-256 is `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`; the per-value form `python3 -B readout.py <repo-root> --fact '<id>'` prints the single JSON line for one named fact (`image`, `regions`, `members`, `payloads`, `oracle`, `record`, `digests`). The stdout carries only repo-relative paths, never the lane's absolute root, so the same bytes give the same 7 lines from any checkout of the same commit.
coverage-map: C07 (`corpus/README.md`, firmware images) — the padding spans and the two zlib-wrapped members of one authored fixture, compared against one authored oracle and one saved `inspect_firmware_regions` record. This entry does not cover the REA `extract_firmware` route, vendor or device firmware families, any container format, or any other firmware fixture: no extraction run and no vendor image was examined, and the C07 row's own scope is "firmware images".
admission-status: candidate — drafted in the round-64 build wave for independent Q01–Q13 review; the README C07 status flip belongs to L1 and follows the fresh-seat decisions

# Firmware-region byte readout of one authored fixture, compared with its authored oracle and a saved Binwalk 3.1.0 record — C07

Scope. One authored 2048-byte file, `corpus/fixtures/firmware-r63/firmware-r63.bin`, and the documents that describe it: the authored oracle `corpus/fixtures/firmware-r63/truth.json`, the generator that wrote both, and the saved round-63 record `corpus/live/runs/round-63/inspection.json`, whose own envelope attributes it to a Binwalk 3.1.0 `inspect_firmware_regions` run, with its receipt and ledger. The analysis is **manual and standard-library only**: a Python script reads the file's bytes, inflates the zlib streams in memory, and hashes the inflated bytes. Nothing is extracted to disk, executed, emulated or mounted; no firmware tool or provider is invoked; no verifier source is read. The comparison is **one fixture's region view**: every all-zero padding span and both compressed members with their decompressed sizes and digests, checked field-by-field against an authored oracle and against the two regions the saved Binwalk run reported. It is not a vendor or device image, not evidence about any real firmware, not an extraction or execution claim, not a provider-completeness claim and not an authenticity claim. "Firmware" here is the C07 coverage label for the route that produced the record, not a format or family identification.

## Observation

Every numbered item below is produced by the readout in §Reproduce or by the command shown. The command is given with the output it printed; item numbers are the entry's own and are not identifiers in any file. The readout's two rules matter for reading the numbers:

- **Members** are found by scanning every byte offset for a zlib stream that reaches end-of-stream cleanly (`zlib.decompressobj`, `eof` set, no unconsumed tail). The scan is blind to the oracle: it starts at offset 0 and never consults `truth.json`.
- **Padding spans** are the maximal all-zero runs of the *complement* of the member byte ranges. Member ranges are subtracted first, because compressed bytes can themselves be `0x00`: the whole-file maximal zero runs include a one-byte run at offset 1098, inside the second member's range `[1024, 1114)`, which this entry does **not** call padding (item 4).

**Image bytes**

1. The fixture is **2048 bytes** with SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`, read from the file's bytes.

```
$ python3 -B readout.py <repo-root> --fact 'image'
{"fact": "image", "path": "corpus/fixtures/firmware-r63/firmware-r63.bin", "sha256": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "size": 2048}
```

2. The six files this entry reads are byte-identical at claim base commit `666ea84b6be2eec2b0359f556ba2429fc9044c36` and in the working tree:

```
$ git show 666ea84b6be2eec2b0359f556ba2429fc9044c36:corpus/fixtures/firmware-r63/firmware-r63.bin | sha256sum
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  -
$ git show 666ea84b6be2eec2b0359f556ba2429fc9044c36:corpus/fixtures/firmware-r63/generator.py | sha256sum
4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4  -
$ git show 666ea84b6be2eec2b0359f556ba2429fc9044c36:corpus/fixtures/firmware-r63/truth.json | sha256sum
9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  -
$ git show 666ea84b6be2eec2b0359f556ba2429fc9044c36:corpus/live/runs/round-63/inspection.json | sha256sum
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  -
$ git show 666ea84b6be2eec2b0359f556ba2429fc9044c36:corpus/live/runs/round-63/receipt.json | sha256sum
e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d  -
$ git show 666ea84b6be2eec2b0359f556ba2429fc9044c36:corpus/live/runs/round-63/LEDGER.md | sha256sum
25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6  -
```

```
$ sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin corpus/fixtures/firmware-r63/generator.py corpus/fixtures/firmware-r63/truth.json corpus/live/runs/round-63/inspection.json corpus/live/runs/round-63/receipt.json corpus/live/runs/round-63/LEDGER.md
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  corpus/fixtures/firmware-r63/firmware-r63.bin
4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4  corpus/fixtures/firmware-r63/generator.py
9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  corpus/fixtures/firmware-r63/truth.json
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  corpus/live/runs/round-63/inspection.json
e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d  corpus/live/runs/round-63/receipt.json
25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6  corpus/live/runs/round-63/LEDGER.md
```

3. Re-running the generator in scratch (never under `corpus/`) reproduces the fixture and the oracle byte-for-byte on this host, whose Python and zlib versions equal the ones the recipe records (`Python 3.14.8`, `zlib 1.3.2` compile and runtime):

```
$ cp corpus/fixtures/firmware-r63/generator.py /tmp/revenger-r64-entry/gen/
$ cd /tmp/revenger-r64-entry/gen && python3 -B generator.py
wrote firmware-r63.bin sha256=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be size=2048
region offset=0 size=512 kind=padding
region offset=512 size=79 kind=zlib
region offset=591 size=433 kind=padding
region offset=1024 size=90 kind=zlib
region offset=1114 size=934 kind=padding
$ sha256sum firmware-r63.bin truth.json
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  firmware-r63.bin
9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  truth.json
```

**Region partition**

4. The image partitions into exactly three all-zero padding spans and two zlib members, in this order and without gaps: `[0,512)`, `[512,591)`, `[591,1024)`, `[1024,1114)`, `[1114,2048)`. The five regions cover **2048** bytes contiguously from offset 0, and all three padding spans are verified all-zero byte by byte. The padding spans are **512**, **433** and **934** bytes.

```
$ python3 -B readout.py <repo-root> --fact 'regions'
{"contiguous_from_zero": true, "covered_bytes": 2048, "fact": "regions", "image_size": 2048, "padding_all_zero": true, "regions": [{"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 0, "size": 512}, {"compressed_size": 79, "decompressed_sha256": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86", "decompressed_size": 78, "kind": "zlib", "offset": 512}, {"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 591, "size": 433}, {"compressed_size": 90, "decompressed_sha256": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9", "decompressed_size": 97, "kind": "zlib", "offset": 1024}, {"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 1114, "size": 934}]}
```

**Compressed members**

5. Both members carry the RFC 1950 header bytes `78 da` (CMF `0x78`, FLG `0xda`): the header check `(CMF<<8|FLG) % 31 == 0` holds, `FLEVEL` is 3 (maximum compression, matching the oracle's level 9) and `FDICT` is 0. The 4-byte big-endian Adler-32 trailer equals the Adler-32 recomputed over the inflated plaintext for both members. Member A starts at offset **512**, is **79** compressed bytes and inflates to **78** bytes with SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`; member B starts at offset **1024**, is **90** compressed bytes and inflates to **97** bytes with SHA-256 `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`.

```
$ python3 -B readout.py <repo-root> --fact 'members'
{"fact": "members", "members": [{"adler32_computed_hex": "7b3b1d2d", "adler32_matches_trailer": true, "adler32_trailer_hex": "7b3b1d2d", "cmf_hex": "78", "compressed_size": 79, "decompressed_sha256": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86", "decompressed_size": 78, "end_offset": 591, "fdict": 0, "flevel": 3, "flg_hex": "da", "header_check_mod31_zero": true, "offset": 512}, {"adler32_computed_hex": "11bf252c", "adler32_matches_trailer": true, "adler32_trailer_hex": "11bf252c", "cmf_hex": "78", "compressed_size": 90, "decompressed_sha256": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9", "decompressed_size": 97, "end_offset": 1114, "fdict": 0, "flevel": 3, "flg_hex": "da", "header_check_mod31_zero": true, "offset": 1024}]}
```

6. The inflated bytes decode as UTF-8 text under the oracle-stated member labels `diagnostic-note` (offset 512) and `component-note` (offset 1024). The labels themselves are **not** byte-derived: a zlib stream carries no name, so the labels are the generator's and oracle's recorded names, not a readout value.

```
$ python3 -B readout.py <repo-root> --fact 'payloads'
{"fact": "payloads", "payloads": [{"decompressed_size": 78, "offset": 512, "utf8": "R63 inert synthetic diagnostic record\nsensor=pressure\nunits=kPa\nstate=nominal\n"}, {"decompressed_size": 97, "offset": 1024, "utf8": "R63 inert synthetic component inventory\ncomponent=radio\nrevision=fixture-only\nexecution=disabled\n"}]}
```

**Correspondence with the authored oracle**

7. All **25** compared fields match `corpus/fixtures/firmware-r63/truth.json`: image size, digest and basename; padding byte `00` and recipe image size; region count 5; each padding span's kind, size and fill; each member's kind, compressed size, decompressed size and decompressed SHA-256; and both `payload_utf8` strings. The oracle's `build_recipe` records Python `3.14.8`, zlib compile/runtime `1.3.2`, level 9 and the same member offsets; those are oracle-stated build metadata, matched only by item 3's reproduction on this host, not by a byte rule.

```
$ python3 -B readout.py <repo-root> --fact 'oracle'
{"all_match": true, "checks": [{"derived": 2048, "field": "image.size", "match": true, "stated": 2048}, {"derived": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "field": "image.sha256", "match": true, "stated": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be"}, {"derived": "firmware-r63.bin", "field": "image.path", "match": true, "stated": "firmware-r63.bin"}, {"derived": "00", "field": "padding_byte_hex", "match": true, "stated": "00"}, {"derived": 2048, "field": "build_recipe.image_size", "match": true, "stated": 2048}, {"derived": 5, "field": "region_count", "match": true, "stated": 5}, {"derived": "padding", "field": "padding@0.kind", "match": true, "stated": "padding"}, {"derived": 512, "field": "padding@0.size", "match": true, "stated": 512}, {"derived": "00", "field": "padding@0.fill_hex", "match": true, "stated": "00"}, {"derived": "padding", "field": "padding@591.kind", "match": true, "stated": "padding"}, {"derived": 433, "field": "padding@591.size", "match": true, "stated": 433}, {"derived": "00", "field": "padding@591.fill_hex", "match": true, "stated": "00"}, {"derived": "padding", "field": "padding@1114.kind", "match": true, "stated": "padding"}, {"derived": 934, "field": "padding@1114.size", "match": true, "stated": 934}, {"derived": "00", "field": "padding@1114.fill_hex", "match": true, "stated": "00"}, {"derived": "zlib", "field": "zlib@512.kind", "match": true, "stated": "zlib"}, {"derived": 79, "field": "zlib@512.compressed_size", "match": true, "stated": 79}, {"derived": 78, "field": "zlib@512.decompressed_size", "match": true, "stated": 78}, {"derived": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86", "field": "zlib@512.decompressed_sha256", "match": true, "stated": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86"}, {"derived": "zlib", "field": "zlib@1024.kind", "match": true, "stated": "zlib"}, {"derived": 90, "field": "zlib@1024.compressed_size", "match": true, "stated": 90}, {"derived": 97, "field": "zlib@1024.decompressed_size", "match": true, "stated": 97}, {"derived": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9", "field": "zlib@1024.decompressed_sha256", "match": true, "stated": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9"}, {"derived": "R63 inert synthetic diagnostic record\nsensor=pressure\nunits=kPa\nstate=nominal\n", "field": "payload_utf8@512", "match": true, "stated": "R63 inert synthetic diagnostic record\nsensor=pressure\nunits=kPa\nstate=nominal\n"}, {"derived": "R63 inert synthetic component inventory\ncomponent=radio\nrevision=fixture-only\nexecution=disabled\n", "field": "payload_utf8@1024", "match": true, "stated": "R63 inert synthetic component inventory\ncomponent=radio\nrevision=fixture-only\nexecution=disabled\n"}], "fact": "oracle"}
```

**Correspondence with the saved record**

8. All **13** compared fields match `corpus/live/runs/round-63/inspection.json`: the record's subject SHA-256, its `normalized_result.input_size` 2048, the operation `inspect_firmware_regions`, the provider version `3.1.0`, a region count of 2, and for each reported region the offset (**512**, **1024**), signature (`zlib`), `reported_size` (**79**, **90**) and `size_basis` (`provider_reported_validation_unknown`). The record's `coverage` is `signature_scan`, `confidence` `observed`, `authority` `shipped-artifact`, and its region kinds are exactly `{"zlib"}`.

```
$ python3 -B readout.py <repo-root> --fact 'record'
{"all_match": true, "authority": "shipped-artifact", "checks": [{"derived": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "field": "subject.digest.sha256", "match": true, "stated": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be"}, {"derived": 2048, "field": "normalized_result.input_size", "match": true, "stated": 2048}, {"derived": "inspect_firmware_regions", "field": "operation", "match": true, "stated": "inspect_firmware_regions"}, {"derived": "3.1.0", "field": "provider.version", "match": true, "stated": "3.1.0"}, {"derived": 2, "field": "region_count", "match": true, "stated": 2}, {"derived": true, "field": "record@512.present", "match": true, "stated": true}, {"derived": "zlib", "field": "record@512.signature", "match": true, "stated": "zlib"}, {"derived": 79, "field": "record@512.reported_size", "match": true, "stated": 79}, {"derived": "provider_reported_validation_unknown", "field": "record@512.size_basis", "match": true, "stated": "provider_reported_validation_unknown"}, {"derived": true, "field": "record@1024.present", "match": true, "stated": true}, {"derived": "zlib", "field": "record@1024.signature", "match": true, "stated": "zlib"}, {"derived": 90, "field": "record@1024.reported_size", "match": true, "stated": 90}, {"derived": "provider_reported_validation_unknown", "field": "record@1024.size_basis", "match": true, "stated": "provider_reported_validation_unknown"}], "confidence": "observed", "coverage": "signature_scan", "fact": "record", "region_kinds": ["zlib"]}
```

9. The four read files' own digests and sizes, as computed by the same script:

```
$ python3 -B readout.py <repo-root> --fact 'digests'
{"fact": "digests", "files": {"corpus/fixtures/firmware-r63/firmware-r63.bin": {"sha256": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "size": 2048}, "corpus/fixtures/firmware-r63/truth.json": {"sha256": "9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6", "size": 1933}, "corpus/live/runs/round-63/LEDGER.md": {"sha256": "25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6", "size": 22671}, "corpus/live/runs/round-63/inspection.json": {"sha256": "f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9", "size": 3904}}}
```

## Correspondence

Against **truth.json** the 25 selected comparisons all match: the 2048-byte image and its digest, the three padding spans with fill `00`, both members' offsets and compressed sizes, both decompressed sizes and digests, and both plaintext strings. The oracle additionally names the members and states the build recipe; the names have no byte counterpart in a zlib stream, and the recipe is reproduced only as item 3's host-level replay.

Against the **saved record** the agreement is narrower and is expected to be: the saved record's own fields name the two zlib signature matches with their offsets and provider-reported sizes, and nothing else. It contains no padding regions (its `coverage` is `signature_scan`), no member names, no decompressed sizes or digests, and `extractions` is `{}`; the second scanner named in the REA route (Unblob) appears nowhere in it. The ledger's `O11` row mentions an author-side Unblob probe outside the record; that probe is **not** used as evidence here and this entry draws no conclusion from it. Where the record and this readout state the same number, they were produced independently — the record by Binwalk 3.1.0 `--search-all`, the readout by inflating the bytes — and they agree on both offsets and both compressed sizes.

What the agreement does **not** establish (Q09). A SHA-256 match proves only that the bytes hashed are the bytes named: not who authored them, not that the oracle is canonical or unique, not that Binwalk's signature inference is correct, and not that the fixture resembles any real firmware. The record's own `raw_result` shows it ran on a private workspace copy (`/tmp/rea-firmware-7rPoLl/firmware.bin`); the link to the fixture is the record's own subject digest and `input_size`, plus S036's statement that region offsets refer to bytes in the original firmware. The oracle's `padding_byte_hex`/`fill_hex` values and member labels are recorded metadata compared for correspondence, not independently authenticated facts.

## Observation, inference and unknown

**Observation (read from bytes or saved fields).**
- O1 — the fixture is 2048 bytes, sha256 `bdfe9f46…510be` (item 1).
- O2 — the same six files hash identically at base commit `666ea84b…` and in the working tree (item 2).
- O3 — the generator, re-run in scratch on this host, writes a fixture and oracle with the same two digests (item 3).
- O4 — the image partitions into padding `[0,512)`, member `[512,591)`, padding `[591,1024)`, member `[1024,1114)`, padding `[1114,2048)`; coverage 2048, contiguous (item 4).
- O5 — both members have `78 da` headers with valid mod-31 check, `FLEVEL` 3, `FDICT` 0, clean end-of-stream and matching Adler-32 trailers; compressed sizes 79 and 90; inflated sizes 78 and 97 with the two digests above (item 5).
- O6 — the inflated bytes are the two UTF-8 strings shown, 78 and 97 bytes (item 6).
- O7 — all 25 oracle comparisons match (item 7).
- O8 — all 13 saved-record comparisons match; record coverage is `signature_scan` and `extractions` is `{}` (item 8).
- O9 — a whole-file maximal-zero-run rule would also emit the one-byte run at offset 1098 inside the second member; this entry's partition subtracts member ranges first (item 4 rule).

**Inference (bounded interpretation of those observations).**
- I1 — both members are RFC 1950 zlib streams, because each decodes to end-of-stream under `zlib.decompressobj` with a mod-31-valid header and an Adler-32 trailer equal to the recomputed value. This is a property of these bytes under this decoder, not a claim about the producer.
- I2 — the three padding spans are authored zero fill rather than scan artifacts, because the oracle records fill `00` and the spans are the maximal zero runs of the member complement.
- I3 — the record's two regions are the same two members this readout found, because offset and compressed size agree for both and no other region is reported.
- I4 — the fixture bytes are reproducible from the committed generator on a host with Python 3.14.8 and zlib 1.3.2, since the replay emitted identical digests; this says nothing about other zlib builds.

**Unknown (not answerable from these bytes and this record).**
- U1 — what the members mean, or whether `diagnostic-note`/`component-note` are the right labels: names live in the generator/oracle, not in the compressed bytes.
- U2 — whether these bytes correspond to any real firmware image, vendor format, container, partition table or device; no vendor image was examined and none is claimed.
- U3 — what extraction or execution would yield: the record extracted nothing (`extractions` `{}`), no extraction route was run, and no member was executed.
- U4 — how another scanner would partition the same image: the record shows Binwalk 3.1.0 only; the ledger's author-side Unblob probe is outside the record and is not evidence here.
- U5 — whether the zero padding has domain meaning or is merely the generator's fill choice.

## Limitations

- **One authored fixture, no format claim.** Every number here describes `corpus/fixtures/firmware-r63/firmware-r63.bin` only. No vendor image, no real firmware family, no container or filesystem format, and no general "firmware region" behaviour is claimed; "firmware" is the C07 coverage label.
- **The padding definition is this readout's rule.** Padding is "maximal all-zero run in the complement of member ranges". A different rule — container-declared padding, a minimum run length, or whole-file zero runs — gives a different partition; whole-file runs additionally yield the one-byte run at 1098 inside the second compressed stream, which this entry deliberately does not count.
- **Digest equality is not authenticity (Q09).** Matching digests prove only that the bytes hashed are the bytes named. They do not authenticate the generator, canonize the oracle, or validate the engine's inference.
- **The saved record is one Binwalk 3.1.0 signature scan.** Its `coverage` is `signature_scan` and its sizes are `provider_reported_validation_unknown`; per S036 lines 91-96 neither a signature nor its confidence byte proves a valid partition, and Binwalk may replace unknown lengths with the next signature or EOF. This entry therefore compares the record's numbers to sizes measured directly from the compressed streams rather than treating them as independent measurement, and it makes no provider-completeness claim.
- **No extraction, execution or re-analysis.** No REA or Binwalk run was performed for this entry; the fixture was read, not re-analysed by a provider. Extraction and execution behaviour remain unknown (U3).
- **Generator replay is host-bounded.** Item 3's byte identity holds on this host's Python 3.14.8 / zlib 1.3.2; another zlib build may emit different compressed bytes for the same plaintext while decompressing identically, so byte reproducibility is not claimed generally.

## Cross-lane scope note (Q10)

Reported, not absorbed. This entry covers only the authored bytes of `corpus/fixtures/firmware-r63/firmware-r63.bin` against the saved `inspect_firmware_regions` record `corpus/live/runs/round-63/inspection.json`. A C07 `held` token does not settle ADJ-06 (fleet `.ufo/l0-questions.md:42` remains open; `tsukuroi-shokunin/PROVINCE.md:51` still names the recipient "protocol integrator — kaidoku/revenger ownership unresolved"), does not absorb kaidoku Core's live `inspect-firmware-regions` / `extract-firmware` surface or its archive inventory (`kaidoku-shokunin/PROVINCE.md:50,76-79,125`) or its provider-pin registry (`:64-71`), and does not absorb tsukuroi's driver/firmware health plane (`tsukuroi-shokunin/PROVINCE.md:3-4,11-13`). No ownership is declared and no other lane's file is cited as support for a value here.

## Q01–Q13 map

| Q | Where this entry answers it |
|---|---|
| Q01 | Every load-bearing sentence is sourced: S036 tier A for route scope (what `inspect-firmware-regions` returns, what `reported_size`/`size_basis` mean, that a signature does not prove a partition), S037 tier A for the byte and record correspondence. No other source is used. |
| Q02 | S036 is cited with URL, pinned tag, blob/commit ids, located ≤25-word quotes with snapshot line numbers (3, 56, 83-85, 91-96), access date 2026-10-24, HTTP 200, byte count and snapshot sha256. S037 is cited by the six file digests at base commit `666ea84b…`. |
| Q03 | The values were derived by scanning the bytes from offset 0 with no oracle input; no author readout was used. Independent blind derivation by a fresh seat is the admission test, not this entry's own claim. |
| Q04 | Falsifiable: `recheck` prints 7 JSON lines with a pinned sha256 `aa353251…`; any changed fixture byte, member boundary, digest or record field changes the stdout and breaks the pin. |
| Q05 | Scope paragraph and §Limitations bound the claim to one authored fixture; no vendor image, format family, extraction, execution, provider completeness or authenticity is claimed. |
| Q06 | The fixture premises are byte-verified against the built bytes: items 1–5 derive the image size and SHA-256, every padding span, both member offsets, both compressed sizes and both decompressed sizes and digests by command from the file itself, before and independently of any comparison with the oracle or the saved record; no offset, size or count is stated from intent. |
| Q07 | The fixture's content is never executed, extracted or written: the script inflates and hashes in memory only; the only writes in this work are the draft file itself and the scratch generator replay under `/tmp/revenger-r64-entry/gen/`, both outside `corpus/`. |
| Q08 | Saved-record claims quote literal fields (`input_size`, `coverage`, `size_basis`, `reported_size`, offsets, signature, `extractions`) and are separated from inference and unknown. |
| Q09 | §Correspondence states the digest disclaimer: a match proves only the bytes hashed; the record is treated as an observation layer, and its build metadata and labels are not authenticated. |
| Q10 | Provenance of the record is named: `inspection.json` (3904 bytes, sha256 `f6997835…`), its receipt (`e930a549…`, exit 0, command `npx -y rea-agents@6.5.0 inspect-firmware-regions … --format json`) and the run's ledger (`25a4a18b…`), all byte-identical at base. |
| Q11 | Every value in §Observation carries its in-entry command and that command's printed output; the 7-line full stdout is reproduced in §Reproduce with its sha256. |
| Q12 | The authored oracle `truth.json` is compared field-by-field (25 selected checks, all match), and the saved record separately (13 checks); the readout is independent of the saved record, but the oracle and the image share one author, so agreement is claimed only for those fields, not for uniqueness or canonicity. |
| Q13 | No guard credit is sought: no verifier, recheck-tool or checker is introduced as coverage, and none of the values is presented as covered by an automatic check. The recheck command is a reproducibility aid, not a gate. |

## Reproduce

Save the code block below verbatim as `readout.py`, then from the lane root run the commands shown in §Observation; the full run prints the 7 lines reproduced here. Python 3 standard library only; no third-party import; no network; no write.

### Code

```python
#!/usr/bin/env python3
"""Stdlib-only byte readout of corpus/fixtures/firmware-r63/firmware-r63.bin.

Every value printed is derived from the bytes of the named files at the
repository root given as argv[1].  Nothing is extracted to disk, executed,
networked or produced by a firmware tool.
"""
import hashlib
import json
import sys
import zlib

FIXTURE = "corpus/fixtures/firmware-r63/firmware-r63.bin"
ORACLE = "corpus/fixtures/firmware-r63/truth.json"
RECORD = "corpus/live/runs/round-63/inspection.json"
LEDGER = "corpus/live/runs/round-63/LEDGER.md"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def members_of(data):
    out = []
    i, n = 0, len(data)
    while i < n:
        if data[i] == 0x78:
            d = zlib.decompressobj()
            try:
                payload = d.decompress(data[i:])
            except zlib.error:
                i += 1
                continue
            if d.eof and not d.unconsumed_tail:
                consumed = n - i - len(d.unused_data)
                cmf, flg = data[i], data[i + 1]
                trailer = data[i + consumed - 4:i + consumed]
                out.append({
                    "offset": i,
                    "compressed_size": consumed,
                    "end_offset": i + consumed,
                    "cmf_hex": "%02x" % cmf,
                    "flg_hex": "%02x" % flg,
                    "header_check_mod31_zero": ((cmf << 8) | flg) % 31 == 0,
                    "flevel": flg >> 6,
                    "fdict": (flg >> 5) & 1,
                    "decompressed_size": len(payload),
                    "decompressed_sha256": sha(payload),
                    "adler32_trailer_hex": trailer.hex(),
                    "adler32_computed_hex": "%08x" % zlib.adler32(payload),
                    "adler32_matches_trailer": trailer == zlib.adler32(payload).to_bytes(4, "big"),
                    "payload": payload,
                })
                i += consumed
                continue
        i += 1
    return out


def complement(n, spans):
    out, cur = [], 0
    for a, b in sorted(spans):
        if cur < a:
            out.append((cur, a))
        cur = max(cur, b)
    if cur < n:
        out.append((cur, n))
    return out


def padding_spans(data, members):
    spans = []
    for a, b in complement(len(data), [(m["offset"], m["end_offset"]) for m in members]):
        start = None
        for i in range(a, b):
            if data[i] == 0:
                if start is None:
                    start = i
            else:
                if start is not None:
                    spans.append({"offset": start, "size": i - start,
                                  "all_zero": all(x == 0 for x in data[start:i])})
                    start = None
        if start is not None:
            spans.append({"offset": start, "size": b - start,
                          "all_zero": all(x == 0 for x in data[start:b])})
    return spans


def load(root, name):
    with open(root + "/" + name, "rb") as f:
        return f.read()


def fact_image(root):
    data = load(root, FIXTURE)
    return {"fact": "image", "path": FIXTURE, "size": len(data), "sha256": sha(data)}


def fact_members(root):
    data = load(root, FIXTURE)
    ms = members_of(data)
    return {"fact": "members", "members": [
        {k: v for k, v in m.items() if k != "payload"} for m in ms]}


def fact_regions(root):
    data = load(root, FIXTURE)
    ms = members_of(data)
    pad = padding_spans(data, ms)
    regions = [{"kind": "padding", "offset": p["offset"], "size": p["size"],
                "fill_hex": "00", "all_zero": p["all_zero"]} for p in pad]
    regions += [{"kind": "zlib", "offset": m["offset"],
                 "compressed_size": m["compressed_size"],
                 "decompressed_size": m["decompressed_size"],
                 "decompressed_sha256": m["decompressed_sha256"]} for m in ms]
    regions.sort(key=lambda r: r["offset"])
    covered, ok = 0, True
    for idx, r in enumerate(regions):
        size = r["size"] if r["kind"] == "padding" else r["compressed_size"]
        if r["offset"] != covered:
            ok = False
        covered = r["offset"] + size
    return {"fact": "regions", "regions": regions, "covered_bytes": covered,
            "image_size": len(data), "contiguous_from_zero": ok,
            "padding_all_zero": all(p["all_zero"] for p in pad)}


def fact_payloads(root):
    data = load(root, FIXTURE)
    return {"fact": "payloads", "payloads": [
        {"offset": m["offset"], "decompressed_size": m["decompressed_size"],
         "utf8": m["payload"].decode("utf-8")} for m in members_of(data)]}


def fact_oracle(root):
    data = load(root, FIXTURE)
    oracle = json.loads(load(root, ORACLE).decode("utf-8"))
    ms = members_of(data)
    pad = padding_spans(data, ms)
    checks = []

    def add(name, derived, stated):
        checks.append({"field": name, "derived": derived, "stated": stated,
                       "match": derived == stated})

    add("image.size", len(data), oracle["image"]["size"])
    add("image.sha256", sha(data), oracle["image"]["sha256"])
    add("image.path", FIXTURE.split("/")[-1], oracle["image"]["path"])
    add("padding_byte_hex", "00" if all(p["all_zero"] for p in pad) else "mixed",
        oracle["build_recipe"]["padding_byte_hex"])
    add("build_recipe.image_size", len(data), oracle["build_recipe"]["image_size"])
    o_regions = oracle["regions"]
    add("region_count", len(pad) + len(ms), len(o_regions))
    by_off = {r["offset"]: r for r in o_regions}
    for p in pad:
        r = by_off.get(p["offset"], {})
        add("padding@%d.kind" % p["offset"], "padding", r.get("kind"))
        add("padding@%d.size" % p["offset"], p["size"], r.get("size"))
        add("padding@%d.fill_hex" % p["offset"], "00", r.get("fill_hex"))
    for m in ms:
        r = by_off.get(m["offset"], {})
        add("zlib@%d.kind" % m["offset"], "zlib", r.get("kind"))
        add("zlib@%d.compressed_size" % m["offset"], m["compressed_size"], r.get("size"))
        dm = r.get("decompressed_member", {})
        add("zlib@%d.decompressed_size" % m["offset"], m["decompressed_size"], dm.get("size"))
        add("zlib@%d.decompressed_sha256" % m["offset"], m["decompressed_sha256"],
            dm.get("sha256"))
    for rec in oracle["build_recipe"]["members"]:
        m = next((x for x in ms if x["offset"] == rec["offset"]), None)
        add("payload_utf8@%d" % rec["offset"],
            None if m is None else m["payload"].decode("utf-8"), rec["payload_utf8"])
    return {"fact": "oracle", "all_match": all(c["match"] for c in checks),
            "checks": checks}


def fact_record(root):
    rec = json.loads(load(root, RECORD).decode("utf-8"))
    data = load(root, FIXTURE)
    ms = members_of(data)
    norm = rec["normalized_result"]
    checks = []
    checks.append({"field": "subject.digest.sha256", "derived": sha(data),
                   "stated": rec["subject"]["digest"]["sha256"],
                   "match": sha(data) == rec["subject"]["digest"]["sha256"]})
    checks.append({"field": "normalized_result.input_size", "derived": len(data),
                   "stated": norm["input_size"], "match": len(data) == norm["input_size"]})
    checks.append({"field": "operation", "derived": "inspect_firmware_regions",
                   "stated": rec["operation"],
                   "match": rec["operation"] == "inspect_firmware_regions"})
    checks.append({"field": "provider.version", "derived": "3.1.0",
                   "stated": rec["provider"]["version"],
                   "match": rec["provider"]["version"] == "3.1.0"})
    regions = norm["regions"]
    checks.append({"field": "region_count", "derived": len(ms), "stated": len(regions),
                   "match": len(ms) == len(regions)})
    for m in ms:
        r = next((x for x in regions if x["offset"] == m["offset"]), None)
        checks.append({"field": "record@%d.present" % m["offset"], "derived": True,
                       "stated": r is not None, "match": r is not None})
        if r is None:
            continue
        checks.append({"field": "record@%d.signature" % m["offset"], "derived": "zlib",
                       "stated": r["signature"], "match": r["signature"] == "zlib"})
        checks.append({"field": "record@%d.reported_size" % m["offset"],
                       "derived": m["compressed_size"], "stated": r["reported_size"],
                       "match": r["reported_size"] == m["compressed_size"]})
        checks.append({"field": "record@%d.size_basis" % m["offset"],
                       "derived": "provider_reported_validation_unknown",
                       "stated": r["size_basis"],
                       "match": r["size_basis"] == "provider_reported_validation_unknown"})
    return {"fact": "record", "coverage": norm["coverage"],
            "confidence": rec["confidence"], "authority": rec["authority"],
            "region_kinds": sorted({r["signature"] for r in regions}),
            "all_match": all(c["match"] for c in checks), "checks": checks}


def fact_digests(root):
    out = {}
    for name in (FIXTURE, ORACLE, RECORD, LEDGER):
        b = load(root, name)
        out[name] = {"size": len(b), "sha256": sha(b)}
    return {"fact": "digests", "files": out}


FACTS = {
    "image": fact_image,
    "members": fact_members,
    "regions": fact_regions,
    "payloads": fact_payloads,
    "oracle": fact_oracle,
    "record": fact_record,
    "digests": fact_digests,
}
ORDER = ["image", "regions", "members", "payloads", "oracle", "record", "digests"]


def main(argv):
    if len(argv) < 2:
        sys.exit("usage: readout.py <repo-root> [--fact <id>]")
    root = argv[1]
    if "--fact" in argv:
        fid = argv[argv.index("--fact") + 1]
        sys.stdout.write(json.dumps(FACTS[fid](root), sort_keys=True) + "\n")
        return
    for fid in ORDER:
        sys.stdout.write(json.dumps(FACTS[fid](root), sort_keys=True) + "\n")


if __name__ == "__main__":
    main(sys.argv)
```

### Stdout

```
$ python3 -B readout.py <repo-root> | tee /tmp/revenger-r64-entry/all.txt
{"fact": "image", "path": "corpus/fixtures/firmware-r63/firmware-r63.bin", "sha256": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "size": 2048}
{"contiguous_from_zero": true, "covered_bytes": 2048, "fact": "regions", "image_size": 2048, "padding_all_zero": true, "regions": [{"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 0, "size": 512}, {"compressed_size": 79, "decompressed_sha256": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86", "decompressed_size": 78, "kind": "zlib", "offset": 512}, {"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 591, "size": 433}, {"compressed_size": 90, "decompressed_sha256": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9", "decompressed_size": 97, "kind": "zlib", "offset": 1024}, {"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 1114, "size": 934}]}
{"fact": "members", "members": [{"adler32_computed_hex": "7b3b1d2d", "adler32_matches_trailer": true, "adler32_trailer_hex": "7b3b1d2d", "cmf_hex": "78", "compressed_size": 79, "decompressed_sha256": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86", "decompressed_size": 78, "end_offset": 591, "fdict": 0, "flevel": 3, "flg_hex": "da", "header_check_mod31_zero": true, "offset": 512}, {"adler32_computed_hex": "11bf252c", "adler32_matches_trailer": true, "adler32_trailer_hex": "11bf252c", "cmf_hex": "78", "compressed_size": 90, "decompressed_sha256": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9", "decompressed_size": 97, "end_offset": 1114, "fdict": 0, "flevel": 3, "flg_hex": "da", "header_check_mod31_zero": true, "offset": 1024}]}
{"fact": "payloads", "payloads": [{"decompressed_size": 78, "offset": 512, "utf8": "R63 inert synthetic diagnostic record\nsensor=pressure\nunits=kPa\nstate=nominal\n"}, {"decompressed_size": 97, "offset": 1024, "utf8": "R63 inert synthetic component inventory\ncomponent=radio\nrevision=fixture-only\nexecution=disabled\n"}]}
{"all_match": true, "checks": [{"derived": 2048, "field": "image.size", "match": true, "stated": 2048}, {"derived": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "field": "image.sha256", "match": true, "stated": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be"}, {"derived": "firmware-r63.bin", "field": "image.path", "match": true, "stated": "firmware-r63.bin"}, {"derived": "00", "field": "padding_byte_hex", "match": true, "stated": "00"}, {"derived": 2048, "field": "build_recipe.image_size", "match": true, "stated": 2048}, {"derived": 5, "field": "region_count", "match": true, "stated": 5}, {"derived": "padding", "field": "padding@0.kind", "match": true, "stated": "padding"}, {"derived": 512, "field": "padding@0.size", "match": true, "stated": 512}, {"derived": "00", "field": "padding@0.fill_hex", "match": true, "stated": "00"}, {"derived": "padding", "field": "padding@591.kind", "match": true, "stated": "padding"}, {"derived": 433, "field": "padding@591.size", "match": true, "stated": 433}, {"derived": "00", "field": "padding@591.fill_hex", "match": true, "stated": "00"}, {"derived": "padding", "field": "padding@1114.kind", "match": true, "stated": "padding"}, {"derived": 934, "field": "padding@1114.size", "match": true, "stated": 934}, {"derived": "00", "field": "padding@1114.fill_hex", "match": true, "stated": "00"}, {"derived": "zlib", "field": "zlib@512.kind", "match": true, "stated": "zlib"}, {"derived": 79, "field": "zlib@512.compressed_size", "match": true, "stated": 79}, {"derived": 78, "field": "zlib@512.decompressed_size", "match": true, "stated": 78}, {"derived": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86", "field": "zlib@512.decompressed_sha256", "match": true, "stated": "a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86"}, {"derived": "zlib", "field": "zlib@1024.kind", "match": true, "stated": "zlib"}, {"derived": 90, "field": "zlib@1024.compressed_size", "match": true, "stated": 90}, {"derived": 97, "field": "zlib@1024.decompressed_size", "match": true, "stated": 97}, {"derived": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9", "field": "zlib@1024.decompressed_sha256", "match": true, "stated": "2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9"}, {"derived": "R63 inert synthetic diagnostic record\nsensor=pressure\nunits=kPa\nstate=nominal\n", "field": "payload_utf8@512", "match": true, "stated": "R63 inert synthetic diagnostic record\nsensor=pressure\nunits=kPa\nstate=nominal\n"}, {"derived": "R63 inert synthetic component inventory\ncomponent=radio\nrevision=fixture-only\nexecution=disabled\n", "field": "payload_utf8@1024", "match": true, "stated": "R63 inert synthetic component inventory\ncomponent=radio\nrevision=fixture-only\nexecution=disabled\n"}], "fact": "oracle"}
{"all_match": true, "authority": "shipped-artifact", "checks": [{"derived": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "field": "subject.digest.sha256", "match": true, "stated": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be"}, {"derived": 2048, "field": "normalized_result.input_size", "match": true, "stated": 2048}, {"derived": "inspect_firmware_regions", "field": "operation", "match": true, "stated": "inspect_firmware_regions"}, {"derived": "3.1.0", "field": "provider.version", "match": true, "stated": "3.1.0"}, {"derived": 2, "field": "region_count", "match": true, "stated": 2}, {"derived": true, "field": "record@512.present", "match": true, "stated": true}, {"derived": "zlib", "field": "record@512.signature", "match": true, "stated": "zlib"}, {"derived": 79, "field": "record@512.reported_size", "match": true, "stated": 79}, {"derived": "provider_reported_validation_unknown", "field": "record@512.size_basis", "match": true, "stated": "provider_reported_validation_unknown"}, {"derived": true, "field": "record@1024.present", "match": true, "stated": true}, {"derived": "zlib", "field": "record@1024.signature", "match": true, "stated": "zlib"}, {"derived": 90, "field": "record@1024.reported_size", "match": true, "stated": 90}, {"derived": "provider_reported_validation_unknown", "field": "record@1024.size_basis", "match": true, "stated": "provider_reported_validation_unknown"}], "confidence": "observed", "coverage": "signature_scan", "fact": "record", "region_kinds": ["zlib"]}
{"fact": "digests", "files": {"corpus/fixtures/firmware-r63/firmware-r63.bin": {"sha256": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "size": 2048}, "corpus/fixtures/firmware-r63/truth.json": {"sha256": "9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6", "size": 1933}, "corpus/live/runs/round-63/LEDGER.md": {"sha256": "25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6", "size": 22671}, "corpus/live/runs/round-63/inspection.json": {"sha256": "f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9", "size": 3904}}}
$ sha256sum /tmp/revenger-r64-entry/all.txt
aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae  /tmp/revenger-r64-entry/all.txt
```
