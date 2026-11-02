#!/usr/bin/env python
"""ag_probe2.py - round-84 coverage criterion A1v2 (registered mapping
revision, frozen before the r84 landing runs). Supersedes the r82 A1
mapping (`reports/round-82/ag_probe.py`, which stays byte-untouched and
frozen) by extending the denominator to the rea-artifact-graph provider's
FULL available-operation set.

A1v2 - artifact-graph operation record depth (full available set): how
many of the provider's declared available operations carry a real,
oracle-checked producer record under corpus/live/runs/round-*/.

The operation set is the provider's own declared availability (S466,
`rea capabilities` 2026-11-02, provider `rea-artifact-graph`):
  available: true, availability_code null (5):
    decode_interface_builder, inspect_keyed_archive,
    trace_dylib_resolution, extract_artifact, inspect_artifact
  available: false, availability_code unsupported_host (1):
    inspect_asset_catalog ("Apple asset catalogs require macOS
    assetutil") - EXCLUDED: not runnable on this host.
The r82 registration counted the first group's no-effects triple only;
the r82/r83 records left the archive-side pair (extract_artifact,
inspect_artifact) "available-but-unrecorded" (r81/r82 scorecard note).
A1v2 counts all five. Denominator disclosure (pre-run, same shape as
r79 F2 / r80 F3 / r81 F4 / r82 A1): on the round base only the triple
is recorded, so A1v2 prints 3/5 (6.00). Only real current-producer
records on the two archive-side operations move it to 5/5 (10.00).

An operation counts RECORDED iff some round dir carries BOTH
  (a) an inspection.json whose top-level `operation` equals the
      operation,
  (b) a receipt.json with exit_code == 0 and an oracle.result starting
      "ORACLE OK" (the identity-oracle gate; a record without a passing
      oracle receipt is not counted).
Byte-derived from the committed corpus only; no README, no K rows, no
knowledge admission is touched.

Scan-shape revision v2.1 (pre-after-run correction, 2026-11-02): the
record round dir may nest operation subdirs; inspection.json is matched
by name at any depth under corpus/live/runs/ (rglob). v2.0's one-level
scan (frozen sha 6e1c07b568d982331c8ce17e9bdb659178066a68d2f44fa1e1e51fec8a71d1e1)
never saw runs/round-84/<operation>/inspection.json - caught by the
c1-only separability dry-run printing 3/5 against landed records; no
after-run receipt existed yet; red re-run as ag2-red-v21.log (3/5,
unchanged values). See the erratum in reports/round-84/claims.md.

Usage:
  PYTHONUTF8=1 python -B ag_probe2.py <tree>/corpus
"""
import json
import sys
from pathlib import Path

A1V2_OPS = [
    "decode_interface_builder",
    "inspect_keyed_archive",
    "trace_dylib_resolution",
    "extract_artifact",
    "inspect_artifact",
]


def main() -> int:
    corpus = Path(sys.argv[1])
    runs = corpus / "live" / "runs"
    found = {op: None for op in A1V2_OPS}
    if runs.is_dir():
        # r84 v2.1 scan shape: records may sit one level below the round dir
        # (runs/round-84/<operation>/inspection.json). The freeze-time v2.0
        # scanned runs/round-*/ directly only, which never sees the r84
        # layout; the c1-only separability dry-run exposed this BEFORE any
        # after-run receipt existed and the instrument was corrected
        # (erratum in claims.md; rglob matches inspection.json by NAME at
        # any depth, so the round-1-era artifact-inspection.json files are
        # still not matched).
        for insp in sorted(runs.rglob("inspection.json")):
            rec = insp.parent / "receipt.json"
            if not (insp.is_file() and rec.is_file()):
                continue
            try:
                record = json.loads(insp.read_text(encoding="utf-8"))
                receipt = json.loads(rec.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError, OSError):
                continue
            if not isinstance(record, dict) or not isinstance(receipt, dict):
                continue
            op = record.get("operation")
            oracle_field = receipt.get("oracle")
            oracle_result = (oracle_field.get("result", "")
                             if isinstance(oracle_field, dict) else "")
            oracle_ok = str(oracle_result).startswith(
                "ORACLE OK") and receipt.get("exit_code") == 0
            if op in found and found[op] is None and oracle_ok:
                found[op] = insp.parent.name
    recorded = 0
    for op in A1V2_OPS:
        state = found[op]
        print("A1V2_OP %s=%s" % (op, state if state else "unrecorded"))
        recorded += 1 if state else 0
    print("A1V2_RECORDED=%d/%d score=%.2f" % (recorded, len(A1V2_OPS),
                                              10.0 * recorded / len(A1V2_OPS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
