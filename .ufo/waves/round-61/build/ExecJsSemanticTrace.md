# ExecJsSemanticTrace — round 61 · C1/C04 · RUNS (read-only, scratch)

Seat CloseChousa26.ExecJsSemanticTrace-10 · 2026-10-21 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (`git rev-parse HEAD` in clone).
Clone /tmp/revenger-r61-ExecJsSemanticTrace: `git status --porcelain --ignored` empty after all runs (logs/clone-status.log, 0 lines). Scratch /tmp/revenger-r61-ExecJsSemanticTrace-scratch, logs in logs/. Lane: read-only (one `git rev-parse --verify`). No REA calls; no JavaScript run (acorn/eslint-scope parse only).

## 1. Fixture and saved records (sha256 from clone)
- fixtures/js-r3: index.js 274 B f7d8bf47…869fd7 · transform.js 379 B cd9f3f63…caa7fa345 · package.json 85 B 92ef8e3d…ea1096d7 (`"main":"index.js"`).
- corpus/verify_semantic_trace.py 088d2062…864b8527 (same bytes in lane and clone).
- live/runs/20261012T164357Z/: analysis.json 193573 B 7c3ba8c1… (parent ev_4a93…c1c7e), LEDGER.md.
- live/runs/round-14/: trace.json 10698 B c78066f4… (ev_5332…95a8a); trace-request.json 342689 B c4b52e43… (embeds full parent; query keys allowed_relations, direction, seed); trace.stderr 0 B; LEDGER.md; reviewer.md.

## 2. Commands and outputs (verbatim; MATCH lines merged; logs/ retained)
$ python3 -B corpus/verify_semantic_trace.py --self-test   [logs/selftest.log, sha fc64c9a1]
POSITIVE ev_53329396d6fe4843b89806ef1ed98b6db8358ec91c41c733d617ea846b995a8a 3/3 returned captures match source tokens and saved parent; partial static trace only
NEGATIVE REJECTED relation differs from source parent
SELFTEST_EXIT=0
$ node derive_captures.js <clone>   [logs/derive.log, sha 801ea082]
DERIVED render scope.through = defaultInput@3:24-3:36, rot13@4:22-4:27, checksum@5:30-5:38
INFO transitive (every enclosing function) count = 2 ; direct count = 5
INFO transitive record transform.js rot13 2:0-4:1 captures alphabet at 3:46-3:54  (and at 3:56-3:64)
MATCH saved parent captures (graph-wide) == direct derivation :: saved=5 derived=5
MATCH round-14 trace relations == direct derivation for render :: trace_relations=3
MATCH binding ranges rot13 1:8-1:13, checksum 1:15-1:23, defaultInput 2:6-2:18; seed render 3:0-6:1
MATCH destructured import rot13 and checksum <- ./transform :: declarator 1:6-1:50, resolved_path transform.js; require call 1:28-1:50
MATCH package.json main -> maps_to index.js (package-entrypoint); digests index.js and package.json match saved artifacts
RESULT: ALL MATCH (exit 0; 12 MATCH lines in log)
$ parent-ledger one-liner on analysis.json (clone, python3 -B -c)  -> True   [logs/parent-ledger-check.log, sha a9ac0c3a]

## 3. First falsifiers (falsify_semantic_trace.py; parent and request resynced when altered; logs/falsify.log, sha 2e6c2399)
F0 control, unaltered: ACCEPTED
F1a trace-only relations[0] column -> 0 (self-test style): REJECTED "relation differs from source parent" (guard :68-71, not the token guard)
F1b same in trace+parent+request: REJECTED "relation source token mismatch" (token guard :75-77 is live)
F2 extra trace query key max_depth: ACCEPTED (request binding is one-directional, :30-31)
F3 rot13 binding declaration range -> col 0 in trace+parent: ACCEPTED (destructured-require binding ranges unasserted)
F4 captures context state inferred -> observed in trace+parent: ACCEPTED (epistemic state unasserted)
F5a index.js 'amber' -> 'Amber', records stale: exit=1 "ValueError: node or source digest mismatch" (:53-54)
F5b index.js line 4 shifted one column, index.js digests re-hashed in parent/trace/request: exit=1 "ValueError: relation source token mismatch"
F6 transform.js 0x13579bdf -> 0x13579bde: exit=0, self-test output unchanged (transform.js never read)

## 4. Derivation facts
- render (index.js:3-6) direct captures = {defaultInput 3:24-36, rot13 4:22-27, checksum 5:30-38} = verifier pin :79 = its 3 saved relations. Each name occurs once on its source line (index.js:3,4,5).
- REA "captures" = references resolved outside their innermost enclosing function. Saved graph: 5 = 3 (render) + 2 (alphabet inside the transform.js arrow). A transitive reading would add 2 more (rot13 -> alphabet) that REA does not emit.
- rot13/checksum bind from `const { rot13, checksum } = require('./transform')` (declarator 1:6-50; require call 1:28-50).

## 5. Which JS facts the verifier supports
SUPPORTED, guarded by verify_semantic_trace.py:
- render has exactly three resolved captures: checksum 5:30-38, rot13 4:22-27, defaultInput 3:24-36 (:64-80).
- index.js bytes = trace node artifact digest f7d8bf47… (:47, :53-54); trace is partial, captures-only, index.js-only (traversed_modules 1, :42-44).
SUPPORTED by saved records plus my derivation, NOT by this verifier (F3 accepted):
- CommonJS destructured-require named imports and require('./transform') -> transform.js (parent graph.edges imports; 20261012T164357Z/LEDGER.md:11-12).
- package.json main -> index.js as maps_to (parent graph.edges; LEDGER.md:13).
NOT supported by anything tested: transform.js contents (F6), call or runtime behaviour, the `r3:` output value (LEDGER.md UNKNOWN row).

## 6. Conflicts to resolve before any C04 entry
- round-14/LEDGER.md:9 labels the captures "OBSERVATION of REA static trace"; their saved context jsrg_evidence_ef1e… is `state: inferred, authority: static-relationship-inference, confidence: high` (trace.json evidence_contexts[1]). Label them inference.
- maps_to extractor operation is `resolve-electron-entrypoint` (analysis.json graph.edges). 20261012T164357Z/LEDGER.md:6 calls it a convention; the fixture has no Electron field. Do not claim Electron.
- Trace query carries `expected: null` and `include_ambiguous_dynamic_edges: false`; the request query has neither (F2). Subject digest 8eec9ffb… (trace-request.json:4-8) is not re-derived; its scheme is unestablished.

## 7. Recommendations (not applied; lane owner decides)
- Verifier: add a parent-consistent negative (F1b) and assertions on binding ranges and state; make request-query binding bidirectional (the request then carries all five trace query keys).
- C04 import and main facts need their own in-lane recheck command (Q02); verify_semantic_trace.py cannot serve as it.

## Installs and files
- npm, local to scratch only: acorn@8.19.0, eslint-scope@9.1.2 (npm registry; reason: independent scope analysis). Already present: node v24.21.0, npm 11.19.0, Python 3.14.8, git. No pacman, uv or global installs.
- Scratch files written: derive_captures.js, falsify_semantic_trace.py, logs/*.log, drift-* copies, node_modules/, npm-install.log. Nothing written in the clone or lane except this report.

VERDICT: verify_semantic_trace.py supports only the three render-capture facts (index.js lines 3, 4, 5; this fixture; partial trace), which an independent AST derivation also reproduces; the destructured-require, package-main and transform.js facts are unguarded (F3, F6), so C04 needs a separate in-lane recheck.
Installs: acorn@8.19.0 and eslint-scope@9.1.2, npm-local to scratch.
