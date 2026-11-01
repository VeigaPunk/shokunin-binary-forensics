#!/usr/bin/env python
"""f_probe.py - frozen F predicate (round-76 instrument, predicate unchanged).

The F criterion and its predicate are unchanged from the SCORECARD F command
and reports/round-71/measure.py F block (families dict byte-equal to
measure.py:161). This revision exists only to give round-76 a runnable,
committed counting instrument on this host; it changes no family, no record
predicate, and no score formula. No counter revision of the mapping was
needed or made: a real rea 6.8.0 record demonstrably carries the frozen
snake_case operation names (S445/S446).

Usage: python -B f_probe.py <corpus-dir>
Prints value lines only; exit 0 when the tree was scanned, 1 on usage error.
"""
import collections
import json
import pathlib
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: f_probe.py <corpus-dir>", file=sys.stderr)
        return 1
    root = pathlib.Path(sys.argv[1])
    if not root.is_dir():
        print(f"not a dir: {root}", file=sys.stderr)
        return 1
    counter = collections.Counter()
    for p in sorted((root / "live" / "runs").rglob("*.json")):
        try:
            x = json.loads(p.read_bytes())
        except (ValueError, UnicodeError, OSError):
            continue
        if isinstance(x, dict) and x.get("evidence_id") and x.get("normalized_result") is not None:
            counter[x.get("operation", "unknown")] += 1
    families = {"native-static": {"inspect_pe_resources"}, "managed": {"inspect_managed_artifact"},
                "javascript": {"analyze_javascript_application"}, "android": {"inspect_android_package"},
                "archives": {"inventory_artifact", "inspect_artifact"}, "firmware": {"inspect_firmware_regions"},
                "browser-runtime": {"inspect_web_page", "capture_browser_scenario", "observe_web_session"},
                "evm": {"inspect_evm_interface"}}
    present = [k for k, v in families.items() if v.intersection(counter)]
    print(json.dumps(dict(sorted(counter.items())), sort_keys=True))
    print(f"F_COVERAGE={len(present)}/{len(families)} score={10 * len(present) / len(families):.2f}")
    print(f"F_FAMILIES={sorted(present)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
