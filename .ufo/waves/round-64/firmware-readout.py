#!/usr/bin/env python3
"""Derive firmware fixture byte facts without consulting the truth record."""

import hashlib
from pathlib import Path
import struct
import zlib


FIXTURE = (
    Path(__file__).resolve().parents[3]
    / "corpus"
    / "fixtures"
    / "firmware-r63"
    / "firmware-r63.bin"
)


def zero_spans(data, member_ranges):
    """Return maximal half-open all-zero spans outside measured members."""
    spans = []
    cursor = 0
    range_index = 0
    while cursor < len(data):
        while (
            range_index < len(member_ranges)
            and cursor >= member_ranges[range_index][1]
        ):
            range_index += 1
        in_member = (
            range_index < len(member_ranges)
            and cursor >= member_ranges[range_index][0]
        )
        if data[cursor] != 0 or in_member:
            cursor += 1
            continue

        start = cursor
        while cursor < len(data):
            while (
                range_index < len(member_ranges)
                and cursor >= member_ranges[range_index][1]
            ):
                range_index += 1
            in_member = (
                range_index < len(member_ranges)
                and cursor >= member_ranges[range_index][0]
            )
            if data[cursor] != 0 or in_member:
                break
            cursor += 1
        spans.append((start, cursor))
    return spans


def scan_members(data):
    """Find valid 0x78 zlib headers whose streams reach EOF."""
    members = []
    for offset in range(len(data) - 1):
        cmf, flg = struct.unpack_from(">BB", data, offset)
        if cmf != 0x78 or ((cmf << 8) | flg) % 31 != 0 or (cmf & 0x0F) != 8:
            continue

        suffix = data[offset:]
        decoder = zlib.decompressobj()
        try:
            decoded = decoder.decompress(suffix)
            decoded += decoder.flush()
        except zlib.error:
            continue
        if not decoder.eof:
            continue

        compressed_size = len(suffix) - len(decoder.unused_data)
        members.append((offset, cmf, flg, compressed_size, decoded))
    return members

def main():
    image = FIXTURE.read_bytes()
    image_digest = hashlib.sha256(image).hexdigest()
    members = scan_members(image)
    member_ranges = [
        (offset, offset + compressed_size)
        for offset, _cmf, _flg, compressed_size, _decoded in members
    ]
    spans = zero_spans(image, member_ranges)

    print(
        f"image: size={len(image)} bytes (len(image)); "
        f"sha256={image_digest} (hashlib.sha256(image).hexdigest())"
    )
    print(
        "padding spans: maximal contiguous all-zero runs outside measured "
        "zlib-member extents;"
    )
    for start, end in spans:
        print(f"  ({start}, {end}) [half-open; end is first non-padding offset]")

    for offset, cmf, flg, compressed_size, decoded in members:
        suffix_size = len(image[offset:])
        unused_size = suffix_size - compressed_size
        print(
            f"zlib member: offset={offset} (all-offset scan found valid "
            f"header=0x{cmf:02x} 0x{flg:02x}); "
            f"compressed_size={compressed_size} bytes "
            f"(suffix length {suffix_size} minus {unused_size} "
            f"trailing unused bytes through EOF); "
            f"decompressed_size={len(decoded)} bytes (len(decoded)); "
            f"decompressed_sha256={hashlib.sha256(decoded).hexdigest()} "
            f"(hashlib.sha256(decoded).hexdigest())"
        )

if __name__ == "__main__":
    main()
