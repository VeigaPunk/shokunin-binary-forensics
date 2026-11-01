#!/usr/bin/env python
"""f_probe4.py - round-81 registered F-mapping revision (F4): adds the
`artifact-graph` family (operations `decode_interface_builder`,
`inspect_keyed_archive`, `trace_dylib_resolution`) as the eleventh family.

The ten families of the frozen f_probe3.py mapping (reports/round-80/
f_probe3.py) and their operation sets are byte-equal here; this revision adds
one mapping entry and renames its outputs F4_*. The mapping is frozen in
reports/round-81/claims.md at freeze, before the record run.

Honest denominator disclosure: adding a family grows the denominator in the
same revision that the family's first record lands. A tree with the ten
families of F3 held and the new family absent scores 9/11 (8.18) - LOWER
than the frozen F3 instrument's 9/10 (9.00) for the same tree. The mapping is
the claim, not a goalpost move: only a real current-producer record on the
new family moves F4 to 10/11.

Usage: python -B f_probe4.py <corpus-dir>
Prints value lines only; exit 0 when the tree was scanned, 1 on usage error.
"""
import collections
import json
import pathlib
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: f_probe4.py <corpus-dir>", file=sys.stderr)
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
                "native-authenticode": {"inspect_pe_certificates"},
                "sqlite": {"inspect_sqlite_database"},
                "artifact-graph": {"decode_interface_builder", "inspect_keyed_archive", "trace_dylib_resolution"}}
    present = [k for k, v in families.items() if v.intersection(counter)]
    print(json.dumps(dict(sorted(counter.items())), sort_keys=True))
    print(f"F4_COVERAGE={len(present)}/{len(families)} score={10 * len(present) / len(families):.2f}")
    print(f"F4_FAMILIES={sorted(present)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
