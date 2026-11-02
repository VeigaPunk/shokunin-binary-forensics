#!/usr/bin/env python
"""orphan_sweep4.py - cited-evidence hygiene instrument v4 (round 83, claim C2).

v4 supersession of reports/round-82/orphan_sweep3.py (v3 stays byte-untouched
as the r82 evidence; v2/v1 stay byte-untouched as the r81/r80 evidence). Same
duty and classes as v3 (committed / orphan / orphan-dir / absent-fleet /
absent, repeated line-ref stripping, dir-style normalization with the
masked-absent negative, registered counting commands with the mutation-checked
fidelity vector, SWEEP_CORPUS count basis, --format full|summary receipts).

v4 change (closes the r83 carry-in class — the bare-filename citation form):

  6. Bare-filename receipt normalization. The r82 carry-in demonstrated the
     class: seven green receipts were cited by the r82 report/LOG/lesson but
     never committed, and the standing v3 instrument flagged only 2 of the 7
     (LANDABLE_ORPHANS=2 over the pre-landing tree, receipt
     .ufo/waves/round-83/sweep-pre-landing.log) because the other five were
     cited by BARE FILENAME (`sweep3-selftest-after.log`, `c1-only.log`, ...)
     and the lane-domain filter `^(?:reports|corpus|\\.ufo/waves)/` skips any
     token without a slash. A cited landable receipt therefore never got
     flagged — a fail-open blind spot in the citation corpus, not in the
     classifier.

     v4 collects bare single tokens (no slash, ASCII, no space/{}*<>|) as
     citations too and normalizes each against the basename index of HEAD ∪
     working tree: no match → not a lane citation (skipped, counted in
     SWEEP_BARE_TOKENS as unmatched); matches → each candidate path is
     classified; any never-committed candidate flags ORPHAN naming the
     candidates; all-committed candidates classify committed. Ambiguity is
     resolved CONSERVATIVELY (one committed match does not launder a second
     uncommitted match with the same basename).

     The frozen sed mutant (one substitution, pinned in
     reports/round-83/claims.md) flips BARE_TOKEN_CLASSIFICATION to False;
     the mutated script's --selftest must die with the attributed last line
     `selftest: bare-filename classification drifted (bare-token class)`,
     exit 1.

v3 change (kept unchanged, closes the r81 non-author closure routed
defect 1 — the counting-command fidelity class):

  5. Registered counting commands. The parser-artifact disposition counts
     become part of the instrument: every plain run prints
       SWEEP_PARSER_GREP_A=<n>   rows matching
                                 ^SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence
       SWEEP_PARSER_GREP_B=<n>   rows matching ^SWEEP absent corpus/lessons/round-64
       SWEEP_PARSER_GREP_AB=<n>  rows matching COUNTCMD_PATTERN (below)
     computed from the same rows the receipt prints, so over a FULL-format
     receipt each value reproduces exactly:
       grep -cE '^SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence' <receipt>
       grep -cE '^SWEEP absent corpus/lessons/round-64' <receipt>
       grep -cE '^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\\.md:57|corpus/lessons/round-64)' <receipt>
     COUNTCMD_PATTERN carries NO trailing space: the r81-closure-pasted form
     `...(corpus/knowledge/round-68-apk-axml-byte-evidence\\.md:57|corpus/lessons/round-64) `
     (trailing space inside the pattern) returns 1, not 2, because the
     multi-ref token prints as `...evidence.md:57,:148,` and the first
     alternative can never be followed by a space. The fidelity vector pins
     truth=2 on exactly that shape; the mutant leg embeds the trailing-space
     defective counter and MUST disagree (1 != 2) — a mutant that agrees
     proves the vector vacuous and dies attributed.

Exit codes (declared, unchanged from v1/v2/v3):
  0   sweep completed, zero landable orphans
  1   >=1 landable orphan flagged, or the sweep could not evaluate (git
      failure), or a selftest leg failed - fail-closed
  64  unrecognized invocation form (usage on stderr)

--selftest runs the hermetic vector suite (no git, no network, no live-tree
write, no producer call): v3's nine legs plus the v4 bare-token vectors
(bare orphan flagged / bare committed / bare unmatched skipped / bare
mutant caught). Plain selftest: last line `SWEEP_SELFTEST=pass`, exit 0.

Usage:
  python -B orphan_sweep4.py --lane <lane-dir> --fleet <fleet-root> [--format full|summary]
  python -B orphan_sweep4.py --selftest
"""
import os
import re
import subprocess
import sys

LANE_DOMAIN = re.compile(r"^(?:reports|corpus|\.ufo/waves)/")
CITE_PAT = re.compile(r"`([^`\n]+)`")
# v4 change 6: the bare-filename classification switch. The frozen mutant
# flips this to False (one sed substitution) and MUST be caught by the
# bare-token selftest vector.
BARE_TOKEN_CLASSIFICATION = True

# v3 registered counting pattern: corrected alternation, NO trailing space.
COUNTCMD_PATTERN = (
    r"^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57"
    r"|corpus/lessons/round-64)"
)
PREFIX_A = r"^SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence"
PREFIX_B = r"^SWEEP absent corpus/lessons/round-64"


def clean_token(tok: str) -> str:
    """Strip command prefixes, fragment anchors and ALL trailing
    line-reference segments (v1 stripped one; v2 strips repeated groups and
    dangling separators - v2 change 1)."""
    tok = tok.strip()
    tok = re.sub(r"^(?:git show \S+?|diff of |sha256sum |cat |bash |python -B )[: ]", "", tok)
    tok = tok.split("#")[0]
    prev = None
    while prev != tok:
        prev = tok
        tok = re.sub(r"(?::\d+[-,\d]*)+$", "", tok)
        tok = re.sub(r"[.,]+$", "", tok)
    return tok.rstrip("/").strip()


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
    # v2 change 2: dir-style cite of a committed .md sibling is not an orphan
    if (cited + ".md") in head_files or (cited + ".md") in disk_files:
        return "committed", "normalized: %s.md committed" % cited
    return "absent", "exists nowhere on this host; recorded, nothing to land"


def classify_blind(cited, head_files, head_dirs, disk_files, disk_dirs, fleet_root):
    """Sabotaged classifier used only by the selftest mutant leg."""
    return "committed", ""


def classify_bare_disabled(cited, head_files, head_dirs, disk_files, disk_dirs):
    """Defective twin used only by the selftest mutant leg: the
    bare-filename class switched off — exactly what the frozen sed mutant
    (BARE_TOKEN_CLASSIFICATION = False) makes every bare token do."""
    return None


def classify_bare(cited, head_files, head_dirs, disk_files, disk_dirs):
    """v4 change 6: normalize a bare (slash-less) cited filename against the
    basename index of HEAD ∪ working tree. Returns None when the token is
    not a lane citation (no candidate path) or the class is switched off;
    otherwise (status, note) over the candidate set — any never-committed
    candidate flags orphan (conservative ambiguity resolution)."""
    if not BARE_TOKEN_CLASSIFICATION:
        return None
    pool = head_files | disk_files | head_dirs | disk_dirs
    candidates = sorted({p for p in pool
                         if p.replace("\\", "/").rsplit("/", 1)[-1] == cited})
    if not candidates:
        return None
    statuses = []
    for cand in candidates:
        status, _note = classify(cand, head_files, head_dirs,
                                 disk_files, disk_dirs, None)
        statuses.append((cand, status))
    bad = [c for c, s in statuses if s.startswith("orphan")]
    if bad:
        return "orphan", "bare-token match never committed: " + ", ".join(bad)
    return "committed", "bare-token normalized: " + ", ".join(
        c for c, _s in statuses)


def count_cmd(lines):
    """v3 registered counting command over SWEEP absent lines (corrected
    form; the fidelity vector pins its truth)."""
    return sum(1 for l in lines if re.search(COUNTCMD_PATTERN, l))


def count_cmd_mutant(lines):
    """Defective twin used only by the selftest mutant leg: the exact
    r81-closure-pasted trailing-space form."""
    pat = r"^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|corpus/lessons/round-64) "
    return sum(1 for l in lines if re.search(pat, l))


def collect_citations(lane_dir, fleet_root):
    """Returns (sorted cited items as (token, is_bare), sources, fleet_report_count,
    lesson_count). v4: bare (slash-less) single tokens are collected as
    citations too and resolved by classify_bare against the basename index;
    slash-bearing tokens must still match LANE_DOMAIN (unchanged)."""
    srcs = []
    rep = os.path.join(fleet_root, ".ufo", "reports")
    n_rep = 0
    if os.path.isdir(rep):
        for rnd in sorted(os.listdir(rep)):
            p = os.path.join(rep, rnd, "revenger.md")
            if os.path.isfile(p):
                srcs.append(("fleet-report-" + rnd, p))
                n_rep += 1
    les = os.path.join(lane_dir, "corpus", "lessons")
    n_les = 0
    if os.path.isdir(les):
        for f in sorted(os.listdir(les)):
            if re.match(r"round-(\d+|-)", f):
                srcs.append(("lesson-" + f, os.path.join(les, f)))
                n_les += 1
    cited = {}
    for name, p in srcs:
        txt = open(p, encoding="utf-8", errors="replace").read()
        for m in CITE_PAT.finditer(txt):
            raw = m.group(1).strip()
            tok = clean_token(raw)
            if not tok or any(c in tok for c in "{}*<>| "):
                continue
            if not all(ord(c) < 128 for c in tok):
                continue
            if LANE_DOMAIN.match(tok):
                cited.setdefault((tok, False), set()).add(name)
            elif "/" not in tok:
                cited.setdefault((tok, True), set()).add(name)
    return sorted(cited.items(), key=lambda kv: kv[0]), n_rep, n_les


def build_tree_sets(lane_dir):
    r = subprocess.run(["git", "-C", lane_dir, "ls-tree", "-r", "--name-only", "HEAD"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("SWEEP_ERROR git ls-tree failed: %s" % r.stderr.strip()[:200], file=sys.stderr)
        return None
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
    return head_files, head_dirs, disk_files, disk_dirs


def run_sweep(lane_dir, fleet_root, fmt="full"):
    sets = build_tree_sets(lane_dir)
    if sets is None:
        return 1, []
    head_files, head_dirs, disk_files, disk_dirs = sets
    cited, n_rep, n_les = collect_citations(lane_dir, fleet_root)
    rows = []
    orphans = 0
    bare_matched = bare_unmatched = 0
    for (tok, is_bare), srcs in cited:
        if is_bare:
            outcome = classify_bare(tok, head_files, head_dirs,
                                    disk_files, disk_dirs)
            if outcome is None:
                bare_unmatched += 1
                continue
            status, note = outcome
            bare_matched += 1
        else:
            status, note = classify(tok, head_files, head_dirs,
                                    disk_files, disk_dirs, fleet_root)
        rows.append((status, tok, note, sorted(srcs)))
        if status.startswith("orphan"):
            orphans += 1
    if fmt == "full":
        for status, tok, note, srcs in rows:
            print("SWEEP %s %s%s" % (status, tok, (" | " + note) if note else ""))
    else:
        print("SWEEP_FORMAT=summary (per-path SWEEP lines suppressed; rerun with --format full)")
    # v3 registered counting commands (computed from the same rows above)
    absent_lines = ["SWEEP absent %s | %s" % (tok, note)
                    for status, tok, note, _srcs in rows if status.startswith("absent")]
    print("SWEEP_PARSER_GREP_A=%d" % sum(1 for l in absent_lines if re.search(PREFIX_A, l)))
    print("SWEEP_PARSER_GREP_B=%d" % sum(1 for l in absent_lines if re.search(PREFIX_B, l)))
    print("SWEEP_PARSER_GREP_AB=%d" % count_cmd(absent_lines))
    print("SWEEP_BARE_TOKENS matched=%d unmatched_skipped=%d" % (
        bare_matched, bare_unmatched))
    print("SWEEP_CORPUS fleet-reports=%d lessons=%d" % (n_rep, n_les))
    print("CITED=%d COMMITTED=%d LANDABLE_ORPHANS=%d ABSENT=%d" % (
        len(rows),
        sum(1 for s, *_ in rows if s.startswith("committed")),
        orphans,
        sum(1 for s, *_ in rows if s.startswith("absent"))))
    print("ORPHAN_SWEEP_LANDABLE=%d" % orphans)
    return (0 if orphans == 0 else 1), rows


def run_selftest():
    """Hermetic vectors over synthetic state; no git, no temp writes."""
    head = {"reports/round-1/claims.md", "corpus/lessons/round-64.md",
            "corpus/knowledge/round-68-apk-axml-byte-evidence.md"}
    head_dirs = {"reports", "reports/round-1", "corpus", "corpus/lessons",
                 "corpus/knowledge"}
    disk = set(head) | {"reports/round-2/secret-draft.log"}
    disk_dirs = {"reports", "reports/round-1", "reports/round-2",
                 "corpus", "corpus/lessons", "corpus/knowledge"}
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
    # v2 line-ref vector: the r80 multi-ref remnant form must clean to the file
    cleaned = clean_token("corpus/knowledge/round-68-apk-axml-byte-evidence.md:57,:148,")
    if cleaned == "corpus/knowledge/round-68-apk-axml-byte-evidence.md" and classify(
            cleaned, head, head_dirs, disk, disk_dirs, fleet)[0] == "committed":
        print("SWEEP_SELFTEST_LINEREF_VECTOR=ok")
    else:
        print("SWEEP_SELFTEST_LINEREF_VECTOR=FAIL")
        fails.append("line-ref remnant not cleaned/classified committed")
    # v2 dir-style vector: extensionless cite of a committed .md sibling
    st3, note3 = classify("corpus/lessons/round-64", head, head_dirs, disk, disk_dirs, fleet)
    if st3 == "committed" and note3.startswith("normalized:"):
        print("SWEEP_SELFTEST_DIRSTYLE_VECTOR=ok")
    else:
        print("SWEEP_SELFTEST_DIRSTYLE_VECTOR=FAIL")
        fails.append("dir-style cite misclassified %s (%s)" % (st3, note3))
    # v2 negative: normalization must not mask a real absent (X and X.md gone)
    st4, _ = classify("corpus/lost-artifact", head, head_dirs, disk, disk_dirs, fleet)
    if st4 == "absent":
        print("SWEEP_SELFTEST_MASKED_ABSENT_NEGATIVE=ok")
    else:
        print("SWEEP_SELFTEST_MASKED_ABSENT_NEGATIVE=FAIL")
        fails.append("normalization masked a real absent as %s" % st4)
    # v2 mutant leg: the blind classifier MUST be caught by the planted-orphan vector
    mst, _ = classify_blind("reports/round-2/secret-draft.log", head, head_dirs, disk, disk_dirs, fleet)
    if mst != "orphan":
        print("SWEEP_SELFTEST_MUTANT_FLAGGED=ok")
    else:
        print("SWEEP_SELFTEST_MUTANT_FLAGGED=FAIL")
        fails.append("mutant not caught (vector vacuous)")
    # v3 count-fidelity vector: exactly the two parser-artifact classes the
    # r81 closure routed (the multi-ref line CANNOT match a trailing-space
    # pattern; truth for the registered command is 2, prefixes 1 + 1).
    vector = [
        "SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence.md:57,:148, | exists nowhere on this host; recorded, nothing to land",
        "SWEEP absent corpus/lessons/round-64 | exists nowhere on this host; recorded, nothing to land",
        "SWEEP absent reports/round-1/nothing-real.md | noise row outside both classes",
        "SWEEP committed corpus/lessons/round-64.md | normalized",
    ]
    truth_total, mut_total = count_cmd(vector), count_cmd_mutant(vector)
    a = sum(1 for l in vector if re.search(PREFIX_A, l))
    b = sum(1 for l in vector if re.search(PREFIX_B, l))
    if truth_total == 2 and a == 1 and b == 1:
        print("SWEEP_SELFTEST_COUNT_FIDELITY=ok (truth=2, A=1, B=1)")
    else:
        print("SWEEP_SELFTEST_COUNT_FIDELITY=FAIL (truth=%d A=%d B=%d)"
              % (truth_total, a, b))
        fails.append("counting-command fidelity drifted (trailing-space class)")
    # v3 mutant leg: the trailing-space defective counter MUST disagree
    # with the pinned truth (1 != 2). Agreement proves the vector vacuous.
    if mut_total != truth_total:
        print("SWEEP_SELFTEST_COUNTCMD_MUTANT_FLAGGED=ok (mutant=%d truth=%d)"
              % (mut_total, truth_total))
    else:
        print("SWEEP_SELFTEST_COUNTCMD_MUTANT_FLAGGED=FAIL")
        fails.append("trailing-space mutant matched the truth (vector vacuous)")
    # v4 bare-token vectors: the r83 carry-in class (cited-by-bare-filename
    # landable receipts invisible to the lane-domain filter). Synthetic
    # state mirrors the carry-in: one committed r81 match + one on-disk-only
    # r82 match under the same basename MUST flag orphan; an all-committed
    # bare token classifies committed; an unmatched bare token is skipped.
    b_head = {"reports/round-81/c1-only.log"}
    b_disk = set(b_head) | {"reports/round-82/c1-only.log"}
    b_dirs = {"reports", "reports/round-81", "reports/round-82"}
    st_b = classify_bare("c1-only.log", b_head, b_dirs, b_disk, b_dirs)
    if st_b is not None and st_b[0] == "orphan" and \
            "reports/round-82/c1-only.log" in st_b[1]:
        print("SWEEP_SELFTEST_BARE_ORPHAN_FLAGGED=ok")
    else:
        print("SWEEP_SELFTEST_BARE_ORPHAN_FLAGGED=FAIL")
        fails.append("bare-token orphan not flagged")
    st_c = classify_bare("claims.md", {"reports/round-1/claims.md"},
                         {"reports", "reports/round-1"},
                         {"reports/round-1/claims.md"},
                         {"reports", "reports/round-1"})
    if st_c is not None and st_c[0] == "committed":
        print("SWEEP_SELFTEST_BARE_COMMITTED=ok")
    else:
        print("SWEEP_SELFTEST_BARE_COMMITTED=FAIL")
        fails.append("bare-token committed misclassified %s" % (st_c,))
    st_u = classify_bare("no-such-receipt.log", b_head, b_dirs, b_disk, b_dirs)
    if st_u is None:
        print("SWEEP_SELFTEST_BARE_UNMATCHED_SKIPPED=ok")
    else:
        print("SWEEP_SELFTEST_BARE_UNMATCHED_SKIPPED=FAIL")
        fails.append("unmatched bare token classified %s" % (st_u,))
    # v4 mutant leg: the disabled twin (the frozen sed mutant's effect) MUST
    # disagree with the bare-orphan vector (skipped != orphan); agreement
    # proves the vector vacuous.
    if classify_bare_disabled("c1-only.log", b_head, b_dirs, b_disk,
                              b_dirs) is None and st_b is not None \
            and st_b[0] == "orphan":
        print("SWEEP_SELFTEST_BARE_MUTANT_FLAGGED=ok (mutant=skipped, vector=orphan)")
    else:
        print("SWEEP_SELFTEST_BARE_MUTANT_FLAGGED=FAIL")
        fails.append("bare mutant agreed with the vector (vacuous)")
    if fails:
        if any("bare" in f for f in fails):
            print("selftest: bare-filename classification drifted (bare-token class)")
        elif any("fidelity" in f for f in fails):
            print("selftest: counting-command fidelity drifted (trailing-space class)")
        else:
            print("selftest: blind classifier accepted a planted orphan")
        return 1
    print("SWEEP_SELFTEST=pass")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args == ["--selftest"]:
        return run_selftest()
    fmt = "full"
    if len(args) in (4, 6) and args[0] == "--lane" and args[2] == "--fleet":
        rest = args[4:]
        if rest and rest[0] == "--format":
            if len(rest) != 2 or rest[1] not in ("full", "summary"):
                print("usage: --format takes full|summary", file=sys.stderr)
                return 64
            fmt = rest[1]
            rest = rest[2:]
        if rest:
            print("usage: orphan_sweep4.py --lane <lane-dir> --fleet <fleet-root> "
                  "[--format full|summary] | --selftest", file=sys.stderr)
            return 64
        code, _ = run_sweep(args[1], args[3], fmt)
        return code
    print("usage: orphan_sweep4.py --lane <lane-dir> --fleet <fleet-root> "
          "[--format full|summary] | --selftest", file=sys.stderr)
    return 64


if __name__ == "__main__":
    raise SystemExit(main())
