#!/usr/bin/env python
"""mg_probe.py - round-85 coverage criterion M (registered mapping, frozen
before the r85 landing runs). New bounded criterion for the rea-dotnet-static
provider, extending the r82 A1 / r84 A1v2 registration pattern to the managed
side: how many of the provider's declared available operations carry a real,
oracle-checked producer record under corpus/live/runs/round-*/.

The operation set is the provider's own declared availability (S469,
`rea capabilities` 2026-11-02, provider `rea-dotnet-static`):
  available: true, availability_code null (3):
    inspect_managed_artifact, inspect_managed_members,
    inspect_managed_native_boundaries
The provider declares no unsupported operations (unlike
rea-artifact-graph's inspect_asset_catalog). The r76 record covered
inspect_managed_artifact only; the members/boundaries pair was
"available-but-unrecorded" through r84 (same shape r81/r82 named for the
archive-side pair). M counts all three. Denominator disclosure (pre-run,
same shape as r79 F2 / r80 F3 / r81 F4 / r82 A1 / r84 A1v2): on the round
base only inspect_managed_artifact is recorded, so M prints 1/3 (3.33).
Only real current-producer records on the members/boundaries pair move it
to 3/3 (10.00).

An operation counts RECORDED iff some round dir carries BOTH
  (a) an inspection.json whose top-level `operation` equals the
      operation,
  (b) a receipt.json with exit_code == 0 and an oracle.result starting
      "ORACLE OK" (the identity-oracle gate; a record without a passing
      oracle receipt is not counted).
Scan shape: rglob inspection.json by NAME at any depth under
corpus/live/runs/ (the r84 v2.1 correction is the starting shape here -
the round-1-era artifact-inspection.json files are not matched).
Byte-derived from the committed corpus only; no README, no K rows, no
knowledge admission is touched.

Usage:
  PYTHONUTF8=1 python -B mg_probe.py <tree>/corpus
"""
import json
import sys
from pathlib import Path

M_OPS = [
    "inspect_managed_artifact",
    "inspect_managed_members",
    "inspect_managed_native_boundaries",
]


def main() -> int:
    corpus = Path(sys.argv[1])
    runs = corpus / "live" / "runs"
    found = {op: None for op in M_OPS}
    if runs.is_dir():
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
    for op in M_OPS:
        state = found[op]
        print("M_OP %s=%s" % (op, state if state else "unrecorded"))
        recorded += 1 if state else 0
    print("M_RECORDED=%d/%d score=%.2f" % (recorded, len(M_OPS),
                                           10.0 * recorded / len(M_OPS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
