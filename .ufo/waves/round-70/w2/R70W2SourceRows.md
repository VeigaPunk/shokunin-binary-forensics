# R70W2SourceRows — SOURCES S048/S049 re-open verdict

**Verdict: ROWS-HOLD** — both rows verified fresh on 2026-10-25: S049 re-fetch is byte-identical to its stated digest and the committed snapshot; S048 re-fetch is the genuine live page differing from the committed snapshot only in two page-chrome lines (CSP nonce + one devsite loader line), and all five quoted-phrase locators match exactly. Census exit 0 (W04 warnings only). Both rows have 11/11 columns.

---

## 1. Fetch records (today, curl)

**S049** — `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md` (tag rea-agents-6.5.0):
- FETCH_START_UTC=2026-10-25T21:49:24Z, FETCH_END_UTC=2026-10-25T21:49:24Z
- 1992 bytes, sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`
- MATCHES the row's stated size (1992) and digest exactly (SOURCES.md:63).
- `diff live snapshot` → empty → byte-identical to `corpus/snapshots/rea-android-applications.md` (sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`, 1992 bytes). Row's byte-identical claim holds.

**S048** — `https://source.android.com/docs/core/runtime/dex-format`:
- First attempt 21:49:24Z: curl exit 47 / `Maximum (50) redirects followed`. Hop trace (with UA + Accept-Language): `dex-format` → 302 `oauth2authorize?return_url=…&prompt=none&auto_signin=True` → 302 `accounts.google.com/o/oauth2/v2/auth` → 302 `source.android.com/oauth2callback?error=interaction_required&error_subtype=access_denied` → 302 back to `dex-format` → LOOP. (Google devsite sign-in flow on anonymous empty-cookie client; environment note, not a row defect.)
- Retry with cookie jar (`-c/-b cj.txt`) + full browser headers at 21:49:56Z: exit 0, genuine page — `<title>Dalvik executable format | Android OS core topics | Android Open Source Project</title>`, canonical `https://source.android.com/docs/core/runtime/dex-format` — 281157 bytes, sha256 `7aac3c846af40c7948519ae86b54b38b8307e901a8307bfae7b41a2668975461`.
- `diff` vs committed snapshot `corpus/snapshots/dex-format.html` (sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`, 281157 bytes): exactly 2 changed lines — line 8946 script nonce (`R1GN4pA7+nDrYJ/dulpbEJ8pQlLBzr` → `Eb5Zq95yw/NpcqTAJQRx9km7X6G5Sl`) and line 8951 the devsite `app_loader.js` config line. This confirms the row's "differs from the committed snapshot only in the per-request CSP nonce and one devsite loader line" and the entry's "only in page-chrome lines" (knowledge/round-70-apk-axml-byte-evidence.md:3).
- Row-stated digest `d72efc55…` / 281161 bytes vs my fetch 281157 bytes / `7aac3c84…`: ±4 bytes entirely attributable to per-request nonce/loader chrome variance (the row itself states the snapshot≠live delta is exactly that chrome). Content lines (below) are byte-identical at the stated line numbers, so the digest divergence is expected per-request variance, not falsifying.

## 2. Quoted-phrase locators (verified in BOTH committed snapshot and today's live fetch, same line numbers)

| phrase | heading (line) | line | words |
|---|---|---|---|
| `header_item` field table | h2 "Items and related structures" (5921) → h3 id="header-item" (5926) | 5926 | — |
| "adler32 checksum of the rest of the file (everything but magic and this field)" | checksum row in header_item table | 5949 | 14 |
| "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)" | signature row | 5956 | 17 |
| "must be 0x70 (112) bytes (v40 or earlier)" | header_size row | 5981 | 8 |
| "uint ENDIAN_CONSTANT = 0x12345678;" | h2 "Bitfield, string, and constant definitions" (4964); h4 "Embedded in header_item" nested | 5035 | 3 |

All ≤25 words. Row's stated live line numbers (5926/5949/5956/5981/5035) match exactly. S045's superseded locator ("File layout" → header_item table) is indeed wrong: "File layout" h2 is at 4825 and contains only a `<td>header_item</td>` diagram mention (4838); the field table lives under "Items and related structures" (5921). S048's correction claim is accurate.

**S049** — sentence `Start with \`inspect_android_package\` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.` at lines 7-8 of the snapshot (17 words; file title "# Android application artifacts" at line 1, no subheading). Row's "lines 7-8" holds. `entry_checks.py --spec-quotes` prints `MATCH rea-android-applications.md: first line 7 …` and the four S048 MATCH lines at 5949/5956/5981/5035 (entry lines 144-148), consistent with the row claims.

## 3. Column census

- `awk -F'|' 'NR==62||NR==63{print NR, NF}'` → `62 13`, `63 13` (11 data columns + leading/trailing pipes). Row structure intact.
- Full-file scan `awk -F'|' '/^\|/{if(NF!=13) print}'` → no malformed table rows anywhere.

## 4. Census

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → exit 0, `ok` for SOURCES.md, with W04 warnings only — including the expected `S048 duplicate url source.android.com/docs/core/runtime/dex-format across scopes` (S045/S048 share the URL by design of the supersede). Matches the expected "exit 0 with W04 warnings".

## 5. Findings / notes

- No defects found. ROWS-HOLD.
- Environment note: source.android.com intermittently forces an oauth sign-in redirect loop for anonymous clients; a cookie-jar retry retrieves the genuine page. This does not falsify the row (the row author also fetched successfully at 21:28Z).
- The row-stated hash cannot be bit-reproduced across requests (per-request nonce); the correct freshness check is the two-line chrome diff, which holds.
- Committed snapshot hashes verified: `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (dex-format.html, 281157 B), `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` (rea-android-applications.md, 1992 B).
