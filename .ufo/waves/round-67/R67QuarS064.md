ABSENT — fetch succeeded (HTTP 200, 41,372 real arXiv bytes) and both quoted strings are missing from every rendering (raw, entity-unescaped, tag-stripped, escaped variants, case-insensitive), confirming the register's absence claim (fabrication-class); likely distortion of the abstract's only obfuscation sentence ("robust under commercial obfuscation (F1 84% post-obfuscation)").

# Quarantine hand-check — register row S064 (wave-4, item 10)

Seat: R67QuarS064 · Date: 2026-10-24 · Lane: revenger-shokunin (quarantine-first, round 67)

## Register row (read-only source, verbatim)

`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` line 154 (marked `*`):

```
*154|| `revenger` | round1 | S064 | `payload-absent` | https://arxiv.org/abs/2510.14344 | `our analysis revealed that over 87% of benign apps and 96% of malicious/undesired apps employ obfuscation`<br>`… XML features are susceptible to manifest manipulation` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

Class: `payload-absent` · Cited source: https://arxiv.org/abs/2510.14344 · The register claims both quoted strings are ABSENT from the source. Re-derived below.

## Fetch receipt

Command (try 1 of 3 allowed; succeeded first try):

```
curl -sL --max-redirs 15 --max-time 90 -o <scratch>/source.bin -w 'HTTP=%{http_code} SIZE=%{size_download} FINAL=%{url_effective}\n' https://arxiv.org/abs/2510.14344
```

Output:

```
HTTP=200 SIZE=41372 FINAL=https://arxiv.org/abs/2510.14344
e544ec87debc586cf000e0dbb05ec749b3ab0b911506fbee7b3ed5ba151feb7a  <scratch>/source.bin
BYTES=41372
```

- HTTP 200, 41,372 bytes ≤ 2 MB → bytes saved at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S064/source.bin` (sha256 `e544ec87debc586cf000e0dbb05ec749b3ab0b911506fbee7b3ed5ba151feb7a`).
- `<title>` of fetched document: `[2510.14344] BinCtx: Multi-Modal Representation Learning for Robust Android App Behavior Detection` — real arXiv abs landing page, not an error/consent page.
- Page contains HTML entities (html.unescape output ≠ raw text), so unescaped search was required and performed.

## Per-string absence results

Search modes per string: (a) fixed-string in raw bytes (Python `bytes.find` + grep-tool fixed-regex pass), (b) raw decoded text, (c) `html.unescape`d text, (d) tag-stripped + whitespace-normalized (covers `&nbsp;`/cross-tag splits), (e) escaped variants of the string searched in raw and unescaped text, (f) case-insensitive pass. All byte offsets are `find()` results; `-1` = not found.

### Q1: `our analysis revealed that over 87% of benign apps and 96% of malicious/undesired apps employ obfuscation`

| mode | result |
|---|---|
| raw bytes / raw text / unescaped / tag-stripped+norm | -1 / -1 / -1 / -1 |
| escaped variants (`html.escape` q=F/q=T, `/`→`&#x2F;`, `/`→`&#47;`) in raw and unescaped | all -1 |
| case-insensitive in stripped text | not found |

grep-tool fixed-regex pass over `source.bin`: `No matches found`.

### Q2: `… XML features are susceptible to manifest manipulation` (leading char U+2026)

| mode | result |
|---|---|
| raw bytes / raw text / unescaped / tag-stripped+norm | -1 / -1 / -1 / -1 |
| escaped variants (`html.escape`, `…`→`&hellip;`, `…`→`&#8230;`, `…`→`&#x2026;`) in raw and unescaped | all -1 |
| case-insensitive in stripped text | not found |

grep-tool fixed-regex pass over `source.bin`: `No matches found`.

## Near-miss findings (what the source actually says)

Fragment sweep over the tag-stripped page (case-insensitive): `87%` 0 hits, `96%` 0 hits, `manifest manipulation` 0 hits, `XML features` 0 hits, `susceptible` 0 hits, `our analysis` 0 hits, `employ obfuscation` 0 hits; `obfuscat` exactly 2 hits, both the same abstract sentence:

> "It remains robust under commercial obfuscation (F1 84% post-obfuscation) and is more resistant to adversarial samples than state-of-the-art bytecode-only systems."

Probable distortion source: Q1 invents an "87% of benign / 96% of malicious employ obfuscation" prevalence statistic that exists nowhere in the fetched document; the paper's only obfuscation claim is the BinCtx robustness figure above (84% post-obfuscation F1). Q2 has no counterpart at all — the abstract's only ellipsis is "The three views are embedded and fused …", and the words "XML", "manifest manipulation", and "susceptible" never appear (closest real concept: "manifested actions, components, declared permissions" in the contextual-view description).

## Verdict

- Q1: ABSENT. Q2: ABSENT. Row S064 verdict: **ABSENT** (fabrication-class confirmation) per the verdict rules — fetch succeeded with real document bytes and every quoted string is missing.
- Register note ("the quote is in none of them") re-derives as true for the cited source.

## Scope limits and bounds compliance

- The cited URL is the arXiv abs landing page (metadata + abstract, 41,372 bytes); the paper's full text (HTML/PDF rendition) was NOT fetched — fetch authorization is the assigned URL only. The verdict is scoped to the fetched bytes per the brief's verdict rules; full-text absence beyond this page is not re-derived here (register states companion URLs were already checked).
- Writes: only this report and the scratch dir `.ufo/waves/round-67/quarantine/S064/` (source.bin). `/home/vgpnk/Projects/shokuknow` accessed read-only. No git/jj mutations, no peer messaging.
- Tooling directive: no tools installed or upgraded (curl/python3 sufficient). Nothing to record.
