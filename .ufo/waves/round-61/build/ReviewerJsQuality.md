# ReviewerJsQuality — round 61 C04 pre-gate (read-only)

Seat CloseChousa26.ReviewerJsQuality-10 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a · access 2026-10-21 · scope C04 only (C09 and C2 not gated). Axes: coverage (K_HELD 4/14; C04 row `uncovered`, corpus/README.md:30). Admitting C04 alone predicts K 5/14 (claims.md:38-39); admitted today: 0.

## Candidate status
- No C04 entry exists: corpus/knowledge/ holds 6 files, none JS (`ls corpus/knowledge`). No r61 clone holds a js/node/cjs/electron-named knowledge file (`ls /tmp/revenger-r61-*/corpus/knowledge | grep -iE 'js|node|cjs|electron'` → empty). The only ScribeEntryJs artifact is /tmp/revenger-r61-ScribeEntryJs-repro.py (a draft).
- Below = what the entry must carry. corpus/lessons/round-61.md is absent; registry ends at S015 (SOURCES.md:29).

## Per-criterion pre-gate (QUALITY.md:13-23)
- Q01 sources. MUST: ≥1 round-61 row per load-bearing claim, tier A for that scope (CORPUS.md:93-97). STATUS: fails until rows land (S001–S015 cover no JS, Node or ECMA text). Scope traps: "named import" is REA vocabulary (`imported_name` on analysis.json edges), not Node/ECMA terms; esm.html "CommonJS Namespaces" covers ESM `import` of CJS ("when importing CommonJS from an ECMAScript module") and cannot support CJS `require` destructuring. ECMA-262 destructuring: no row; not opened here.
- Q02 headers. MUST: `source:` (S### + URL + heading), `verified-at: 2026-10-21`, `recheck:` command with inline expected output, `coverage-map: C04`. Exemplars: pe-resource-directory-layout.md:1-6; utf16-unpaired-surrogates-in-resource-names.md:1-7; digest-scope-versus-provenance.md:1-7; tool-validation-by-function-and-version.md:1-8. Trap: fetched Node HTML has 0 `id="…"` attributes, so `#fragment` anchors are unverifiable; cite heading text + page revision.
- Q03 independent expectations. MUST: named set and main derived from fixture bytes. Two methods agree: regex (verify_js_graph_delta.py:23) and acorn 8.19.0 AST (my run, no execution): js-r3 destructures {checksum, rot13} at line 1; js-r7-v2 {rot13}; main "index.js" exists. Trap: ScribeEntryJs-repro.py:48-50 derives the removed delta from saved records; print the source-derived delta beside it.
- Q04 tool claims. MUST: `rea-agents@6.4.0` `analyze-javascript-application` → provider `rea-javascript-application` v1 (analysis.json top-level `provider`). Do NOT credit compare: provider `rea-javascript-application-workflows` v1 returned 15 items, 0 naming checksum (`15 0`); round-7 LEDGER:17 scores 0/1. Removed-checksum delta is manual/verifier-side and must be labelled (M02).
- Q05 capability. n/a only if the entry says "saved record contains …". Any "REA detects/emits" is a capability claim: no producer call is in scope, the 2026-10-12 run is an older probe (M19), current pin is 6.7.0 (seed.md:60). Fails if present tense.
- Q06 fixture premises. MUST byte-verify before stating premises: js-r3/index.js f7d8bf47…, transform.js cd9f3f63…, package.json 92ef8e3d…; js-r7-v2/index.js b53d96d4… (= round-7 LEDGER:5). `cmp`: js-r7-v2 package.json and transform.js identical to js-r3 (exit 0). Round-7 `invalid_request` input (LEDGER:6) is not retained; cite only as "not retained".
- Q07 predictions. n/a: claims.md:19-40 pre-registers no C04 parser prediction, and no producer calls are in scope. FA1–FA6 below are checks on saved bytes, not predictions. Causes (why compare missed checksum) stay UNKNOWN (LEDGER:13).
- Q08 counts. Superseded by Q11 (QUALITY.md:23); apply at entry level (M20, round-1.md:129-131).
- Q09 digests. Bind bytes only. Observed: analysis.json 7c3ba8c1…, v2-analysis.json 331ec252…, comparison.json f6c9a3cd…. REA subject digests 8eec9ffb… (v1) / 696c2496… (v2) are recorded only; r3 LEDGER:5 gives no method. No origin or authenticity claim (M13); records stay byte-preserved (M11).
- Q10 scope. MUST: analyze_javascript_application; 2 authored fixtures; specifier ./transform; main index.js. OUT: ESM, dynamic require, property access, renames, multi-line destructuring, Electron (r3 LEDGER:6: electron-main is a convention), ASAR, runtime, shapes-r12 (outside claims.md C04 scope). Cross-lane: kaidoku/revenger overlap (ADJ-06) is L0: name it, do not absorb (SCORECARD.md:136; round-1-verifier-spotcheck.md:17).
- Q11 in-entry derivations. MUST: `## Provenance (Q11, appended 2026-10-21)` with command + output per value (pattern pe-resource-directory-layout.md:172-265). Commands to embed: sha256sum of fixtures and records; `stat -c %s`; `cmp`; python json read of evidence_id, provider, edges, statistics; acorn listing. Values re-derived here: v1 13 edges (imports 3 = 2 named + 1 unnamed); v2 12 edges (imports 2 = 1 named + 1 unnamed); parsed_javascript_files 2; visited_ast_nodes 136 (v1; r3 LEDGER:6) and 120 (v2); edge evidence.confidence `high` for imports and maps_to; contains 5 observed + 1 inferred, others inferred (both records).

## Node/ECMA quotes (verbatim; fetched 2026-10-21; page title "… | Node.js v26.12.1 Documentation")
- packages.html › "Package entry points": "The "main" field is supported in all versions of Node.js, but its capabilities are limited: it only defines the main entry point of the package." (25 words)
- modules.html › "Folders as modules" (Stability: 3 - Legacy): "then Node.js will attempt to load an index.js or index.node file out of that directory" (15 words; applies when main is missing or unresolvable)
- modules.html › "All together" (LOAD_AS_DIRECTORY pseudocode): "Parse X/package.json, and look for "main" field." (7 words)
- esm.html › "CommonJS Namespaces": "a heuristic static analysis is performed against the source text of the CommonJS module" (14 words; ESM-import scope)

## Findings
- F1 ScribeEntryJs-repro.py:48-50 derives the delta from saved records, not source (M06). Run in a /tmp copy: `delta named removed=['checksum'] added=[] kept=['rot13']`, all record-derived.
- F2 corpus/README.md:9 says QUALITY Q01–Q10; QUALITY.md:23 defines Q11. Exemplar QUALITY tables stop at Q10 (pe…:161-170; utf16…:108-117; digest…:105-114; tool-validation…:102-111). The C04 table needs Q01–Q11.
- F3 verify_js_graph_delta.py:23-24: regex matches only one-line, column-0 `const {…} = require('…');`; multi-line or aliased forms fail at :24 or mis-parse. State as a method limit.
- F4 `ls -la` of js-r3, js-r7-v2, shapes-r12: no truth.json (40 exist elsewhere under corpus/fixtures). C12's truth.json convention (tool-validation…:19-22) does not cover C04 fixtures.
- F5 round-7 LEDGER:4-5 and r3 LEDGER:4-5 cite `.shokunin/revenger/…` and prymeagnt paths; PROVINCE.md:30-31: historical paths identify imported evidence only. Use `corpus/…` locators.

## First falsifiers (predicates on saved bytes; none fired)
- FA1 destructured name absent from source: none (regex and acorn agree).
- FA2 record names differ from source names: none (`agrees_with_source names=True`, both).
- FA3 package main missing on disk: none (`main_exists True`).
- FA4 record coverage not complete: none (complete, omitted 0, both).
- FA5 named import not state=inferred: none (imports inferred: 3 v1, 2 v2).
- FA6 destructured name not exported by transform.js: none (acorn module.exports keys rot13, checksum at line 12).
These test saved records only; they are not REA capability tests.

## Gaps before admission
- corpus/lessons/round-61.md `## Gate` absent: needs URL, access date, ≤25-word quote, location per row (CORPUS.md:112-115).
- SOURCES rows S016+ needed: Node packages, modules, esm (tier A for their scope only); ECMA-262 destructuring (open and quote); own-work rows for the two saved records (pattern SOURCES.md:27). E11 requires used-by paths on disk (sources-census.sh:567).
- README row flips uncovered → held only for an admitted entry (claims.md:33-34).

Installs: acorn@8.19.0 via npm (official registry) into /tmp/revenger-r61-ReviewerJsQuality-tools; reason: independent AST oracle for Q03; no global install. Node v24.21.0 / npm 11.19.0 pre-existing.
Writes: this report only, plus /tmp scratch (derive.cjs; tree/ = cp copies of fixtures and two saved run dirs). No lane write, no git/jj mutation, no REA call.

VERDICT: no C04 candidate exists; it cannot clear the gate until Q01 (round-61 Node/ECMA rows with in-Gate quotes), Q02 (headers + Q01–Q11 table), Q03 (source-derived delta printed) and Q11 (in-entry commands) hold; Q05 and Q07 are n/a only while the entry stays on saved-record observations.
