# R67QuarS092 — quarantine hand-check, register row S092 (`payload-absent`)

ABSENT — fetch succeeded (HTTP 200, real 27-page PDF, 1,073,057 bytes, sha256 `8062f232d48525dc96adfb465cac215e8baaa7956218720a141677491e619c63`) and both quoted strings are missing from the raw bytes AND from the extracted text layer (exact and whitespace-collapsed); near-misses identified and named below, so this is fabrication-class confirmation for both strings.

## Row identity

Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` line 162 (READ-ONLY, not modified):

```
| `revenger` | round3 | S092 | `payload-absent` | http://cjc.ict.ac.cn/online/bfpub/yyc-2020818141436.pdf | `计 算 机 学 报 / 2020 CHINESE JOURNAL OF COMPUTERS / 嵌入式设备固件安全分析技术研究综述 / 于颖超 1) 陈左宁 2) 甘水滔 1) 秦晓军 1) / 1) (数学工程与先进计算国家重点实验室，江`<br>`从静态分析、符号执行、模糊测试、程序验证、基于机器学习的方法等角度综述了现有固件缺陷检测方法` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

Register class definition (same file, line 13): `payload-absent` = "every relevant source fetched cleanly and the quote is in none of them — **the fabrication class**: verify by hand, then correct the quote or refuse the row". Verdict rules applied verbatim from my item brief.

## Fetch provenance (try 1 of 3 — succeeded first try)

Command: `curl -sL --max-redirs 15 --max-time 120 -w '…' -o source.bin 'http://cjc.ict.ac.cn/online/bfpub/yyc-2020818141436.pdf'`

- `HTTP:200 DLBYTES:1073057 FINALURL:http://cjc.ict.ac.cn/online/bfpub/yyc-2020818141436.pdf` (no redirect), `curl_exit=0`
- Saved bytes (≤ 2 MB rule satisfied): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S092/source.bin`, 1,073,057 bytes
- sha256: `8062f232d48525dc96adfb465cac215e8baaa7956218720a141677491e619c63`
- `file`: `PDF document, version 1.5, 27 page(s)`; first bytes `25 50 44 46 2d 31 2e 35` (`%PDF-1.5`) — real document bytes, not an HTML error page
- Extracted text layer: `pdftotext -enc UTF-8 -layout` (poppler 26.08.0, pre-existing at `/usr/bin/pdftotext`) → `quarantine/S092/extracted.txt`, 82,037 chars / 1,632 lines over 27 pages (full text layer present, masthead + abstract extracted cleanly)

## String A — `计 算 机 学 报 / 2020 CHINESE JOURNAL OF COMPUTERS / 嵌入式设备固件安全分析技术研究综述 / 于颖超 1) 陈左宁 2) 甘水滔 1) 秦晓军 1) / 1) (数学工程与先进计算国家重点实验室，江`

**ABSENT.**

- Raw `source.bin` bytes, fixed-string, case-sensitive: absent in every tested encoding (utf-8, utf-16-le, utf-16-be, gb18030, big5) × every variant (as-is, `html.escape`, `html.unescape`, numeric-entities `&#NNNNN;`). Expected — PDF text lives in encoded content streams.
- Extracted text: absent exact; absent whitespace-collapsed (collapsing cannot rescue it: the quote's literal ` / ` separators do not exist in the document, and the document has the extra token `Online` between COMPUTERS and the title).
- **Near-miss (the true masthead it distorted)** — `extracted.txt` lines 1–8 (flat offsets 45–400):

  ```
  计      算     机       学   报
  2020                       CHINESE JOURNAL OF COMPUTERS                                                            Online
  嵌入式设备固件安全分析技术研究综述
  于颖超 1) 陈左宁 2) 甘水滔 1) 秦晓军 1)
  1) (数学工程与先进计算国家重点实验室，江苏无锡 214083)
  2) (中国工程院, 北京 100088)
  ```

  Every slash-separated segment of the quote IS present in the document (verified: all segments of `A.split('/')` found in whitespace-collapsed text), but the document joins them with whitespace and `Online`, not ` / `, and the affiliation continues `江苏无锡 214083)` where the quote truncates at `…国家重点实验室，江`. The register's string A is therefore a slash-joined re-transcription of the real masthead — not document text.

## String B — `从静态分析、符号执行、模糊测试、程序验证、基于机器学习的方法等角度综述了现有固件缺陷检测方法`

**ABSENT.**

- Raw `source.bin` bytes: absent (same encoding × variant matrix as above).
- Extracted text: absent exact; absent whitespace-collapsed.
- Corpus-wide absence of the quote's distinctive vocabulary in all 27 pages: `综述了现有` 0 occurrences; `现有固件` 0; `缺陷检测` 0; `程序验证` 0; `基于机器学习` 0 (`机器学习` occurs exactly once, offset 46330, in a body paragraph about Pretenter[108] peripheral modeling — unrelated phrasing). English abstract likewise has no `program verification` / `machine learning` (0 hits).
- **Near-miss (the true sentence it distorted)** — the abstract, `extracted.txt` offset 899 (line ~19):

  > 从静态分析、符号执行、**二进制漏洞关联、动态分析平台**和模糊测试等**五个方面进行了详细分析和横向评估**。

  The document's method taxonomy is 静态分析 / 符号执行 / 二进制漏洞关联 / 动态平台 / 模糊测试 (corroborated by the English abstract, offset 2588: "ranging from static analysis, symbol execution, the binary vulnerability association, dynamic analysis platform to fuzzing test"). The register's string B keeps the first two items, then swaps in 模糊测试→position 3, and invents `程序验证`、`基于机器学习的方法` (neither in the document's taxonomy), and appends the tail `综述了现有固件缺陷检测方法`, which appears nowhere. It reads as a plausible-sounding generic survey-summary sentence — fabricated, consistent with the register's fabrication-class designation.

## Verdict-rule application

- Fetch succeeded with real document bytes → not `UNREACHABLE`.
- Both quoted strings missing from fetched bytes (raw + extracted, exact + collapsed) → the register's absence claim is **re-derived and confirmed**: verdict **ABSENT** (fabrication-class confirmation), with near-misses named per the brief.

## Caveats / limits

- Verdict is grounded in the cited source only (per brief); companion URLs and local artifacts were not re-checked (register note says they were checked; out of my scope).
- Text-layer check used poppler pdftotext 26.08.0; a rendering-level (OCR) re-check is unnecessary here because the extraction cleanly captured precisely the masthead/abstract region where both quotes would have to live, and the full 82K-char layer matches the 27-page document.
- No tool installs were needed: poppler-utils (pdftotext 26.08.0) pre-existing; python3 stdlib only.

## Bounds compliance

- Written: this report + scratch dir `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S092/` (`source.bin`, `extracted.txt`, `check.py`). Nothing else under the lane or fleet; `/home/vgpnk/Projects/shokuknow` accessed read-only (register read only). No git/jj mutations, no subagents, no peer messages.
- Frozen contract `reports/round-67/claims.md` read (head, assimilation posture + C1/C2 predicates); this seat is a read-only hand-check — no corpus/README/counter mutations, per seat rules.

Report: `.ufo/waves/round-67/R67QuarS092.md`
