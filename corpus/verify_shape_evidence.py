#!/usr/bin/env python3
"""Check saved round-12 REA shape evidence against the authored fixture; no JS execution."""
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parent
RUN = CORPUS / "live" / "runs" / "round-12"
FIXTURE = CORPUS / "fixtures" / "shapes-r12"
PARENTS = {side: RUN / f"{side}-direct-analysis.json" for side in ("v1", "v2")}
COMPARISON = RUN / "comparison-direct.json"
EXPECTED_IDS = {
    "v1": "ev_2a492f5d829a57115e954269e08d4c7d8465f3129dd2f82ded2d01b2fb4e3064",
    "v2": "ev_913f14fa3ee334269cef30ff0af6835d6622a3053f08a5a4583260d7f35416d7",
    "comparison": "ev_bb7e1c308a60b0cc45919a4a441347a0b6119df2c49f0de40c737615f94cb872",
}


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def source_fields(side):
    text = (FIXTURE / side / "index.js").read_text()
    match = re.fullmatch(
        r'function describe\(\) \{\s*return \{([^{}]+)\};\s*\}\s*module\.exports = describe;\s*', text
    )
    require(match is not None, f"{side}: source shape changed")
    pairs = re.findall(r'([A-Za-z]+):\s*(?:"([^"]+)"|(\d+))', match.group(1))
    require(len(pairs) == len(match.group(1).split(",")), f"{side}: unparsed property")
    values = {key: value if value else int(number) for key, value, number in pairs}
    require(len(values) == len(pairs) and values.get("kind") == "fixture", f"{side}: source fields changed")
    return values


def parent_fields(side, record):
    require(record["operation"] == "analyze_javascript_application", f"{side}: parent operation")
    result = record["normalized_result"]
    require(result["graph"]["coverage"]["status"] == "complete" and
            result["graph"]["coverage"]["omitted_count"] == 0, f"{side}: graph incomplete")
    digest = hashlib.sha256((FIXTURE / side / "index.js").read_bytes()).hexdigest()
    matches = [(node["node_id"], o) for node in result["graph"]["nodes"] for o in node["observations"]
               if o["properties"].get("semantic_role") == "export-return-shapes" and
               o["properties"].get("module_path") == "index.js" and
               o["properties"].get("exported_name") == "default"]
    require(len(matches) == 1 and matches[0][1]["evidence"]["artifact"]["sha256"] == digest,
            f"{side}: parent artifact identity")
    shapes = matches[0][1]["properties"]["static_return_shapes"]
    require(len(shapes) == 1 and shapes[0]["value_status"] == "object" and
            shapes[0]["property_coverage"] == [{"path": "", "status": "complete", "omitted": 0}],
            f"{side}: return shape incomplete")
    fields = shapes[0]["fields"]
    require(all(f["presence"] == "present" and f["state"] == "literal" for f in fields),
            f"{side}: nonliteral field")
    actual = {f["path"].removeprefix("/"): f["value"] for f in fields}
    require(len(actual) == len(fields) and actual == source_fields(side), f"{side}: source mismatch")
    return actual, matches[0][0]


def verify(parents, comparison):
    require(comparison["operation"] == "compare_javascript_export_shapes" and
            comparison["evidence_id"] == EXPECTED_IDS["comparison"], "comparison identity")
    result = comparison["normalized_result"]
    for side, label in (("v1", "left"), ("v2", "right")):
        parent = parents[side]
        selected = result[label]
        require(comparison["parameters"][f"{label}_evidence_id"] == parent["evidence_id"] ==
                selected["evidence_id"] == EXPECTED_IDS[side] and selected["graph_id"] ==
                parent["normalized_result"]["graph"]["graph_id"], f"{side}: parent link")
        require(selected["status"] == "selected" and selected["requested_module_path"] == "index.js" and
                selected["requested_export_name"] == "default" and len(selected["candidates"]) == 1 and
                selected["selected_node_id"] == selected["candidates"][0]["node_id"] and
                selected["omitted_candidates"] == 0, f"{side}: ambiguous selection")
    (left, left_node), (right, right_node) = (parent_fields(s, parents[s]) for s in ("v1", "v2"))
    require(result["left"]["selected_node_id"] == left_node and
            result["right"]["selected_node_id"] == right_node, "selected node is not checked return shape")
    require(set(left) - set(right) == {"removed"} and set(right) - set(left) == {"added"} and
            set(left) & set(right) == {"kind", "retained"}, "unexpected source delta")
    inventories = {item["side"]: item for item in result["property_inventories"]}
    require(len(result["property_inventories"]) == 2 and set(inventories) == {"left", "right"},
            "inventory sides")
    for label, fields in (("left", left), ("right", right)):
        item = inventories[label]
        require(item["properties"] == sorted("/" + key for key in fields) and item["paired"] is True and
                item["discriminant"] == {"path": "/kind", "value": "fixture"} and
                item["property_coverage"] == [{"path": "", "status": "complete"}],
                f"{label}: inventory mismatch")
    expected = {"/removed": ("removed", "present", "absent"),
                "/added": ("added", "absent", "present")}
    changes = {item["path"]: (item["status"], item["presence"]["left"],
                                item["presence"]["right"]) for item in result["changes"]}
    require(len(result["changes"]) == len(changes) == 2 and changes == expected,
            "changed-property evidence mismatch")
    coverage = result["coverage"]
    require(coverage["status"] == "complete-within-inputs" and coverage["paired_variants"] == 1 and
            coverage["left_graph_status"] == coverage["right_graph_status"] == "complete" and
            all(value == 0 for key, value in coverage.items() if key.startswith(("omitted_", "unpaired_", "left_omitted_", "right_omitted_"))),
            "comparison coverage incomplete")
    require(result["summary"] == {"added": 1, "removed": 1, "changed": 0, "unknown": 0},
            "comparison summary mismatch")
    return "saved REA static shape evidence: 2/2 presence deltas; 2/2 stable names; no runtime claim"


def main():
    parents = {side: json.loads(path.read_text()) for side, path in PARENTS.items()}
    comparison = json.loads(COMPARISON.read_text())
    print("POSITIVE", comparison["evidence_id"], verify(parents, comparison))
    if "--self-test" in sys.argv:
        altered = copy.deepcopy(comparison)
        altered["normalized_result"]["changes"][0]["presence"]["right"] = "present"
        try:
            verify(parents, altered)
        except ValueError as error:
            print("NEGATIVE REJECTED", error)
        else:
            raise AssertionError("altered presence was accepted")


if __name__ == "__main__":
    main()
