# Round 29 independent language-byte oracle

## Evidence pointers

- Input bytes: `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe` (1024 bytes; SHA-256 `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`).
- Baseline source manifest: `.shokunin/revenger/corpus/fixtures/pe-r28/truth.json` (claims type 10, name 1, language 1033, payload offset 600/length 15 and payload SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`).
- Baseline parser record: `.shokunin/revenger/corpus/live/runs/round-28/inspection.json`, Evidence `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`.
- New run record and ledger, for comparison only: `.shokunin/revenger/corpus/live/runs/round-29/inspection.json` (Evidence `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb`) and `LEDGER.md`.

## Raw-byte derivation / reproducible checks

The PE resource directory is at file offset 512 (`0x200`); the three directory levels are at 512, 536, and 560. The language leaf entry is the third entry at file offset 576 (`0x240`), after its 16-byte directory header. Its four bytes are `09 04 00 00`: the first DWORD is an integer ID entry (`0x00000409`), hence language ID 1033. The following DWORD points to the data entry at offset 584. That entry reports payload RVA `0x2058` and size 15; section mapping places it at file offset 600. This agrees with the baseline manifest and saved baseline parser record.

Read-only commands (run from repository root):

```sh
sha256sum .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
xxd -g1 -s 0x200 -l 0x70 .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
python3 - <<'PY'
from pathlib import Path
import hashlib
p = Path('.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe')
b = p.read_bytes()
print('size', len(b), 'sha256', hashlib.sha256(b).hexdigest())
print('resource root / entries / data entry:', b[512:528].hex(), b[528:536].hex(), b[552:560].hex(), b[576:584].hex(), b[584:600].hex())
print('language word', hex(int.from_bytes(b[576:578], 'little')), 'payload', b[600:615], hashlib.sha256(b[600:615]).hexdigest())
# Oracle only; do not write this candidate. It differs at one byte.
candidate = b[:576] + bytes([0x0c]) + b[577:]
print('delta offsets', [i for i,(x,y) in enumerate(zip(b,candidate)) if x != y])
print('candidate bytes', candidate[576:580].hex(), 'language', int.from_bytes(candidate[576:578], 'little'))
print('candidate sha256', hashlib.sha256(candidate).hexdigest())
PY
```

Observed source values from these checks: file SHA-256 `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`; language bytes `09 04`, payload bytes `SEV-R27-PAYLOAD`, payload SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. The in-memory candidate oracle changes only offset 576 from `0x09` to `0x0c`; it yields language bytes `0c 04` / little-endian ID 1036 and candidate whole-file SHA-256 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`. No fixture was written or REA command run by this worker.

## OBSERVATION

The r28 raw bytes encode the language ID as 1033 at offset 576. The exact proposed one-byte replacement is `09→0c`, yielding ID 1036; resource type/name entries and data-entry/payload bytes are outside this mutation. In the existing saved r29 record, the parser reports type 10, name 1, language 1036, payload offset 600, length 15, and the same payload SHA-256. The saved r29 record reports whole-file SHA-256 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`, matching the independently computed in-memory candidate.

## INFERENCE

The source bytes independently support the specified mutation oracle: changing the low byte of the leaf language ID at offset 576 from `09` to `0c` converts `0x0409` (1033) to `0x040c` (1036), without changing the payload bytes. The saved r29 output is consistent with that one-byte candidate and with unchanged payload attribution. This supports only fixture-scoped static parser sensitivity to this field, subject to independent verification of the produced r29 fixture bytes.

## UNKNOWN

I did not read or hash `corpus/fixtures/pe-r29/fixture.exe` in this assigned oracle task, so the saved r29 digest/output alone does not establish its actual bytes or independently prove a one-byte file delta. No Windows loader behavior, language fallback, resource selection, or execution semantics are established. No general PE parser correctness is established.
