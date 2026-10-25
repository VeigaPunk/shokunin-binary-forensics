DIFFERS (2 rows) — met=11 / falsified=7 (5 of them honest-stop) / pending=0 on 18 claims; wave 1's 10/2/5/1 differs at r65 C1 (I read falsified, they read pending) and r66 C1 (I read met, they read falsified), because the round-end scorecard cell and the claim's own frozen predicate disagree on exactly those two rows.

Seat: R70W2LedgerRederive (revenger round 70, wave 2 — falsify). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Assignment: independently re-derive the claim hit-rate ledger for lane rounds 61-69 (considerthese `2026-10-24.md` proposal 3).
Fresh seat: wave-1 material was read **only after** this table and its totals were derived from `reports/round-6*/claims.md`,
`SCORECARD.md` and `corpus/lessons/round-6*.md`. No lane file was edited. No `/tmp` scratch was created (all commands were
read-only, run from the lane root). Tool installs: none.

---

## 1. Method (three independent derivations, then a cross-check)

1. **Claim inventory** — ids and axes from each pre-registration, not from the scorecard:
```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ for r in 61 62 63 64 65 66 67 68 69; do printf "%s " $r; \
    grep -cE '^## C[0-9]+ — |^\*\*C[0-9]+ — ' reports/round-$r/claims.md; done
61 2
62 1
63 3
64 2
65 2
66 2
67 2
68 2
69 2
```
sum = 18 claims. Headings (same command without `-c`): r61 C1 coverage-K / C2 calibration; r62 C1 coverage-K; r63 C1 coverage-K,
C2 coverage-F, C3 calibration; r64 C1 coverage-K, C2 calibration; r65 C1 coverage-K, C2 calibration; r66 C1 coverage (C05
disposition), C2 calibration; r67 C1 coverage-K, C2 calibration; r68 C1 calibration, C2 coverage-K; r69 C1 coverage-K,
C2 calibration. **No round 61-69 declared a freshness claim** — freshness appears only as an unchanged hold (`FRESH_ROWS=18/18`),
so the ledger has two axes, coverage (10 claims) and calibration (8 claims).

2. **Verdict cells** — the last cell of the matching `SCORECARD.md` row, line numbers confirmed by reading the line, not by
   trusting any index:
```
$ for n in 247 248 272 313 314 315 379 380 435 436 462 463 492 493 520 521 565 566; do \
    printf "%s: " $n; sed -n "${n}p" SCORECARD.md | cut -c1-150; done
```
(each line reproduced in the table's *source* column below).

3. **Mechanical label cross-check** — the verdict is re-read from the round's own `measure-after.log` labels where the
   scorecard cell is prose:
```
$ for r in 61 62 63 64 65 66 67 68 69; do echo "=== r$r ==="; \
    grep -nE 'HOLDS_C[0-9]|C05_|K_HELD|K_ROW|C[0-9]_[A-Z_]*KILLED|Q15_|HOLDS_OK|^exit' reports/round-$r/measure-after.log | head -14; done
```
Key results used: r61 final block `K_HELD=4/14`, `K_ROW C04/C09 status=uncovered` (`reports/round-61/measure-after.log:100-103`);
r62 `K_HELD_BACKED=6/14` (`:9`); r63 `K_HELD_BACKED=7/14`, `F_COVERAGE=5/8`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`;
r64 `K_HELD_BACKED=8/14`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`; r65 `K_HELD=8/14`, `K_ROW C05 status=frontier`,
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`; r66 `K_ROW C05 status=uncovered`, `C05_REJECTED_MARKED=yes`, `K_HELD_BACKED=8/14`,
`README_TOKEN_LEGEND_MISMATCH=0 rows=[]` (`:1-10`), `C6_RECEIPT_KILLED_ATTRIBUTED=4/4` (`:62`); r67 `HOLDS_OK_V5=no` (`:90`);
r68 `HOLDS_OK_V6=yes` (`:98`), `C1 (calibration, C8) — improved: C7_MUTANT_KILLED_ATTRIBUTED 0/1 -> 1/1` (`:110`);
r69 `K_ROW C05 status=uncovered`, `HOLDS_C2_V4=no` (`:17-33`).

4. **Byte check on the one row where prose and predicate diverge** (r66 C1, §3.1): the claim's frozen after-state is a set of
   landed bytes, so it can be tested directly at the r66 tip `a4c712a0`:
```
$ git show a4c712a0:corpus/README.md | grep -n 'C05'
34:| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) | uncovered |
$ git show a4c712a0:corpus/knowledge/round-65-apk-axml-byte-evidence.md | grep -n 'admission-status'
7:admission-status: rejected — the round-65 orchestrator-dispatched wave's fresh-seat decisions, adjudicated round-66 by L1 revenger-r66: Q02 FAIL, Q06 FAIL, Q11 FAIL …
```
Every conjunct of r66 C1's frozen after-state (`K_ROW C05 status=uncovered` AND `C05_REJECTED_MARKED=yes` AND
`K_HELD=K_HELD_BACKED=K_HELD_BACKED_STRICT=8/14` AND `README_TOKEN_LEGEND_MISMATCH=0`, plus "the retained candidate is marked
`admission-status: rejected`" and "no other coverage-map row changes status") holds on the landed bytes.

---

## 2. The ledger (my derivation)

| round | claim | axis | verdict | source line read (command in §1) |
|---|---|---|---|---|
| 61 | C1 | coverage K | **falsified** | `SCORECARD.md:247` "coverage — K \| 4/14 → 4/14 (2.9 → 2.9); provisional 6/14 withdrawn … \| **C1 falsified: neither candidate survives the fresh attacks**"; `reports/round-61/measure-after.log:100-103` `K_HELD=4/14`, C04/C09 `uncovered` |
| 61 | C2 | calibration | **met** | `SCORECARD.md:248` "… \| **C2 improved independently**"; `reports/round-61/measure-after.log:13,15` `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` |
| 62 | C1 | coverage K | **met** | `SCORECARD.md:272` "… \| **improved**, C1 met"; `corpus/lessons/round-62.md:318` "C1's measured minimum5/14 is met at6/14"; log `K_HELD_BACKED=6/14` |
| 63 | C1 | coverage K | **met** | `SCORECARD.md:313` "**improved, C1 met**"; log `K_HELD_BACKED=7/14` |
| 63 | C2 | coverage F | **met** | `SCORECARD.md:314` "**improved, C2 met**"; log `F_COVERAGE=5/8 score=6.2` |
| 63 | C3 | calibration | **met** | `SCORECARD.md:315` "**improved, C3 met**"; log `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` |
| 64 | C1 | coverage K | **met** | `SCORECARD.md:379` "**improved, C1 met**"; `corpus/lessons/round-64.md:256` "**C1 ADMITTED.**"; log `K_HELD_BACKED=8/14` |
| 64 | C2 | calibration | **met** | `SCORECARD.md:380` "**improved, C2 met**"; `corpus/lessons/round-64.md:273` "**C2 VERIFIED.**"; log `C4_RECEIPT_KILLED_ATTRIBUTED=2/2` |
| 65 | C1 | coverage K | **falsified** (superseded) | `reports/round-65/claims.md:25` "8/14 falsifies" + log `K_HELD=8/14`, `K_ROW C05 status=frontier`; adjudicated `corpus/lessons/round-66.md:40` "**Decision: C1 of round 65 is FALSIFIED.**" and `SCORECARD.md:462` "**falsified C05 candidate, order executed**" |
| 65 | C2 | calibration | **met** | `SCORECARD.md:435` "**improved, C2 met**"; log `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` |
| 66 | C1 | coverage (C05 disposition) | **met** | `corpus/lessons/round-66.md:44` "C1 (coverage disposition): LANDED per the frozen order's falsification branch"; log `:1-10` (C05 `uncovered`, rejected marked, K 8/14, legend 0); bytes at `a4c712a0` (§1.4) |
| 66 | C2 | calibration | **met** | `SCORECARD.md:463` "**improved, C2 met**"; log `C6_RECEIPT_KILLED_ATTRIBUTED=4/4` |
| 67 | C1 | coverage K | **honest-stop** | `SCORECARD.md:492` "**C1 falsified — honest stop**"; `corpus/lessons/round-67.md:8` "Both claims FALSIFIED — honest stop" |
| 67 | C2 | calibration | **honest-stop** | `SCORECARD.md:493` "**C2 falsified — honest stop**"; log `HOLDS_OK_V5=no` |
| 68 | C1 | calibration | **met** (instrument caveat) | `SCORECARD.md:520` "**improved, C1 met** — with the named instrument caveat"; log `:110` `C7_MUTANT_KILLED_ATTRIBUTED 0/1 -> 1/1`, `HOLDS_OK_V6=yes` |
| 68 | C2 | coverage K | **honest-stop** | `SCORECARD.md:521` "**C2 FALSIFIED — honest stop**" |
| 69 | C1 | coverage K | **honest-stop** | `SCORECARD.md:565` "**C1 FALSIFIED — honest stop**"; log `C05_STATUS=uncovered`, `HOLDS_C2_V4=no` |
| 69 | C2 | calibration | **honest-stop** | `SCORECARD.md:566` "**C2 FALSIFIED — honest stop, instrument defect**"; log `:12` (uncaught `NameError` before every `C7_*`/`Q15_*`/`HOLDS_OK*` label) |

### Totals

```
met                = 11   (r61 C2, r62 C1, r63 C1/C2/C3, r64 C1/C2, r65 C2, r66 C1/C2, r68 C1)
falsified          =  7   (r61 C1, r65 C1, r67 C1/C2, r68 C2, r69 C1/C2)
  of which honest-stop = 5 (r67 C1/C2, r68 C2, r69 C1/C2)
pending            =  0
total              = 18   (11 + 7 = 18)
```

By axis: **coverage 5 met / 5 falsified of 10** (met r62C1, r63C1, r63C2, r64C1, r66C1);
**calibration 6 met / 2 falsified of 8** (met r61C2, r63C3, r64C2, r65C2, r66C2, r68C1).
Rounds 67-69 alone: 6 claims, 1 met (r68 C1) — reproduces the sentence at `reports/round-70/claims.md`
("the lane's hit rate on the six pre-registered claims of rounds 67-69 is 1 met (r68 C1) of 6").

---

## 3. Where I differ from `.ufo/waves/round-70/w1/R70W1ErratumDraft.md` §3, and why

Wave 1's totals: `met=10 falsified=2 honest-stop=5 pending=1` (same 18 claims, same inventory). Two rows differ; the
round-end scorecard cell and the claim's own frozen predicate disagree on exactly those two, and I resolved both on the
predicate.

### 3.1 r66 C1 — they say falsified, I say **met**

- Their cell (`R70W1ErratumDraft.md` §3.1, row 66 C1) reads `SCORECARD.md:462` = "**falsified C05 candidate, order
  executed — verdict recorded**", and their §3.2 note calls it "an **either-way** claim (execute the frozen order) whose
  executed outcome was candidate falsification — the claim was executed as specified while the axis did not move".
- The claim's frozen predicate is not "the axis moves". `reports/round-66/claims.md:64-72` freezes an after-state —
  `K_ROW C05 status=uncovered` AND `C05_REJECTED_MARKED=yes` AND `K_HELD=K_HELD_BACKED=K_HELD_BACKED_STRICT=8/14` AND
  `README_TOKEN_LEGEND_MISMATCH=0` — and states explicitly that "`K_HELD` is unchanged by construction (the claim is the
  honest adjudicated-negative move on the named coverage-map surface, not held ground)". A claim that pre-registers a
  no-move predicate and then lands that predicate is met, not falsified; "executed as specified" **is** this claim's
  success condition.
- Verified on the bytes, not the prose: `reports/round-66/measure-after.log:1-10` prints all four labels; `git show
  a4c712a0:corpus/README.md | grep -n C05` → `:34` `… | uncovered`; `git show
  a4c712a0:corpus/knowledge/round-65-apk-axml-byte-evidence.md | grep -n admission-status` → `:7 admission-status: rejected …`.
  The lesson's own Gate agrees: `corpus/lessons/round-66.md:44` "C1 (coverage disposition): **LANDED**".
- Consequence: their `falsified` bucket contains a claim that came true, and their `met` count is one low.

### 3.2 r65 C1 — they say pending, I say **falsified** (superseded by the round-66 adjudication)

- Their cell reads `SCORECARD.md:436` "**pending — candidate landed, flip deferred to dispatched wave**" and
  `corpus/lessons/round-65.md:22` "CANDIDATE LANDED, admission pending". At r65's tip that is accurate.
- But r65 C1's own kill text is `reports/round-65/claims.md:25` "… `K_HELD_BACKED_STRICT` equal at both ends); **8/14
  falsifies**", and the r65 tip reads `K_HELD=8/14`, `K_ROW C05 status=frontier`
  (`reports/round-65/measure-after.log:1-5`). The next round then decided it: `corpus/lessons/round-66.md:40`
  "**Decision: C1 of round 65 is FALSIFIED.**" and `SCORECARD.md:462` "falsified C05 candidate".
- A hit-rate ledger asks whether the claim came true, and it never did; "pending" is a round-end state, not a verdict.
- Note this is the *same* event as §3.1: one candidate rejection is being counted in r66 (wrongly, as that round's claim
  failure) and excused in r65 (wrongly, as pending). Moving both rows fixes both errors and leaves the total at 18.

### 3.3 What does **not** differ

- Inventory (18 claims, ids, axes) — identical; my §1.1 count reproduces theirs.
- The five honest-stop rows (r67 C1/C2, r68 C2, r69 C1/C2) — identical.
- r68 C1 `met` with the instrument caveat — identical; I keep the caveat (predicate satisfiable by a non-detecting gate,
  `SCORECARD.md:520`).
- The remaining 9 `met` rows (r61 C2, r62 C1, r63 C1/C2/C3, r64 C1/C2, r65 C2, r66 C2) — identical, and every one is
  re-read from its own after-log label in §1.3.

### 3.4 The two ledgers side by side (the only cells that move)

| round | claim | w1 verdict | my verdict | discriminating command |
|---|---|---|---|---|
| 65 | C1 | pending | falsified | `grep -n '8/14 falsifies' reports/round-65/claims.md` → `:25`; `grep -n 'Decision: C1 of round 65 is FALSIFIED' corpus/lessons/round-66.md` → `:40` |
| 66 | C1 | falsified | met | `grep -n 'C1 (coverage disposition): LANDED' corpus/lessons/round-66.md` → `:44`; `sed -n '1,10p' reports/round-66/measure-after.log` (all four frozen labels) |

Totals under each reading, for the lesson's use:

```
reading A (round-end cell, = w1)      met=10 falsified=2 honest-stop=5 pending=1   (18)
reading B (claim predicate, = mine)   met=11 falsified=7 (5 honest-stop) pending=0 (18)
```

Reading A's `falsified=2` bucket (r61 C1, r66 C1) mixes two different kinds — r61 C1 is a genuine fresh-wave rejection of
both candidates (`SCORECARD.md:247`), r66 C1 is a disposition that succeeded — so it should not be pasted into the lesson as
a single class. If the lesson wants a three-way split with no `pending` bucket, reading B is the one that keeps every row
classified by the claim's own frozen predicate.

---

## 4. Residual / limits of this derivation

- The ledger's verdicts for r61 C1 and r65 C1 rest on the *final* adjudication, not on the provisional rows that the
  scorecard itself supersedes (`SCORECARD.md:236` "supersedes provisional K row"; `reports/round-61/measure-after.log:2-5`
  still shows the withdrawn `K_HELD=6/14` provisional block above the final `:100-103` block). A reader who reads the first
  block of that log gets the wrong verdict — the log's own order is the trap, not the scorecard.
- r61 C1 is an honest stop in substance (both candidates retained rejected, no acceptance condition weakened,
  `SCORECARD.md:243-247`) but the scorecard does not use the "honest stop" label for it; I count it under `falsified` and
  flag it rather than silently inflating `honest-stop` to 6.
- I did not re-run any round's frozen counter (that is wave-1's and the C2/C3 seats' job); verdicts here are label reads plus
  the r66 byte check in §1.4. The only row I re-derived from bytes rather than prose is r66 C1.
- Nothing in this report is an input to the C1 kill rule: the ledger is C2's unscored companion
  (`reports/round-70/claims.md` "Unscored companion"), and no Q01-Q15 decision on the landed candidate bytes is recorded here.
