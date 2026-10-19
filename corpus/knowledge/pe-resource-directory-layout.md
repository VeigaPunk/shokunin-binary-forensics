source: S009 — https://learn.microsoft.com/en-us/windows/win32/debug/pe-format — anchor `The .rsrc Section` and its four subsections (`Resource Directory Table`, `Resource Directory Entries`, `Resource Directory String`, `Resource Data Entry`); page ms.date 2026-09-10, git_commit_id 55e845e9f3a6a3261f59a2f460f61edc25ffcdd5
source: S010 — https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/ — anchor `3.9.2 UTF-16`, definition D91 and Table 3-5; page meta-revision b734c94a21cc49b89c2e1823d65129189a40bf28 (version index marks 18.0.0 a preliminary draft)
source: S013 — `corpus/live/runs/round-59/inspection.stdout.json` — saved `inspect_pe_resources` record, Evidence `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db`, SHA-256 `bf7922db…`
verified-at: 2026-10-19
recheck: `python3 -B -` on the `## Reproduce` code block below, run from the lane root (stdlib only, read-only); expected output shown inline
coverage-map: C01

# PE resource directory (.rsrc) layout — byte-verified against fixture pe-r55

Narrow claims about the on-disk layout of the resource tree in one authored
fixture family (`corpus/fixtures/pe-r55/fixture.exe`, SHA-256
`41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`, 1536 bytes,
PE32+ magic `0x20b`). Every field statement below was re-derived from fixture
bytes on 2026-10-19 with the `## Reproduce` block, not taken from the saved
record under test (Q03/Q06/Q08).

## Observation

Each observation names the spec clause it instantiates and the bytes observed.

1. **Locating the tree.** Per the spec's data-directories table, the resource
   table is data-directory index 2 (`Resource Table … see The .rsrc Section`).
   Derived from the headers, not assumed: `e_lfanew` (u32 at 0x3c) = 64,
   signature `PE\0\0`, optional-header magic `0x20b` (PE32+), so data
   directories start 112 bytes into the optional header and index 2 sits at
   file offset 216: RVA 8192, size 240. The single section `.rsrc` has
   VirtualAddress 8192 and PointerToRawData 512, so the tree occupies file
   offsets 512–751 (240 bytes). Command (L1 re-run 2026-10-19):

   ```text
   python3 -c "import struct;b=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();e=struct.unpack_from('<I',b,0x3c)[0];o=e+24;m=struct.unpack_from('<H',b,o)[0];d=o+(112 if m==0x20b else 96)+16;r=struct.unpack_from('<II',b,d);s=o+struct.unpack_from('<H',b,e+20)[0];print(e,b[e:e+4],hex(m),d,r,b[s:s+8].rstrip(b'\0'),struct.unpack_from('<IIII',b,s+8))"
   64 b'PE\x00\x00' 0x20b 216 (8192, 240) b'.rsrc' (1024, 8192, 1024, 512)
   ```

2. **Resource Directory Table = 16-byte header.** Per `Resource Directory
   Table`: Characteristics (u32, offset 0), Time/Date Stamp (u32, 4), Major
   Version (u16, 8), Minor Version (u16, 10), Number of Name Entries (u16, 12),
   Number of ID Entries (u16, 14); entries follow immediately. Observed six
   tables (named, id counts; all zero version/characteristics fields):

   ```text
   dir@file512 named=0 ids=2   dir@file544 named=0 ids=2   dir@file576 named=1 ids=0
   dir@file600 named=0 ids=1   dir@file624 named=0 ids=1   dir@file648 named=0 ids=1
   ```

3. **Resource Directory Entry = 8 bytes.** Per `Resource Directory Entries`:
   offset 0 holds either a 32-bit Integer ID or a Name Offset (observed high
   bit set marks the string-offset case); offset 4 holds either a Subdirectory
   Offset (high bit 1, lower 31 bits are the `.rsrc`-relative address of the
   next table) or a Data Entry Offset (high bit 0). Observed entry at file
   offset 592: name field `0x800000e0` → high bit 1, offset 224 → string at
   file 736; child field `0x80000088` → subdirectory at 512+136=648. Observed
   leaf entry at file 616: ID 1033, child `0x000000a0` → data entry at
   512+160=672. All entry offsets are `.rsrc`-relative, not file-absolute —
   add the section's file base (here 512) to locate them on disk.

4. **Resource Directory String = u16 length + UTF-16LE code units, no
   terminator.** Per `Resource Directory String`: offset 0 is a 2-byte Length
   ("size of the string, not including length field itself"), then word-aligned
   Unicode data. Observed at file offset 736: length field 5, code-unit bytes
   `41003dd800de42002100`, strict UTF-16LE decode `A😀B!` — the 😀 (U+1F600)
   is the surrogate pair `D83D DE00` exactly as D91/Table 3-5 specifies for
   scalar values ≥ U+10000. Byte count = 2 + 2·length = 12, matching the saved
   record's `location {offset:736, bytes:12}`.

5. **Resource Data Entry = 16 bytes.** Per `Resource Data Entry`: Data RVA
   (u32, 0), Size (u32, 4), Codepage (u32, 8), Reserved (u32, 12). Observed
   three data entries at file offsets 672, 688, 704; e.g. 672 → RVA 8448, size
   48, codepage 0, reserved 0. For this fixture, payload file offset = Data
   RVA − 7680 (the `.rsrc` section maps RVA 8192 → file 512), so RVA 8448 →
   file 768; payload bytes there hash to
   `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`
   (`python3 -c "import hashlib;b=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();print(hashlib.sha256(b[768:816]).hexdigest())"`; fixture digest by `sha256sum corpus/fixtures/pe-r55/fixture.exe` → `41c0132a…`).

6. **Three-level tree.** Per the spec, "Windows uses three levels: Type Name
   Language" and "the first table determines Type ID, the second … Name ID,
   and the third … Language ID". Observed paths (type, name, language):
   `(3, 1, 1033)` → data@672, `(3, 2, 1033)` → data@688,
   `(14, name@736, 1033)` → data@704. The type-14 branch's name-level table
   carries 1 named + 0 ID entries, exercising the Name-entries-first layout.

7. **Saved-record cross-check.** The saved (byte-preserved, no producer rerun)
   `inspect_pe_resources` result for the one-byte-mutated sibling fixture r59 —
   Evidence `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db`,
   `corpus/live/runs/round-59/inspection.stdout.json` SHA-256
   `bf7922dbda2bc2dd817eaa13652f04e19c10ed8701feab5790a8703d55f22c0f`
   (`sha256sum`) — reports the same six directory locations/entry counts, data
   entries at 672/688/704, and `coverage.examined_entries=8` (6 tables' 8
   entries total). Command (L1 re-run 2026-10-19):
   `python3 -c "import json;r=json.load(open('corpus/live/runs/round-59/inspection.stdout.json'))['normalized_result'];print([(x['location']['offset'],x['named_entries'],x['id_entries']) for x in r['directories']],[x['data_entry_location']['offset'] for x in r['resources']],r['coverage'])"`
   → `[(512, 0, 2), (544, 0, 2), (600, 0, 1), (624, 0, 1), (576, 1, 0), (648, 0, 1)] [672, 688, 704] {'status': 'complete', 'examined_entries': 8, 'resources': 3}`. Consistent.

## Reproduce

```python
import struct
b = open('corpus/fixtures/pe-r55/fixture.exe', 'rb').read()
e = struct.unpack_from('<I', b, 0x3c)[0]                        # e_lfanew
opt = e + 24                                                     # optional header
magic = struct.unpack_from('<H', b, opt)[0]
rva, size = struct.unpack_from('<II', b, opt + (112 if magic == 0x20b else 96) + 16)
sec = opt + struct.unpack_from('<H', b, e + 20)[0]               # first section header
nsec = struct.unpack_from('<H', b, e + 6)[0]
for i in range(nsec):
    va, raw = struct.unpack_from('<I', b, sec + 40*i + 12)[0], struct.unpack_from('<I', b, sec + 40*i + 20)[0]
    vsz = struct.unpack_from('<I', b, sec + 40*i + 8)[0]
    if va <= rva < va + vsz: base = raw + (rva - va)             # .rsrc file offset
print(f'resource dir rva={rva} size={size} file_base={base}')
u16 = lambda o: struct.unpack_from('<H', b, o)[0]
u32 = lambda o: struct.unpack_from('<I', b, o)[0]
def walk(off, depth):
    named, ids = u16(off + 12), u16(off + 14)
    print('  ' * depth + f'dir@file{off} named={named} ids={ids}')
    for i in range(named + ids):
        e = off + 16 + i * 8
        name, child = u32(e), u32(e + 4)
        if name & 0x80000000:
            so = base + (name & 0x7fffffff)
            ln = u16(so); raw = b[so + 2:so + 2 + ln * 2]
            tag = f'STR@file{so} len={ln} raw={raw.hex()}'
        else:
            tag = f'ID={name & 0xffff}'
        print('  ' * depth + f'  e{i}@file{e}: {tag} -> child 0x{child:08x}')
        if child & 0x80000000:
            walk(base + (child & 0x7fffffff), depth + 1)
        else:
            de = base + child
            print('  ' * depth + f'    data@file{de}: '
                  f'rva={u32(de)} size={u32(de+4)} cp={u32(de+8)} res={u32(de+12)}')
walk(base, 0)
```

## Inference

- The spec's field table is sufficient to decode this fixture's tree
  byte-for-byte with stdlib `struct` alone; no loader semantics were needed.
- Named entries are rare in observed resources here (one of eight), so a
  decoder that assumes ID-only names would fail exactly on the
  `(14, A😀B!, 1033)` leaf — the leaf that motivated fixtures r55/r59.

## Unknown

- Whether multi-name tables in this fixture family exercise the spec's
  case-sensitive ascending sort (only one name entry exists to check).
- Semantics of nonzero Codepage/TimeDateStamp/Characteristics — all zero here.
- Whether any Windows loader or other parser accepts this authored tree.
- Trees deeper than Type/Name/Language ("can incorporate 2**31 levels").

## Limitations

- One authored PE32+ fixture family (r42-derived r55, mutated r59); no claim
  about arbitrary PE files, packed/truncated trees, or PE32.
- Static layout only. No Windows loader, icon rendering, or runtime claim.
- No claim about REA parser internals; the saved record is compared, not
  re-derived (Q04/Q09: its Evidence ID binds that saved output only).

## QUALITY check

| Q | verdict | basis |
|---|---|---|
| Q01 | pass | layout claims rest on S009 (spec, tier A for .rsrc field semantics); surrogate-pair claim on S010 D91; saved-record cross-check on S013 (own-work, tier A for what the saved record contains) |
| Q02 | pass | source/verified-at/recheck headers present; anchors name subsections and revision ids |
| Q03 | pass | expected values derived from fixture bytes and the spec, not from the saved normalized record |
| Q04 | pass | REA claim names `inspect_pe_resources` provider `rea-pe-resources` v1, saved Evidence ID; byte walk labeled manual |
| Q05 | n/a | no readiness/capability claim; the REA record is a saved artifact cited by hash, not a probe result |
| Q06 | pass | every offset/count re-derived by the `## Reproduce` command on 2026-10-19, including the data-directory slot and `.rsrc` file base (critic-post HIGH finding fixed: no hard-coded 216/512) |
| Q07 | n/a | no parser-behavior prediction made or relied on (r59 falsification lives in the C11 entry) |
| Q08 | pass | all counts/offsets carry their command; `examined_entries=8` re-derived as 2+2+1+1+1+1 table entries |
| Q09 | pass | digest cited only for the bytes it hashes; no origin/authenticity claim for the saved record |
| Q10 | pass | claims scoped to this fixture family, PE32+, static layout; cross-family behavior left unknown |

## Provenance (Q11, appended 2026-10-19)

Appended after orchestrator review; nothing above is rewritten. Each stated
value is derived by the command below, run from the lane root at `35b2e8b`
(lane HEAD `19b3174` for the corpus), with its observed output.

- fixture identity (exit 0):

  ```sh
  sha256sum corpus/fixtures/pe-r55/fixture.exe; stat -c %s corpus/fixtures/pe-r55/fixture.exe
  ```

  ```text
  41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b  corpus/fixtures/pe-r55/fixture.exe
  1536
  ```

- header-derived resource directory and .rsrc base (obs. 1) (exit 0):

  ```sh
  python3 -c "import struct;b=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();e=struct.unpack_from('<I',b,0x3c)[0];o=e+24;m=struct.unpack_from('<H',b,o)[0];d=o+(112 if m==0x20b else 96)+16;r=struct.unpack_from('<II',b,d);s=o+struct.unpack_from('<H',b,e+20)[0];print(e,b[e:e+4],hex(m),d,r,b[s:s+8].rstrip(b'\\0'),struct.unpack_from('<IIII',b,s+8))"
  ```

  ```text
  64 b'PE\x00\x00' 0x20b 216 (8192, 240) b'.rsrc' (1024, 8192, 1024, 512)
  ```

- tables, entries, string, data entries and paths (obs. 2-6) (exit 0):

  ```sh
  awk '/^```python/{f=1;next} /^```/{f=0} f' corpus/knowledge/pe-resource-directory-layout.md | python3 -
  ```

  ```text
  resource dir rva=8192 size=240 file_base=512
  dir@file512 named=0 ids=2
    e0@file528: ID=3 -> child 0x80000020
    dir@file544 named=0 ids=2
      e0@file560: ID=1 -> child 0x80000058
      dir@file600 named=0 ids=1
        e0@file616: ID=1033 -> child 0x000000a0
          data@file672: rva=8448 size=48 cp=0 res=0
      e1@file568: ID=2 -> child 0x80000070
      dir@file624 named=0 ids=1
        e0@file640: ID=1033 -> child 0x000000b0
          data@file688: rva=8512 size=48 cp=0 res=0
    e1@file536: ID=14 -> child 0x80000040
    dir@file576 named=1 ids=0
      e0@file592: STR@file736 len=5 raw=41003dd800de42002100 -> child 0x80000088
      dir@file648 named=0 ids=1
        e0@file664: ID=1033 -> child 0x000000c0
          data@file704: rva=8576 size=34 cp=0 res=0
  ```

- raw entry words at 592, 596, 620 (obs. 3) (exit 0):

  ```sh
  python3 -c "import struct;b=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();print([hex(struct.unpack_from('<I',b,o)[0]) for o in (592,596,620)])"
  ```

  ```text
  ['0x800000e0', '0x80000088', '0xa0']
  ```

- name string decode (obs. 4) (exit 0):

  ```sh
  python3 -c "import struct;b=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();n=struct.unpack_from('<H',b,736)[0];r=b[738:738+2*n];print(n,r.hex(),r.decode('utf-16-le'),2+2*n)"
  ```

  ```text
  5 41003dd800de42002100 A😀B! 12
  ```

- payload digest at file 768 (obs. 5) (exit 0):

  ```sh
  python3 -c "import hashlib;b=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();print(hashlib.sha256(b[768:816]).hexdigest())"
  ```

  ```text
  d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003
  ```

- saved-record cross-check (obs. 7) (exit 0):

  ```sh
  sha256sum corpus/live/runs/round-59/inspection.stdout.json; python3 -c "import json;d=json.load(open('corpus/live/runs/round-59/inspection.stdout.json'));r=d['normalized_result'];print(d['evidence_id'],[(x['location']['offset'],x['named_entries'],x['id_entries']) for x in r['directories']],[x['data_entry_location']['offset'] for x in r['resources']],r['coverage'])"
  ```

  ```text
  bf7922dbda2bc2dd817eaa13652f04e19c10ed8701feab5790a8703d55f22c0f  corpus/live/runs/round-59/inspection.stdout.json
  ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db [(512, 0, 2), (544, 0, 2), (600, 0, 1), (624, 0, 1), (576, 1, 0), (648, 0, 1)] [672, 688, 704] {'status': 'complete', 'examined_entries': 8, 'resources': 3}
  ```
