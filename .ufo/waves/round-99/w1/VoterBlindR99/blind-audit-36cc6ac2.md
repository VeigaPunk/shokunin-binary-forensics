# Blind audit — VoterBlindR99 (reviewer) — candidate 36cc6ac2

- Seat: VoterBlindR99 (reviewer, pinned)
- Entry audited: `corpus/knowledge/round-98-rea-host-readiness.md`
- Vote-binding digest: `36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5`
- Blindness: written before reading any round-99 vote file, any other seat's audit, or any
  round-98 critic/reviewer audit. Sources used: the entry, `corpus/QUALITY.md`,
  `corpus/SOURCES.md`, `corpus/README.md`, the S506 committed body and fetch log, the three
  S507 records, `corpus/fixtures/archive-r2/truth.json`, the frozen v7 counter source (digest
  and note rules only), and the round-98 claims-freeze predicate in `reports/round-99/claims.md`.
- Method: every derivation-table command re-ran verbatim from the lane root
  (markdown `\|` unescaped); receipt `derivations-rerun.txt`
  (sha256 `67bdb246d57007b1fe1078d9c78ce275599b21a6ee3b2ad9b7b68fbecbce154f`), runner
  `run-derivations.sh` (sha256 `13213116adc4ac3c272c308ff210db3d87af459902d4f50e066234c5e714a009`),
  both beside this file.

## 1. Digest recompute (v7 rule, reports/round-98/c1_k_admit_counter7.py:109-111)

Extracted the frozen `def digest` from v7 by AST and applied it to the worktree entry text:

```
DIGEST_WORKTREE = 36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5
MATCHES_FROZEN = True
```

The worktree entry carries `admission-status: candidate`; the digest matches the frozen
vote-binding value, so these decisions bind the frozen candidate bytes.

## 2. S506 quote verification (round-73 procedure, body committed 16650 bytes, sha256 `ce2d122b…`)

| Entry quotation | grep -nF on S506.body | Result |
|---|---|---|
| "Doctor checks registration; it cannot establish the current agent's connection." | line 22, row "Aligned registration, but no connected tools" | byte-exact substring |
| "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra." | line 34, paragraph after the remedy table | byte-exact substring |
| Paraphrase (own prerequisites per route), marked as paraphrase | lines 35-37: "Native / decompilation, Android analysis and firmware extraction have their own / bring-your-own prerequisites." | content matches; wrap attribution lines 35-37 exact |
| "Inspect the actual shell PATH and launcher/runtime." | line 26, row "`rea` is missing in a child shell, or Node is incompatible" | byte-exact substring |

Unquoted locator prose ("remedy table, row …", "paragraph after the remedy table") was used only
as a locator, never as quote match. Fetch log row (line 9) prints HTTP 200, 16650 bytes,
sha256 `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`; D20/D21 below
re-derived the committed body to the same values.

## 3. Derivation table re-run — all 21 rows reproduced

Run from the lane root; every recorded output matched byte-for-byte (full transcript in
`derivations-rerun.txt`):

- D1 verdict lines → `healthy: false` / `environment_healthy: false` ✓
- D2 scope checks ok:true/ok:false → `11` / `13` (24 scope checks) ✓
- D3 classes → `10 config_drift / 11 healthy / 3 missing_analysis_engine` ✓ (sums 24)
- D4 registration pairs → 14 lines: antigravity,claude_code,copilot_cli,cursor,gemini_cli,kimi,opencode,pi missing; codex,devin,grok_build,zcode aligned; grok_bot manual; omp stale ✓
- D5 client count → `14` ✓; D6 split → `4 aligned / 1 manual / 8 missing / 1 stale` ✓; D7 missing-or-stale → `9` ✓
- D8 ghidra healthy → `8` ✓; D9 ghidra names → the eight names in table order ✓
- D10 doctor versions → `detail: 12.1.4` and `detail: 21.0.13; 64-bit; JDK; /usr/lib/jvm/java-21-openjdk; accepted a 64-bit full JDK 21 or newer` ✓
- D11 engine/jadx → `hopper missing_analysis_engine` / `ida-registration missing_analysis_engine` / `jadx healthy` / `kuna-installation missing_analysis_engine` ✓
- D12 paths count → `3` (paths[3] line at doctor line 316 holds three comma-separated fnm_multishells paths — counts paths, not lines: the r98 count-by-lines defect is fixed) ✓
- D13 installation state → `1` ✓; D14 cli_package_version → `  cli_package_version: 6.7.0` ✓
- D15 evidence_id → `ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382` ✓
- D16 substep status → `      status: completed`; P10 shows the only `status: completed` (record line 29) belongs to `operation: inventory_artifact` (line 28) ✓
- D17 declared sizes → `2964` / `84` / `16160` (root, README.txt, bin/checksum in record order) ✓
- D18 fixture digest → `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` ✓ = truth.json `archive_sha256`
- D19 record digests → prefixes `94eaa6ff…` (host-probes), `fb9a4824…` (doctor), `c373f656…` (inspect) ✓
- D20 S506 body digest → `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50` ✓
- D21 S506 body length → `16650` ✓

## 4. Prose versus record checks

- Probe transcript `host-probes-r98.txt` (header prints `2026-11-05T17:46:13-03:00, host Linux 7.2.11-arch1-1 x86_64`): `rea --version`→`6.7.0` rc=0; `command -v rea`→`/run/user/1000/fnm_multishells/3146096_1793846990804/bin/rea` rc=0; `jadx --version`→`1.5.6` rc=0; `java -version`→`openjdk version "21.0.13"` rc=0; `binwalk --version`→`binwalk 3.1.0` rc=0; `unblob --version`→`26.6.4` rc=0; `command -v analyzeHeadless` rc=1; `command -v idat64` rc=1; `command -v hopper` rc=1; `python3 -c 'import pwn'` rc=0. Every version string the preamble credits to the transcript is printed there, and every `$ …` line is followed by output and an `rc=` line.
- jadx detail quotation — `grep -nF "This checks configuration, not whether a selected APK fits in the worker's memory."` on the doctor record → lines 65, 161, 236, byte-exact.
- "Doctor has no binwalk or unblob check" — `grep -cE 'binwalk|unblob'` on the doctor record → `0` (rc=1); true of the record bytes.
- Installed skill identity stale — scope check `skill:identity` ok:false, detail `Installed REA skill identity is stale.`; installations `skill.state: stale` (doctor tail).
- "doctor finds it under the install directory" — `ghidra-headless` detail `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/support/analyzeHeadless`; `ghidra-installation` detail `…/Ghidra/application.properties` ✓.
- truth.json (round-2 expectation source): `archive_sha256 857989f5…`, `archive_size 2964`, members `bin/checksum` size 16160 sha256 `f5ba0697…` and `README.txt` size 84 sha256 `7d8f6a8d…`. The evidence's root node sha256 (`857989f5…`) equals both `archive_sha256` and the D18 sha256sum output — the prose "root digest match" holds. Member sha256s in the evidence equal truth.json's member sha256s (not cited by the entry; extra corroboration).
- K05 correction claim — `## Re-verification 2026-10-19` row K05 (checklist line 40) records "pwntools import fails"; the round-98 probe's rc=0 corrects it. The later `## Re-verification 2026-11-04` row (line 61) is a different section; the entry's sentence names the 2026-10-19 row and is accurate.
- Exit codes 1 (doctor) and 0 (inspect): `grep -c 'rc='` on both records → 0 matches each; the entry's disclosure that they were session observations, not record lines, is honest.
- SOURCES rows 523/524: S506 docs tier A, S507 own-work tier A, both opened 2026-11-05 (the round that wrote the entry); scopes match how the entry cites them.
- Cited-path sweep: every `corpus/` and `reports/` path the entry names resolves at the lane root (12 paths, all OK, including `corpus/knowledge/round-96-native-analysis-sessions.md` and `corpus/fixtures/archive-r2/truth.json`).

## 5. Per-Q decisions (command + output evidence)

- **Q01 PASS** — `sed -n '523,524p' corpus/SOURCES.md` → S506 `docs | A`, S507 `own-work | A`, both opened 2026-11-05; the S506 table credits exactly what the reference states (§2 quote check) and host facts cite the lane's own S507 records. No tier-C support anywhere.
- **Q02 PASS** — entry opens with two `source:` lines (S506 with pinned commit URL + named remedy-table anchor; S507 with `corpus/live/runs/round-98/`), `verified-at: 2026-11-05`, a concrete `recheck:` line, `coverage-map: C14`; `grep -n 'C14' corpus/README.md` → line 61 row C14 exists (`partial`, pre-landing state).
- **Q03 PASS** — `cat corpus/fixtures/archive-r2/truth.json` → `archive_sha256 857989f5…`, members 16160/84; expectations fixed in round 2, independent of the round-98 record under test; the record's printed values were compared against it, not copied from it.
- **Q04 PASS** — `grep -nE 'provider|operation' rea-inspect-artifact-archive-r2.txt` → `provider: id: rea-artifact-graph`, `operation: inspect_artifact`; probes print each version with its own command and rc= line; version lines are scored as configuration, not capability.
- **Q05 PASS** — the single capability row carries command, date (transcript header 2026-11-05T17:46:13-03:00), exit 0 (disclosed session observation), Evidence ID ev_0ef6c8cd…; all other rows labeled configuration or absent; "present, capability unprobed" keeps presence from becoming capability.
- **Q06 PASS** — `sha256sum corpus/fixtures/archive-r2/fixture.zip` → `857989f5f2722fc0…` equal to truth.json `archive_sha256`; declared_size 2964/84/16160 matches truth.json sizes; the fixture was round-2 mint, nothing authored or edited this round.
- **Q07 n/a** — `grep -niE 'predict|pre-regist|will (accept|refuse)'` on the entry → one hit, the entry's own Q07 map row; the entry offers nothing predicting parser accept/refuse/cause, so Q07 has no trigger.
- **Q08 n/a** — `grep -n 'Supersedes Q08' corpus/QUALITY.md` → line 23 "Q11 | Supersedes Q08"; Q11 applied below instead, per the criterion's own supersession.
- **Q09 PASS** — re-derived fixture, three record-file, and S506-body digests myself (D18-D20); each binds the exact committed bytes it names; scope section states "it treats no digest as authenticity or origin"; evidence_id used as a receipt pointer only.
- **Q10 PASS** — scope section limits claims to this host (`Linux 7.2.11-arch1-1 x86_64`, printed in the probe transcript header), 2026-11-05, REA 6.7.0 and the named routes; unprobed routes labeled unprobed; no family-level universal anywhere.
- **Q11 PASS** — all 21 derivation rows re-ran byte-identically from the lane root (§3); the "three installation paths" row counts paths and prints `3`; doctor-printed versions 12.1.4 / 21.0.13 are derived inside the entry; transcript-sourced values are attributed to the transcript; exit codes are labeled session observations, i.e. recorded, not re-derived.
- **Q12 n/a** — `grep -niE 'reject'` on the entry → one hit, the entry's own Q12 map row; no rejected registry row is load-bearing here.
- **Q13 n/a** — `grep -niE 'verifier|guard'` on the entry → one hit, the Q13 map row itself; the recheck line names re-derivation procedures, not a verifier credited with guarding clauses.
- **Q14 n/a** — `grep -nE '[0-9a-f]{32,}'` on the entry → four lines (S506 URL commit id, evidence_id, fixture digest, body digest), none pairing hex with a byte count in the same clause; truncated record digests carry `…` and no length.
- **Q15 n/a** — `grep -noE '[0-9a-f]{40}'` → the 40-hex REA revision appears only inside the fetched S506 URL (line 1, twice); no lane-tree git identity sentence exists to re-derive; the revision is corroborated by the fetch-log row and the committed body digest.
- **Q16 PASS** — every derivation command's stdout matched its recorded output row by row (§3); the absence sentence is backed by `grep -cE 'binwalk|unblob'` → `0`; `status: completed` is credited to `inventory_artifact` and the record shows exactly that substep; the skill-stale, ghidra-names, engine-classification and registration-split sentences each match their printed bytes.
- **Q17 n/a** — cited-path sweep (§4): 12/12 paths resolve at the lane root; nothing was relocated for this entry, so the sweep duty has no trigger.

## 6. Findings

No criterion fails. Two observations, neither rising to a Q failure:

1. The doctor exit code (1) and inspect exit code (0) are derived from no record and no
   derivation row; the entry discloses them as L1-session observations, which Q11 permits
   ("a value cited only to prose is labeled recorded"). Residual risk: if those records were
   regenerated by a re-run, nothing in the lane would re-check the two exit codes.
2. "Of 14 client registrations … 8 missing" is derived (D5/D6/D7), but the prose names the
   four aligned clients while leaving the eight missing ones implicit in D4; the derivation
   table's D4 output enumerates them, so Q16's stdout-match bar is met.

Decision: 10 PASS (Q01, Q02, Q03, Q04, Q05, Q06, Q09, Q10, Q11, Q16), 7 n/a (Q07, Q08, Q12, Q13, Q14, Q15, Q17), 0 FAIL.
