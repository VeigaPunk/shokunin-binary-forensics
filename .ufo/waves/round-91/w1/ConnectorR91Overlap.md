# ConnectorR91Overlap: sibling-overlap scan (round 91, w1)

Seat ConnectorR91Overlap (connector, leaf). Read-only across every sibling lane; nothing outside
this directory and `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-91/w1/ConnectorR91Overlap.md`
was written. No sibling repository was edited, no sibling file imported. No tool installed or
upgraded (nothing was needed). Scratch `/fast/scratch/hyaku/revenger-r91/ConnectorR91Overlap`
removed at exit; its two receipts are copied here under `receipts/`.

Frozen claims read first, in full: `reports/round-91/claims.md` (lane base `b13aac756ac33aa5245c13966c624de4370206d0`).
Lane HEAD at scan time `d509e982844d31bd26f3cb96e1a663e7d36f2ca8`; declared C2 range
`7fab03f..refs/heads/main` measured at **23 commits** (the freeze counted 21; L1 committed twice
after the freeze, so the receipt will read N=23 — still inside the frozen `N ≥ 20` leg).

Question asked: does any other shokunin lane already hold (a) a commit-message↔tree conformance
instrument, or (b) a self-assessment gate that reads a **stated cell**, that this lane is about to
duplicate?

Short answer: **(a) yes — tameshi owns it, as a registered capability, and this lane's C2
converges on it in the only grammar that can pass the frozen `M ≥ 20` leg; (b) no — every sibling
self-assessment gate reads a different object (header-keyword cell, published prose fraction, or a
round-scoped positional cell without the truncation rule), so C1's SM6 v3 rule is new.**

---

## 1. Method

- Scope: `/home/vgpnk/Projects/shokunin/*-shokunin/` (20 siblings, revenger excluded) **plus** the
  fleet root's `scripts/` read-only. Skipped: `.git`, `.jj`, `node_modules`, `.venv`, `__pycache__`,
  `target`, `dist`.
- Pass 1 (name): `*check*|*probe*|*audit*|*sweep*|*verify*|*lint*` under `*.py` at depth ≤ 4 —
  400+ candidates.
- Pass 2 (job): three targeted greps over code only —
  commit-message readers (`--format=%B`, `--pretty=%B`, "commit message"),
  tree-existence readers (`cat-file -e`, `ls-tree`),
  and the metric token this lane's C1 keys on (`K_HELD_BACKED`).
- Pass 3 (read): header/docstring + the decisive code path of every candidate that survived, plus
  the fleet's own attribution register (`kama-shokunin/corpus/knowledge/cross-lane-scope.md`).
- One sibling instrument was **run** read-only (git objects only, no index, no worktree write) as a
  cross-check; receipt at `receipts/tameshi-bind-over-lane-range.log`. Its interface was read
  first and its write surface verified (`out` is `sys.stdout`; no `open(...,'w')`, no network).
- Fleet root `scripts/` contains only `fixtures/`, `hyaku/`, `shokunin-watchdog.sh`,
  `sources-census.sh`. **No fleet-level instrument reads commit messages or resolves cited paths.**

---

## 2. Hit table

`relation` is asserted against the round-91 surface, not against the sibling's own purpose.
`reusable` = runs unmodified against another lane's repo and answers the same question;
`adjacent` = same family, different object or different input.

### 2a. Commit-message ↔ tree conformance

| # | lane | path | one-line scope | relation |
|---|---|---|---|---|
| 1 | **tameshi** | `tools/receipt-commit-bind.py` (503 L; registered capability `SCORECARD.md:254`) | Sweeps `base..tip` on git objects: (arm 1) every `.ufo/evidence/` path ADDED in range and named in a message must exist in that commit's tree; (arm 2) every `.ufo/evidence/…`/`tools/…` **span** in a message must resolve at that commit via `git cat-file -e`; (arm 3) every file-like token (declared extension list incl. `.log`) must resolve to *some* path in that commit's tree; `BIND_DEFECT` + exit 1, exit 2 on a vacuous range; 7-arm hermetic `--selftest` | **reusable** — closest sibling; ran green against this lane (see §5). Cannot satisfy C2's frozen predicate (different CLI, output contract, pass line, and a prefix-restricted span arm) |
| 2 | mado | `quality/check-cited-revisions.py` (180 L) | A row citing a revision as an instrument's last change must cite a prefix of `git log -1 --format=%H -- <instrument>` | adjacent (message never read) |
| 3 | kama | `tools/prereg-time-check.py` | Preregistration timestamp vs `git log -1 --format=%cI` | adjacent (timestamp only) |
| 4 | kama | `corpus/knowledge/cross-lane-scope.md:120-133` | The fleet's cross-lane attribution register; already names `receipt-commit-bind.py` as prior art for receipt→revision binding | register, not instrument — **the adoption surface** |
| 5 | tameshi | `tools/receipt-revision-gate.py` (385 L) | Binds a receipt's `rev=` to the revision it certifies | adjacent (receipt↔revision) |
| 6 | revenger (own) | `corpus/q15_tree_id_check.py` | `tree-identity restatement:` pairs must resolve via `git rev-parse <hex>:corpus` | adjacent, own lane (tree identity, not messages) |

No shell instrument anywhere in the fleet reads commit messages (`grep -rln 'git log .*%B' --include='*.sh'`
returns only wave-local fixtures, none a conformance checker).

### 2b. Cited-path existence sweeps (the family C2's extraction step belongs to)

| # | lane | path | one-line scope | relation |
|---|---|---|---|---|
| 7 | kotoba | `verifiers/check_report_pointers.py` (902 L) | Every backticked lane pointer of a round report resolves at `--rev`; `unresolved U` exit 0 iff U=0 | adjacent — **nearest grammar match** (backticked path extraction), object is the report not the message |
| 8 | kama | `tools/round53-cited-path-check.py` (504 L), `round54-cited-path-check.py` (862 L) | Every repo path the self-assessment cites resolves at a lane revision, or is ledgered with a git-re-derivable reason; drop-guard per surface | adjacent (round-scoped; SCORECARD/SHONEN/SKILL surfaces) |
| 9 | tsukuroi | `tools/check-cited-receipts-r62.py` (351 L) | Every `.ufo/waves/round-<N>/…` path named by any tracked text blob at a revision exists as a blob at the same revision | adjacent — same predicate, population = tracked blobs |
| 10 | mado | `quality/check-evidence-pointers.py` (250 L) | Every pointer in the lane's own records resolves at a rev; correction-pair `old` sides exempt | adjacent |
| 11 | kotodama | `tools/check-orphan-evidence.py` (229 L) | Evidence cited by closed round reports but never committed (orphan sweep) | adjacent |
| 12 | kotodama | `tools/check-cited-records.py` (198 L) | `EMPTY` (cited path is a 0-byte file) and `SCRATCH` (absolute scratch path cited) legs | adjacent |
| 13 | kama | `tools/round68-receipt-pointer-audit.py` (485 L) | Section-relative `measured/…` backtick pointers resolve at `--rev` | adjacent |
| 14 | kasegi | `corpus/instruments/citation-ground-check.py` (537 L) | Citations that exist on disk but the resolver cannot open (bare `corpus/` prefix class) | adjacent |
| 15 | chousa | `tools/digest-in-tree.py` (187 L) | Every pinned sha256 re-derives from committed blob bytes | adjacent (digest, not path) |
| 16 | revenger (own) | `reports/round-90/source_path_check.py` (201 L) | `corpus/SOURCES.md` Registry rows: anchored spans must resolve under TREE | adjacent, own lane |

### 2c. Landing / receipt sweeps (the "cited thing must be committed" family)

| # | lane | path | one-line scope | relation |
|---|---|---|---|---|
| 17 | tsukuroi | `tools/check-report-receipts.py` (452 L) | Every revision-cited report gate has a committed receipt in the lane snapshot | adjacent |
| 18 | kaidoku | `tools/round-56/receipt-audit.py` (266 L) | Freeze-receipt completeness against the freeze commit's tree | adjacent (round-scoped) |
| 19 | kama | `tools/round67-worktree-landing-check.py` (237 L) | Worktree bytes must be byte-identical to the HEAD blob, per declared path | adjacent |
| 20 | mori | `tools/mori-unlanded-check.py` (250 L) | Round work on disk but not committed | adjacent |
| 21 | revenger (own) | `reports/round-88/receipt_sweep.py` | Registry-wide re-runnability of receipts citing counting commands | adjacent, own lane |

### 2d. Self-assessment / mismatch gates (the family C1's SM6 belongs to)

| # | lane | path | one-line scope | relation |
|---|---|---|---|---|
| 22 | **tsukuroi** | `tools/check-self-assessment.py` (1134 L; registered `SKILL.md:2356`) | 27 fixed K-checks between stated axes and observed state at a bound revision; the axes table is read as **cells selected by header keyword** (`header_index`), the score cell parsed by `number_after` | **reusable in principle** (`--revision --repo`, selftest) but its check set hard-codes tsukuroi's surfaces → adjacent for SM6; closest sibling for the *family* |
| 23 | kaidoku | `tools/round-26/c2-calibration.py` | K1–K6: "the **first N/M token** in the observable cell" of the depth/coverage rows; the cell is read **positionally** at `cells[2]` (`:181`) | adjacent (round-scoped) — **nearest precedent for the positional-cell shape, and it carries exactly the token-adjacency weakness v3 repairs** |
| 24 | kaidoku | `tools/round-49/c2-mismatch.py` | 9 atoms: a stated sentence paired with a re-derivation from committed bytes | adjacent (round-scoped) |
| 25 | mado | `quality/check-axis-scores.py` | The last published axis table's fraction must equal the fraction its own instrument re-derives | adjacent (published prose, per-axis instrument) |
| 26 | kama | `tools/round35-statement-audit.py` (199 L), `round36-statement-audit.py` (290 L) | Frozen statement corrected iff a correction row names it and the re-derived fact agrees | adjacent (round-scoped, correction-row audit) |
| 27 | revenger (own) | `corpus/self_assessment_check.py` (v1), `corpus/self_assessment_check2.py` (v2) | SM1–SM6 between lane self-description and repo state; v2's SM6 is the token-adjacent reading v3 supersedes | own lane — v3 supersedes v2, v1/v2 bytes stay |

No sibling anywhere contains the string `K_HELD_BACKED` in code (`grep -rln K_HELD_BACKED --include='*.py'`
across the fleet → 0 hits; every other hit is prose in a report or wave artifact).

---

## 3. Closest sibling, per round-91 instrument

- **C1 (calibration, SM6 v3) — closest: `tsukuroi-shokunin/tools/check-self-assessment.py`.**
  It is the fleet's only *registered* self-assessment capability, lane-agnostic in CLI, git-only in
  input, with a selftest. But its 27 checks answer a different question: it compares the axes
  table's **score column** (a single integer per axis, located by header keyword) against a
  re-derivation, and its path checks resolve SHONEN/capabilities citations. It has no rule that
  reads a **before→after** statement, and no rule keyed on a metric token inside a row.
  The nearest *shape* is kaidoku `round-26/c2-calibration.py:181` — `cells[2]`, "first N/M token" —
  which is round-scoped, reads a different row set, and is the very rule that false-flags a
  before→after cell carrying a parenthesised score.
- **C2 (operability, message↔tree) — closest: `tameshi-shokunin/tools/receipt-commit-bind.py`.**
  Same job class, same input class (git objects, `base..tip`), same defect class (a message naming
  content its tree does not carry), and it is a **declared capability** in tameshi's SCORECARD
  (`:254`, "commit-message receipt binding sweep"), so the fleet already counts this job as owned.

---

## 4. What the two round-91 instruments add that no sibling covers

### C1 — `corpus/self_assessment_check3.py`

No sibling's check set states, let alone implements, the v3 rule. What is new is the **reading
rule**, not the metric:

1. **Region selection by row shape**: last `K_HELD_BACKED` line; if it is a `|`-row with ≥5 cells
   the stated region is **cell index 2**, otherwise the whole line. Every sibling that reads a
   table cell picks it by *header keyword* (tsukuroi) or by a *fixed position for a different row
   set* (kaidoku); none makes the row's own shape decide between a cell and a bare line.
2. **Boundary at a sibling metric**: the region truncates at the first `K_HELD_BACKED_STRICT`. No
   sibling gate knows that two metrics can share one cell, so none truncates — this is the exact
   failure the round-90 critic produced on the lane's real row format.
3. **Right-side-of-`→` preference with an optional parenthesised score skip** (`8/14 (5.7) → 8/15 (5.3)`).
   kaidoku's rule takes the *first* N/M token in the cell; on this row shape that reads the
   **before** value and silently scores a stale statement as current.
4. **Fail-closed on "the row does not state the quantity"** (SM6 = 1 when no group is found) —
   no sibling self-assessment gate has a "the record does not state what it is judged on" arm.

Nothing in the fleet is reusable here as bytes: tsukuroi's gate is bound to its own surfaces and
its own 27 ids; kaidoku's is frozen to a round-26 row set. The lane is **not duplicating** C1.

### C2 — `reports/round-91/message_tree_check.py`

Adds, relative to tameshi's bind:

1. **Prefix-unrestricted, backtick-anchored path extraction** — any repo-relative backticked path,
   not just `.ufo/evidence/` or `tools/`; tameshi's arm 2 sees `spans=0` on this lane's range
   (§5) because none of its messages cite those prefixes.
2. **`.log` filenames as a first-class, bare-tolerated class** (`bare` reported separately), where
   tameshi treats `.log` as one extension among twenty.
3. **A single summary contract** `MESSAGE_TREE commits=N cited=M misses=K` with exit 0/1/2, and a
   `--selftest` that prints `MSG_TREE_SELFTEST=pass` — a machine-readable pass line tameshi's
   selftest does not emit (`RECEIPT_COMMIT_BIND_SELFTEST: 7/7 pass`).
4. **A frozen planted-miss leg in the counter** (probe-built repo, `c0..c1` clean / `c1..c2` red on
   `missing/r91.txt`) that a stub cannot satisfy — a stronger anti-stub contract than a selftest the
   instrument itself runs.

But see §6: items 1–2 are **not exercised** by the declared range, so the instrument as frozen will
be driven by the bare-token arm — i.e. by the arm tameshi already owns.

---

## 5. Measured cross-check (read-only, sibling instrument on this lane)

`python3 -I -B tameshi-shokunin/tools/receipt-commit-bind.py --repo <revenger lane> --base 7fab03f --tip refs/heads/main`
→ exit **1**, receipt `receipts/tameshi-bind-over-lane-range.log`:

```
RECEIPT_COMMIT_BIND: commits=23 evidence=0 named=0 carried=0 spans=0 bare=24 findings=1
BIND_DEFECT d509e9828 names-unknown ufo-wave-policy.json -> no tree path with that name at that commit
```

Three facts follow, all measured (`receipts/citation-grammar-census.log`):

| reading of "cited" | count over `7fab03f..refs/heads/main` (23 commits) |
|---|---|
| backticked repo-relative paths | **0** (the range contains **no backtick character** in any message) |
| prefix path tokens (`corpus/ reports/ tools/ scripts/ templates/ .ufo/`) | 9 |
| bare `*.log` filenames | 7 |
| widest token grammar (tameshi arm-3 extension list) | **24** (22 distinct) |

So on this lane's own history the C2 instrument's **claimed** extraction classes read 0 + 7 = 7
citations. The frozen `cap_probe.py` leg 4 requires `cited=M` with **M ≥ 20**. Only the widest
token grammar clears that bar.

The one `BIND_DEFECT` tameshi reports is `ufo-wave-policy.json` — a **fleet-root** file cited in a
commit message, not a lane path. That is a false positive for a lane-relative check, and the lane's
backtick+prefix grammar avoids it. It is also the honest boundary: tameshi's reach and the lane's
precision trade against each other on the same range.

---

## 6. Risks and contradictions (stated, not smoothed)

1. **The C2 predicate may be unreachable under the frozen grammar.** `M ≥ 20` cannot be met by
   backticked paths (0) plus `.log` filenames (7). If the executor implements the spec's literal
   grammar the counter prints `CAP_MESSAGE_TREE=fail` on a *correct* instrument; if it widens to
   bare tokens to clear 20 it lands on tameshi's arm 3. Either way the frozen `before → after`
   sentence ("every backticked repo-relative path and every `.log` filename") describes a grammar
   that this lane's history does not exercise. Reported as a defect against the frozen claim, not
   edited — `claims.md` is not this seat's to change.
2. **Two instruments, one range, opposite verdicts.** After C2 lands, tameshi's bind will read
   `findings=1` on `7fab03f..refs/heads/main` while the lane's instrument may read `misses=0`.
   That is defensible (different grammars, one fleet-root false positive) but must be **stated** in
   the C2 receipt, or the fleet reads a contradiction.
3. **`cell index 2` is a lane-format assumption.** Inserting a SCORECARD column silently re-points
   the SM6 rule. kaidoku's `cells[2]` has the same fragility and no sibling check catches it. The
   v3 rule as frozen does not fall back to a header name when one exists; that is a known limit of
   the claim, not a defect to fix inside this round.
4. **No shared home for fleet-level instruments.** `scripts/` at the fleet root holds no checker, so
   every lane that needs "cited thing must exist" re-implements it: 21 distinct paths in §2b–2c do
   the same predicate over different populations. That is the duplication this scan actually found —
   C1's is not part of it, C2's is.

---

## 7. The cross-lane pattern the fleet should adopt

Promote one **lane-agnostic citation-conformance instrument** out of the two existing owners —
tameshi's `receipt-commit-bind.py` (commit-message arm, git objects only, fail-closed on an empty
population) and this round's `message_tree_check.py` (prefix-unrestricted backtick extraction,
`.log` class, single `MESSAGE_TREE` contract, planted-miss leg in the counter) — and make it a
fleet-level tool that any lane runs against its own range rather than re-writes. The instrument
should declare its **citation grammar in one place**: a backticked repo-relative span class, a bare
basename class with an explicit extension list, and an explicit **exemption list for fleet-root
files** (`ufo-wave-policy.json`, `MANIFEST.json`, `.ufo/state/*`) so a lane-relative check does not
redden on a correctly-cited fleet artifact — the `ufo-wave-policy.json` finding in §5 is the
motivating instance. It should print one summary line, carry a `--selftest` with a planted-miss arm
plus a fleet-root-exemption arm, and refuse a vacuous range (exit 2). Lanes then **cite** it, with
the lane's own round-91 or tameshi's round-65 range as the non-synthetic red/green pair, and record
the adoption in `kama-shokunin/corpus/knowledge/cross-lane-scope.md` § Overlap rules, which is
already the fleet's register for exactly this kind of settlement (it names `receipt-commit-bind.py`
at `:126`). The rule of record: *a lane that needs message↔tree conformance runs the shared
instrument and reports its line; a lane that re-implements it must state which arm the shared
instrument cannot reach — otherwise the fleet owns N instruments with N-1 different verdicts on the
same commit range.*

---

## 8. Verification and limits

Run (this seat):

- `git -C revenger-shokunin log/show/cat-file/rev-parse` (read-only) for range, messages, counts.
- `python3 -I -B tameshi-shokunin/tools/receipt-commit-bind.py --repo <lane> --base 7fab03f --tip refs/heads/main`
  → exit 1, receipt `receipts/tameshi-bind-over-lane-range.log`. Interface and write surface read
  before running: git objects only, output to stdout, fixtures only under TMPDIR.
- Citation-grammar census over the range → `receipts/citation-grammar-census.log`.
- Header/code reads of the 27 paths in §2; `grep -rln` sweeps named in §1.

Not run, and therefore **not** claimed: any sibling's `--selftest`; tsukuroi's
`check-self-assessment.py` against this lane (its check set is tsukuroi-specific, so a run would
prove nothing about reuse); the round-91 instruments themselves (other seats own them; no
`message_tree_check.py` or `self_assessment_check3.py` existed at scan time); any mutation or
mutation-testing of a sibling. Sibling state is read at each lane's working tree / HEAD as found at
scan time and may differ at integration.

Limit of this scan, stated plainly: it reads sibling **code and registry rows**, not sibling
green/red state. A sibling instrument that is registered but currently failing is still counted as
ownership here.

Report: .ufo/waves/round-91/w1/ConnectorR91Overlap.md
