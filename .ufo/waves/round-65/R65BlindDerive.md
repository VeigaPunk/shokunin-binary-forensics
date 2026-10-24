PASS — Raw-byte archive identity and every ZIP field represented in `truth.json` agree; payload offsets and AXML chunk records are independently derived but not declared in the truth file.

## Evidence

The initial derivation read only `corpus/fixtures/apk-r65/fixture.apk`; I did not read `readout.py` or the knowledge entry. Raw-file measurement:

```text
stat -c 'size=%s' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk && sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk
size=947
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk
```

Python bytes walk of that APK found EOCD offset `925`, 3 entries, central-directory offset `737`, size `188`, comment length `0`. I decoded EOCD as `<4s4H2LH`, central headers as `<4s6H3L5H2L` (advancing by 46 plus name/extra/comment lengths), then local headers as `<4s5H3L2H`; payload offset is local offset + 30 + local filename length + local extra length. Actual output:

```text
ZIP[0] central_name='AndroidManifest.xml' local_name='AndroidManifest.xml' local_header_offset=0 payload_offset=49 compressed_size=416 uncompressed_size=416 local_name_len=19 local_extra_len=0 local_end=465
ZIP[1] central_name='classes.dex' local_name='classes.dex' local_header_offset=465 payload_offset=506 compressed_size=112 uncompressed_size=112 local_name_len=11 local_extra_len=0 local_end=618
ZIP[2] central_name='META-INF/MANIFEST.MF' local_name='META-INF/MANIFEST.MF' local_header_offset=618 payload_offset=668 compressed_size=69 uncompressed_size=69 local_name_len=20 local_extra_len=0 local_end=737
```

Comparison with `corpus/fixtures/apk-r65/truth.json`:

| Value | Raw-byte derivation | Truth | Result |
|---|---:|---:|---|
| APK size | 947 | 947 (`image.size`, lines 69–72) | match |
| APK SHA-256 | `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` | same (lines 69–72) | match |
| `AndroidManifest.xml` name / local offset / compressed / uncompressed | name / 0 / 416 / 416 | same (lines 75–83) | all match |
| `classes.dex` name / local offset / compressed / uncompressed | name / 465 / 112 / 112 | same (lines 84–92) | all match |
| `META-INF/MANIFEST.MF` name / local offset / compressed / uncompressed | name / 618 / 69 / 69 | same (lines 93–100) | all match |
| ZIP payload offsets | 49, 506, 668 | not specified | no truth value to compare |

The central and local filename bytes agreed for all three entries. The three truth member objects do not contain payload offsets (truth lines 74–101).

## AXML chunk walk

I selected the `AndroidManifest.xml` payload by its central-directory name, confirmed payload length `416`, and walked chunks from payload offset 8, reading each `<HHI` type/headerSize/size and advancing by size. Actual output:

```text
AXML payload_length=416 starts_chunk_walk_at=8
AXML[0] offset=8 type=0x0001 headerSize=28 size=196
AXML[1] offset=204 type=0x0180 headerSize=8 size=44
AXML[2] offset=248 type=0x0100 headerSize=16 size=24
AXML[3] offset=272 type=0x0102 headerSize=16 size=96
AXML[4] offset=368 type=0x0103 headerSize=16 size=24
AXML[5] offset=392 type=0x0101 headerSize=16 size=24
```

All chunks were in-bounds and ended exactly at payload length 416. The manifest length agrees with both ZIP sizes in truth (lines 75–83). `truth.json` lines 2–48 has `axml_declared` attributes, resource IDs, and strings, but no AXML chunk table or chunk offsets/types/sizes/headerSizes; therefore those six rows have no per-field truth comparator, rather than a truth divergence.

## Blockers / risks

No blocker for the requested byte derivation. The only comparison limit is that `truth.json` does not record payload offsets or the AXML chunk table.
