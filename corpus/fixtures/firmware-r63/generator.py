#!/usr/bin/env python3
"""Build the inert round-63 raw firmware-region fixture deterministically.

The image contains only two zlib-wrapped text records and explicit zero padding;
no member is executable. `truth.json` region measurements are derived from the
finished image bytes, not copied from the layout declarations.
"""
import hashlib
import json
import platform
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE_PATH = HERE / "firmware-r63.bin"
TRUTH_PATH = HERE / "truth.json"
IMAGE_SIZE = 2048
PADDING_BYTE = b"\x00"
MEMBERS = (
    {
        "name": "diagnostic-note",
        "offset": 512,
        "payload": (
            b"R63 inert synthetic diagnostic record\n"
            b"sensor=pressure\nunits=kPa\nstate=nominal\n"
        ),
    },
    {
        "name": "component-note",
        "offset": 1024,
        "payload": (
            b"R63 inert synthetic component inventory\n"
            b"component=radio\nrevision=fixture-only\nexecution=disabled\n"
        ),
    },
)


def decode_member(image, offset):
    """Return the actual zlib member length and decompressed bytes at offset."""
    decoder = zlib.decompressobj()
    content = decoder.decompress(image[offset:])
    content += decoder.flush()
    if not decoder.eof:
        raise ValueError(f"incomplete zlib member at offset {offset}")
    member_size = len(image) - offset - len(decoder.unused_data)
    if member_size <= 0:
        raise ValueError(f"empty zlib member at offset {offset}")
    return member_size, content


def derive_regions(image):
    """Measure contiguous regions and member hashes from the finished bytes."""
    regions = []
    cursor = 0
    for spec in MEMBERS:
        offset = spec["offset"]
        if offset < cursor:
            raise ValueError(f"member {spec['name']} overlaps the preceding region")
        if offset > cursor:
            padding = image[cursor:offset]
            if padding != PADDING_BYTE * len(padding):
                raise ValueError(f"non-zero padding at offset {cursor}")
            regions.append({
                "offset": cursor,
                "size": len(padding),
                "kind": "padding",
                "fill_hex": PADDING_BYTE.hex(),
            })

        member_size, content = decode_member(image, offset)
        if content != spec["payload"]:
            raise ValueError(f"decompressed bytes differ for {spec['name']}")
        regions.append({
            "offset": offset,
            "size": member_size,
            "kind": "zlib",
            "name": spec["name"],
            "decompressed_member": {
                "sha256": hashlib.sha256(content).hexdigest(),
                "size": len(content),
            },
        })
        cursor = offset + member_size

    if cursor > len(image):
        raise ValueError("member extends beyond image")
    if cursor < len(image):
        padding = image[cursor:]
        if padding != PADDING_BYTE * len(padding):
            raise ValueError(f"non-zero trailing padding at offset {cursor}")
        regions.append({
            "offset": cursor,
            "size": len(padding),
            "kind": "padding",
            "fill_hex": PADDING_BYTE.hex(),
        })

    if sum(region["size"] for region in regions) != len(image):
        raise ValueError("region table does not cover the image exactly")
    return regions


def main():
    image = bytearray(PADDING_BYTE * IMAGE_SIZE)
    for spec in MEMBERS:
        compressed = zlib.compress(spec["payload"], level=9)
        end = spec["offset"] + len(compressed)
        if end > IMAGE_SIZE:
            raise ValueError(f"member {spec['name']} extends beyond image")
        image[spec["offset"]:end] = compressed

    image = bytes(image)
    regions = derive_regions(image)
    truth = {
        "image": {
            "path": IMAGE_PATH.name,
            "sha256": hashlib.sha256(image).hexdigest(),
            "size": len(image),
        },
        "regions": regions,
        "build_recipe": {
            "command": "python3 -B generator.py",
            "image_size": IMAGE_SIZE,
            "padding_byte_hex": PADDING_BYTE.hex(),
            "compression": {
                "format": "RFC 1950 zlib-wrapped DEFLATE",
                "implementation": "zlib.compress(payload, level=9)",
                "level": 9,
                "compile_version": zlib.ZLIB_VERSION,
                "runtime_version": zlib.ZLIB_RUNTIME_VERSION,
            },
            "python_version": platform.python_version(),
            "determinism": (
                "Fixed payloads, offsets, padding, and compression level; no timestamps "
                "or randomness. Byte-for-byte reproducible with the recorded Python/zlib "
                "versions."
            ),
            "members": [
                {
                    "name": spec["name"],
                    "offset": spec["offset"],
                    "payload_utf8": spec["payload"].decode("ascii"),
                }
                for spec in MEMBERS
            ],
        },
    }
    IMAGE_PATH.write_bytes(image)
    TRUTH_PATH.write_text(json.dumps(truth, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"wrote {IMAGE_PATH.name} sha256={truth['image']['sha256']} "
        f"size={truth['image']['size']}"
    )
    for region in regions:
        print(
            f"region offset={region['offset']} size={region['size']} "
            f"kind={region['kind']}"
        )


if __name__ == "__main__":
    main()
