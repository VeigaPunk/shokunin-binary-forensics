# Round 48 independent PE resource review — PASS

A read-only, stdlib-only verifier decoded the PE32+ resource directory directly from the two fixture binaries; it did not use `truth.json` or execute REA or the PE. **PASS:** the binaries have equal length (1536 bytes) and differ at exactly file offset 664 (`0c` → `11`, changing the group-language ID 1036 → 1041). The type-3 RT_ICON/name-1 leaves remain at languages 1033 and 1036, with distinct, unchanged 48-byte payloads. The type-14 RT_GROUP_ICON/name-1 leaf has language 1041; its image ID 1 has candidates `[0, 1]` but no same-language leaf, so `same_language_resource_index` and `size_matches` are both `null`. The old group at language 1036 selected candidate 1, with a matching payload size. Reachable tree: 5 directories, exactly 7 directory entries and 3 leaves. Independently computed all tree entry/data/payload locations, payload hashes, and the normalized saved inventory; every compared field agrees.

- r47 fixture SHA-256: `cc02c78b44883f2217b7a8f82fa6fafc990ae6d0ca71f0eab8a3fbc4f2ba44ba`
- r48 fixture SHA-256: `dc6483a985f12dbc0da4122db64565ed76c14a5e76ea8758658b4a54c35bc129`
- Saved raw JSON byte SHA-256: `3a21b0e9ff72140360f72229810f0787265e07b86ec9af5148708128ade53325`
- Payload SHA-256 by resource index: 0 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`; 1 `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`; 2 `cc3745185dc1ae877dff5b3561df1162b7487fe78af6761a85649989979a3d01`.
- Receipt `fixture_sha256`, `stdout_sha256`, and `evidence_id` agree with the local fixture, saved raw JSON bytes, and raw record, respectively. The recorded command references the r48 fixture, and the recorded exit code is 0.

Run the following from any working directory; it reads the two fixtures and saved records and writes nothing:

```python
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
```

**Limits:** The receipt's command and exit code are saved assertions, not independently replayed proof of execution. The raw-file hash is compared to its receipt, but no independent producer transport or provenance is established. This static inspection does not determine operating-system language fallback, image decoding, or what icon a shell/window actually loads. Payloads other than the RT_GROUP_ICON descriptor are treated as opaque bytes.
