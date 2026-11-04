# round-90 claims (frozen before any candidate score)

Lane `revenger`, round 90 attempt 1, lane repo
`/home/vgpnk/Projects/shokunin/revenger-shokunin`. Base
`77574c99845ab6662812bd6a88def1e72bf8d71b` (r89 adjudication + r89 non-author
spot-check). This file, the four instruments, the two frozen batteries (with
their hand-written labels and case bytes), and the red receipts are committed
as the freeze BEFORE the v2 instruments are scored on a battery and BEFORE any
round-90 producer run. Instrument digests: `reports/round-90/instrument-pins.log`
(derived by `sha256sum` at freeze; the closure re-derives them over the freeze
commit).

Two claims, distinct axes (calibration, coverage), causally separable, neither
exploratory. Both take routed items from the r89 SCORECARD section
("Routed forward" (2) and (3)).

## Lowest-axis obligation

Coverage is the lowest non-retired axis (K 8/15 = 5.3; F4 10/11 = 9.09). K
stays operator-blocked: the r74 L0 question is unanswered (re-read this round
in `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`). C2 takes the lowest
**reachable** coverage criterion, F4, as r83–r89 did.

## C1 — calibration: the self-assessment gate's SM6 class stops misjudging the lane's K statement (SM6_MISCLASS 7/14 → 0/14)

Surface: `corpus/self_assessment_check.py` (v1, r70) SM6 hard-codes a `/14`
denominator while the coverage map has 15 rows since r72. At base the lane's
own K statement is TRUE (`K_HELD_BACKED=8/15`; README 15 map rows, 8 held —
`reports/round-90/c1-real-label.log`) yet v1 reports `SM6=1`
(`reports/round-90/c1-red-v1-selfmismatch.log`), and v1 passes a stale
`8/14`. The gate that counts mismatches between self-assessment and repo state
is itself mismatched with the repo. v2 (`corpus/self_assessment_check2.py`)
changes SM6 only.

- Predicate, one sentence: SM6 misjudges a case iff its SM6 verdict differs
  from the case's hand-written truth label (0 iff the current side states
  N = held rows AND D = map rows); `SM6_MISCLASS` counts such cases over the
  frozen 14-case battery (B01–B12 synthetic, R1 the real tree, R2 the real
  tree with a forged `K_HELD_BACKED 8/14` line).
- Counter: `python3 -B reports/round-90/sm6_battery.py --impl <checker> --real TREE`
  with TREE = `git archive <rev> corpus SHONEN.md SCORECARD.md SKILL.md`.
- Red (v1, base): `SM6_MISCLASS=7/14` (`reports/round-90/c1-red-v1-battery.log`).
- Target: `SM6_MISCLASS=0/14` with `--impl corpus/self_assessment_check2.py`
  over the landing tree.
- Kill rules: (a) v2 `--self-test` must print `SELFTEST OK` (exit 0); (b) v2
  over the landing tree must print SM1–SM5 equal to v1's SM1–SM5 over the same
  tree (only SM6 may change) and `SELF_MISMATCH=0`; (c) the do-nothing control
  — v1 unchanged over the landing tree — must stay above 0 (it does by
  construction: B01/B02/B07/B10/B11/R1/R2 are v1 misjudgements); (d) R2, the
  forgery that makes v1 read clean, must be flagged by v2.
- Not claimed: that SCORECARD's K statement changed (it did not; it was
  already true). The surface moved is the gate's verdict fidelity.

## C2 — coverage: the android family's first admitted current-producer record (F4 10/11 → 11/11 under six conjuncts)

Surface: F4 family `android` (`inspect_android_package`) moves from
unrecorded to recorded in `corpus/live/runs/`. r89 was killed on two counts
this round answers with new frozen predicates declared before data: the v1
oracle accepted manifest forgeries (substring legs), and the byte-identity
rule could not hold for a producer that mints per-run ids and temp paths.

- Instruments: `corpus/fixtures/apk-r65/oracle_check2.py` (v2: parses the
  manifest XML; checks the ROOT `<manifest>`'s `package`, `versionCode`,
  `versionName` and `package_name` agreement); `reports/round-90/norm_eq.py`
  (frozen volatile set V1–V4 declared in its docstring from the r89 measured
  receipt — nothing else is normalised); `reports/round-90/oracle_battery.py`
  (9 frozen cases, labels fixed in the file; case bytes in
  `reports/round-90/oracle-battery-cases/`); `reports/round-90/c2_counter.py`.
- Predicate, one sentence: the landing tree satisfies all six conjuncts K1–K6
  of `c2_counter.py` (F4 11/11; oracle v2 accepts the landed record; oracle v2
  misjudges 0/9 battery cases; the two committed producer runs are equal
  after V1–V4 normalisation; the receipt's stdout digests equal both run
  files; the runs carry distinct evidence ids, neither the r89 one).
- Counter: `python3 -B reports/round-90/c2_counter.py --tree TREE`, TREE =
  `git archive <rev> corpus reports` (or the lane root at that revision).
- Red: F4 at base `F4_COVERAGE=10/11` (`reports/round-90/c2-red-f4.log`);
  the v1 oracle misjudges 5/9 battery cases
  (`reports/round-90/c2-red-v1-battery.log`: F1, F4, F5, F6, F7 accepted).
- Target: `C2_CONJUNCTS=6/6` over the landing tree.
- Kill rules: (a) any battery `reject` case accepted by v2 → killed; (b) the
  two producer runs differ outside V1–V4 → killed (no post-data widening of
  the volatile set); (c) the landed record is not run1's exact stdout → killed;
  (d) controls run after this freeze and before the producer run must fail
  the predicate: the no-record tree (K1/K2 fail) and the copy-r89 control
  (the r89 record copied as both runs with a matching receipt: K6 fails).
- Not claimed: provenance or authenticity. A hand-written content-accurate
  record passes the oracle by design (battery P2, labelled `accept`), and
  hand-edited distinct ids would pass K6; Q09 non-provenance boundary, stated
  as a limit, not a capability.
- Sourced: the v2 manifest legs rest on the Android `<manifest>` element
  reference (root element; `package`, `android:versionCode`,
  `android:versionName` attributes) and on the Python `xml.etree.ElementTree`
  parser's comment handling — both opened this round and registered as new
  `SOURCES.md` rows before landing (row ids assigned at landing; the round
  lesson's `## Gate` carries URL, access date and located quote).

## Separability

C1 reads only README/SCORECARD (and SM1–SM5 inputs); it never opens
`corpus/live/runs` or the apk fixture. C2 reads only `corpus/live/runs`, the
apk fixture and `reports/round-90/*`; it never opens SCORECARD or the SM
checker. A C1-only tree keeps F4 10/11; a C2-only tree keeps v1 SM6 7/14.

## No-harm statement (pre-declared)

v1 `corpus/self_assessment_check.py`, v1 `oracle_check.py`,
`reports/round-81/f_probe4.py` and every other registered instrument stay
byte-unchanged. `PROVINCE.md`, `corpus/QUALITY.md` table rows already present,
`corpus/knowledge/**` filed bytes and `corpus/live/runs` before round-90 stay
byte-unchanged; additions are appends. Census `sources-census.sh validate`
must exit 0 at round end.
