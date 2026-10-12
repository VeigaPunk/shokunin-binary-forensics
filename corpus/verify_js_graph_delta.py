#!/usr/bin/env python3
"""Compare two saved REA static application graphs against authored fixture source."""
import copy
import json
import re
import sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parent
RUNS = CORPUS / "live" / "runs"
ROOT = CORPUS / "fixtures"
V1 = RUNS / "20261012T164357Z" / "analysis.json"
V2 = RUNS / "round-7" / "v2-analysis.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_facts(directory):
    text = (directory / "index.js").read_text()
    match = re.search(r"^const\s*\{([^}]+)\}\s*=\s*require\(['\"]([^'\"]+)['\"]\);", text, re.M)
    require(match is not None and match.group(2) == "./transform", "source import expression changed")
    names = {part.strip() for part in match.group(1).split(",")}
    package = json.loads((directory / "package.json").read_text())
    return names, package["main"]


def graph_facts(evidence):
    require(evidence["operation"] == "analyze_javascript_application", "wrong REA operation")
    result = evidence["normalized_result"]
    require(result["graph"]["coverage"]["status"] == "complete"
            and result["graph"]["coverage"]["omitted_count"] == 0, "incomplete application graph")
    edges = result["graph"]["edges"]
    named = [edge for edge in edges if edge["relation"] == "imports" and edge["properties"].get("imported_name")]
    require(all(edge["properties"].get("specifier") == "./transform"
                and edge["properties"].get("resolved_path") == "transform.js"
                and edge["properties"].get("resolution_status") == "resolved"
                and edge["evidence"]["state"] == "inferred"
                and edge["evidence"]["location"]["value"].get("source") == "index.js"
                for edge in named), "named import has wrong static provenance")
    names = {edge["properties"]["imported_name"] for edge in named}
    require(len(names) == len(named), "duplicate named imports")
    main = [edge for edge in edges if edge["relation"] == "maps_to"
            and edge["properties"].get("resolution_context") == "package-entrypoint"]
    require(len(main) == 1 and main[0]["evidence"]["state"] == "inferred"
            and main[0]["properties"]["resolution_status"] == "resolved", "unresolved package main")
    return names, main[0]["properties"]["resolved_path"]


def verify(left, right):
    require(left["evidence_id"] == "ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e"
            and right["evidence_id"] == "ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c",
            "wrong saved parent IDs")
    actual_left, actual_right = graph_facts(left), graph_facts(right)
    truth_left, truth_right = source_facts(ROOT / "js-r3"), source_facts(ROOT / "js-r7-v2")
    require(actual_left == truth_left and actual_right == truth_right, "saved graph disagrees with source truth")
    require(truth_left[0] - truth_right[0] == {"checksum"}
            and truth_right[0] - truth_left[0] == set()
            and truth_left[0] & truth_right[0] == {"rot13"}
            and truth_left[1] == truth_right[1] == "index.js", "unexpected source delta")
    return "saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only"


def main():
    left, right = json.loads(V1.read_text()), json.loads(V2.read_text())
    print("POSITIVE", verify(left, right))
    if "--self-test" in sys.argv:
        altered = copy.deepcopy(right)
        edges = altered["normalized_result"]["graph"]["edges"]
        named = next(edge for edge in edges if edge["relation"] == "imports" and edge["properties"].get("imported_name") == "rot13")
        named["properties"]["imported_name"] = "checksum"
        try:
            verify(left, altered)
        except ValueError as error:
            print("NEGATIVE REJECTED", error)
        else:
            raise AssertionError("altered v2 graph was accepted")


if __name__ == "__main__":
    main()
