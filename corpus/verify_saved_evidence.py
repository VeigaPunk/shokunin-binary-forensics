#!/usr/bin/env python3
"""Verify the bounded r2 ZIP and r3 static-JS claims against saved REA evidence."""
import copy
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

CORPUS = Path(__file__).resolve().parent
RUNS = CORPUS / "live" / "runs"
ZIP = CORPUS / "fixtures" / "archive-r2" / "fixture.zip"
TRUTH = CORPUS / "fixtures" / "archive-r2" / "truth.json"
JS = CORPUS / "fixtures" / "js-r3"
ZIP_RECORD = RUNS / "20261012T164246Z" / "artifact-inspection.json"
JS_RECORD = RUNS / "20261012T164357Z" / "analysis.json"
ZIP_EVIDENCE = "ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b"
JS_EVIDENCE = "ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_zip(record, truth):
    require(record["operation"] == "inspect_artifact", "ZIP: wrong REA operation")
    step = record["normalized_result"]["substeps"][0]
    require(step["operation"] == "inventory_artifact" and step["status"] == "completed", "ZIP: inventory incomplete")
    require(step["evidence_id"] == ZIP_EVIDENCE, "ZIP: unexpected nested Evidence ID")
    graph = step["evidence"]["normalized_result"]
    manifest = graph["manifest"]
    data = ZIP.read_bytes()
    require(manifest["root_format"] == "zip", "ZIP: wrong root format")
    require(manifest["root_sha256"] == truth["archive_sha256"] == digest(data), "ZIP: wrong root digest")
    nodes = {node["artifact_id"]: node for node in graph["nodes"]}
    occurrences = graph["occurrences"]
    roots = [item for item in occurrences if item["parent_occurrence_id"] is None]
    require(len(roots) == 1 and roots[0]["logical_path"] == ".", "ZIP: wrong root occurrence")
    root = nodes[roots[0]["artifact_id"]]
    require(root["format"] == "zip" and root["size"] == truth["archive_size"] == len(data), "ZIP: wrong root size/format")
    require(root["sha256"] == digest(data), "ZIP: wrong root node digest")
    observed = {}
    for item in occurrences:
        if item["logical_path"] == ".":
            continue
        require(item["parent_occurrence_id"] == roots[0]["occurrence_id"], "ZIP: detached member")
        node = nodes[item["artifact_id"]]
        require(item["hash_status"] == "verified", "ZIP: unverified member hash")
        require(item["logical_path"] not in observed, "ZIP: duplicate logical member")
        observed[item["logical_path"]] = (node["sha256"], node["size"], item["compressed_size"], node["format"])
    with zipfile.ZipFile(ZIP) as archive:
        infos = archive.infolist()
        actual = {item.filename: (digest(archive.read(item)), len(archive.read(item)), item.compress_size) for item in infos}
    declared = {item["path"]: (item["sha256"], item["size"], item["compressed_size"]) for item in truth["members"]}
    require(len(declared) == len(truth["members"]) == len(infos), "ZIP: duplicate/missing truth member")
    require(actual == declared, "ZIP: fixture differs from truth manifest")
    require(set(observed) == set(actual), "ZIP: REA member paths differ from fixture")
    for name, values in actual.items():
        expected_format = "elf" if name == "bin/checksum" else "file"
        require(observed[name] == (*values, expected_format), f"ZIP: wrong REA member {name}")
    edges = graph["edges"]
    child_ids = {item["occurrence_id"] for item in occurrences if item["logical_path"] != "."}
    require(len(edges) == len(actual) and {edge["occurrence_id"] for edge in edges} == child_ids,
            "ZIP: wrong edge count/targets")
    require(all(edge["relation"] == "contains" and edge["parent_artifact_id"] == roots[0]["artifact_id"] for edge in edges),
            "ZIP: wrong containment relationship")
    require(manifest["node_count"] == len(nodes) == 3 and manifest["occurrence_count"] == len(occurrences) == 3
            and manifest["edge_count"] == len(edges) == 2, "ZIP: wrong graph counts")
    require(truth["source_binary_sha256"] == digest((CORPUS / "fixtures" / "checksum-r1" / "checksum").read_bytes()),
            "ZIP: source ELF digest mismatch")
    return "ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match"


def verify_js(record):
    require(record["operation"] == "analyze_javascript_application", "JS: wrong REA operation")
    require(record["evidence_id"] == JS_EVIDENCE, "JS: unexpected Evidence ID")
    graph = record["normalized_result"]["graph"]
    edges = graph["edges"]
    index = (JS / "index.js").read_text()
    transform = (JS / "transform.js").read_text()
    package = json.loads((JS / "package.json").read_text())
    source = re.search(r"^const\s*\{([^}]+)\}\s*=\s*require\(['\"]([^'\"]+)['\"]\);", index, re.M)
    require(source is not None, "JS: expected source require missing")
    names = {name.strip() for name in source.group(1).split(",")}
    require(names == {"rot13", "checksum"} and source.group(2) == "./transform", "JS: source imports changed")
    exported = re.search(r"^module\.exports\s*=\s*\{([^}]+)\};", transform, re.M)
    require(exported is not None and {name.strip() for name in exported.group(1).split(",")} == names,
            "JS: source exports changed")
    require(package["main"] == "index.js" and package["type"] == "commonjs", "JS: package main changed")
    expected_sha = {name: digest((JS / name).read_bytes()) for name in ("index.js", "transform.js", "package.json")}
    require({node["identity"]["sha256"] for node in graph["nodes"] if node["kind"] == "javascript-asset"}
            == {expected_sha["index.js"], expected_sha["transform.js"]}, "JS: REA asset digests differ from source")
    bindings = [edge for edge in edges if edge["relation"] == "imports" and edge["properties"].get("imported_name") in names]
    require(len(bindings) == 2 and {edge["properties"]["imported_name"] for edge in bindings} == names,
            "JS: missing/duplicate named bindings")
    for edge in bindings:
        props, evidence = edge["properties"], edge["evidence"]
        require(props["specifier"] == "./transform" and props["resolved_path"] == "transform.js"
                and props["resolution_status"] == "resolved" and props["local_name"] == props["imported_name"],
                "JS: wrong import resolution")
        require(evidence["state"] == "inferred" and evidence["location"]["value"]["source"] == "index.js"
                and evidence["location"]["value"]["start"]["line"] == 1,
                "JS: wrong import evidence kind/source")
    mains = [edge for edge in edges if edge["relation"] == "maps_to"
             and edge["properties"].get("resolution_context") == "package-entrypoint"]
    require(len(mains) == 1, "JS: wrong package-entrypoint count")
    main = mains[0]
    require(main["properties"]["declared_path"] == package["main"]
            and main["properties"]["resolved_path"] == "index.js"
            and main["properties"]["resolution_status"] == "resolved", "JS: wrong package-main mapping")
    require(main["evidence"]["state"] == "inferred" and main["evidence"]["location"]["value"]["path"] == "package.json",
            "JS: wrong package-main evidence kind/source")
    require(record["normalized_result"]["semantic_graph"]["coverage"]["status"] == "unknown",
            "JS: unknown semantic coverage unexpectedly changed; reassess conclusion")
    return "JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests"


def main():
    archive = json.loads(ZIP_RECORD.read_text())
    truth = json.loads(TRUTH.read_text())
    application = json.loads(JS_RECORD.read_text())
    print("POSITIVE", ZIP_EVIDENCE, verify_zip(archive, truth))
    print("POSITIVE", JS_EVIDENCE, verify_js(application))
    if "--self-test" in sys.argv:
        changed_zip = copy.deepcopy(archive)
        changed_zip["normalized_result"]["substeps"][0]["evidence"]["normalized_result"]["nodes"][0]["size"] += 1
        changed_js = copy.deepcopy(application)
        main = next(edge for edge in changed_js["normalized_result"]["graph"]["edges"]
                    if edge["relation"] == "maps_to" and edge["properties"].get("resolution_context") == "package-entrypoint")
        main["properties"]["resolved_path"] = "wrong.js"
        for label, fn, args in (("ZIP", verify_zip, (changed_zip, truth)), ("JS", verify_js, (changed_js,))):
            try:
                fn(*args)
            except ValueError as error:
                print("NEGATIVE", label, "REJECTED:", error)
            else:
                raise AssertionError(f"{label}: altered proof accepted")


if __name__ == "__main__":
    main()
