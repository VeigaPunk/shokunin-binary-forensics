# PE header: section virtual size and data-directory size

## Scope and method

Inspected the fixture bytes directly; did not invoke REA or execute the target. Fixture: `.shokunin/revenger/corpus/fixtures/pe-r31/fixture.exe`, 1,024 bytes, SHA-256 `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47`.

## Concrete observations

- DOS header points to PE signature at file offset `0x40`; COFF machine is `0x014c` (i386), one section. Optional header is PE32 (`0x010b`), 224 bytes, with 16 data-directory entries.
- Section/file alignments are `0x1000` / `0x200`; `SizeOfImage=0x3000`, `SizeOfHeaders=0x200`.
- The sole `.rsrc` section has `VirtualAddress=0x2000`, `VirtualSize=0xD0`, `PointerToRawData=0x200`, `SizeOfRawData=0x200`. Thus its virtual extent is `[0x2000, 0x20D0)`; its raw extent is `[0x200, 0x400)` (file-alignment padding beyond the declared virtual size).
- Data-directory entry 2 (resource directory) is `(VirtualAddress=0x2000, Size=0xD0)`. It exactly matches the `.rsrc` virtual extent and fits within that section's raw-backed bytes. All other directory entries are `(0,0)`.

## Interpretation and pitfalls

- For this fixture, the resource directory's nonzero RVA and size are internally bounded by the one section: `RVA + size = 0x20D0`, equal to section `VA + VirtualSize`. The raw data available for that RVA range is `0x200` bytes. This is a static layout observation, not validation of resource-tree contents or loader acceptance.
- Do not treat `SizeOfRawData` as the section's logical virtual size: raw alignment accounts for the extra `0x130` bytes. Conversely, do not require `VirtualSize` itself to be file-aligned.
- A generic rule that every directory must fit wholly inside one section is too strong. The security/certificate directory (index 4) uses a file offset rather than an RVA; directories may also need format-specific treatment. Apply RVA-to-file mapping and bounds checks only to RVA-based directories, and account for overlaps/headers and section boundaries rather than blindly using raw sizes.
- Zero address/zero size entries here are absent. In malformed or adversarial files, validate arithmetic/bounds and avoid silently accepting only one of address/size as zero.

## Bounded recommendation

For this fixture and similar PE checks, report each nonempty RVA directory against section virtual and raw-backed ranges, distinguishing declared virtual extent from alignment padding. Add targeted cases where directory size ends exactly at `VirtualSize`, exceeds it by one, and falls in raw padding; separately test the certificate-table file-offset convention. Do not infer runtime behavior from header consistency alone.
