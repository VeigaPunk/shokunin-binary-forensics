ABSENT — both quoted strings verified missing from the fetched document (and no ILSpy/.NET content exists in it at all); the register's `payload-absent` claim for row S095 (revenger, round3) is confirmed.

# R67QuarS095 — quarantine hand-check, wave-4 item 10

- Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:165`
  (`revenger` | round3 | S095 | `payload-absent` | https://www.ffri.jp/assets/files/research/research_papers/Embedded.pdf)
- Note: two other campaigns use id S095 (`chousa` :45, `game-dev-2d` :65); this check covers the `revenger` row only, per assignment.
- Register note under test: "cited source, companion URLs and local artifacts were all checked; the quote is in none of them".

## Fetch receipt (try 1 of ≤3 — succeeded)

```
curl -sL --max-redirs 15 -o source.bin -w ... 'https://www.ffri.jp/assets/files/research/research_papers/Embedded.pdf'
http_code=200 size=4120207 url_effective=https://www.ffri.jp/assets/files/research/research_papers/Embedded.pdf
```

- http code: 200 · bytes: 4,120,207 (>2MB → source.bin deleted per brief; retained sha256 + excerpt)
- sha256: `32318d4eb22bd979ae3e3055d64f9020eb33a1ce4c9f3940a6cccf9deab753b3`
- `file`: PDF document, version 1.6 (zip deflate encoded)
- Real document bytes: yes — it is a Japanese slide deck, "組み込みシステムのセキュリティ" (Embedded Systems Security), Fourteenforty Research Institute / 株式会社フォティーンフォティー技術研究所, 鵜飼裕司.
- Excerpt: `.ufo/waves/round-67/quarantine/S095/excerpt-20lines.txt`; extracted text (pdftotext -layout, 92,109 bytes): `.ufo/waves/round-67/quarantine/S095/source.txt`

## Per-string results

1. `ILSpy is the open-source, cross-platform .NET assembly browser and decompiler.` — **ABSENT**
   - raw bytes `grep -F`: 0 (also on `&#44;`-escaped variant: 0)
   - pdftotext -layout extraction `grep -F`: 0
   - python `html.unescape` rendering `in`: False
   - 208 zlib-decompressed PDF streams (22,193,214 bytes) `count`: 0
   - Near-miss: none — `ILSpy` alone is also 0 everywhere; no .NET/decompiler-family text exists in the document.
2. `Privacy Policy for ILSpy` — **ABSENT**
   - raw bytes `grep -F`: 0 · pdftotext `grep -F`: 0 · unescaped `in`: False · decompressed streams `count`: 0
   - Near-miss: none — `Privacy Policy` alone is 0 in the extracted text.

## Near-miss / fabrication-family finding

The document's only decompiler-adjacent content is **IDA**, not ILSpy — firmware reverse-engineering slides, e.g. `source.txt:709` (`ida`) and `source.txt:1739` (`・ファームウエアを吸出し、IDAなどで解析` = "dump firmware and analyze with IDA etc."). Additional absence anchors: `decompiler`, `.NET assembly browser`, `assembly browser`, `open-source`, `Privacy Policy` — all 0. The quoted sentences are the stock ILSpy tagline ("ILSpy is the open-source .NET assembly browser and decompiler") and an ILSpy privacy-policy page heading — i.e., the fabricated payload is pasted ILSpy boilerplate that has no counterpart in this source at all. Fabrication-class confirmation of the register's absence claim stands.

## Tooling record

- `curl` 200 fetch; `pdftotext` (/usr/bin/pdftotext, poppler) for text extraction; `sha256sum`, `grep -F`, python3 zlib/html for stream decompression and escaping variants. No installs needed; no pacman transactions.

## Unknowns

- None for the assigned row: fetch succeeded first try, both strings absent under every rendering checked.
