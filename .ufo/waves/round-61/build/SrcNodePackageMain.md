# SrcNodePackageMain — C04 source open, round 61 (access 2026-10-21)
Scope: independent read-only open of `https://nodejs.org/api/packages.html` for the
`package.json` `"main"` definition and its relation to `"exports"`. No production edits,
no clone, no REA producer calls, no delegation. Tools installed or updated: none.
## Open record (observed)
Command: `curl -sS -o /tmp/revenger-r61-SrcNodePackageMain-page.html -D - -w 'HTTP %{http_code} size=%{size_download}\n' https://nodejs.org/api/packages.html`
Output: `HTTP 200 size=156551`; `content-type: text/html; charset=utf-8`;
`etag: "04494db5832595a2adc3ef27aad9ab5b"`; `last-modified: Wed, 21 Oct 2026 07:34:29 GMT`;
`date: Wed, 21 Oct 2026 15:42:50 GMT`.
Version (on page): `<title>Modules: Packages | Node.js v26.12.1 Documentation</title>`,
footer `Node.js v26.12.1 Documentation`. On-page revision date: none — regex sweep of the
tag-stripped page for `2026-[0-9]{2}-[0-9]{2}` returned zero matches; the only date is the HTTP
`Last-Modified` server revision, not a content revision.

## Anchors located (raw HTML, exact ids)
- `#package-entry-points`: `<h3>Package entry points<span><a class=mark id=package-entry-points`
  at HTML offset 39871; the precedence sentence is in its 4th `<p>` (paragraph split checked).
- `#main`: `<h3>"main"` with `id=main href=#main` at offset 142995, inside
  `<h2 id=nodejs-packagejson-field-definitions>` ("Node.js package.json field definitions").
  Paragraphs verified: p1 field definition + path value; p2 `exports` precedence; p3 the
  `require(<directory>)` sentence.
- `#exports`: `id=exports href=#exports` at offset 150246 (consulted, not quoted).

## Verbatim quotes (exact-string match on tag-stripped page; counts by `split()`)
Q1 — `#main`, paragraph 1 (23 words):
  "The "main" field defines the entry point of a package when imported by name via a node_modules lookup. Its value is a path."
Q2 — `#main`, paragraph 2 (18 words):
  "The "exports" field, if it exists, takes precedence over the "main" field when importing the package by name."
Q3 — `#package-entry-points`, paragraph 4 (19 words):
  "If both "exports" and "main" are defined, the "exports" field takes precedence over "main" in supported versions of Node.js."
Check: python `q in clean_text` returned `True` for all three; no quote came from a search snippet or memory.

## Proposed SOURCES.md row (contract v1, 11 columns)
id TBD: registry read 2026-10-21 ends at S015. Sibling
`.ufo/waves/round-61/build/ScribeSourcesRowsJs.md:64-70` already proposes S016 for
`modules.html` and S017 for this same `packages.html`; this row has the same source and scope,
so merge into that S017 rather than mint a duplicate. If that proposal is dropped, the next free
id for this page is S017; if both land independently, this one is S018.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| TBD (S017/S018) | Modules: Packages — Node.js v26.12.1 Documentation — https://nodejs.org/api/packages.html | docs | A | field semantics only: what `package.json` `"main"` names and when `"exports"` overrides it for by-name package loading, as published for Node.js v26.12.1 | `#main` p1–p2 under `#nodejs-packagejson-field-definitions`, and `#package-entry-points` p4; page `Node.js v26.12.1`; header Last-Modified 2026-10-21 | `"main"` is a path entry for by-name `node_modules` and package-directory loads, but any `"exports"` field takes precedence, so a static mapping must branch on `exports` first. | queued | 2026-10-21 | on-release | — (becomes `mined` when the C04 entry cites it) |

Tier A for that scope only (official docs for their own field semantics); not A for
destructuring semantics, bundler/Electron mapping, or any version other than v26.12.1.

## What the source does NOT state (absence observed, not recalled)
- No destructured-`require` semantics: tag-stripped page has `destructur` 0, `Electron` 0,
  `bundler` 0, `webpack`/`rollup`/`esbuild` 0, `defaults to` 0. C04's named-import-edge half is
  unsupported by this row and needs its own opened source (ECMAScript `ObjectBindingPattern`
  semantics or the CommonJS wrapper), left as a lead, not a row.
- No default entry when `main` is absent. `index.js` appears only in examples and in the
  `#module-resolution-and-loading` cross-reference to "folders as modules"; `#main` p3's example
  comment `// This resolves to ./path/to/directory/index.js.` is an example, not a stated default.
- No static-analysis algorithm for `require()`. The only static-analysis sentence is about ESM
  importers of CJS at `#module-resolution-and-loading`: named exports are
  "which are available if they can be determined through static analysis." (11 words, exact match).
- No general requirement that `"main"` exist: it "is required" only for packages supporting
  Node.js 10 and below (`#package-entry-points` p4).
- No statement about the lane's fixtures (`fixtures/js-r3`, `js-r7-v2`, `shapes-r12`) or that any
  saved REA record was produced by Node.js v26.12.1.

## Consequence for C04 (inference, labeled)
A `main` → file mapping is inferable only for a package whose `package.json` lacks `"exports"`,
or for the `require(<directory>)` path; when both fields exist `exports` wins (Q2, Q3), so an
entry must test for `exports` presence before claiming a `main` mapping. First falsifier: a built
fixture `package.json` carrying both fields with different targets — a `main`-based edge must not
be emitted for it.

VERDICT: packages.html opened (HTTP 200, Node.js v26.12.1); `#main` and `#package-entry-points` located; three verbatim quotes exact-match verified; one tier-A scoped row proposed under a colliding id (merge with sibling S017); destructured-require and bundler behavior remain unsourced by this page.
