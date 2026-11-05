# ConnectorOverlap — revenger round 93, wave 1 (seat report, 2026-11-05)

Scope: sibling-overlap scan (kaidoku, tabi, kotoba, kumitate, kengaku — read-only) + considerthese mining (exactly one proposal: proposal 2 of `considerthese/2026-11-05.md`). Outputs: `.ufo/waves/round-93/w1/ConnectorOverlap/overlap.tsv`, `.../measurement.tsv`, `.../measurement-commands.sh`, `.../considerthese-note.md`. All sibling reads were read-only (`grep`/`read`/`git show` at pinned revs); no sibling or frozen file was modified; no subagents were dispatched; no tools were installed (none needed).

## 1. Sibling overlap: C08 absorbs nothing, and three standing contest marks say it must not

C08 is the coverage-map row "browser/Electron runtime evidence" (ops `capture_browser_scenario`, `inspect_web_page`, `observe_web_session`). The r93 C1 entry is scoped to the authored fixture + the saved round-77 CDP record only (claims.md Q10: no general browser, Chrome, CDP or Electron claim). The scan confirms that scope discipline is not just polite — it is required by the record:

- **tabi** holds the deepest CDP ground (loopback session recipes, `/json/version`/`/json/list`/`Target.getTargets`, determinism classes E1–E11; `corpus/knowledge/cdp-evidence-patterns.md`, `live-dynamic-capture.md`, plus external CDP authorities S001–S012). Tabi's own cross-lane ledger `corpus/adjacency.tsv:5` pins revenger PROVINCE.md:5 as **contested-open** against tabi's CDP session discipline, and the fleet L0 question `.ufo/l0-questions.md:65` (tabi round-17) — *"say whether the ruling covers revenger and kama on these surfaces or rule a split"* — is unanswered as of this scan. Tabi's r16 integrator ruling (`corpus/lessons/round-16-verifier-spotcheck.md:142-146`) names only tabi (owns live browser/CDP page observation incl. WebMCP) and kaidoku (CDP only as an REA provider surface for shipped-artifact analysis); revenger is outside it. Provenance note: that ruling's authoritative home is tabi's file — kaidoku's live corpus carries no "keeps CDP" text (grep 2026-11-05), matching the L0 line's own citation.
- **kaidoku** holds live CDP ground on this host (README.md:36-37 "Runtime observation … held — CDP enumerate/inspect on self-launched chromium + electron"; knowledge `2026-10-13-r3-runtime-observation.md:13-30,60-72`), bounded by the r16 ruling; its Electron SOURCES rows (S012–S014) are static-integrity docs, a different sub-surface from C08's runtime cell.
- **kotoba, kumitate, kengaku** hold no browser/CDP runtime-evidence ground. Kotoba independently corroborates the arbitration gap (README.md:308-310: named overlaps incl. kagi↔kake CDP, "0/5 descriptions carry an arbitration clause"). Kumitate's "runtime" hits are the agent runtime (V8 heap-cap vs cgroup, `agent-isolation-substrates.md:134-136`) plus a browser-extension naming row. Kengaku's hits are benchmark/paper ground (WebArena "deterministic browser"; arXiv 2605.14786 browser-agent fingerprinting as prior art), and its PROVINCE refuses runtime task validity.
- **Lane-internal precedent:** `.ufo/waves/round-61/build/ConnectorRosterScan.md:15-28` ran the same scan 30+ rounds ago and found the same contest rows; tsukuroi PROVINCE.md:150-152 (verified live) still reads "Kaidoku/Revenger arbitration remains unresolved". Tabi's r36 drift-audit note (`adjacency-drift-audit-r36.md:157-160`) records that revenger moved with zero browser-ground screen rows citing it at those heads — the r93 entry will be the first new revenger browser-ground bytes tabi's delta leg sees, which is one more reason to keep it fixture-scoped.

**Verdict:** no sibling row's scope is absorbed by the C08 entry; `overlap.tsv` names contested scope, never absorbs it. No defect in the r93 claims' scope wording was found — Q10's fixture+record-only scope is exactly what the contested-open marks require.

## 2. Considerthese mining: proposal 2 measured — the running rate is flat at 8/8

Proposal: "Frozen-counter validity rate" (`considerthese/2026-11-05.md`, proposal 2). Measured on committed bytes at the r93 freeze (`git show 02050cb…:<path>`; commands in `measurement-commands.sh`, table in `measurement.tsv`):

- r89: 2/2 failed/killed (C1 MISS 10→2 vs target 0; C2 KILLED — forged records pass the oracle, runs differ at byte 20)
- r90: 2/2 (C1 met-contested; C2 met-but-NOT-VERIFIED — ctl-idedit/ctl-stub also 6/6)
- r91: 2/2 (C1 met-contested — 21-entry lookup table passes, spot-check re-measured NOT VERIFIED; C2 NOT VERIFIED — stubD/stubE pass)
- r92: 2/2 met-contested (critic full forgery passes the C1 counter 12/12 legs; four cheaper moves + probe shadow pass the C2 counter) — yet the round was **admitted** on the spot-check's independent re-derivation (§2), with the forgery routed to r93 (§6 item 5)
- **Running rate: 8 of 8 = 100%** (met-on-the-counter subset r90–r92: 6/6 = 100%)

Reading: r92's pre-freeze skip-work controls did **not** reduce the rate — they caught lazy skips, while the surviving reachability is skilled forgery, which only r93's successor counters + forge battery target. Three caveats are baked into the TSV: compute from correction rows, never first-pass headings (SCORECARD.md:1674 still says r91 "verified" — the r92 correction row r91 D2 is the record); "later contested" vs r92's in-round contest are kept as separate sub-classes; r93 is self-referential for this metric, so its reading should be appended at adjudication and re-confirmed by r94, not graded by this round's own gate.

**Proposed move (the one bounded proposal):** land the validity rate as a QUALITY.md criterion row citing `considerthese/2026-11-05.md` proposal 2 with the fixed denominator, the corrections-over-headings source rule, and the committed 8/8 baseline (`measurement.tsv`), or as a round-93 lesson section if the L1 prefers — full shape and risks in `considerthese-note.md`. QUALITY.md itself was not edited.

## Affected axes

- **coverage (C1):** no change proposed to the entry or counter; the overlap scan confirms C08's scope wording. Zero-harm.
- **adjacency:** the report makes the standing contest state visible at the moment C08 moves `uncovered → held`; it adjudicates nothing. Zero-harm.
- **calibration:** the mined criterion would give the calibration axis a running instrument-quality number with a committed baseline. Improvement, pending L1 adoption.

## Risks

- The validity-rate criterion could become a target to game (safe claim shapes); mitigated by counting claims with a per-claims.md frozen denominator and keying on (round, claim id).
- Tabi's drift meter will classify the new entry's bytes; fixture-scoped wording keeps that classification trivial (its BG vocabulary), and no tabi file was or should be touched by r93.
- The stale r91 SCORECARD heading could mislead a future rate computation; the criterion's source rule (corrections authoritative) is the guard.

## Verification

- Verdict bytes re-read at the frozen tip via `git show 02050cb2…:<path>` for all 13 source files (claims ×4, SCORECARD, lessons ×4, spot-checks ×4); every count in `measurement.tsv` names path+lines.
- Sibling rows pinned by path:line in `overlap.tsv` (tabi adjacency.tsv:5; tabi r16 spotcheck :142-146; fleet l0-questions.md:65; kaidoku README.md:36-37; r3-runtime-observation.md:13-30,60-72; kotoba README.md:308-310; kumitate agent-isolation-substrates.md:134-136; kengaku attrib-prior-art-r21.md:88, benchmark-selection.md:18; lane-internal round-61 ConnectorRosterScan.md:15-28; tsukuroi PROVINCE.md:150-152 read live).
- The `awk` rate line in `measurement-commands.sh` §4 was run over `measurement.tsv` (claims=8 invalid=8 running_rate=8/8 = 100%).
- Untested/unsupported: nothing in this report was executed against the frozen counters (they are not this seat's instruments); the r93 entry draft itself was not read or judged (not this seat's scope).
