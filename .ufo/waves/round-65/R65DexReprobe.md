PASS — independently re-derived every requested `classes.dex` declared-header fact; no divergence.

## Evidence

- Independently read `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk` as bytes, walked its ZIP end-of-central-directory and central-directory records with `struct`, selected the `classes.dex` local payload (stored member, offset 506, 112 bytes), and parsed its little-endian fields. The calculation imported only `hashlib`, `zlib`, and `struct`.
- Actual calculation output:
  ```text
  apk_bytes=947
  apk_sha256=05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
  classes.dex_method=0 payload_offset=506 payload_bytes=112
  magic_hex=6465780a30333500
  declared_adler32=0x3d120c30
  adler32_bytes_12_on=0x3d120c30
  declared_sha1=a5fc7bea8fa9ffaa52243540c8026066511b9fce
  sha1_bytes_32_on=a5fc7bea8fa9ffaa52243540c8026066511b9fce
  file_size=112
  header_size=112
  endian_tag=0x12345678
  dex_payload_bytes=112
  ```
- Comparison: entry item 9, `corpus/knowledge/round-65-apk-axml-byte-evidence.md:103-107`, reports the same magic, recomputed and declared Adler-32 and SHA-1, file size, header size, and endian tag. The readout calculation is at `corpus/fixtures/apk-r65/readout.py:232-248`.

## Risks and blockers

- No divergence or blocker found. This re-probe establishes only the requested declared-header facts for this authored fixture; it makes no claim that the header-only payload is a valid or executable DEX.

## Files changed

- `.ufo/waves/round-65/R65DexReprobe.md` only.
