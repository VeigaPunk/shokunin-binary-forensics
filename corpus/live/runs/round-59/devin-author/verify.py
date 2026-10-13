#!/usr/bin/env python3
"""Author byte-oracle for the pe-r59d named-type fixture (round 59, devin host).

Independently decodes the PE32+ resource tree from fixture bytes, builds the
same normalized shape REA reports, and compares it to the saved
inspection.raw.json normalized_result plus receipt consistency. Then rejects
forged in-memory claims. Stdlib only; no REA rerun, no PE execution.
"""
from pathlib import Path
import copy, hashlib, json, struct

RUN = Path(__file__).resolve().parent
CORPUS = RUN.parents[3]
FIXTURE = CORPUS / "fixtures/pe-r59d/fixture.exe"
RAW = RUN / "inspection.raw.json"
RECEIPT = RUN / "receipt.json"
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = FIXTURE.read_bytes()
raw_bytes = RAW.read_bytes()
record = json.loads(raw_bytes)
receipt = json.loads(RECEIPT.read_text())

assert len(blob) == 1536
assert sha(blob) == "99bebcf14c462075e63d6504c97a45267063f33e05f215c1235f89d666b5c0f3"


def decode(b):
    u16 = lambda o: struct.unpack_from("<H", b, o)[0]
    u32 = lambda o: struct.unpack_from("<I", b, o)[0]
    assert b[:2] == b"MZ"
    pe = u32(0x3C)
    assert b[pe:pe + 4] == b"PE\0\0"
    machine, nsec = u16(pe + 4), u16(pe + 6)
    opt = pe + 24
    assert u16(opt) == 0x20B
    sections = []
    for i in range(nsec):
        s = opt + u16(pe + 20) + 40 * i
        sections.append((u32(s + 12), u32(s + 8), u32(s + 20), u32(s + 16)))

    def mapped(rva, size):
        m = [p + rva - v for v, vs, p, rs in sections
             if v <= rva and rva + size <= v + min(vs, rs)]
        assert len(m) == 1 and m[0] + size <= len(b)
        return m[0]

    dd = opt + 112 + 8 * 2
    root_rva, root_size = struct.unpack_from("<II", b, dd)
    base = mapped(root_rva, root_size)
    directories, resources = [], []

    def traverse(rel, path, entries):
        off = base + rel
        assert base <= off and off + 16 <= base + root_size
        f = struct.unpack_from("<IIHHHH", b, off)
        count = f[4] + f[5]
        assert off + 16 + 8 * count <= base + root_size
        directories.append(dict(location=dict(offset=off, bytes=16 + 8 * count),
                                characteristics=f[0], timestamp=f[1],
                                major_version=f[2], minor_version=f[3],
                                named_entries=f[4], id_entries=f[5]))
        # PE spec: named entries precede id entries inside one directory.
        seen_id = False
        for i in range(count):
            e = off + 16 + 8 * i
            key, target = struct.unpack_from("<II", b, e)
            if key & 0x80000000:
                assert not seen_id, "named entry after id entry"
                noff = base + (key & 0x7FFFFFFF)
                units = u16(noff)
                assert base <= noff and noff + 2 + 2 * units <= base + root_size
                enc = b[noff + 2:noff + 2 + 2 * units]
                ident = dict(kind="name", name=enc.decode("utf-16-le"),
                             utf16le_hex=enc.hex(),
                             location=dict(offset=noff, bytes=2 + 2 * units))
            else:
                seen_id = True
                ident = dict(kind="id", id=key)
            nxt = entries + [dict(offset=e, bytes=8)]
            if target & 0x80000000:
                assert len(path) < 2
                traverse(target & 0x7FFFFFFF, path + [ident], nxt)
            else:
                assert len(path) == 2
                de = base + target
                assert base <= de and de + 16 <= base + root_size
                prva, size, page, res = struct.unpack_from("<IIII", b, de)
                poff = mapped(prva, size)
                resources.append(dict(
                    index=len(resources), type=path[0], name=path[1], language=ident,
                    entry_locations=nxt,
                    data_entry_location=dict(offset=de, bytes=16),
                    code_page=page, reserved=res,
                    payload=dict(rva=prva, location=dict(offset=poff, bytes=size),
                                 sha256=sha(b[poff:poff + size]))))

    traverse(0, [], [])
    groups = []
    for res in resources:
        if res["type"] != dict(kind="id", id=14):
            continue
        loc = res["payload"]["location"]
        off, size = loc["offset"], loc["bytes"]
        reserved, kind, count = struct.unpack_from("<HHH", b, off)
        assert reserved == 0 and kind == 1 and 6 + 14 * count == size
        images = []
        for i in range(count):
            e = off + 6 + 14 * i
            w, h, c, pad, planes, bits, ln, rid = struct.unpack_from("<BBBBHHIH", b, e)
            cand = [r["index"] for r in resources
                    if r["type"] == dict(kind="id", id=3)
                    and r["name"] == dict(kind="id", id=rid)]
            same = next((j for j in cand if resources[j]["language"] == res["language"]), None)
            images.append(dict(location=dict(offset=e, bytes=14), width=w, height=h,
                               color_count=c, reserved=pad, planes=planes, bit_count=bits,
                               declared_bytes=ln, resource_id=rid,
                               candidate_resource_indices=cand,
                               same_language_resource_index=same,
                               size_matches=None if same is None else
                               resources[same]["payload"]["location"]["bytes"] == ln))
        groups.append(dict(resource_index=res["index"], images=images))
    return dict(format="pe32-plus", machine=machine,
                directory=dict(rva=root_rva, location=dict(offset=base, bytes=root_size),
                               data_directory_location=dict(offset=dd, bytes=8)),
                directories=directories, resources=resources, icon_groups=groups)


tree = decode(blob)
norm = record["normalized_result"]
checks = 0
for key in tree:
    assert tree[key] == norm[key], key
    checks += 1
# hard spot-asserts on the new named-type surface
leaf = tree["resources"][0]
assert leaf["type"] == dict(kind="name", name="REVTEST",
                            utf16le_hex="5200450056005400450053005400",
                            location=dict(offset=812, bytes=16))
assert leaf["name"] == dict(kind="id", id=1)
assert leaf["payload"] == dict(rva=8648, location=dict(offset=968, bytes=23),
                             sha256="d069b3846e5c7185f65263b6ca4e7a81670214b038f38805ed355f6c55191da6")
checks += 2
# icon-group relations intact and no false link onto the named-type leaf
imgs = tree["icon_groups"][0]["images"]
assert tree["icon_groups"][0]["resource_index"] == 3
assert [i["candidate_resource_indices"] for i in imgs] == [[1], [2]]
assert [i["same_language_resource_index"] for i in imgs] == [1, 2]
assert [i["size_matches"] for i in imgs] == [True, True]
assert all(0 not in i["candidate_resource_indices"] for i in imgs)
checks += 5
assert norm["artifact"] == dict(path=str(FIXTURE), sha256=sha(blob), bytes=len(blob))
assert norm["coverage"] == dict(status="complete", examined_entries=11, resources=4)
checks += 2
assert record["subject"]["digest"]["sha256"] == sha(blob)
assert record["operation"] == "inspect_pe_resources"
assert record["parameters"]["path"] == str(FIXTURE)
assert receipt["command"] == f"npx -y rea-agents@6.4.0 inspect-pe-resources {FIXTURE} --format json"
assert receipt["exit_code"] == 0
assert receipt["stdout_sha256"] == sha(raw_bytes)
assert receipt["fixture_sha256"] == sha(blob)
assert receipt["evidence_id"] == record["evidence_id"]
checks += 7

# forged-claim rejections on a deep copy of the byte-derived tree
rejected = 0
mut = copy.deepcopy(tree)
mut["icon_groups"][0]["images"][0]["candidate_resource_indices"] = [0]  # claim REVTEST leaf is icon candidate
try:
    assert mut["icon_groups"] == norm["icon_groups"]; raise SystemExit("forge passed")
except AssertionError:
    rejected += 1
mut = copy.deepcopy(tree)
mut["resources"][0]["type"] = dict(kind="id", id=24)  # claim leaf sat under numeric type
try:
    assert mut["resources"] == norm["resources"]; raise SystemExit("forge passed")
except AssertionError:
    rejected += 1
mut = copy.deepcopy(tree)
mut["resources"][0]["payload"]["sha256"] = sha(b"forged")  # claim wrong payload digest
try:
    assert mut["resources"] == norm["resources"]; raise SystemExit("forge passed")
except AssertionError:
    rejected += 1

print(f"PASS: {checks} positive checks; {rejected}/3 forged claims rejected "
      "(named-type leaf as icon candidate, numeric-type claim, payload digest). "
      "Limits: authored pe-r59d fixture, not general PE validation.")
