ABSENT — row S094 (`revenger`, round3, `payload-absent`, SWGDE 12-F-003-2.0 PDF): fetch succeeded (HTTP 200, real PDF bytes); both quoted strings are missing from raw bytes and every text rendering. Both quotes are slash/space-joined distortions of real header/TOC lines.

## Item
- Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` line 164 (`revenger` | `round3` | `S094` | `payload-absent`). (Note: an unrelated `chousa` round2 S094 row exists at line 44 — different campaign, different source.)
- Cited source: https://www.swgde.org/wp-content/uploads/2025/09/2025-07-12-Core-Competencies-for-Mobile-Device-Forensics-12-F-003-2.0.pdf

## Fetch receipt
- Command: `curl -sL --max-redirs 15 -o source.bin -w 'HTTP:%{http_code} SIZE:%{size_download}' <url>`
- Result: `HTTP:200 SIZE:290583` (first try, no retries needed)
- File: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S094/source.bin`
- sha256: `593956e1e28b30e00ab3a2195a1baa9494f072043c1ba8e095b6df24053250c1` (290,583 bytes ≤ 2 MB → full bytes saved)
- `file`: `PDF document, version 1.6 (zip deflate encoded)`; `pdfinfo` Title: "Core Competencies for Mobile Device Forensics", CreationDate 2025-07-12 → genuine target document, not an error page.

## Per-string results

### String 1: `Scientific Working Group on Digital Evidence / Core Competencies for Mobile Device Forensics / SWGDE 12-F-003-2.0 / Vers`
- `grep -c -F` on raw `source.bin`: **0**
- `bytes.find()` on raw bytes, HTML-escaped, and HTML-unescaped variants: **-1 for all three** (python3 check)
- `pdftotext -layout` rendering (`source.txt`, 27,862 bytes): **absent**
- `pdftotext` (non-layout) rendering (`source-nolayout.txt`): **0** matches
- Verdict: **ABSENT**.
- Near-miss (probable distortion source): the real cover-page header is four separate centered lines — `Scientific Working Group on` / `Digital Evidence` / `Core Competencies for Mobile Device Forensics` / `SWGDE 12-F-003-2.0` (source.txt lines 1-4) followed later by `Version: 2.0 (7/12/2025)`. The quote joins those lines with " / " and truncates "Version:" to "Vers" — a concatenation that exists in no rendering.

### String 2: `5.1 Legal Considerations and Ethical Standards 5.2 Foundational Skills 5.3 Evidence Identification 5.4 Collection, Seizu`
- `grep -c -F` on raw `source.bin`: **0**
- `bytes.find()` on raw/escaped/unescaped variants: **-1 for all three**
- `pdftotext -layout` rendering: **absent**
- `pdftotext` non-layout rendering: **0** matches
- Verdict: **ABSENT**.
- Near-miss (probable distortion source): the real Table of Contents rows carry dot leaders — `5.1      Legal Considerations and Ethical Standards ................................................ 3`, `5.2      Foundational Skills...`, `5.3      Evidence Identification...`, `5.4      Collection, Seizure, and Preservation ...` — and section bodies repeat each heading on its own line (`5.1    Legal Considerations and Ethical Standards` etc.). The quote strips the dot leaders, space-joins the four TOC entries, and truncates "Seizure" to "Seizu". No rendering contains that join.

## Component hits (sanity: the document does contain the real phrases)
- `Scientific Working Group`: 17 hits; `Core Competencies`: 13; `SWGDE`: 74; `12-F`: 10; `Version: 2.0 (7/12/2025)`: 9 (all `Vers` hits are this string)
- `Legal Considerations`: 3; `Foundational`: 3; `Evidence Identification`: 3; `Collection, Seiz` : 3 — all as separate headings/TOC rows, never in the quoted concatenated form.

## Notes
- HTML-escape/unescape variants are no-ops for these strings (no `&<>"'` characters), but all three variants were checked anyway.
- No installs performed; `pdftotext`/`pdfinfo` already present at /usr/bin (poppler). curl + python3 stdlib only.
- Register note ("cited source, companion URLs and local artifacts were all checked; the quote is in none of them") is **confirmed** for the cited source.
