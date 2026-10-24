---
round: 65
date: 2026-10-24
author: revenger-r65
claims: [C1, C2]
lane: revenger-shokunin
claim_base: 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f
contract: reports/round-65/claims.md
counter: reports/round-65/measure.py
status: pre-registered by L1 revenger-r65 before any after-measurement
---

# Round 65 — transplant-bound receipts and a first Android-APK byte readout

Two claims on distinct frozen criteria, same shape as rounds 62–64 (one
coverage-K admission, one calibration guard), plus one registered (not scored)
counter repair that pays routed debt from the round-64 closure.

**C1 — coverage K (lowest non-retired axis, 8/14 = 5.7):** exactly one
independently gated admitted entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md`
covering README row **C05 (Android packages)**, authored over an authored
known-truth fixture `corpus/fixtures/apk-r65/` (binary-AXML `AndroidManifest.xml`
+ declared-header `classes.dex` + `META-INF/MANIFEST.MF`, zip container).
Frozen target: `K_HELD` **8/14 → 9/14** (`K_HELD_BACKED` and
`K_HELD_BACKED_STRICT` equal at both ends); 8/14 falsifies. README C05 flips
**either way** at round end: `frontier → held` naming only the new entry on
all-criteria (Q01–Q13) admission; `frontier → uncovered` if C1 falsifies.
No other README row changes. Entry scope is manual byte-derived readout of the
authored APK only — no install, signing, dex-validity, provider-completeness or
authenticity claim (Q10 fence inside the entry).

**C2 — calibration, new criterion C5 (evidence-id transplant guard):**
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` **0/2 → 2/2** by exactly one in-script
control per script in `corpus/verify_icon_languages.py` and
`corpus/verify_multi_icon_states.py`: immediately after the existing
forged-stdout control in `check()`, deep-copy the receipt, transplant a **real
foreign** evidence ID (languages: `ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d`,
the multi script's round-42 ID; multi: `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421`,
the languages script's round-47 ID — both real IDs recorded in this lane's
`corpus/live/runs/`), require `not receipt_ok(...)` with message ending
`forged receipt evidence accepted`. Frozen fix shape: keep every existing
saved-input assertion and the existing forged-command and forged-stdout
controls; insertions only, `receipt_ok` untouched. Frozen mutation (the round's
own kill rule): delete exactly the conjunct `receipt['evidence_id']==evidence_id`
(and its connecting `and`) from `receipt_ok` — regex
`receipt\['evidence_id'\]\s*==\s*evidence_id`, exactly one match per script —
run `--self-test` on a fresh tree copy; a kill is **attributed** iff the mutant
run exits non-zero and its last output line ends with `forged receipt evidence
accepted`. Red-before: both mutants exit 0 at base (control receipt below).
This seeds routed prong (c) of the round-63/64 Evidence-ID transplant check
(`corpus/lessons/round-64.md` routed row 4); prongs (a),(b) and the
injectivity registry remain future-round debt (owner named in the lesson).

**Registered counter repair (diagnostic, not scored, declared before any
after-measurement):** the round-64 probe's `rejected_marked` scanned only the
first 2000 bytes of an entry for the `admission-status: rejected` marker
(routed by R64ReviewSeparability). The round-65 probe scans the whole file and
adds `STRICT_REJECT_WINDOW_SELFTEST` — it seeds a synthetic candidate whose
rejected marker starts at byte 3000 and asserts (i) the fixed scan detects it
and (ii) the old `[:2000]` window misses it. The fix must not change current
counts: both retained rejected candidates carry their marker before byte 2000
(commonjs 859, evm 712 — verified at base), so `K_HELD_BACKED_STRICT` is
identical under both windows at base. Frozen label `HOLDS_OK_V2` keeps its
round-64 formula unchanged; a new additive line `HOLDS_OK_V3` = V2 formula ∧
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED==2` ∧ `STRICT_REJECT_WINDOW_SELFTEST=pass`.

## Frozen counter and red-before

Counter: `reports/round-65/measure.py` (extends the round-64 probe; all
round-64 labels and formulas unchanged; new labels: `K_ROW C05`,
`STRICT_REJECT_WINDOW_SELFTEST`, `C5_CONTROLS_PASS`, `C5_RECEIPT_KILLED`,
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED`, `HOLDS_OK_V3`).
Do-nothing control: `reports/round-65/measure-before.log`, measured over
`git archive 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f corpus` with the
round-65 probe — a tree containing none of the claimed work, so it can meet no
target. Kill rule and predicate are frozen in this file; a rule changed after
any seat has scored is not the claim's rule.

Expected red-before lines (C1): `K_HELD=8/14`, `K_ROW C05 status=frontier`,
`K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`,
`README_TOKEN_LEGEND_MISMATCH=0`. Expected red-before lines (C2): `C5_CONTROL_PRESENT=0/2` (the control
string exists nowhere at base), `C5_CONTROLS_PASS=2/2` (the unmutated scripts
pass their pre-existing self-tests), `C5_RECEIPT_KILLED=0/2`,
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2` — the C5 mutant deletes the
conjunct, no control catches it, self-test exits 0. After:
`C5_CONTROL_PRESENT=2/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=2/2`,
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`. `C5_CONTROL_PRESENT` is the
anti-spoof guard: it greps the landed script bytes for the control's
attribution string, so a tree printing kills without landing the control
cannot satisfy the after-state.

Expected red-before (diagnostic): `STRICT_REJECT_WINDOW_SELFTEST=pass` even at
base (the self-test is internal to the probe and tree-independent) — its
red demonstration is the seeded old-window miss recorded inside the same line's
evidence trail (the log records `old_window_miss=True`).

## Claim sizing and controls (fleet lesson conformance)

- After-states re-derive from committed bytes with one command:
  `git archive <commit> corpus | tar -x -C <tree> && python3 -B reports/round-65/measure.py <tree>`.
- Do-nothing control: the before-log above (a tree with no claimed work scores
  no target).
- C1 target names its surface (README C05 ground) and the command that shows it
  unmoved (`K_ROW C05 status`). C2 is a calibration guard on the receipt
  identity conjunct family (C2/C3/C4 chain continuation), not a re-score.
- One round, two claims, distinct axes (coverage / calibration), causally
  separable: C1 touches corpus knowledge/registry/README only; C2 touches two
  verifier scripts only; the probe lines are independent.

## Admission order (frozen)

1. Wave lands candidates in the working tree **without** the README flip:
   fixture `corpus/fixtures/apk-r65/`, entry, source rows S038+ (+S039 if the
   zipfile-docs opener lands it), the two verifier controls, lesson draft.
2. Fresh in-wave attacks: named fresh-seat Q01–Q13 pass decisions on the entry
   from reviewers other than its author; frozen C5 mutant attribution;
   counter-spoof probes; patch-shape reviews.
3. L1 adjudicates. Only on an all-criteria pass does L1 flip C05
   `frontier → held` naming only the new entry (same revision as the SCORECARD
   row). On falsification: `frontier → uncovered`. Either flip lands; K moves
   only on admission.
4. Measure on a committed archive at the final tip; `HOLDS_OK_V3=yes` and
   probe exit 0 required at round end.

## Frontier step conformance

- Census before: exit 0 (37 rows ending S037; four disclosed W04s
  S024/S028/S029/S034). Census after must exit 0 with rows 37 → 38+.
- At least one sourced claim: C1 rests on S038 (AOSP `ResourceTypes.h`, pinned
  ref — byte-level AXML structure scope) and S039 (REA android-analysis guide,
  pinned tag `rea-agents-6.5.0` — route-scope sentences only), both opened this
  round; candidate S040 = CPython zipfile docs (resolves the round-63 lead).
- Mistake M37 (STRICT scan window) pre-registered in the lesson; wave-found
  mistakes append with the same shape.

## Routed inputs from the round-64 closure — disposition

1. SHONEN box 1 `[x]` verifier lane-dispatched → this round reports the box as
   `[~]` (named verifier is a lane seat; only a fresh non-lane reviewer may
   write `[x]`). No lane-side flip.
2. AST-bound mutation counter → carried forward as future-counter debt (owner:
   a round that registers it; the STRICT window fix this round narrows but does
   not close the text-scan spoof surface).
3. Recheck-pin scope holes H1–H3 → carried forward, named in the lesson.
4. r58/59 139→142 PASS-count quotes → not triggered (this round does not touch
   `verify_named_multi_icon_states.py` / `verify_icon_states.py`); owner rule
   restated in the lesson.
5. Freshness wording → `FRESH_ROWS` remains the frozen byte-survival hold.
