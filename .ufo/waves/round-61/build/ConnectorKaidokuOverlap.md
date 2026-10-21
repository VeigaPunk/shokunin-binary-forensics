# ConnectorKaidokuOverlap — ADJ-06 scan of the round-61 C04/C09 entries

Read-only seat; base observed `git -C revenger-shokunin rev-parse HEAD` = `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`; only this report written (lane `git status --porcelain` → `?? .ufo/waves/round-61/`). ADJ-06 (`.ufo/l0-questions.md:42`) is still OPEN: `kaidoku-shokunin/PROVINCE.md:240` and `:272-273` "arbitration is still open", and revenger `PROVINCE.md` (32 lines) has zero "kaidoku" occurrences (`grep -rln kaidoku revenger-shokunin/{PROVINCE.md,corpus/README.md,corpus/SOURCES.md}` → rc 1).

## Answer

**C09 as pre-registered absorbs kaidoku ground. C04 does not absorb kaidoku's fact, but its row label claims Electron-container ground revenger holds no artifact for.** Both rows can still flip `uncovered → held` (K_HELD 6/14) if the two entries are re-subjected as below: the counter is a README status regex (`reports/round-61/measure.py:26`), not entry wording.

## Evidence

1. The split is already routed one way: kaidoku `PROVINCE.md:69-71` adopts revenger's split as its authority — map entries "never stands for that lane's current runtime capability (routing: `../revenger-shokunin/reports/round-1/connector.md:25,33-36`)"; that split assigns ledger facts to revenger and "what the `rea` tool currently is" to kaidoku (`reports/round-1/connector.md:33-36`). Revenger never reciprocates.
2. kaidoku owns both provider surfaces verbatim: `PROVINCE.md:49` Core `analyze_javascript_application` (12 pinned ASARs, `ev_2628de89…`); `PROVINCE.md:54` Core `rea inspect-evm-interface` (EVMole 0.9.3, 81-byte dispatcher, `dispatch:"abi"`). Revenger `PROVINCE.md:4` claims the same nouns ("Electron/JavaScript packages"), so the noun is not the discriminator — the claim's *subject* must be.
3. **C09 prior art is exact.** `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-evm-interface.md:151-153`: "`bytecodeOffset` records the **JUMPDEST dispatch-target position**, not the PUSH4 comparison site"; re-confirmed on real solc bytes at `2026-10-19-arc3-r1-evm-real-solc.md:23` ("every reported offset lands on byte `5b` (JUMPDEST)"). The registered C09 wording — "PUSH4 selector candidates and their JUMPDEST destinations" (`reports/round-61/claims.md` C1) — is that proposition.
4. **kaidoku holds no validity/decoy lattice; revenger's fixtures are exactly that.** Byte walk I ran read-only over `corpus/fixtures/evm-r{19,21..26}`: all `truth.json` digests re-derived true; destinations land on `0x5b` (r21 @16, r22 @30/@32, r25/r26 @17); `evm-r24` = PUSH32 with embedded `63deadbeef14601057` at offsets 1 and 9 and **0 executable PUSH4**; `evm-r25` byte 16 = `0x00` STOP while JUMPDEST is at 17 (`jump_target_valid:false`), repaired by one byte `0x10→0x11`@14 in `evm-r26`; `evm-r23` = PUSH4+POP+STOP, `comparison_or_jump:false`. These are the Yellow Paper §9.4.3 "not sitting in the data portion of PUSH" boundary cases, which no kaidoku entry constructs.
5. **C04 is complementary, not duplicate.** kaidoku holds the relation vocabulary on real ASARs (`2026-10-13-r2-asar-deep-obsidian.md:17` — `imports` 76/`maps_to` 28; `2026-10-13-r3-typora-signal.md:33,49`) and records main resolution as `2026-10-13-r3-renderer-asar.md:81`: → `resolution_status: "not-found"` in obsidian.asar — opposite state to revenger's authored-fixture "resolved". kaidoku holds **no** per-binding `imported_name`: `grep -rn imported_name kaidoku-shokunin/corpus/knowledge/` → rc 1; revenger uses it at `corpus/verify_js_graph_delta.py:36,43`.
6. **Revenger has zero container evidence for "Electron".** `find corpus/fixtures/{js-r3,js-r7-v2,shapes-r12} -type f` → 10 files, all bare `.js`/`.json`, no `.asar`; every saved run self-reports `nested_asar_containers: 0` (`grep -roh ".\{40\}asar.\{40\}" corpus/live/runs/`). So `corpus/README.md:30` "JavaScript/Electron packages" asserts `kaidoku PROVINCE.md:49` ground with no artifact behind it.
7. C04's current subject is the record, not the tool: `verify_js_graph_delta.py:31` requires `operation == "analyze_javascript_application"`, `:53` pins `ev_4a93276c…`, `:58` equates the saved graph to source-derived truth. Citing a saved run as data is in-province (`PROVINCE.md:5`); asserting what the analyzer *does* is kaidoku's.

## Proposed move (one bounded synthesis)

- **C09 — re-subject to the discriminator, not the offset semantics:** "on authored inert bytecode, a PUSH4 not on an instruction boundary (inside PUSH32) or whose operand misses `0x5b` yields no valid destination; a dispatch-shaped PUSH4 landing on `0x5b` yields one candidate." Derivation = the §4 byte walk handed over verbatim (Q11 requires command+output in-entry). Cite the Yellow Paper §9.4.3 eq. 160-161 (scribe row `S017`) as the rule, and kaidoku `2026-10-13-r3-evm-interface.md:151-153` **as prior art only**, never as this round's finding. r23/r24/r25 become the milestone's first falsifiers: they must yield zero candidates.
- **C04 — subject the claim to the record:** "in saved run `ev_4a93276c…`, the named-import edge set carries exactly `{rot13, checksum}` with `imported_name`, and the `maps_to` edge resolves `main`→`index.js`", with scope "extracted CommonJS directory; ASAR/Electron container facts are kaidoku's (`PROVINCE.md:49`), unexamined here; `exports`-bearing packages excluded (`S017` Q5)". Contrast cite kaidoku's `not-found` case (`r3-renderer-asar.md:81`) as the complement.
- **Both — one provenance line:** "provider capability/version/availability claims are kaidoku's (`../kaidoku-shokunin/PROVINCE.md:49,54`); ADJ-06 is unarbitrated (`.ufo/l0-questions.md:42`) and these entries presume no split." No revenger `SOURCES.md` row may cite a sibling corpus entry — sibling knowledge is not a tier-A source.

## Affected axes

Coverage K: counter unchanged, `4/14 → 6/14` (2.9 → 4.3) still reachable, and the move adds the C09 falsifier class the milestone asks for. Calibration C2 untouched (the two verifier scripts are not in the move's path; `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10` unchanged). Freshness/substrate unchanged. No axis harmed: nothing is deleted, two claims narrow and two prior-art citations are added.

## Risks

1. **Scope-shrink reading** on C09. Mitigation: same row flip on the same regex, and the narrowed entry covers r21–r26 instead of r19 alone.
2. **Label contradiction survives if only entries change** — `PROVINCE.md:4` and `README.md:30` still say "Electron"; one qualifier in the row, no row-count change, closes it.
3. **C04 source split**: `ScribeSourcesRowsJs.md` §4 already found destructuring is unsourced by S016/S017; either open an ECMAScript destructuring source this round or label that half `[INFERENCE]` with the fixture derivation only.
4. **Id collision**: both scribes proposed S016/S017 (`ScribeSourcesRowsJs.md` §5, `ScribeSourcesRowsEvm.md` §4) — L1 must assign four distinct ids or the census validate fails.
5. **No verifier covers r22–r26**; `verify_evm_evidence.py` is scoped to r19, so Q11's in-entry byte walk carries the new claims.

## Verification (for L1; I ran none of these as lane edits)

- `python3 -B corpus/verify_evm_evidence.py --self-test` and `verify_js_graph_delta.py` → exit 0 (both green in `reports/round-61/measure-before.log`).
- `python3 -B reports/round-61/measure.py <TREE>` → `K_HELD=6/14`, `K_ROW C04 status=held`, `K_ROW C09 status=held`.
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → exit 0 with four new distinct ids.
- `grep -c kaidoku corpus/SOURCES.md` → 0 as a post-condition; re-run my §4 byte walk and diff it against the landed entry text.

VERDICT: C09 must be re-subjected to the boundary/decoy lattice (its registered wording duplicates kaidoku `2026-10-13-r3-evm-interface.md:151-153`) and C04 narrowed from "Electron" to extracted-CommonJS with record-subject phrasing; with those edits neither entry absorbs kaidoku ground, ADJ-06 stays open, and no measured axis moves. No installs. Files written: `.ufo/waves/round-61/build/ConnectorKaidokuOverlap.md` (digest taken at integration; read-only seat, no clone patch).
