#!/usr/bin/env python
"""build_zip.py - author the round-84 inert zip fixture (criterion A1v2).

Builds R84Sample.zip: a deterministic ZIP_STORED archive with three
authored entries (fixed DOS timestamp 2026-11-02 00:00:00, no extra
fields, external_attr 0o644<<16). The archive bytes are fully
determined by the entry contents below; two builds are byte-identical.

The entries are inert data: text and range bytes. Nothing in the
archive is executed by this lane or by the producers; the producers
(inventory/extract) only read structure and bytes.

SELFCHECK (Q06 derive-then-assert; no byte-size constants anywhere):
re-opens the BUILT bytes with the stdlib zipfile reader and re-derives
every oracle-checked fact from those bytes - entry order, names,
content sizes, CRC32s, content sha256s, the fixture-file sha256 - and
asserts each against the authored CONTENT constants (the only literals
in this file are the entry payloads and their names). Any mismatch
fails the build before a producer ever sees the bytes.

derive_truth(fixture_bytes): computes the truth.json payload the
oracle checks against - every expected value derived from the built
bytes by the stdlib reader, never copied from a producer record.

Usage:
  python -I -B build_zip.py selfcheck <out.zip>       # build + SELFCHECK
  python -I -B build_zip.py derive <out.zip> <truth.json>  # build + derive truth
  python -I -B build_zip.py regen <a.zip> <b.zip>     # two builds must be byte-identical
"""
import hashlib
import io
import json
import sys
import zipfile
import zlib

ENTRIES = [
    ("MANIFEST.txt",
     b"R84 archive fixture - authored inert zip for the artifact-graph "
     b"inventory/extract records\n"),
    ("data/blob.bin", bytes(range(48))),
    ("data/nested/note.md", b"# note\nauthored fixture content\n"),
]

DOS_STAMP = (2026, 11, 2, 0, 0, 0)


def build(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as z:
        for name, data in ENTRIES:
            zi = zipfile.ZipInfo(name, date_time=DOS_STAMP)
            zi.external_attr = 0o644 << 16
            z.writestr(zi, data)


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def derive_facts(fb):
    """Re-derive every checked fact from the built bytes (stdlib reader)."""
    facts = {"entry_count": 0, "entries": []}
    import io, zlib
    with zipfile.ZipFile(io.BytesIO(fb)) as z:
        infos = z.infolist()
        facts["entry_count"] = len(infos)
        for zi in infos:
            data = z.read(zi.filename)
            facts["entries"].append({
                "name": zi.filename,
                "size": len(data),
                "crc32": "%08x" % (zi.CRC & 0xFFFFFFFF),
                "sha256": hashlib.sha256(data).hexdigest(),
                "compress_type": zi.compress_type,
            })
    facts["fixture_sha256"] = hashlib.sha256(fb).hexdigest()
    return facts


def selfcheck(path):
    fb = read_bytes(path)
    facts = derive_facts(fb)
    checks = []
    ok = True

    def chk(label, cond):
        nonlocal ok
        checks.append((label, bool(cond)))
        ok = ok and cond

    chk("entry count == authored", facts["entry_count"] == len(ENTRIES))
    for i, (name, data) in enumerate(ENTRIES):
        e = facts["entries"][i]
        chk("entry %d name" % i, e["name"] == name)
        chk("entry %d size == len(content)" % i, e["size"] == len(data))
        chk("entry %d crc32 re-derived" % i,
            e["crc32"] == "%08x" % (zlib.crc32(data) & 0xFFFFFFFF))
        chk("entry %d sha256 re-derived" % i,
            e["sha256"] == hashlib.sha256(data).hexdigest())
        chk("entry %d stored (no compression)" % i, e["compress_type"] == zipfile.ZIP_STORED)
    # fixture sha256 must equal the hash of exactly these bytes
    chk("fixture sha256 == sha256(built bytes)",
        facts["fixture_sha256"] == hashlib.sha256(fb).hexdigest())
    for label, c in checks:
        print("SELFCHECK %s %s" % ("ok" if c else "FAIL", label))
    print("SELFCHECK %d/%d" % (sum(1 for _l, c in checks if c), len(checks)))
    return 0 if ok else 1


def derive(path, truth_path):
    fb = read_bytes(path)
    facts = derive_facts(fb)
    payload = {
        "fixture": "corpus/fixtures/arc-r84/R84Sample.zip",
        "fixture_sha256": facts["fixture_sha256"],
        "entries": facts["entries"],
        "entry_count": facts["entry_count"],
        # Q07 pre-registered hypotheses (provider/output semantics), frozen
        # BEFORE the committed producer runs; recorded whichever way they fall.
        "hyp": {
            "provider_id": "rea-artifact-graph",
            "predicate_type": "rea.analysis",
            "inspect_operation": "inspect_artifact",
            "inspect_substep_operation": "inventory_artifact",
            "substep_status": "completed",
            "root_format": "zip",
            "inspect_node_count": facts["entry_count"] + 1,
            "inspect_edge_count": facts["entry_count"],
            "node_content_state": "embedded",
            "extract_operation": "extract_artifact",
            "extract_node_count": facts["entry_count"] + 1,
            "extract_edge_count": facts["entry_count"],
            "extract_created_all": True,
            "containment_verified": True,
            "integrity_contradictions_empty": True,
            "cleanup_pending": False,
            "output_root_outside_repo": True,
            "evidence_id_form": "ev_[0-9a-f]{64}",
            "extraction_id_form": "aex_[0-9a-f]{64}",
            "manifest_id_form": "agm_[0-9a-f]{64}",
        },
    }
    with open(truth_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, indent=1, sort_keys=True)
        f.write("\n")
    print("derive: wrote %s (fixture sha %s…%s, %d entries)"
          % (truth_path, facts["fixture_sha256"][:8], facts["fixture_sha256"][-4:],
             facts["entry_count"]))
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "selfcheck":
        build(args[1])
        raise SystemExit(selfcheck(args[1]))
    if len(args) == 3 and args[0] == "derive":
        build(args[1])
        sc = selfcheck(args[1])
        if sc != 0:
            raise SystemExit(sc)
        raise SystemExit(derive(args[1], args[2]))
    if len(args) == 3 and args[0] == "regen":
        build(args[1])
        build(args[2])
        a, b = read_bytes(args[1]), read_bytes(args[2])
        print("REGEN %s (%d bytes each)"
              % ("byte-identical" if a == b else "DIFFERS", len(a)))
        raise SystemExit(0 if a == b else 1)
    print(__doc__)
    raise SystemExit(64)
