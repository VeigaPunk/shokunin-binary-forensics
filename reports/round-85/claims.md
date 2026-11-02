# round-85 claims (frozen before any committed after-run)

Base `8cf92f0c7c3d983181ac458ae90c2bb687226f62` (r84 tip + the r84
verifier spot-check). Carry-in landing (THIS round's first commit, before
this freeze): the r84 non-author closure's three routed status-neutral
defects — (D1) the wording-precision correction
(`reports/round-85/corrections.md` correction 1; the fleet report prose is
orchestrator-owned and not rewritten; this file and every r85 text quote
the class exactly); (D2) the post-adjudication sweep absolute landed as a
committed receipt (`.ufo/waves/round-85/postadjudication-sweep.log`, run
from the committed v5 blob over tip+fleet trees: `CITED=1024 COMMITTED=964
LANDABLE_ORPHANS=0 ABSENT=60` exit 0, basis `SWEEP_CORPUS fleet-reports=25
lessons=50 log=1`); (D3) the dual round-start census receipts
(`.ufo/waves/round-85/census-round-start-{sanctioned,literal}.log`;
sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, disclosed
r74–r84 lineage, routed around). This file, the sha-pinned criterion-M
instrument (`mg_probe.py`), the sha-pinned v6 instrument
(`orphan_sweep6.py`), the red-befores (`mg-red.log`, the v5/v6 red pair
`v5-full-prelanding.log` + `v6-full-prelanding.log` over the SAME
pre-landing tree), the mutant-kill receipt (`sweep6-mutant-kill.log`), the
preprobe (`preprobe-managed-shape.log`) and the §7 gate
(`freshstart-probes.log`) freeze BEFORE the landing (fixture + producer
records) and BEFORE any after-run. Two claims, distinct axes (coverage,
calibration), causally separable, neither exploratory.

## C1 — coverage: the managed provider's full available set moves through real oracle-checked producer records (criterion M, 0/3 → 3/3)

Registered criterion M (`reports/round-85/mg_probe.py`, sha pinned below):
the rea-dotnet-static provider's full available-operation set counts
RECORDED iff some `corpus/live/runs/round-*/` carries both an
`inspection.json` whose `operation` equals the operation AND a
`receipt.json` with `exit_code == 0` and an `oracle.result` starting
`ORACLE OK`. Denominator disclosure (pre-run, S469): the provider declares
exactly THREE available operations (`rea capabilities` 2026-11-02:
`inspect_managed_artifact`, `inspect_managed_members`,
`inspect_managed_native_boundaries` — no unsupported group, unlike
artifact-graph's `inspect_asset_catalog`). The r76 record for
`inspect_managed_artifact` is real but predates the oracle-receipt gate
(its receipt carries no `oracle` field), so under the registered
definition it counts UNRECORDED: the red instrument prints 0/3, not 1/3 —
disclosed here and in the r76-record LEDGER before the freeze. The
members/boundaries pair has NO saved record anywhere under
`corpus/live/runs/` through r84 ("available-but-unrecorded", the r81/r82
scorecard class; the freshstart probe 2026-11-02 receipt). The scan shape
is the r84 v2.1 correction from birth (rglob `inspection.json` by name at
any depth under runs/ — the round-1-era `artifact-inspection.json` files
are not matched; no v1 defect to re-learn).

- BEFORE (red, committed `mg-red.log`): over the round-base archive
  `8cf92f0`: `M_RECORDED=0/3 score=0.00` with all three operations
  unrecorded; the r76 receipt's missing `oracle` field is the reason the
  artifact operation counts unrecorded.
- WORK: author the inert managed fixture (`corpus/fixtures/managed-r85/`:
  `generator.py` — a minimal IL-only PE/CLI image, 1048 bytes, built
  byte-by-byte with no compiler; `self_check()` re-opens the built bytes
  and re-derives every checked premise (PE/COFF + COR20 + metadata root +
  five streams + six tables + MethodDef rows + ImplMap + heaps); regen
  byte-identical across three builds including the landed copy;
  `truth.json` written by the generator's derive() from the built bytes,
  with the Q07 hypotheses frozen BEFORE the committed runs;
  `oracle_check.py` — 20 BYTE+HYP checks for the artifact record, 47 for
  members, 39 for boundaries, each BYTE check re-deriving its expected
  value from the fixture bytes with its OWN independent CLI-image parser
  (Q03: identity values never taken from the record or the generator);
  negative control demonstrated pre-run — one mutated producer field
  flips the members oracle to `ORACLE FAILED (46/47)`), run THREE bounded
  producer runs on the committed-path bytes from the lane root
  (`rea inspect-managed-artifact` Evidence
  `ev_0eea92d75cd2bb0d69be542825a96f9f2a98ea359ffdf607fd7cb910dbf796e2`,
  3190 bytes stdout; `rea inspect-managed-members` Evidence
  `ev_e5d7a0b9864b61a963b76848fb927fdbbbba6333c85602dcefbfe6c58ae359f4`,
  6974 bytes stdout; `rea inspect-managed-native-boundaries` Evidence
  `ev_2115d335dfdbe362fd4979099713275b2637394ebe73501614fad779063890ba`,
  3982 bytes stdout; all exit 0, stderr 0 bytes, receipts with fixture
  shas and Evidence IDs), oracles `ORACLE OK (20/20 checks)`,
  `ORACLE OK (47/47 checks)`, `ORACLE OK (39/39 checks)`.
- AFTER (green, `mg-after.log`, landing archive): `M_RECORDED=3/3
  score=10.00` with all three operations recorded; oracle re-runs over
  the landing-archive bytes reproduce all three OK lines; the frozen
  holds re-print: r84 A1v2 5/5, r82 A1 3/3, r81 F4 10/11 over the same
  archive.

VERIFY conditions (all five must hold): (a) M prints 3/3 over the
landing archive; (b) all three records carry `operation ==
inspect_managed_*`, provider `rea-dotnet-static`, exit 0, stderr 0
bytes, `evidence_id` form `ev_<64hex>`; (c) all three oracles reproduce
OK over the archive bytes (HYP checks against the pre-registered
`truth.json` — recorded whichever way they fall); (d) the frozen holds:
r84 A1v2 5/5, r82 A1 3/3, r81 F4 10/11 unchanged over the same archive
(the managed records do not move the artifact-graph criteria or the
family instrument); (e) fixture regen byte-identical from the committed
generator. KILL RULE: any condition fails → the candidate records are
retained rejected (`admission-status` note in the LEDGERs),
README byte-unchanged, M prints 0/3 — recorded honestly as falsified.

Boundary: operation-record presence on the managed provider's full
available set. The records demonstrate the built-in provider's static
PE/CLI metadata decode of one authored inert 1048-byte image (Q10 scope
notes in the LEDGERs: nothing loaded, nothing executed, no general
managed-format claim; the P/Invoke row declares an import from a
`native.dll` string that names no existing library — the provider's own
"managed-declaration-only" verification semantics, recorded as
observed). The r76 record is not re-graded (no in-place rewrite of r76
evidence). No knowledge admission (K untouched, 8/15); no README byte
changes; PROVINCE byte-unchanged.

## C2 — calibration: orphan_sweep v6 — the fleet-root bare-token class resolves inside the standing instrument (routed v6 candidate vector 2)

v6 supersession of the r84 instrument (`reports/round-85/
orphan_sweep6.py`, sha256 pinned below; v5 `reports/round-84/
orphan_sweep5.py`, v4, v3, v2, v1 stay byte-untouched). One named
change, the r84 lesson's second routed v6 candidate vector ("a fleet-side
basename resolution for absent-fleet bare tokens — each needs its own
falsifiable red/green"):

9. An unmatched bare token whose basename exists under the FLEET root
   resolves `absent-fleet` with note `bare-token normalized: fleet/<rel>`
   (up to 3 matches shown, `(+N more)` beyond; multiple matches listed,
   never silently one) instead of being recorded as an unmatched absent
   row. The routed defect live: the r84 lesson dispositioned the
   fleet-root bare names (`MISSION.md`, `AXES.md`, `PROTOCOL.md`,
   `LEARNING.md`, `CORPUS.md`, `l0-questions.md`, `MANIFEST.json`, …) as
   "the absent-fleet class, path-form twin already records them so" —
   but the BARE form still recorded them as unmatched-absent noise rows
   (48 on the pre-landing tree). v6 resolves them against a fleet-root
   basename index (os.walk, .git skipped); non-gating either way (absent
   and absent-fleet never gate; exit codes 0/1/64 unchanged).
   `SWEEP_BARE_TOKENS` gains an always-printed `fleet_resolved=` term
   (the `SWEEP_CORPUS` basis line's shape is unchanged). Red/green over
   ONE tree (the pre-landing worktree + fleet root, both receipts
   frozen): `v5-full-prelanding.log` — 48 unmatched recorded absent,
   rows `SWEEP absent MISSION.md | bare-token unmatched: no file named
   MISSION.md under HEAD or the working tree`;
   `v6-full-prelanding.log` — SAME tree, `unmatched_recorded_absent=26
   fleet_resolved=22`, rows `SWEEP absent-fleet MISSION.md |
   bare-token normalized: fleet/MISSION.md`; CITED/COMMITTED/
   LANDABLE_ORPHANS/ABSENT identical (1024/964/0/60) — v6 moves
   attribution, no gating value. The post-landing real-tree pair
   (v5-red vs v6-green over the committed adjudication tip) re-runs both
   instruments from the committed blobs and lands as the receipt
   completion (the r80/r82/r83 class); its green receipt must show the
   fleet class resolved and LANDABLE_ORPHANS=0 exit 0.

Selftest: v5's eighteen legs + three new vectors (fleet-bare resolved /
fleet-bare absent negative — a token under NEITHER pool still records
absent / fleet-bare mutant twin disagreement) = 21 legs +
`SWEEP_SELFTEST=pass`, exit 0. ONE frozen sed mutant (one substitution,
recipe pinned below), dying exit 1 attributed:
`FLEET_BARE_RESOLUTION` → `selftest: fleet-bare resolution drifted
(fleet-bare class)`.

VERIFY conditions (all five must hold): (a) v6 selftest 21 legs + pass,
exit 0, from the committed blob; (b) the sed-mutated copy dies exit 1
with the attributed last line, exactly one changed line; (c) the frozen
red pair shows the same-tree contrast (48 vs 26+22, identical gating
values); (d) the post-landing real-tree pair shows the fleet class
resolved with LANDABLE_ORPHANS=0 exit 0 from the committed blobs; (e)
v5 bytes and the r84 receipts unchanged (no rewrite of r84 evidence).
KILL RULE: any condition fails → v6 retained as a rejected candidate in
`reports/round-85/`, the carry-in landing stays (it is the closure duty,
not claim-consequent), and C2 records falsified honestly.

Boundary: v6 moves no criterion score; the moved quantity is citation
attribution fidelity (a bare token that names a real fleet-root file
stops being recorded as unmatched noise and is attributed to its actual
surface). Counts remain per-revision-corpus (basis lines cited first):
every receipt's `SWEEP_CORPUS` line names its corpus composition; the
red pair ran over the pre-landing tree, the real-tree pair over the
committed adjudication tip; movements disclosed in each receipt header.
Exit codes 0/1/64 unchanged (absent-fleet never gates; only
LANDABLE_ORPHANS does).

## Frozen sha256 pins

- `reports/round-85/mg_probe.py` = 3593 bytes,
  `1840c30cf4f1cad0815c89ca80492053d4a43c5d752609a2edf33fa21a3ac03f`
- `reports/round-85/orphan_sweep6.py` = 33109 bytes,
  `b2db45b07bc86ffd501971582730497e2d5ddc83e685665c200fc24b3c7f12b7`
- `reports/round-84/orphan_sweep5.py` (frozen r84, unchanged) =
  `d9a7ba174ce3c30a4414fcebe8e074ea00d58bfce4cfbf2c2cdb76f888ca46cb`
- fixture bytes (`corpus/fixtures/managed-r85/`):
  `fixture.dll` = 1048 bytes,
  `94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760`;
  `truth.json` = 2187 bytes,
  `210c68a22cf7dbaf220e26c539224394a631a9f8bc0a2cc074ae834b68046d83`;
  `generator.py` = 17688 bytes,
  `06a55942c5e090fcac9766e35c55687d7cc8802bf3bcbc727614501fa695b2cd`;
  `oracle_check.py` = 16227 bytes,
  `2c38ca030c44f4496dd4b2a9a3a6abdd254eb2bf4854f7780cf1056fa511ca88`
- frozen sed mutant recipe (C2, one substitution, verified by diff at
  demonstration — the mutated copy hashes
  `8a1706ee50446f89391f440b99e8bddef5f398125b0f4948814f3fb607005a78`):
  `sed 's/^FLEET_BARE_RESOLUTION = True$/FLEET_BARE_RESOLUTION = False/'`
  → dies `selftest: fleet-bare resolution drifted (fleet-bare class)`;
  demonstration receipt `sweep6-mutant-kill.log` at the freeze; re-run
  over the committed blob at adjudication
  (`sweep6-mutant-kill-after.log`)

## §7 fresh-start gate (r71/r72/r73 rejected closures re-read; fresh probes 2026-11-02, receipt `freshstart-probes.log`)

All three closures are K-admission claims whose wave Q-review surface
never settled on this host (r71: Q09/Q16 FAIL at the wave; r72: wave
unconfirmed, no worker outcomes; r73: 34/64 spawned, 0 settled, no vote
files) — a do-nothing control reaches each identically here; neither r85
claim routes through K. Ruled out with fresh probes (receipt
`freshstart-probes.log`):

- **F android** (the only unrecorded F4 family): `REA_JADX_MCP_JAR`
  UNSET; no jadx on PATH — S448 stands; F4's honest exception stays
  10/11.
- **macho/signature families**: `rea capabilities` → 7
  `unsupported_host` groups this round (8 at r84 — the provider's
  declared group composition moved between rounds; the lane owns no
  probe of why, only the count it prints) — S453 stands.
- **K admissions**: the r74 L0 unanswered (re-read this round) — routed
  around, never treated as answered.
- **criterion C repair**: standing §9 disposition (r78–r84).
- **criterion R full extension / N attribution pair**: stay routed —
  this round's calibration claim is the v6 fleet-resolution vector the
  r84 lesson routed as a named candidate.
- **M's route**: AVAILABLE and CLAIMED this round (C1) — the
  members/boundaries pair is the one route every standing ruling-out map
  left open (the freshstart probe prints both greps empty); the
  artifact operation rides the same fixture to close the r76 oracle-gate
  gap the registered definition exposes.
- **ghidra-headless** (a second do-nothing-control check): the r75
  capability row already holds (`ghidra-headless-recon`,
  `pe-r75-headless-smoke`); a repeat run reaches no new measurement and
  is not claimed.

## Carry-in dispositions (r84 non-author closure; addressed first, before any claim work)

1. **D1 — report prose imprecision** ("ZERO instrument rows" vs the
   PATH-form twin row): `corrections.md` correction 1 — the precise
   class statement and the standing wording rule; every r85 text quotes
   the class exactly or cites the r84 claims.md wording; no in-place
   rewrite of any r84 surface.
2. **D2 — post-adjudication sweep absolutes only in report prose**: the
   absolute is now a committed file —
   `.ufo/waves/round-85/postadjudication-sweep.log`, run from the
   committed v5 blob over tip+fleet trees, `CITED=1024 COMMITTED=964
   LANDABLE_ORPHANS=0 ABSENT=60` exit 0, basis
   `fleet-reports=25 lessons=50 log=1` cited first.
3. **D3 — literal census form**: standing operator-side lineage
   (r74–r84); dual receipts at round start, routed around, nothing
   assumed answered.

## Sources opened this round (rows appended inside the Registry at the landing)

| row | path/command | decision |
|---|---|---|
| S469 | `PYTHONUTF8=1 rea capabilities` (provider `rea-dotnet-static`: three operations, all `available: true`) + `rea inspect-managed-members --help` + `rea inspect-managed-native-boundaries --help` + `reports/round-85/freshstart-probes.log`, opened 2026-11-02 | ADMIT (tier A, own-work environment) |
| S470 | `corpus/live/runs/round-85/{inspect-managed-artifact,inspect-managed-members,inspect-managed-native-boundaries}/` (records, receipts, LEDGERs, oracle logs) + `corpus/fixtures/managed-r85/` (fixture, generator, truth, oracle), opened 2026-11-02 | ADMIT (tier A, own-work) |
| S471 | the r85 C2 class evidence — `reports/round-85/v5-full-prelanding.log` (v5: the fleet-root bare tokens recorded as unmatched absent rows) + `v6-full-prelanding.log` (v6: the same tree, absent-fleet normalized rows) + the r84 lesson's routed v6-vector note (`corpus/lessons/round-84.md` Routed forward), opened 2026-11-02 | ADMIT (tier A, own-work) |

C1 is sourced by S469 + S470; C2 is sourced by S471.
