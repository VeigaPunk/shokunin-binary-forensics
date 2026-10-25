ABSENT — all 3 quoted strings are missing from the fetched bytes of the cited source; the fetch returns a real, deterministic jos.org.cn article-template page whose article fields are entirely empty, so the register's absence claim for row S113 (revenger round4, `payload-absent`) is confirmed.

# Scope
Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:170` (`revenger` | round4 | S113 | `payload-absent` | https://www.jos.org.cn/ch/reader/view_abstract.aspx?file_no=5651&flag=1). (shokuknow read-only; no writes there.)

# Fetch evidence
- `curl -sL --max-redirs 15 'https://www.jos.org.cn/ch/reader/view_abstract.aspx?file_no=5651&flag=1'` → HTTP 200, 29,818 bytes.
- sha256 `ad0309245abce946f87ddd8deb8b510cdd9bc218bfebbd57459d0dfcccb1af07`, saved at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S113/source.bin` (<=2MB, full bytes kept).
- Encoding: HTML document, UTF-8, CRLF (`charset=utf-8`).
- Retry 1 and retry 2 with browser UA + `Accept-Language: zh-CN` returned byte-identical bodies (same sha256, same 29,818 bytes) — the response is deterministic, not an intermittent partial.
- Control fetches of `file_no=5650`, `5652`, `5600` all return the identical 29,818-byte shell: the endpoint currently serves an article-template page with every record field empty for any file_no (the journal moved to `www.jos.org.cn`→jos.iscas.ac.cn-era backend; the legacy view_abstract endpoint now renders zero rows).

# What the page actually contains
Stripped text is 761 chars of template boilerplate only: 主页/期刊介绍/编委会/投稿指南 navigation, `摘要 :`, `关键词 :`, `DOI：`, `基金项目:`, `Abstract :`, `Key words :` labels with empty values, footer `欢迎访问软件学报网站`, `jos@iscas.ac.cn`. `file_no=5651` appears only inside template links (create_pdf.aspx, appraise.aspx, article_export.aspx, search_reference.aspx — source.bin:127,129-131,452). No title, authors, abstract, keywords, citation, or volume/issue/page data anywhere. Title tag is empty.

# Per-string results (fixed-string, case-sensitive)

| # | Quoted string (abbrev.) | raw bytes | decoded text | html.unescape | tag-stripped | entity-escaped variant | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | `介绍了若干基本程序分析技术（抽象解释、数据流分析、基于摘要的分析、符号执行、动态分析、基于机器学习的程序分析等），特别是最近10余年的研究进展.` | -1 | -1 | -1 | -1 | -1 | ABSENT |
| 2 | `进而介绍了针对不同类型软件（移动应用、并发软件、分布式系统、二进制代码等）的分析方法.` | -1 | -1 | -1 | -1 | -1 | ABSENT |
| 3 | `张健,张超,玄跻峰,熊英飞,王千祥,梁彬,李炼,窦文生,陈振邦,陈立前,蔡彦.程序分析研究进展.软件学报,2019,30(1):80-109` | -1 | -1 | -1 | -1 | -1 | ABSENT |

Method: `bytes.find(s.encode('utf-8'))` on raw; `str.find` on utf-8-decoded text, on `html.unescape(text)`, on tag-stripped text, and on the `xmlcharrefreplace`/`html.escape` entity-encoded variants of each string. All -1.

# Near-miss search
Zero near-misses exist to name: the page contains no article content at all. Component-token grep over the rendered text yields: `程序分析` 0 hits, `张健` 0, `抽象解释` 0, `进而介绍` 0, `介绍了若干` 0, `数据流分析` 0, `符号执行` 0, `机器学习` 0, `移动应用` 0, `分布式系统` 0, `二进制代码` 0, `玄跻峰` 0, `熊英飞` 0, `研究进展` 0, `30(1)` 0, `80-109` 0. `软件学报` appears only at offsets ~11731/~26186 as the site-name boilerplate `欢迎访问软件学报网站` — not part of a citation.

# Characterization
The three quoted strings are a recognizable abstract + citation of a real 软件学报 paper (`程序分析研究进展`, 2019, 30(1)) — consistent with a fabricated/distorted payload attributed to a cited source that serves no record content. The register's claim "the quote is in none of them" is CONFIRMED for the cited URL as fetched today. [INFERENCE] The payload likely cites a wrong/invalid `file_no` for that paper (5651 maps to no populated record on the legacy endpoint).

# Verdict
Row S113 verdict: **ABSENT** (fabrication-class confirmed — every quoted string missing from real fetched document bytes; no near-miss present because the endpoint renders an empty-record template).

No tools installed or upgraded (pacman paused per guard; curl/python3 already present).
