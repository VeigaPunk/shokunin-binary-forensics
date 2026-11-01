#!/usr/bin/env python
"""oracle_check.py - verify the saved producer record against the authored truth.

Usage: python -B oracle_check.py <truth.json> <record.json> <fixture.dll>
Exit 0 iff every producer-derived fact in the record equals the authored
premise it must derive from (identity oracle: the producer's own parser read
the authored bytes and reported exactly what was embedded). Observation vs
inference: the record's fields are observations; the truth values are derived
from the authored bytes by generator.py's self-check (Q06).
"""
import hashlib
import json
import sys
from pathlib import Path


def dig(node, *path):
    for k in path:
        node = node[k]
    return node


def main() -> int:
    truth = json.loads(Path(sys.argv[1]).read_bytes())
    record = json.loads(Path(sys.argv[2]).read_bytes())
    fixture = Path(sys.argv[3]).read_bytes()
    exp = truth["producer_expected"]
    e0 = exp["entry0"]
    checks = []  # (name, ok)

    def ck(name, got, want):
        checks.append((name, got == want))
        if got != want:
            print(f"MISMATCH {name}: got {got!r} want {want!r}")

    ck("operation", record.get("operation"), exp["operation"])
    ck("evidence_id present", bool(record.get("evidence_id")), True)
    ck("provider_id", dig(record, "provider", "id"), exp["provider_id"])
    ck("fixture sha on disk", hashlib.sha256(fixture).hexdigest(),
       truth["sha256"])
    ck("subject sha256", dig(record, "subject", "digest", "sha256"),
       exp["subject_sha256"])
    ck("artifact bytes", dig(record, "normalized_result", "artifact", "bytes"),
       truth["byte_length"])
    ck("format", dig(record, "normalized_result", "format"), exp["format"])
    ck("machine", dig(record, "normalized_result", "machine"), exp["machine"])
    ck("table location",
       dig(record, "normalized_result", "table", "location"),
       exp["table_location"])
    ck("ddir slot location",
       dig(record, "normalized_result", "table", "data_directory_location"),
       exp["data_directory_location"])
    entries = dig(record, "normalized_result", "entries")
    ck("entry count", len(entries), exp["entry_count"])
    ent = entries[0]
    ck("entry0 length", ent["length"], e0["length"])
    ck("entry0 revision", ent["revision"], e0["revision"])
    ck("entry0 cert type", ent["certificate_type"], e0["certificate_type"])
    ck("entry0 cert type name", ent["certificate_type_name"],
       e0["certificate_type_name"])
    ck("entry0 payload location", ent["payload"]["location"],
       {"offset": e0["payload_offset"], "bytes": e0["payload_bytes"]})
    ck("entry0 payload sha256", ent["payload"]["sha256"], e0["payload_sha256"])
    pk = ent["pkcs7"]
    ck("content_type_oid", pk["content_type_oid"], e0["content_type_oid"])
    ck("digest_algorithm_oids", pk["digest_algorithm_oids"],
       e0["digest_algorithm_oids"])
    ck("signer count", len(pk["signers"]), e0["signer_count"])
    s0 = pk["signers"][0]
    for k in ("digest_algorithm_oid", "signature_algorithm_oid",
              "subject_key_identifier_hex", "issuer", "serial_hex",
              "authenticated_attributes"):
        ck(f"signer0 {k}", s0[k], e0["signer0"][k])
    ck("coverage", dig(record, "normalized_result", "coverage"),
       exp["coverage"])

    ok = sum(1 for _, good in checks if good)
    print(f"ORACLE {'OK' if ok == len(checks) else 'FAIL'} ({ok}/{len(checks)} checks)")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
