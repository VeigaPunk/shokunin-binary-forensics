#!/usr/bin/env python3
"""Replay the instrument's own selftest plants and print WHICH branch fired.

Usage: attr_legs.py <instrument.py>
Prints, per plant, the findings the instrument's check_rows produced. A plant
caught only by the token-presence branch leaves the forbidden-opposite or
phantom branch unexercised (that is the attribution this probe measures).
"""
import importlib.util
import sys
import tempfile
from pathlib import Path


def load(path):
    spec = importlib.util.spec_from_file_location("instr", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PLANTS = [
    ("presence-opposite", "K01", "| K01 | mint ABSENT | now absent | holds |"),
    ("presence-unstated", "K01", "| K01 | mint ABSENT | not on path | holds |"),
    ("version-missing", "F05", "| F05 | mint | p | v1.2.3 | STALE -> v1.2.3 |"),
    ("import-opposite", "K02", "| K02 | mint | import fails | holds |"),
    ("mcp-missing", "F06", "| F06 | mint | p | key `rea` | STALE -> registered |"),
    ("listing-phantom", "F01", "| F01 | mint | p | `SKILL.md`, `gone.md` | holds |"),
    ("skill-missing", "F02", "| F02 | mint | p | version 9.9 | STALE -> 9.9 |"),
    ("pin-missing", "F04", "| F04 | mint | p | `rea-agents@1.0` | holds |"),
]


def main(argv):
    m = load(Path(argv[0]))

    def fake_live(spec):
        kind, arg = spec
        table = {
            ("listing", "skill_dir"): (["skill.md"], []),
            ("skill", None): (["9.9", "7"], []),
            ("presence", "jadx"): (["present"], ["absent"]),
            ("pin", None): (["rea-agents@9.9"], []),
            ("version", "node --version"): (["v1.2.3"], []),
            ("version", "npm --version"): (["4.5.6"], []),
            ("mcp", None): (["rea-agents@9.9"], []),
            ("import", "pwn"): (["imports"], ["fails", "ModuleNotFound"]),
        }
        return (kind, arg) + table[(kind, arg)]

    real_live, real_rows = m.live, m.ROWS
    m.live = fake_live
    m.ROWS = {
        "F01": ("seed", [("listing", "skill_dir")]),
        "F02": ("seed", [("skill", None)]),
        "F03": ("seed", [("presence", "jadx")]),
        "F04": ("seed", [("pin", None)]),
        "F05": ("seed", [("version", "node --version"), ("version", "npm --version")]),
        "F06": ("seed", [("mcp", None)]),
        "K01": ("check", [("presence", "jadx")]),
        "K02": ("check", [("import", "pwn")]),
    }
    try:
        for name, rid, line in PLANTS:
            with tempfile.TemporaryDirectory() as t2:
                r2 = m._fixture(t2)
                target = r2 / (m.SEED if m.ROWS[rid][0] == "seed" else m.CHECK)
                body = []
                for l in target.read_text().splitlines():
                    body.append(line if l.startswith(f"| {rid} ") else l)
                target.write_text("\n".join(body) + "\n")
                _, f2 = m.check_rows(r2)
                hit = [x for x in f2 if x.startswith(f"CENSUS_MISMATCH {rid} ")]
                branch = "NONE"
                if hit:
                    if "against the live value" in hit[0]:
                        branch = "forbidden-opposite"
                    elif "names absent entr" in hit[0]:
                        branch = "listing-phantom"
                    elif "does not state live value" in hit[0]:
                        branch = "token-presence"
                print(f"{name:20s} rid={rid} caught={len(hit)} branch={branch}")
                for h in hit:
                    print(f"    {h}")
    finally:
        m.live, m.ROWS = real_live, real_rows
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
