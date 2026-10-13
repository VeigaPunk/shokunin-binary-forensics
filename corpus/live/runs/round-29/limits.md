# Round 29 — static boundary observation (LEAF)

## Evidence pointers

- Baseline saved record: `.shokunin/revenger/corpus/live/runs/round-28/inspection.json`
  - `/evidence_id` = `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`
  - `/subject/digest/sha256` and `/normalized_result/artifact/sha256` = `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`; `/normalized_result/artifact/bytes` = 1024.
  - `/normalized_result/directories/0/location` = `{offset:512, bytes:24}`, directories 1 and 2 at offsets 536 and 560, each 24 bytes.
  - `/normalized_result/resources/0` reports type ID 10, name ID 1, language ID 1033; its `/entry_locations` are offsets 528, 552, 576 (8 bytes each). `/data_entry_location` is offset 584 (16 bytes). `/payload/location` is offset 600 (15 bytes), and `/payload/sha256` = `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
  - `/normalized_result/limitations` (also top-level `/limitations`) explicitly says this is a static resource inventory; language fallback, image decoding, and actual shell/window loading are not observed. Non-icon payloads remain opaque.
- Baseline bytes: `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe`.
- Round 29 declaration in `.shokunin/revenger/LOG.md`, “Round 29 declaration — calibration”: proposed sole byte change is offset 576, `0x09→0x0c`, with a claimed resulting language ID 1036. This report independently checks the baseline only; it does not inspect a round-29 artifact or result.

## Raw-byte checks (read-only)

Commands from repository root:

```sh
sha256sum .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
xxd -g1 -s 560 -l 40 .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
python3 - <<'PY'
from pathlib import Path
import hashlib
p = Path('.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe')
b = p.read_bytes()
print('size', len(b), 'sha256', hashlib.sha256(b).hexdigest())
for off, n in ((512,24),(536,24),(560,24),(576,8),(584,16),(600,15)):
    print(off, b[off:off+n].hex(' '))
print('payload sha256', hashlib.sha256(b[600:615]).hexdigest())
PY
```

Observed output: size 1024; file SHA-256 `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`. At offset 560 the 24-byte language directory entry is `00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 48 00 00 00`; thus its ID field at 576–577 is little-endian `09 04` = 0x0409 (decimal 1033), and its target is offset 584 (`0x48`). At 584 the data entry begins `58 20 00 00 0f 00 00 00`, reporting RVA 0x2058 and length 15; the mapped raw payload begins at file offset 600 and is `SEV-R27-PAYLOAD`. Payload SHA-256 matches the saved record above. The 0x0409→0x040c byte-field prediction is a static encoding comparison only; it does not establish what any loader selects or displays.

## Assessment

- **OBSERVATION:** The saved r28 inspection and source bytes agree on one reported resource: IDs `(type 10, name 1, language 1033)`, data entry at 584, 15-byte payload at 600, and the recorded payload digest. The language entry's two ID bytes are `09 04`.
- **INFERENCE:** If an otherwise identical file has only bytes 576–577 changed from `09 04` to `0c 04`, the bytes encode 0x040c (decimal 1036) at that resource-language entry. This predicts a static directory identity difference, not loader behavior. A saved inspection of that mutated artifact would be needed to establish parser output for it.
- **UNKNOWN:** No observation here establishes Windows/resource-loader language fallback or selection, whether a particular application requests this language, whether the resource is loaded or displayed, or behavior on malformed/other PE variants. The saved JSON is normalized output (`/raw_result` is null); by itself it does not authenticate the original CLI invocation. This worker did not run REA, inspect a round-29 artifact/result, execute the PE, or test loader behavior.
