# ReviewerGate — round 97 wave w1: advisory Q01–Q17 gate audit of the C02 candidate

Target: `corpus/knowledge/round-96-native-analysis-sessions.md` (frozen at lane commit
`3b4b4e5c1d123d5fc5337ad59015b4752366854a`). This is an advisory audit against
`corpus/QUALITY.md` Q01–Q17. It is NOT a vote; no `vote.json` was written anywhere.
Axes named: quality-gate compliance (primary, the Q-table), C1-linked risk (any FAIL that
could affect the C02 partial→held admission), evidence-off command (the digest re-derivation).
All reads/pins are read-only over the lane tree at its current bytes; every `Report:` path
below is relative to `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

Tooling record: no tool installed or upgraded this seat (operator 2026-10-19 duty — read
`/home/vgpnk/.omp/agent/RULES.md` first; all legs ran on existing host `python3`, `git`,
coreutils; nothing to record).

## Vote-binding digest re-derivation (frozen command, run as given)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && PYTHONUTF8=1 python3 -B -c "import hashlib,re;t=open('corpus/knowledge/round-96-native-analysis-sessions.md',encoding='utf-8').read();n=re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t);print(hashlib.sha256(n.encode('utf-8')).hexdigest())"
2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923
exit: 0
```

**MATCH** with the frozen `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`
(`:1` exit 0). The entry's bytes (modulo the normalized admission-status line) are exactly the
voted bytes; the three r96 votes stay bound.

## Source-row checks (Q02 substrate)

`corpus/SOURCES.md` table header `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (:13).

| row | line | kind | tier | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|
| S502 | :519 | docs | A | mined | 2026-11-05 | on-release | `corpus/knowledge/round-96-native-analysis-sessions.md` (exactly once) |
| S503 | :520 | docs | A | mined | 2026-11-05 | on-release | `corpus/knowledge/round-96-native-analysis-sessions.md` (exactly once) |
| S504 | :521 | own-work | A | mined | 2026-11-05 | on-release | `corpus/knowledge/round-96-native-analysis-sessions.md` (exactly once) |

- Used-by exclusivity re-derived: `awk -F'|' '$12 ~ /round-96-native-analysis-sessions.md/'` names **exactly** S502, S503, S504 — no extra row, none missing; each names the census-form path once. Consistent with the frozen C1 predicate's "accepts the census form `corpus/knowledge/<entry>` … exactly once across the S502/S503/S504 rows".
- S502/S503 committed bodies re-hashed: `sha256sum reports/round-96/quote-receipts/raw/S502.body reports/round-96/quote-receipts/raw/S503.body` → `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24` / `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc`, sizes 38167 / 35095 (`wc -c` exit 0) — both match the row `anchor` cells and the receipts (`reports/round-96/quote-receipts/S502.receipt.json`, `S503.receipt.json` `verdict: verified`, `http_status: 200`).
- Quote spans re-checked against body bytes: S502 span [26309,26411) resolves inside `...; CLI \`rea decompile <path> --file-offset=0x... --provider ghidra\` resolves the source byte offset internally. An unr…`; S503 span [257,389) resolves inside the frontmatter "Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction." Both verified (`node -e`-free python read, exit 0).

## Q01–Q17 audit table

| Q | verdict | evidence |
|---|---|---|
| Q01 | **PASS** | Load-bearing claims split between docs sources (S502, S503 — tier A for route-doc scope, opened 2026-11-05 = the round that wrote the entry, commit `ff76743` 2026-11-05) and own-work tier A (S504 re-runnable record with digests). S002 (`~/.agents/skills/.../SKILL.md`, opened 2026-10-19) is cited as context only, never sole support. No claim rests on tier C. |
| Q02 | **PASS** | Entry :1–:7 carry `source:` (3 S-rows + S002 context with anchors — S502 anchor = "commit 12f6e09…; heading 'DOS MZ with Ghidra'; the CLI decompile sentence", not a bare homepage), `verified-at: 2026-11-05` with body-path and fetch-log pointers (both resolve: `reports/round-96/quote-receipts/raw/S502.body`, `fetch-log.md`), `recheck:` naming specific re-derivation commands, `coverage-map: C02 — native analysis sessions (decompile/disassemble providers)` matching the `corpus/README.md` C02 row (:49, currently `partial`). Header paths resolve (`ls corpus/live/runs/round-96/`, exit 0). |
| Q03 | **PASS** | Expected decompiled body `return 0x2a;` is pinned outside the record under test: `corpus/fixtures/pe-r75-headless-smoke/truth.json` (`entry_bytes_hex: "B82A000000C3"`, `expected_decompile_sha_watch: "the decompiled body contains \`return 0x2a;\`"`) committed **r75, commit `e783101` (2026-11-01)**, four days before the r96 records (commit `ff76743`, 2026-11-05). Generator asserts (`gen_pe_r75.py` :89–:104) re-derive every fixture premise. 159-byte claim: no such length claim in the entry — the 159-byte clause is n/a for Q03 (a false length claim there would be a Q14 matter; see Q14). |
| Q04 | **PASS** | Each run names tool, version, function: `rea decompile … 140001000` (CLI route), provider ghidra 12.1.4 (record :10–:13 `id: ghidra / version: 12.1.4`), `analyzeHeadless` (Ghidra 12.1.4) with the committed r75 Java postScript. The tool's own printed output (Evidence record, decompiled `.c`, doctor receipt) is scored, and the doctor's exit 1 is recorded alongside healthy:false, not reconciled away. Noted dot, not a FAIL: the record files stamp rea's own version only in the doctor receipt (`cli_package_version: 6.7.0` at :307 of `rea-doctor-r96.txt`); `rea-decompile.raw.txt` itself does not print a rea-version line — the entry's "rea 6.7.0 driving Ghidra 12.1.4" (Q-map :65) attributes the decompile run's driver from a connected receipt, not from the Evidence's own bytes. C1 impact: none (no leg of the counter reads this clause). |
| Q05 | **PASS** | Readiness claims carry command, date (2026-11-05) and observed exit for each run: decompile (exit 0, Evidence `ev_cc0b9d88…` verified in record :1), headless (exit 0; receipt log present with `INFO  REPORT` count 6 re-derived, exit 0), doctor (observed exit **1**, recorded, with `healthy: false` / `environment_healthy: false` at :1–:2 and Hopper's `remediation` line :24, IDA "not configured" :60). Presence is not upgraded to general capability anywhere; the Limitations section carries the same fence. |
| Q06 | **PASS** | Fixture premises byte-verified before producer calls — generator asserts at :89–:104 enforce every header field and the entry bytes (`assert buf[0x200:0x205] == bytes.fromhex("B82A000000"), "mov eax,0x2A"` :102 etc.); this round's regen re-run: `wrote …/fixture-regen.exe (1024 bytes)` then `cmp` → `REGEN-BYTE-IDENTICAL`, **exit 0**. |
| Q07 | n/a | No parser-behavior prediction or pre-registered hypothesis is offered by the entry; nothing to apply. |
| Q08 | n/a | Superseded by Q11 (per QUALITY.md table); the AUDIT SUBSECTION'S own Q08 row already says so. |
| Q09 | **PASS** | Every digest in the entry re-derives byte-exact from the committed bytes: fixture `fe060de1…` (`sha256sum`, exit 0), record files `d717b491… / 6ce217fa… / 2fba7fbf… / 6a1d18c3…` (all four match, exit 0), fetched bodies as above. None is presented as origin, completeness or authenticity; the Unknown section explicitly declines the evidence_id-stability claim. |
| Q10 | **PASS** | Scoped to one authored 1024-byte PE32+ fixture, one address, Ghidra 12.1.4, this host, 2026-11-05; Hopper reported absent, no IDA — both recorded as absent, not absorbed; no sibling scope touched; the pinned-vs-installed (`12f6e09` vs 6.7.0-era) byte drift is disclosed in Unknown. |
| Q11 | **PASS** | Derivation table: every value re-derived by the named command with its recorded output — `sed -n 3p` → `function_count=1` ✓, `sed -n 4p` → `// ==== FUNC entry @ 140001000 ====` ✓, lines 6–10 → `undefined8 entry(void)` … `return 0x2a;` ✓, `grep -c "INFO  REPORT"` → `6` ✓, `grep -m1 evidence_id` ✓, `grep -A3 ^provider:` ✓. All re-run verbatim this seat with matching outputs (exit 0 each). |
| Q12 | n/a | No rejected registry row is load-bearing for the entry's claims. |
| Q13 | n/a | No verifier command is credited as mutation-guarding a prose clause; the entry itself states the recheck commands are named with re-derivation targets and no clause is claimed as guarded (Q-map :76). Nothing to falsify. |
| Q14 | **PASS** | The one length-claimed hex run is `B82A000000C3` with the `2 × 6 hex characters` phrasing (:38); 6 bytes × 2 chars = 12 chars ✓; the ASCII rendering `mov eax, 0x2A; ret` decodes from exactly those bytes (B8 2A 00 00 00 = `mov eax,0x2A`; C3 = `ret`), matching generator asserts :102–:103 and `truth.json`. No other hex string in the entry carries a length claim. |
| Q15 | n/a | The entry asserts no git object id or tree-identity sentence (grep for commit ids in the entry: none besides the `12f6e09` REA-revision pin, which is a source pin, not a git identity sentence about the lane tree). |
| Q16 | **PASS** | Each output-crediting sentence is checked against the command's actual stdout: the derivation-table outputs were re-run and agree (Q11 list); the digest row's `sha256sum corpus/live/runs/round-96/*` four-line output is exactly what the glob prints (verified); the doctor claim names its greps' scope (ghidra-* lines list re-derived against `rea-doctor-r96.txt` :25–:54 — every named line value present: ghidra, ghidra-platform linux, ghidra-architecture x64, ghidra-version 12.1.4, ghidra-headless, ghidra-native_decompiler, ghidra-java 21.0.13 wait — ghidra-java detail verified as healthy/ok, java 21.0.13 version matches the headless log's `openjdk version "21.0.13"`; the entry credits the doctor's own printed version line). No sentence reaches past printed output. |
| Q17 | n/a | No relocation happened: every `corpus/live/runs/round-96/` and `corpus/fixtures/pe-r75-headless-smoke/` path the entry and the S502–S504 rows cite resolves at the current bytes (`ls` exit 0). Machine check re-run: `PYTHONUTF8=1 python3 reports/round-90/source_path_check.py --root .` → **`SOURCE_PATH_DEAD=0`, `SOURCE_PATH_MALFORMED=0`, exit 0** (excused S481 by S486, pre-existing). Rounds r92–r96 have not relocated `/round-96/live/` either. |

**Fails: none.** No FAIL in the table affects C1.
**C1 risk read:** the gate-grade risks for the C02 admission are the cursor dots called out
inside Q04 (record-side rea-version attribution via doctor receipt) — informational only; the
vote-binding digest holds; used-by exclusivity already matches the frozen v6 predicate's census
form; the counter legs themselves are not this seat's surface.
**n/a carries its why** in each row (admission procedure §1 honored).

## Exit codes observed (all real, no fabrication)

| leg | cmd (short form) | exit |
|---|---|---|
| digest re-derivation | `sha256sum` normalized-entry | 0, output match |
| `sha256sum` 6 files (fixture + 4 records + 2 bodies) | sha256sum | 0 |
| `grep` evidence_id / provider / REPORT-count / sed lines on records | grep/sed | 0 |
| `awk -F'|'` used-by split (S502–S504 rows) | awk | 0 |
| regen + `cmp` byte-identity | python3 + cmp | 0 |
| `wc -c` both bodies | wc | 0 |
| quote-span byte window reads re both bodies | python3 | 0 |
| `source_path_check.py --root .` | python3 | 0 (SOURCE_PATH_DEAD=0) |
| `ls corpus/live/runs/round-96/` | ls | 0 |

## Verdict

Advisory gate audit **clean**:

- PASS: Q01, Q02, Q03, Q04, Q05, Q06, Q09, Q10, Q11, Q14, Q16 — **11 PASS**.
- n/a: Q07, Q08, Q12, Q13, Q15, Q17 — **6 n/a**, each with its why in the table.
- FAIL: **0**.

**Advisory stance:** no action recommended to the L1 beyond visibility: (i) the digest matches
(`2f7d4c1b…5466d923`→`…d923`); do not edit the entry bytes, and if any correction is pursued it
must go through the vote procedure, never in place. (ii) No false FAIL can move C02 during the
L1 freeze; nothing found here blocks `admission-status: candidate → admitted` at gate level.
(iii) The Q04 réa-version attribution dot and the round-96 SCORECARD/lesson 13-vs-14 count
mismatch are already recorded findings — the latter is a frozen claim fact, not a gate defect.

Residual risk and verification gaps: (a) the pinned S502/S503 bodies are checked here against
the committed bytes and receipts, not against a fresh 2026-11-05 re-fetch of the URL — the
entry's own `recheck:` line and the C1 counter legs are the L1's surface for that (out of my
runs per discipline); (b) `rea decompile` / `rea doctor` / `analyzeHeadless` were re-run this
round only by the entry's already-recorded r96 runs; the L1 landing-time re-derivation re-runs
them fresh, which this seat did not duplicate to avoid double-execution; (c) no `vote.json`
anywhere; the findings file is the deliverable.
