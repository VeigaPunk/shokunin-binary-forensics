# revenger round-68 claims — pre-registration (frozen before any after-measurement)

date: 2026-10-24 · author: L1 revenger-r68 (attempt 1, Kimi fresh L1) · claim base
(lane branch tip at declaration): `f165908aaffcf14798de53405fe788986bd33ff9`
(round-67 tip `8e97e3a2…` + the operator considerthese sweep and the non-author
round-67 spot-check, both read-only for this lane)
counter: `reports/round-68/measure.py` sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`
· red-before receipt: `reports/round-68/measure-before.log` (run on the base tree
`f165908`, committed in this same revision, before any after-run)

Both claims are declared here **before** any seat scores anything. The predicate,
the counter, the kill rule and the target below are frozen: a rule changed after a
seat has scored is not this claim's rule.

## Why these two claims

The round-67 closure (`corpus/lessons/round-67-verifier-spotcheck.md`) closed the
round `rejected-honest-stop`, `admitted=false`, with both claims falsified on their
own frozen rules. Two lane-owned axes are open and each has exactly one routed,
mechanically-fixable defect:

- **calibration** — the C7 embedded-output gate landed but its *registered
  attribution* was false: `corpus/check_embedded_outputs.py:132-134` raises before
  the marker `require` at `:141`, so the marker is shadowed dead code
  (`C7_MUTANT_KILLED_ATTRIBUTED=0/1` while the mutant is killed). The r67 closure
  routed the fix; the r68 closure's contract says the repair must make the marker
  actually fire and fail the mutant, not merely relocate the dead code.
- **coverage** — the lane's lowest non-retired criterion (knowledge-map ground K,
  5.7) is unchanged at 8/14 because the C05 candidate was rejected on one anchor
  off-by-one (`:244` where the pinned snapshot has `:245`). The r67 lesson's fix
  shape (M44) is that the builder must *derive* symbol lines from the pinned
  snapshot programmatically instead of transcribing them.

The two claims are causally separable: C1 changes only `corpus/check_embedded_outputs.py`
and the counter's new C7 labels; C2 changes only a new knowledge entry plus one
README row. Neither counter reads the other's artifact (C1's counter labels read
the gate file; C2's aggregate reads the README row and the knowledge column).

## C1 — calibration: the C7 attribution repair (new criterion C8 on the same surface)

**Claim.** The registered embedded-output gate must be able to *attribute* its own
kill: the mutant that removes the verbatim comparison must die with the registered
marker as the last output line, and the attribution rule must reject any other
message.

**Frozen predicate (pass branch), all over the final measured tree:**

- `C7_GATE_PRESENT=yes`
- `C7_SELFTEST=pass`
- `C7_CONTROL_PASS=1/1`
- `C7_MUTANT_KILLED=1/1`
- **`C7_MUTANT_KILLED_ATTRIBUTED=1/1`** (the round-67 value was `0/1`)
- `C7_NEG_SPOOF_KILLED=1/1` **and** `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1` (the negative
  control: the same mutant with the marker *text* spoofed is killed but is **not**
  attributable — so the attribution rule cannot be satisfied by "any non-zero exit")
- `C7_RED_ON_R65_CANDIDATE=yes` (the gate still detects the committed M39 drift)
- `HOLDS_OK_V5=yes` **and** `HOLDS_OK_V6=yes`
- the counter's own exit code is `0`.

**Frozen mutant.** The round-67 mutant, unchanged: the single comparison call
`problems += drift(lines, stdout_set, lineno)` (the regex must match exactly once)
is replaced by `problems += []  # mutant: verbatim comparison removed`. The gate's
own `--self-test` must then exit non-zero **with its last output line ending
`drifted entry output accepted`**. Attributed iff both hold.

**Frozen negative control (new in this round).** The same mutant **plus** the
marker assignment `MARKER = "drifted entry output accepted"` replaced by
`MARKER = "drifted entry output accepted (spoofed)"` (the clause must match exactly
once). Expected: exit non-zero (killed) but `last.endswith(C7_MARKER)` false →
`C7_NEG_SPOOF_KILLED=1/1` and `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`.

**Kill rule (fail branch).** If the repaired gate's self-test does not exit 0, or
the frozen mutant is not killed, or `C7_MUTANT_KILLED_ATTRIBUTED` is not `1/1`, or
the negative control reads other than `1/1` and `0/1`, or any prior hold regresses
(`HOLDS_OK_V4` no, `HOLD_CALIBRATION` < 4/4, `HOLD_REPLAY` < 10/10,
`FRESH_ROWS` != 18/18), then C1 is reported **FALSIFIED** — honest stop, no
re-target, no repaired acceptance condition. The gate's registry row is then
corrected to state the measured truth (as round 67 did for its own false claim).

**Do-nothing control (red-before, committed history).** On the base tree
`f165908`: `C7_GATE_PRESENT=yes`, `C7_SELFTEST=pass`, `C7_CONTROL_PASS=1/1`,
`C7_MUTANT_KILLED=1/1`, **`C7_MUTANT_KILLED_ATTRIBUTED=0/1`**,
`C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`,
`HOLDS_OK_V5=no`, `HOLDS_OK_V6=no` (receipt: `reports/round-68/measure-before.log`).
The control cannot reach `1/1` on the attributed conjunct: the marker is
structurally unreachable in the base file, so no pass branch that does not change
the gate can produce it.

**Measured commits.** Before `f165908…` (`measure-before.log`); after = the final
measured tip (`measure-after.log`).

## C2 — coverage: the C05 re-gate, third pass, with machine-derived anchors

**Claim.** The lane's knowledge-map ground moves from 8/14 to 9/14 by admitting the
third-pass C05 candidate — the round-67 candidate plus the two `:244` → `:245`
anchor fixes, with **every** spec line number derived by a committed script from the
pinned snapshot instead of transcribed.

**The candidate.** `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, a new
file. It carries the round-67 v2 candidate's bytes with exactly these deltas:

1. `RES_XML_START_NAMESPACE_TYPE` is anchored at **:245** in both places (the r67
   candidate wrote `:244`, which is `RES_XML_FIRST_CHUNK_TYPE`);
2. the attrExt comment is anchored at line **686** and the field declaration at
   line **687** (the r67 candidate wrote the range `685-687`);
3. a new item 11 embeds the derivation command and its output — the anchors are
   printed by `corpus/derive_axml_anchors.py`, which searches the pinned snapshot
   bytes for each cited symbol and refuses to print a line it did not find
   (missing or ambiguous symbol = exit 2);
4. `corpus/snapshots/ResourceTypes.h` is a byte-exact copy of the lane's pinned
   snapshot (sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`,
   86255 bytes) so the derivation runs from any corpus tree;
5. `admission-status: candidate` — the README C05 row is **not** flipped at build
   time;
6. the readout, oracle and fixture bytes are **unchanged** since round 65.

**Frozen predicate (pass branch).** `K_HELD_BACKED=9/14` **and**
`K_HELD_BACKED_STRICT=9/14` **and** `K_ROW C05 status=held` **and**
`C05_SINGLE_V3=yes` (the C05 row's knowledge column names exactly the round-68
entry) **and** `README_TOKEN_LEGEND_MISMATCH=0` **and** `HOLDS_C2_V3=yes` **and**
`C7_V3_CLEAN=yes` (the candidate is clean under the repaired gate — 17 blocks, 0
problems) **and** every applicable Q01–Q13 decision of the dispatched wave on the
landed v3 bytes is PASS (n/a only with the entry's named reason) **and** the wave's
outside-discernment spot-check is not REJECT **and** the counter's exit code is 0.

**Kill rule (fail branch).** Any Q FAIL on the v3 bytes, or a spot-check REJECT →
the C05 row stays `uncovered`, the v3 entry is marked `admission-status: rejected`
(retained as evidence, every other byte kept), and C2 is reported **FALSIFIED** —
honest stop, no re-target, no repaired acceptance condition. The flip and the Gate
decision land in the same revision.

**Do-nothing control (red-before, committed history).** On the base tree
`f165908`: `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`,
`K_ROW C05 status=uncovered`, `C05_SINGLE_V3=no`, `HOLDS_C2_V3=no`,
`C7_V3_CLEAN=n/a (no v3 file)` (receipt: `reports/round-68/measure-before.log`).
The control cannot reach 9/14 without the new entry **and** the all-pass wave: the
C05 row is `uncovered` and no admitted entry backs it.

**Measured commits.** Before `f165908…`; after = the final measured tip.

## Frozen counter

`python3 -B reports/round-68/measure.py TREE` — invocation contract:

```sh
git archive <commit> corpus | tar -x -C <tree>
cd / && TMPDIR=/tmp/revenger-r68-counter-XXXX python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py <tree>
```

The counter is the round-67 counter plus the round-68 labels (`C7_NEG_SPOOF_KILLED`,
`C7_NEG_SPOOF_KILLED_ATTRIBUTED`, `C7_V3_CLEAN`, `C05_SINGLE_V3`, `C05_STATUS`,
`HOLDS_C2_V3`, `HOLDS_OK_V6`). Every round-66 and round-67 label keeps
byte-identical semantics; the exit contract is unchanged (2 = not evaluable,
0 = the V1 holds hold, 1 = a hold failed). The counter's sha256 is pinned above and
in `measure-before.log`; it is never edited after this revision.

## Admission order (binding)

1. Land the build with **no** README status flip. 2. Fresh in-wave attacks; every
   Q01–Q13 decision from a named seat that is not the author; blind independence =
   at least one seat derives the AXML enum anchors without the author's table.
   3. Adjudicate; flip the affected coverage row only on an all-criteria pass; a
   falsified claim stops honestly. 4. Calibration needs red-before below target
   (committed) and attributed counts at target at the final measured commit.
   5. Only the C05 row may change; the 14-row denominator, the ten-verifier replay
   set, `FRESH_ROWS` 18 and Q01–Q13 stay fixed.

## Void conditions

Changed `corpus/live` or `corpus/fixtures` bytes (this round registers **no** change
to any existing fixture or live path — the round-65 fixture bytes are the claim
surface and stay frozen; the only new corpus path is `corpus/snapshots/`, a
byte-exact copy of an already-committed snapshot); a lost baseline held row; a
README status change other than C05 (either-way); a changed denominator; weakened
Q01–Q13; attributed calibration counts below target (C2 2/2, C3 2/2, C4 2/2, C5 2/2,
C6 4/4, C7 1/1) or a negative control that reads other than `1/1` / `0/1`;
`HOLD_CALIBRATION` < 4/4; `HOLD_REPLAY` < 10/10; `FRESH_ROWS` != 18/18;
`STRICT_REJECT_WINDOW_SELFTEST` not pass; `HOLDS_OK_V4`/`HOLDS_OK_V5`/`HOLDS_OK_V6`
not yes; counter exit non-zero at final; prior rejected candidates altered (the
round-65 candidate and the round-67 candidate keep every byte, including the r67
candidate's drifted `:244` anchors — they are the red-before surface); any write
outside the lane repo + this round's report path.

## Wave contract (registered, not a claim)

ONE v2 wave of exactly 64 seats under `scripts/hyaku/ufo-wave-policy-v2.json`
(band 64–128, `maxLanes` 256), validated (`plan` exit 0) and dispatched as exactly
ONE batched call; ≥25% attack roles; build items (counter/census re-runs, the
anchor-derivation re-run) and attack items (Q01–Q13 on the v3 bytes, the C7 mutant
and spoof attacks, separability, claims critics, the discernment spot-check)
together; the §3 planner seat is held by the L1 (the validator rejects `planner`;
a bounded planning data-walk rides scout/connector items). The slot is acquired via
`scripts/hyaku/wave-slot.sh acquire` immediately before dispatch and released only
after settlement. Dead seats stay dead and are reported; no replacement seats.

## Registered (not claims)

The round-67 routed defects D1–D4 (abort-evidence strength, gate-vs-probe
reconciliation, the S045 quote word count, the S045 `used-by` re-point) are carried
as repairs in this round's report and lesson; they are not axis claims and are not
scored. The new registry row **S046** (own-work: the AXML anchor derivation) is
the frontier step's sourced row for C2. The item-10 assimilation posture for this
round is recorded in the report's Sources & frontier section.

## Frontier step (§2b)

One mistake is mined in `corpus/lessons/round-68.md` `## Mistakes` (class ·
evidence pointer · captured-by · fix), the census before → after is recorded with
both outputs and exit codes, and C2 cites the `S###` row opened this round
(`S046`, own-work, tier A, opened 2026-10-24) in the entry's `source:` header.
