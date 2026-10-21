RESULT: COMPLETE

# R62JsDeltaOracle — independent source-name vs saved-import-name comparison (C04)

Scope: derive, from fixture bytes and from the two saved records **separately**, the
destructured-name sets and the saved `imports` `imported_name` sets; derive removed/added/kept;
derive **source-file** differences rather than a one-name label; state which cross-version
identity claims the records do and do not support. No entry authored, no README row flipped,
no corpus byte written, no JS executed, no producer/REA/chain call.
Ground: `reports/round-62/claims.md` (frozen `a3498e25`), `corpus/QUALITY.md:13-25`,
`corpus/lessons/round-61.md:105` (round-61 C04 Q11: block printed no location/column fields),
`corpus/lessons/round-61-verifier-spotcheck.md:39-45`, retained rejected candidate
`corpus/knowledge/commonjs-destructured-require-edges.md`.
Full detail with every excerpt: `/fast/scratch/hyaku/revenger-r62/R62JsDeltaOracle/findings_full.md`.

## Frozen scratch + integrity

`git -C …/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C
/fast/scratch/hyaku/revenger-r62/R62JsDeltaOracle` (`EXTRACT_OK`); pristine reference copy
`…/R62JsDeltaOracle_tree`; after every run `diff -rq …_tree/corpus …/corpus` →
`EXTRACT_CORPUS_IDENTICAL_TO_FROZEN`. Repo after all runs: `git status --porcelain` → only
`?? .ufo/waves/round-62/`; `corpus/live/runs/**` and fixture digests unchanged
(`analysis.json` `7c3ba8c1…`, `v2-analysis.json` `331ec252…`, `comparison.json` `f6c9a3cd…`,
`js-r3/index.js` `f7d8bf47…`, `js-r7-v2/index.js` `b53d96d4…`).

## Artifacts (scratch; cwd = extract root; stdlib only; stdout only; exit 0)

| file | purpose | sha256 |
|---|---|---|
| `js_delta_oracle.py` | full oracle, 10 sections | `559c90e0b3dd598e9a6fb686c856c7c06d5ebe8d10032ebc9bdf9038719172a2` |
| `js_delta_oracle.out` | its stdout (170 lines) | `90e3ff7b7965b8f87163f8c008e92585a527e2907026468cd3aca89e2bbdb6cf` |
| `proposed_entry_reproduce.py` | **in-entry `## Reproduce` block for the C04 candidate** | `a9db8ba3db29fbb99e458fc3c7f7fdb463f99adec00e49559575ed70b162907b` |
| `proposed_entry_reproduce.out` | its stdout | `c6d4341a308a0c7d1d29488e0a9f57b93c16d8c6642aba787da8656b71f81b54` |
| `verifier_mutation_probe.py` | Q13 clause-detection probe, 14 mutations | `05fcc5b835da806b4ec38eea5b70233baf89bf3610df20ab7bc0f8b56f60e46f` |
| `verifier_mutation_probe.out` | its stdout | `f78c0a125f91e25ef8001094a4a582f29974d43516787cf95dc3248ad2960dc6` |
| `measure_baseline.out` | unchanged round-61 probe, frozen extract, `cwd=/` | — |

## 1 Name delta — derived twice on the source side, once on the record side; all agree

Source derivation A (regex on the fixture line) and B (byte-scan to `require(`, walk back to
the braces, split on commas) agree: `v1 token_scan_names=['rot13','checksum'] regex_names=['rot13','checksum'] agree=True`;
`v2 token_scan_names=['rot13'] regex_names=['rot13'] agree=True`. Record side from `imports`
edges with an `imported_name`: v1 `{checksum, rot13}` (2 named + 1 unnamed), v2 `{rot13}`
(1 named + 1 unnamed); both `coverage=complete`, `omitted_count=0`, nodes 10/10, edges 13/12.

```
source_delta removed=['checksum'] added=[] kept=['rot13']
record_delta removed=['checksum'] added=[] kept=['rot13']
source_names_equal_record_names v1=True v2=True
deltas_agree=True
```

## 2 Source-file differences — not a one-name label

`index.js` differs in **two** lines (L1 destructuring, L5 render expression);
`transform.js` and `package.json` are byte-identical (`byte_identical=True`, `changed_lines=0`).
Consequences: the **export side is unchanged** — both versions contain
`module.exports = { rot13, checksum };` (`source_exports_checksum=True` in both), so a
"one name removed" label would wrongly imply the exported surface shrank. The removed name
leaves **two** source traces, binding (L1) and call site (L5): occurrence sites from bytes
are v1 `rot13` L1c8/L4c22, v1 `checksum` L1c15/L5c30, v2 `rot13` L1c8/L4c22 only.
**`checksum` is still in the v2 record**, only as `transform.js` definitions:
`v1 …by_source={'index.js': 4, 'transform.js': 4}`, `v2 …={'transform.js': 4}` — any claim
that the name "disappeared" from the v2 record is false.

## 3 No literal whole-edge equality (subject IDs differ)

For the kept name `rot13`, only `imported_name`, `specifier`, `resolved_path`,
`resolution_status` and `state` are equal across the two records. `edge_id`
(`jag_edge_66e056c7…` vs `jag_edge_7a0c9240…`), `source_node_id`, `target_node_id`,
`artifact_sha256` and `end_column` (50 vs 40) all differ; `subject_sha256_equal=False`,
`evidence_id_equal=False`, `graph_id_equal=False`; `shared_edge_ids=1 of 13/12` and that one
shared edge is the `loads`/package-entrypoint edge, not an import. The two v1 named-import
edges share **one** recorded location (both `1:6-1:50`), so the application graph gives no
per-name span there. Correct phrasing: the *name* `rot13` is kept; the *edge* is not the
same edge; no whole-edge equality may be asserted.

## 4 Spans re-derived from source bytes (the round-61 Q11 gap)

Recorded locations: v1 `checksum`/`rot13` both `1:6-1:50`; v2 `rot13` `1:6-1:40`; unnamed
require v1 `1:28-1:50`, v2 `1:18-1:40`. Re-derived (0-based columns, exclusive end):
`v1 loc_span edge=rot13 span_text="{ rot13, checksum } = require('./transform');"` ·
`v1 loc_span edge=<unnamed-require> span_text="require('./transform');"` ·
`v2 loc_span edge=rot13 span_text="{ rot13 } = require('./transform');"` ·
`end_column_equals_len_minus_1=True` · `start_column_equals_brace_col=True` ·
`start_column_equals_require_col=True` (unnamed edge only). Per-name spans live in the
record's **semantic graph** (exclusive end): `v1 binding rot13 L1 c8-13 'rot13'`,
`v1 binding checksum L1 c15-23 'checksum'`, `v2 binding rot13 L1 c8-13 'rot13'`; call-site
expression nodes `v1 expression checksum L5 c30-38 'checksum'`, `v1/v2 expression rot13
L4 c22-27 'rot13'`. Every source occurrence column equals the record node start column
(`source_column_equals_record_start=True`, 3/3). `checksum`'s call-site node exists only in
v1 — the second trace's absence in v2 is derivable in-entry.

## 5 Proposed in-entry artifact (not written by this seat)

`proposed_entry_reproduce.py` is a stdlib-only read-only block deriving every printed value:
fixture digests, source names/specifier/require-call count/occurrence sites, per-file
changed-line diff, saved imported names + recorded locations + edge/node identifiers +
record digests, source- and record-derived deltas, the kept-name field-by-field identity
table, relation-type inventories, and per-name binding/call-site spans — i.e. it prints the
span fields the round-61 block never printed. Run from the corpus root: `python3 -B <file>`;
output deterministic. Peer `R62JsEntry` should inline this block and paste
`proposed_entry_reproduce.out` as `## Provenance`. **No** `corpus/knowledge/` file, **no**
README row, **no** SOURCES row written here; S028–S031 are L1's to write from opened sources.

## 6 Q13 — clause detection measured (14 mutations × 2 verifiers)

Mutations applied only to throw-away copies under scratch `verifier_mutants/<case>`;
`corpus/live` never written. Baseline: both verifiers exit 0.
`verify_js_graph_delta.py` detects (exit 1): M1 v2 `rot13`→`checksum`, M2 v1 `checksum`→`rot13`
("duplicate named imports"), M3 v1 drop the `checksum` edge, M6 `resolved_path` change and
M7 specifier change and M8 edge state `observed` ("wrong static provenance"), M9 `maps_to`
path change. `verify_saved_evidence.py` detects: M2, M3 ("JS: missing/duplicate named
bindings"), M13 v1 `local_name` change ("JS: wrong import resolution").
**Unguarded by both (exit 0, POSITIVE — must be named unguarded):** M4 shift every `end`
column, M5 shift every `start` column, M10 drop `checksum` semantic-graph nodes, M11 drop
all semantic-graph nodes, M12 drop the unnamed `require` edge, M14 change every edge
`authority`. M6–M9 are also undetected by `verify_saved_evidence.py` alone. ⇒ the existing
verifiers guard the **name set** and **specifier/resolved_path/state** (delta verifier) and
**binding count/local_name** (saved-evidence verifier); they guard **no** recorded span,
**no** semantic-graph content, **no** unnamed edge, **no** authority. Round-61's Q13
over-credit is a live defect and must not be repeated.

## 7 The saved comparison record did not report the removed name

`corpus/live/runs/round-7/comparison.json` (`ev_5e4b17c1…`): `summary={"added":5,"changed":1,
"removed":5,"unchanged":4,"unknown":0}`, `matching={…,"exact_node_identity":2,
"exact_content_digest":2,"semantic_key":1,"unmatched":10,…}`, `coverage.status=
complete-within-inputs` (both sides `complete/0`), `items_mention_imported_name=False`,
`items_mention_checksum=False`, 15 items. The 5 removed / 5 added are unmatched module
nodes; `checksum` occurs only inside the embedded left graph (3 occurrences), never in an
item. The tool detects **0 of 1** removed named import; the delta comes from the per-record
name sets.

## 8 Mutant discrimination — a name set does not identify the source change

Synthetic mutants of `js-r7-v2/index.js` in scratch `mutants/` (not `corpus/fixtures`):
`M1_destructuring_only names=['rot13','checksum'] name_set_matches_v2=False changed_lines=2`;
`M2_render_only names=['rot13'] name_set_matches_v2=True changed_lines=2` with
`checksum_referenced_in_body=True checksum_destructured=False`. M2 changes the source while
leaving the name set identical ⇒ the entry must state the two-line source difference, not
only the name delta.

## 9 Baseline (unchanged round-61 probe, frozen extract, `cwd=/`)

`K_HELD=4/14 score=2.9` · `K_ROW C04 status=uncovered` · `K_ROW C09 status=uncovered` ·
`K_HELD_BACKED=4/14` · `C2_CONTROLS_PASS=2/2` · `C2_RECEIPT_B_KILLED=2/2` · `C2_D2_KILLED=2/2`
· `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` · `HOLD_CALIBRATION=4/4` · `HOLD_REPLAY=10/10` ·
`HOLDS_OK=yes`; exit 0. No flip performed, none authorized; C04/C09 stay `uncovered`
(`corpus/README.md:33`, `:38`).

## Unknowns / limits

Records are saved 2026-10-12 `rea-agents@6.4.0` output; nothing re-run — all record
statements are past tense about saved bytes. The v1/v2 subject digests `8eec9ffb…` /
`696c2496…` are recorded directory digests whose hashing method was not reproduced; the
three fixture file digests were re-derived. Static only: no runtime loading, no `checksum`
value, no Node export-detection result, no Electron claim — the record's `electron-main`
node kind / `electron-role` namespace are recorded facts about the saved graph. The
records' `exposes` edges name only `default`, so no export-side correspondence may be
claimed from them. Source-side naming uses two fixture-specific parses, not a JavaScript
parser: aliases, rest, nested or computed destructuring are not exercised. Whether the
comparison tool's unmatched module items track real program differences is unknown (its own
round-7 ledger says so).

## Proposed changes

None to production. The C04 entry writer should inline `proposed_entry_reproduce.py` + its
stdout, state the two-line source difference and the `transform.js`-only survival of
`checksum` in v2, avoid any whole-edge equality claim for the kept name, and name the
unguarded verifier clauses from §6.

Installs: none (python3 standard library only; no pacman/uv/npm/cargo transaction).
