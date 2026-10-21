# SrcNodeCjsRequire — C1/C04 source opening: Node.js CommonJS require resolution

Seat `CloseChousa26.SrcNodeCjsRequire-10`; read-only; round 61 only. Wrote only this report. No installs. Scope: the `require()` resolution pseudocode on the page, not destructuring semantics or bundler behavior.

## Opened
- URL `https://nodejs.org/api/modules.html`; `curl -sS -D - -o /dev/null --max-time 30 https://nodejs.org/api/modules.html` → `HTTP/2 200`, `content-type: text/html; charset=utf-8`, `content-length: 161249`, `etag: "d64a55b4c2e2034b250cbd534575bb43"`, `last-modified: Wed, 21 Oct 2026 07:34:29 GMT`, `cf-cache-status: HIT`, `age: 2271`.
- Page version: `<title>Modules: CommonJS modules | Node.js v26.12.1 Documentation</title>`; `<meta name=nodejs.org:node-version content=v26.12.1>`; canonical `<link rel=canonical href=https://nodejs.org/api/modules.html>`. No on-page publication/revision date (raw-HTML search found none). Release date: `curl -sS https://nodejs.org/dist/index.json` → `[('v26.12.1', '2026-10-21'), ('v26.12.0', '2026-10-14')]`.
- Fetched bytes: sha256 `b35916f2cc28629dafa7d4e9b9825fc51acbe3bf76f6a4c9fed4ed79c2a90edd`, 161249 B.
- Anchors present in raw HTML: `#all-together` (the require algorithm), `#file-modules`, `#folders-as-modules`, `#loading-from-node_modules-folders`.

## Quotes (verbatim; inline `<code>` markup removed, whitespace normalized; HTMLParser exact-substring check)
- Q1 `#all-together`, require(X) step 3 (19 tokens): `3. If X is equal to '.', or X begins with './', '/' or '../' a. LOAD_AS_FILE(Y + X)`
- Q2 `#file-modules`, first paragraph (25 words): `If the exact filename is not found, then Node.js will attempt to load the required filename with the added extensions: .js, .json, and finally .node.`
- Q3 `#all-together`, LOAD_AS_DIRECTORY step 1 (13 words): `If X/package.json is a file, a. Parse X/package.json, and look for "main" field.`

## Observed (anchor-cited)
- Relative specifier: X = `.` or leading `./`, `/`, `../` → `LOAD_AS_FILE(Y+X)` then `LOAD_AS_DIRECTORY(Y+X)`, else throw (Q1; step 3).
- `LOAD_AS_FILE`: exact X first; then X.js with the nearest package scope (`"type":"module"` → ESM, `"type":"commonjs"` → CJS, absent/other → syntax detection); then X.json as JSON; then X.node as addon (Q2; `#all-together` LOAD_AS_FILE). Filename mapping `./transform` → `transform.js` holds when transform.js exists; "loads as CommonJS" additionally needs `"type":"commonjs"` or no `"type"`.
- `LOAD_AS_DIRECTORY`: `package.json` `"main"` names M; falsy main → `LOAD_INDEX`; then `LOAD_AS_FILE(M)`, `LOAD_INDEX(M)`, deprecated `LOAD_INDEX(X)` (Q3; `#folders-as-modules` example: `require('./some-library')` → `./some-library/lib/some-library.js`).
- The page calls the block a high-level pseudocode summary, not a normative implementation (`#all-together`).
- The page never contains `transform` (HTMLParser text count 0); `./transform` is the lane fixture specifier (`corpus/fixtures/js-r3/index.js:1`), and r3's manifest is `{"name":"revenger-r3-fixture","version":"1.0.0","main":"index.js","type":"commonjs"}` (`corpus/fixtures/js-r3/package.json:1`). `./transform` → `transform.js` is therefore [INFERENCE] from Q2, not a page example.
- The saved verifier asserts specifier/resolved_path/status/state/location (`corpus/verify_js_graph_delta.py:37-42`) and one `maps_to` package-entrypoint edge (`:45-49`); the page states none of those record fields or inference labels.
- Sibling `ScribeSourcesRowsJs.md` independently opened this page for the folder-`main` scope and proposed S016; my row below is scoped to relative-specifier/extension resolution, so L1 should merge it into S016 or append it as the next free id.

## What the source does NOT state
- No static-inference rule for `require` edges or destructured named imports; it documents runtime loading. CJS destructuring is ECMAScript language semantics, not module resolution (the word "destructuring" does not occur; the page's only 2 destructured `require` lines are `const { distance } = require('./point.mjs')` in the `require(esm)` interop section).
- No bundler, Electron/ASAR, packaging or path-rewrite behavior; nothing about the lane's fixtures or REA records.
- No `"exports"` precedence or `node_modules` name-import rule (packages.html scope, sibling row).
- No computed/dynamic specifier rule; no promise that a `require` call is statically resolvable.
- No version-history claim beyond v26.12.1; no on-page revision date. The docs are the mutable "latest" page, so the anchor must pin v26.12.1.

## Proposed SOURCES.md row (contract v1, 11 columns; id TBD, next free S018 if sibling S016/S017 land)
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| TBD | Modules: CommonJS modules — Node.js v26.12.1 Documentation — https://nodejs.org/api/modules.html | docs | A | relative-specifier `require()` resolution as the page's high-level pseudocode states it: dispatch to `LOAD_AS_FILE`, `.js`/`.json`/`.node` fallback, the nearest package-scope `"type"` gate, and `LOAD_AS_DIRECTORY` `"main"` handling | `#all-together` require(X) step 3, `LOAD_AS_FILE`, `LOAD_AS_DIRECTORY`; `#file-modules`; page `node-version content=v26.12.1`, Last-Modified 2026-10-21 | A relative specifier reaches `LOAD_AS_FILE`, which tries `X.js` before `.json`/`.node`; the nearest package scope's `"type"` decides CommonJS or ESM; a folder's `"main"` names the file loaded. | queued | 2026-10-21 | on-release | — |

Tier A only for that scope; not for destructuring, bundlers, Electron/ASAR, `"exports"`, or other Node versions. Target entry: `corpus/knowledge/commonjs-static-import-edges.md` (proposed; L1 sets `used-by` when the entry lands).

## Gate line draft (contract rule 1)
- S0NN (TBD) — `https://nodejs.org/api/modules.html` — accessed 2026-10-21, HTTP 200, Node.js v26.12.1 — Q1 above (`#all-together`, require step 3); Q2 above (`#file-modules`); Q3 above (`#all-together`, LOAD_AS_DIRECTORY step 1).

## First falsifiers for the C04 candidate
- Fixture `"type":"module"`: `./transform` still maps to transform.js but loads as ESM; an entry calling it CJS fails the type gate.
- Both `transform.js` and `transform.json`: `.js` must win (Q2 order).
- `main` plus `"exports"`: do not claim a `main` mapping from this page (packages.html; sibling S017).
- Computed `require('./' + name)`: page states no static resolution; the entry must record unknown, not an edge.
- Property absent from `module.exports`: page states nothing; no name-resolution claim.
- ASAR-packed fixture: page states nothing; only unpacked-directory fixtures are in scope.

## Address check
- Web documentation; no code symbols to trace, so the `lsp` device is n/a (no server for a URL).

VERDICT: Node.js v26.12.1 `Modules: CommonJS modules` opened (HTTP 200, sha256 b35916f2…); three verbatim quotes matched; the page grounds relative-specifier → LOAD_AS_FILE and `.js`/`.json`/`.node` order (so `./transform` → `transform.js` is inference, not an example) and `main` handling; no static-inference or destructuring rule; proposed tier-A queued row (id TBD), no lane edits, no installs.
