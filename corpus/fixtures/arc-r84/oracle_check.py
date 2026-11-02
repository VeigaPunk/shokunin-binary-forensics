#!/usr/bin/env python
"""oracle_check.py - round-84 identity oracle for the two A1v2 producer
records (inspect_artifact, extract_artifact) over the authored inert zip
fixture (criterion A1v2, corpus/fixtures/arc-r84/).

Every BYTE check re-derives its expected value from the built fixture
bytes (stdlib zipfile/zlib/hashlib) or from the truth payload the
generator's derive() wrote from those bytes (Q03: nothing is copied from
the record under test). Every HYP check compares against a pre-registered
hypothesis frozen in the truth payload BEFORE the committed producer runs
(Q07: recorded whichever way it falls). Producer-internal identifiers
(evidence/manifest ids) are checked for FORM only - they are derived by
the producer, not by this oracle.

The oracle dispatches on the record's own top-level `operation` field and
counts only that operation's check set.

Usage:
  python -I -B oracle_check.py <truth.json> <record.json> <fixture.zip>

Exit 0 and last line `ORACLE OK (N/M checks)` iff every check passes;
exit 1 with the failing lines otherwise.
"""
import hashlib
import json
import os
import re
import sys
import zipfile


def load(path):
    with open(path, "rb") as f:
        return f.read()


def form_ok(value, pattern):
    return isinstance(value, str) and re.fullmatch(pattern, value) is not None


def fixture_facts(fb):
    facts = {"sha256": hashlib.sha256(fb).hexdigest(), "entries": []}
    import io
    with zipfile.ZipFile(io.BytesIO(fb)) as z:
        for zi in z.infolist():
            data = z.read(zi.filename)
            facts["entries"].append({
                "name": zi.filename,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            })
    facts["fixture_size"] = len(fb)
    return facts


def oracle_inspect(rec, truth, facts):
    checks = []

    def chk(label, cond):
        checks.append((label, bool(cond)))

    nr = rec.get("normalized_result", {})
    ss = (nr.get("substeps") or [{}])[0]
    ssev = ss.get("evidence", {})
    ssman = (ssev.get("normalized_result") or {}).get("manifest", {})
    man_nodes = (ssev.get("normalized_result") or {}).get("nodes") or []
    fsha = facts["sha256"]
    hyp = truth["hyp"]
    chk("BYTE operation == inspect_artifact",
        rec.get("operation") == "inspect_artifact")
    chk("BYTE provider.id == rea-artifact-graph",
        (rec.get("provider") or {}).get("id") == "rea-artifact-graph")
    chk("BYTE nr.subject.root_sha256 == fixture sha",
        (nr.get("subject") or {}).get("root_sha256") == fsha)
    chk("BYTE nr.subject.root_format == zip",
        (nr.get("subject") or {}).get("root_format") == "zip")
    chk("BYTE substep.operation == inventory_artifact",
        ss.get("operation") == "inventory_artifact")
    chk("BYTE substep.status == completed", ss.get("status") == "completed")
    chk("BYTE substep subject digest == fixture sha",
        ((ssev.get("subject") or {}).get("digest") or {}).get("sha256") == fsha)
    chk("BYTE substep subject format == zip",
        (ssev.get("subject") or {}).get("format") == "zip")
    chk("BYTE substep manifest root_sha256 == fixture sha",
        ssman.get("root_sha256") == fsha)
    chk("BYTE substep manifest root_format == zip",
        ssman.get("root_format") == "zip")
    roots = [n for n in man_nodes if n.get("format") == "zip"]
    chk("BYTE exactly one root node, format zip", len(roots) == 1)
    if roots:
        chk("BYTE root node size == fixture size",
            roots[0].get("size") == facts["fixture_size"])
        chk("BYTE root node content_state == materialized",
            roots[0].get("content_state") == "materialized")
    else:
        chk("BYTE root node size == fixture size", False)
        chk("BYTE root node content_state == materialized", False)
    for i, e in enumerate(facts["entries"]):
        m = [n for n in man_nodes if n.get("sha256") == e["sha256"]]
        chk("BYTE entry %d (%s): node sha256 match" % (i, e["name"]), len(m) == 1)
        if m:
            chk("BYTE entry %d (%s): node size == %d" % (i, e["name"], e["size"]),
                m[0].get("size") == e["size"])
        else:
            chk("BYTE entry %d (%s): node size" % (i, e["name"]), False)
    chk("BYTE matched entry nodes content_state == embedded",
        all(n.get("content_state") == "embedded"
            for e in facts["entries"]
            for n in man_nodes if n.get("sha256") == e["sha256"]))
    # pre-registered hypotheses (Q07; recorded whichever way they fall)
    chk("HYP evidence_id form ev_hex64",
        form_ok(rec.get("evidence_id"), hyp["evidence_id_form"]))
    chk("HYP inspection_id form ai_hex64",
        form_ok(nr.get("inspection_id"), "ai_[0-9a-f]{64}"))
    chk("HYP manifest_id form agm_hex64",
        form_ok(ssman.get("manifest_id"), hyp["manifest_id_form"]))
    chk("HYP substep_id form ais_hex64",
        form_ok(ss.get("substep_id"), "ais_[0-9a-f]{64}"))
    chk("HYP node_count == entries+1",
        ssman.get("node_count") == hyp["inspect_node_count"])
    chk("HYP occurrence_count == entries+1",
        ssman.get("occurrence_count") == hyp["inspect_node_count"])
    chk("HYP edge_count == entries",
        ssman.get("edge_count") == hyp["inspect_edge_count"])
    chk("HYP substep provider.id == rea-artifact-graph",
        (ssev.get("provider") or {}).get("id") == hyp["provider_id"])
    chk("HYP authority == shipped-artifact",
        rec.get("authority") == "shipped-artifact")
    chk("HYP predicate_type == rea.analysis",
        rec.get("predicate_type") == hyp["predicate_type"])
    chk("HYP confidence == observed", rec.get("confidence") == "observed")
    chk("HYP substep evidence_id form ev_hex64",
        form_ok(ss.get("evidence_id"), hyp["evidence_id_form"]))
    chk("HYP nr.contradictions empty", nr.get("contradictions") == [])
    cov = nr.get("coverage") or {}
    chk("HYP nr.coverage.status == complete-within-substeps",
        cov.get("status") == "complete-within-substeps")
    chk("HYP nr.coverage.substeps_completed == 1",
        cov.get("substeps_completed") == 1)
    chk("HYP nr.coverage.observations_omitted == 0",
        cov.get("observations_omitted") == 0)
    return checks


def oracle_extract(rec, truth, facts):
    checks = []

    def chk(label, cond):
        checks.append((label, bool(cond)))

    nr = rec.get("normalized_result", {})
    man = nr.get("manifest", {})
    exm = nr.get("extraction_manifest", {})
    arts = nr.get("artifacts") or []
    fsha = facts["sha256"]
    hyp = truth["hyp"]
    chk("BYTE operation == extract_artifact",
        rec.get("operation") == "extract_artifact")
    chk("BYTE provider.id == rea-artifact-graph",
        (rec.get("provider") or {}).get("id") == "rea-artifact-graph")
    chk("BYTE manifest.root_sha256 == fixture sha",
        man.get("root_sha256") == fsha)
    chk("BYTE manifest.root_format == zip", man.get("root_format") == "zip")
    chk("BYTE manifest.node_count == entries+1",
        man.get("node_count") == hyp["extract_node_count"])
    for i, e in enumerate(facts["entries"]):
        rows = [a for a in arts if a.get("relative_path") == e["name"]]
        chk("BYTE entry %d (%s): artifact row present" % (i, e["name"]),
            len(rows) == 1)
        if rows:
            chk("BYTE entry %d (%s): sha256 match" % (i, e["name"]),
                rows[0].get("sha256") == e["sha256"])
            chk("BYTE entry %d (%s): bytes_written == %d" % (i, e["name"], e["size"]),
                rows[0].get("bytes_written") == e["size"])
            chk("BYTE entry %d (%s): created true" % (i, e["name"]),
                rows[0].get("created") is True)
        else:
            chk("BYTE entry %d (%s): sha256 match" % (i, e["name"]), False)
            chk("BYTE entry %d (%s): bytes_written" % (i, e["name"]), False)
            chk("BYTE entry %d (%s): created true" % (i, e["name"]), False)
    out_root = nr.get("output_root") or ""
    fixture_dir = os.path.dirname(os.path.abspath(truth.get("_fixture_path", ""))) \
        if truth.get("_fixture_path") else None
    chk("BYTE output_root outside the fixture directory",
        bool(out_root) and fixture_dir is not None
        and not out_root.startswith(fixture_dir))
    chk("HYP evidence_id form ev_hex64",
        form_ok(rec.get("evidence_id"), hyp["evidence_id_form"]))
    chk("HYP extraction_id form aex_hex64",
        form_ok(exm.get("extraction_id"), hyp["extraction_id_form"]))
    chk("HYP manifest_id form agm_hex64",
        form_ok(man.get("manifest_id"), hyp["manifest_id_form"]))
    chk("HYP manifest.edge_count == entries",
        man.get("edge_count") == hyp["extract_edge_count"])
    chk("HYP selected_occurrence_ids == entries",
        len(exm.get("selected_occurrence_ids") or []) == len(facts["entries"]))
    chk("HYP containment_verified true", nr.get("containment_verified") is True)
    chk("HYP integrity_contradictions empty",
        nr.get("integrity_contradictions") == [])
    chk("HYP cleanup attempted false / verified true / no residuals",
        nr.get("cleanup") == {"attempted": False, "verified": True,
                              "residual_paths": []})
    chk("HYP coverage == container-entries/complete",
        nr.get("coverage") == {"scope": "container-entries",
                               "status": "complete"})
    chk("HYP authority == shipped-artifact",
        rec.get("authority") == "shipped-artifact")
    chk("HYP predicate_type == rea.analysis",
        rec.get("predicate_type") == hyp["predicate_type"])
    chk("HYP confidence == observed", rec.get("confidence") == "observed")
    chk("HYP output_root under the host temp area",
        "Temp" in out_root or "tmp" in out_root.lower())
    return checks


def main() -> int:
    truth_path, rec_path, fixture_path = sys.argv[1], sys.argv[2], sys.argv[3]
    truth = json.loads(load(truth_path).decode("utf-8"))
    rec = json.loads(load(rec_path).decode("utf-8"))
    truth["_fixture_path"] = fixture_path
    facts = fixture_facts(load(fixture_path))
    if truth.get("fixture_sha256") != facts["sha256"]:
        print("ORACLE FAIL truth fixture_sha256 %s != built bytes %s"
              % (truth.get("fixture_sha256"), facts["sha256"]))
        return 1
    op = rec.get("operation")
    if op == "inspect_artifact":
        checks = oracle_inspect(rec, truth, facts)
    elif op == "extract_artifact":
        checks = oracle_extract(rec, truth, facts)
    else:
        print("ORACLE FAIL unknown record operation %r" % (op,))
        return 1
    ok = 0
    for label, c in checks:
        print("ORACLE %s %s" % ("ok" if c else "FAIL", label))
        ok += 1 if c else 0
    total = len(checks)
    if ok == total:
        print("ORACLE OK (%d/%d checks)" % (ok, total))
        return 0
    print("ORACLE FAILED (%d/%d checks)" % (ok, total))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
