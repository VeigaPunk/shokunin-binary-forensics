# Quarantine verdicts — revenger slice of the absent-defect register (round 92, wave 1)
Seat: `ScoutR92Quarantine` · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · date 2026-11-05.
Verdict-only: **nothing was adopted this round**.
## Exact command that produced `slice.raw`
```
awk -F'|' -v l='revenger' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $0}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md \
  > slice.raw
```
Slice rows extracted: **26** (expected 26 — matches; no rows dropped or added).
`slice.raw` is kept beside this file for re-derivation.
## Counts per verdict
| verdict | rows | meaning in this round |
|---|---|---|
| `candidate-present` | 24 | the quoted span was located verbatim in a fetched document; adoption is still CLOSED this round, so this is a verdict only |
| `refuse-absent` | 0 | fetched, quote/fact not present — fabrication class |
| `unverifiable` | 2 | prose class ('could not be fetched' / 'named no locator'), or unreachable; unreachable is NOT fabrication |
| **total** | **26** | one line per slice row |

## Fetch status of the register row's cited URL
| HTTP | rows |
|---|---|
| 200 | 25 |
| 404 | 1 |

## Location column
| located | rows |
|---|---|
| no | 2 |
| yes | 24 |

## Method

1. `slice.raw` extracted with the command above (26 rows).
2. Each row's cited URL fetched with `curl -sSL --max-time 60` into the seat scratch dir
   (`$HYAKU_SCRATCH/revenger-r92/ScoutR92Quarantine/`); HTTP code recorded per row.
3. Each document rendered into a searchable corpus: raw bytes, tag-stripped text, and
   `pdftotext` in `-layout`, `-raw` and flow modes. HTTP response headers kept separately
   (the `Content-Disposition` filename is a header, not body text).
4. Each quoted span searched against that corpus, NFKC-normalised, whitespace-insensitive,
   with the register's backslash-escaped quotes unescaped, and — for spans the register
   stored as several source lines joined by ` / ` — every fragment required present.
5. Where the register stored a *reconstructed* span (a locator fragment, a stripped
   contents-list, a one-character miscopy), the underlying claimed fact was searched
   instead and the defect recorded in the `note` column. No verdict was upgraded on a
   reconstruction without the underlying fact being located verbatim.

## Two defects found in the register itself (not in the lane's quotes)

**(a) The register's cited-URL column is off by one row against its own quoted spans.**
The upstream census (`quote-lint-full-v5.json`, `verdict: ABSENT`, `binding: id`) bound each
quoted span to the S-id of the *following* SOURCES row. In 14 of the 24 `payload-absent` rows
the span is absent from the row's own cited URL but present verbatim in the document the
row's own SOURCES line names — i.e. the neighbouring row's source. Rows and their true homes:
S053→dex-format page, S058→lac.co.jp article, S060→kanxue thread, S061→arXiv 2412.11539,
S062→arXiv 2112.02606, S075→rea-agents javascript-recovery.md, S081→RFC 6238,
S083→SWGDE 18-F-002-2.0, S085→SWGDE 18-F-003-2.0, S087→learn.microsoft ildasm page,
S089→JSAC2026 PDF, S092→NJU PDF, S095→ILSpy README, S098→developer.android.com apkanalyzer.
Two prose rows are the same defect seen from the other side: S054's cited URL (dex-format)
holds S053's spans, and S099's cited URL (apkanalyzer) holds S098's spans.

**(b) S085's cited URL is truncated at 140 characters** and returns HTTP 404. The register
row is not a fabrication candidate on that URL (unreachable ≠ fabrication); the true source
(SWGDE 18-F-003-2.0, the S086 row's URL) was resolved and both spans located verbatim there.
Recorded `fetch_status=404`, `verdict=candidate-present`.

## Rows with no quoted span (prose class)

S054 and S099 carry no quoted span — the register records only "the cited source could not be
fetched, so no quote was checked". Nothing can be located, so both are `unverifiable`, not
fabrications. Both cited URLs now fetch HTTP 200.

## Tooling

No tools were installed or upgraded for this seat. Everything used was already present:
`curl` (HTTP fetch), `pdftotext` (PDF text), `python3` 3.14.8 (parsing/matching),
`jq`, `awk`, `grep`.
