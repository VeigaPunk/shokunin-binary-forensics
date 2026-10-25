ABSENT — fetch succeeded (HTTP 200, 41,461 real arXiv bytes, sha256 `e10ccee211c9a9b173a1a19e1e7f6d86ac193ff2dc26587c41a286fb6cd8afa2`) and all three quoted strings are missing from raw bytes, HTML-unescaped, and tag-stripped renders; fabrication-class confirmation with near-misses named below.

# Quarantine hand-check — register row S063 (wave-4 item 10, revenger round1)

Seat: R67QuarS063 · Date: 2026-10-24 · Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin (read-only except this report + quarantine/S063 scratch)

## Register row checked (verbatim, /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:153)

```
*153|| `revenger` | round1 | S063 | `payload-absent` | https://arxiv.org/abs/2112.02606v1 | `In our experiments`<br>`In our experiments, the decompilation errors has occurred in some applications.`<br>`Reverse engineering tools such as apktool can be used to extract opcode sequences from the `dex' file` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

Register note re-checked for this row only: cited source re-derived here; companion URLs and local artifacts NOT re-checked by this seat (bounds: assigned URL only). The third register quote is backtick-nested; the literal payload taken is "…extract opcode sequences from the dex' file" (checked also with curly apostrophe and no apostrophe).

## Fetch receipt (freshness: live fetch 2026-10-24)

```
$ curl -sSL --max-redirs 15 -w 'HTTP_CODE=%{http_code} SIZE=%{size_download} FINAL_URL=%{url_effective}\n' -o /tmp/r67s063.bin https://arxiv.org/abs/2112.02606v1
HTTP_CODE=200 SIZE=41461 FINAL_URL=https://arxiv.org/abs/2112.02606v1
CURL_EXIT=0
BYTES=41461
e10ccee211c9a9b173a1a19e1e7f6d86ac193ff2dc26587c41a286fb6cd8afa2  /tmp/r67s063.bin
```

41461 bytes ≤ 2 MB → bytes archived at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S063/source.bin` (sha256 `e10ccee211c9a9b173a1a19e1e7f6d86ac193ff2dc26587c41a286fb6cd8afa2`, re-verified after copy). Real document bytes, not an error page: `<title>[2112.02606v1] On Impact of Semantically Similar Apps in Android Malware Datasets</title>`, `citation_date = 2021/12/05`, abstract present ("Malware authors reuse the same program segments … we propose a novel opcode subsequence based malware clustering algorithm …").

## Per-string results (fixed-string, case-sensitive)

Renders searched: R0 = raw bytes; R1 = `html.unescape` of raw; R2 = R1 with tags stripped (`re.sub(r'(?s)<[^>]+>', '', …)`). Escaped variants searched in raw: `html.escape(s)` (quote form), `html.escape(s, quote=False)`, and spaces→`&#32;`.

| # | Quoted string | R0 raw | R1 unescaped | R2 stripped | escaped variants |
|---|---|---|---|---|---|
| S1 | `In our experiments` | absent (grep -F -c = 0) | absent | absent | absent (all 3 forms) |
| S2 | `In our experiments, the decompilation errors has occurred in some applications.` | absent (grep -F -c = 0) | absent | absent | absent (all 3 forms) |
| S3 | `Reverse engineering tools such as apktool can be used to extract opcode sequences from the dex' file` | absent (grep -F -c = 0) | absent | absent | absent (all 3 forms) |

S3 apostrophe variants also absent: `dex’ file` (U+2019) and `dex file` (no apostrophe) — 0 hits each.

## Near-misses found (what the source actually says)

1. **S1 near-miss:** the page contains (case-insensitive, tag-stripped render): "In our **experimentation** with Drebin dataset, we found that, after removing the exact dup…" — the abstract's real phrase is "In our experimentation…", which does NOT contain the fixed string "In our experiments" (`experiment` is followed by `a`, not `s`). The quoted `In our experiments` looks like a truncation/distortion of this phrase.
2. **S2 near-miss:** `decompil` occurs **0 times** in the entire fetched document; the abstract never mentions decompilation errors. The quoted sentence's non-native grammar ("the decompilation errors has occurred") is fabrication-class; no source sentence found on this page.
3. **S3 near-miss:** `apktool` occurs **0 times**; the page's only `opcode` hit is "we propose a novel **opcode** subsequence based malware clustering algorithm to identify the semant…" — topic-adjacent (the paper is about opcode subsequences in Android malware datasets) but the quoted sentence itself is absent; `dex file` also 0 hits.

## Verdict

**ABSENT** (fabrication-class confirmation for row S063): real document bytes fetched and every quoted string is missing under fixed-string case-sensitive search across raw, HTML-unescaped, tag-stripped, and HTML-escaped variants; near-misses named above. Consistent with the register's note for this row.

## Known limits

- The cited source is the arXiv **abstract page** (v1 landing page); the absence verdict applies to that document as cited. Full text (PDF / arXiv HTML rendering) was not fetched — bounds allow network fetches for the assigned URL only.
- Companion URLs and local artifacts in the register note were not re-derived by this seat (register's claim, not execution evidence here).
- If the register's evidence intent for S063 was full-text absence, a full-text pass would be a separate receipt.

## Tooling record

No tools installed or upgraded for this seat (curl/python/grep sufficient); pacman untouched per host-wide pause.

## Artifact paths

- Report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67QuarS063.md`
- Source bytes: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S063/source.bin` (41,461 bytes, sha256 `e10ccee211c9a9b173a1a19e1e7f6d86ac193ff2dc26587c41a286fb6cd8afa2`)
