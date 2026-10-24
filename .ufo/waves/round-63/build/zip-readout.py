#!/usr/bin/env python3
"""Read archive-r2's ZIP structures directly from bytes and compare to truth.json."""
import hashlib
import json
import pathlib
import struct
import zlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
ARCHIVE = ROOT / "corpus/fixtures/archive-r2/fixture.zip"
TRUTH = ROOT / "corpus/fixtures/archive-r2/truth.json"


def u16(data, offset):
    return struct.unpack_from("<H", data, offset)[0]


def u32(data, offset):
    return struct.unpack_from("<I", data, offset)[0]


def find_eocd(data):
    signature = b"PK\x05\x06"
    earliest = max(0, len(data) - 22 - 0xFFFF)
    pos = len(data)
    while True:
        pos = data.rfind(signature, earliest, pos)
        if pos < 0:
            raise ValueError("EOCD record not found")
        if pos + 22 <= len(data) and pos + 22 + u16(data, pos + 20) == len(data):
            return pos


def decode_name(raw_name, flags):
    return raw_name.decode("utf-8" if flags & 0x0800 else "cp437")


def read_members(data, cd_offset, count):
    members = []
    pos = cd_offset
    for index in range(count):
        if data[pos:pos + 4] != b"PK\x01\x02":
            raise ValueError(f"central-directory record {index} has invalid signature at {pos}")
        flags = u16(data, pos + 8)
        method = u16(data, pos + 10)
        crc32 = u32(data, pos + 16)
        compressed_size = u32(data, pos + 20)
        uncompressed_size = u32(data, pos + 24)
        name_len = u16(data, pos + 28)
        extra_len = u16(data, pos + 30)
        comment_len = u16(data, pos + 32)
        local_offset = u32(data, pos + 42)
        name_bytes = data[pos + 46:pos + 46 + name_len]
        name = decode_name(name_bytes, flags)
        pos += 46 + name_len + extra_len + comment_len

        if data[local_offset:local_offset + 4] != b"PK\x03\x04":
            raise ValueError(f"{name}: local header has invalid signature at {local_offset}")
        local_flags = u16(data, local_offset + 6)
        local_method = u16(data, local_offset + 8)
        local_name_len = u16(data, local_offset + 26)
        local_extra_len = u16(data, local_offset + 28)
        local_name = data[local_offset + 30:local_offset + 30 + local_name_len]
        if local_name != name_bytes or local_method != method or local_flags != flags:
            raise ValueError(f"{name}: local and central header metadata disagree")
        payload_start = local_offset + 30 + local_name_len + local_extra_len
        payload_end = payload_start + compressed_size
        compressed = data[payload_start:payload_end]
        if len(compressed) != compressed_size:
            raise ValueError(f"{name}: compressed payload is truncated")
        if method == 8:
            uncompressed = zlib.decompress(compressed, -15)
        elif method == 0:
            uncompressed = compressed
        else:
            raise ValueError(f"{name}: unsupported ZIP compression method {method}")
        if len(uncompressed) != uncompressed_size:
            raise ValueError(f"{name}: inflated size does not match central-directory size")
        members.append({
            "name": name,
            "local_header_offset": local_offset,
            "compressed_size": compressed_size,
            "uncompressed_size": uncompressed_size,
            "crc32": crc32,
            "sha256": hashlib.sha256(uncompressed).hexdigest(),
        })
    return members, pos


def show_comparison(field, actual, expected):
    result = "N/A" if expected is None else str(actual == expected)
    expected_text = "<not recorded>" if expected is None else str(expected)
    print(f"{field:<48} | {str(actual):<72} | {expected_text:<72} | {result}")


def main():
    data = ARCHIVE.read_bytes()
    truth = json.loads(TRUTH.read_text(encoding="utf-8"))
    eocd = find_eocd(data)
    disk_number = u16(data, eocd + 4)
    central_disk = u16(data, eocd + 6)
    entries_on_disk = u16(data, eocd + 8)
    total_entries = u16(data, eocd + 10)
    central_size = u32(data, eocd + 12)
    central_offset = u32(data, eocd + 16)
    members, central_end = read_members(data, central_offset, total_entries)

    print(f"Archive: {ARCHIVE}")
    print(f"Archive size (bytes, from bytes): {len(data)}")
    print(f"Archive SHA-256 (from bytes): {hashlib.sha256(data).hexdigest()}")
    print(f"EOCD location (byte offset): {eocd}")
    print(f"EOCD disk number: {disk_number}")
    print(f"EOCD central-directory disk: {central_disk}")
    print(f"EOCD entries on this disk: {entries_on_disk}")
    print(f"EOCD total central-directory entries: {total_entries}")
    print(f"EOCD central-directory size: {central_size}")
    print(f"EOCD central-directory offset: {central_offset}")
    print(f"Central-directory records end at: {central_end}")
    print("Members (record fields read from central-directory bytes; SHA-256 from inflated local payload):")
    for member in members:
        print(
            "  "
            f"name={member['name']!r} "
            f"local_header_offset={member['local_header_offset']} "
            f"compressed_size={member['compressed_size']} "
            f"uncompressed_size={member['uncompressed_size']} "
            f"crc32=0x{member['crc32']:08x} "
            f"inflated_sha256={member['sha256']}"
        )

    truth_members = {member["path"]: member for member in truth["members"]}
    print("Comparison table (True/False against truth.json; N/A means truth.json has no corresponding field):")
    print(f"{'Field':<48} | {'Derived value':<72} | {'truth.json value':<72} | Match")
    print("-" * 201)
    show_comparison("archive_size", len(data), truth.get("archive_size"))
    show_comparison("archive_sha256", hashlib.sha256(data).hexdigest(), truth.get("archive_sha256"))
    show_comparison("eocd_location", eocd, None)
    show_comparison("eocd_disk_number", disk_number, None)
    show_comparison("eocd_central_directory_disk", central_disk, None)
    show_comparison("eocd_entries_on_disk", entries_on_disk, len(truth["members"]))
    show_comparison("eocd_total_entries", total_entries, len(truth["members"]))
    show_comparison("eocd_central_directory_size", central_size, None)
    show_comparison("eocd_central_directory_offset", central_offset, None)
    for member in members:
        expected = truth_members.get(member["name"])
        prefix = f"member[{member['name']}]"
        show_comparison(f"{prefix}.name", member["name"], expected.get("path") if expected else None)
        show_comparison(f"{prefix}.local_header_offset", member["local_header_offset"], None)
        show_comparison(f"{prefix}.compressed_size", member["compressed_size"], expected.get("compressed_size") if expected else None)
        show_comparison(f"{prefix}.uncompressed_size", member["uncompressed_size"], expected.get("size") if expected else None)
        show_comparison(f"{prefix}.crc32", f"0x{member['crc32']:08x}", None)
        show_comparison(f"{prefix}.inflated_sha256", member["sha256"], expected.get("sha256") if expected else None)


if __name__ == "__main__":
    main()
