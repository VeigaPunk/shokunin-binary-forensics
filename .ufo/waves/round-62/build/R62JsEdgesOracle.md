RESULT: COMPLETE

# R62JsEdgesOracle — independent saved-graph parser for the two C04 records

Axes: coverage (C1 C04 ground); Q11 derivability; Q13 guard-scope accuracy. Frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7`. Scratch `/fast/scratch/hyaku/revenger-r62/R62JsEdgesOracle/`.
No admission, no held flip, no README/corpus/report edit, no source row, no git/jj mutation. No JS executed, no producer called, no chain/RPC, no service.

## Artifacts (scratch only; full stdout in `parser_stdout.txt`, quoted sections in `excerpts.txt`)

| file | sha256 | lines |
|---|---|---|
| `parse_saved_graph_edges.py` | `dfae3f897c403040beedf454e8790cf98fb3b24b770d9f14bf2cb834bd1b1b4e` | 448 |
| `parser_stdout.txt` | `430b4dddb2a161274e6a9241d136a204994fd245008beff22a26dbcbb52d49e8` | 288 |
| `excerpts.txt` | `d003bfcd046570ad09efb574ff00fa0cc4609df2e7785e0a5348d9f3b37d6217` | 120 |
| `proposed_entry_readout.py` | `7057e65cd588d65f5168e8165423f09ad45ab8ab73bb51aa4db556bae2820729` | 114 |
| `proposed_entry_readout.stdout.txt` | `d9b2c37276bc115561c9fd28e81e4b057e9ff893d759fdfbc6eb0ad403cd9fd7` | 55 |
| `mutation_matrix.txt` | `19541de29ae545d03d8c3dd44825de3734e180c56ae5245782d1ec73f8b0210f` | 25 |

Extraction (cwd `/`): `mkdir -p /fast/scratch/hyaku/revenger-r62/R62JsEdgesOracle/archive && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C /fast/scratch/hyaku/revenger-r62/R62JsEdgesOracle/archive`; exit 0, no stdout.
Run (cwd archive): `python3 -B ../parse_saved_graph_edges.py .` → exit 0, stderr empty (`e3b0c442…b855`). Re-run byte-identical (`cmp` clean). Stdlib only (`hashlib,json,re,sys,pathlib`); reads the two saved records and two archived fixture dirs; executes nothing.

## Finding 1 — every `imports` edge, full saved fields (stdout §3)

v1 `imports_edges=3 of total_edges=13`; v2 `imports_edges=2 of total_edges=12`. Per edge the parser prints relation, `identifier_strategy`/`stability`, source+target node id/kind/identity (namespace, key, sha), `imported_name`/`imported_path`/`local_name`/`exported_name`, `specifier`/`resolved_path`/`resolution_status`/`module_link_kind`/`target_file_kind`/`target_json_status`/`kind`/`expression`, `evidence.state`/`confidence`/`authority`/coverage, extractor name+operation+version, evidence artifact sha+id, and the whole `source-range` location (source, start/end line and column).

Target kinds differ by edge role, both read from the saved node table: the **unnamed** require edge targets a `javascript-asset` node (identity `content-digest`, sha `cd9f3f63…a345` = transform.js bytes); the **named** edges target a `javascript-module` node (namespace `source-module`, key `<dir-sha>:transform.js`). Extractor operation also differs: `map-static-relationship` (unnamed) vs `resolve-semantic-module-relationship` (named). Every `imports` edge in both records: `state=inferred`, `confidence=high`, `authority=static-relationship-inference`, `coverage.status=complete`.

## Finding 2 — the saved column convention is DERIVED, not assumed (stdout §4)

The unnamed require edge carries the whole `require(...)` call, so its slice must equal the call text located independently in the authored source. All four candidate conventions tried in both records; exactly one reproduces it: `0-based, end-exclusive` (`v1` offsets `[28,50)`, `v2` `[18,40)`, each `slice_equals_require_call=YES`; the other three give `slice_equals_require_call=no` in both records) → `column_convention_chosen=0-based, end-exclusive`.

Independent corroboration using no import edge (§9): each `contains` whole-file `source-range` is `line1:col0 → lineN+1:col0` where N = the file's content-line count (`end_line_equals_content_lines_plus_one=True` for all four files, `end_column_zero=True`, `start_line_one=True`). Lines 1-based, columns 0-based, ends exclusive — consistent with the import-edge derivation.

## Finding 3 — span slices matched to source call text (§5, §10)

Each edge sliced with **its own** saved location under the derived convention (1-based columns; `excerpts.txt` §5):

```text
v1 unnamed-require cols 29-50 "require('./transform')"   v1 checksum cols 7-50 "{ rot13, checksum } = require('./transform')"
v1 rot13        cols  7-50 "{ rot13, checksum } = require('./transform')"
v2 unnamed-require cols 19-40 "require('./transform')"   v2 rot13 cols 7-40 "{ rot13 } = require('./transform')"
```

**Material fact the round-61 C04 rejection turned on.** In v1 the two *distinct* named edges (`rot13`, `checksum`) carry the **identical** saved range `[6,50)` — the whole destructuring pattern. `names_present_in_slice=['checksum','rot13']` for both; `span_uniquely_identifies_this_name=False` for both; each names the other in `span_text_identical_to_other_named_edge_span`. In v2 the single named edge's slice holds only `rot13` (`True`). So **a saved `imports` span does not localize a destructured name**; `imported_name` is the only per-name field. "Carries edge spans" must not be restated as "the span identifies the name". v1 `distinct_named_edge_spans=1` vs `distinct_named_names=2`; v2 `1` and `1`.

## Finding 4 — NAMES sets vs EDGES sets, unambiguous (§7, §8)

`v1 NAMES_set=['checksum','rot13'] count=2`; `v1 EDGES_set count=3 unnamed_require_edges=1 named_edges=2`; `v1 names_set_equals_edge_set=False (names_set_subset_of_edge_names=True)`. `v2 NAMES_set=['rot13'] count=1`; `v2 EDGES_set count=2 unnamed_require_edges=1 named_edges=1`; `v2 names_set_equals_edge_set=False (names_set_subset_of_edge_names=True)`.

NAMES ≠ EDGES: each graph has one extra unnamed `imports` edge for the `require` call itself, so names ⊂ edge-names strictly (2⊂3, 1⊂2). Equating "import names" with "import edges" is false by one edge per graph. Cross-version delta on both projections, so nothing is overclaimed:
- **NAMES delta** (the honest one): `removed=['checksum'] added=[] kept=['rot13']`.
- **EDGE signature incl. location columns**: `removed=3 added=2 kept=0` — the sources differ so columns move; this is *not* edge-set equality.
- **PROJECTED edge signature** (name|specifier|resolved|module_link_kind|kind|resolution_status|state; columns dropped): `removed=1` (the `checksum` edge), `added=0`, `kept=2`; `PROJECTED_sets_equal=False`.
- Identifiers are **not** equal across versions and must not be claimed so: `edge_id literal equality=False` (3 v1-only, 2 v2-only), `source_node_id` equality=False (none shared), `target_node_id` equality=False with exactly one shared target node `jag_node_b054a72f…` (the `content-digest` javascript-asset node for the byte-identical transform.js).

**`edge_id` is RECORDED, not re-derived** (§11): four bounded canonicalizations probed (relation|source|target; properties sorted-JSON; whole-edge sorted-JSON; source|target|properties) → `candidates_tested=4 matching_candidates=[]` for all five edges → `status=RECORDED (not re-derived here)`. The saved `identifier_strategy=semantic-content-sha256` is provider-declared; this seat does not reproduce it.

## Finding 5 — Q13 guard scope, measured on scratch copies only (mutation_matrix.txt)

Eight mutants of the archived v1 record, each run against the two existing JS verifiers (scratch copies under `mut/`; production tree untouched). `0`/`1` are verifier exit codes; "NOT detected" = exit 0 on a mutated record.

| mutant | change | `verify_js_graph_delta.py` | `verify_saved_evidence.py` |
|---|---|---|---|
| m1 | named `rot13` edge start/end columns → 99 | NOT detected (0) | NOT detected (0) |
| m2 | unnamed require edge columns → 7 | NOT detected (0) | NOT detected (0) |
| m3 | named `rot13` `target_node_id` → the `javascript-asset` node | NOT detected (0) | NOT detected (0) |
| m4 | swap `imported_name` only | NOT detected (0) | detected (1, `JS: wrong import resolution`) |
| m5 | unnamed require edge `kind` `require`→`import` | NOT detected (0) | NOT detected (0) |
| m6 | swap `imported_name`+`local_name`+`imported_path` together | NOT detected (0) | NOT detected (0) |
| m7 | delete the `checksum` named edge | detected (1) | detected (1) |
| m8 | add a third named edge `sha1` | detected (1) | NOT detected (0) |

The two JS verifiers guard the **name set** and the **resolution fields** and detect a name-count change; they do **not** guard saved spans/columns (m1, m2), target node kind/identity (m3), the unnamed edge's `kind` (m5), a self-consistent name swap (m6), or an extra unknown name in `verify_saved_evidence.py` alone (m8). The rejected entry credited them only for "the names and the entry path" — correct, and it must not be widened to spans, target kind or the unnamed edge. `verify_js_graph_delta.py --self-test` still rejects its own altered-v2 record (`NEGATIVE REJECTED saved graph disagrees with source truth`).

## Preserved evidence, unknowns, proposed changes

- `git diff --stat a3498e2 -- corpus/live corpus/fixtures corpus/knowledge corpus/QUALITY.md corpus/README.md corpus/SOURCES.md` → empty; `git diff --stat HEAD -- corpus/ reports/` → empty; `git status --porcelain` → only `?? .ufo/waves/round-62/`. `corpus/README.md:33` C04 and `:38` C09 remain `uncovered`. No held flip, admission, new gate, producer-capability, runtime, Electron-role or authenticity claim.
- Unknowns: (a) the provider's column convention is inferred from two fixtures — not confirmed against provider source; (b) `edge_id` derivation unresolved (4 candidates, none matched); (c) whether the shared named-edge span is provider design or fixture coincidence is **not** established — the observation stands as "identical saved range in this record"; (d) `target_json_status`/`expression` are `null` in both records, so their semantics are unexercised; (e) `raw_result` is `null` in both records, so nothing beyond `normalized_result` was readable. The rejected `corpus/knowledge/commonjs-destructured-require-edges.md` was read only to locate the frozen C04 claim and is **not** cited as factual support.
- Proposed production changes: none. `R62JsEntry` may embed `proposed_entry_readout.py` + `proposed_entry_readout.stdout.txt` (114-line script, 55-line exact stdout) as its `## Reproduce` block: it prints every `imports` edge with full saved fields, derives the column convention from the require-call text, slices each edge's own saved location, and prints NAMES/EDGES counts separately. It must also carry Findings 2–5, especially that v1's two named edges share one saved span, that `edge_id` is recorded rather than re-derived, and that the existing verifiers guard neither spans nor target kind.
- Installs or updates: none.
