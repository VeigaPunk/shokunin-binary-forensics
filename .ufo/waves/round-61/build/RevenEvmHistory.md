# RevenEvmHistory — round 61, C1/C09 EVM history (read-only)

Seat RevenEvmHistory (leaf; no dispatch). Paths are lane-relative to `/home/vgpnk/Projects/shokunin/revenger-shokunin`; `LOG:n` = LOG.md line n. Checks: read/grep/glob; `sha256sum`, `stat`, `xxd -p` on `corpus/fixtures/evm-*`; `git --no-pager log|show --stat` (read-only). Not run: REA, verify_evm_evidence.py, bytecode execution, clones, builds. Only file written: this report. Installs: none.

## A. Rounds 19–26: declared, fixture, REA Evidence, observed, review, halt

| R | LOG decl→result | Axis · AFTER test (LOG decl) | Fixture · sha · truth | REA Evidence (evmole@0.9.3; CLI rea-agents@6.4.0 per LEDGER:5) | Observed | Non-author review (reviewer.md) | Refusal / falsification / halt |
|---|---|---|---|---|---|---|---|
| 19 | 227→233-236 | coverage · candidate "at the corresponding byte offset" (:229) | hex text 39 B, 294e6fd2…; decoded 18 B, d1086bce…; truth has no destination field | ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 | 1 candidate 0xdeadbeef, destination 16 = JUMPDEST (not selector offset) | evm-selector-review (:231) → reviewer.md:19 coverage narrow | none; AFTER wording unmet literally (:229 vs :235) |
| 20 | 238→244-247 | calibration · verifier over saved r19 Evidence (:240); no fixture declared | none; no REA call | none (reads r19 ID) | self-test exit 0: POSITIVE + NEGATIVE REJECTED (LEDGER:3-8) | evm-proof-review (:242) → reviewer.md:7 gap, :9 patched | reviewer-found gap fixed before commit (:246); no refusal |
| 21 | 249→255-258 | coverage · raw encoding parity (:251) | raw 18 B = r19 decoded, d1086bce… | ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85 | 1 candidate 0xdeadbeef, destination 16 | evm-raw-review (:253) → reviewer.md:3 | none; "second carrier encoding, not a second bytecode" (reviewer.md:3) |
| 22 | 260→266-269 | depth · two branches, no extra (:262) | raw 34 B, 94c1790f…; truth.json:1-22 | ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b | 2 candidates: aaaaaaaa→30, bbbbbbbb→32 | evm-two-branch-review (:264) → reviewer.md:24-26 | none |
| 23 | 271→277-280 | calibration · bare PUSH4 negative (:273) | raw 7 B, 8047ddff…; comparison_or_jump false | ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201 | 0 candidates | evm-negative-review (:275) → reviewer.md:9 | none; one control only (LEDGER:5) |
| 24 | 282→288-291 | calibration · PUSH32 immediate decoy (:284) | raw 35 B, b69834e0…; embedded_pattern_offsets [1,9] (a range) | ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e | 0 candidates | evm-immediate-review (:286) → reviewer.md:3,9 | none; one decoy only (:290) |
| 25 | 293→299-302 | calibration · entry-STOP reachability (:295) | raw 19 B, 2d87a4e2…; jump_target_valid false (truth.json:10) | ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579 | 0 candidates; cause unknown (LEDGER:5) | evm-stop-review (:297) → reviewer.md:9,19 | premise "valid jump destination" falsified (:295); NOT ADMITTED (:302) |
| 26 | 304→310-315 | calibration · one-byte operand 0x10→0x11 (:306) | raw 19 B, ebe2d675…; truth has no expected output | ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090 | 0 candidates; static decode has valid PUSH4→JUMPDEST 17 (reviewer.md:9) | evm-stop-control-review (:308) → reviewer.md:9,14,17 | operator pause "round 26 closed, no round 27" (:315); reason not recorded |

Refusal scan (grep `refus|declin|halt|falsif|not admitted|could-not|blocked|confound`, each of the eight run folders): matches only in round-25 and round-26 ("confound" wording). No refusal text in r19–r26. Seven Evidence records exist (r19, r21–r26); r20 has none.

## B. Why there is no evm-r20

- Declared move: calibration, a read-only verifier over saved r19 Evidence (LOG:240). Declared scope: "r19 fixture truth and saved REA Evidence plus r20 verifier/receipt" (LOG:242). No fixture, no REA call.
- Artifacts: `corpus/verify_evm_evidence.py` and `corpus/live/runs/round-20/{LEDGER,reviewer}.md`; no inspection.json or inspection.stderr in that run folder (glob).
- Git: `git log --all -- corpus/fixtures/evm-r20` is empty: never committed, not deleted. Commit 21aac22 (2026-10-12) = LOG.md +11, SCORECARD.md, round-20 receipts, verifier; no fixture.
- The lane already names the gap: corpus/README.md:35 "(no `evm-r20`)"; `.ufo/waves/kaika-r1/planner.md:80` "sparse shorthand … (no evm-r20 fixture); the verifier exists"; claims.md:23-24 lists r19, r21–r26. Write "r19, r21–r26", not "r19…r26".

## C. Provenance and version facts

- REA version: rea-agents@6.4.0 appears only in ledger prose (LEDGER:5 in r19, r21–r26); no saved inspection.json names it (grep, no matches). Records name only provider `evmole-interface` / `evmole@0.9.3`. Pin chosen at mint (corpus/knowledge/2026-10-12-rea-readiness-checklist.md:14). The 2026-10-19 re-check gives skill pin 6.7.0 (:37) and host MCP 6.5.0 (:38); no run used either.
- Path drift: all seven Evidence records carry `subject.local_path` / `parameters.path` = `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-rNN/…`. The lane has no `.shokunin/` (glob: skipped). SCORECARD.md:160 records Evidence IDs as path-sensitive (content+path+params).
- All seven records: `authority: shipped-artifact`; `evidence_kind`/`confidence` inferred; `discovery_completeness` unknown; `runtime_execution` not-performed. Limitation text: "Empty results do not prove the absence of callable dispatch."
- Bytes re-derived read-only: carrier and decoded sha256/sizes match every LEDGER (r19 39 B; r21 18 B; r22 34 B; r23 7 B; r24 35 B; r25 19 B; r26 19 B). No authored carrier contains opcode 0x34 (CALLVALUE). No truth.json (r19, r21–r26) declares a function signature.
- "exit 0" and "no install": ledger prose; reviewers could not authenticate them (reviewer.md r23:6, r24:6, r25:13). `npx -y` may fetch the package when uncached [INFERENCE; cache state unrecorded], against "No provider install" (LOG:230).
- Non-author status rests on LOG spec lines only (e.g., LOG:231 "reviewer, `openai-codex/gpt-6-sol`"); reviewer.md files record no identity.

## D. History claims the C09 entry must NOT repeat as fact

1. REA "recovers" ABI functions, signatures, arguments or `payable`. These are upstream inferences (Evidence limitations); the bytes contain no CALLVALUE guard that would produce `payable` [INFERENCE on REA's default].
2. `bytecode_offset` / `bytecodeOffset` is a selector or PUSH4 location. It is the JUMPDEST destination (LOG:235; LEDGER r19:3; reviewer.md r19:13).
3. r19 met its AFTER test. LOG:229 requires the candidate "at the corresponding byte offset"; REA reported destination 16. LOG:236 reads "corresponding" as destination.
4. Empty output = "no interface" or "REA ignores X". Completeness is unknown in all seven records.
5. Specificity or false-positive rate. One negative per class (LOG:279, LOG:290); LOG:279 disclaims any rate.
6. Entry STOP causes suppression, or REA is reachability-aware. r25 is confounded (LEDGER r25:5 "cause is unknown"); r26 is empty with a valid operand (LEDGER r26:5; reviewer.md r26:14).
7. r26 is a "controlled negative". truth.json:1-11 has no expected output; the label is post-hoc (LEDGER r26:7). Its static decode has a valid PUSH4→JUMPDEST 17 (reviewer.md r26:9). Call it a non-report; whether it is a false negative depends on whether behind-STOP code counts, which is unresolved.
8. r25 is a valid-target STOP control or a calibration success. truth.json:10 `jump_target_valid: false`; LOG:302 "Not admitted". Commit 7f8748c is its only commit and already holds the corrected truth, so no pre-correction version exists in git; the premise survives only in LOG:295.
9. r21 is an independent bytecode. It has the same 18 decoded bytes as r19 (reviewer.md r21:3,5). Distinct positive bytecodes: 2 (r19, r22); selector→destination pairs: 3.
10. The verifier covers r19–r26 or authenticates REA. verify_evm_evidence.py:10-11 hard-code r19; :12 and :37 compare a constant ID; the only negative mutates the normalized offset (:68) and is rejected at :53, not at the relation (:54-55); no producer authentication (LOG:246). No committed check covers r21–r26; REPLAY.md and replay_fixtures.py have no EVM reference (grep).
11. `.shokunin/revenger/…` (LOG, ledgers) or the prymeagnt Evidence path as lane locations. Cite `corpus/…` plus SHA-256 and name the Evidence path as prymeagnt's.
12. Destination 16 is "in truth.json" (LOG:234 cites it). truth.json:1-11 has no destination field; it lives only in verify_evm_evidence.py:54 and LEDGER r19:3.
13. r24 `embedded_pattern_offsets: [1, 9]` as two match offsets. It is an inclusive range (LOG:289 "offsets 1–9"); byte 9 is 0x57 (xxd).
14. "EVM family" as coverage. LOG:736 and LOG:755 are a presence census; LOG:755 says "a presence probe, not a clean admission gate or capability proof".
15. `authority: shipped-artifact` as fixture provenance. It is REA's label; the fixtures are lane-authored (LOG:228-229).
16. rea-agents@6.7.0 as the version used. It is the 2026-10-19 skill pin (checklist:37); all runs used 6.4.0, ledger prose only.
17. "standing-loop round N" = corpus round N. LOG:227 "standing-loop round 7" is corpus round 19.
18. An admissible EVM source exists. corpus/SOURCES.md has no EVM, Keccak or bytecode row (grep); corpus/knowledge has no EVM entry (listing). ScribeEntryEvm.md:10-12 agrees: Q01 fails.

## E. First falsifiers from the history (designs only; none run)

- F1 (halt vs shift): r19 with a leading `5b` (non-halting JUMPDEST) and operand 0x11 (JUMPDEST 17). A candidate reported means the r26 empty result tracks the halting STOP; still empty implicates the shift or another cause, not the STOP. This separates the two hypotheses that r25/r26 cannot.
- F2: commit a negative that mutates only the raw `bytecodeOffset`; the committed self-test mutates only the normalized field (verify_evm_evidence.py:68). The reviewer's raw+normalized double mutation (reviewer.md r20:3) is not in the verifier.
- F3: declare expected candidates in truth.json before any new REA call, so "negative" is not assigned after the output is seen (r26 has none).

VERDICT: evm-r20 is a verifier-only calibration round, never committed as a fixture; the seven r19–r26 Evidence records match the bytes, and the C09 entry may say only "candidates on r19/r21 (same bytes) and r22; empty on r23–r26; causes unknown" — no selector location, completeness, ABI, STOP suppression, or rate. Installs: none.
