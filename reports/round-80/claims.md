# Round 80 claims — frozen before any after-run

Date 2026-11-01. Base `4eb2856a88514ae12e67337c1bb962197b4bd189` (r79 tip + non-author
spot-check, pushed). Two claims, distinct axes (coverage, calibration), causally
separable, neither exploratory; C2 is a capability acquisition. Instruments sha-pinned
below; red-befores committed in the same freeze. Kill rules are execute-as-frozen: a
falsified claim keeps its evidence bytes and takes no repair-and-revote in this round.

## §7 fresh-start duty (r71/r72/r73 rejected closures re-read and spot-checked)

Same class as r79's ruling, re-checked with fresh probes 2026-11-01: all three rejected
closures are wave-blocked K-admission claims (C05/C15/C10) — the wave Q-review surface
still does not exist on this host and the r74 L0 (fleet `.ufo/l0-questions.md:233`)
still stands unanswered (re-read this round; no operator reply after line 233). A
do-nothing control reaches the identical state on all three, so none is declared.
Also re-ruled out this round (fresh probes, 2026-11-01):

- **F android (the ninth F2 family — the honest exception)** — `REA_JADX_MCP_JAR`
  UNSET, no jadx on PATH, no `~/tools/jadx*`; S448 receipt stands. Hard-gated; moves
  only if the operator supplies the JAR.
- **A macho/signature F-family route** — `rea capabilities` 2026-11-01:
  `inspect_macho`/`inspect_signature` remain `available: false`,
  `availability_code: unsupported_host` (S453). Not manufacturable here.
- **K admissions** — wave surface absent, L0 unanswered (above).
- **Criterion C repair** — §9 sizing, unchanged from r78/r79 rulings; stays routed.
- **Criterion R extension / criterion N attribution pair** — the r79 planned row
  offered these as the round's calibration work; superseded THIS round by C2 (the
  carry-in duty institutionalized as a standing instrument). Both stay routed; N's
  negctl harness already selftests (r75), R's extension remains open.

## r79 carry-in dispositions (addressed first)

1. **Lesson §Census "32 W" vs its own receipt and §Gate's 31 W** — the receipt
   (`reports/round-79/census-after.log`) re-counted this round:
   `grep -cE '^shokunin-binary-forensics\s+W0'` = **31** (21 W01 + 10 W04); §Gate and
   the closure judge agree. Correction filed as an **appended erratum** in
   `corpus/lessons/round-79.md` (the closure ruling: never an in-place rewrite); the
   class is mined in `corpus/lessons/round-80.md` §Mistakes.
2. **Orphaned-evidence hygiene duty** — the sweep ran this round (twice: hand sweep in
   scratch, then C2's committed instrument over the real tree): 344 cited lane paths,
   **zero landable orphans** (no cited evidence file exists on disk uncommitted).
   Dispositions: 6 cited paths resolve under the fleet root's shared `.ufo/waves`
   (other lanes' seats — jj-w1/kaika-w1/kaika-w3/kaika/round-24; never this lane's
   commits), 8 recorded absents with named causes (r69-documented misroot ScoutAmp.md
   no longer anywhere; `round-73/votes` cited AS EMPTY (do-nothing control);
   `w1.ready` renamed at r73, the rename committed; a gitignored `.pyc` cite; a
   line-ref parser remnant whose file IS committed; a dir-style cite of the committed
   `corpus/lessons/round-64.md`; `reports/round-61/measurements.json` — a stale name
   in the r62 report whose bytes landed as `measure-before/after.log` + `measure.py`,
   all committed; `reports/round-70/controls/A-H` — range shorthand, controls A–K all
   committed). Full instrument output: the C2 receipts.

## C1 — coverage: a real producer record on a tenth F family (`sqlite`)

Falsifiable move: the frozen F2 mapping cannot see the `inspect_sqlite_database`
surface at all (the operation is in no family set; `rea capabilities` 2026-11-01 marks
the built-in `sqlite` provider `available: true` on this host); r80 registers the F3
mapping revision adding `sqlite: {inspect_sqlite_database}` and lands one real
producer record on an authored inert SQLite fixture.

- Instrument (new, frozen): `reports/round-80/f_probe3.py` sha256
  `9441640dc0ff37195337097f677a80bac529b3372f5d352750b7c52da714b418` — the nine F2
  families and predicate repr-equal to the frozen `reports/round-79/f_probe2.py`
  (sha256 `0be0d8b5ac131963f273e296c6c2822d277614d634db25b559256f4744e4cc12`,
  unchanged, re-verified at freeze), plus the one mapping entry; outputs renamed
  `F3_*`. v1 `f_probe.py` sha `e15a43af…39ed` unchanged.
- Counting commands:
  - before (base archive `4eb2856`): `PYTHONUTF8=1 python -B reports/round-76/f_probe.py
    <base>/corpus` → `F_COVERAGE=7/8 score=8.75`; `…/f_probe2.py` →
    `F2_COVERAGE=8/9 score=8.89`; `…/f_probe3.py <base>/corpus` →
    `F3_COVERAGE=8/10 score=8.00` (sqlite absent). Receipt:
    `reports/round-80/f3-before.log`.
  - after (landing archive): the three same commands → v1 7/8 unchanged, F2 8/9
    unchanged (frozen nine hold), `F3_COVERAGE=9/10 score=9.00` with `sqlite` in
    `F3_FAMILIES`. Receipt: `reports/round-80/f3-after.log`.
- Fixture discipline (Q06): `corpus/fixtures/sqlite-r80/generator.py` (sha256
  `94d016df3a76ecc302b73234df601f7886354b158514eaf6b8489a08a9722fa3` at freeze) builds
  a small SQLite 3 database (page_size 4096, UTF-8) with two ordinary tables
  (`meta(k,v)`, `samples(id,name,score)`) and their two implicit unique indexes; its
  self-check derives EVERY oracle-checked fact from the built bytes (file header magic,
  page size, page count, text-encoding code, and a page-1 sqlite_master b-tree parse
  giving each object's kind/table/root_page plus the stored CREATE sql; column names
  derive from that stored sql and each CREATE text is byte-verified present in the
  built file). `truth.json` pins those derived facts; `oracle_check.py` (sha256
  `706a776e031a2f30a5b631e8d8a2e44f57478664d3474b09ff712b74d1d10133` at freeze)
  compares the saved record against them. Regen byte-identical (`cmp` receipt at
  landing). The database is inert: authored bytes, offline schema-inventory target;
  the producer declares the source database is never opened by SQLite or modified.
  The scratch pre-probe that informed the record SHAPE is committed at this freeze as
  `reports/round-80/preprobe-sqlite-shape.log` (with the refused iterations
  disclosed).
- Record discipline: one bounded static run
  `PYTHONUTF8=1 rea inspect-sqlite-database <lane>/corpus/fixtures/sqlite-r80/fixture.db
  --schema-scope database --format json` (rea 6.8.0, built-in provider `sqlite`,
  SQLite 3.x worker), exact stdout saved as `corpus/live/runs/round-80/inspection.json`
  with `receipt.json` (command, exit, stdout sha256, fixture sha256), `LEDGER.md`
  (observation/inference/unknown split) and `stderr.txt`.
- **C1 verifies iff**: (a) the saved record carries `evidence_id` and
  `normalized_result` with `operation == "inspect_sqlite_database"`; (b)
  `oracle_check.py truth.json inspection.json fixture.db` prints `ORACLE OK` with
  every check passing; (c) the committed fixture regenerates byte-identically and its
  sha256 equals the record's `subject.digest.sha256`; (d) the after counting commands
  print the stated values. **Kill rule**: any oracle mismatch, missing record field or
  regen drift → C1 falsified; the fixture and record stay as evidence; F3 prints 8/10
  on the final tree and the SCORECARD records the falsification.
- Grounding: the producer record and the producer's declared capability surface
  (`rea capabilities` / `rea --llms`: "Inspect SQLite schema and optional ordinary-
  table rows from a local snapshot") — SOURCES rows landed with the work (S454/S455).
  §9: a do-nothing control cannot reach a new-family producer record — the fixture,
  the run and the mapping revision are all round work.

## C2 — calibration capability acquisition: a standing cited-evidence orphan sweep

Falsifiable move: the routed hygiene duty (which cited evidence files were never
committed?) has been executed BY HAND every time it fired (the r78 class: four logs
the r78 adjudication cited but the lane tree did not carry, caught by the closure
judge's mandated diff check and landed late at `46c605c`; the r80 carry-in repeats the
duty). Before r80 no standing instrument exists; the capability acquires one:
`reports/round-80/orphan_sweep.py` enumerates every lane path cited by the closed
round reports (fleet `.ufo/reports/round-*/revenger.md`) and the lane lessons,
classifies each against HEAD and the working tree, and exits 1 naming any landable
orphan (on-disk, never committed).

- Instrument (new, frozen): `reports/round-80/orphan_sweep.py` sha256
  `f21f5e3d730624d53ad4d370d1d50fe6d2cd4e94c6c557009d292bfe2d71890b`. Declared exits
  (docstring): 0 = sweep completed, zero landable orphans; 1 = orphan flagged or the
  sweep could not evaluate (fail-closed); 64 = unrecognized invocation form.
  §Gate-standard self-test (S452 clause): `--selftest` is hermetic (no git, no
  network, no live-tree write, no producer call — synthetic state only) asserting a
  clean vector, a planted orphan that MUST be flagged, an absent vector, and a mutant
  leg (a sabotaged blind classifier that the planted-orphan vector must catch —
  `SWEEP_SELFTEST_MUTANT_FLAGGED=ok`; last line `SWEEP_SELFTEST=pass`, exit 0).
- Counting commands:
  - before (base `4eb2856`): `git cat-file -e 4eb2856:reports/round-80/orphan_sweep.py`
    → exit 128 (capability absent; `reports/round-80` absent entirely). Receipt:
    `reports/round-80/orphan-before.log`.
  - after (worktree, then landing archive):
    `PYTHONUTF8=1 python -B reports/round-80/orphan_sweep.py --selftest` → four ok
    legs, `SWEEP_SELFTEST=pass`, exit 0; mutant leg re-run under the sabotaged
    classifier prints `SWEEP_SELFTEST_MUTANT_FLAGGED=ok` inside the same receipt;
    `PYTHONUTF8=1 python -B reports/round-80/orphan_sweep.py --lane <lane> --fleet
    <fleet-root>` → `CITED=344 COMMITTED=330 LANDABLE_ORPHANS=0 ABSENT=14`,
    `ORPHAN_SWEEP_LANDABLE=0`, exit 0. Receipts: `reports/round-80/selftest-after.log`,
    `reports/round-80/sweep-real-after.log`.
- **C2 verifies iff**: the selftest is green with the mutant leg killed, the real
  sweep exits 0 over the final tree with `LANDABLE_ORPHANS=0`, and the capability row
  enters the SCORECARD capabilities table this round. **Kill rule**: a vacuous
  selftest (mutant not caught), a real-tree orphan the sweep misses (verified by the
  hand sweep's dispositions), or a non-hermetic leg (any git/network/producer call in
  `--selftest`) → C2 falsified; the instrument stays as evidence, the duty returns to
  hand-sweeping, and the SCORECARD records the falsification.
- Known limitation (named, Q16): the citation tokenizer leaves multi-line-ref
  remnants (`path:57,:148,`) and dir-style cites (`corpus/lessons/round-64`) as
  recorded absents; every such token's underlying file was hand-verified committed.
  The instrument prints each disposition line; it is a hygiene net, not a parser
  oracle.
- Grounding: the r78 orphan-class receipt (SOURCES row landed with the work, S456:
  commit `46c605c` "the four evidence logs the adjudication commit cited but did not
  carry") and the PROVINCE evidence-ledger discipline. §9: a do-nothing control leaves
  the duty hand-run only; the instrument, its selftest and the mutant kill are round
  work. The class question (whether instruments take full SKILL registry rows) stays
  routed — this lands as a capability, NOT a registry row, same as r79's F2.

## Boundary (honest)

- C1's score move is numerator+denominator together (8/9→8/10 before, 9/10 after):
  the mapping revision is registered at freeze and would LOWER the score to 8.00 had
  the record not landed — the moved quantity is the new in-province family with a
  real, oracle-checked record, not the 9.00 print. The F2 honest exception stands
  unchanged: android stays hard-gated (9/10, not 10/10).
- C2 moves no criterion score; the moved quantity is the capability (hand duty →
  standing instrument), with the selftest kills attributed.
- v1/F2 criterion instruments (f_probe, f_probe2, P2/P3, receipt/gate v1+v2, r71
  counter) stay byte-identical; the no-harm diff at adjudication proves it.

## Separability (to be receipted at adjudication)

- C1-only tree: base archive + fixture/record + f_probe3 (no orphan_sweep) → F3
  9/10; the capability remains absent (`cat-file` fails).
- C2-only tree: base archive + orphan_sweep (no fixture, no record) → selftest green,
  real sweep over that tree exit 0 (its own citation set shrinks by one report
  round); f_probe3 over that tree prints 8/10.
