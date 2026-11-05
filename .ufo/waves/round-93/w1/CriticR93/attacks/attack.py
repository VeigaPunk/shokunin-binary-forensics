#!/usr/bin/env python3
"""CriticR93 attack driver. Scratch only. Builds fixture trees from the frozen base
archive and runs the frozen v2 counters with --tree. Never writes the lane tree."""
import hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
S = Path("/fast/scratch/hyaku/revenger-r93/CriticR93")
HS = S / "hs"
TREES = S / "trees"
BASE = "281a5bad66e844190a570cb35d257c6974749993"
ENTRY_REL = "knowledge/round-93-browser-cdp-runtime-evidence.md"
ENTRY = "corpus/" + ENTRY_REL
QS = [f"Q{i:02d}" for i in range(1, 18)]
TAIL = "ORACLE OK (17/17 checks)"
RSHA = "b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868"
FIX = {"index.html": "46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45",
       "app.js": "fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593"}
C1 = LANE / "reports/round-93/c1_k_admit_counter2.py"
C2 = LANE / "reports/round-93/c2_legend_counter2.py"
ENV = dict(os.environ, HYAKU_SCRATCH=str(HS))


def sh(b):
    return hashlib.sha256(b).hexdigest()


def digest(text):
    norm = re.sub(r"^admission-status: (candidate|admitted|rejected)$",
                  "admission-status: candidate", text, flags=re.M)
    return sh(norm.encode("utf-8"))


def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]


def archive(rev, paths, dest):
    ar = subprocess.run(["git", "-C", str(LANE), "archive", rev, *paths], capture_output=True, check=True)
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(["tar", "-x", "-C", str(dest)], input=ar.stdout, check=True)


def entry_text(status="admitted", s495_date="2026-11-05", body="", head_extra=""):
    return ("source: S495 — round-77 record corpus/live/runs/round-77/inspection.json "
            "(own-work, tier A, opened 2026-11-05)\n"
            "verified-at: 2026-11-05\n"
            f"recheck: oracle tail {TAIL}\n"
            "coverage-map: C08\n"
            f"admission-status: {status}\n"
            f"{head_extra}\n# Entry\n\nBody text for the round-93 browser CDP entry.\n{body}")


def source_row(sid, opened="2026-11-05", status="mined", used=ENTRY, loc=None, kind="own-work"):
    loc = loc or f"corpus/live/runs/round-77 record (own-work, tier A, opened {opened})"
    return ("| " + " | ".join([sid, loc, kind, "A", "record identity", "oracle 17/17",
                              "identity facts re-derive", status, opened, "180d", used]) + " |")


def base_tree(name, entry=None, s495_row=None, stub_tools=True):
    t = TREES / name
    shutil.rmtree(t, ignore_errors=True)
    t.mkdir(parents=True)
    archive(BASE, ["corpus"], t)
    rd = t / "corpus/README.md"
    out = []
    for ln in rd.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\|[ \t]*C08 ", ln):
            c = cells(ln)
            c[2] = "`" + ENTRY_REL + "`"
            c[4] = "held"
            ln = "| " + " | ".join(c) + " |"
        out.append(ln)
    rd.write_text("\n".join(out) + "\n", encoding="utf-8")
    ent = t / ENTRY
    ent.parent.mkdir(parents=True, exist_ok=True)
    ent.write_text(entry if entry is not None else entry_text(), encoding="utf-8")
    src = t / "corpus/SOURCES.md"
    lines = [l for l in src.read_text(encoding="utf-8").splitlines() if not re.match(r"^\| S495 ", l)]
    lines.append(s495_row or source_row("S495"))
    src.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if stub_tools:
        (t / "corpus/lint_entry.py").write_text("import sys\nsys.exit(0)\n")
        (t / "corpus/check_embedded_outputs.py").write_text("import sys\nsys.exit(0)\n")
    w = t / ".ufo/waves/round-93/w1"
    w.mkdir(parents=True)
    reg = json.loads((LANE / ".ufo/waves/round-93/w1/swarm-registry.json").read_text(encoding="utf-8"))
    (w / "swarm-registry.json").write_text(json.dumps(reg), encoding="utf-8")
    (t / "reports/round-93/votes").mkdir(parents=True)
    write_opens(t)
    return t


def write_opens(t, fixture_shas=None, record_sha=RSHA, tail=TAIL):
    o = {"record_sha256": record_sha, "oracle_tail": tail,
         "fixture_shas": fixture_shas if fixture_shas is not None else dict(FIX)}
    (t / "reports/round-93/opens.json").write_text(json.dumps(o), encoding="utf-8")


def add_vote(t, seat, role="reviewer", sha=None, ds=None, notes=None, apath=None, asha=None,
             art_text=None, seat_field=None, write_art=True):
    if apath is None:
        apath = f".ufo/waves/round-93/w1/{seat}/evidence.md"
    art = t / apath
    if write_art and not art.exists() and not ".." in apath:
        art.parent.mkdir(parents=True, exist_ok=True)
        art.write_text(art_text if art_text is not None else f"{seat} review evidence\n", encoding="utf-8")
    if asha is None:
        asha = sh(art.read_bytes()) if art.is_file() else "0" * 64
    if sha is None:
        sha = digest((t / ENTRY).read_text(encoding="utf-8"))
    if ds is None:
        ds = {q: "PASS" for q in QS}
    if notes is None:
        notes = {q: "clean: checked against the entry text" for q in QS}
    v = {"seat": seat_field or seat, "role": role, "candidate_sha256": sha, "decisions": ds,
         "notes": notes, "artifact_path": apath, "artifact_sha256": asha}
    (t / "reports/round-93/votes" / f"{seat}-{len(list((t/'reports/round-93/votes').glob('*.json')))}.json").write_text(
        json.dumps(v), encoding="utf-8")
    return v


def honest(name, **kw):
    t = base_tree(name, **kw)
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    return t


def run(counter, t, extra=()):
    cmd = [sys.executable, "-B", str(counter), "--tree", str(t), *extra]
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=str(S))
    out = r.stdout + r.stderr
    verdict = re.search(r"(C[12]_VERDICT)=(\w+)", out)
    fails = re.findall(r"^(C[12]_\w+)=fail$", out, re.M)
    return {"rc": r.returncode, "verdict": verdict.group(2) if verdict else "no-label",
            "fails": fails, "out": out}


def report(name, res, note=""):
    (S / "out" / f"{name}.txt").write_text(res["out"], encoding="utf-8")
    print(f"{name}: rc={res['rc']} verdict={res['verdict']} failing={','.join(res['fails']) or '-'} {note}")
    sys.stdout.flush()
    return res


def c1(name, t, note=""):
    return report(name, run(C1, t), note)


def c2(name, t, note=""):
    return report(name, run(C2, t), note)


def summary_k(res):
    m = re.search(r"C1_K_HELD_BACKED=(\d+)/(\d+)", res["out"])
    return m.group(0) if m else "K=?"
