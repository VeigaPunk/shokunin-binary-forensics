author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# round-85 verifier spot-check — revenger (hyaku closure, non-author)

Lane round: revenger 85. Base `8cf92f0c7c3d983181ac458ae90c2bb687226f62` → tip
`d14e4c847a8895d9571b8fc2facaf840bf5d2687` (branch `main`, pushed). I did not
author this round; every number below was re-derived by me at closure time from
committed bytes, in a lane-local scratch dir, with read-only commands. All
extracted material was handled in scratch only; nothing in the lane repo or the
fleet root was written or mutated.

## 1. Conformance (step 1)

| check | result |
|---|---|
| report committed in fleet repo by lane identity | OK — `git -C <fleet-root> log --format='%an <%ae> %H' -1 -- .ufo/reports/round-85/revenger.md` → `revenger-shokunin <revenger@shokunin.local> 26eff811e1e263823b830f069b1ba5c3d390dfe7` |
| `SHONEN` heading | OK — `## SHONEN` with four `[~]` lines, each with a resolvable pointer (no `[x]` written; correct — `[x]` is non-author-only and this round's author could not write it) |
| cited lane commits exist + ancestry | OK — all eight (`8cf92f0`, `ac91c05`, `9cadaed`, `acfb3b4`, `d27cf95`, `8b49e2d`, `f09cada`, `d14e4c8`) resolve with `cat-file -e <h>^{commit}` and hold `merge-base --is-ancestor <h> refs/heads/main` |
| push state | OK — local `refs/heads/main` = `d14e4c847a88…` = `ls-remote origin refs/heads/main` |
| reachability | OK — `git log 8cf92f0..d14e4c8` is exactly the seven lane commits, linear chain, all authored `revenger-shokunin` |
| dispatch/complete digest | OK — watchdog digest in the closure contract (launch 2026-11-01T23:44:31-08:00, complete 2026-11-02T02:19:07-08:00 head=`d14e4c847a88 pushed=True`) matches the landed chain and report |
| report minimum content | OK — work performed with evidence pointers, landed-changes table with LOG ties, before→after per claim with counting commands + measured commits, Sources & frontier (468 → 471 with counting command), trend verdicts, SHONEN |
| commit ordering | OK — freeze `d27cf95` (09:28:51Z) precedes landing `8b49e2d` (09:35:39Z) precedes adjudication `f09cada` (10:11:03Z); freeze's file list carries claims + instruments + reds + preprobe + mutant receipt + §7 gate and NOT the fixture/records (they first appear in `8b49e2d`) |
| evidence timestamps | OK — every receipt date (mg-after 09:37:36Z, noharm 09:45:28Z, census-after 10:07:20Z) is at or before the commit that ships it (`f09cada` 10:11:03Z) |
| landing numstat | OK — `diff-tree -r --numstat 8b49e2d^ 8b49e2d` → 20 files, 1226 insertions, 0 deletions (matches report exactly) |

No conformance defects found. Notes (status-neutral observations) are in §6.

## 2. Claim C1 — coverage, criterion M (managed provider full available set). RE-MEASURED

Sha pins verified first, on bytes extracted from the tip commit:

- `git show d14e4c8:reports/round-85/mg_probe.py` → sha256
  `1840c30cf4f1cad0815c89ca80492053d4a43c5d752609a2edf33fa21a3ac03f` — matches the report pin.
- `corpus/fixtures/managed-r85/fixture.dll` (from `git archive d14e4c8 corpus`) → 1048 bytes,
  sha256 `94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760` — matches all three
  receipt `fixture_sha256` pins.

Red, disclosed AT the freeze (the honest 0/3 disclosure):

- `git show d27cf95:reports/round-85/mg-red.log` → three `M_OP …=unrecorded` lines,
  `M_RECORDED=0/3 score=0.00`. The freeze commit message itself discloses: "the r76 record
  predates the oracle-receipt gate, disclosed pre-freeze". The report carries the same
  disclosure (red is 0/3, not 1/3; r76 record not re-graded). VERIFIED.
- My own re-derivation over the base archive: `git archive 8cf92f0 corpus` extracted, then
  `PYTHONUTF8=1 python -I -B mg_probe.py <base-extract>/corpus` → `M_RECORDED=0/3 score=0.00`,
  byte-identical conclusion to the committed red.

Green:

- `PYTHONUTF8=1 python -I -B mg_probe.py <tip-archive>/corpus` →
  `M_OP inspect_managed_artifact=inspect-managed-artifact`,
  `M_OP inspect_managed_members=inspect-managed-members`,
  `M_OP inspect_managed_native_boundaries=inspect-managed-native-boundaries`,
  `M_RECORDED=3/3 score=10.00`, exit 0 — matches the committed `mg-after.log` green block.

Three committed oracles re-run by me over the tip-archive bytes (all exit 0):

- `oracle_check.py truth.json corpus/live/runs/round-85/inspect-managed-artifact/inspection.json fixture.dll` → `ORACLE OK (20/20 checks)`
- `… inspect-managed-members/inspection.json …` → `ORACLE OK (47/47 checks)`
- `… inspect-managed-native-boundaries/inspection.json …` → `ORACLE OK (39/39 checks)`

The oracle is a real detector, not a rubber stamp — negative control reproduced by me
(scratch copy of the members record, one field mutated `methods[0].name → SayHelloX`):
`ORACLE FAILED (46/47 checks)`, exit 1 — exactly the shape the preprobe receipt discloses
(preprobe mutated the same field to `WrongName`).

Byte-level integrity cross-checks, all OK:

- each `inspection.json`'s sha256 equals its receipt's `stdout_sha256` pin
  (`90440ec1…`, `8d81f038…`, `2217af2c…`);
- all three receipts carry `oracle.result` starting `ORACLE OK`, `oracle.exit_code` 0,
  `exit_code` 0, `stderr_bytes` 0 (on-disk stderr files are 0 bytes) — this is exactly the
  predicate mg_probe counts on, and exactly what the r76 record lacks;
- evidence ids match the report: `ev_0eea92d7…f796e2`, `ev_e5d7a0b9…ae359f4`,
  `ev_2115d335…063890ba`;
- generator re-run (scratch output path): `self-check OK`, regen wrote 1048 bytes,
  sha256 `94429fa4…` — byte-identical to the landed fixture;
- frozen holds re-run by me over the same tip archive: `A1V2_RECORDED=5/5 score=10.00`,
  `A1_RECORDED=3/3 score=10.00`, `F4_COVERAGE=10/11 score=9.09` — no hold moved.

**C1 verdict: verified (re-measured). coverage improved, 0/3 (0.00) → 3/3 (10.00) on the
registered instrument, measured `8cf92f0` → `8b49e2d`.**

## 3. Claim C2 — calibration, orphan_sweep v6. RE-MEASURED

Sha pins:

- `git show d14e4c8:reports/round-85/orphan_sweep6.py` → sha256
  `b2db45b07bc86ffd501971582730497e2d5ddc83e685665c200fc24b3c7f12b7` — matches the report pin;
  `FLEET_BARE_RESOLUTION = True` (change 9) present.
- `git show d14e4c8:reports/round-84/orphan_sweep5.py` → sha256
  `d9a7ba174ce3c30a4414fcebe8e074ea00d58bfce4cfbf2c2cdb76f888ca46cb` — matches the
  "v5 blob unchanged `d9a7ba17…46cb`" pin.

Selftest (from the committed blob): `PYTHONUTF8=1 python -I -B orphan_sweep6.py --selftest`
→ 21 `SWEEP_SELFTEST_*` legs all `ok` (18 carried + FLEET_BARE_RESOLVED /
FLEET_BARE_ABSENT_NEGATIVE / FLEET_BARE_MUTANT_FLAGGED) + `SWEEP_SELFTEST=pass`, exit 0.
Matches `sweep6-selftest-after.log`.

Mutant kill reproduced by me: `sed 's/^FLEET_BARE_RESOLUTION = True$/FLEET_BARE_RESOLUTION = False/'`
→ mutated sha `8a1706ee50446f89391f440b99e8bddef5f398125b0f4948814f3fb607005a78` (matches the
claims.md pin), diff is exactly line 115; `--selftest` on the mutant dies exit 1 with
`selftest: fleet-bare resolution drifted (fleet-bare class)`. Matches `sweep6-mutant-kill-after.log`.

Red pair at the freeze, verified from the committed logs (same pre-landing tree, basis
`fleet-reports=25 lessons=50 log=1` in both):

- `v5-full-prelanding.log`: `unmatched_recorded_absent=48`, no `fleet_resolved`;
  sample row `SWEEP absent MISSION.md | bare-token unmatched: no file named MISSION.md under HEAD or the working tree`;
  gating `CITED=1024 COMMITTED=964 LANDABLE_ORPHANS=0 ABSENT=60`, exit 0.
- `v6-full-prelanding.log`: `unmatched_recorded_absent=26 fleet_resolved=22` (26+22 = 48 —
  every moved row is accounted for); sample row `SWEEP absent-fleet MISSION.md | bare-token normalized: fleet/MISSION.md`;
  gating identical `1024/964/0/60`, exit 0.

Real-tree pair re-run by me over the lane repo + fleet root, from the committed blobs
(v5 then v6, `--format full`), same tree both runs:

- v5: `unmatched_recorded_absent=49`, gating `CITED=1048 COMMITTED=987 LANDABLE_ORPHANS=0 ABSENT=61`, exit 0.
- v6: `unmatched_recorded_absent=27 fleet_resolved=22` (27+22 = 49 — the structural invariant
  v5_absent = v6_absent + fleet_resolved holds), gating identical `1048/987/0/61`, exit 0,
  `ORPHAN_SWEEP_LANDABLE=0`.

My counts sit +1 report / +5 citations above the committed `sweep6-real-after.log`
(`1025/965/0/60`, basis `fleet-reports=25 lessons=50 log=1`) and the report's CLOSURE-PREP tip
confirmation (`1043/982/0/61`). This is the disclosed per-revision-corpus movement: fleet
commit `26eff811` (the round-85 fleet report, 2026-11-02T10:19:08Z) entered the citation
corpus AFTER the lane's tip confirmation (tip committed 10:12:46Z). Basis line cited first,
as the report instructs; gating class unchanged (`LANDABLE_ORPHANS=0`, exit 0, both instruments).

Separability receipts `c1-only.log` / `c2-only.log`: evidence-verified (committed; each shows
its claim's instruments present and the other claim's absent; c1-only M 3/3 + oracle 47/47,
c2-only selftest pass — consistent with my own independent re-runs of both instruments).

**C2 verdict: verified (re-measured). calibration improved (capability supersession v5→v6;
no criterion score moved — the moved quantity is bare-token attribution fidelity, machine-caught
with a mutation-checked switch and a same-tree red pair).**

## 4. Carry-in D1–D3 (r84 closure), verified

- **D1** — `reports/round-85/corrections.md` correction 1 landed (`9cadaed`): the r84 prose
  absolute corrected to the bare-token-class statement; the PATH-form twin row re-opened by me:
  `git show d14e4c8:reports/round-84/v4-invisible-red.log | sed -n '637p'` →
  `SWEEP absent reports/round-83/v4-postlanding-recon.log | exists nowhere on this host; recorded, nothing to land`.
  No in-place rewrite of any r84 surface (r84 file list untouched in the range). VERIFIED.
- **D2** — `.ufo/waves/round-85/postadjudication-sweep.log` committed (`9cadaed`):
  `CITED=1024 COMMITTED=964 LANDABLE_ORPHANS=0 ABSENT=60`, `ORPHAN_SWEEP_LANDABLE=0`,
  `exit_code=0`, basis `fleet-reports=25 lessons=50 log=1` cited first, run from the committed
  v5 blob (sha printed in the receipt header and re-verified by me). VERIFIED.
- **D3** — dual round-start census receipts committed (`acfb3b4`): sanctioned
  explicit-lane-dir form exit 0 (21 W01 + 10 W04, zero E); contract-literal form exit 2
  (`revenger-shokunin/corpus/SOURCES.md` missing under the fleet root — the disclosed r74–r84
  lineage, routed around, nothing assumed answered). I re-ran BOTH forms at closure: literal
  → exit 2 with the same missing-path line; sanctioned → exit 0, 21 W01 + 10 W04, zero E,
  final line `ok`. VERIFIED (the literal-form exit 2 persists as disclosed; see §6).

## 5. Discernment spot-check (step 3) — outside re-openings

Gate sample (lesson `## Gate`): three admits (S469, S470, S471), no explicit reject rows; the
round's reject-shaped decisions are the §7 fresh-start ruling-outs. I sampled two admits and
one reject, re-opened each source myself:

| item | decision | re-opened source (mine) | agree/disagree | reason |
|---|---|---|---|---|
| S469 provider surface | ADMIT (tier A, own-work) | `PYTHONUTF8=1 rea inspect-managed-members --help` — the quoted sentence "Inspect PE/CLI metadata members, signatures, CIL anchors, and ldstr string literals without loading target code" appears verbatim in the tool's own description; `printf … | wc -w` → 15 words, ≤25 as the Gate row states | agree | quote is verbatim, located (tool help), ≤25 words; the three-operation available set is real (the operations are the ones C1 records) |
| S470 records + fixture | ADMIT (tier A, own-work) | the three committed records/fixture themselves — my independent oracle re-runs 20/20, 47/47, 39/39; stdout-sha-to-receipt-pin equality; regen byte-identity | agree | "ORACLE OK (20/20 checks)" etc. are literal committed strings I reproduced from committed bytes; the oracle is a live detector (my negative control fails it) |
| S471 fleet-root bare-token class | ADMIT (tier A, own-work) | the committed pair logs — both quoted rows printed verbatim above (v5 absent unmatched vs v6 absent-fleet normalized) | agree | the class is demonstrated over ONE tree with identical gating; the quoted rows are exactly in the committed bytes |
| F android (§7 ruling-out) | REJECT-shaped (stay routed) | committed `freshstart-probes.log` probe 1 (`REA_JADX_MCP_JAR=UNSET`, no jadx) + my own host probe: `REA_JADX_MCP_JAR` UNSET, `command -v jadx` → absent | agree | the hard gate's absence is re-confirmed on the host at closure time; keeping F4's honest exception 10/11 is the calibrated call (F4 re-derived 10/11 by me) |
| ghidra-headless repeat (§7) | REJECT-shaped (no new measurement) | SCORECARD capabilities row `ghidra-headless-recon` (round-75, pointer `reports/round-75/ghidra-headless-recon.log`, fixture with regen pin) resolves at the tip | agree | the r75 capability row holds as cited; a repeat run would re-print an already-frozen measurement — the ruling-out is grounded, not evasive |

Census: contract validate command run by me — literal form exit 2 (disclosed D3 lineage),
sanctioned explicit-lane-dir form exit 0 (21 W01 + 10 W04, zero E). SOURCES.md row count at
tip: 471 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`) — matches the report 468 → 471;
S469–S471 each present exactly once, appended inside the Registry after S468.

## 6. Trend verdicts (with my evidence) and no-harm

- **expansion: improved** — M 0/3 → 3/3 re-measured end-to-end (probe, oracles, receipts, pins,
  regen); no knowledge admission claimed or made (K untouched; `corpus/knowledge` absent from
  the changed-file list); F4's honest exception re-derived 10/11.
- **quality: improved** — a new registered criterion with a byte-derived oracle split whose
  negative control I reproduced as failing; the standing sweep's routed class became
  machine-caught with a mutation kill I reproduced (same sha, same line, same attributed death);
  all verdicts re-derive from committed bytes (I re-derived every one).
- **discernment: improved** — six real mistakes mined with class · evidence · captured-by · fix
  (lesson `## Mistakes`); the two treecommit no-op catches are corroborated by the commit chain
  itself (`ac91c05` is EMPTY — `diff-tree` on it shows no file change; `9cadaed` carries 2 of 4
  files; `acfb3b4` completes them); the honest 0/3 disclosure and the 7-vs-8 group count are
  recorded rather than papered over.

No-harm: full `diff-tree -r --name-status 8cf92f0 d14e4c8` — only `LOG.md`/`SCORECARD.md`/
`corpus/SOURCES.md` appends (numstat 9/0, 76/0, 3/0) plus additions; `SKILL.md`, `PROVINCE.md`,
`SHONEN.md`, `corpus/README.md`, `corpus/knowledge/`, `corpus/QUALITY.md` byte-unchanged;
orphan_sweep[1-5] + ag_probe + ag_probe2 + f_probe4 absent from the range (v5 re-hashed
`d9a7ba17…` byte-identical); FRESH_ROWS 12+6 = 18/18 re-derived. Per-axis: coverage improved
(C1), calibration improved (C2), freshness unchanged (18/18 hold), depth unchanged,
operability unchanged, adjacency unchanged. No axis harmed; neither claim exploratory.

## 7. Routed items for next round (status-neutral)

1. **mg_probe.py docstring prediction line** — the probe's pre-run denominator paragraph says
   "on the round base only inspect_managed_artifact is recorded, so M prints 1/3 (3.33)", but
   the frozen red prints 0/3 under the registered oracle-receipt definition (the r76 record
   predates the gate). The 0/3-not-1/3 shape is disclosed at the freeze, in claims.md, in the
   LEDGER and in the report, so substance is unaffected — but the docstring's own prediction
   line was not updated to the registered definition. Same precision family as r84's D1; a
   one-line docstring correction (new committed version, instruments are mutable) is owed next
   round the lane touches this file.
2. **Census contract-literal form exit 2** — persists as disclosed (r74–r85 lineage; the lane
   repo is not at `<fleet-root>/revenger-shokunin/`). Dual receipts landed again this round;
   routing stays operator-side. Nothing for the lane to fix locally.
3. **Per-revision-corpus basis movement** — the live fleet root grows between the lane's
   confirmation run and any later re-run (this closure re-run included: +1 fleet report,
   `26eff811`). The report's basis-first instruction is the right discipline; keep citing the
   basis line first in every future receipt.
4. **SHONEN boxes** — remain four `[~]` lane-asserted lines (correct for an author). The
   standing routed need for a non-author re-confirmation of the CURRENT SKILL.md bytes
   (round-69 spot-check V7; r84 closure D4) remains open for the operator; this closure did
   not check any SHONEN box and repeats that recommendation.

## 8. Closure decision

Both claims verify (re-measured by me from committed bytes), no axis harmed, no exploratory
claim, carry-ins D1–D3 landed and verified, conformance clean. **revenger round 85: status ok,
admitted.**
