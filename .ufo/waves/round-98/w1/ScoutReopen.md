# ScoutReopen — round 98, wave w1, C14 candidate re-opened independently

Seat: `ScoutReopen` (scout). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Claims read in full from `reports/round-98/claims.md` (frozen at `9d49002a3804de48d365b7d32849ada06745d64f`).
Subject: `corpus/knowledge/round-98-rea-host-readiness.md` (admission-status `candidate`) and rows
`S506` / `S507` (`corpus/SOURCES.md:523` / `:524`).

Read-only seat: nothing under `corpus/`, `reports/round-9[0-7]/`, `reports/round-98/claims.md`,
`reports/round-98/controls/`, `reports/round-98/quote-receipts/` was edited. No counter was run on any
tree with C14 held. No `rea setup`, no campaign tool run in `/home/vgpnk/Projects/shokuknow`.

Evidence copies kept in this wave dir: `S506.refetched.body`, `rea-doctor-live.txt`,
`rea-inspect-live.txt`, `assimilation-{reg-ids,staged-ids,collisions}.txt`.
Scratch `/fast/scratch/hyaku/revenger-r98/ScoutReopen/` deleted at yield.

**Tools installed or upgraded: none.** No `pacman`, no `uv tool`, no `npx`, no binary download.

---

## A. S506 — independent re-open of the pinned URL

Fetched myself into scratch (2026-11-05), not read from the committed receipt.

| # | Expected | Observed | Verdict | Command |
|---|---|---|---|---|
| A1 | HTTP 200 | HTTP 200 | MATCH | `curl -sS -o S506.fetched.md -w '%{http_code}' 'https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md'` |
| A2 | 16650 bytes (receipt `length`, row anchor) | 16650 | MATCH | `wc -c S506.fetched.md` |
| A3 | sha256 `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50` (receipt `fetch_sha256`, row anchor, entry derivation table) | same | MATCH | `sha256sum S506.fetched.md` |
| A4 | fetched body byte-identical to committed `reports/round-98/quote-receipts/raw/S506.body` | `cmp` silent, exit 0 | MATCH | `cmp S506.fetched.md reports/round-98/quote-receipts/raw/S506.body` |
| A5 | receipt span 7126–7202 holds the anchor quote | `text[7126:7202]` == `"Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra."` (76 chars), norm-equal | MATCH | python slice + `corpus/audit_source_quotes.py` rule |
| A6 | receipt quote == last double-quoted segment of the S506 anchor cell | both = `Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra.` | MATCH | `python3` `anchor_quote()` over `corpus/SOURCES.md:523` cell 6 |
| A7 | committed quote audit passes for S506 | `S506 terminal=S506 state=verified (ok)`, `SUMMARY rows=1 verified=1 unreachable=0 unresolved=0`, exit 0 | MATCH | `python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-98/quote-receipts --sid S506` |

### A8 — every quoted sentence in the entry, counted in the fetched body

`grep -cF` against `S506.fetched.md` (count; line):

| Quoted string in the entry | count | body line | verdict |
|---|---|---|---|
| `"Doctor checks registration; it cannot establish the current agent's connection."` | 1 | 22 | MATCH (remedy-table row `Aligned registration, but no connected tools`) |
| `"Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra."` | 1 | 34 | MATCH (byte-exact, one line, as the entry claims) |
| `"Inspect the actual shell PATH and launcher/runtime."` | 1 | 26 | MATCH (remedy-table row `` `rea` is missing in a child shell, or Node is incompatible ``) |
| `"Choose the remedy from the observed failure"` (entry `source:` header anchor) | 1 | 16 (heading `## Choose the remedy from the observed failure`) | MATCH |
| `"This checks configuration, not whether a selected APK fits in the worker's memory."` | 0 in S506 body / **3 in the S507 doctor record** | doctor `:65`, `:161`, `:236` | MATCH — the entry attributes this quote to the doctor record (S507), not to S506; not a defect |
| `21.0.13` | 0 in S506 body / 3 in the doctor record, 3 in host-probes | — | MATCH — same attribution, not an S506 quote |

Command: `grep -cF -- "<quote>" S506.fetched.md` and the same over `corpus/live/runs/round-98/rea-doctor-r98.txt`.

### A9 — the entry's third S506 row is marked as a paraphrase, with a body line span

Entry: "native decompilation, Android analysis and firmware extraction each have their own
bring-your-own prerequisites (paragraph after the remedy table, body lines 35–37)". Body lines
35/36/37 = `HAR inspection is offline and does not require a live browser. Native` /
`decompilation, Android analysis and firmware extraction have their own` /
`bring-your-own prerequisites. Use supported inventory/static evidence when it`. The sentence really
does wrap across lines 35–37. **MATCH** (paraphrase is honestly marked, span is right).

### A10 — observation on the anchor wording (precision note, not a mismatch)

Both the frozen S506 registry anchor cell and the frozen entry header say the sentence sits in the
"paragraph after the remedy table". The remedy table ends at body line 26; body lines 28–32 are the
paragraph immediately after it, and the quoted sentence is in the *next* paragraph (lines 34–40). The
quote itself is byte-exact and the audit tool's last-quoted-segment rule resolves to the same string,
so nothing fails. Recorded as a wording-precision note for the L1; not a MISMATCH against any frozen
predicate.

---

## B. S507 — record re-opened, derivation table re-derived row by row

### B1 — S507 anchor byte span

Expected: `corpus/live/runs/round-98/rea-doctor-r98.txt` lines 1–2, 1-based bytes 1–41 =
`healthy: false` / `environment_healthy: false` (row 524 anchor cell).

Observed: `head -c 41 corpus/live/runs/round-98/rea-doctor-r98.txt | od -c` →
`healthy: false\nenvironment_healthy: false`, exactly 41 bytes, no trailing newline inside the span.
**MATCH.**

### B2 — every row of the entry's derivation table, re-run from the lane root

All commands run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`, exactly as written in the
entry.

| Row | Expected (entry) | Observed | Verdict | Command |
|---|---|---|---|---|
| doctor verdict lines | `healthy: false` / `environment_healthy: false` | identical | MATCH | `sed -n 1,2p corpus/live/runs/round-98/rea-doctor-r98.txt` |
| scope-check count | `11` and `13` (24 scope checks) | `11`, `13`, total scope checks `24` | MATCH | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -c '    ok: true'` and `ok: false` |
| scope-check classes | `10 config_drift` / `11 healthy` / `3 missing_analysis_engine` | identical | MATCH | `… \| grep -oE 'classification: [a-z_]+' \| sort \| uniq -c` |
| registration states | `antigravity missing claude_code missing codex aligned copilot_cli missing cursor missing devin aligned gemini_cli missing grok_bot manual grok_build aligned kimi missing omp stale opencode missing pi missing zcode aligned` | identical, one pair per line | MATCH | `awk '/^    - client:/{c=$3} /^      state:/{print c, $2}' corpus/live/runs/round-98/rea-doctor-r98.txt` |
| CLI package version | `  cli_package_version: 6.7.0` | identical (leading 2 spaces kept) | MATCH | `grep cli_package_version corpus/live/runs/round-98/rea-doctor-r98.txt` |
| inventory Evidence ID | `evidence_id: ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382` | identical | MATCH | `grep -m1 evidence_id corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt` |
| inventory substep status | `      status: completed` | identical (6-space indent) | MATCH | `grep -m1 'status: completed' corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt` |
| inventory member sizes | `declared_size: 2964` / `84` / `16160` (root, README.txt, bin/checksum in record order) | identical, and record order is root → README.txt → bin/checksum | MATCH | `grep -E 'declared_size: ' corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt \| sed 's/^ *//'` |
| fixture digest | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` | identical | MATCH | `sha256sum corpus/fixtures/archive-r2/fixture.zip` |
| record file digests | `94eaa6ff…` (host-probes-r98.txt), `fb9a4824…` (rea-doctor-r98.txt), `c373f656…` (rea-inspect-artifact-archive-r2.txt) | identical prefixes, same file order | MATCH | `sha256sum corpus/live/runs/round-98/*` |
| S506 body digest | `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50` (16650 bytes) | identical | MATCH | `sha256sum reports/round-98/quote-receipts/raw/S506.body`; `wc -c` → 16650 |

**11 of 11 derivation rows MATCH.** No row of the table is stale.

### B3 — route-decision-table claims checked against the record (not in the derivation table)

| Entry claim | Observed | Verdict |
|---|---|---|
| doctor receipt is REA CLI 6.7.0 | `cli_package_version: 6.7.0` | MATCH |
| `rea doctor` exited 1 | live run exit 1 | MATCH |
| eight ghidra scope checks healthy: ghidra, ghidra-platform, ghidra-architecture, ghidra-installation, ghidra-version 12.1.4, ghidra-headless, ghidra-native_decompiler, ghidra-java 21.0.13 | all eight present, `ok: true`, `classification: healthy`; `ghidra-version` detail `12.1.4`; `ghidra-java` detail `21.0.13; 64-bit; JDK; …` | MATCH |
| `command -v analyzeHeadless` exited 1, launcher not on PATH, doctor finds it under the install dir | live rc=1; doctor `ghidra-headless` detail `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/support/analyzeHeadless` | MATCH |
| hopper, ida-registration, kuna-installation reported as `missing_analysis_engine` | exactly those three carry `missing_analysis_engine` | MATCH |
| `command -v hopper`, `command -v idat64` exited 1 | live rc=1 each | MATCH |
| jadx healthy; its detail says "This checks configuration, not whether a selected APK fits in the worker's memory." | `jadx` `ok: true`, `classification: healthy`; that sentence present in the detail | MATCH |
| `jadx --version` → 1.5.6; `java -version` → openjdk 21.0.13 | live identical | MATCH |
| binwalk 3.1.0, unblob 26.6.4, both exit 0; doctor has no binwalk/unblob check | live identical; `grep -ci binwalk` = 0 and `grep -ci unblob` = 0 in the doctor record | MATCH |
| 14 client registrations: 4 aligned (codex, devin, grok_build, zcode), 8 missing, 1 manual (grok_bot), 1 stale (omp) | the awk listing gives exactly 8 missing, 4 aligned, 1 manual, 1 stale = 14 | MATCH |
| installed skill identity `stale` | `skill:identity` `ok: false`, `classification: config_drift`, detail "Installed REA skill identity is stale." | MATCH |
| `rea --version` → 6.7.0; `command -v rea` → per-shell `fnm_multishells` path; doctor lists three such paths, `state: multiple` | live identical; doctor `paths[3]` = three fnm_multishells paths, `state: multiple` | MATCH |
| `python3 -c 'import pwn'` exited 0; "corrects the 2026-10-19 re-probe row K05, which recorded the import as failing" | live rc=0; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:40` K05 (2026-10-19 table) reads "pwntools import fails | STALE → 3 of 4 present" | MATCH (note: the checklist's later 2026-11-04 table at `:61` already recorded "pwntools imports"; the entry's wording is about the 2026-10-19 row specifically and is accurate) |
| ZIP inventory: `inspect_artifact` → `inventory_artifact`, `status: completed` | record line 28–29 `operation: inventory_artifact` / `status: completed` | MATCH |
| members README.txt 84 B, bin/checksum 16160 B, root digest match `fixtures/archive-r2/truth.json` | truth.json: `archive_sha256` = 857989f5…, `archive_size` 2964, README.txt size 84 sha 7d8f6a8d…, bin/checksum size 16160 sha f5ba0697…; the record carries the same three digests | MATCH |
| Hopper was absent during the run | doctor reports hopper missing; `command -v hopper` rc=1 | MATCH |

---

## C. Live drift check (read-only `rea` commands, never `rea setup`)

| Item | Committed record | Live run today | Verdict |
|---|---|---|---|
| `rea doctor` (stdout+stderr, from the lane root) | `corpus/live/runs/round-98/rea-doctor-r98.txt` | byte-identical, `cmp` exit 0 (398 lines each) | MATCH — **zero drift** |
| `rea doctor` exit code | entry: 1 | live exit 1 | MATCH |
| `rea inspect-artifact corpus/fixtures/archive-r2/fixture.zip` | `corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt` | byte-identical, `cmp` exit 0 | MATCH — **zero drift** |
| inspect exit code / Evidence id | entry: exit 0, `ev_0ef6c8cd…` | live exit 0, same `evidence_id` | MATCH |
| host probes in `host-probes-r98.txt` (13 commands, recorded outputs and exit codes) | `rea --version` 6.7.0, `command -v rea` fnm path, node v24.21.0, npm 11.19.0, binwalk 3.1.0, unblob 26.6.4, jadx 1.5.6, java 21.0.13, `command -v analyzeHeadless` rc=1, `command -v ghidra` /usr/bin/ghidra rc=0, `command -v idat64` rc=1, `command -v hopper` rc=1, `import pwn` rc=0 | every value and exit code reproduced live | MATCH — no drift note needed |

No wall-clock or path-only differences arose: the live outputs are byte-equal to the committed ones.

---

## D. Vote-binding digest and header shape (read-only, for the counter author)

| Item | Expected | Observed | Verdict | Command |
|---|---|---|---|---|
| normalized digest (v6 `digest()` rule: every `admission-status` line normalized to `admission-status: candidate`) | `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8` | identical | MATCH | `python3` with `re.sub(r"(?im)^\s*admission-status\s*:.*$","admission-status: candidate", text)` then sha256 |
| `admission-status` occurrences in the entry | exactly 1 | exactly 1, at line 6 | MATCH | `grep -nE '^\s*admission-status\s*:' corpus/knowledge/round-98-rea-host-readiness.md` |
| header trio present in the head window | `source:`, `verified-at:`, `recheck:` | lines 1 (S506), 2 (S507), 3, 4 | MATCH | head -6 of the entry |

**Interface note for the counter author (not a defect):** the entry carries **two** `source:` lines
(S506 at line 1, S507 at line 2) plus `verified-at:` (3), `recheck:` (4), `coverage-map:` (5),
`admission-status:` (6). Any new `C1_HEADER_POSITION` leg must accept two `source:` lines, since the
entry text is frozen under the binding digest above.

**Used-by grounding for the two new rows** (input to the new `C1_USEDBY_GROUNDED` leg): S506 and S507
both carry `used-by = corpus/knowledge/round-98-rea-host-readiness.md`, and that entry does cite both
(`grep -c S506` = 11, `grep -c S507` = 3). Grounded.

**Still-ungrounded row at the freeze commit (known mined defect, not this round's row set):**
`S505` (row 522) has `used-by = corpus/knowledge/round-96-native-analysis-sessions.md`, and that file
never cites S505 (`grep -c S505` → 0, exit 1). This is the r97 defect the claims name as this round's
mistake; it matches `reports/round-98/controls/s505-ungrounded-count.txt` (507 registry rows, 471
mined-with-used-by rows, 470 grounded, 1 ungrounded = S505). The correction is a sibling seat's
scope; I did not touch it.

---

## E. Assimilation — package presence and id-collision recipe

Package **exists** at `/home/vgpnk/Projects/shokuknow/merge/revenger` (read-only inspection; nothing
written there):

```
MERGE-REPORT.json   44638 B  sha256 (not hashed — md only)
MERGE-REPORT.md     22437 B  sha256 924d23a514afc82814860a60056cff11b7ac3530e150f4d4f8d22e9580a085ff
SOURCES.append.md  129727 B  sha256 d845829efcee876288b8a67a992c4a60239ef86078aa04ae13b8171146c9fd7a
knowledge/corpus/knowledge/   87 staged knowledge files
```

Id-collision recipe (the r97 recipe: derive registry ids from the lane `corpus/SOURCES.md`, derive
staged ids from the package `SOURCES.append.md`, intersect), run into scratch only:

| Item | Expected (r97 claim) | Observed today | Verdict | Command |
|---|---|---|---|---|
| staged rows | 155 | 155 | MATCH | `grep -cE '^\| S[0-9]+ ' merge/revenger/SOURCES.append.md` |
| staged id range | S047 … S201 | S047 … S201 | MATCH | sorted unique ids |
| lane registry rows | 504 at r97 | **507** today (S505, S506, S507 added since) | drift note, expected | `grep -oE '^\| S[0-9]+ ' corpus/SOURCES.md \| sort -u \| wc -l` |
| collisions (staged ∩ registry) | 155 | **155** | MATCH | `comm -12 reg-ids staged-ids \| wc -l` |
| all staged ids collide? | yes | yes, 155/155, file byte-identical to r97's `assimilation/collisions` (`diff` exit 0) | MATCH | `diff` against `.ufo/waves/round-97/assimilation/collisions` |
| staged ids file unchanged vs r97 | — | `diff` exit 0 (package not re-staged) | MATCH | `diff` against `.ufo/waves/round-97/assimilation/staged-ids` |
| staged knowledge entries | 87 | 87 | MATCH | `ls merge/revenger/knowledge/corpus/knowledge/ \| wc -l` |

Package mtimes are 2026-10-24 23:33 for all four entries — the package has **not** been re-staged
since the r97 observation, so the round-97 collision (155/155 staged ids collide) stays open on L0 and
nothing is adopted. The package's own `MERGE-REPORT.md` still says "lane registry currently holds
46 rows; first staged id is S047" — stale package prose, not a lane fact.

---

## F. Bottom line

- **S506 re-opened independently and verified**: HTTP 200, 16650 bytes, sha256 matches the receipt and
  the committed body byte-for-byte, receipt span 7126–7202 resolves to the quoted sentence, the
  committed quote audit passes, and every quote the entry attributes to S506 occurs exactly once in
  the body at the line the entry names.
- **S507 re-opened and re-derived**: the anchor byte span (1–41) matches, and **all 11 rows of the
  entry's derivation table re-derive exactly**; the route-decision table's additional claims all
  check out against the saved record.
- **Live drift: none.** `rea doctor` and `rea inspect-artifact` reproduce the committed records
  byte-for-byte, and all 13 host probes reproduce their recorded outputs and exit codes.
- **Assimilation**: package present (155 staged rows, 87 staged knowledge files, unchanged since
  2026-10-24); 155/155 staged ids collide with the lane registry (507 rows today) — the r97 collision
  remains open on L0, nothing adopted.
- **MISMATCHES found: 0.** Two precision notes for the L1: (i) the S506 anchor wording "paragraph
  after the remedy table" points one paragraph past the table (the quote is in the second paragraph,
  body lines 34–40) — the quote and span are nonetheless exact and every machine check passes;
  (ii) the frozen entry has two `source:` header lines, which the new `C1_HEADER_POSITION` leg must
  accept given the binding digest.

## G. Open questions for the L1 (interface only)

1. Should `C1_QUOTE_BYTES` treat the S506 span as the receipt's 0-based half-open slice
   (`text[7126:7202]`, as `corpus/audit_source_quotes.py` does) or as 1-based inclusive bytes
   (the quote is 1-based bytes 7127–7202)? The registry anchor cell says "body bytes 7126-7202"
   without a base, while the S507 cell says "1-based bytes 1-41". Today both readings pass the
   committed audit; the leg should pick one and apply it to S506 and S507 alike.
