# revenger round-69 claims — pre-registration (frozen before any after-measurement)

date: 2026-10-25 · author: L1 revenger-r69 (hyaku run 6, fresh L1) · claim base
(lane branch tip at declaration): `222a7a702529fb60598633ebdf5e1442007bc15d`
(round-68 tip + the non-author round-68 verifier spot-check, read-only for this lane)
counter: `reports/round-69/measure.py` sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` (pinned below; a copy of the
round-68 counter `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`
plus the round-69 labels — C05 v4, Q15)
· red-before receipt: `reports/round-69/measure-before.log` (run on the base tree
`222a7a7`, committed in this same revision, before any after-run)

Both claims are declared here **before** any seat scores anything. The predicate,
the counter, the kill rule and the target below are frozen: a rule changed after a
seat has scored is not this claim's rule.

## Why these two claims

The round-68 closure (`corpus/lessons/round-68-verifier-spotcheck.md`) closed the
round `rejected-honest-stop`, `admitted=false`, with C1 verified (calibration
`improved`) and C2 falsified (coverage `unchanged`). It routed five defects:

- **D1** (calibration/evidence, medium): `reports/round-68/measure-after.log:102`
  states the `1c34603` `corpus/` tree is "byte-identical to the earlier measured
  14774a2c tree — 51894d15… — and to the receipt commit's". Observed:
  `1c34603:corpus` = `ddc6a4f6…`, `dddf147:corpus` = `51894d15…` — the identity
  sentence is false and the command it names contradicts it. Fix per the closure:
  restate, and add a criterion row that a stated git object id is re-derived with
  the command that names it. Same class as M46/M47; Q14 does not cover tree ids.
- **D2** (evidence durability, low): the wave-slot grant is not committed; commit
  the raw `acquire` output with the wave evidence, or present it at restatement
  strength (the slot file is now empty; the only committed trace is
  `R68WaveContractAudit.md:93`).
- **D3** (wave-shape precision, low): name the attack-share predicate counted under
  (the lane's own predicate vs the prompt §2 v2 floor's role list).
- **D4** (prose consistency, low): `SCORECARD.md`'s round-68 paragraph says SHONEN
  box 1 "keeps its `[~]`-with-outside-verifier state" while the report and the
  committed `SHONEN.md` read `[x]` with the named verifier `revenger-r64.R64ReviewSkill`;
  reconcile in this round's SCORECARD entry (append-only).
- **D5** (carried forward, still open): the counter C7 gameability, the
  `HOLDS_OK_V6`/`c7_v3_clean` separability coupling, kill-rule closure over every
  mechanical conjunct, the two-line partial-drift fixture, and the C05 repair set.

The lane's open L0 (`revenger | round-68`: may the next round replace
marker-presence with behavioural legs and drop `c7_v3_clean` from `HOLDS_OK_V6`?)
is NOT pre-empted: this round leaves the frozen C7 instrument and the V-labels
exactly as they are and works other calibration ground.

Two lane-owned axes are open:

- **coverage** — the lane's lowest non-retired criterion (knowledge-map ground K,
  5.7) is unchanged at 8/14 because the C05 candidate was rejected, on its third
  pass, on five wave Q FAILs whose causes are all enumerated and mechanically
  fixable (round-68 §Routed forward item 6).
- **calibration** — the D1 false identity sentence is an uncaught instance of the
  class mined as M46/M47 (an identity asserted against contradicting bytes), and no
  criterion covers it.

## C1 — coverage: the C05 re-gate, fourth pass, with the complete routed repair bundle

**Claim.** The lane's knowledge-map ground moves from 8/14 to 9/14 by admitting the
fourth-pass C05 candidate — the round-68 v3 candidate plus the full round-68
routed repair set:

1. `corpus/derive_axml_anchors.py` is extended with `RES_XML_FIRST_CHUNK_TYPE`
   (:244), the enum-block bounds (:237 open, :263 close) and the enum values, so
   **every** S038 line number and value the entry states is printed by the
   derivation (19 cited-symbol/bound lines + the sha256 line = 20 lines).
2. The entry's item 11 re-embeds the new 20-line derivation output and bounds its
   credit to exactly the numbers the command prints (no universal "every line"
   overstatement).
3. Item 5's struct-width table is labeled **manual** (transcribed in
   `readout.py:51-58` from S038's field lists); the Q04 "literal presented as
   derived" defect is removed.
4. The chunk-type enum-block range is corrected to 237-263 (open/close) with the
   AXML chunk-type subset at 239-253 — the v3 "237-253" range claim is number-
   drift from intent (the block runs to :263).
5. Item 7 drops "framework" from the resource-id sentence (the oracle-declared
   ids are claimed, not framework-wide semantics).
6. The resource-id/namespace-resolution sentence is re-scoped as an observation of
   this fixture's readout (Q07: no parser-behavior prediction written as fact).
7. The `META-INF/MANIFEST.MF` hex clause is corrected to Q14 shape (9 bytes quoted
   against "nine bytes", not "the 16-byte prefix").
8. The header gains `S032`/`S034` `source:` lines and pins `generator.py`'s sha256
   in the S041 source line.
9. The new own-work row **S047** (supersedes S046) records the extended derivation
   script (new sha256, 20 output lines); the entry's `source:` cites S047.

**The candidate.** `corpus/knowledge/round-69-apk-axml-byte-evidence.md`, a new
file carrying the round-68 v3 candidate's bytes with exactly the deltas above, and
`admission-status: candidate` — the README C05 row is **not** flipped at build
time. The readout, oracle and fixture bytes are **unchanged** since round 65.

**Frozen predicate (pass branch), all over the final measured tree:**

- `K_HELD_BACKED=9/14` **and** `K_HELD_BACKED_STRICT=9/14`
- `K_ROW C05 status=held`
- `C05_SINGLE_V4=yes` (the C05 row's knowledge column names exactly the round-69 entry)
- `HOLDS_C2_V4=yes`
- `README_TOKEN_LEGEND_MISMATCH=0`
- `C7_V4_CLEAN=yes` (the candidate is clean under the registered gate — exit 0)
- every applicable Q01–Q15 decision of the dispatched wave on the landed v4 bytes
  is PASS (n/a only with the entry's named reason)
- the wave's outside-discernment spot-check is not REJECT
- the counter's exit code is 0.

**Kill rule (fail branch).** Any Q FAIL on the v4 bytes, or a spot-check REJECT →
the C05 row stays `uncovered`, the v4 entry is marked `admission-status: rejected`
(retained as evidence, every other byte kept), and C1 is reported **FALSIFIED** —
honest stop, no re-target, no repaired acceptance condition. The flip and the Gate
decision land in the same revision.

**Do-nothing control (red-before, committed history).** On the base tree
`222a7a7`: `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`,
`K_ROW C05 status=uncovered`, `C05_SINGLE_V4=no`, `HOLDS_C2_V4=no`,
`C7_V4_CLEAN=n/a (no v4 file)` (receipt: `reports/round-69/measure-before.log`).
The control cannot reach 9/14 without the new entry **and** the all-pass wave: the
C05 row is `uncovered` and no admitted entry backs it.

## C2 — calibration: the Q15 tree-identity criterion (D1) and its restatement

**Claim.** The lane's self-assessment bar gains criterion **Q15** — a stated git
object id or tree identity must be re-derived with the command that names it — and
the round-68 D1 false identity sentence is restated correctly in this round's
lesson. The criterion is shown able to fail on the D1 sentence and to pass the
restated sentence.

**Frozen predicate (pass branch), all over the final measured tree:**

- `Q15_PRESENT=yes` (corpus/QUALITY.md carries the Q15 row)
- `Q15_SELFTEST=pass` (the committed checker's own true/false fixtures behave)
- `Q15_FALSE_KILLED=yes` (the checker flags the committed D1 false-sentence
  fixture `reports/round-69/d1-false-sentence.md` — the ability-to-fail receipt)
- `Q15_RESTATE_OK=yes` (the lesson's restated tree-identity sentence re-derives
  against `git rev-parse <hash>:corpus`)
- the counter's exit code is 0.

**Red-before (committed history).** On the base tree: `Q15_PRESENT=no` (no
criterion row), `Q15_RESTATE_OK=n/a` (no round-69 lesson), `Q15_SELFTEST=pass`
and `Q15_FALSE_KILLED=yes` (the checker ships with the claims revision and the D1
fixture is committed as evidence of the defect class). The control cannot reach
`Q15_PRESENT=yes` without adding the criterion row, and cannot reach
`Q15_RESTATE_OK=yes` without writing the corrected sentence.

**Kill rule (fail branch).** If `Q15_PRESENT` is not yes, or `Q15_SELFTEST` is
not pass, or `Q15_FALSE_KILLED` is not yes, or `Q15_RESTATE_OK` is not yes on the
final measured tree, C2 is reported **FALSIFIED** — honest stop, no repaired
acceptance condition.

**Measured commits.** Before `222a7a7…` (`measure-before.log`); after = the final
measured tip (`measure-after.log`).

## Frozen counter

`python3 -B reports/round-69/measure.py TREE` — invocation contract:

```sh
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive <commit> corpus | tar -x -C <tree>
cd / && TMPDIR=/tmp/revenger-r69-counter-XXXX python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py <tree>
```

The counter is the round-68 counter plus the round-69 labels (`C05_SINGLE_V4`,
`C7_V4_CLEAN`, `HOLDS_C2_V4`, `Q15_PRESENT`, `Q15_SELFTEST`,
`Q15_FALSE_KILLED`, `Q15_RESTATE_OK`). Every round-66/67/68 label keeps
byte-identical semantics; the exit contract is unchanged (2 = not evaluable, 0 =
the V1 holds hold, 1 = a hold failed). The counter's sha256 is pinned above and in
`measure-before.log`; it is never edited after this revision. The Q15 tree-id
verification uses `git -C <lane> rev-parse <hash>:corpus` (read-only) against the
lane's object store at measurement time; the text verified is the committed lesson
bytes from the archived tree.

## Admission order (binding)

1. Land the build with **no** README status flip. 2. Fresh in-wave attacks; every
   Q01–Q15 decision from a named seat that is not the author; blind independence =
   at least one seat derives the AXML enum anchors without the author's table.
   3. Adjudicate; flip the affected coverage row only on an all-criteria pass; a
   falsified claim stops honestly. 4. Calibration needs red-before below target
   (committed) and the criterion/restatement at target at the final measured commit.
   5. Only the C05 row may change; the 14-row denominator, the ten-verifier replay
   set, `FRESH_ROWS` 18 and Q01–Q15 stay fixed.

## Void conditions

Changed `corpus/live` or `corpus/fixtures` bytes (this round registers **no** change
to any existing fixture or live path — the round-65 fixture bytes are the claim
surface and stay frozen); a lost baseline held row; a README status change other
than C05 (either-way); a changed denominator; weakened Q01–Q15; attributed
calibration counts below target (C2 2/2, C3 2/2, C4 2/2, C5 2/2, C6 4/4, C7
1/1) or a negative control that reads other than `1/1` / `0/1`;
`HOLD_CALIBRATION` < 4/4; `HOLD_REPLAY` < 10/10; `FRESH_ROWS` != 18/18;
`STRICT_REJECT_WINDOW_SELFTEST` not pass; `HOLDS_OK_V4`/`HOLDS_OK_V5`/`HOLDS_OK_V6`
not yes; counter exit non-zero at final; prior rejected candidates altered (the
round-65, round-67 and round-68 candidates keep every byte); any write outside the
lane repo + this round's report path.

## Wave contract (registered, not a claim)

ONE v2 wave of exactly 64 seats under `scripts/hyaku/ufo-wave-policy-v2.json`
(band 64–128, `maxLanes` 256), validated (`plan` exit 0) and dispatched as exactly
ONE batched call; ≥25% attack roles; build items (counter/census re-runs, the
anchor-derivation re-run, the Q15 checker runs) and attack items (Q01–Q15 on the
v4 bytes, the C7 mutant and spoof attacks, separability, claims critics, the
discernment spot-check, the quarantine slice) together; the §3 planner seat is held
by the L1 (the validator rejects `planner`). The slot is acquired via
`scripts/hyaku/wave-slot.sh acquire` immediately before dispatch — the raw
`acquire` output is committed with the wave evidence (repair D2) — and released
only after settlement. Dead seats stay dead and are reported; no replacement seats.
Attack share is reported under **both** predicates: the lane's own
(`build-wave-spec.py` counters reviewer/critic/mutation-tester/sentinel/revenger)
and the prompt §2 v2 floor's (reviewer/critic/mutation-tester/labrat) — repair D3.

## Registered (not claims)

The round-68 routed defects D1–D4 are carried as repairs in this round's report,
SCORECARD entry and lesson (Q15 + restatement = C2; D2 slot receipt committed; D3
both predicates named; D4 reconciliation appended). D5 (counter C7 gameability, V6
coupling, kill-rule closure, two-line partial-drift fixture) stays open and is not
pre-empted (the C7 L0 is pending). The new registry row **S047** (own-work: the
extended AXML anchor derivation, supersedes S046) is the frontier step's sourced
row for C1. Item-10 assimilation posture: the register slice is re-derived and
hand-checked verdict-per-row (adoption stays closed; wave-4 remains in force).
considerthese: `2026-10-24.md` proposal 2 (provider-refusal seats recorded as their
own line) lands in the round lesson/wave record.

## Frontier step (§2b)

One mistake is mined in `corpus/lessons/round-69.md` `## Mistakes` (class ·
evidence pointer · captured-by · fix), the census before → after is recorded with
both outputs and exit codes, and C1 cites the `S###` row opened this round
(`S047`, own-work, tier A, opened 2026-10-25) in the entry's `source:` header.
