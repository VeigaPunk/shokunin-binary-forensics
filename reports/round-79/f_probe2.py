#!/usr/bin/env python
"""f_probe2.py - round-79 registered F-mapping revision (F2): adds the
`native-authenticode` family (operation `inspect_pe_certificates`) as the
ninth family.

The eight round-1 families and their operation sets are byte-equal to the
frozen f_probe.py mapping (reports/round-76/f_probe.py, predicate unchanged
from the SCORECARD F command and reports/round-71/measure.py F block); this
revision adds one mapping entry and renames its outputs F2_*. The mapping is
frozen in reports/round-79/claims.md at freeze, before the record run.

Honest denominator disclosure: adding a family grows the denominator in the
same revision that the family's first record lands. A tree with the eight
old families held and the new family absent scores 7/9 (7.78) - LOWER than
the frozen instrument's 7/8 (8.75) for the same tree. The mapping is the
claim, not a goalpost move: only a real current-producer record on the new
family moves F2 to 8/9.

Usage: python -B f_probe2.py <corpus-dir>
Prints value lines only; exit 0 when the tree was scanned, 1 on usage error.
"""
import collections
import json
import pathlib
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: f_probe2.py <corpus-dir>", file=sys.stderr)
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
                "evm": {"inspect_evm_interface"},
                "native-authenticode": {"inspect_pe_certificates"}}
    present = [k for k, v in families.items() if v.intersection(counter)]
    print(json.dumps(dict(sorted(counter.items())), sort_keys=True))
    print(f"F2_COVERAGE={len(present)}/{len(families)} score={10 * len(present) / len(families):.2f}")
    print(f"F2_FAMILIES={sorted(present)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
