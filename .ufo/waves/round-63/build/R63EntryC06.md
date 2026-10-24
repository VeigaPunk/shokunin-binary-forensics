# R63EntryC06 — C06 candidate entry, second bounded correction (EDITs 1–5)

Seat: `revenger-r63.R63EntryC06` (scribe, build wave, round 63, correction pass 2).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Date: 2026-10-23.

## Result

Corrected entry: **`/tmp/revenger-r63-entry/candidate2.md`**
sha256 **`285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1`**, 86999 bytes.
Superseded: `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53` (pass 1), `630b974a…`/`dcfe131c…` (pre-correction). No other file was touched; nothing was written under `corpus/`.

| artifact | path | sha256 | size |
|---|---|---|---|
| corrected entry (pass 2) | `/tmp/revenger-r63-entry/candidate2.md` | `285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1` | 86999 B |
| readout script (embedded verbatim) | `/tmp/revenger-r63-entry/readout.py` | `8dbefe4dae2fd170d4bd658c4d1111e66a15b266687fe586e385d9aab74c367f` | 329 lines |
| readout stdout (embedded verbatim) | `/tmp/revenger-r63-entry/readout.stdout.txt` | `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5` | 17 lines |

## Per-edit before → after

**EDIT 1 (Q11 false output).** *Before:* §Reproduce printed `wc -w` → **8** for the quote `local file header signature 4 bytes (0x04034b50)`. *After:* the printed output is **7**, the real return of `printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w`. Verified by re-running that exact command and by re-running **all ten** quoted-string word counts: every printed value now equals the command's real output (0 failures). The other nine counts were already correct and are unchanged.

**EDIT 2 (Q01 scope lag).** *Before:* every §4.3.7-based citation named **S032**, whose registry scope covered only the central-directory and end-of-central-directory layouts; the LEDGER.md provenance citations named a bare path with no row. *After:*

- **S032** now carries only the central-directory and end-of-central-directory claims. Its header `source:` line's scope reads "the central directory file header and end-of-central-directory record field layout"; its anchors list §4.3.12, §4.3.16, §4.3.3, §4.4.7, §4.4.10–4.4.12, §4.4.16, §4.4.21–4.4.22 and **no longer §4.3.7**; its §Sources bullet carries the eight §4.3.12/§4.3.16/§4.3.3/§4.4.7/§4.4.16 quotes and states "It is not cited for … the local file header layout (that is S034)".
- **S034** is a new `source:` header line and a new §Sources bullet: same APPNOTE URL, same document, same snapshot digest `0b993022…`/174585 bytes, scope "the local file header record field layout", anchor §4.3.7, carrying the two §4.3.7 quotes (`"local file header signature 4 bytes (0x04034b50)"` — 7 words; `"file name length 2 bytes extra field length 2 bytes"` — 10 words), both byte-verbatim in the snapshot. A copy-paste-ready registry row for L1 is included in that bullet.
- Item 5 now reads: "the local file header's widths from **S034 §4.3.7**, the central directory file header's and the end-of-central-directory record's widths from **S032 §4.3.12 and §4.3.16**".
- Items 8 and 9 (payload-offset claims) now read "the local header's 30-byte fixed part, computed from **S034 §4.3.7**'s field widths".
- The readout's own `spec_derived_field_offsets` fact now prints `source_anchor`: "APPNOTE 6.3.10 §4.3.7 local file header field table **(S034)**; §4.3.12 and §4.3.16 field tables **(S032)**", and the script's field-width comment names `S032: §4.3.12 … §4.3.16 …; S034: §4.3.7 local file header`.
- Limitation 31 now reads "**S032's** anchor is the central directory file header and end-of-central-directory record field layout, and **S034's** is the local file header record field layout".
- **S035** is a new `source:` header line and a new §Sources bullet for `corpus/live/runs/20261012T164246Z/LEDGER.md` (sha256 `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`, 3959 bytes), scope "the recorded layer for the producer invocation that produced the saved record named above". The LEDGER.md citations are repointed: item 2 names "the run's ledger `corpus/live/runs/20261012T164246Z/LEDGER.md` (**S035**)"; item 13 names it "(**S035**; sha256 …)"; the recorded-not-authenticated and manual-analysis limitations name it "(**S035**)"; the Q04 basis names it "(**S035**)".
- **S033** now covers the fixture bytes, the oracle and the saved record only; `LEDGER.md` is removed from its paths and its proposed registry row text.
- The Q01 basis now states the scope mapping explicitly: "no local-header-layout claim cites S032, and no central-directory or end-of-central-directory claim cites S034. No claim in this entry rests on a row outside those four." Q02 now says "four rows".
- §Sources bullets are ordered S032, S033, S034, S035.

**EDIT 3 (Q11 — zipfile digest).** *Before:* the excluded page's digest `9520a8cb…` and size 139782 were stated as prose only. *After:* §Reproduce carries a new measurement block with command and printed output — `wc -c .ufo/waves/round-63/source-snapshots/zipfile.html` → `139782 …`; `sha256sum …zipfile.html` → `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739  .ufo/waves/round-63/source-snapshots/zipfile.html`. Both re-run and match.

**EDIT 4 (Q11 — S032 revision facts).** *Before:* "6.3.10 / FINAL / Nov 01 2022" was prose only. *After:* §Reproduce carries the command `tr -d '\r' < .ufo/waves/round-63/source-snapshots/appnote.txt | head -5` with its exact five printed lines (the `tr` is needed because the snapshot is CRLF-served; the printed `Version: 6.3.10 ` line keeps its trailing space exactly as the command emits it). The §Sources bullet now marks the revision facts as read from the snapshot's own header lines, and the inventory lists them under the **recorded** kind.

**EDIT 5 (Q11/H6 — inventory overclaim).** *Before:* "Every factual sentence above maps to a command that prints it and to the output that command printed." *After:* the inventory states the split exactly: every factual sentence is of one of two kinds — **Derived** (the readout's `--fact` command form, plus the file-measurement commands `sha256sum`, `wc -c`, `wc -l`, `head` whose outputs are printed in §Reproduce for the script, the stdout, the APPNOTE snapshot, the zipfile snapshot and the fixture/oracle/record/ledger files) or **Recorded** (the saved record's Evidence IDs, operation, provider id and version, subject digest and `executable`/`encrypted`/`hash_status` values — S033; the run ledger's recorded producer invocation — S035; the oracle's recorded values including its `build` string — S033; and the APPNOTE document's own version/status/revision-date header lines, read from the snapshot by the printed `tr -d '\r' … | head -5` command and recorded from that document rather than derived from the archive). It closes with "No other kind of value is asserted, and the sentence above makes no claim beyond these two kinds."

## Re-run evidence

| check | result |
|---|---|
| `python3 -B readout.py <repo-root>` | **exit 0**, 17 stdout lines, sha256 `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5` |
| all 17 `--fact` invocations | **exit 0** each; every block printed in the entry byte-identical to a fresh run (**0 mismatches**) |
| stdout block in the entry vs fresh run | identical; stated line count 17 = actual; stated digest = actual |
| script metadata block | stated `8dbefe4d…` / 329 lines = actual |
| **every** `$` command block in the entry, re-executed | 24 blocks run, **0 failures** (the `readout.py .` block's stdout is the following separate block, verified identical) |
| ten quoted-string `wc -w` counts, re-executed | 10 / **0 failures** (EDIT 1's value now 7) |
| zipfile measurement block, re-executed | `139782` and `9520a8cb…` = actual |
| APPNOTE revision block, re-executed | the five header lines = actual |
| embedded script extracted from the entry | **exit 0**, reproduces `ccaffa32…`, bytes identical to `readout.py` |
| citation-scope audit | **no** local-header-layout claim cites S032; S032 §-sections = {§4.3.12, §4.3.16, §4.3.3, §4.4.7, §4.4.16}; S034 §-sections = {§4.3.7} only; every `LEDGER.md` mention is S035-attributed or a bare path inside a hash command whose prose lead-in names S035 |
| §Sources bullet order | S032, S033, S034, S035 (ascending) |

## Final citation counts

| row | occurrences in the entry | scope as cited |
|---|---|---|
| **S032** | 13 | central-directory and end-of-central-directory record field layout (§4.3.12, §4.3.16, §4.3.3, §4.4.7, §4.4.16) |
| **S033** | 11 | the authored fixture bytes, the authored oracle and the saved archive-inventory record |
| **S034** | 15 | the local file header record field layout (§4.3.7) |
| **S035** | 11 | the run's ledger — the recorded layer for the producer invocation |

## Scope of the claim after correction

Unchanged from the previous pass except for the citation-scope repair: the entry claims the three fixed records' field layout, the values those records state for this one fixture, the independently recomputed inflated payload digests and CRC-32 values, agreement with the authored oracle on the enumerated fields, and correspondence with one saved record's literal fields. Each of those now names the registry row whose scope covers it. `claims.md` is unchanged and unweakened.

## Out of scope / not done

- No `corpus/` write: `corpus/knowledge/round-63-zip-central-directory-evidence.md` is not created (L1 lands `candidate2.md`); `corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md` untouched; the README C06 flip stays L1's, after fresh falsify decisions.
- No fixture/oracle/record/ledger byte modified; no target execution; no network; no producer invocation; no git/jj mutation, commit or push; no model arguments; no routing-table edit.
- No tool installed or upgraded.
- The four registry rows S032/S033/S034/S035 are cited with their scopes and their proposed row texts; **the rows themselves are L1's to append** — this seat did not edit `corpus/SOURCES.md`.

## Artifacts

| path | what |
|---|---|
| `/tmp/revenger-r63-entry/candidate2.md` | the corrected C06 candidate entry (pass 2) |
| `/tmp/revenger-r63-entry/readout.py` | the readout script, embedded verbatim in the entry |
| `/tmp/revenger-r63-entry/readout.stdout.txt` | its exact stdout, embedded verbatim in the entry |
| `/tmp/revenger-r63-entry/template.md` | the symbolic template (item numbering and cross-references resolved at generation) |
| `.ufo/waves/round-63/build/R63EntryC06.md` | this report |
