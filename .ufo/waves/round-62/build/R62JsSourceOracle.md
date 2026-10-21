RESULT: COMPLETE

# R62JsSourceOracle — bounded CommonJS-require source oracle (C04 source side)
Seat `RevengerR61-2.R62JsSourceOracle`. Scope: write and run **my own** bounded tokenizer over the archived
`js-r3` / `js-r7-v2` fixture files; report each `require` call line, literal specifier, binding names, 1-based
exact span + source substring, and directory listing / entry type / full SHA-256. No JavaScript executed, no
general parser, no production file written, README untouched (C04 stays `uncovered`).

## 1. Inputs (frozen, extracted copy only)
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C /fast/scratch/hyaku/revenger-r62/R62JsSourceOracle/frozen`
`git log -1 --format='%H %ci %s' a3498e2…` → `a3498e25ad87bf756288812d0ea7c474b09433c7 2026-10-21 14:56:58 -0300 round-62: freeze C1 coverage replacement admission and K4/14 baseline before build`.
All runs used `cwd=/` and the extracted tree only; the working tree was never written (`git status --porcelain` → only untracked `.ufo/waves/round-62/`).
Frozen bytes == committed bytes (6/6 SHA-256 SAME, `sha256sum` on both trees: `js-r3` and `js-r7-v2` × `index.js`, `package.json`, `transform.js`).

## 2. Tool (own code, standard library only, Python 3.14.8)
- `scratch/js_source_oracle.py` — 455 lines, SHA-256 `d3ad81296dc73b31593fc520212e98a2c8066aa643cba001cca816c04a4d366c`.
- Bounded by construction: it recognises only `const/let/var { id [, id]* } = require('<literal>')` and `const/let/var id = require('<literal>')`; any other `require` shape is printed as `UNPARSED … reason=…` and never guessed at. It is not a JavaScript parser.
- Fixture bytes are read as UTF-8 text; **no JavaScript is executed**.
- Boundedness self-test `python3 -B js_source_oracle.py --self-test` (exit 0): `calls=2 unparsed=2`; the `require` word inside a string literal, a line comment and a block comment is not counted, and `const d = require;` is not a call site (`scratch/self_test.out`, SHA-256 `aa2629892b1b…75270a`).
- Deterministic: two consecutive runs gave byte-identical stdout (`diff -q` → identical).
- Main run (cwd=/): `python3 -B /fast/scratch/hyaku/revenger-r62/R62JsSourceOracle/js_source_oracle.py /fast/scratch/hyaku/revenger-r62/R62JsSourceOracle/frozen` → exit 0, 76 lines, stdout `scratch/js_source_oracle.out`, SHA-256 `1b9ad9ea9306dcc632385c0474d25f55515b2e546f9b87937d7c410fa1d862b3`.

## 3. Derived require call sites (re-derived from the bytes)
js-r3/index.js — bytes 274, sha256 `f7d8bf47…e929f32`, 7 lines, `REQUIRE_CALL_COUNT 1`, `UNPARSED_REQUIRE_COUNT 0`
- `CALL 1 line=1 col1_start=29 col1_end_exclusive=51` (inclusive cols 29–50) = 0-based `[28,50)`; `SPECIFIER './transform'` (single-quoted), literal at 1-based cols 38–48
- `BINDING_FORM DESTRUCTURED NAMES ['rot13', 'checksum']`; `PATTERN` 1-based cols 7–25 = 0-based `[6,25)`, substring `{ rot13, checksum }`
- `INITIALIZER` 0-based `[6,50)`, substring `{ rot13, checksum } = require('./transform')`; `STATEMENT` 0-based `[0,51)`, substring `const { rot13, checksum } = require('./transform');`
- `SUBSTRING "require('./transform')"`; `SPAN_CHECK substring_len=22 col1_len=22 … result=OK`
js-r7-v2/index.js — bytes 209, sha256 `b53d96d4…c4c42a`, 7 lines, 1 call, 0 unparsed
- `CALL 1 line=1 col1_start=19 col1_end_exclusive=41` (inclusive cols 19–40) = 0-based `[18,40)`; `SPECIFIER './transform'`, literal at 1-based cols 28–38; `BINDING_FORM DESTRUCTURED NAMES ['rot13']`
- `PATTERN` 1-based cols 7–15 = 0-based `[6,15)`, substring `{ rot13 }`; `INITIALIZER` 0-based `[6,40)`, substring `{ rot13 } = require('./transform')`; `STATEMENT` 0-based `[0,41)`, substring `const { rot13 } = require('./transform');`
- `SUBSTRING "require('./transform')"`; `SPAN_CHECK substring_len=22 col1_len=22 … result=OK`
js-r3/transform.js and js-r7-v2/transform.js — bytes 379, sha256 `cd9f3f63…ca7fa345`, 12 lines each, `REQUIRE_CALL_COUNT 0`, `UNPARSED_REQUIRE_COUNT 0`.

## 4. Directory listing / type / full SHA-256 (derived)
js-r3: `index.js` file 274 `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7`; `package.json` file 85 `92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7`; `transform.js` file 379 `cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345`; `ENTRY_COUNT 3`.
js-r7-v2: `index.js` file 209 `b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a`; `package.json` file 85 `92ef8e3d…03ea1096d7`; `transform.js` file 379 `cd9f3f63…ca7fa345`; `ENTRY_COUNT 3`.

## 5. Derived vs the import fields RECORDED in the two saved records
Saved records read from the same frozen tree: `corpus/live/runs/20261012T164357Z/analysis.json` (`ev_4a93276c…00c1c7e`) and `corpus/live/runs/round-7/v2-analysis.json` (`ev_66f5dc7e…2cd7987c`). Printed checks (`js_source_oracle.out:51-76`):
- js-r3: require-call-span derived `[28,50)` == recorded `[28,50)` MATCH; binding names `['checksum','rot13']` == recorded MATCH; specifier MATCH; binding-initializer span `[6,50)` == recorded `[6,50)` MATCH (both named edges); file digest, file size and line count MATCH for `index.js` and `transform.js`.
- js-r7-v2: require-call-span `[18,40)` == recorded `[18,40)` MATCH; binding names `['rot13']` == recorded MATCH; specifier MATCH; initializer span `[6,40)` == recorded `[6,40)` MATCH; digest, size and line count MATCH.
- **One MISMATCH, kept visible on purpose**: the recorded named-import edge span starts at the `{` of the binding pattern, not at `const`; my whole-statement span (`[0,51)` / `[0,41)`) therefore prints `result=MISMATCH` against it. Definitional, not a byte disagreement — the entry must state which span it claims.

## 6. Unknowns / honest limits
- The provider **directory** digests (`8eec9ffb…e929f32`, `696c2496…8f655`) are RECORDED only: this tool does not re-derive a directory digest (its canonicalisation is undocumented in the saved record) and labels them so.
- `package.json` `main`, the `electron-main` / package-entrypoint role fields and the graph's `import_relationships` counters are recorded fields, not derived by this tool.
- The tool establishes agreement between fixture bytes and the recorded import fields at the recorded spans; it proves nothing about producer origin, graph completeness, runtime resolution or any other JavaScript shape.

## 7. Proposed artifact (scratch only, no corpus write)
`scratch/proposed-c04-derivation-block.md` — a ready-to-paste command+output derivation block for `corpus/knowledge/round-62-commonjs-require-name-evidence.md` (C04): derived facts, recorded-only values, limitations the entry must carry. The entry must embed the tool source itself to satisfy Q11 in-entry derivation. I did not write that corpus file (not my seat) and did not touch `corpus/README.md`.

## 8. Not done / out of scope
No REA producer call, no JS/bytecode execution, no network/RPC, no `measure.py` probe run (the L1 owns the before/final count), no corpus or fixtures byte changed, no gate, no promotion, no admission claim, README not marked held.
Scratch (lane/round owned, remove on landing): `/fast/scratch/hyaku/revenger-r62/R62JsSourceOracle/` (`js_source_oracle.py`, `js_source_oracle.out`, `self_test.out`, `proposed-c04-derivation-block.md`, `frozen/`).

Installs / updates by this seat: none (no tool, package or provider was installed or updated).
