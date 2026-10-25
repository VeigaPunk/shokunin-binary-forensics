#!/usr/bin/env python3
"""Build and verify the authored offline artifact for the bounty-triage exercise.

The artifact is one deterministic ZIP (ZIP_STORED, fixed member timestamps, sorted
names) that stands in for a program-provided client bundle.  It contains no live
endpoint and no real credential material; every host name uses the reserved
`.test` TLD.

Usage (from the lane root):

    python3 -B corpus/training/bounty-triage/fixtures/build_exercise.py
    python3 -B corpus/training/bounty-triage/fixtures/build_exercise.py --verify

Both modes rewrite `artifacts/client.zip` in the two exercise packages and
`truth.json`.  `--verify` additionally checks that every `scope.json` and
`report.md` digest still names the built bytes; a mismatch exits 1 and the
exercise text must be repaired, never the artifact silently regenerated into a
different digest.

Exit codes: 0 built/verified · 1 digest drift or unreadable package · 2 unreadable
truth/artifact · 64 usage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKAGES = (
    HERE / "exercise-r1" / "package",
    HERE / "exercise-r1-defective" / "package",
)
TRUTH = HERE / "truth.json"

MEMBERS = {
    "README.txt": (
        "Authored training fixture for the bounty-triage module.\n"
        "All host names use the reserved .test TLD; nothing here is live.\n"
    ),
    "config.json": (
        '{\n'
        '  "debug": true,\n'
        '  "telemetry_endpoint": "https://telemetry.example.test/collect",\n'
        '  "update_channel": "beta"\n'
        '}\n'
    ),
    "main.js": (
        'const { app } = require("electron");\n'
        'const API_BASE = "https://api.example.test/v1";\n'
        'app.whenReady().then(() => {\n'
        '  console.log("ready", API_BASE);\n'
        '});\n'
    ),
    "package.json": (
        '{\n'
        '  "name": "sample-client",\n'
        '  "version": "1.4.2",\n'
        '  "main": "main.js"\n'
        '}\n'
    ),
}


def build_bytes() -> bytes:
    """Return the artifact bytes; deterministic across runs and interpreters."""
    import io

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(MEMBERS):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o644 << 16
            info.create_system = 3
            archive.writestr(info, MEMBERS[name])
    return buf.getvalue()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args(argv)

    data = build_bytes()
    digest = sha256(data)

    for package in PACKAGES:
        target = package / "artifacts" / "client.zip"
        if not package.is_dir():
            print(f"missing package: {package}", file=sys.stderr)
            return 1
        target.parent.mkdir(parents=True, exist_ok=True)
        old = target.read_bytes() if target.is_file() else None
        target.write_bytes(data)
        state = "unchanged" if old == data else "written"
        print(f"{state}: {target.relative_to(HERE)} sha256={digest} size={len(data)}")

    truth = {
        "artifact": {
            "path": "artifacts/client.zip",
            "sha256": digest,
            "size": len(data),
        },
        "members": [
            {
                "name": name,
                "size": len(MEMBERS[name].encode("utf-8")),
                "sha256": sha256(MEMBERS[name].encode("utf-8")),
            }
            for name in sorted(MEMBERS)
        ],
        "build_recipe": {
            "command": "python3 -B corpus/training/bounty-triage/fixtures/build_exercise.py",
            "compression": "ZIP_STORED",
            "timestamps": "1980-01-01T00:00:00",
            "ordering": "sorted member names",
        },
    }
    TRUTH.write_text(json.dumps(truth, indent=2) + "\n", encoding="utf-8")
    print(f"written: {TRUTH.relative_to(HERE)}")

    if args.verify:
        failures = []
        for package in PACKAGES:
            scope = json.loads((package / "scope.json").read_text(encoding="utf-8"))
            declared = {a["path"]: a["sha256"] for a in scope.get("artifacts", [])}
            if declared.get("artifacts/client.zip") != digest:
                failures.append(
                    f"{package}/scope.json declares {declared.get('artifacts/client.zip')!r}"
                )
            report = (package / "report.md").read_text(encoding="utf-8")
            if digest not in report:
                failures.append(f"{package}/report.md does not name {digest}")
        if failures:
            for line in failures:
                print(f"drift: {line}", file=sys.stderr)
            print(f"VERDICT=FAIL built-digest={digest}", file=sys.stderr)
            return 1
        print(f"verified: 2 packages bind {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
