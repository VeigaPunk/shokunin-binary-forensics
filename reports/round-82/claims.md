# round-82 claims (frozen before any after-run)

Base `33764dd29aaab69457327618e2a2c14900d5b634` (r81 tip + non-author
spot-check). This file, both sha-pinned instruments (`ag_probe.py`,
`orphan_sweep3.py`), the red-befores (`ag-red.log`, `countgrep-red.log`,
`sweep-v2-selftest-red.log`, `carryin-numstat.log`) and the preprobe receipt
(`preprobe-macho-shape.log`) freeze BEFORE the landing (fixture + producer
record) and BEFORE any after-run. Two claims, distinct axes (coverage,
calibration), causally separable, neither exploratory.

## C1 — coverage: a second artifact-graph operation (`trace_dylib_resolution`) moves through a real dylib-resolution producer record (criterion A1, registered this round)

Registered criterion A1 (`reports/round-82/ag_probe.py`, sha256 pinned
below) — an operation-record-depth criterion split from coverage (the same
split shape as K from coverage r1-kaika and C2 from calibration r61): the
rea-artifact-graph provider's declared operation group (S457, opened r81,
`available: true` / `availability_code: null` on this host, re-probed this
round): `decode_interface_builder`, `inspect_keyed_archive`,
`trace_dylib_resolution`. An operation counts RECORDED iff some
`corpus/live/runs/round-*/` carries both an `inspection.json` whose
`operation` equals the operation AND a `receipt.json` with `exit_code == 0`
and an `oracle.result` starting `ORACLE OK`. The probe prints
`A1_OP <op>=<round|unrecorded>` per operation and
`A1_RECORDED=<n>/3 score=<10n/3>`.

Denominator disclosure (pre-run, same shape as r79 F2 / r80 F3 / r81 F4):
A1 is a NEW instrument — its before-print exists only from this freeze
onward. On the base tree A1 prints 1/3 (3.33). Only a real
current-producer record on a second operation moves it to 2/3 (6.67).
`decode_interface_builder` stays unrecorded (an `.app`-bundle surface,
untouched this round) — A1's honest exception is 2/3, not 3/3. The
family-level instrument F4 (10/11) is NOT re-run as a claim: this record
does not move F4 (the family is already present); the moved quantity is
operation-record depth inside the covered family.

- BEFORE (red, committed `ag-red.log`): over the base archive `33764dd`:
  `A1_RECORDED=1/3 score=3.33` (only `inspect_keyed_archive=round-81`).
- WORK: author the inert two-image Mach-O fixture
  (`corpus/fixtures/macho-r82/`: generator whose 15-check self-check
  derives every byte-derived oracle fact from the built bytes — magics,
  cpu type, file type, ncmds, 8-alignment, install names, rpaths, load
  list, leaf-ness, tree layout; regen byte-identical 304 + 80 bytes;
  fixture shas `5f56d14d…9507d` / `bda3d4ff…bcf07`; `truth.json`;
  `oracle_check.py` with 37 BYTE + 10 pre-registered Q07 HYPOTHESIS checks
  — 47 total), run ONE bounded producer run on the committed bytes from
  the lane root (`rea trace-dylib-resolution
  corpus/fixtures/macho-r82/image/main.dylib --format json`, exact stdout
  saved, exit 0, stderr 0 bytes, receipt), oracle `ORACLE OK (47/47
  checks)`. Preprobe receipt committed at the freeze
  (`preprobe-macho-shape.log`, incl. the parser's cmdsize%8 constraint
  discovery and the resolved-case shape).
- AFTER (green, `ag-after.log`, landing archive): `A1_RECORDED=2/3
  score=6.67` with `trace_dylib_resolution=<round-82>`; oracle re-run over
  the landing-archive bytes, 47/47.

VERIFY conditions (all four must hold): (a) A1 prints 2/3 over the landing
archive; (b) the record's `operation == trace_dylib_resolution`, provider
`rea-artifact-graph`, subject sha == fixture sha, `evidence_id` form
`ev_<64hex>`; (c) oracle `ORACLE OK (47/47 checks)` over the archive bytes
(the 10 HYP checks pass against their pre-registered values — recorded
whichever way they fall); (d) F4 frozen instrument hold unchanged over the
landing archive (`f_probe4.py` 10/11, blob byte-equal to its r81 pin).
KILL RULE: any condition fails → the candidate record is retained rejected
(`admission-status` note in the LEDGER), README byte-unchanged, A1 prints
1/3 — recorded honestly as falsified.

Boundary: operation-record presence only; the record demonstrates the
built-in provider's dyld load-path resolution read of one authored inert
two-image tree (Q10 scope note in the LEDGER: no general Mach-O claim, no
app-bundle claim, no dyld load-simulation claim — the producer's own
coverage semantics stay unexplained; `decode_interface_builder` and the
android family stay unrecorded). No knowledge admission (K untouched, 8/15);
no README byte changes; PROVINCE byte-unchanged.

## C2 — calibration: orphan_sweep v3 — the counting-command fidelity class closes inside the standing instrument

v3 supersession of the r81 capability instrument (`reports/round-82/
orphan_sweep3.py`, sha256 pinned below; v2 `reports/round-81/
orphan_sweep2.py` and v1 stay byte-untouched). One named change (v3 change
5), closing the r81 non-author closure routed defect 1 (carry-in item 1):

5. Registered counting commands. Every plain run prints
   `SWEEP_PARSER_GREP_A=<n>` / `SWEEP_PARSER_GREP_B=<n>` /
   `SWEEP_PARSER_GREP_AB=<n>`, computed from the same rows the receipt
   prints — each value reproduces exactly by `grep -cE` over the
   FULL-format receipt with the registered corrected patterns:
   `^SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence`,
   `^SWEEP absent corpus/lessons/round-64`, and the corrected alternation
   `^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|corpus/lessons/round-64)`
   — with NO trailing space. The r81-closure-pasted trailing-space form
   returns 1, not the stated 2 (the multi-ref token prints
   `…evidence.md:57,:148,`; the first alternative can never be followed by
   a space) — first-hand reproduced at the freeze
   (`countgrep-red.log`: pasted = 1, corrected = 2, prefixes 1 + 1, over
   `git show 33764dd:reports/round-81/sweep-v1-red.log`). The selftest
   gains two legs: `SWEEP_SELFTEST_COUNT_FIDELITY=ok` (truth=2 on exactly
   that multi-ref shape, prefixes 1 + 1) and
   `SWEEP_SELFTEST_COUNTCMD_MUTANT_FLAGGED=ok` (the embedded trailing-space
   defective counter must disagree: 1 != 2; agreement = vacuous vector,
   attributed death). The frozen sed mutant (one substitution, pinned
   below) turns `COUNTCMD_PATTERN` into the trailing-space form; the
   mutated script's `--selftest` must die exit 1 with the attributed last
   line `selftest: counting-command fidelity drifted (trailing-space
   class)`. The `SWEEP_CORPUS` count-basis header (v2 change 3) stands
   unchanged — receipts cite basis lines first, never bare CITED values
   across corpora (carry-in item 3, adopted).

- BEFORE (red, committed `sweep-v2-selftest-red.log`): the committed v2
  instrument over the base archive — selftest exits 0 (`SWEEP_SELFTEST=pass`,
  7 legs) with ZERO count-fidelity legs
  (`grep -c "SWEEP_SELFTEST_COUNT\|SWEEP_PARSER" → 0`), and no plain run
  prints any `SWEEP_PARSER_*` value; the pasted-vs-corrected grep drift is
  reproduced over committed r81 bytes (`countgrep-red.log`).
- AFTER (green): v3 `--selftest` from the extracted landing archive
  outside any repo → 9 legs ok + `SWEEP_SELFTEST=pass`, exit 0;
  sed-mutated bytes die attributed (exit 1, the pinned last line);
  real-tree full receipt carries the `SWEEP_CORPUS` basis line + the three
  `SWEEP_PARSER_GREP_*` values + verdict summary
  (`sweep3-real-after.log`).

VERIFY conditions (all four must hold): (a) v3 selftest 9/9 legs + pass,
exit 0, hermetic (archive run); (b) sed-mutated v3 dies exit 1 with the
attributed last line; (c) real-tree full receipt: exit 0, LANDABLE_ORPHANS
0, `SWEEP_CORPUS` line present, the three `SWEEP_PARSER_GREP_*` lines each
reproduced by their registered grep over the receipt bytes; (d) v2 bytes
and v2 receipts unchanged (no rewrite of r81 evidence). KILL RULE: any
condition fails → v3 retained as a rejected candidate in
`reports/round-82/`, the carry-in corrections still land (they are
protocol duties, not claim-consequent), and C2 records falsified honestly.

Boundary: v3 moves no criterion score; the moved quantity is the standing
capability's counting-command fidelity (the drift class the r81 closure
caught by hand becomes machine-caught inside the instrument) plus receipt
value lines. Counts remain per-revision-corpus (v2/v3 erratum rule); every
narrative count in this round cites a `grep -c` of a named-corpus receipt.

## Frozen sha256 pins

- `reports/round-82/ag_probe.py` =
  `22be124b248338ccc7f29fd9096a86c86e0d15b2475073a2f6f026bbe74a08a5`
- `reports/round-82/orphan_sweep3.py` =
  `af64b4c5c2a36198d5cef2f399e9fba5791803f07c5fefd5896384c0913b8748`
- fixture bytes: `corpus/fixtures/macho-r82/image/main.dylib` = 304 bytes,
  `5f56d14d5648176be1dd3028ded42a298c5f198fc86b035a2dc914a96a49507d`;
  `corpus/fixtures/macho-r82/image/rpathdir/libalpha.dylib` = 80 bytes,
  `bda3d4ffb44d4d291f3388c265a4c773bc651310414b3772dad165c0a2bbcf07`
  (scratch-built bytes, copied unchanged into the landing)
- frozen sed mutant recipe (C2): `sed 's/corpus\/lessons\/round-64)"/corpus\/lessons\/round-64) "/'`
  applied to `reports/round-82/orphan_sweep3.py` (exactly one substitution:
  the `COUNTCMD_PATTERN` string) — demonstration receipt
  `sweep3-mutant-kill.log` at adjudication.

## §7 fresh-start gate (r71/r72/r73 rejected closures re-read this round; fresh probes 2026-11-01)

All three closures are K-admission claims whose wave Q-review surface never
settled on this host (r71: Q09/Q16 FAIL at the wave; r72: wave unconfirmed,
no worker outcomes; r73: 34/64 spawned, 0 settled, no vote files) — a
do-nothing control reaches each identically here; K stays operator-blocked
(the r74 L0, re-read unanswered at the fleet `.ufo/l0-questions.md` this
round). Ruled out with fresh probes (2026-11-01):

- **F android** (the only unrecorded F4 family): `REA_JADX_MCP_JAR` UNSET;
  no jadx on PATH; `~/tools` = downloads/ + ghidra only — S448 receipt
  stands; F4's honest exception stays 10/11.
- **macho/signature F families**: `rea capabilities` → `unsupported_host`
  for the native-macho provider (demangle_swift, inspect_macho,
  inspect_plist, list_architectures) and the signature provider
  (inspect_signature, observe_native_ui) — S453 stands. NOTE: the
  artifact-graph provider's `trace_dylib_resolution` is a DIFFERENT surface
  (its own provider group, `available: true`, availability_code null on
  win32 — it parses the file, no macOS native utility is invoked), which is
  exactly why C1's route is manufacturable here.
- **K admissions**: the r74 L0 unanswered (re-read this round) — routed
  around, never treated as answered.
- **criterion C repair**: §9 sizing (the r78-r81 standing disposition).
- **criterion R extension / criterion N attribution pair**: stay routed —
  R's bounded extension is subsumed this round by C2's registered-counting
  form for the parser classes only; the full legacy-row extension and N's
  pair are NOT declared.
- **`decode_interface_builder`**: available but NOT claimed — it takes an
  `.app` bundle path (its `--help`); authoring a full inert app-bundle
  surface is a separate bounded round, not crammed into this one.

## Carry-in dispositions (r81 non-author closure; addressed first, all status-neutral)

1. **Red-grep count** — first-hand reproduced over committed bytes
   (`countgrep-red.log`): the pasted trailing-space pattern returns 1 (not
   the stated 2); corrected alternation 2; separate prefixes 1 + 1.
   Substance unchanged (v1 misdispositions exactly those two committed
   files). The fix lands as C2's v3 change 5 (registered corrected
   counting commands + mutation-checked fidelity vector), and this round's
   SCORECARD/LOG/lesson quote ONLY corrected-form greps.
2. **Correction numstat convention** — first-hand reproduced
   (`carryin-numstat.log`): raw numstat of the r81 correction vs its
   landing = `10 0` LOG.md (9 content lines + 1 blank separator = 10 raw
   added lines; 0 deletions). The r81 wording "0 deleted / 9 added" counted
   content lines excluding the blank separator. Correction appended in the
   adjudication LOG entry (counting convention stated; no in-place rewrite
   of the r81 entry).
3. **Receipt-vs-regrown-corpus comparability** — adopted: every sweep
   receipt this round carries its `SWEEP_CORPUS` basis line; narrative
   counts cite `grep -c` of named-corpus receipts; basis lines are compared
   first, never bare CITED values across corpora.

## Sources opened this round (rows appended inside the Registry after S458 at the landing)

| row | path/command | decision |
|---|---|---|
| S459 | `PYTHONUTF8=1 rea trace-dylib-resolution --help` + `PYTHONUTF8=1 rea capabilities` (provider `rea-artifact-graph` group, `available: true`), opened 2026-11-01 | ADMIT (tier A, own-work environment) |
| S460 | `corpus/live/runs/round-82/` (record, receipt, LEDGER) + `corpus/fixtures/macho-r82/` (fixture, generator, truth, oracle), opened 2026-11-01 | ADMIT (tier A, own-work) |
| S461 | `corpus/lessons/round-81-verifier-spotcheck.md` §6 defect 1 (the routed repin rule), opened 2026-11-01 | ADMIT (tier A, own-work) |

C1 is sourced by S459 + S460; C2 is sourced by S461.
