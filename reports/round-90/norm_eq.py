#!/usr/bin/env python3
"""Two-run normalized equality for inspect_android_package records (round-90 C2).

Usage:
    python3 -B norm_eq.py <run1.json> <run2.json>
    python3 -B norm_eq.py --selftest

Frozen volatile set (declared before any round-90 producer run; the round-89
receipt `reports/round-89/rejected-android-record/receipt.json` measured it):
  V1 the record's `evidence_id` value, wherever it appears as a whole string;
  V2 the per-run private runtime directory: any path prefix ending in
     `/rea-android-<suffix>` is rewritten to `<RUNTIME>/rea-android-X`;
  V3 key order inside JSON payloads that the producer carries as text strings
     (every string that parses as a JSON object/array is canonicalised);
  V4 the key `load_duration_ms` (a wall-clock measurement), at any depth.
Nothing else is normalised. Any other difference is a reproducibility failure.

Prints `NORM_EQ=identical` (exit 0) or `NORM_EQ=DIFFER` followed by one
`DIFF <json-path>` line per differing leaf (exit 1). Exit 2 on a missing or
unparseable input, 64 on usage. Read-only.
"""
import json
import re
import sys
from pathlib import Path

RUNTIME = re.compile(r"[^\"\s]*/rea-android-[A-Za-z0-9_]+")
DROP_KEYS = {"load_duration_ms"}


def norm(x, evid):
    if isinstance(x, dict):
        return {k: norm(v, evid) for k, v in sorted(x.items()) if k not in DROP_KEYS}
    if isinstance(x, list):
        return [norm(v, evid) for v in x]
    if isinstance(x, str):
        if evid and x == evid:
            return "<EVIDENCE_ID>"
        s = x.strip()
        if s[:1] in "{[":
            try:
                return {"<json-text>": norm(json.loads(s), evid)}
            except ValueError:
                pass
        return RUNTIME.sub("<RUNTIME>/rea-android-X", x)
    return x


def diff(a, b, path="$"):
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            out += diff(a.get(k), b.get(k), f"{path}.{k}") if k in a and k in b else [f"{path}.{k}"]
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [path + "[len]"]
        out = []
        for i, (p, q) in enumerate(zip(a, b)):
            out += diff(p, q, f"{path}[{i}]")
        return out
    return [] if a == b else [path]


def compare(r1, r2):
    n1, n2 = norm(r1, r1.get("evidence_id")), norm(r2, r2.get("evidence_id"))
    return diff(n1, n2)


def selftest():
    base = {"evidence_id": "ev_" + "a" * 64, "links": ["ev_" + "a" * 64],
            "p": "/s/x/rea-android-ab12cd/target.apk",
            "t": json.dumps({"x": 1, "y": 2, "load_duration_ms": 170}), "n": {"package_name": "com.example.r65"}}
    twin = {"evidence_id": "ev_" + "b" * 64, "links": ["ev_" + "b" * 64],
            "p": "/s/x/rea-android-zz99yy/target.apk",
            "t": json.dumps({"load_duration_ms": 175, "y": 2, "x": 1}), "n": {"package_name": "com.example.r65"}}
    legs = [("volatile-only twin", compare(base, twin), 0),
            ("non-volatile leaf changed", compare(base, {**twin, "n": {"package_name": "com.other"}}), 1),
            ("non-volatile text payload value", compare(base, {**twin, "t": json.dumps({"x": 9, "y": 2})}), 1),
            ("extra key", compare(base, {**twin, "extra": 1}), 1),
            ("evidence id leaks into a non-whole string", compare(
                {**base, "q": "see " + base["evidence_id"]}, {**twin, "q": "see " + twin["evidence_id"]}), 1)]
    bad = [(name, got) for name, got, want in legs if (len(got) > 0) != bool(want)]
    for name, got, want in legs:
        print(f"NORM_SELFTEST_{name.replace(' ', '_')}={'ok' if (len(got) > 0) == bool(want) else 'FAIL'}")
    print("NORM_SELFTEST=" + ("pass" if not bad else "FAIL"))
    return 0 if not bad else 1


def main(argv):
    if argv[1:] == ["--selftest"]:
        return selftest()
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 64
    try:
        r1, r2 = (json.loads(Path(p).read_text(encoding="utf-8")) for p in argv[1:])
    except (OSError, ValueError) as e:
        print(f"unreadable input: {e}", file=sys.stderr)
        return 2
    d = compare(r1, r2)
    if not d:
        print("NORM_EQ=identical")
        return 0
    print("NORM_EQ=DIFFER")
    for p in d:
        print("DIFF " + p)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
