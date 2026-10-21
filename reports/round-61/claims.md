# Round 61 pre-registration — claims, counting probe, predictions

Lane `revenger-shokunin`, hyaku round 61, attempt 1 (driver line
`.ufo/watchdog.log:614`, launch 2026-10-21T12:05:35-03:00; no earlier
round-61 attempt and no inherited `.ufo/waves/round-61/`). Claim base
`cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` (branch `main`, jj-colocated).
L1 coordinator: CloseChousa26 (reused idle agent; Main spawn job-capped).
Registered before any implementation or knowledge drafting.

Counting probe: `python3 -B reports/round-61/measure.py TREE`, where TREE is
`git archive --format=tar <commit> corpus | tar -x -C TREE`. It never writes in
TREE; mutants run in fresh temporary copies with `cwd=/`. Before output on the
base: `reports/round-61/measure-before.log`.

Scores in `SCORECARD.md` (fleet round-1 kaika table): calibration runnability
10.0, coverage F 5.0, coverage K 2.9, freshness 10.0. The lowest non-retired
criterion is coverage K; C1 works it. No stagnation waiver is used.

## C1 — coverage (knowledge-map K): admit gated entries on uncovered C04 and C09

Rows C04 (JavaScript/Electron packages) and C09 (EVM bytecode interfaces) are
`uncovered` at the base: work evidence exists (`fixtures/js-r3`, `js-r7-v2`,
`shapes-r12`, `verify_js_graph_delta.py`; `fixtures/evm-r19`, `evm-r21`…`evm-r26`,
`verify_evm_evidence.py`) but no knowledge entry.

Change: draft at most one entry per row, scoped to what the saved REA records
and fixture bytes show (C04: CommonJS destructured `require` named-import
edges and the package `main` entrypoint mapping as static inference; C09:
PUSH4 selector candidates and their JUMPDEST destinations as inferred
interface candidates, no execution). Each entry is admitted only if it passes
`corpus/QUALITY.md` Q01–Q11, cites at least one `corpus/SOURCES.md` row opened
in round 61 that is tier A for its scope, carries in-entry derivations (Q11),
and survives the wave-2 attacks. The README row flips `uncovered` → `held`
only for an admitted entry.

Counting: `K_HELD` printed by the probe (same regex as `SCORECARD.md:133`,
`grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md`).
Predictions: before `K_HELD=4/14` (2.9). After `6/14` (4.3) if both admit,
`5/14` (3.6) if one admits. `4/14` falsifies C1. Rejected candidates are
recorded with their failing Q id, never counted.

## C2 — calibration (receipt-identity mutation kill): kill kaika mutant b

`.ufo/waves/kaika-r1/mutation-post.md:15,21`: deleting the receipt-command
conjunct from `verify_icon_languages.py` and `verify_multi_icon_states.py`
leaves both scripts exiting 0, because neither carries an in-script
forged-receipt-command control. The data forgery (d2) is caught only while the
clause exists.

Change: each script's own run (`--self-test` or plain) must check a receipt
whose `command` is forged in memory and fail with a nonzero exit if that forged
receipt is accepted. Saved records and fixtures stay byte-identical. Each
script keeps exactly one `receipt['command']==<expr>` conjunct (the probe's
mutant site; more or fewer matches is could-not-evaluate, exit 2).

Counting: `C2_RECEIPT_B_KILLED=k/2` (mutant b: that conjunct and its `and`
deleted; killed = nonzero exit). New calibration criterion
"receipt-identity mutation kill", score `10 × k/2`.
Predictions: before `0/2` (0.0), after `2/2` (10.0).
Holds (any change voids C2): `C2_CONTROLS_PASS=2/2`, `C2_D2_KILLED=2/2`,
`HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, and
`git diff <base> <after> -- corpus/live corpus/fixtures` empty.

## Separability, harms, frontier

C1 touches only `corpus/knowledge/`, `corpus/README.md`, `corpus/SOURCES.md`
and the round lesson; C2 touches only the two verifier scripts. Each is
measurable with the other absent. Harm voids admission: a changed saved
record or fixture, a lost hold, an entry that overstates its evidence, or a
source row not opened this round.

Frontier step: `corpus/SOURCES.md` rows only after opening (≤25-word located
quote in `corpus/lessons/round-61.md` `## Gate`); census
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
before (`revenger ok`, exit 0) and after; one mined mistake; C1 is the
sourced claim.

## Amendment A1 — measurement hardening (2026-10-21, before any after-run)

Appended after the build wave's probe and pre-registration audits
(`.ufo/waves/round-61/build/ReviewerProbeAudit.md`, `CriticCalibrationClaim.md`,
`ReviewerPreregAudit.md`, `CriticSeparability.md`) and before the probe ran on
any changed tree. Original lines above are unchanged.

- C2 is admitted on `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`: a mutant-b kill counts
  only when the run's last line ends with `forged receipt command accepted`
  (the in-script control), never a crash or another assertion. The original
  `C2_RECEIPT_B_KILLED` line is still printed. The forged receipt differs from
  the saved one only in `command`, and the real receipt must pass first.
- C1 is admitted on `K_HELD_BACKED`: a held row counts only if every
  `knowledge/<slug>.md` its knowledge cell names exists. A README text flip
  alone counts 0. Rows other than C04/C09 must keep their base status, and the
  row count stays 14.
- Holds are now part of the probe exit: exit 1 when controls, d2,
  `HOLD_CALIBRATION` or `HOLD_REPLAY` fail (`HOLDS_OK=no`); exit 2 stays
  could-not-evaluate. Byte identity of saved records and fixtures is checked
  separately: `git diff --stat <base> <after> -- corpus/live corpus/fixtures`
  must print nothing.
- Base re-run with the amended probe on the same archive of `cf02419`:
  `K_HELD_BACKED=4/14`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK=yes`,
  exit 0 (appended to `measure-before.log`).
- Axis wording: "lowest criterion" means the lowest scored criterion at the
  base (K 2.9). The new calibration criterion is declared as a split in
  `SCORECARD.md` with its reason; its denominator is exactly the two kaika
  survivors and it is reported as a narrow regression guard, not a broad
  calibration gain. The other receipt conjuncts and the receipt clauses of
  `verify_named_multi_icon_states.py` and `verify_icon_states.py` stay outside
  the claim (`MutationReceiptConjuncts.md`, `ReviewerOtherVerifiersGap.md`).

## Amendment A2 — C1 scope narrowing (2026-10-21, before any entry drafting landed)

- C09 is restricted to what the seven saved `inspect_evm_interface` records and
  the fixture bytes show. Kaidoku already holds "`bytecodeOffset` is the JUMPDEST
  dispatch target" (`kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-evm-interface.md:151-153`).
  The revenger entry cites that as prior art (Q10) and does not claim the
  proposition as new ground. Its own subject is the lane's negative and decoy
  fixtures, where empty output has causes that are unknown.
- C04 is restricted to the single relative destructured `require` per fixture
  in `js-r3`/`js-r7-v2` and the package `main` edge, which the fixtures cannot
  separate from the `index.js` fallback. No Electron, ASAR, ESM, bundler,
  `exports` or named-export claim.

## Post-wave adjudication — frozen target unchanged (2026-10-21)

The initial 65-seat falsify wave died at the host-session kill. After the
first report was filed, the parent authorized one fresh validated wave
(66 seats, `.ufo/waves/round-61/falsify-w3/`) over landed `ab580698`.
This supplied the missing attack opportunity, not a relaxed admission gate.
Both candidates failed Q11 as written: C04 claimed its block carried edge
spans that it never printed; C09 asserted r24 counts/span/target without
in-entry derivations. Their original pass tables are superseded by the
rejection decisions in `corpus/lessons/round-61.md`.

C04/C09 return to `uncovered`; K is 4/14, the pre-registered falsifier for C1.
The rejected candidates and every counterexample remain as evidence; neither
is repaired or admitted this round. C2 remains causally separate at 2/2.

Timing clarification: A2 landed with the entries after the build drafts and
critics, not before drafting. The provisional README flips preceded the
attacks; the rollback corrects that premature admission rather than changing
the original target.
