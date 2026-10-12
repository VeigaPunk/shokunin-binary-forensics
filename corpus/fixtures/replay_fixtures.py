#!/usr/bin/env python3
"""Rebuild the authored ZIP fixture from committed bytes in a caller-selected directory."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "checksum-r1" / "checksum"
TRUTH = ROOT / "archive-r2" / "truth.json"
README = b"Ground truth fixture: bin/checksum is the round-1 ELF; this manifest is plain text.\n"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new path for reconstructed ZIP, outside committed fixture")
    args = parser.parse_args()
    target = args.output.resolve()
    if target.exists():
        parser.error(f"output already exists: {target}")
    if not target.parent.is_dir():
        parser.error(f"output directory missing: {target.parent}")
    truth = json.loads(TRUTH.read_text())
    binary = SOURCE.read_bytes()
    if sha(binary) != truth["source_binary_sha256"]:
        parser.error("committed ELF differs from source digest")
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        info = zipfile.ZipInfo("bin/checksum", (2026, 10, 12, 13, 38, 30))
        info.create_system = 3
        info.external_attr = 0o100755 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, binary, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        info = zipfile.ZipInfo("README.txt", (2026, 10, 12, 13, 42, 38))
        info.create_system = 3
        info.external_attr = 0o600 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, README, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    rebuilt = target.read_bytes()
    print(f"sha256={sha(rebuilt)} size={len(rebuilt)} expected_sha256={truth['archive_sha256']}")
    if sha(rebuilt) != truth["archive_sha256"] or len(rebuilt) != truth["archive_size"]:
        raise SystemExit("archive byte-for-byte replay differs from committed truth")


if __name__ == "__main__":
    main()
