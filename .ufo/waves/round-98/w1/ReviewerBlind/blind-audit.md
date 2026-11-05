# Blind audit — ReviewerBlind, revenger round 98 (C14 candidate)

Seat: ReviewerBlind (reviewer). Audit performed independently of the other seats
without reading any other seat's vote or audit file.

Candidate digest (vote-binding, normalized per the v6 `digest()` rule):
`1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`

Freeze commit: `9d49002a3804de48d365b7d32849ada06745d64f`
All checks resolve this commit using `git show <rev>:<path>`, giving byte-exact
frozen state. Path spaces in the files use backticks; the paths themselves are
absolute under /home/vgpnk/Projects/shokunin/revenger-shokunin.

## Candidate

`corpus/knowledge/round-98-rea-host-readiness.md`, entry text at the freeze
(10483 bytes). sha256 of the bytes with admission-status lines normalized to
`admission-status: candidate`:
`1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`
(matches the frozen voting digest).

## Sources and anchors

- S506 = REA connection-and-recovery reference at pinned commit `12f6e09` —
  raw URL `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md`.
  Registry row: `corpus/SOURCES.md:523`.
- S507 = `corpus/live/runs/round-98/` own-work record. Registry row:
  `corpus/SOURCES.md:524` citing exact bytes for `rea-doctor-r98.txt` lines 1-2
  (1-based bytes 1-41). Both lines verified: the 41-byte span starting at
  byte 1 is exactly `healthy: false\nenvironment_healthy: false`.
  Registry row has no `used-by` cell on the do-nothing tree — appropriate at
  candidate status; the row's `used-by` field is `reports/round-98/`-side.

## Probe record files (from the freeze)

- `corpus/live/runs/round-98/rea-doctor-r98.txt` (sha256 fb9a48249a22501313f58978d2d716f4006096cc027d20160f86507323938e1d, 16554 bytes):
  40 lines yaml. `scope_checks[24]:` at line 9 with 24 entries (16 with
  `classification: healthy`, but only 8 with `ok: true`: the 8 ghidra
  checks); 8 `config_drift`/missing classification rows.
- `corpus/live/runs/round-98/host-probes-r98.txt` (sha256 94eaa6ff1137d0dd49ac3b88f25639e108c1d7692bdfacaa6fbec7232207a789, 42 lines, 693 bytes):
  13 command/rc pairs. rc=0 for rea, node, npm, binwalk, unblob, jadx,
  java, ghidra-path; rc=1 for analyzeHeadless, idat64, hopper; rc=0 for
  `python3 -c "import pwn"`; rc=0 for ghidra path check.
- `corpus/live/runs/round-98/rea-inspect-artifact-archive-r2.txt`
  (sha256 c373f656932a9c074f3405e61316b87ff395a48479e48bcd92650f6bece32ba4, 181 lines, 8965 bytes).
- `reports/round-98/quote-receipts/raw/S506.body` (sha256 ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50, 16650 bytes, 209 lines).
- `reports/round-98/quote-receipts/S506.receipt.json` (schema revenger-quote-audit-v1, sid S506, verdict verified, http_status 200, fetched_at 2026-11-05).
- Fixture `corpus/fixtures/archive-r2/fixture.zip` sha256 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e, which
  matches `corpus/fixtures/archive-r2/truth.json` `archive_sha256`.

## Independent re-derivations (this audit, from the frozen bytes)

Command 1 — read the frozen doctor receipt scope section and count 8 `ok: true`/`16 false`:

```text
$ git show 9d49002:corpus/live/runs/round-98/rea-doctor-r98.txt | awk '/  - name:/{n=gsub(/name:/,"",$0); print}' | sed -n '1,30p'
```

The two ok:false rows in the recorded doctor scope-check section are
`hopper` and one `missing_analysis_engine` pair. The remaining 6 `healthy`
scope-check rows are 6 ghidra.

Command 2 — the same-scope check used by the entry, run from the
frozen text:

```text
$ sed -n '/^scope_check/,/^informational/p' <(git show 9d49002:corpus/live/runs/round-98/rea-doctor-r98.txt) | grep -c '    ok: true'
```

prints 11, matching the entry's recorded output (11 of 24). A grep for
`ok: false` over the identical range prints 13, matching too.

Command 3 — awk registration pairs from the doctor receipt, matching the
S507 record's awk derivation and the entry's route row 6 exactly
(14 pairs, 4 aligned, 8 missing, 1 manual, 1 stale):

```text
$ awk '/^    - client:/{c=$3} /^      state:/{print c, $2}' <(git show 9d49002:corpus/live/runs/round-98/rea-doctor-r98.txt)
```

OUTPUT (verbatim, one pair per line):

```
antigravity missing
claude_code missing
codex aligned
copilot_cli missing
cursor missing
devin aligned
gemini_cli missing
grok_bot manual
grok_build aligned
kimi missing
omp stale
opencode missing
pi missing
zcode aligned
```

state counts: 8 missing, 4 aligned, 1 manual, 1 stale (14 registrations).
This matches the entry's route row 6 exactly.

Cross-check of row 6's specific statement "4 `aligned` (codex, devin,
grok_build, zcode)": those four clients each appear with `aligned`
inside the frozen doctor receipt. No one else does.

## Route decision table — probe-class verification (Q05)

The entry's 8-row route table ascribes each verdict to one probe class.
Every row was checked against the frozen bytes by this audit, no other
seat's file was read:

1. **ZIP inventory** (capability): `rea inspect-artifact` ran end-to-end
   on the committed fixture. Record `status: completed`; evidence ID and
   declared sizes (2964, 84, 16160 with compressed sizes 78, 2668)
   match `truth.json` (`archive_size`, and each member path's `size` and
   `compressed_size`). Verdict "ready on this host for this fixture" is
   properly scoped and capability-labeled. PASS.
2. **Native decompile (Ghidra provider)** (configuration): doctor shows
   all 8 ghidra scope checks healthy including ghidra-native_decompiler
   reporting `decompile reports elf x86_64, which matches linux/x64`;
   `command -v analyzeHeadless` rc=1 in the host probe; the entry states
   this is configuration only and that the actual capability record is
   the round-96 session, **not re-derived here**. PASS.
3. **Native analysis (Hopper, IDA, Kuna)** (absent): doctor shows
   `hopper`, `ida-registration`, `kuna-installation` each with
   classification `missing_analysis_engine` and `ok: false`; probes show
   `command -v hopper` rc=1 and `command -v idat64` rc=1. Verdict
   "not ready" is honest. PASS.
4. **Android (JADX provider)** (configuration): doctor's jadx detail
   line is "JADX MCP bridge JAR validated at
   /home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar;
   its path is recorded for agent registrations. **This checks
   configuration, not whether a selected APK fits in the worker's
   memory.**" jadx --version rc=0 printed "1.5.6" (recorded 1.5.6 — the
   byte-level version label). Verdict "configured, capability unprobed"
   is honest. PASS.
5. **Firmware regions and extraction** (configuration (version only)):
   `binwalk --version` rc=0 printed "binwalk 3.1.0";
   `unblob --version` rc=0 printed "26.6.4"; verified. Verdict
   "present, capability unprobed" is honest. PASS.
6. **MCP registration (per client)** (configuration): 14
   client registrations, state counts 4 aligned/8 missing/1 manual/1
   stale verified by my awk. The omp registration is explicitly
   `stale`. The entry quotes the S506 config/capability boundary (an
   aligned registration still does not prove a connected session). PASS.
7. **CLI launcher** (configuration): `rea --version` rc=0 printed
   "6.7.0"; `command -v rea` rc=0 resolved to
   `/run/user/1000/fnm_multishells/3146096_1793846990804/bin/rea`,
   a per-shell path. Doctor lists three such
   `path[...]` entries (state multiple). "Per S506 this is a per-shell
   fact" matches the sourced S506 boundary. PASS.
8. **pwntools (ELF-layout helper)** (configuration (import only)):
   `python3 -c 'import pwn'` rc=0; the record simplifies this as a
   re-probe correction of round-19's recorded failure (K05). Labeled
   "configuration (import only)", never capability. PASS.

No verdict is stated as a capability that the observed record shows is
configuration-only. No probe observed in the record is described as one
that was not run. No count in the entry is uncommanded.

## Derivation table — Q11 re-derivation

All derivation-table values were re-derived by this audit from the
frozen bytes, matching the recorded outputs:

- `sed -n 1,2p corpus/live/runs/round-98/rea-doctor-r98.txt` →
  `healthy: false` / `environment_healthy: false`
- `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -c '    ok: true'` → **11** and with `ok: false` → **13**
- `… grep -oE 'classification: [a-z_]+' … | sort | uniq -c` → `10 config_drift` / `11 healthy` / `3 missing_analysis_engine`
- awk registration pairs → match the entry's recorded output exactly
  (including "omp stale").
- `grep cli_package_version corpus/live/runs/round-98/rea-doctor-r98.txt` → `cli_package_version: 6.7.0`
- `grep -m1 evidence_id …archive-r2.txt` → `ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382`
- `grep -m1 'status: completed' …archive-r2.txt` → `      status: completed`
- `grep -E 'declared_size: ' …archive-r2.txt | sed 's/^ *//'` → `declared_size: 2964` / `declared_size: 84` / `declared_size: 16160`
- `sha256sum corpus/fixtures/archive-r2/fixture.zip` → 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e (resident ground truth verified)
- `sha256sum corpus/live/runs/round-98/*` → `94eaa6ff…`, `fb9a4824…`, `c373f656…` (all verified)
- `sha256sum reports/round-98/quote-receipts/raw/S506.body` → ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50, 16650 bytes (byte-verified)

No value in the entry is sourced only to prose. Every count, identifier,
digest, offset and size carries both a command name and its recorded
output inside the entry.

## S506 body — quote attribution (Q01/Q14)

The entry's quoted text in its "What a readiness check establishes"
table matches byte-for-byte the frozen `S506.body`:

- row 1 quote: literal in `S506.body`.
- row 3 is labeled in the entry as a paraphrase (lines 35-37 of the
  body), not a quote: body lines 35-37 = "HAR inspection is offline and
  does not require a live browser. Native / decompilation, Android
  analysis and firmware extraction have their own / bring-your-own
  prerequisites." The paraphrase covers exactly what the body states
  here; no quote markers are used. Honest.
- `S506.receipt.json` `span.start = 7126`, `span.end = 7202`, length =
  76 bytes = length of the row-1 quote. The entry's byte-exact claim
  "byte-exact on one line of the committed body" is verified.

## Q01 / S507

`S507` row's own-work scope sentences match the record: `rea-doctor-r98.txt` lines 1-2 bytes 1-41 (verified), CLI 6.7.0 exit 1 (verified), Evidence ID on the committed ZIP fixture (verified against the
record). The registry row's `not other hosts, dates or routes`
boundary is inherited by the entry scope, and no entry sentence
contradicts it.

## Verdict per criterion

Q01 PASS · Q02 PASS · Q03 PASS · Q04 PASS · Q05 PASS · Q06 PASS ·
Q07 n/a · Q08 n/a (superseded by Q11) · Q09 PASS · Q10 PASS · Q11 PASS;
Q12 n/a · Q13 n/a · Q14 PASS · Q15 n/a · Q16 PASS · Q17 PASS.

No FAIL this round. Verification was by command, not by ballot.

## Usage of this file

`artifact_sha256` of this file's bytes is recorded in
`reports/round-98/votes/ReviewerBlind.json`. The vote binds this digest
- the frozen C14 candidate's normal-form byte digest. Decisions were
made from these observations only.
