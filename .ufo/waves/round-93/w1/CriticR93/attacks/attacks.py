#!/usr/bin/env python3
import json, re, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, "/fast/scratch/hyaku/revenger-r93/CriticR93")
from attack import *  # noqa

which = sys.argv[1:] or ["all"]
R = {}


def want(n):
    return "all" in which or n in which


def reg_path(t):
    return t / ".ufo/waves/round-93/w1/swarm-registry.json"


# A0 honest-shaped control (lint/embedded stubbed, as the frozen self-test does)
if want("A0"):
    t = honest("A0-honest")
    R["A0c1"] = c1("A0-honest-c1", t, "control: must pass")
    R["A0c2"] = c2("A0-honest-c2", t, "control: C2 on honest tree")

# A1 two distinct registry seats, ONE shared artifact file + sha
if want("A1"):
    t = base_tree("A1-shared-artifact")
    shared = ".ufo/waves/round-93/w1/ReviewerGate/evidence.md"
    add_vote(t, "ReviewerGate", "reviewer", apath=shared)
    add_vote(t, "ReviewerBlind", "critic", apath=shared)
    R["A1"] = c1("A1-shared-artifact", t, "two seats, same bytes+path")

# A2 artifact_path traversal that still starts with the wave prefix (4 x '..' reaches root)
if want("A2"):
    t = base_tree("A2-traversal")
    add_vote(t, "ReviewerGate", "reviewer", apath=".ufo/waves/round-93/w1/../../../../corpus/SOURCES.md")
    add_vote(t, "ReviewerBlind", "critic", apath=".ufo/waves/round-93/w1/../../../../reports/round-93/opens.json")
    R["A2"] = c1("A2-traversal", t, "artifacts resolve to corpus/SOURCES.md and opens.json")

# A3 registry self-attested: fabricated seats in the same wave registry + bound junk artifacts
if want("A3"):
    t = base_tree("A3-forged-registry")
    reg = json.loads(reg_path(t).read_text())
    reg["members"]["FabA"] = {"kind": "spawn", "role": "reviewer"}
    reg["members"]["FabB"] = {"kind": "spawn", "role": "critic"}
    reg_path(t).write_text(json.dumps(reg))
    add_vote(t, "FabA", "reviewer", art_text="x\n")
    add_vote(t, "FabB", "critic", art_text="x\n")
    R["A3"] = c1("A3-forged-registry", t, "fabricated seats added to registry, artifacts junk")

    # A3b: the battery's F1 shape without artifact binding (control: must die)
    t = base_tree("A3b-f1-shape")
    reg = json.loads(reg_path(t).read_text())
    reg["members"]["FabA"] = {"kind": "spawn", "role": "reviewer"}
    reg["members"]["FabB"] = {"kind": "spawn", "role": "critic"}
    reg_path(t).write_text(json.dumps(reg))
    for seat, role in (("FabA", "reviewer"), ("FabB", "critic")):
        v = {"seat": seat, "role": role, "candidate_sha256": digest((t / ENTRY).read_text()),
             "decisions": {q: "PASS" for q in QS}, "notes": {q: "clean" for q in QS}}
        (t / "reports/round-93/votes" / f"{seat}.json").write_text(json.dumps(v))
    R["A3b"] = c1("A3b-f1-shape-no-artifact", t, "control: expect kill (no artifact binding)")

# A4 empty artifact (zero bytes, sha of empty string) bound to two votes
if want("A4"):
    t = base_tree("A4-empty-artifact")
    add_vote(t, "ReviewerGate", "reviewer", art_text="")
    add_vote(t, "ReviewerBlind", "critic", art_text="")
    R["A4"] = c1("A4-empty-artifact", t, "zero-byte artifacts")

# A5 the vote's artifact is the registry JSON itself (content unrelated to the entry)
if want("A5"):
    t = base_tree("A5-registry-as-artifact")
    rp = ".ufo/waves/round-93/w1/swarm-registry.json"
    add_vote(t, "ReviewerGate", "reviewer", apath=rp)
    add_vote(t, "ReviewerBlind", "critic", apath=rp)
    R["A5"] = c1("A5-registry-as-artifact", t, "artifact = registry json, no mention of candidate digest")

# A6 forged oracle script: record + 2 fixture pins still pass
if want("A6"):
    t = honest("A6-forged-oracle")
    (t / "corpus/fixtures/browser-r77/oracle_check.py").write_text(
        'import sys\nprint("ORACLE OK (17/17 checks)")\n', encoding="utf-8")
    R["A6"] = c1("A6-forged-oracle", t, "oracle_check.py replaced; only record+2 fixtures pinned")

# A6b: truth.json (oracle input) is unpinned; semantic change to truth
if want("A6b"):
    t = honest("A6b-truth-json")
    truth = json.loads((t / "corpus/fixtures/browser-r77/truth.json").read_text())
    s = json.dumps(truth)
    (t / "corpus/fixtures/browser-r77/truth.json").write_text(s.replace("17", "17", 1) + "\n", encoding="utf-8")
    R["A6b"] = c1("A6b-truth-json-touched", t, "truth.json rewritten (unpinned input)")

# A7 opens.json: stale fixture sha, correct record sha
if want("A7"):
    t = honest("A7-stale-opens")
    write_opens(t, fixture_shas={"index.html": FIX["index.html"], "app.js": "0" * 64})
    R["A7"] = c1("A7-stale-opens", t, "record sha correct, one fixture sha stale")

# A8 header S-row opened one day off
if want("A8"):
    t = base_tree("A8-date-off", s495_row=source_row("S495", opened="2026-11-04"))
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    R["A8"] = c1("A8-date-off", t, "S495 opened 2026-11-04 in SOURCES")

# A9 body-only source citation, beyond the 15-line header window the counter scans
if want("A9"):
    filler = "".join(f"Filler line {i} of the entry body.\n" for i in range(12))
    body = filler + "Background: S901 (invented docs row) states the browser runtime behaviour this entry relies on.\n"
    t = base_tree("A9-body-source", entry=entry_text(body=body))
    sr = t / "corpus/SOURCES.md"
    sr.write_text(sr.read_text() + source_row("S901", opened="2026-10-02", status="rejected",
                                              used="corpus/knowledge/other.md",
                                              loc="https://invented.example/docs") + "\n")
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    head = (t / ENTRY).read_text().splitlines()[:15]
    print("  A9 S901 in head window:", any("S901" in l for l in head))
    R["A9"] = c1("A9-body-source", t, "S901 rejected+wrong date+wrong used-by, cited only in body after line 15")

# A10 duplicate admission-status line: header rejected, body line admitted
if want("A10"):
    body = "```\nadmission-status: admitted\n```\n"
    t = base_tree("A10-dup-status", entry=entry_text(status="rejected", body=body))
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    R["A10"] = c1("A10-dup-status", t, "header rejected; body has admission-status: admitted")

# A11 entry admission-status rejected, C08 held citing it (K target without admission)
if want("A11"):
    t = base_tree("A11-rejected-k", entry=entry_text(status="rejected"))
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    r = c1("A11-rejected-k", t, "rejected entry named in C08")
    print("  A11 K-line:", summary_k(r))
    R["A11"] = r

# A12 K=10 without ANY entry file: C08 held citing an existing seed file
if want("A12"):
    t = base_tree("A12-seed-k")
    rd = t / "corpus/README.md"
    rows = []
    for l in rd.read_text().splitlines():
        if re.match(r"^\|[ \t]*C08 ", l):
            c = cells(l)
            l = "| " + " | ".join([c[0], c[1], "`knowledge/seed.md`", c[3], "held"]) + " |"
        rows.append(l)
    rd.write_text("\n".join(rows) + "\n")
    add_vote(t, "ReviewerGate", "reviewer", sha=sh(b"placeholder"))
    add_vote(t, "ReviewerBlind", "critic", sha=sh(b"placeholder"))
    (t / ENTRY).unlink()
    R["A12"] = c1("A12-seed-k", t, "no entry file at all; C08 held citing knowledge/seed.md")
    print("  A12 K-line:", summary_k(R["A12"]))

# A13 votes with seat name differing only by case from the registry member
if want("A13"):
    t = base_tree("A13-case-seat")
    add_vote(t, "reviewergate", "reviewer", apath=".ufo/waves/round-93/w1/ReviewerGate/evidence.md")
    add_vote(t, "reviewerblind", "critic", apath=".ufo/waves/round-93/w1/ReviewerBlind/evidence.md")
    R["A13"] = c1("A13-case-seat", t, "lowercase seats vs registry ReviewerGate/ReviewerBlind")

# A14 tilde-fenced fabricated output: REAL check_embedded_outputs.py, stubbed lint
if want("A14"):
    body = ("~~~\n$ python3 -B corpus/fixtures/browser-r77/oracle_check.py truth.json rec.json\n"
            "ORACLE OK (99/99 checks)\n~~~\n")
    t = base_tree("A14-tilde-fence", entry=entry_text(body=body), stub_tools=True)
    archive(BASE, ["corpus/check_embedded_outputs.py"], t)  # restore REAL checker
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    R["A14"] = c1("A14-tilde-fence", t, "real check_embedded_outputs.py; fabricated output in ~~~ fence")
    emb = subprocess.run([sys.executable, "-B", "corpus/check_embedded_outputs.py", "--entry", ENTRY],
                         cwd=str(t), capture_output=True, text=True)
    print("  A14 real checker rc=", emb.returncode, (emb.stdout + emb.stderr).strip()[-200:])

# A15 C2 second row moved to held (backed by an existing file), C08 honest
if want("A15"):
    t = honest("A15-second-row")
    rd = t / "corpus/README.md"
    moved = None
    out = []
    for l in rd.read_text().splitlines():
        m = re.match(r"^\|[ \t]*(C\d+) ", l)
        c = cells(l) if m else None
        if (moved is None and m and c and len(c) == 5 and c[0] != "C08"
                and c[4] in ("uncovered", "partial", "frontier")
                and re.findall(r"knowledge/[\w.-]+\.md", c[2])
                and all((t / "corpus" / f).is_file() for f in re.findall(r"knowledge/[\w.-]+\.md", c[2]))):
            moved = c[0]
            c[4] = "held"
            l = "| " + " | ".join(c) + " |"
        out.append(l)
    rd.write_text("\n".join(out) + "\n")
    print("  A15 moved row:", moved)
    R["A15c2"] = c2("A15-second-row-c2", t, "C08 held+entry AND a second row moved to held")

# A16 C2 positive with a zero-byte entry file (token-only, no content check)
if want("A16"):
    t = base_tree("A16-zero-entry", entry="")
    R["A16"] = c2("A16-zero-byte-entry-c2", t, "C2 token passes with empty entry")

# A17 n/a reasons are content-free; one PASS vote carries 16 n/a
if want("A17"):
    t = base_tree("A17-vacuous-na")
    ds = {q: "n/a" for q in QS}
    ds["Q01"] = "PASS"
    notes = {q: "-" for q in QS}
    add_vote(t, "ReviewerGate", "reviewer", ds=ds, notes=notes)
    add_vote(t, "ReviewerBlind", "critic", ds=ds, notes=notes)
    R["A17"] = c1("A17-vacuous-na", t, "1 PASS + 16 n/a with reason '-'")

# A18 honest entry with REAL lint + embedded (no stubs)
if want("A18"):
    t = base_tree("A18-real-tools", stub_tools=False)
    add_vote(t, "ReviewerGate", "reviewer")
    add_vote(t, "ReviewerBlind", "critic")
    R["A18"] = c1("A18-real-tools", t, "honest entry, real lint/embedded")

# A19 registry deleted on an otherwise honest tree (battery F3 shape)
if want("A19"):
    t = honest("A19-no-registry")
    reg_path(t).unlink()
    R["A19c1"] = c1("A19-no-registry-c1", t, "battery F3 shape on honest tree")
    R["A19c2"] = c2("A19-no-registry-c2", t, "C2 must be unaffected by registry")

# A20 lowercase registry key added alongside the real one; honest votes unchanged
if want("A20"):
    t = honest("A20-extra-seat")
    reg = json.loads(reg_path(t).read_text())
    reg["members"]["reviewergate"] = {"kind": "spawn", "role": "reviewer"}
    reg_path(t).write_text(json.dumps(reg))
    R["A20"] = c1("A20-lowercase-registry-key", t, "registry key added in lowercase; honest votes unchanged")

print("DONE", ",".join(sorted(R)))
