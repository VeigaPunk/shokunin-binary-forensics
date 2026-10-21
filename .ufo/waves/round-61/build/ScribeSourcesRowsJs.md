# ScribeSourcesRowsJs — round 61, C04 load-bearing sources (access 2026-10-21)

Scope: independent opening of the two C04 sources only. No edits to `corpus/SOURCES.md`,
`corpus/lessons/round-61.md`, `corpus/knowledge/` or any verifier. Only this report written.
Tools installed or updated: none.

## 1. Sources opened

| # | URL opened | HTTP | Content-Type | Page version (on page) | Header Last-Modified (not on page) |
|---|---|---|---|---|---|
| A | https://nodejs.org/api/modules.html | 200 | text/html; charset=utf-8 | `<title>` "Modules: CommonJS modules \| Node.js v26.12.1 Documentation"; `node-version content=v26.12.1` | Wed, 21 Oct 2026 07:34:29 GMT |
| B | https://nodejs.org/api/packages.html | 200 | text/html; charset=utf-8 | `<title>` "Modules: Packages \| Node.js v26.12.1 Documentation"; `node-version content=v26.12.1` | Wed, 21 Oct 2026 07:34:29 GMT |

No on-page publication date exists on either page. The only date is the HTTP header, which
records a server revision and is not a content revision. Version scope is Node.js v26.12.1.
Both pages were read via the reader and re-matched against the raw HTML (curl-equivalent
fetch, tags stripped, whitespace normalized). Every quote below was found by exact string match.

## 2. Anchors and quotes (verbatim, located)

Q1 — A, section "Folders as modules" (`modules.html#folders-as-modules`), paragraph 1 (19 words):
  "The first is to create a package.json file in the root of the folder, which specifies a main module."

Q2 — A, same section, paragraph 3, after the example (19 words):
  "or if the "main" entry is missing or cannot be resolved, then Node.js will attempt to load an index.js"

Q3 — A, same section, status line directly under the heading (11 words):
  "Stability: 3 - Legacy: Use subpath exports or subpath imports instead."

Q4 — B, section "main" (`packages.html#main`), first paragraph (18 words):
  "The "main" field defines the entry point of a package when imported by name via a node_modules lookup."

Q5 — B, section "Package entry points" (`packages.html#package-entry-points`), paragraph 3 (18 words):
  "The "exports" field, if it exists, takes precedence over the "main" field when importing the package by name."

Q6 — B, section "Module resolution and loading" (`packages.html#module-resolution-and-loading`), `import`/`import()` loading bullets (11 words):
  "which are available if they can be determined through static analysis."

Q7 — B, section "Package entry points", paragraph 2 (14 words):
  "its capabilities are limited: it only defines the main entry point of the package."

Also relevant, not quoted: A `#loading-from-node_modules-folders` (lookup order by walking parent
`node_modules`); A `#loading-ecmascript-modules-using-require` (require of ESM is synchronous only).

## 3. What the two sources establish (scope: Node.js v26.12.1 docs as published)

- `require(<folder>)` loads `"main"` from the folder's `package.json`; if `main` is absent or
  unresolvable it tries `index.js` then `index.node` (Q1, Q2). The doc's own algorithm lists
  `LOAD_AS_DIRECTORY`: read `"main"`, if falsy go to index (A, algorithm block near line 356-362 of reader text).
- The mechanism is Legacy, Stability 3 (Q3).
- `"main"` is the entry for a `node_modules` import by name (Q4). `"exports"` takes precedence
  over `"main"` when it exists (Q5). So a `main`→file mapping is a valid inference only for
  packages whose `package.json` has no `exports` field, or for the `require(<dir>)` path (A).
- `"main"` "only defines the main entry point" (Q7): it does not enumerate any other entry.
- For `import` of a CommonJS module, named exports are "available if they can be determined
  through static analysis" (Q6); the page names `merve` as the analyzer (B, same section).

## 4. What the sources do NOT state

- Nothing on destructuring semantics: `const { x } = require(...)` is ECMAScript language
  behavior. Neither Node page defines or cites it. That side needs its own opened source (lead, not opened here).
- No statement that a CJS named-import edge exists for any particular package or bundler.
  Q6 is conditional ("if they can be determined"); it does not guarantee a given name is found.
- No statement about bundlers (webpack, rollup, esbuild, Electron/ASAR loaders) or how they map
  `main`. Packages in `fixtures/js-r3`, `js-r7-v2`, `shapes-r12` are not covered by these pages.
- No statement about Node versions other than v26.12.1; no version-history claim for `main` beyond "Added in: v0.4.0" (B, `#main`).
- No statement that the saved REA records or fixture bytes were produced by Node.js resolution.
- `index.node` is named in the doc but the C04 scope is JS (no native addon claim).

## 5. Proposed SOURCES.md rows (contract v1, 11 columns)

Id: `S016` and `S017` are the next unused ids (registry read 2026-10-21 ends at S015).
If another seat takes them first, renumber to the next free ids; the row shape is fixed.
Status is `queued` (opened, not yet cited by an admitted entry). Flip to `mined` only when
the C04 knowledge entry lands and its path is added to `used-by`.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 | Modules: CommonJS modules — Node.js v26.12.1 Documentation — https://nodejs.org/api/modules.html | docs | A | `require()` of a folder: `"main"` mapping and index fallback, as published for Node.js v26.12.1 | "Folders as modules" `#folders-as-modules`; page `node-version content=v26.12.1`; header Last-Modified 2026-10-21 | When `require(<folder>)` runs, `package.json` `"main"` names the file loaded; if absent or unresolvable, `index.js` or `index.node` is tried; the mechanism is Stability 3 legacy. | queued | 2026-10-21 | on-release | — |
| S017 | Modules: Packages — Node.js v26.12.1 Documentation — https://nodejs.org/api/packages.html | docs | A | `"main"` field and `"exports"` precedence for `node_modules` imports, and static-analysis limits for CJS named exports, as published for Node.js v26.12.1 | `#main`, `#package-entry-points`, `#module-resolution-and-loading`; page `node-version content=v26.12.1`; header Last-Modified 2026-10-21 | `"main"` is the package's entry point for a name import and is overridden by `"exports"` when present; CJS named exports for ESM importers exist only when static analysis finds them. | queued | 2026-10-21 | on-release | — |

Both rows are tier A only for the stated scope. Neither is tier A for destructuring semantics,
bundler behavior, or any other Node version. The ECMAScript destructuring claim needs its own row.

## 6. Proposed lesson Gate lines (for `corpus/lessons/round-61.md` `## Gate`)

- S016 `https://nodejs.org/api/modules.html` — accessed 2026-10-21, HTTP 200, Node.js v26.12.1 docs,
  "Folders as modules": "The first is to create a package.json file in the root of the folder, which specifies a main module."
- S016 same URL, same section, paragraph 3: "or if the "main" entry is missing or cannot be resolved, then Node.js will attempt to load an index.js"
- S017 `https://nodejs.org/api/packages.html` — accessed 2026-10-21, HTTP 200, Node.js v26.12.1 docs,
  `#main`: "The "main" field defines the entry point of a package when imported by name via a node_modules lookup."
- S017 same URL, `#package-entry-points`: "The "exports" field, if it exists, takes precedence over the "main" field when importing the package by name."

Contract rule 1 is met: each row has its URL, access date, and a located quote of 25 words or fewer.

## 7. First falsifiers for the C04 entry (to be checked by the executor, not run here)

- A fixture `package.json` with both `main` and `exports`: a `main`-based mapping must not be claimed for that package (S017 Q5).
- A fixture whose `main` target is missing: the entry must not claim a `main` mapping; S016 says `index.js` is tried (Q2).
- A destructured `require` whose property is absent from the module's `exports`: the Node docs say nothing about this (section 4), so the entry must not state the result.

## 8. Unknowns

- The Node.js v26.12.1 docs do not carry an on-page revision date; the 2026-10-21 HTTP
  Last-Modified header is the only date and is recorded as such.
- Whether the fixtures under `fixtures/js-r3`, `js-r7-v2`, `shapes-r12` were resolved by Node.js
  v26.12.1 is unknown (not observed in this scope).

VERDICT: Both load-bearing C04 Node.js docs opened (HTTP 200, v26.12.1); seven quotes verified verbatim; S016/S017 drafted as queued tier-A rows with scope limits; destructuring and bundler behavior remain unsourced.
