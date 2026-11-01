# round-81 claims (frozen before any after-run)

Base `081f032fda9502ebfbceb295d7e097dd8803bce1` (r80 tip + non-author spot-check).
This file, both sha-pinned instruments (`f_probe4.py`, `orphan_sweep2.py`), the
red-befores (`f4-before.log`, `sweep-v1-red.log`) and the preprobe receipt
(`preprobe-keyed-shape.log`) freeze BEFORE the landing (fixture + producer
record) and BEFORE any after-run. Two claims, distinct axes (coverage,
calibration), causally separable, neither exploratory.

## C1 — coverage: an eleventh F family (`artifact-graph`) moves through a real keyed-archive producer record

Registered mapping revision F4 (`reports/round-81/f_probe4.py`, sha256 pinned
below): the ten F3 families byte-equal to the frozen `reports/round-80/
f_probe3.py` (sha `9441640d…b418`), plus
`artifact-graph: {decode_interface_builder, inspect_keyed_archive, trace_dylib_resolution}`
(provider `rea-artifact-graph`, `available: true` on this host per S457 —
opened this round; the operation is in no F3 family set).

Denominator disclosure (pre-run, same shape as r79 F2 / r80 F3): adding the
family grows the denominator in the same revision as the family's first
record. With the family registered and unrecorded, F4 prints 9/11 (8.18) —
LOWER than frozen F3's 9/10 (9.00) on the same tree. Only a real
current-producer record on the new family moves F4 to 10/11 (9.09).

- BEFORE (red, committed `f4-before.log`): over the base archive `081f032`:
  v1 `F_COVERAGE=7/8 score=8.75`; `F2_COVERAGE=8/9 score=8.89`;
  `F3_COVERAGE=9/10 score=9.00`; `F4_COVERAGE=9/11 score=8.18` (artifact-graph
  absent).
- WORK: author the inert Foundation keyed-archive fixture
  (`corpus/fixtures/keyed-r81/`: generator whose self-check derives every
  oracle-checked fact from the built bytes — roots, 6 objects, 4 references,
  format, totals; 14/14 self-checks; regen byte-identical; fixture sha256
  `f0e02e64e0a3c10b82c736c7927577de24091ebee660df17156e83258937785c`;
  `truth.json`; `oracle_check.py`), run ONE bounded producer run on the
  committed bytes (`rea inspect-keyed-archive corpus/fixtures/keyed-r81/
  fixture.plist --format json`, exact stdout saved, exit 0, stderr 0 bytes,
  Evidence `ev_6eb77fb0…02af4b73`), oracle `ORACLE OK (27/27 checks)`.
  Preprobe receipt committed at the freeze (`preprobe-keyed-shape.log`,
  incl. the Q06 stale-constants catch and the oracle sort-defect catch).
- AFTER (green, `f4-after.log`, landing archive): `F4_COVERAGE=10/11
  score=9.09` with artifact-graph present; F3 9/10, F2 8/9, v1 7/8 unchanged
  (frozen holds); oracle re-run over the landing-archive bytes, 27/27.

VERIFY conditions (all four must hold): (a) F4 prints 10/11 over the landing
archive; (b) the record's `operation == inspect_keyed_archive`, provider
`rea-artifact-graph`, `evidence_id` form `ev_<64hex>`, subject sha == fixture
sha; (c) oracle `ORACLE OK (27/27 checks)` over the archive bytes; (d) frozen
instruments hold byte-identically (v1 7/8, F2 8/9, F3 9/10 over the landing
archive). KILL RULE: any condition fails → the candidate record is retained
rejected (`admission-status` note in the LEDGER), README byte-unchanged, F4
prints 9/11 — recorded honestly as falsified.

Boundary: family presence only (F stays presence-only, r63); the family's
other two operations (`decode_interface_builder`, `trace_dylib_resolution`)
stay available-but-unrecorded; android stays hard-gated (F4 honest exception:
10/11, not 11/11); no knowledge admission (K untouched); no README byte
changes.

## C2 — calibration: orphan_sweep v2 — the r80 carry-in classes close inside the standing instrument

v2 supersession of the r80 capability instrument (`reports/round-81/
orphan_sweep2.py`, sha256 pinned below; v1 `reports/round-80/orphan_sweep.py`
stays byte-untouched). Four named changes, each closing a carried or routed
item:

1. Repeated trailing line-ref segments strip (`file.md:57,:148,` → `file.md`)
   — the r80 ABSENT list carried that multi-ref remnant whose file IS
   committed (false disposition). v1 strips one segment only.
2. Dir-style cites: extensionless cited path with a committed `<path>.md`
   sibling classifies `committed` with a `normalized:` note (r80:
   `corpus/lessons/round-64` absent while `round-64.md` is committed). A
   negative vector proves normalization cannot mask a real absent.
3. Count basis (the r80 closure routed rule): every run prints
   `SWEEP_CORPUS fleet-reports=<n> lessons=<n>` — a receipt regenerated after
   its citation corpus grows carries its count basis (the CITED=344-vs-357
   class).
4. Receipt shape: `--format full` (default) or `--format summary` (states the
   filter in its output) — the r80 real-tree receipt carried 2 of the SWEEP
   lines with no stated filter. The r81 real-tree receipt carries FULL output.

- BEFORE (red, committed `sweep-v1-red.log`): the committed v1 instrument
  over the real tree prints `CITED=358 COMMITTED=344 LANDABLE_ORPHANS=0
  ABSENT=14` with NO `SWEEP_CORPUS` line, and `grep -cE
  '^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|
  corpus/lessons/round-64) '` = **2** (two committed files misdispositioned);
  the r80 truncated receipt class (2 SWEEP lines, no filter) is the committed
  `reports/round-80/sweep-real-after.log`.
- AFTER (green): `--selftest` → 7 legs ok + `SWEEP_SELFTEST=pass` exit 0
  (clean, planted-orphan, absent, line-ref, dir-style, masked-absent
  negative, mutant attributed kill) run from the extracted landing archive
  outside any repo; real tree `--format full` receipt carries every SWEEP
  line + `SWEEP_CORPUS fleet-reports=21 lessons=42` +
  `CITED=357 COMMITTED=345 LANDABLE_ORPHANS=0 ABSENT=12` exit 0 (the two
  artifacts now committed; `grep -cE '^SWEEP absent
  (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|
  corpus/lessons/round-64) '` = **0**); unrecognized forms exit 64.

VERIFY conditions: (a) selftest 7/7 legs + pass, exit 0, hermetic (archive
run); (b) real-tree full receipt: ABSENT=12, LANDABLE_ORPHANS=0, exit 0,
SWEEP_CORPUS line present, parser-artifact grep = 0; (c) mutant leg
`SWEEP_SELFTEST_MUTANT_FLAGGED=ok` (attributed kill preserved); (d) v1 bytes
and v1 receipts unchanged (no rewrite of r80 evidence; the correction for the
r80 CITED/COMMITTED drift is APPENDED in SCORECARD/LOG, never in-place).
KILL RULE: any condition fails → v2 retained as a rejected candidate in
`reports/round-81/`, the carry-in corrections still land (they are protocol
duties, not claim-consequent), and C2 records falsified honestly.

Boundary: C2 moves no criterion score; the moved quantity is the standing
capability's disposition accuracy (2 false absents → 0) plus the receipt
contract (count basis + full output). Counts remain per-revision-corpus (the
erratum rule): v2's `CITED=357` over the current tree is the v2 tokenizer over
the corpus its header names — not comparable to v1's numbers without the
basis line.

## Separability

- c1-only tree (base archive + fixture/record + f_probe4, no orphan_sweep2):
  F4 10/11 + oracle OK; `reports/round-81/orphan_sweep2.py` ABSENT from the
  tree → `c1-only.log`.
- c2-only tree (base archive + orphan_sweep2 only, no fixture/record/
  f_probe4): selftest pass; F2 over that tree prints 8/9; f_probe4 ABSENT →
  `c2-only.log`.

## No-harm (protected paths)

corpus/knowledge/, corpus/README.md, corpus/QUALITY.md, corpus/verify_*.py,
SKILL.md, SHONEN.md, PROVINCE.md, LOG.md and SCORECARD.md (until the
adjudication commit), all pre-r81 fixtures, frozen instruments (f_probe.py
`e15a43af…`, f_probe2.py `0be0d8b5…`, f_probe3.py `9441640d…`, orphan_sweep.py
`f21f5e3d…`, province_probe2/3, gate/receipt probes v1+v2, r71 counter): no
byte changes base→tip except the declared additions; `noharm-diff.txt` at
adjudication.

## Fresh-start §7 (r71/r72/r73 rejected closures re-read + spot-checked)

All three re-read this round (fleet `.ufo/reports/round-7{1,2,3}/revenger.md`)
and spot-checked against the lane's own records: r71 C1 (C05 sixth pass) —
falsified by wave Q09/Q16 FAILs, honest stop; r72 C1 (C15) — wave never
settled, falsified by its own frozen predicate (0/1), honest stop; r73 C1
(C10) — wave released un-settled, claim unresolved by the frozen rule. All
three are **K-admission claims whose 16-vote wave Q-review surface never
existed or never settled** — on this host that surface still does not exist
(no `.ufo/state/` dispatcher; the r74 L0 at `fleet .ufo/l0-questions.md:233`
re-read this round: still unanswered). A do-nothing control reaches each
identically (the claims move only if a settled wave rules). Ruled out this
round, with fresh probes (2026-11-01):

- **F android** — `REA_JADX_MCP_JAR` UNSET, no jadx on PATH, no `~/tools/jadx*`
  (`~/tools` holds only downloads/ + ghidra_12.1.4_PUBLIC); S448 receipt
  stands. F4's honest exception: 10/11, not 11/11.
- **macho/signature families** — `rea capabilities`: `unsupported_host`
  ("Native macOS utilities require macOS."), S453; Hopper also
  `unsupported_host` on win32; IDA `not_configured` (no REA_IDA_MCP_CONFIG);
  kuna `not_configured` (no REA_KUNA_COMMAND).
- **K admissions** — wave Q-review surface absent, L0 unanswered (re-read).
- **criterion C repair** — §9 sizing, unchanged r78–r80 ruling.
- **criterion R extension / criterion N attribution pair** — stay routed
  (r75/r76/r79/r80 lineage); not declared this round (C2 supersedes the
  orphan-sweep parser item only).
- Declared claims are ones a do-nothing control cannot reach: a new producer
  record + mapping revision (C1) and an instrument supersession with new
  attributed vectors (C2).

## Carry-in dispositions (r80 non-author closure, addressed first)

1. **Sweep-count drift** (`CITED=344 COMMITTED=330` quoted in the r80
   report/claims/SCORECARD C2 row vs the committed receipt's
   `CITED=357 COMMITTED=343`): root-caused FIRST-HAND this round
   (`preprobe-keyed-shape.log` §r80-corpus reconstruction): the tokenizer over
   lessons@`ef7d3ee3` + fleet reports minus round-80 yields **exactly
   CITED=344**, classified (v1 rules, current HEAD) committed=330 +
   absent-fleet=6 + absent=8 — the quoted figure is the LANDING-ERA citation
   corpus. The tokenizer over lessons@`b1e0c60e` + current fleet yields
   **exactly CITED=357** — the receipt's corpus (the round-80 adjudication
   lesson + r79 erratum and the fleet round-80 report joined the corpus
   after the landing). Current tree (v1): CITED=358 (the r80 spot-check
   lesson +1 net-new). Verdict values identical in all three corpora:
   LANDABLE_ORPHANS=0, ABSENT=14, exit 0. Fix: an APPENDED erratum section in
   SCORECARD.md + a correction entry in LOG.md naming per-revision citation
   corpora (never an in-place rewrite); the rule lands as v2 change 3
   (SWEEP_CORPUS header).
2. **Truncated sweep receipt**: the r81 real-tree receipt carries FULL output
   via v2 `--format full` (default); `--format summary` states its filter.
   The r80 receipt stays as committed evidence.
3. **SHONEN `[~]` reviewer debt**: operator-side (the r80 closure noted it
   for the operator; the lane cannot mint a non-author verifier for its own
   bytes). Routed around: this round files `[~]` lines with resolvable
   pointers again, claims no `[x]`, and takes no SHONEN claim.

## Sources opened this round (SOURCES rows land with the landing commit)

- S457: `rea capabilities` (provider `rea-artifact-graph` groups) +
  `rea inspect-keyed-archive --help` + `rea --llms`, opened 2026-11-01 —
  located quote: "Inspect a Foundation keyed archive as an object-reference
  graph" (`rea --llms` manifest table; 9 words). ADMIT, tier A own-work.
- S458: `corpus/live/runs/round-81/` (record, receipt, LEDGER) +
  `corpus/fixtures/keyed-r81/` (fixture, generator, truth, oracle), opened
  2026-11-01. ADMIT, tier A own-work.

C1 is the sourced claim (S457); C2 rests on the r80 closure's routed rule
(S456 lineage) and the committed r80 receipts.

## Instrument sha256 pins (at freeze)

- `f_probe4.py` sha256 `4d871971…6a3c7`; the ten F3 family lines are
  byte-equal to `f_probe3.py`'s (its sha `9441640dc0ff…14b418` unchanged).
- `orphan_sweep2.py` sha256 `30aa3527…93eb6`; v1
  `reports/round-80/orphan_sweep.py` blob unchanged (`f21f5e3d7306…1890b`).
- `generator.py` / `oracle_check.py` / fixture land in the landing commit;
  their receipts are in `preprobe-keyed-shape.log` + `receipt.json`.
