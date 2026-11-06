#!/usr/bin/env python3
"""ReviewerCapR100 attack 2 — fixture copy carrying a SECOND AndroidManifest.xml
member whose versionName is tampered (1.0 -> 9.9), with truth.json updated so
the digest check alone cannot catch it. Probe must still refuse (decoders should
disagree with truth on at least one reading, or the probe flags the anomaly)."""
import hashlib
import json
import struct
import sys
import zipfile
from pathlib import Path

SRC = Path(sys.argv[1])          # corpus/fixtures/apk-r65
DST = Path(sys.argv[2])          # output fixture dir

apk = (SRC / "fixture.apk").read_bytes()


def axml_bytes(data):
    # first local entry: AndroidManifest.xml (stored)
    nlen = struct.unpack_from("<H", data, 26)[0]
    elen = struct.unpack_from("<H", data, 28)[0]
    csize = struct.unpack_from("<I", data, 18)[0]
    return data[30 + nlen + elen: 30 + nlen + elen + csize]


orig = axml_bytes(apk)
patched = orig.replace(b"1.0\x00", b"9.9\x00")
assert patched != orig and len(patched) == len(orig), "versionName not patched"

DST.mkdir(parents=True, exist_ok=True)
members = [
    ("AndroidManifest.xml", orig),
    ("classes.dex", None),
    ("META-INF/MANIFEST.MF", None),
    ("AndroidManifest.xml", patched),  # duplicate member, tampered
]
# pull the untouched members from the source zip
with zipfile.ZipFile(SRC / "fixture.apk") as z:
    blobs = {n: z.read(n) for n in ("classes.dex", "META-INF/MANIFEST.MF")}
members = [(n, blobs[n] if b is None else b) for n, b in members]

out_apk = DST / "fixture.apk"
with zipfile.ZipFile(out_apk, "w", zipfile.ZIP_STORED) as z:
    dt = (2026, 10, 24, 12, 0, 0)
    for n, b in members:
        zi = zipfile.ZipInfo(n, date_time=dt)
        zi.external_attr = 0o644 << 16
        z.writestr(zi, b)

# rebuild truth.json: update image + members; keep axml_declared/build_recipe
truth = json.loads((SRC / "truth.json").read_text())
blob = out_apk.read_bytes()
truth["image"]["sha256"] = hashlib.sha256(blob).hexdigest()
truth["image"]["size"] = len(blob)
new_members = []
with zipfile.ZipFile(out_apk) as z:
    for zi in z.infolist():
        b = z.read(zi)
        new_members.append({
            "name": zi.filename,
            "compressed_size": len(b),
            "uncompressed_size": len(b),
            "method": 0,
            "crc32": f"{zipfile.crc32(b) & 0xFFFFFFFF:08x}",
            "local_header_offset": zi.header_offset,
            "sha256": hashlib.sha256(b).hexdigest(),
        })
truth["members"] = new_members
(DST / "truth.json").write_text(json.dumps(truth, indent=2) + "\n")
print(json.dumps({
    "attack2_sha256": truth["image"]["sha256"],
    "attack2_size": len(blob),
    "members": [m["name"] for m in new_members],
}, indent=1))
