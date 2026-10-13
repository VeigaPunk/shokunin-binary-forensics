# Round 37 non-author LEAF review — PASS

I independently decoded the PE32 `.rsrc` directory from fixture bytes. The saved REA result matches the decoded directory and every leaf. The 1024-byte r36 and r37 fixtures differ at **exactly one byte**, file offset **850** (`01` → `02`), the little-endian group icon image ID. No other resource bytes changed.

| Resource type/name/language IDs | Payload offset / length | r37 payload SHA-256 |
|---|---:|---|
| RT_ICON 3 / 1 / 1033 | 768 / 48 | `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` |
| RT_GROUP_ICON 14 / 1 / 1033 | 832 / 20 | `3a05333329e38ad829edf1753f7e12de8a4ee0a9a63143d1da49203808ae6f76` |

The group's one image entry is at 838/14, 1×1, 32-bit, with **48 declared image bytes**. In r36 it referenced image ID 1: candidate resource `[0]`, same-language resource `0`, size match `true`. In r37 it references image ID **2**, while the sole RT_ICON still has name ID **1**: candidates `[]`, same-language match `null`, size match `null`. The absence is not a zero-byte or size-mismatch result; there is no image resource to compare. REA reports exactly those fields, both payload offsets/lengths/hashes, and complete coverage (6 examined entries, 2 leaves). There is no false icon-group relationship.

Receipt consistency: the r37 fixture SHA-256 is `917d909cbb205293dd3020e24d3c33b0d6b3cfed3553dd6fbc86b5a56f40dc85`; the **exact saved `inspection.raw.json` bytes including trailing newline** hash to `6e76c0dcb61a5adf4998ee25ddbee37cfc11ed3990627e6fbd7587ab8c850567`. Both match `producer-receipt.json`, whose evidence ID matches the saved result and whose recorded exit code is 0. These digest comparisons prove internal consistency only, **not origin authentication**, that the recorded command ran, or that its declared producer is trustworthy.

Limitations: static PE resource-table analysis only. The RT_ICON payload is opaque here; no image decoding, OS loader, language fallback, icon rendering, or actual shell/window behavior was observed. This tiny fixture and its two leaves do not establish parser behavior on arbitrary PEs. No PE was executed and no REA invocation was performed in this review.

## Exact rerunnable verification (Python standard library; reads only)

Run this block directly; it does not write files:

```sh
python - <<'PY'
from pathlib import Path
import hashlib, json, struct

base = Path("/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus")
prior = (base / "fixtures/pe-r36/fixture.exe").read_bytes()
current = (base / "fixtures/pe-r37/fixture.exe").read_bytes()
run = base / "live/runs/round-37"
raw = (run / "inspection.raw.json").read_bytes()
inspection = json.loads(raw)
receipt = json.loads((run / "producer-receipt.json").read_bytes())
sha = lambda blob: hashlib.sha256(blob).hexdigest()
U16 = lambda b, p: struct.unpack_from("<H", b, p)[0]
U32 = lambda b, p: struct.unpack_from("<I", b, p)[0]
loc = lambda offset, size: {"offset": offset, "bytes": size}

# Derive the resource RVA mapping from DOS, PE, optional header, and section headers.
def decode(b):
    assert b[:2] == b"MZ"
    pe = U32(b, 0x3c)
    assert b[pe:pe+4] == b"PE\0\0"
    machine, section_count, optional_size = U16(b, pe+4), U16(b, pe+6), U16(b, pe+20)
    opt = pe + 24
    magic = U16(b, opt)
    assert machine == 0x14c and magic == 0x10b and section_count == 1
    data_dir = opt + 96 + 2 * 8  # IMAGE_DIRECTORY_ENTRY_RESOURCE
    root_rva, root_size = struct.unpack_from("<II", b, data_dir)
    section = opt + optional_size
    assert b[section:section+8].rstrip(b"\0") == b".rsrc"
    virtual_size, section_rva, raw_size, raw_offset = struct.unpack_from("<IIII", b, section+8)
    assert section_rva <= root_rva and root_rva + root_size <= section_rva + virtual_size
    assert raw_offset + raw_size <= len(b)
    offset = lambda rva: raw_offset + rva - section_rva
    root = offset(root_rva)
    assert (root_rva, root_size, root, machine) == (8192, 160, 512, 332)
    dirs, leaves = [], []
    def walk(relative, levels, entries):
        pos = root + relative
        characteristics, stamp, major, minor, named, ids = struct.unpack_from("<IIHHHH", b, pos)
        assert (characteristics, stamp, major, minor, named) == (0, 0, 0, 0, 0)
        assert pos + 16 + 8 * (named + ids) <= root + root_size
        dirs.append({"location": loc(pos, 16 + 8 * (named + ids)),
                     "characteristics": characteristics, "timestamp": stamp,
                     "major_version": major, "minor_version": minor,
                     "named_entries": named, "id_entries": ids})
        for i in range(named + ids):
            ep = pos + 16 + 8*i
            key, target = struct.unpack_from("<II", b, ep)
            assert not key & 0x80000000  # all entries in this fixture are numeric IDs
            chain, points = levels + [key], entries + [loc(ep, 8)]
            if len(chain) < 3:
                assert target & 0x80000000
                walk(target & 0x7fffffff, chain, points)
            else:
                assert len(chain) == 3 and not target & 0x80000000
                dp = root + target
                assert dp + 16 <= root + root_size
                rva, count, code_page, reserved = struct.unpack_from("<IIII", b, dp)
                file_offset = offset(rva)
                assert raw_offset <= file_offset and file_offset + count <= raw_offset + raw_size
                blob = b[file_offset:file_offset+count]
                leaves.append({"index": len(leaves),
                               "type": {"kind": "id", "id": chain[0]},
                               "name": {"kind": "id", "id": chain[1]},
                               "language": {"kind": "id", "id": chain[2]},
                               "entry_locations": points,
                               "data_entry_location": loc(dp, 16),
                               "code_page": code_page, "reserved": reserved,
                               "payload": {"rva": rva, "location": loc(file_offset, count),
                                           "sha256": sha(blob)}})
    walk(0, [], [])
    groups = []
    for leaf in leaves:
        if leaf["type"]["id"] != 14:
            continue
        p = leaf["payload"]["location"]["offset"]
        end = p + leaf["payload"]["location"]["bytes"]
        reserved, kind, count = struct.unpack_from("<HHH", b, p)
        assert (reserved, kind) == (0, 1) and p + 6 + 14*count == end
        images = []
        for i in range(count):
            ep = p + 6 + 14*i
            width, height, colors, zero, planes, depth, size, image_id = struct.unpack_from("<BBBBHHIH", b, ep)
            candidates = [x["index"] for x in leaves if x["type"]["id"] == 3 and x["name"]["id"] == image_id]
            same_language = next((x["index"] for x in leaves if x["index"] in candidates and
                                  x["language"] == leaf["language"]), None)
            size_matches = None if same_language is None else (leaves[same_language]["payload"]["location"]["bytes"] == size)
            images.append({"location": loc(ep, 14), "width": width, "height": height,
                           "color_count": colors, "reserved": zero, "planes": planes,
                           "bit_count": depth, "declared_bytes": size, "resource_id": image_id,
                           "candidate_resource_indices": candidates,
                           "same_language_resource_index": same_language,
                           "size_matches": size_matches})
        groups.append({"resource_index": leaf["index"], "images": images})
    return {"directory": {"rva": root_rva, "location": loc(root, root_size),
                          "data_directory_location": loc(data_dir, 8)},
            "directories": dirs, "resources": leaves, "icon_groups": groups}

old, fresh = decode(prior), decode(current)
n = inspection["normalized_result"]
for field in ("directory", "directories", "resources", "icon_groups"):
    assert fresh[field] == n[field], field
assert (len(prior), len(current)) == (1024, 1024)
assert [(i, x, y) for i, (x, y) in enumerate(zip(prior, current)) if x != y] == [(850, 1, 2)]
assert [(x["type"]["id"], x["name"]["id"], x["language"]["id"],
         x["payload"]["location"], x["payload"]["sha256"]) for x in fresh["resources"]] == [
    (3, 1, 1033, loc(768, 48), "d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003"),
    (14, 1, 1033, loc(832, 20), "3a05333329e38ad829edf1753f7e12de8a4ee0a9a63143d1da49203808ae6f76")]
assert old["resources"][0] == fresh["resources"][0]
assert old["icon_groups"][0]["images"][0]["resource_id"] == 1
assert old["icon_groups"][0]["images"][0]["candidate_resource_indices"] == [0]
assert old["icon_groups"][0]["images"][0]["same_language_resource_index"] == 0
assert old["icon_groups"][0]["images"][0]["size_matches"] is True
assert old["icon_groups"][0]["images"][0]["declared_bytes"] == 48
assert fresh["icon_groups"][0]["images"][0]["resource_id"] == 2
assert fresh["icon_groups"][0]["images"][0]["declared_bytes"] == 48
assert fresh["icon_groups"][0]["images"][0]["candidate_resource_indices"] == []
assert fresh["icon_groups"][0]["images"][0]["same_language_resource_index"] is None
assert fresh["icon_groups"][0]["images"][0]["size_matches"] is None
assert n["coverage"] == {"status": "complete", "examined_entries": 6, "resources": 2}
assert n["artifact"]["sha256"] == inspection["subject"]["digest"]["sha256"] == sha(current)
assert n["artifact"]["bytes"] == len(current)
assert inspection["evidence_id"] == receipt["evidence_id"]
assert receipt["exit_code"] == 0
assert receipt["fixture_sha256"] == sha(current)
assert receipt["stdout_sha256"] == sha(raw)
print("PASS: static resources, baseline one-byte delta, REA result, receipt digests")
PY
```
