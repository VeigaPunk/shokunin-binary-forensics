# round-66 lesson — revenger

author: L1 revenger-r66 (attempt 1)
date: 2026-10-24
claims: C1 (coverage, README C05 adjudicated disposition per the round-65 frozen order), C2 (calibration, new criterion C6 — exit_code and fixture_sha256 receipt guards)
claim base: 8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0 · pre-registration: reports/round-66/claims.md at 16b9387b (counter + red-before committed in the same revision)

## Gate — source rows opened this round

Every new row below was opened this round by the L1. The two superseding rows re-open the round-65 committed snapshots (no new network fetch); S042 is the orchestrator-dispatched wave corpus read in full as the adjudication authority.

- S042 — round-65 dispatched wave finding corpus, `.ufo/waves/round-65/` (64 seat reports over the committed candidate tree) — opened 2026-10-24 (each report read; the three gate FAILs re-verified by command, below). Located quote (≤25 words), `R65ReviewEntryQ11.md:1`: "FAIL (Q11) — item 3's `member[META-INF/MANIFEST.MF]` output line in the entry is not what its stated deriving command prints" (22 words).
- S043 — supersedes S039 — re-opened `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` (sha256 `412d9cb4…874c`, matches the row) — opened 2026-10-24. Located quote, snapshot lines 7-8: "Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence." (17 words). S039 cited "line 5"; line 5 is `older server.`.
- S044 — supersedes S040 — re-opened `.ufo/waves/round-65/source-snapshots/zipfile-docs.html` (sha256 `e7fe6715…c6a`, matches the row) — opened 2026-10-24. Located quote, `<title>` element: "zipfile — Work with ZIP archives — Python 3.15.1 documentation" (11 words). S040 titled the same bytes "3.15.0".

Census old→new: rows 41 → 44 (+S042 mined own-work, +S043 queued supersedes S039, +S044 queued supersedes S040). `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` exit 0 at round end; the same four disclosed W04s (S024/S028/S029/S034). No pre-existing row's status/recheck/used-by changed. `## Search log` gained the retro round-65 note (R65ReviewSources F3) and this round's note.

## Gate — round-65 C05 adjudication (the frozen order's step 3)

The orchestrator-dispatched 64-seat wave (spec `.ufo/waves/round-65/wave-spec.json`, 64/64 reports delivered, zero dead, committed as evidence this round) ruled on the candidate `corpus/knowledge/round-65-apk-axml-byte-evidence.md`. Named fresh-seat decisions, re-verified by this L1 against committed bytes at `8214e4dd`:

| criterion | decision | seat report | L1 re-verification |
|---|---|---|---|
| Q01 | PASS | R65ReviewEntryQ01 | consistent — tier-A rows cover load-bearing claims; two non-load-bearing citation defects recorded |
| Q02 | **FAIL** | R65ReviewEntryQ02 | re-run: snapshot line 5 is `older server.`, quote at line 7; `RES_XML_RESOURCE_MAP_TYPE` at ResourceTypes.h:253 (outside cited :239-250); entry:41 not the recheck output |
| Q03 | PASS | R65ReviewEntryQ03 | consistent — expected values byte-derived or externally pinned |
| Q04 | PASS | R65ReviewEntryQ04 | consistent — manual analysis labeled manual; the one tool claim is credited to S039's documented scope |
| Q05 | PASS | R65ReviewEntryQ05 | consistent — no readiness/capability claim |
| Q06 | **FAIL** | R65ReviewEntryQ06 | re-run: `python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'` prints `payload_first16_hex 4d616e69666573742d56657273696f6e`; entry:41 records `4d616e696673742d56657273696f6e` — a quoted premise that does not reproduce |
| Q07 | PASS | R65ReviewEntryQ07 | consistent — no parser prediction is made |
| Q08 | superseded by Q11 | QUALITY.md:23 | — |
| Q09 | PASS | R65ReviewEntryQ09 | consistent — 16/16 digest instances re-derived by the seat |
| Q10 | PASS | R65ReviewEntryQ10 | consistent — fixture/operation/pin fencing holds; ADJ-06 reported-not-absorbed |
| Q11 | **FAIL** | R65ReviewEntryQ11 | re-run: full-stdout diff shows exactly one diff — line 41 (15-byte `Manifst-Version` hex vs 16-byte `Manifest-Version`) |
| Q12 | PASS (correctly n/a) | R65ReviewEntryQ12 | consistent — entry writes no rejected row |
| Q13 | PASS | R65ReviewEntryQ13 | consistent — no verifier is credited; recheck is the entry's own readout |

Outside-discernment spot-check (LEARNING.md): `R65SpotcheckDiscern` — **REJECT** the candidate at its current bytes (Q11, entry:41; one corrected line + re-run clears it); **AGREE** the two retained round-61 rejected candidates stay rejected. Corroborating off-criterion FAILs: R65MutEntry (the pristine entry misquotes the same field), R65CriticEntryDeps (item-8 provenance over-claim + two silent value dependencies), R65EntryQmapDraft (dangling `### Code`/stdout pointers), R65ReviewSourcesTier (S038 cited outside its declared scope at entry:71/:126; item-9 dex semantics on no registry row).

**Decision: C1 of round 65 is FALSIFIED.** Per `reports/round-65/claims.md:110-123` step 3 the C05 row flips `frontier → uncovered`; the candidate is marked `admission-status: rejected` and retained as evidence (fixture/oracle/readout bytes untouched — every value except the transcribed line re-derives). The flip and this Gate record land in the same revision.

## Gate — admission decisions

- C1 (coverage disposition): LANDED per the frozen order's falsification branch. `corpus/README.md:34` now reads `uncovered` naming `fixtures/apk-r65` as work evidence and the retained rejected candidate; `## Frontier` C05 prose refreshed in the same revision. `K_HELD` stays 8/14 by construction — the claim is the honest adjudicated disposition, not held ground. Counter receipt: `K_ROW C05 status=uncovered`, `C05_REJECTED_MARKED=yes`, `README_TOKEN_LEGEND_MISMATCH=0`.
- C2 (C6 controls): LANDED. `verify_icon_languages.py:158-163` and `verify_multi_icon_states.py:157-162` each gained exactly two in-script controls after the forged-evidence control: `forged['exit_code']=1` → `forged receipt exit accepted`; `forged['fixture_sha256']=H(b'')` → `forged receipt fixture accepted`. Insertions only; `receipt_ok` untouched. Frozen mutants (delete `receipt['exit_code']==0` / `receipt['fixture_sha256']==expected_hash`, one regex match per script each) exit non-zero with last line ending the matching marker on both scripts — `C6_RECEIPT_KILLED_ATTRIBUTED 4/4`, red-before 0/4 at `8214e4dd`.
- Registered dispositions (claims.md §Registered): C06/C07 stale `candidate` headers flipped to `admitted` (R65ScoutReadme §C — counter-neutral); S043/S044 superseding rows (D2 + R65ReviewSources F1/F2); search-log retro + current notes (F3); SKILL.md currency refresh (R65ReviewSkillCites); D1 seat-mix erratum: the round-65 committed spec is **scribe 4**, not the "scribe 3" the round-65 report printed (spec roles: reviewer 20, critic 10, executor 10, scout 9, mutation-tester 7, scribe 4, sentinel 1, simplifier 1, revenger 1, connector 1).

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M39 | number-drift (a quoted output value transcribed, not reproduced) | `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` vs `readout.py --fact 'member[META-INF/MANIFEST.MF]'` output — `4d616e696673742d…` recorded, `4d616e69666573742d…` printed; caught by `R65ReviewEntryQ02/Q06/Q11` and `R65MutEntry` | Q11 (the criterion that caught it — "output it printed" is falsified); the author-side check that should have caught it is a verbatim diff of embedded output lines against the recheck stdout — **routed** as a future registered counter (claims.md §Routed forward), not claimed as a fix | the candidate is rejected and retained; the verbatim-diff gate is routed forward with owner = a future round that registers it |
| M40 | number-drift/anchor (located-quote pointers stated from intent) | `corpus/lessons/round-65.md:12` "lines 608-611" (actual span 607-609), `:13` "line 5" (actual 7-8), `:14` "(16 words)" (actual 14) — `R65LessonDraft`, `R65CriticLesson`, `R65ReviewSources` | the round-lesson located-quote rule (quotes verbatim + located) caught it at wave review; the row-level fix is contract rule 2 (correction = new row) | S043/S044 superseding rows land this round with re-opened anchors; the r65 lesson stays immutable history |
| M41 | attribution (a count asserted from a draft, not the committed spec) | r65 closure D1: report seat mix "scribe 3" sums 63 vs committed `wave-spec.json` scribe 4 / total 64 | report-vs-spec reconciliation at closure | erratum recorded in this lesson and the round-66 report |

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `/home/vgpnk/Projects/shokunin/unblob.log` — inspected: a 10-line unblob debug log over `/tmp/test-fw.bin` timestamped inside the r65 window but naming no revenger artifact, lane or round; `R65ScoutMisroot` classed it a plausible candidate, not confirmed. It does not name this lane's work → not claimed, not copied, not deleted (the one fleet-root deletion rule applies only to confirmed lane-seat files). All 64 R65 reports sit inside the lane's `.ufo/waves/round-65/`; no confirmed misroot.

## Routed forward (dispositions)

1. Counter label-spoof surface (R65CriticCounter): a one-line README edit prints the C1 after-state with zero work — the Q-gate is the defense; the AST-bound counter stays registered debt (owner: a future round that registers it).
2. Generator conditional symlink escape (R65SentinelScope): `fixtures/apk-r65/generator.py` output paths; fixture bytes are sha-pinned (S041), so the generator cannot be patched without breaking the pin — recorded limitation; any future fixture family regenerates under a new id.
3. Evidence-ID transplant prongs (a)/(b)/(d) + injectivity registry (R65RevengerLedger); one-sided endswith attribution asymmetry (R65LabAttribution); readout.py self-consistency mutation surface (R65MutProbe).
4. Verbatim-output-diff gate for embedded entry outputs (R65ReviewEntryQ02 recommendation) — the M39 fix shape; registered-debt owner.
5. Recheck-pin scope holes H1–H3; SHONEN box 1 `[x]` still needs a non-lane reviewer (D3 carried); r58/59 PASS-count quotes (owner rule: the round touching those two scripts).
6. C05 re-gate path: the falsified candidate's repairs are all text-level (entry:41 hex pair, S039/S038 anchors, item-8 provenance sentence, item-9 dex spec row, Q08 Q-map row, dangling pointers); a v2 candidate would need a dex-header spec row plus S043 as its route-scope source — named for the next coverage round, not claimed here.

## Round shape and receipts

L1-seat work under the accepted host mapping (this seat prepares waves; the orchestrator dispatches between rounds): adjudication re-verifications, C05 flip + marker, C6 controls, S042–S044, header repairs, SKILL.md refresh, census before/after, frozen counter on the base archive (red) and the committed tip (green). A fresh round-66 wave spec is prepared and validated under `.ufo/waves/round-66/` (prepared-but-undispatched, per the host-surface note). §3 planner seat held by the L1. Tool installs: none.
