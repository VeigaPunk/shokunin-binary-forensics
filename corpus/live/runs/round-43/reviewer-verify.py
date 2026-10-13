from pathlib import Path
import hashlib, json, struct

C = Path("/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus")
P = C / "fixtures/pe-r43/fixture.exe"
B = C / "fixtures/pe-r42/fixture.exe"
R = C / "live/runs/round-43/inspection.raw.json"
Q = C / "live/runs/round-43/producer-receipt.json"
new, old = P.read_bytes(), B.read_bytes()
raw_bytes = R.read_bytes()
e = json.loads(raw_bytes)
receipt = json.loads(Q.read_bytes())
n = e["normalized_result"]
h = lambda data: hashlib.sha256(data).hexdigest()
U16 = lambda x, o: struct.unpack_from("<H", x, o)[0]
U32 = lambda x, o: struct.unpack_from("<I", x, o)[0]
loc = lambda o, size: {"offset": o, "bytes": size}
assert len(new) == len(old) == 1536
assert [(i, old[i], new[i]) for i in range(len(new)) if old[i] != new[i]] == [(928, 2, 3)]
assert h(new) == receipt["fixture_sha256"] == e["subject"]["digest"]["sha256"] == n["artifact"]["sha256"] == "146bdde3ec3ce9f23b75b31f7a9d2fc0cbc8826f2a5d239a83fd82694f4c31a2"
assert h(old) == "3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941"
assert h(raw_bytes) == receipt["stdout_sha256"]
assert receipt["exit_code"] == 0 and receipt["evidence_id"] == e["evidence_id"]
assert receipt["command"] == f"npx -y rea-agents@6.4.0 inspect-pe-resources {P} --format json"
assert e["operation"] == "inspect_pe_resources" and e["parameters"]["path"] == str(P)
assert e["subject"]["local_path"] == n["artifact"]["path"] == str(P)
assert n["artifact"]["bytes"] == len(new) and n["format"] == "pe32-plus"
assert new[:2] == b"MZ"
pe = U32(new, 0x3c)
assert new[pe:pe+4] == b"PE\0\0"
coff = pe + 4
machine, count = U16(new, coff), U16(new, coff+2)
opt = coff + 20
assert machine == n["machine"] == 0x8664 and count == 1
assert U16(new, opt) == 0x20b and U16(new, coff+16) == 240
assert U32(new, opt+108) >= 3  # NumberOfRvaAndSizes
section = opt + 240
assert new[section:section+8] == b".rsrc\0\0\0"
virtual_size, section_rva, section_raw_size, section_raw = (U32(new, section+i) for i in (8, 12, 16, 20))
assert (virtual_size, section_rva, section_raw_size, section_raw) == (1024, 8192, 1024, 512)
def file_offset(rva, size):
    assert section_rva <= rva and rva+size <= section_rva+min(virtual_size, section_raw_size)
    offset = section_raw + rva - section_rva
    assert offset+size <= len(new)
    return offset
dd = opt + 112 + 2*8
res_rva, res_size = U32(new, dd), U32(new, dd+4)
root = file_offset(res_rva, res_size)
assert (res_rva, res_size, root) == (8192, 208, 512)
assert n["directory"] == {"rva": res_rva, "location": loc(root, res_size), "data_directory_location": loc(dd, 8)}
seen = set()
directories, resources = [], []
def walk(rel, path, entry_locs):
    d = root + rel
    assert d not in seen and root <= d and d+16 <= root+res_size
    seen.add(d)
    characteristics, timestamp, major, minor, named, ids = struct.unpack_from("<IIHHHH", new, d)
    total = named + ids
    assert d+16+8*total <= root+res_size
    directories.append({"location": loc(d, 16+8*total), "characteristics": characteristics, "timestamp": timestamp,
                        "major_version": major, "minor_version": minor, "named_entries": named, "id_entries": ids})
    for i in range(total):
        entry = d+16+i*8
        name, target = struct.unpack_from("<II", new, entry)
        assert not name & 0x80000000 and i >= named  # this fixture has only numeric IDs
        ident = {"kind": "id", "id": name}
        if len(path) < 2:
            assert target & 0x80000000
            walk(target & 0x7fffffff, path+[ident], entry_locs+[loc(entry, 8)])
        else:
            assert len(path) == 2 and not target & 0x80000000
            data_entry = root+target
            assert root <= data_entry and data_entry+16 <= root+res_size
            rva, size, code_page, reserved = struct.unpack_from("<IIII", new, data_entry)
            payload_off = file_offset(rva, size)
            resources.append({"index": len(resources), "type": path[0], "name": path[1], "language": ident,
                              "entry_locations": entry_locs+[loc(entry, 8)], "data_entry_location": loc(data_entry, 16),
                              "code_page": code_page, "reserved": reserved,
                              "payload": {"rva": rva, "location": loc(payload_off, size), "sha256": h(new[payload_off:payload_off+size])}})
walk(0, [], [])
assert sorted(directories, key=lambda d: d["location"]["offset"]) == sorted(n["directories"], key=lambda d: d["location"]["offset"])
assert resources == n["resources"]
assert [tuple(z[k]["id"] for k in ("type", "name", "language")) for z in resources] == [(3,1,1033),(3,2,1033),(14,1,1033)]
assert [(d["location"]["offset"],d["location"]["bytes"]) for d in directories] == [(512,32),(544,32),(600,24),(624,24),(576,24),(648,24)]
assert [r["payload"]["location"] for r in resources] == [loc(768,48),loc(832,48),loc(896,34)]
assert [r["payload"]["sha256"] for r in resources] == ["d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003", "2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae", "672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d"]
group = resources[2]["payload"]["location"]
start, length = group["offset"], group["bytes"]
assert struct.unpack_from("<HHH", new, start) == (0,1,2) and length == 6+2*14
images = []
for i in range(2):
    o = start+6+14*i
    width,height,color,reserved,planes,bits,declared,rid = struct.unpack_from("<BBBBHHIH",new,o)
    candidates = [r["index"] for r in resources if r["type"]["id"] == 3 and r["name"]["id"] == rid]
    same = next((j for j in candidates if resources[j]["language"] == resources[2]["language"]),None)
    images.append({"location":loc(o,14), "width":width,"height":height,"color_count":color,"reserved":reserved,
                   "planes":planes,"bit_count":bits,"declared_bytes":declared,"resource_id":rid,
                   "candidate_resource_indices":candidates,"same_language_resource_index":same,
                   "size_matches": (resources[same]["payload"]["location"]["bytes"] == declared) if same is not None else None})
assert n["icon_groups"] == [{"resource_index":2,"images":images}]
assert [(z["resource_id"],z["candidate_resource_indices"],z["same_language_resource_index"],z["size_matches"]) for z in images] == [(1,[0],0,True),(3,[],None,None)]
assert n["coverage"] == {"status":"complete","examined_entries":8,"resources":3}
assert len(directories) == 6 and len(seen) == 6 and sum(d["named_entries"]+d["id_entries"] for d in directories) == 8
assert new[:896] == old[:896] and new[930:] == old[930:]
assert new[768:816] == old[768:816] and new[832:880] == old[832:880]
assert h(old[896:930]) == "45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a"
assert U16(old, 928) == 2 and U16(new,928) == 3
print("PASS: byte delta, PE map, all reachable directory entries, three leaves, group links, hashes, and receipt match")
