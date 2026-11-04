#!/usr/bin/env python3
"""Self-assessment mismatch checker v3 (round-91 C1, calibration; supersedes
v2 `corpus/self_assessment_check2.py`, round-90 C1, whose bytes stay unchanged).

v3 changes SM6 only: v2 read the last token-adjacent `N/D` anywhere on the last
`K_HELD_BACKED` line, which in the lane's own five-cell SCORECARD row is the
*evidence-pointer* cell (round-90 critic, `c1-realformat-counterexample.log`),
so v2 both false-flagged a true row and passed a false one. v3 reads the
**stated before->after cell** — cell index 2 of that table row — and nothing
else. SM1-SM5 are v2's implementations, byte-identical.

Calibration is the distance between what the lane says about itself and what the
repository shows. This gate counts that distance as six named mismatch classes,
each re-derived from bytes or from the lane's git object store, never from prose:

  SM1  README index range: the `QUALITY.md` index line states `Q01-Qnn`; nn must
       equal the highest criterion id in the QUALITY.md table.
  SM2  README index coverage: every top-level `corpus/*.py` file and every
       `corpus/*/` directory must be named in the README (`verify_*.py` files are
       named by the literal glob `verify_*.py`).
  SM3  SHONEN quoted digests: a box that names an existing file and quotes
       `N bytes` or a `sha256 `hex…`` prefix must quote the CURRENT bytes of one
       of the files it names (one mismatch per quoted value).
  SM4  SHONEN verifier authorship: a `[x]` box whose named verifier is a lane
       seat (`revenger-rNN.Name` or `RNNName`) is lane attestation, not a
       non-author check; each such box is one mismatch.
  SM5  SCORECARD commit citations: a backticked 7-40 hex token introduced by
       `pre-registration`, `base`, `tip` or `commit` (from `## Round 61` on) must
       resolve under `git cat-file -e <h>^{commit}` in the lane repo, unless an
       appended `erratum: \\`bad\\` -> \\`good\\`` line names a resolving `good`.
  SM6  SCORECARD K statement (v3, the frozen rule of
       `reports/round-91/claims.md` §C1): take the LAST SCORECARD line that
       names `K_HELD_BACKED`; its *stated region* is cell index 2 when that
       line is a `|`-delimited table row of at least 5 cells, else the whole
       line; truncate the region at the first `K_HELD_BACKED_STRICT`; then read
       the first `N/D` group immediately following the `K_HELD_BACKED` token
       (skipping non-digits, allowing an optional parenthesised score such as
       `(5.7)` between the sides and preferring the right side of `→`/`->`),
       else the last `N/D` group in the region under the same preference, else
       one mismatch (the row does not state the quantity it is judged on).
       SM6 = 0 iff N = README rows whose status is `held` and D = README
       coverage-map rows (`| C<n> ` lines).

Usage:
    python3 -B corpus/self_assessment_check3.py --root TREE [--lane LANE]
        TREE holds corpus/, SHONEN.md, SCORECARD.md and SKILL.md (a
        `git archive <commit> corpus SHONEN.md SCORECARD.md SKILL.md`
        extraction). --lane (required) is the git repo that resolves SM5 hashes.
        Prints SM1..SM6 and
        `SELF_MISMATCH=<n>`. Exit 0 iff n == 0, 1 if n > 0, 2 if a required
        file is missing.
    python3 -B corpus/self_assessment_check3.py --self-test
        A clean synthetic tree scores 0; one planted defect per class scores
        exactly that class; two real-format SM6 legs plant a row whose stated
        cell is false while the pointer cell agrees, and a row whose stated
        cell is true while the pointer cell disagrees; a file-less root exits 2.
        Exit 0 iff all hold.

Read-only: it reads TREE and runs `git cat-file -e` in LANE; it writes nothing
outside its own temp directories.
"""
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CLASSES = ("SM1", "SM2", "SM3", "SM4", "SM5", "SM6")


def txt(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")


def sm1(root):
    readme, quality = txt(root / "corpus/README.md"), txt(root / "corpus/QUALITY.md")
    ids = sorted(int(x) for x in re.findall(r"^\|\s*Q(\d+)\s*\|", quality, re.M))
    m = re.search(r"`QUALITY\.md` — admission criteria Q01[–—-]Q(\d+)", readme)
    if not ids or not m:
        return 1
    contiguous = ids == list(range(1, max(ids) + 1))
    return 0 if int(m.group(1)) == max(ids) and contiguous else 1


def sm2(root):
    readme = txt(root / "corpus/README.md")

    def named(name):
        return re.search(rf"(?<![\w.-]){re.escape(name)}(?![\w-])", readme) is not None

    missing = 0
    for p in sorted((root / "corpus").iterdir()):
        if p.name == "__pycache__":
            continue
        if p.is_file() and p.suffix.lower() == ".py":
            ok = named(p.name) or (p.name.startswith("verify_") and "verify_*.py" in readme)
            missing += 0 if ok else 1
        elif p.is_dir():
            missing += 0 if named(p.name) else 1
    return missing


def boxes(shonen):
    out, cur = [], None
    for line in shonen.splitlines():
        m = re.match(r"^- \[( |x|~)\] ", line)
        if m:
            cur = [m.group(1), [line]]
            out.append(cur)
        elif cur is not None and re.match(r"^\s+\S", line):
            cur[1].append(line)
        else:
            cur = None
    return [(state, "\n".join(lines)) for state, lines in out]


def sm3(root):
    """Each quoted `N bytes` / `sha256 `hex`` is attributed to the NEAREST preceding backticked
    file token in its box; a value with no preceding file token, or whose nearest token is a
    file that does not resolve, or whose bytes differ, is one mismatch."""
    bad = 0
    for _state, text in boxes(txt(root / "SHONEN.md")):
        toks = [(m.start(), m.group(1)) for m in re.finditer(r"`([\w./-]+\.(?:md|py|json))`", text)]

        def near(pos):
            before = [t for t in toks if t[0] < pos]
            return before[-1][1] if before else None

        def blob(tok):
            for cand in (root / tok, root / "corpus" / tok):
                if cand.is_file():
                    return cand.read_bytes()
            return None

        for m in re.finditer(r"(?<![\w-])(\d[\d,]*) bytes", text):
            b = blob(near(m.start())) if near(m.start()) else None
            bad += 0 if b is not None and len(b) == int(m.group(1).replace(",", "")) else 1
        for m in re.finditer(r"sha256 `([0-9a-f]{8,64})", text):
            b = blob(near(m.start())) if near(m.start()) else None
            bad += 0 if b is not None and hashlib.sha256(b).hexdigest().startswith(m.group(1)) else 1
    return bad


SEAT = re.compile(r"(?i:revenger[-_]?r\d+[._]\w+)|(?<![A-Za-z0-9_])R\d{2}[A-Z]\w+")


def sm4(root):
    """A `[x]` box must name its verifier in a `Named non-author verifier:` clause, and the
    named verifier must not be a lane seat. A box that cites a seat report elsewhere in its
    text while naming an outside verifier is not a mismatch."""
    bad = 0
    for state, text in boxes(txt(root / "SHONEN.md")):
        if state != "x":
            continue
        m = re.search(r"Named non-author verifier:\s*([^\n]+?)\.?\s*(?:\n|$)", text)
        bad += 1 if not m or SEAT.search(m.group(1)) else 0
    return bad


def sm5(root, lane, resolve=None):
    resolve = resolve or (lambda h: subprocess.run(
        ["git", "-C", str(lane), "cat-file", "-e", f"{h}^{{commit}}"],
        capture_output=True).returncode == 0)
    text = re.sub(r"```.*?```", "", txt(root / "SCORECARD.md"), flags=re.S)
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("## Round 61")), 0)
    excused = {}
    for l in lines:
        for bad_h, good in re.findall(r"^erratum: `([0-9a-fA-F]{7,40})` -> `([0-9a-fA-F]{7,40})`", l):
            # the correction must share a >= 6 character prefix with the token it corrects
            # (a typo in the tail), never an unrelated commit
            if len(commonprefix(bad_h.lower(), good.lower())) >= 6:
                excused[bad_h.lower()] = good.lower()
    cite = re.compile(r"(?i:pre[- ]?registration|\bbases?|\btips?|\bcommits?)\s*:?\s+`([0-9a-fA-F]{7,40})`(?!…)")
    bad = 0
    for l in lines[start:]:
        if l.startswith("erratum:"):
            continue
        for h in cite.findall(l):
            h = h.lower()
            if resolve(h):
                continue
            good = excused.get(h)
            bad += 0 if good and resolve(good) else 1
    return bad


def commonprefix(a, b):
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return a[:n]


PAIR = r"(\d+)\s*/\s*(\d+)"
ARROW = r"(?:\s*(?:\(\s*[\d.]+\s*\))?\s*(?:→|->)\s*(\d+)\s*/\s*(\d+))?"


def stated_region(line):
    """Step 2: cell index 2 of a `|`-delimited row of >= 5 cells, else the whole line."""
    s = line.strip()
    if s.startswith("|") and s.endswith("|"):
        cells = s.split("|")
        if len(cells) >= 5:
            return cells[2]
    return s


def sm6(root):
    """SCORECARD K statement (v3). The lane states its before->after numbers in
    the stated cell of its own SCORECARD table row; the evidence-pointer cell
    (the counter/probe column) quotes the same counter but is NOT the
    statement. Read the stated region only:

      1. the LAST SCORECARD line containing `K_HELD_BACKED`;
      2. its stated region = cell index 2 if it is a `|` row of >= 5 cells,
         else the whole line;
      3. truncate at the first `K_HELD_BACKED_STRICT` (a different metric);
      4. with the token present, the FIRST `N/D` group immediately following it
         (skipping non-digits, optional `(5.3)` score, right side of `→`/`->`
         preferred); otherwise the LAST `N/D` group in the region under the
         same right-side preference;
      5. no group => one mismatch: the row does not state the quantity it is
         judged on;
      6. SM6 = 0 iff N = README `held` rows and D = README coverage-map rows.
    """
    readme = txt(root / "corpus/README.md")
    rows = [l for l in readme.splitlines() if re.match(r"^\| C[0-9]+ ", l)]
    held = sum(1 for l in rows if re.search(r"\|\s*held\s*\|\s*$", l))
    last = [l for l in txt(root / "SCORECARD.md").splitlines() if "K_HELD_BACKED" in l]
    if not last:
        return 1
    region = stated_region(last[-1]).split("K_HELD_BACKED_STRICT")[0]
    got = None
    m = re.search(r"K_HELD_BACKED", region)
    if m:
        mm = re.match(r"[^0-9]*" + PAIR + ARROW, region[m.end():])
        if mm:
            got = (int(mm.group(1)), int(mm.group(2)))
    if got is None:
        nums = []
        for g in re.finditer(PAIR + ARROW, region):
            nums.append((int(g.group(3) or g.group(1)), int(g.group(4) or g.group(2))))
        if not nums:
            return 1
        got = nums[-1]
    return 0 if got == (held, len(rows)) else 1


def evaluate(root, lane, resolve=None):
    return {"SM1": sm1(root), "SM2": sm2(root), "SM3": sm3(root), "SM4": sm4(root),
            "SM5": sm5(root, lane, resolve), "SM6": sm6(root)}


def required(root):
    return all((root / r).is_file() for r in
               ("corpus/README.md", "corpus/QUALITY.md", "SHONEN.md", "SCORECARD.md"))


def _fixture(root):
    (root / "corpus/fixtures").mkdir(parents=True)
    (root / "corpus/fixtures/f.txt").write_text("f", encoding="utf-8")
    (root / "corpus/tool.py").write_text("print(1)\n", encoding="utf-8")
    (root / "corpus/verify_a.py").write_text("print(1)\n", encoding="utf-8")
    (root / "corpus/QUALITY.md").write_text("| id |\n|---|\n| Q01 | a |\n| Q02 | b |\n", encoding="utf-8")
    rows = "".join(f"| C{i:02d} | s | k | w | {'held' if i <= 8 else 'frontier'} |\n" for i in range(1, 15))
    (root / "corpus/README.md").write_text(
        "- `QUALITY.md` — admission criteria Q01–Q02\n- `tool.py`\n- `fixtures/`\n- `verify_*.py`\n" + rows,
        encoding="utf-8")
    body = b"x" * 100
    (root / "SKILL.md").write_bytes(body)
    (root / "SHONEN.md").write_text(
        f"- [x] Landed `SKILL.md` (100 bytes, sha256 `{hashlib.sha256(body).hexdigest()[:12]}…`).\n"
        "  Named non-author verifier: Someone Outside.\n", encoding="utf-8")
    (root / "SCORECARD.md").write_text(
        "## Round 61 x\nPre-registration `aaaaaaa` ok.\nK_HELD_BACKED 8/14 → 8/14\n", encoding="utf-8")


def _add_row(root, k_line):
    """Append a fifteenth (frontier) coverage-map row and set the K statement."""
    (root / "corpus/README.md").write_text(
        txt(root / "corpus/README.md") + "| C15 | s | k | w | frontier |\n", encoding="utf-8")
    (root / "SCORECARD.md").write_text(
        txt(root / "SCORECARD.md").replace("K_HELD_BACKED 8/14 → 8/14", k_line), encoding="utf-8")


def _table_row(root, row):
    """Append a fifteenth (frontier) coverage-map row and make `row` the whole
    SCORECARD statement: the lane's own five-cell shape
    `| axis | before->after | counter | commits | verdict |`."""
    (root / "corpus/README.md").write_text(
        txt(root / "corpus/README.md") + "| C15 | s | k | w | frontier |\n", encoding="utf-8")
    (root / "SCORECARD.md").write_text(
        "## Round 61 x\nPre-registration `aaaaaaa` ok.\n" + row + "\n", encoding="utf-8")


def self_test():
    good = lambda h: h == "aaaaaaa"  # noqa: E731
    with tempfile.TemporaryDirectory(prefix="rev-r70-sm-") as d:
        d = Path(d)
        clean = d / "clean"
        _fixture(clean)
        got = evaluate(clean, d, good)
        if any(got.values()):
            print(f"SELFTEST FAIL clean tree scored {got}")
            return 1
        muts = {
            "SM1": lambda r: (r / "corpus/README.md").write_text(
                txt(r / "corpus/README.md").replace("Q01–Q02", "Q01–Q01"), encoding="utf-8"),
            "SM2": lambda r: (r / "corpus/new.py").write_text("print(2)\n", encoding="utf-8"),
            "SM3": lambda r: (r / "SHONEN.md").write_text(
                txt(r / "SHONEN.md").replace("100 bytes", "101 bytes"), encoding="utf-8"),
            "SM4": lambda r: (r / "SHONEN.md").write_text(
                txt(r / "SHONEN.md").replace("Someone Outside", "revenger-r64.R64ReviewSkill"), encoding="utf-8"),
            "SM5": lambda r: (r / "SCORECARD.md").write_text(
                txt(r / "SCORECARD.md").replace("`aaaaaaa`", "`bbbbbbb`"), encoding="utf-8"),
            "SM6": lambda r: (r / "SCORECARD.md").write_text(
                txt(r / "SCORECARD.md").replace("8/14 → 8/14", "8/14 → 9/14"), encoding="utf-8"),
        }
        for cls, mutate in muts.items():
            t = d / cls
            _fixture(t)
            mutate(t)
            got = evaluate(t, d, good)
            if got[cls] != 1 or sum(got.values()) != 1:
                print(f"SELFTEST FAIL {cls} planted defect scored {got}")
                return 1
        # erratum: a resolving correction that shares a >= 6 char prefix with the token excuses it;
        # an unrelated resolving commit, or a non-resolving correction, does not
        t = d / "erratum"
        _fixture(t)
        sc = txt(t / "SCORECARD.md").replace("`aaaaaaa`", "`aaaaaab`")
        for tail, want in (("erratum: `aaaaaab` -> `aaaaaaa`\n", 0), ("erratum: `aaaaaab` -> `cccccc1`\n", 1),
                           ("erratum: `aaaaaab` -> `bbbbbbb`\n", 1)):
            (t / "SCORECARD.md").write_text(sc + tail, encoding="utf-8")
            if evaluate(t, d, good)["SM5"] != want:
                print(f"SELFTEST FAIL erratum {tail.strip()} scored SM5={evaluate(t, d, good)['SM5']} want {want}")
                return 1
        # tightened-class legs: each probe must score exactly the named class
        probes = [
            ("SM1", "em dash correct range stays clean", lambda r: (r / "corpus/README.md").write_text(
                txt(r / "corpus/README.md").replace("Q01–Q02", "Q01—Q02"), encoding="utf-8"), 0),
            ("SM1", "a gap in the Q table", lambda r: (r / "corpus/QUALITY.md").write_text(
                "| id |\n|---|\n| Q01 | a |\n| Q03 | b |\n", encoding="utf-8"), 1),
            ("SM2", "name only a substring of a longer README token", lambda r: (r / "corpus/tool_x.py").write_text(
                "print(3)\n", encoding="utf-8"), 1),
            ("SM2", "hidden directory", lambda r: (r / "corpus/.hidden").mkdir(), 1),
            ("SM2", "upper-case suffix", lambda r: (r / "corpus/tool.PY").write_text("print(4)\n", encoding="utf-8"), 1),
            ("SM3", "digest on a non-file", lambda r: (r / "SHONEN.md").write_text(
                "- [~] x\n  `corpus/gone.py` (7 bytes)\n", encoding="utf-8"), 1),
            ("SM3", "stale value on a one-space continuation", lambda r: (r / "SHONEN.md").write_text(
                "- [~] x\n  `SKILL.md` ok\n  `SKILL.md` (9 bytes)\n", encoding="utf-8"), 1),
            ("SM4", "verifier spelled RevengerR64.ReviewSkill", lambda r: (r / "SHONEN.md").write_text(
                txt(r / "SHONEN.md").replace("Someone Outside", "RevengerR64.ReviewSkill"), encoding="utf-8"), 1),
            ("SM4", "outside verifier plus a cited seat report", lambda r: (r / "SHONEN.md").write_text(
                txt(r / "SHONEN.md").replace("Someone Outside.\n", "Someone Outside.\n  Seat report `.ufo/R64ReviewSkill.md` is context.\n"), encoding="utf-8"), 0),
            ("SM5", "upper-case hash", lambda r: (r / "SCORECARD.md").write_text(
                txt(r / "SCORECARD.md").replace("`aaaaaaa`", "`DEADBEE`"), encoding="utf-8"), 1),
            ("SM5", "colon after the introducer", lambda r: (r / "SCORECARD.md").write_text(
                txt(r / "SCORECARD.md") + "commit: `bbbbbbb`\n", encoding="utf-8"), 1),
            ("SM5", "fenced example is not a citation", lambda r: (r / "SCORECARD.md").write_text(
                txt(r / "SCORECARD.md") + "```\nthe token tip `bbbbbbb` must resolve\n```\n", encoding="utf-8"), 0),
            ("SM6", "two K statements, the first wrong", lambda r: (r / "SCORECARD.md").write_text(
                txt(r / "SCORECARD.md").replace("K_HELD_BACKED 8/14 → 8/14", "K_HELD_BACKED 9/14 → 9/14 · K_HELD_BACKED_STRICT 8/14 → 8/14"), encoding="utf-8"), 1),
            ("SM6", "held row with trailing whitespace stays clean", lambda r: (r / "corpus/README.md").write_text(
                txt(r / "corpus/README.md").replace("| held |\n", "| held |  \n"), encoding="utf-8"), 0),
            # v2 denominator legs (round 90): a fifteenth map row makes `/14` stale
            ("SM6", "fifteen rows, stale 8/14 statement", lambda r: _add_row(r, "K_HELD_BACKED 8/14 → 8/14"), 1),
            ("SM6", "fifteen rows, true 8/15 statement", lambda r: _add_row(r, "K_HELD_BACKED 8/14 → 8/15"), 0),
            ("SM6", "fifteen rows, scores between sides", lambda r: _add_row(r, "`K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3)"), 0),
            ("SM6", "fifteen rows, reversed sides", lambda r: _add_row(r, "K_HELD_BACKED 8/15 → 8/14"), 1),
            ("SM6", "fifteen rows, counter-output form", lambda r: _add_row(r, "(`K_HELD_BACKED=8/15`)"), 0),
            ("SM6", "fifteen rows, wrong numerator", lambda r: _add_row(r, "K_HELD_BACKED 8/15 → 9/15"), 1),
            # v3 real-format legs (round 91): the lane's own five-cell row shape, where
            # the stated cell (index 2) and the evidence-pointer cell disagree
            ("SM6", "row: stated cell true, pointer agrees", lambda r: _table_row(r,
                "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3); C05 uncovered | "
                "`reports/round-91/measure.py TREE` (`K_HELD_BACKED=8/15`) | `aaaaaaa` → `bbbbbbb` | **unchanged** |"), 0),
            ("SM6", "row: stated cell FALSE while the pointer cell agrees", lambda r: _table_row(r,
                "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 9/15 (5.3); C05 uncovered | "
                "`reports/round-91/measure.py TREE` (`K_HELD_BACKED=8/15`) | `aaaaaaa` → `bbbbbbb` | **improved** |"), 1),
            ("SM6", "row: stated cell TRUE while the pointer cell disagrees", lambda r: _table_row(r,
                "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3); C05 uncovered | "
                "`reports/round-91/measure.py TREE` (`K_HELD_BACKED=9/15`) | `aaaaaaa` → `bbbbbbb` | **unchanged** |"), 0),
            ("SM6", "row: stated cell carries scores only, pointer carries the N/D", lambda r: _table_row(r,
                "| coverage — knowledge-map ground (K) | 2.9 → **4.3** | probe `K_HELD_BACKED` "
                "(`K_HELD_BACKED` 8/15 → 8/15) | `aaaaaaa` → `bbbbbbb` | improved |"), 1),
        ]
        for i, (cls, label, mutate, want) in enumerate(probes):
            t = d / f"probe{i}"
            _fixture(t)
            mutate(t)
            got = evaluate(t, d, good)
            if got[cls] != want or sum(got.values()) != want:
                print(f"SELFTEST FAIL probe {label}: got {got} want {cls}={want}")
                return 1
        empty = d / "empty"
        empty.mkdir()
        if required(empty):
            print("SELFTEST FAIL empty root counted as evaluable")
            return 1
    print("SELFTEST OK: clean 0; six planted defects each scored exactly their class; twenty-four tightened-class probes (six v2 denominator legs, four v3 real-format legs where the stated cell and the pointer cell disagree) scored as declared; erratum excuses only a resolving, prefix-sharing correction")
    return 0


def main():
    args = sys.argv[1:]
    if args == ["--self-test"]:
        sys.exit(self_test())
    if "--root" in args:
        root = Path(args[args.index("--root") + 1]).resolve()
        if "--lane" not in args:
            print("usage: --lane <repo> is required with --root (SM5 resolves hashes in the lane repo, never in the tree)")
            sys.exit(64)
        lane = Path(args[args.index("--lane") + 1]).resolve()
        if not required(root):
            print("could-not-evaluate: TREE lacks corpus/README.md, corpus/QUALITY.md, SHONEN.md or SCORECARD.md")
            sys.exit(2)
        got = evaluate(root, lane)
        for k in CLASSES:
            print(f"{k}={got[k]}")
        n = sum(got.values())
        print(f"SELF_MISMATCH={n}")
        sys.exit(0 if n == 0 else 1)
    print(__doc__)
    sys.exit(64)


if __name__ == "__main__":
    main()
