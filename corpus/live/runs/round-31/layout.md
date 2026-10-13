# Round 31 two-name PE resource tree layout (pre-producer)

**Scope:** derive a candidate layout from the committed r30 PE bytes only. No fixture was written, no REA producer was run, and no parser outcome is claimed. This is a layout proposal to support the declared two-resource test.

## Baseline observations

Source: `.shokunin/revenger/corpus/fixtures/pe-r30/fixture.exe` (1024 bytes). Commands used:

```sh
xxd -g1 -l 256 .shokunin/revenger/corpus/fixtures/pe-r30/fixture.exe
xxd -g1 -s 512 -l 128 .shokunin/revenger/corpus/fixtures/pe-r30/fixture.exe
```

- DOS `e_lfanew` at file `0x3c` is `0x40`; `PE\0\0` at `0x40`. COFF optional-header size is `0xe0` at `0x54`; PE32 optional header starts `0x58` (`0x010b`). Resource data-directory entry is index 2 at `0x58 + 96 + 16 = 0xc8`: RVA `0x2000`, size `0x67` (103 bytes).
- Section headers at `0x178` (first section) map RVA `0x2000` to raw file offset `0x200` (512): section virtual address `0x2000`, raw pointer `0x200`. Thus resource-relative offsets below can be used directly as file offsets for this fixture.
- At `0x200`, root directory header has `NumberOfNamedEntries=0`, `NumberOfIdEntries=1`; its sole entry at `0x210` has type ID 10 and child-directory offset `0x18` (relative to resource root, file `0x218`). Type directory at `0x218` has one ID entry, name ID 2, child directory offset `0x30` (`0x230`). Name directory at `0x230` has language ID 1036 (`0x040c`) and data-entry offset `0x48` (`0x248`). Data entry at `0x248` points to payload RVA `0x2058`, size 15, which maps to file offset `0x258` (600); bytes `[600:615)` are `SEV-R27-PAYLOAD`.

## Proposed exact tree and placements

Use root-relative resource offsets, with all directory/data-entry structures 4-byte aligned:

| File offset | Resource-relative offset | Structure / entry | Proposed contents |
|---:|---:|---|---|
| 512 | 0x00 | root directory | named=0, IDs=1 (type 10) |
| 536 | 0x18 | type-10 directory | named=0, IDs=2; entries name IDs 2, 3 |
| 568 | 0x38 | name-ID-2 directory | named=0, IDs=1; language 1036 |
| 592 | 0x50 | name-ID-3 directory | named=0, IDs=1; language 1033 |
| 616 | 0x68 | name-2/language-1036 data entry | payload RVA `0x20a0`, size 15 |
| 632 | 0x78 | name-3/language-1033 data entry | payload RVA `0x20c0`, size 15 |
| 672 | 0xa0 | payload 1 | distinct 15-byte payload A |
| 704 | 0xc0 | payload 2 | distinct 15-byte payload B |

The 16-byte directory header followed by 8-byte entries gives: root at relative 0 has one entry and ends at 24 (`0x18`); type directory at `0x18` has two entries and ends at `0x38`; each language directory is 24 bytes and occupies `0x38..0x50` and `0x50..0x68`. Two 16-byte data entries then occupy `0x68..0x88`. Payload slots start at raw offsets 672 and 704 (RVA `0x20a0`, `0x20c0` under the existing section mapping); both are separate, non-overlapping 15-byte ranges.

For each directory header, set `Characteristics=0`, `TimeDateStamp=0`, version fields 0; set named-entry count 0 and ID-entry count as shown. Each ID entry is `<uint32 id, uint32 target>`; child directory target is `0x80000000 | relative_offset`. Therefore type entry target is `0x80000018`; name entries target `0x80000038` and `0x80000050`; language entries target data entries `0x68` and `0x78` (high bit clear). Data entries are `<uint32 payload_RVA, uint32 size=15, uint32 CodePage, uint32 Reserved>`; retaining r30's observed code page 0 and reserved 0 is a reasonable controlled choice. The existing resource data-directory size `0x67` must increase to cover the new structures and payloads; `0xc0+15 = 0xcf` bytes from resource root is sufficient, so size `0xcf` is a clear exact bound. Preserve the existing section mapping and unrelated bytes. These are proposed values, not an authored artifact.

## Checkable boundaries

The proposal encodes exactly paths `(type=10,name=2,lang=1036)` and `(type=10,name=3,lang=1033)`, with data entries at distinct offsets and payload RVAs mapping to distinct raw ranges. Payload bytes/digests must be chosen and recorded in fixture truth before production; do not assume bytes or hashes here. Validate directory targets as resource-root-relative offsets (not file offsets), payload addresses as image RVAs, and verify the section mapping against the actual section header. This predicts a valid PE resource-tree layout only; neither acceptance by REA nor Windows loader behavior is established.
