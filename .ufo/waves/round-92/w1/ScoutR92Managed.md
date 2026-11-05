# ScoutR92Managed — round 92, wave 1 seat report

**Output:** `.ufo/waves/round-92/w1/ScoutR92Managed/sources.md`
**Snapshots:** `.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/` (5 files, sha256 listed in sources.md)
**Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin` — read-only; nothing under
`reports/round-92/`, `corpus/SOURCES.md` or any frozen file was touched.

## Four usable tier-A sources, in the S491–S494 order the L1 will use

| id | source | kind | status | the one located quote (≤25 words) |
|---|---|---|---|---|
| S491 | ECMA-335 **6th ed** (June 2012) PDF, ecma-international.org | spec | HTTP 200, 4 982 145 B | `Magic signature for physical metadata : 0x424A5342.` (7 w) — §II.24.2.1, printed p. 271 |
| S492 | ECMA-335 **5th ed** (Dec 2010) PDF, ecma-international.org | spec | HTTP 200, 7 238 968 B | `Magic signature for physical metadata : 0x424A5342.` (7 w) — §24.2.1, PDF p. 299 |
| S493 | PE Format, learn.microsoft.com | spec | HTTP 200, 281 747 B | `208/224 8 CLR Runtime Header The CLR runtime header address and size.` (12 w) — data-directory table row, offset 208/224 |
| S494 | `System.Reflection.Metadata.Ecma335.MetadataRootBuilder`, learn.microsoft.com | docs | HTTP 200, 63 589 B | `Metadata root constitutes of a metadata header followed by metadata streams ( #~ , #Strings , #US , #Guid and #Blob ).` (22 w) — Remarks |

No community page is listed as usable. Every quote was re-verified **byte-exactly** (whitespace-
normalised) against the saved snapshot; the five re-derivation commands published in sources.md were
run and all returned `True`/the expected bytes.

## The round's three quotable facts, each with a located quote, the date and a URL

1. **F1 metadata-root magic** `0x424A5342` = ASCII `BSJB` little-endian — quote from S491, corroborated
   by the same quote at the prior edition (S492). URL: `.../ECMA-335_6th_edition_june_2012.pdf`. Date 2026-11-05.
2. **F2 CLI header location** — PE data-directory entry 14 "CLR Runtime Header" — quote from S493.
   URL: `https://learn.microsoft.com/en-us/windows/win32/debug/pe-format`. Date 2026-11-05.
3. **F3 table row counts** from the `#~` stream's `Rows` array —
   `The Rows array contains the number of rows for each of the tables that are present.` (16 w) —
   S491, same quote in S492. Backup row: S494's five-stream quote for the stream-name half of F3.

## Lane-side byte re-derivation (facts the quotes actually ground)

- Both fixtures carry `BSJB` = `42 53 4a 42` at file offset **640**; `round-76/truth.json`
  `metadata.signature "BSJB"` and the r85/r76 records' `metadata.version "v4.0.30319"` agree.
- `corpus/fixtures/managed-r85/fixture.dll`: PE data directory **14** = RVA `0x1000`, size **72**;
  section `.text` maps that RVA to file offset **512** — exactly the `pe.cli.header_offset 512`,
  `header_size 72` in `round-85/inspect-managed-artifact/inspection.json`, and `cor20.data_directory_index 14`
  in `managed-r76/truth.json`. The ECMA §II.25.3.3 field widths (4+2+2+8+4+4+8×5) sum to **72** = `Cb`.
- `round-85/inspect-managed-members/inspection.json` `metadata.table_row_counts {Module 1, TypeDef 2,
  MethodDef 2, ModuleRef 1, ImplMap 1, Assembly 1}` is the observation F3's `Rows`-array rule derives.

## Defects / cautions for the L1 (three, all actionable)

1. **Version-string divergence.** ECMA-335 §II.24.2.1 requires the root version string
   `"Standard CLI 2005"`; both lane fixtures and the r85 record carry **`v4.0.30319`**. The entry must
   not assert ECMA sanctions `v4.0.30319` — either scope it as "the version string this producer
   reported" (observation) or cite the .NET runtime source row explicitly. Only the opened
   `MetadataRootBuilder.cs` (`private const string DefaultMetadataVersionString = "v4.0.30319";`)
   states it as the .NET default, and that is implementation, not format.
2. **Casing.** S494 spells the GUID heap `#Guid`; ECMA-335 and the lane records spell it `#GUID`.
   The fact is the stream set; do not silently normalise the two spellings.
3. **Duplicate risk, and a stale LEADS pointer.** The lane already has **S136** (ECMA-335 6th ed,
   opened 2026-10-29) and **S009** (PE Format, opened 2026-10-19, scoped to `.rsrc`). S491/S493 must
   therefore be written as *narrower re-opens with distinct scopes* (the pattern S032/S034 and
   S028/S029 already use), or the append will read as a re-mine. Separately, **S136's own scope cell
   says the .NET `Ecma-335-Augments.md` addendum is "unopened — see LEADS"** — this seat opened it
   (HTTP 200, blob `6a929a15f286e5c0f95e92050d7eece7e819fddf`, last commit
   `b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4`, 2026-10-18), so that LEADS entry is now false and
   needs updating. The addendum's content (heap-size limits of 2^29, metadata merging, module
   initializers) is **not exercised** by any lane record, so it is deliberately **not** one of the
   four rows.

## Unreachable / screened destinations (so the L1 does not re-open them)

- `learn.microsoft.com/en-us/dotnet/standard/metadata-and-cominterop-rules` — **HTTP 404**.
- `learn.microsoft.com/en-us/windows/win32/debug/cormeta` and `.../cormeta-.cormeta-section-object-only`
  — **HTTP 404**; the `.cormeta` text is an *anchor inside* the PE Format page (S493).
- `www.ecma-international.org/wp-content/uploads/ECMA-335-6th-edition-June-2012.pdf` — **HTTP 404**;
  the canonical URL is the underscore form on the apex host (S491).
- `dotnet/runtime` `mdimport.cpp` / `MetadataReader.cs` paths — **HTTP 404** (moved);
  `mdutil.cpp`, `import.cpp`, `mdutil.h` fetched (200) contain **no** `BSJB` literal.
- `MetadataReader` API page (HTTP 200) holds `GetTableRowCount(MetadataReader, TableIndex) Returns the
  number of rows in the specified table.` — a usable fallback for F3, but it is API surface rather
  than file format, so S491/S492 are the better grounding; held, not in the S491–S494 order.

## Tooling

No install, upgrade or removal; `curl` and `pdftotext` (poppler-utils) were already present and used
as-is. The host `pacman` pause was respected (no `pacman`/`uv`/`npx`/`~/.local/bin` operation).
Scratch was removed on exit.
