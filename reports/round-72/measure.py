#!/usr/bin/env python3
"""Frozen, read-only round-72 C15 coverage predicate over an extracted committed tree."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ENTRY = "corpus/knowledge/round-72-tool-landscape.md"
REQUIRED = [*(f"S{i:03d}" for i in range(54, 71)), "S073"]


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tree", type=Path, help="extracted committed tree root")
    parser.add_argument(
        "--control-status-flip-only",
        action="store_true",
        help="simulate a C15 README status flip without the knowledge or registry work",
    )
    args = parser.parse_args()
    root = args.tree
    readme = root / "corpus/README.md"
    registry = root / "corpus/SOURCES.md"
    entry = root / ENTRY
    if not all(path.is_file() for path in (readme, registry)):
        print("could-not-evaluate: missing corpus/README.md or corpus/SOURCES.md")
        return 2

    c15_held = False
    for line in readme.read_text(encoding="utf-8").splitlines():
        cells = table_cells(line)
        if len(cells) == 5 and cells[0] == "C15":
            c15_held = cells[2].find(ENTRY) >= 0 and cells[4] == "held"
            break
    if args.control_status_flip_only:
        c15_held = True

    cited = set()
    if entry.is_file():
        text = entry.read_text(encoding="utf-8")
        cited = set(re.findall(r"\bS\d{3,}\b", text))

    rows: dict[str, list[str]] = {}
    for line in registry.read_text(encoding="utf-8").splitlines():
        cells = table_cells(line)
        if len(cells) == 11 and re.fullmatch(r"S\d{3,}", cells[0]):
            rows[cells[0]] = cells

    valid = 0
    for source_id in REQUIRED:
        cells = rows.get(source_id)
        if (
            source_id in cited
            and cells is not None
            and cells[2] == "tool"
            and cells[3] == "A"
            and cells[7] == "mined"
            and ENTRY in cells[10]
        ):
            valid += 1

    backed = int(c15_held and entry.is_file() and valid == len(REQUIRED))
    print(f"C15_HELD_BACKED={backed}/1")
    print(f"C15_TOOL_ROWS={valid}/{len(REQUIRED)}")
    print(f"C15_STATUS={'held' if c15_held else 'not-held-or-absent'}")
    print(f"ENTRY_PRESENT={'yes' if entry.is_file() else 'no'}")
    print("HOLDS_C15=" + ("yes" if backed else "no"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
