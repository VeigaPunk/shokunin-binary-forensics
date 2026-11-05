# ReviewerClaims — round 98 w1 attack findings on the frozen claims

Seat: ReviewerClaims (reviewer). Claims freeze: `9d49002a3804de48d365b7d32849ada06745d64f`
(lane HEAD at review time; working tree clean except untracked `.ufo/waves/round-98/`).
Attacked: `reports/round-98/claims.md` + `reports/round-98/controls/` as frozen.
Scratch: `/fast/scratch/hyaku/revenger-r98/ReviewerClaims/` (deleted after receipts were copied
into `.ufo/waves/round-98/w1/ReviewerClaims/`). No landing tree was built or scored; no frozen
bytes edited; git used read-only only. No tools installed (none needed); no pacman transactions.
Note on tooling: no `lsp` device is mounted in this session, so all caller/definition checks used
literal text grep + byte reads; no semantic server evidence is claimed anywhere below.

## 0. Recounts and verifications that PASSED (attack item 5, plus digest/receipt chain)

All commands run from the lane root.

- Vote-binding digest, recomputed from the freeze commit's entry bytes with the exact v6 `digest()`
  rule (`re.sub(r"(?im)^\s*admission-status\s*:.*$", "admission-status: candidate", t)`):
  `git show 9d49002a…:corpus/knowledge/round-98-rea-host-readiness.md | python3 -c …sha256…`
  → `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8` — **matches** the claims.
- Do-nothing receipt: `grep -c 'ACCEPTED-by-v5' reports/round-98/controls/c2-do-nothing-v6-holdout.log`
  → **5**; per-vector rc lines: FR00 rc=0 pass; FR02/FR08/FR09/FR10/FR12 rc=0 pass (the accepted
  five, exactly the routed five); FR01/03/04/05/06/07/11 and the three -unsigned variants rc=1
  refused; line 17 `BUILD_OK=True vectors=15 accepted=5` — matches the claims' "Before".
- Base row-status: `reports/round-98/controls/c1-base-rowstatus.log` lists C01–C15: C05
  `uncovered`, C14 `partial`, 13 `held`, and its own summary line says `13 held / 1 partial /
  1 uncovered` — matches the claims' Before (K 13/15).
- S506 receipt chain: `S506.receipt.json` fetched_at=2026-11-05, http 200, host
  raw.githubusercontent.com, quote span 7126–7202; `sha256sum reports/round-98/quote-receipts/raw/S506.body`
  → `ce2d122b…2282e50`, 16650 bytes — matches the receipt, the SOURCES S506 row, and the entry's
  derivation-table row. `fetch-log.md` has one `- S506 GET … sha256 ce2d122b…` bullet (satisfies the
  v6-style fetch-log line rule).
- Wave registry: on-disk `.ufo/waves/round-98/w1/swarm-registry.json` member→role map equals the
  c14 pinned seat map in the interface contract exactly (12 members, roles executor×3, scout,
  scribe, connector, reviewer×3, critic, mutation-tester, sentinel). It is **untracked**; the L1
  must commit it (with `reports/round-98/votes/*.json`) before the landing run, since the c14
  profile's registry/votes legs read them from the tree.
- S507 own-work pointer: `corpus/live/runs/round-98/` exists at the freeze commit with the three
  record files the entry names. S506/S507 used-by cells are grounded (audit below). The r98 entry
  cites S506/S507, header `admission-status: candidate` is at line 6 (inside any head window), and
  `verified-at: 2026-11-05` = ROUND_DATE.
- Do-nothing / junk-row reachability (attack item 1): **no hole found.** The freeze tree fails the
  c14 target via `C1_K_HELD_BACKED` (13/15; v6's held-back rule = status held AND every knowledge
  cell file exists, `c1_k_admit_counter6.py:605-610`) and via `C1_ADMITTED` (entry is candidate).
  The junk-row tree (only the C14 status cell → held) reaches K=14/15 but still fails
  `C1_ADMITTED`; a degenerate counter that printed only the K line would pass junk-row and be
  caught by the control kill rule. Both controls are sound under the predicate as written.

## Findings

### F1 [HIGH][BINDING before v7 freeze] The C2 "positive control on the real tree" is unreachable: the c02 profile reads the C14 row that C1 must flip (attack item 3 — answer: YES, coupled)

`claims.md` C2: *"Positive control on the real tree (reported): v7 `--profile c02` on the landing
archive must print `C1_VERDICT=pass`."* But the c02 profile keeps every v6 constant, and v6's
`C1_ONLY_C02` leg (`c1_k_admit_counter6.py:519-529`) passes **only** when the target row is the
*only* README row differing from the frozen base (`base_readme()` archives `FREEZE_REV`):
`legs["C1_ONLY_C02"] = (not diffs and … baserows.get(TARGET_ROW) != _raw_line(readme, TARGET_ROW))`.
On the round-98 landing tree the C14 row *must* differ (C1's own "Surface moved"), and C14 ≠
TARGET_ROW (C02) under every candidate base (`2875b9c9`, `34c56f9`, `9d49002a`) → `diffs={C14}` →
leg fails → the frozen sentence *"must print C1_VERDICT=pass, so C02 stays held"* can never be
true; the round is forced to report "harm to C02" even when C02 is untouched and healthy. The
claims' separability sentence ("the c02 profile … do[es] not read the C14 row or entry") holds for
the synthetic holdout trees but is false for this reported real-tree control.

Evidence: v6 leg semantics cited above; claims.md "Surface moved" (C14 row change is mandatory);
`git show 9d49002a…:corpus/README.md | grep '^| C14'` →
`| C14 | host readiness for REA routes | knowledge/2026-10-12-rea-readiness-checklist.md … | partial |`
(the landing changes exactly this line; no frozen base makes it equal to the base AND the C02 row
differ from it).

Proposed amendment (L1 picks one before the v7 freeze):
(a) drop the real-tree c02 positive control and rely on `C2_POSITIVE` (FR00) for the c02 side; or
(b) scope the c02 `C1_ONLY_TARGET` comparison to "every row other than the profile target and the
round's coverage target (C14) byte-identical to the claims-freeze README"; or
(c) re-word the control to "must print `C1_VERDICT=pass` **or fail only on legs that name C14**"
and require the failing-leg list to be recorded. (a) is cheapest and touches no frozen target.

### F2 [HIGH][BINDING before v7 freeze] `C1_USEDBY_GROUNDED` has no pinned scope; the registry carries 47 ungrounded used-by cells (36 rows), so any global implementation fails both profiles; the S505 fix's new value must be pinned to `—` (attack items 1 and 3)

The claims define the leg only as "shown able to fail on the base registry" (S505). My audit of the
freeze tree (`usedby_audit.py`, copied to my wave dir; rule: a used-by cell naming
`knowledge/<f>.md` is grounded iff `corpus/knowledge/<f>.md` exists and its bytes contain the row
id) gives:

- `python3 usedby_audit.py <freeze-root>` → `checked=564 ungrounded=47`; ungrounded rows:
  `S445 S446 S447 S449 S450 S452 S454–S482 S505` (36 rows; 47 cells).
- Same audit on the r97 synthetic base `2875b9c9:corpus` → `checked=558 ungrounded=46`
  (the c02 holdout trees inherit these rows).

So a "global" `C1_USEDBY_GROUNDED` makes C1 fail on the landing tree and makes `C2_POSITIVE` fail
on FR00 — both frozen targets unreachable. The leg must be scoped to the profile's row set
(c14: S505/S506/S507 — c02: S502–S504) or to "rows introduced this round"; nothing frozen says so.
Additionally, the S505 correction target value is unpinned: the r96 entry does not cite S505
(`grep -c S505 corpus/knowledge/round-96-native-analysis-sessions.md` → 0) and the r98 entry does
not either (full read), so the only grounded fix is used-by → `—` (empty). If the executor instead
"corrects" the cell to name an entry, the leg fails on the landing tree and C1 is not verified.
Editing the r96 entry to add an S505 token is not an option: it would break the frozen r96 votes'
digest binding read by the c02 profile.

Proposed amendment text: *"C1_USEDBY_GROUNDED: for each registry row in the profile's row set
(c14: S505, S506, S507; c02: S502–S504), if the used-by cell names an entry path, the named entry's
committed bytes must cite the row id; the leg must not scan other rows. The S505 correction is
used-by `… → —` (captured-by: none), logged old→new."*

### F3 [MEDIUM][BINDING decision before v7 freeze] C2's 0/5 forces a fixture-shaped FR10 refusal: FR00 and FR10 are byte-identical in every note field, and the r98 PASS-note rule must not be applied to the c02 profile (attack item 2 — C2_POSITIVE alone is NOT sufficient, and the honest fixture's PASS notes are boilerplate)

The c02 honest fixture's votes are synthesized by the frozen builder with
`notes[q] = NA_BY_Q["Q01"] if q == "Q01" else NA_NOTE` for **all** Qs — including the PASS rows
(`build_fresh.py`, `_fixture`). FR10 flips ReviewerGate Q09 PASS→n/a and keeps the same shared
`NA_NOTE`. Therefore FR00 and FR10 contain the identical `(seat, q, note)` triple at Q09 and differ
only in the decision bit; **no rule over note content can refuse FR10 without refusing FR00.**
Consequences the claims do not state:
- The wave contract's vote rule ("a PASS note: your own specific evidence, never boilerplate")
  can only be enforced in the c14 profile; applied to c02 it fails FR00 (`C2_POSITIVE=fail`).
- The only principled FR10 separator I found is **inter-seat PASS-set consistency** (all three
  fixture seats share the identical decision map; FR10 breaks it). Otherwise FR10 can only be
  refused by pinning the honest decision map — dev-set memorization, which nothing frozen detects
  (see F4).
My rebuild of the vectors under frozen v6 (see F5) confirms FR00 pass / FR10 accepted-by-v6 today.

Proposed amendment text: *"C1_VOTE_NOTES enforces the PASS-note rule only in the c14 profile; in
the c02 profile the leg checks n/a-note form plus inter-seat PASS-set consistency, and the L1's
v7-freeze commit message names the mechanism that refuses FR10."*

### F4 [MEDIUM][recommended-binding] C2 cannot distinguish calibration from memorization: the positive fixture is deterministic and public (attack item 2)

`_fixture()` builds FR00 deterministically (fixed archive `2875b9c9` + fixed synthetic bodies/
votes/entry overlay), so the honest tree's bytes are reproducible by any implementer. A v7 that
passes **only** a byte-match of that fixture satisfies `C2_ACCEPTED=0/5` + `C2_POSITIVE=pass` +
`C2_STUB_SELFTEST=ok` + both `C2_ROWSET_*` lines (a refuse-everything-else counter refuses FR06/07
with all legs failing, which still prints `C1_ROWSET` in the leg list, satisfying the kill rule).
`C2_STUB_SELFTEST` proves harness wiring only. The fresh r98 holdout is (i) not part of the target
and (ii) forgery-shaped, so it cannot catch a fixture-hash stub either. As frozen, the calibration
claim's evidentiary value is exactly "dev-set + one known tree".

Proposed amendment text: *"C2_POSITIVE runs on two honest trees: the FR00 fixture and a second
honest variant disclosed only at scoring time (e.g., the FR00 tree plus one benign added file under
`reports/round-96/`), both required to print `C1_VERDICT=pass`."* This adds no counter change and
can be applied by the harness at scoring time; the claims' kill rule would need one extra clause.

### F5 [MEDIUM][non-binding, record in the round report] The frozen do-nothing receipt is not re-derivable from the cited recipe: the cited builder's default counter is v5, which accepts 8/15 today; the receipt matches a v6-driven run (attack items 5 and 6)

`.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py` hardcodes
`COUNTER = LANE / "reports/round-96/c1_k_admit_counter5.py"` and labels acceptances
`ACCEPTED-by-v5` regardless of the counter driven. I rebuilt all 16 vectors twice in scratch from
an unmodified copy and from a copy whose single patched line pointed COUNTER at frozen v6:

- v5 (unmodified copy): `BUILD_OK=True vectors=15 accepted=8` — FR02, **FR06, FR07**, FR08, FR09,
  FR10, **FR11**, FR12 accepted (tables: `ReviewerClaims/rb5-table.txt`).
- v6 (one-line patched copy): `BUILD_OK=True vectors=15 accepted=5` — exactly FR02/08/09/10/12;
  FR06/07 refused via `C1_ADMITTED_UNION`, FR11 via `C1_SOURCES` — **byte-for-byte the frozen
  receipt's outcome column** (tables: `ReviewerClaims/rb6-table.txt`).

So the claims' "Before (frozen v6): accepted = 5/5" is **correct and independently reproduced**,
but a closure that re-runs the cited builder unpatched gets accepted=8 and would misread the frozen
receipt as irreproducible. Proposed fix (documentation, not a claims edit): one sentence where the
round report cites the receipt — *"receipt produced with the builder's COUNTER pointed at
`reports/round-97/c1_k_admit_counter6.py`; the committed builder default drives v5 and yields
accepted=8."* ExecHarness7 must likewise not reuse the builder's `main()` unmodified.

### F6 [LOW][recommended before v7 freeze] Predicate/contract wording gaps a closure cannot re-derive (attack item 4)

- The rename `C1_ONLY_C02` → `C1_ONLY_TARGET` exists only in the wave interface contract, not in
  claims.md's predicate sentence ("every v6 leg retargeted to C14").
- The c14 profile's constants (pinned seat map, FREEZE_REV `9d49002a`, HELD_TARGET 14, votes/receipts/
  registry paths, `NEW_ROW_IDS=S506,S507`, `RECEIPT_ROW_IDS=S506`) live only in the wave contract;
  the claims' "the same in the counter" sentence is not self-contained.
- Printed leg names for retargeted v6 legs under c14 (e.g. whether `C1_C02_HELD` becomes
  `C1_TARGET_HELD`) are specified nowhere; the kill rule keys only on `C1_VERDICT` and the K line,
  so this is ambiguity, not breakage.
Proposed amendment: one clause in the C1 predicate — *"leg names and profile constants are as
pinned in the wave interface contract, which is normative."*

### F7 [LOW][non-binding] Vacuous-retarget risk in `C1_DERIV_TABLE` (attack item 6)

v6's `C1_DERIV_TABLE` enforces r96-shaped rules (FG15: derivation rows keyed by Q01–Q17 tokens;
FG11: a hardcoded `pe-r75` fixture digest check). The r98 entry's derivation table is keyed by
value names, not Q tokens, so a mechanical retarget is vacuously true on the landing tree — the
leg prints pass while checking nothing r98-specific. Since the r98 entry is digest-heavy, propose
the retarget require the table's recorded digests (record files, S506 body, fixture.zip) to be
recomputed from the named commands. This is an implementation requirement, not a claims change.

## Residual risk and verification gaps

- No v7 bytes exist yet (`.ufo/waves/round-98/w1/` contains only the untracked registry), so F1–F4
  are spec-level findings; they bind ExecCounterV7/ExecHarness7/ExecControls and the L1's freeze
  decision, and MutationR98 should derive its deltas from F2/F3.
- The c02 coupling list (F1) covers the legs v6 actually has; any additional c02-visible leg the
  implementer adds could add coupling — the harness should print the failing-leg list on the
  real-tree c02 run to keep the harm report diagnostic.
- I did not run `forge_reach7.py` (does not exist yet) nor any landing tree, per seat bounds.
- The untracked wave registry must be committed by the L1 before the landing run (§0).

## Receipts (copied into `.ufo/waves/round-98/w1/ReviewerClaims/`)

`usedby_audit.py` (sha256-prefix 63e51ab752720cb9), `rb5-table.txt`, `rb5-counter5-results.json`,
`rb6-table.txt`, `rb6-counter6-results.json`. Scratch `/fast/scratch/hyaku/revenger-r98/ReviewerClaims/`
deleted after copying.
