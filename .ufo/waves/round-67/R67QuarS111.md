ABSENT — register row S111 (round4, payload-absent): all three quoted strings are absent verbatim from the cited source in raw, HTML-escaped, and HTML-unescaped renderings; however EVERY string has a byte-identical modulo-whitespace near-miss (the npm document is compact JSON — no space after `:`, while the register quotes pretty-printed `"k": v` with a space). This is a normalization artifact, not fabrication-class content: the data the quotes describe (engines spec, node version, SLSA predicateType) is all real and correct.

# Row checked
- Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:169` (line 169: `revenger | round4 | S111 | payload-absent | https://registry.npmjs.org/rea-agents/6.7.0`)
- Three quoted strings in the row (separated by `<br>`), checked separately below. My item brief named only a truncation of string 1; I checked all register strings plus the brief's literal.

# Fetch receipt
- URL: https://registry.npmjs.org/rea-agents/6.7.0
- Command: `curl -sL --max-redirs 15 -o source.bin -w 'HTTP %{http_code} bytes %{size_download}' <URL>` — first try succeeded
- Result: HTTP 200, 22380 bytes, sha256 `ae3429d52774e39bda4f8c9ba9aa141b26901ec65f82a394e540ed9cc479c236`
- Content type: JSON text (npm version metadata for `rea-agents@6.7.0`; verified `name`/`version` fields). Compact/minified JSON — zero spaces after `:` or `,`.
- Saved: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S111/source.bin` (22380 B <= 2 MB, full bytes retained)

# String 1: `"engines": {"node": "^22.19.0 || ^24.11.0 || >=26.0.0"}`
- `grep -F -b -o` on raw bytes → MISS
- Brief's literal truncation `"engines": {"node": "^22.19.0` → also MISS
- HTML-escaped variant (`&quot;engines&quot;…`) → MISS; html.unescape rendering identical to raw (no entities present) → MISS
- **Near-miss (verbatim-present after whitespace normalization):** source.bin byte 1023: `"engines":{"node":"^22.19.0 || ^24.11.0 || >=26.0.0"},"imports":…` — identical content, spaces after `:` removed by minification.
- Parsed field confirms: `engines = {'node': '^22.19.0 || ^24.11.0 || >=26.0.0'}`
- **Verdict: ABSENT verbatim** (present modulo one space after `:` — the quote is a faithful pretty-print of real data, not a distortion).

# String 2: `"_nodeVersion": "24.18.0"`
- `grep -F` on raw bytes → MISS; escaped/unescaped variants → MISS
- **Near-miss:** source.bin byte 20464: `"_nodeVersion":"24.18.0","allowScripts":…` — exact content minus the space.
- **Verdict: ABSENT verbatim** (real value, whitespace-normalized).

# String 3: `"predicateType": "https://slsa.dev/provenance/v1"`
- `grep -F` on raw bytes → MISS; escaped/unescaped variants → MISS
- **Near-miss:** source.bin byte 834: `"predicateType":"https://slsa.dev/provenance/v1"}},"unpackedSize":…` — exact content minus the space (inside `dist.attestations.provenance`).
- **Verdict: ABSENT verbatim** (real value, whitespace-normalized).

# Row verdict rationale
Per the literal verdict rule (a string is PRESENT only if it IS in the fetched bytes as a fixed, case-sensitive string), all three quoted strings are ABSENT — matching sibling precedent (R67QuarS108: "present only after whitespace normalization" → ABSENT). BUT the register's classification `payload-absent` ("the quote is in none of them", implying fabrication) is misleading here: this is not a distorted/fabricated quote — it is exact npm data re-rendered with canonical JSON spacing. If the register's purpose is catching fabricated citations, this row is a false positive caused by pretty-print vs. minified byte comparison; the underlying facts (`engines.node`, `_nodeVersion`, `predicateType`) are all genuinely in the source.

# Method notes
- Searched: `grep -F -b -o` on raw bytes; `html.escape(quote)` variants; `html.unescape(doc)` rendering (identical — document contains no HTML entities; tag-stripping N/A for JSON).
- Near-miss scan: searched each bare key (`"engines"`, `"_nodeVersion"`, `"predicateType"`, `22.19.0`, `24.18.0`, `slsa.dev`) to locate canonical locations; byte offsets above are `bytes.find()` results, verified by parsing the JSON.

# Tooling
- No installs performed; used stock curl/python3/grep/sha256sum/file.
