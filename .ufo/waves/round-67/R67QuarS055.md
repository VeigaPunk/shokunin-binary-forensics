PRESENT — the quoted string occurs verbatim 3× in the fetched ECMA-335 page bytes (offsets 2336, 2802, 3785); the register's absence claim for row `revenger | round1 | S055` is wrong.

## Row under check

- Register file (read-only): `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:148`
- Row: `| revenger | round1 | S055 | payload-absent | https://www.ecma-international.org/publications-and-standards/standards/ecma-335/ | ` + quoted string + ` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |`
- Register claim being re-derived: the quoted string is ABSENT from the cited source.

## Fetch receipt

- Command: `curl -sL --max-redirs 15 -w '%{http_code}' -o /tmp/r67s055_source.bin 'https://www.ecma-international.org/publications-and-standards/standards/ecma-335/'`
- Result on first try (no retries needed): `HTTP=200`, `BYTES=90253`
- sha256: `ff5aac3e441100c6a60fae539f00a75190b9309c57a7c9c5db6e16ff1a147c5e` of `/tmp/r67s055_source.bin`
- Saved artifact (≤ 2MB): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S055/source.bin` — same sha256 `ff5aac3e441100c6a60fae539f00a75190b9309c57a7c9c5db6e16ff1a147c5e`, 90253 bytes.
- Real document bytes confirmed: page contains `<title>ECMA-335 - Ecma International</title>` and body text "This Standard defines the Common Language Infrastructure (CLI) in which applications written in multiple high-level languages can be executed in different system environments…".

## Per-string results

String 1 (the only quoted string in this row):
`Common Language Infrastructure (CLI) - Defines the infrastructure in which applications written in multiple high-level l`

- Raw bytes, `grep -boF` (fixed-string, case-sensitive): **3 hits** — byte offsets 2336, 2802, 3785. exit 0.
- `html.unescape` rendering: **present** (Python `'…' in html.unescape(text)` → True).
- `html.unescape` + tag-stripped rendering: **present** (`True`).
- Escaped-variant check on raw bytes (`html.escape(quote)`): present (quote contains no escapable chars; variant identical → same hits).
- Verdict for this string: **PRESENT**.

Context at each hit (~15 words, verbatim bytes):

- Offset 2336 (`<meta name="description">`): `…<title>ECMA-335 - Ecma International</title> <meta name="description" content="Common Language Infrastructure (CLI) - Defines the infrastructure in which applications written in multiple high-level languages can be executed" /> <link rel="canonical" href="https://ecma-international.org/…`
- Offset 2802 (`<meta property="og:description">`): `…content="ECMA-335 - Ecma International" /> <meta property="og:description" content="Common Language Infrastructure (CLI) - Defines the infrastructure in which applications written in multiple high-level languages can be executed" /> <meta property="og:url" content="https://ecma-international.org/…`
- Offset 3785 (JSON-LD `"description"`): `…"dateModified":"2022-01-26T09:17:16+00:00","description":"Common Language Infrastructure (CLI) - Defines the infrastructure in which applications written in multiple high-level languages can be executed","breadcrumb":{"@id":"https:\/\/ecma-international.org\/…`

The quoted string is a character-prefix truncation of the page's own meta/og/JSON-LD description (cut mid-word at `high-level l`); the full sentence in the page is `Common Language Infrastructure (CLI) - Defines the infrastructure in which applications written in multiple high-level languages can be executed`. Three independent embeds of that description contain the quoted prefix verbatim.

## Row verdict

**PRESENT** — register class `payload-absent` is falsified for this row: the "absent" quote is copied (truncated) from the cited source itself, at 3 byte offsets. Not a fabrication; the lane's search evidently missed it (likely because the description lives in `<head>` metadata / JSON-LD rather than body text, or the trailing mid-word cut defeated a different comparison).

## Tooling / installs

None. `curl`, `grep`, `python3` (stdlib `html`, `re`) already present; no installs or updates performed. Pacman untouched per host-wide pause.

## Bounds

- Reads: register file (read-only) at `/home/vgpnk/Projects/shokuknow/...` — grep only, no writes to shokuknow.
- Writes: only this report and `quarantine/S055/source.bin` under `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/`. Scratch fetch at `/tmp/r67s055_source.bin`.
- No corpus/, reports/, LOG.md, SCORECARD.md, SHONEN.md, git, or jj mutations.
