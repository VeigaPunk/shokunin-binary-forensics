# Routed debt — round 63 (falsify wave, attempt 1)

Seat: `revenger-r63.W2RoutedDebt` (scribe, calibration axis).
Date: 2026-10-24.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

Purpose: single reconciled table of every routed-debt item the round-63 **build
wave** reports hand to later rounds, with a per-item disposition
(**fixed-this-round** / **bounded-future** / **explicitly-unresolved**) and an
owner. This file feeds the round report's routed-debt section; it is a table of
debts, not a verdict on C1/C2/C3.

## Tip under attack

**Committed tip = `98ad3a0cb26c78b95f94535897b61c7a73113428`** ("round-63: final
measurement, SCORECARD and LOG; wave-2 receipts and falsify spec; all three claims
met at f6ea2932"), whose ancestry in this wave is
`aaa046326d92ba983f3ae99341438c9b8509a6cc` ("round-63: corrected C1 entry (wc-w
fix, S034/S035 citations, derived metadata), S034+S035 registry rows, LEDGER
receipt-pin fix, lesson Gate+M35 updates") → `db55bd6488e24e956df5818ae34c2a043d7ddc12`
("round-63: C1 candidate entry …, SOURCES S032+S033, round-63 lesson; README
still partial pending falsify wave").

The tip advanced **seven times while this seat was working**: `db55bd6` →
`aaa0463` → `3af3acb` → `34cfa24` → `f6c618b` → `f6ea293` → `98ad3a0`. Every row
below was re-verified against the tip, and once more at `98ad3a0` ("round-63:
final measurement, SCORECARD and LOG; wave-2 receipts and falsify spec; all three
claims met at f6ea2932"), the round's final integration commit. **That commit
lands `reports/round-63/measure-after.log` and `reports/round-63/final-verification.json`
as tracked files** (so D6 is discharged — see its row) and changes nothing else
this table asserts: the lesson line numbers (`:152`, `:237`, `:250`, `:220`,
`:295-301`), the entry's `:682` sentence, the entry's S-id census
(`S032 ×14 / S033 ×12 / S034 ×17 / S035 ×12`), the registry's 35 rows, the receipt
digest and its LEDGER pin, the LEDGER's padding wording, and the README's **C07**
row (still `frontier` — see D2) are all identical at `98ad3a0`.

The two commits after `98ad3a0` touch **only this table's own two files**
(`aaa1790`: `W2RoutedDebt.md`; `a6f5c42`: `routed-debt.md`), so every fact below
is unchanged by them; `98ad3a0` remains the last commit that changed the
corpus, the registry, the README or the round's receipts.

Because the tip moves, the row line numbers below are the ones **at `98ad3a0`**
(they are unchanged across `3af3acb` → `34cfa24` → `f6c618b` → `f6ea293` →
`98ad3a0` for every lesson line this table cites). The lane working tree carries
only this seat's own two files as modifications.
Where a row cites a build-wave report, that report is read at its committed
bytes (`2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e` for the build state; the
`aaa0463` commit later edited five of those reports, and the two variants are
called out where the line number differs).

**The build-wave commits are `2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e`** (build
state) and `54ab973c021cc62ca65dcbe2cbfabe3235d5ee38` (frozen contract); the
frozen contract is `reports/round-63/claims.md`, the frozen counter is
`reports/round-63/measure.py` (sha256 `3b7fba2d…`), and the red-before receipt
is `reports/round-63/measure-before.log`.

Disposition vocabulary (as assigned by this seat):

- **fixed-this-round** — the debt named in the build report is discharged by
  bytes that exist at the committed tip.
- **bounded-future** — not fixed here, but a *specific, bounded* later-round
  action is named and an owner is named; the debt is recorded, not open-ended.
- **explicitly-unresolved** — not fixed, no bounded later action and/or no
  owner was named in the source report; it stays open and is only *recorded*.

## Table

| # | Routed-debt item | Source pointer (verified) | State at tip `f6ea293` | Disposition | Owner |
|---|---|---|---|---|---|
| D1 | **M35 residual unguarded receipt conjunct** — the `stdout_sha256` conjunct of `receipt_ok()` is covered by no in-script forged-receipt control, so deleting it leaves the self-test green (undetectable from the script's own run). The build wave named **one** conjunct in `verify_icon_states.py`; the falsify wave widened it to **two** scripts. | `.ufo/waves/round-63/build/R63MutC3.md:174` (§5.5 M3), `:59` (M3 table row), `:205` (routed-debt statement), `:299-301` (summary); lesson mistake row `corpus/lessons/round-63.md:220`; lesson routed-debt row `corpus/lessons/round-63.md:299`. Falsify corroboration: `.ufo/waves/round-63/falsify/W2MutC3Final.md:18-19` (D1 named script, D2 icon script), `:420-422`; `.ufo/waves/round-63/falsify/W2ClaimsAdmission.md:120`. | **Still open at the tip, and the widening is committed.** `corpus/verify_icon_states.py:121` (`assert receipt.get('stdout_sha256', …) == sha(raw_bytes)`) and `corpus/verify_named_multi_icon_states.py:17` (`receipt['stdout_sha256']==H(raw)`) both carry the conjunct; the only in-script controls forge `fixture_sha256` (`verify_icon_states.py`, in `check_saved`) and `command` (`corpus/verify_named_multi_icon_states.py:77`). The verifier files are byte-unchanged between `db55bd6` and `aaa0463` (`git diff --stat db55bd6 aaa0463 -- corpus/verify_icon_states.py corpus/verify_named_multi_icon_states.py` → empty). The committed lesson's M35 row and routed-debt row now say **both** conjuncts are unguarded. The frozen C3 claim is **not** falsified by this (it names only the `command` and `fixture_sha256` mutants); the falsify wave confirmed the frozen 2/2 still holds and separately confirmed the debt mutants survive. | **bounded-future** — recorded as M35 in the committed lesson (`corpus/lessons/round-63.md:220`), captured-but-not-enforced (Q13 constrains *credit*, not the file). Named later-round action: widen the in-script forged-receipt controls to the `stdout_sha256` conjunct in **both** scripts. Owner: next round's revenger lane (L1 for that round). | next round's revenger L1 (calibration axis) |
| D2 | **C07 `frontier`-token legend staleness** — the README legend defines `frontier` as "no knowledge and no saved record"; once C2's firmware saved record lands, C07's status token `frontier` no longer matches the legend. | `.ufo/waves/round-63/build/R63ReadmeFlipDraft.md:126-132` (Observation for L1) and `:161-162` (finding F5). Independent falsify-side restatement: `.ufo/waves/round-63/falsify/W2VerifyReadmeContract.md:206-211` (finding F8). Legend text: `corpus/README.md:24`; C07 row: `corpus/README.md:36`. | **Live at the tip.** `corpus/live/runs/round-63/inspection.json` is committed (it landed in build commit `2a34e45`) and carries `operation = inspect_firmware_regions` (re-derived from the committed blob at `98ad3a0`), i.e. a saved firmware record now exists — so C07's `frontier` token contradicts the legend's own definition. `corpus/README.md:36` still reads `\| C07 \| firmware images \| — \| — \| frontier \|` at `98ad3a0` — the tip's C06 flip (`f6ea293`, `corpus/README.md:35` `partial` → `held`, naming the new entry) touched only C06, as claims.md requires.  The `## Frontier` prose at `corpus/README.md:63-67` also still says "an authored known-truth firmware fixture is the next probe", although that fixture is committed at `corpus/fixtures/firmware-r63/`. claims.md forbids any README status change other than C06 this round, so both are deliberately untouched — and the C06 flip has now landed, so the "any README status change other than C06" constraint for this round is discharged and cannot be re-litigated. | **bounded-future** — must not be fixed this round (claims.md void condition: "any README status change other than C06"). Bounded later action: a future round's claims author re-derives C07's status token against the legend (and the `## Frontier` prose against the committed fixture), or amends the legend wording. Owner: next round's revenger L1 (claims author) — *not* this round's flip seat. | next round's revenger L1 (claims author) |
| D3 | **`HOLDS_OK` contract-wording drift (D1)** — the frozen probe's `HOLDS_OK` is not the round-61 definition it claims to inherit; it adds `killed_b == 2`, `c3_controls == 2`, `fresh == 18`. | `.ufo/waves/round-63/build/R63SimplifierProbe.md:39` (D1 text) and `:14` (verdict: "MATCHES with one flagged drift (D1)"). Contract sentence: `reports/round-63/claims.md:97` — "`C2_*`/`HOLD_*`/`HOLDS_OK` (same definitions as the round-61 probe), and". Probe code: `reports/round-63/measure.py:179-181` vs `reports/round-61/measure.py:111`. Lesson routed-debt row `corpus/lessons/round-63.md:298`. | **Open, unfixed, and correctly so.** Re-derived by this seat: `reports/round-63/measure.py:179-181` computes `holds_ok = (controls == 2 and killed_d2 == 2 and c3_controls == 2 and killed_b == 2 and ok == len(names) and replay == len(results) and fresh == 18)`, while `reports/round-61/measure.py:111` computes `holds_ok = controls == 2 and killed_d2 == 2 and ok == len(names) and replay == len(results)` — three extra conjuncts, so claims.md:97 is strictly false for `HOLDS_OK` alone. Direction is strictly conservative (can only turn holds red). Both files are frozen (claims.md at `54ab973`, measure.py at pre-registration), so **neither may be edited this round**; both are byte-identical at `98ad3a0`. The committed `reports/round-63/measure-after.log` (commit `98ad3a0`) satisfies the *reading* discipline this row demands — it prints `C3_CONTROLS_PASS=2/2` and `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` as **separate lines** (lines 25–26) rather than leaning on `HOLDS_OK` — but it does not repair the wording drift, which lives in a frozen file. | **bounded-future** — recorded, not fixed; the disposition cell in the committed lesson states the binding gate is unchanged: the final committed `measure-after.log` must show the C3 controls passing **and** `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` as separate printed lines, because `HOLDS_OK` alone does not prove C3. Bounded later action: either the next contract's wording stops inheriting the r61 definition by name, or the probe is re-aligned to a named definition. Falsify-wave sharpening (not in the build report): `.ufo/waves/round-63/falsify/W2AttackProbeC3.md:144-150` (W2C3-2) shows `c3_controls` measures only "unmutated self-test exits zero" — it does **not** demonstrate that forged-receipt controls exist or ran, so `HOLDS_OK`/`C3_CONTROLS_PASS` must not be cited as control-presence evidence. | next round's revenger L1 (contract author) + the falsify-wave adjudicator that must read the printed C3 label, not `HOLDS_OK` |
| D4 | **S033-screen recording** — the decision to screen the Python `zipfile` docs **out** with no registry row, plus the forward id note it leaves behind for a future round that needs such a row. | Screen decision: `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:11` ("**Screened and excluded — NO S033 row.**") and `:251-256` (contingency closed, id note); sibling confirmation `.ufo/waves/round-63/build/R63SourcesRows.md:33` (decision confirmed), `:37`, `:58` ("Finding 5 (id space) is closed"); residual search-log observation `.ufo/waves/round-63/build/R63SourcesRows.md:60` and `.ufo/waves/round-63/build/sources-rows-review.md:127`, closed at `.ufo/waves/round-63/build/sources-rows-review.md:257`. Committed lesson `corpus/lessons/round-63.md:76-107` (Gate record of the screen, exclusion line verbatim, 19-word located quote), `:111` (S033 own-work row), `:145` (id allocation decided). | **The screen recording is discharged at the tip** — the Gate record is committed with URL, access date, snapshot digest and the ≤25-word located quote, and no registry row was written for the zipfile docs (its snapshot digest `9520a8cb…` appears in the Gate only, and `grep -rn "S036" corpus/ .ufo/waves/round-63/` → no hit). The **forward id note is now stale twice over**: `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:254-255` says a future zipfile-docs row "could no longer use S033; … the next unused id would be **S034**" — but `98ad3a0` has landed **S034** (APPNOTE local-file-header scope) and **S035** (saved round-2 archive ledger), so the next unused id is now **S036**. The ready-made row text for that future use is retained in `build/R63SourceZipfileDocs.md` §7. Separately, the committed lesson's own id-allocation paragraph (`corpus/lessons/round-63.md:148`, `:150`) still reads "**S032 ×10 / S033 ×5 / S034 ×0**" and "The round's ids are therefore the contiguous pair **S032 + S033 with no id skipped**", while the tip's entry now cites **S032 ×13 / S033 ×11 / S034 ×15 / S035 ×11** and `corpus/SOURCES.md` holds **35** rows ending at S035 — see D12. | **Split.** The screen decision itself is **fixed-this-round** (recorded verbatim in the committed lesson; no zipfile-docs row exists or is pending). The **id-note** portion is **bounded-future**: a future round needing a zipfile-docs row must take **S036**, not S034. Owner: next round's revenger source-opener seat (re-number on use, using the retained §7 text) + this round's L1 for the id-paragraph staleness in D12. | next round's revenger source-opener seat; this round's L1 for D12 |
| D5 | **Evidence-ID transplant corollary** — no committed check distinguishes a genuine Evidence ID from a *real foreign* Evidence ID transplanted across record+stdout+receipt with recomputed digests; and, at the ledger layer, nothing binds `LEDGER.md` to `inspection.json`. | `.ufo/waves/round-63/build/R63RevengerLedger.md:104` (transplant scenario, executed on copies), `:110` (result: `ORACLE OK`, exit 0), `:115-117` (no byte preimage; residual gap: `receipt.evidence_id == record.evidence_id` observed only manually), `:118` (corollary: nothing binds LEDGER.md to inspection.json), `:46` (no byte preimage for either ID). Independent falsify corroboration: `.ufo/waves/round-63/falsify/W2AttackRecordForgery.md:41` (Forgery A), `:57-61` (cross-row reconciliation is the only stopper — a process stopper, not an artifact check), `:126` ("would ever expose a transplant"). | **Split.** The **receipt-pin defect is now fixed at the tip**: `corpus/live/runs/round-63/LEDGER.md:26` at `98ad3a0` reads `…5c6b94d`, and `git show 98ad3a0:corpus/live/runs/round-63/receipt.json \| sha256sum` = `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` — the pin now matches the bytes (it was mis-keyed in the final hex char, `…5c6b94b`, at `db55bd6`; `.ufo/waves/round-63/falsify/W2AttackRecordForgery.md:77-99` located it). The **corollary itself remains unrecorded in the committed corpus**: `grep -c "transplant" corpus/lessons/round-63.md` = 0 and `grep -c "transplant" corpus/live/runs/round-63/LEDGER.md` = 0 at the tip; the lesson's routed-debt table (`corpus/lessons/round-63.md:295-301`) has no row for it. `measure.py` and `oracle_check.py` read neither the receipt nor the Evidence ID (`grep -n "receipt\|evidence_id" corpus/live/runs/round-63/oracle_check.py` → no hit). | **fixed-this-round** for the receipt pin (now correct at the tip). **explicitly-unresolved** for the transplant corollary: it is stated only in a build-wave report and a falsify-wave report; no committed artifact carries it, no bounded mechanism (no ledger digest, no byte preimage for an Evidence ID) is named, and no check would expose it. Owner: the falsify-wave adjudicator must state the corollary in the round report; a *mechanism* (ledger↔record binding, or a pin that covers the receipt's own bytes) is **not** named and is a candidate for the next round's claims — owner **unassigned**. | round report author (statement) / **unassigned** for the mechanism |

## Additional routed-debt rows the build wave handed over (same table, same vocabulary)

Present in the build reports' own routed-debt material and in the committed
lesson's `## Routed debt` table; listed so the round report's routed-debt section
does not drop them.

| # | Item | Source pointer (verified) | State at tip `f6ea293` | Disposition | Owner |
|---|---|---|---|---|---|
| D6 | **Round-62 closure defect (a)** — the on-tip probe re-verification output must be committed *alongside* the report claim, not only as a mid-round revision. | `corpus/lessons/round-62-verifier-spotcheck.md:63`; committed lesson row `corpus/lessons/round-63.md:297`; claims.md "Frontier and routed debt" section. |**Discharged at the final tip.** Commit `98ad3a0` ("round-63: final measurement, SCORECARD and LOG; wave-2 receipts and falsify spec; all three claims met at f6ea2932") lands `reports/round-63/measure-after.log` as a **tracked file** (`git ls-tree -r --name-only 98ad3a0 -- reports/round-63/` now lists `claims.md`, `final-verification.json`, `measure-after.log`, `measure-before.log`, `measure.py`), together with `reports/round-63/final-verification.json`. I read the committed log: it records `FINAL_TIP=f6ea293…`, `K_HELD=7/14 score=5.0`, `K_ROW C06 status=held`, `K_HELD_BACKED=7/14`, `F_COVERAGE=5/8 score=6.2`, `F_FAMILIES=[… firmware …]`, `FRESH_ROWS=18/18`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `PROBE_EXIT=0` — i.e. the on-tip re-verification output now sits in the same commit as the report claim, which is what the round-62 closure defect (a) required. **Caveat for the round report:** the log's `FINAL_TIP` is `f6ea293`, while the commit that carries it is `98ad3a0` — the measurement was taken on `f6ea293` (the commit that flips C06) and committed in the following commit, exactly the ordering the defect asked for; a reader who expects the log to name its own commit will find `f6ea293` instead, which is correct but worth stating.|**fixed-this-round** — the receipt exists, is tracked, and is committed alongside the round's final commit. Owner: closed.| this round's L1 |
| D7 | **Sibling scope on archives and firmware (ADJ-06 open)** — `kaidoku-shokunin` holds Core archive/package inventory and firmware-region extraction on vendor blobs; `tsukuroi-shokunin` ADJ-06 keeps "protocol integrator — kaidoku/revenger ownership unresolved" open. | `.ufo/waves/round-63/build/R63ConnectorOverlap.md:11` (the three unreduced sentences), `:29-33` (C06 contested item), `.ufo/waves/round-63/build/R63LessonDraft.md:88-96` (build-wave restatement: "the sibling scope on archives/firmware (ADJ-06 open, no province sentence edited)" — at build commit `2a34e45`; the same paragraph is at `:110-118` after the `aaa0463` edit of that report); committed lesson row `corpus/lessons/round-63.md:300`. | **Reported, not absorbed** — as recorded. No province sentence was edited; the C06 entry and the C2 record are scoped to this lane's own authored bytes. | **explicitly-unresolved** (deliberately reported-not-absorbed; no owner inside this lane can close a cross-lane ownership question). Owner: the fleet operator / `kaidoku-shokunin` + `tsukuroi-shokunin` L1s via ADJ-06. | fleet operator (ADJ-06), not revenger |
| D8 | **Outside spot-check for round 63** — a discernment sample by a seat outside this lane. | committed lesson row `corpus/lessons/round-63.md:301` ("not yet performed — the round's gate seats are this lane"); `build/R63LessonDraft.md` §Routed-debt. | Not performed; the lesson records no outside discernment verdict. | **explicitly-unresolved** — deferred to independent closure exactly as in round 62. Owner: the independent closure seat for round 63 (not this lane). | independent closure seat |
| D9 | **`C2_RECEIPT_B_KILLED_ATTRIBUTED` is printed but absent from `holds_ok`** — the probe's `holds_ok` uses raw `killed_b` instead of the *attributed* count, so `HOLDS_OK` does not certify the C2 attributed kills. | `.ufo/waves/round-63/build/R63CriticClaims.md:111` (frozen-obligation row) and `:116` (the most consequential operational mistake: conflating `HOLDS_OK`, the three printed targets, and the complete claim contract); `reports/round-63/measure.py:116` (attribution rule) and `:179-181` (`holds_ok`). | Open and unfixed (frozen files). The falsify wave re-confirmed the same shape from the other side: `.ufo/waves/round-63/falsify/W2AttackProbeC3.md:69` ("`HOLDS_OK=yes` does not imply the C3 target was met"); `.ufo/waves/round-63/falsify/W2AttackProbeF.md:7` and `:48` (a hand-written fabricated firmware record still prints `HOLDS_OK=yes`, exit 0). | **bounded-future** — the build report already names the smallest safe final check: require the separately printed `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` label rather than exit 0 / `HOLDS_OK`; the committed lesson's D3 disposition cell applies the same rule to the C3 label. Owner: this round's L1 for the final measurement + the next round's contract author for the probe. | this round's L1 (measurement discipline) + next round's contract author |
| D10 | **Search-log count convention for the own-work row** — the landed `## Search log` counts "identified 3 / screened 3 / included 1 row (S032) / excluded 2" while the round lands two registry rows (S032 + S033), the own-work bundle having no search-log unit of its own. | `.ufo/waves/round-63/build/R63SourcesRows.md:60` (residual observation, one remedy sentence); `.ufo/waves/round-63/build/sources-rows-review.md:127` (same observation with its remedy) and `:257` (L1's acceptance: "accepted as-is by L1 … no remedy clause is added"). Committed lesson `## Search log` ("Reconciliation, append-only" paragraph) records the divergence between the two seats verbatim. | **Closed as a non-blocker** — the seat's own re-review accepted the landed note as-is because the unit convention ("the lane's own authored fixture/record sets count once each") already covers the own-work row's absence from the "included" figure; the divergence is recorded in the lesson rather than smoothed. (The same note is now stretched further by D12: the round lands **four** registry rows, S032–S035.) | **fixed-this-round** (accepted-as-is, recorded in the lesson's search log). Owner: closed, with D12 as the residual. | closed (L1 accepted) |
| D11 | **LEDGER "zero padding" wording leak (L2)** — the U1 row said "zero padding" where the fixture has three all-zero padding spans. | `.ufo/waves/round-63/build/R63RevengerLedger.md:129-136` (leak L2, with the suggested one-word-class fix); the row itself is `corpus/live/runs/round-63/LEDGER.md:51`. | **Fixed at the tip.** The committed `corpus/live/runs/round-63/LEDGER.md:51` reads "This image contains only two zlib members and three all-zero padding spans (O6)" — verified on the committed blob at `98ad3a0`, matching the truth oracle's three padding spans (0–512, 591–1024, 1114–2048). The sibling leak L1 (receipt command rendered non-verbatim) was likewise already fixed in the final LEDGER (`.ufo/waves/round-63/build/R63RevengerLedger.md:137-140`; `corpus/live/runs/round-63/LEDGER.md:19` is byte-verbatim). | **fixed-this-round** — the one-word-class correction landed before the tip commit. (A separate residual inside the same document, **not** this leak: `corpus/live/runs/round-63/LEDGER.md:9` still says "explicit zero padding" in the scope sentence, which describes the fixture's construction rather than claiming a span count — recorded for completeness, not as a debt.) Owner: closed. | closed (ledger author) |
| D12 | **Lesson id-allocation paragraph vs the tip's registry** — *new item, surfaced by the tip moving under this seat, not by a build-wave report.* The lesson's id-allocation paragraph states "**S032 ×10 / S033 ×5 / S034 ×0**" (`corpus/lessons/round-63.md:148`) and "The round's ids are therefore the contiguous pair **S032 + S033 with no id skipped**" (`:150`), and its search-log note says "included **1** row (S032)" (`:237`), while the tip's entry cites **S032 ×14 / S033 ×12 / S034 ×17 / S035 ×12** and `corpus/SOURCES.md` holds **35** rows ending at S035 — while the lesson's own Gate paragraphs for S034 (`:111`) and S035 (`:123`) are present. Left unmarked this would have been an internal inconsistency: the lesson would describe two extra rows in its Gate while its id/count paragraph and search-log counts described the two-row world. **All three mismatched places now carry an explicit UPDATE marker at `98ad3a0`** (see the state cell), so the draft-time counts are retained as history rather than presented as current. | `corpus/lessons/round-63.md:111`, `:123`, `:148`, `:150`, `:237` (committed at `98ad3a0`); tip facts re-derived by this seat from `git show 98ad3a0:corpus/knowledge/round-63-zip-central-directory-evidence.md` (S-id census) and the seven-census commands of `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:71-81` run against `98ad3a0:corpus/SOURCES.md` (rows 35, malformed 0, tier A=33/C=2, status mined=30/queued=1/rejected=4, duplicate ids none, enum violations none, mined used-by paths missing none). Falsify-side prior art: `.ufo/waves/round-63/falsify/W2SpotcheckDiscern.md:228-238` (F4, integration hazard from the S034 row) and `.ufo/waves/round-63/falsify/W2SpotcheckDiscern.md:330` (F5, the entry's own "No third source is cited" sentence). |**Closed by the tip's own commits.** The registry is conforming (census clean) and the entry's citation set matches the rows. All three halves of the mismatch are discharged at `98ad3a0`: (i) the entry's own false sentence is fixed — entry `:682` reads "- No fifth source is cited: S032, S033, S034 and S035 above are this entry's complete registry basis." (it read "No third source is cited." at `db55bd6`/`aaa0463`, flagged by `.ufo/waves/round-63/falsify/W2AttackEntryQ11.md:299` and `.ufo/waves/round-63/falsify/W2ClaimsAdmission.md:185`); (ii) the lesson's id-allocation paragraph carries an UPDATE marker (`:152-157`: "two further rows landed after this paragraph was drafted — S034 … and S035 …; the registry ids are now the contiguous block S032–S035, and this paragraph is retained un-rewritten as the draft-time record with this marker appended"); (iii) the lesson's search-log counts carry their own UPDATE marker (`:250`: "two further rows, S034 and S035, were appended after the Q01 attack showed the entry needs a local-header-layout scope and a ledger provenance row; the round's registry total is four rows (S032, S033, S034, S035) — logged here per the append-only rule rather than rewriting the counts above"). The same commit `34cfa24` adds the S033/S035 located quotes required by SOURCES contract rule 1 and corrects the §4.4.7 snapshot line reference to 913–914. The lesson's draft-time count sentence is deliberately *retained* rather than rewritten, per the append-only rule — the markers are the record.|**fixed-this-round** — all three halves are discharged at the tip by the round's own integration commits (`aaa0463` / `3af3acb` / `34cfa24` / `f6c618b` / `f6ea293` / `98ad3a0`). Owner: closed.| this round's L1 (before the final commit) |
| D13 | **The falsify wave's own new integration hazard** — *new item, surfaced by the tip moving under this seat.* The integration commits `aaa0463`, `3af3acb`, `34cfa24`, `f6c618b`, `f6ea293` and `98ad3a0` changed the committed entry (87 + 6 + 4 + 4 lines), the registry, the README's C06 status and the round's measurement receipts while the falsify wave's own Q01/Q11 seats had pinned the pre-correction entry bytes; several falsify findings were stated against `db55bd6` and are now stated against different bytes. | `.ufo/waves/round-63/falsify/W2SpotcheckDiscern.md:228-238` (F4: an S034 row the entry did not cite — now it does), `:330` (F5: "No third source is cited" — now fixed at the tip); `.ufo/waves/round-63/falsify/W2AttackEntryQ11.md:299` (entry:682 said "No third source is cited" at the measured tip; fixed by `3af3acb`); `.ufo/waves/round-63/falsify/W2ClaimsAdmission.md:185` (same). | **Open for adjudication.** The tip moved **seven times** during the falsify wave (`db55bd6` → `aaa0463` → `3af3acb` → `34cfa24` → `f6c618b` → `f6ea293` → `98ad3a0`); the falsify seats' byte-pinned findings must be re-anchored to the final tip's bytes (or state the commit they were measured on) before they are used as admission evidence. One instance is already visible: F5 and the entry:682 "No third source" defect were measured on `db55bd6`/`aaa0463` and were **fixed by `3af3acb`** (entry `:682` now reads "No fifth source is cited: S032, S033, S034 and S035 above are this entry's complete registry basis"). | **bounded-future** — bounded action: re-read each falsify finding against `98ad3a0` bytes (or state the commit it was measured on) and adjudicate against the final tip. Owner: the falsify-wave adjudicator / L1 at the final commit. | falsify-wave adjudicator + L1 |

## Pointer-existence verification (every pointer cited above)

Each pointer was opened and read; the quoted cell text is the line actually
present at that path:line, re-read at tip `f6ea293` where the file changed
during this seat's run. Verified non-empty and on-topic —
`.ufo/waves/round-63/build/R63MutC3.md:174`, `:59`, `:205`, `:299-301`; `.ufo/waves/round-63/build/R63ReadmeFlipDraft.md:126`, `:161`;
`.ufo/waves/round-63/build/R63SimplifierProbe.md:14`, `:39`; `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:11`, `:251-256`;
`.ufo/waves/round-63/build/R63SourcesRows.md:33`, `:37`, `:58`, `:60`; `.ufo/waves/round-63/build/sources-rows-review.md:127`, `:257`;
`.ufo/waves/round-63/build/R63RevengerLedger.md:46`, `:104`, `:110`, `:115-118`, `:129-140`; `.ufo/waves/round-63/build/R63ConnectorOverlap.md:11`;
`.ufo/waves/round-63/build/R63CriticClaims.md:111`, `:116`; `.ufo/waves/round-63/build/R63LessonDraft.md:88-96` (and `:110-118` at the post-`aaa0463` revision of that report);
`corpus/lessons/round-63.md:76-107`, `:111`, `:123`, `:145`, `:148`, `:150`, `:215`, `:232`, `:290-296`;
`corpus/lessons/round-62-verifier-spotcheck.md:63`;
`corpus/README.md:24`, `:36`, `:63-67`; `corpus/SOURCES.md:46-49`;
`corpus/knowledge/round-63-zip-central-directory-evidence.md:664-684`, `:682`, `:722`;
`corpus/live/runs/round-63/LEDGER.md:9`, `:19`, `:26`, `:51`;
`corpus/verify_icon_states.py:121`; `corpus/verify_named_multi_icon_states.py:17`, `:77`;
`corpus/live/runs/round-63/oracle_check.py:15-39`;
`reports/round-63/claims.md:97`; `reports/round-63/measure.py:116`, `:179-181`;
`reports/round-61/measure.py:111`;
`.ufo/waves/round-63/falsify/W2MutC3Final.md:18-19`, `:420-422`; `.ufo/waves/round-63/falsify/W2ClaimsAdmission.md:120`, `:151`, `:185`;
`.ufo/waves/round-63/falsify/W2AttackRecordForgery.md:41`, `:57-61`, `:77`, `:126`;
`.ufo/waves/round-63/falsify/W2AttackProbeC3.md:69`, `:144-150`; `.ufo/waves/round-63/falsify/W2AttackProbeF.md:7`, `:48`;
`.ufo/waves/round-63/falsify/W2VerifyReadmeContract.md:206-211`; `.ufo/waves/round-63/falsify/W2SpotcheckDiscern.md:228-238`, `:330`;
`.ufo/waves/round-63/falsify/W2RerunAllCounters.md:350`; `.ufo/waves/round-63/falsify/W2AttackEntryQ11.md:299`.

**Absent-by-design pointers (recorded, not failed):**

- `reports/round-63/measure-after.log` — **does not exist** at `98ad3a0` (see D6).
  It is a future commit, not a missing file to cite.
- `S036` — no **registry row or build/falsify report** mentions it
  (`git show 98ad3a0:corpus/SOURCES.md | grep -c "S036"` → 0; the only hits for
  `S036` anywhere under `corpus/` and `.ufo/waves/round-63/` are in this seat's
  own two files, which name it as the next unused id). That absence *is* the D4
  finding.
- `corpus/knowledge/round-63-zip-central-directory-evidence.md` exists at the tip
  but is attacked by the falsify wave's Q01/Q11 seats; this table cites it only
  for the S-id census and the "No third source" sentence (D12).

## Cross-check against the committed lesson's own routed-debt table

The committed lesson (`corpus/lessons/round-63.md:295-301`) carries five rows:
(a) round-62 closure defect → D6; `HOLDS_OK` wording drift → D3; residual
unguarded `stdout_sha256` conjunct → D1; sibling scope ADJ-06 → D7; outside
spot-check → D8. **Two of the five items this seat was asked to reconcile — the
C07 legend staleness (D2) and the evidence-ID transplant corollary (D5) — have
no row in the committed lesson's routed-debt table**, and neither is recorded
anywhere in the committed corpus (verified at `98ad3a0`: `grep -c "C07" corpus/lessons/round-63.md` = 0;
`grep -c -i "transplant\|preimage" corpus/lessons/round-63.md` = 0). They exist
only in build-wave and falsify-wave reports. The round report's routed-debt
section must therefore carry D2 and D5 explicitly, or they drop out of the round
record entirely.

## Notes for the round report author

1. **Do not let `HOLDS_OK` stand in for a target.** The build wave
   (`.ufo/waves/round-63/build/R63CriticClaims.md:116`) and the falsify wave
   (`.ufo/waves/round-63/falsify/W2AttackProbeC3.md:69`, `.ufo/waves/round-63/falsify/W2AttackProbeF.md:7-48`) agree: a
   green hold is not a claim. Read the printed `C3_RECEIPT_KILLED_ATTRIBUTED`
   and `C2_RECEIPT_B_KILLED_ATTRIBUTED` lines, and check the on-tip
   `measure-after.log` (D6).
2. **D1 is not a C3 falsification.** The frozen C3 mutants are killed; the
   unguarded conjuncts are a *coverage* debt in the lesson's own words
   (`corpus/lessons/round-63.md:220`).
3. **D4's id note moved twice.** A future zipfile-docs row takes **S036**; the
   retained §7 row text in `build/R63SourceZipfileDocs.md` is the template. The
   round's own id narrative is now stale at the tip (D12) — quote the registry
   census, not the lesson's counts.
4. **D5's mechanism is unassigned.** The corollary can be *stated* in the round
   report, but no bounded later action is named for closing it; if the round
   report is to carry it as debt rather than as a note, it needs an owner.
5. **The tip moved seven times during this wave** (`db55bd6` → `aaa0463` →
   `3af3acb` → `34cfa24` → `f6c618b` → `f6ea293` → `98ad3a0`). Re-anchor falsify findings to the final commit
   before using them as admission evidence (D13). D12's narrative-count
   mismatch was itself fixed by the tip's own commits, so the lesson's
   draft-time counts are now marked rather than current — quote the registry
   census, not the lesson's numbers.

## Method and limits

- Everything above was read from the lane's committed bytes at `98ad3a0` (with
  the build-wave reports at their committed bytes, `2a34e45`) plus the falsify
  reports as they existed on disk. The lane's *uncommitted* working tree is
  cited only where explicitly marked (D12), never as committed fact. Nothing was inferred from a report's own
  assertion: each pointer was opened and the cited cell re-derived where it was
  a digest, a count, or a code path (`sha256sum` on the committed receipt blob;
  `sed -n` on `reports/round-63/measure.py:179-181` vs `reports/round-61/measure.py:111`;
  `grep -o "S03[0-9]"` on the committed entry; the seven SOURCES census commands
  from `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
  run against the committed registry).
- No product code, judge, contract, counter, manifest, spec or registry file
  was edited; no git/jj mutation, no commit, no push, no publish, no deploy; no
  target was executed; no other runtime invoked. The only file written is this
  table plus the seat report.
- No tool was installed or upgraded (no pacman — the host pacman gate is paused
  host-wide; no `uv tool`, no `npx`, no binary download). Only read-only shell
  (`git`, `grep`, `sed`, `awk`, `sha256sum`) and the already-present Python 3
  standard library were used.
- Scratch: `/tmp/revenger-r63-routeddebt/` (one small row-extraction helper and
  one committed-registry snapshot for the census), removed after this report
  lands.
- Limits: the falsify wave's sibling seats were still writing when this table
  was compiled; rows D1–D13 cite only falsify reports that existed on disk at
  read time, and a later falsify finding that supersedes one of them would
  supersede the corresponding row here. The C07 legend-staleness row (D2)
  asserts staleness *by the legend's own definition*; it does not assert that
  the legend is the contract's wording (it is `corpus/README.md`'s). D12 and
  D13 are this seat's own findings, not build-wave handovers — they are marked
  as such and kept out of the build-wave rows.
