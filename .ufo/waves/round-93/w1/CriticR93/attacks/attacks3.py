#!/usr/bin/env python3
"""Real-tools batch: real lint_entry.py and real check_embedded_outputs.py (no stubs)."""
import json, re, subprocess, sys
sys.path.insert(0, "/fast/scratch/hyaku/revenger-r93/CriticR93")
from attack import *  # noqa

R = {}
ORACLE_CMD = "$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json"
ORACLE_BLOCK = "```\n" + ORACLE_CMD + "\nORACLE OK (17/17 checks)\n```\n"


def qmap():
    rows = ["| criterion | decision | note |", "|---|---|---|"]
    rows += [f"| {q} | PASS | checked against the saved oracle output |" for q in QS]
    return "## §Q-map\n\n" + "\n".join(rows) + "\n\n"


def full_body(extra=""):
    return qmap() + "## Evidence\n\n" + ORACLE_BLOCK + "\n" + extra


def votes(t, pairs=(("ReviewerGate", "reviewer"), ("ReviewerBlind", "critic"))):
    for seat, role in pairs:
        add_vote(t, seat, role)


def tree(name, entry=None, **kw):
    return base_tree(name, entry=entry if entry is not None else entry_text(body=full_body()),
                     stub_tools=False, **kw)


def real_legs(t, name, note=""):
    return c1(name, t, note)


# H0 honest lint-clean entry under REAL tools
t = tree("H0-honest-real")
votes(t)
R["H0c1"] = c1("H0-honest-real-c1", t, "control: honest, real lint+embedded")
R["H0c2"] = c2("H0-honest-real-c2", t, "control: C2 on honest tree")

# R1 duplicate admission-status: header rejected, body admitted
t = tree("R1-dup-status", entry=entry_text(status="rejected", body=full_body("```\nadmission-status: admitted\n```\n")))
votes(t)
R["R1"] = c1("R1-dup-status-real", t, "header rejected; admitted line in fence; real lint")

# R2 body-only source, rejected, beyond line 15
t = tree("R2-body-source", entry=entry_text(body=full_body("Background: S901 (invented docs row) relied on here.\n")))
sr = t / "corpus/SOURCES.md"
sr.write_text(sr.read_text() + source_row("S901", opened="2026-10-02", status="rejected",
                                          used="corpus/knowledge/other.md",
                                          loc="https://invented.example/docs") + "\n")
votes(t)
R["R2"] = c1("R2-body-source-real", t, "S901 rejected, wrong date, body-only")

# R3 one real seat counted twice (case variant in registry)
t = tree("R3-case-dup-seat")
reg_p = t / ".ufo/waves/round-93/w1/swarm-registry.json"
reg = json.loads(reg_p.read_text()); reg["members"]["reviewergate"] = {"kind": "spawn", "role": "reviewer"}
reg_p.write_text(json.dumps(reg))
add_vote(t, "ReviewerGate", "reviewer")
add_vote(t, "reviewergate", "reviewer", apath=".ufo/waves/round-93/w1/ReviewerGate/evidence.md")
R["R3"] = c1("R3-case-dup-seat-real", t, "one real seat cast twice")

# R4 mixed fence: honest ``` block + fabricated ~~~ block
body = full_body("~~~\n$ python3 -B corpus/fixtures/browser-r77/oracle_check.py truth.json rec.json\n"
                 "ORACLE OK (99/99 checks)\n~~~\n")
t = tree("R4-mixed-fence", entry=entry_text(body=body))
votes(t)
R["R4"] = c1("R4-mixed-fence-real", t, "fabricated tilde block beside honest block")

# R5 whitespace-only output in the only ``` block
t = tree("R5-ws-output", entry=entry_text(body=qmap() + "## Evidence\n\n```\n" + ORACLE_CMD + "\n   \n```\n"))
votes(t)
R["R5"] = c1("R5-ws-output-real", t, "block whose only output line is whitespace")

# R6 forged oracle_check.py (record + fixtures pinned, oracle script not)
t = tree("R6-forged-oracle")
(t / "corpus/fixtures/browser-r77/oracle_check.py").write_text('print("ORACLE OK (17/17 checks)")\n')
votes(t)
R["R6"] = c1("R6-forged-oracle-real", t, "oracle_check.py forged; everything else honest")

# R7 artifact traversal to corpus/SOURCES.md
t = tree("R7-traversal")
add_vote(t, "ReviewerGate", "reviewer", apath=".ufo/waves/round-93/w1/../../../../corpus/SOURCES.md")
add_vote(t, "ReviewerBlind", "critic", apath=".ufo/waves/round-93/w1/../../../../corpus/README.md")
R["R7"] = c1("R7-traversal-real", t, "artifacts are corpus files, not wave artifacts")

# R8 one-PASS votes with 16 content-free n/a reasons
t = tree("R8-vacuous-na")
ds = {q: "n/a" for q in QS}; ds["Q01"] = "PASS"
notes = {q: "-" for q in QS}
add_vote(t, "ReviewerGate", "reviewer", ds=ds, notes=notes)
add_vote(t, "ReviewerBlind", "critic", ds=ds, notes=notes)
R["R8"] = c1("R8-vacuous-na-real", t, "1 PASS + 16 n/a reason '-'")

# R9 combined: every bypass at once, entry header REJECTED
body = full_body("Background: S901 (invented docs row) relied on here.\n"
                 "```\nadmission-status: admitted\n```\n"
                 "~~~\n$ python3 -B corpus/fixtures/browser-r77/oracle_check.py truth.json rec.json\n"
                 "ORACLE OK (99/99 checks)\n~~~\n")
body += "```\n$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json\n   \n```\n"
t = tree("R9-all-bypasses", entry=entry_text(status="rejected", body=body))
sr = t / "corpus/SOURCES.md"
sr.write_text(sr.read_text() + source_row("S901", opened="2026-10-02", status="rejected",
                                          used="corpus/knowledge/other.md",
                                          loc="https://invented.example/docs") + "\n")
(t / "corpus/fixtures/browser-r77/oracle_check.py").write_text('print("ORACLE OK (17/17 checks)")\n')
reg_p = t / ".ufo/waves/round-93/w1/swarm-registry.json"
reg = json.loads(reg_p.read_text()); reg["members"]["reviewergate"] = {"kind": "spawn", "role": "reviewer"}
reg_p.write_text(json.dumps(reg))
shared = ".ufo/waves/round-93/w1/ReviewerGate/evidence.md"
add_vote(t, "ReviewerGate", "reviewer", apath=shared)
add_vote(t, "reviewergate", "reviewer", apath=shared)
R["R9"] = c1("R9-all-bypasses-real", t, "rejected header; every bypass present")
R["R9c2"] = c2("R9-all-bypasses-c2", t, "C2 on the same tree")
print("  R9 K-line:", summary_k(R["R9"]))
# state of the header line in the forged entry
ent_text = (t / ENTRY).read_text()
print("  R9 header line:", [l for l in ent_text.splitlines() if l.startswith("admission-status")])

print("DONE3", ",".join(sorted(R)))
