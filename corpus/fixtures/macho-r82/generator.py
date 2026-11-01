#!/usr/bin/env python
"""generator.py - round-82 Mach-O dylib-resolution fixture builder.

Builds an inert two-image Mach-O tree that exercises dyld load-path
resolution classes, then derives EVERY oracle-checked fact by re-parsing
the built bytes (Q06 discipline, SKILL.md section 2: the truth is derived
from the built bytes, never from intent and never from the producer's own
output).

Authored tree (built under image/):
  image/main.dylib                x86_64 MH_DYLIB, 5 load commands:
      LC_ID_DYLIB    @rpath/librevenger-r82.dylib
      LC_LOAD_DYLIB  @rpath/libalpha.dylib            (resolves via the rpath)
      LC_LOAD_DYLIB  @loader_path/../Frameworks/libbeta.dylib  (escapes root)
      LC_LOAD_DYLIB  /usr/lib/libSystem.B.dylib       (outside root)
      LC_RPATH       @loader_path/rpathdir
  image/rpathdir/libalpha.dylib   x86_64 MH_DYLIB leaf, 1 load command:
      LC_ID_DYLIB    @rpath/libalpha.dylib

The 6.8.0 trace-dylib-resolution parser REQUIRES every load command's
cmdsize to be a multiple of 8 in this 64-bit image (pre-probe: a 4-aligned
cmdsize 68 was rejected, code target_unavailable); the builder asserts
8-alignment for every command it emits.

Usage: python -B generator.py            # build image/ + truth.json
       python -B generator.py regen      # rebuild to a temp dir, byte-compare
       python -B generator.py self-check # derive truth from built bytes
"""
import hashlib
import json
import struct
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "image"
MAIN = IMAGE / "main.dylib"
ALPHA = IMAGE / "rpathdir" / "libalpha.dylib"
TRUTH = HERE / "truth.json"

MH_MAGIC_64 = 0xFEEDFACF
CPU_TYPE_X86_64 = 0x01000007
CPU_SUBTYPE_X86_64_ALL = 0x00000003
MH_DYLIB = 0x6
LC_LOAD_DYLIB = 0xC
LC_ID_DYLIB = 0xD
LC_RPATH = 0x8000001C  # LC_REQ_DYLD | LC_RPATH
VERSION_1_0_0 = 0x10000
TIMESTAMP = 2


def align8(n: int) -> int:
    """The 6.8.0 trace-dylib-resolution parser rejects a cmdsize that is not
    a multiple of 8 in a 64-bit image (pre-probe receipt, cmdsize 68)."""
    return (n + 7) & ~7


def dylib_cmd(cmd: int, name: str) -> bytes:
    name_b = name.encode("ascii") + b"\x00"
    cmdsize = align8(24 + len(name_b))
    body = struct.pack("<IiIIII", cmd, cmdsize, 24, TIMESTAMP,
                       VERSION_1_0_0, VERSION_1_0_0)
    body += name_b + b"\x00" * (cmdsize - 24 - len(name_b))
    assert len(body) == cmdsize
    return body


def rpath_cmd(path: str) -> bytes:
    # rpath_command: cmd(4), cmdsize(4), path.offset(4) = 12-byte header
    path_b = path.encode("ascii") + b"\x00"
    cmdsize = align8(12 + len(path_b))
    body = struct.pack("<IiI", LC_RPATH, cmdsize, 12)
    body += path_b + b"\x00" * (cmdsize - 12 - len(path_b))
    assert len(body) == cmdsize
    return body


MAIN_CMDS = [
    ("LC_ID_DYLIB", dylib_cmd(LC_ID_DYLIB, "@rpath/librevenger-r82.dylib")),
    ("LC_LOAD_DYLIB", dylib_cmd(LC_LOAD_DYLIB, "@rpath/libalpha.dylib")),
    ("LC_LOAD_DYLIB", dylib_cmd(LC_LOAD_DYLIB, "@loader_path/../Frameworks/libbeta.dylib")),
    ("LC_LOAD_DYLIB", dylib_cmd(LC_LOAD_DYLIB, "/usr/lib/libSystem.B.dylib")),
    ("LC_RPATH", rpath_cmd("@loader_path/rpathdir")),
]
ALPHA_CMDS = [("LC_ID_DYLIB", dylib_cmd(LC_ID_DYLIB, "@rpath/libalpha.dylib"))]


def build_image(cmds) -> bytes:
    body = b"".join(c for _, c in cmds)
    for _, c in cmds:
        cmd, cmdsize = struct.unpack_from("<Ii", c, 0)
        assert cmdsize % 8 == 0, "cmdsize %d violates the parser's 8-alignment" % cmdsize
    header = struct.pack("<IiiIIIII", MH_MAGIC_64, CPU_TYPE_X86_64,
                         CPU_SUBTYPE_X86_64_ALL, MH_DYLIB, len(cmds),
                         len(body), 0, 0)
    return header + body


def build_tree() -> dict:
    return {
        "image/main.dylib": build_image(MAIN_CMDS),
        "image/rpathdir/libalpha.dylib": build_image(ALPHA_CMDS),
    }


def parse_image(data: bytes) -> dict:
    magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags, _res = \
        struct.unpack_from("<IiiIIIII", data, 0)
    assert magic == MH_MAGIC_64, "bad magic"
    cmds = []
    off = 32
    for _ in range(ncmds):
        cmd, cmdsize = struct.unpack_from("<Ii", data, off)
        name = None
        if cmd in (LC_ID_DYLIB, LC_LOAD_DYLIB):
            noff = struct.unpack_from("<I", data, off + 8)[0]
            end = data.index(b"\x00", off + noff)
            name = data[off + noff:end].decode("ascii")
        elif cmd == LC_RPATH:
            noff = struct.unpack_from("<I", data, off + 8)[0]
            end = data.index(b"\x00", off + noff)
            name = data[off + noff:end].decode("ascii")
        cmds.append({"cmd_hex": "0x%08x" % cmd, "cmdsize": cmdsize,
                     "name": name})
        off += cmdsize
    assert off == 32 + sizeofcmds, "commands do not tile sizeofcmds"
    return {
        "magic_hex": "0x%08x" % magic,
        "cpu_type": cputype,
        "cpu_subtype": cpusubtype,
        "file_type_code": filetype,
        "file_type": {MH_DYLIB: "dylib"}[filetype],
        "ncmds": ncmds,
        "sizeofcmds": sizeofcmds,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "commands": cmds,
    }


def derive(tree: dict) -> dict:
    """Derive every oracle-checked fact from the built bytes and the
    authored tree layout."""
    main = parse_image(tree["image/main.dylib"])
    alpha = parse_image(tree["image/rpathdir/libalpha.dylib"])
    main_loads = [c["name"] for c in main["commands"]
                  if c["cmd_hex"] == "0x%08x" % LC_LOAD_DYLIB]
    main_rpaths = [c["name"] for c in main["commands"]
                   if c["cmd_hex"] == "0x%08x" % LC_RPATH]
    main_id = [c["name"] for c in main["commands"]
               if c["cmd_hex"] == "0x%08x" % LC_ID_DYLIB][0]
    alpha_id = [c["name"] for c in alpha["commands"]
                if c["cmd_hex"] == "0x%08x" % LC_ID_DYLIB][0]
    assert main_rpaths == ["@loader_path/rpathdir"]
    assert "image/rpathdir/libalpha.dylib" in tree
    assert "image/Frameworks/libbeta.dylib" not in tree
    # declared resolution expectations, from the authored bytes + tree only:
    # edge 0: @rpath/libalpha.dylib, rpath @loader_path/rpathdir ->
    #         rpathdir/libalpha.dylib EXISTS in the authored root
    # edge 1: @loader_path/../Frameworks/libbeta.dylib -> escapes the root
    # edge 2: /usr/lib/libSystem.B.dylib -> absolute, outside the root
    expected_versions = "1.0.0"
    return {
        "build_recipe": {
            "command": "python -B generator.py",
            "container": "mach-o-64-little-endian-load-command-tree",
            "struct_format": "<IiiIIIII header; <IiIIII dylib; <IiI rpath",
            "python_version": sys.version.split(" ")[0],
            "determinism": "byte-deterministic (fixed constants, no time)",
        },
        "main": dict(main, path="image/main.dylib", install_name=main_id,
                     rpaths=main_rpaths, load_dylibs=main_loads),
        "alpha": dict(alpha, path="image/rpathdir/libalpha.dylib",
                      install_name=alpha_id, rpaths=[], load_dylibs=[]),
        "declared_resolution": {
            "edge_install_names": main_loads,
            "edge_current_versions": [expected_versions] * len(main_loads),
            "edge_compatibility_versions": [expected_versions] * len(main_loads),
            "edge0_candidate_path": "rpathdir/libalpha.dylib",
            "edge0_candidate_exists_in_root": True,
            "edge1_candidate_escapes_root": True,
            "edge2_candidate_outside_root": True,
            "tree_files": sorted(tree.keys()),
        },
    }


def self_check() -> int:
    tree = {}
    for rel in ("image/main.dylib", "image/rpathdir/libalpha.dylib"):
        tree[rel] = (HERE / rel).read_bytes()
    d = derive(tree)
    m, a = d["main"], d["alpha"]
    checks = [
        ("main_magic", m["magic_hex"] == "0xfeedfacf"),
        ("alpha_magic", a["magic_hex"] == "0xfeedfacf"),
        ("main_cpu_type", m["cpu_type"] == 0x01000007),
        ("main_file_type", m["file_type_code"] == 6 and m["file_type"] == "dylib"),
        ("main_ncmds_5", m["ncmds"] == 5),
        ("alpha_ncmds_1", a["ncmds"] == 1),
        ("cmds_tile_main", all(c["cmdsize"] % 8 == 0 for c in m["commands"])),
        ("cmds_tile_alpha", all(c["cmdsize"] % 8 == 0 for c in a["commands"])),
        ("main_install_name", m["install_name"] == "@rpath/librevenger-r82.dylib"),
        ("alpha_install_name", a["install_name"] == "@rpath/libalpha.dylib"),
        ("main_loads_3", m["load_dylibs"] == [
            "@rpath/libalpha.dylib",
            "@loader_path/../Frameworks/libbeta.dylib",
            "/usr/lib/libSystem.B.dylib"]),
        ("main_rpath_1", m["rpaths"] == ["@loader_path/rpathdir"]),
        ("alpha_leaf", a["load_dylibs"] == [] and a["rpaths"] == []),
        ("rpath_target_present",
         "image/rpathdir/libalpha.dylib" in d["declared_resolution"]["tree_files"]),
        ("escape_target_absent",
         "image/Frameworks/libbeta.dylib" not in d["declared_resolution"]["tree_files"]),
    ]
    bad = 0
    for name, ok in checks:
        print(("SELFCHECK %s ok" % name) if ok else ("SELFCHECK %s FAIL" % name))
        bad += 0 if ok else 1
    truth = dict(d)
    truth["derived_checks"] = len(checks)
    TRUTH.write_text(json.dumps(truth, indent=1, sort_keys=True) + "\n",
                     encoding="utf-8")
    print("GENERATOR derived %d checks; truth.json written" % len(checks))
    return 1 if bad else 0


def regen() -> int:
    tree = build_tree()
    ok = True
    with tempfile.TemporaryDirectory() as td:
        for rel, data in sorted(tree.items()):
            tmp = Path(td) / rel
            tmp.parent.mkdir(parents=True, exist_ok=True)
            tmp.write_bytes(data)
            old = (HERE / rel).read_bytes()
            same = tmp.read_bytes() == old
            ok = ok and same
            print("REGEN %s: %s (%d bytes)" % (
                rel, "byte-identical" if same else "BYTE-DRIFT", len(data)))
    return 0 if ok else 1


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    if mode == "regen":
        return regen()
    if mode == "self-check":
        return self_check()
    if mode == "build":
        tree = build_tree()
        for rel, data in tree.items():
            p = HERE / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        return self_check()
    print("usage: generator.py [build|regen|self-check]", file=sys.stderr)
    return 64


if __name__ == "__main__":
    raise SystemExit(main())
