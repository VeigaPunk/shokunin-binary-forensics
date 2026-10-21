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
