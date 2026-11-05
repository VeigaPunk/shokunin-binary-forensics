# Round 92 — ScoutR92Managed: primary sources for the managed (.NET/CLI) metadata facts

Seat: `ScoutR92Managed` (scout, wave 1). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Access date for every fetch below: **2026-11-05**. Scope: read-only over the lane; nothing under
`reports/round-92/`, `corpus/SOURCES.md`, `corpus/README.md` or any other frozen file was modified.

**Task constraints honoured.** Rows are tier A only for a specification or an official document.
No community page is listed as usable. Every quote below was located in the fetched bytes and
re-verified byte-exactly (whitespace-normalised) against the saved snapshot; the command used is
reproduced per source so the L1 can re-derive it. Fetch method for every source:
`curl -sS -L --max-time <t> -o <file> -w "HTTP=%{http_code}" <url>` (HTTP status recorded below);
PDFs were then rendered with `pdftotext -layout` (poppler, already present on this host).

**Facts the lane's records actually exercise** (so the sources were chosen to match, not the other
way round):

| Fact the C1 entry needs | Where the lane exercises it |
|---|---|
| CLI header presence (`COR20`, 72 bytes at file offset 512) | `corpus/live/runs/round-85/inspect-managed-artifact/inspection.json` → `pe.cli.header_offset=512`, `header_size=72`, `flags=1` (`il-only`), `runtime_version "4.0"`; `corpus/fixtures/managed-r76/truth.json` → `cor20.cb=72`, `flags "COMIMAGE_FLAGS_ILONLY (1)"`, `data_directory_index 14`; PE re-read of `corpus/fixtures/managed-r85/fixture.dll` shows data directory 14 = RVA 0x1000, size 72 (→ file offset 512), and the CLI header field widths sum to exactly 72 bytes |
| Metadata root signature `BSJB` | `corpus/fixtures/managed-r76/truth.json` → `metadata.signature "BSJB"`; byte read of both fixtures: `BSJB` = `42 53 4a 42` at file offset 640 (little-endian read of `0x424A5342`) |
| The five stream names `#~ #Strings #US #GUID #Blob` | `round-76/inspection.json` → `metadata.stream_names`; `round-76/truth.json` → `metadata.streams`; `round-85/inspect-managed-artifact/inspection.json` → `metadata.status "complete"`, `version "v4.0.30319"` |
| Table row counts derived from the `#~` stream's `Rows` array | `round-85/inspect-managed-members/inspection.json` → `metadata.table_row_counts {Module 1, TypeDef 2, MethodDef 2, ModuleRef 1, ImplMap 1, Assembly 1}`; `round-85/inspect-managed-artifact/LEDGER.md` ("table row counts re-derived") |

---

## Usable sources (the L1 assigns **S491, S492, S493, S494** in this order)

### U1 → S491 — ECMA-335, 6th edition (CLI), Partition II §II.24.2.1 + §II.24.2.2 + §II.24.2.6 + §II.25.3.3
- **URL:** https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf
- **Fetch method / status:** `curl -sS -L --max-time 180` → **HTTP 200**, 4 982 145 bytes,
  `application/pdf`; text rendered with `pdftotext -layout`.
- **Access date:** 2026-11-05.
- **Page's own revision marker (anchor):** "6th edition, June 2012"; PDF SHA-256
  `8c1decf6d482f020776a12dd601537e024d5d5f30df130a3ea3bbf3c51adb1d6`; landing page
  https://ecma-international.org/publications-and-standards/standards/ecma-335/ (HTTP 200,
  `dateModified` `2022-01-26T09:17:16+00:00`) lists the same "6th edition, June 2012" PDF.
  Printed pages: metadata root **p. 271**, stream header **p. 272**, `#~` stream **p. 273**,
  CLI header **p. 283** (PDF page 297 / 298 / 299 / 309).
- **Section headings:** "II.24.2.1 Metadata root"; "II.24.2.2 Stream header"; "II.24.2.6 `#~`
  stream"; "II.25.3.3 CLI header"; "II.25.3.3.1 Runtime flags".
- **Quote (located, ≤25 words, one specific format fact):**
  `Magic signature for physical metadata : 0x424A5342.`
  (7 words; §II.24.2.1, "Metadata root" table, row `0 | 4 | Signature`, printed p. 271.)
  — **located: yes**
- **Fact it grounds:** the physical metadata root begins with a 4-byte magic signature whose value
  is `0x424A5342`; stored little-endian those bytes are `42 53 4A 42` = ASCII `BSJB`, which is the
  signature both lane fixtures carry at file offset 640 and which the lane's `truth.json` names.
- **Additional located quotes from the same opened document (for the other facts of the entry, all
  ≤25 words, all verified byte-exactly in the same snapshot):**
  - `Both logical tables and heaps are stored in streams. There are five possible kinds of streams.`
    (16 words; §II.24.2.2, printed p. 272) — the stream-count fact; the same paragraph names
    `#Strings`, `#US`, `#Blob`, `#GUID`, `#~`.
  - `The Rows array contains the number of rows for each of the tables that are present.`
    (16 words; §II.24.2.6, printed p. 273) — the table-row-count derivation; the same paragraph
    states that the number of 1's in `Valid` gives the number of `Rows` elements, and the `#~`
    table row states `Array of n 4-byte unsigned integers indicating the number of rows for each
    present table.`
  - `The CLI header (§II.25.3.3) is found using CLI Header directory entry in the PE header.`
    (15 words; §II.25.1, printed p. 277) — the CLI-header-presence fact; §II.25.3.3's field table
    (printed p. 283) fixes `Cb` at offset 0, `MetaData` at offset 8, `Flags` at offset 16,
    `EntryPointToken` at offset 20, and §II.25.3.3.1 fixes `COMIMAGE_FLAGS_ILONLY 0x00000001`
    ("Shall be 1") — matching the lane's `header_size 72`, `flags 1`/`il-only` and `entrypoint_token 0`.
- **Located-verification command (re-runnable):**
  `python3 -c "import re;t=re.sub(r'\s+',' ',open('snapshots/ecma335-6th-edition.txt',encoding='utf-8').read().replace(chr(8217),chr(39)));print('Magic signature for physical metadata : 0x424A5342.' in t)"`

### U2 → S492 — ECMA-335, 5th edition (CLI), Partition II §II.24.2.1 / §II.24.2.2 / §II.24.2.6
- **URL:** https://ecma-international.org/wp-content/uploads/ECMA-335_5th_edition_december_2010.pdf
- **Fetch method / status:** `curl -sS -L --max-time 240` → **HTTP 200**, 7 238 968 bytes,
  `application/pdf`; text rendered with `pdftotext -layout`.
- **Access date:** 2026-11-05.
- **Page's own revision marker (anchor):** "5th edition, December 2010"; PDF SHA-256
  `f51034d1feb3de7026c1e4710f2330ac7de346d09c97b340a092a694fa71dfd4`; the ECMA-335 landing page
  (same URL as above, HTTP 200, `dateModified` 2022-01-26) lists the 5th edition under
  "5th edition, December 2010". Section numbering in this edition prints as "24.2.1" / "24.2.6"
  (no leading "II."); PDF pages 299 (metadata root), 300 (stream header), 301 (`#~` stream).
- **Section headings:** "24 Metadata physical layout"; "24.2.2 Stream header"; "24.2.6 `#~` stream".
- **Quote (located, ≤25 words, one specific format fact):**
  `Magic signature for physical metadata : 0x424A5342.`
  (7 words; §24.2.1 metadata root table, row `0 | 4 | Signature`, PDF p. 299.)
  — **located: yes**
- **Fact it grounds:** the same magic-signature fact at the **previous (5th, December 2010) edition**,
  independently re-opened today. This is the edition-independent corroboration the entry should
  cite for the `BSJB` root signature: the value is not a 6th-edition-only reading.
- **Additional located quotes from the same opened document (≤25 words, verified byte-exactly):**
  - `Both logical tables and heaps are stored in streams. There are five possible kinds of streams.`
    (16 words; §24.2.2, PDF p. 300) — stream-count/stream-name fact at the previous edition.
  - `The Rows array contains the number of rows for each of the tables that are present.`
    (16 words; §24.2.6, PDF p. 301) — table-row-count derivation at the previous edition.
- **Why this is a separate row from U1 and not a duplicate:** it is a *different document* (5th vs
  6th edition, distinct URL, distinct PDF digest), opened and quoted on its own; the lane's existing
  row S136 covers only the **6th** edition, so this edition is not yet registered.

### U3 → S493 — PE Format (Microsoft Learn) — optional-header data directory entry 14 "CLR Runtime Header"
- **URL:** https://learn.microsoft.com/en-us/windows/win32/debug/pe-format
- **Fetch method / status:** `curl -sS -L --max-time 60` → **HTTP 200**, 281 747 bytes HTML; text
  extracted by stripping tags and collapsing whitespace.
- **Access date:** 2026-11-05.
- **Page's own revision marker (anchor):** `ms.date` `2026-09-10T00:00:00Z`;
  `git_commit_id` `55e845e9f3a6a3261f59a2f460f61edc25ffcdd5`; HTML SHA-256
  `7a3bba593caa94e39c3f2475fea58ab20d28ed03cdba2760594b92e3ed2e1d28`.
- **Section heading:** "Optional Header Data Directories (Image Only)" — data-directory table row
  `208/224 | 8 | CLR Runtime Header`.
- **Quote (located, ≤25 words, one specific format fact):**
  `208/224 8 CLR Runtime Header The CLR runtime header address and size.`
  (12 words; data-directory table, "CLR Runtime Header" row, offset 208/224, size 8.)
  — **located: yes**
- **Fact it grounds:** in a PE32/PE32+ image the **15th** optional-header data-directory entry
  (index 14 counting from 0, i.e. `NumberOfRvaAndSizes` entry 14) is the CLR Runtime Header, whose
  RVA+size locate the CLI header. The lane's `corpus/fixtures/managed-r76/truth.json` records exactly
  this: `cor20.data_directory_index 14`; a byte re-read of `corpus/fixtures/managed-r85/fixture.dll`
  shows data directory 14 = RVA `0x1000`, size `72`, which the section table maps to file offset
  `0x200` = 512 — the `header_offset 512` in the r85 record. This row also notes the page's own
  caveat that the directory count is not fixed and `NumberOfRvaAndSizes` must be checked.
- **Duplicate note:** the lane's existing row **S009** already registers this same URL for the
  `.rsrc` section field layouts. This row is a **different scope of the same document** (the CLR
  Runtime Header data-directory entry), the same "narrower re-open" pattern the lane already uses
  for S032/S034 and S028/S029. It is a distinct S-id on a distinct scope, not a re-mine of S009.

### U4 → S494 — `System.Reflection.Metadata.Ecma335.MetadataRootBuilder` (Microsoft Learn API reference)
- **URL:** https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.ecma335.metadatarootbuilder?view=net-10.0
- **Fetch method / status:** `curl -sS -L --max-time 60` → **HTTP 200** (final URL
  `...metadatarootbuilder?view=net-10.0`; the same page without `view` resolves to
  `?view=net-11.0-pp`), 63 589 bytes HTML.
- **Access date:** 2026-11-05.
- **Page's own revision marker (anchor):** `ms.date` `2025-07-01T00:00:00Z`;
  `git_commit_id` `e50d1863acf6da5affec9b315ba2ed88d12274e3`; HTML SHA-256
  `cdbb4789255f5545b3c240d7792106f6b7f0e2a542884b2191999e2ef8a79ae2`; the page names its own
  source file `MetadataRootBuilder.cs`.
- **Section heading:** "Remarks" (class `MetadataRootBuilder`, namespace
  `System.Reflection.Metadata.Ecma335`, assembly `System.Reflection.Metadata.dll`).
- **Quote (located, ≤25 words, one specific format fact):**
  `Metadata root constitutes of a metadata header followed by metadata streams ( #~ , #Strings , #US , #Guid and #Blob ).`
  (22 words; Remarks paragraph.) — **located: yes**
- **Fact it grounds:** the **official .NET implementation's own statement of the stream set** — a
  metadata root is a header followed by the streams `#~`, `#Strings`, `#US`, `#Guid`, `#Blob` — which
  is exactly the five-name set the lane's r76/r85 records report
  (`#Blob #GUID #Strings #US #~`). It is the vendor-side corroboration of the ECMA text (U1/U2)
  for the *stream-names* fact, and it is a `docs`-kind official Microsoft page (tier A).
- **Additional located quote from the same opened document (≤25 words, verified byte-exactly):**
  `The metadata version.` (3 words; `MetadataVersion` property row) — the property whose value the
  lane's r85 record reports as `metadata.version "v4.0.30319"`.
- **Casing note for the L1:** this page spells the GUID heap `#Guid`, while ECMA-335 and the lane's
  own records spell it `#GUID`. The entry must not silently normalise the two spellings; the fact
  is the stream set, and the source's own casing is `#Guid`.

---

## The round's three quotable facts, each with its located quote

The task requires three facts, each carrying a located ≤25-word quote, the access date 2026-11-05
and a URL. Grounded on the facts the lane's records exercise:

| # | Fact | Quote (≤25 words, located) | Source | URL | Date |
|---|---|---|---|---|---|
| F1 | The physical metadata root starts with a 4-byte magic signature `0x424A5342`, i.e. ASCII `BSJB` little-endian | `Magic signature for physical metadata : 0x424A5342.` (7 w) | U1/S491 (6th ed) + U2/S492 (5th ed, same quote at the prior edition) | https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf | 2026-11-05 |
| F2 | A PE image locates its CLI header through data-directory entry 14, the "CLR Runtime Header" | `208/224 8 CLR Runtime Header The CLR runtime header address and size.` (12 w) | U3/S493 | https://learn.microsoft.com/en-us/windows/win32/debug/pe-format | 2026-11-05 |
| F3 | Metadata tables and heaps live in five named streams, and the per-table row counts come from the `#~` stream's `Rows` array | `The Rows array contains the number of rows for each of the tables that are present.` (16 w) | U1/S491 (6th ed) + U2/S492 (5th ed, same quote) | https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf | 2026-11-05 |
| F3b (backup) | The five stream names, from the vendor's own API reference | `Metadata root constitutes of a metadata header followed by metadata streams ( #~ , #Strings , #US , #Guid and #Blob ).` (22 w) | U4/S494 | https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.ecma335.metadatarootbuilder?view=net-10.0 | 2026-11-05 |

## Facts deliberately **not** claimed (the records do not exercise them)

- Portable PDB, R2R / NativeAOT, .NET runtime-specific metadata deviations, and any `.NET 5+`
  metadata extension: no lane record exercises these. The `Ecma-335-Augments.md` addendum is
  therefore **not** usable for this entry's facts (see below).
- The metadata root version string: ECMA-335 §II.24.2.1 requires `"Standard CLI 2005"`, while both
  lane fixtures and the r85 record carry `v4.0.30319`. That divergence is a `.NET`-implementation
  fact, and the only opened source that states `v4.0.30319` as a *default* is the .NET runtime
  source file (below). The entry should either scope the fact as "the version string this producer
  reported" (observation) or cite the runtime source row explicitly — it must **not** assert that
  ECMA-335 sanctions `v4.0.30319`.

## Reachable-but-not-usable (recorded so the L1 does not re-open them)

| Source | Status | Why not usable as a tier-A row for this entry |
|---|---|---|
| https://github.com/dotnet/runtime/blob/main/docs/design/specs/Ecma-335-Augments.md (raw: `raw.githubusercontent.com/dotnet/runtime/main/docs/design/specs/Ecma-335-Augments.md`) | **HTTP 200**, 69 577 bytes; blob SHA `6a929a15f286e5c0f95e92050d7eece7e819fddf`; last commit touching the file `b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4` (2026-10-18) | It **is** tier-A-shaped (official .NET runtime design spec) and was read in full, but its content (heap-size limits of 2^29, metadata merging, module initializers, covariant returns, …) is **not exercised by any lane record**: the fixtures' heaps are far below 2^29 and nothing in the r76/r85 records concerns module initializers or merging. Usable only if the entry's scope widens beyond the observed fixtures — it is not one of the entry's four facts. (Also already noted in the lane's SOURCES row S136 as "unopened — see LEADS"; this seat opened it, and the LEADS entry is now false.) |
| https://learn.microsoft.com/en-us/dotnet/standard/metadata-and-cominterop-rules | **HTTP 404** (unreachable) | Wrong document for the facts; no page exists at this URL. |
| https://learn.microsoft.com/en-us/windows/win32/debug/cormeta-.cormeta-section-object-only and https://learn.microsoft.com/en-us/windows/win32/debug/cormeta | **HTTP 404** (both) | The `.cormeta` material is an **anchor inside** the PE Format page (`#the-cormeta-section-object-only`), which is itself U3; there is no standalone page. |
| https://www.ecma-international.org/wp-content/uploads/ECMA-335-6th-edition-June-2012.pdf | **HTTP 404** | The `www.` host with hyphens does not serve the file; the working canonical URL is the underscore form on the apex host (U1). |
| https://raw.githubusercontent.com/dotnet/runtime/main/src/coreclr/md/compiler/mdimport.cpp`, `.../src/coreclr/md/compiler/mdimport.cpp` (404), `.../src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/Ecma335/MetadataReader.cs` (404) | **HTTP 404** | Paths moved in the current tree. `src/coreclr/md/compiler/mdutil.cpp`, `import.cpp`, `mdutil.h` were fetched (HTTP 200) and contain **no** `BSJB` literal — CoreCLR checks the metadata signature elsewhere, so these files ground no quote for this entry. |
| `https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.metadatareader?view=net-10.0` | **HTTP 200** (read) | Official Microsoft doc (tier A) and it does state `GetTableRowCount(MetadataReader, TableIndex) Returns the number of rows in the specified table.` (11 w, located) — a usable *alternative* row for the table-row-count fact, but it is the API surface, not the file format, so U1/U2 are the better grounding for a **format** fact. Held as a fallback, not in the S491–S494 order. |
| https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.ecma335.metadatarootbuilder?view=net-10.0 — `MetadataRootBuilder.cs` (dotnet/runtime source) | **HTTP 200**, 6 114 bytes; blob SHA `241d4132c69269ca519785d147b40f5ec2da443c`; last commit `1494723e045bf8d8734393dd5b30d38879bbf7ab` (2026-04-24) | Read in full. It carries `private const string DefaultMetadataVersionString = "v4.0.30319";` (6 w, located) — the only opened source that states the lane's observed metadata version string as the .NET default. Kind would be `code` (tier A code is allowed in this lane's registry), but it is **implementation, not format**, so it is not one of the four rows above; use it only if the entry asserts the version-string default. |
| `https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.ecma335.metadatabuilder?view=net-10.0` | **HTTP 200** (read) | Official page, but it states no metadata-root/stream/row-count format fact that is not already better grounded by U1/U2/U4. |

## Snapshots committed under this seat's wave dir (for re-derivation, not part of the entry)

`.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/`
- `ecma335-6th-edition.txt` — `pdftotext -layout` of U1; sha256 `a1b789e9851d38300fd52b68c0261f57d8cec17a9cc597a8b6ffcfeb2da032da`
- `pe-format.txt` — tag-stripped text of U3; sha256 `3d3ba5f65cbc2bd0d4f60ca8280da087f4fa5a6f39e6874a7586728ff1677b67`
- `api-metadatarootbuilder.txt` — tag-stripped text of U4; sha256 `c061503bd1e161a2d3636ff7f9918a04d0b817e2259bc354534eb28f4be006a8`
- `api-metadatareader.txt` — tag-stripped text of the fallback page; sha256 `853b06c2be622bdaeb51749f953935efd18254474c4546914149dc4ff42691d8`
- `Ecma-335-Augments.md` — the reachable-but-not-usable addendum; sha256 `1e6e225aa41cd1ccf957b3c13ec4682fc6be2265327c3632f2e8fa01279b0828`

The PDF and HTML originals remain in scratch and are re-fetchable from the URLs above; the PDFs are
5.0 MB and 7.2 MB and were left out of the lane tree deliberately.

## Re-derivation commands (what the L1 can re-run)

```
# F1 / F3 quotes, 6th edition
python3 -c "import re;t=re.sub(r'\s+',' ',open('.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/ecma335-6th-edition.txt',encoding='utf-8').read().replace(chr(8217),chr(39)));\
print('Magic signature for physical metadata : 0x424A5342.' in t);\
print('The Rows array contains the number of rows for each of the tables that are present.' in t);\
print('Both logical tables and heaps are stored in streams. There are five possible kinds of streams.' in t);\
print('The CLI header (§II.25.3.3) is found using CLI Header directory entry in the PE header.' in t)"
# F2 quote, PE Format page
python3 -c "import re;t=re.sub(r'\s+',' ',open('.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/pe-format.txt',encoding='utf-8').read());\
print('208/224 8 CLR Runtime Header The CLR runtime header address and size.' in t)"
# F3b quote, MetadataRootBuilder API page
python3 -c "import re;t=re.sub(r'\s+',' ',open('.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/api-metadatarootbuilder.txt',encoding='utf-8').read());\
print('Metadata root constitutes of a metadata header followed by metadata streams ( #~ , #Strings , #US , #Guid and #Blob ).' in t)"
# lane-side byte re-derivation of the facts the quotes ground
python3 -c "d=open('corpus/fixtures/managed-r85/fixture.dll','rb').read();i=d.find(b'BSJB');print('BSJB at',i,d[i:i+4].hex())"
python3 -c "import struct;d=open('corpus/fixtures/managed-r85/fixture.dll','rb').read();pe=struct.unpack_from('<I',d,0x3c)[0];o=pe+24+96+8*14;print('dir14 rva',hex(struct.unpack_from('<I',d,o)[0]),'size',struct.unpack_from('<I',d,o+4)[0])"
```

## Tooling

No tool was installed, upgraded or removed this round; `curl` and `pdftotext` (poppler-utils) were
already present on this host and were used as-is. The host-wide `pacman` pause was respected: no
`pacman`, `uv`, `npx` or `~/.local/bin` operation was performed.
