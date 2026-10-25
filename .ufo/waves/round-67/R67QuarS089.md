ABSENT — fetch succeeded (HTTP 200, real document bytes, 63,884 B) and BOTH quoted strings are fixed-string absent from raw and every HTML-unescaped/tag-stripped rendering; the fabrication-class confirmation stands, and no near-miss exists in the page at all.

# Quarantine hand-check — register row S089 (wave-4, item 10)

Seat: R67QuarS089 · checked 2026-10-24 (fetch stamp 2026-10-25T00:33:25Z) · read-only hand-check, no production edits.

## Register row (verbatim, /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md line 160)

> `revenger` | round3 | S089 | `payload-absent` | https://learn.microsoft.com/ja-jp/visualstudio/debugger/decompilation?view=visualstudio | `Re:birth the fidb: Reverse Engineering the .NET AOT Malware`<br>`Ready To Run` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |

(grep of id `S089`; sibling rows S087/S090/S092/S093 shown for context, untouched.)

## Fetch receipt

Command: `curl -sL --max-redirs 15 -D headers -w ... -o /tmp/r67S089_source.bin 'https://learn.microsoft.com/ja-jp/visualstudio/debugger/decompilation?view=visualstudio'` (first try; no retries needed)

- FINAL_URL: `https://learn.microsoft.com/ja-jp/visualstudio/debugger/decompilation?view=visualstudio` (no redirect off-target)
- HTTP_CODE: 200 · content-type: `text/html` · content-length: 63884
- byte size: 63,884 (≤ 2 MB → full bytes saved)
- sha256: `a64d1eb230b4c05a67a97327a334e1730e4cfc821f9c3887812fa8d18f9080be`
- etag: `"knB/E8B3L2fHGhfiubC5awc3R08="` · last-modified: `Wed, 14 Oct 2026 19:44:40 GMT`
- fetched_at: 2026-10-25T00:33:25Z
- artifact: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S089/source.bin` (copy re-hashed identically)

Real-document evidence (not a JS shell / consent page): `<title>` = `デバッグ中に .NET コードを逆コンパイルする - Visual Studio (Windows) | Microsoft Learn`; `<h1>` = `デバッグ中に .NET アセンブリからソース コードを生成する`; body contains `逆コンパイル` ×26 and `.NET` ×13.

## Per-string verdicts

### `Re:birth the fidb: Reverse Engineering the .NET AOT Malware` — ABSENT

- raw `grep -Fob -e 'Re:birth the fidb: Reverse Engineering the .NET AOT Malware'`: exit 1, no match.
- Python renderings (all zero hits, case-sensitive): raw; tags→space + `html.unescape`; `html.unescape` + tags→''; whitespace-collapsed reading order.
- Escaped/URL variants in raw bytes (`Re%3Abirth`, `Re&#58;birth`): exit 1, no match.
- Case-insensitive scan of all four renderings (`re.escape` under `re.I`, plus token regex `re\s*[:：]\s*birth`, `fidb`): NONE.

### `Ready To Run` — ABSENT

- raw `grep -Fob -e 'Ready To Run'`: exit 1, no match.
- Python renderings (all zero hits, case-sensitive): same four renderings as above.
- Escaped/URL variants in raw bytes (`Ready%20To%20Run`, `Ready+To+Run`, `Ready%20to%20Run`): exit 1, no match.
- Case-insensitive scan of all four renderings, including boundary-tolerant `ready\s*to\s*run` and the joined form `readytorun`: NONE.

## Near-miss

None found. The page contains neither string nor any of their key tokens in any casing across raw and all stripped/unescaped renderings — not even `ReadyToRun`/`Ready to Run` or `AOT`, which the cited Japanese VS-debugger decompilation doc never mentions. So the register's absence claim is not merely right about the exact strings; there is no distorted true sentence to name on this page. [INFERENCE] The quoted strings read like a malware-analysis talk title and the .NET R2R term — plausibly a wrong-source transcription (the register's companion URLs may carry the true carrier document), which does not affect this verdict: the cited source is clean of both.

## Verdict

Row S089 (`payload-absent`, round3): **ABSENT — confirmed**. Fetch succeeded with real document bytes; every quoted string is missing from the fetched bytes under fixed-string, case-sensitive, escaped/unescaped, and tag-stripped search. Fabrication-class confirmation stands.

## Scope, limits, tooling

- Re-derived absence for the cited source only; companion URLs and local artifacts were NOT re-checked (register note claims they were checked; out of this seat's scope, no conflict observed).
- Single-fetch freshness: 2026-10-25T00:33:25Z snapshot; etag/last-modified above allow future re-validation.
- `/home/vgpnk/Projects/shokuknow` was only read (register grep); no writes anywhere outside `quarantine/S089/` and this report.
- Tooling directive: no installs/updates performed — used pre-existing system `curl` and `python3`.
