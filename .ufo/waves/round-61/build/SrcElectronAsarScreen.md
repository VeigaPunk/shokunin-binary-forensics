# SrcElectronAsarScreen — C1/C04 source screen: Electron ASAR Archives

Seat `CloseChousa26.SrcElectronAsarScreen-10`, read-only, round 61 only. No installs.

## Open result

- URL: `https://www.electronjs.org/docs/latest/tutorial/asar-archives` — curl → `HTTP=200 SIZE=51166`; `content-type: text/html`, `last-modified: Wed, 21 Oct 2026 12:13:21 GMT`, `cf-cache-status: DYNAMIC` (`/tmp/ea-headers.txt`). Canonical: `https://electronjs.org/docs/latest/tutorial/asar-archives`.
- Page identity: Docusaurus `v3.10.0`, `<html class="…docs-version-current…">` — the `latest` alias. **No on-page version, revision or date** (the `lastUpdated` div is empty in the HTML).
- Revision, out of band: `GET api.github.com/repos/electron/electron/commits?path=docs/tutorial/asar-archives.md` → newest `7377022f0332da858dfc3e8590adec4440208e64` (2026-08-22T06:03:41Z); raw file at that commit HTTP 200, 6800 B, sha256 `3e4ca507…1a02`. Current stable release `v45.0.0` (2026-10-21T05:22:39Z) — not stated on the page.
- Anchors used: `#asar-archives` (lede), `#using-asar-archives` → `#node-api`, `#adding-unpacked-files-to-asar-archives`.

## Verbatim quotes (accessed 2026-10-21)

1. Lede, before `## Using ASAR Archives`: "the app's source code is usually bundled into an ASAR archive, which is a simple extensive archive format designed for Electron apps." (22 words; matches raw markdown at 7377022 with link target unwrapped, `q in m` → True).
2. `## Using ASAR Archives → ### Node API` (`#node-api`): "Node APIs like fs.readFile and require treat ASAR archives as virtual directories, and the files in it as normal files in the filesystem." (23 words; `q in t` → True).
3. `## Adding Unpacked Files to ASAR archives`: "a folder named app.asar.unpacked was created together with the app.asar file." (11 words; `q in t` → True).

## Does it support statements about the lane's saved JS fixtures? — No.

- `find corpus -name '*.asar*' -print | wc -l` → `0`; `file corpus/fixtures/js-r3 corpus/fixtures/js-r7-v2 corpus/fixtures/shapes-r12/v1` → all `directory`. The fixtures are unpacked trees (`index.js`, `transform.js`, `package.json` with `"main":"index.js"`, `"type":"commonjs"`).
- The saved records already report archive absence: `corpus/live/runs/round-6/view.json:1` (§statistics, byte 989) and `corpus/live/runs/20261012T164357Z/analysis.json:1` (byte 37636) both carry `"nested_asar_containers":0`.
- C04's real claims are elsewhere: `corpus/verify_js_graph_delta.py:23` parses `const {…} = require('./transform')`; `:27` reads `package["main"]`; `:45-49` asserts the `maps_to`/`resolved_path` edge. The page states nothing about either.
- Refusal grounding: at 7377022, `grep -nc 'package.json\|"main"\|destructur' /tmp/asar.md` → `0`. The page never calls an unpacked directory a shipped layout; its only unpack construct is additive (`app.asar.unpacked` beside `app.asar`).
- Inference (labeled): the page supports at most a scope-limit sentence — Electron packages *usually* ship as ASAR and `require` resolves archive contents like directories — so C04's fixture-derived inference is scoped to unpacked directories and does not cover archive-embedded packages. It cannot carry the `main`/destructured-require claims (Q01).

## Proposed SOURCES.md row (contract v1, 11 columns) — queued

Next unused id: `S016` (`grep -oE '^\| S[0-9]{3,}' corpus/SOURCES.md | tail -3` → S013,S014,S015; 15 rows). Id is TBD if a sibling lands S016 first.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 | ASAR Archives — Electron documentation — https://www.electronjs.org/docs/latest/tutorial/asar-archives | docs | A | what Electron's own docs state about ASAR packaging and how Node/Web APIs treat archive contents as a directory | lede and “Using ASAR Archives → Node API”; docs `latest` (`docs-version-current`), file revision 7377022 dated 2026-08-22 | An Electron package may ship as an ASAR archive whose contents `require` resolves like a directory, so a directory-only fixture set is a declared scope limit, not the product's only layout. | queued | 2026-10-21 | on-release | — |

Reason for `queued`, not `mined`: tier A only for that narrow packaging statement; zero of C04's load-bearing claims appear on it. If the C04 entry cites it for the scope-limit sentence, flip to `mined` with `used-by: corpus/knowledge/<c04-entry>.md` — the only admissible use.

## What the source does NOT state

- Nothing about `package.json`, the `main` field, or Node/CJS module-resolution order.
- Nothing about CommonJS named imports, destructuring, or any static/AST inference.
- Nothing making an unpacked directory a shipped distribution; `--unpack` output ships *with* `app.asar`, it does not replace it.
- Nothing about ASAR container bytes (header JSON, offsets); it references the `asar` CLI and `original-fs` only. The format lives in `github.com/electron/asar` (linked, unopened — lead only if a future round claims archive-embedded packages).
- No on-page revision or date, so the anchor revision must be cited from GitHub history, not the page.

Installs: none.

VERDICT: Page opened HTTP 200 but supports no statement about the lane's directory-based JS fixtures and none of C04's `main`/destructured-require claims; record one queued scope-limited row (S016 TBD) usable only as a C04 scope-limit citation.
