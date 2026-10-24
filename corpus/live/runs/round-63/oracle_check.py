#!/usr/bin/env python3
"""Compare the round-63 REA firmware regions with the authored byte oracle."""
import argparse
import hashlib
import json
import sys
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_RECORD = HERE / "inspection.json"
DEFAULT_TRUTH = HERE.parents[3] / "corpus" / "fixtures" / "firmware-r63" / "truth.json"


def load_json(path, field, errors):
    try:
        with path.open(encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{field}: {exc}")
        return None


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


def mismatch(errors, field, detail):
    errors.append(f"{field}: {detail}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=DEFAULT_RECORD)
    parser.add_argument("--truth", type=Path, default=DEFAULT_TRUTH)
    args = parser.parse_args()
    errors = []
    record = load_json(args.record, "inspection.json", errors)
    truth = load_json(args.truth, "truth.json", errors)

    if not isinstance(record, dict):
        record = {}
    if not isinstance(truth, dict):
        truth = {}

    if record.get("operation") != "inspect_firmware_regions":
        mismatch(errors, "operation", "expected inspect_firmware_regions")
    subject = record.get("subject")
    digest = subject.get("digest") if isinstance(subject, dict) else None
    record_image_sha = digest.get("sha256") if isinstance(digest, dict) else None
    if not isinstance(record_image_sha, str):
        mismatch(errors, "subject.digest.sha256", "missing or not a string")

    result = record.get("normalized_result")
    if not isinstance(result, dict):
        mismatch(errors, "normalized_result", "missing or not an object")
        result = {}

    truth_regions = truth.get("regions")
    if not isinstance(truth_regions, list):
        mismatch(errors, "truth.regions", "missing or not an array")
        truth_regions = []
    reported_regions = result.get("regions")
    if not isinstance(reported_regions, list):
        mismatch(errors, "normalized_result.regions", "missing or not an array")
        reported_regions = []

    image_info = truth.get("image")
    image_bytes = None
    if not isinstance(image_info, dict):
        mismatch(errors, "truth.image", "missing or not an object")
    else:
        image_path_value = image_info.get("path")
        if not isinstance(image_path_value, str) or not image_path_value:
            mismatch(errors, "truth.image.path", "missing or not a path")
        else:
            image_path = Path(image_path_value)
            if not image_path.is_absolute():
                image_path = args.truth.resolve().parent / image_path
            try:
                image_bytes = image_path.read_bytes()
            except OSError as exc:
                mismatch(errors, "truth.image.path", str(exc))
        if image_bytes is not None:
            image_size = image_info.get("size")
            if not integer(image_size) or image_size != len(image_bytes):
                mismatch(errors, "truth.image.size", f"expected {image_size!r}, actual {len(image_bytes)}")
            expected_image_sha = image_info.get("sha256")
            actual_image_sha = hashlib.sha256(image_bytes).hexdigest()
            if not isinstance(expected_image_sha, str) or expected_image_sha != actual_image_sha:
                mismatch(errors, "truth.image.sha256", f"expected {expected_image_sha!r}, actual {actual_image_sha}")
            if record_image_sha != actual_image_sha:
                mismatch(errors, "subject.digest.sha256", f"expected {actual_image_sha}, got {record_image_sha!r}")
            input_size = result.get("input_size")
            if not integer(input_size) or input_size != len(image_bytes):
                mismatch(errors, "normalized_result.input_size", f"expected {len(image_bytes)}, got {input_size!r}")

    reportable = []
    spans = []
    region_results = {}
    for index, region in enumerate(truth_regions):
        field = f"truth.regions[{index}]"
        if not isinstance(region, dict):
            mismatch(errors, field, "not an object")
            region_results[index] = "invalid truth region"
            continue
        kind = region.get("kind")
        offset = region.get("offset")
        size = region.get("size")
        if not integer(offset):
            mismatch(errors, f"{field}.offset", "missing or not an integer")
        if not integer(size) or size <= 0:
            mismatch(errors, f"{field}.size", "missing or not a positive integer")
        if integer(offset) and integer(size) and size > 0:
            spans.append((offset, offset + size, index))
            in_bounds = image_bytes is not None and 0 <= offset <= len(image_bytes) and offset + size <= len(image_bytes)
            if image_bytes is not None and not in_bounds:
                mismatch(errors, field, "region is outside the image")
        else:
            in_bounds = False

        if kind == "padding":
            fill_hex = region.get("fill_hex")
            fill_ok = False
            if isinstance(fill_hex, str):
                try:
                    fill = bytes.fromhex(fill_hex)
                    if fill and in_bounds:
                        fill_ok = image_bytes[offset:offset + size] == (fill * ((size + len(fill) - 1) // len(fill)))[:size]
                except ValueError:
                    pass
            if not fill_ok:
                mismatch(errors, f"{field}.fill_hex", "padding bytes do not match the declared fill")
            region_results[index] = f"record=not-expected padding={'OK' if fill_ok else 'MISMATCH'}"
        elif kind in ("zlib", "gzip"):
            reportable.append((index, region))
            member = region.get("decompressed_member")
            member_sha = member.get("sha256") if isinstance(member, dict) else None
            member_size = member.get("size") if isinstance(member, dict) else None
            decompressed_sha = None
            decompressed_size = None
            complete = False
            if in_bounds:
                try:
                    wbits = zlib.MAX_WBITS if kind == "zlib" else zlib.MAX_WBITS | 16
                    decoder = zlib.decompressobj(wbits)
                    decompressed = decoder.decompress(image_bytes[offset:offset + size])
                    decompressed += decoder.flush()
                    complete = decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
                    decompressed_sha = hashlib.sha256(decompressed).hexdigest()
                    decompressed_size = len(decompressed)
                except zlib.error as exc:
                    mismatch(errors, f"{field}.decompressed_member", f"cannot decompress bytes: {exc}")
            hash_ok = isinstance(member_sha, str) and decompressed_sha == member_sha
            size_ok = integer(member_size) and decompressed_size == member_size
            if not complete:
                mismatch(errors, f"{field}.size", "compressed member does not end exactly at its declared size")
            if not hash_ok:
                mismatch(errors, f"{field}.decompressed_member.sha256", f"expected {member_sha!r}, actual {decompressed_sha!r}")
            if not size_ok:
                mismatch(errors, f"{field}.decompressed_member.size", f"expected {member_size!r}, actual {decompressed_size!r}")
            region_results[index] = (
                f"decompressed_sha256={'OK' if hash_ok else 'MISMATCH'}"
                + (f" ({decompressed_sha})" if decompressed_sha else "")
            )
        else:
            mismatch(errors, f"{field}.kind", f"unsupported region kind {kind!r}")
            region_results[index] = f"record=unsupported kind={kind!r}"

    spans.sort()
    cursor = 0
    for start, end, index in spans:
        if start != cursor:
            mismatch(errors, f"truth.regions[{index}].offset", f"expected contiguous start {cursor}, got {start}")
        cursor = end
    if image_bytes is not None and cursor != len(image_bytes):
        mismatch(errors, "truth.regions", f"regions end at {cursor}, image ends at {len(image_bytes)}")

    reportable.sort(key=lambda item: item[1].get("offset", -1) if integer(item[1].get("offset")) else -1)
    observed = sorted(
        enumerate(reported_regions),
        key=lambda item: item[1].get("offset", -1) if isinstance(item[1], dict) and integer(item[1].get("offset")) else -1,
    )
    if len(observed) != len(reportable):
        mismatch(errors, "normalized_result.regions", f"expected {len(reportable)} reportable regions, got {len(observed)}")

    paired = {}
    for position, (truth_index, truth_region) in enumerate(reportable):
        record_region = observed[position][1] if position < len(observed) else None
        if not isinstance(record_region, dict):
            paired[truth_index] = "record=MISSING offset=MISSING size=MISSING"
            mismatch(errors, f"normalized_result.regions[{position}]", "missing reported region")
            continue
        record_offset = record_region.get("offset")
        record_size = record_region.get("reported_size")
        offset_ok = integer(record_offset) and record_offset == truth_region.get("offset")
        size_ok = integer(record_size) and record_size == truth_region.get("size")
        kind_ok = record_region.get("signature") == truth_region.get("kind")
        if not offset_ok:
            mismatch(errors, f"normalized_result.regions[{position}].offset", f"expected {truth_region.get('offset')!r}, got {record_offset!r}")
        if not size_ok:
            mismatch(errors, f"normalized_result.regions[{position}].reported_size", f"expected {truth_region.get('size')!r}, got {record_size!r}")
        if not kind_ok:
            mismatch(errors, f"normalized_result.regions[{position}].signature", f"expected {truth_region.get('kind')!r}, got {record_region.get('signature')!r}")
        paired[truth_index] = (
            f"offset={'OK' if offset_ok else 'MISMATCH'} size={'OK' if size_ok else 'MISMATCH'} "
            f"signature={'OK' if kind_ok else 'MISMATCH'}"
        )

    for index, region in enumerate(truth_regions):
        if not isinstance(region, dict):
            print(f"REGION index={index} invalid={region_results[index]}")
            continue
        name = region.get("name", region.get("kind", "unknown"))
        offset = region.get("offset", "?")
        size = region.get("size", "?")
        check = region_results.get(index, "unverified")
        if index in paired:
            check = f"{paired[index]} {check}"
        print(f"REGION name={name} kind={region.get('kind')} offset={offset} size={size} {check}")

    for error in errors:
        print(f"MISMATCH {error}")
    print("ORACLE MISMATCH" if errors else "ORACLE OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
