#!/usr/bin/env python3
"""Commit-message <-> tree conformance over a git range (round-91 C2).

Usage:
    python3 -B reports/round-91/message_tree_check.py --lane REPO --range A..B [--json]
    python3 -B reports/round-91/message_tree_check.py --selftest

For every commit in `git rev-list A..B` (an empty A means all history of B)
the message is read with `git log -1 --format=%B <commit>` and every token
that looks like a repo-relative path is extracted: a token ending in .py .md
.json .log .txt .sh .mjs .yml .yaml .toml .cfg .ini, or an explicit directory
(`corpus/`), or a slash token whose segments carry a file-like dot
(`corpus/v1.2/x`), with no whitespace, no glob characters and no `..`
segment (a revision range such as `A..B` is not a path).  Backticks and
surrounding punctuation act as delimiters (so a backticked `path:12` and a
bare prose mention are both read), a leading `./` and a trailing `:line`
suffix are stripped, and an explicit directory citation keeps its meaning
(`corpus/` is checked as the tree `corpus`).  Slash-only prose
(`red/green`, `0/1/2/64/selftest`) is not a citation; an extension-less
directory written without the trailing `/` is therefore not read (declared
limitation).

Each cited path is checked against the commit's own tree with
`git -C REPO cat-file -e <commit>:<path>`.  A path without `/` that does not
resolve is retried as a unique suffix of `git ls-tree -r --name-only
<commit>`; exactly one match counts as resolved and is reported as `bare`.

Output:
    COMMIT <hash> cited=<n> misses=<k> [missing=<p>,...] [bare=<p>,...]
    MESSAGE_TREE commits=<N> cited=<M> misses=<K>

Exit: 0 iff K == 0, 1 if K > 0, 2 on usage error.

`--selftest` builds a throwaway fixture repo under $HYAKU_SCRATCH (default
/fast/scratch/hyaku), checks a clean range (exit 0), a planted missing-path
range (exit 1 naming the absent path) and a `.log` leg (a subdirectory .log
cited both by full path and by bare filename, resolving by unique suffix),
prints `MSG_TREE_SELFTEST=pass` and exits 0 iff all three hold.

Read-only over the lane: it writes only inside its own fixture dir, which the
self-test removes before returning.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXTS = (".py", ".md", ".json", ".log", ".txt", ".sh",
        ".mjs", ".yml", ".yaml", ".toml", ".cfg", ".ini")
PATH_CHARS = re.compile(r"^[A-Za-z0-9._/-]+$")
TOKEN = re.compile(r"[^\s`()\[\],;:\"']+")
LINE_SUFFIX = re.compile(r":\d+(?:-\d+)?$")
TRAIL = ".,;:!?*'\""
LEAD = "'\""


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def git_out(repo, *args):
    r = git(repo, *args)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def path_shaped(p, is_dir):
    """A token looks like a repo-relative path (declared extraction rule).

    Path-like means: a listed file extension, or an explicit directory
    (`corpus/`), or a slash token whose segments carry a file-like dot
    (`corpus/v1.2/x`).  Slash-only prose (`red/green`, `0/1/2/64/selftest`)
    is not a path citation; an extension-less directory written without the
    trailing `/` is therefore not read (declared limitation).
    """
    if not p or not PATH_CHARS.match(p):
        return False
    if p.startswith("/") or "://" in p or ".." in p:
        return False
    if not ("/" in p or p.endswith(EXTS) or is_dir):
        return False
    if p.rsplit("/", 1)[-1] in EXTS:  # a bare extension is prose, not a file
        return False
    if "/" in p and not p.endswith(EXTS) and not is_dir:
        if not any("." in s for s in p.split("/") if s):
            return False
    if "/" in p and all(s.isdigit() for s in p.split("/") if s):
        return False
    return True


def cited_paths(message):
    """Repo-relative path citations in one commit message, in first-seen order."""
    seen, out = set(), []
    for raw in TOKEN.findall(message):
        t = raw.rstrip(TRAIL).lstrip(LEAD)
        if "*" in t or "?" in t:  # globs are not literal citations
            continue
        t = LINE_SUFFIX.sub("", t)
        t = t.rstrip(TRAIL)
        is_dir = t.endswith("/")
        p = t.rstrip("/")
        while p.startswith("./"):
            p = p[2:]
        if not path_shaped(p, is_dir):
            continue
        if p in seen:
            continue
        seen.add(p)
        out.append(p)
    return out


def resolve(repo, commit, path, tree_names):
    """'hit' (present in this commit's tree), 'bare' (unique suffix), or 'miss'."""
    if git(repo, "cat-file", "-e", f"{commit}:{path}").returncode == 0:
        return "hit"
    if "/" not in path:
        hits = [n for n in tree_names if n == path or n.endswith("/" + path)]
        if len(hits) == 1:
            return "bare"
    return "miss"


def rev_list(repo, rng):
    if ".." in rng:
        a, b = rng.split("..", 1)
        if a:                       # A..B, or A.. (B defaults to HEAD)
            spec = f"{a}..{b or 'HEAD'}"
        elif b:                     # ..B: an empty A means all history of B
            spec = b
        else:
            spec = "HEAD"
    else:
        spec = rng
    r = git(repo, "rev-list", spec)
    if r.returncode != 0:
        raise RuntimeError(f"rev-list {spec} failed: {r.stderr.strip()}")
    return r.stdout.split()


def scan(repo, rng):
    commits = rev_list(repo, rng)
    rows, n_cited, n_miss = [], 0, 0
    for commit in commits:
        message = git_out(repo, "log", "-1", "--format=%B", commit)
        tree_names = git_out(repo, "ls-tree", "-r", "--name-only",
                             commit).splitlines()
        cited, missing, bare = cited_paths(message), [], []
        for p in cited:
            verdict = resolve(repo, commit, p, tree_names)
            if verdict == "miss":
                missing.append(p)
            elif verdict == "bare":
                bare.append(p)
        rows.append({"commit": commit, "cited": len(cited),
                     "missing": missing, "bare": bare})
        n_cited += len(cited)
        n_miss += len(missing)
    return rows, n_cited, n_miss


def report(rows, n_cited, n_miss):
    lines = []
    for row in rows:
        line = (f"COMMIT {row['commit']} cited={row['cited']} "
                f"misses={len(row['missing'])}")
        if row["missing"]:
            line += " missing=" + ",".join(row["missing"])
        if row["bare"]:
            line += " bare=" + ",".join(row["bare"])
        lines.append(line)
    lines.append(f"MESSAGE_TREE commits={len(rows)} cited={n_cited} "
                 f"misses={n_miss}")
    return "\n".join(lines)


def scratch_root():
    for cand in (os.environ.get("HYAKU_SCRATCH"), "/fast/scratch/hyaku"):
        if cand and Path(cand).is_dir() and os.access(cand, os.W_OK):
            return Path(cand)
    return Path(tempfile.gettempdir())


def run_instrument(lane, rng):
    return subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()),
                           "--lane", str(lane), "--range", rng],
                          capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def selftest():
    """Throwaway fixture: clean range, planted miss, and a `.log` leg."""
    root = scratch_root() / "revenger-r91" / "ExecR91MsgTree"
    root.mkdir(parents=True, exist_ok=True)
    d = Path(tempfile.mkdtemp(prefix="selftest-", dir=str(root)))
    failures = []

    def g(*args):
        return subprocess.run(["git", "-C", str(d), *args],
                              capture_output=True, text=True,
                              encoding="utf-8", errors="replace")

    try:
        if g("init", "-q").returncode != 0:
            print("MSG_TREE_SELFTEST=fail fixture init")
            return 1
        top = g("rev-parse", "--show-toplevel").stdout.strip()
        if Path(top).resolve() != d.resolve():
            print(f"MSG_TREE_SELFTEST=fail fixture toplevel {top!r} != {d}")
            return 1
        g("config", "user.name", "r91-selftest")
        g("config", "user.email", "r91@selftest.invalid")

        g("commit", "-q", "--allow-empty", "-m", "root")
        c0 = g("rev-parse", "HEAD").stdout.strip()

        (d / "a.txt").write_text("a\n", encoding="utf-8")
        g("add", "a.txt")
        g("commit", "-q", "-m", "add `a.txt`")
        c1 = g("rev-parse", "HEAD").stdout.strip()

        g("commit", "-q", "--allow-empty", "-m",
          "cite `missing/r91.txt` as the planted miss")
        c2 = g("rev-parse", "HEAD").stdout.strip()

        (d / "reports").mkdir()
        (d / "reports" / "probe.log").write_text("log\n", encoding="utf-8")
        g("add", "reports/probe.log")
        g("commit", "-q", "-m",
          "log leg cites `reports/probe.log` and the bare `probe.log`")
        c3 = g("rev-parse", "HEAD").stdout.strip()

        clean = run_instrument(d, f"{c0}..{c1}")
        cout = clean.stdout + clean.stderr
        if clean.returncode != 0 or "missing=" in cout:
            failures.append(f"clean range exit={clean.returncode} out={cout.strip()!r}")

        dirty = run_instrument(d, f"{c1}..{c2}")
        dout = dirty.stdout + dirty.stderr
        if dirty.returncode != 1 or "missing/r91.txt" not in dout:
            failures.append(f"planted range exit={dirty.returncode} out={dout.strip()!r}")

        logleg = run_instrument(d, f"{c2}..{c3}")
        lout = logleg.stdout + logleg.stderr
        if logleg.returncode != 0 or "bare=probe.log" not in lout:
            failures.append(f"log leg exit={logleg.returncode} out={lout.strip()!r}")
    finally:
        shutil.rmtree(d, ignore_errors=True)

    if failures:
        for f in failures:
            print("  " + f)
        print("MSG_TREE_SELFTEST=fail")
        return 1
    print("MSG_TREE_SELFTEST=pass")
    return 0


def main(argv):
    lane = rng = None
    as_json = want_selftest = False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--lane":
            if i + 1 >= len(argv):
                print("usage: --lane needs a value", file=sys.stderr)
                return 2
            lane = argv[i + 1]; i += 2
        elif a == "--range":
            if i + 1 >= len(argv):
                print("usage: --range needs A..B", file=sys.stderr)
                return 2
            rng = argv[i + 1]; i += 2
        elif a == "--json":
            as_json = True; i += 1
        elif a == "--selftest":
            want_selftest = True; i += 1
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: unknown argument {a}", file=sys.stderr)
            return 2
    if want_selftest:
        return selftest()
    if not lane or not rng:
        print(__doc__, file=sys.stderr)
        return 2
    if git(lane, "rev-parse", "--git-dir").returncode != 0:
        print(f"usage: {lane} is not a git repository", file=sys.stderr)
        return 2
    try:
        rows, n_cited, n_miss = scan(lane, rng)
    except RuntimeError as exc:
        print(f"usage: {exc}", file=sys.stderr)
        return 2
    if as_json:
        print(json.dumps({
            "commits": [{"commit": r["commit"], "cited": r["cited"],
                         "missing": r["missing"], "bare": r["bare"]}
                        for r in rows],
            "summary": {"commits": len(rows), "cited": n_cited,
                        "misses": n_miss},
            "ok": n_miss == 0,
        }, indent=2))
    else:
        print(report(rows, n_cited, n_miss))
    return 0 if n_miss == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
