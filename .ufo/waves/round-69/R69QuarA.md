FAIL — the register's `payload-absent` (fabrication-class) label does not survive hand-check: 7/9 rows are correctly "not in the cited source", but 7/7 of those rows carry a locatable payload elsewhere (5 fully, 2 with one untraceable fragment each), and S055's quote IS verbatim in its own cited source (register wrong).

Seat: `L1Revenger69.R69QuarA` · wave-4 quarantine hand-check · read-only campaign tree · adoption stays closed.
Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
sha256 `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833` · 375 lines.
Rows read at `:147-154` (payload-absent block) and `:359` (S054, unreachable block). Lane slice `revenger` = 24 rows (line 237); assigned 9: S053 S054 S055 S058 S060 S061 S062 S063 S064.

## Verdict per row

```
S053 ABSENT       Dalvik executable format: 0 hits in the api.github.com release JSON (14,981 B), 0 in the release HTML page; quote is verbatim 5x in S054's cited source (archived dex-format doc)
S054 UNREACHABLE  https://source.android.com/docs/core/runtime/dex-format: 302 into an OAuth loop (oauth2callback, error=interaction_required), curl max-redirs 15 exhausted; no body, no quote in register to test
S055 PRESENT      register quote "…written in multiple high-level l" is verbatim at raw offset 2336 (also 2802, 3785) in the cited page's meta/og/twitter description — register is wrong
S058 ABSENT       all three Japanese headings 0 hits in https://rea.tools/ja/ (61,099 B) and in its sitemap + /ja/blog; all three verbatim on the LAC WATCH article instead
S060 ABSENT       "[原创]安卓逆向的核心流程" 0 hits in the crifan jadx chapter page; verbatim 6x in bbs.kanxue.com/thread-288487.htm (S061's cited source)
S061 ABSENT       q1 "非营利性质的技术交流平台" PRESENT at raw 665 (og:description); q2 paper title and q3 section title 0 hits in kanxue, both 54x / 4x in arXiv 2412.11539v1 (S062's cited source)
S062 ABSENT       0/3: "cell):" nowhere; "On Impact of Semantically Similar Apps in Android" 0 hits, 11x in arXiv 2112.02606v1 (S063's source); "In our experiments" 0 hits in the HTML, verbatim in 2112.02606 PDF
S063 ABSENT       all three 0 hits on the /abs/ page; q2 and q3 verbatim in the paper PDF of the same id (q3 only with ‘dex’ curly quotes vs register's `dex')
S064 ABSENT       both 0 hits on the /abs/ abstract page; both verbatim in the paper PDF of the same id (flat offsets 19730, 28292)
```

Tally (assigned rows): **PRESENT 1 · ABSENT 7 · UNREACHABLE 1 · UNVERIFIED-REACHABLE 0 = 9.**

## Method

For each row: `curl -sSL --max-redirs 15` (read-only, UA set), bytes saved per `<S-id>/raw.bin`. Renderings searched per file: raw UTF-8; HTML-stripped text (script/style/comments dropped, tags→space, entities unescaped); whitespace-flattened text; and for the GitHub JSON, every decoded string value. Crossref: `pdftotext` renderings of the same-id PDFs, plus the same-lane neighbouring rows' fetched bytes. Exact offsets below are byte offsets in the cited source's raw bytes unless marked `flat`.

Reproducible hashes (sha256, fetched 2026-10-25):

| file | sha256 |
|---|---|
| S053/raw.bin | `ab45144f923459734d6769af2a888bd87daaf3365edc0bb2993b459eb46780af` |
| S055/raw.bin | `ff5aac3e441100c6a60fae539f00a75190b9309c57a7c9c5db6e16ff1a147c5e` |
| S058/raw.bin | `087f7abe400d55707c7af918110d191a677430b3b251688efee1755e0fde61c2` |
| S060/raw.bin | `a481c3699ceb5b280e6c7d80c39b3266de194f5906f1e548d14e55c18126841e` |
| S061/raw.bin | `3dc5d9e24c3d2dda17d90a6d68b883725f4500bf3bc140e9cac9d219621b8208` |
| S062/raw.bin | `c353587e00a6652d35a89ad1ec1f895cf6fa372661d53ff07da6153693a13189` |
| S063/raw.bin | `e10ccee211c9a9b173a1a19e1e7f6d86ac193ff2dc26587c41a286fb6cd8afa2` |
| S064/raw.bin | `e544ec87debc586cf000e0dbb05ec749b3ab0b911506fbee7b3ed5ba151feb7a` |
| S058/lac.html (LAC WATCH) | `ccf91cf9e9ac4a41ef133009db7c74aeeaa0ec406a241b2f1e28c4a2ff9b1751` |
| S053/wayback_dex.html | `4696e1aa2c88e328e49d3ae4391d9f0a7c35d54301f3ed90bba4d4a435c0caf4` |
| S063/paper.txt (pdftotext 2112.02606v1) | `ceb7d80218919ef2aab9d771c22a64f361ad591992daa1acc1b946bffc883f63` |
| S064/paper.txt (pdftotext 2510.14344) | `027253686465cb681d304aa6c748bd8420950561202f696473724d385099f142` |
| S062/paper.txt (pdftotext 2412.11539v1) | `d8dadad4daccb72062dfa853e1dadc700552239caddb1219596b87c33cec1f60` |

## Row evidence

### S053 — ABSENT (partially traceable)
- `https://api.github.com/repos/skylot/jadx/releases/tags/v1.5.6` → 200, 14,981 B, `{"name":"1.5.6","tag_name":"v1.5.6", created_at 2026-07-10T18:57:10Z, updated_at/published_at 2026-07-10T19:07:35Z}`.
- `Dalvik executable format`: **0** in raw JSON, 0 in every JSON string value, 0 in the release HTML page (`releases/tag/v1.5.6`, 249,382 B), 0 in the repo README (`Dalvik bytecode to Java code` at README offset 1326 — different phrase). Repo API description is `Dex to Java decompiler`, not this string.
- Provenance: the same string is verbatim **5x** (raw) in the archived `source.android.com/docs/core/runtime/dex-format` page (`web.archive.org/web/2026/...`, 481,188 B; title `Dalvik executable format | Android Open Source Project`; flat offsets 1, 15387, 21382). That document is **S054's cited source** — i.e. the quote set belongs to the neighbouring row.
- `Last updated 2026-10-09 UTC`: **0 hits anywhere fetched.** That page's footer reads `Last updated 2025-10-03 UTC` (two occurrences). Date is not corroborated by any byte I hold → the single untraceable fragment of this row.

### S054 — UNREACHABLE
- `curl -sSL --max-redirs 15 https://source.android.com/docs/core/runtime/dex-format` → `302`, chain ends at `https://source.android.com/oauth2callback?state=…&error_subtype=access_denied&error=interaction_required`, then `curl: (47) Maximum (15) redirects followed`. No body written, 0 bytes.
- Register row (line 359) lists the URL only, no quotes: there is no payload to test. Fetch failure is an access gate, **not** evidence of fabrication. The Wayback mirror *is* retrievable (`wayback_dex.html`, 200/481,188 B) and contains the S053 quotes; that mirror is why S053's payload is traceable.
- Register says "the cited source could not be fetched" — confirmed true for a plain non-interactive fetch.

### S055 — PRESENT (register wrong)
- `https://www.ecma-international.org/publications-and-standards/standards/ecma-335/` → 200, 90,253 B.
- Register's span (truncated mid-word at `…multiple high-level l`) found verbatim at **raw offsets 2336, 2802, 3785**. Offset 2336 context: `<meta name="description" content="Common Language Infrastructure (CLI) - Defines the infrastructure in which applications written in multiple high-level languages can be executed" />`; the full sentence continues `languages can be executed`. Same string repeats in the og/twitter description metas.
- Cause of the false row: the string lives only in `<meta>` attributes, so the checker's body-text fold (which drops tag interiors) could not see it. `html_text`/`flat` counts are 0, raw count 3 — a rendering-coverage defect in the census, not a source defect.

### S058 — ABSENT (real payload, wrong site)
- `https://rea.tools/ja/` → 200, 61,099 B, Japanese landing page (`REA-コーディングエージェントのリバースエンジニアリング`).
- All three headings: **0 hits** in raw, stripped text, flattened text. Also 0 in `https://rea.tools/sitemap.xml` (26,123 B) and `https://rea.tools/ja/blog` (15,418 B). `ファームウェア` and `IoT` are absent from the entire Japanese page.
- All three are verbatim on a different site: LAC WATCH `https://www.lac.co.jp/lacwatch/service/20230523_003378.html` → 200, 52,640 B, `<title>IoTセキュリティ検証でなぜファームウェア解析調査が必要なのか、8年の実績から見えたこと | LAC WATCH</title>`; counts raw 3 / 2 / 2, flat offsets 1/812, 1276/3001, 1230/2374. So the row's `cited source` cell is plain wrong, the payload is not invented.

### S060 — ABSENT (payload belongs to S061's source)
- `https://book.crifan.org/books/android_re_static_analysis/website/related_items/decompile/tools/jadx/` → 200, 57,634 B; page is the book's chapter TOC (`jadx · Android逆向：静态分析`).
- `[原创]安卓逆向的核心流程`: **0 hits**; `原创` 0, `核心流程` 0, `逆向的核心` 0.
- Verbatim **6x** (raw; flat offsets 1, 179, 220) inside `https://bbs.kanxue.com/thread-288487.htm` — the `S061` cited source (`<meta name="keywords" content="[原创]安卓逆向的核心流程" />`). Row is a one-row attribution shift, not fabrication.

### S061 — ABSENT (mixed 1/3 present in own source, 2/3 belong to S062's source)
- `https://bbs.kanxue.com/thread-288487.htm` → 200, 827,849 B (sha `3dc5d9e2…`; size varies ±100 B between fetches — live ads).
- q1 `非营利性质的技术交流平台`: **raw offset 665**, inside `og:description` — `看雪安全社区是一个非营利性质的技术交流平台，致力于汇聚全球的安全研究者和开发者…`. Verbatim PRESENT (flat count 0 only because the fold drops attribute text). Note `og:title` nearby carries the different string `非营利性质的安全技术交流平台` (offset 595), so the register's shorter span is the description, not the title.
- q2 `Android App Feature Extraction: A review of approaches for malware and app similarity detection`: **0 hits** in kanxue; verbatim **54x** (raw) in `arxiv.org/html/2412.11539v1` = S062's cited source.
- q3 `APK Decompiler and APK Analysis Tools`: **0 hits** in kanxue; verbatim **4x** (flat offsets 582, 27289, 27393, 32491) in 2412.11539v1 (TOC entry and §2.3.1 heading).
- Row claim "the quote is in none of them" is false for q1 and misattributed for q2/q3.

### S062 — ABSENT (0/3; two traceable, one untraceable artifact)
- `https://arxiv.org/html/2412.11539v1` → 200, 446,522 B, title `Android App Feature Extraction: A review of approaches for malware and app similarity detection` (matches S061's q2 — confirming the shift).
- `cell):`: **0 hits** in raw HTML, stripped text, and its own PDF text (`arxiv.org/pdf/2412.11539v1`, 135,564 chars). Also 0 in the 2112.02606 and 2510.14344 PDFs. Only `cell` occurrence in the text is `bankmycell.com`. This is the row's untraceable fragment (looks like a PDF-table extraction fragment, not prose).
- `On Impact of Semantically Similar Apps in Android`: **0 hits** in the 446 KB HTML, 0 in its PDF; verbatim **11x** (raw; flat offsets 16, 287, 411, 2422) in `arxiv.org/abs/2112.02606v1` = S063's cited source (paper title).
- `In our experiments`: **0 hits** in the HTML (`experiments` = 0 in 146,082 flat chars; no `In our`), 0 in its own PDF; verbatim at **flat offset 28463** in the 2112.02606v1 PDF text.

### S063 — ABSENT as cited, but payload in the same id's PDF
- `https://arxiv.org/abs/2112.02606v1` → 200, 41,461 B, abstract page, title `On Impact of Semantically Similar Apps in Android Malware Datasets`.
- All three quotes: **0 hits** in the abstract page (raw and stripped).
- Same id's PDF (`arxiv.org/pdf/2112.02606v1`, 1,180,624 B → 38,415 chars text):
  - `In our experiments` flat offset **28463**; full span `In our experiments, the decompilation errors has occurred in some applications.` flat offset **28463** (the pdftotext render gates underscores as spaces: `P ERFORMANCE IN H OLDOUT`).
  - `Reverse engineering tools such as apktool can be used to extract opcode sequences from the ` flat offset **13182**, and with the paper's own curly quotes `opcode sequences from the ‘dex’ file` present at flat **13247** (49 characters after the register's backtick-apostrophe form). Register writes `` `dex' `` — a typographic fold the eleven-fold checker evidently did not apply.
- Reading: citation-granularity artifact (`/abs/` URL, body quote), not fabrication.

### S064 — ABSENT as cited, but payload in the same id's PDF
- `https://arxiv.org/abs/2510.14344` → 200, 41,372 B, abstract page, title `BinCtx: Multi-Modal Representation Learning for Robust Android App Behavior Detection`; abstract is about the three views and does not carry either quote.
- Same id's PDF (`arxiv.org/pdf/2510.14344`, 624,458 B → 50,912 chars):
  - `our analysis revealed that over 87% of benign apps and 96% of malicious/undesired apps employ obfuscation` flat offset **19730** (raw 0 due to PDF line-break hyphenation `state-ofthe-art` neighbourhood).
  - `XML features are susceptible to manifest manipulation` **raw 1 / flat 1** at flat offset **28292** (preceded by `D EEP R EFINER’s` small-caps rendering; register's leading `… ` ellipsis is its own marker, the quoted span itself is verbatim).

## Calibration findings (the load-bearing part)

1. **The `payload-absent` class over-claims.** Its definition says every relevant source was checked and the quote is in none. For these 9 rows, only 2 quoted fragments are genuinely untraceable (S053 `Last updated 2026-10-09 UTC`; S062 `cell):`, both apparently render artifacts, not prose). Every other quoted span is a literal substring of some fetched page.
2. **Attribution shift of one row, round-1 block.** Quote sets sit on the *next* row's source: S053→dex-format doc (S054's URL), S060→kanxue 288487 (S061's URL), S061 q2/q3→arXiv 2412.11539 (S062's URL), S062 q2/q3→arXiv 2112.02606 (S063's URL). S055 breaks the pattern by being present in its own source. This is the dominant mechanism, and it means the register's "cited source … all checked" statement is a *within-row* check that cannot see a shifted payload.
3. **URL granularity.** S063 and S064 cite `/abs/` pages while quoting body text; both quotes exist verbatim in `/pdf/` of the same arXiv id. Any quote census keyed on the webpage of an `/abs/` URL will systematically manufacture fabrication-class rows from real body quotes. Fold needed: same-id PDF, and typographic folding of `` ` ``, `‘ ’`, `“ ”`.
4. **Meta-attribute blindness.** S055 shows the checker's text rendering drops `<meta content="…">`: 3 raw occurrences, 0 after stripping. `og:`/`twitter:`/`keywords`/`description` attributes are a routine carrier of the exact phrase a lane quotes, so rows built on them will always read ABSENT. `og:description` is also where S061's q1 lives (offset 665) and where S060's/S053's would live if correctly attributed.
5. **Auth gates masquerade as unreachable.** S054 is a `302` OAuth loop (`error=interaction_required`), which the register correctly filed as unreachable — but the same document is fetchable from Wayback, so "unreachable" ≠ "unverifiable". S053's payload only became visible through that mirror.
6. **Zero fabrication-class confirmations among 9 assigned rows.** No row is shown to contain invented prose. Two rows contain one untraceable fragment each; the correct remediation is "re-point the citation / re-quote", not "refuse the row".

## Scope / discipline notes

- Nothing in `/home/vgpnk/Projects/shokuknow` was written; the register and campaign tree were read only.
- No mutating git/jj operation anywhere; only `curl` GETs, `sha256sum`, `pdftotext`, Python stdlib.
- No package installs or upgrades (host pacman transactions paused). Tools used were pre-existing: `/usr/bin/pdftotext`, `python3`, `curl`.
- Scratch `/tmp/revenger-r69-quarantine/` (fetched bytes, PDFs, texts) deleted before returning; the hashes above pin every byte these findings rest on.
- One transient environment event: the scratch tree was deleted mid-run by an external sweep; all cited files were re-fetched and re-hashed afterwards (sizes identical except the live-ad kanxue page), and every number above comes from the post-re-fetch copies.
- Remaining unknowns: S053's `Last updated 2026-10-09 UTC` date and S062's `cell):` fragment have no located source (searched cited source, sibling sources, and same-id PDFs); they may sit in a lane-local artifact or a PDF table I did not fetch.
