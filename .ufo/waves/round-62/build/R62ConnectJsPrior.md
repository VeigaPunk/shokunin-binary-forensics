RESULT: COMPLETE

# R62ConnectJsPrior — kaidoku CommonJS/ASAR ground for the C04 destructured-require candidate

Seat `RevengerR61-2.R62ConnectJsPrior` · 2026-10-21 · read-only on kaidoku; read-only on revenger's frozen tree. No corpus file created or modified; no README row touched; **no admission claimed**; README C04/C09 stay `uncovered` (held count still 4). **Axes:** coverage K (a new C04 entry must clear unchanged Q01–Q13); adjacency/Q10 (cross-lane scope reported, not absorbed); quality/Q11 (the missing in-entry derivation).

## Evidence 1 — kaidoku holds no destructured-require import-name ground (distinct, not overlap)

Read-only, kaidoku HEAD `69e82c48be5614ce96f7c1c32445fe61c4870630` (2026-10-21T13:54:36-03:00), corpus digests: `README.md` `568c647d…`, `2026-10-13-r3-typora-signal.md` `5f28475a…`, `2026-10-13-r2-asar-deep-obsidian.md` `6e61383f…`, `2026-10-13-r4-09-js-export-compare.md` `7fac8891…`, `2026-10-13-r4-07-jsc-bytecode.md` `eb18239d…`, `2026-10-13-asar-surface.md` `24be2d11…`.

- `grep -rin 'destructure' kaidoku-shokunin/corpus/` → **0 lines**; same for `imported_name`, `local_name`, `imported_path`, `source-range` → **0 lines each** (run in `evidence_c04_span_ground.py`, output above). The one `named import` hit in kaidoku's corpus is ELF, not JS: `knowledge/2026-10-13-r5-02-call-targets-jq.md:107` "N targets == N named imports, not N recovered bodies."
- So kaidoku holds **no** `imported_name`/`imported_path`/`local_name` field ground and **no** per-edge span ground for CommonJS destructuring. Its require ground is a *different provider representation*: unresolved-reference module nodes keyed by specifier — `require:electron`, `require:fs`, `require:require(main)`, `dynamic-import:electron` (`knowledge/2026-10-13-r2-asar-deep-obsidian.md:52`), `require:fs/path/vm/v8/module`, `require:./atom.compiled.dist.jsc`, `require:e.require(t)` (`2026-10-13-r3-typora-signal.md:33`, `:41`, `:43`, `:73`).
- The single require **call-site span** in kaidoku's corpus is `require:./atom.compiled.dist.jsc` anchored to `launch.dist.js` **line 1 col 1345–1380**, `resolution: "unresolved"`, confidence low (`2026-10-13-r3-typora-signal.md:41`, run-log row `:73`). Distinct from revenger's ground: kaidoku's is an unresolved reference inside a real third-party Electron/ASAR app; revenger's C04 subject is resolved named-import edges on two authored CommonJS directories.

## Evidence 2 — the one genuine overlap (already flagged PARTIAL in round 61)

`kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-09-js-export-compare.md:59` — authored 4-line CJS fixtures `/tmp/mini-a`, `/tmp/mini-b` (analyses `ev_6e6e173b…`/`ev_f36db5b9…`); `:65` — "`module.exports = {config, tags}` yields `default` binding only, NO return shapes; `exports.X = function` yields both". That is the same *export-side family fact* the C04 subject observes (`fixtures/js-r3/transform.js:12` is `module.exports = { rot13, checksum };` → each module's only exposed export is `default`). Round-61's `falsify-w3/W3JsCrossLaneCites.md` already graded this as PARTIAL for omitting adjacent kaidoku ground; the new C04 entry must report it (Q10) and must not absorb it as support.

## Evidence 3 — folder/label ≠ Electron or ASAR ownership (do not import by folder name)

- kaidoku's own corpus shows the `electron-main` **kind label appears without Electron involvement**: `2026-10-13-r3-typora-signal.md:33` records `electron-main` 1 in typora's `app.asar` graph while `:41` records "every Electron boundary counter = 0 (`browser_windows`, `explicit_web_preferences`, `preload_entrypoints`, `context_bridge_apis`, `native_addon_bindings`…)"; `2026-10-13-r4-07-jsc-bytecode.md:119` records that "`/usr/share/typora/Typora` itself IGNORES `ELECTRON_RUN_AS_NODE`". A `.asar` path and an `electron-main` node therefore carry no Electron-ownership evidence.
- Where ownership *is* claimed, it rests on a launcher/exec fact, not a folder: `2026-10-13-asar-surface.md:15` — "`/usr/bin/obsidian` execs `electron43 /usr/lib/obsidian/app.asar`". Also `:21`: `file(1)` misreports obsidian's `app.asar` as `data` while it is a valid Electron ASAR — extension/`file` output is not evidence either.
- Consequence for C04: the new entry must keep the scope fence "no Electron, ASAR, ESM, bundler or `exports`-field ground", and must not restate the rejected entry's `electron-main` sentence — round-61 `falsify-w3/W3JsElectronMainLabel.md` graded that clause BROKEN because the provider's own 6.4.0 docs define the node as an inferred Electron main role (`docs/javascript-application-graph.md:60`, `docs/javascript-artifact-reconstruction.md:65-66`), so "a neutral kind name" misstates record semantics.

## Evidence 4 — the derivation round 61 found missing (my lane's deliverable)

Frozen revenger tree `a3498e25ad87bf756288812d0ea7c474b09433c7`, extracted read-only to `/fast/scratch/hyaku/revenger-r62/R62ConnectJsPrior/` (`git archive`). The rejected entry's `Limitations` claimed "this entry's block carries those values" for *edge spans*; `falsify-w3/W3JsOverclaimCritic.md` B1 measured 0 matches of `location|start|span|column` in that block. The saved records **do** carry the spans — the derivation was simply never printed. Derived from `corpus/live/runs/20261012T164357Z/analysis.json` (v1) and `corpus/live/runs/round-7/v2-analysis.json` (v2), stdlib only, no JavaScript executed:

- v1 `js-r3/index.js` sha256 `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7`, line 1 = `const { rot13, checksum } = require('./transform');` (51 chars). v2 `js-r7-v2/index.js` sha256 `b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a`, line 1 = `const { rot13 } = require('./transform');` (41 chars).
- **Every** `imports` edge in both graphs carries `evidence.location` = `{kind: "source-range", source: "index.js", start/end {line,column}}`, `state` `inferred`, `authority` `static-relationship-inference`. v1: named `rot13` and `checksum` edges span `1:6-1:50`; the unnamed `kind: "require"` edge spans `1:28-1:50`. v2: named `rot13` `1:6-1:40`; unnamed require edge `1:18-1:40`.
- **The edge range is statement-wide and does NOT localise the name.** Under the 0-based half-open reading (see below) `1:6-1:50` slices to `{ rot13, checksum } = require('./transform')` and `1:28-1:50` to `require('./transform')`.
- The **per-name** spans live in the semantic graph, not on the edge: `expression` nodes `destructure:/rot13` `role_key object:destructure:8:13` (slice `rot13`), `destructure:/checksum` `object:destructure:15:23` (slice `checksum`); `binding` nodes labelled `rot13`/`checksum` at the same ranges; `call-site` `role_key call:call:call:28:50` (v1) / `call:call:call:18:40` (v2) slicing to `require('./transform')`; `expression` `require` at `28-35`/`18-25`; `argument 0` at `36-49`/`26-39` slicing to `'./transform'`.
- **Column convention [INFERENCE from byte reconstruction, not documented]:** 0-based start column, exclusive end column. Corroborated inside the lane by a committed verifier that already uses exactly this convention: `corpus/verify_semantic_trace.py:73-76` requires `source_lines[start["line"]-1][start["column"]:end["column"]] == name`; I ran it on the frozen copy → `POSITIVE … 3/3 returned captures match source tokens and saved parent` and `--self-test` → `NEGATIVE REJECTED relation differs from source parent` (a mutated `start.column` is caught).
- The round-7 comparison record `corpus/live/runs/round-7/comparison.json` (sha256 `f6c9a3cd7d0d80cfad82f7e9a4837e7b0e8aa8bc8c5b816dff51c50c9365f918`, `ev_5e4b17c1…`) carries 5 `imports` edges, 3 with non-null `imported_name`, with the same spans (`1:6-1:50` ×2, `1:6-1:40`, `1:28-1:50`, `1:18-1:40`) — but its `items[]` carry no named-import dimension. "The comparison items do not report the delta" and "the comparison record has no import-name fields" are different claims; the second is false.

Full script + captured output: `/fast/scratch/hyaku/revenger-r62/R62ConnectJsPrior/evidence_c04_span_ground.py` and `.out`; drop-in derivation text for the entry writer: `/fast/scratch/hyaku/revenger-r62/R62ConnectJsPrior/proposed_c04_span_ground.md` (scratch, not landed).

## Honesty limits the new entry must carry

- The semantic graph's columns are **not** uniformly exact: of 187 source-range spans (both graphs, file+line resolvable inside the fixture), 122 slice to a bare identifier and 71 equal their node's own label (19/19 `binding`, 8/8 `parameter`, 44/110 `expression`); 65 are neither (e.g. `nsfor`, `aultI`). Claim exactness only for the spans actually printed.
- "Each named import edge carries its name's span" is **unsupported** — the edge range is statement-wide; the name's range is a separate semantic-graph fact.
- The `imports` edges are `state: inferred` static relationships; no runtime loading, export-binding, package-resolution or Electron claim follows.
- Q13 credit is clause-scoped: `verify_semantic_trace.py` guards the source-token slicing convention and the three captured names (its own negative rejects a mutated column); `verify_js_graph_delta.py:41` checks only `location.source == "index.js"`, and `verify_saved_evidence.py:107-108` checks `state`/`source`/`start.line == 1` but **not** columns — the edge span columns are unguarded and must be named as such.
- Per routed item 1 (`corpus/lessons/round-61-verifier-spotcheck.md:206-210`), these scratch derivations are **not** the in-entry derivation: the candidate must carry its own command and printed output; my checks are supporting material only, and the row stays uncovered until a fresh falsify wave and explicit all-criteria admission.

## Proposed move (one bounded, for the C04 entry writer / L1)

Adopt the Evidence-4 derivation as the candidate's in-entry `## Reproduce`+`## Provenance` span block, printed per `imports` edge (`imported_name`, `kind`, `specifier`, `resolved_path`, `resolution_status`, `location.value`, `state`, `authority`) and per `destructure:/` / `binding` semantic node (`role_key`, span, byte slice), with the column convention labelled as an inference and the edge-vs-name distinction stated; report kaidoku `2026-10-13-r4-09-js-export-compare.md:59,65` in the Q10 row; drop every `electron-main` semantics sentence and keep the no-Electron/no-ASAR fence.

## Risks

- **R1** repeating round-61's overclaim by asserting edge spans localise names → stated explicitly as false above.
- **R2** restating `electron-main` as a neutral kind name → repeat of `W3JsElectronMainLabel` BROKEN; fence instead.
- **R3** importing kaidoku's Electron/ASAR holdings as C04 support → different artifacts and a different representation (unresolved `require:` keys); would violate Q01/Q10 and the no-Electron scope.
- **R4** an unverifiable column convention → the convention is an inference from byte reconstruction, corroborated by `verify_semantic_trace.py`; it must be labelled, not asserted as documented.
- **R5** a new source row for kaidoku would need its own opened-source discipline; L1 owns S-row writes — none written by me.

## Verification performed (scratch only, no production edit)

`git archive a3498e25` extraction; read-only greps over kaidoku's corpus with digests and HEAD recorded; stdlib `python3 -B` derivation over the two saved graphs, the comparison record and the fixture bytes; `corpus/verify_semantic_trace.py` (+`--self-test`) run on the frozen copy; `git status --porcelain` → only `?? .ufo/waves/round-62/` (this untracked wave dir, no tracked file changed). Not run: `measure.py`, REA producers, fixture JS, bytecode, network.

Installs: none (no tool installed or updated).
