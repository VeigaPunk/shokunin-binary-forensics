# Forgery vector FG13-status-below-window (r97 port of CriticR96 fg13_status_below_window).
# Source: .ufo/waves/round-96/w1/CriticR96/receipts/drv.py :: FORGERIES entry
# (expected under frozen v5: fail:C1_ADMITTED).
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



def fg13_status_below_window(root):
    text = entry_read(root)
    lines = text.splitlines(True)
    idx = next(i for i, l in enumerate(lines)
               if re.match(r"(?i)^\s*admission-status\s*:", l))
    line = lines.pop(idx)
    lines.insert(40, line)
    entry_write(root, "".join(lines))
    repin(root)

BUILDER_FN = fg13_status_below_window
