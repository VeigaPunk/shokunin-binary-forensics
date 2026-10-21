GRADE: HOLDS — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04), lane R62FJsNameDelta: source-vs-record name deltas, cross-record name-value delta, nameset-not-edgeset, prose/count/array/inventory match, no retained 0/1 comparison-tool claim

# Target identity (frozen)
- frozen candidate revision d97761952be256d145d298022de03091de91d358 (git rev-parse confirmed); pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7; claim base 5bd4a90fc1a34caa94496601b60537b3aab12301
- candidate file corpus/knowledge/round-62-commonjs-require-name-evidence.md sha256 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3 (identical in the d9776195 extract and in the working copy)
- admission-status: candidate (not admitted); README row C04 = uncovered (corpus/README.md:33)
- my scope: the name-set delta claims only (items 10, 12, 13, 14, 15, 25 and the inventory rows they feed). No repair, no admission, no repo/Git mutation.

# Method (archived copies only)
- extracts: git archive a3498e25… -> tree_pre, git archive d9776195… -> tree_cand; cwd=/fast/scratch/hyaku/revenger-r62/R62FJsNameDelta, TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FJsNameDelta/tmp
- entry's own readout.py extracted from the markdown: sha256 31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac (== the entry's claim, entry:76)
- MY derivation: indep.py sha256 81de610929a31e165915f7ee10e40ad8e8762b7fb416d4b6c86d653d94046b50 — independent parser (manual back-brace/paren scan, no shared regex) + direct JSON walk of the records
- no JavaScript executed, no producer call, no network, no verifier source read

# Observation (primary evidence)
1. Entry readout reproduced exactly: `python3 -B readout.py tree_pre` -> exit 0, 25 stdout lines, stdout sha256 58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416 (entry's `recheck:` header, entry:4); `diff` against the §Reproduce stdout block is empty; identical sha from tree_cand and from cwd=/ with an absolute root (path-independence claim, entry:78).
2. Independent within-fixture delta: js-r3 source names {rot13, checksum} vs record imported_name values {rot13, checksum} -> kept ["checksum","rot13"], removed_source_only [], added_record_only []; js-r7-v2 {rot13} vs {rot13} -> kept ["rot13"], removed [], added []. Matches entry:41 (item 12) exactly.
3. Independent cross-record name-value delta: removed ["checksum"], added [], kept ["rot13"], left=js-r3, right=js-r7-v2. Matches entry:42 (item 13); direction confirmed by entry:47 (item 15: checksum is the value js-r3 carries and js-r7-v2 does not).
4. Nameset, not whole edgeset: my contrast run over the same two records gives an edge-id set delta of 3 removed / 2 added / 0 kept — categorically different from the printed name-value answer. The entry's deltas are computed over `imported_name` values only (entry:41-42) and no edge-set delta is claimed (entry:46-47, entry:63 item 25). HOLDS.
5. Counts: js-r3 imports 3 / named 2 / unnamed 1 (record relation counts {contains 6, exposes 2, imports 3, loads 1, maps_to 1}); js-r7-v2 imports 2 / named 1 / unnamed 1 ({contains 6, exposes 2, imports 2, loads 1, maps_to 1}). Matches entry:36 (item 10). No duplicate name values in either record (duplicate_name_values False).
6. Digests/sizes recomputed from the a3498e25 extract: index.js 274 B f7d8bf47…, 209 B b53d96d4…; package.json 85 B 92ef8e3d…; transform.js 379 B cd9f3f63…; records 193573 B 7c3ba8c1…, 171150 B 331ec252… — all match entry:18 and entry:29; byte-identical at d9776195.
7. Source-side spans independently re-derived: js-r3 call [28,50) text `require('./transform')`, pattern [6,25), binding [6,50); js-r7-v2 call [18,40), pattern [6,15), binding [6,40) — match entry:24-25 (items 4-5). Saved record columns: named edges 6->50 / 6->40, unnamed 28->50 / 18->40 — match entry:37 (item 11).
8. Fails-closed claim exercised on mutated archived copies: a second matching require line in js-r3 -> exit 1, `expected exactly one destructured require line, found 2`, 0 stdout lines; an alias pattern `{ rot13: r }` in js-r7-v2 -> exit 1, `found 0`, 0 stdout lines. entry:23 (item 3) and entry:61 (item 23) hold.
9. Old comparison tool 0/1 NOT quietly retained: grep of the candidate for "0/1", "ledger", "comparison tool" hits only the negative guard statements (entry:64-65, :276, :287, :296). The rejected round-61 file's claim ("the round-7 comparison tool did not report it (0/1, recorded in the round-7 ledger)", corpus/knowledge/commonjs-destructured-require-edges.md:33) is absent; the delta is derived in-entry, not inherited.
10. Rejected round-61 candidate byte-unchanged across a3498e25 and d9776195 (sha256 690db9f17ac2e64b35efeb90392fae3401ae8e14c843a1ac4eac6f240ef2a6f3) — entry:67 (item 29) holds.
11. Source rows: corpus/SOURCES.md:43-44 (S029/S030) match the entry headers exactly — anchors §14.3.1.3 / §14.3.3.3 / Table 54 / §16.2.2 Imports, single-page sha256 06db92a8…, tier A, mined, opened 2026-10-21, S030 record digests. entry:1-2 (Q01/Q02 basis) hold.
12. Q11 inventory: every field path cited in the §Sentence-to-output inventory exists in the printed stdout (only `location.*` / `target.*` are pattern forms); every literal in items 1-13 resolves to printed output or to a documented rendering form (interval notation, digest elision, pointer syntax). No unbacked value in the name-delta sentences.

# Findings (severity ordered)
- No material finding; lane target HOLDS.
- F1 (low, non-blocking, disclosure precision): entry:34-35 say the unnamed edge "carries `imported_name` `null`". In the saved records the unnamed imports edge has NO `imported_name` key (indep dump: props_keys = ['expression','kind','resolved_path','specifier']); the printed null is readout.py's `props.get("imported_name")` default, so the stdout cannot distinguish absent from null. Substance ("no name") and every count/delta are unaffected. Under the lesson's directive to audit claims that the block "carries" a field, not just the printed value (corpus/lessons/round-62.md, M27 row), this is the single spot where the sentence outruns the printed value. Minimal clarification L1 may require before admission: say the unnamed edge carries no `imported_name` field (readout prints null) — no re-derivation needed. Not repaired by me.
- F2 (low, wording): entry:29 (item 6) labels bytes/sha256 "recorded fields of the saved files, not re-derived here", while entry:49 (item 17) and readout.py compute them over the record file bytes; the "not re-derived" label belongs to evidence_id/operation/provider and to root_artifact_sha256 (item 7). No value changes.
- F3 (low, convention-dependent count; flagged for the sources seat, not this lane): §Sources calls the S029 quote "8 words"; whitespace tokens = 6, alphabetic words = 6. Non-material — the <=25-word gate holds under every convention.

# Inference
- [INFERENCE] The name-delta claims are reproducible from the frozen bytes and saved records by a code path unrelated to the entry's own readout; the entry's stdout is byte-reproducible and path-independent, so the delta does not depend on the entry's tool being trusted.
- [INFERENCE] The "names, not edges" framing is load-bearing and materially correct: on the same two records the edge-set answer (3 removed / 2 added / 0 kept) differs categorically from the printed name-value answer (removed checksum / added none / kept rot13).

# Unknown / residual risk / verification gaps
- Unknown (declared by the entry, verified consistent): export side (item 19), runtime property presence (item 18), provider root-digest construction (item 7), other packages/versions (item 22).
- Residual risk: the two fixtures cannot discriminate name-set from named-edge-set semantics by cardinality (js-r3 2 named edges / 2 distinct names; js-r7-v2 1 / 1); the name-level scoping rests on the code path and labels, not on a discriminating case.
- Residual risk: coverage rests on 2 authored fixtures and 2 saved records (entry items 22, 28); C04 stays `uncovered` in corpus/README.md:33.
- Verification gap: I did not re-fetch the public ECMA-262 page (outside my lane); the S029 quote was checked against corpus/SOURCES.md:43 and the lesson row, which carry the identical string "Set value to ? GetV(value, propertyName)."
- Verification gap: no LSP server answers this markdown-only lane (no semantic references to resolve); all cross-file claims were checked by direct byte-level comparison.

# VERDICT
HOLDS for the lane target: the source-vs-record deltas, the cross-record name-value delta (removed checksum / added none / kept rot13), the nameset-not-edgeset scoping, and the prose/count/array/inventory match are independently reproduced from the frozen extracts; the old comparison tool's 0/1 is not retained. F1 is the only wording item L1 may want as a one-clause clarification before admission; it changes no printed value, no count and no delta. Recommendation only — no admission, repair or integration performed by this seat.

Installs: none (Python 3 standard library only; no package, tool or system change).
