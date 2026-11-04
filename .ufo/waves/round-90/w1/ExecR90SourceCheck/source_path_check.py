#!/usr/bin/env python3
"""Dead repo-path check for corpus/SOURCES.md `## Registry` rows (r89 routed D1).

Usage:
  source_path_check.py --root TREE   check TREE/corpus/SOURCES.md against TREE
  source_path_check.py --selftest    hermetic legs in a TMPDIR scratch tree

Rules (declared before data):
- Registry rows: lines inside `## Registry` (up to the next `## ` heading)
  that start with 0-3 spaces then `|`; cells split on unescaped `|`; a row
  must carry exactly 11 cells and an id cell `S<digits>`, else it is counted
  as MALFORMED (reported, not checked).
- A `source` cell span is a backticked token. A span containing whitespace
  contributes its first word only (`path --flag`). Skipped as not
  repo-relative: http://, https://, ~/, absolute /..., drive `X:/`,
  AppData/, spans with glob/brace/ellipsis/`$`/`<`/`>` characters, and spans
  whose first `/`-segment is not an entry at TREE's root (relative
  shorthand such as `round-21`, `dist/...`, or a single word that is not a
  root file). Such spans are counted as UNANCHORED, never as dead.
- An anchored span resolves iff it names an existing file or directory
  under TREE after normalisation (a span escaping TREE never resolves).
- A row is DEAD iff at least one anchored span does not resolve.
- A dead row S<id> is EXCUSED iff a LATER row's `teaches` or `source` cell
  contains `supersedes S<id>` (id word-bounded) AND that later row has at
  least one anchored span and every anchored span of it resolves.
- Output: `DEAD <id> <path>` per dead span, `EXCUSED <id> by <id2>`,
  then counters. Exit 0 iff SOURCE_PATH_DEAD=0, 1 if >0, 2 if SOURCES.md
  is missing.
"""
import os
import re
import sys
import tempfile

ID_RE = re.compile(r"^S\d+$")
ROW_RE = re.compile(r"^ {0,3}\|")
CELL_SPLIT = re.compile(r"(?<!\\)\|")
TICK_RE = re.compile(r"`([^`]+)`")
SKIP_PREFIX = ("http://", "https://", "~/", "/", "AppData/")
DRIVE_RE = re.compile(r"^[A-Za-z]:[/\\]")
BAD_CHARS = set("*?{}[]$<>…")
COL_SOURCE, COL_TEACHES = 1, 6


def registry_rows(text):
    """Yield (lineno, cells or None) for every table row in ## Registry."""
    inside = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            inside = line.strip() == "## Registry"
            continue
        if not inside or not ROW_RE.match(line):
            continue
        body = line.strip()
        if body.startswith("|"):
            body = body[1:]
        if body.endswith("|") and not body.endswith("\\|"):
            body = body[:-1]
        cells = [c.strip() for c in CELL_SPLIT.split(body)]
        if set(cells[0]) <= set("-: ") or cells[0] == "id":
            continue  # header / separator
        yield n, cells


def spans(cell, root):
    """Return (anchored, unanchored) path spans of one source cell."""
    anchored, unanchored = [], []
    for raw in TICK_RE.findall(cell):
        tok = raw.strip().split()[0] if raw.strip() else ""
        if not tok or tok.startswith(SKIP_PREFIX) or DRIVE_RE.match(tok):
            continue
        if BAD_CHARS & set(tok):
            continue
        first = tok.split("/", 1)[0]
        if first in ("", ".", "..") or not os.path.lexists(os.path.join(root, first)):
            unanchored.append(tok)
            continue
        anchored.append(tok)
    return anchored, unanchored


def resolves(root, rel):
    real_root = os.path.realpath(root)
    target = os.path.realpath(os.path.join(root, rel))
    if target != real_root and not target.startswith(real_root + os.sep):
        return False
    return os.path.isfile(target) or os.path.isdir(target)


def check(root, out=sys.stdout):
    path = os.path.join(root, "corpus", "SOURCES.md")
    if not os.path.isfile(path):
        print(f"MISSING {path}", file=out)
        return 2
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    rows, malformed = [], 0
    for n, cells in registry_rows(text):
        if len(cells) != 11 or not ID_RE.match(cells[0]):
            print(f"MALFORMED line {n} cells={len(cells)}", file=out)
            malformed += 1
            continue
        anchored, unanchored = spans(cells[COL_SOURCE], root)
        dead = [p for p in anchored if not resolves(root, p)]
        rows.append({"id": cells[0], "src": cells[COL_SOURCE], "teaches": cells[COL_TEACHES],
                     "anchored": anchored, "unanchored": unanchored, "dead": dead})
    n_dead = n_exc = n_checked = n_unanch = 0
    for i, row in enumerate(rows):
        n_unanch += len(row["unanchored"])
        if row["anchored"]:
            n_checked += 1
        if not row["dead"]:
            continue
        sup = re.compile(r"\bsupersedes\s+" + re.escape(row["id"]) + r"(?![0-9A-Za-z_])")
        by = next((later["id"] for later in rows[i + 1:]
                   if (sup.search(later["teaches"]) or sup.search(later["src"]))
                   and later["anchored"] and not later["dead"]), None)
        if by:
            print(f"EXCUSED {row['id']} by {by}", file=out)
            n_exc += 1
            continue
        for p in row["dead"]:
            print(f"DEAD {row['id']} {p}", file=out)
        n_dead += 1
    print(f"SOURCE_PATH_ROWS={len(rows)}", file=out)
    print(f"SOURCE_PATH_ROWS_CHECKED={n_checked}", file=out)
    print(f"SOURCE_PATH_UNANCHORED_SPANS={n_unanch}", file=out)
    print(f"SOURCE_PATH_MALFORMED={malformed}", file=out)
    print(f"SOURCE_PATH_EXCUSED={n_exc}", file=out)
    print(f"SOURCE_PATH_DEAD={n_dead}", file=out)
    return 0 if n_dead == 0 else 1


HEADER = ("## Registry\n\n| id | source | kind | tier | scope | anchor | teaches | status"
          " | opened | recheck | used-by |\n|---|---|---|---|---|---|---|---|---|---|---|\n")


def row(rid, source, teaches="t", indent=""):
    return f"{indent}| {rid} | {source} | own-work | A | s | a | {teaches} | mined | 2026-11-04 | 90d | — |\n"


def selftest():
    import io
    base = tempfile.mkdtemp(prefix="spc-selftest-")  # honours TMPDIR
    legs = [
        ("clean-resolves", row("S001", "x — `corpus/live/a.json`"), 0, []),
        ("dead-row", row("S481", "x — `corpus/live/runs/round-89/receipt.json`"), 1, ["DEAD S481"]),
        ("dead-superseded-by-resolving",
         row("S481", "x — `corpus/live/runs/round-89/receipt.json`")
         + row("S490", "x — `corpus/live/a.json`", "supersedes S481 — relocated"), 0, ["EXCUSED S481 by S490"]),
        ("dead-superseded-by-dead",
         row("S481", "x — `corpus/live/runs/round-89/receipt.json`")
         + row("S490", "x — `corpus/live/gone.json`", "supersedes S481"), 1, ["DEAD S481", "DEAD S490"]),
        ("prefix-id-no-excuse",
         row("S481", "x — `corpus/live/runs/round-89/receipt.json`")
         + row("S490", "x — `corpus/live/a.json`", "supersedes S48 only"), 1, ["DEAD S481"]),
        ("indented-row-parsed", row("S481", "x — `corpus/live/missing.json`", indent="  "), 1, ["DEAD S481"]),
        ("url-source-ignored", row("S002", "page — https://example.org/x and `https://example.org/y`"), 0, []),
        ("source-cell-supersedes",
         row("S481", "x — `corpus/live/runs/round-89/receipt.json`")
         + row("S490", "supersedes S481 — `corpus/live/a.json`"), 0, ["EXCUSED S481 by S490"]),
        ("earlier-row-no-excuse",
         row("S470", "x — `corpus/live/a.json`", "supersedes S481")
         + row("S481", "x — `corpus/live/runs/round-89/receipt.json`"), 1, ["DEAD S481"]),
    ]
    ok = True
    try:
        for name, body, want_rc, want_lines in legs:
            tree = tempfile.mkdtemp(prefix=name + "-", dir=base)
            os.makedirs(os.path.join(tree, "corpus", "live"))
            open(os.path.join(tree, "corpus", "live", "a.json"), "w").close()
            with open(os.path.join(tree, "corpus", "SOURCES.md"), "w", encoding="utf-8") as fh:
                fh.write("# Sources\n\n" + HEADER + body + "\n## Search log\n\n| S999 | `corpus/no` |\n")
            buf = io.StringIO()
            rc = check(tree, buf)
            got = buf.getvalue()
            good = rc == want_rc and all(w in got for w in want_lines)
            ok &= good
            print(f"LEG {name} rc={rc} want={want_rc} {'ok' if good else 'FAIL'}")
        empty = tempfile.mkdtemp(prefix="missing-", dir=base)
        rc = check(empty, io.StringIO())
        ok &= rc == 2
        print(f"LEG missing-sources rc={rc} want=2 {'ok' if rc == 2 else 'FAIL'}")
    finally:
        import shutil
        shutil.rmtree(base, ignore_errors=True)
    print(f"SOURCE_PATH_SELFTEST={'pass' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    if len(argv) == 2 and argv[0] == "--root":
        return check(argv[1])
    print(__doc__.split("\n\n")[1], file=sys.stderr)
    return 64


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
