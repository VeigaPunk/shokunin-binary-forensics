#!/usr/bin/env python3
"""MutationR93 harness: one dropped-leg mutant per leg of both v2 counters.

Runs the FROZEN original and the mutant over constructed fixture trees.
Originals run from their frozen lane paths (read-only); mutants run from
$S/reports/round-93/ (same directory depth so parents[2] == $S, which is a
git repo borrowing lane objects via .git/objects/info/alternates -- read-only).
Never mutates the lane tree; scratch only.
"""
import hashlib, io, json, os, re, shutil, subprocess, sys, tarfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
S = Path("/fast/scratch/hyaku/revenger-r93/MutationR93")
BASE = "281a5bad66e844190a570cb35d257c6974749993"
TREES = S / "trees"
LOGS = S / "logs"
MUTDIR = S / "reports" / "round-93"
ENTRY_REL = "knowledge/round-93-browser-cdp-runtime-evidence.md"
RECORD_REL = "live/runs/round-77/inspection.json"
RECORD_SHA = "b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868"
TAIL = "ORACLE OK (17/17 checks)"
FIX = {"index.html": "46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45",
       "app.js": "fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593"}
QS = [f"Q{i:02d}" for i in range(1, 18)]
C1_SRC = LANE / "reports/round-93/c1_k_admit_counter2.py"
C2_SRC = LANE / "reports/round-93/c2_legend_counter2.py"

def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def archive(rev, paths, dest):
    ar = subprocess.run(["git", "-C", str(LANE), "archive", rev, *paths], capture_output=True)
    assert ar.returncode == 0, ar.stderr[:300]
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(["tar", "-x", "-C", str(dest)], input=ar.stdout, check=True)

def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]

def edit_rows(readme, mutate):
    out = []
    for ln in readme.splitlines():
        m = re.match(r"^\| ([C0-9]+) ", ln)
        if m:
            ln = mutate(m.group(1), ln)
        out.append(ln)
    return "\n".join(out) + "\n"

def set_row(readme_path, rid, cite=None, status=None, drop_cell=False):
    def mut(r, ln):
        if r != rid:
            return ln
        c = cells(ln)
        if drop_cell:
            del c[3]
            return "| " + " | ".join(c) + " |"
        if cite is not None:
            c[2] = "`" + cite + "`"
        if status is not None:
            c[4] = status
        return "| " + " | ".join(c) + " |"
    p = Path(readme_path)
    p.write_text(edit_rows(p.read_text(encoding="utf-8"), mut), encoding="utf-8")

def append_row(tree, line):
    p = tree / "corpus/README.md"
    p.write_text(p.read_text(encoding="utf-8") + line + "\n", encoding="utf-8")

def digest(text):
    norm = re.sub(r"^admission-status: (candidate|admitted|rejected)$",
                  "admission-status: candidate", text, flags=re.M)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()

def quality_ids(tree):
    txt = (tree / "corpus/QUALITY.md").read_text(encoding="utf-8")
    return re.findall(r"^\| (Q\d+) \|", txt, re.M)

def entry_text(variant, qids):
    head = ["source: S495 — round-77 record corpus/live/runs/round-77 (own-work, tier A, opened 2026-11-05)"]
    if variant == "ext":
        head.append("source: S500 — https://invented.invalid/quote-check (docs, tier A, opened 2026-11-05)")
    head.append("verified-at: 2026-11-05")
    if variant != "norecheck":
        head.append("recheck: oracle tail ORACLE OK (17/17 checks)")
    if variant != "nocovmap":
        head.append("coverage-map: C08")
    head.append("admission-status: " + ("candidate" if variant == "cand" else "admitted"))
    head += ["", "# Browser CDP runtime evidence (fixture-scoped)", "",
             "## §Q-map", "", "| criterion | decision | basis |", "|---|---|---|"]
    for i, q in enumerate(qids):
        head.append(f"| {q} | pass | check {i + 1} covered by the receipt rerun |")
    body = "\n".join(head) + "\n"
    cmd = "$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json"
    if variant == "vacuous":
        body += "\n```\n" + cmd + "\n```\n"
    if variant == "drift":
        body += "\n```\n" + cmd + "\nORACLE OK (16/17 checks)\n```\n"
    return body

S495 = ("| S495 | round-77 record corpus/live/runs/round-77 (own-work, tier A, opened 2026-11-05) "
        "| own-work | A | record identity | opened 2026-11-05 oracle 17/17 | The saved record's "
        "identity facts re-derive | mined | {date} | 180d | corpus/" + ENTRY_REL + " |")
S500 = ("| S500 | https://invented.invalid/quote-check (docs, tier A, opened 2026-11-05) | docs | A "
        "| quote-audit scope | anchor \"located quote\" | quote audit exercises the receipts leg "
        "| mined | 2026-11-05 | 180d | corpus/" + ENTRY_REL + " |")

def write_entry(tree, variant):
    qids = quality_ids(tree)
    (tree / "corpus" / ENTRY_REL).write_text(entry_text(variant, qids), encoding="utf-8")

def write_votes(tree, entry_variant="pos"):
    text = (tree / "corpus" / ENTRY_REL).read_text(encoding="utf-8")
    want = digest(text)
    art1 = tree / ".ufo/waves/round-93/w1/SeatA/evidence.md"
    art2 = tree / ".ufo/waves/round-93/w1/SeatB/evidence.md"
    art1.parent.mkdir(parents=True, exist_ok=True)
    art2.parent.mkdir(parents=True, exist_ok=True)
    art1.write_text("seat A evidence\n")
    art2.write_text("seat B evidence\n")
    reg = {"members": {"SeatA": {"role": "reviewer"}, "SeatB": {"role": "critic"}}}
    (tree / ".ufo/waves/round-93/w1/swarm-registry.json").write_text(json.dumps(reg))
    vd = tree / "reports/round-93/votes"
    vd.mkdir(parents=True, exist_ok=True)
    for seat, role, art in (("SeatA", "reviewer", art1), ("SeatB", "critic", art2)):
        v = {"seat": seat, "role": role, "candidate_sha256": want,
             "decisions": {q: "PASS" for q in QS},
             "notes": {q: "clean" for q in QS},
             "artifact_path": str(art.relative_to(tree)),
             "artifact_sha256": hashlib.sha256(art.read_bytes()).hexdigest()}
        (vd / f"{seat}.json").write_text(json.dumps(v))

def write_opens(tree, tail=TAIL):
    o = {"record_sha256": RECORD_SHA, "oracle_tail": tail, "fixture_shas": dict(FIX)}
    (tree / "reports/round-93/opens.json").write_text(json.dumps(o))

def build_c1_positive(name):
    t = TREES / name
    if t.exists():
        shutil.rmtree(t)
    archive(BASE, ["corpus"], t)
    (t / "reports/round-93/votes").mkdir(parents=True)
    (t / "reports/round-93/quote-receipts").mkdir(parents=True)
    (t / ".ufo/waves/round-93/w1").mkdir(parents=True)
    set_row(t / "corpus/README.md", "C08", cite=ENTRY_REL, status="held")
    write_entry(t, "pos")
    for ln in (t / "corpus/README.md").read_text(encoding="utf-8").splitlines():
        if re.match(r"^\|[ \t]*C[0-9]+ ", ln) and ln.rstrip().endswith("| held |"):
            for p in re.findall(r"knowledge/[\w.-]+\.md", ln):
                f = t / "corpus" / p
                if not f.exists():
                    f.parent.mkdir(parents=True, exist_ok=True)
                    f.write_text("fixture stub\n")
    src = t / "corpus/SOURCES.md"
    src.write_text(src.read_text(encoding="utf-8") + S495.format(date="2026-11-05") + "\n",
                   encoding="utf-8")
    write_votes(t)
    write_opens(t)
    (t / "corpus/lint_entry.py").write_text("import sys\nsys.exit(0)\n")
    (t / "corpus/check_embedded_outputs.py").write_text("import sys\nsys.exit(0)\n")
    return t

def restore_base_file(tree, rel):
    ar = subprocess.run(["git", "-C", str(LANE), "archive", BASE, rel], capture_output=True)
    assert ar.returncode == 0, ar.stderr[:200]
    with tarfile.open(fileobj=io.BytesIO(ar.stdout)) as tf:
        data = tf.extractfile(rel).read()
    dst = tree / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)

def build_c2_tree(name, kind):
    t = TREES / name
    if t.exists():
        shutil.rmtree(t)
    archive(BASE, ["corpus"], t)
    rd = t / "corpus/README.md"
    if kind != "base":
        set_row(rd, "C08", cite=ENTRY_REL, status="held")
        e = t / "corpus" / ENTRY_REL
        e.parent.mkdir(parents=True, exist_ok=True)
        e.write_text("stub entry for c2 fixture\n")
        for ln in rd.read_text(encoding="utf-8").splitlines():
            if re.match(r"^\|[ \t]*C[0-9]+ ", ln) and ln.rstrip().endswith("| held |"):
                for p in re.findall(r"knowledge/[\w.-]+\.md", ln):
                    f = t / "corpus" / p
                    if not f.exists():
                        f.parent.mkdir(parents=True, exist_ok=True)
                        f.write_text("fixture stub\n")
    if kind == "rowskill":
        append_row(t, "| C16 | extra probe row | `knowledge/c16-stub.md` | — | held |")
        f = t / "corpus/knowledge/c16-stub.md"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("fixture stub\n")
    elif kind == "seedtok":
        set_row(rd, "C08", cite="knowledge/seed.md", status="held")
        (t / "corpus" / ENTRY_REL).unlink()
    elif kind == "recmut":
        rec = t / "corpus" / RECORD_REL
        rec.write_bytes(rec.read_bytes() + b"x")
    elif kind == "unbacked":
        (t / "corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md").unlink()
    elif kind == "c15held":
        set_row(rd, "C15", status="held")
    elif kind == "c07frontier":
        set_row(rd, "C07", status="frontier")
        rec = t / "corpus/live/runs/round-93-fw/inspection.json"
        rec.parent.mkdir(parents=True, exist_ok=True)
        rec.write_text(json.dumps({"operation": "inspect_firmware_regions",
                                   "evidence_id": "ev_" + "0" * 64,
                                   "normalized_result": {"regions": []}}))
    elif kind == "posfrontier":
        set_row(rd, "C07", status="frontier")
        rec = t / "corpus/live/runs/round-93-fw/inspection.json"
        rec.parent.mkdir(parents=True, exist_ok=True)
        rec.write_text(json.dumps({"operation": "inspect_firmware_regions",
                                   "evidence_id": "ev_" + "0" * 64,
                                   "normalized_result": {"regions": []}}))
    elif kind == "f5partial":
        set_row(rd, "C08", status="partial")
    return t

MUTANTS = [
    # (counter, name, exact old line, replacement)
    ("c1", "c1leg-rows-total",
     '    legs["C1_ROWS_TOTAL"] = len(cov) == 15', '    legs["C1_ROWS_TOTAL"] = True'),
    ("c1", "c1leg-c08-held",
     '    legs["C1_C08_HELD"] = bool(c08) and c08[4] == "held"', '    legs["C1_C08_HELD"] = True'),
    ("c1", "c1leg-c08-cites",
     '    legs["C1_C08_CITES"] = bool(c08) and ENTRY_REL in c08[2] and (root / ENTRY).is_file()',
     '    legs["C1_C08_CITES"] = True'),
    ("c1", "c1leg-admitted",
     '    legs["C1_ADMITTED"] = bool(re.search(r"^admission-status: admitted$", text, re.M))',
     '    legs["C1_ADMITTED"] = True'),
    ("c1", "c1leg-trio",
     '    legs["C1_TRIO"] = all(any(l.startswith(k) for l in head) for k in ("source:", "verified-at:", "recheck:"))',
     '    legs["C1_TRIO"] = True'),
    ("c1", "c1leg-votes", '    legs["C1_VOTES"] = len(votes_ok) >= 2', '    legs["C1_VOTES"] = True'),
    ("c1", "c1leg-lint", '        legs["C1_LINT"] = lint.returncode == 0', '        legs["C1_LINT"] = True'),
    ("c1", "c1leg-embedded", '        legs["C1_EMBEDDED"] = emb.returncode == 0', '        legs["C1_EMBEDDED"] = True'),
    ("c1", "c1leg-embed-nonvacuous", '        legs["C1_EMBED_NONVACUOUS"] = not vacuous',
     '        legs["C1_EMBED_NONVACUOUS"] = True'),
    ("c1", "c1leg-sources", '    legs["C1_SOURCES"] = src_ok', '    legs["C1_SOURCES"] = True'),
    ("c1", "c1leg-quotes", '    legs["C1_QUOTES"] = q_ok', '    legs["C1_QUOTES"] = True'),
    ("c1", "c1leg-opens", '    legs["C1_OPENS"] = o_ok', '    legs["C1_OPENS"] = True'),
    ("c1", "c1leg-k-held-backed", '    legs["C1_K_HELD_BACKED"] = held_backed == 10',
     '    legs["C1_K_HELD_BACKED"] = True'),
    ("c1", "c1gate-all", '    ok = all(legs.values())', '    ok = True'),
    ("c2", "c2leg-rows-total",
     '    legs["C2_ROWS_TOTAL"] = len(five) == 15 and len(rows) == 15', '    legs["C2_ROWS_TOTAL"] = True'),
    ("c2", "c2leg-c08-token",
     '    legs["C2_C08_TOKEN"] = bool(c08) and c08[4] == "held" and entry_ok', '    legs["C2_C08_TOKEN"] = True'),
    ("c2", "c2leg-c08-record",
     '    legs["C2_C08_RECORD"] = rec.is_file() and hashlib.sha256(rec.read_bytes()).hexdigest() == RECORD_SHA',
     '    legs["C2_C08_RECORD"] = True'),
    ("c2", "c2leg-no-new", '    legs["C2_NO_NEW"] = labels["rows"] == []', '    legs["C2_NO_NEW"] = True'),
    ("c2", "c2leg-no-unbacked", '    legs["C2_NO_UNBACKED"] = labels["held"] == labels["backed"]',
     '    legs["C2_NO_UNBACKED"] = True'),
    ("c2", "c2leg-only-c08", '        legs["C2_ONLY_C08"] = moved <= {"C08"}',
     '        legs["C2_ONLY_C08"] = True'),
    ("c2", "c2gate-all", '    ok = all(legs.values())', '    ok = True'),
]

def make_mutants():
    out = {}
    srcs = {"c1": C1_SRC, "c2": C2_SRC}
    for counter, name, old, new in MUTANTS:
        text = srcs[counter].read_text(encoding="utf-8")
        assert text.count(old) == 1, f"{name}: pattern count={text.count(old)}"
        srcs[counter].read_text(encoding="utf-8")  # noqa
        mp = MUTDIR / f"{name}.py"
        mp.write_text(text.replace(old, new), encoding="utf-8")
        out[name] = (counter, old, new, mp)
    return out

def run_counter(script, mode, target, tag):
    env = {**os.environ, "HYAKU_SCRATCH": str(S / "hyaku-env"), "PYTHONUTF8": "1"}
    r = subprocess.run([sys.executable, "-B", str(script), mode, str(target)],
                       capture_output=True, text=True, env=env, timeout=300, cwd=str(S))
    out = r.stdout + r.stderr
    vm = re.search(r"(C1|C2)_VERDICT=(\w+)", out)
    legs = {}
    for k, v in re.findall(r"((?:C1|C2)_[A-Z0-9_]+)=(pass|fail)\b", out):
        legs.setdefault(k, v)
    (LOGS / f"{tag}.log").write_text(out, encoding="utf-8")
    return {"rc": r.returncode, "verdict": vm.group(2) if vm else "none", "legs": legs}

def main():
    TREES.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    MUTDIR.mkdir(parents=True, exist_ok=True)
    results = []
    mut = make_mutants()

    # ---- sanity: harness git repo with alternates ----
    if not (S / ".git").exists():
        subprocess.run(["git", "init", "-q", str(S)], check=True)
        (S / ".git/objects/info").mkdir(parents=True, exist_ok=True)
        (S / ".git/objects/info/alternates").write_text(
            "/home/vgpnk/Projects/shokunin/revenger-shokunin/.git/objects\n")
    top = sh(["git", "-C", str(S), "rev-parse", "--show-toplevel"]).stdout.strip()
    assert top == str(S), f"scratch toplevel {top}"
    ar = sh(["git", "-C", str(S), "cat-file", "-e", f"{BASE}:corpus/README.md"])
    assert ar.returncode == 0, "alternates do not resolve base objects"

    # ---- pristine positive sanity ----
    c1pos = build_c1_positive("c1-positive")
    o = run_counter(C1_SRC, "--tree", c1pos, "sanity-c1-positive-original")
    print("SANITY c1 positive original:", o["verdict"], o["legs"])
    c2pos = build_c2_tree("c2-positive", "pos")
    o2 = run_counter(C2_SRC, "--tree", c2pos, "sanity-c2-positive-original")
    print("SANITY c2 positive original:", o2["verdict"], o2["legs"])
    base1 = build_c2_tree("c2-base", "base")
    od = run_counter(C2_SRC, "--tree", base1, "sanity-c2-donothing-original")
    print("SANITY c2 do-nothing original:", od["verdict"])
    basec1 = build_c2_tree("c1-base", "base")  # bare corpus tree for C1 gate/do-nothing
    od1 = run_counter(C1_SRC, "--tree", basec1, "sanity-c1-donothing-original")
    print("SANITY c1 do-nothing original:", od1["verdict"])

    # ---- per-leg C1 cases ----
    c1_cases = [
        ("c1leg-rows-total", "c1-rows", lambda t: set_row(t / "corpus/README.md", "C02", drop_cell=True)),
        ("c1leg-c08-held", "c1-c08held", lambda t: (set_row(t / "corpus/README.md", "C08", status="uncovered"),
                                                    set_row(t / "corpus/README.md", "C15", status="held"))),
        ("c1leg-c08-cites", "c1-c08cites", lambda t: set_row(t / "corpus/README.md", "C08", cite="knowledge/seed.md")),
        ("c1leg-admitted", "c1-admitted", lambda t: write_entry(t, "cand")),
        ("c1leg-trio", "c1-trio", lambda t: (write_entry(t, "norecheck"), write_votes(t))),
        ("c1leg-votes", "c1-votes", lambda t: (t / "reports/round-93/votes/SeatB.json").unlink()),
        ("c1leg-lint", "c1-lint", lambda t: (write_entry(t, "nocovmap"), write_votes(t),
                                             restore_base_file(t, "corpus/lint_entry.py"))),
        ("c1leg-embedded", "c1-embedded", lambda t: (write_entry(t, "drift"), write_votes(t),
                                                     restore_base_file(t, "corpus/check_embedded_outputs.py"))),
        ("c1leg-embed-nonvacuous", "c1-nonvac", lambda t: (write_entry(t, "vacuous"), write_votes(t))),
        ("c1leg-sources", "c1-sources", lambda t: None),  # built with date variant below
        ("c1leg-quotes", "c1-quotes", lambda t: (write_entry(t, "ext"), write_votes(t),
                                                 src_append(t, S500))),
        ("c1leg-opens", "c1-opens", lambda t: write_opens(t, tail="ORACLE OK (16/17 checks)")),
        ("c1leg-k-held-backed", "c1-khb", lambda t: (t / "corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md").unlink()),
    ]

    def src_append(tree, row):
        p = tree / "corpus/SOURCES.md"
        p.write_text(p.read_text(encoding="utf-8") + row + "\n", encoding="utf-8")

    for mname, tree_name, delta in c1_cases:
        counter, old, new, mpath = mut[mname]
        t = build_c1_positive(tree_name)
        if mname == "c1leg-sources":
            src = t / "corpus/SOURCES.md"
            src.write_text(src.read_text(encoding="utf-8").replace(S495.format(date="2026-11-05"),
                                                                   S495.format(date="2026-11-04")),
                           encoding="utf-8")
        else:
            delta(t)
        orig = run_counter(C1_SRC, "--tree", t, f"{tree_name}-original")
        mu = run_counter(mpath, "--tree", t, f"{tree_name}-mutant")
        mu_pos = run_counter(mpath, "--tree", c1pos, f"{tree_name}-mutant-positive")
        fail = sorted(k for k, v in orig["legs"].items() if v == "fail")
        verdict = "KILLED" if (orig["verdict"] == "fail" and mu["verdict"] == "pass") else "SURVIVED"
        results.append({"mutant": mname, "counter": counter, "old": old.strip(), "new": new.strip(),
                        "tree": tree_name, "orig_verdict": orig["verdict"], "orig_failing": fail,
                        "mut_verdict": mu["verdict"], "mut_on_positive": mu_pos["verdict"],
                        "class": verdict})

    # C1 gate: do-nothing tree must kill
    counter, old, new, mpath = mut["c1gate-all"]
    orig = run_counter(C1_SRC, "--tree", basec1, "c1gate-original")
    mu = run_counter(mpath, "--tree", basec1, "c1gate-mutant")
    fail = sorted(k for k, v in orig["legs"].items() if v == "fail")
    results.append({"mutant": "c1gate-all", "counter": "c1", "old": old.strip(), "new": new.strip(),
                    "tree": "c1-base(do-nothing)", "orig_verdict": orig["verdict"],
                    "orig_failing": fail, "mut_verdict": mu["verdict"], "mut_on_positive": "n/a",
                    "class": "KILLED" if (orig["verdict"] == "fail" and mu["verdict"] == "pass") else "SURVIVED"})

    # ---- per-leg C2 cases ----
    c2_cases = [
        ("c2leg-rows-total", "c2-rowskill", "rowskill"),
        ("c2leg-c08-token", "c2-seedtok", "seedtok"),
        ("c2leg-c08-record", "c2-recmut", "recmut"),
        ("c2leg-no-unbacked", "c2-unbacked", "unbacked"),
        ("c2leg-only-c08", "c2-c15held", "c15held"),
    ]
    for mname, tree_name, kind in c2_cases:
        counter, old, new, mpath = mut[mname]
        t = build_c2_tree(tree_name, kind)
        orig = run_counter(C2_SRC, "--tree", t, f"{tree_name}-original")
        mu = run_counter(mpath, "--tree", t, f"{tree_name}-mutant")
        mu_pos = run_counter(mpath, "--tree", c2pos, f"{tree_name}-mutant-positive")
        fail = sorted(k for k, v in orig["legs"].items() if v == "fail")
        verdict = "KILLED" if (orig["verdict"] == "fail" and mu["verdict"] == "pass") else "SURVIVED"
        results.append({"mutant": mname, "counter": counter, "old": old.strip(), "new": new.strip(),
                        "tree": f"{tree_name}({kind})", "orig_verdict": orig["verdict"],
                        "orig_failing": fail, "mut_verdict": mu["verdict"], "mut_on_positive": mu_pos["verdict"],
                        "class": verdict})

    # C2 NO_NEW: equivalence demonstration (no single-tree kill exists)
    counter, old, new, mpath = mut["c2leg-no-new"]
    for kind, tn in (("c07frontier", "c2-frontier"), ("posfrontier", "c2-posfrontier"), ("f5partial", "c2-f5partial")):
        t = build_c2_tree(tn, kind)
        orig = run_counter(C2_SRC, "--tree", t, f"{tn}-original")
        mu = run_counter(mpath, "--tree", t, f"{tn}-mutant")
        fail = sorted(k for k, v in orig["legs"].items() if v == "fail")
        mufail = sorted(k for k, v in mu["legs"].items() if v == "fail")
        results.append({"mutant": "c2leg-no-new", "counter": "c2", "old": old.strip(), "new": new.strip(),
                        "tree": f"{tn}({kind})", "orig_verdict": orig["verdict"], "orig_failing": fail,
                        "mut_verdict": mu["verdict"], "mut_failing": mufail, "mut_on_positive": "n/a",
                        "class": "EQUIVALENT-candidate"})

    # C2 gate: do-nothing tree must kill
    counter, old, new, mpath = mut["c2gate-all"]
    orig = run_counter(C2_SRC, "--tree", base1, "c2gate-original")
    mu = run_counter(mpath, "--tree", base1, "c2gate-mutant")
    fail = sorted(k for k, v in orig["legs"].items() if v == "fail")
    results.append({"mutant": "c2gate-all", "counter": "c2", "old": old.strip(), "new": new.strip(),
                    "tree": "c2-base(do-nothing)", "orig_verdict": orig["verdict"],
                    "orig_failing": fail, "mut_verdict": mu["verdict"], "mut_on_positive": "n/a",
                    "class": "KILLED" if (orig["verdict"] == "fail" and mu["verdict"] == "pass") else "SURVIVED"})

    (S / "results.json").write_text(json.dumps(results, indent=1))
    print("\n==== RESULTS ====")
    for r in results:
        print(f"{r['class']:22s} {r['mutant']:24s} orig={r['orig_verdict']:4s} "
              f"failing={','.join(r['orig_failing']) or '-'} mutant={r['mut_verdict']:4s} "
              f"mut_on_pos={r.get('mut_on_positive', 'n/a')}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
