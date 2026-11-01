#!/usr/bin/env python
"""oracle_check.py - round-82 dylib-resolution record identity oracle.

Usage:
  python -I -B oracle_check.py truth.json inspection.json <image/main.dylib>

Every BYTE-DERIVED check compares the record against facts derived from the
built fixture bytes and the authored tree (truth.json, itself written by
generator.py's derive()). The HYPOTHESIS checks are the pre-registered
Q07 predictions about the producer's declared dyld-resolution vocabulary
(outcome/resolution/coverage/confidence/authority); they are checked and
recorded whichever way they fall. The two classes are printed separately.
Host-dependent fields (evidence_id, caller_input_path, absolute
root_path/local_path parameters) are never checked.
"""
import hashlib
import json
import sys
from pathlib import Path


def main() -> int:
    truth_p, rec_p, main_p = sys.argv[1], sys.argv[2], sys.argv[3]
    truth = json.loads(Path(truth_p).read_text(encoding="utf-8"))
    rec = json.loads(Path(rec_p).read_text(encoding="utf-8"))
    main_bytes = Path(main_p).read_bytes()
    main_sha = hashlib.sha256(main_bytes).hexdigest()
    alpha_sha = truth["alpha"]["sha256"]
    m, a, dr = truth["main"], truth["alpha"], truth["declared_resolution"]
    n = rec["normalized_result"]
    byte_checks = []
    hyp_checks = []

    def B(name, ok):
        byte_checks.append((name, bool(ok)))

    def H(name, ok):
        hyp_checks.append((name, bool(ok)))

    B("truth_main_sha_matches_fixture_bytes", truth["main"]["sha256"] == main_sha)
    B("operation", rec.get("operation") == "trace_dylib_resolution")
    B("provider_id", rec.get("provider", {}).get("id") == "rea-artifact-graph")
    B("subject_format", rec.get("subject", {}).get("format") == "mach-o")
    B("subject_sha_eq_fixture", rec.get("subject", {}).get("digest", {}).get("sha256") == main_sha)
    B("target_sha_eq_fixture", n.get("target_sha256") == main_sha)
    B("roots", n.get("roots") == [{"image": "main.dylib", "architecture": "x86_64"}])
    images = n.get("images", [])
    B("images_count_2", len(images) == 2)
    if images:
        s0 = images[0].get("slices", [{}])[0]
        B("img0_path", images[0].get("path") == "main.dylib")
        B("img0_sha", images[0].get("sha256") == main_sha)
        B("img0_parsed", images[0].get("parse_status") == "parsed")
        B("img0_arch", s0.get("architecture") == "x86_64")
        B("img0_slice_size", s0.get("slice_size") == m["bytes"])
        B("img0_cpu_type", s0.get("cpu_type") == m["cpu_type"])
        B("img0_file_type_code", s0.get("file_type_code") == m["file_type_code"])
        B("img0_file_type", s0.get("file_type") == m["file_type"])
        B("img0_install_name", s0.get("install_name") == m["install_name"])
        B("img0_rpaths", s0.get("rpaths") == m["rpaths"])
    if len(images) > 1:
        s1 = images[1].get("slices", [{}])[0]
        B("img1_path", images[1].get("path") == "rpathdir/libalpha.dylib")
        B("img1_sha", images[1].get("sha256") == alpha_sha)
        B("img1_parsed", images[1].get("parse_status") == "parsed")
        B("img1_slice_size", s1.get("slice_size") == a["bytes"])
        B("img1_install_name", s1.get("install_name") == a["install_name"])
        B("img1_rpaths_empty", s1.get("rpaths") == [])
    edges = n.get("edges", [])
    B("edges_count_3", len(edges) == 3)
    if len(edges) == 3:
        B("edge_install_names", [e.get("install_name") for e in edges] == dr["edge_install_names"])
        B("edge_command_encoding", all(
            e.get("command") == "LC_LOAD_DYLIB" and e.get("encoding") == "dylib_command"
            for e in edges))
        B("edge_versions", all(
            e.get("current_version") == dr["edge_current_versions"][i]
            and e.get("compatibility_version") == dr["edge_compatibility_versions"][i]
            for i, e in enumerate(edges)))
        B("edge0_candidate_source_rpath", edges[0].get("candidates", [{}])[0].get("source") == "rpath")
        B("edge0_candidate_rpath", edges[0].get("candidates", [{}])[0].get("rpath") == "@loader_path/rpathdir")
        B("edge0_candidate_path", edges[0].get("candidates", [{}])[0].get("path") == dr["edge0_candidate_path"])
        B("edge0_resolved_path", edges[0].get("candidates", [{}])[0].get("resolved_path") == dr["edge0_candidate_path"])
        B("edge1_source_loader_path", edges[1].get("candidates", [{}])[0].get("source") == "loader_path")
        B("edge1_candidate_path", edges[1].get("candidates", [{}])[0].get("path") == "../Frameworks/libbeta.dylib")
        B("edge2_source_literal", edges[2].get("candidates", [{}])[0].get("source") == "literal")
        B("edge2_candidate_path", edges[2].get("candidates", [{}])[0].get("path") == "/usr/lib/libSystem.B.dylib")
    locs = [(l.get("kind"), l.get("path")) for l in rec.get("locations", [])]
    B("locations", ("artifact-path", "main.dylib") in locs
       and ("artifact-path", "rpathdir/libalpha.dylib") in locs)
    # pre-registered Q07 hypothesis checks (producer dyld vocabulary)
    if len(edges) == 3:
        H("hyp_edge0_outcome_undetermined", edges[0].get("candidates", [{}])[0].get("outcome") == "undetermined")
        H("hyp_edge0_resolution_undetermined", edges[0].get("resolution", {}).get("status") == "undetermined")
        H("hyp_edge1_outcome_escapes_target", edges[1].get("candidates", [{}])[0].get("outcome") == "escapes-target")
        H("hyp_edge1_resolution_undetermined", edges[1].get("resolution", {}).get("status") == "undetermined")
        H("hyp_edge2_outside_target", edges[2].get("candidates", [{}])[0].get("outcome") == "outside-target")
        H("hyp_edge2_resolution_undetermined", edges[2].get("resolution", {}).get("status") == "undetermined")
    H("hyp_findings_empty", n.get("findings") == [])
    H("hyp_coverage_partial", n.get("coverage", {}).get("status") == "partial")
    H("hyp_confidence_observed", rec.get("confidence") == "observed")
    H("hyp_authority_shipped_artifact", rec.get("authority") == "shipped-artifact")

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
