ABSENT — register row S058's absence claim is confirmed: all three quoted strings are missing from https://rea.tools/ja/ in raw, HTML-unescaped, and tag-stripped renderings (HTTP 200, 61,099 bytes fetched 2026-10-24).

# Quarantine hand-check — wave-4, item 10, row S058

Register row under review (READ-ONLY, not modified):
`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:149`
> `revenger` | round1 | S058 | `payload-absent` | https://rea.tools/ja/ | three quoted strings | "cited source, companion URLs and local artifacts were all checked; the quote is in none of them"

Class: `payload-absent` — register asserts the quotes are ABSENT from the cited source. Re-derived independently.

## Fetch

- Command: `curl -sL --max-redirs 15 -o source.bin -w '%{http_code}' https://rea.tools/ja/` — succeeded on try 1 (no retries needed).
- http_code: **200**; size: **61,099 bytes**; sha256: `087f7abe400d55707c7af918110d191a677430b3b251688efee1755e0fde61c2`
- `file` says: HTML document, Unicode text, UTF-8.
- Real document bytes confirmed — `<title>REA-コーディングエージェントのリバースエンジニアリング</title>`, ~8,492 chars of Japanese body text after tag-stripping (a product page for "REA", a reverse-engineering coding agent; embedded i18n JSON + DX-Ball/cactus game text + case-study prose).
- Saved bytes: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S058/source.bin` (≤2MB, full bytes kept); derived `source.unescaped.txt` (html.unescape) and `source.stripped.txt` (tags removed) alongside.

## Per-string results (grep -F, case-sensitive, on raw bytes + unescaped + tag-stripped)

| # | Quoted string | raw | unescaped | stripped | Verdict |
|---|---------------|-----|-----------|----------|---------|
| 1 | `IoTセキュリティ検証でなぜファームウェア解析調査が必要なのか、8年の実績から見えたこと` | absent | absent | absent | **ABSENT** |
| 2 | `ファームウェア解析調査はなぜ必要か` | absent | absent | absent | **ABSENT** |
| 3 | `調査実績から分かった興味深いこと` | absent | absent | absent | **ABSENT** |

HTML-escaped variants (`html.escape`) and entity-encoded punctuation (`、→&#12289;`) also absent at the byte level for all three strings.

## Near-miss / distortion analysis

Component-keyword sweep over the tag-stripped text (`ファームウェア`, `IoT`, `実績`, `興味深い`, `解析調査`, `8年`, `調査実績`, `必要`): **zero hits for every keyword**. The page contains no firmware, IoT-security, or track-record content whatsoever — the domain-level topic (IoT firmware analysis with 8 years of results) does not exist anywhere in the document. There is no single "true sentence" these quotes distorted; the three quotes read like marketing headline copy (title/subtitle/lede triplet) fabricated wholesale for a different site. No near-miss to name beyond this topic-level absence.

## Evidence commands (reproducible)

```
mkdir -p .../quarantine/S058 && cd .../quarantine/S058
curl -sL --max-redirs 15 -o source.bin -w '%{http_code}' https://rea.tools/ja/   # 200, 61099 bytes
grep -F -q '<each quoted string>' source.bin source.unescaped.txt source.stripped.txt   # all: no match
python3 -c "import re,html; ..."   # unescape + strip renderings, find() == -1 for all three
```

## Row verdict

**ABSENT** — the register's claim for S058 stands: none of the three quoted strings appears in the cited source in any checked form (raw bytes, HTML-unescaped, tag-stripped, escaped/entity variants). Fabrication-class absence confirmed; the quotes are not even a distortion of this page's content — the page is about a coding-agent RE tool and shares zero vocabulary with the quotes.

## Bounds / provenance

- Read-only respected: no writes under `/home/vgpnk/Projects/shokuknow`; register file untouched.
- Writes confined to `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/` (this report + `quarantine/S058/` artifacts, per brief).
- No installs or updates performed; no tools needed beyond curl/grep/python3 stdlib.
