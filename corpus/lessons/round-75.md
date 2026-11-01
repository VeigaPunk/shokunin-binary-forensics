# Round 75 — the r74 province probe's PATH-only blind spot: ghidra was present all along; criterion P2 + mismatch negative control; first local headless decompilation

Base `f29dc92b3adb4202195bc7fc25b4aa6a5b7a2563` (r74 tip + the non-author spot-check
commit). Declared claims: **C1 coverage** (criterion P revision — `province_probe2.sh`
plus the PROVINCE.md ghidra correction it forces) and **C2 calibration** (new bounded
criterion N — record-vs-reality mismatch detection, demonstrated with the v1 false-pass
as its red-before). Neither claim is exploratory. The capability
`ghidra-headless-recon` enters the SCORECARD capabilities table on this round's
demonstration (`reports/round-75/ghidra-headless-recon.log`).

## Gate

Fresh-start §7 duties: the three rejected closures named in the round prompt (r71, r72,
r73) were read in full (fleet `.ufo/reports/round-7{1,2,3}/revenger.md`) and spot-checked
before declaring. What was ruled out, and why (each a claim a do-nothing control reaches
or that is operator-blocked):

- **K-map admissions (C05 sixth+ pass, C15, C10)** — ruled out. C05 failed wave Q09/Q16
  (r71) and Q04/Q11b/Q13 (r70) with the repair bundle routed but every admission path
  requires the 16-seat Q-review surface, absent on this host (no `.ufo/state/`
  dispatcher; r74 planned item (b) and the filed L0 both say a K move stays blocked
  until the operator rules). C15: r72's own rejection note requires an independent
  source review plus the unchanged frozen counter first. C10: disposed `rejected` by
  the frozen kill rule in r74; no repair-and-revote under that claim.
- **Coverage F family moves (android / managed / browser-runtime)** — ruled out on
  producer evidence (S444, opened this round): the frozen F counter counts records by
  `operation` name (`inspect_android_package`, `inspect_managed_artifact`,
  `inspect_web_page`, …); the installed producer `rea` 6.8.0 declares 175 commands and
  **zero** `inspect_*` operations (`rea --llms` | `grep -cE 'inspect_'` → 0). A record
  hand-authored with a 6.5-era operation name would be fabricated producer evidence and
  was not attempted; a do-nothing control holds F at 5/8 either way.
- **P (province surface accuracy) as scored in r74** — not declared as-is: its probe is
  defective (below), so the honest move is the probe revision itself (declared C1).

Opened sources this round (both rows appended to `corpus/SOURCES.md`):

| row | path/command and representation | located quote (≤25 words) | decision |
|---|---|---|---|
| S443 | `C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC/Ghidra/application.properties` + `rea doctor` scope_checks, opened 2026-11-01 | `application.version=12.1.4` … `name: ghidra … classification: healthy` | ADMIT (tier A, own-host): grounds the PROVINCE ghidra correction and criterion P2 |
| S444 | `rea --llms` + `rea doctor` stdout, opened 2026-11-01 | `cli_commands: 175` … "Run one bounded Playwright browser scenario and return Evidence" | ADMIT (tier A, own-host): documents the F-block (zero `inspect_*` operations in 6.8.0) |

C1 (coverage — criterion P2, probe revision + forced record correction):

- Red-before: `bash reports/round-75/province_probe2.sh <fixture-with-base-PROVINCE.md>`
  → exit 1, `P2_SURFACES_RESOLVED=10/11 UNRECORDED_ABSENT=0 STALE_RECORDS=1 P2_SCORE=9.1`,
  `engine-ghidra STALE-RECORD (surface present on host; PROVINCE.md still records it
  absent)` (`reports/round-75/p2-before.log`; fixture = `git show f29dc92:PROVINCE.md`
  in a scratch dir with `.git/` and the bounty-module path stubbed, as P2 resolves those
  two surfaces against its argument directory).
- The contradiction is real in the committed base bytes: PROVINCE.md carried
  `[absent on this host, 2026-10-31: ghidra / analyzeHeadless — PATH probe]` while
  ghidra 12.1.4 has been installed off-PATH at `C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC`
  since 2026-10-26 23:14 (directory CreationTime) — five days before the r74 probe ran —
  and `rea doctor` reports ghidra, ghidra-headless and ghidra-native_decompiler healthy
  (S443).
- Landing: PROVINCE.md's ghidra line replaced by a dated present-record (one block, other
  lines untouched; the ida/jadx/binwalk/pwntools absent lines were re-verified today with
  the wider probe — PATH, `~/tools`, `/c/Program Files`, python imports — and remain
  absent; the re-verification is recorded here and in LOG.md without editing those
  lines, so the r74 receipts stay historically accurate).
- Green-after: `bash reports/round-75/province_probe2.sh` → exit 0,
  `P2_SURFACES_RESOLVED=11/11 UNRECORDED_ABSENT=0 STALE_RECORDS=0 P2_SCORE=10.0`
  (`reports/round-75/p2-after.log`).
- Instrument supersession, disclosed: v1 (`reports/round-74/province_probe.sh`) on the
  fixed bytes exits 1 by construction — its grammar has no PRESENT-record state, so it
  prints `engine-ghidra UNRECORDED-ABSENT`. P2 supersedes v1 as the criterion's
  instrument from this round (same pattern as the HOLDS_OK V1→V8 counter revisions);
  the r74 receipts remain the historical record of what v1 could see.
- Boundary: K stays 8/15 (5.3), F stays 5/8, no coverage-map row moved, no admission is
  claimed — P2 is instrument-level coverage, same bounded scope as r74's P.

C2 (calibration — criterion N, record-vs-reality mismatch detection):

- `reports/round-75/probe_negctl.sh` builds a stale-record fixture (the fixed PROVINCE
  with the ghidra present-record swapped back to the historical absent line) and runs
  both probe revisions on it, plus a record-less-absent fixture under a fake empty
  HOME, plus the fixed lane as positive control. Receipt
  `reports/round-75/negctl-run.log`, exit 0:
  `NEGCTL_V1_STALE_RECORD_FLAGGED=0/1` (v1 exits 0 on a record that contradicts the
  host — the demonstrable false-pass), `NEGCTL_V2_STALE_RECORD_FLAGGED=1/1` (exit 1,
  attributed `engine-ghidra … STALE-RECORD`), `NEGCTL_V2_UNRECORDED_ABSENT_FLAGGED=1/1`,
  `NEGCTL_V2_POSITIVE_CONTROL=pass`, `NEGCTL_SELFTEST=pass`.
- Attribution: the kill leg requires the specific `engine-ghidra` line and the
  `STALE-RECORD` token, not merely a non-zero exit. Criterion N score 0.0 → 10.0
  (before: the r74 instrument cannot flag the mismatch class; after: shown to fire, and
  shown to fire for the right reason, on the exact fixture).

Capability (`ghidra-headless-recon`): first local headless decompilation. Authored
fixture `corpus/fixtures/pe-r75-headless-smoke/` (generator byte-verifies its own
premises, Q06; regen byte-identical; sha256
`fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72`); headless run exit
0, `1 functions, 1 decompiled`, `entry @ 140001000` → `return 0x2a;`, matching the
authored entry bytes `B82A000000C3` and the truth pin — full receipt
`reports/round-75/ghidra-headless-recon.log`. On pe-r53 (committed resource-only
fixture) the same pipeline runs exit 0 and Ghidra's own output reports 0 functions; no
decompile claim is made from that leg.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| PATH-only presence probe (inherited r74 defect, P-probe class) | r74 `province_probe.sh:33` probes `command -v ghidra ‖ command -v analyzeHeadless`; ghidra 12.1.4 installed off-PATH 2026-10-26 23:14 (CreationTime), `rea doctor` healthy (S443); on 2026-10-31 the probe printed `engine-ghidra ABSENT-RECORDED … P_SCORE=10.0`, exit 0 | this round's first `rea doctor` run on this host | P2 probes PATH + the host tools convention (`~/tools/<name>*`) + `/c/Program Files` for engines; absent-record markers become per-surface tokens; mismatch made a fail state (STALE-RECORD) with a negative control (criterion N). Rule: an absent record must name the probe that established it, and a presence probe wider than that probe must be able to falsify it |
| restored-instrument mode drift (r74 carry-in, closed by note) | `git ls-tree 85db6ab reports/round-74/measure.py` → `100755` blob `50f8aae0`; same blob id at HEAD (`f29dc92`) with mode `100644` — bytes identical (equal blob id), mode changed by the r74 repair commit `704be4d` | r74 non-author closure carry-in routed to this round; re-verified here by `git ls-tree` at both commits | Mode-correction note recorded (this entry + LOG.md): treecommit cannot repair it — `update_tree` preserves the previous mode of an existing blob entry and pins `100644` for new blobs, and the docstring's `<path>[:mode]` syntax is not implemented in the helper's code — so no treecommit invocation can produce `100755`. Operational impact none (the instrument is invoked `python -B`). Rule: when a repair re-lists deleted files, verify `git ls-tree` modes against the pre-deletion tree, not only blob ids |
| frozen-counter / producer operation-name drift (routed) | F counter families count `operation` values (`inspect_android_package`, `inspect_managed_artifact`, `inspect_web_page`, …); `rea --llms` (S444): 175 commands, zero `inspect_*` in 6.8.0 | the §9 ruled-out sweep before declaring claims | Routed, not claimed: an F move first needs a registered counter revision mapping the current producer's operation names (or a producer-version pin frozen alongside the counter). A hand-authored record carrying a 6.5-era operation name would be fabricated producer evidence; not attempted |
| shared absent-marker genericity in the new STALE branch (self-caught, within-round) | first P2 draft reused v1's one generic marker `[absent on this host, 2026-10-31` for every surface; the red-before then printed 5 STALE lines (rea-cli, npx-fallback, bounty-triage-module, lane-repo, engine-ghidra) because the generic marker matches any line of the file | inspecting the red-before's 5 STALE lines before any after-run | per-surface dedicated absent-record tokens (`…: ghidra`, `…: ida`, `… — no ~/Projects tree exists`, …) plus sentinel tokens for surfaces that have no absent-record vocabulary yet (`[absent on this host: rea-cli]` etc.); red-before re-taken: exactly 1 STALE (the true defect) |
| generator assert-offset defects (self-caught, Q06 held) | `gen_pe_r75.py` first runs: assert sliced `.text` name as `0x188:0x193` (11 bytes for an 8-byte field) and checked `SizeOfRawData` at `0x1A0` where the field sits at `0x198` — both asserts failed on the built bytes; the header writes themselves were correct in both cases | the generator's own byte-verify step refusing to write (Q06 working as designed) | corrected assert offsets; regen check then byte-identical; the fixture's declared premises are re-derived from the built bytes, not from intent |

## Census

Round start (this host, sanctioned explicit-lane-dir invocation):
`bash <fleet>/scripts/sources-census.sh validate --root <fleet> <lane-dir>` → exit 0,
warnings W01/W04 only (28 W at start; disclosed classes: tierC-mined used-by W01s and
cross-scope duplicate-URL W04s inherited from the superseding-row corrections),
final line `ok … corpus/SOURCES.md`. Round end: re-run after the S443/S444 append;
receipt `reports/round-75/census-after.log`. Row count:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 442 at base
(`git show f29dc92:corpus/SOURCES.md |` same grep) → 444 after.

## Routed forward

- F counter revision for current-producer operation names (owner: a future registering
  round; needs a frozen mapping table, not an in-place edit of the frozen F command).
- `rea doctor`'s node gate (`24.21.0` vs required `>=24.22.1`; `environment_healthy:
  false`) and missing registrations are environment facts recorded here; substrate
  remediation stays refused per PROVINCE.
- The r74 P row's "10.0" is historical under v1; P2's red-before shows the honest base
  was 9.1 under a probe that can see the mismatch class. Both tables keep their own
  receipts; no historical byte is edited.
- Carry-in treecommit discipline (dir-arg class): this round's commit passes explicit
  file paths only, each verified on disk before invocation, followed by the mandated
  `git diff <base>..<new> --stat` check.
