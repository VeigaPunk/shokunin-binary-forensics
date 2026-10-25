# R67QuarS060 — quarantine hand-check, row S060 (revenger / round1 / `payload-absent`)

ABSENT — fetch succeeded (HTTP 200, real HTML document) and the quoted string `[原创]安卓逆向的核心流程` is missing from the fetched bytes in raw form, after html.unescape + tag-stripping, and in every HTML-escape/URL-encode variant checked; fabrication-class confirmation.

## Row checked

Source: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` (READ-ONLY; never written), line 150:

> `revenger` | round1 | S060 | `payload-absent` | https://book.crifan.org/books/android_re_static_analysis/website/related_items/decompile/tools/jadx/ | `[原创]安卓逆向的核心流程` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them

## Fetch (fresh, 2026-10-24)

```
$ curl -sL --max-redirs 15 -w 'HTTP_CODE=%{http_code} SIZE=%{size_download} FINAL_URL=%{url_effective}\n' \
    -o source.bin 'https://book.crifan.org/books/android_re_static_analysis/website/related_items/decompile/tools/jadx/'
HTTP_CODE=200 SIZE=57634 FINAL_URL=https://book.crifan.org/books/android_re_static_analysis/website/related_items/decompile/tools/jadx/
$ wc -c < source.bin
57634
$ sha256sum source.bin
a481c3699ceb5b280e6c7d80c39b3266de194f5906f1e548d14e55c18126841e  source.bin
```

- 57,634 bytes ≤ 2 MB → bytes retained at `quarantine/S060/source.bin`.
- Real document bytes confirmed: not gzip (`is_gzip: False`), contains `<html`, `<title>jadx · Android逆向：静态分析</title>` — the correct jadx chapter of the crifan gitbook, so the fetch was not a soft-404/interstitial.

## Per-string check (1 string on this row)

Quoted string: `[原创]安卓逆向的核心流程`

| check | result |
|---|---|
| `grep -cF` on raw fetched bytes | `raw_exact=0` |
| `grep -cF` on html.unescape + tag-stripped, whitespace-normalized rendering | `stripped_exact=0` |
| decimal entities `&#21407;&#21019;…` | 0 in raw, 0 in stripped |
| hex entities `&#x539F;&#x521B;…` (upper + lower) | 0 in raw, 0 in stripped |
| URL-encoded `%5B%E5%8E%9F%E5%88%9B%5D…` | 0 in raw, 0 in stripped |
| bracket-entities-only combo `&#91;原创]…&#93;` | 0 in raw, 0 in stripped |
| bracket-less substring `安卓逆向的核心流程` | 0 in raw, 0 in stripped |

Component probes (near-miss hunt, stripped rendering): `原创` → 0 hits anywhere in the page; `核心流程` → 0 hits anywhere; `安卓逆向` → 1 hit, at byte offset ~6986 of the stripped text, inside the gitbook config JSON (`"description":"介绍安卓逆向之静态分析。包括先是概览；…"`), i.e. the book's own title/description, not the quoted sentence.

Near-miss analysis: the quote has the shape of a Chinese forum post title (`[原创]` = "[original work]" prefix, typical of bbs.kanxue.com / 52pojie thread titles), not of any heading on this gitbook page — the page's real title is `jadx · Android逆向：静态分析`. No distorted on-page sentence was found that the quote could plausibly derive from (`原创` and `核心流程` never occur at all). The register's absence claim re-derives exactly.

## Verdict rules applied

- ABSENT branch: fetch succeeded with real document bytes (200, valid HTML, expected page title) AND the quoted string is missing in all forms checked. Row S060 `payload-absent` classification is CONFIRMED (fabrication-class: quote does not exist at the cited source).

## Scope & limits

- Only the one cited-source URL in row S060 was re-fetched, per assignment. The register note also mentions companion URLs and local artifacts; re-checking those was not in scope. No writes to `/home/vgpnk/Projects/shokuknow` (read-only throughout).
- Bounds respected: writes limited to `…/.ufo/waves/round-67/quarantine/S060/` (source.bin, source.stripped.txt) and this report. No git/jj mutations, no installs (none needed; curl/python3 already present — no tool added this run).

## Artifacts

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S060/source.bin` — fetched bytes, 57,634 B, sha256 `a481c3699ceb5b280e6c7d80c39b3266de194f5906f1e548d14e55c18126841e`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S060/source.stripped.txt` — html.unescape + tag-stripped rendering used for the second grep pass
