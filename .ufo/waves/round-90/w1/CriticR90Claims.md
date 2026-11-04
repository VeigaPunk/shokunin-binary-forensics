# CriticR90Claims — round 90 w1 claim-design attack (revenger)

Seat: critic, leaf. Freeze `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`, base
`77574c99845ab6662812bd6a88def1e72bf8d71b`. Everything below ran on
`git archive` extractions in scratch `/fast/scratch/hyaku/revenger-r90/CriticR90Claims`
with `TMPDIR` set to that path. Scratch was deleted before yielding. Receipts
were copied to
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/CriticR90Claims/receipts/`.
I ran no lane-mutating command and installed no tools (none were needed).

Inputs read:
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-89-verifier-spotcheck.md`
- `/home/vgpnk/Projects/shokunin/AXES.md`
- every `*.log` and `*.py` in `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/rejected-android-record/receipt.json`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-81/f_probe4.py`
- v1 and v2 `sm6()` (`corpus/self_assessment_check.py:175-187`, `corpus/self_assessment_check2.py:183-198`)

Setup: `git -C <lane> archive c7767789… | tar -x -C $S/freeze` (the same for base into `$S/base`).
The control builder is `receipts/mk_ctl.py`.

## Q1 — can a cheap control that skips the claimed work reach either target?

### C2: yes, two of my own controls reach `C2_CONJUNCTS=6/6` (`receipts/c2-controls.log`)

**ctl-idedit.** I started from the freeze tree and copied the r89 rejected record
(`reports/round-89/rejected-android-record/inspection.json`) to
`corpus/live/runs/round-90/inspection.json` (run1) and to
`reports/round-90/android-run2.json` (run2). In each copy I replaced the
whole-string `evidence_id` with a fresh random `ev_<64 hex>`. I then wrote a
receipt `{"runs":[{stdout_sha256},{stdout_sha256}]}`. No producer was run.

```
K1=pass ['F4_COVERAGE=11/11 score=10.00']
K2=pass ['ORACLE OK (22/22 checks)']
K3=pass ['ORACLE_MISCLASS=0/9']
K4=pass ['NORM_EQ=identical']
K5=pass ['88aca5fb1c632616', 'a8fb9dc48f51ff8b']
K6=pass ['ev_bf6e273dafe9c6c62', 'ev_7fbe94f5d0653740c']
C2_CONJUNCTS=6/6   EXIT=0
```

claims.md:86-89 discloses that "hand-edited distinct ids would pass K6". The
disclosure does not change the result: the frozen target is reachable with
zero producer work. Kill rule (d) lists only two controls, no-record and
verbatim copy-r89, and both are weaker than this obvious third one. Both copies
still carry r89's private runtime directory `rea-android-ugg7mp` (3
occurrences). norm_eq V2 normalises that directory away, so the counter never
sees it.

**ctl-stub.** I started from the freeze tree with no record. In the tree I
replaced `reports/round-81/f_probe4.py`, `corpus/fixtures/apk-r65/oracle_check2.py`,
`reports/round-90/oracle_battery.py` and `reports/round-90/norm_eq.py` with
one-line `print(...)` stubs. run1 and run2 are `{"evidence_id":"ev_stub0|1"}`,
with a matching receipt. Result: `C2_CONJUNCTS=6/6`, `EXIT=0`.

The cause is that `c2_counter.py:140-146` executes the instruments that live
inside the TREE under test (`t / ...`). It never checks them against
`instrument-pins.log`. claims.md:9-11 says the closure re-derives the pins
"over the freeze commit". That check covers the freeze bytes, not the
landing-tree bytes. The no-harm statement covers `f_probe4.py` but not the four
round-90 instruments. A pin check on the landing tree does catch the stub
(`receipts/pins-controls.log`):

```
-- freeze      PINS_EXIT=0
-- ctl-idedit  PINS_EXIT=0
-- ctl-stub    oracle_check2.py / norm_eq.py / oracle_battery.py / f_probe4.py: FAILED  PINS_EXIT=1
```

### C1: v1 skip controls fail, but the target is already met at the freeze (`receipts/c1-controls.log`)

| control | SM6_MISCLASS |
|---|---|
| do-nothing v1 (kill c) | 7/14 |
| `sed s#/14#/15#` on v1 (`receipts/ctl_v1_sed15.diff`) | 5/14 (B04 B05 B06 B08 B10) |
| **v2 over the freeze tree itself, nothing landed after freeze** | **0/14** |
| `ctl_lastfrac.py`: "the last `N/D` on the head must equal held/rows", no arrow or score parsing | **0/14** |

- The battery cases B01–B12 do not depend on the tree, and v2 is a frozen
  file. R1/R2 read only `corpus/README.md` and `SCORECARD.md`. So the C1
  "after" value is fixed at freeze time. The only post-freeze work C1 needs is
  kill rule (b).
- Over the freeze tree, v2 gives `SM2=1 SELF_MISMATCH=1`. The new file
  `corpus/self_assessment_check2.py` is not named in `corpus/README.md`
  (UNNAMED probe output). Adding one README line (my ctl-c1only) gives
  `SELF_MISMATCH=0`.
- C1 is therefore a pre-registered prediction about frozen bytes, not a
  post-freeze move. That is a legitimate design. But the actual do-nothing
  control is "freeze tree, v2", and it already meets the target. Kill rule (c)
  names v1 as the control, which is a strawman.
- The 4-line `ctl_lastfrac` passing 14/14 shows a power gap. The battery cannot
  tell v2's arrow and parenthesised-score parsing apart from "last fraction on
  the line". No case puts a non-current fraction after the current side.

**Q1 verdict: C2's target is reachable by cheap work-skipping controls; this is a defect. C1's target is not reachable by a v1-level skip, but it is met at the freeze, so the claim carries no post-freeze work beyond one README line.**

## Q2 — is C1 a calibration claim under AXES.md?

AXES.md:15 defines calibration as "Self-assessment quality … SHONEN.md/SCORECARD
entries match observed repo state". claims.md:51-52 states that no
SCORECARD/SHONEN entry changes ("it was already true"). The quantity that moves
is the gate's accuracy on a synthetic battery. That is meter repair. It fits
the operability signal better (AXES.md:13: "scripts that run … produce the
stated outcome"). Lane precedent exists for calibration-as-receipt-fidelity
(SCORECARD.md:1537, r88 "criterion R receipt fidelity"), but r88 also corrected
six false entries, and C1 corrects none.

C1 is also weak on the "overreach caught" reading, on the lane's real row
format (`receipts/c1-realformat-counterexample.log`). The last K line
(SCORECARD.md:693) states its value in the cell `8/15 (5.3) → 8/15 (5.3)` at
char 54. The `K_HELD_BACKED` token appears only at char 192, inside the
evidence-pointer cell `` (`K_HELD_BACKED=8/15`) ``. v2's regex starts at that
token, so it reads the pointer and never reads the stated before→after cell:

```
CX stated-after-cell-false-9/15: truth label=1; v1 sm6=1 v2 sm6=0
CX stated-after-cell-false-8/14: truth label=1; v1 sm6=1 v2 sm6=0
```

A stale `8/14` self-assessment written in the lane's own row format reads clean
under v2. That is exactly the R2 forgery class, which the battery tests only as
a bare appended `K_HELD_BACKED 8/14` line, a format the lane never writes. On
real rows this is a regression against v1 (v1 flags both, although only by
accident). R1 scores 0 only because the pointer cell happens to equal the
stated cell.

**Q2 verdict: mis-named. C1 is gate fidelity (operability, or at best a calibration sub-axis, which AXES.md:37-38 says must be split and recorded with a reason). It does not move self-assessment accuracy, and on real rows it introduces a blind spot.**

## Q3 — is C2 a coverage move or a re-labelling?

The surface is genuinely uncovered at base and at freeze: F4 is 10/11 and
`inspect_android_package` is absent from `corpus/live/runs`. A fresh producer
record would be a real coverage move.

The predicate, however, cannot tell a fresh record from the r89 record:
- The verbatim r89 copy passes K1–K5 (`reports/round-90/c2-control-copy89.log`: 5/6).
- The only discriminator is K6, a string inequality on `evidence_id`, and
  ctl-idedit defeats it.
- The volatile set V1–V4 (norm_eq.py:8-15) is a one-to-one restatement of r89's
  measured `volatile_field_set`
  (`reports/round-89/rejected-android-record/receipt.json`: evidence_id,
  `rea-android-XXXXXX`, calls[0] key order, `load_duration_ms`). r89 already
  recorded `normalized_result_identical_across_runs: true`.
- The kill that ended r89, byte-identity, has been replaced by a rule fitted to
  r89's observed diff. So K4 adds almost no evidence that r89 lacked.
- The new evidential content is oracle v2 (K2/K3), and it rejects forgeries,
  not re-use. P2, a hand-written content-accurate record, is labelled `accept`.

**Q3 verdict: a real coverage surface whose counter admits re-labelling. The predicate cannot separate "re-ran the producer" from "re-used the r89 bytes with new ids", so the coverage credit rests on receipt honesty outside the counter.**

## Q4 — is each predicate the same sentence, the same code condition and the same receipt label?

| item | claims.md sentence | counter code | receipt label | match? |
|---|---|---|---|---|
| C1 misjudge | verdict ≠ "hand-written truth label" | `got != label` (sm6_battery.py:84) | `SM6_MISCLASS=n/14` | partial. R1's label is a CLI default (`--real-label`, default 0, sm6_battery.py:66), not a per-tree hand label. It was derived independently only at base (`c1-real-label.log`). With a false last K line on R1, a correct v2 is scored MISCLASS (`c1-controls.log`: `R1 label=0 got=1`). The landing tree will append an r90 SCORECARD section, so R1's label must be re-derived at landing |
| C1 "current side states N/D" | right of `→` | v2 regex anchored at the `K_HELD_BACKED` token | — | **no** on real rows: it reads the pointer cell (Q2) |
| C1 kill (b) | SM1–SM5 equal, SELF_MISMATCH=0 | — | — | holds only after a README edit. At freeze, `SM2=1` for v1 and v2 |
| C2 K1 F4 11/11 | yes | substring `F4_COVERAGE=11/11`, but uses the TREE's `f_probe4.py` | `K1=pass` | partial (unpinned) |
| C2 K2/K3 "oracle v2" | the oracle v2 | TREE's `oracle_check2.py` / `oracle_battery.py`, unpinned | `ORACLE OK (22/22)`, `ORACLE_MISCLASS=0/9` | partial (ctl-stub) |
| C2 K4 "two committed **producer runs**" | two runs | `norm_eq` on two files; nothing tests producer identity or that two runs happened | `NORM_EQ=identical` | **no**: "producer"/"current-producer" in the title and sentence has no code condition |
| C2 K5 / kill (c) "run1's exact stdout" | exact stdout | digest equals the receipt's *claimed* digest | `K5=pass` | partial: the stdout is receipt-asserted, not observed |
| C2 K6 | distinct, ≠ r89 | `i1 != i2 and R89_ID not in` | `K6=pass` | yes; the sentence matches the code |

**Q4 verdict: not identical. Five drifts: C1's R1 label is a default rather than a hand label; C1's "current side" is not what v2 reads; C2's K1–K3 instruments are unpinned; "producer runs" has no condition in the code; and kill (c)'s "exact stdout" is asserted by the receipt.**

## Q5 — separability (`receipts/c1-controls.log`)

- C1 counter on the C2-only tree (freeze + ctl-idedit record): v2 0/14, v1 7/14.
  v2 full checker gives `SM2=1`, i.e. the same README omission.
- C2 counter on the C1-only tree (freeze + README line): `C2_CONJUNCTS=1/6`,
  `F4_COVERAGE=10/11`. v2 full checker gives `SELF_MISMATCH=0`.

**Q5 verdict: separable, as claims.md:97-102 states. The C1 half is separable trivially, because C1's number is fixed at freeze.**

## Smallest safe corrections (frozen instruments untouched; closure-side or next round)

1. **C2, closure-side.** Before reading `C2_CONJUNCTS`, run
   `sha256sum -c reports/round-90/instrument-pins.log` inside the landing tree.
   This kills ctl-stub.
2. **C2, closure-side.** Require the run1 and run2 `rea-android-<suffix>`
   (the V2 targets) to differ from each other and from r89's `ugg7mp`. This
   kills ctl-idedit as built. It is still forgeable, so also state in the
   report that 6/6 is necessary, not sufficient, and that freshness rests on
   the receipt (Q09).
3. **C2, wording.** Drop "current-producer" from the claim title, or carry it
   only as an unproven limit.
4. **C1, wording.** Re-name C1 to gate fidelity (operability, or a recorded
   calibration sub-axis), or keep the name and state its no-entry-change
   limit.
5. **C1, blind spot.** Register the real-row-format blind spot as a v2 limit in
   the SKILL gate registry. Do not claim "stops misjudging the lane's K
   statement". Next round: a v3 that reads the stated cell, with a battery case
   in the real row format.
6. **C1, kill rule (b).** Re-derive `c1-real-label.log` at the landing
   revision, and pass `--real-label` explicitly. Land the README line naming
   `self_assessment_check2.py` so that kill (b)'s `SELF_MISMATCH=0` can hold.

Impacted axes: calibration (C1 naming, C1 real-row blind spot); coverage (C2
re-use admissible, unpinned instruments).

Distinguishing fixable defects from tradeoffs the judge must rule on:
- Fixable: the unpinned instruments (1); the R1 label default and README
  naming (6).
- Tradeoff, for the judge: C2 being reachable without a producer run is
  disclosed, and Q09 means it cannot be fully fixed. C1's axis naming is a
  definition question.

VERDICT: C2 target reachable by two zero-work controls (id-edited r89 copy and in-tree instrument stubs, both 6/6), so admit only with a landing-tree pin check and runtime-suffix freshness; C1 meets its target at the freeze (0/14 before any post-freeze work), is gate-fidelity mis-named as calibration, and v2 is blind to false K cells in the lane's real SCORECARD row format (v2 sm6=0 on a stale 8/14 cell); separability holds.
