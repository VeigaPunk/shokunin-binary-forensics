# Round 29 — raw-byte resource entry map

## Scope

Read-only inspection of `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe` to locate the resource-language entry declared for the planned round-29 byte change. No fixture mutation, REA invocation, or executable/loader test was performed.

## OBSERVATION — artifact and PE mapping

- Fixture size: 1024 bytes. SHA-256: `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`.
- DOS `e_lfanew` at file offset `0x3c` is `0x40`; signature at `0x40` is `50 45 00 00` (`PE\0\0`). COFF machine at `0x44` is `0x014c` (i386); optional-header magic at `0x58` is `0x010b` (PE32).
- PE32 resource data-directory entry is at file offset `0xc8` (decimal 200; directory index 2, 8 bytes each, beginning at optional-header offset 96). It contains RVA `0x2000`, size `0x67` (103 bytes).
- The sole section header at `0x138` names `.rsrc`, with VirtualAddress `0x2000`, SizeOfRawData `0x200`, PointerToRawData `0x200`. Thus resource-relative offset `r` maps to file offset `0x200 + r` for the shown resource structures.

## OBSERVATION — resource directory entries

All offsets below are absolute file offsets; each entry is 8 bytes, encoded as a 32-bit ID/name followed by a 32-bit target (high bit indicates a subdirectory; low 31 bits are relative to resource-directory RVA `0x2000`).

| Level | Directory header | Entry bytes | Decoded entry | Target |
|---|---:|---:|---|---|
| type | `0x200` | `0x210–0x217` (`0a 00 00 00 18 00 00 80`) | ID 10; subdirectory | relative `0x18` → file `0x218` |
| name | `0x218` | `0x228–0x22f` (`01 00 00 00 30 00 00 80`) | ID 1; subdirectory | relative `0x30` → file `0x230` |
| language | `0x230` | `0x240–0x247` (`09 04 00 00 48 00 00 00`) | ID `0x0409` = 1033; data entry | relative `0x48` → file `0x248` |

The exact round-29 target is therefore the two-byte language ID at **file offset `0x240` (576)**, bytes `09 04` in little-endian order. The containing eight-byte language entry is `[0x240,0x248)`. The following 16-byte data entry at `[0x248,0x258)` has `OffsetToData` RVA `0x2058`, size `0x0f`; section mapping gives payload file offset `0x200 + (0x2058 - 0x2000) = 0x258` (600), length 15. Payload bytes at `[0x258,0x267)` are `SEV-R27-PAYLOAD`.

The saved baseline record `.shokunin/revenger/corpus/live/runs/round-28/inspection.json` independently lists the resource path type ID 10 / name ID 1 / language ID 1033, `entry_locations` offsets 528, 552, 576 (8 bytes each), data entry offset 584 (16 bytes), and payload offset 600/length 15. This is consistent with the byte decode above. The fixture truth manifest `.shokunin/revenger/corpus/fixtures/pe-r28/truth.json` gives the same whole-file and payload hashes and language ID 1033.

## Raw-byte checks / commands

Run from repository root; these commands only read the artifact and print fields. `struct.unpack_from` uses little-endian PE fields.

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, struct
p = Path('.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe')
b = p.read_bytes()
u16 = lambda o: struct.unpack_from('<H', b, o)[0]
u32 = lambda o: struct.unpack_from('<I', b, o)[0]
pe = u32(0x3c)
opt = pe + 24
section = opt + u16(pe + 20)
print('size, sha256:', len(b), hashlib.sha256(b).hexdigest())
print('PE, machine, optional magic:', b[pe:pe+4].hex(), hex(u16(pe+4)), hex(u16(opt)))
print('resource RVA/size:', hex(u32(opt+96+16)), u32(opt+96+20))
print('section name/RVA/raw-size/raw-pointer:', b[section:section+8], hex(u32(section+12)), u32(section+16), hex(u32(section+20)))
for o in (0x210, 0x228, 0x240):
    print(hex(o), b[o:o+8].hex(' '), 'first DWORD=', hex(u32(o)), 'second DWORD=', hex(u32(o+4)))
print('language ID:', hex(u16(0x240)), u16(0x240))
print('data-entry RVA/size:', hex(u32(0x248)), u32(0x24c))
print('payload:', b[0x258:0x267], hashlib.sha256(b[0x258:0x267]).hexdigest())
PY
```

Expected relevant output: resource RVA/size `0x2000 103`; entries `0x210` → ID `0xa`, target `0x80000018`, `0x228` → ID `0x1`, target `0x80000030`, `0x240` → ID `0x409`, target `0x48`; language ID `0x409 1033`; data-entry RVA/size `0x2058 15`; payload `b'SEV-R27-PAYLOAD'`.

## INFERENCE

The declared round-29 mutation at offset 576 (`0x240`) from first byte `0x09` to `0x0c`, with second byte `0x04` unchanged, changes the little-endian language ID from `0x0409` (1033) to `0x040c` (1036). It does not overlap the data-entry or payload bytes. If the remaining file is copied byte-for-byte, the payload mapping and its bytes/hash remain unchanged. This is a structural byte-level prediction, not an observed mutated artifact or parser result.

## UNKNOWN

This check alone does not establish that the planned mutated file was made, that REA reports language 1036, that its whole-file digest/Evidence identity is as claimed, or that a Windows loader accepts or selects the resource. It does not test PE parser completeness or runtime/resource-language fallback behavior.
