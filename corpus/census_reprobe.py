#!/usr/bin/env python3
"""Host-readiness census re-probe gate (revenger, round-89 freeze, v1).

The lane's freshness criterion counted `holds` / `STALE ->` markers, so a row
that states a host fact the current host contradicts still scored as current
(the round-89 red: ten of eighteen rows). This gate re-derives each census
fact from the live host and requires the row to state the observed value.

Rows read: `corpus/knowledge/seed.md` F01-F12 and
`corpus/knowledge/2026-10-12-rea-readiness-checklist.md` K01-K06.

Row shape accepted: `| <id> | <mint> | <probe> | <observed> | <verdict> |`
(seed) or `| <id> | <mint> | <observed> | <verdict> |` (checklist). Only the
last two cells are scored: the mint cell legitimately records the old state.

A row MISMATCHES when the scored cells fail to state the live value:
  presence  live on PATH -> must contain `present` and must not contain
            `absent`; live off PATH -> must contain `absent`.
  version   must contain the live version token (first line of the command).
  import    import succeeds -> must contain `imports` and must not contain
            `fails`/`ModuleNotFound`; fails -> must contain `fails`.
  mcp       server key `rea` must exist; the row must contain the live
            `rea-agents@<version>` spec (no values from mcp.json are read
            beyond the `rea` entry's own args).
  listing   every live `*.md` entry (backup/recovery copies excluded) must be
            named; every `.md` name the row names must exist (phantom check).
  skill     SKILL.md frontmatter `version` and `tool_count` values.
  pin       the `rea-agents@<version>` spec the skill names.

Usage:
    python3 -B corpus/census_reprobe.py --root <tree> [--json]
        TREE holds corpus/knowledge/{seed.md,2026-10-12-rea-readiness-checklist.md}.
    python3 -B corpus/census_reprobe.py --selftest
        Hermetic: one planted defect per rule kind scores exactly one
        mismatch and a clean fixture scores zero.

Prints `CENSUS_ROWS=<n>`, one `CENSUS_MISMATCH <id> ...` line per mismatch and
`CENSUS_STALE_UNFLAGGED=<n>`. Exit 0 iff n == 0, 1 if n > 0, 2 when a required
file is missing, 64 on usage. Read-only: it writes nothing and honours no
scratch path because it creates none.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL_DIR = Path.home() / ".agents/skills/reverse-engineer-anything"
MCP_JSON = Path.home() / ".omp/agent/mcp.json"
SEED = "corpus/knowledge/seed.md"
CHECK = "corpus/knowledge/2026-10-12-rea-readiness-checklist.md"

# rid -> (file key, probe spec). A probe spec is a list of (kind, arg) pairs;
# the row must state every probe's live value.
ROWS = {
    "F01": ("seed", [("listing", "skill_dir")]),
    "F02": ("seed", [("skill", None)]),
    "F03": ("seed", [("listing", "references")]),
    "F04": ("seed", [("presence", "rea")]),
    "F05": ("seed", [("pin", None)]),
    "F06": ("seed", [("version", "node --version"), ("version", "npm --version")]),
    "F07": ("seed", [("mcp", None)]),
    "F08": ("seed", [("presence", "ghidra")]),
    "F09": ("seed", [("presence", "jadx")]),
    "F10": ("seed", [("presence", "binwalk")]),
    "F11": ("seed", [("presence", "unblob")]),
    "F12": ("seed", [("import", "pwn")]),
    "K01": ("check", [("presence", "rea")]),
    "K02": ("check", [("version", "node --version"), ("version", "npm --version")]),
    "K03": ("check", [("mcp", None)]),
    "K04": ("check", [("presence", "ghidra"), ("presence", "ida")]),
    "K05": ("check", [("presence", "jadx"), ("presence", "binwalk"),
                      ("presence", "unblob"), ("import", "pwn")]),
    "K06": ("check", [("version", "unzip -v"), ("version", "zipinfo -v")]),
}


def first_line(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    out = (r.stdout or r.stderr).strip().splitlines()
    return out[0].strip() if out else None


def skill_meta(d):
    p = d / "SKILL.md"
    if not p.is_file():
        return None
    head = p.read_text(encoding="utf-8", errors="ignore")[:2000]
    ver = re.search(r'^\s*version:\s*"?([0-9][\w.]*)"?\s*$', head, re.M)
    cnt = re.search(r"^\s*tool_count:\s*(\d+)\s*$", head, re.M)
    return (ver.group(1), cnt.group(1)) if ver and cnt else None


def skill_pin(d):
    p = d / "SKILL.md"
    if not p.is_file():
        return None
    m = re.search(r"rea-agents@([0-9][\w.]*)", p.read_text(encoding="utf-8", errors="ignore"))
    return m.group(1) if m else None


def mcp_spec():
    try:
        d = json.loads(MCP_JSON.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    servers = d.get("mcpServers", d) if isinstance(d, dict) else {}
    entry = servers.get("rea") if isinstance(servers, dict) else None
    if not isinstance(entry, dict):
        return None
    for a in entry.get("args", []):
        m = re.search(r"rea-agents@([0-9][\w.]*)", str(a))
        if m:
            return m.group(1)
    return None


def md_names(d):
    if not d.is_dir():
        return None
    return sorted(p.name for p in d.iterdir()
                  if p.is_file() and p.name.endswith(".md")
                  and ".rea.backup" not in p.name and ".recovery" not in p.name)


def live(spec):
    """Return (kind, arg, tokens, forbidden) for one probe."""
    kind, arg = spec
    if kind == "presence":
        on = shutil.which(arg) is not None
        return (kind, arg, ["present"] if on else ["absent"],
                ["absent"] if on else ["present"])
    if kind == "version":
        v = first_line(arg)
        if v is None:
            return (kind, arg, [], [])
        m = re.search(r"\d+(?:\.\d+)+", v)
        return (kind, arg, [m.group(0) if m else v], [])
    if kind == "import":
        try:
            r = subprocess.run([sys.executable, "-B", "-c", f"import {arg}"],
                               capture_output=True, text=True, timeout=60)
            ok = r.returncode == 0
        except (OSError, subprocess.SubprocessError):
            ok = False
        return (kind, arg, ["imports"] if ok else ["fails"],
                ["fails", "ModuleNotFound"] if ok else ["imports"])
    if kind == "mcp":
        spec_v = mcp_spec()
        if spec_v is None:
            return (kind, "rea", ["not registered"], ["registered"])
        return (kind, "rea", [f"rea-agents@{spec_v}"], [])
    if kind == "listing":
        names = md_names(SKILL_DIR if arg == "skill_dir" else SKILL_DIR / "references")
        if names is None:
            return (kind, arg, ["absent"], [])
        return (kind, arg, names, [])
    if kind == "skill":
        meta = skill_meta(SKILL_DIR)
        if meta is None:
            return (kind, "skill", ["absent"], [])
        return (kind, "skill", list(meta), [])
    if kind == "pin":
        v = skill_pin(SKILL_DIR)
        return (kind, "pin", [f"rea-agents@{v}"] if v else ["absent"], [])
    raise SystemExit(f"unknown probe kind {kind}")


def scored_text(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return " | ".join(cells[-2:]) if len(cells) >= 2 else line


def check_rows(root):
    files = {"seed": root / SEED, "check": root / CHECK}
    for p in files.values():
        if not p.is_file():
            return None, [f"missing {p}"]
    lines = {}
    for key, p in files.items():
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = re.match(r"^\|\s*([FK]\d{2})\s*\|", line)
            if m:
                lines[m.group(1)] = line
    findings, rows = [], 0
    for rid in sorted(ROWS):
        key, specs = ROWS[rid]
        line = lines.get(rid)
        if line is None:
            findings.append(f"CENSUS_MISMATCH {rid} row-absent")
            continue
        rows += 1
        text = scored_text(line).lower()
        for spec in specs:
            kind, arg, tokens, forbidden = live(spec)
            if kind == "listing" and tokens and tokens != ["absent"]:
                named = set(re.findall(r"([\w.-]+\.md)", text))
                live_l = {t.lower() for t in tokens}
                phantom = sorted(n for n in named if n not in live_l)
                if phantom:
                    findings.append(f"CENSUS_MISMATCH {rid} listing:{arg} "
                                    f"names absent entr{'y' if len(phantom) == 1 else 'ies'} "
                                    f"{', '.join(phantom)}")
                    continue
            for tok in tokens:
                if tok.lower() not in text:
                    findings.append(f"CENSUS_MISMATCH {rid} {kind}:{arg} "
                                    f"does not state live value {tok!r}")
                    break
            else:
                bad = [w for w in forbidden if w.lower() in text]
                if bad:
                    findings.append(f"CENSUS_MISMATCH {rid} {kind}:{arg} "
                                    f"states {bad[0]!r} against the live value")
    return rows, findings


# ---------------------------------------------------------------- self-test
def _fixture(tmp):
    """A clean synthetic census tree: every row states the live value of a
    probe kind whose live value is fixed inside this fixture."""
    d = Path(tmp)
    (d / "corpus/knowledge").mkdir(parents=True)
    seed = [
        "| F01 | mint | p | `SKILL.md` | holds |",
        "| F02 | mint | p | version 9.9, tool_count 7 | STALE -> 9.9 / 7 |",
        "| F03 | mint | p | now present | STALE -> present |",
        "| F04 | mint | p | `rea-agents@9.9` | STALE -> 9.9 |",
        "| F05 | mint | p | v1.2.3, 4.5.6 | STALE -> v1.2.3 / 4.5.6 |",
        "| F06 | mint | p | `rea-agents@9.9` | STALE -> registered |",
    ]
    (d / SEED).write_text("\n".join(seed) + "\n")
    check = [
        "| K01 | mint ABSENT | now present | STALE -> present |",
        "| K02 | mint | imports | holds |",
    ]
    (d / CHECK).write_text("\n".join(check) + "\n")
    return d


def selftest():
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

    global live
    real, live = live, fake_live
    global ROWS
    saved = ROWS
    ROWS = {
        "F01": ("seed", [("listing", "skill_dir")]),
        "F02": ("seed", [("skill", None)]),
        "F03": ("seed", [("presence", "jadx")]),
        "F04": ("seed", [("pin", None)]),
        "F05": ("seed", [("version", "node --version"), ("version", "npm --version")]),
        "F06": ("seed", [("mcp", None)]),
        "K01": ("check", [("presence", "jadx")]),
        "K02": ("check", [("import", "pwn")]),
    }
    legs = []
    with tempfile.TemporaryDirectory() as tmp:
        root = _fixture(tmp)
        rows, findings = check_rows(root)
        legs.append(("clean", rows == 8 and not findings, findings))
        plants = [
            ("presence-opposite", "K01", "| K01 | mint ABSENT | now absent | holds |"),
            ("presence-unstated", "K01", "| K01 | mint ABSENT | not on path | holds |"),
            ("version-missing", "F05", "| F05 | mint | p | v1.2.3 | STALE -> v1.2.3 |"),
            ("import-opposite", "K02", "| K02 | mint | import fails | holds |"),
            ("mcp-missing", "F06", "| F06 | mint | p | key `rea` | STALE -> registered |"),
            ("listing-phantom", "F01", "| F01 | mint | p | `SKILL.md`, `gone.md` | holds |"),
            ("skill-missing", "F02", "| F02 | mint | p | version 9.9 | STALE -> 9.9 |"),
            ("pin-missing", "F04", "| F04 | mint | p | `rea-agents@1.0` | holds |"),
        ]
        for name, rid, line in plants:
            with tempfile.TemporaryDirectory() as t2:
                r2 = _fixture(t2)
                target = r2 / (SEED if ROWS[rid][0] == "seed" else CHECK)
                body = []
                for l in target.read_text().splitlines():
                    body.append(line if l.startswith(f"| {rid} ") else l)
                target.write_text("\n".join(body) + "\n")
                _, f2 = check_rows(r2)
                hit = [x for x in f2 if x.startswith(f"CENSUS_MISMATCH {rid} ")]
                legs.append((name, len(hit) >= 1, f2))
    ok = all(v for _, v, _ in legs)
    for name, verdict, findings in legs:
        print(f"CENSUS_SELFTEST_{name}={'ok' if verdict else 'FAIL'}")
        if not verdict:
            print("  findings:", findings)
    print(f"CENSUS_SELFTEST={'pass' if ok else 'fail'}")
    live, ROWS = real, saved
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--root" not in argv:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        print("usage: census_reprobe.py --root TREE [--json] | --selftest", file=sys.stderr)
        return 64
    root = Path(argv[argv.index("--root") + 1])
    rows, findings = check_rows(root)
    if rows is None:
        for f in findings:
            print(f)
        print("CENSUS_STALE_UNFLAGGED=could-not-evaluate")
        return 2
    if "--json" in argv:
        print(json.dumps({"rows": rows, "mismatches": len(findings),
                          "findings": findings}, sort_keys=True))
    else:
        print(f"CENSUS_ROWS={rows}")
        for f in findings:
            print(f)
        print(f"CENSUS_STALE_UNFLAGGED={len(findings)}")
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
