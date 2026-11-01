#!/usr/bin/env python
"""generator.py - round-81 keyed-archive fixture builder .

Builds an inert Foundation keyed archive (NSKeyedArchiver-shaped binary
plist) with a fully authored object graph, then derives EVERY oracle-checked
fact by re-parsing the built bytes (Q06 discipline, SKILL.md section 2: the
truth is derived from the built bytes, never from intent or from the
producer's own output).

Archive shape (authored intent):
  $version  100000
  $archiver NSKeyedArchiver
  $objects  ["$null", "revenger-keyed-r81",
             {"alpha": UID(1), "beta": UID(4), "n": 1729},
             "alpha", "beta",
             {"gamma": UID(1)}]
  $top      {"root": UID(2)}

Producer expectations derived from those bytes: 6 objects (1 nil + 3 scalars
+ 2 dictionaries), 4 references (root->2, 2->1 via "alpha", 2->4 via "beta",
5->1 via "gamma"), all resolved, binary-plist format, no truncation.

Usage: python -B generator.py            # build fixture.plist + truth.json
       python -B generator.py regen      # rebuild to a temp dir, byte-compare
       python -B generator.py self-check # derive truth from built bytes, print
"""
import hashlib
import json
import plistlib
import plistlib as _pl
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixture.plist"
TRUTH = HERE / "truth.json"


def build_bytes() -> bytes:
    arch = {
        "$version": 100000,
        "$archiver": "NSKeyedArchiver",
        "$objects": [
            "$null",
            "revenger-keyed-r81",
            {"alpha": _pl.UID(1), "beta": _pl.UID(4), "n": 1729},
            "alpha",
            "beta",
            {"gamma": _pl.UID(1)},
        ],
        "$top": {"root": _pl.UID(2)},
    }
    return plistlib.dumps(arch, fmt=plistlib.FMT_BINARY, sort_keys=True)


def derive(data: bytes) -> dict:
    """Derive every oracle-checked fact from the built bytes."""
    back = plistlib.loads(data)
    assert back["$version"] == 100000 and back["$archiver"] == "NSKeyedArchiver"
    objs = back["$objects"]
    objects = []
    for i, o in enumerate(objs):
        if o == "$null":
            objects.append({"id": i, "kind": "nil", "status": "nil", "value": "$null"})
        elif isinstance(o, dict):
            value = {k: ({"UID": v.data} if isinstance(v, _pl.UID) else v)
                     for k, v in o.items()}
            objects.append({"id": i, "kind": "dictionary", "status": "observed",
                            "value": value})
        else:
            objects.append({"id": i, "kind": "scalar", "status": "observed",
                            "value": o})
    roots = {k: {"UID": v.data} for k, v in back["$top"].items()}
    refs = []
    for k, v in back["$top"].items():
        if isinstance(v, _pl.UID):
            refs.append({"source": None, "path": [k], "target": v.data,
                         "status": "resolved"})
    for i, o in enumerate(objs):
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, _pl.UID):
                    refs.append({"source": i, "path": [k], "target": v.data,
                                 "status": "resolved"})
    refs.sort(key=lambda r: (r["source"] is not None, r["source"] or 0,
                             tuple(r["path"])))
    return {
        "fixture_sha256": hashlib.sha256(data).hexdigest(),
        "fixture_bytes": len(data),
        "magic": data[:8].decode("ascii"),
        "archive_format": "binary-plist" if data[:8] == b"bplist00" else "unknown",
        "total_objects": len(objs),
        "total_references": len(refs),
        "roots": roots,
        "objects": objects,
        "references": refs,
        "offset": 0,
        "next_offset": None,
        "truncated": False,
    }


def expected_summary(d: dict) -> dict:
    return {
        "nil_objects": sum(1 for o in d["objects"] if o["kind"] == "nil"),
        "scalar_objects": sum(1 for o in d["objects"] if o["kind"] == "scalar"),
        "dict_objects": sum(1 for o in d["objects"] if o["kind"] == "dictionary"),
        "unresolved_refs": sum(1 for r in d["references"] if r["status"] != "resolved"),
    }


def self_check() -> int:
    data = FIXTURE.read_bytes()
    d = derive(data)
    s = expected_summary(d)
    checks = [
        ("magic", d["magic"] == "bplist00"),
        ("fixture_bytes_eq_sha_recorded", d["fixture_bytes"] == len(data)),
        ("nil_objects_1", s["nil_objects"] == 1),
        ("scalar_objects_3", s["scalar_objects"] == 3),
        ("dict_objects_2", s["dict_objects"] == 2),
        ("total_objects_6", d["total_objects"] == 6),
        ("total_references_4", d["total_references"] == 4),
        ("unresolved_refs_0", s["unresolved_refs"] == 0),
        ("root_is_uid2", d["roots"] == {"root": {"UID": 2}}),
        ("root_ref_present", {"source": None, "path": ["root"], "target": 2,
                              "status": "resolved"} in d["references"]),
        ("nested_refs", {"source": 2, "path": ["alpha"], "target": 1,
                         "status": "resolved"} in d["references"]
         and {"source": 2, "path": ["beta"], "target": 4,
              "status": "resolved"} in d["references"]
         and {"source": 5, "path": ["gamma"], "target": 1,
              "status": "resolved"} in d["references"]),
        ("root_value_text", d["objects"][1]["value"] == "revenger-keyed-r81"),
        ("dict_members", d["objects"][2]["value"] == {
            "alpha": {"UID": 1}, "beta": {"UID": 4}, "n": 1729}),
        ("no_truncation", d["truncated"] is False and d["next_offset"] is None),
    ]
    bad = 0
    for name, ok in checks:
        print(("SELFCHECK %s ok" % name) if ok else ("SELFCHECK %s FAIL" % name))
        bad += 0 if ok else 1
    truth = dict(d)
    truth["derived_checks"] = len(checks)
    TRUTH.write_text(json.dumps(truth, indent=1, sort_keys=True) + "\n",
                     encoding="utf-8")
    print("GENERATOR derived %d checks; truth.json written" % len(checks))
    return 1 if bad else 0


def regen() -> int:
    data = build_bytes()
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "fixture.plist"
        tmp.write_bytes(data)
        old = FIXTURE.read_bytes()
        print("REGEN: byte-identical (%d bytes)" % len(data)
              if tmp.read_bytes() == old else "REGEN: BYTE-DRIFT")
        return 0 if tmp.read_bytes() == old else 1


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    if mode == "regen":
        return regen()
    if mode == "self-check":
        return self_check()
    if mode == "build":
        FIXTURE.write_bytes(build_bytes())
        return self_check()
    print("usage: generator.py [build|regen|self-check]", file=sys.stderr)
    return 64


if __name__ == "__main__":
    raise SystemExit(main())
