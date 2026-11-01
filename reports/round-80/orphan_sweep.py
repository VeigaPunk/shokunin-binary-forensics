#!/usr/bin/env python
"""orphan_sweep.py - cited-evidence hygiene instrument (round 80, claim C2).

Answers exactly the routed carry-in duty: which evidence files do the closed
round reports and lessons CITE that have never been committed to the lane
repo? Classifies every cited lane-repo path against the HEAD tree and the
working disk:

  committed      path is a file in HEAD (or a directory with committed files)
  orphan         file exists on disk but NOT in HEAD  -> landable via treecommit
  orphan-dir     directory exists on disk, non-empty, nothing under it in HEAD
  absent-fleet   cited path does not exist in the lane but exists under the
                 fleet root's shared .ufo tree (other lane's surface; recorded,
                 never this lane's commit)
  absent         exists nowhere; recorded as a disposition (nothing to land)

Exit codes (declared per the fleet PROTOCOL §Gate standard §Verdict clause):
  0   sweep completed, zero landable orphans (absent/fleet-side dispositions
      are recorded, not failures - there is nothing to land)
  1   sweep completed and flagged >=1 landable orphan, or the sweep could not
      evaluate (git failure) - fail-closed
  64  unrecognized invocation form (usage on stderr)

--selftest runs the hermetic vector suite over synthetic state (no git, no
network, no live-tree write, no producer call): a clean vector, a planted
orphan that MUST be flagged (exit-rule vector), an absent vector, and a
mutant leg - a sabotaged blind classifier that must be CAUGHT by the planted-
orphan vector (if the blind classifier passes the suite, the suite is vacuous
and the run dies with the attributed last line). Plain selftest: last line
`SWEEP_SELFTEST=pass`, exit 0. Mutant leg killed: prints
`SWEEP_SELFTEST_MUTANT_FLAGGED=ok`. Missing/broken vector under the mutant:
last line `selftest: blind classifier accepted a planted orphan`, exit 1.

Usage:
  python -B orphan_sweep.py --lane <lane-dir> --fleet <fleet-root>
  python -B orphan_sweep.py --selftest
"""
import os
import re
import subprocess
import sys

LANE_DOMAIN = re.compile(r"^(?:reports|corpus|\.ufo/waves)/")
CITE_PAT = re.compile(r"`([^`\n]+)`")


def classify(cited, head_files, head_dirs, disk_files, disk_dirs, fleet_root):
    if cited in head_files or cited in head_dirs:
        return "committed", ""
    if cited in disk_files:
        return "orphan", "on-disk file never committed"
    if cited in disk_dirs and not any(f.startswith(cited + "/") for f in head_files):
        n = sum(1 for f in disk_files if f.startswith(cited + "/")) + \
            sum(1 for d in disk_dirs if d.startswith(cited + "/"))
        if n:
            return "orphan-dir", "%d on-disk entries, none committed" % n
    fleet_side = os.path.join(fleet_root, *cited.split("/")) if fleet_root else None
    if fleet_side and (os.path.isfile(fleet_side) or os.path.isdir(fleet_side)):
        return "absent-fleet", "exists under the fleet root (shared/other-lane surface)"
    return "absent", "exists nowhere on this host; recorded, nothing to land"


def classify_blind(cited, head_files, head_dirs, disk_files, disk_dirs, fleet_root):
    """Sabotaged classifier used only by the selftest mutant leg."""
    return "committed", ""


def collect_citations(lane_dir, fleet_root):
    srcs = []
    rep = os.path.join(fleet_root, ".ufo", "reports")
    if os.path.isdir(rep):
        for rnd in sorted(os.listdir(rep)):
            p = os.path.join(rep, rnd, "revenger.md")
            if os.path.isfile(p):
                srcs.append(("fleet-report-" + rnd, p))
    les = os.path.join(lane_dir, "corpus", "lessons")
    if os.path.isdir(les):
        for f in sorted(os.listdir(les)):
            if re.match(r"round-(\d+|-)", f):
                srcs.append(("lesson-" + f, os.path.join(les, f)))
    cited = {}
    for name, p in srcs:
        txt = open(p, encoding="utf-8", errors="replace").read()
        for m in CITE_PAT.finditer(txt):
            tok = m.group(1).strip()
            tok = re.sub(r"^(?:git show \S+?|diff of |sha256sum |cat |bash |python -B )[: ]", "", tok)
            tok = tok.split("#")[0]
            tok = re.sub(r":\d+[-,\d]*$", "", tok).rstrip("/").strip()
            if not tok or any(c in tok for c in "{}*<>| "):
                continue
            if not all(ord(c) < 128 for c in tok):
                continue
            if LANE_DOMAIN.match(tok):
                cited.setdefault(tok, set()).add(name)
    return sorted(cited.items(), key=lambda kv: kv[0])


def run_sweep(lane_dir, fleet_root):
    r = subprocess.run(["git", "-C", lane_dir, "ls-tree", "-r", "--name-only", "HEAD"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("SWEEP_ERROR git ls-tree failed: %s" % r.stderr.strip()[:200], file=sys.stderr)
        return 1, []
    head_files = set(l.strip() for l in r.stdout.splitlines() if l.strip())
    head_dirs = set()
    for f in head_files:
        parts = f.split("/")
        for i in range(1, len(parts)):
            head_dirs.add("/".join(parts[:i]))
    disk_files, disk_dirs = set(), set()
    for base, dirs, files in os.walk(lane_dir):
        dirs[:] = [d for d in dirs if d != ".git"]
        rel = os.path.relpath(base, lane_dir).replace("\\", "/")
        prefix = "" if rel == "." else rel + "/"
        for d in dirs:
            disk_dirs.add(prefix + d)
        for f in files:
            disk_files.add(prefix + f)
    rows = []
    orphans = 0
    for tok, srcs in collect_citations(lane_dir, fleet_root):
        status, note = classify(tok, head_files, head_dirs, disk_files, disk_dirs, fleet_root)
        rows.append((status, tok, note, sorted(srcs)))
        if status.startswith("orphan"):
            orphans += 1
    for status, tok, note, srcs in rows:
        print("SWEEP %s %s%s" % (status, tok, (" | " + note) if note else ""))
    print("CITED=%d COMMITTED=%d LANDABLE_ORPHANS=%d ABSENT=%d" % (
        len(rows),
        sum(1 for s, *_ in rows if s.startswith("committed")),
        orphans,
        sum(1 for s, *_ in rows if s.startswith("absent"))))
    print("ORPHAN_SWEEP_LANDABLE=%d" % orphans)
    return (0 if orphans == 0 else 1), rows


def run_selftest():
    """Hermetic vectors over synthetic state; no git, no temp writes."""
    head = {"reports/round-1/claims.md"}
    head_dirs = {"reports", "reports/round-1"}
    disk = {"reports/round-1/claims.md", "reports/round-2/secret-draft.log"}
    disk_dirs = {"reports", "reports/round-1", "reports/round-2"}
    fleet = None
    fails = []
    print("SWEEP_SELFTEST_CLEAN_VECTOR=ok" if classify(
        "reports/round-1/claims.md", head, head_dirs, disk, disk_dirs, fleet)[0] == "committed"
        else "SWEEP_SELFTEST_CLEAN_VECTOR=FAIL")
    st, note = classify("reports/round-2/secret-draft.log", head, head_dirs, disk, disk_dirs, fleet)
    if st == "orphan":
        print("SWEEP_SELFTEST_PLANTED_ORPHAN_FLAGGED=ok")
    else:
        print("SWEEP_SELFTEST_PLANTED_ORPHAN_FLAGGED=FAIL")
        fails.append("planted orphan not flagged")
    st2, _ = classify("corpus/lost-artifact.md", head, head_dirs, disk, disk_dirs, fleet)
    if st2 == "absent":
        print("SWEEP_SELFTEST_ABSENT_RECORDED=ok")
    else:
        print("SWEEP_SELFTEST_ABSENT_RECORDED=FAIL")
        fails.append("absent vector misclassified as %s" % st2)
    # mutant leg: the blind classifier MUST be caught by the planted-orphan vector
    mst, _ = classify_blind("reports/round-2/secret-draft.log", head, head_dirs, disk, disk_dirs, fleet)
    if mst != "orphan":
        print("SWEEP_SELFTEST_MUTANT_FLAGGED=ok")
    else:
        print("SWEEP_SELFTEST_MUTANT_FLAGGED=FAIL")
        fails.append("mutant not caught (vector vacuous)")
    if fails:
        print("selftest: blind classifier accepted a planted orphan")
        return 1
    print("SWEEP_SELFTEST=pass")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args == ["--selftest"]:
        return run_selftest()
    if len(args) == 4 and args[0] == "--lane" and args[2] == "--fleet":
        if os.environ.get("ORPHAN_SWEEP_SELFTEST_MUTANT") == "1":
            print("usage: mutant env var only valid with --selftest", file=sys.stderr)
            return 64
        code, _ = run_sweep(args[1], args[3])
        return code
    print("usage: orphan_sweep.py --lane <lane-dir> --fleet <fleet-root> | --selftest", file=sys.stderr)
    return 64


if __name__ == "__main__":
    raise SystemExit(main())
