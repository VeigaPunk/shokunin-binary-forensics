# ReviewerGate — gate evidence, round 96 candidate entry

Seat: ReviewerGate (registry role: reviewer). Lane-internal vote, disclosed as such.
Candidate: `corpus/knowledge/round-96-native-analysis-sessions.md`
Candidate digest (vote-bound): `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`
Audit basis: `corpus/QUALITY.md` (Q01–Q17), `reports/round-96/claims.md` C1 section, the entry's own §Q-map (decided independently below, not copied).

## Digest and freeze checks (re-derived)

- Normalized candidate digest re-derived at the lane root with the frozen normalization
  (every `admission-status:` line replaced by `admission-status: candidate`): output
  `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` — equals the frozen claim value.
- Working-tree entry bytes equal the freeze commit's bytes:
  `git show ff767436feed32cf2f4074f05f938f8cea98e69a:corpus/knowledge/round-96-native-analysis-sessions.md | sha256sum`
  → `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923 -`; the file's own sha256 → the same value
  (the working tree already carries `admission-status: candidate`, so the plain file digest equals the normalized digest).

## Derivation table — every command re-run, every recorded output compared

| Entry value | Command re-run | Recorded in entry | Observed here | Match |
|---|---|---|---|---|
| fixture sha256 | `sha256sum corpus/fixtures/pe-r75-headless-smoke/fixture.exe` | `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72` | same | YES (size 1024) |
| regen identity | `python3 -B corpus/fixtures/pe-r75-headless-smoke/gen_pe_r75.py <ReviewerGate scratch>/fixture-regen.exe && cmp …` | byte-identical, exit 0 | `wrote … (1024 bytes)`; cmp silent, exit 0 | YES |
| Evidence ID | `grep -m1 evidence_id corpus/live/runs/round-96/rea-decompile.raw.txt` | `evidence_id: ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe` | same | YES |
| CLI provider line | `grep -A3 "^provider:" …rea-decompile.raw.txt` | `id: ghidra` / `name: Ghidra` / `version: 12.1.4` | same | YES |
| headless function count | `sed -n 3p corpus/live/runs/round-96/codeable-decompiled.c` | `function_count=1` | same | YES |
| headless entry line | `sed -n 4p …codeable-decompiled.c` | `// ==== FUNC entry @ 140001000 ====` | same | YES |
| decompiled body | lines 6–10 | `undefined8 entry(void)` … `{` … `return 0x2a;` … `}` and `// decompiled_ok=1 of 1` | body lines 6–10 exact; `// decompiled_ok=1 of 1` sits at line 13 | YES for values; locator under-covers (finding F1) |
| headless receipt | `grep -c "INFO  REPORT" …ghidra-headless-r96.log` | `6` | `6` | YES |
| record file digests | `sha256sum corpus/live/runs/round-96/*` | `d717b491…`, `6ce217fa…`, `2fba7fbf…`, `6a1d18c3…` | full digests match each prefix | YES |

## Independent checks beyond the derivation table

- Fixture premise from bytes, not prose: `xxd -s 0x200 -l 16 fixture.exe` → `b82a 0000 00c3 …` =
  `B82A000000C3` = `mov eax,0x2A; ret` (B8=mov eax imm32; imm32 little-endian 2A000000=0x2A; C3=ret),
  matching `truth.json` (`entry_file_offset 0x200`, `entry_bytes_hex`, `entry_bytes_meaning`,
  `expected_ghidra_function entry @ 140001000`, expected body contains `return 0x2a;`) — Q03/Q06 ground is outside the records under test.
- Quote-receipt side (claims C1 receipt legs): `S502.body` 38167 B sha256 `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24`;
  `S503.body` 35095 B sha256 `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc`; both receipts HTTP 200,
  `fetched_at 2026-11-05`, URLs pin commit `12f6e0974cc0db0b3a9b86246accc76556837222`; fetch-log lines present, including the
  honest 404 disclosure for the cli-command-map probe.
- Quote anchors verified inside the committed bodies (round-73 paired-delimiter comparison):
  S502 line 425 carries the exact sentence `…`rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally`;
  `## Native targets` at line 285; `## DOS MZ with Ghidra` at line 418; `procedure_pseudo_code` present; `inspect_native_load_image` at line 420
  ("use … to check measured loaded bytes…"). S503 frontmatter description carries the receipt quote
  "Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction." verbatim.
- Evidence record coherence: subject digest = the fixture's sha256; `operation: procedure_pseudo_code`; `procedure: "140001000"`;
  `raw_result.value` = `undefined8 entry(void) { return 0x2a; }` — matches the headless body and the authored premise.
- Doctor receipt (`rea-doctor-r96.txt`): `healthy: false`; `hopper` = `missing_analysis_engine`; `ida` not configured; all eight named
  ghidra scope checks `ok: true` (ghidra, ghidra-platform linux, ghidra-architecture x64, ghidra-installation, ghidra-version 12.1.4,
  ghidra-headless, ghidra-native_decompiler, ghidra-java 21.0.13) — exactly what the entry claims and only that.
- Coverage-map row: `corpus/README.md` row C02 = "native analysis sessions (decompile/disassemble providers)", currently `partial` —
  the row the entry names; the flip to `held` with the entry in the knowledge cell is a landing event, not a candidate-stage fact.
- Sequencing note (not a defect): `corpus/SOURCES.md` does not yet carry S502/S503/S504 rows; per claims §Frontier they are appended
  at landing. The frozen receipts pin the fetched bodies at candidate stage; the counter's C1_SOURCES leg checks the rows at `--rev <landing>`.

## Findings

- F1 (minor, non-blocking): the derivation-table row "decompiled body" cites `codeable-decompiled.c` lines 6–10, but the quoted item
  `// decompiled_ok=1 of 1` sits at line 13 (lines 6–10 are the body plus blanks). The value itself is correct and re-verified; the
  locator under-covers the last quoted member. Flagged against Q16/Q11; does not flip any decision.
- F2 (observation): the doctor receipt also reports `skill:identity` stale and several `config_drift` registrations — consistent with the
  entry's disclosed installed-copy (6.7.0-era) vs pinned-revision drift in Unknown; no undisclosed claim.

## Decisions (independent; entry's own row agreed on every decision; F1 noted under Q11/Q16)

PASS: Q01 Q02 Q03 Q04 Q05 Q06 Q09 Q10 Q11 Q14 Q16 (11)
n/a: Q07 Q08 Q12 Q13 Q15 Q17 (6; vocabulary-compliant notes in vote.json)

Rationale one-liners:
- Q01: route-contract claims rest on the pinned-revision fetched bodies (receipts, tier A) and session claims on the lane's own re-runnable record; S002 cited as context only. SOURCES rows pending landing per claims sequencing.
- Q02: header carries four source lines with URLs/paths and section anchors (not bare homepages), `verified-at` with date + commit, a concrete `recheck`, and `coverage-map: C02` matching README row C02.
- Q03: the expectation (`return 0x2a;`, entry bytes, function name) is fixed by the committed generator's asserts + `truth.json`, byte-verified here, never copied from the outputs under test.
- Q04: each run names tool, version and function (rea decompile / provider ghidra 12.1.4 / operation procedure_pseudo_code; analyzeHeadless 12.1.4 + committed postScript) and scores the tools' own printed output; no manual step is credited.
- Q05: capability statements carry this round's probes with command, date and observed exit (0 / 0 / 1) plus Evidence ID and receipt log; readiness is not generalized beyond the demonstrated surface.
- Q06: fixture premises byte-verified before producer calls (generator asserts; regen byte-identical re-run here; entry bytes read from the built bytes here).
- Q09: digests bind exact committed bytes (fixture, records, fetched bodies) and the entry explicitly disclaims origin/completeness/authenticity.
- Q10: scoped to the one fixture, one address, ghidra 12.1.4, this host, this date; absent engines recorded as absent; no universal claim.
- Q11: every count/identifier/offset/digest carries an in-entry deriving command and recorded output; all re-ran clean here (F1 locator note only).
- Q14: `B82A000000C3` carries "2 × 6 hex characters" (2×6=12 chars ✓); the ASCII rendering `mov eax, 0x2A; ret` decodes from that run ✓; truncated digest ellipses carry no length claim.
- Q16: every output-crediting sentence matches the command's actual stdout as re-run here; F1 is a locator-label imprecision, not an output overreach.

n/a grounds:
- Q07: no parser accept/refuse/cause prediction is offered; the expected body is an authored-bytes premise (Q03), not a parser hypothesis.
- Q08: historical criterion superseded by Q11, which is applied in full above.
- Q12: no rejected registry row is load-bearing; no reject reason or flip is cited.
- Q13: no verifier command is credited as mutation-guarding any clause; recheck targets are named without unguaranteed coverage claims.
- Q15: no git object id or tree identity sentence is asserted in the entry.
- Q17: no adjudication relocated a cited artifact for this entry; nothing to sweep.
