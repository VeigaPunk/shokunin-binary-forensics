#!/usr/bin/env python3
import json, re, subprocess, sys
sys.path.insert(0, "/fast/scratch/hyaku/revenger-r93/CriticR93")
from attack import *  # noqa

R = {}
ORACLE_CMD = "$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json"

# A21a one real seat counted twice via a case-variant registry key
t = base_tree("A21a-case-dup-seat")
reg_p = t / ".ufo/waves/round-93/w1/swarm-registry.json"
reg = json.loads(reg_p.read_text())
reg["members"]["reviewergate"] = {"kind": "spawn", "role": "reviewer"}
reg_p.write_text(json.dumps(reg))
add_vote(t, "ReviewerGate", "reviewer")
add_vote(t, "reviewergate", "reviewer", apath=".ufo/waves/round-93/w1/ReviewerGate/evidence.md")
R["A21a"] = c1("A21a-case-dup-seat", t, "ONE real seat (ReviewerGate) cast twice as two distinct seats")

# A21b trailing-space variant of the same seat
t = base_tree("A21b-space-dup-seat")
reg_p = t / ".ufo/waves/round-93/w1/swarm-registry.json"
reg = json.loads(reg_p.read_text())
reg["members"]["ReviewerGate "] = {"kind": "spawn", "role": "reviewer"}
reg_p.write_text(json.dumps(reg))
add_vote(t, "ReviewerGate", "reviewer")
add_vote(t, "ReviewerGate ", "reviewer", apath=".ufo/waves/round-93/w1/ReviewerGate/evidence.md")
R["A21b"] = c1("A21b-space-dup-seat", t, "trailing-space registry key counted as a second seat")

# A14b mixed fence: one honest ``` block (real command, real output line) + fabricated ~~~ block
body = (ORACLE_CMD[0:] + "\n")  # placeholder, replaced below
body = ("```\n" + ORACLE_CMD + "\nORACLE OK (17/17 checks)\n```\n"
        "~~~\n$ python3 -B corpus/fixtures/browser-r77/oracle_check.py truth.json rec.json\n"
        "ORACLE OK (99/99 checks)\nFORGED LINE 2\n~~~\n")
t = base_tree("A14b-mixed-fence", entry=entry_text(body=body), stub_tools=True)
archive(BASE, ["corpus/check_embedded_outputs.py"], t)
add_vote(t, "ReviewerGate", "reviewer")
add_vote(t, "ReviewerBlind", "critic")
R["A14b"] = c1("A14b-mixed-fence", t, "real checker; one honest ``` block + fabricated ~~~ block")
emb = subprocess.run([sys.executable, "-B", "corpus/check_embedded_outputs.py", "--entry", ENTRY],
                     cwd=str(t), capture_output=True, text=True)
print("  A14b real checker rc=", emb.returncode, (emb.stdout + emb.stderr).strip()[-300:])

# A27 whitespace-only output line defeats the counter-level nonvacuous leg
body = ("```\n" + ORACLE_CMD + "\n   \n```\n")
t = base_tree("A27-ws-output", entry=entry_text(body=body), stub_tools=True)
archive(BASE, ["corpus/check_embedded_outputs.py"], t)
add_vote(t, "ReviewerGate", "reviewer")
add_vote(t, "ReviewerBlind", "critic")
R["A27"] = c1("A27-ws-output", t, "block whose only output is a whitespace-only line")
emb = subprocess.run([sys.executable, "-B", "corpus/check_embedded_outputs.py", "--entry", ENTRY],
                     cwd=str(t), capture_output=True, text=True)
print("  A27 real checker rc=", emb.returncode, (emb.stdout + emb.stderr).strip()[-300:])

# A23 control: external header row with no fetch receipt (must die in C1_QUOTES)
head_extra = "source-2: S496 https://example.org/spec-page (docs, tier A, opened 2026-11-05)"
ent = entry_text(head_extra=head_extra)
t = base_tree("A23-external-no-receipt", entry=ent)
sr = t / "corpus/SOURCES.md"
sr.write_text(sr.read_text() + source_row("S496", loc="https://example.org/spec-page", kind="docs") + "\n")
add_vote(t, "ReviewerGate", "reviewer")
add_vote(t, "ReviewerBlind", "critic")
R["A23"] = c1("A23-external-no-receipt", t, "control: external header row, no receipts")

# A18 lint probe: real lint_entry on the dup-status and body-source trees and on the honest real-tools tree
for name in ("A10-dup-status", "A9-body-source", "A18-real-tools"):
    tt = TREES / name
    lr = subprocess.run([sys.executable, "-B", "corpus/lint_entry.py", "--entry", ENTRY, "--lane", str(LANE)],
                        cwd=str(tt), capture_output=True, text=True)
    print(f"  LINT {name}: rc={lr.returncode} :: {(lr.stdout + lr.stderr).strip()[-260:]!r}")

print("DONE2", ",".join(sorted(R)))
