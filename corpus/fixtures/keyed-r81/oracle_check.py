#!/usr/bin/env python
"""oracle_check.py - keyed-r81 identity oracle.

Compares the saved producer record (exact stdout JSON of one
`rea inspect-keyed-archive` run) against truth.json, whose every expected
value was derived by generator.py from the built fixture bytes - never from
the producer's own output (Q06).

Usage: python -B oracle_check.py truth.json inspection.json fixture.plist
Prints one ORACLE line per check and `ORACLE OK (n/n checks)`; exit 0 iff
every check passes, 1 otherwise.
"""
import hashlib
import json
import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: oracle_check.py truth.json inspection.json fixture.plist",
              file=sys.stderr)
        return 64
    truth = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    rec = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    fix = Path(sys.argv[3]).read_bytes()
    checks = []

    def ck(name, ok):
        checks.append((name, bool(ok)))

    fix_sha = hashlib.sha256(fix).hexdigest()
    nr = rec.get("normalized_result") or {}
    subj = rec.get("subject") or {}
    # envelope checks
    ck("operation", rec.get("operation") == "inspect_keyed_archive")
    ck("provider", (rec.get("provider") or {}).get("id") == "rea-artifact-graph")
    ck("predicate_type", rec.get("predicate_type") == "rea.analysis")
    ck("evidence_id_form",
       bool(re.fullmatch(r"ev_[0-9a-f]{64}", rec.get("evidence_id") or "")))
    ck("subject_sha_eq_fixture", (subj.get("digest") or {}).get("sha256") == fix_sha)
    ck("confidence", rec.get("confidence") == "observed")
    ck("authority", rec.get("authority") == "shipped-artifact")
    # normalized checks, each value derived from the built bytes
    ck("target_sha_eq_fixture", nr.get("target_sha256") == fix_sha)
    ck("archive_sha_eq_fixture", nr.get("archive_sha256") == fix_sha)
    ck("archive_format", nr.get("archive_format") == truth["archive_format"])
    ck("total_objects", nr.get("total_objects") == truth["total_objects"])
    ck("total_references", nr.get("total_references") == truth["total_references"])
    ck("roots", nr.get("roots") == truth["roots"])
    ck("offset", nr.get("offset") == truth["offset"])
    ck("next_offset", nr.get("next_offset") == truth["next_offset"])
    ck("truncated", nr.get("truncated") == truth["truncated"])
    # per-object checks (kind/status/value exactly as derived from the bytes)
    got_objs = {o.get("id"): o for o in nr.get("objects") or []}
    for t in truth["objects"]:
        g = got_objs.get(t["id"])
        ck("object_%d" % t["id"],
           g is not None and g.get("kind") == t["kind"]
           and g.get("status") == t["status"] and g.get("value") == t["value"])
    # per-reference checks (exact set equality on source/path/target/status)
    def ref_key(r):
        src = r.get("source")
        return ((-1 if src is None else src), tuple(r.get("path") or []),
                r.get("target"), r.get("status"))
    got_refs = sorted((ref_key(r) for r in nr.get("references") or []))
    want_refs = sorted((ref_key(r) for r in truth["references"]))
    for i, want in enumerate(want_refs):
        ck("reference_%d" % i, want in got_refs)
    ck("no_extra_references", got_refs == want_refs)

    bad = 0
    for name, ok in checks:
        if not ok:
            bad += 1
            print("ORACLE FAIL %s" % name)
    total = len(checks)
    if bad == 0:
        print("ORACLE OK (%d/%d checks)" % (total, total))
        return 0
    print("ORACLE %d/%d checks failed" % (total - bad, total))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
