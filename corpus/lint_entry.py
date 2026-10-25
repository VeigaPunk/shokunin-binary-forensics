#!/usr/bin/env python3
"""Knowledge-entry mechanical pre-flight lint (round-70, operability).

Four rounds of the C05 candidate failed on defects a script can see before any
seat is spent: a quoted hex run whose stated byte count is not its length (Q14,
M39/M47), a §Q-map that silently dropped criteria (r69: 8 rows against 15), a
git object id with no resolving commit (Q15, M48), and a header trio that is
missing (Q02). This lint reports exactly those four classes. It is a pre-flight,
not an admission gate: a clean lint never substitutes a Q decision.

Checks (each prints one `LINT_<name>=<n>` count of findings):
  QMAP   every `| Qnn |` criterion row of QUALITY.md has a row in the entry's
         `## §Q-map` table (decision cell non-empty).
  Q14    on a prose line (outside fences) with exactly one backticked hex run
         `H` of >= 4 hex chars and exactly one `N-byte`/`N bytes` count: an
         ellipsis-terminated H must carry no count; otherwise len(H) must be 2*N.
  Q15    a backticked 7-40 hex token introduced by `commit`, `base`, `tip`,
         `since` or `at` must resolve under `git cat-file -e <h>^{commit}` in the
         lane repo.
  HEADER the first lines carry `source:`, `verified-at:`, `recheck:` and
         `coverage-map:` keys.

Usage (cwd = lane root or --lane):
    python3 -B corpus/lint_entry.py --entry <knowledge.md> [--lane <repo>]
        exit 0 iff every count is 0; 1 otherwise; 2 if unreadable.
    python3 -B corpus/lint_entry.py --self-test
        a clean synthetic entry scores 0 on all four; one planted defect per
        class scores exactly that class. Exit 0 iff all hold.

Read-only: reads the entry, QUALITY.md beside this file, and runs git cat-file.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAMES = ("QMAP", "Q14", "Q15", "HEADER")


def prose_lines(text):
    fenced = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            yield n, line


def lint_qmap(text, quality):
    want = re.findall(r"^\| (Q\d+) \|", quality, re.M)
    m = re.search(r"^## §Q-map\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    have = set()
    if m:
        for row in re.findall(r"^\| (Q\d+) \| ([^|]+)\|", m.group(1), re.M):
            if row[1].strip():
                have.add(row[0])
    return [q for q in want if q not in have]


def lint_q14(text):
    """Clause = text between `;` or sentence-final `. `; digest lengths (40, 64) are
    file digests, not byte runs, and odd-length tokens are not byte runs."""
    hits = []
    for n, line in prose_lines(text):
        for clause in re.split(r";|\.\s", line):
            runs = [(h, e) for h, e in re.findall(r"`([0-9a-f]{4,})(…?)`", clause)
                    if len(h) % 2 == 0 and len(h) not in (40, 64, 128)]
            counts = re.findall(r"(\d+)[- ]bytes?\b", clause)
            if len(runs) != 1 or len(counts) != 1 or int(counts[0]) > 32:
                continue
            h, ell = runs[0]
            if ell or len(h) != 2 * int(counts[0]):
                hits.append(n)
    return hits


def lint_q15(text, lane, resolve=None):
    resolve = resolve or (lambda h: subprocess.run(
        ["git", "-C", str(lane), "cat-file", "-e", f"{h}^{{commit}}"], capture_output=True).returncode == 0)
    cite = re.compile(r"(?i:\bcommit|\bbase|\btip|\bsince|\bat)\s+`([0-9a-f]{7,40})`(?!…)")
    return [(n, h) for n, line in prose_lines(text) for h in cite.findall(line) if not resolve(h)]


def lint_header(text):
    head = "\n".join(text.splitlines()[:40])
    return [k for k in ("source:", "verified-at:", "recheck:", "coverage-map:")
            if not re.search(rf"^{re.escape(k)}", head, re.M)]


def lint(path, lane, quality, resolve=None):
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    return {"QMAP": lint_qmap(text, quality), "Q14": lint_q14(text),
            "Q15": lint_q15(text, lane, resolve), "HEADER": lint_header(text)}


CLEAN = """source: S001 — x
verified-at: 2026-10-25
recheck: `cmd`
coverage-map: C05
admission-status: candidate

# T

The payload begins `4d616e69666573742d` — ASCII `Manifest-` (9 bytes) at commit `aaaaaaa`.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | x |
| Q02 | n/a | y |
"""


def self_test():
    quality = "| id |\n|---|\n| Q01 | a |\n| Q02 | b |\n"
    good = lambda h: h == "aaaaaaa"  # noqa: E731
    with tempfile.TemporaryDirectory(prefix="rev-r70-lint-") as d:
        d = Path(d)
        muts = {
            "clean": (CLEAN, None),
            "QMAP": (CLEAN.replace("| Q02 | n/a | y |\n", ""), "QMAP"),
            "Q14": (CLEAN.replace("(9 bytes)", "(8 bytes)"), "Q14"),
            "Q15": (CLEAN.replace("`aaaaaaa`", "`bbbbbbb`"), "Q15"),
            "HEADER": (CLEAN.replace("recheck: `cmd`\n", ""), "HEADER"),
        }
        for label, (body, cls) in muts.items():
            p = d / f"{label}.md"
            p.write_text(body, encoding="utf-8")
            got = {k: len(v) for k, v in lint(p, d, quality, good).items()}
            want = {k: (1 if k == cls else 0) for k in NAMES}
            if got != want:
                print(f"SELFTEST FAIL {label}: got {got} want {want}")
                return 1
        trunc = CLEAN.replace("`4d616e69666573742d` — ASCII `Manifest-` (9 bytes)",
                              "`4d616e69666573742d…` (9 bytes)")
        p = d / "trunc.md"
        p.write_text(trunc, encoding="utf-8")
        if len(lint(p, d, quality, good)["Q14"]) != 1:
            print("SELFTEST FAIL an ellipsis-truncated run carrying a count was not flagged")
            return 1
    print("SELFTEST OK: clean 0; four planted defects each scored exactly their class; truncated-run-with-count flagged")
    return 0


def main():
    args = sys.argv[1:]
    if args == ["--self-test"]:
        sys.exit(self_test())
    if "--entry" in args:
        entry = Path(args[args.index("--entry") + 1])
        lane = Path(args[args.index("--lane") + 1]) if "--lane" in args else HERE.parent
        if not entry.is_file() or not (HERE / "QUALITY.md").is_file():
            print("could-not-evaluate: entry or QUALITY.md unreadable")
            sys.exit(2)
        got = lint(entry, lane, (HERE / "QUALITY.md").read_text(encoding="utf-8"))
        for k in NAMES:
            print(f"LINT_{k}={len(got[k])} {got[k] if got[k] else ''}".rstrip())
        sys.exit(0 if not any(got.values()) else 1)
    print(__doc__)
    sys.exit(64)


if __name__ == "__main__":
    main()
