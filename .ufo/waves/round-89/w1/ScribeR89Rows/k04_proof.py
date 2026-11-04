"""Exhaustive proof: K04 cannot reach 0 findings under the frozen instrument.

The instrument scores ONE shared text per row (the row's last two cells joined).
K04 probes presence of ghidra (ON PATH -> token 'present', forbidden 'absent')
and presence of ida (OFF PATH -> token 'absent', forbidden 'present').
Both probes are applied to the same text, so the row must contain 'present'
AND 'absent' AND contain neither. Enumerated exhaustively below.
"""
import itertools, sys, importlib.util

spec = importlib.util.spec_from_file_location(
    "crp", "/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/census_reprobe.py")
crp = importlib.util.module_from_spec(spec); spec.loader.exec_module(crp)

def findings_for_K04(text):
    """Replicate the instrument's per-spec loop for K04 on an arbitrary text."""
    out = []
    for kind, arg, tokens, forbidden in (crp.live(("presence", "ghidra")),
                                          crp.live(("presence", "ida"))):
        t = text.lower()
        if any(tok.lower() not in t for tok in tokens):
            out.append(f"{kind}:{arg} does-not-state")
        else:
            bad = [w for w in forbidden if w.lower() in t]
            if bad:
                out.append(f"{kind}:{arg} states-{bad[0]!r}")
    return out

# Exhaustive over the truth-relevant alphabet {present, absent} x filler.
filler = ["", " ghidra", " ida", " on PATH", " no output", " ghidra present; ida absent"]
words = ["present", "absent"]
best = None
combos = 0
for mask in range(4):                       # which of present/absent appear
    for f in filler:
        t = f
        if mask & 1: t += " present"
        if mask & 2: t += " absent"
        combos += 1
        n = len(findings_for_K04(t))
        if best is None or n < best[0]:
            best = (n, t, findings_for_K04(t))
        if n == 0:
            print("ZERO-FINDING TEXT FOUND (would refute the proof):", repr(t))
print(f"combinations checked: {combos}")
print(f"minimum K04 findings over all texts: {best[0]}  text={best[1]!r}")
print(f"  -> {best[2]}")
print("K04 minimal-findings texts, by literal-token combination:")
for mask in range(4):
    t = ""
    if mask & 1: t += " present"
    if mask & 2: t += " absent"
    print(f"  present={bool(mask&1)} absent={bool(mask&2)}: {len(findings_for_K04(t))} finding(s) {findings_for_K04(t)}")
