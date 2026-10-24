NOT-FALSIFIED — `truth.json:axml_declared` is fully byte-derivable from fixture.apk and regeneration is byte-exact, but the fixture is tool-mistakable for a real APK and its "inert" self-label never reaches the bytes.

Scope: attack `corpus/fixtures/apk-r65/` fitness as known truth — member mistakability, inertness legibility, oracle derivability. Read-only seat; no production edits.

## Counterexample A — every member misidentifies as a genuine artifact

`file(1)` (magic 5.46 host tool) on the extracted members and the container:

```
$ file fixture.apk classes.dex AndroidManifest.xml META-INF_MANIFEST.MF
fixture.apk:            Android package (APK), with AndroidManifest.xml
classes.dex:            Dalvik dex file version 035
AndroidManifest.xml:    Android binary XML
META-INF_MANIFEST.MF:   JAR Manifest, ASCII text, with CRLF line terminators
```

The stock host classifier calls the fixture "Android package (APK)" outright — not "contains" or "fragment of". The dex member carries a **fully self-consistent header**: verified magic `6465780a30333500` (file off `0x1fa`), stored Adler-32 `0x3d120c30` == recomputed over bytes 12+, stored SHA-1 `a5fc7bea…1b9fce` == recomputed over bytes 32+, `file_size=112==header_size=112`, `endian_tag=0x12345678`. A header-only validator (checksum+signature+size, no map/section sanity) accepts it as a real dex. Its inertness is legible only from `map_off=0` (off `0x252`→`52+0x1fa`) plus bytes 56–112 all-zero — a dex-literate read, not a legible marker.

The AXML package name `com.example.r65` (bytes `0xcb`) is a syntactically valid package id on the reserved `example.` domain — a scanner extracting (package, versionCode=1, versionName="1.0", `http://schemas.android.com/apk/res/android` ns) gets plausible package identity.

## Counterexample B — the intended "inert" label is dead code; inertness is only half-legible

`generator.py:31` defines `PADDING_NOTE = "R65 inert synthetic APK fixture; no executable content.\n"` but **no code path writes it**: it is never referenced after definition (grep: only line 31). Byte grep on the 947-byte image: `b'inert'` → none, `b'synthetic'` → none, `b'fixture'` → once at offset 716 (inside MANIFEST.MF `Created-By:`), `b'R65'` → none (the package string is lowercase `r65`). EOCD comment length = 0 (bytes `0x3a9–0x3aa` = `0000`); no extra fields on any member.

The sole self-label in the bytes is `Created-By: revenger-r65 fixture generator` at `META-INF/MANIFEST.MF` payload offset 668, `0x2be–0x2e2` — and it is only in the *provenance slot of the weakest member*: anyone taking `AndroidManifest.xml` or `classes.dex` out of the archive gets no inertness signal at all. Same-date DOS stamp `0x5d58 0x6000` (2026-10-24 12:00) on all three members hints synthetic, but a build could do that too.

## Derivability of `truth.json:axml_declared` — survives attack (strongest test run)

Independent `struct` walk (not readout.py; my own offsets: member payload at 49, string pool `sp=8`, `stringsStart=64` UTF-8 len-prefixed decode, resource map at 204, start-element at 272 attrs at `chunk+16+attributeStart`):

```
strings match: True        # all 9 pool strings
resource_ids match: True   # all 9 uint32 entries incl. 0x0101021b/0x0101021c
attrs match: True          # all 5 fields × 3 rows: ns_idx/name_idx/raw_value_idx/data_type/data
```

Every declared field — including `ns_idx: 4294967295` (the NO_INDEX null), `raw_value_idx` (unusual-but-honest choice: real aapt often emits `0xffffffff` for typed-attr rawValue; here 4/7/8 are declared and present), `data_type: 3`/`16`, `data: 4`/`1`/`8` — is exactly what sits in the struct fields; nothing is generator-intent-only. Regeneration reproduced fixture.apk byte-for-byte (`sha256 05d2280f…7afe7d03e`, 947 bytes) via `build_apk()` in a scratch dir, Python 3.14.8.

## Impacted axes

- **coverage**: C1's fixture premise ("authored known-truth") holds — the oracle is byte-faithful and regenerable, so the entry's known-truth footing is sound. The weaknesses are legibility/mistakability, not oracle fidelity; the entry's own §Limitations ("header only… intentionally not a valid dex") concedes the dex shape, though it does not disclose that `file(1)` and header-only dex checks accept the members as real.
- **calibration**: none — C2 is unaffected (fixture not in verifier surface).

## Smallest safe correction (fixable defect, not a judge-required rejection)

`file(1)`-level mistakability is a tradeoff (the fixture must parse as APK to exercise the AXML readout — a parser must accept it). The **dead `PADDING_NOTE`** is the fixable half: append a ZIP EOCD comment or member extra field with the note (one line in `build_apk()`, regenerates deterministically), and/or rename the package to an unambiguously synthetic id carrying `fixture` in-band (e.g. `com.example.r65.fixture`), so the AXML member self-labels on extraction. Alternatively `truth.json`/the entry may simply record the mistakability result as a limitation. Neither blocks the claims; both remove the "unlabeled inertness" gap.
