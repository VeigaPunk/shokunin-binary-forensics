#!/usr/bin/env python
"""ag_probe.py - round-82 coverage criterion A1 (registered mapping, frozen
before the r82 landing run).

A1 — artifact-graph operation record depth: how many of the rea-artifact-graph
provider's declared operations carry a real, oracle-checked producer record
under corpus/live/runs/round-*/.

The operation set is the provider's own declared group (S457, `rea
capabilities` 2026-11-01, group `available: true`, availability_code null):
  decode_interface_builder, inspect_keyed_archive, trace_dylib_resolution

An operation counts RECORDED iff some round dir carries BOTH
  (a) an inspection.json whose top-level `operation` equals the operation,
  (b) a receipt.json with exit_code == 0 and an oracle.result starting
      "ORACLE OK" (the identity-oracle gate; a record without a passing
      oracle receipt is not counted).
Byte-derived from the committed corpus only; no README, no K rows, no
knowledge admission is touched.

Denominator disclosure (pre-run, same shape as r79 F2 / r80 F3 / r81 F4):
A1 is a NEW instrument — its before-print exists only from this freeze
onward. On the base tree only inspect_keyed_archive is recorded: A1 prints
1/3 (3.33). Only a real current-producer record on a second operation moves
it to 2/3 (6.67). decode_interface_builder stays unrecorded (an .app-bundle
surface) — A1's honest exception is 2/3, not 3/3.

Usage:
  PYTHONUTF8=1 python -B ag_probe.py <tree>/corpus
"""
import json
import sys
from pathlib import Path

A1_OPS = [
    "decode_interface_builder",
    "inspect_keyed_archive",
    "trace_dylib_resolution",
]


def main() -> int:
    corpus = Path(sys.argv[1])
    runs = corpus / "live" / "runs"
    found = {op: None for op in A1_OPS}
    if runs.is_dir():
        for rd in sorted(runs.iterdir()):
            if not rd.is_dir():
                continue
            insp = rd / "inspection.json"
            rec = rd / "receipt.json"
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
                found[op] = rd.name
    recorded = 0
    for op in A1_OPS:
        state = found[op]
        print("A1_OP %s=%s" % (op, state if state else "unrecorded"))
        recorded += 1 if state else 0
    print("A1_RECORDED=%d/%d score=%.2f" % (recorded, len(A1_OPS),
                                            10.0 * recorded / len(A1_OPS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
