#!/usr/bin/env python3
"""Verify the fixture-scoped saved REA semantic capture trace; no JS execution."""
import copy
import hashlib
import json
import sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parent
PARENT = CORPUS / "live/runs/20261012T164357Z/analysis.json"
RUN = CORPUS / "live/runs/round-14"
SOURCE = CORPUS / "fixtures/js-r3/index.js"
PARENT_ID = "ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e"
TRACE_ID = "ev_53329396d6fe4843b89806ef1ed98b6db8358ec91c41c733d617ea846b995a8a"
SEED = "jsrg_node_c82112b8b59795d1f05fc48493bb107894622416db870b070178f03477857337"


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def verify(parent, request, trace):
    graph = parent["normalized_result"]["semantic_graph"]
    result = trace["normalized_result"]
    query = trace["parameters"]["query"]
    require(parent["evidence_id"] == PARENT_ID and parent["operation"] == "analyze_javascript_application"
            and trace["evidence_id"] == TRACE_ID and trace["operation"] == "trace_javascript_semantics",
            "wrong saved Evidence identity")
    require(request["application"] == parent and request["query"] == {k: query[k] for k in request["query"]},
            "request does not bind saved parent/query")
    require(result["source_evidence_id"] == trace["parameters"]["application_evidence_id"] == PARENT_ID
            and trace["evidence_links"] == result["evidence_links"] == [PARENT_ID]
            and result["source_graph_id"] == graph["graph_id"], "parent or graph link mismatch")
    require(query["seed"] == result["seed"] == {"kind": "semantic-node", "node_id": SEED}
            and query["direction"] == result["direction"] == "backward-provenance"
            and query["allowed_relations"] == ["captures"]
            and query["include_ambiguous_dynamic_edges"] is False,
            "wrong semantic trace query")
    require(result["status"] == "found" and result["seed_node_ids"] == [SEED]
            and result["coverage"]["status"] == "partial"
            and result["summary"] == {"total_seed_matches": 1, "traversed_nodes": 4,
                                       "traversed_relations": 3, "traversed_functions": 1,
                                       "traversed_modules": 1, "relevant_unknowns": 0}
            and graph["coverage"]["status"] == "unknown", "trace scope or limits changed")
    parent_nodes = {node["node_id"]: node for node in graph["nodes"]}
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    source_lines = SOURCE.read_text().splitlines()
    nodes = {node["node_id"]: node for node in result["nodes"]}
    require(len(nodes) == len(result["nodes"]) == 4 and set(nodes) == {SEED} |
            {relation["source_node_id"] for relation in result["relations"]}, "wrong trace node set")
    for node_id, node in nodes.items():
        require(node == parent_nodes[node_id] and node["identity"]["module_path"] == "index.js"
                and node["identity"]["artifact_sha256"] == digest, "node or source digest mismatch")
    require(nodes[SEED]["kind"] == "function" and nodes[SEED]["label"] == "render"
            and nodes[SEED]["identity"]["source_range"]["start"]["line"] == 3,
            "wrong seeded function")
    parent_relations = {relation["relation_id"]: relation for relation in graph["relations"]}
    context_ids = {context["context_id"] for context in result["evidence_contexts"]}
    parent_contexts = {context["context_id"]: context for context in graph["evidence_contexts"]}
    require(len(context_ids) == len(result["evidence_contexts"]) and
            all(context == parent_contexts[context["context_id"]] for context in result["evidence_contexts"]),
            "evidence context mismatch")
    require(len(result["relations"]) == 3 and len({r["relation_id"] for r in result["relations"]}) == 3,
            "unexpected relation count")
    observed = {}
    for relation in result["relations"]:
        require(relation == parent_relations[relation["relation_id"]] and
                relation["relation"] == "captures" and relation["resolution"] == "resolved" and
                relation["target_node_id"] == SEED and relation["evidence"]["context_id"] in context_ids,
                "relation differs from source parent")
        name = nodes[relation["source_node_id"]]["label"]
        location = relation["evidence"]["location"]["value"]
        start, end = location["start"], location["end"]
        require(location["source"] == "index.js" and start["line"] == end["line"]
                and source_lines[start["line"] - 1][start["column"]:end["column"]] == name,
                "relation source token mismatch")
        observed[name] = start["line"]
    require(observed == {"checksum": 5, "defaultInput": 3, "rot13": 4},
            "wrong source-backed captures")
    return "3/3 returned captures match source tokens and saved parent; partial static trace only"


def main():
    parent = json.loads(PARENT.read_text())
    request = json.loads((RUN / "trace-request.json").read_text())
    trace = json.loads((RUN / "trace.json").read_text())
    print("POSITIVE", TRACE_ID, verify(parent, request, trace))
    if "--self-test" in sys.argv:
        altered = copy.deepcopy(trace)
        altered["normalized_result"]["relations"][0]["evidence"]["location"]["value"]["start"]["column"] = 0
        try:
            verify(parent, request, altered)
        except ValueError as error:
            print("NEGATIVE REJECTED", error)
        else:
            raise AssertionError("altered relation location accepted")


if __name__ == "__main__":
    main()
