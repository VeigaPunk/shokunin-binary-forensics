# Round 81 — an eleventh F family moves through a real keyed-archive producer run (criterion F4, `artifact-graph`); the orphan sweep learns the r80 carry-in classes (v2 supersession)

Base `081f032fda9502ebfbceb295d7e097dd8803bce1` (r80 tip + non-author
spot-check). Freeze `8261a24cb806d60a47a640f948de339912dcc96b` (claims +
sha-pinned instruments + red-befores + preprobe receipt, committed before any
after-run). Landing `88b7e7cee2f07c77b7d9597e8d9e3159aed37f19` (keyed-archive
fixture + producer record + S457–S458). Adjudication = the commit carrying
this lesson. Two claims, distinct axes, causally separable, neither
exploratory: **C1 coverage** (F4 mapping revision + one real
`rea inspect-keyed-archive` record on an authored inert Foundation keyed
archive) and **C2 calibration** (orphan_sweep v2 — the r80 carry-in classes
close inside the standing instrument: repeated line-ref stripping, dir-style
cite normalization with a masked-absent negative, the SWEEP_CORPUS count
basis, and full-output receipts).

## Carry-in dispositions (r80 non-author closure; addressed first)

1. **Sweep-count drift** — first-hand reproduced, not taken on trust
   (`preprobe-keyed-shape.log` §r80-corpus reconstruction): the v1 tokenizer
   over lessons@`ef7d3ee3` + fleet reports minus round-80 yields **exactly
   CITED=344**; classified with v1 rules against current HEAD: committed=330 +
   absent-fleet=6 + absent=8, LANDABLE_ORPHANS=0 — the r80
   report/claims/SCORECARD figure is the LANDING-ERA citation corpus, exactly
   as the closure judge reconstructed. The tokenizer over lessons@`b1e0c60e` +
   current fleet reports yields **exactly CITED=357** — the committed
   receipt's corpus (the round-80 adjudication lesson + r79 erratum and the
   fleet round-80 report joined after the landing; the fleet report
   contributes +11 tokens, the lesson/erratum +2 net-new). The current tree
   (v1) prints CITED=358 (the r80 spot-check lesson, +1 net-new:
   `corpus/live/runs/round-80`). Verdict values identical in all three
   corpora (LANDABLE_ORPHANS=0, ABSENT=14, exit 0). Correction filed as an
   APPENDED erratum section in SCORECARD.md + a correction entry in LOG.md
   naming per-revision citation corpora — never an in-place rewrite; the rule
   lands as v2 change 3 (`SWEEP_CORPUS` header).
2. **Truncated sweep receipt** — the r81 real-tree receipt
   (`sweep2-real-after.log`) carries FULL output (all 357 SWEEP lines +
   summary + the `SWEEP_CORPUS fleet-reports=21 lessons=42` basis line);
   `--format summary` exists and states its filter in its own output. The r80
   receipt stays as committed evidence (never rewritten).
3. **SHONEN `[~]` reviewer debt** — operator-side (the r80 closure noted it
   for the operator; a lane cannot mint a non-author verifier for its own
   bytes). Routed around: `[~]` lines with resolvable pointers again in this
   round's report; no `[x]` claimed; no SHONEN claim declared.

## Gate

Fresh-start §7 (r71/r72/r73 rejected closures re-read at fleet
`.ufo/reports/round-7{1,2,3}/revenger.md`; full dispositions in
`reports/round-81/claims.md` §7): all three are K-admission claims whose
16-vote wave Q-review surface never existed or never settled — a do-nothing
control reaches each identically on this host. Ruled out with fresh probes
(2026-11-01): **F android** (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH,
`~/tools` = downloads/ + ghidra only — S448 stands; F4's honest exception is
10/11, not 11/11); **macho/signature** (`rea capabilities`:
`unsupported_host`, S453; Hopper `unsupported_host` on win32; IDA
`not_configured` — no `REA_IDA_MCP_CONFIG`; kuna `not_configured` — no
`REA_KUNA_COMMAND`); **K admissions** (r74 L0 re-read, unanswered);
**criterion C repair** (§9 sizing, unchanged r78–r80); **criterion R
extension / criterion N attribution pair** (stay routed — not declared this
round). The C1 route is the one the ruling-out map leaves open: an
in-province producer surface that IS manufacturable here and is in NO F3
family set (S457 — the r74–r80 capability scans covered macho/signature and
sqlite scopes but never this provider's decode group).

Sources opened this round (rows appended inside the Registry section,
directly after S456):

| row | path/command | located quote (≤25 words) | decision |
|---|---|---|---|
| S457 | `PYTHONUTF8=1 rea capabilities` (provider `rea-artifact-graph` groups) + `rea inspect-keyed-archive --help` + `rea --llms`, opened 2026-11-01 | "Inspect a Foundation keyed archive as an object-reference graph" | ADMIT (tier A, own-work environment; the r81 re-open of S453's scan, narrower scope) |
| S458 | `corpus/live/runs/round-81/` (record, receipt, LEDGER) + `corpus/fixtures/keyed-r81/` (fixture, generator, truth, oracle), opened 2026-11-01 | exit 0; `operation: inspect_keyed_archive`, provider `rea-artifact-graph`; oracle `ORACLE OK (27/27 checks)` | ADMIT (tier A, own-work) |

Census: round start — sanctioned explicit-lane-dir form exit 0, 31 W (21 W01 +
10 W04, the same disclosed classes; literal form exit 2, disclosed r74–r81
lineage, L0 consolidation line stands). Round end — receipts in
`reports/round-81/census-after.log`: sanctioned worktree form exit 0, 31 W;
literal form exit 2 (unchanged lineage); landing-archive-bytes census over
`88b7e7ce` fires **E11 ×2** (`S457`/`S458` used-by
`corpus/lessons/round-81.md` preceding the lesson — the expected intermediate
state, same shape as r80's S455 E11; resolved by the adjudication commit that
carries this lesson) with 31 W and zero other E-findings (S457/S458 appended
inside the Registry, grammar-checked mid-flight: 458 rows, no E01, no
duplicate ids, no enum violations). The final-tip archive census (exit 0,
zero E) is re-runnable by the closure judge per the receipt's note. A
receipt-defect was self-caught in the first census-after draft (it grepped
the wrong row prefix over the extraction and printed 0 W-lines) — disclosed
in the receipt itself.

C1 evidence chain: S457 (the decode group `available: true`, in no F3 family
set) → F4 mapping revision frozen at `8261a24c` BEFORE the run (f_probe4 sha
`4d871971…6a3c7`; the ten F3 families byte-equal; denominator disclosure in
the instrument header and claims) → red `f4-before.log` (base archive: v1
7/8, F2 8/9, F3 9/10, `F4_COVERAGE=9/11 score=8.18`, artifact-graph absent) →
fixture authored (`corpus/fixtures/keyed-r81/`: generator self-check derives
EVERY oracle-checked fact from the built bytes — roots, 6 objects, 4
references, format, totals, offset/truncation; 14/14 SELFCHECK; regen
byte-identical; fixture sha256 `f0e02e64…37785c`) → one bounded producer run
on the committed bytes (`inspection.json` = exact stdout, 3174 bytes, sha256
`83fe4046…348fcf`, exit 0, stderr 0 bytes, Evidence
`ev_6eb77fb0…02af4b73`) → oracle `ORACLE OK (27/27 checks)` (operation,
provider, evidence form, subject sha == fixture sha, format binary-plist,
6 objects exact, 4 references exact + no extras, roots/offset/next_offset/
truncated, confidence observed, authority shipped-artifact — every value
byte-derived, never copied from the record) → green `f4-after.log`
(landing archive: `F4_COVERAGE=10/11 score=9.09` with artifact-graph; v1
7/8, F2 8/9, F3 9/10 unchanged; oracle + regen re-run over archive bytes).

C2 evidence chain: the r80 closure's routed rule (S456 lineage) → v2 frozen
at `8261a24c` (orphan_sweep2.py sha `30aa3527…93eb6`; v1 blob unchanged
`f21f5e3d…1890b`; declared exits 0/1/64 unchanged) → red `sweep-v1-red.log`
(v1 over the real tree: full output per the carry-in rule, CITED=358
COMMITTED=344 ABSENT=14, NO count-basis line, the two parser artifacts
misdisposed absent — grep = 2; the r80 truncated receipt is the committed
second red) → green `sweep2-selftest-after.log` (7 legs from the extracted
landing archive outside any repo: clean, planted-orphan flagged, absent,
line-ref, dir-style, masked-absent negative, mutant
`SWEEP_SELFTEST_MUTANT_FLAGGED=ok`; `SWEEP_SELFTEST=pass`, exit 0) +
`sweep2-real-after.log` (FULL output: `SWEEP_CORPUS fleet-reports=21
lessons=42`, `CITED=357 COMMITTED=345 LANDABLE_ORPHANS=0 ABSENT=12`, exit 0;
the parser-artifact grep = 0 — both artifacts now classified committed with
auditable notes/merges). Separability: `c1-only.log` (F4 10/11 + oracle OK
with orphan_sweep2 ABSENT) and `c2-only.log` (selftest pass + F2 8/9 with
f_probe4 ABSENT).

Boundary: C1's print moves 9.00 → 9.09 only because the mapping revision adds
the family in the same round as its first real record — had the record not
landed, F4 would print 9/11 (8.18), LOWER than the frozen F3's 9/10 (9.00) on
the same tree; the moved quantity is the in-province family with an
oracle-checked record, not the print. Android stays hard-gated (the F4 honest
exception: 10/11, not 11/11). C2 moves no criterion score; the moved quantity
is the standing capability's disposition accuracy (2 false absents → 0) plus
the receipt contract (count basis + full output). Counts remain
per-revision-corpus: v2's CITED=357 over the current tree is the v2 tokenizer
over the corpus its own header names (one v1 token merges into an existing
cite after cleaning: 358 → 357), not comparable to v1 numbers without the
basis line. No knowledge admission (K 8/15 untouched — operator-blocked route
re-checked, not attempted); no README byte changes; PROVINCE byte-unchanged.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Frozen-expectation drift: the fixture generator's self-check constants (scalar=4/dict=1) were drafted from the rehearsal-2 shape and never updated when the authored shape changed to 6 objects (1 nil + 3 scalars + 2 dicts; the integer 1729 lives inside object 2, not as a separate scalar) | the build run: `SELFCHECK scalar_objects_4 FAIL` / `SELFCHECK dict_objects_1 FAIL` while every byte-derived check passed (`preprobe-keyed-shape.log` §generator self-check catch) | the Q06 discipline itself (SKILL.md §2: derive from the built bytes, then assert) — the derive/truth path was right, the hardcoded expectations were stale | constants corrected to the authored shape; final build 14/14; mined so a generator's check constants are re-derived at every shape change, never carried from a prior draft |
| Oracle sort defect: the reference set-equality sort crashed on the real record (`TypeError: '<' not supported between instances of 'int' and 'NoneType'`) because the root reference's `source` is null and Python 3 refuses None-vs-int tuple ordering | first real run of `oracle_check.py` over the saved record (traceback; the record bytes were saved unregenerated and the fixed oracle re-ran over the SAME bytes) | the first real run (self-caught, pre-commit; disclosed in `preprobe-keyed-shape.log` §oracle sort defect) | a None→-1 sort key; the oracle now sorts both sides through the same key; mined so "sort for set equality" over mixed-null producer fields needs a total order, not the default tuple order |
| (carry-in, item 1, captured by the r80 closure — root-caused first-hand this round) narrative counts quoted from one run's corpus vs a receipt regenerated over a grown corpus: `CITED=344 COMMITTED=330` (landing-era corpus) vs the receipt's `CITED=357 COMMITTED=343` (b1e0c60e corpus) | this round's reconstruction: 344 and 357 both reproduced EXACTLY (`preprobe-keyed-shape.log`); verdict values identical in all corpora | the r80 non-author closure (routed to this round) | the appended SCORECARD erratum + the LOG correction entry name per-revision citation corpora; the rule lands as orphan_sweep2's `SWEEP_CORPUS` header (a receipt carries its count basis) — a narrative count is a `grep -c` of a named-corpus receipt, never a recalled or cross-corpus number |
| (self-caught, pre-freeze, in scratch) the first recon sweep passed the REAL fleet root instead of the scratch recon fleet root, printing CITED=355 and 3 spurious absents (`corpus/lessons/round-80.md`, `reports/round-80/census-after.log`, `reports/round-80/noharm-diff.txt`) — a corpus-isolation error that would have poisoned the erratum's numbers | the decomposition run: `collect_citations(recon-lane, recon-fleet)` = 344 exactly, with NO round-80 tokens, vs the 355 full-sweep output | the cross-check between the tokenizer-level count (344) and the sweep-level count (355) disagreeing | the reconstruction re-run with the scratch fleet root; both load-bearing numbers (344, 357) then reproduced exactly; mined so a reconstruction isolates BOTH sides of the corpus, not just the lane side |
| (self-caught, pre-commit) the first census-after draft grepped the archive-census output for the lane's row prefix (`^shokunin-binary-forensics`) while an extraction is named by its own directory name (`census-arch`), printing `W0_lines: 0` and hiding the real 31 W + the two E11 findings | `reports/round-81/census-after.log` form-3 NOTE (the defective draft's numbers and the corrected re-run are both on record) | review of the receipt against the raw census output before commit | the receipt rewritten from the raw output with the correct prefix; the archive extraction keeps its own name in census rows — a receipt grep must match the row prefix the census actually prints for that input form |

## Routed forward

- **Criterion R extension** (legacy receipt-quoting registry rows) and
  **criterion N's mutation-killed attribution pair** — r75/r76/r79/r80/r81
  lineage; still open, not declared this round.
- **Criterion C repair** — §9 sizing, unchanged since r78.
- **Criterion-instrument class question** — unchanged; orphan_sweep2 lands as
  a capability supersession note in the existing r80 row, NOT a registry row.
- **F android** — hard-gated on the caller-supplied `REA_JADX_MCP_JAR`
  (re-probed; S448 receipt stands). F4's honest exception: 10/11, not 11/11.
- **K** — blocked on the wave Q-review surface (r74 L0 unanswered, re-read at
  `fleet .ufo/l0-questions.md:233`).
- **Census literal form** — operator-side routing continues (r74–r81
  lineage; the consolidation L0 line landed r79).
- The artifact-graph family's other two operations
  (`decode_interface_builder`, `trace_dylib_resolution`) stay
  available-but-unrecorded (same shape as browser-runtime's unrecorded
  operations) — each is one bounded fixture+record round if a later round
  wants it.
- The remaining real absents in the sweep (ScoutAmp misroot, `round-73/votes`
  empty-dir cite, `w1.ready` rename, the gitignored `.pyc`,
  `measurements.json` stale name, `controls/A-H` range shorthand) keep their
  recorded dispositions — v2 touches only the two parser-artifact classes.
