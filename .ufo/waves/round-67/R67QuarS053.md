ABSENT — fetched 200/14981 bytes; all 3 quoted strings missing from the jadx v1.5.6 release JSON (fixed-string, raw and HTML-unescaped/tag-stripped); register row `revenger|round1|S053` confirmed.

# Quarantine hand-check — wave-4 item 10, row S053 (revenger, round1, payload-absent)

Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:147`
Cited source: https://api.github.com/repos/skylot/jadx/releases/tags/v1.5.6
Register note checked verbatim; /home/vgpnk/Projects/shokuknow accessed READ-ONLY.

## Fetch receipt

```
$ curl -sL --max-redirs 15 -o source.bin -w 'http_code=%{http_code} size=%{size_download}\n' <URL>
http_code=200 size=14981
$ sha256sum source.bin
85e8921e38333af6b77730ebec6b9fd0a2a0e5e7744fd1baa8811d89bd79a92a  source.bin
```
Saved bytes (<=2MB): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S053/source.bin` (14981 B, GitHub REST release JSON for tag v1.5.6 — real document bytes: tag_name "v1.5.6", name "1.5.6", assets jadx-1.5.6.zip etc.).

## Per-string results

Method: `grep -Fbo` (fixed-string, byte offsets) on raw bytes; `python3 html.escape` produced no differing encodings for either string (no `<>&"'` chars); `html.unescape` + regex tag-strip rendering checked in Python. Case-sensitive throughout.

1. `Dalvik executable format` — **ABSENT**. `grep -Fbo` → NO MATCH; unescaped: False; tag-stripped: False. Case-insensitive `grep -oi 'dalvik[^"]*'` → zero hits anywhere in the document (no "dex"/"Dalvik" text in release body either).
2. `Dalvik executable format` (2nd identical quote on the row) — **ABSENT**, same result; the string appears zero times, so a second instance cannot exist.
3. `Last updated 2026-10-09 UTC` — **ABSENT**. `grep -Fbo` → NO MATCH; unescaped: False; tag-stripped: False. `grep -o '2026-10-09[^"]*'` → zero hits; `grep -oi 'last updated[^"]*'` → zero hits.

## Near-misses (probable distortion sources)

- For quote 3: the document's only dates are `created_at`/`updated_at`/`published_at` = `2026-07-10T18:57:10Z`–`2026-07-10T19:07:35Z` (ISO-8601 `updated_at` field, not the prose "Last updated 2026-10-09 UTC"; the date itself, 2026-10-09, appears nowhere).
- For quotes 1–2: nearest lexical hit is `[cli] ... executable permissions on start scripts (PR #2838)` in the changelog body — substring "executable" only; no format-spec sentence exists in this JSON.

## Scope / limits

- Only the cited source URL was fetched (per seat rules: assigned URL only); companion URLs / local artifacts named in the register note were not re-fetched — the per-string verdicts above cover the cited source.
- Verdict = **ABSENT** for all three strings → row verdict ABSENT (fabrication-class claim confirmed as stated for the cited source).

Report: .ufo/waves/round-67/R67QuarS053.md
