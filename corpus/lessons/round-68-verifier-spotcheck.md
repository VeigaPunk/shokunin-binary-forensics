# round-68 verifier spot-check — revenger

author: hyaku closure (non-author integrator, @m_flash)
agent: fresh hyaku closure subagent dispatched by the hyaku orchestrator, never by the lane. This
file was written after the round closed: no round-68 byte was authored, edited, improved or
repaired by this reviewer, no lane-authored file was touched, no subagent was dispatched, and no
lane-owned gate or counter was executed. Every number below was produced by a command this reviewer
ran itself on committed bytes (git/grep/wc/jq/sha256 over `git archive` trees) and is quoted as it
printed; where a claim rests on the lane's own instrument, its **committed evidence** was verified
instead of re-running the instrument, per the closure brief's gate rule.

lane: revenger · lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · fleet root:
`/home/vgpnk/Projects/shokunin`
lane HEAD before the round: `f165908aaffcf14798de53405fe788986bd33ff9` · after (tip):
`d00f77942d78cb9a3b41547370d7a8a4ebea6c72` (pushed; `ahead=0`, `tracked=0`, `untracked=0`)
report: `.ufo/reports/round-68/revenger.md`, committed in the fleet repo by
`revenger-shokunin <revenger@shokunin.local>` as `739ba3a0e7e9ea5b87ba525d5dca03e0a20272dc`
(on `origin/main`)
date: 2026-10-25 · round: 68 (hyaku, attempt 2)

## Verdict in one line

**C1 verifies — calibration `improved`. C2 is falsified by its own frozen kill rule and was executed
as an honest stop — coverage `unchanged`. No axis is harmed.** Lane status `ok` (real report, six
committed and pushed round commits, honest stop). Admission `false`, verdict
`rejected-honest-stop`.

## 1 · Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by the lane identity | `git log --format='%an <%ae> %H' -- .ufo/reports/round-68/revenger.md` (fleet repo) | `revenger-shokunin <revenger@shokunin.local> 739ba3a0e7e9ea5b87ba525d5dca03e0a20272dc` | PASS |
| report durable on the remote | `git -C … merge-base --is-ancestor 739ba3a origin/main` | exit 0 (`origin/main` = `51ceb0ee`) | PASS |
| `SHONEN` heading, one line per box | report §SHONEN vs `SHONEN.md` | heading present, 4 lines for the 4 boxes; box 1 `[x]` carries the pre-existing non-lane verifier `revenger-r64.R64ReviewSkill`; `SHONEN.md` is byte-identical base→tip, so no new `[x]` was written by this round | PASS |
| cited lane commits exist and are ancestors | `git merge-base --is-ancestor <hash> HEAD` for `f505526`, `4232235`, `14774a2c`, `dddf147`, `1c34603`, `d00f779` | all six `OK-ANCESTOR-HEAD`; each carries the lane identity and its stated subject | PASS |
| lane pushed, no uncommitted round work | `scripts/hyaku/jj-lane.sh state …/revenger-shokunin`; `git status --porcelain` | `state branch=main local=d00f779… remote=d00f779… ahead=0 behind=0 head=detached tracked=0 untracked=0`; porcelain empty | PASS |
| report cites the lane tip | report line 3 | `d00f77942d78cb9a3b41547370d7a8a4ebea6c72` = actual `refs/heads/main` | PASS |
| dispatched prompt carries the template contract | `.ufo/prompts/revenger-round-68.md` read against `templates/round-prompt.md` §1–§5 | §1 mission/axes, §2 claims, §2b frontier, §3 L2 floor, §4 report contract, §5 commit/push/L0 present, plus the hyaku addendum §6; the five child-lane items are present: report path (`…/.ufo/reports/round-68/revenger.md`), commit-before-report ordering ("The report lands last and cites the pushed lane hash"), the `SHONEN` heading requirement, the commit-hash citation rule ("every change tied to a LOG.md entry and to the commit hash that carries it"), and the lane write scope (§3) | PASS |
| L2 route map matches `MISSION.md` | prompt §3 ("at least 8 L2 subagents in ONE batched AgentSwarm call") vs `MISSION.md` §L2 concurrency | both say ≥ 8 lanes in one batched call; no model alias pinned in the prompt (operator role map decides) | PASS |

Conformance is clean and no marker predicate fires: the report carries work performed, evidence
pointers, landed changes tied to `LOG.md` entries, a checkable commit citation, a Sources & frontier
section and trend verdicts.

**Wave shape, reconciled from committed bytes.** `plan-validated.json` → `counts={"spawn":64,…,
"total":64}`, `dispatch.calls=1`; `.ufo/waves/round-68/R68*.md` = **64** seat reports; `wave-spec.json`
= 64 items whose role tally is reviewer 25 · critic 15 · executor 12 · mutation-tester 3 · scribe 3 ·
sentinel 2 · scout 1 · simplifier 1 · connector 1 · revenger 1 = 64; `milestone` = 235 bytes
(`jq -r .milestone | wc -c` = 236 including the newline). Attack share under the lane's own predicate
(`build-wave-spec.py:338-340`: reviewer, critic, mutation-tester, sentinel, revenger) = **46/64 =
71.9 %**, matching the report; under the prompt §2 v2 floor's stricter role list (reviewer, critic,
mutation-tester, labrat) it is 43/64 = 67.2 % — both far above the 25 % floor (defect D3 below is
about the predicate being unstated, not about the number).

## 2 · Claim re-derivation

Per the closure brief, a lane-owned gate/selftest is **evidence-verified, never executed**. Instrument
integrity: `sha256sum reports/round-68/measure.py` →
`0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`, identical to the pre-registration
pin in `reports/round-68/claims.md` (and to `SKILL.md`'s `measured-against` cell).

### C1 — calibration (C8: the registered gate attributes its own kill): **improved** (evidence-verified + byte re-derived)

Committed receipts, as printed (no re-run):

| label | `measure-before.log` (base `f165908`) | `measure-after.log` (final tree) |
|---|---|---|
| `C7_GATE_PRESENT` | `yes` (l.68) | `yes` (l.68) |
| `C7_SELFTEST` | `pass` (l.69) | `pass` (l.69) |
| `C7_CONTROL_PASS` | `1/1` (l.75) | `1/1` (l.75) |
| `C7_MUTANT_KILLED` | `1/1` (l.76) | `1/1` (l.76) |
| `C7_MUTANT_KILLED_ATTRIBUTED` | **`0/1`** (l.77) | **`1/1`** (l.77) |
| `C7_NEG_SPOOF_KILLED` / `…_ATTRIBUTED` | `1/1` / `0/1` (l.79-80) | `1/1` / `0/1` (l.79-80) |
| `C7_RED_ON_R65_CANDIDATE` | `yes` (l.72) | `yes` (l.72) |
| `C7_V3_CLEAN` | `n/a (no v3 file)` (l.74) | `yes (17 blocks, 0 problems)` (l.74) |
| `HOLDS_OK_V5` / `HOLDS_OK_V6` | **`no` / `no`** (l.97-98) | **`yes` / `yes`** (l.97-98) |
| counter exit | `0` (l.105) | `0` (l.99 `EXIT=0`) |

The endpoint behaviour was re-derived from the committed gate bytes by this reviewer:

- **Base** `f165908:corpus/check_embedded_outputs.py:141` is `require(not ok(dproblems), MARKER)` with
  `ok(problems) = not problems` (`:145`) — when the drifted entry is correctly caught, `dproblems` is
  non-empty, so the argument is `not (not dproblems)` = true and `require` passes. The forged control
  can never fire and the marker can never be the killing line: the `0/1` attribution is structural.
- **Tip** `d00f779:corpus/check_embedded_outputs.py:135-146` computes `caught = (dproblems is not None
  and dchecked == 1 and dproblems and dproblems[0].startswith("drift entry:"))` and, when not caught,
  runs `print("self-test: drifted entry not caught")` then `print(MARKER)` then `sys.exit(1)` — the
  marker is the **last** line of the exit-1 path and is reachable only through the drift branch.
- The counter's attribution rule is textual: `measure.py:428` and `:492`
  (`c7_mut_attributed += rc != 0 and last.endswith(C7_MARKER)`), which is exactly the instrument gap
  the report discloses rather than hides.

**Verdict: improved.** The frozen predicate is met on the final measured tree and the improvement is
visible in the bytes, not only in a label. The caveat the report carries is real and independently
supported by the wave's own critic seats (`lines[:1]` weakening survives; a non-detecting gate can
print the marker) — routed, not repaired after the wave, which is the correct posture because the
reviewed artifact stays the measured artifact.

### C2 — coverage (K, lowest non-retired criterion): **FALSIFIED** (re-measured by this reviewer over committed bytes)

The falsification does not depend on the counter. Re-derived from `git archive d00f779 … corpus`:

1. **The credit is false.** `python3 -B corpus/derive_axml_anchors.py` → exit 0, **17** stdout lines;
   `grep -nE ':(237|244)$'` over that stdout → **no match**; the only enum anchor near the block is
   `enum RES_XML_START_NAMESPACE_TYPE : 245` (output line 11). The entry states `lines 237-253` at
   `:57`, `:148`, `:157` and `line 244 is RES_XML_FIRST_CHUNK_TYPE` at `:148`, while item 11 claims
   "Every S038 line number this entry states is printed by a committed derivation script". So `:237`
   and `:244` are stated and never printed — Q04's F1 confirmed at the byte level.
2. **The widths are a literal.** `corpus/fixtures/apk-r65/readout.py:51-58` is
   `w8, w16, w32 = 1, 2, 4` plus a hand-written `widths = {...}` dict under a comment asserting the
   offsets are "computed here from the field widths in ResourceTypes.h's own struct definitions, not
   assumed", while item 5 presents the same numbers as summed from S038 — Q04's F2 confirmed.
3. **Coverage did not move.** `grep -cE '^\| *C[0-9]+ .*\| *held' corpus/README.md` = **8**, with
   **14** C-rows; the C05 row's knowledge column is `—` and its status is `uncovered`;
   `git diff --stat f165908 d00f779 -- corpus/README.md` is empty (byte-unchanged).
4. **The kill rule was executed.** The v3 entry carries `admission-status: rejected` at `:9` with the
   rest of its bytes kept; `reports/round-68/measure-after.log` reports `K_HELD_BACKED=8/14`,
   `C05_STATUS=uncovered`, `C05_SINGLE_V3=no`, `HOLDS_C2_V3=no` — unchanged from the before receipt.
5. **The new criterion can fail.** Q14 was added (`corpus/QUALITY.md` diff is exactly **one added
   line, zero removed**), and the falsifier it was added for holds: entry `:46` quotes
   `4d616e69666573742d` = 18 hex chars = **9** bytes while the clause calls it "the 16-byte prefix".

**Verdict: coverage `unchanged`, honest stop.** The frozen order ran to its fail branch: no target was
narrowed, no acceptance condition was repaired, `corpus/README.md` was not flipped.

### No axis harmed (re-derived)

`corpus/fixtures`, `corpus/live`, `PROVINCE.md`, `SHONEN.md`, `corpus/README.md` and the retained
round-65 candidate are **byte-identical** base→tip (`git rev-parse <commit>:<path>` pair comparison,
six of seven planned surfaces identical); `corpus/QUALITY.md` changed by a single **added** Q14 row
with no existing criterion weakened; the ten-verifier replay family under `corpus/verify_*.py` is
untouched (changed paths list: no `corpus/verify_*`). Every prior attributed hold is at target in the
after receipt (`HOLD_CALIBRATION 4/4`, `HOLD_REPLAY 10/10`, `FRESH_ROWS 18/18`, `C2`–`C5` 2/2 each,
`C6` 4/4, `F_COVERAGE 5/8`, `README_TOKEN_LEGEND_MISMATCH 0`, `STRICT_REJECT_WINDOW_SELFTEST pass`).

## 3 · Discernment spot-check (LEARNING.md §"Discernment is checked from outside")

Sampled from `corpus/lessons/round-68.md` `## Gate`. This round admitted **no knowledge entry**, so
the admit sample is the round's only admission-shaped decision (the new `SOURCES.md` row) and the
reject sample is the v3 candidate. Sources were re-opened from committed bytes, not the network.

| item | gate decision | re-opened source | agree / disagree | reason |
|---|---|---|---|---|
| S046 — AXML anchor derivation (own-work, tier A) | **admit** row (new row; `used-by` → the round-68 entry) | `python3 -B corpus/derive_axml_anchors.py` over `corpus/snapshots/ResourceTypes.h` from `git archive d00f779 corpus`; `sha256sum` of both files | **agree** | digests in the row match disk exactly (`bce497d6…1f249`, `56b88bc4…57c56f`, 86255 B); stdout is **17** lines as the row states; the ≤25-word located quote `enum RES_XML_START_NAMESPACE_TYPE : 245` is verbatim at output line 11; with `used-by` set, the round-start census `W03 S046 mined but unused` clears |
| S038 — AOSP `ResourceTypes.h` | **re-open** (existing row, tier A) | `corpus/snapshots/ResourceTypes.h:243-246` | **agree** | `:244` = `RES_XML_FIRST_CHUNK_TYPE = 0x0100` and `:245` = `RES_XML_START_NAMESPACE_TYPE = 0x0100`; the lesson's located quote matches `:245` byte for byte and the `:244`→`:245` repair it claims is real |
| `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (v3 candidate) | **reject** (`admission-status: rejected`) | entry `:11` + script stdout + `readout.py:51-58` + entry `:46` (all committed) | **agree** | item 11's universal credit is false for `:237`/`:244`; item 5's widths are a Python literal presented as derived; entry `:46` quotes 9 bytes against a stated 16 (Q14); the entry's own `source:`/`verified-at:`/`recheck:` header and the passing criteria (Q02, Q03, Q09, Q10) are accurate, so the reject is criterion-scoped, not blanket |
| "no knowledge entry admitted this round" | gate summary | `git ls-tree -r d00f779 corpus/knowledge/` | **agree** | only `round-65-…`, `round-67-…`, `round-68-…` (the last marked rejected); no expansion credit was taken, consistent with `K_HELD_BACKED=8/14` at both ends |

Caveat, stated for the operator: the lane's own "outside-discernment" seat (`R68SpotcheckDiscern`)
is lane-dispatched, so under `LEARNING.md` it is still the lane. The outside check that sustains the
discernment trend is **this file's** sample, which agrees on all four decisions.

**Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin revenger` → **exit 0**, 46 rows (`grep -cE '^\| S[0-9]{3} '` = 46; base
`f165908` = 45), the same four disclosed `W04` duplicate-scope warnings (S024, S028, S029, S034) and
no `W03`. This matches both census outputs pasted in the report and in the lesson.

## 4 · Trend verdicts (this reviewer's, with evidence)

| trend | verdict | evidence |
|---|---|---|
| expansion | **unchanged** | no admitted knowledge entry: `K_HELD_BACKED=8/14` at both ends, C05 `uncovered` at both ends, `corpus/README.md` byte-identical base→tip; `SOURCES.md` grew 45 → 46 by one honestly-mined own-work row whose only consumer is a rejected candidate, which earns no expansion credit (`CORPUS.md` §Rules 4) |
| quality | **improved** | the registered gate's forged control went from structurally dead to reachable and last-line (`:141` → `:135-146`), re-derived from bytes; the `SKILL.md` gate-registry row was rewritten from the after-run (self-test cell names the reachable marker, both controls and the single-line-fixture limitation; `measured-against` re-pointed to the r68 counter) and §6.1 now names `C7_*`/`HOLDS_OK_V5`/`V6` with the V6↔C05 coupling; the S046 `used-by` repair clears the census `W03`; the bar gained Q14, shown able to fail on entry `:46` and to pass the admitted r63 entry. Every prior attributed hold is at target. Caveat: the after receipt carries one false identity sentence (defect D1) — a receipt, not a corpus entry, so it does not flip the trend, but it is routed |
| discernment | **improved** | six wave Q decisions falsified C2 on the landed bytes **before** any flip and the frozen kill rule was executed rather than the target repaired; the round mined M46/M47 with fixes that can fail (Q14's falsifier transcript); the outside sample above agrees on the admit and the reject. Caveat: D1 is an uncaught instance of the very class the round mined (an identity asserted against contradicting bytes), and no criterion covers it — routed to the next round |

## 5 · Routed defects the lane must fix next round (status-neutral)

1. **R68-D1 (calibration/evidence, medium).** `reports/round-68/measure-after.log:102` states the
   `1c34603` `corpus/` tree is "byte-identical to the earlier measured 14774a2c tree —
   51894d153a6e69487da2a273680d014abd240f61 — and to the receipt commit's, verified with `git
   rev-parse <commit>:corpus`". Observed: `14774a2c:corpus` = `51894d15…` (the id it prints),
   `1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`, `dddf147:corpus` = `51894d15…`, and
   `git diff --name-only 14774a2c 1c34603 -- corpus/` = `corpus/lessons/round-68.md`. The stdout
   determinism claim survives (the counter does not read lesson prose), but the tree-identity
   sentence is false and the command it names contradicts it. Fix: restate as "only
   `corpus/lessons/round-68.md` differs between the two measured trees; the counter's inputs are
   unchanged", and add a criterion row that a stated git object id is re-derived with the command
   that names it. Same class as M46/M47; Q14 does not cover tree ids.
2. **R68-D2 (evidence durability, low).** The wave-slot grant quoted in the report
   (`granted lane=revenger wave=round-68-w1 seats=64 live=66 pending=0 cap=256`) is not committed;
   `~/.local/state/shokunin-hyaku/wave-slots:68` is now empty (slot released) and the only committed
   trace is `R68WaveContractAudit.md:93`'s restatement. Fix: commit the raw `acquire` output with the
   wave evidence, or present it at restatement strength.
3. **R68-D3 (wave-shape precision, low).** "attack 46/64 = 71.9 %" uses `build-wave-spec.py:338-340`'s
   predicate (reviewer/critic/mutation-tester/sentinel/revenger); the round prompt's §2 v2 floor names
   reviewer/critic/mutation-tester/labrat (43/64 = 67.2 %). Both clear 25 %; the report should name the
   predicate it counted under.
4. **R68-D4 (prose consistency, low).** `SCORECARD.md`'s round-68 paragraph says SHONEN box 1 "keeps
   its `[~]`-with-outside-verifier state" while the report's §SHONEN line and the committed
   `SHONEN.md` read `[x]` with the named non-lane verifier `revenger-r64.R64ReviewSkill`. Reconcile in
   the next round's entry (append-only; do not rewrite the r68 text).
5. **Carried forward, still open (not new):** the round's own routed bundle — counter C7 gameability,
   the `HOLDS_OK_V6`/`c7_v3_clean` separability coupling, kill-rule closure over every mechanical
   conjunct, a two-line partial-drift fixture, and the C05 repair set — remains open and is already in
   the round's `planned` row. The operator L0 (`revenger | round-68`) asks whether behavioural legs may
   replace marker-presence in the frozen instrument; the round did not block on it.

## 6 · Admission

- C1 verified (frozen predicate met on the final measured tree; improved at the byte level).
- C2 falsified by its own frozen kill rule and executed as an honest stop (no target narrowed, no
  acceptance condition repaired, `README` not flipped).
- No axis harmed; protected surfaces byte-identical.
- **The round is not admitted.** Status `ok`, verdict `rejected-honest-stop`, `admitted: false`.
