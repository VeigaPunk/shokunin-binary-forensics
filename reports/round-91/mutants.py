#!/usr/bin/env python3
"""Frozen rule mutants for round-91 C1 (calibration).

Eleven implementations of the frozen SM6 rule (see `claims.md`), each with
exactly one rule element broken. `reports/round-91/c1_counter.py` runs the
frozen battery (`sm6_battery_v3.py`) against every one of them; a mutant is
KILLED iff the battery scores it at least one mismatch. All eleven must die,
or the battery does not discriminate and C1 is not verified.

| id  | broken rule element | battery case that must kill it |
|---|---|---|
| M01 | reads the last token-adjacent group on the whole LINE (the v2 rule) | R03, R04 |
| M02 | prefers the LEFT side of an arrow | B04 |
| M03 | takes the FIRST `N/D` in the stated region, not the token-adjacent one | R02, R07 |
| M04 | compares the numerator only | B02 |
| M05 | compares the denominator only | B03 |
| M06 | hard-codes the denominator 15 | B06 |
| M07 | hard-codes the numerator 8 | B10 |
| M08 | passes when no K line exists | B09 |
| M09 | passes when the stated region carries no `N/D` | R06 |
| M10 | accepts `N >= held` instead of `N == held` | B12 |
| M11 | token-adjacent pattern without the parenthesised-score allowance | B07 |

`reference(root)` is the same rule as prose in `claims.md`, written here so the
mutants are single-element deltas of one implementation. The submitted
implementation (`corpus/self_assessment_check3.py`) is scored on the battery,
never compared against this file's bytes.
"""
import re
from pathlib import Path


def txt(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")


def map_counts(root):
    rows = [l for l in txt(root / "corpus/README.md").splitlines() if re.match(r"^\| C[0-9]+ ", l)]
    held = sum(1 for l in rows if re.search(r"\|\s*held\s*\|\s*$", l))
    return held, len(rows)


def k_lines(root):
    return [l for l in txt(root / "SCORECARD.md").splitlines() if "K_HELD_BACKED" in l]


def region_of(line):
    s = line.strip()
    if s.startswith("|") and s.endswith("|"):
        cells = s.split("|")
        if len(cells) >= 5:
            return cells[2]
    return s


ARROW = r"(?:\s*(?:\(\s*[\d.]+\s*\))?\s*(?:→|->)\s*(\d+)\s*/\s*(\d+))?"
PAIR = r"(\d+)\s*/\s*(\d+)"


def numbers(text):
    """Every N/D group in text, right side of an arrow preferred."""
    out = []
    for m in re.finditer(PAIR + ARROW, text):
        n, d = int(m.group(1)), int(m.group(2))
        if m.group(3):
            n, d = int(m.group(3)), int(m.group(4))
        out.append((n, d))
    return out


def _verdict(got, held, rows, *, num_only=False, den_only=False, den15=False,
             num8=False, ge=False):
    n, d = got
    if num8:
        n = 8
    if den15:
        d = 15
    if num_only:
        ok = (n >= held) if ge else (n == held)
    elif den_only:
        ok = d == rows
    else:
        ok = (n == held and d == rows) if not ge else (n >= held and d == rows)
    return 0 if ok else 1


def reference(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    got = None
    m = re.search(r"K_HELD_BACKED", region)
    if m:
        mm = re.match(r"[^0-9]*" + PAIR + ARROW, region[m.end():])
        if mm:
            got = (int(mm.group(3) or mm.group(1)), int(mm.group(4) or mm.group(2)))
    if got is None:
        nums = numbers(region)
        if not nums:
            return 1
        got = nums[-1]
    return 0 if got == (held, rows) else 1


def m01(root):
    """v2's rule: last token-adjacent group anywhere on the line."""
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    head = lines[-1].split("K_HELD_BACKED_STRICT")[0]
    stmts = re.findall(r"K_HELD_BACKED[^0-9]*" + PAIR + ARROW, head)
    if not stmts:
        return 1
    n0, d0, n1, d1 = stmts[-1]
    got = (int(n1), int(d1)) if n1 else (int(n0), int(d0))
    return 0 if got == (held, rows) else 1


def m02(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums:
        return 1
    m = re.search(r"K_HELD_BACKED", region)
    if m:
        mm = re.match(r"[^0-9]*" + PAIR, region[m.end():])
        if mm:
            return 0 if (int(mm.group(1)), int(mm.group(2))) == (held, rows) else 1
    return 0 if nums[-1] == (held, rows) else 1


def m03(root):
    """First raw `N/D` in the stated region, ignoring token adjacency and arrows."""
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    m = re.search(PAIR, region)
    if not m:
        return 1
    return 0 if (int(m.group(1)), int(m.group(2))) == (held, rows) else 1


def _num_only(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums:
        return 1
    return _verdict(nums[-1], held, rows, num_only=True)


def _den_only(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums:
        return 1
    return _verdict(nums[-1], held, rows, den_only=True)


def _den15(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums:
        return 1
    return _verdict(nums[-1], held, rows, den15=True)


def _num8(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums:
        return 1
    return _verdict(nums[-1], held, rows, num8=True)


def m08(root):
    held, rows = map_counts(root)
    if not k_lines(root):
        return 0
    return reference(root)


def m09(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    if not numbers(region):
        return 0
    return reference(root)


def m10(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    nums = numbers(region)
    if not nums:
        return 1
    return _verdict(nums[-1], held, rows, ge=True)


def m11(root):
    held, rows = map_counts(root)
    lines = k_lines(root)
    if not lines:
        return 1
    region = region_of(lines[-1]).split("K_HELD_BACKED_STRICT")[0]
    m = re.search(r"K_HELD_BACKED", region)
    got = None
    if m:
        mm = re.match(r"[^0-9]*" + PAIR + r"(?:\s*(?:→|->)\s*(\d+)\s*/\s*(\d+))?",
                      region[m.end():])
        if mm:
            got = (int(mm.group(3) or mm.group(1)), int(mm.group(4) or mm.group(2)))
    if got is None:
        nums = numbers(region)
        if not nums:
            return 1
        got = nums[-1]
    return 0 if got == (held, rows) else 1


MUTANTS = {
    "M01": m01, "M02": m02, "M03": m03, "M04": _num_only, "M05": _den_only,
    "M06": _den15, "M07": _num8, "M08": m08, "M09": m09, "M10": m10, "M11": m11,
}
