#!/usr/bin/env python
"""oracle_check.py - round-83 decode_interface_builder record identity oracle.

Usage:
  python -I -B oracle_check.py truth.json inspection.json <R83Sample.app dir>

Every BYTE-DERIVED check compares the record against facts derived from the
built fixture bytes (re-hashed here) and truth.json (itself written by
build_app.py's derive() from the built bytes). The HYPOTHESIS checks are the
pre-registered Q07 predictions about the producer's declared Interface
Builder vocabulary, frozen in truth.json BEFORE the committed run (from the
preprobe receipts + the installed parser source) and checked/recorded
whichever way they fall. Host-dependent fields (evidence_id,
caller_input_path, absolute canonical/roots paths) are never checked.
"""
import base64
import hashlib
import json
import sys
from pathlib import Path


def main() -> int:
    truth_p, rec_p, bundle_p = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    truth = json.loads(Path(truth_p).read_text(encoding="utf-8"))
    rec = json.loads(Path(rec_p).read_text(encoding="utf-8"))
    bundle = truth["bundle"]["path"]

    def sha(rel):
        return hashlib.sha256((bundle_p / rel).read_bytes()).hexdigest()

    pl_sha = sha("Info.plist")
    mm_sha = sha("Base.lproj/MainMenu.nib")
    sv_sha = sha("Base.lproj/SecondView.nib")
    n = rec["normalized_result"]
    g = n["graph"]
    byte_checks = []
    hyp_checks = []

    def B(name, ok):
        byte_checks.append((name, bool(ok)))

    def H(name, ok):
        hyp_checks.append((name, bool(ok)))

    # truth vs built bytes
    B("truth_plist_sha_matches_built",
      truth["bundle"]["info_plist"]["sha256"] == pl_sha)
    B("truth_menubar_sha_matches_built", truth["documents"][0]["sha256"] == mm_sha)
    B("truth_secondview_sha_matches_built", truth["documents"][1]["sha256"] == sv_sha)
    # envelope
    B("operation", rec.get("operation") == "decode_interface_builder")
    B("provider_id", rec.get("provider", {}).get("id") == "rea-artifact-graph")
    B("provider_version", rec.get("provider", {}).get("version") == "1")
    # resource root (derived: Info.plist authored at the bundle root)
    rr = n.get("resource_root", {})
    B("resource_root_layout", rr.get("layout") == truth["bundle"]["layout"])
    B("resource_root_plist_tail", (rr.get("info_plist_path") or "").replace(
        "\\", "/").endswith("/%s/Info.plist" % bundle))
    # documents (derived: two authored nibs, lexical order)
    docs = n.get("documents", [])
    tdocs = truth["documents"]
    B("documents_count_2", len(docs) == len(tdocs) == 2)
    if len(docs) == 2:
        B("doc_paths_lexical",
          [d.get("relative_path") for d in docs] ==
          [t["relative_path"] for t in tdocs])
        B("doc_kinds_nib", all(d.get("document_kind") == "nib" for d in docs))
        B("doc0_sha_eq_built", docs[0].get("archive_sha256") == mm_sha)
        B("doc1_sha_eq_built", docs[1].get("archive_sha256") == sv_sha)
        B("doc0_object_count", docs[0].get("object_count") == tdocs[0]["object_count"])
        B("doc1_object_count", docs[1].get("object_count") == tdocs[1]["object_count"])
        B("doc0_connection_count",
          docs[0].get("connection_count") == tdocs[0]["connection_objects_with_source_encoded"])
        B("doc1_connection_count",
          docs[1].get("connection_count") == tdocs[1]["connection_objects_with_source_encoded"])

    def doc_node(doc_path, object_id):
        prefix = 'ib:"%s":object:' % doc_path
        for node in g.get("nodes", []):
            if node.get("id", "").startswith(prefix) and \
                    node.get("attributes", {}).get("interface_builder_object_id") == str(object_id):
                return node
        return None

    if len(docs) == 2:
        t0 = {o["id"]: o for o in tdocs[0]["objects"]}
        n0 = doc_node(tdocs[0]["relative_path"], 0)
        n1 = doc_node(tdocs[0]["relative_path"], 1)
        n2 = doc_node(tdocs[0]["relative_path"], 2)
        n3 = doc_node(tdocs[0]["relative_path"], 3)
        B("doc0_obj0_class_and_values",
          n0 is not None and n0.get("name") == t0[0]["class"]
          and n0.get("attributes", {}).get("nibValues") == t0[0]["values"])
        B("doc0_obj1_class_and_values",
          n1 is not None and n1.get("name") == t0[1]["class"]
          and n1.get("attributes", {}).get("nibValues") == t0[1]["values"])
        conn = t0[2]["values"]
        want_label = {"$nib_data_base64": base64.b64encode(
            conn["NSLabel_utf8"].encode()).decode()}
        B("doc0_obj2_class", n2 is not None and n2.get("name") == t0[2]["class"])
        if n2 is not None:
            v2 = n2.get("attributes", {}).get("nibValues", {})
            B("doc0_obj2_source_ref",
              v2.get("NSSource") == {"objectID": str(conn["NSSource"]["$ref"])})
            B("doc0_obj2_destination_ref",
              v2.get("NSDestination") == {"objectID": str(conn["NSDestination"]["$ref"])})
            B("doc0_obj2_label_base64",
              v2.get("NSLabel") == want_label)
        else:
            B("doc0_obj2_source_ref", False)
            B("doc0_obj2_destination_ref", False)
            B("doc0_obj2_label_base64", False)
        B("doc0_obj3_annotation_empty",
          n3 is not None and n3.get("name") == t0[3]["class"]
          and n3.get("attributes", {}).get("nibValues") == {})
        t1 = tdocs[1]["objects"][0]
        s0 = doc_node(tdocs[1]["relative_path"], 0)
        B("doc1_obj0_class_and_values",
          s0 is not None and s0.get("name") == t1["class"]
          and s0.get("attributes", {}).get("nibValues") == t1["values"])
        B("class_names_cover_truth",
          [nd.get("name") for nd in g.get("nodes", [])
           if str(nd.get("id", "")).startswith('ib:"%s":object:' % tdocs[0]["relative_path"])]
          == [t0[i]["class"] for i in (0, 1, 2, 3)])

    # pre-registered Q07 hypothesis checks (producer Interface Builder vocabulary)
    pv = truth["predicted_producer_vocabulary"]
    H("hyp_subject_null", rec.get("subject") is None)
    H("hyp_target_sha_null", n.get("target_sha256") is None)
    H("hyp_graph_tool_version",
      g.get("provider", {}).get("tool_version") == pv["graph_provider_tool_version"])
    H("hyp_node_count", len(g.get("nodes", [])) == pv["node_count"])
    scenes = [nd for nd in g.get("nodes", []) if nd.get("kind") == "scene"]
    H("hyp_scene_nodes", len(scenes) == pv["scene_nodes"]
      and sorted(nd.get("name") for nd in scenes) ==
      sorted(t["relative_path"] for t in tdocs))
    H("hyp_hierarchy_complete_false",
      all(d.get("hierarchy_complete") == pv["hierarchy_complete"] for d in docs))
    edges = g.get("edges", [])
    H("hyp_edge_count", len(edges) == pv["edge_count"])
    H("hyp_edge_relation", all(e.get("relation") == pv["edge_relation"] for e in edges))
    action = [nd for nd in g.get("nodes", []) if nd.get("kind") == pv["action_node"]["kind"]]
    H("hyp_action_node", len(action) == 1 and
      action[0].get("attributes", {}).get("selector") == pv["action_node"]["selector"] and
      action[0].get("attributes", {}).get("type") == pv["action_node"]["type"])
    if len(edges) == 2 and action and n2 is not None and n1 is not None:
        aid = action[0]["id"]
        H("hyp_edge0_source_to_action",
          edges[0].get("from") == n0.get("id") and edges[0].get("to") == aid)
        H("hyp_edge1_action_to_destination",
          edges[1].get("from") == aid and edges[1].get("to") == n1.get("id"))
    else:
        H("hyp_edge0_source_to_action", False)
        H("hyp_edge1_action_to_destination", False)
    facets = {c.get("facet"): c.get("status") for c in g.get("coverage", [])}
    H("hyp_coverage_facet_count", len(facets) == 9)
    H("hyp_archive_decode_complete", facets.get("archive_decode") == "complete")
    H("hyp_connections_facets",
      facets.get("connections:%s" % tdocs[0]["relative_path"]) == pv["connections_facet"]
      and facets.get("connections:%s" % tdocs[1]["relative_path"]) == pv["connections_facet"])
    H("hyp_hierarchy_facets_unsupported",
      facets.get("hierarchy:%s" % tdocs[0]["relative_path"]) == pv["hierarchy_facet"]
      and facets.get("hierarchy:%s" % tdocs[1]["relative_path"]) == pv["hierarchy_facet"])
    H("hyp_truncated_false", g.get("truncated") == pv["truncated"])
    H("hyp_confidence_observed", rec.get("confidence") == pv["confidence"])
    H("hyp_authority_shipped_artifact", rec.get("authority") == pv["authority"])

    total, bad = 0, 0
    for cls, checks in (("BYTE", byte_checks), ("HYP", hyp_checks)):
        for name, ok in checks:
            total += 1
            bad += 0 if ok else 1
            if not ok:
                print("ORACLE %s %s FAIL" % (cls, name))
    print("ORACLE byte-derived %d/%d, hypothesis %d/%d" % (
        sum(1 for _, ok in byte_checks if ok), len(byte_checks),
        sum(1 for _, ok in hyp_checks if ok), len(hyp_checks)))
    print("ORACLE OK (%d/%d checks)" % (total - bad, total) if bad == 0
          else "ORACLE FAIL (%d/%d checks)" % (total - bad, total))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
