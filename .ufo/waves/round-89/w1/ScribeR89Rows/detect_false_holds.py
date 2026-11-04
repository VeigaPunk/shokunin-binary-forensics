#!/usr/bin/env python3
"""Detect census rows whose verdict says 'holds' while the row's own recorded
value contradicts the live host.

The 2026-11-04 tables' own preamble defines the rule:
  'holds' means the recorded value still matches.
For every row whose verdict cell starts with 'holds', the row's recorded cell
must still match the live value the frozen instrument derives. This checker
re-derives the live value with the instrument's own live() and compares it
against the recorded cell literally.

Read-only. Prints one block per contradiction; exit 1 if any found.
"""
import importlib.util, pathlib, re, sys

LANE = pathlib.Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
spec = importlib.util.spec_from_file_location("crp", LANE / "corpus/census_reprobe.py")
crp = importlib.util.module_from_spec(spec); spec.loader.exec_module(crp)

FILES = {
    "seed": LANE / "corpus/knowledge/seed.md",
    "check": LANE / "corpus/knowledge/2026-10-12-rea-readiness-checklist.md",
}

def rows_of(path):
    """id -> (recorded_cell, observed_cell, verdict_cell) for the LAST row per id."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*([FK]\d{2})\s*\|", line)
        if not m:
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        out[m.group(1)] = (c[1], c[-2], c[-1])
    return out

def contradiction(kind, arg, tokens, rec):
    """Does the recorded cell contradict the live value?"""
    r = rec.lower()
    if kind == "presence":
        live_on = tokens == ["present"]
        rec_says_on = ("present" in r) and ("absent" not in r)
        rec_says_off = ("absent" in r) or ("not on path" in r) or ("no output" in r)
        if live_on and rec_says_off:   return "live=present, recorded says absent"
        if (not live_on) and rec_says_on: return "live=absent, recorded says present"
        return None
    if kind in ("skill", "version"):
        live_nums = [t for t in tokens if re.fullmatch(r"\d+(\.\d+)*", t)]
        rec_nums = re.findall(r"\d+(?:\.\d+)+", r)
        if live_nums and rec_nums:
            if not any(lv in rec_nums for lv in live_nums):
                return f"live={live_nums}, recorded numbers={rec_nums}"
            return None
        if live_nums and not rec_nums:
            return f"live={live_nums}, recorded cell states no number"
        return None
    if kind in ("mcp", "pin"):
        live = [t for t in tokens if "@" in t]
        rec_specs = re.findall(r"rea-agents@([0-9][\w.]*)", r)
        if live and rec_specs:
            lv = live[0].split("@", 1)[1]
            if lv not in rec_specs:
                return f"live={live[0]}, recorded={rec_specs}"
        return None
    if kind == "listing":
        names = [t.lower() for t in tokens]
        rec_names = [n.lower() for n in re.findall(r"([\w.-]+\.md)", r)]
        missing = [n for n in names if n not in rec_names]
        if missing:
            return f"live *.md entries not named in recorded cell: {missing}"
        return None
    if kind == "import":
        live_ok = tokens == ["imports"]
        rec_ok = ("imports" in r) or ("import pwn" in r and "fail" not in r)
        rec_fail = ("fails" in r) or ("modulenotfound" in r)
        if live_ok and rec_fail:  return "live=imports, recorded says it fails"
        if (not live_ok) and rec_ok: return "live=fails, recorded says it imports"
        return None
    return None

bad = []
for rid, (key, specs) in sorted(crp.ROWS.items()):
    rec, obs, verd = rows_of(FILES[key])[rid]
    if not verd.lower().startswith("holds"):
        continue
    for kind, arg, tokens, forbidden in (crp.live(sp) for sp in specs):
        why = contradiction(kind, arg, tokens, rec)
        if why:
            bad.append((rid, f"{kind}:{arg}", why, rec, obs, verd))

for rid, what, why, rec, obs, verd in bad:
    print(f"FALSE_HOLDS {rid} {what}: {why}")
    print(f"  recorded cell : {rec}")
    print(f"  observed cell : {obs}")
    print(f"  verdict cell  : {verd}")
    print()
print(f"rows whose verdict says 'holds' but whose recorded value contradicts the live host: {len(bad)}")
for rid, what, why, *_ in bad:
    print(f"  - {rid} {what}")
sys.exit(1 if bad else 0)
