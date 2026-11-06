source: S506 — REA connection and task recovery reference, https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md — "Choose the remedy from the observed failure" table and the paragraph after it, commit 12f6e0974cc0db0b3a9b86246accc76556837222
source: S507 — saved round-98 host-readiness record, `corpus/live/runs/round-98/` — the `rea doctor` receipt, the host probe transcript and one `rea inspect-artifact` Evidence on the committed ZIP fixture, opened 2026-11-05
verified-at: 2026-11-05 — S506 fetched this round at REA revision `12f6e09` (body committed at `reports/round-98/quote-receipts/raw/S506.body`, fetch log `reports/round-98/quote-receipts/fetch-log.md`); the S507 record was produced and saved this round on this host
recheck: re-open the S506 raw URL and compare `fetch_sha256` against the committed body; re-run `rea doctor`, the probe commands in `corpus/live/runs/round-98/host-probes-r98.txt` and `rea inspect-artifact corpus/fixtures/archive-r2/fixture.zip`, then re-derive every row of the derivation table below
coverage-map: C14 — host readiness for REA routes
admission-status: admitted

# Host readiness for REA routes — one host, one date, route by route

## Scope

This entry records what one host (this Linux host, `Linux 7.2.11-arch1-1 x86_64`) showed on
2026-11-05 for the REA routes this lane uses, and what REA's own recovery reference says such a
readiness check can and cannot establish. It supersedes, for this host and date, the pre-contract
2026-10-12 checklist (`knowledge/2026-10-12-rea-readiness-checklist.md`, re-probed 2026-10-19),
which stays in the knowledge base as history. It does not claim readiness on any other host, date
or REA version; it does not claim that any route other than the one exercised below produces
correct results; and it treats no digest as authenticity or origin (Q09).

## What a readiness check establishes (S506)

At the pinned revision the recovery reference states the boundaries below. Quoted text is the
reference's own words, byte-exact on one line of the committed body; the third row is a
paraphrase (marked) because its sentence wraps across lines 35–37 of the body.

| Documented fact (S506 anchor) | What it means for a readiness row |
|---|---|
| "Doctor checks registration; it cannot establish the current agent's connection." (remedy table, row "Aligned registration, but no connected tools") | A `rea doctor` result is a configuration observation. It is not a capability probe (Q05). |
| "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra." (paragraph after the remedy table) | A missing native engine does not block the static JavaScript or ZIP-inventory routes. |
| Paraphrase, not a quote: native decompilation, Android analysis and firmware extraction each have their own bring-your-own prerequisites (paragraph after the remedy table, body lines 35–37) | Each of those routes needs its own probe; one route's readiness does not carry to another. |
| "Inspect the actual shell PATH and launcher/runtime." (remedy table, row "`rea` is missing in a child shell, or Node is incompatible") | The `rea` path seen by one shell is a per-shell fact, not a host fact. |

## The host on 2026-11-05 (S507)

Three saved records, produced on this host on 2026-11-05:

1. `corpus/live/runs/round-98/rea-doctor-r98.txt` — the stdout and stderr of `rea doctor`
   (REA CLI 6.7.0). The run exited 1. The record's first two lines are `healthy: false` and
   `environment_healthy: false`.
2. `corpus/live/runs/round-98/host-probes-r98.txt` — each probe command, its output (first three
   lines) and its exit code.
3. `corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt` — the Evidence printed by
   `rea inspect-artifact corpus/fixtures/archive-r2/fixture.zip`, which exited 0.

### Route decision table

Each row states the observation and the probe class: **capability** (a route was run end to end
this round and its output was compared with an expected value fixed before the run),
**configuration** (doctor or a version probe only) or **absent**.

| Route | Observation on 2026-11-05 | Probe class | Readiness verdict |
|---|---|---|---|
| ZIP inventory (`inspect_artifact` → `inventory_artifact`) | `rea inspect-artifact` on `fixtures/archive-r2/fixture.zip` exited 0. Its substep `inventory_artifact` has `status: completed`. The members `README.txt` (84 bytes) and `bin/checksum` (16160 bytes) and the root digest match `fixtures/archive-r2/truth.json`, which round 2 fixed before this run. Doctor reported Hopper missing the same day (record 1). | capability | ready on this host for this fixture |
| Native decompile (Ghidra provider) | Doctor reports the eight ghidra scope checks healthy: ghidra, ghidra-platform, ghidra-architecture, ghidra-installation, ghidra-version 12.1.4, ghidra-headless, ghidra-native_decompiler, ghidra-java 21.0.13. `command -v analyzeHeadless` exited 1 (probe transcript). Doctor's `ghidra-headless` check reports the launcher at a path under the Ghidra install directory (derivation table). | configuration | configured. Not re-run this round. The capability record is the round-96 session (`knowledge/round-96-native-analysis-sessions.md`), which is not re-derived here. |
| Native analysis (Hopper, IDA, Kuna engines) | Doctor reports `hopper`, `ida-registration` and `kuna-installation` as `missing_analysis_engine`. `command -v hopper` and `command -v idat64` each exited 1. | absent | not ready |
| Android (JADX provider) | Doctor reports `jadx` healthy, and its own detail says "This checks configuration, not whether a selected APK fits in the worker's memory." `jadx --version` printed `1.5.6` and `java -version` printed `openjdk version "21.0.13"`. | configuration | configured, capability unprobed |
| Firmware regions and extraction | `binwalk --version` printed `binwalk 3.1.0` and `unblob --version` printed `26.6.4`, both exit 0. Doctor has no binwalk or unblob check. | configuration (version only) | present, capability unprobed |
| MCP registration (per client) | Of 14 client registrations, doctor reports 4 `aligned` (codex, devin, grok_build, zcode), 8 `missing`, 1 `manual` (grok_bot) and 1 `stale` (omp). Doctor also reports the installed skill identity `stale`. | configuration | the omp registration is stale. Per S506, an aligned registration still does not prove a connected session. |
| CLI launcher | `rea --version` printed `6.7.0`. `command -v rea` resolved to a per-shell `fnm_multishells` path. Doctor lists three such installation paths (`state: multiple`). | configuration | available in this shell. Per S506 this is a per-shell fact. |
| pwntools (ELF-layout helper) | `python3 -c 'import pwn'` exited 0. | configuration (import only) | importable. This corrects the 2026-10-19 re-probe row K05, which recorded the import as failing. |

### Derivation table

Every count, identifier, digest and doctor-printed version stated above is derived below from a
saved record by the command shown. The commands run from the lane root. Each output cell gives the
command's stdout verbatim, one code span per stdout line, lines joined by ` / `; in the
record-digest row the code span covers the digest prefix and the file name in parentheses is the rest
of the same stdout line. Text after an em dash (` — `) in an output cell is annotation, not output.
In a table cell, `\|` is the markdown escape of a shell pipe or a regex alternation bar. Two version
strings come from the doctor record and are derived below (`ghidra-version` detail `12.1.4`,
`ghidra-java` detail `21.0.13`). The other version strings (`rea --version`, `jadx --version`,
`java -version`, `binwalk --version`, `unblob --version`) and the probe exit codes are not derived
here: each comes from the probe transcript `corpus/live/runs/round-98/host-probes-r98.txt`, where
every command line (`$ …`) is followed by its printed output and an `rc=` line, and that transcript
is the record for those values. The doctor exit code (1) and the `rea inspect-artifact` exit code (0)
were observed in the L1 session and are not lines of any record.

| Value | Deriving command | Recorded output |
|---|---|---|
| host identity | `sed -n 1p corpus/live/runs/round-98/host-probes-r98.txt \| grep -oE 'Linux [^ ]+ [^ ]+$'` | `Linux 7.2.11-arch1-1 x86_64` |
| doctor verdict lines | `sed -n 1,2p corpus/live/runs/round-98/rea-doctor-r98.txt` | `healthy: false` / `environment_healthy: false` |
| healthy scope checks | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -c '    ok: true'` | `11` |
| failing scope checks | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -c '    ok: false'` | `13` |
| scope-check classes | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -oE 'classification: [a-z_]+' \| sed 's/^classification: //' \| sort \| uniq -c \| sed 's/^ *//'` | `10 config_drift` / `11 healthy` / `3 missing_analysis_engine` |
| registration states | `awk '/^    - client:/{c=$3} /^      state:/{print c, $2}' corpus/live/runs/round-98/rea-doctor-r98.txt` | `antigravity missing` / `claude_code missing` / `codex aligned` / `copilot_cli missing` / `cursor missing` / `devin aligned` / `gemini_cli missing` / `grok_bot manual` / `grok_build aligned` / `kimi missing` / `omp stale` / `opencode missing` / `pi missing` / `zcode aligned` |
| client registration count | `grep -c '^    - client:' corpus/live/runs/round-98/rea-doctor-r98.txt` | `14` |
| registration state split | `awk '/^    - client:/{c=$3} /^      state:/{print $2}' corpus/live/runs/round-98/rea-doctor-r98.txt \| sort \| uniq -c \| sed 's/^ *//'` | `4 aligned` / `1 manual` / `8 missing` / `1 stale` |
| missing-or-stale registrations ("nine") | `awk '/^    - client:/{c=$3} /^      state:/{print $2}' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -cE '^(missing\|stale)$'` | `9` |
| ghidra-named scope checks | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -c '^  - name: ghidra'` | `8` |
| ghidra scope checks healthy | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -A1 '^  - name: ghidra' \| grep -c '    ok: true'` | `8` |
| ghidra scope-check names | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -oE '^  - name: ghidra[a-z_-]*' \| sed 's/^  - name: //' \| paste -sd' '` | `ghidra ghidra-platform ghidra-architecture ghidra-installation ghidra-version ghidra-headless ghidra-native_decompiler ghidra-java` |
| ghidra headless launcher path | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -A3 '^  - name: ghidra-headless$' \| grep 'detail:' \| sed 's/^ *//'` | `detail: /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/support/analyzeHeadless` |
| doctor-printed ghidra and java versions | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -A3 -E '^  - name: ghidra-(version\|java)$' \| grep 'detail:' \| sed 's/^ *//'` | `detail: 12.1.4` / `detail: 21.0.13; 64-bit; JDK; /usr/lib/jvm/java-21-openjdk; accepted a 64-bit full JDK 21 or newer` |
| engine and jadx classifications | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -A3 -E '^  - name: (hopper\|ida-registration\|kuna-installation\|jadx)$' \| grep -E 'name:\|classification:' \| paste - - \| sed -E 's/^ *- name: //; s/\t *classification: / /'` | `hopper missing_analysis_engine` / `ida-registration missing_analysis_engine` / `jadx healthy` / `kuna-installation missing_analysis_engine` |
| installed skill identity | `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt \| grep -A3 'name: "skill:identity"' \| sed 's/^ *//'` | `- name: "skill:identity"` / `ok: false` / `classification: config_drift` / `detail: Installed REA skill identity is stale.` |
| doctor binwalk or unblob checks | `grep -c -E 'binwalk\|unblob' corpus/live/runs/round-98/rea-doctor-r98.txt` | `0` — the record has no binwalk or unblob check; grep exits 1 on zero matches |
| installation paths ("three") | `grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt \| sed 's/^    paths\[3\]: //' \| tr ',' '\n' \| grep -c .` | `3` — the record prints the three comma-separated paths on one line |
| installation state | `grep '^    state: multiple' corpus/live/runs/round-98/rea-doctor-r98.txt \| sed 's/^ *//'` | `state: multiple` |
| CLI package version | `grep cli_package_version corpus/live/runs/round-98/rea-doctor-r98.txt \| sed 's/^ *//'` | `cli_package_version: 6.7.0` |
| inventory Evidence ID | `grep -m1 evidence_id corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt` | `evidence_id: ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382` |
| inventory substep status | `grep -m1 -A1 'operation: inventory_artifact' corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt \| sed 's/^ *//'` | `operation: inventory_artifact` / `status: completed` |
| inventory members and sizes | `awk '/logical_path:/{p=$2} /declared_size:/{print p, $2}' corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt` | `. 2964` / `README.txt 84` / `bin/checksum 16160` |
| inventory root digest | `grep -m1 root_sha256 corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt \| sed 's/^ *//'` | `root_sha256: 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` |
| truth.json archive digest | `grep -oE '"archive_sha256": *"[0-9a-f]+"' corpus/fixtures/archive-r2/truth.json` | `"archive_sha256": "857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e"` |
| fixture digest | `sha256sum corpus/fixtures/archive-r2/fixture.zip \| cut -d' ' -f1` | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` |
| record file digests | `sha256sum corpus/live/runs/round-98/* \| awk '{print substr($1,1,8) "… (" substr($2,27) ")"}'` | `fb9a4824…` (host-probes-r98.txt) / `94eaa6ff…` (rea-doctor-r98.txt) / `c373f656…` (rea-inspect-artifact-archive-r2.txt) |
| S506 body digest | `sha256sum reports/round-98/quote-receipts/raw/S506.body \| cut -d' ' -f1` | `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50` |
| S506 body length | `wc -c < reports/round-98/quote-receipts/raw/S506.body` | `16650` |

## Observation, inference, unknown

**Observation:** on 2026-11-05 `rea doctor` exited 1 with `healthy: false`. It reports 11
healthy and 13 failing scope checks; the failures are three missing engines (Hopper, IDA, Kuna),
nine stale or missing client registrations and a stale installed skill. `rea inspect-artifact`
inventoried the committed ZIP fixture with the values that `truth.json` fixed before the run, on
the same day that doctor reported Hopper missing.

**Inference:** on this host the ZIP-inventory route is usable even though doctor's overall
verdict is unhealthy. This matches S506's statement that ZIP inventory needs neither Hopper nor
Ghidra. A failing overall doctor verdict is therefore not a readiness verdict for a given route.
Each route is judged by its own probe.

**Unknown:** whether the Android, firmware and native-decompile routes produce correct output on
this host today (none was run this round); whether the omp session has a live REA MCP connection
(doctor cannot establish that, per S506); and how the installed skill copy differs from the pinned
revision (S506 is the pinned revision, not the installed copy).

## §Q-map

| Q | decision | entry evidence / boundary |
|---|---|---|
| Q01 | PASS | The route-boundary statements cite S506, a tier-A docs row opened this round, whose body and receipt are committed. The host observations cite S507, the lane's own record saved this round. |
| Q02 | PASS | The headers give S506 and S507 with URL or path and anchor, `verified-at`, `recheck`, and the coverage-map row C14. |
| Q03 | PASS | The ZIP-inventory expectations (member paths, sizes, archive digest) come from `fixtures/archive-r2/truth.json`, fixed in round 2 before this run. The record under test does not supply them. |
| Q04 | PASS | Each tool claim names the tool, version and function (`rea` CLI 6.7.0 `doctor` and `inspect-artifact`, provider `rea-artifact-graph`) and scores only what that tool printed. Version lines are probe outputs, not capability. |
| Q05 | PASS | Each readiness verdict carries its probe class. Only the ZIP-inventory row is a capability probe (command, date, exit 0, Evidence ID). Doctor and version rows are labelled configuration, and no presence is called capability. |
| Q06 | PASS | The ZIP-inventory producer call ran on `fixtures/archive-r2/fixture.zip`. Its premise, the archive digest and members in round 2's `truth.json`, matches the fixture bytes: `sha256sum` gives `857989f5…`, which equals truth.json `archive_sha256`, as the derivation table shows. No fixture was authored or edited this round. |
| Q07 | n/a | No parser accept, refuse or cause prediction is offered by this entry; see Q07 in corpus/QUALITY.md. |
| Q08 | n/a | Historical criterion superseded by Q11, which is applied below. |
| Q09 | PASS | The digests bind exact committed bytes only (fixture, record files, S506 body). None is offered as origin, completeness or authenticity. |
| Q10 | PASS | Scoped to one host, one date, REA 6.7.0 and the routes named. Unprobed routes are labelled unprobed, and the absent engines are recorded as absent. |
| Q11 | PASS | Every count, identifier, digest, path and doctor-printed version in the scope paragraph, route table and observation is in the derivation table with its deriving command and that command's verbatim stdout; the "three installation paths" row counts paths, not lines, and prints `3`; `reports/round-99/controls/deriv_check.py` re-runs every row and compares it with its output cell. |
| Q12 | n/a | No rejected registry row is load-bearing for this entry; see Q12 in corpus/QUALITY.md. |
| Q13 | n/a | No verifier is credited as guarding a clause. The recheck line names re-derivation procedures only; see Q13 in corpus/QUALITY.md. |
| Q14 | n/a | No hex string is quoted with a byte count in the same clause, and no truncated run carries a length; see Q14 in corpus/QUALITY.md. |
| Q15 | n/a | No lane-tree git identity sentence is asserted. The pinned REA revision is part of a fetched URL; see Q15 in corpus/QUALITY.md. |
| Q16 | PASS | Each output cell is the command's stdout verbatim under the stated cell rule (one code span per line, annotation only after an em dash), and `reports/round-99/controls/deriv_check.py` reports 0 mismatches. The two doctor-printed versions (12.1.4, 21.0.13) are credited to the doctor record and derived; the remaining version strings are credited to the probe transcript, which prints each of them; the doctor and inspect exit codes are credited to the session, not to a record. |
| Q17 | n/a | No adjudication relocated a cited artifact for this entry; see Q17 in corpus/QUALITY.md. |
