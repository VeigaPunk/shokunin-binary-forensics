RESULT: COMPLETE

Scope: propose S030 (own-work, tier A) for frozen fixtures js-r3/js-r7-v2
source text and the two saved graph records' fields. No corpus edit, no
admission, no README/K claim.

Frozen base
- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse a3498e25ad87bf756288812d0ea7c474b09433c7`
  -> `a3498e25ad87bf756288812d0ea7c474b09433c7`
- Extracted `git archive a3498… | tar -x` under
  `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceJsOwn/`.
- Opened: `corpus/fixtures/js-r3/{index.js,package.json,transform.js}`,
  `corpus/fixtures/js-r7-v2/{index.js,package.json,transform.js}`,
  `corpus/live/runs/20261012T164357Z/analysis.json`,
  `corpus/live/runs/round-7/v2-analysis.json` (all at the revision above).

Derivation (script + captured output in scratch: `derive_s030.py`,
`derive_s030.out`; `python3 -B derive_s030.py`, cwd = archive root)
- Fixture files (bytes, sha256):
  js-r3 index.js 274 f7d8bf47…69fd7; package.json 85 92ef8e3d…96d7;
  transform.js 379 cd9f3f63…a345; js-r7-v2 index.js 209 b53d96d4…c42a;
  package.json and transform.js byte-identical to js-r3 (same two digests).
- Records:
  js-r3 `…/analysis.json` 193573 B sha256 7c3ba8c1…d452, evidence_id
  ev_4a93276c…c1c7e; js-r7-v2 `…/v2-analysis.json` 171150 B sha256
  331ec252…564e, evidence_id ev_66f5dc7e…7987c (asserted equal in script,
  both True).
- Per-file graph identity equals frozen SHA-256 (script `equals_frozen=True`
  4/4 path-bearing nodes each record): index.js, transform.js, package.json
  (artifact kind) and package.json (package kind).
- Saved `subject.digest.sha256` / `root_artifact_sha256`
  (`8eec9ffb…` js-r3, `696c2496…` js-r7-v2) are directory digests; no method
  in the frozen tree re-derives them -> recorded, not derived.
- Source line 1, `js-r3/index.js:1`:
  `const { rot13, checksum } = require('./transform');` (7 words)
  `js-r7-v2/index.js:1`:
  `const { rot13 } = require('./transform');` (6 words)
- `normalized_result.graph.edges` relation `imports`:
  js-r3 total 3, named 2 — edges[4] imported_name/local_name `rot13`,
  edges[10] `checksum`, both specifier `./transform`, resolved_path
  `transform.js`, resolution_status `resolved`, module_link_kind `require`;
  edges[9] has specifier/kind=require/resolved_path but no imported_name.
  js-r7-v2 total 2, named 1 — edges[9] `rot13`; edges[2] unnamed equivalent.
- Module node: index.js import_relationships js-r3=2, js-r7-v2=1;
  module_format `commonjs`, export_names `["default"]` both.

Proposed artifact (scratch, for L1 to place)
- `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceJsOwn/S030-row-proposal.md`
  holds the full table row, the Gate note (opener this seat 2026-10-21, both
  located quotes), anchors and scope labels.
- Row shape: S030 | own-work | A | authored fixture bytes + literal saved
  per-file digest/import-name fields only | six file SHA-256, record SHA-256,
  `js-r3/index.js:1` quote, `graph.edges` `imports` properties | mined
  2026-10-21 | on-release | corpus/knowledge/round-62-commonjs-require-name-evidence.md.
- Rationale for a new row: S027 states what the provider outputs contain;
  S030 anchors the owned fixture text at a3498e2 and the digest identity
  between saved file nodes and those exact bytes, plus the literal saved
  import-name fields the C04 candidate compares against. If L1 judges the
  saved-field half duplicative of S027, the non-overlapping core is fixture
  text + per-file digest identity; S030 is not offered as provider support.

Honest limits / unknowns
- Saved records' `subject.local_path` is a prior checkout
  (`/home/vgpnk/Projects/prymeagnt/revenger/...`); correspondence rests on
  per-file digest equality, not path.
- No creation timestamp in either record; 2026-10-21 is this row's open date.
- Both fixtures' `package.json` name is `revenger-r3-fixture` (r7 included);
  recorded as authored text, no resolution claim.
- S030 claims no provider accuracy/coverage, no runtime loading, no Electron
  role, no general method, no authenticity, no C1/K/README admission. The
  retained rejected entry was not used as support.
- No other seat is claimed to have opened these bytes.

Installs: none.
