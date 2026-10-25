#!/usr/bin/env python3
"""Q15 tree-identity sentence checker (round-69 C2 calibration claim).

Criterion Q15 (corpus/QUALITY.md, added this round): a stated git object id or
tree identity must be re-derived with the command that names it. This checker is
the mechanical form of that criterion for the round-69 lesson's tree-identity
sentences:

- a line beginning `tree-identity restatement:` asserts pairs of the form
  `` `<hex>:corpus` = `<hex>` ``. Every pair is VERIFIED against the live lane
  repository with `git rev-parse <hex>:corpus`; a pair that does not resolve to
  the claimed value fails the scan.
- a line beginning `tree-identity false-sentence:` quotes the defect class (the
  D1 sentence). AT LEAST ONE of its pairs must FAIL verification, otherwise the
  quote does not demonstrate the class and the scan fails.

Usage (cwd = lane root):
    python3 -B corpus/q15_tree_id_check.py --self-test
        fixed true/false fixtures; exit 0 iff the checker scores both correctly.
    python3 -B corpus/q15_tree_id_check.py --scan <lesson.md> [--lane <path>]
        verifies every tree-identity line in the file; exit 0 iff every
        restatement pair resolves and at least one false-sentence pair fails.
        --lane defaults to the repo root computed from this file's location
        (parents[1]); pass it explicitly when the script runs from an archived
        tree (the counter does this).

Read-only: it runs `git rev-parse` and writes nothing.
"""
import re
import subprocess
import sys
from pathlib import Path

PAIR = re.compile(r"`([0-9a-f]{7,40}):corpus`\s*=\s*`([0-9a-f]{40})`")


def lane_root():
    return Path(__file__).resolve().parents[1]


def resolve(short, lane):
    proc = subprocess.run(["git", "-C", str(lane), "rev-parse", f"{short}:corpus"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    return proc.stdout.strip()


def check_line(line, lane, resolver=None):
    """Verify one tree-identity line. Returns (ok_pairs, bad_pairs)."""
    ok, bad = [], []
    for short, claimed in PAIR.findall(line):
        actual = (resolver(short, lane) if resolver else resolve(short, lane))
        if actual is not None and actual == claimed:
            ok.append((short, claimed))
        else:
            bad.append((short, claimed, actual))
    return ok, bad


def self_test(lane):
    # Fake resolver: fixed mapping; the algorithm is what is under test.
    fake = {"1c34603": "ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7"}
    true_line = ("tree-identity restatement: `1c34603:corpus` = "
                 "`ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`")
    false_line = ("tree-identity false-sentence: `1c34603:corpus` = "
                  "`51894d153a6e69487da2a273680d014abd240f61`")
    ok_t, bad_t = check_line(true_line, lane, fake.get)
    ok_f, bad_f = check_line(false_line, lane, fake.get)
    good = (len(ok_t) == 1 and not bad_t) and (not ok_f and len(bad_f) == 1)
    if not good:
        print(f"Q15_SELFTEST=fail true_ok={ok_t} true_bad={bad_t} "
              f"false_ok={ok_f} false_bad={bad_f}")
        return False
    print("Q15_SELFTEST=pass (true sentence verified; false sentence killed)")
    return True


def scan(path, lane):
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    restate_bad = []
    restate_count = 0
    false_found_bad = False
    for ln, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("tree-identity restatement:"):
            restate_count += 1
            ok, bad = check_line(line, lane)
            for short, claimed, actual in bad:
                restate_bad.append((ln, short, claimed, actual))
        elif line.lstrip().startswith("tree-identity false-sentence:"):
            ok, bad = check_line(line, lane)
            if bad:
                false_found_bad = True
    if restate_bad:
        for ln, short, claimed, actual in restate_bad:
            print(f"Q15_RESTATE_BAD line {ln}: `{short}:corpus` claimed {claimed} "
                  f"resolved {actual}")
        return False
    if not false_found_bad:
        print("Q15_RESTATE_BAD: no false-sentence pair failed (quote does not "
              "demonstrate the class)")
        return False
    if restate_count == 0:
        print("Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)")
        return False
    print("Q15_RESTATE_OK=yes (every restatement pair re-derived; false-sentence "
          "pair killed)")
    return True


def main():
    args = sys.argv[1:]
    lane = lane_root()
    if args and args[0] == "--lane" and len(args) >= 3:
        lane = Path(args[1])
        args = args[2:]
    if args == ["--self-test"]:
        sys.exit(0 if self_test(lane) else 1)
    if len(args) >= 2 and args[0] == "--scan":
        path = args[1]
        if len(args) >= 4 and args[2] == "--lane":
            lane = Path(args[3])
        sys.exit(0 if scan(path, lane) else 1)
    print(__doc__)
    sys.exit(64)


if __name__ == "__main__":
    main()
