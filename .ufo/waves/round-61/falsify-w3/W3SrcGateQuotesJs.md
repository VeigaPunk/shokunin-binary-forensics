GRADE: HOLDS — Gate quotes for S020–S023 (corpus/lessons/round-61.md:59-62), attacking C1's C04 admission

Seat: RevengerR61-2.W3SrcGateQuotesJs. Landed state ab580698212258a55e43e9bb9bf6ac78c91eae2a (archive extracted to /tmp/revenger-r61w3-W3SrcGateQuotesJs). No lane/jj/git mutation; read-only git archive.

Method (observed, 2026-10-21): `curl -sS` each URL today; HTTP 200; sizes 161249 / 156551 / 137245 / 7629271. Each fetch is byte-identical to the copy the round-61 seat saved, so the check runs on the round's own opened bytes, not a drifted page:
- modules.html sha256 b35916f2…ed79c2a90edd == /tmp/node-modules-r61.html and /tmp/revenger-r61f-ReopenS020-modules.html
- packages.html be108e419f61…5fc0a9ad2ae4 == /tmp/revenger-r61-SrcNodePackageMain-page.html
- esm.html f3d3f9c9…bb213301a162b208d == /tmp/r61-esm.html (equals body sha256 recorded in .ufo/waves/round-61/build/SrcNodeCjsLexer.md:7)
- ecma262.html 06db92a8331a…2398f27d7f == /tmp/revenger-r61-src-ecma/front.html
Headers today: node last-modified Wed, 21 Oct 2026 07:34:29 GMT (same as seat records); tc39 last-modified Mon, 19 Oct 2026 16:26:55 GMT, etag 6ad644cf-7469d7 vs seat 16:26:53 / 6ad644cd-7469d7 — header drift only, body hash identical, no quote impact.

Verification (rendered text = tags stripped, entities unescaped, whitespace collapsed; match = contiguous substring):
| row | line | words | stated section re-located | match |
|---|---|---|---|---|
| S020 | :59 | 25 | "File modules" h3, id=file-modules 97573 < quote 97658 < next h3 99256 | exact, 1× |
| S021 | :60 | 23 | `"main"` h4, id=main 142995 < quote 144040 < next h4 145609 | exact, 1× |
| S022 | :61 | 6 | §14.3.3.3 id=sec-runtime-semantics-keyedbindinginitialization 3285692; SingleNameBinding steps 1 `Let name…`, 2 `Let lhs…`, 3 `Set value…`; multipage mirror clause 667558 shows same step 3 | exact |
| S023 | :62 | 19 | "CommonJS Namespaces" h4, id=commonjs-namespaces 67724 < quote 80489 < next h4 80935 | exact, 1× |

Version pins hold: node pages carry `node-version content=v26.12.1` (rows' "v26.12.1", corpus/SOURCES.md:34,35,37); ecma h1 "Draft ECMA-262 / October 16, 2026" (S022 row, SOURCES.md:36). Access date 2026-10-21 matches :50 and the `opened` column.

HTML line-break / character artefacts found — all whitespace-class; no word, case or punctuation change:
- S020 raw `load the\nrequired filename` and `finally\n<code>.node</code>` (modules.html:97658); quote joins with single spaces, rendered text identical.
- S021 raw `imported by name\nvia a <code>node_modules</code> lookup.  Its value is a path.` (packages.html:144040) — newline plus DOUBLE space after "lookup."; HTML collapses to one space; rendered identical.
- S022 raw `Set <var>value</var> to ?\xa0<emu-xref …>GetV</emu-xref>(<var>value</var>, <var>propertyName</var>).` (ecma262.html:3288201) — NBSP U+00A0 after `?` (ecmarkup AO-call convention) and inline <var>/<emu-xref>; quote uses U+0020; rendered identical.
- S023 raw `but does not\nalways correctly detect` (esm.html:80489) — newline; rendered identical.
No quote inserts an ellipsis or changes a word; each is a contiguous substring of the collapsed rendered text.

Non-breaking observations:
- S020 is exactly at the cap: 25 whitespace tokens against the rule "at most 25 words" (:50); passes at the limit (a tokenizer splitting `Node.js` would read 26).
- :60 wraps the sentence in `"…"` while the sentence itself contains `"main"`; delimiter ambiguity only — the quoted characters are verbatim.
- :61 itself discloses S022 was "not re-opened by L1"; my independent open today confirms quote, step and section on both single-page and multipage forms.
- S022's sentence also occurs at §13.15.5.3 and §13.15.5.6 (destructuring assignment); the stated SingleNameBinding step 3 location is correct.
- Scope note: S020's quote grounds the LOAD_AS_FILE `.js`/`.json`/`.node` clause of the row's `teaches` but not the folder fallback; S021's grounds the `main` clause but not exports precedence. Both unquoted clauses are verbatim on the re-opened pages — "If there is no package.json file present in the directory, or if the "main" entry is missing or cannot be resolved, then Node.js will attempt to load an index.js or index.node file" (modules.html #folders-as-modules) and "The "exports" field, if it exists, takes precedence over the "main" field when importing the package by name." (packages.html, immediately after the quoted sentence) — so neither row nor entry overstates; the one-quote-per-row rule (fleet .ufo/waves/kaika/SOURCES-CONTRACT-v1.md:46-48) is met.
- Entry side: corpus/knowledge/commonjs-destructured-require-edges.md:62-63 quotes "does not always correctly detect named exports" (S023), a verbatim substring; S020–S022 appear there as paraphrase with anchors, no quotation marks.

Negative sweep: all lesson lines naming S020–S023 or the four URLs are :52 and :59-62 (plus rejection table :83, a candidate wording, not a source quote); no other down-quoted sentence attributed to these rows.

VERDICT: HOLDS — four for four gate quotes re-open verbatim at the stated sections, 6–25 words, against byte-identical copies of the round's own fetched pages; only whitespace-class HTML artefacts, no mismatch and no row/entry overstatement.

Installs: none (curl/python3 already present; no pacman, uv, npm or cargo action).
