ABSENT (3 of 9) — S075, S083, S093(partial) confirm fabrication-class; 2 PRESENT (S090, S092) are register-wrong; 3 (S081, S087, S089) are locator/attribution errors with the quote verbatim elsewhere; 1 (S085) is UNREACHABLE because the census `url` field is truncated at exactly 140 chars.

# R69QuarB — quarantine register hand-check (revenger lane, 9 rows)

Wave-4 hand-check of the absent-defect register. Read-only on the campaign tree; no
register/campaign file was written. Adoption remains closed — nothing here proposes a
register edit, only per-row verdicts and their evidence.

## Lane slice derivation

`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
(83,621 B) has **24** data rows whose lane cell is `` `revenger` `` with a round cell and an
S-id (register lines 147-170: S053, S055, S058, S060, S061, S062, S063, S064 | S075, S081,
S083, S085 | S087, S089, S090, S092, S093, S094, S095, S098 | S107, S108, S111, S113), plus
2 blank-class summary rows at lines 359-360. This seat is the assigned 9: register lines
155-163. The other 15 rows are outside this ticket.

Verification of the slice (exact command, exact output):

```
$ grep -n '^| `revenger` ' .../absent-defect-register.md | sed -E 's/^([0-9]+):\| `revenger` \| ([a-z0-9]+) \| ([A-Z0-9]+) \|.*/\1 \2 \3/'
147 round1 S053 ... 155 round2 S075 156 round2 S081 157 round2 S083 158 round2 S085
159 round3 S087 160 round3 S089 161 round3 S090 162 round3 S092 163 round3 S093 ...
170 round4 S113
```

## Verdict rule used (calibration-relevant)

The task's four classes are applied strictly to the **cited source**, and a row whose quote
is absent from the cited bytes **but verbatim elsewhere** is *not* promoted to
fabrication-class:

| observed | verdict |
|---|---|
| quote verbatim (or verbatim after a transparent layout fold: line-wrap inside a token, bullet/reading-order join) in the cited bytes | `PRESENT` — register wrong |
| quote in none of the renderings of the cited bytes, **and** not found verbatim in any companion/sibling artifact | `ABSENT` — fabrication-class confirm |
| fetch failed (404/timeout) | `UNREACHABLE` — not fabrication |
| fetch succeeded, quote not in the cited bytes, but verbatim in a companion, the cited file's own named source, or a sibling document of the same publisher | `UNVERIFIED-REACHABLE` — locator/attribution class, not fabrication |

Renderings searched for every row: raw bytes decoded UTF-8 (`errors=replace`), and
`pdftotext -enc UTF-8` text for PDFs. Folds applied symmetrically to needle **and**
haystack: `exact`, whitespace-collapse, NFKC, NFKC+whitespace-collapse, whitespace-delete,
NFKC+whitespace-delete.

## Per-row verdicts

```
S075 ABSENT   both fragments in no rendering of the cited analysis.mjs (10,289 B) nor of 3 sibling repo docs
S081 UNVERIFIED-REACHABLE  0/3 in the cited test-vectors.json (494 B, no prose); 3/3 verbatim in RFC 6238, the URI the JSON names in its own "source" field
S083 ABSENT  all 3 fragments in none of 870 APK files (UTF-8/UTF-16LE/BE); "filename=ApiDemos-debug.apk" exists only percent-encoded in the release-asset redirect URL (transfer metadata, not payload)
S085 UNREACHABLE   cited URL returns 404 and is truncated mid-word at exactly 140 chars; both quotes are verbatim in a sibling SWGDE document
S087 UNVERIFIED-REACHABLE  0x "ildasm" in the cited ECMA-335 PDF; the exact string is the <title> of the ja-jp Ildasm page (char 306)
S089 UNVERIFIED-REACHABLE  0x "Re:birth"/"Ready To Run"/"AOT" in the cited MS docs page; both fragments verbatim in the JSAC2026 deck cited by S090
S090 PRESENT  all four fragments verbatim and contiguous at char 2223-2320; only the register's " / " bullet join is non-verbatim
S092 PRESENT  5/6 fragments verbatim in the cited PDF (2 only under layout folds); the 6th (abstract sentence) is verbatim in S093
S093 ABSENT   2 of 3 quote strings verbatim (one with one deleted character); "CLI header 结构速查" in none of 87,332 B of text
```

Tally for the 9 assigned rows: **PRESENT 2 · ABSENT 3 · UNVERIFIED-REACHABLE 3 ·
UNREACHABLE 1**. Of the 9, **5 rows (S081, S085, S087, S089, S092-partial) are citation /
attribution artifacts whose quoted text is real and verbatim at another resolvable
locator**, i.e. the register's `payload-absent` label over-reports fabrication by 5/9 on
this seat.

## Fetch receipts

Note: every body was fetched twice in this session (before and after a scratch wipe) and
all sha256 values were identical both times.

| row | cited URL | HTTP | bytes | sha256 of fetched body |
|---|---|---|---|---|
| S075 | `raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/scripts/verify/android/analysis.mjs` | 200 text/plain | 10,289 | `a3b6f712151121242f14535b40dbe5745c065c2189a09adfd2f2a41eccd40e8f` |
| S081 | `raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/website/public/showcase/aegis/test-vectors.json` | 200 text/plain | 494 | `f193953c7ef0d92a5006702412eb35ab85ad9f997a1cbdf28189dab7db73beb0` |
| S083 | `github.com/appium/android-apidemos/releases/download/v6.0.18/ApiDemos-debug.apk` | 200 apk | 6,521,217 | `a9eecf37b26cd084855c530db81c2bb1b91f4c1b095a04f47aa7c20e2791f686` |
| S085 | `swgde.org/wp-content/uploads/2026/05/2025-01-13-…-Analysis-from-C` | **404** text/html | 148,736 | `6ceb8b516b42cffe4c26b0ec304cc5f403682ad76cafe878516d774a2444ee01` |
| S087 | `ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf` | 200 pdf | 4,982,145 | `8c1decf6d482f020776a12dd601537e024d5d5f30df130a3ea3bbf3c51adb1d6` |
| S089 | `learn.microsoft.com/ja-jp/visualstudio/debugger/decompilation?view=visualstudio` | 200 html | 64,260 | `d1d0bac4e79e8c8cf976b8bd3cdfa99ec049a10ce6c2674671c82033078d8866` |
| S090 | `jsac.jpcert.or.jp/archive/2026/pdf/JSAC2026_workshop3_jp.pdf` | 200 pdf | 6,015,111 | `6a06c80e952310dd1cf026f329e71c4b784efa50d14ff9159b53914b0430ca57` |
| S092 | `cjc.ict.ac.cn/online/bfpub/yyc-2020818141436.pdf` | 200 pdf | 1,073,057 | `8062f232d48525dc96adfb465cac215e8baaa7956218720a141677491e619c63` |
| S093 | `seg.nju.edu.cn/uploadPublication/copyright/1221412498312.pdf` | 200 pdf | 731,467 | `16826e4f9c911f35c7cae3e9ab49c0697e38c1ba23580101018af48fbc53e4a1` |

Command shape used for every row:
`curl -sL --max-redirs 15 --max-time 120 -A 'Mozilla/5.0 (X11; Linux x86_64)' -o <dir>/body.bin -w '%{http_code} %{content_type} %{size_download} %{url_effective}' <url>`
then `pdftotext -enc UTF-8 body.bin txt.txt` for the four PDFs; the APK was unpacked with
`unzip -qq` (869 entries, 14 MB) and scanned file-by-file.

## Evidence per row

### S075 — ABSENT
Cited script read in full (10,289 B). Its nearest tokens to the quoted headings are
`signature_verification` (line 238) and `engine: packageResult.engine` (line 295); no
"Caller-supplied engine", no "Resource policy". Four other repo files that a design-style
heading could live in were fetched and are also clean (0 hits each, both fragments, all
folds): `docs/android-analysis.md` (21,995 B), `docs/tool-design.md` (12,870 B),
`website/evidence/reverse-engineering-models.md` (8,652 B), `README.md` (404).
Repo file list obtained from `api.github.com/repos/morluto/rea/git/trees/rea-agents-6.7.0?recursive=1`
(4,334 blobs, 186 `.md`). **Limit:** 186 docs were not all fetched; the cited file and the
four most plausible docs are exhaustively clean, and the phrases read like a design-doc
section pair that no doc in this repo exposes.

```
$ grep -a -n -i -E 'caller|resource policy|engine|verification' analysis.mjs
238:assert.equal(packageResult.signature_verification, "not_performed");
295:  engine: packageResult.engine,
```

### S081 — UNVERIFIED-REACHABLE (locator → own declared source)
The cited `test-vectors.json` is 494 B of pure data and contains zero prose:

```json
{"source":"https://www.rfc-editor.org/rfc/rfc6238.html#appendix-B",
 "public_test_key_ascii":"12345678901234567890","algorithm":"HMAC-SHA1",
 "period_seconds":30,"vectors":[{"seconds":59,"sha1":"94287082"},…]}
```

0/3 fragments in it. All three are verbatim in RFC 6238, which this file itself names as its
`source`: `"TOTP: Time-Based One-Time Password Algorithm"` at char 679, `"Test Vectors"` at
4477 and 27861, `"X represents the time step in seconds (default value X = 30 seconds)"` at
folded char 6565 (the RFC wraps the line). The quote is real; the locator points one hop too
close. Not fabrication.

### S083 — ABSENT (payload class; one fragment is transfer metadata)
APK 6,521,217 B, 869 entries unpacked. Scan over the container **and every decompressed
entry** (870 files) for each of the three needles × {`utf-8`, `utf-16-le`, `utf-16-be`}:

```
files 870 hits-per-needle {'Data Integrity': 0,
 'Best Practices for Digital Evidence Collection': 0,
 'filename=ApiDemos-debug.apk': 0}
```

The first fragment does exist — but in the HTTP transfer metadata, percent-encoded in the
GitHub release-asset redirect URL, not in the artifact:

```
$ python3 -c 'urllib.parse.unquote_plus(<%{url_effective}>)'
... &rscd=attachment; filename=ApiDemos-debug.apk&rsct=application/vnd.android.pac…
```

So `payload-absent` is correct for the payload and the quote is nonetheless verifiable at a
non-payload locator; a payload-byte checker can never see it. The other two fragments appear
in no artifact fetched in this wave, including the two SWGDE PDFs (see S085) where
`Data Integrity` exists only lowercase (`data integrity`, folded char 15,647).

### S085 — UNREACHABLE (census truncation, not fabrication)
1. Cited URL → **404** (`148,736 B` WordPress 404 page, sha `6ceb…ee01`).
2. The URL in the register is exactly **140 characters** and stops mid-word:
   `…Preservation-and-Analysis-from-C`. The identical 140-char string is in the census
   (`quote-lint-full-v5.json`), so the truncation is upstream of the register generator —
   `absent-defect-register.py:144` emits `{r['url']}` verbatim and does not truncate URLs
   (only quotes, `absent-defect-register.py:142`, `q[:120]`).
3. **[INFERENCE]** The 2026/05 SWGDE document with this prefix is
   `2025-01-13-…-Analysis-from-Cloud-Service-Providers-23-F-004-1.1.pdf` (found by
   `wp-json/wp/v2/media?search=…`; 11 media hits, exactly one with this prefix). Fetched:
   825,892 B, 200. It contains **neither** quote under any fold or case (folded char −1
   for both) — so even the untruncated locator would have produced ABSENT.
4. Both quotes are verbatim in a **different** SWGDE document, 18-F-003-2.0
   (`2025-08-21-Best-Practices-for-Mobile-Device-Evidence-Collection-Preservation-Handling-and-Acquisition-18-F-003-2.0.pdf`,
   767,292 B): the title span at folded char 45 (`…Collection & Preservation
   Handling and Acquisition` — the register inserts a comma the title page does not have);
   `Hash values from multiple extractions` at folded char 11,749, exact wording
   (`Hash values from multiple extractions of the same device may not match due to the
   dynamic nature of storage media…`). Substance real, locator wrong twice (truncated and
   wrong document).

### S087 — UNVERIFIED-REACHABLE (wrong locator entirely)
Cited PDF identity verified from page 1: `ECMA-335 / 6th Edition / June 2012 / Common
Language Infrastructure (CLI) / Partitions I to VI`. Rendered text 1,419,315 B; `ildasm`
case-insensitive = **0**, `逆アセンブラ` = **0** (an English ISO/IEC spec cannot carry that
Japanese title). The exact quote is the `<title>` of
`learn.microsoft.com/ja-jp/dotnet/framework/tools/ildasm-exe-il-disassembler` at char 306:

```
<title>Ildasm.exe (IL 逆アセンブラー) - .NET Framework | Microsoft Learn</title>
```

### S089 — UNVERIFIED-REACHABLE (cross-source splice)
Cited page (`64,260 B`) is the ja-jp "デバッグ中に .NET コードを逆コンパイルする" article:
`逆コンパイル` ×26, but `Re:birth` = −1, `ready` (case-insens.) = −1, `AOT` = −1. Both
fragments are verbatim in the PDF cited by **S090** (`JSAC2026_workshop3_jp.pdf`):
`Re:birth` at chars 11, 940, 13,177 (`Re:birth the fidb: / Reverse Engineering the .NET
AOT Malware`), `Ready To Run` at chars 2,183 and 2,516. The row's quote and its locator
belong to different sources.

### S090 — PRESENT (register wrong)
Cited PDF 6,015,111 B, text 36,140 B. All fragments exact:

```
2223  AOT(Ahead-Of-Time)形式          (byte 3476, line 180)
2247  .NETの最適化により、プラットフォームによってはILではなく、
2280  ネイティブコードが実行される
2297  解析では、実際にどちらが実行されるのかに注意を払う必要が
```

Source layout: `• AOT(Ahead-Of-Time)形式\n\n• .NETの最適化により、…ILではなく、\n
ネイティブコードが実行される\n• 解析では、…必要が\nある`. The whole register string
(fragments joined with ` / `) misses under all six folds — the joins are the register's
bullet separators, and `ある` is wrapped to its own line. Content is contiguous over
chars 2223-2320, i.e. one slide. Nothing is fabricated; the span is simply not verbatim.

### S092 — PRESENT (5/6 in the cited PDF; 6th verbatim in S093)
Cited PDF 1,073,057 B, text 105,054 B.

| fragment | result |
|---|---|
| `计 算 机 学 报` | exact, char 2578 (byte 3866) |
| `嵌入式设备固件安全分析技术研究综述` | **nospace fold char 40** — source wraps the title: `…研究综\n述` |
| `于颖超 1) 陈左宁 2) 甘水滔 1) 秦晓军 1)` | exact, char 77 |
| `1) (数学工程与先进计算国家重点实验室，江` | **ws fold char 98** — source has `1)\n\n(数学工程…` |
| `2020 CHINESE JOURNAL OF COMPUTERS` | not contiguous: masthead is vertical — `计\n2020\n\n算\n\n机\n\n学\n\n报\n\nCHINESE JOURNAL OF COMPUTERS` (2020 at byte 2, CJC at byte 30) |
| `从静态分析、符号执行、模糊测试、程序验证、基于机器学习的方法等角度综述了现有固件缺陷检测方法` | **not in S092** (max common prefix 11 chars; S092's own sentence is `从静态分析、符号执行、二进制漏洞关联、动态分析平台和模糊测试等五个方面…`); verbatim in **S093** at char 955 / byte 1695 / line 49 |

The register's claim ("in none of them") is false for 5 of 6 fragments. The one genuinely
foreign fragment is verbatim in the sibling paper — an S092↔S093 quote-splice, not invention.

### S093 — ABSENT (1 of 3 quote strings)
Cited PDF 731,467 B, text 87,332 B.

* String 1 (`Software Engineering Group` / `Department of Computer Science` / `Nanjing
  University` / `Technical Report No. NJU-SEG-2021-CJ-`) — exact at chars 0, 27, 58, 100;
  the four lines are contiguous on the cover. **PRESENT.**
* String 2 (`中图分类号 TP311 DOI 号 10.19363/J.cnki.cn10-1380/tn.2021.05.09`) — the source
  says `中图法分类号 TP311 DOI 号 10.19363/J.cnki.cn10-1380/tn.2021.05.09` at char 1118
  / 1131 (line 53). One character (`法`) deleted. Substantially present, technically
  non-verbatim.
* String 3 (`CLI header 结构速查`) — `CLI header` ×0, `结构速查` ×0 in the whole text, and
  ×0 in every other document fetched this wave. **ABSENT — fabrication-class for this
  source.**

## Calibration findings (what this hand-check says about the register itself)

1. **Census `url` truncation at 140 chars manufactures UNREACHABLE rows.** S085's locator is
   cut mid-word in `quote-lint-full-v5.json`; the register copies it. Any long SWGDE /
   publisher URL is therefore pre-doomed to 404, and the register files the row under
   `payload-absent`. Fix is in the census emitter, not the register.
2. **Register truncates quotes at 120 chars** (`absent-defect-register.py:142`), so the
   register's visible quote is not always the quote that was checked; S092/S093 comparisons
   must use the census row, not the printed cell.
3. **5 of 9 rows are attribution, not fabrication** (S081 companion, S085 truncated+wrong
   document, S087 wrong page, S089 cross-source splice, S092 partial splice). A blanket
   `payload-absent` count over-reports fabrication on this seat by 5/9.
4. **The fold set has three concrete gaps**, all of which this seat hit:
   * reading-order joins in vertical/multi-column CJK PDF layout (S092 masthead);
   * line-wrap **inside** a token, which needs whitespace-delete on both sides rather than
     whitespace-collapse (S092 title, S092 affiliation);
   * bullet-join separators the registry itself inserted (` / ` in S090) and wrap-to-next-line
     last characters (`ある`).
5. **Payload-only checking cannot see transfer metadata.** S083's `filename=…` lives in the
   release-asset redirect URL (percent-encoded `rscd=attachment%3B+filename%3DApiDemos-debug.apk`),
   so a byte checker will always report it absent.

## Hygiene, scope, and remaining unknowns

* No tool was installed, upgraded, or run through pacman (host pacman transactions are
  paused; nothing was needed — `curl`, `unzip`, `pdftotext`, `python3` stdlib sufficed).
* Campaign tree read-only: only `read`/`grep`/`sed -n` and `python3` reads. No register,
  census, script, or `.qcache` file was modified; no git/jj command of any kind was run.
* Scratch was `/tmp/r69quarB` (bodies, extractions). **Operational finding:** the seat
  instruction's shared cleanup glob `rm -rf /tmp/revenger-r69-*` is not seat-safe — my
  first scratch `/tmp/revenger-r69-quarantine` was deleted mid-run by another seat's
  cleanup, forcing a full re-fetch (all sha256 values matched, so no evidence lost). Seats
  should namespace scratch by seat id, not by round.
* Not checked (declared gaps): the other 186 `.md` files of the `rea` repo for S075's two
  headings (4 most plausible fetched, all clean); whether S093's `CLI header 结构速查`
  exists in some fourth document not cited by any row in this wave; the exact SWGDE suffix
  for S085 is reconstructed `[INFERENCE]` from the media index (two independent fetches of
  the candidate both returned 200 and the prefix is unique in the index).
