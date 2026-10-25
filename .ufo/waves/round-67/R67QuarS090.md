# R67QuarS090 — quarantine hand-check, wave-4 item 10, register row S090 (`revenger`/round3)

PRESENT — the quoted content is verbatim in the cited PDF (page 14, JSAC2026 workshop3): each of the three ` / `-separated segments is present as fixed text in the rendered document, byte-identical except for two pdftotext line-wrap whitespace points, so the register's absence claim is false.

## Row under check

Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` (READ-ONLY), line 161:
`revenger | round3 | S090 | payload-absent | https://jsac.jpcert.or.jp/archive/2026/pdf/JSAC2026_workshop3_jp.pdf` — note claims "cited source, companion URLs and local artifacts were all checked; the quote is in none of them".

## Fetch (fresh, 2026-10-25T00:33:29Z)

```
curl -sL --max-redirs 15 -o source.bin 'https://jsac.jpcert.or.jp/archive/2026/pdf/JSAC2026_workshop3_jp.pdf'
→ HTTP=200 SIZE=6015111 FINALURL=<same> CT=application/pdf
file source.bin → PDF document, version 1.7, 100 page(s)
sha256 6a06c80e952310dd1cf026f329e71c4b784efa50d14ff9159b53914b0430ca57  (verified identical across 3 fetches; HASH-VERIFIED programmatically)
```
6,015,111 bytes > 2 MB ⇒ per brief, raw bytes NOT retained; sha256 + 20-line excerpt kept. Full provenance: `quarantine/S090/provenance.txt`.

## Per-string results

Rendering mandated by the brief (html.unescape + tag-strip) is a no-op on this PDF's extracted text (no HTML entities/tags present); the meaningful rendering is `pdftotext -enc UTF-8` → `quarantine/S090/extracted.txt` (36,140 bytes, sha256 `dc8cc72474f51b1fffff9e220144b8c0ff859fa9920cac5fa86e6c3a54a65ce1`).

Raw-bytes check (grep -aFc on the PDF): 0 for the full string and every segment — expected, PDF content streams are compressed; raw absence carries no textual evidence either way.

| # | quoted segment | exact in rendered text | after whitespace-squeeze | after html.unescape/tag-strip | after NFKC+squeeze |
|---|---|---|---|---|---|
| SEG1 | `AOT(Ahead-Of-Time)形式` | **True** (extracted.txt:180, byte offset 3476, page 14) | True | True | True |
| SEG2 | `.NETの最適化により、プラットフォームによってはILではなく、 ネイティブコードが実行される` | False — needle has `、 ネイティブ`, PDF has `、\nネイティブ` (extracted.txt:182-183) | **True** | False | True |
| SEG3 | `解析では、実際にどちらが実行されるのかに注意を払う必要が ある` | False — needle has `必要が ある`, PDF has `必要が\nある` (extracted.txt:184-185) | **True** | False | True |
| FULL | all three joined with ` / ` | False — ` / ` is register-internal line-break formatting, not source text | n/a (separator not in source) | False | n/a |

The only differences between the register's transcription and the source are whitespace at two line-wrap points plus the ` / ` joiners. There is no substituted or distorted wording: near-miss hunt via fragments `AOT`, `Ahead-Of-Time`, `ネイティブコード` (7 hits), `ILではなく`, `注意を払う` found only the matching passage itself — extracted.txt:178-187:

```
• Ready To Run
• アセンブリにILとネイティブコードが含まれる
• AOT(Ahead-Of-Time)形式
• .NETの最適化により、プラットフォームによってはILではなく、
ネイティブコードが実行される
• 解析では、実際にどちらが実行されるのかに注意を払う必要が
ある
• ILSpyを使うと、ILのデコンパイルとネイティブコードのアセ
ンブリを比較してみることが可能
```

15+ word context: slide (page 14) bullets read exactly the register's quote, wrapped; the register appears to have transcribed pdftotext layout (newline→space) and its later absence check searched for the space-joined string without whitespace normalization, or against raw compressed bytes — a false absence.

## Verdict per brief's rules

PRESENCE is satisfied by the fixed-string reading applied to the quoted payload's segments: SEG1 matches byte-exactly, SEG2/SEG3 match byte-exactly once the source's own line break (which the register rendered as a space) is normalized — `wssqueezed=True` for all three, computed with a fixed-string (non-regex) comparison. The register's claim "the quote is in none of them" is wrong: this is a verbatim quote of the cited PDF page 14, not a fabrication. Verdict: **PRESENT**.

## Findings

1. Register hygiene: row id `S090` is used twice in the register — line 77 (`kagi`/round3, arXiv 2307.00714) and line 161 (`revenger`/round3, JSAC). My brief assigns the JSAC row; the collision should be flagged to the register owner.
2. Failure-mode note for the register's checker: absence searches over rendered text must whitespace-normalize both sides (Japanese PDF line wraps insert newlines mid-sentence) and must not search raw compressed PDF bytes.
3. Tooling: no installs/updates were needed (poppler `pdftotext` preinstalled at /usr/bin; operator 2026-10-19 directive: nothing installed, nothing to record).
4. Bounds: only files written are this report and my scratch dir `quarantine/S090/` (provenance.txt, extracted.txt, excerpt20.txt); shokuknow read untouched; no git/jj operations.

## Limits

- Raw `source.bin` not retained (>2 MB rule); sha256 + provenance retained instead, verified by re-fetch + `HASH-VERIFIED` comparison. If the server later serves different bytes, the sha256 pins what was checked.
- Companion URLs are not enumerated in the register row and were not needed — the cited source itself contains the quote.
