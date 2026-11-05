#!/usr/bin/env python3
"""Build mutated scratch-tree copies for the round-99 skip-work dry-runs.

Reads only; writes only under dryruns/mut/. Route mapping:
  r2-header    header/legend-only flip, C0x rows untouched (route: flip header only)
  r4-digest    round-98 votes with candidate_sha256 re-pointed at the round-99 digest
  r5-artifact  r4 + all FAIL decisions forced to PASS + one forged voter whose
               artifact file does not exist
  r6-notes     one PASS note copied verbatim between two voters
  r7-receipt   S506.receipt.json fetched_at drifted one day back
"""
import json, shutil, sys
from pathlib import Path

DIGEST = "36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5"
SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])
VOTES = "reports/round-98/votes"
README_LINES = {
    "legend": "Status: `held` — at least one admitted knowledge entry covers the ground;",
    "tabhdr": "| row | surface | knowledge entries | work evidence | status |",
}


def fresh(name):
    dst = OUT / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(SRC, dst, symlinks=True)
    return dst


def rd(p):
    return p.read_text(encoding="utf-8")


def wr(p, s):
    p.write_text(s, encoding="utf-8")


def vote(dst, name):
    return json.loads((dst / VOTES / name).read_text(encoding="utf-8"))


def save(dst, name, v):
    (dst / VOTES / name).write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n",
                                    encoding="utf-8")


OUT.mkdir(parents=True, exist_ok=True)

# r2-header
d = fresh("r2-header")
p = d / "corpus/README.md"
t = rd(p)
assert t.count(README_LINES["legend"]) == 1 and t.count(README_LINES["tabhdr"]) == 1
t = t.replace(README_LINES["legend"],
              README_LINES["legend"] + " (probe: legend flipped, rows untouched)")
t = t.replace(README_LINES["tabhdr"],
              "| row | surface | knowledge entries | work evidence | state |")
wr(p, t)
print("r2-header: legend + table-header lines edited; C0x rows untouched")

# r4-digest
d = fresh("r4-digest")
for f in sorted((d / VOTES).glob("*.json")):
    v = json.loads(f.read_text(encoding="utf-8"))
    v["candidate_sha256"] = DIGEST
    f.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("r4-digest: candidate_sha256 re-pointed in", sorted(x.name for x in (d / VOTES).glob("*.json")))

# r5-artifact (from a fresh r4-style copy, plus forced PASS + forged voter)
d = fresh("r5-artifact")
for f in sorted((d / VOTES).glob("*.json")):
    v = json.loads(f.read_text(encoding="utf-8"))
    v["candidate_sha256"] = DIGEST
    for q, dec in list(v.get("decisions", {}).items()):
        if dec == "FAIL":
            v["decisions"][q] = "PASS"
    f.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
probe = vote(d, "ReviewerGate.json")
probe["seat"] = "ReviewerClaims"
probe["artifact_path"] = ".ufo/waves/round-98/w1/ReviewerClaims/audit-missing.md"
probe["artifact_sha256"] = "0" * 64
(d / VOTES / "ReviewerClaims.json").write_text(
    json.dumps(probe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for seat in ("CriticR98", "ReviewerBlind", "ReviewerGate"):
    ap = json.loads((d / VOTES / f"{seat}.json").read_text(encoding="utf-8"))["artifact_path"]
    print(f"r5-artifact: {seat} artifact exists={(d / ap).is_file()} path={ap}")

# r6-notes
d = fresh("r6-notes")
g = vote(d, "ReviewerGate.json")
b = vote(d, "ReviewerBlind.json")
pick = None
for q in sorted(g.get("decisions", {})):
    note = str(g.get("notes", {}).get(q, ""))
    if g["decisions"][q] == "PASS" and len(note.split()) >= 6:
        pick = q
        break
assert pick, "no PASS note >=6 tokens in ReviewerGate"
b["decisions"][pick] = "PASS"
b.setdefault("notes", {})[pick] = g["notes"][pick]
save(d, "ReviewerBlind.json", b)
print(f"r6-notes: copied ReviewerGate {pick} note verbatim into ReviewerBlind ({pick} decision forced PASS)")

# r7-receipt
d = fresh("r7-receipt")
p = d / "reports/round-98/quote-receipts/S506.receipt.json"
v = json.loads(rd(p))
assert v["fetched_at"] == "2026-11-05", v["fetched_at"]
v["fetched_at"] = "2026-11-04"
wr(p, json.dumps(v, ensure_ascii=False, indent=2) + "\n")
print("r7-receipt: S506 fetched_at 2026-11-05 -> 2026-11-04")

print("done")
