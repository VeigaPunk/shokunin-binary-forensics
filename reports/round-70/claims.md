# revenger round-70 claims — pre-registration (frozen before any seat scores anything)

date: 2026-10-25 · author: L1 `RevengerR70` (hyaku run 7, fresh-start round) · claim base (lane branch tip at
declaration): `3f5edbc206351232a3d2d801334dd930499ccaf5` (round-69 tip + the non-author round-69 verifier
spot-check, read-only for this lane)
counter: `reports/round-70/measure.py` sha256 `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`
(derived: `sha256sum reports/round-70/measure.py`) · red-before receipts, committed in this same revision
before any after-run: `reports/round-70/measure-before.log`, `reports/round-70/before-treated-tools-on-base.log`,
and eight control receipts `reports/round-70/controls/*.log` built by `reports/round-70/build-controls.py`.

The predicate, counter, kill rules and targets below are frozen. A rule changed after a seat has scored is
not this claim's rule (kumitate r42; round-69 M50). This round's counter is a **new, small instrument** with a
new exit contract (0 holds green, 1 a named hold red, 2 the counter could not evaluate — an uncaught
exception maps to 2, never to 1); it does not repair the frozen round-69 counter and does not pre-empt the
open round-68/69 L0 questions. Every helper it calls is defined before first use.

## Fresh-start read (prompt section 6 run-7 block)

Last three closures read: `corpus/lessons/round-67-verifier-spotcheck.md` (rejected-honest-stop),
`round-68-verifier-spotcheck.md` (rejected-honest-stop), `round-69-verifier-spotcheck.md` (**rejected-harmed**:
freshness and operability harmed by self-inflicted regressions V5/V6, plus V1-V4, V7 routed). Pattern across
r65-r69: the C05 candidate was an author-built entry gated once by a wave, and each pass found new prose
defects; the lane's hit rate on the six pre-registered claims of rounds 67-69 is 1 met (r68 C1) of 6. This round changes the
*process*, not the target's size: wave 1 pre-gates and drives repairs of the candidate before it lands; wave 2
gates the landed bytes with fresh seats; and a mechanical lint catches the defect classes a script can see
before any seat is spent.

## Claims — three, on three distinct axes

### C1 — coverage (knowledge-map ground K, the lane's lowest non-retired criterion, 5.7): C05 fifth pass

**Claim.** `K_HELD_BACKED` moves 8/14 → 9/14 by admitting the round-70 candidate
`corpus/knowledge/round-70-apk-axml-byte-evidence.md` (v5: the round-69 v4 text with the routed repair set —
probe-or-drop the exit-2 clause (Q05); `:91` restated as direct string-pool indexing (Q07); labeled recorded
ZIP widths and signature (Q11/Q08); Q14-clean counts; the `c7b7cf98` identity derived and a Q15 row; the full
15-row §Q-map; S032/S034 anchor pins). Surface moved: frontier→core ground **C05 Android packages (APK)**,
`uncovered` → `held`. The command that would show it unmoved is the counter below.

**Frozen predicate (`HOLDS_C1_V5=yes`, same sentence in the counter's code and the receipt label).** At the
final lane tip: `K_HELD_BACKED=9/14` and `K_HELD_BACKED_STRICT=9/14` and `C05_STATUS=held` and
`C05_KNOWLEDGE_COLUMN` names exactly `knowledge/round-70-apk-axml-byte-evidence.md` and the entry carries
`admission-status: admitted` with no `admission-status: rejected` anywhere and `C1_GATE` reads
`checked_blocks>=17 problems=0` and `C1_LINT` exits 0 (`LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0`).
**And** every Q01-Q15 decision recorded by the fresh wave-2 seats on the landed candidate bytes is PASS or a
named n/a. The counter reads only the mechanical conjuncts; the wave decisions are the non-mechanical
conjunct, and a counter-only pass is **not** admission (control E below shows why).

**Landing order (frozen).** (1) The candidate lands with `admission-status: candidate` and the README row
unflipped. (2) Wave 1 findings (pre-gate) are advisory and drive repairs *before* step 1's landed bytes are
declared final; they are not kill-rule inputs. (3) Wave 2 (fresh seats, none of them wave-1 seats) decides
Q01-Q15 on the final candidate bytes. (4) All PASS/n-a → one revision flips README C05 → `held` naming only the
v5 entry and sets the header `admitted`. Any FAIL → the README stays `uncovered`, the header becomes
`admission-status: rejected` with every other byte kept, and the claim is **falsified — honest stop**, with no
re-gate in this round.

**Kill rule.** Any wave-2 Q FAIL carrying a located defect (path:line + the deriving command's output) falsifies
C1. A FAIL stands unless the L1 shows by command that the cited defect is absent from the landed bytes **and** a
second fresh reviewer seat concurs in writing; both are recorded. A wave-2 PASS never overrides a mechanical
label. No target narrowing after landing.

**Do-nothing controls (receipts committed).** A base tree reads `HOLDS_C1_V5=no`, K 8/14
(`controls/A-do-nothing-base.log`); flip-only (`B`), stub entry + flip (`C`) and the rejected v4 clone + flip
(`D`) all read `HOLDS_C1_V5=no` (gate/lint/backing conjuncts red). **Known limit of the counter, stated
before data:** a v4 clone with a padded 15-row §Q-map would satisfy every mechanical conjunct; that is why the
wave-2 decisions are part of the predicate and the counter alone never admits.

### C2 — calibration: self-assessment vs observed repo state

**Claim.** The lane's self-assessment records and its observed repository state disagree in a counted number of
places; this claim drives that count to 0 and ships the checker that counts it. Surface moved: a **new
tool** (`corpus/self_assessment_check.py`, registered as a gate) over the lane's own README index, SHONEN.md,
SCORECARD.md. Six mismatch classes SM1-SM6 are defined in the tool's docstring; each is re-derived from bytes or
`git cat-file`, not from prose.

**Before.** `SELF_MISMATCH=9` (SM1=1 README says `Q01–Q13` while QUALITY.md holds Q15; SM2=4 unnamed
`q15_tree_id_check.py`, `derive_axml_anchors.py`, `check_embedded_outputs.py`, `snapshots/`; SM3=2 SHONEN box 1
quotes `39098 bytes` / sha256 `bfd92057…` of SKILL.md whose bytes are now 51809 / `a12fb8e2…`; SM4=1 box 1 `[x]`
names the lane-dispatched seat `revenger-r64.R64ReviewSkill`; SM5=1 SCORECARD cites pre-registration
`e1d22caf`, which does not resolve; SM6=0) —
`reports/round-70/before-treated-tools-on-base.log`, command printed in that file.

**Frozen predicate (`HOLDS_C2_V5=yes`).** At the final lane tip: `SELF_MISMATCH=0` **and**
`SELF_CLEAN_FIXTURE=0` **and** `SELF_MUTANTS_KILLED=6/6` (the counter builds its own clean fixture and one
planted defect per class; the tool under test must score the clean fixture 0 and each defect exactly its class)
**and** `SHONEN_BOX_COUNT=4` **and** `README_ROWS=14` (the boxes and map rows are corrected, never deleted).
Unscored companion (considerthese `2026-10-24.md` proposal 3): a claim hit-rate ledger in
`corpus/lessons/round-70.md`, every cell derived by command.

**Kill rule.** Any conjunct false at the final tip falsifies C2. The claim is never narrowed: SM-class
corrections are made by editing the stale self-assessment (README index, SHONEN box state, SCORECARD erratum),
not by weakening the checker; the checker's bytes are re-attacked by a mutation-tester seat in wave 2.

**Do-nothing and gaming controls.** Base `HOLDS_C2_V5=no` (tool absent; `A`); an always-0 checker reads
`SELF_MUTANTS_KILLED=0/6` → no (`E`); deleting SHONEN boxes reads `SHONEN_BOX_COUNT=0` → no (`F`); the treated
tools laid over the unrepaired base reads `SELF_MISMATCH=12`, no (`H`).

### C3 — freshness: retained entries re-derive against the script revision that printed them

**Claim.** The round-68 retained candidate's embedded derivation block drifted when round 69 extended
`corpus/derive_axml_anchors.py` in place (`EMB_R68` problems=7, spot-check V6, freshness harmed). The gate
`corpus/check_embedded_outputs.py` learns a **digest-pinned historical-script** rule: an entry named in
`corpus/embedded_output_pins.json` re-derives against the pinned earlier script revision
(`corpus/derive_axml_anchors_r68.py`, sha256 `bce497d6…` = the S046 row's digest), which the gate verifies by
sha256 before use. Surface moved: the gate's coverage of retained candidates (an operation the gate did not
perform before).

**Before.** `EMB_R68=checked_blocks=17 problems=7` (`reports/round-70/measure-before.log`).

**Frozen predicate (`HOLDS_C3_V1=yes`).** `EMB_R68 checked_blocks=17 problems=0` **and**
`EMB_R65 problems=1` (the round-65 candidate legitimately retains its M39 transcription drift, so the gate must
still see it) **and** `EMB_R67 problems=0` **and** `EMB_R69 problems=0` **and** the r68 and r65 entry bytes
unchanged (`EMB_R68_BYTES_UNCHANGED=yes`, `EMB_R65_BYTES_UNCHANGED=yes`, pinned sha256 in the counter) **and**
`EMB_PINNED_SCRIPT_IS_S046=yes` **and** `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1` (a one-byte tamper of the pinned
script exits non-zero with the attributed text `pinned historical script digest mismatch`) **and**
`GATE_SELFTEST` exit 0 (below, in `HOLDS_OK_V7`).

**Kill rule.** Any conjunct false at the final tip falsifies C3. The registered C7 comparison line
(`problems += drift(lines, stdout_set, lineno)`) stays byte-identical; the open round-68 C7 L0 is not
pre-empted.

**Controls.** Base `HOLDS_C3_V1=no` (7 problems; `A`); deleting the seven drifting lines from the r68 entry
instead of fixing the gate reads `EMB_R68_BYTES_UNCHANGED=no` → no (`G`).

## Holds (every claim carries them; a red hold is "harm")

`HOLDS_OK_V7=yes` at the final tip: `HOLD_REPLAY=10/10` (every `verify_*.py --self-test` exit 0),
`GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`. Counter exit 0.

## Separability

Each claim is verifiable in a tree that carries only its own change: README index lines are claimed
per-claim (C1 names `lint_entry.py` and flips the C05 row; C2 repairs the Q-range line and names the four old
files plus `self_assessment_check.py`; C3 names `derive_axml_anchors_r68.py`), so no claim's tree raises another
claim's label above its base value. A wave-2 seat builds the three single-claim trees and reports each
claim's labels (`W2Separability*` seats).

## Admission and void conditions

Admission: every claim verifies and no axis is harmed. Void conditions (recorded, never hidden): counter exit
non-zero at the final tip; `HOLDS_OK_V7` not yes; a frozen predicate edited after any seat scored. No claim is
exploratory; no `unprovable-but-better` ruling is sought.

## Frontier step and assimilation (not claims)

SOURCES census before/after (`scripts/sources-census.sh validate`), one mined mistake in
`corpus/lessons/round-70.md` `## Mistakes`, C1 sourced (its entry cites S038/S043/S045/S032/S034/S047/S041,
re-opened this round, with the S045 row's `used-by` re-pointed old→new at admission, spot-check r67 item 4).
Assimilation (addendum section 10): considerthese `2026-10-24.md` proposal 3 (claim hit-rate ledger) is mined
under C2's companion; a `merge/revenger/` theme, if any entry clears the per-entry gates, is chosen in wave 1 and
recorded in the lesson's Gate with at least one admit and one reject, never as a README flip (the C05 row stays
single-entry under C1).
