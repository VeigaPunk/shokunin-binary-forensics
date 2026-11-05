# ScoutR92Quarantine — quarantine verdicts, revenger slice of the absent-defect register

Round 92, wave 1, lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Date 2026-11-05.
**Verdict-only: nothing adopted this round.**

## Outputs

- `.ufo/waves/round-92/w1/ScoutR92Quarantine/verdicts.tsv` — 26 data lines, 8 columns
  (`row_no, s_id, cited_url, fetch_status, located, location, verdict, note`), one per slice row.
- `.ufo/waves/round-92/w1/ScoutR92Quarantine/summary.md` — counts per verdict, the exact
  `slice.raw` command, method, and the two register defects.
- `.ufo/waves/round-92/w1/ScoutR92Quarantine/slice.raw` — the extracted slice, for re-derivation.

## Slice

`awk -F'|' -v l='revenger' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $0}' <register> > slice.raw`
→ **26 rows**, matching the expected count. 24 `payload-absent` + 2 prose-class rows.

## Key numbers

| verdict | rows |
|---|---|
| `candidate-present` | **24** |
| `refuse-absent` | **0** |
| `unverifiable` | **2** (S054, S099 — prose class, no quoted span) |

Fetch status of each row's cited URL: 25 × HTTP 200, 1 × HTTP 404 (S085).
Located: 24 yes, 2 no (the two prose rows carry no span).

**Zero fabrications.** Every quoted span in the slice was located verbatim in a fetched
document — in the row's own cited URL, in its true SOURCES neighbour's URL, or, for three
reconstructed spans, in the fact the span itself names.

## The defect: the register's cited-URL column is off by one row

The upstream census (`quote-lint-full-v5.json`, `verdict: ABSENT`, `binding: id`) bound each
quoted span to the S-id of the **following** SOURCES row. So in 14 of the 24 `payload-absent`
rows the span is absent from the row's own cited URL yet present verbatim in the document the
row's own SOURCES line names. The two prose rows are the same defect from the other side:
S054's URL (dex-format) holds S053's spans; S099's URL (apkanalyzer) holds S098's spans.

Pairs (register row → true source): S053→source.android.com dex-format · S058→lac.co.jp ·
S060→bbs.kanxue · S061→arXiv 2412.11539 · S062→arXiv 2112.02606 · S075→rea-agents
javascript-recovery.md · S081→RFC 6238 · S083→SWGDE 18-F-002-2.0 · S085→SWGDE 18-F-003-2.0 ·
S087→learn.microsoft ildasm · S089→JSAC2026 PDF · S092→NJU PDF · S095→ILSpy README ·
S098→developer.android.com apkanalyzer.

**S085's cited URL is truncated at 140 chars** and 404s. Unreachable ≠ fabrication: the true
source (SWGDE 18-F-003-2.0, the S086 row's URL) was resolved and both spans located verbatim.
Recorded `fetch_status=404`, `verdict=candidate-present`.

## Reconstructed spans (fact located, span defective)

- **S062** — register stores `cell):`, a truncation of its own locator line
  `(location: Appendix Table A1, "IDA" row, "Extracted features" cell)`. The cited span
  `disassembly, code analysis, data structure views, dependency graphs` is verbatim in the
  row's cited URL (arXiv 2412.11539v1 HTML, Table A1).
- **S093** — register reads `中图分类号`; the cited NJU PDF reads `中图法分类号` (one character
  dropped). `TP311` and `DOI 号 10.19363/J.cnki.cn10-1380/tn.2021.05.09` are verbatim.
- **S094** — register re-joins the section-5 contents list after stripping dot leaders and
  page numbers; every heading is verbatim in the cited SWGDE 12-F-003-2.0 PDF.

## Method

Fetch with `curl -sSL --max-time 60` into the seat scratch dir; each document rendered into a
searchable corpus (raw bytes, tag-stripped text, `pdftotext` `-layout`/`-raw`/flow), HTTP
response headers kept separately (the `Content-Disposition` filename is a header, not body).
Matching: NFKC, whitespace-insensitive, register backslash-escapes unescaped; for spans the
register stored as several source lines joined by ` / `, every fragment must be present. No
verdict was upgraded on a reconstruction without the underlying fact being located verbatim.

The register was **not modified**; it was opened read-only. No file was written outside this
seat's wave dir. Scratch (`$HYAKU_SCRATCH/revenger-r92/ScoutR92Quarantine/`) was removed on exit.

## Tooling

Nothing installed or upgraded — `curl`, `pdftotext`, `python3` 3.14.8, `jq`, `awk`, `grep`
were already present.

## Defects to route

1. **Register pairing bug (14 rows)** — `absent-defect-register.py` / `quote-lint.py` bind a
   quoted span to the neighbouring row's id and URL. The register's "cited source" column
   cannot be trusted as the source of the span in the same row.
2. **S085 URL truncated at 140 chars** — the register stores a truncated URL, which 404s and
   reads as "checked and absent".
