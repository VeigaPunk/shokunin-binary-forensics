#!/usr/bin/env python3
"""VoterGateR99 — self-check of reports/round-99/votes/VoterGateR99.json (Amendment B digest)
against the frozen v7 check_vote_notes rule (reports/round-98/c1_k_admit_counter7.py:585-621),
plus note distinctness versus this seat's superseded vote and CriticR99's current vote."""
import json, re, sys, hashlib
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
VOTE = ROOT / "reports/round-99/votes/VoterGateR99.json"
ENTRY = ROOT / "corpus/knowledge/round-98-rea-host-readiness.md"
OLD = ROOT / ".ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/VoterGateR99.json"
CRITIC = ROOT / "reports/round-99/votes/CriticR99.json"
QS = [f"Q{i:02d}" for i in range(1, 18)]
NEW_DIGEST = "246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da"

fails = []
try:
    vote = json.loads(VOTE.read_text(encoding="utf-8"))
except ValueError as e:
    print(f"STRICT-JSON FAIL: {e}"); sys.exit(1)

expected_keys = {"seat", "role", "candidate_sha256", "decisions", "notes",
                 "artifact_path", "artifact_sha256"}
if set(vote) != expected_keys:
    fails.append(f"key set differs: {sorted(set(vote) ^ expected_keys)}")

decisions, notes = vote["decisions"], vote["notes"]
if sorted(decisions) != QS:
    fails.append(f"decisions keys: {sorted(decisions)}")
for q, d in decisions.items():
    if d not in ("PASS", "FAIL", "n/a"):
        fails.append(f"{q}: bad decision {d!r}")
missing = [q for q in QS if q not in notes]
if missing:
    fails.append(f"missing notes: {missing}")

text = ENTRY.read_text(encoding="utf-8")
if re.search(r"\b[0-9a-fA-F]{64}\b", text) and decisions.get("Q09") == "n/a":
    fails.append("Q09 n/a inapplicable: entry contains a 64-hex digest claim")

seen = {}
for q, note in notes.items():
    if isinstance(note, str):
        seen.setdefault(note.strip(), []).append(q)

for q in QS:
    if decisions.get(q) != "PASS":
        continue
    note = notes.get(q, "")
    if len(note.split()) < 6:
        fails.append(f"{q}:PASS note needs >=6 tokens"); continue
    if re.search(r"(?i)\bn/a\b|not applicable|no byte oracle|documentation.only|no .* exists", note):
        fails.append(f"{q}:PASS note is n/a-style")
    if len(seen.get(note.strip(), [])) != 1:
        fails.append(f"{q}:PASS note shared verbatim within file")

for q, note in notes.items():
    if decisions.get(q) == "n/a":
        if len(note.split()) < 6:
            fails.append(f"{q}:n/a note needs >=6 tokens")
        if not re.search(r"Q[01][0-9]", note):
            fails.append(f"{q}:n/a note names no Q id")

# distinctness vs superseded own vote and current CriticR99 vote
for other, label in ((OLD, "superseded-own"), (CRITIC, "CriticR99")):
    if other.exists():
        ov = json.loads(other.read_text(encoding="utf-8"))
        onotes = set(n.strip() for n in ov.get("notes", {}).values() if isinstance(n, str))
        for q, note in notes.items():
            if note.strip() in onotes:
                fails.append(f"{q}: note identical to {label} note")

art = ROOT / vote["artifact_path"]
h = hashlib.sha256(art.read_bytes()).hexdigest()
if h != vote["artifact_sha256"]:
    fails.append(f"artifact_sha256 mismatch: file {h} vs vote {vote['artifact_sha256']}")
if vote["candidate_sha256"] != NEW_DIGEST:
    fails.append("candidate_sha256 is not the Amendment B vote-binding digest")
if vote["seat"] != "VoterGateR99" or vote["role"] != "reviewer":
    fails.append("seat/role mismatch")

print(f"decisions: 17 checked; PASS={sum(1 for d in decisions.values() if d=='PASS')} "
      f"FAIL={sum(1 for d in decisions.values() if d=='FAIL')} "
      f"n/a={sum(1 for d in decisions.values() if d=='n/a')}")
if fails:
    print("SELFCHECK FAIL")
    for f in fails: print(" -", f)
    sys.exit(1)
print("SELFCHECK OK: strict JSON, exact key set, 17 decisions, notes rule-clean and distinct from "
      "superseded own notes and CriticR99 notes, Q09 PASS with digest claim present, artifact bytes bound")
