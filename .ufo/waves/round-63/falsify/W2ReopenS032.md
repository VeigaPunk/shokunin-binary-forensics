# W2ReopenS032 — S032 APPNOTE re-open

Attacks: **C1** (coverage K), source row **S032** and the anchors on `corpus/knowledge/round-63-zip-central-directory-evidence.md:1` (§4.3.3, §4.3.7, §4.3.12, §4.3.16, §4.4.7, §4.4.10–4.4.12, §4.4.16, §4.4.21–4.4.22).

**VERDICT: CONFIRMS.** This fetch of the primary URL is byte-identical to the committed snapshot. The fallback URL serves a different revision (6.3.9). Every section the entry cites, and the whole of chapters 4.3 and 4.4, is byte-identical across the two revisions. The only byte drift is outside those sections (header, §2.2 change log, §4.6 third-party mappings, APPENDIX B).

Access date of this re-open: 2026-10-24 (HTTP `Date` on both responses: `Sat, 24 Oct 2026 02:59:50 GMT`). No tool installed. No pacman.

## This fetch — primary URL

| field | value |
|---|---|
| request / final URL | `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` (0 redirects) |
| HTTP status | **200** (`HTTP/2 200`) |
| `Date` | `Sat, 24 Oct 2026 02:59:50 GMT` |
| `Last-Modified` | `Tue, 01 Nov 2022 17:34:41 GMT` |
| `Content-Type` | `text/plain` |
| `Content-Length` / `wc -c` | **174585** |
| sha256 | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` |
| version line | `Version: 6.3.10` / `Status: FINAL - replaces version 6.3.9` / `Revised: Nov 01, 2022` |
| line endings | CRLF only (3798 lines) |

## Diff against the committed snapshot

Committed file: `.ufo/waves/round-63/source-snapshots/appnote.txt`.

`sha256sum` of the committed file equals the fetch digest above. `wc -c` = 174585. `cmp -s` exit **0**. `diff -q` exit **0**. The served bytes and the committed snapshot are the same file.

Provenance sidecar `.ufo/waves/round-63/source-snapshots/appnote.provenance.json` records the same sha256, length, version, and `Last-Modified`. Its `server_date_header` (`Sat, 24 Oct 2026 02:21:34 GMT`) is an earlier fetch the same day; this re-open's `Date` is `02:59:50 GMT`. Content identity did not move.

## Two URLs, two revisions

Fallback request: `https://pkware.com/documents/casestudies/APPNOTE.TXT`.

| field | value |
|---|---|
| first hop | `HTTP/2 301`, `Location: https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.9.TXT` (`x-redirect-by: Yoast SEO Premium`) |
| final status | **200** (`HTTP/1.1 200 OK`) |
| final URL | `https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.9.TXT` |
| `Date` | `Sat, 24 Oct 2026 02:59:50 GMT` |
| blob `Last-Modified` | `Fri, 08 Mar 2024 17:48:19 GMT` (blob metadata, not the spec's revised date) |
| `Content-Length` / `wc -c` | **173575** |
| sha256 | `c7cf1fecfbde36ebbfbac643e6183d5c76fac983c2066fb8e32c6e4058a87e80` |
| version line | `Version: 6.3.9` / `Status: FINAL - replaces version 6.3.8` / `Revised: July 15, 2020` |

These match the provenance sidecar's fallback sha256, length, final URL, and version. The two URLs do not serve the same revision.

## Cited sections — byte-identical

Section span = the heading line through the line before the next dotted-number heading, CRLF included. Line numbers are 1-based, inclusive. Every cited span has equal length and equal sha256 in 6.3.10 (this fetch = snapshot) and 6.3.9. The 6.3.9 copy of each span starts 5 lines earlier, which is the change-log insert below and nothing else.

| section | 6.3.10 lines | 6.3.9 lines | lines | bytes | sha256 (both) |
|---|---|---|---|---|---|
| §4.3.3 | 348–352 | 343–347 | 5 | 303 | `9bb728ca00eeeff450f2770364a772e3c1794fe955276fa7dea214ea67160751` |
| §4.3.7 | 387–403 | 382–398 | 17 | 635 | `0dff403ac8d6dfbe9031dc551b030d7436644ac166deddf657d1481b3f1cc81d` |
| §4.3.12 | 511–543 | 506–538 | 33 | 1156 | `407729188800993e4e0a25364fc3fbf5a53678bf8d5ec5bde07e17b8087fa988` |
| §4.3.16 | 632–648 | 627–643 | 17 | 676 | `1201d153902c378a17e9e1e63f87785e2db44492f4b83f502b1ed052a3c1c6f9` |
| §4.4.7 | 900–918 | 895–913 | 19 | 987 | `34948995dce26e2e47176386dd23f261bcf225d363d7ef6c2c27efda048c8ed6` |
| §4.4.10 | 937 | 932 | 1 | 39 | `791c16a429d266c281e2fcd6652a2743f10d5450e605f9b078d796e23ded4822` |
| §4.4.11 | 938 | 933 | 1 | 41 | `4e4f53e69fd44425d92d599c64342251185377c7e396cb5ceb9d2b545bdc6309` |
| §4.4.12 | 939–947 | 934–942 | 9 | 348 | `0fc23795c8d09e59b5c5873f891b531c8056b8d80f5b62d3bb6cebf1aa3b4751` |
| §4.4.16 | 981–988 | 976–983 | 8 | 384 | `4cf2e1c7dfb0da709adfb16fec8174c2c9bfa68a375657e5e4180427bffeb66f` |
| §4.4.21 | 1032–1040 | 1027–1035 | 9 | 341 | `ae2878550ada446c436e92d80761be9fd8581877122d41ca83bb03cb3d62bd9e` |
| §4.4.22 | 1041–1047 | 1036–1042 | 7 | 298 | `41dac1c13a81f7dde093e7de0a7b3780dd17c6d2cad5c06b3e16d90d3ecbe06e` |

§4.4.10–§4.4.12 are cited as one range. Their shared following paragraph sits in the §4.4.12 span (through the line before §4.4.13). Each piece matches, so the range matches.

Stronger than the cited list, still identical:

- Chapter 4.3 (heading `4.3` through the line before `4.4`): 6.3.10 lines 333–648, 14169 bytes, sha256 `a9ff45c4dd5b9c6677214e1a864f9f144d66f0bc10625a3722e1090717aab19a`.
- Chapter 4.4 (heading `4.4` through the line before the `4.5` that follows §4.4.28): 6.3.10 lines 649–1093, 19923 bytes, sha256 `77a9c78888c03bc8b99cc44dbc4a536e5c5aa42477215425456162d32358303c`.

A dotted-number regex also hits version-needed rows inside §4.4.3.2 (`4.5 - File uses ZIP64…`, `5.0 - File is encrypted…`). Those are table rows, not headings, and they sit in neither a cited span nor the chapter-4.4 end bound used above. They are the same bytes in both revisions.

The entry's located quotes (§Sources, lines 645–654) are substrings of these identical spans. Single-line quotes match raw in both files. The wrapped quotes (§4.4.7, §4.4.16, the §4.3.16 entry-count sentence) match both files after whitespace is collapsed to single spaces. No quote drift.

## Drift located (not in any cited section)

`difflib` of 6.3.9 → 6.3.10: **6 hunks**, 75 unified-diff lines. Nothing in §4.3 or §4.4.

1. **Header, lines 2–5.** Version `6.3.9` → `6.3.10`; status "replaces version 6.3.8" → "replaces version 6.3.9"; revised `July 15, 2020` → `Nov 01, 2022`; copyright gains `, 2022`.
2. **§2.2 Change Log, 6.3.10 lines 229–233** (insert after the 6.3.9 bullet). Five added lines: "Added several z/OS attribute values for APPENDIX B" and "Added several additional 3rd party Extra Field mappings" (credit: Armijn Hemel). This is the +5 line shift seen in every 4.3/4.4 line number above.
3. **§4.6.1 Third party mappings, 6.3.10 lines 1568–1582.** Added `0x1986` Pixar USD, `0x4154` Tandem, `0x4854` THEOS (old?), `0x4d63` Macintosh Smartzip. `0x4d49` Info-ZIP OpenVMS gains one trailing space.
4. **§4.6.1 continued, 6.3.10 lines 1590–1600.** Added `0x6854` THEOS, `0x7441` AtheOS/Syllable, `0x7875` Info-ZIP UNIX (newer UID/GID), `0xcafe` Java JAR, `0xd935` Android ZIP Alignment, `0xe57a` Korean ZIP code page.
5. **§4.6.3, 6.3.10 line 1635.** Added "Not all third-party extra field mappings are documented here."
6. **APPENDIX B field table (`B.2`), 6.3.10 lines 3668–3670.** Added `00A2` Cluster Log, `00A3` Cluster LSID Length, `00A4` Cluster LSID.

Hunks 3–6 are exactly the two change-log bullets. No other region differs.

## What this does not attack

Not re-checked here: S033 own-work bytes, the readout's numeric offsets, Q01–Q13 of the entry, or whether the S032 `teaches` cell's 46/16/42 and 22/8/10 figures match the field tables. Those are other seats. The field tables they would read (§4.3.7, §4.3.12, §4.3.16) are the spans above and did not move.

## Tooling

None installed or upgraded. `curl` and `python3` (stdlib `hashlib` / `difflib`) were already present. No pacman. Scratch `/tmp/revenger-r63-W2ReopenS032/` (this fetch's bodies and header dumps) removed after this report was written.
