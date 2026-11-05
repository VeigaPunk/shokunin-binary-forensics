# Round 96 — gate, frontier, mistakes (revenger, hyaku run 15, attempt 1)

Base `2875b9c9fa4cc15fd5a8ff991f04cdd0417bec97`; freeze `ff767436feed32cf2f4074f05f938f8cea98e69a`
(claims `reports/round-96/claims.md`, counter `reports/round-96/c1_k_admit_counter5.py`, battery
`reports/round-96/forge_battery5.py`, controls and per-delta receipts, the C02 candidate
`corpus/knowledge/round-96-native-analysis-sessions.md`, the session record `corpus/live/runs/round-96/`,
S502/S503 receipts). Claims and predicates: `claims.md`, unchanged since the freeze.

**Verdict of record: C1 NOT VERIFIED (honest miss); C2 met on its frozen predicate, contested.**
The candidate entry is NOT admitted this round; the C02 row stays `partial`; K stays 12/15.

## Gate

### Votes (lane-internal; LEARNING.md: a subagent the lane dispatched is still the lane)

Three lane-dispatched votes bind candidate digest `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`
(normalized; the entry's status line is `candidate` in the frozen bytes), each with 11 PASS decisions
and n/a reasons carrying a Q cross-reference: `reports/round-96/votes/{ReviewerGate,ReviewerBlind,CriticR96}.json`,
artifacts under `.ufo/waves/round-96/w1/<seat>/`. The votes recommend admission on the Q-map. They are
not the admission: the frozen counter is the admission instrument (`corpus/QUALITY.md` procedure step 2,
`reports/round-96/claims.md` C1).

### Candidates considered

- **C02 native analysis sessions — ENTRY, NOT ADMITTED this round.** Entry grounds REA's documented
  native routes (S502, S503, fetched 2026-11-05 at `12f6e09`) and one demonstrated session on this
  host (S504, own-work: `rea decompile` Evidence `ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe`
  over the committed pe-r75 fixture; ghidra-headless reproduction). Reject record (frozen counter, landed
  tree): with the admission flip applied, the frozen counter fails exactly one leg, `C1_SOURCES`, because
  its used-by exclusivity compares against the fixture-form path `knowledge/round-96-native-analysis-sessions.md`
  while the real used-by cells carry the census form `corpus/knowledge/round-96-native-analysis-sessions.md`
  (`reports/round-96/c1-tree-flip-diagnostic.log`; the census resolves used-by paths from the lane root, so
  the short form would be a census defect). The entry itself is not the failing object: it passes every
  other leg (`C1_ADMITTED_UNION`, `C1_LINT`, `C1_EMBEDDED`, `C1_QUOTES`, `C1_RECEIPTS`, `C1_SIDS`, `C1_TRIO`,
  `C1_K_HELD_BACKED` at 13/15 with the flip). Flip to admit: a successor counter whose used-by normalizer
  accepts the census form (frozen as a v6 on a new round's freeze) with a red-before on a corpus-prefixed fixture.
  The candidate digest is unchanged, so the three votes remain valid for that successor round.
- **C05 Android K-move — REJECTED.** The round-95 spot-check (§3 item 4) ruled that a seventh APK/AXML candidate
  without a new primary source repeats a known failure; none was opened this round. Flip: a primary
  APK/AXML byte source opened and grounded into a candidate passing Q01–Q17 with the six prior classes addressed.
- **Adding a C16 atlas row — REJECTED.** A new row would change the frozen K denominator mid-round. Flip: a
  round whose claims are frozen against the enlarged denominator.

### Located quotes (new rows; ≤25 words each; bodies committed at `reports/round-96/quote-receipts/raw/`)

- S502 — https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md — accessed 2026-11-05 — located quote (12 words; receipt span 26309–26411, section "DOS MZ with Ghidra"): "`rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally"
- S503 — https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/SKILL.md — accessed 2026-11-05 — located quote (17 words; receipt span 257–389, frontmatter description): "Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction."
- S504 — `corpus/live/runs/round-96/` (own-work record; opened 2026-11-05) — located quote (saved headless output `codeable-decompiled.c`, entry block, 3 lines): "undefined8 entry(void) { return 0x2a; }" (the Evidence's `normalized_result` carries the same body)

`audit_source_quotes.py verify` over S502/S503: `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`
(`reports/round-96/controls/` and wave `ExecReceipts/verify.md`).

### Rejected sources — none appended as rows this round

No row was rejected this round. Two candidate sources were ruled out by their own content: the installed
skill copy (S002 context only; it differs in bytes from the pinned body, disclosed in the entry's Unknown);
`cli-command-map.md` at the pinned revision (HTTP 404; recorded in the fetch log, no row).

## Frontier

- Rows 501 → 504: S502, S503, S504 appended (all `mined`, tier A, opened 2026-11-05; used-by = the candidate
  entry, exact). Rows are kept although the entry is not admitted: each is an opened, receipted primary
  source; the candidate cites them. Census round start exit 0 (`controls/census-round-start.log`); landing-tree
  census exit 0 (`controls/census-landing-tree.log`).
- Coverage: none. K 12/15 unchanged; C02 `partial` unchanged (admission withheld).

## Post-freeze observations (recorded here; the frozen entry bytes are NOT edited — the votes bind them)

- **Evidence-ID stability (the entry's Unknown):** wave seat `ExecSession` re-ran `rea decompile … 140001000`
  on this host: printed `evidence_id` equal to the frozen `ev_cc0b9d88…`; `diff rea-decompile-repro.txt`
  against the frozen `rea-decompile.raw.txt` empty (`.ufo/waves/round-96/w1/ExecSession/rea-diff.txt`).
  Stable across two runs on this host. The entry's Unknown sentence still reads "whether … stable"; it is
  answered for this host by one re-run, which a future admission should cite.
- **Doctor run:** the re-run's ghidra scope set equals the frozen receipt; the only differing line is a
  per-invocation `fnm_multishells` PID path (`doctor-diff.txt`).

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M1 | fixture-constant drift: v5 deltas carried v4 constants (CriticR95 vote name, S500/S501 receipt sids, the F19 quote anchor); the self-test crashed before any freeze | pre-freeze self-test run (FileNotFoundError on S504.receipt.json); clean rerun `controls/selftest-c1v5.log` | the self-test itself (crash on run) | constants re-keyed to the v5 row set; shown able to fail (crash before fix; `SELFTEST_C1V5=pass legs=33` after) |
| M2 | materialization blindness: the planted `reports/round-94/__pycache__` delta was dropped by the fixture materializer (not an archive path) and decided `rc=0 failing=[]` | pre-freeze self-test `SELFTEST FAIL: M8-pycache-frozen-dir … got rc=0 failing=[]` (observed; fixed) | the decide-on-expected-leg check | archive list widened to every scanned dir; shown able to fail (FAIL line before, `decide` after) |
| M3 | parser self-disarm: the failing-legs parser dropped any line containing `BACKED`, so `KHELDBACK-broken-cell` could never decide on `C1_K_HELD_BACKED` | pre-freeze `SELFTEST FAIL: KHELDBACK-broken-cell … failing=['C1_ONLY_C02','C1_VERDICT']` (observed; fixed) | the decide-on-expected-leg check | the parser filters only `WHY`/`DIFFS` print lines; shown able to fail |
| M4 | index gap: `corpus/knowledge/claude-red-re-bridge.md` carries `admission-status: candidate` and is named nowhere in `corpus/README.md` | `grep -c claude-red corpus/README.md` → 0 (file header `admission-status: candidate`) | none (found by a union survey, not a leg; the union leg only constrains admitted files) | **routed to r97**: index it or reject it with a flip; not fixed this round (frozen-instrument discipline is unaffected, but the README edit would be unreviewed scope) |
| M5 | **real-tree path-form mismatch (this round's miss):** the v5 exclusivity leg compares used-by to `knowledge/round-96-…md` (fixture form) while the census and every existing row use `corpus/knowledge/round-96-…md`; the fixture hid it because the fixture writes the short form | `reports/round-96/c1-tree-flip-diagnostic.log` (`C1_SOURCES_WHY=S502:usedby-exclusivity:['corpus/knowledge/round-96-native-analysis-sessions.md']`, S503, S504); `corpus/SOURCES.md` rows 519–521 | none — the self-test and the frozen battery both ran the fixture form | the admission is withheld (honest miss); **routed to r97**: a v6 successor whose used-by normalizer accepts the census form, with a red-before on a corpus-prefixed landed-tree fixture; the counter is NOT edited |
| M6 | **decorated admitted line evades the new A4 leg:** `C1_ADMITTED_UNION` uses `\s*admission-status\s*:\s*admitted\s*$`, so `admission-status: admitted (round-96 gate, two reviewer votes)` passes the union check | CriticR96 F1 `reports/round-96/c1_k_admit_counter5.py` leg + `.ufo/waves/round-96/w1/CriticR96/receipts/FG01-shadow-decorated-admitted.log` (C1_ADMITTED_UNION=pass) | none (the leg's self-test has no decorated delta) | **routed to r97**: drop the `$` anchor and add a decorated delta to the self-test (red-before on the frozen v5 bytes) |
| M7 | **mislabelled self-test count:** `SELFTEST_C1V5=pass legs=33` prints `len(EXPECT_FAIL)+2` (31 deltas + 2), not the number of legs; the counter has 18 legs. The claims file and the SKILL registry first repeated the label as a leg count | `reports/round-96/controls/selftest-c1v5.log` (the printed line); `reports/round-96/c1_k_admit_counter5.py` `print(f"SELFTEST_C1V5=… legs={len(EXPECT_FAIL) + 2}")` | none | the SKILL row and the SCORECARD now state the measured 18; the counter's print is frozen (a label, not a verdict input) and corrected in v6 |

Other critic findings (CriticR96 F2–F14, MutationR96 d-host) are routed to r97 with their receipts; see the
SCORECARD r96 section. None changes a frozen predicate.

## Routed forward (r97)

1. Counter v6 successor on a new freeze: (a) used-by normalizer accepts the census form (M5), with red-before
   on a corpus-prefixed landed-tree fixture; (b) `C1_ADMITTED_UNION` anchor without `$` and a decorated delta (M6);
   (c) F2–F4 union scan recursive, case-insensitive extension, byte-tolerant decode; (d) F5/F6 vote artifacts
   must contain non-comment substantive text and resolve without symlinks; (e) F7/F8 sid and pycache coverage;
   (f) MutationR96 `d-host` killed by a delta that swaps the receipt host. The candidate digest is unchanged
   by any of this, so the three existing votes remain valid; the non-author closure is still required.
2. Admission of C02 on v6 if (1) passes, with the same entry bytes; the outside check remains the non-author closure.
3. M4: index or reject `claude-red-re-bridge.md`.
4. `considerthese/`: no proposal adopted this round beyond the standing receipt practice (SCORECARD r96).
5. L0 `revenger | round-91` (assimilation id collisions, 155/155) remains unanswered; assimilation: none.
