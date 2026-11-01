#!/usr/bin/env python
"""oracle_check.py - checks the saved producer record against byte-derived truth.

Usage: python -B oracle_check.py truth.json <record.json> fixture.db

Every expectation comes from truth.json (derived from the built fixture bytes
by generator.py's self-check) or from the fixture bytes re-read here. The
record is evidence, never the premise (Q03/Q06). Prints one line per check
and finishes with `ORACLE OK (N/N checks)` (exit 0) or `ORACLE FAILED`
(exit 1) listing the failed check ids.
"""
import json
import pathlib
import re
import sys

PREPROBE_EVIDENCE_ID = "ev_7fc82dd0260c01a60"  # prefix of the scratch dress-rehearsal record; the committed run must differ


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: oracle_check.py truth.json <record.json> fixture.db", file=sys.stderr)
        return 2
    truth = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    rec = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
    fixture = pathlib.Path(sys.argv[3]).read_bytes()
    fixture_sha = truth["fixture_sha256"]
    assert fixture_sha == __import__("hashlib").sha256(fixture).hexdigest(), "fixture.db drifted from truth.json"

    checks = []

    def chk(cid, ok, detail=""):
        checks.append((cid, bool(ok)))
        print("%s=%s%s" % (cid, "pass" if ok else "FAIL", (" " + detail if detail and not ok else "")))

    envelope_ok = isinstance(rec, dict) and rec.get("evidence_id") and rec.get("normalized_result") is not None
    chk("ENVELOPE", envelope_ok)
    chk("OPERATION", rec.get("operation") == "inspect_sqlite_database", rec.get("operation"))
    prov = rec.get("provider") or {}
    chk("PROVIDER_ID", prov.get("id") == "sqlite", prov.get("id"))
    chk("PROVIDER_VERSION", bool(re.match(r"^SQLite \d+\.\d+\.\d+$", str(prov.get("version")))), prov.get("version"))
    subj = rec.get("subject") or {}
    chk("SUBJECT_NAME", subj.get("name") == truth["fixture_name"], subj.get("name"))
    chk("SUBJECT_SHA", (subj.get("digest") or {}).get("sha256") == fixture_sha)
    chk("SUBJECT_FORMAT", subj.get("format") == "file", subj.get("format"))
    nr = rec.get("normalized_result") or {}
    art = nr.get("artifact") or {}
    chk("ARTIFACT_SHA", art.get("sha256") == fixture_sha)
    chk("ARTIFACT_BYTES", art.get("bytes") == truth["file_size"], art.get("bytes"))
    chk("WAL_ABSENT", nr.get("wal") is None, nr.get("wal"))
    eng = nr.get("engine") or {}
    chk("ENGINE_NAME", eng.get("name") == "SQLite", eng.get("name"))
    chk("DB_ENCODING", nr.get("database_encoding") == truth["encoding_name"], nr.get("database_encoding"))
    chk("PAGE_SIZE", truth["page_size"] == 4096 and truth["file_size"] == truth["page_size"] * truth["page_count"])
    sc = nr.get("schema") or {}
    chk("SCOPE", sc.get("scope") == "database", sc.get("scope"))
    chk("COMPLETENESS", sc.get("completeness") == "complete", sc.get("completeness"))
    tables = sc.get("tables") or []
    chk("TABLE_COUNT", len(tables) == 2, len(tables))
    tnames = sorted(t.get("name") for t in tables)
    chk("TABLE_NAMES", tnames == ["meta", "samples"], tnames)
    byname = {t.get("name"): t for t in tables}
    for tname, want in (("meta", truth["objects"]["meta"]), ("samples", truth["objects"]["samples"])):
        t = byname.get(tname) or {}
        chk("ROOT_%s" % tname.upper(), t.get("root_page") == want["root_page"], t.get("root_page"))
        chk("COLCOUNT_%s" % tname.upper(), t.get("column_count") == want["column_count"], t.get("column_count"))
        got_cols = [c.get("name") if isinstance(c, dict) else c for c in (t.get("columns") or [])]
        chk("COLS_%s" % tname.upper(), got_cols == want["columns"], got_cols)
        chk("KIND_%s" % tname.upper(), t.get("kind") == "table" and t.get("without_rowid") is False and t.get("strict") is False)
    idx = sc.get("indexes") or []
    chk("INDEX_COUNT", len(idx) == 2, len(idx))
    iby = {i.get("name"): i for i in idx}
    for iname, want, tag in (("sqlite_autoindex_meta_1", truth["objects"]["sqlite_autoindex_meta_1"], "META"),
                             ("sqlite_autoindex_samples_1", truth["objects"]["sqlite_autoindex_samples_1"], "SAMPLES")):
        i = iby.get(iname) or {}
        chk("AUTOIDX_%s" % tag, i.get("table") == want["table"] and i.get("root_page") == want["root_page"],
            "%s/%s" % (i.get("table"), i.get("root_page")))
    chk("VIEWS_NONE", sc.get("views") == truth["views_expected"], sc.get("views"))
    chk("TRIGGERS_NONE", sc.get("triggers") == truth["triggers_expected"], sc.get("triggers"))
    chk("ROWS_UNREQUESTED", nr.get("rows") is None, nr.get("rows"))
    chk("CONFIDENCE", rec.get("confidence") == "observed", rec.get("confidence"))
    chk("AUTHORITY", rec.get("authority") == "shipped-artifact", rec.get("authority"))
    ev = rec.get("evidence_id") or ""
    chk("EVIDENCE_ID_FORM", bool(re.match(r"^ev_[0-9a-f]{64}$", ev)) and not ev.startswith(PREPROBE_EVIDENCE_ID), ev[:20])

    npass = sum(1 for _, ok in checks if ok)
    n = len(checks)
    if npass == n:
        print("ORACLE OK (%d/%d checks)" % (npass, n))
        return 0
    print("ORACLE FAILED (%d/%d checks): %s" % (npass, n, [cid for cid, ok in checks if not ok]))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
