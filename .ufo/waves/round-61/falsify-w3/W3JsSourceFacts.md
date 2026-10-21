GRADE: HOLDS — C04 Observation 1 (commonjs-destructured-require-edges.md:20-24) at landed ab580698212258a55e43e9bb9bf6ac78c91eae2a
Scope: Observation 1 only. Observations 2-5 are other seats' items. One header wording nit (line 11) is reported below as PARTIAL.
Setup: landed archive extracted to /tmp/revenger-r61w3-W3JsSourceFacts/landed (git archive tar sha256 c774b23e31657f93c3818cc51eaf6cf53e287819805bdf2534f4ca9f880cab24). Base archives cf02419 and e0a4b0c (fixtures + corpus/live/runs) in base-cf02419/ and base-e0a4b0c/. Own tokenizer, stdlib Python; no JavaScript executed. Live lane tree touched read-only (cmp only).

Findings (observed unless marked):
1. HOLDS — js-r3 line 1 destructures checksum and rot13 from require('./transform').
   `grep -n` -> `js-r3/index.js:1:const { rot13, checksum } = require('./transform');`
   Own tokenizer: require call at line 1 col 29, specifier './transform', names {rot13, checksum}. Entry line 20 lists "checksum and rot13": set-equal; prose order differs from source order, not counted.
2. HOLDS — js-r7-v2 destructures rot13 only.
   `js-r7-v2/index.js:1:const { rot13 } = require('./transform');`; names {rot13}.
3. HOLDS — both package.json: main "index.js", no exports.
   Keys [name, version, main, type]; "exports" absent from the JSON (own check); index.js present in both dirs (Reproduce output: main_file_exists=True).
4. HOLDS — transform.js and package.json byte-identical across the pair.
   cmp exit 0 for both pairs; sha256 transform cd9f3f633355...a345, package 92ef8e3d5d3a...96d7 in js-r3 and js-r7-v2.
5. HOLDS — exactly one require call per fixture.
   Tokenizer require_calls: index.js 1, transform.js 0. `grep -o require | wc -l`: index.js 1 each; package.json and transform.js 0. No import tokens, only module.exports; no CR, BOM or non-ASCII in the six files.
6. HOLDS — Q03/Q06/Q11 for this item.
   Entry Reproduce block (53 lines, extracted) run from the extracted root with `python3 -B`: exit 0. Diff against the `## Provenance` output block (lines 151-179) is empty: 29/29 lines. Provenance digests for js-r3/index.js (f7d8bf47...), transform.js (cd9f3f63...), package.json (92ef8e3d...), js-r7-v2/index.js (b53d96d4...) equal my sha256 of landed bytes.
7. HOLDS — harm check. All 6 fixture files are byte-identical at cf02419, e0a4b0c and ab580698 (12 cmp at base commits). Live corpus/fixtures identical to landed (6 cmp). No fixture changed.
8. Discriminator (mutants on scratch copies, mutants.py). Control m0 passes every clause. Each mutant breaks the clause it targets:
   m1 drop checksum from js-r3 import -> v1 names ['rot13'];
   m2 add "exports" -> 'exports absent: False';
   m3 +1 byte in transform.js -> 'byte-identical: False';
   m4 second require -> 'require calls ...: 2';
   m5 alias `{ rot13: r }` -> v2 names [];
   m6 main "lib.js" -> 'main==index.js: False';
   m8 'use strict' prepended -> 'require line: 2 (claim: 1)'.
   m7 require only in a comment -> still 1 call (correct). The clauses can fail, so the HOLDS verdicts are not vacuous.

PARTIAL (wording; outside Observation 1 text): entry line 11 "`js-r3` and its one-name-removed sibling `js-r7-v2`" understates the sibling delta. `diff js-r3/index.js js-r7-v2/index.js` shows two hunks: line 1 (`, checksum` removed, 10 bytes) and line 5 (`:${checksum(transformed).toString(16).padStart(8, '0')}` removed, 55 bytes); 274 - 209 = 65 bytes. Observation 3 (lines 30-33) and the graph relations (Provenance lines 162 and 172) change only imports 3 -> 2, so no claim is contradicted. Suggested wording: "one imported name removed, with its call site in the return template also removed".
Not counted: entry line 22 writes `"main": "index.js"` with spaces; the bytes are compact `"main":"index.js"`. Prose quoting only.

Observed, not attacked: the same Reproduce run also reproduces the record-side Provenance lines 161-179 on this archive (record sha256 7c3ba8c1..., 331ec252...). Observations 2-5 are other seats' items.

Installs: none (python3 stdlib; git, tar, cmp, grep, diff, od, sha256sum pre-installed).
Scratch: /tmp/revenger-r61w3-W3JsSourceFacts/ — parse_c04_obs1.py (sha256 7486748e...), mutants.py (6e18837d...), harness.py (1f2dd2b3...), reproduce_block.py (287a061d...), repro.out (2936df69...).

VERDICT: HOLDS — every Observation 1 clause re-derived from the bytes by an independent tokenizer, checked against falsifying mutants, and unchanged since cf02419; the only defect is the wording of header line 11 (PARTIAL), which does not void Observation 1.
