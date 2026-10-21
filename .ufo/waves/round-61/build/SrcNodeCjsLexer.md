# SrcNodeCjsLexer — C04 source opening: Node.js ESM docs, CommonJS namespaces

Seat `CloseChousa26.SrcNodeCjsLexer-10`. Read-only: no clone, no lane edit, no verifier run; wrote only this report.

## Opened source

- URL `https://nodejs.org/api/esm.html`; `curl -sS -D` → `HTTP/2 200`, `content-length: 137245`, `last-modified: Wed, 21 Oct 2026 07:34:29 GMT`, `etag: "978e42acbf81238ea0ebb705a88aba89"`; body sha256 `f3d3f9c92ba3e51995004a908f9ac56e0fe9beed1334c84bb213301a162b208d` (saved `/tmp/r61-esm.html`).
- Version: title `Modules: ECMAScript modules | Node.js v26.12.1 Documentation`; `meta-nodejs.org:node-version` = `v26.12.1`; v26.12.1 release date 2026-10-21 (`https://nodejs.org/dist/index.json` entry 0: `{"version":"v26.12.1","date":"2026-10-21",...}`). The page carries no doc revision id; `last-modified` is the served file's mtime.
- Anchor: `#interoperability-with-commonjs` → `#commonjs-namespaces`; heading `CommonJS Namespaces`, `Added in: v14.13.0`; raw HTML `<a class=mark id=commonjs-namespaces href=#commonjs-namespaces>` inside `<h4>`.
- Access date: 2026-10-21.

## Verbatim quotes (≤25 words; source line-wraps collapsed to single spaces)

1. §CommonJS Namespaces ¶3 — "In addition, a heuristic static analysis is performed against the source text of the CommonJS module to get a best-effort static list of exports" (24 words).
2. §CommonJS Namespaces, after the worked example — "Live binding updates or new exports added to `module.exports` are not detected for these named exports." (16).
3. §CommonJS Namespaces, next sentence — "The detection of named exports is based on common syntax patterns but does not always correctly detect named exports." (19).

## Proposed SOURCES.md row (11 columns)

| TBD (next free; S016–S017 claimed by sibling drafts) | Modules: ECMAScript modules — Node.js v26.12.1 Documentation — https://nodejs.org/api/esm.html | docs | A | Node.js's documented CommonJS-to-ESM named-export detection behavior: heuristic static analysis of source text, best-effort, may misdetect, ignores live updates; excludes the pattern table and package resolution | §CommonJS Namespaces (`#commonjs-namespaces`), `Added in: v14.13.0`, Node.js v26.12.1 docs, file last-modified 2026-10-21T07:34:29Z | Node.js builds CommonJS named exports from best-effort static analysis of module source before evaluation, so a named export's presence is an inference, not a guarantee. | queued | 2026-10-21 | on-release | — |

Flip at integration: if the C04 entry exists and cites it, write `mined` with `used-by` = that entry's repo path; otherwise keep `queued`/`—` (census `mined` check requires used-by paths to exist).

## What the source does NOT state

- Does not name `cjs-module-lexer`: `grep -o 'cjs-module-lexer' /tmp/r61-esm.html | wc -l` → `0`. `merve` occurs 2×; v26.12.1 links `https://github.com/anonrig/merve/tree/v1.0.0` for "the exact semantics implemented". This row cannot attribute Node's detection to cjs-module-lexer. The opened cjs-module-lexer README (raw main, HTTP 200, 15248 bytes) still claims "used in Node.js core" — an attribution conflict to resolve before any entry names a lexer.
- Does not mention destructuring: `grep -oi 'destructur' /tmp/r61-esm.html | wc -l` → `0`. Nothing about `const { a } = require('m')`; C04's destructured-require edge is fixture inference plus this page's "may be missed" caveat, not a documented mapping.
- Does not map package `main`: `"main"` → 0 hits; the package section says "This section was moved to Modules: Packages". That half of C04 rests on sibling rows (modules.html#folders-as-modules / packages.html#main).
- No completeness or version-independent guarantee, no pattern list, and no statement that a missing named export fails the import (the fallback it offers is the default import).
- No Electron statement (`grep -oi electron` → 0), and no statement about which namespaces result for non-object `module.exports` beyond "can be of any type".

## Supporting opens (not proposed as rows)

- `https://raw.githubusercontent.com/nodejs/cjs-module-lexer/main/README.md` HTTP 200, 15248 bytes: "detect the most likely list of named exports"; grammar runs "without scope analysis", explicitly over- and underclassifies (read via `artifact://75882:1-300`).
- `https://raw.githubusercontent.com/anonrig/merve/main/README.md` HTTP 200, 11647 bytes, sha256 `40be0d07089167712e04f77d2f93c0ae44ea12dcb82c782b774096f03329fbfb`: "performs static analysis to detect CommonJS export patterns without executing the code"; no "destructur" match.

## Consequence for the C04 entry

Grounded claim available from this row: detection is static, heuristic, best-effort, runs before evaluation, ignores live updates, and can miss. A destructured-require edge must be labelled inferred and cite the saved fixture run; this page supports "not guaranteed", not "detected". Naming cjs-module-lexer as Node's current mechanism is unsupported by v26.12.1 docs.

VERDICT: Opened (HTTP 200) Node.js v26.12.1 docs `#commonjs-namespaces`; 3 verbatim quotes recorded; one tier-A scoped row proposed (id TBD, queued); the page does not name cjs-module-lexer (defers to merve), does not mention destructured require or package `main`.
Installs: none.
