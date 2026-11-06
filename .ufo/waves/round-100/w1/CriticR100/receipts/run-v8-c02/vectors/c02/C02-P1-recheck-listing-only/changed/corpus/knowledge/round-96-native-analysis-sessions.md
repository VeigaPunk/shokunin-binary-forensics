source: S502 — REA native-and-artifacts reference, https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md — "Native targets" and "DOS MZ with Ghidra" sections, commit 12f6e0974cc0db0b3a9b86246accc76556837222
source: S503 — REA skill SKILL.md, https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/SKILL.md — frontmatter description (decompile code among the declared shipped-artifact uses), same commit
source: S504 — saved round-96 native-session record, `corpus/live/runs/round-96/` — the saved `rea decompile` Evidence, the ghidra-headless log and decompiled output, and the `rea doctor` receipt, opened 2026-11-05
source: S002 — installed REA skill, `~/.agents/skills/reverse-engineer-anything/SKILL.md` — declared version and CLI-first host policy context
verified-at: 2026-11-05 — S502 and S503 fetched this round at REA revision `12f6e09` (bodies committed at `reports/round-96/quote-receipts/raw/`, fetch log `reports/round-96/quote-receipts/fetch-log.md`); the session record was produced and saved this round on this host
recheck: `ls corpus/live/runs/round-96/` lists the saved record files
coverage-map: C02 — native analysis sessions (decompile/disassemble providers)
admission-status: admitted

# Native analysis sessions — the documented routes and one demonstrated session on this host

## Scope

This entry states (a) what REA's own reference documents about its native-analysis routes at
revision `12f6e09`, and (b) one demonstrated native-analysis session on this host on the
committed authored fixture, saved as a record with receipts. It is scoped to that fixture,
those tool versions, this host and this date. It does not claim general host readiness for
any artifact family, does not claim the absent engines (Hopper is reported missing by the
doctor receipt; no IDA is installed), and does not treat any digest as authenticity or
origin (Q09).

## The documented native-analysis routes (S502, S503)

At the pinned revision, the reference names the route facts below; each boundary sentence is
the reference's own.

| Documented fact (S502/S503 anchor) | Boundary the source itself states |
|---|---|
| Native analysis opens a binary and then uses focused search, procedure or function tools; addresses and recovered pseudocode are analysis observations, not original source (S502, "Native targets") | Provider unavailability and unsupported metadata remain unknown rather than false |
| `procedure_pseudo_code` decompiles a procedure; it also accepts a `procedure: "file-offset:0x…"` selector, and "CLI `rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally" (S502, "DOS MZ with Ghidra") | Existing symbols and analysis addresses win; multiple mappings fail as ambiguous; ELF virtual addresses are distinct from file offsets |
| `inspect_native_load_image` checks measured loaded bytes, file mappings, relocations and the entry against the immutable snapshot (S502, "DOS MZ with Ghidra") | Verified import covers the reported static image, not runtime behavior |
| Decompiling code is among the skill's declared shipped-artifact uses (S503, frontmatter description) | The skill's scope sentence is product intent; the reference sections above are the route contract |

## The demonstrated session on this host (S504)

The committed authored fixture `corpus/fixtures/pe-r75-headless-smoke/fixture.exe`
(authored round 75 by the committed generator; regenerated this round and compared) is a
1024-byte PE32+ whose entry point is the authored byte sequence `B82A000000C3` (2 × 6 hex
characters) = `mov eax, 0x2A; ret`. On 2026-11-05, on this Linux host:

1. The REA CLI route ran end to end: `rea decompile corpus/fixtures/pe-r75-headless-smoke/fixture.exe 140001000`
   exited 0 and printed an Evidence record saved at `corpus/live/runs/round-96/rea-decompile.raw.txt`.
2. The direct Ghidra-headless route reproduced the round-75 capability on this host:
   `analyzeHeadless` (Ghidra 12.1.4 at `~/.local/opt/ghidra_12.1.4_PUBLIC`) with the committed
   round-75 Java postScript exited 0; its receipt is `corpus/live/runs/round-96/ghidra-headless-r96.log`
   and its output `corpus/live/runs/round-96/codeable-decompiled.c`.
3. Readiness probes: `rea doctor` (receipt `corpus/live/runs/round-96/rea-doctor-r96.txt`)
   reports the ghidra scope healthy (ghidra, ghidra-platform linux, ghidra-architecture x64,
   ghidra-installation, ghidra-version 12.1.4, ghidra-headless, ghidra-native_decompiler,
   ghidra-java 21.0.13), with overall `healthy: false` because the Hopper engine is absent.
   The observed exit of the doctor run was 1; both facts are recorded, not reconciled away.

Derivation table (every value below is recorded with the command that derives it from the
primary record; outputs are the commands' actual stdout, truncated only at whole lines):

| Value | Deriving command | Recorded output |
|---|---|---|
| fixture sha256 | `sha256sum corpus/fixtures/pe-r75-headless-smoke/fixture.exe` | `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72` |
| regen byte-identity | `python3 -B corpus/fixtures/pe-r75-headless-smoke/gen_pe_r75.py /fast/scratch/hyaku/revenger-r96/l1/fixture-regen.exe && cmp /fast/scratch/hyaku/revenger-r96/l1/fixture-regen.exe corpus/fixtures/pe-r75-headless-smoke/fixture.exe` | `wrote …fixture-regen.exe (1024 bytes)` then no output and exit 0 (byte-identical) |
| Evidence ID | `grep -m1 evidence_id corpus/live/runs/round-96/rea-decompile.raw.txt` | `evidence_id: ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe` |
| CLI provider line | `grep -A3 "^provider:" corpus/live/runs/round-96/rea-decompile.raw.txt` | `id: ghidra` / `name: Ghidra` / `version: 12.1.4` |
| headless function count | `sed -n 3p corpus/live/runs/round-96/codeable-decompiled.c` | `function_count=1` |
| headless entry line | `sed -n 4p corpus/live/runs/round-96/codeable-decompiled.c` | `// ==== FUNC entry @ 140001000 ====` |
| decompiled body | `corpus/live/runs/round-96/codeable-decompiled.c` lines 6–10 | `undefined8 entry(void)` … `{` … `return 0x2a;` … `}` and `// decompiled_ok=1 of 1` |
| headless receipt | `grep -c "INFO  REPORT" corpus/live/runs/round-96/ghidra-headless-r96.log` | `6` (import, analysis, script, post-analysis, save, import succeeded) |
| record file digests | `sha256sum corpus/live/runs/round-96/*` | `d717b491…` (codeable-decompiled.c), `6ce217fa…` (ghidra-headless-r96.log), `2fba7fbf…` (rea-decompile.raw.txt), `6a1d18c3…` (rea-doctor-r96.txt) |

## Observation, inference, unknown

**Observation:** the cited reference sections at the pinned revision state the route facts in
the table above; the saved record shows one `rea decompile` Evidence (operation
`procedure_pseudo_code`) and one Ghidra-headless session, both exit 0, both reporting the
entry function decompiled with body `return 0x2a;`, matching the authored fixture premise
(Q06 fixture premise, Q03 expectation fixed by the generator's asserts and `truth.json`
before any producer call).

**Inference:** the documented REA native-analysis route is executable on this host through
both the CLI (`rea decompile`, provider ghidra 12.1.4) and the direct headless
(analyzeHeadless + postScript) form on this fixture; the lane can therefore run and record a
native-analysis session end to end here, as the round-75 capability already showed on the
prior host.

**Unknown:** whether the `evidence_id` is stable across re-runs on this route (the saved
record binds one run; a repeat run that prints a different Evidence ID would not contradict
this entry — the record's identity rests on its own saved bytes); whether other providers,
formats (ELF, Mach-O), packed targets or larger binaries behave the same; whether the
installed 6.7.0-era skill copy matches the pinned `12f6e09` bytes (the installed
`native-and-artifacts.md` differs in bytes from the pinned body — disclosed, and the rows
cite the pinned bytes).

## Limitations

- Fixture-scoped: exactly one authored 1024-byte PE32+ fixture, one address; no claim about
  any other artifact, provider, engine or family (Q05/Q10).
- The doctor receipt's overall `healthy: false` (missing Hopper engine) is recorded; only the
  ghidra scope is claimed, and only as observed on 2026-11-05.
- Documentation-side claims are pinned to revision `12f6e09`; the installed skill copy is
  6.7.0-era and is cited only as context (S002).
- No disassembly-level claim: the session output used here is the pseudo-code form; no
  instruction-level route was exercised this round.

## §Q-map

| Q | decision | entry evidence / boundary |
|---|---|---|
| Q01 | PASS | The route-contract claims cite tier-A rows opened this round (S502, S503, committed bodies and receipts); the session claims cite the lane's own re-runnable record (S504, own-work tier A) with digests and commands; S002 is context, not sole support. |
| Q02 | PASS | Headers list S-IDs with URLs/paths and anchors, `verified-at`, `recheck`, and the coverage-map row C02; the new rows carry receipt paths and the fetch date. |
| Q03 | PASS | The expected decompiled body (`return 0x2a;` from authored entry bytes) is fixed by the committed generator's asserts and `truth.json`, written before any producer call; the records under test never supplied the expectation. |
| Q04 | PASS | Each run names the tool, version and function (`rea decompile` on rea 6.7.0 driving Ghidra 12.1.4; `analyzeHeadless` 12.1.4 with the committed postScript) and scores the tool's own printed output; no manual step is credited as tool output. |
| Q05 | PASS | The readiness statements carry this round's probes with command, date and observed exit: the decompile run (exit 0, Evidence ID), the headless run (exit 0, receipt log), the doctor run (exit 1, ghidra scope healthy, Hopper absent). Presence claims elsewhere are not generalized. |
| Q06 | PASS | The fixture's premises were byte-verified before the producer calls: the generator's own asserts re-derive every declared field, and this round's regen is byte-identical to the committed bytes (derivation table). |
| Q07 | n/a | No parser-behavior prediction or pre-registered hypothesis is offered; see Q07 in corpus/QUALITY.md. |
| Q08 | n/a | Historical criterion superseded by Q11, applied below. |
| Q09 | PASS | Digests bind exact committed bytes only (fixture, record files, fetched bodies); none is offered as origin, completeness or authenticity. |
| Q10 | PASS | Scoped to the demonstrated fixture, versions, host and date; the missing engines are recorded as absent, not absorbed; no sibling scope is touched. |
| Q11 | PASS | Every count, identifier, offset and digest is stated in the derivation table with its deriving command and recorded output; the Evidence ID, file digests and function count are recorded values tied to commands, not memory. |
| Q12 | n/a | No rejected registry row is load-bearing for this entry's claims; see Q12 in corpus/QUALITY.md. |
| Q13 | n/a | No verifier command is credited as guarding this prose; the recheck commands are named with their re-derivation targets, and no clause is claimed as mutation-guarded; see Q13 in corpus/QUALITY.md. |
| Q14 | PASS | The one hex string with a length claim, `B82A000000C3`, carries the `2 × 6 hex characters` phrasing; no ellipsis-truncated run is length-claimed; the ASCII rendering `mov eax, 0x2A; ret` decodes from that same run (generator premise). |
| Q15 | n/a | No lane-tree git identity sentence is asserted; see Q15 in corpus/QUALITY.md. |
| Q16 | PASS | Each sentence crediting a command with output is checked against that command's stdout (derivation table outputs were pasted from the actual runs); the doctor's healthy-line count names the grep that produced it. |
| Q17 | n/a | No adjudication relocated a cited artifact for this entry; see Q17 in corpus/QUALITY.md. |
