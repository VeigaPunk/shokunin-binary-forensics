#!/usr/bin/env python3
"""Re-run every `### Derivation table` row of an entry and compare stdout with the output cell.

Usage: python3 -B deriv_check.py --entry <entry.md> --root <tree root>
Cell rule (the entry's own preamble): one code span per stdout line, joined by " / "; text after
" — " is annotation; in a row whose cell has `xxxxxxxx…` (name) pairs, each line is "<prefix>… (name)".
Prints DERIV <value> MATCH|MISMATCH per row and DERIV_ROWS=<n> DERIV_MISMATCH=<m>; exit 0 iff m == 0
and n > 0.
"""
import argparse, re, subprocess, sys


def rows(text):
    sect = text.split("### Derivation table", 1)[1].split("\n## ", 1)[0]
    for ln in sect.splitlines():
        if not ln.startswith("| ") or ln.startswith("| Value") or ln.startswith("|---"):
            continue
        cells = re.split(r"(?<!\\)\|", ln)[1:-1]
        if len(cells) != 3:
            yield None, ln, None
            continue
        value, cmd, out = (c.strip() for c in cells)
        yield value, cmd, out


def expected_lines(out):
    out = out.split(" — ", 1)[0].strip()
    pairs = re.findall(r"`([^`]*…)` (\([^)]*\))", out)
    if pairs:
        return [f"{a} {b}" for a, b in pairs]
    return re.findall(r"`([^`]*)`", out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entry", required=True)
    ap.add_argument("--root", required=True)
    a = ap.parse_args()
    text = open(a.entry, encoding="utf-8").read()
    n = bad = 0
    for value, cmd, out in rows(text):
        n += 1
        if value is None:
            print(f"DERIV <unparsed> MISMATCH row={cmd!r}")
            bad += 1
            continue
        if not (cmd.startswith("`") and cmd.endswith("`")):
            print(f"DERIV {value} MISMATCH command not one code span")
            bad += 1
            continue
        shell = cmd[1:-1].replace("\\|", "|")
        got = subprocess.run(["bash", "-c", shell], cwd=a.root, capture_output=True, text=True).stdout
        got_lines = got.rstrip("\n").split("\n") if got else []
        want = expected_lines(out)
        ok = got_lines == want
        bad += not ok
        print(f"DERIV {value} {'MATCH' if ok else 'MISMATCH'}" + ("" if ok else f" got={got_lines!r} want={want!r}"))
    print(f"DERIV_ROWS={n} DERIV_MISMATCH={bad}")
    return 0 if n and not bad else 1


if __name__ == "__main__":
    sys.exit(main())
