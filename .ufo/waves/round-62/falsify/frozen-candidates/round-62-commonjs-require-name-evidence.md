source: S029 — ECMA-262 object binding and import-name roles, https://tc39.es/ecma262/ (row `mined`, opened 2026-10-21; cited here as the existing row, pending independent audit) — anchor: Draft ECMA-262 October 16 2026, §14.3.1.3 BindingEvaluation, §14.3.3.3 KeyedBindingInitialization, §16.2.1.7 Table 54, §16.2.2 Imports; single-page SHA-256 `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`; this entry uses only the §14.3.3.3 property-read text, quoted in §Sources
source: S030 — Authored CommonJS bytes and saved graph literals, `corpus/fixtures/js-r3`, `corpus/fixtures/js-r7-v2`, `corpus/live/runs/20261012T164357Z/analysis.json`, `corpus/live/runs/round-7/v2-analysis.json` (row `mined`, opened 2026-10-21; cited here as the existing row, pending independent audit) — scope: fixture text and literal saved import-name/location fields at `a3498e25ad87bf756288812d0ea7c474b09433c7`; anchor: each fixture `index.js:1`, saved `normalized_result.graph.edges` where `relation=imports`, `properties` and `evidence.location.value`; record SHA-256 `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452` and `331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e`
verified-at: 2026-10-21
recheck: `python3 -B readout.py <archive-root>` (full code and exact stdout in §Reproduce) -> exit 0, 25 stdout lines, stdout SHA-256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416`; the archive root is the extraction of the frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7` (`git archive a3498e25… | tar -x -C <scratch>/tree`)
coverage-map: C04 (`corpus/README.md`, JavaScript/Electron packages) — candidate; the map row stays `uncovered` until a fresh falsify wave and an explicit all-criteria admission
admission-status: candidate (not admitted)

# Destructured `require` names and call spans in two authored CommonJS fixtures, matched to the saved graphs' import fields — C04

Scope. Two authored fixture directories (`corpus/fixtures/js-r3`, `corpus/fixtures/js-r7-v2`) and the two saved static-graph records that describe them (`corpus/live/runs/20261012T164357Z/analysis.json` for js-r3, `corpus/live/runs/round-7/v2-analysis.json` for js-r7-v2), at revision `a3498e25ad87bf756288812d0ea7c474b09433c7`. The comparison is **names and call spans only**: the identifiers a `const { … } = require('…')` destructuring pattern binds, and the source range of that `require` call, against the `imported_name` and location fields the two records already carry. The analysis is **manual** — a Python standard-library whole-line regular expression bounded to the two `index.js` files. It is not a JavaScript parser, it executes no fixture JavaScript, it calls no producer, it resolves no module loading, and it reads no verifier source. No claim is made about package `main`, entrypoint resolution, any role label, any export binding, or any comparison-tool score.

## Observation

Each numbered item is produced by the `readout.py` block in §Reproduce; the pointer names the stdout record and its field. Every stdout line is one compact JSON object (JSON Lines).

**Fixture bytes**

1. Each fixture directory holds exactly three files, with byte length and SHA-256 for each. js-r3 — `index.js` 274 B `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7`, `package.json` 85 B `92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7`, `transform.js` 379 B `cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345`; js-r7-v2 — `index.js` 209 B `b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a`, `package.json` 85 B `92ef8e3d…`, `transform.js` 379 B `cd9f3f63…`. The two directories therefore share byte-identical `package.json` and `transform.js` and differ only in `index.js`. — §A `{"fixture":…,"files":[…]}`, `files[].bytes`, `files[].sha256`
2. Each fixture's `package.json` carries `"type":"commonjs"`. That string is the only package metadata this entry uses. — §A `{"fixture":…,"package_type":…}`

**Source side**

3. js-r3 `index.js` has 7 non-empty lines; line 1 is `const { rot13, checksum } = require('./transform');`, specifier literal `"./transform"`, bound names `["rot13","checksum"]`. js-r7-v2 `index.js` has 7 non-empty lines; line 1 is `const { rot13 } = require('./transform');`, specifier literal `"./transform"`, bound names `["rot13"]`. The readout exits non-zero unless exactly one line matches, so the bound is enforced, not assumed. — §A `source_file`, `source_sha256`, `non_empty_lines`, `line_number_1based`, `line_text`, `specifier_literal`, `destructured_names`
4. **`require` call span** — js-r3: `offset_0based` 28, 0-based end-exclusive `[28,50)`, 1-based inclusive `29-50`, text `require('./transform')`; js-r7-v2: `offset_0based` 18, `[18,40)`, `19-40`, same text. — §A `{"fixture":…,"span":"require_call",…}`
5. **Binding-assignment span** (`{ … } = require('…')`) — js-r3: 0-based end-exclusive `[6,50)`, 1-based inclusive `7-50`, text `{ rot13, checksum } = require('./transform')`; js-r7-v2: `[6,40)`, `7-40`, text `{ rot13 } = require('./transform')`. The destructuring pattern alone is `[6,25)` / `7-25` and `[6,15)` / `7-15`. The call span and the binding-assignment span are different spans and are reported separately. — §A `{"fixture":…,"span":"binding_assignment",…}`, `{"fixture":…,"span":"destructuring_pattern",…}`

**Saved records**

6. js-r3 record: 193573 bytes, file SHA-256 `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452`, Evidence ID `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`, operation `analyze_javascript_application`, provider id `rea-javascript-application`, provider version `1`. js-r7-v2 record: 171150 bytes, file SHA-256 `331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e`, Evidence ID `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`, same operation, provider id and provider version. These are **recorded** fields of the saved files, not re-derived here. — §A `{"fixture":…,"record":{…}}`, `bytes`, `sha256`, `evidence_id`, `operation`, `provider_id`, `provider_version`
7. The records' own `root_artifact_sha256` values (`8eec9ffb…` for js-r3, `696c2496…` for js-r7-v2) are **recorded, not re-derived**: no opened source specifies that construction, and this entry derives no digest over a directory. — §A `recorded_root_artifact_sha256`

**Saved `imports` edges**

8. js-r3 has three `imports` edges. The two named ones carry `imported_name` `"rot13"` and `"checksum"`, `specifier` `"./transform"`, `resolved_path` `"transform.js"`, `state` `"inferred"`, a `source-range` location on `index.js` with `start_column_0based` 6 and `end_column_0based_end_exclusive` 50, `span_1based_inclusive` `[1,7,1,50]`, `span_text_from_fixture` `{ rot13, checksum } = require('./transform')`, and a target of kind `javascript-module` with identity strategy `artifact-local-key`, namespace `source-module`, key `8eec9ffb…:transform.js`. The third edge carries `imported_name` `null` (no name), the same `specifier` and `resolved_path`, `state` `"inferred"`, a location with `start_column_0based` 28 and `end_column_0based_end_exclusive` 50, `span_1based_inclusive` `[1,29,1,50]`, `span_text_from_fixture` `require('./transform')`, and a target of kind `javascript-asset` with identity strategy `content-digest` and no namespace or key. — §A `{"fixture":"js-r3","imports_edge":{…}}`
9. js-r7-v2 has two `imports` edges: the named one carries `imported_name` `"rot13"`, `specifier` `"./transform"`, `resolved_path` `"transform.js"`, `state` `"inferred"`, location `start_column_0based` 6, `end_column_0based_end_exclusive` 40, `span_1based_inclusive` `[1,7,1,40]`, `span_text_from_fixture` `{ rot13 } = require('./transform')`, target `javascript-module` / `artifact-local-key` / `source-module` / key `696c2496…:transform.js`; the unnamed one carries `imported_name` `null`, location `start_column_0based` 18, `end_column_0based_end_exclusive` 40, `span_1based_inclusive` `[1,19,1,40]`, `span_text_from_fixture` `require('./transform')`, target `javascript-asset` / `content-digest`. — §A `{"fixture":"js-r7-v2","imports_edge":{…}}`
10. Counts: js-r3 `imports_edges` 3, `named_imports_edges` 2, `unnamed_imports_edges` 1; js-r7-v2 `imports_edges` 2, `named_imports_edges` 1, `unnamed_imports_edges` 1. — §A `{"fixture":…,"counts":{…}}`
11. The saved spans are the manual spans: each unnamed edge's saved location (0-based end-exclusive `[28,50)` and `[18,40)`) is exactly the manual `require` call span and its `span_text_from_fixture` is the call text; each named edge's saved location (`[6,50)` and `[6,40)`) is exactly the manual binding-assignment span and its `span_text_from_fixture` is the assignment text. The column base is not assumed — it is shown, because the bytes read back at the saved columns are the texts above. — §A `location.start_column_0based`, `location.end_column_0based_end_exclusive`, `location.span_1based_inclusive`, `location.span_text_from_fixture`

**Name-set deltas (name values only)**

12. Within one fixture, that fixture's source-side bound names against that fixture's own saved `imported_name` values: js-r3 `kept` `["checksum","rot13"]`, `removed_source_only` `[]`, `added_record_only` `[]`; js-r7-v2 `kept` `["rot13"]`, `removed_source_only` `[]`, `added_record_only` `[]`. — §A `{"fixture":…,"named_set_delta_within_fixture":{…}}`
13. Across the two records, over `imported_name` **values** only: `removed` `["checksum"]`, `added` `[]`, `kept` `["rot13"]`. — §A `{"cross_record_named_name_value_delta":{…}}`

## Inference

14. [INFERENCE, scoped to these two fixtures, these two records, this provider id and version, this operation] The `imported_name` values the records carry for their named `imports` edges agree with the names the fixture source binds: within each fixture, nothing removed and nothing added. This is agreement of two name sets within one fixture, not of two edge sets. Basis: items 3, 8, 9, 12.
15. [INFERENCE] The two records' named-import name-value sets differ by exactly one value, `checksum`, which js-r3 carries and js-r7-v2 does not. This is a statement about name values; the two records' edge sets are not compared and no per-edge difference is claimed. Basis: items 8, 9, 13.
16. [INFERENCE, language semantics only] In ECMAScript a destructuring binding reads the named property from the evaluated value of the initializer expression: §14.3.3.3 KeyedBindingInitialization specifies "Set value to ? GetV(value, propertyName)." for the `SingleNameBinding : BindingIdentifier` case. So in these two fixture lines `rot13` and `checksum` name properties of the value of the `require(...)` call, and the recorded agreement in item 14 is agreement of two literals — a source-side binding name and a saved field called `imported_name` — not an observed export binding and not an ECMAScript module import (S029's scope: no loader, graph-producer or CommonJS runtime behavior). This says nothing about how any host loads modules. Basis: §Sources and item 3.
17. [INFERENCE] Each digest printed here binds the exact bytes it was computed over: the six fixture-file digests cover those files, and the two record digests cover those saved record files. A digest match is not evidence of who produced a record, that a record is complete, that a record is authentic, or that the provider's own directory digest (`root_artifact_sha256`, item 7) was re-derived — it was not, and no equality between a provider digest and a local file digest is claimed. Basis: items 1, 6 and 7.

## Unknown

18. Whether the required module object carries a property named `rot13` or `checksum` at run time is **unknown**. No JavaScript was executed and no runtime was observed. Basis: item 3 and §Limitations.
19. The export side of either module is **unknown and out of scope**; nothing here speaks to what a module exports.
20. The provider's root/directory digest construction is **recorded, not re-derived** (item 7).
21. Whether the two records' other edges, nodes and relations are correct is **unknown**: only the fields named in items 1-13 were read.
22. Whether any other package, fixture, provider version or operation behaves the same way is **unknown**; two directories and two records were observed.

## Limitations

23. This is **manual** analysis: a Python standard-library whole-line regular expression over two authored files, accepting exactly one syntactic shape and failing closed otherwise (the script exits non-zero unless exactly one line matches). It is not a JavaScript parser.
24. The scope is names and call spans only. The saved edges' other properties and the records' other content were not compared, and no claim about them is made.
25. Both deltas (items 12 and 13) are over `imported_name` **name values**; the two records' edge sets were not compared and no edge-set delta is claimed.
26. The readout in §Reproduce touched no network, service, runtime or chain: it reads local bytes and JSON only, and it executed no fixture JavaScript or bytecode, called no producer, resolved no module loading and read no verifier source. The one network access this round was the read-only opening of the public ECMA-262 page for the S029 row — a published document fetch, with no account, service or state change.
27. No repository verifier is executed or credited, and **no deletion-sensitive guard credit is claimed** for anything in this entry: every value rests on the in-entry derivation of §Reproduce, not on a recheck, a verifier run or a comparison-tool score. No automatic gate, checker or scorer is introduced or claimed here.
28. The two fixtures are authored by this lane; the conclusions are scoped to them and to the two saved records.
29. The retained rejected candidate `corpus/knowledge/commonjs-destructured-require-edges.md` (round 61) is left byte-unchanged and is **not** cited here as support for any claim.
30. The sibling-lane overlap is recorded in this lane's own round intake (`corpus/lessons/round-62.md`, "ADJ-06 sibling arbitration: operator-owned and unresolved; new entries do not declare ownership or a ruling"). This entry declares no ownership and no ruling, cites no other lane's file as support, and any same-family ground held elsewhere is neither absorbed nor contested by the statements above.

## Reproduce

One command, run once on the frozen extract; the code and the exact stdout are reproduced below. Python 3 standard library only; no third-party package and no install.

```
git -C <repo> archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C <scratch>/tree
cd <scratch>
python3 -B readout.py tree        # exit 0; 25 stdout lines
```

`readout.py` SHA-256 `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac`; stdout SHA-256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` (25 lines). The stdout carries no path, so the same bytes give the same 25 lines from any extraction directory. Each stdout line is one JSON object; `python3 -m json.tool` reformats any line.

### Code — `readout.py` (complete)

```python
#!/usr/bin/env python3
"""Manual readout for the round-62 C04 candidate (Python standard library only).

One input: the extracted root of the frozen corpus archive. It reads bytes and
JSON only: no JavaScript is executed, no producer is called, no module loading
is resolved, no verifier source is read. Each stdout line is one compact JSON
object (JSON Lines); `python3 -m json.tool` reformats any line.
Usage: python3 readout.py <archive-root>
"""
import hashlib
import json
import os
import re
import sys

ROOT = sys.argv[1]
FIXTURES = [
    ("js-r3", "corpus/fixtures/js-r3", "corpus/live/runs/20261012T164357Z/analysis.json"),
    ("js-r7-v2", "corpus/fixtures/js-r7-v2", "corpus/live/runs/round-7/v2-analysis.json"),
]
# One source shape only, anchored to the whole line: const { a, b } = require('s');
LINE_RE = re.compile(r"^const\s*\{\s*(?P<names>[A-Za-z_$][A-Za-z0-9_$]*"
                     r"(?:\s*,\s*[A-Za-z_$][A-Za-z0-9_$]*)*)\s*\}\s*=\s*require"
                     r"\(\s*'(?P<specifier>[^']+)'\s*\)\s*;$")
CALL_RE = re.compile(r"require\(\s*'[^']*'\s*\)")
BRACE_RE = re.compile(r"\{[^{}]*\}")


def sha(data): return hashlib.sha256(data).hexdigest()


def read(rel):
    with open(os.path.join(ROOT, rel), "rb") as handle:
        return handle.read()


def span(text, start, end):
    """0-based end-exclusive span -> both bases, plus the covered text."""
    return {"span_0based_end_exclusive": [start, end], "span_1based_inclusive": [start + 1, end], "text": text[start:end]}


def emit(obj): print(json.dumps(obj, separators=(",", ":"), sort_keys=False))


def import_edges(graph, line):
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    out = []
    for edge in graph["edges"]:
        if edge.get("relation") != "imports":
            continue
        props, evidence = edge.get("properties", {}), edge.get("evidence", {})
        loc = (evidence.get("location") or {}).get("value") or {}
        start, end = loc.get("start", {}), loc.get("end", {})
        target = nodes.get(edge.get("target_node_id"), {})
        identity = target.get("identity", {})
        out.append({"edge_id": edge.get("edge_id"), "imported_name": props.get("imported_name"),
                    "specifier": props.get("specifier"), "resolved_path": props.get("resolved_path"),
                    "state": evidence.get("state"),
                    "location": {"kind": loc.get("kind"), "source": loc.get("source"),
                                 "start_line": start.get("line"), "start_column_0based": start.get("column"),
                                 "end_line": end.get("line"), "end_column_0based_end_exclusive": end.get("column"),
                                 "span_1based_inclusive": [start.get("line"), start.get("column") + 1,
                                                           end.get("line"), end.get("column")],
                                 "span_text_from_fixture": line[start.get("column"):end.get("column")]},
                    "target": {"kind": target.get("kind"), "identity_strategy": identity.get("strategy"),
                               "identity_namespace": identity.get("namespace"), "identity_key": identity.get("key")}})
    return out


def fixture_records(fid, rel_dir, rel_record):
    files = []
    for name in sorted(os.listdir(os.path.join(ROOT, rel_dir))):
        data = read(rel_dir + "/" + name)
        files.append({"path": name, "bytes": len(data), "sha256": sha(data)})
    package = json.loads(read(rel_dir + "/package.json").decode("utf-8"))
    text = read(rel_dir + "/index.js").decode("utf-8")
    lines = [line for line in text.split("\n") if line.strip()]
    hits = [(n, line) for n, line in enumerate(lines, 1) if LINE_RE.match(line)]
    if len(hits) != 1:
        raise SystemExit("expected exactly one destructured require line, found %d" % len(hits))
    lineno, line = hits[0]
    match, call, brace = LINE_RE.match(line), CALL_RE.search(line), BRACE_RE.search(line)
    names = [n.strip() for n in match.group("names").split(",")]
    record_bytes = read(rel_record)
    record = json.loads(record_bytes.decode("utf-8"))
    normalized = record["normalized_result"]
    edges = import_edges(normalized["graph"], line)
    named = sorted(e["imported_name"] for e in edges if e["imported_name"] is not None)
    source_names = sorted(names)
    out = [{"fixture": fid, "dir": rel_dir, "files": files},
           {"fixture": fid, "package_type": package.get("type")},
           {"fixture": fid, "source_file": rel_dir + "/index.js", "source_sha256": sha(text.encode("utf-8")),
            "non_empty_lines": len(lines), "line_number_1based": lineno, "line_text": line,
            "specifier_literal": match.group("specifier"), "destructured_names": names},
           dict({"fixture": fid, "span": "require_call", "offset_0based": call.start()},
                **span(line, call.start(), call.end())),
           dict({"fixture": fid, "span": "destructuring_pattern"},
                **span(line, brace.start(), brace.end())),
           dict({"fixture": fid, "span": "binding_assignment"},
                **span(line, brace.start(), call.end())),
           {"fixture": fid, "record": {"path": rel_record, "bytes": len(record_bytes),
               "sha256": sha(record_bytes), "evidence_id": record.get("evidence_id"),
               "operation": record.get("operation"), "provider_id": record.get("provider", {}).get("id"),
               "provider_version": record.get("provider", {}).get("version"),
               "recorded_root_artifact_sha256": normalized.get("root_artifact_sha256")}},
           {"fixture": fid, "counts": {"imports_edges": len(edges), "named_imports_edges": len(named),
               "unnamed_imports_edges": len(edges) - len(named), "named_import_name_values": named}},
           {"fixture": fid, "named_set_delta_within_fixture": {
               "kept": sorted(set(source_names) & set(named)),
               "removed_source_only": sorted(set(source_names) - set(named)),
               "added_record_only": sorted(set(named) - set(source_names))}}]
    out.extend({"fixture": fid, "imports_edge": edge} for edge in edges)
    return out


records = [{"tool": "readout.py (manual, Python standard library)", "scope": "names and call spans only; "
            "no execution, no producer call, no module-loading resolution, no verifier source read"}]
blocks = {}
for spec in FIXTURES:
    blocks[spec[0]] = fixture_records(*spec)
    records.extend(blocks[spec[0]])
left = set(blocks["js-r3"][7]["counts"]["named_import_name_values"])
right = set(blocks["js-r7-v2"][7]["counts"]["named_import_name_values"])
records.append({"cross_record_named_name_value_delta": {
    "left": "js-r3", "right": "js-r7-v2", "removed": sorted(left - right),
    "added": sorted(right - left), "kept": sorted(left & right),
    "note": "over imported_name values only; the two records' edge sets are not compared"}})
for record in records:
    emit(record)
```

### Exact stdout — `readout.py` (complete)

```
{"tool":"readout.py (manual, Python standard library)","scope":"names and call spans only; no execution, no producer call, no module-loading resolution, no verifier source read"}
{"fixture":"js-r3","dir":"corpus/fixtures/js-r3","files":[{"path":"index.js","bytes":274,"sha256":"f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7"},{"path":"package.json","bytes":85,"sha256":"92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7"},{"path":"transform.js","bytes":379,"sha256":"cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345"}]}
{"fixture":"js-r3","package_type":"commonjs"}
{"fixture":"js-r3","source_file":"corpus/fixtures/js-r3/index.js","source_sha256":"f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7","non_empty_lines":7,"line_number_1based":1,"line_text":"const { rot13, checksum } = require('./transform');","specifier_literal":"./transform","destructured_names":["rot13","checksum"]}
{"fixture":"js-r3","span":"require_call","offset_0based":28,"span_0based_end_exclusive":[28,50],"span_1based_inclusive":[29,50],"text":"require('./transform')"}
{"fixture":"js-r3","span":"destructuring_pattern","span_0based_end_exclusive":[6,25],"span_1based_inclusive":[7,25],"text":"{ rot13, checksum }"}
{"fixture":"js-r3","span":"binding_assignment","span_0based_end_exclusive":[6,50],"span_1based_inclusive":[7,50],"text":"{ rot13, checksum } = require('./transform')"}
{"fixture":"js-r3","record":{"path":"corpus/live/runs/20261012T164357Z/analysis.json","bytes":193573,"sha256":"7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452","evidence_id":"ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e","operation":"analyze_javascript_application","provider_id":"rea-javascript-application","provider_version":"1","recorded_root_artifact_sha256":"8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32"}}
{"fixture":"js-r3","counts":{"imports_edges":3,"named_imports_edges":2,"unnamed_imports_edges":1,"named_import_name_values":["checksum","rot13"]}}
{"fixture":"js-r3","named_set_delta_within_fixture":{"kept":["checksum","rot13"],"removed_source_only":[],"added_record_only":[]}}
{"fixture":"js-r3","imports_edge":{"edge_id":"jag_edge_66e056c717487d0a912cf5f316791e3869852fdd8a3aad2bb6f66961e6254116","imported_name":"rot13","specifier":"./transform","resolved_path":"transform.js","state":"inferred","location":{"kind":"source-range","source":"index.js","start_line":1,"start_column_0based":6,"end_line":1,"end_column_0based_end_exclusive":50,"span_1based_inclusive":[1,7,1,50],"span_text_from_fixture":"{ rot13, checksum } = require('./transform')"},"target":{"kind":"javascript-module","identity_strategy":"artifact-local-key","identity_namespace":"source-module","identity_key":"8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32:transform.js"}}}
{"fixture":"js-r3","imports_edge":{"edge_id":"jag_edge_b5c88eb64853f53cff70eaf288a3a9aca4c07f46d577d882da831cd3ca249757","imported_name":null,"specifier":"./transform","resolved_path":"transform.js","state":"inferred","location":{"kind":"source-range","source":"index.js","start_line":1,"start_column_0based":28,"end_line":1,"end_column_0based_end_exclusive":50,"span_1based_inclusive":[1,29,1,50],"span_text_from_fixture":"require('./transform')"},"target":{"kind":"javascript-asset","identity_strategy":"content-digest","identity_namespace":null,"identity_key":null}}}
{"fixture":"js-r3","imports_edge":{"edge_id":"jag_edge_b6378db39482d11dbe1812ba90afddedf703a520bdab711936b6e4c05be4aad3","imported_name":"checksum","specifier":"./transform","resolved_path":"transform.js","state":"inferred","location":{"kind":"source-range","source":"index.js","start_line":1,"start_column_0based":6,"end_line":1,"end_column_0based_end_exclusive":50,"span_1based_inclusive":[1,7,1,50],"span_text_from_fixture":"{ rot13, checksum } = require('./transform')"},"target":{"kind":"javascript-module","identity_strategy":"artifact-local-key","identity_namespace":"source-module","identity_key":"8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32:transform.js"}}}
{"fixture":"js-r7-v2","dir":"corpus/fixtures/js-r7-v2","files":[{"path":"index.js","bytes":209,"sha256":"b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a"},{"path":"package.json","bytes":85,"sha256":"92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7"},{"path":"transform.js","bytes":379,"sha256":"cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345"}]}
{"fixture":"js-r7-v2","package_type":"commonjs"}
{"fixture":"js-r7-v2","source_file":"corpus/fixtures/js-r7-v2/index.js","source_sha256":"b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a","non_empty_lines":7,"line_number_1based":1,"line_text":"const { rot13 } = require('./transform');","specifier_literal":"./transform","destructured_names":["rot13"]}
{"fixture":"js-r7-v2","span":"require_call","offset_0based":18,"span_0based_end_exclusive":[18,40],"span_1based_inclusive":[19,40],"text":"require('./transform')"}
{"fixture":"js-r7-v2","span":"destructuring_pattern","span_0based_end_exclusive":[6,15],"span_1based_inclusive":[7,15],"text":"{ rot13 }"}
{"fixture":"js-r7-v2","span":"binding_assignment","span_0based_end_exclusive":[6,40],"span_1based_inclusive":[7,40],"text":"{ rot13 } = require('./transform')"}
{"fixture":"js-r7-v2","record":{"path":"corpus/live/runs/round-7/v2-analysis.json","bytes":171150,"sha256":"331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e","evidence_id":"ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c","operation":"analyze_javascript_application","provider_id":"rea-javascript-application","provider_version":"1","recorded_root_artifact_sha256":"696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655"}}
{"fixture":"js-r7-v2","counts":{"imports_edges":2,"named_imports_edges":1,"unnamed_imports_edges":1,"named_import_name_values":["rot13"]}}
{"fixture":"js-r7-v2","named_set_delta_within_fixture":{"kept":["rot13"],"removed_source_only":[],"added_record_only":[]}}
{"fixture":"js-r7-v2","imports_edge":{"edge_id":"jag_edge_2ff2c8d463e5ca77371bdb2e0108d81834969590471cee0b21c649a8dccdbc13","imported_name":null,"specifier":"./transform","resolved_path":"transform.js","state":"inferred","location":{"kind":"source-range","source":"index.js","start_line":1,"start_column_0based":18,"end_line":1,"end_column_0based_end_exclusive":40,"span_1based_inclusive":[1,19,1,40],"span_text_from_fixture":"require('./transform')"},"target":{"kind":"javascript-asset","identity_strategy":"content-digest","identity_namespace":null,"identity_key":null}}}
{"fixture":"js-r7-v2","imports_edge":{"edge_id":"jag_edge_7a0c9240fb755c4a2d9a1d96638b81c2cc6b1af38bf9a6067a5dbfe81d202edf","imported_name":"rot13","specifier":"./transform","resolved_path":"transform.js","state":"inferred","location":{"kind":"source-range","source":"index.js","start_line":1,"start_column_0based":6,"end_line":1,"end_column_0based_end_exclusive":40,"span_1based_inclusive":[1,7,1,40],"span_text_from_fixture":"{ rot13 } = require('./transform')"},"target":{"kind":"javascript-module","identity_strategy":"artifact-local-key","identity_namespace":"source-module","identity_key":"696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655:transform.js"}}}
{"cross_record_named_name_value_delta":{"left":"js-r3","right":"js-r7-v2","removed":["checksum"],"added":[],"kept":["rot13"],"note":"over imported_name values only; the two records' edge sets are not compared"}}
```

## Sources

- **S029** (existing row, `mined`, opened 2026-10-21) — ECMA-262 object binding and import-name roles, https://tc39.es/ecma262/ , draft of October 16 2026; single-page SHA-256 `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f` (the row's anchor also lists §14.3.1.3 BindingEvaluation, §14.3.3.3 KeyedBindingInitialization, §16.2.1.7 Table 54 and §16.2.2 Imports). This entry uses **one** quoted text, the property read in §14.3.3.3: "Set value to ? GetV(value, propertyName)." — 8 words. (The page's HTML text renders the same step as "Set value to ? GetV ( value , propertyName )." when whitespace is normalised.) The row's scope is language semantics only — no loader, graph-producer or CommonJS runtime behavior — and it is not cited here for module resolution, loader behaviour, package metadata or any provider behaviour.
- **S030** (existing row, `mined`, opened 2026-10-21) — own-work bytes at revision `a3498e25ad87bf756288812d0ea7c474b09433c7`: `corpus/fixtures/js-r3/`, `corpus/fixtures/js-r7-v2/`, `corpus/live/runs/20261012T164357Z/analysis.json`, `corpus/live/runs/round-7/v2-analysis.json`. The fixture bytes, their digests and the record bytes, digests, Evidence IDs, operation and provider fields are items 1-13; the provider, operation, Evidence ID and root digest values are **recorded** fields of those saved files, and the source-side names and spans are derived from the fixture bytes by the command in §Reproduce.

## Sentence-to-output inventory (Q11)

Every factual sentence above maps to the command that prints it (`python3 -B readout.py <archive-root>`, exit 0, stdout SHA-256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416`) and to the stdout record and field it comes from. The stdout is JSON Lines, so the pointer is the record key and the field path.

| # | Sentence (short form) | stdout record | field |
|---|---|---|---|
| 1 | three files per fixture, sizes and digests; shared vs differing files | `{"fixture":…,"files":[…]}` | `files[].bytes`, `files[].sha256` |
| 2 | package type `commonjs` | `{"fixture":…,"package_type":…}` | `package_type` |
| 3 | the require line, its text, specifier, names | `{"fixture":…,"source_file":…}` | `line_number_1based`, `line_text`, `specifier_literal`, `destructured_names`, `source_sha256` |
| 4 | require-call span, both bases | `{"fixture":…,"span":"require_call",…}` | `offset_0based`, `span_0based_end_exclusive`, `span_1based_inclusive`, `text` |
| 5 | binding-assignment and pattern spans, both bases | `{"fixture":…,"span":"binding_assignment",…}` / `"destructuring_pattern"` | `span_0based_end_exclusive`, `span_1based_inclusive`, `text` |
| 6 | record bytes, digest, Evidence ID, operation, provider | `{"fixture":…,"record":{…}}` | `bytes`, `sha256`, `evidence_id`, `operation`, `provider_id`, `provider_version` |
| 7 | provider root digest (recorded) | same | `recorded_root_artifact_sha256` |
| 8 | js-r3's three `imports` edges, all saved fields | `{"fixture":"js-r3","imports_edge":{…}}` | `imported_name`, `specifier`, `resolved_path`, `state`, `location.*`, `target.*` |
| 9 | js-r7-v2's two `imports` edges, all saved fields | `{"fixture":"js-r7-v2","imports_edge":{…}}` | same |
| 10 | edge counts | `{"fixture":…,"counts":{…}}` | `imports_edges`, `named_imports_edges`, `unnamed_imports_edges` |
| 11 | saved spans equal the manual spans | `imports_edge` records | `location.start_column_0based`, `location.end_column_0based_end_exclusive`, `location.span_1based_inclusive`, `location.span_text_from_fixture` |
| 12 | within-fixture named-set delta | `{"fixture":…,"named_set_delta_within_fixture":{…}}` | `kept`, `removed_source_only`, `added_record_only` |
| 13 | cross-record name-value delta | `{"cross_record_named_name_value_delta":{…}}` | `removed`, `added`, `kept` |
| 14-17 | the four inferences | the records above | as cited in each item |
| 18-22 | the unknowns | no output claimed | — |
| 23-30 | the limitations and the Q13 stance | no output claimed | — |

## Q13 — no deletion-sensitive guard credit

No verifier, recheck command, comparison tool or automatic checker is credited as a guard of any value in this entry, and none is introduced: every value above rests on the in-entry derivation in §Reproduce (a command and that command's printed output), not on a recheck run, a verifier run or a comparison-tool score. No repository verifier was executed or read, so no clause of any such script is claimed to be detected or undetected here, and none is named as a guard. The entry therefore asserts no coverage of any value by any check, and creates no gate.

## QUALITY check — decisions, not admission

This entry is a CANDIDATE. The rows below are this seat's reading of unchanged `corpus/QUALITY.md` Q01-Q13; they are not an admission, and `corpus/README.md` C04 stays `uncovered` until a fresh falsify wave and an explicit all-criteria admission by the integrator.

| Q | decision | basis |
|---|---|---|
| Q01 | pass, cited against the existing rows, pending independent audit | S029 and S030 are existing `mined` rows (opened 2026-10-21); this entry cites the one S029 text it uses, with its clause location, and S030's own-work bytes at the frozen revision. S029's scope is language semantics only, and no claim exceeds it. |
| Q02 | pass | `source:` (two rows with URL, clause anchors and verbatim quotes), `verified-at: 2026-10-21`, `recheck:` (one runnable command with its stdout digest) and `coverage-map: C04` are present; the anchors are clause ids, not a bare homepage. |
| Q03 | pass | the source-side expectations (names, spans, digests) are derived from the fixture bytes, never copied from the records; the records supply the compared side only. |
| Q04 | pass | the analysis is labelled manual; no tool is credited with a result it did not output; no comparison-tool score is claimed (§Limitations 23, 26-27). |
| Q05 | n/a (no readiness or capability claim) | the entry claims no readiness, no producer capability and no current-host state; the two records are read as saved files, in the past tense, at their saved revision. |
| Q06 | pass | every fixture premise is byte-verified in this entry: per-file SHA-256 and length for all six fixture files (§A item 1), and the source file's own digest is printed with the source readout. |
| Q07 | n/a (no predicted parser behaviour) | the entry predicts nothing about any parser or provider; the regular expression is this entry's own bounded instrument, and its one-match condition is enforced in the code. |
| Q08 | superseded by Q11 | — |
| Q09 | pass | each printed digest binds the bytes it was computed over (§A items 1, 6); no origin, completeness or authenticity claim is made, and the provider's own directory digest is labelled recorded and not re-derived (items 7, 17). |
| Q10 | pass | scope is the two fixtures, the two records, one provider id and version, one operation (item 14, §Limitations 28); the sibling-lane overlap is reported as operator-owned per this lane's own round intake, with no ownership declared and no other lane's file cited as support (item 30). |
| Q11 | pass | the §Sentence-to-output inventory maps every factual sentence to a command and to a printed field; the provider's root digest is labelled recorded, not re-derived (item 7). |
| Q12 | n/a (no rejected source row cited) | the entry cites no rejected row. |
| Q13 | n/a by construction — no guard credit | no verifier, recheck command, comparison tool or automatic checker is credited or introduced, and no value is presented as covered by any check (§Q13). |
