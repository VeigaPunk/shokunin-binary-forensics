GRADE: PARTIAL — Q13 (`corpus/QUALITY.md:25`) as applied in the C09 entry (HOLDS) and the C04 entry (BROKEN on the credit clause)

Scope: only Q13's two requirements — (a) a verifier/recheck command is credited only for clauses whose deletion its own run is shown to detect; (b) other clauses are named as unguarded — in
`corpus/knowledge/evm-saved-interface-candidates.md` (row C09) and `corpus/knowledge/commonjs-destructured-require-edges.md` (row C04).
Base: landed `ab580698212258a55e43e9bb9bf6ac78c91eae2a`; entries byte-identical to the live tree (`cmp` → IDENTICAL, both files); extracted read-only at `/tmp/revenger-r61w3-W3QualityQ13Apply` via the mandated `git archive`. Verifier sources are unchanged between the mutation base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` and the landed commit (`git diff --stat e0a4b0c… ab58069… -- corpus/verify_evm_evidence.py corpus/verify_js_graph_delta.py corpus/verify_saved_evidence.py` → empty), so the build reports' observations still apply. No REA producer call, no bytecode/JavaScript execution, no RPC, no lane write.

## F1 (HIGH, C04) — the two JS verifiers are credited for a clause whose deletion their own run cannot see
`corpus/knowledge/commonjs-destructured-require-edges.md:202` claims Q13 pass: "the two JS verifiers are credited only for the names and the entry path, whose forgeries their own negatives reject". `:74-77` says the verifiers "guard the names and the entry mapping". Two of the three clauses in that credit fail Q13's deletion test.

Method (independent of the build reports): forge a saved-record field, then delete exactly ONE conjunct of the credited `require(...)` and call the verifier's check function directly (no self-test confound — a self-test `AssertionError` is not a rejection of the forgery). "Mutant ACCEPT" = the check survives deletion, i.e. the clause is unguarded in that verifier's own run.

| verifier clause | forged record | pristine | mutant (that conjunct deleted) | mutant's own `--self-test` |
|---|---|---|---|---|
| `verify_js_graph_delta.py:58` conjunct0 `actual_left == truth_left` | v1 named import `rot13`→`zzz` | REJECT | **ACCEPT** | exit 0 (blind) |
| `verify_js_graph_delta.py:58` conjunct0 `actual_left == truth_left` | v1 second package-entrypoint edge | REJECT | **ACCEPT** | exit 0 (blind) |
| `verify_js_graph_delta.py:47` conjunct1 `main[0]["evidence"]["state"] == "inferred"` | v2 main edge state→`observed` | REJECT | **ACCEPT** | exit 0 (blind) |
| `verify_js_graph_delta.py:47` conjunct0 `len(main) == 1` | v1 second package-entrypoint edge | REJECT | **ACCEPT** | exit 0 (blind) |
| `verify_saved_evidence.py:117` conjunct0 `main["evidence"]["state"] == "inferred"` | v1 main edge state→`observed` | REJECT | **ACCEPT** | exit 0 (blind) |

The credited clauses that DO survive Q13's test: `verify_js_graph_delta.py:58` conjunct1 `actual_right == truth_right` (deletion detected, own `--self-test` exit 1, "altered v2 graph was accepted") and `verify_saved_evidence.py:115` `resolved_path == "index.js"` (deletion detected, exit 1, "JS: altered proof accepted"). So the entry's own negatives cover the *v2 name* and the *v1 entry path* only — not the v1 names, not the entry-edge count, not the `state: inferred` part of the entry mapping that the entry states at `:34-36` ("one `maps_to` edge with `resolution_context: package-entrypoint`, resolved to `index.js`, state `inferred`").
Corroboration already in the lane: `.ufo/waves/round-61/build/MutantJsVerifier.md:18-26` (8/9 mutants survive; only `:58` killed) and `ReviewerOtherVerifiersGap.md` row `Z8` (`verify_saved_evidence.py:114-116 c0 … U`) — the entry cites the first of these only for the JS delta and never names `:47`/`:117`/`Z8` as unguarded. Under Q13's second requirement ("other clauses are named as unguarded"), the entry names only "the v2 digests, edge spans or the unnamed edge" (`:75`); the entry-edge count and the `state: inferred` conjunct are named nowhere.

## F2 (HIGH, C04) — the entry's own recheck command has blind clauses, and the entry credits it for every value
`corpus/knowledge/commonjs-destructured-require-edges.md:3` defines the recheck as "run the `## Reproduce` block … compare with `## Provenance`", and `:202` says every value rests on that block. Under that protocol, a clause is detected only when the block's stdout changes. Deleting one conjunct at a time from the block and diffing stdout against the recorded Provenance (digest lines normalised to `HASH` so the block's own SHA-256 printouts cannot stand in for semantic detection):

- `43:38` conjunct1 and `43:69` `e["properties"].get("resolution_context") == "package-entrypoint"` — **IDENTICAL** stdout when deleted.
- `46:44` `set(named) == src_names` and `46:75` `entry[0]["properties"]["resolved_path"] == src_main` — **IDENTICAL** stdout when deleted.
- `51:150` / `52:150` `e["relation"] == "imports"` (the `v1_named`/`v2_named` delta sets) — **IDENTICAL** stdout when deleted.
The block therefore cannot show the entry-point *kind* (`resolution_context`), the agreement booleans (`agrees_with_source names=… main=…`), or the delta's edge selection changing. These are the values the entry states at `:25-29` (named-import edges), `:30-33` (delta) and `:34-36` (entrypoint edge).

## F3 (MEDIUM, C04) — the block does not detect three drifts it is relied on for
Applying the drift to a copy of the corpus tree and running the block against the recorded Provenance: v1 `maps_to` `resolved_path` → `wrong.js` → **not detected**; v1/v2 `maps_to` edge `state` → `observed` → **not detected**; v1 `index.js` destructuring gains `extra` → detected only via the fixture digest line (`v1 source destructured=…` also changes); v1 `package.json` `main` → `main.js` → detected only via the digest line and the printed `main=` value. The `maps_to` blind spot is the same conjunct as F2 (`43:69`).

## F4 (LOW, C04) — one credited verifier claim is stale relative to the lane's own survey
`:202` says "the two JS verifiers are credited only for the names and the entry path, whose forgeries their own negatives reject". `verify_saved_evidence.py` has no `round-7` reference at all (`grep -c round-7 corpus/verify_saved_evidence.py` → 0), so it cannot reject any v2 forgery; `ReviewerJsVerifierRun.md` records this as defect D4. The v2 clauses are therefore carried by `verify_js_graph_delta.py` alone, which is not stated in the entry.

## F5 (holds, C09) — the EVM entry withholds verifier credit correctly
`corpus/knowledge/evm-saved-interface-candidates.md:85-88` states `verify_evm_evidence.py` "reads r19 only, and its own run detects none of 37 single-conjunct deletions … so under Q13 it is not credited as a guard; all seven fixtures rest on this entry's walk"; `:189` repeats the 0/37 figure. I reproduced the count independently with literal single-conjunct deletion on the extracted tree: 9 spot mutants (`:23` carrier prefix, `:26` carrier digest, `:37` evidence_id, `:41` artifact sha256, `:47` candidate count, `:51` selector equality, `:54` `target == immediate + 9`, `:54` `decoded[target] == 0x5b`, `:59` `runtime_execution`) → **9/9 SURVIVED**, pristine and restored exit 0. This agrees with `.ufo/waves/round-61/build/MutantEvmVerifier.md` ("KILLED 0/37; SURVIVED 37/37") and with the fresh literal-deletion probe in `.ufo/waves/round-61/falsify-w3/W3EvmVerifierCredit.md`. The entry's own walk was re-run from the extracted tree: stdout **identical** to the recorded `## Provenance` (14 lines, exit 0).
Residual (not a Q13 failure of the entry): the EVM block's own blind conjuncts are `23:32` `ins[k - 1][1] == 0x60` (never exercised — every JUMPI in all seven fixtures is PUSH1-preceded, checked by walk) and `33:64` `rec["subject"]["digest"]["sha256"] in (sha(raw), sha(d))` (the only load-bearing conjunct of the block: deleting it hides a forged r19 subject digest). The entry credits the block for every value (`:189`), and no deletion-detection run for the block is recorded in `.ufo/waves/round-61/build/` — the Q13 requirement is not yet met for the block itself, though nothing in the entry overstates a verifier's guard.

## F6 (holds, C04, non-Q13) — no harm to the recorded inputs
`git diff --name-status cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 ab580698212258a55e43e9bb9bf6ac78c91eae2a -- corpus/live corpus/fixtures` → **empty** (no saved record or fixture changed), so the claims.md harm clause "a changed saved record or fixture" is not triggered.

## Residual risk / verification gaps
- Q13 has no machine-checkable form; the criterion's own reject example is a single survivor. I therefore report the criterion as PARTIAL for C04 rather than BROKEN: the over-credit is real and citable, but "the names and the entry path" is a summary phrase, and the one clause the entry's own negative demonstrably covers (`:58` c1, `:115`) is correctly included.
- The `## Reproduce` blocks were mutation-tested by me for the first time; no build-wave seat ran them (`.ufo/waves/round-61/build/MutantJsVerifier.md` and `MutantEvmVerifier.md` cover only the three verifier scripts). My harnesses are at `/tmp/revenger-r61w3-W3QualityQ13Apply/{tbl,lb,twobytwo,final}.py`; they mutate only copies under `/tmp/revenger-r61w3-W3QualityQ13Apply/`.
- `verify_saved_evidence.py` was never mutation-surveyed in this round's build wave before this seat; `ReviewerOtherVerifiersGap.md` rows Z6–Z9 cover parts of it.

VERDICT: PARTIAL — C09's Q13 credit discipline holds (0/37 reproduced; guard credit correctly withheld); C04's Q13 row is BROKEN on the credit clause: `verify_js_graph_delta.py:58` c0, `:47` c0/c1 and `verify_saved_evidence.py:117` c0 are credited for names / the entry mapping although deleting them leaves the verifier accepting the forgery with its own run still exiting 0, and the entry's own recheck block has six deletion-blind conjuncts that are named nowhere.
Installs: none (Python 3.14.8 preinstalled; no pacman/uv/npm transaction).
