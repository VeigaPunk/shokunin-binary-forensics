RESULT: COMPLETE

# R62ReviewJsNames — C04 named-import values vs destructured source names

Scope: `normalized_result.graph` `imports`-edge `properties.imported_name` in the two primary C04 saved records; target-node kinds/identities; `graph` vs `semantic_graph`. No admission claimed; README rows untouched (C04/C09 stay uncovered); prior rejected entry and round-61 evidence untouched.

**Verdict: set equality is NOT a binding-to-exports claim.** The `imported_name` values equal the names the fixture destructures from `require('./transform')` — a source-text name match. No record field ties those names to an exported member.

## Evidence

Primary records: `corpus/live/runs/20261012T164357Z/analysis.json` (sha256 `7c3ba8c1…`, ev `ev_4a93276c…`) and `corpus/live/runs/round-7/v2-analysis.json` (sha256 `331ec252…`, ev `ev_66f5dc7e…`). Command (stdlib only, lane root; no JS executed, no provider called): `python3 -B /fast/scratch/hyaku/revenger-r62/R62ReviewJsNames/js_names_evidence.py` → output `…/R62ReviewJsNames/js_names_evidence.out`; supporting probes `inspect_names.out`, `inspect_semantic.out`, `inspect_slots.out`, `verify_slice.out`, `probe_calls.out`, `probe_destructure.out`, `probe_alias.out` beside it. Cited as `js_names_evidence.out:LINE`:

- `:4` `v1 imports_total=3 named=2 named_values=['checksum','rot13'] equals_src_destructured=True`; `:12` `v2 imports_total=2 named=1 named_values=['rot13'] equals_src_destructured=True`.
- `:6`/`:10` named edge → `target kind='javascript-module' namespace='source-module'`, span 1:6→1:50, slice `{ rot13, checksum } = require('./transform')`; `:8`/`:14` unnamed edge → `target kind='javascript-asset' namespace=None key=None`, span 1:28→1:50 (v1) / 1:18→1:40 (v2), slice `require('./transform')`.
- `:17`/`:18` `exposes_exported_names=['default','default'] module_export_nodes=2 exported_name_in_src_names=[]`.
- `:19`/`:20` `has_imports_relation=False`, `destructure_nodes=[('index.js','destructure:/checksum',15,23),('index.js','destructure:/rot13',8,13)]` (v1) / `[(…,'destructure:/rot13',8,13)]` (v2), `family_status={'partial': 12}`, `unknowns=32`/`25`; `:21`/`:22` `imports_edge_spans_to_names={(6,50): ['rot13','checksum'], (28,50): [None]}` `distinct_spans=1`.

Binding-to-exports is foreclosed by four record facts: `exported_name` is `null` on every `imports` edge; the only exported names anywhere are `default` (2 `exposes` edges per graph, one per module), so `exported_name_in_src_names` is empty; the named edges target the `transform.js` `javascript-module` node (namespace `source-module`), not a `module-export` node; the two `module-export` nodes (`[<root>,index.js,default]`, `[<root>,transform.js,default]`) contain neither `rot13` nor `checksum`. `transform.js` does write `module.exports = { rot13, checksum }`, but that is fixture source truth only, absent from the saved graph.

**Target node kinds/identities (named ≠ unnamed).** named `imports` → `javascript-module`, namespace `source-module`, key `<root_artifact_sha256>:transform.js`, stability `artifact-version`; unnamed `imports` → `javascript-asset`, identity `{sha256, stability global-exact, strategy content-digest}`, **no namespace, no key**; `exposes` targets → `javascript-module`, namespace `module-export`.

**`graph` vs `semantic_graph`.** `imports`/`imported_name` exist only in `normalized_result.graph` (`JavaScriptApplicationGraph`, ids `jag_2b3e4fab…`/`jag_50ff7754…`, `coverage.status=complete`, `omitted_count=0`). `semantic_graph` (`JavaScriptSemanticRelationGraph`, `application_graph_id` = that graph id) has **no `imports` relation**; the names occur there only as `expression` nodes `destructure:/rot13` / `destructure:/checksum` inside `index.js` (`operation_kind=destructure`, `property_path=[name]`), and **0 relations cross a module boundary** in either record (`probe_alias.out`). Its coverage status is `unknown`, all 12 families `partial` (32 / 25 unknowns) — not citable as complete. Span localization therefore differs — the round-61 Q11 trap re-encountered: in v1 **both** named edges carry one shared range 1:6→1:50, so the application-graph edge range does **not** isolate a name; per-name ranges live only in `semantic_graph` (`destructure:/rot13` 1:8–1:13, `destructure:/checksum` 1:15–1:23, each slicing exactly to its name). The `require()` call span agrees across both graphs: unnamed `imports` edge 1:28→1:50 (v1) / 1:18→1:40 (v2) = `require('./transform')`, matching semantic call-site role keys `call:call:call:28:50` / `call:call:call:18:40`.

## Proposed artifact

`/fast/scratch/hyaku/revenger-r62/R62ReviewJsNames/proposed-wording.md` — drop-in exact wording restricted to `normalized_result.graph` `imported_name` values, plus a 6-item hazard list: no "named import"/"binding"/"resolved export" phrasing; no claim the graph records `rot13`/`checksum` as exports; no claim the edge range isolates a name; no "semantic_graph is complete"; do not conflate named/unnamed target kinds; do not count names from `round-7/comparison.json` (its `imports` values `['rot13','rot13','checksum']` are the two-sided comparison, not either primary record).

## Q13 verifier credit boundaries (observed)

`python3 -B corpus/verify_js_graph_delta.py --self-test` → `POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only` / `NEGATIVE REJECTED saved graph disagrees with source truth`. Creditable for the Evidence IDs, the named `imported_name` set, named-edge provenance fields, no-duplicate-names, the `checksum` removal, package-main mapping. **Unguarded**: `exported_name` null, `exposes`/`default` inventory, `module-export` identities, any edge range, the unnamed edge, `semantic_graph` `destructure:/` nodes — name them unguarded. `python3 -B corpus/verify_saved_evidence.py --self-test` → `NEGATIVE JS REJECTED: JS: wrong package-main mapping`; that negative mutates only the package-main mapping, so it is **not** evidence a name-set mutation is caught.

## Unknowns / not claimed

Aliasing, rest, nested, computed destructuring, several `require` calls, non-literal specifiers, `exports` precedence, ESM, bundles, ASAR: none occurs in these fixtures; no claim made. No runtime-loading, Electron-role, provider-method, package-resolution or export-detection claim.

## Harms

None. No corpus/fixture/live byte modified (`git status --porcelain -- corpus/` empty; fixture digests `f7d8bf47…`/`b53d96d4…` unchanged); no README, map, SCORECARD or lesson edited; no jj/Git index or history touched; no subagent dispatched. Installs: none.
