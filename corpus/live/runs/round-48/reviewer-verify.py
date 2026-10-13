from pathlib import Path
import hashlib, json, struct
B = Path("/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus")
old = B / "fixtures/pe-r47/fixture.exe"
new = B / "fixtures/pe-r48/fixture.exe"
run = B / "live/runs/round-48"
raw_file, receipt_file = run / "inspection.raw.json", run / "producer-receipt.json"
sha = lambda b: hashlib.sha256(b).hexdigest()
loc = lambda offset, size: {"offset": offset, "bytes": size}
def decode(p):
    b = p.read_bytes()
    u16 = lambda o: struct.unpack_from("<H", b, o)[0]
    u32 = lambda o: struct.unpack_from("<I", b, o)[0]
    assert b[:2] == b"MZ"
    pe = u32(0x3c)
    assert b[pe:pe+4] == b"PE\0\0"
    machine, sections, optional_size = u16(pe+4), u16(pe+6), u16(pe+20)
    op = pe + 24
    assert u16(op) == 0x20b and sections == 1 and machine == 0x8664
    data_dir = op + 112 + 2 * 8  # PE32+ resource data directory
    root_rva, root_size = struct.unpack_from("<II", b, data_dir)
    sh = op + optional_size
    section_va, raw_size, raw_base = u32(sh+12), u32(sh+16), u32(sh+20)
    assert b[sh:sh+8].rstrip(b"\0") == b".rsrc"
    assert section_va <= root_rva and root_rva + root_size <= section_va + raw_size
    rva_to_file = lambda rva: raw_base + rva - section_va
    base = rva_to_file(root_rva)
    assert base + root_size <= len(b)
    dirs, leaves, entries = [], [], 0
    def walk(relative, path, entry_locs):
        nonlocal entries
        o = base + relative
        assert o + 16 <= base + root_size
        chars, stamp, major, minor, named, ids = struct.unpack_from("<IIHHHH", b, o)
        assert named == 0 and o + 16 + 8 * ids <= base + root_size
        dirs.append({"location": loc(o, 16+8*ids), "characteristics": chars,
                     "timestamp": stamp, "major_version": major,
                     "minor_version": minor, "named_entries": named, "id_entries": ids})
        for j in range(ids):
            eo = o + 16 + 8*j
            ident, target = struct.unpack_from("<II", b, eo)
            assert ident < 0x80000000
            entries += 1
            next_path, next_locs = path + [ident], entry_locs + [loc(eo, 8)]
            if target & 0x80000000:
                assert len(next_path) < 3
                walk(target & 0x7fffffff, next_path, next_locs)
            else:
                assert len(next_path) == 3
                de = base + target
                assert de + 16 <= base + root_size
                rva, size, code_page, reserved = struct.unpack_from("<IIII", b, de)
                payload_at = rva_to_file(rva)
                assert section_va <= rva and rva + size <= section_va + raw_size
                assert payload_at + size <= len(b)
                leaves.append({"index": len(leaves),
                    "type": {"kind": "id", "id": next_path[0]},
                    "name": {"kind": "id", "id": next_path[1]},
                    "language": {"kind": "id", "id": next_path[2]},
                    "entry_locations": next_locs,
                    "data_entry_location": loc(de, 16), "code_page": code_page,
                    "reserved": reserved, "payload": {"rva": rva,
                    "location": loc(payload_at, size), "sha256": sha(b[payload_at:payload_at+size])}})
    walk(0, [], [])
    groups = []
    for leaf in leaves:
        if leaf["type"]["id"] != 14: continue
        payload = leaf["payload"]["location"]
        at = payload["offset"]
        reserved, typ, count = struct.unpack_from("<HHH", b, at)
        assert reserved == 0 and typ == 1 and payload["bytes"] == 6 + count * 14
        images = []
        for j in range(count):
            o = at + 6 + 14*j
            width, height, colors, zero, planes, bits, size, image_id = struct.unpack_from("<BBBBHHIH", b, o)
            candidates = [x["index"] for x in leaves if x["type"]["id"] == 3 and x["name"]["id"] == image_id]
            same = next((i for i in candidates if leaves[i]["language"] == leaf["language"]), None)
            images.append({"location": loc(o, 14), "width": width, "height": height,
                "color_count": colors, "reserved": zero, "planes": planes,
                "bit_count": bits, "declared_bytes": size, "resource_id": image_id,
                "candidate_resource_indices": candidates,
                "same_language_resource_index": same,
                "size_matches": None if same is None else leaves[same]["payload"]["location"]["bytes"] == size})
        groups.append({"resource_index": leaf["index"], "images": images})
    return b, {"format": "pe32-plus", "machine": machine,
        "directory": {"rva": root_rva, "location": loc(base, root_size),
                      "data_directory_location": loc(data_dir, 8)},
        "directories": dirs, "resources": leaves, "icon_groups": groups,
        "coverage": {"status": "complete", "examined_entries": entries, "resources": len(leaves)}}
a, old_tree = decode(old)
b, tree = decode(new)
raw_bytes, receipt_bytes = raw_file.read_bytes(), receipt_file.read_bytes()
raw, receipt = json.loads(raw_bytes), json.loads(receipt_bytes)
assert len(a) == len(b) == 1536
assert [(i, a[i], b[i]) for i in range(len(b)) if a[i] != b[i]] == [(664, 12, 17)]
assert struct.unpack_from("<I", a, 664)[0] == 1036
assert struct.unpack_from("<I", b, 664)[0] == 1041
assert old_tree["resources"][2]["language"]["id"] == 1036
assert old_tree["icon_groups"][0]["images"][0]["candidate_resource_indices"] == [0,1]
assert old_tree["icon_groups"][0]["images"][0]["same_language_resource_index"] == 1
assert old_tree["icon_groups"][0]["images"][0]["size_matches"] is True
old_tree["resources"][2]["language"]["id"] = 1041
assert old_tree["resources"] == tree["resources"]
assert old_tree["directory"] == tree["directory"]
assert old_tree["directories"] == tree["directories"]
assert tree["coverage"] == {"status":"complete", "examined_entries":7, "resources":3}
assert [r["language"]["id"] for r in tree["resources"]] == [1033, 1036, 1041]
assert [(r["type"]["id"],r["name"]["id"]) for r in tree["resources"]] == [(3,1),(3,1),(14,1)]
icons = tree["resources"][:2]
assert [r["payload"]["location"]["bytes"] for r in icons] == [48,48]
assert icons[0]["payload"]["sha256"] != icons[1]["payload"]["sha256"]
assert tree["icon_groups"] == [{"resource_index":2, "images":[{
    "location":loc(902,14), "width":1,"height":1,"color_count":0,
    "reserved":0,"planes":1,"bit_count":32,"declared_bytes":48,
    "resource_id":1,"candidate_resource_indices":[0,1],
    "same_language_resource_index":None,"size_matches":None}]}]
normalized = raw["normalized_result"]
assert normalized["artifact"] == {"path":str(new),"sha256":sha(b),"bytes":len(b)}
for key, value in tree.items(): assert normalized[key] == value, key
assert raw["subject"]["local_path"] == raw["parameters"]["path"] == str(new)
assert raw["subject"]["digest"]["sha256"] == sha(b)
assert raw["locations"] == [{"kind":"artifact-path","path":str(new)}]
assert raw["evidence_id"] == receipt["evidence_id"]
assert receipt["fixture_sha256"] == sha(b)
assert receipt["stdout_sha256"] == sha(raw_bytes)
assert receipt["exit_code"] == 0
assert receipt["command"] == "npx -y rea-agents@6.4.0 inspect-pe-resources " + str(new) + " --format json"
print("PASS: independently decoded PE32+ resources; 7 entries, 3 leaves; all saved paths, offsets, sizes, hashes and receipt digests agree")
print("r47", sha(a), "r48", sha(b), "raw", sha(raw_bytes))
