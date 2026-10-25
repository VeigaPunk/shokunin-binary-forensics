ABSENT — fetch succeeded (HTTP 200, 69,784-byte JSON commit list) and all three quoted strings (`apkanalyzer`, `description`, `keywords`) are missing from raw, HTML-unescaped, and tag-stripped renderings; register's absence claim confirmed.

# Seat R67QuarS098 — quarantine hand-check, register row S098

- Register: /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:166
- Row: `revenger` | round3 | S098 | `payload-absent`
- Cited source: https://api.github.com/repos/morluto/rea/commits?path=docs/readme/README_zh.md&per_page=10
- Quoted strings checked (fixed-string, case-sensitive): `apkanalyzer`, `description`, `keywords`

## Fetch receipt

- Command: `curl -sL --max-redirs 15 -o source.bin -w ... 'https://api.github.com/repos/morluto/rea/commits?path=docs/readme/README_zh.md&per_page=10'`
- http_code: 200; size_download: 69784 bytes (<= 2MB, full bytes saved)
- sha256(source.bin): `8b0b207ac6cbb79c524a73c165176766f9157b5466665f0d144002afd61398f8`
- Saved: /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S098/source.bin
- Content type: JSON text (`file`: "JSON text data"); top-level JSON array of 10 commit objects touching `docs/readme/README_zh.md` in morluto/rea. First commit: `403fef0d40` "docs(i18n): add complete Romanian README (#7026)" dated 2026-10-24 (fresh fetch, today's data).

## Per-string results

Each string searched via `grep -Fbo` on raw bytes and via Python `str.find` on `html.unescape(bytes)` and a tag-stripped rendering (`re.sub(r'<[^>]*>','',unescaped)`). Strings contain no HTML-significant characters, so escaped/unescaped variants are identical to the raw token; case variants (upper, capitalize) also checked — all missing.

| string | raw bytes | html.unescape | tag-stripped | verdict |
|---|---|---|---|---|
| `apkanalyzer` | MISSING (grep -Fbo: 0 hits) | MISSING | MISSING | ABSENT |
| `description` | MISSING (0 hits; case-insensitive also 0) | MISSING | MISSING | ABSENT |
| `keywords` | MISSING (0 hits; case-insensitive also 0) | MISSING | MISSING | ABSENT |

## Near-miss scan (probable distortion source)

- Fragment hits in fetched bytes: `apk` 0; `analy` 1 ("translated setup and analysis facts" in commit 9b656dda29 message); `descri` 10 (all "descriptor"/"descriptors" in commit 4ef916da03's PE import-table message); `keyw`/`keyword` 0.
- The token set `apkanalyzer` + `description` + `keywords` matches HTML `<meta name="description">`/`<meta name="keywords">` fields of an `apkanalyzer` documentation page — the register's own revenger-round3 row S099 (line 360) cites `https://developer.android.com/tools/apkanalyzer` (marked unfetchable there). The quote was likely lifted from that companion page's meta tags and attributed to this commits-API URL, whose payload is a JSON commit array with no such fields (commit objects carry sha/author/message, never `description`/`keywords`; those live on repo objects).
- No closer near-miss exists inside the fetched document itself; nothing resembling the quoted triplet appears.

## Verdict

Row verdict: **ABSENT** — fabrication-class confirmation. Real document bytes retrieved on 2026-10-24; every quoted string is missing in every rendering checked.

## Tools

- No installs or upgrades performed; used system `curl`, `grep`, `python3` (stdlib `html`, `re`, `json`).
