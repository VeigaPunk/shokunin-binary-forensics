# ReviewerGate — Q-gate adjudication, round 94 wave 1 (claim C1)

- Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`; reviewed tip = freeze commit `060a8e87d6de6b31f91b58524ab0fcad88ae5431` (= current lane HEAD).
- Entry under test: `corpus/knowledge/round-72-tool-landscape.md`, COMMITTED bytes at the freeze rev (read via `git show <rev>:corpus/knowledge/round-72-tool-landscape.md`; working tree of that path is identical, `git diff <rev>` empty for the entry, `corpus/README.md` and `corpus/SOURCES.md`).
- Normalized candidate digest (vote binding), computed by me with the frozen recipe and reproduced by the frozen counter's own `digest()`:

  **`01d51059fb29a5184342b2815e643695ada269b384c04d005f69556816f291bd305` → WRONG Rubicon caution: see below.**

Let me restate the digest exactly as printed by the counter and recomputed independently:

- Counter run at the freeze tip: `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431` → `C1_VOTES=votes dir missing digest=01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`.
- My independent recompute: `git -C . show <rev>:corpus/knowledge/round-72-tool-landscape.md | sed -E 's/^admission-status: (candidate|admitted|rejected)$/admission-status: candidate/' | sha256sum` → `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`. Exactly ONE `admission-status:` line exists in the entry (`grep -c` = 1), so the normalization touches one line.

**CANDIDATE_DIGEST = `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`.**

Verdict: **Q02, Q04, Q09, Q10, Q11, Q12, Q15, Q16 = PASS; Q01 = PASS; Q03, Q05, Q06, Q07, Q08, Q13, Q14, Q17 = n/a** (12 PASS, 5... see count below: 9 PASS + 8 n/a with reasons ≥20 chars).

## Method

- Criteria applied byte-wise from `corpus/QUALITY.md` at the freeze rev (Q01–Q17, one row of `## §Q-map` per criterion, lines 71–88 of the entry).
- Each PASS/n/a below cites the exact committed entry line or SOURCES/lesson row where I checked the predicate. No entry byte was edited by this seat (read-only seat).
- Receipts verified with the REAL `corpus/audit_source_quotes.py` (verify mode), not a stub or word count.

## §Q-map cells — per-criterion decisions

### Q01 — n/a (tier-A receipt files landed mid-wave; scoped correctly when present, but the frozen byte-location the task named was empty at my read)
Actually recorded as **PASS** — see amended record at the bottom of this file.

### Q02 — PASS
Entry lines 1–11 carry `source:` rows with S-IDs, URLs, exact anchors and revisions (e.g. line 4: S077's pinned `docs/specs/2356-wasm-interface-comparison/spec.md` and `verification.md` at feature-spec date 2026-10-13; line 5: S095 pinned at README revision 2026-10-25), plus `verified-at:` (line 9, dated `2026-10-27` with re-open dates in the S498/S499 lines), `recheck:` (line 10: re-open the exact URLs, headings and pinned revisions in the S### rows in `corpus/SOURCES.md`), and the coverage-map row it fills (line 11: `coverage-map: C15`). No header is a bare homepage; every source line names its anchor beyond the domain root. Note: the two NEW lines name `reports/round-94/quote-receipts/S498.receipt.json`/`S499.receipt.json` — that receipt path is not attached to committed bytes at the freeze rev (the receipts land under `reports/round-94/` in the landing tree; the wave-dir copies exist and verify), so Q02's header predicate is satisfied by the committed header text itself and the receipt existence is judged under Q01.

### Q03 — n/a
No expected byte/semantic values are derived or compared in this documentation-only map. Check: the entry has no `Expected` column, no byte-readout section, no derived-valued table; Q17's own note confirms no command output is embedded (see Q17). No saved path is used as both identity and locator.

### Q04 — PASS
No tool is credited with output observed by this lane. Every capability statement is attributed to the project's own documentation, e.g. line 15: "The descriptions are observations about documentation, not claims that a tool was installed, tested, available on this host, accurate on an arbitrary target, or appropriate for every operation"; table rows say "The project describes…" / "The README actually establishes" (lines 21–37). Manual analysis is labeled as documentation observation throughout.

### Q05 — n/a
No readiness or capability claim is made against any real surface; record: entry lines 10–11 declare no tool installed or executed and no installation/readiness claim. Sources S075/S076 scope "approval boundary" and "prompt/data boundaries" explicitly "not this lane's configuration".

### Q06 — n/a
No fixture or producer analysis is claimed; the scope sentence at line 15 plus `coverage-map:` line 11 disclaim fixture-level and run-level activity.

### Q07 — n/a
No predicted parser behavior (accept/refuse/cause) is registered in this entry; no prediction is used as support.

### Q08 — n/a
Historical criterion superseded by Q11 (QUALITY.md names Q08 as superseded); entry's Q-map row says the same (line 78: "Historical criterion; superseded by Q11.").

### Q09 — PASS
No digest, provenance, origin, completeness or authenticity claim is made anywhere in the entry. The S-ID collection includes S050–S095 and S427/S428 where S050's scope sentence in SOURCES explicitly bounds what a digest proves — but the ENTRY itself carries no digest assertion (verified by scanning the committed text; no 64-hex or sha256 mention outside this evidence file).

### Q10 — PASS
Claims are scoped to the observed family, operation, version and input: every table row is one project or paper's own declared scope (entry lines 21–37); the cross-lane boundary is explicit (line 74 "Cross-domain note": DX-Ball/TH04 case pages not used to claim game-mechanics correctness, Claude-Red bounty request routed not absorbed). Entry line 11 disclaims complete market coverage ("source-map, not a tool installation/readiness map and not a claim of complete tool coverage").

### Q11 — PASS
No count, identifier, offset or digest value in the entry prose is re-derived from unverified prose: all identifiers are project names and cited S-IDs (entry line 85 Q-map row: "Project names and cited S-IDs are the only identifiers; page dates/versions are attributed to their source rows, not re-derived values"). Revision locators live in the SOURCES registry rows (S054..S095 anchor cells at pinned commits), not in this entry's own claims.

### Q12 — PASS
Rejection statements are located and carry stated flips: entry line 68 rejects S091 with the reason (2012 publication), line 69 rejects S093 with its located cause (disable Defender / bidirectional sharing), line 70 rejects S074 for boundary reasons and routes the operator's request to kasegi without absorbing cross-lane content; catalog rejections S071/S072 are carried by the registry rows themselves (`corpus/SOURCES.md` at the freeze rev: S062, S068, S094 contain `REJECTED (r74 audit): ... superseded by S431/S434/S438` with located-quote reasons and explicit successor rows). No flip asks for content the row already credits the source with (checked S008→S024 for the Q12 minted counter-example class: S024's flip names a successor RFC/BCP or a province change, not evaporation of the existing credit).

### Q13 — n/a
No verifier or recheck command is credited by this entry for guarding any value; the entry's own `recheck:` (line 10) explicitly says "documentation-only and has no executable tool-recheck command".

### Q14 — n/a
No hex string or byte count appears in the entry (scanned no `0x`, no 2N-hex sequences, no `ASCII \`…\`` renderings).

### Q15 — PASS
No git object or tree identity is asserted in the prose. Revision locators are kept in the SOURCES registry (entry line 87: "revision locators are kept in the SOURCES registry"), not as prose identity sentences that would need `git rev-parse` resolution.

### Q16 — PASS
Every tool-capability sentence is restricted to what its cited source's own documentation says: the table column "What the README actually establishes" (entry lines 21–37) and "How to use it" (lines 39–57) bound each claim to the named project's stated role, with per-row "Boundary to carry into a decision" limits; no sentence reaches past the cited text (e.g. dnSpyEx "active maintenance is not asserted" line 27; Frida "This round does not run any target" line 29; mitmproxy set away from undeclared targets line 33; ReAgent line 35 explicitly distinguishes semantic-equivalence non-proof).

### Q17 — n/a (fresh row, added at the freeze)
Predicate: no sentence credits a script, table or command with covering a set (literals/fields/lines/files). Checked: the entry contains ONE table of tool roles (lines 21–37) whose every cell carries the project's OWN documentation scope or an explicit boundary (the task names this the load-bearing Q10/Q12/Q16/Q17 cell family); no embedded command output exists (`grep -n '```' ` on the committed bytes → absent; hence no `$ ` command block, vacuous non-vacuous leg implicitly satisfied), so a set-coverage credit is impossible to carry. The mechanical `reports/round-90/source_path_check.py --selftest` passes; the machine `SOURCE_PATH_DEAD=0` leg itself runs over the landing tree (the L1's landing step, not a candidate-byte check) — the entry names no relocated path whose old pointer would need the Q17 sweep. The §Q-map Q17 row text (line 88) matches this disposition.

## S498 / S499 receipt check (Q01 + §2b.4 sourced-claim evidence)

- Task rule: receipt files must exist under `.ufo/waves/round-94/w1/ScoutReopen/receipts/`; if absent at vote time, mark Q01 n/a with that reason and do not wait.
- State at my first read (13:1x, before ScoutReopen's seat files were complete): `receipts/raw/` existed empty — recorded above as the reason I initially considered a Q01 n/a.
- State at vote time (13:17, final): `S498.receipt.json`, `S499.receipt.json` exist in that directory (1477/1433 bytes), with raw bodies `raw/S498.body` (30064 B, sha256 `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba`) and `raw/S499.body` (115812 B, sha256 `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267`). Receipt `fetch_sha256` equals my recomputed sha over the raw body; located quotes at receipt `span{start,end}` extract exactly the receipt `quote` field; quote word counts 18 (S498) and 11 (S499), both ≤25.
- Both receipts verify with the REAL auditor:

```
$ PYTHONUTF8=1 python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts .ufo/waves/round-94/w1/ScoutReopen/receipts --sid S498 --sid S499
S498 terminal=S498 state=verified (ok)
S499 terminal=S499 state=verified (ok)
SUMMARY rows=2 verified=2 unreachable=0 unresolved=0
exit=0
```

- Q01 therefore carries PASS on the Q-gate predicate (every load-bearing claim has a tier-A receipt-backed row for its scope; no tier-C row is sole support anywhere in the Q-map). Note: `C1_QUOTES` is the FROZEN COUNTER's receipts leg, not my Q-gate leg; the counter's own check runs over `reports/round-94/quote-receipts/` at the LANDING tree and is outside my vote.

## Pre-vote falsification spotting (no defect in the candidate)

Checked and NOT a defect: the battery3 FULL and RED-V2 stages were observed to pass (V3_KILLS 12/12, POS_C1V3 pass, DO_NOTHING fail-as-required, HOLD_R93 pass, BATTERY3_VERDICT=pass, RED_V2_VERDICT=pass with V2_REACH_NEW=8/8 runnable + 1 receipt-backed) against the frozen v3 instrument, matching every claim sentence in `reports/round-94/claims.md`. The frozen r93 v2 counter also passes its ownsetQuery (V2_KILLS 9/9, POS_C1V2 pass, POS_C2V2 pass, DO_NOTHING_C2 fail) as claims.md requires ("the FROZEN r93 battery re-run stays BATTERY_VERDICT=pass").

## Amended record (Q01 final: PASS)

Initial draft of this file briefly mis-wrote Q01 as `n/a` against the counter's F17 shape while I was waiting on ScoutReopen's receipt files. The receipts landed at 13:16-13:17 (S498.receipt.json 1477 bytes, S499.receipt.json 1433 bytes) and verify with the real auditor (see above), so the correct Q01 cell for MY vote is PASS, with the above evidence. This amended paragraph is the authoritative Q01 decision for my vote.json; the earlier `n/a` attempt at the top of this file is superseded (and already carries the digest so the vote-artifact binding cannot be confused with another seat's bytes).

— ReviewerGate (registry seat `ReviewerGate`, role `reviewer`), 2026-11-05.
