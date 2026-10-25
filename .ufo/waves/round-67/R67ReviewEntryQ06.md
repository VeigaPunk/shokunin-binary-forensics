Q06 PASS — every fixture sha256/offset/size/count premise in the landed v2 entry re-derives from the committed built bytes; fixture dir untouched since round-65 commit c7b7cf98; failed input (rejected r65 candidate) retained byte-identical to r66 tip.

Seat: R67ReviewEntryQ06 (fresh seat, not the author). Entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md`. Criterion: `corpus/QUALITY.md:18` (Q06 — fixture premises byte-verified against the built fixture; failed inputs retained; reject when an offset/operand/size/count is stated from intent rather than built bytes, M04/M05).

## 1. Hash-pinned premises match the built fixture (entry:4, :5, :20, :166)

`sha256sum corpus/fixtures/apk-r65/*` (cwd `/home/vgpnk/Projects/shokunin/revenger-shokunin`):

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk   (entry:4,:20 claim — match)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json    (entry:4 claim — match)
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py    (entry:4,:16,:166 claim — match)
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  generator.py  (not claimed in entry)
```

`wc -c fixture.apk` → `947` — matches entry:20 (`947 bytes`).

## 2. Recheck command reproduces the claimed receipt (entry:6, :166)

`python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r67-readout.out` → `exit=0`, `wc -l` → `15`, `sha256sum` → `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the pinned receipt. The stdout's only path is repo-relative `corpus/fixtures/apk-r65/fixture.apk`, as claimed.

## 3. Independent non-author re-derivation of offsets/sizes/operands

Blind pass with `zipfile`+`struct` over the built bytes (not the author's readout):

```
AndroidManifest.xml      hdr_off=0    crc=962d075f csize=416 usize=416 payload_offset=49  first16=03000800a001000001001c00c4000000
classes.dex              hdr_off=465  crc=2635c82a csize=112 usize=112 payload_offset=506 first16=6465780a30333500300c123da5fc7bea
META-INF/MANIFEST.MF     hdr_off=618  crc=e948d738 csize=69  usize=69  payload_offset=668 first16=4d616e69666573742d56657273696f6e
file_size=947  eocd_at=925  cd_entries=3  cd_size=188  cd_off=737  (737+188=925)
```

Every value equals the entry's embedded outputs at entry:27-45 (items 2-3), including the repaired 16-byte `4d616e69666573742d56657273696f6e` = ASCII `Manifest-Version` (entry:42/:45). `payload_offset = local_header_offset + 30 + name_len + extra_len` re-derived per the entry's stated derivation (entry:34). Dex bytes 8-11 of first16 are `300c123d` = little-endian `0x3d120c30`, the declared checksum at entry:110 — internally consistent.

## 4. No fixture byte changed since round 65

- `git log -- corpus/fixtures/apk-r65/` → exactly one commit: `c7b7cf9` (round-65 introduction; full sha `c7b7cf98ddeecbd5464e47396f224e6384b78905` — matches the entry:5 pin `c7b7cf98`).
- `git diff c7b7cf98..HEAD -- corpus/fixtures/` → empty, exit 0.
- `git status --short corpus/fixtures corpus/knowledge` → empty (no uncommitted edits).

Void condition `corpus/fixtures` byte-freeze (claims.md:127-128) holds.

## 5. Failed inputs retained

The falsified round-65 candidate — the failed input carrying the M39 drift — is retained and byte-preserved:

`git show 8362a235:corpus/knowledge/round-65-apk-axml-byte-evidence.md | cmp - corpus/knowledge/round-65-apk-axml-byte-evidence.md` → **BYTE-IDENTICAL** to the r66 tip version (which carries `admission-status: rejected` and the drifted entry:41). Its drifted hex is intact as the C7 red-before surface, per claims.md:133-134.

## 6. Intent-vs-bytes scan

Every offset, operand, size and count in items 1-10 is printed by the saved `readout.py` (sha-pinned, runs stdlib-only against the committed bytes) — nothing is stated from intent. The one premise not re-run this round (generator regeneration, entry:124) is explicitly labeled prior evidence with the bytes hash-pinned instead — a recorded provenance, not a silent assumption.

OFF- entry:45 wording — `the 16-byte prefix of 'Manifest-Version: 1.0'` loosely attaches "16-byte" to a sentence whose inline hex `4d616e69666573742d` is the 9-byte `Manifest-`; the value itself is verified correct, only the phrasing is slightly loose.
OFF- `git status` cleanliness confirmed only for `corpus/fixtures` and `corpus/knowledge`; other paths outside Q06 scope were not inspected.

Checks exercised: sha256 of all four fixture files, readout full-run receipt (exit/line-count/stdout-sha), blind zipfile+struct re-derivation of all ZIP premises, git log/diff fixture freeze, cmp byte-preservation of the rejected r65 candidate.
