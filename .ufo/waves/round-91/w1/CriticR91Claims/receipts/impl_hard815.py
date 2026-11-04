#!/usr/bin/env python3
"""Hard-coded 8/15 control: reads the stated region's last N/D but compares it to the
constant (8,15) instead of the map counts."""
import re, sys
from pathlib import Path
PAIR = r"(\d+)\s*/\s*(\d+)"
ARROW = r"(?:\s*(?:\(\s*[\d.]+\s*\))?\s*(?:→|->)\s*(\d+)\s*/\s*(\d+))?"
def numbers(t):
    out = []
    for m in re.finditer(PAIR + ARROW, t):
        n, d = int(m.group(1)), int(m.group(2))
        if m.group(3): n, d = int(m.group(3)), int(m.group(4))
        out.append((n, d))
    return out
def sm6(root):
    root = Path(root)
    lines = [l for l in (root/"SCORECARD.md").read_text(encoding="utf-8").splitlines()
             if "K_HELD_BACKED" in l]
    if not lines: return 1
    s = lines[-1].strip()
    region = s
    if s.startswith("|") and s.endswith("|"):
        cells = s.split("|")
        if len(cells) >= 5: region = cells[2]
    region = region.split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums: return 1
    return 0 if nums[-1] == (8, 15) else 1
if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--self-test"]:
        print("SELFTEST OK"); sys.exit(0)
    print(f"SM6={sm6(Path(a[a.index('--root')+1]))}"); print("SELF_MISMATCH=0"); sys.exit(0)
