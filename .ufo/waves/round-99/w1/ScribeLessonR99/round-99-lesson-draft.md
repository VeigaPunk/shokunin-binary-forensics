# Round 99 — gate, mistakes, frontier (revenger, attempt 1)

Claims frozen at `7e6edd4db649f99c425daa46a91edbbd18a6e27c` (`reports/round-99/claims.md`).
Base at round start `3d054a98e3fa768e63b631665a2372fadb51a77a`. Landing, votes, v8 freeze and
measurements are cited in the SCORECARD round-99 section and the report.

**Verdict of record:** C1 (coverage, K 13/15 → 14/15 through C14 held): <<L1: verdict>>.
C2 (calibration, v8 accepts 0/12 on the round-98 holdout): <<L1: verdict>>.

## Gate

### C14 candidate — the r98 → r99 edit

Entry `corpus/knowledge/round-98-rea-host-readiness.md`. The only change between base and freeze is
this entry (`git diff --stat 3d054a98 7e6edd4 -- corpus/knowledge/round-98-rea-host-readiness.md` →
1 file, 17 insertions, 10 deletions; five hunks at `@@ -64,4 +64,7`, `-69,3 +72,3`, `-83 +86,5`,
`-125 +132`, `-130 +137`). Full diff: `.ufo/waves/round-99/w1/ScribeLessonR99/candidate-diff-r98-to-r99.diff`.

| change | where (freeze tree) | what the record now shows |
|---|---|---|
| "three installation paths" row | `:89` (was `:83`) | `installation paths ("three")` counts paths: `grep '^    paths\[3\]: ' … \| sed 's/^    paths\[3\]: //' \| tr ',' '\n' \| grep -c .` → `3`; `installation state` (`:90`), `grep -c '^    state: multiple' …` → `1` |
| ghidra scope-check names | `:86` (new) | eight names, `ghidra ghidra-platform ghidra-architecture ghidra-installation ghidra-version ghidra-headless ghidra-native_decompiler ghidra-java` |
| doctor-printed versions | `:87` (new) | `ghidra-version` detail `12.1.4`, `ghidra-java` detail `21.0.13`, both credited to the doctor record and derived by command |
| engine and jadx classifications | `:88` (new) | `hopper`, `ida-registration`, `kuna-installation` = `missing_analysis_engine`; `jadx` = `healthy` |
| preamble | `:64-74` | two versions credited to the doctor record and derived; the remaining version strings credited to the probe transcript |
| Q11 and Q16 PASS notes | `:132`, `:137` | amended to name the path-count row and the doctor-attributed versions |

Derivation rows: 17 at base, 21 at freeze (python diff over the derivation table: added 5, removed 1).
The route-table cell at `:59` still reads "Doctor lists three such installation paths", which is now
derived at `:89`.

**Vote-binding digest (v7 `digest()` rule: sha256 of the entry text with every admission-status line
normalized to `admission-status: candidate`).** Recomputed by the scribe from the committed bytes:

```
python3 -c "import re,hashlib,subprocess;old=subprocess.run(['git','show','3d054a98e3fa768e63b631665a2372fadb51a77a:corpus/knowledge/round-98-rea-host-readiness.md'],capture_output=True,text=True).stdout;new=open('corpus/knowledge/round-98-rea-host-readiness.md',encoding='utf-8').read();d=lambda t:hashlib.sha256(re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t).encode()).hexdigest();print(d(old));print(d(new))"
6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f   (base, r98 1b76b4d)
36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5   (freeze 7e6edd4)
```

The digest moved from `6d27c129…5330f` to `36cc6ac2…fce5`, so every r98 vote (superseded) is void for
r99. Both `admission-status` lines read `admission-status: candidate` at base and at freeze.

**Lint.** `reports/round-99/controls/lint-candidate-freeze.log` records `LINT_QMAP=0 LINT_Q14=0
LINT_Q15=0 LINT_HEADER=0`, rc 0, written at the freeze. The scribe did not re-run it.

**S506 re-open** (`reports/round-99/quote-receipts/S506-reopen-r99.txt`). URL at pinned revision
`12f6e09`; `fetched_at=2026-11-05T18:43:20-03:00`; `http=200`; `bytes=16650`; sha256
`ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`, byte-identical to the committed
body (`cmp=identical`). Located quote, 11 words, 76 bytes, verbatim: *"Static JavaScript and ordinary
ZIP inventory need neither Hopper nor Ghidra."* Counts: `grep -c -F` on
`reports/round-98/quote-receipts/raw/S506.body` → `1`; `head -c 7202 … | tail -c +7127` prints the
sentence (span 7126–7202, as in `S506.receipt.json`).

**S507 re-hash** (`reports/round-99/controls/s507-reopen-r99.txt`). The three saved records
`corpus/live/runs/round-98/{host-probes-r98.txt,rea-doctor-r98.txt,rea-inspect-artifact-archive-r2.txt}`
re-hash to `94eaa6ff…`, `fb9a4824…`, `c373f656…`, equal to the r98 values. Located quote: *"healthy:
false"* / *"environment_healthy: false"*, bytes 1–41 of `rea-doctor-r98.txt` (`head -c 41` → 41 bytes,
both lines).

### C2 calibration — the frozen v7 reach on the r98 holdout (do-nothing control, before the v8 freeze)

| run | accepted | control | receipt |
|---|---|---|---|
| v7 `--profile c02` on the r98 holdout (V01, V02, E01, E02, E03 accepted; R01 refused by `C1_ONLY_TARGET,C1_ADMITTED_UNION,C1_VERDICT`) | **5/6** | control-ok | `reports/round-99/controls/c2-do-nothing-v7-holdout98-c02.log` |
| v7 `--profile c14` (R01, V02, O01, L01 accepted; V01 refused by `C1_VOTE_NOTES`, Q01 by `C1_QUOTES`) | **4/6** | control-ok | `reports/round-99/controls/c2-do-nothing-v7-holdout98-c14.log` |

Baseline 9/12, the number the v8 target has to move to 0/12. Target and kill rule are as frozen in
`claims.md`. v8 result: <<L1: C2_ACCEPTED, C2_STUB_SELFTEST, C2_VERDICT>>.

### C1 coverage — the rows and the base

- Base: `grep -cE '^\|[[:space:]]*C[0-9]+.*\|[[:space:]]*held[[:space:]]*\|' corpus/README.md` → `13`;
  C14 cell `partial` (`reports/round-99/controls/c1-base-rowstatus.log`).
- Votes on digest `36cc6ac2…fce5`: <<L1: vote outcome per seat, FAIL count, C1_VOTE_NOTES>>.
- v8 `c14r99` landing run and the two controls: <<L1: C1_K_HELD_BACKED, C1_VERDICT, control verdicts>>.

### Census

`reports/round-99/controls/census-round-start.log` ends `# rc=0 base=3d054a98…`: 21 × W01, 13 × W04,
0 E-codes (`grep -c W01`, `grep -c W04`, `grep -cE 'revenger	E'`). Round-end census:
<<L1: rc and counts>>.

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M16 | **count by lines, not paths:** the r98 route table stated "Doctor lists three such installation paths", and the row that should derive it counted `paths[3]:` *lines*. The record prints three comma-separated paths on one line, so the recorded command printed `1` against a claimed `3`. | `reports/round-99/controls/q11-paths-old-vs-new.log`: old `grep -c '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt` → `1`; new `grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt \| sed 's/^    paths\[3\]: //' \| tr ',' '\n' \| grep -c .` → `3`. Re-run by the scribe with the same two outputs. Captured in r98 by the critic's Q11 FAIL (`reports/round-98/votes/CriticR98.json`; `corpus/lessons/round-98-verifier-spotcheck.md:109`). | CriticR98 vote Q11 (digest `6d27c129…`) | the **path-counting derivation row** (`:89`). Shown able to fail: the old command prints `1`, so the old row cannot back a `3`; the new row prints `3`. |
| M17 | **version credited to a transcript that does not print it:** the r98 preamble said each version string "comes from the probe transcript". `ghidra-version 12.1.4` appears zero times in `host-probes-r98.txt` and seventeen times in the doctor record. | `reports/round-99/controls/q16-version-attribution.log`: `grep -c -F <version>` per record — `12.1.4` host-probes `0`, doctor `17`; `21.0.13` host-probes `3`, doctor `3`; `6.7.0` host-probes `1`, doctor `11`. Re-run by the scribe. | CriticR98 vote Q16 (digest `6d27c129…`) | the **attribution**: `12.1.4` and `21.0.13` are credited to the doctor record and derived by command (`:87`, `:72-74`); the transcript is credited only for strings it prints (`6.7.0`, `1.5.6`, `3.1.0`, `26.6.4`). Shown able to fail: the `12.1.4` count against the transcript is `0`, so the old credit fails by the same command. |
| M18 | **seat-name collision across rounds:** the r98 re-vote messages were addressed to `ReviewerGate` and `ReviewerBlind`, the seat names of earlier rounds, not the r98 instances `ReviewerGate-6` and `ReviewerBlind-5`. The earlier-round seats declined and wrote nothing, so the re-vote silently reached no r98 seat. | `.ufo/waves/round-99/w1/ScribeLessonR99/m18-seat-name-collision.txt`: `for f in .ufo/waves/round-9*/w1/swarm-registry.json; do …; done` lists `round-93,94,95,96,98: ReviewerGate,ReviewerBlind` and `round-97: ReviewerGate` (six registries); the r98 report line is `/home/vgpnk/Projects/shokunin/.ufo/reports/round-98/revenger.md:36`. | **none** (the r98 report recorded it by hand; no check, no lint, no roster test) | **round-suffixed seat names in r99** (`VoterGateR99`, `VoterBlindR99`, `CriticR99`, and the rest of the twelve members of `.ufo/waves/round-99/w1/swarm-registry.json`, none of which appears in the list above). Shown able to fail: the same command finds the r98 names in six registries, so the name test rejects reuse. |

## Frontier

- **Census.** Round start exit 0 (see Gate). Round end: L1.
- **Rows.** No row changed by the scribe. S506 and S507 stay `mined`, tier A, `used-by` the candidate
  (`corpus/SOURCES.md:523-524`).
- **S505 `used-by` is still ungrounded.** `grep -c S505 corpus/knowledge/round-96-native-analysis-sessions.md`
  → `0`, while the same file cites S504 three times. r98 routed the fix as a citation: a superseding C02
  entry revision that cites S505 in place of S504. The r99 frozen claims contain no S505 leg, so that
  revision is a new claim for the L1 to decide, not part of C1 or C2.
- **Producer version drift (new, measured, not claimed).** The lane's own records disagree on which
  `rea` version the host ran. See the considerthese section for the measurements.
- **Next probes, still unprobed.** Android capability on `corpus/fixtures/apk-r65/fixture.apk` (947
  bytes, `truth.json`, `oracle_check*.py`) and firmware capability on
  `corpus/fixtures/firmware-r63/firmware-r63.bin` (2048 bytes, `truth.json`). Configuration present on
  this host: `REA_JADX_MCP_JAR=/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar`
  (42619858 bytes, `ls -la`), `REA_BINWALK_COMMAND=/usr/bin/binwalk` → `binwalk 3.1.0`,
  `REA_UNBLOB_COMMAND=/home/vgpnk/.local/bin/unblob` → `unblob 26.6.4`. Capability: unprobed. Configuration
  does not move C14 to `held`.
- **Carried from r98, not re-measured by the scribe.** `d-host` survives the mutate7 run
  (`reports/round-98/controls/mutate7-v7-c02.out`, `SURVIVORS_TREE=…,d-host,…`, `MUTANT_KILL_V7=173/249`).
  The mutate7 self-test baseline exit (3 in r98, per the r98 SCORECARD) is unreconciled with
  `reports/round-98/controls/selftest-v7-frozen.log` (`SELFTEST_C1V7=OK legs=55`, rc 0).
- **M4.** `corpus/knowledge/claude-red-re-bridge.md` is still unindexed: `grep -c claude-red-re-bridge
  corpus/README.md` → `0`.
- **Assimilation.** Not re-checked by the scribe. The r98 figure (155 of 155 staged ids collide with
  the registry) stays on L0; `ScoutReopenR99` owns the re-check.

## considerthese

**Proposal 4 of `considerthese/2026-11-05.md`** (not mined in r97 or r98; r98 recorded proposals 3 and 4
as "likewise not adopted") — quoted verbatim from `considerthese/2026-11-05.md:37`:

> **Upstream drift watch for the tool the lane tests.** Round 89 evidence puts the host at `rea` 6.7.0
> and the registry's latest at 6.8.0. I can read the public changelog read-only each day and list
> operations or format changes the lane has no oracle-checked record for.

**How the lane's own bar refuses it as written.** A daily changelog reader is a paper report about an
upstream product. The lane refused that shape before (the r93 spot-check: "adopting a criterion without
its own frozen predicate would violate the lane's own bar", `corpus/lessons/round-93-verifier-spotcheck.md:78`).

**What the lane's own committed bytes and host show now.** The proposal's premise is observed, but in
the lane's records, not upstream. Measured by the scribe (`.ufo/waves/round-99/w1/ScribeLessonR99/proposal4-measurements.txt`):

| measurement | command | output |
|---|---|---|
| live records naming `rea 6.8.0` | `grep -rl 'rea 6\.8\.0' corpus/live/runs/ \| wc -l` | `15` (rounds 76–85) |
| doctor records with `cli_package_version: 6.7.0` | `grep -rl 'cli_package_version: 6\.7\.0' corpus/live/runs/ \| wc -l` | `2` (`round-96/rea-doctor-r96.txt`, `round-98/rea-doctor-r98.txt`) |
| doctor records with `cli_commands: 153` / `175` | `grep -rl 'cli_commands: 153' …` / `… 175` | `2` / `0` |
| S444 records the 6.8.0 manifest as `cli_commands: 175` | `grep -n 'cli_commands: 175' corpus/SOURCES.md \| cut -c1-60` | `459:` (S444) |
| PROVINCE says 6.8.0 is installed | `grep -n 'installed on this host at 6.8.0' PROVINCE.md` | `22:` (2026-10-31) |
| host binary | `rea --version`; `…/rea-agents/package.json` version | `6.7.0`; `6.7.0` |

The records name two producers. Fifteen live files, from rounds 76 to 85 (the 6.8.0 era the records
themselves name), say `rea 6.8.0`; the two doctor records (r96, r98) say `6.7.0` and 153 commands.
Nothing in the committed bytes dates the change, and the scribe did not establish the cause.

**Operation census against the installed manifest** (the proposal's "no oracle-checked record" test):
153 declared commands (`rea --llms` on this host, saved at `.ufo/waves/round-99/w1/ScribeLessonR99/rea-llms-6.7.0-host.txt`);
30 distinct recorded `operation` names across `corpus/live/runs/`; 22 have a declared kebab twin; 8 have
none in 6.7.0 (`current_document`, `get_android_manifest`, `get_app_info`, `inspect_pe_certificates`,
`inventory_artifact`, `load_apk`, `open_binary`, `rea_jvm_status`); 131 declared commands have no recorded
operation. The 8 include `inspect_pe_certificates`, which S453 records as a 6.8.0 surface, so the records
were made by a producer the installed manifest does not declare.

**How it lands.** Not as a daily tracker. As a counting predicate over committed bytes and the host, with a
denominator, which is what the bar accepts. Proposed for r100 with its own frozen predicate, not adopted:
`producer-attribution census`. A live record's producer version must equal the `cli_package_version` of the
doctor record captured in the same round, or the record is labelled with the version it names, not the
host's current version. The census above is its first run: none of the 15 `6.8.0` records has a
same-round doctor record naming 6.8.0. The proposal's operation-coverage half is the 22/8/131 split above,
and it lands as a Frontier count, not a criterion, until a round freezes it.

## Frontier items for the L1 to decide

1. Whether the S505 citation fix goes into a superseding C02 entry revision (new claim) or waits.
2. Whether the producer-attribution census is frozen in r100 (proposal above) or left as a Frontier count.
3. Assimilation re-check result from `ScoutReopenR99`, for the L0 question.
