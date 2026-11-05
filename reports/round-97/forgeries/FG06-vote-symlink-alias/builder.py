# Forgery vector FG06-vote-symlink-alias (r97 port of CriticR96 fg06_symlink_alias).
# Source: .ufo/waves/round-96/w1/CriticR96/receipts/drv.py :: FORGERIES entry
# (expected under frozen v5: pass).
# File mutations below are copied verbatim from that builder; only the
# root/mod binding is supplied by the harness (forge_reach6.py).
import hashlib, json, os, re
from pathlib import Path

WAVE_DIR = ".ufo/waves/round-96"
SEATS = (("ReviewerGate", "reviewer", "gate-evidence.md"),
         ("ReviewerBlind", "reviewer", "blind-evidence.md"),
         ("CriticR96", "critic", "critic-evidence.md"))

mod = None
VOTES_DIR = None

def _bind(mod_obj):
    global mod, VOTES_DIR
    mod = mod_obj
    VOTES_DIR = mod.VOTES_DIR

def repin(root):
    "Re-pin the three votes to the current entry digest (forger owns the tree)."
    text = (root / mod.ENTRY).read_text(encoding="utf-8")
    want = mod.digest(text)
    for seat, role, art in SEATS:
        rel = f"{WAVE_DIR}/w1/{seat}/{art}"
        p = root / rel
        p.write_text(f"seat evidence for {seat}\ncandidate {want}\n", encoding="utf-8")
        v = json.loads((root / VOTES_DIR / f"{seat}.json").read_text())
        v["candidate_sha256"] = want
        v["artifact_sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
        (root / VOTES_DIR / f"{seat}.json").write_text(json.dumps(v))
    return want

def entry_read(root):
    return (root / mod.ENTRY).read_text(encoding="utf-8")

def entry_write(root, text):
    (root / mod.ENTRY).write_text(text, encoding="utf-8")

def apply(root, mod_obj):
    _bind(mod_obj)
    return BUILDER_FN(root)



def fg06_symlink_alias(root):
    text = entry_read(root)
    want = mod.digest(text)
    planted = root / f"{WAVE_DIR}/w1/ReviewerBlind/planted-shared.md"
    planted.write_text(f"shared wave evidence naming ReviewerGate and ReviewerBlind\n"
                       f"candidate {want}\n", encoding="utf-8")
    link = root / f"{WAVE_DIR}/w1/ReviewerGate/link.md"
    if link.exists() or link.is_symlink():
        link.unlink()
    os.symlink("../ReviewerBlind/planted-shared.md", link)
    v = json.loads((root / VOTES_DIR / "ReviewerGate.json").read_text())
    v["artifact_path"] = f"{WAVE_DIR}/w1/ReviewerGate/link.md"
    v["artifact_sha256"] = hashlib.sha256(planted.read_bytes()).hexdigest()
    (root / VOTES_DIR / "ReviewerGate.json").write_text(json.dumps(v))

BUILDER_FN = fg06_symlink_alias
