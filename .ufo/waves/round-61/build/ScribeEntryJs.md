# ScribeEntryJs — round 61 C04 candidate entry (draft, not written to the lane)

Scope: C04 (JavaScript/Electron packages) only. C09 (EVM) and the C2 receipt-command control belong to other seats and are not drafted here. Nothing was written to `corpus/`; the draft below is the deliverable. It runs past the 70-line report cap only because the assignment asks for the full entry in the report.

Installs/updates: none. Scratch only: `/tmp/revenger-r61-ScribeEntryJs-repro.py` (read-only derivation script, run with `python3 -B` from the lane root; exit 0).

## Draft entry — `corpus/knowledge/commonjs-static-import-edges.md`

```
source: S016 (proposed by ScribeSourcesRowsJs, unregistered) — https://nodejs.org/api/modules.html — anchor `#folders-as-modules` ("Folders as modules"); page title "Modules: CommonJS modules | Node.js v26.12.1 Documentation" (meta node-version v26.12.1); opened 2026-10-21
source: S017 (proposed by ScribeSourcesRowsJs, unregistered) — https://nodejs.org/api/packages.html — anchor `#main` ("main"); page title "Modules: Packages | Node.js v26.12.1 Documentation" (meta node-version v26.12.1); opened 2026-10-21
source: fixtures `corpus/fixtures/js-r3/`, `corpus/fixtures/js-r7-v2/` (authored, pinned by SHA-256 below) and saved REA records `corpus/live/runs/20261012T164357Z/analysis.json` (Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`) and `corpus/live/runs/round-7/v2-analysis.json` (Evidence `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`)
verified-at: 2026-10-21
recheck: save the `## Reproduce` block as a file; run `python3 -B <file>` from the lane root (stdlib only, read-only); expected output in `## Provenance`
coverage-map: C04

# CommonJS destructured `require` and package `main` as static import edges — two authored fixtures

Narrow claims about what the saved REA static JavaScript graphs record for one authored CommonJS package family (`js-r3` and its one-name-removed sibling `js-r7-v2`, rea-agents@6.4.0 per the round-3 and round-7 ledgers). Every fact below is re-derived by the `## Reproduce` block on 2026-10-21 from fixture bytes and the saved records, not taken from ledger prose (Q03/Q08/Q11). No JavaScript was executed.

## Observation

1. **Fixture identity.** `index.js` (v1) `f7d8bf47…`; `transform.js` (both) `cd9f3f63…`; `package.json` (both) `92ef8e3d…`; `index.js` (v2) `b53d96d4…`. Full digests in `## Provenance`. The v1 `index.js` digest equals the saved record's `art_f7d8bf47…` identifier; the v2 `index.js` equals the round-7 record's artifact identifier.
2. **Source import.** v1 line 1 is `const { rot13, checksum } = require('./transform');` (names `checksum`, `rot13`); v2 line 1 is `const { rot13 } = require('./transform');` (names `rot13`). Both use one `require` call and specifier `./transform`. `package.json` `main` is `"index.js"` in both, and `index.js` exists in both.
3. **Saved v1 graph.** Coverage `complete`, 0 omitted, 10 nodes, 13 edges. Relations: `contains` 6, `exposes` 2, `imports` 3, `loads` 1, `maps_to` 1. States: `observed` 5, `inferred` 8. The three `imports` edges are one edge with no `imported_name` (specifier `./transform`, resolved `transform.js`) plus one named edge each for `rot13` and `checksum`, all resolved to `transform.js`. The `maps_to` edge with `resolution_context: package-entrypoint` resolves to `index.js`, state `inferred`.
4. **Saved v2 graph.** Coverage `complete`, 0 omitted, 10 nodes, 12 edges. Relations: `contains` 6, `exposes` 2, `imports` 2, `loads` 1, `maps_to` 1. States: `observed` 5, `inferred` 7. `imports`: one unnamed edge plus one named `rot13` edge, resolved `transform.js`. Package-entrypoint `maps_to` resolves to `index.js`, state `inferred`.
5. **Agreement with source.** For each record the set of named-import names equals the set destructured in source, and the package-entrypoint resolved path equals `package.json` `main` (both `True`).
6. **Delta v1 → v2.** Named imports removed: `checksum`; added: none; kept: `rot13`. Edge count 13 → 12; `imports` 3 → 2; `inferred` 8 → 7; all other relation counts unchanged.
7. **Primary text, verbatim.** S017 `#main`: "The "main" field defines the entry point of a package when imported by name via a node_modules lookup. Its value is a path." S016 `#folders-as-modules`: "if the "main" entry is missing or cannot be resolved, then Node.js will attempt to load an index.js or index.node file out of that directory" (both quoted from the pages fetched 2026-10-21).

## Inference

- In this family, one destructured `require` statement produces one unnamed `imports` edge plus one named `imports` edge per destructured name, all sharing specifier and resolved path. Scope: two files, one `require` statement each.
- The REA `package-entrypoint` `maps_to` edge records the package's `main` value as its resolved path. Node's documented meaning of `main` (S017) matches what the edge records; this is a static statement about the package's declared entry, not about Electron or any runtime load.
- The v1 → v2 named-edge removal of `checksum` is consistent with the one-line source change; it is not a runtime observation.

## Unknown

- **Whether the entrypoint edge comes from `main` or from the default fallback.** On this family `main` is `index.js`, which is also Node's fallback (S016). The fixture cannot separate the two. The entry does not claim the `main` mapping is discriminated.
- Renamed destructuring (`{ rot13: r }`), non-destructured `require` with member access, multiple `require` statements, and computed specifiers: not tested.
- Binding semantics of destructuring (ECMAScript): no source opened in round 61; the entry makes no claim about them.
- Whether REA's edges match runtime behavior: not measured. `rot13` and `checksum` were never called.
- `exports` precedence (S017, `#package-entry-points`): fixtures have no `exports` field; not tested.
- The `electron-main` node label on the package entry: REA's convention per the round-3 ledger; no Electron API appears in these fixtures (`grep -ril electron` exit 1).
- Directory subject digests `8eec9ffb…` (v1) and `696c2496…` (v2): recorded in the saved records; the hashing method was not reproduced. Recorded, not re-derived.

## Limitations

- One authored three-file family (`js-r3`, `js-r7-v2`) and two saved REA runs. No claim about real packages, bundles, ESM, or other `require` shapes.
- Static only. The graph's own limitations (`Static imports, entrypoints … do not prove runtime execution`) apply.
- The saved records were produced by `rea-agents@6.4.0 analyze-javascript-application` (round-3 and round-7 ledgers; recorded, not re-run here). This entry scores saved output against fixture bytes; it does not credit the tool's explicit output as truth.
- The round-7 comparison workflow (`compare-application-versions`, Evidence `ev_5e4b17c1db1a06126558586f188b8eae81117c4d4bdf43d2278aefcd945f1a78`) did not report the removed named import (0/1 in the round-7 ledger, recorded). Use per-graph edges, not the comparison output, for this delta.

## Reproduce

```python
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

F = Path('corpus/fixtures')
R = Path('corpus/live/runs')
RECORDS = {'v1': R / '20261012T164357Z/analysis.json', 'v2': R / 'round-7/v2-analysis.json'}
FIXTURES = {'v1': F / 'js-r3', 'v2': F / 'js-r7-v2'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


for tag, d in FIXTURES.items():
    for name in ('index.js', 'transform.js', 'package.json'):
        print(f'{tag} {d.name}/{name} {sha(d / name)}')

source = {}
for tag, d in FIXTURES.items():
    text = (d / 'index.js').read_text()
    m = re.search(r"^const\s*\{([^}]+)\}\s*=\s*require\(['\"]([^'\"]+)['\"]\);", text, re.M)
    names = sorted(p.strip() for p in m.group(1).split(','))
    main = json.loads((d / 'package.json').read_text())['main']
    source[tag] = (set(names), main)
    print(f'{tag} source destructured={names} specifier={m.group(2)} main={main!r} main_file_exists={(d / main).is_file()} require_calls={text.count("require(")}')

for tag, path in RECORDS.items():
    rec = json.loads(path.read_text())
    g = rec['normalized_result']['graph']
    nodes = {n['node_id']: n for n in g['nodes']}
    print(f'{tag} record {path.name} sha256={sha(path)}')
    print(f'{tag} evidence_id={rec["evidence_id"]} subject_sha256={rec["subject"]["digest"]["sha256"]}')
    print(f'{tag} graph coverage={g["coverage"]["status"]} omitted={g["coverage"]["omitted_count"]} nodes={len(nodes)} edges={len(g["edges"])}')
    print(f'{tag} relations={dict(sorted(Counter(e["relation"] for e in g["edges"]).items()))}')
    print(f'{tag} states={dict(sorted(Counter(e["evidence"]["state"] for e in g["edges"]).items()))}')
    imports = [e["properties"] for e in g["edges"] if e["relation"] == "imports"]
    named = sorted(p["imported_name"] for p in imports if p.get("imported_name"))
    print(f'{tag} imports={len(imports)} named={named} unnamed_require={sum(1 for p in imports if not p.get("imported_name"))}')
    print(f'{tag} named_import_specifiers={sorted({p["specifier"] for p in imports})} resolved={sorted({p["resolved_path"] for p in imports})}')
    entry = [e for e in g["edges"] if e["relation"] == "maps_to" and e["properties"].get("resolution_context") == "package-entrypoint"]
    print(f'{tag} package_entrypoint_maps_to={len(entry)} resolved={[e["properties"]["resolved_path"] for e in entry]} state={[e["evidence"]["state"] for e in entry]}')
    src_names, src_main = source[tag]
    print(f'{tag} agrees_with_source names={set(named) == src_names} main={entry[0]["properties"]["resolved_path"] == src_main}')

v1_named = {p for p in [e["properties"].get("imported_name") for e in json.loads(RECORDS["v1"].read_text())["normalized_result"]["graph"]["edges"] if e["relation"] == "imports"] if p}
v2_named = {p for p in [e["properties"].get("imported_name") for e in json.loads(RECORDS["v2"].read_text())["normalized_result"]["graph"]["edges"] if e["relation"] == "imports"] if p}
print(f'delta named removed={sorted(v1_named - v2_named)} added={sorted(v2_named - v1_named)} kept={sorted(v1_named & v2_named)}')
```

## Provenance (Q11)

Run `python3 -B <file>` from the lane root at base `e0a4b0c` (2026-10-21); observed output, exit 0:

```text
v1 js-r3/index.js f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7
v1 js-r3/transform.js cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345
v1 js-r3/package.json 92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7
v2 js-r7-v2/index.js b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a
v2 js-r7-v2/transform.js cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345
v2 js-r7-v2/package.json 92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7
v1 source destructured=['checksum', 'rot13'] specifier=./transform main='index.js' main_file_exists=True require_calls=1
v2 source destructured=['rot13'] specifier=./transform main='index.js' main_file_exists=True require_calls=1
v1 record analysis.json sha256=7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452
v1 evidence_id=ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e subject_sha256=8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32
v1 graph coverage=complete omitted=0 nodes=10 edges=13
v1 relations={'contains': 6, 'exposes': 2, 'imports': 3, 'loads': 1, 'maps_to': 1}
v1 states={'inferred': 8, 'observed': 5}
v1 imports=3 named=['checksum', 'rot13'] unnamed_require=1
v1 named_import_specifiers=['./transform'] resolved=['transform.js']
v1 package_entrypoint_maps_to=1 resolved=['index.js'] state=['inferred']
v1 agrees_with_source names=True main=True
v2 record v2-analysis.json sha256=331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e
v2 evidence_id=ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c subject_sha256=696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655
v2 graph coverage=complete omitted=0 nodes=10 edges=12
v2 relations={'contains': 6, 'exposes': 2, 'imports': 2, 'loads': 1, 'maps_to': 1}
v2 states={'inferred': 7, 'observed': 5}
v2 imports=2 named=['rot13'] unnamed_require=1
v2 named_import_specifiers=['./transform'] resolved=['transform.js']
v2 package_entrypoint_maps_to=1 resolved=['index.js'] state=['inferred']
v2 agrees_with_source names=True main=True
delta named removed=['checksum'] added=[] kept=['rot13']
```

Primary-text provenance: `https://nodejs.org/api/packages.html` (page title "Modules: Packages | Node.js v26.12.1 Documentation", meta node-version v26.12.1; section `#main`) and `https://nodejs.org/api/modules.html` (page title "Modules: CommonJS modules | Node.js v26.12.1 Documentation"; section `#folders-as-modules`), both opened 2026-10-21 (access date 2026-10-21). The pages show no revision date.

## QUALITY check

| Q | verdict | basis |
|---|---|---|
| Q01 | pass, conditional on S016/S017 registration | `main` meaning rests on S017 (tier A for `main`); fallback on S016 (tier A); edge facts on saved records and bytes (own-work, tier A for what they contain) |
| Q02 | pass | source/verified-at/recheck headers present; coverage-map row named |
| Q03 | pass | expected values from fixture bytes (`re` pattern on `index.js`, `main` from `package.json`), not from the saved record |
| Q04 | pass | tool named (`rea-agents@6.4.0`, provider `rea-javascript-application` v1); its saved output scored against bytes; the CLI was not re-run |
| Q05 | n/a | no readiness or capability claim |
| Q06 | pass | every fixture premise carries its SHA-256 from the Reproduce output |
| Q07 | n/a | no parser prediction is counted; falsifiers below are unscored |
| Q08 | pass | every count re-derived by command with output |
| Q09 | pass | digests cited only for the bytes hashed; no origin claim for saved records |
| Q10 | pass with scope | "main" is not discriminated from the `index.js` fallback (Unknown); two files, one require each |
| Q11 | pass | each value carries the command and output in `## Provenance` |

## First falsifiers (pre-registered, not run, not counted — Q07)

- F1: `package.json` `main` set to `lib/entry.js` (file present), `index.js` absent. Prediction: `maps_to` resolves to `lib/entry.js`. Falsifies the main-mapping half if REA resolves to `index.js` or emits no edge. Ground truth: S017 `#main`.
- F2: `main` absent, `index.js` present. Prediction: `maps_to` resolves to `index.js` via fallback. Ground truth: S016 `#folders-as-modules`.
- F3: `const { rot13: r } = require('./transform');`. Prediction: named edge with `imported_name` `rot13` and `local_name` `r`. Ground truth: ECMAScript destructuring (NOT sourced in round 61; TBD source row required before this counts).
- F4: two destructuring `require` statements from `./transform`. Prediction: one unnamed edge per statement. Tests the "one unnamed edge" inference.

## Ledger rows (for the round lesson, not written here)

- S016, S017: proposed by ScribeSourcesRowsJs (ids unregistered; `SOURCES.md` still ends at S015 in the lane).
- Fixture and record hashes: as in `## Provenance`.
```

## Findings (scoped)

- Derivation (run read-only, exit 0): both fixtures agree with saved graphs on named-import names and on the package-entrypoint path; delta is exactly `checksum` removed.
- The entry's main-mapping half does not discriminate from the `index.js` fallback on this fixture family. Entry scopes it as Unknown; it is the first falsifier (F1), not a counted result.
- Round-7 comparison output missed the named-import delta (0/1, recorded in round-7 ledger). The entry uses per-graph edges instead.
- No EVM content, no C2 mutant work, no lane writes. Scratch: `/tmp/revenger-r61-ScribeEntryJs-repro.py`.

## Verdict

C04 candidate entry drafted and derivation-checked: admissible under Q01–Q11 once S016/S017 are registered, with the `main` half scoped as undiscriminated from the default fallback (reviewer decision). Installs: none.
