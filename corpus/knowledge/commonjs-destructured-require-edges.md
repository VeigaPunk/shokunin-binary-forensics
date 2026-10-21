source: S027 (saved `analyze_javascript_application` records ev_4a93276c… and ev_66f5dc7e…); S020 Node.js v26.12.1 "Modules: CommonJS modules", "All together" (LOAD_AS_FILE, LOAD_AS_DIRECTORY) and "Folders as modules"; S021 Node.js v26.12.1 "Modules: Packages", `"main"` and "Package entry points"; S022 ECMA-262 draft 2026-10-16 §14.3.1.3 and §14.3.3.3; S023 Node.js v26.12.1 "Modules: ECMAScript modules", "CommonJS Namespaces"
verified-at: 2026-10-21, lane base e0a4b0c4348ef1fade46539f520e94fa140c4d8a; fixture bytes and saved records re-derived by `## Reproduce`
recheck: save the `## Reproduce` block as a file and run `python3 -B <file>` from the lane root (stdlib only, read-only, executes no JavaScript); compare with `## Provenance`
coverage-map: C04 (CommonJS destructured `require` only; no Electron, ASAR, ESM, bundler or `exports` ground)

# Destructured `require` as named-import edges in two saved static graphs

This entry is about what two saved REA static graphs
(`rea-agents@6.4.0 analyze-javascript-application` per the round-3 and round-7
ledgers; recorded, not re-run) contain for one authored CommonJS package pair,
`js-r3` and its one-name-removed sibling `js-r7-v2`, checked against the
fixture source. Each fixture has exactly one `require` call, a relative
destructuring one. No JavaScript was executed. Despite the coverage row's
label, nothing here is Electron evidence.

## Observation

Values come from the `## Reproduce` output below.

1. **Source.** `js-r3/index.js` line 1 destructures `checksum` and `rot13`
   from `require('./transform')`; `js-r7-v2/index.js` destructures `rot13`
   only. Both `package.json` files declare `"main": "index.js"` and no
   `exports` field; `transform.js` and `package.json` are byte-identical
   across the pair.
2. **Named-import edges.** In each saved graph the set of `imports` edges with
   an `imported_name` equals the destructured names (v1 `checksum`, `rot13`;
   v2 `rot13`). Every `imports` edge has specifier `./transform` and resolved
   path `transform.js`; each graph also has one unnamed `imports` edge for the
   `require` call itself.
3. **Delta.** v1 → v2 removes exactly the named edge `checksum` (`imports`
   3 → 2, edges 13 → 12). This comes from the two per-graph edge sets; the
   round-7 comparison tool did not report it (0/1, recorded in the round-7
   ledger).
4. **Entrypoint edge.** Each graph has one `maps_to` edge with
   `resolution_context: package-entrypoint`, resolved to `index.js`, state
   `inferred`.
5. **Labels and exports.** Both graphs label the entry node kind
   `electron-main` although the fixtures contain zero `electron` tokens, and
   both record a single exposed export named `default`, not the
   `module.exports` keys.

## Inference

- S022 makes `const { a } = expr` an evaluation of `expr` followed by a
  property read of `a` from the result; it is not an import declaration. The
  saved `imported_name` edges therefore record names read from the value of a
  `require` call, matched to source text, not bindings to exports.
- S020's LOAD_AS_FILE order (`.js` first) makes `./transform` → `transform.js`
  the documented resolution for this layout; the edge agrees with it.
- `electron-main` is the provider's kind name for a package `main` file, not an
  observation that Electron was involved.

## Unknown

- **Whether the entrypoint edge reflects `main` or the folder fallback.** `main`
  is `index.js`, which is also the documented fallback when `main` is missing
  (S020). These fixtures cannot separate the two (S021 defines `main`).
- Aliased (`{ rot13: r }`), rest, nested or computed destructuring; several
  `require` calls; non-literal specifiers; `exports` precedence (S021); ESM;
  bundles; ASAR archives. None occurs in these fixtures.
- Export-side correspondence. Node itself detects CommonJS named exports by
  best-effort static analysis that "does not always correctly detect named
  exports" (S023), and these records keep only `default`.
- The directory subject digests (`8eec9ffb…`, `696c2496…`) are recorded, not
  re-derived; the hashing method was not reproduced.

## Limitations

- One authored package pair, one `require` site each, three named edges in
  total; two saved runs from 2026-10-12 with one provider version, while the
  host skill now names `rea-agents@6.7.0` (S002). No rate is quoted.
- Static only: the graphs do not show runtime loading, and `rot13`/`checksum`
  were never called.
- `corpus/verify_js_graph_delta.py` and `verify_saved_evidence.py` guard the
  names and the entry mapping but not the v2 digests, edge spans or the
  unnamed edge (`.ufo/waves/round-61/build/ReviewerJsVerifierRun.md`); this
  entry's block carries those values.

## Cross-lane contest (Q10)

Kaidoku holds the Electron/ASAR/JavaScript row
(`kaidoku-shokunin/corpus/README.md:23`) and an unresolved package `main` on a
real ASAR (`kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-renderer-asar.md:79-81`).
This entry claims neither; its own ground is the destructured-require edge on
authored CommonJS directories. The kaidoku/revenger split (ADJ-06) remains with
the operator.

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
    kinds = sorted({n.get("kind") for n in g["nodes"]})
    exposed = sorted({e["properties"].get("exported_name") for e in g["edges"] if e["relation"] == "exposes"}, key=str)
    print(f'{tag} node_kinds={kinds} exposes_exported_names={exposed} exports_field={"exports" in json.loads((FIXTURES[tag] / "package.json").read_text())} electron_tokens={sum((FIXTURES[tag] / n).read_text().lower().count("electron") for n in ("index.js", "transform.js", "package.json"))}')

v1_named = {p for p in [e["properties"].get("imported_name") for e in json.loads(RECORDS["v1"].read_text())["normalized_result"]["graph"]["edges"] if e["relation"] == "imports"] if p}
v2_named = {p for p in [e["properties"].get("imported_name") for e in json.loads(RECORDS["v2"].read_text())["normalized_result"]["graph"]["edges"] if e["relation"] == "imports"] if p}
print(f'delta named removed={sorted(v1_named - v2_named)} added={sorted(v2_named - v1_named)} kept={sorted(v1_named & v2_named)}')
```

## Provenance (Q11)

Observed output, run from the lane root on 2026-10-21 at base `e0a4b0c`, exit 0:

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
v1 node_kinds=['artifact', 'electron-main', 'javascript-asset', 'javascript-module', 'package'] exposes_exported_names=['default'] exports_field=False electron_tokens=0
v2 record v2-analysis.json sha256=331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e
v2 evidence_id=ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c subject_sha256=696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655
v2 graph coverage=complete omitted=0 nodes=10 edges=12
v2 relations={'contains': 6, 'exposes': 2, 'imports': 2, 'loads': 1, 'maps_to': 1}
v2 states={'inferred': 7, 'observed': 5}
v2 imports=2 named=['rot13'] unnamed_require=1
v2 named_import_specifiers=['./transform'] resolved=['transform.js']
v2 package_entrypoint_maps_to=1 resolved=['index.js'] state=['inferred']
v2 agrees_with_source names=True main=True
v2 node_kinds=['artifact', 'electron-main', 'javascript-asset', 'javascript-module', 'package'] exposes_exported_names=['default'] exports_field=False electron_tokens=0
delta named removed=['checksum'] added=[] kept=['rot13']
```

The source regex matches only the single-line destructuring form these
fixtures use; it is a fixture oracle, not a JavaScript parser (round-61 seat
`ExecJsOracleR7v2` shows it mis-reads aliases and rest elements).

## QUALITY check

| Q | verdict | basis |
|---|---|---|
| Q01 | pass | destructuring semantics on S022, resolution and fallback on S020, `main` on S021, export-detection limit on S023 (all tier A for their stated scope, opened 2026-10-21); saved outputs on S027 |
| Q02 | pass | `source:`, `verified-at:`, `recheck:` and `coverage-map: C04` headers |
| Q03 | pass | expected names and `main` come from fixture source bytes, not from the saved records |
| Q04 | pass | provider operation and recorded version named; only the provider's explicit edges are scored; the comparison tool's 0/1 is not credited |
| Q05 | pass (past tense) | no current capability claim; runs dated 2026-10-12, not re-probed |
| Q06 | pass | every fixture premise carries its SHA-256 from the block above |
| Q07 | n/a | no parser prediction is made |
| Q08 | superseded by Q11 | — |
| Q09 | pass | digests bind the hashed bytes only; Evidence IDs are recorded identifiers |
| Q10 | pass | scoped to one fixture pair and one provider version; kaidoku ground reported, not absorbed |
| Q11 | pass | every count, name and digest carries the command above and its output |
| Q12 | n/a | no rejected source row is cited as support |
| Q13 | pass | the two JS verifiers are credited only for the names and the entry path, whose forgeries their own negatives reject; digests, spans and the unnamed edge are named as unguarded |
