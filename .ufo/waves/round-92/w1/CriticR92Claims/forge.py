#!/usr/bin/env python3
"""CriticR92Claims forgery reproducer (read-only over the lane; writes only under SCRATCH).

Builds the cheapest trees that the frozen counters must reject and reports their verdicts:
  C1: full forgery (stub entry, invented SOURCES row, invented votes, README C03 held)
      plus variants: wrong vote sha, no fenced $ block, all-n/a decisions.
  C2: C08 token edits (partial, held citing seed.md, trailing cell), round-77 record deletion,
      intended uncovered token, and a shadow probe module in a scratch copy of reports/round-66.
Run: python3 -B .ufo/waves/round-92/w1/CriticR92Claims/forge.py   (from the lane root or anywhere)
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r92" / "CriticR92Claims"
C1 = LANE / "reports/round-92/c1_k_admit_counter.py"
C2 = LANE / "reports/round-92/c2_legend_counter.py"
ENTRY_REL = "knowledge/round-92-managed-assembly-metadata-evidence.md"
QS = [f"Q{i:02d}" for i in range(1, 18)]
C08_OPS = {"inspect_web_page", "capture_browser_scenario", "observe_web_session"}
C08_ROW = "| C08 | browser/Electron runtime evidence | — | — | frontier |"


def fresh(name, r92=True):
    d = SCRATCH / name
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    shutil.copytree(LANE / "corpus", d / "corpus", ignore=shutil.ignore_patterns("__pycache__"))
    if r92:
        (d / "reports").mkdir()
        shutil.copytree(LANE / "reports/round-92", d / "reports/round-92")
    return d


def digest(text):
    norm = re.sub(r"^admission-status: (candidate|admitted|rejected)$", "admission-status: candidate",
                  text, flags=re.M)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def run(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def forge_c1(name, votes=True, sha_ok=True, embed=True, decision="PASS"):
    d = fresh(name)
    qrows = "\n".join(f"| {q} | forged criterion | {decision} | forged |" for q in QS)
    fence = "```\n$ python3 -B corpus/lint_entry.py --self-test\n```\n" if embed else ""
    text = ("source: S491 — forged SOURCES row (not opened)\n"
            "verified-at: 2026-11-05\n"
            "recheck: `python3 -B corpus/lint_entry.py --self-test`\n"
            "coverage-map: C03 (`corpus/README.md`, managed (.NET/CLI) assemblies)\n"
            "admission-status: admitted\n\n"
            "# Forged C03 entry\n\n## §Q-map\n\n| id | criterion | decision | note |\n|---|---|---|---|\n"
            + qrows + "\n\n## Check\n\n" + fence)
    (d / "corpus" / ENTRY_REL).write_text(text, encoding="utf-8")
    with open(d / "corpus/SOURCES.md", "a", encoding="utf-8") as f:
        f.write("\n| S491 | Forged row | docs | A | forged | forged | forged | mined | 2026-11-05 | 90d "
                "| corpus/knowledge/round-92-managed-assembly-metadata-evidence.md |\n")
    rp = d / "corpus/README.md"
    s = rp.read_text(encoding="utf-8")
    s2 = re.sub(r"^\| C03 \| managed \(\.NET/CLI\) assemblies \| — \| — \| frontier \|$",
                "| C03 | managed (.NET/CLI) assemblies | `knowledge/round-92-managed-assembly-metadata-evidence.md` | — | held |",
                s, flags=re.M)
    assert s2 != s
    rp.write_text(s2, encoding="utf-8")
    if votes:
        vd = d / "reports/round-92/votes"
        vd.mkdir(parents=True)
        dg = digest(text) if sha_ok else "0" * 64
        for seat, role in (("ForgerA", "reviewer"), ("ForgerB", "critic")):
            (vd / f"{seat}.json").write_text(json.dumps({
                "seat": seat, "role": role, "candidate_sha256": dg,
                "decisions": {q: decision for q in QS}}), encoding="utf-8")
    return d


def c08_edit(d, new):
    rp = d / "corpus/README.md"
    s = rp.read_text(encoding="utf-8")
    s2 = s.replace(C08_ROW + "\n", new + "\n", 1)
    assert s2 != s, "C08 row not matched"
    rp.write_text(s2, encoding="utf-8")


def forge_c2(name, edit=None, delete_r77=False):
    d = fresh(name, r92=False)
    if edit:
        c08_edit(d, edit)
    if delete_r77:
        for p in (d / "corpus/live/runs/round-77").glob("*.json"):
            try:
                x = json.loads(p.read_bytes())
            except ValueError:
                continue
            if isinstance(x, dict) and x.get("operation") in C08_OPS:
                p.unlink()
    return d


def main():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    print("== C1 (frozen counter, --tree)")
    for name, kw in [
        ("c1-forge-full", {}),
        ("c1-forge-badsha", {"sha_ok": False}),
        ("c1-forge-noembed", {"embed": False}),
        ("c1-forge-allna", {"decision": "n/a"}),
    ]:
        d = forge_c1(name, **kw)
        rc, o = run([sys.executable, "-B", str(C1), "--tree", str(d)])
        print(f"-- {name} exit={rc}")
        print(o.rstrip())
    print("== C2 (frozen counter, --tree)")
    c2_cases = [
        ("c2-partial", {"edit": "| C08 | browser/Electron runtime evidence | — | — | partial |"}),
        ("c2-held-seed", {"edit": "| C08 | browser/Electron runtime evidence | `knowledge/seed.md` | — | held |"}),
        ("c2-trailing-cell", {"edit": "| C08 | browser/Electron runtime evidence | — | — | frontier | note |"}),
        ("c2-del-r77", {"delete_r77": True}),
        ("c2-uncovered-intended", {"edit": "| C08 | browser/Electron runtime evidence | — | — | uncovered |"}),
    ]
    for name, kw in c2_cases:
        d = forge_c2(name, **kw)
        rc, o = run([sys.executable, "-B", str(C2), "--tree", str(d)])
        print(f"-- {name} exit={rc}")
        print(o.rstrip())
    print("== C2 probe shadowing (scratch copy; the lane is not touched)")
    sh = SCRATCH / "shadow"
    if sh.exists():
        shutil.rmtree(sh)
    (sh / "reports/round-66").mkdir(parents=True)
    (sh / "reports/round-92").mkdir(parents=True)
    shutil.copy(LANE / "reports/round-66/measure.py", sh / "reports/round-66/measure.py")
    shutil.copy(C2, sh / "reports/round-92/c2_legend_counter.py")
    shutil.copytree(LANE / "corpus", sh / "corpus", ignore=shutil.ignore_patterns("__pycache__"))
    (sh / "reports/round-66/tempfile.py").write_text(
        "import sys, os\n"
        "print('K_HELD=9/15 score=6.0'); print('K_HELD_BACKED=9/15')\n"
        "print('README_TOKEN_LEGEND_MISMATCH=0 rows=[]')\n"
        "sys.stdout.flush(); os._exit(0)\n", encoding="utf-8")
    rc, o = run([sys.executable, "-B", str(sh / "reports/round-92/c2_legend_counter.py"), "--tree", str(sh)], cwd="/")
    print(f"-- shadow-probe exit={rc}")
    print(o.rstrip())
    shutil.rmtree(SCRATCH, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
