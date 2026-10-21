# ReviewerPreregAudit — round 61 pre-registration audit (read-only)

Lane `revenger-shokunin`, landed `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` (parent `ea95ab8`; claim base `cf02419`). Axes: **coverage** (contract §2, §2b, §4 items present) and **calibration** (before values reproduce; measure validity). Installs: none. Scratch: `/tmp/revenger-r61-ReviewerPreregAudit-*`. Live lane: read-only.

## 1. Before values reproduce (calibration: pass)
- `git archive e0a4 corpus | tar -x -C /tmp/revenger-r61-ReviewerPreregAudit-e0a4`; probe taken from `git show e0a4:reports/round-61/measure.py`; run `python3 -B <probe> <archive>`.
- Output lines diffed against `measure-before.log` (K_/MUTANT/C2_/HOLD/probe_exit): no difference. Values: `K_HELD=4/14 score=2.9`; C04, C09 `uncovered`; mutant b `exit=0` on both scripts; d2 killed 2/2; `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=0/2`, `C2_D2_KILLED=2/2`; `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`; rc 0.
- Probe wrote nothing into the archive (466 files; sha256 manifest unchanged).
- Cross-checks: held-row regex on archive README → 4 rows (C01, C11, C12, C13). SCORECARD F command on archive → `COVERAGE 4 / 8 score= 5.0` (inspect_evm_interface 7 records, analyze_javascript_application 6).
- Census at round start, live: `validate --root … revenger` → `revenger ok`, rc 0 (measure-before.log:28-30). `census` → rows 15, tier A 14, tier C 1, mined 12, queued 1, rejected 2.
- Live lane: `git --no-optional-locks status` clean for corpus, reports, LOG.md, SCORECARD.md; e0a4 is HEAD.

## 2. Conformance: present vs missing
Present (verified):
- §2: two claims (cap 3) on distinct axes. K=2.9 is the lowest owned non-retired criterion (SCORECARD.md:131-134: calibration 10.0, F 5.0, K 2.9, freshness 10.0; depth retired). Saturation 7.0 (SCORECARD.md:173), so no nudge. Each claim has before→after and a pasteable counting command (claims.md:19-62). Motivation in LOG.md:785-791. No corpus or SCORECARD change after e0a4.
- Watchdog: `.ufo/watchdog.log:614` launch 12:05:35 matches; no `lane-dead-no-report revenger round=61` line.
Missing:
- **M1 sourced claim (§2b.4): none.** No SOURCES row opened this round. SOURCES.md:15-29 holds S001–S015; none covers Node CommonJS, ECMAScript or EVM scope (tier-A rows: PE, Unicode, digests, CFTT, own records). Needed: rows from S016, each opened this round with URL, access date 2026-10-21 and a ≤25-word located quote in `corpus/lessons/round-61.md ## Gate` (round-1.md:61-68; CORPUS.md:112-115). C1 entries cite `S###` in `source:` (QUALITY Q02; knowledge/pe-resource-directory-layout.md:1-5).
- **M2 mistake (§2b.3): none.** `corpus/lessons/round-61.md` absent (lessons/: round-1.md, round-1-verifier-spotcheck.md, 2026-10-12-r1-provider-gap.md).
- **M3 census after (§2b.2):** pending; must be exit 0 at round end.
- **M4 SCORECARD measured rows and LOG verdicts (§2.5):** pending.
- **M5 report (§4):** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-61/revenger.md` absent; not yet due.
- Inherited debt outside §2–§4: SKILL.md and AGENTS.md absent (SCORECARD.md:109-110; corpus/README.md:47).

Mistake candidates for M2 (each verified in-lane; captured-by `none` for all):
- (a) Receipt-clause survivor: `.ufo/waves/kaika-r1/mutation-post.md:15,21` (b exit 0 ×2); routed debt `corpus/lessons/round-1-verifier-spotcheck.md:17`. Fix = C2; base 0/2 shows the gap.
- (b) Rejected row contradicting its own flip: `corpus/SOURCES.md:22` (S008 flip: "needs its volatility-ordering primitive specifically") vs spot-check `:13` ("§2.1 Order of Volatility is the very primitive its flip names"). Fix: reopen S008 §2.1; status change logged old→new (CORPUS.md:116-118).
- (c) Index drift: `corpus/README.md:9` says Q01–Q10; QUALITY.md:23 has Q11 (M20, round-1.md:131). Fix: edit; `grep -c 'Q01–Q10' corpus/README.md` 1 → 0.
- (d) D1 below: a pre-registered counter satisfiable without the claimed state. Fix: companion check.

## 3. Calibration defects in the pre-registration
- **D1 (high; demonstrated).** K_HELD counts README text only. On a /tmp copy of the archive README, flipping the C04 and C09 status text with zero knowledge files gives 4/14 → 6/14 (score 4.3), exactly C1's "both admit" prediction. Inherited from SCORECARD.md:133. Fix: amend before any corpus edit; also require each held row's knowledge file to exist with `source:`, `verified-at:`, `recheck:` headers.
- **D2 (medium; inferred from code, not demonstrated).** Kill is `rc != 0` (measure.py:81, :83). A SyntaxError or NameError confined to the b variant counts as a kill. Fix: require the printed tail (measure.py:77) to be the control's own message. n=2 gives 0/5/10 steps, so one false kill moves the score 5.0.
- **D3 (medium).** No-harm holds omit owned criteria. F and freshness (SCORECARD.md:132,134) are not in the holds (claims.md:60-62, 68-70). F is covered only indirectly by the corpus/live diff; freshness by none.
- **D4 (low).** The byte-identity hold (`git diff … -- corpus/live corpus/fixtures`) is not computed by measure.py. HOLD runs use `cwd=TREE` (measure.py:90), so "never writes inside TREE" (measure.py:6) is observed here, not enforced.
- **D5 (low).** Claim base `cf02419` is not the parent `ea95ab8`; they differ only by `considerthese/2026-10-20.md` and `2026-10-21.md`. Corpus identical, so the before values stand.
- **D6 (C2 feasibility).** Both verifiers read receipts from disk in `check()` (verify_icon_languages.py:126; verify_multi_icon_states.py:127). The forged receipt must pass through the same clause (:144-145; :142-143), so the control needs a receipt parameter. A control that compares outside the clause leaves b alive. Keep exactly one `receipt['command']==command|f'…'` match or the probe returns exit 2 (measure.py:38-39).
- Pre-registered falsifiers: K_HELD stays 4/14 (C1 fails); C2 k<2 (C2 fails); any lost hold voids C2.

## 4. Evidence facts for C1 entries (for wave-2 attackers)
- C04: js-r3/index.js:1 `const { rot13, checksum } = require('./transform');`; js-r3/package.json `"main":"index.js"`; js-r7-v2/index.js:1 one named import; promotion-review-r5.md:7 (two named imports and package-main edge compared to source). Saved records keep absolute input_path values from another checkout (20261012T164357Z/analysis.json:1): cite bytes, not saved paths (Q03; M14).
- C09: evm-r19/truth.json:6-9 (`deadbeef`, PUSH4 opcode 6, immediate 7, length 4). Saved candidates at destination offset 16 (round-19 LEDGER.md:3; round-21 reviewer.md:7; round-24 reviewer.md:7), 30 and 32 (round-22 LEDGER.md:3,5). Empty results: round-25 LEDGER.md:5 (cause unknown) and round-26 LEDGER.md:5. State the empty cases; offsets are destinations, not selector locations; no ABI or execution claim (truth.json:10).
- Receipts and Evidence show internal consistency, not producer origin (Q09; M13).

## 5. Not done
- No web opens. `.ufo/waves/round-61/build/*.md` exist from sibling seats and were not audited. No after-measurement (not due).

VERDICT: e0a4 is conformant at pre-registration and its before values reproduce exactly; the §2b sourced claim, mistake and round-end census are missing (expected pre-measurement); amend D1–D3 before any after-run.
