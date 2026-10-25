ABSENT — register row S108 (round4, payload-absent): the quoted single-line string is absent from the cited source in raw, HTML-escaped, and HTML-unescaped/tag-stripped renderings; a whitespace-different near-miss (identical statement split across lines) exists at source.bin:7-10.

# Fetch receipt
- URL: https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/scripts/fixtures/firmware/generate.mjs
- Command: `curl -sL --max-redirs 15 -w "HTTP %{http_code} %{size_download} bytes\n" -o source.bin <URL>` — first try succeeded
- Result: HTTP 200, 1179 bytes, sha256 `9bea82e92e5462bbaf524161105b79c1845c95d5062d826732b402a9c5351a5c`
- Saved: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S108/source.bin` (1179 B <= 2 MB, full bytes retained)

# String 1 (checked separately)
Quoted (fixed-string, case-sensitive):
`const root = resolve(process.env.REA_FIRMWARE_FIXTURE_ROOT ?? "_reference/firmware-integration/generated",);`

Searches performed:
- `grep -F` literal on raw bytes → MISS
- `grep -F` backslash-escaped variant (`?? \"…\",` as printed in the register) → MISS
- `html.escape(quote)` against raw bytes → MISS
- `html.unescape` + regex tag-strip rendering, both literal and backslash-escaped needles → MISS
- Whitespace-collapsed rendering (`tr -s ' \n' '  '`) → HIT: `const root = resolve( process.env.REA_FIRMWARE_FIXTURE_ROOT ?? "_reference/firmware-integration/generated", );`

**Verdict per string: ABSENT** (exact byte sequence absent in all renderings; present only after whitespace normalization).

# Near-miss (the true statement it probably flattened)
source.bin:7-10 contains the identical statement reformatted multi-line:
```js
const root = resolve(
  process.env.REA_FIRMWARE_FIXTURE_ROOT ??
    "_reference/firmware-integration/generated",
);
```
Every token in the quote (identifier `root`, `resolve`, env var `REA_FIRMWARE_FIXTURE_ROOT`, `??` fallback, literal `"_reference/firmware-integration/generated"`, trailing comma before `)`) appears verbatim at source.bin:7-10 — the register's quoted string is a single-line flattening of this statement, not a fabrication of different content.

# Row verdict
ABSENT — absence claim re-derived and confirmed for the exact quoted string; near-miss named above.

# Tooling
No installs or upgrades performed; system `curl` and `python3` sufficed.
