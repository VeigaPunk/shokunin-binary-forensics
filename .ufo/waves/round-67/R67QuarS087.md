# R67QuarS087 — quarantine hand-check, register row S087

ABSENT — fetch succeeded (genuine ECMA-335 6th-edition PDF, HTTP 200, sha256 8c1decf6d482f020776a12dd601537e024d5d5f30df130a3ea3bbf3c51adb1d6) and the quoted string is missing from raw bytes, html-unescape+tag-stripped rendering, and extracted text; fabrication-class confirmation.

## Row checked (READ-ONLY source, untouched)

`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` line 159:

`|| revenger | round3 | S087 | payload-absent | https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf | `Ildasm.exe (IL 逆アセンブラー) - .NET Framework` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |`

Campaign round round3, class payload-absent, one quoted string to check.

## Fetch (2026-10-24)

Command: `curl -sL --max-redirs 15 -o /tmp/revenger-r67-quar-S087/source.bin https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf`

- Result line: `HTTP:200 SIZE:4982145 FINAL:https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf`
- sha256: `8c1decf6d482f020776a12dd601537e024d5d5f30df130a3ea3bbf3c51adb1d6`
- Size: 4,982,145 bytes → > 2 MB, so full bytes NOT saved to scratch `source.bin` per brief; working copy held at `/tmp/revenger-r67-quar-S087/source.bin`.
- `file(1)`: `PDF document, version 1.6, header %PDF-1.6`
- `pdfinfo`: Title `ECMA-335, 6th edition, June 2012`, Author `ECMA`, Pages `574`, CreationDate `2012-06-29`, ModDate `2022-02-18` — genuine cited document bytes, first try, no retries needed.

## String check 1/1 — `Ildasm.exe (IL 逆アセンブラー) - .NET Framework`

- Raw fixed-string grep: `grep -aobF 'Ildasm.exe (IL 逆アセンブラー) - .NET Framework'` → no match (MISSING in raw bytes).
- Raw encodings (python): utf-8 count=0, utf-16-le count=0, utf-16-be count=0.
- html.unescape + tag-stripped rendering of fetched bytes: full string count=0.
- Corroborating fragment searches, all zero:
  - `Ildasm` in raw bytes: 0 (grep -aobF, case-sensitive).
  - `Ildasm` / `ildasm` any case in `pdftotext -layout` extraction (25,815 lines): 0 / 0.
  - `.NET Framework` in raw bytes: 0; in extracted text: 0 (`Framework` alone appears 11×, never with the `.NET` prefix).
  - `逆アセンブラー`: 0; CJK-range characters in the entire extracted text: 0 (document contains no Japanese text at all).
  - case-insensitive `disassembl*`: 0 hits.

Every verdict-rule channel negative on real document bytes → ABSENT.

## Near-miss named

- The document does cover the companion tool by acronym: `ILAsm` appears 46× in extracted text (e.g. source.txt:6205-6206: "the ILAsm assembly language. In addition, Partition VI contains a longer example of a program written in the ILAsm assembly language."), but ildasm/the disassembler and ".NET Framework" never appear.
- The quoted string's exact shape — `<tool>.exe (<Japanese tool gloss>) - .NET Framework` — matches the title convention of Microsoft's ja-JP .NET Framework tools documentation (the Ildasm.exe article), not of any ECMA standard text. [INFERENCE] — companion URL not fetched; network use was restricted to the assigned URL per seat bounds.

## Register note cross-check

Register note claims cited source, companion URLs and local artifacts all lack the quote. My independent re-derivation for the cited source agrees: absence confirmed on today's bytes. Companion URLs and local artifacts were not re-checked (out of my scope; note recorded verbatim above).

## Artifacts

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S087/fetch-record.txt` — fetch provenance (command, HTTP code, size, sha256, pdfinfo summary).
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S087/excerpt-hex-20.txt` — 20-line hexdump of the first 320 bytes.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S087/excerpt-text-20.txt` — first 20 lines of pdftotext output.
- Working copy of the 4.9 MB source and extracted text: `/tmp/revenger-r67-quar-S087/` (volatile).

## Tooling / limits

- No tool installs or upgrades performed (preinstalled: curl, grep, poppler pdftotext/pdfinfo, python 3.14.8).
- Primary gate is fixed-string search on fetched bytes as prescribed; pdftotext extraction and CJK census are corroboration (absence in extraction is consistent with, and here redundant to, the raw-byte absence — even the pure-ASCII fragment `Ildasm.exe` has zero raw-byte occurrences, which no font encoding could mask).
- No writes outside my report file and the named scratch subdir; register and all of /home/vgpnk/Projects/shokuknow untouched; no git/jj commands run.
