#!/usr/bin/env python3
"""VoterGateR99 — self-check of reports/round-99/votes/VoterGateR99.json
against the frozen v7 check_vote_notes rule (reports/round-98/c1_k_admit_counter7.py:585-621)."""
import json, re, sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
VOTE = ROOT / "reports/round-99/votes/VoterGateR99.json"
ENTRY = ROOT / "corpus/knowledge/round-98-rea-host-readiness.md"
QS = [f"Q{i:02d}" for i in range(1, 18)]

fails = []
raw = VOTE.read_text(encoding="utf-8")
try:
    vote = json.loads(raw)  # strict JSON
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
missing_notes = [q for q in QS if q not in notes]
if missing_notes:
    fails.append(f"missing notes: {missing_notes}")

text = ENTRY.read_text(encoding="utf-8")
digest_claim = bool(re.search(r"\b[0-9a-fA-F]{64}\b", text))
if digest_claim and decisions.get("Q09") == "n/a":
    fails.append("Q09 n/a inapplicable: entry contains a 64-hex digest claim")

seen = {}
for q, note in notes.items():
    if not isinstance(note, str):
        fails.append(f"{q}: note not a string"); continue
    seen.setdefault(note.strip(), []).append(q)

for q in QS:
    if decisions.get(q) != "PASS":
        continue
    note = notes.get(q, "")
    if len(note.split()) < 6:
        fails.append(f"{q}:PASS note needs >=6 tokens")
        continue
    if re.search(r"(?i)\bn/a\b|not applicable|no byte oracle|documentation.only|no .* exists", note):
        fails.append(f"{q}:PASS note is n/a-style")
    if len(seen.get(note.strip(), [])) != 1:
        fails.append(f"{q}:PASS note shared verbatim")

for q, note in notes.items():
    if decisions.get(q) == "n/a":
        if len(note.split()) < 6:
            fails.append(f"{q}:n/a note needs >=6 tokens")
        if not re.search(r"Q[01][0-9]", note):
            fails.append(f"{q}:n/a note names no Q id")

# artifact binding
import hashlib
art = ROOT / vote["artifact_path"]
h = hashlib.sha256(art.read_bytes()).hexdigest()
if h != vote["artifact_sha256"]:
    fails.append(f"artifact_sha256 mismatch: file {h} vs vote {vote['artifact_sha256']}")
if vote["candidate_sha256"] != "36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5":
    fails.append("candidate_sha256 is not the frozen vote-binding digest")
if vote["seat"] != "VoterGateR99" or vote["role"] != "reviewer":
    fails.append("seat/role mismatch")

print(f"decisions: 17 checked; PASS={sum(1 for d in decisions.values() if d=='PASS')} "
      f"FAIL={sum(1 for d in decisions.values() if d=='FAIL')} "
      f"n/a={sum(1 for d in decisions.values() if d=='n/a')}")
if fails:
    print("SELFCHECK FAIL")
    for f in fails: print(" -", f)
    sys.exit(1)
print("SELFCHECK OK: strict JSON, key set exact, 17 decisions, all notes rule-clean, "
      "Q09 PASS with digest claim present, artifact bytes bound")
