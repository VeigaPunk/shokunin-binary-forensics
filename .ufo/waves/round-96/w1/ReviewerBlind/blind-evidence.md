# ReviewerBlind — blind derivation record (round 96, w1)

Seat: ReviewerBlind · role: reviewer · vote binding digest:
`2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`

Method honored: every derivation below was produced from `corpus/live/runs/round-96/`,
`corpus/fixtures/pe-r75-headless-smoke/`, and `reports/round-96/quote-receipts/raw/`
ALONE, before the candidate entry
`corpus/knowledge/round-96-native-analysis-sessions.md` was read. The entry was read
only after the table below was fixed.

## 0. Vote-binding preconditions (derived first)

| Check | Command | Result |
|---|---|---|
| Candidate digest (normalized admission-status → candidate) | `PYTHONUTF8=1 python3 -B -c "import hashlib,re; …"` per the task text | `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` — equals the frozen digest |
| Working tree == freeze commit bytes | `git show ff767436feed32cf2f4074f05f938f8cea98e69a:corpus/knowledge/round-96-native-analysis-sessions.md \| sha256sum` vs `sha256sum` of the file | both `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` (note: working-file digest equals the normalized digest because its single `admission-status: candidate` line already normalizes to itself) |

## 1. Blind derivations (pre-entry-read)

| # | Value | Source | Derived result |
|---|---|---|---|
| D1 | fixture sha256 | `sha256sum corpus/fixtures/pe-r75-headless-smoke/fixture.exe` (own run) | `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72` |
| D2 | entry-point byte meaning per generator asserts | `gen_pe_r75.py` asserts: `buf[0x200:0x205] == B82A000000` ("mov eax,0x2A"), `buf[0x205:0x206] == C3` ("ret"), entry RVA assert `0xA8 == 0x1000`, image base `0x140000000`, `.text` raw ptr `0x200`, TOTAL 1024 | entry bytes `B82A000000C3` (12 hex digits = 2 × 6; 6 bytes) at file offset 0x200 / RVA 0x1000 / VA 0x140001000 = `mov eax, 0x2A; ret`; deterministic, self-verifying generator |
| D3 | headless function_count | `codeable-decompiled.c` line 3 (own read); log line `REV75_DUMP wrote …: 1 functions, 1 decompiled` | `function_count=1` |
| D4 | headless entry line | `codeable-decompiled.c` line 4 | `// ==== FUNC entry @ 140001000 ====` |
| D5 | decompiled body | `codeable-decompiled.c` lines 6–10; Evidence `raw_result.value` | `undefined8 entry(void)` / `{` / `return 0x2a;` / `}` and `// decompiled_ok=1 of 1` |
| D6 | decompile Evidence evidence_id | `rea-decompile.raw.txt` first line | `ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe` |
| D7 | decompile Evidence provider lines | `rea-decompile.raw.txt` `provider:` block | `id: ghidra` / `name: Ghidra` / `version: 12.1.4` (also in `analysis_profile.provider`) |
| D8 | doctor ghidra-scope states | `rea-doctor-r96.txt` scope_checks | all eight ghidra* checks `ok: true` / `classification: healthy`: `ghidra` (install dir), `ghidra-platform` linux, `ghidra-architecture` x64, `ghidra-installation`, `ghidra-version` 12.1.4, `ghidra-headless` analyzeHeadless, `ghidra-native_decompiler` (elf x86_64 matches linux/x64), `ghidra-java` 21.0.13 JDK |
| D9 | doctor overall + missing engines | same receipt, lines 1–2 and scope_checks | literal line 1 `healthy: false`, line 2 `environment_healthy: false`; `hopper` `ok: false` missing_analysis_engine; `ida-registration` `ok: false` missing_analysis_engine ("IDA MCP registration is not configured") |
| D10 | rea CLI version on this host | `rea-doctor-r96.txt` line 307 | `cli_package_version: 6.7.0` (installed SKILL.md, S002 context: `version: "42"`, invocation `npx -y rea-agents@6.7.0`) |
| D11 | record file digests | `sha256sum corpus/live/runs/round-96/*` (own run) | codeable-decompiled.c `d717b491…`, ghidra-headless-r96.log `6ce217fa…`, rea-decompile.raw.txt `2fba7fbf…`, rea-doctor-r96.txt `6a1d18c3…` (full 64-hex in run log) |
| D12 | regen byte-identity | own run `python3 -B gen_pe_r75.py <scratch>/fixture-regen.exe && cmp …` | `wrote … (1024 bytes)`, cmp silent, exit 0 → byte-identical |
| D13 | headless receipt REPORT lines | count of `INFO  REPORT` in `ghidra-headless-r96.log` | 6 (Processing input files / Analysis succeeded / Execute script / Post-analysis succeeded / Save succeeded / Import succeeded) |
| D14 | committed round-75 postScript | glob lane | `rev75_dump.java` committed at `reports/round-75/rev75_dump.java` |
| D15 | pinned bodies vs claims | `sha256sum` + `wc -c` (own run) | S502.body 38167 B `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24`; S503.body 35095 B `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc` — equal to the frozen claim values |
| D16 | S502 quote anchors | grep of pinned body | `## Native targets` (L285) with "Addresses and recovered pseudocode are analysis observations, / not original source. Provider unavailability and unsupported metadata remain / unknown rather than false." (L290–292 verbatim); `## DOS MZ with Ghidra` (L418) with `inspect_native_load_image` sentence and the verbatim CLI file-offset sentence (L425) |
| D17 | S503 anchor | grep of pinned body | frontmatter description includes "…decompile code, or guide a reconstruction…"; pinned metadata `version: "49"` |

## 2. Entry vs derivations — mismatch list

Read after D1–D17. **Value/scope/boundary mismatches: NONE.** Row-by-row:

- fixture sha256 row = D1 ✓; regen row = D12 ✓ (same command shape, same outcome).
- Evidence ID row = D6 ✓; CLI provider row = D7 ✓.
- headless function count row = D3 ✓; entry line row = D4 ✓; body row = D5 ✓ (lines 6–10 exactly).
- headless receipt row = D13 ✓ (`grep -c "INFO  REPORT"` → 6, six items named in the row all present in the log).
- record file digests row = D11 ✓ (all four truncated prefixes match my full digests).
- doctor claim (item 3): the eight named ghidra-scope entries = D8 ✓ including versions 12.1.4 / 21.0.13 / linux / x64; "overall `healthy: false`" = receipt line 1 literal ✓; Hopper absent = D9 ✓; "no IDA is installed" ≈ `ida-registration` missing_analysis_engine (receipt wording: registration not configured — fair paraphrase, noted below).
- fixture premise `B82A000000C3` (2 × 6 hex characters) = D2 ✓ — 12 hex digits, decodes via the generator's own asserts to `mov eax, 0x2A; ret` (Q14 length phrasing is exact).
- S502/S503 route-fact table rows = D16/D17 ✓ — every quoted boundary sentence found verbatim in the pinned bodies at the named sections.
- Scope/Unknown disclosures: installed copy `version: "42"` + `npx rea-agents@6.7.0` vs pinned `version: "49"` — the entry's "6.7.0-era, bytes differ from pinned body" disclosure is accurate (D10/D17).

### Findings (non-blocking, disclosed for the record)

1. **Q16 dangling clause.** The entry's Q16 row ends "…the doctor's healthy-line count
   names the grep that produced it" — no such derivation row or sentence exists in the
   entry (the only `grep -c` row is the headless receipt row). The Q16 substance holds
   (every command-credited sentence I checked matches its recorded stdout), but this
   self-description clause is stale/dangling. Cosmetic wording defect only.
2. **Doctor causation not exhaustive.** Item 3 attributes `healthy: false` to "the Hopper
   engine" alone; the receipt shows a second `missing_analysis_engine` check
   (`ida-registration`). The entry's Scope discloses both absent engines, so the entry is
   internally consistent; noted for precision.
3. **"No IDA is installed"** is a paraphrase of the receipt's "IDA MCP registration is not
   configured" (classification `missing_analysis_engine` supports it).

### Verification gaps (claims consistent with the record but not byte-derivable from it)

- `rea decompile` **exit 0** (entry item 1): the saved Evidence carries no exit-code
  field; consistent (complete Evidence with raw_result) but not bound by record bytes.
- `analyzeHeadless` **exit 0** (entry item 2): the log ends `REPORT: Import succeeded`,
  consistent with exit 0, but the log does not record the process exit code.
- `rea doctor` **exit 1** (entry item 3): the receipt records `healthy: false` but not its
  own exit code; consistent with an unhealthy environment, not byte-derived.
- **"Committed" postScript at run time**: the script is committed at
  `reports/round-75/rev75_dump.java` (D14), but the headless log shows the run executed a
  scratch copy (`/fast/scratch/hyaku/revenger-r96/l1/rev75_dump.java`); byte-identity of
  that run-time copy to the committed bytes is not evidenced inside the record.

## 3. Vote basis

All seventeen Q rows were evaluated from the derivations above: fourteen PASS, three
scope-absent n/a beyond the entry's own six n/a (this reviewer's n/a set: Q07, Q08, Q12,
Q13, Q15, Q17 — same rows the entry marks n/a, each with a cross-reference note). The
candidate digest derives exactly to the frozen value, the working tree equals the freeze
commit, and no value, scope or boundary claim of the entry contradicts any blind
derivation. Verdict: the entry is met on the blind check; findings 1–3 and the four gaps
above are disclosed, none is disqualifying.

— ReviewerBlind, round 96 w1, 2026-11-05
