#!/usr/bin/env python
"""oracle_check.py - verify the saved producer record against the authored truth.

Usage: python -B oracle_check.py <truth.json> <record.json> <fixture.dll>
Exit 0 iff every producer-derived fact in the record equals the authored
premise it must derive from (identity oracle: the producer's own parser read
the authored bytes and reported exactly what was embedded).
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
    if len(sys.argv) != 4:
        print("usage: oracle_check.py <truth.json> <record.json> <fixture.dll>", file=sys.stderr)
        return 2
    truth = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    rec = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    fixture_sha = hashlib.sha256(Path(sys.argv[3]).read_bytes()).hexdigest()

    checks = []
    exp = truth["producer_expected"]
    checks.append(("operation", rec.get("operation"), exp["operation"]))
    norm = rec.get("normalized_result") or {}
    checks.append(("classification.status", dig(norm, "classification", "status"), exp["classification_status"]))
    checks.append(("classification.implementation", dig(norm, "classification", "implementation"), exp["implementation"]))
    checks.append(("module.name", dig(norm, "module", "name"), exp["module_name"]))
    checks.append(("assembly.name", dig(norm, "assembly", "name"), exp["assembly_name"]))
    checks.append(("assembly.version", str(dig(norm, "assembly", "version")), exp["assembly_version"]))
    streams = sorted(dig(norm, "metadata", "stream_names") or [])
    checks.append(("metadata.stream_names", streams, sorted(exp["stream_names"])))
    checks.append(("subject.sha256", dig(rec, "subject", "digest", "sha256"), fixture_sha))
    checks.append(("fixture.sha256==truth", fixture_sha, truth["sha256"]))
    checks.append(("evidence_id present", bool(rec.get("evidence_id")), True))

    ok = True
    for name, got, want in checks:
        good = got == want
        ok = ok and good
        print(f"{'OK ' if good else 'FAIL'} {name}: got={got!r}" + ("" if good else f" want={want!r}"))
    print(f"ORACLE {'OK' if ok else 'FAILED'} ({sum(1 for _, g, w in checks if g == w)}/{len(checks)} checks)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
