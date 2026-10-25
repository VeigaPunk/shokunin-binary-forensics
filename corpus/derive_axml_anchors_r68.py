#!/usr/bin/env python3
"""Derive the AXML spec anchors this lane's knowledge entries cite (round-68 C2).

The round-65 and round-67 candidates both failed an admission gate on one
transcribed line number (`RES_XML_START_NAMESPACE_TYPE` written as :244 where
the pinned snapshot has it at :245 — mistake class M40/M44). This script is
the capture for that class: every anchor an entry states is printed here by
searching the pinned AOSP `ResourceTypes.h` bytes for the symbol, so the entry
can embed the derivation as a command whose output the registered gate
(`corpus/check_embedded_outputs.py`) re-checks verbatim.

The snapshot it reads is committed at `corpus/snapshots/ResourceTypes.h`, a
byte-exact copy of the lane's pinned snapshot
`.ufo/waves/round-65/source-snapshots/ResourceTypes.h`
(sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f,
86255 bytes). The copy exists so the derivation runs from any corpus tree;
the digest is pinned below and a mismatch is a hard error.

Usage (cwd = lane root):
    python3 -B corpus/derive_axml_anchors.py
        Exit 0; one line per cited anchor, in a fixed order.
    Exit 2: the snapshot is missing, its digest differs from the pin, or a
        cited symbol is absent or ambiguous (the script never prints a line
        number it did not find).

Read-only: it reads one file in this repository and writes nothing.
"""
import hashlib
import sys
from pathlib import Path

SNAPSHOT_REL = "snapshots/ResourceTypes.h"
SNAPSHOT_SHA256 = "56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f"

STRUCTS = (
    "ResChunk_header",
    "Res_value",
    "ResStringPool_header",
    "ResXMLTree_header",
    "ResXMLTree_node",
    "ResXMLTree_attrExt",
    "ResXMLTree_attribute",
)

ENUMS = (
    "RES_STRING_POOL_TYPE",
    "RES_XML_TYPE",
    "RES_XML_START_NAMESPACE_TYPE",
    "RES_XML_END_NAMESPACE_TYPE",
    "RES_XML_START_ELEMENT_TYPE",
    "RES_XML_END_ELEMENT_TYPE",
    "RES_XML_RESOURCE_MAP_TYPE",
)

COMMENT_TEXT = "Byte offset from the start of this structure where the attributes start"
COMMENT_FIELD = "uint16_t attributeStart;"


def fail(msg):
    print(f"derive_axml_anchors: {msg}")
    sys.exit(2)


def find_unique(lines, predicate, what):
    hits = [i + 1 for i, line in enumerate(lines) if predicate(line)]
    if not hits:
        fail(f"{what}: not found")
    if len(hits) > 1:
        fail(f"{what}: ambiguous ({len(hits)} hits at {hits})")
    return hits[0]


def main():
    path = Path(__file__).resolve().parent / SNAPSHOT_REL
    if not path.is_file():
        fail(f"snapshot missing: {path}")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != SNAPSHOT_SHA256:
        fail(f"snapshot digest {digest} != pinned {SNAPSHOT_SHA256}")
    text = raw.decode("utf-8", errors="replace")
    lines = text.splitlines()

    out = [f"sha256 {digest} ResourceTypes.h"]
    for name in STRUCTS:
        line = find_unique(lines, lambda l, n=name: l.strip() == f"struct {n}",
                           f"struct {name}")
        out.append(f"struct {name} : {line}")
    for name in ENUMS:
        line = find_unique(lines, lambda l, n=name: l.strip().startswith(n + " "),
                           f"enum {name}")
        out.append(f"enum {name} : {line}")
    comment = find_unique(lines, lambda l: COMMENT_TEXT in l, "attributeStart comment")
    field = find_unique(lines, lambda l: l.strip() == COMMENT_FIELD, "attributeStart field")
    out.append(f"comment attributeStart : {comment}")
    out.append(f"field attributeStart : {field}")
    print("\n".join(out))
    sys.exit(0)


if __name__ == "__main__":
    main()
