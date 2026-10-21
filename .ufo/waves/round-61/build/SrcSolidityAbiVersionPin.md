# SrcSolidityAbiVersionPin — Solidity ABI spec pinned to v0.8.37 (read-only)

Seat `CloseChousa26.SrcSolidityAbiVersionPin-10` · lane base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` · 2026-10-21. No clone, no lane edit, no install, no bytecode execution.
## Axes

| axis | move |
|---|---|
| Immutability | anchor a release tag, not `/en/latest/` (which serves 0.8.38-develop) |
| Verifiability | compare the selector section's bytes, then diff the whole page |
| Scope honesty | tier A confined to the selector definition; opcode/dispatch facts excluded |
| Derivation reuse | record the page's own selector KATs for C09's expected values |

## Current stable (observed)

- `curl -s 'https://api.github.com/repos/ethereum/solidity/releases?per_page=10'` → newest non-prerelease `v0.8.37 2026-09-10T06:38:29Z False`; next `v0.8.36 2026-07-09T07:40:02Z False`.
- `GET /repos/argotorg/solidity/git/ref/tags/v0.8.37` → `refs/tags/v0.8.37 commit f401782df49be312ea4ef52a2d467cf5183b5906`; the tag listing ends at `v0.8.37` (no `v0.8.38` tag).
- Blog index: newest release post is `/blog/2026/09/10/solidity-0.8.37-release-announcement`; fetched HTTP 200, body reads "Posted by Solidity Team on September 10, 2026" / "We have released Solidity v0.8.37".
⇒ Current stable = 0.8.37; `/en/latest/` is titled "Solidity 0.8.38-develop documentation".
## Pages opened (2026-10-21, `curl -sSL`)

| URL | HTTP | bytes | served version | last-modified | sha256 |
|---|---|---|---|---|---|
| https://docs.soliditylang.org/en/v0.8.37/abi-spec.html | 200, `text/html; charset=utf-8` | 112708 | `x-rtd-version: v0.8.37`; title "Solidity 0.8.37-develop documentation" | Thu, 10 Sep 2026 06:40:15 GMT | a25662d7e40982150d48b09ba747722bb8c6b59199cd90629746a0590a762568 |
| https://docs.soliditylang.org/en/latest/abi-spec.html | 200, `text/html; charset=utf-8` | 112838 | `x-rtd-version: latest`; title "Solidity 0.8.38-develop documentation" | Tue, 29 Sep 2026 13:01:06 GMT | 4bb56ed3f2aaed824d3eb3c6df758284cbd9c714f063bdc23bfb45cbb0943926 |

- Tagged source `docs/abi-spec.rst` at f401782 (`raw.githubusercontent.com/argotorg/solidity/f401782…/docs/abi-spec.rst`): HTTP 200, 41437 B, sha256 `bda1c34bf57f3c63e426486e688bf24feda1c8fe439209df1cb4dec8c884eb79`; "Function Selector" heading at line 24, next heading at 40.
## Function Selector diff — `/en/v0.8.37/` vs `/en/latest/`

- Section from `<h2>Function Selector<a` up to the next `<h2>` (`#argument-encoding`): 1167 bytes, sha256 `7ff79db926f09e60effb21460c1bdfa95cf894ce5b3851bd6234f8d6c30cc573` in **both** fetches — byte-identical, no textual difference.
- Whole page: 9 diff hunks, all version plumbing — title `0.8.37`→`0.8.38`, `documentation_options.js?v=` hash, rtd meta slug, one nav link (`frequently-reported-non-bugs.html`), Edit-on-GitHub tag `v0.8.37`→`latest`, four remix `version=0.8.37`→`0.8.38` params. No ABI prose changed.
- Consequence: `/en/latest/` moves (0.8.38-develop, Last-Modified 2026-09-29) and cannot anchor; the v0.8.37 text is still current on 2026-10-21.
## Quotes (verbatim, ≤25 words; revision v0.8.37 / commit f401782…, accessed 2026-10-21)

| # | quote | location |
|---|---|---|
| Q1 | "The first four bytes of the call data for a function call specifies the function to be called." (18 w) | §Function Selector, docs/abi-spec.rst:27 |
| Q2 | "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function." (20 w) | §Function Selector, rst:27-29 |
| Q3 | "Note that `uint` is replaced with its canonical representation `uint256`." (10 w) | §Examples, `sam` bullet, rst:293 |

- Not quoted, located (rst:35): the note excludes the return type from the signature.
## Proposed row (contract v1, 11 columns)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 (TBD) | Contract ABI Specification — Solidity 0.8.37 docs — https://docs.soliditylang.org/en/v0.8.37/abi-spec.html | spec | A | Solidity 0.8.37 definition and normalization of a function selector and the ABI type mapping needed to write its signature text; excludes opcode byte values, dispatcher layout and reachability | "Function Selector" (#function-selector), docs/abi-spec.rst:24-39 at tag commit f401782df49be312ea4ef52a2d467cf5183b5906; x-rtd-version v0.8.37, last-modified 2026-09-10T06:40:15Z | A selector is the high-order four bytes of Keccak-256 over the function's signature text, so a 4-byte immediate's expected selector value is recomputable from a candidate signature. | queued | 2026-10-21 | on-release | — |

- `id`: registry ends at S015 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `15`), so S016 is next free; a sibling already proposes S016 for the moving URL (below).
- `kind`: `spec` is proposed; the sibling chose `docs` — both pass E05, L1 harmonizes.
- `status queued` because E11 rejects `mined` whose used-by path is absent; flip to `mined` with the C09 entry path when admitted, logging old→new (CORPUS.md:116-117).

## What the source does NOT state

- No `PUSH` and no `JUMPDEST`: counts are 0 and 0 in the fetched page; the single "opcode" hit is unnamed (§Errors, "a special opcode to abort execution").
- No opcode byte values, immediate width, dispatcher shape, or claim that a selector occurs literally in deployed code ⇒ "PUSH4 candidate = method" and "candidate → JUMPDEST" are [INFERENCE] over fixture bytes, not ABI facts. Opcode/JUMPDEST support must come from the sibling rows (SrcExecSpecsOpcodes, SrcYellowPaperJumpdest).
- Names Keccak-256 but defines no padding, test vectors, or SHA3-256 distinction (sibling SrcKeccakVsSha3).
- No selector-collision handling, no proxy/fallback dispatch semantics, no recovery of signature text from bytecode.
- It does record worked selector KATs — `0xfce353f6` (rst:259), `0xcdcd77c0` (rst:274), `0xa5643bf2` (rst:293), `0x8be65246` (rst:316) — and the Solidity→ABI type table (rst:100-127): recorded, not re-derived here; recomputing them needs an independent Keccak, which this page does not supply.

## Coordination hazard for L1

- `ScribeSourcesRowsEvm.md:9,32,39` opens `/en/latest/abi-spec.html` and proposes S016 `mined` with used-by `[C09 entry, TBD by L1]` — that path does not exist (E11), and the URL is a moving 0.8.38-develop build.
- Cite this pinned row for the selector claim; E04 keys on URL+scope, so a second ABI row on `/en/latest/` is at most a W04 same-source warning, never a hard error.

## Gate line draft

- S016 — https://docs.soliditylang.org/en/v0.8.37/abi-spec.html — accessed 2026-10-21 — "The first four bytes of the call data for a function call specifies the function to be called." (§Function Selector, docs v0.8.37)

Files written: this report only. Installs: none. No lane tree, git or jj state touched.

VERDICT: Solidity stable is 0.8.37 (2026-09-10); the version-pinned `#function-selector` section is byte-identical to `/en/latest/` (sha256 7ff79db9…), so the C09 anchor can name `docs.soliditylang.org/en/v0.8.37/abi-spec.html` + tag commit f401782…, and it must not be used for PUSH4/JUMPDEST facts.
