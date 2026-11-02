#!/usr/bin/env python
"""orphan_sweep7.py - cited-evidence hygiene instrument v7 (round 86, claim C1).

v7 supersession of reports/round-85/orphan_sweep6.py (v6 stays byte-untouched
as the r85 evidence; v5/v4/v3/v2/v1 stay byte-untouched as the r84/r83/r82/
r81/r80 evidence). Same duty and classes as v6 (committed / orphan /
orphan-dir / absent-fleet / absent, repeated line-ref stripping, dir-style
normalization with the masked-absent negative, bare-filename receipt
normalization with the fleet-root resolution, recorded unmatched-absent rows,
LOG corpus, registered counting commands with the mutation-checked fidelity
vector, SWEEP_CORPUS count basis, --format full|summary receipts).

v7 change (closes the routed vector the r84 lesson named and r85 routed
again - "a per-source citation-sites accounting", candidate vector 1):

  10. SOURCES.md used-by pointer accounting. The census (CORPUS.md v1)
     checks used-by path EXISTENCE for mined rows only; no standing
     instrument checked that a used-by pointer names a document that
     actually CITES the row id back. The r86 preprobe found six live
     drift rows (S448/S449/S450/S451/S453/S456 - one pointer each names
     a real, committed file whose bytes never mention the row; the
     census existence check passes on all six, so the drift was
     invisible by construction). v7 parses the 11-column registry
     (id/status/used-by; the placeholder classes - em dash U+2014,
     en dash U+2013, ASCII hyphen/hyphens, empty - mean no citation
     sites), splits pointers on commas and semicolons, resolves each
     pointer against the working tree first and HEAD second, and counts
     a pointer CITED only when the row id appears word-bounded in the
     named file's bytes. Output (always printed when the registry
     parses, before the gating line): one summary line
     `SWEEP_SRC registry=<disk|HEAD> rows=<n> sites=<n> cited=<n>
     mismatch=<n> absent=<n>` plus one `SWEEP_SRC_MISMATCH <sid> ->
     <pointer>` / `SWEEP_SRC_ABSENT <sid> -> <pointer>` line per
     exception. NON-GATING by design: nothing here changes the exit
     codes (0/1/64 unchanged; only LANDABLE_ORPHANS gates, per v1-v6).
     The r86 claim fixes the six live rows by dropping the one
     non-citing pointer per row (SOURCES rule 2 in-place used-by change,
     old->new logged in the round lesson); the green runs over the same
     tree print mismatch=0, and the hermetic planted vectors + the
     frozen mutant keep the detector mutation-checked.

v6 change (kept unchanged, closes the r84 routed class):

  9. Fleet-root bare-token resolution (see v6 docstring; an unmatched
     extension-bearing bare token whose basename exists under the fleet
     root resolves absent-fleet instead of an unmatched absent row;
     SWEEP_BARE_TOKENS gains an always-printed fleet_resolved= term).

v5 changes (close the two gaps the r83 non-author closure routed on the
standing instrument):

  7. Unmatched extension-bearing bare tokens are RECORDED, not skipped.
     The r83 closure routed the exact defect live: the bare-cited token
     `v4-postlanding-recon.log` (cited by the r83 report x2, the round-83
     lesson, SCORECARD and LOG) matched NOTHING under HEAD or the working
     tree, so v4's classify_bare returned None and the token was skipped as
     unmatched - a cited-but-unresolvable pointer invisible to the
     instrument by construction (its PATH-form twin in the r83
     verifier-spotcheck lesson WAS recorded, as an absent row). v5 records
     an unmatched bare token as an ABSENT row (status "absent", note
     "bare-token unmatched ...") iff it looks like a filename:
       - no ".." (a git range like 60693f2..b56d81b is not a file),
       - not all digits and dots (a version like 6.8.0 is not a file),
       - tail extension ^[A-Za-z0-9][A-Za-z0-9._-]*\\.[A-Za-z0-9]{1,8}$.
     Known disclosed noise classes (recorded, not gating; dispositioned in
     the round lesson): dotted JSON field paths (provider.version,
     subject.digest.sha256, tool.task, parameters.path) pass the filename
     test and print as absent rows; they are not files. The recorded rows
     enter the ABSENT count; exit semantics are unchanged (absent never
     gates - only LANDABLE_ORPHANS does, per v1-v4).
     The v4 selftest leg BARE_UNMATCHED_SKIPPED pinned the token
     `no-such-receipt.log`, which under change 7 is RECORDED; the leg now
     pins the prose class (`no-such-token`, no extension) under the same
     label, and the extension class moves to its own recorded-absent leg.

  8. LOG.md joins the citation corpus. v4 normalized bare tokens found in
     fleet reports + lessons only; the lane's own LOG.md - which cites the
     same receipts the report/lesson cite (LOG.md cited every one of the
     r82 carry-in's seven receipts too) - was a standing corpus blind spot
     (routed r83: "a LOG-corpus expansion is a future registered change
     with its own red/green, not smuggled into v4"). v5 appends LOG.md as
     a citation source; SWEEP_CORPUS gains a log= term (printed always, 0
     when the file is absent or the class is switched off, so the basis
     line's shape is grep-stable).

Frozen sed mutants (one substitution each, recipes pinned in
reports/round-86/claims.md):
  - `USED_BY_ACCOUNTING = True` -> False (change 10 off, the new recipe):
    every used-by pointer is counted but never classified; the
    cite-back vector leg dies attributed `selftest: used-by accounting
    drifted (used-by class)`.
  - `BARE_TOKEN_CLASSIFICATION = True` -> False (the r83 change-6 recipe,
    unchanged): every bare token returns None; the bare orphan/committed
    legs die attributed `selftest: bare-filename classification drifted
    (bare-token class)`.
  - `UNMATCHED_BARE_ABSENT = True` -> False (change 7 off): unmatched
    extension-bearing tokens are skipped again; the recorded-absent leg
    dies attributed `selftest: unmatched-absent recording drifted
    (unmatched-absent class)`.
  - `LOG_CORPUS = True` -> False (change 8 off): LOG.md is not a corpus;
    the log-corpus leg dies attributed `selftest: log-corpus collection
    drifted (log-corpus class)`.
  - `FLEET_BARE_RESOLUTION = True` -> False (change 9 off, the r85
    recipe, unchanged): fleet-side bare tokens fall through to the
    recorded-absent row; the fleet-bare legs die attributed
    `selftest: fleet-bare resolution drifted (fleet-bare class)`.

v4 change (kept unchanged, closes the r83 carry-in class):

  6. Bare-filename receipt normalization (see v4 docstring; classify_bare
     resolves each bare token against the basename index of HEAD + working
     tree; any never-committed candidate flags ORPHAN; conservative
     ambiguity).

v3 change (kept unchanged):

  5. Registered counting commands (SWEEP_PARSER_GREP_A/B/AB with the
     trailing-space fidelity vector and its mutant).

Exit codes (declared, unchanged from v1-v4):
  0   sweep completed, zero landable orphans
  1   >=1 landable orphan flagged, or the sweep could not evaluate (git
      failure), or a selftest leg failed - fail-closed
  64  unrecognized invocation form (usage on stderr)

--selftest runs the hermetic vector suite (no git, no network, no live-tree
write, no producer call): v6's twenty-one legs plus the v7 vectors
(placeholder parse / cite-back vectors with a planted mismatch / absent
pointer vector / used-by mutant caught). Plain selftest: last line
`SWEEP_SELFTEST=pass`, exit 0.

Usage:
  python -B orphan_sweep7.py --lane <lane-dir> --fleet <fleet-root> [--format full|summary]
  python -B orphan_sweep7.py --selftest
"""
import os
import re
import subprocess
import sys

LANE_DOMAIN = re.compile(r"^(?:reports|corpus|\.ufo/waves)/")
CITE_PAT = re.compile(r"`([^`\n]+)`")
# v4 change 6: the bare-filename classification switch. The frozen mutant
# flips this to False (one sed substitution) and MUST be caught by the
# bare-token selftest vectors.
BARE_TOKEN_CLASSIFICATION = True
# v5 change 7: unmatched extension-bearing bare tokens are recorded absent.
UNMATCHED_BARE_ABSENT = True
# v5 change 8: LOG.md joins the citation corpus.
# v6 change 9: an unmatched bare token that names a file under the FLEET
#     root resolves absent-fleet (bare-token normalized) instead of being
#     recorded as an unmatched absent row - the fleet-root bare-name class
#     the r84 lesson dispositioned as known noise. Non-gating either way;
#     exit codes 0/1/64 unchanged.
LOG_CORPUS = True
# v6 change 9: fleet-root bare-token resolution. The frozen mutant flips
# this to False (one sed substitution) and MUST be caught by the
# fleet-bare selftest vectors.
FLEET_BARE_RESOLUTION = True

# v7 change 10: SOURCES.md used-by pointer accounting (per-source
# citation-sites accounting; non-gating). The frozen mutant flips this to
# False (one sed substitution) and MUST be caught by the used-by selftest
# vectors.
USED_BY_ACCOUNTING = True

# v7 change 10: used-by placeholder classes - the registry's "no citation
# sites" markers. The em dash (U+2014) is the contract form (CORPUS.md
# used-by: "...or `—`"); the en dash and the ASCII hyphen forms are kept
# here because a parser that excludes only the ASCII hyphen reads the
# em-dash placeholder as a path (the r86 preprobe's own false-positive
# class: 20 phantom no-disk rows, mined in the round-86 lesson).
USED_BY_PLACEHOLDERS = {"", "-", "--", "\u2014", "\u2013"}

# v3 registered counting pattern: corrected alternation, NO trailing space.
COUNTCMD_PATTERN = (
    r"^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57"
    r"|corpus/lessons/round-64)"
)
PREFIX_A = r"^SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence"
PREFIX_B = r"^SWEEP absent corpus/lessons/round-64"

# v5 change 7: the filename-shape test for unmatched bare tokens.
BARE_FILE_TAIL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*\.[A-Za-z0-9]{1,8}$")


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
    bare-filename class switched off - exactly what the frozen sed mutant
    (BARE_TOKEN_CLASSIFICATION = False) makes every bare token do."""
    return None


def bare_token_fileish(tok: str) -> bool:
    """v5 change 7: does an unmatched bare token look like a filename?
    Ranges (..) and all-digits-and-dots versions are never files; the tail
    extension decides the rest. Dotted JSON field paths pass - a disclosed
    noise class (recorded rows, dispositioned in the round lesson)."""
    if ".." in tok:
        return False
    if re.fullmatch(r"[0-9.]+", tok):
        return False
    return bool(BARE_FILE_TAIL.match(tok))


def classify_bare_absent_disabled(cited, head_files, head_dirs, disk_files, disk_dirs):
    """Defective twin used only by the selftest mutant leg: change 7
    switched off - what the frozen sed mutant (UNMATCHED_BARE_ABSENT =
    False) makes every unmatched bare token do."""
    return None


def classify_bare_fleet_disabled(cited, head_files, head_dirs, disk_files,
                                 disk_dirs, fleet_files):
    """Defective twin used only by the selftest mutant leg: change 9
    switched off - what the frozen sed mutant (FLEET_BARE_RESOLUTION =
    False) makes every fleet-root bare token do: fall through to the v5
    recorded-absent row."""
    if bare_token_fileish(cited):
        return ("absent",
                "bare-token unmatched: no file named %s under HEAD or the "
                "working tree" % cited)
    return None


def classify_bare(cited, head_files, head_dirs, disk_files, disk_dirs,
                  fleet_files=None):
    """v4 change 6 + v5 change 7: normalize a bare (slash-less) cited
    filename against the basename index of HEAD + working tree. Returns
    None when the token is not a lane citation (no candidate path, or the
    class is switched off); otherwise (status, note) over the candidate
    set - any never-committed candidate flags orphan (conservative
    ambiguity resolution). v5: NO candidate and a filename-shaped token
    records an absent row (change 7) instead of being skipped."""
    if not BARE_TOKEN_CLASSIFICATION:
        return None
    pool = head_files | disk_files | head_dirs | disk_dirs
    candidates = sorted({p for p in pool
                         if p.replace("\\", "/").rsplit("/", 1)[-1] == cited})
    if not candidates:
        # v6 change 9: resolve against the fleet-root basename index first
        if FLEET_BARE_RESOLUTION and fleet_files and bare_token_fileish(cited):
            base = cited.replace("\\", "/").rsplit("/", 1)[-1]
            hits = sorted(p for p in fleet_files
                          if p.replace("\\", "/").rsplit("/", 1)[-1] == base)
            if hits:
                shown = ", ".join("fleet/" + h for h in hits[:3])
                more = " (+%d more)" % (len(hits) - 3) if len(hits) > 3 else ""
                return ("absent-fleet",
                        "bare-token normalized: %s%s" % (shown, more))
        if UNMATCHED_BARE_ABSENT and bare_token_fileish(cited):
            return ("absent",
                    "bare-token unmatched: no file named %s under HEAD or the "
                    "working tree" % cited)
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


def parse_sources_registry(txt):
    """v7 change 10 (pure): parse the 11-column SOURCES.md table into
    (sid, status, [pointers]) rows. Placeholder cells (em/en dash, ASCII
    hyphens, empty) parse as no citation sites; non-placeholder cells
    split on commas and semicolons. Rows failing the 11-column shape are
    skipped (the census owns malformed-row gating, W/E codes)."""
    rows = []
    for line in txt.splitlines():
        if not re.match(r"^\|\s*S\d{3,}\s*\|", line):
            continue
        cols = line.split("|")
        if len(cols) < 13:
            continue
        sid = cols[1].strip()
        status = cols[9].strip()
        used_by = cols[11].strip()
        ptrs = []
        if used_by not in USED_BY_PLACEHOLDERS:
            for p in re.split(r"[,;]", used_by):
                p = p.strip()
                if p and p not in USED_BY_PLACEHOLDERS:
                    ptrs.append(p)
        rows.append((sid, status, ptrs))
    return rows


def used_by_accounting(reg_rows, reader, enabled=None):
    """v7 change 10 (pure): per-source citation-sites accounting. For
    every row with at least one pointer, resolve each pointer through
    `reader` (path -> file bytes, or None when unresolvable) and count it
    CITED only when the row id appears word-bounded in the bytes.
    Returns (rows_with_pointers, sites, cited, mismatches, absents) with
    mismatches/absents as lists of (sid, pointer). Non-gating by design:
    the counts feed the SWEEP_SRC summary only, never the exit code.
    enabled=None means the module switch (the frozen sed mutant's
    surface); enabled=False is the twin behavior the mutant produces:
    pointers are counted but never classified, so every mismatch and
    absent is invisible."""
    if enabled is None:
        enabled = USED_BY_ACCOUNTING
    n_rows = n_sites = n_cited = 0
    mismatches, absents = [], []
    for sid, _status, ptrs in reg_rows:
        if not ptrs:
            continue
        n_rows += 1
        for p in ptrs:
            n_sites += 1
            if not enabled:
                continue
            txt = reader(p)
            if txt is None:
                absents.append((sid, p))
            elif re.search(r"(?<![A-Za-z0-9_])" + re.escape(sid)
                           + r"(?![A-Za-z0-9_])", txt):
                n_cited += 1
            else:
                mismatches.append((sid, p))
    return n_rows, n_sites, n_cited, mismatches, absents


def make_used_by_reader(lane_dir, disk_files, head_files):
    """v7 change 10: pointer bytes reader - working tree first (the same
    bytes the census reads), HEAD blob second (committed receipts whose
    checkout is unavailable), None when the pointer resolves nowhere."""
    def reader(path):
        p = path.replace("\\", "/")
        if p in disk_files:
            fp = os.path.join(lane_dir, *p.split("/"))
            try:
                with open(fp, encoding="utf-8", errors="replace") as fh:
                    return fh.read()
            except OSError:
                pass
        if p in head_files:
            r = subprocess.run(["git", "-C", lane_dir, "show",
                                "HEAD:" + p], capture_output=True)
            if r.returncode == 0:
                return r.stdout.decode("utf-8", "replace")
        return None
    return reader


def run_used_by_accounting(lane_dir, disk_files, head_files):
    """v7 change 10: registry parse + accounting + SWEEP_SRC output block.
    Returns nothing; prints the summary line and one exception line per
    mismatch/absent pointer. Registry-missing prints a shape-stable line
    so downstream greps never break. NON-GATING: no return value is
    consumed by the exit-code path."""
    reg_txt = None
    reg_src = "missing"
    rp = os.path.join(lane_dir, "corpus", "SOURCES.md")
    if os.path.isfile(rp):
        with open(rp, encoding="utf-8", errors="replace") as fh:
            reg_txt = fh.read()
        reg_src = "disk"
    elif "corpus/SOURCES.md" in head_files:
        r = subprocess.run(["git", "-C", lane_dir, "show",
                            "HEAD:corpus/SOURCES.md"], capture_output=True)
        if r.returncode == 0:
            reg_txt = r.stdout.decode("utf-8", "replace")
            reg_src = "HEAD"
    if reg_txt is None:
        print("SWEEP_SRC registry=missing rows=0 sites=0 cited=0 "
              "mismatch=0 absent=0")
        return
    reg_rows = parse_sources_registry(reg_txt)
    n_rows, n_sites, n_cited, mism, absm = used_by_accounting(
        reg_rows, make_used_by_reader(lane_dir, disk_files, head_files))
    print("SWEEP_SRC registry=%s rows=%d sites=%d cited=%d mismatch=%d "
          "absent=%d" % (reg_src, n_rows, n_sites, n_cited, len(mism),
                         len(absm)))
    for sid, p in mism:
        print("SWEEP_SRC_MISMATCH %s -> %s" % (sid, p))
    for sid, p in absm:
        print("SWEEP_SRC_ABSENT %s -> %s" % (sid, p))


def count_cmd(lines):
    """v3 registered counting command over SWEEP absent lines (corrected
    form; the fidelity vector pins its truth)."""
    return sum(1 for l in lines if re.search(COUNTCMD_PATTERN, l))


def count_cmd_mutant(lines):
    """Defective twin used only by the selftest mutant leg: the exact
    r81-closure-pasted trailing-space form."""
    pat = r"^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|corpus/lessons/round-64) "
    return sum(1 for l in lines if re.search(pat, l))


def collect_from_text(txt, name, cited, log_enabled=True):
    """v5 change 8 (refactor): token collection from one source text.
    Pure (no I/O) so the selftest can drive it hermetically. When
    log_enabled is False and the source is the LOG corpus, nothing is
    collected - the twin behavior the frozen sed mutant (LOG_CORPUS =
    False) produces for every log-sourced token."""
    if name.startswith("log-") and not (LOG_CORPUS and log_enabled):
        return
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


def collect_citations(lane_dir, fleet_root):
    """Returns (sorted cited items as (token, is_bare), sources,
    fleet_report_count, lesson_count, log_count). v5: LOG.md is appended
    as a citation corpus (change 8); collection itself lives in the pure
    collect_from_text."""
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
    n_log = 0
    if LOG_CORPUS:
        logp = os.path.join(lane_dir, "LOG.md")
        if os.path.isfile(logp):
            srcs.append(("log-LOG.md", logp))
            n_log = 1
    cited = {}
    for name, p in srcs:
        txt = open(p, encoding="utf-8", errors="replace").read()
        collect_from_text(txt, name, cited)
    return sorted(cited.items(), key=lambda kv: kv[0]), n_rep, n_les, n_log


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
    fleet_files = set()
    if FLEET_BARE_RESOLUTION and fleet_root:
        for base, dirs, files in os.walk(fleet_root):
            dirs[:] = [d for d in dirs if d != ".git"]
            rel = os.path.relpath(base, fleet_root).replace("\\", "/")
            prefix = "" if rel == "." else rel + "/"
            for f in files:
                fleet_files.add(prefix + f)
    cited, n_rep, n_les, n_log = collect_citations(lane_dir, fleet_root)
    rows = []
    orphans = 0
    bare_matched = bare_skipped = bare_unmatched_absent = 0
    bare_fleet_resolved = 0
    for (tok, is_bare), srcs in cited:
        if is_bare:
            outcome = classify_bare(tok, head_files, head_dirs,
                                    disk_files, disk_dirs, fleet_files)
            if outcome is None:
                bare_skipped += 1
                continue
            status, note = outcome
            if status == "absent":
                bare_unmatched_absent += 1
            elif status == "absent-fleet":
                bare_fleet_resolved += 1
            else:
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
    print("SWEEP_BARE_TOKENS matched=%d unmatched_skipped=%d "
          "unmatched_recorded_absent=%d fleet_resolved=%d" % (
              bare_matched, bare_skipped, bare_unmatched_absent,
              bare_fleet_resolved))
    print("SWEEP_CORPUS fleet-reports=%d lessons=%d log=%d" % (n_rep, n_les, n_log))
    if USED_BY_ACCOUNTING:
        run_used_by_accounting(lane_dir, disk_files, head_files)
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
    # bare token classifies committed; an unmatched PROSE bare token is
    # skipped (v5 re-pins this leg to the prose class; the extension class
    # is change 7's recorded-absent vector below).
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
    st_u = classify_bare("no-such-token", b_head, b_dirs, b_disk, b_dirs)
    if st_u is None:
        print("SWEEP_SELFTEST_BARE_UNMATCHED_SKIPPED=ok")
    else:
        print("SWEEP_SELFTEST_BARE_UNMATCHED_SKIPPED=FAIL")
        fails.append("unmatched prose token classified %s" % (st_u,))
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
    # v5 change 7 vector: an unmatched EXTENSION-bearing bare token is
    # RECORDED as an absent row - the exact routed r83 defect class
    # (`v4-postlanding-recon.log` cited bare, matched nothing, was skipped).
    st_a = classify_bare("no-such-receipt.log", b_head, b_dirs, b_disk, b_dirs)
    if st_a is not None and st_a[0] == "absent" and \
            "bare-token unmatched" in st_a[1]:
        print("SWEEP_SELFTEST_BARE_UNMATCHED_ABSENT_RECORDED=ok")
    else:
        print("SWEEP_SELFTEST_BARE_UNMATCHED_ABSENT_RECORDED=FAIL")
        fails.append("unmatched absent-file token not recorded (got %s)" % (st_a,))
    # v5 negatives: a git range and a version are never recorded as files.
    st_r = classify_bare("60693f2..b56d81b", b_head, b_dirs, b_disk, b_dirs)
    st_v = classify_bare("6.8.0", b_head, b_dirs, b_disk, b_dirs)
    if st_r is None and st_v is None:
        print("SWEEP_SELFTEST_BARE_RANGE_VERSION_SKIPPED=ok")
    else:
        print("SWEEP_SELFTEST_BARE_RANGE_VERSION_SKIPPED=FAIL (range=%s version=%s)"
              % (st_r, st_v))
        fails.append("range/version token recorded as file (range=%s version=%s)"
                     % (st_r, st_v))
    # v5 mutant leg: the change-7-off twin MUST disagree with the
    # recorded-absent vector (skipped != absent); agreement proves vacuous.
    st_m = classify_bare_absent_disabled("no-such-receipt.log", b_head, b_dirs,
                                         b_disk, b_dirs)
    if st_m is None and st_a is not None and st_a[0] == "absent":
        print("SWEEP_SELFTEST_BARE_ABSENT_MUTANT_FLAGGED=ok (mutant=skipped, vector=absent)")
    else:
        print("SWEEP_SELFTEST_BARE_ABSENT_MUTANT_FLAGGED=FAIL")
        fails.append("unmatched-absent mutant agreed with the vector (vacuous)")
    # v5 change 8 vector: LOG.md is a citation corpus - collect_from_text
    # over a synthetic LOG body collects both a bare receipt token and a
    # reports/ path token under the log source name.
    log_txt = ("notes: `sweep-final.log` landed and `reports/round-9/summary.md` "
               "committed\n")
    lc = {}
    collect_from_text(log_txt, "log-LOG.md", lc)
    got_bare = ((("sweep-final.log", True), {"log-LOG.md"}) in lc.items()
                or ("sweep-final.log", True) in lc)
    got_path = ("reports/round-9/summary.md", False) in lc
    if got_bare and got_path and all(
            "log-LOG.md" in s for s in lc.values()):
        print("SWEEP_SELFTEST_LOGCORPUS_VECTOR=ok")
    else:
        print("SWEEP_SELFTEST_LOGCORPUS_VECTOR=FAIL (collected=%s)" % (sorted(lc.items()),))
        fails.append("log-corpus token not collected")
    # v5 change 8 mutant leg: the log-disabled twin MUST disagree (the log
    # token is not collected when the class is off).
    lc2 = {}
    collect_from_text(log_txt, "log-LOG.md", lc2, log_enabled=False)
    if (("sweep-final.log", True) not in lc2
            and ("reports/round-9/summary.md", False) not in lc2):
        print("SWEEP_SELFTEST_LOGCORPUS_MUTANT_FLAGGED=ok (mutant=empty, vector=2 tokens)")
    else:
        print("SWEEP_SELFTEST_LOGCORPUS_MUTANT_FLAGGED=FAIL")
        fails.append("log-corpus mutant agreed with the vector (vacuous)")
    # v6 change 9 vector: a bare token naming a fleet-root file resolves
    # absent-fleet (bare-token normalized) - the r84 lesson's known-noise
    # class. Negative: a token under NEITHER pool still records absent.
    f_head = {"reports/round-1/claims.md"}
    f_dirs = {"reports", "reports/round-1"}
    f_fleet = {"MISSION.md", ".ufo/reports/round-9/revenger.md"}
    st_fb = classify_bare("MISSION.md", f_head, f_dirs, f_head, f_dirs, f_fleet)
    if st_fb is not None and st_fb[0] == "absent-fleet" and \
            "fleet/MISSION.md" in st_fb[1]:
        print("SWEEP_SELFTEST_FLEET_BARE_RESOLVED=ok")
    else:
        print("SWEEP_SELFTEST_FLEET_BARE_RESOLVED=FAIL (got %s)" % (st_fb,))
        fails.append("fleet-root bare token not resolved (got %s)" % (st_fb,))
    st_fn = classify_bare("no-such-receipt.log", f_head, f_dirs, f_head,
                          f_dirs, f_fleet)
    if st_fn is not None and st_fn[0] == "absent" and \
            "bare-token unmatched" in st_fn[1]:
        print("SWEEP_SELFTEST_FLEET_BARE_ABSENT_NEGATIVE=ok")
    else:
        print("SWEEP_SELFTEST_FLEET_BARE_ABSENT_NEGATIVE=FAIL (got %s)" % (st_fn,))
        fails.append("fleet resolution masked a real absent (got %s)" % (st_fn,))
    # v6 mutant leg: the change-9-off twin MUST disagree with the resolved
    # vector (recorded-absent row != absent-fleet); agreement proves vacuous.
    st_fm = classify_bare_fleet_disabled("MISSION.md", f_head, f_dirs, f_head,
                                         f_dirs, f_fleet)
    if st_fm is not None and st_fm[0] == "absent" and st_fb is not None \
            and st_fb[0] == "absent-fleet":
        print("SWEEP_SELFTEST_FLEET_BARE_MUTANT_FLAGGED=ok "
              "(mutant=absent-row, vector=absent-fleet)")
    else:
        print("SWEEP_SELFTEST_FLEET_BARE_MUTANT_FLAGGED=FAIL (mutant=%s)" % (st_fm,))
        fails.append("fleet-bare mutant agreed with the vector (vacuous)")
    # v7 change 10 vectors: the SOURCES.md used-by pointer accounting.
    # Synthetic registry: S001 one pointer; S002 three pointers (comma,
    # comma, semicolon); S003 em-dash placeholder; S004 ASCII-hyphen
    # placeholder (the preprobe false-positive class - a parser that
    # excludes only ASCII hyphens reads the em-dash form as a path).
    reg_txt_v = (
        "| id | source | kind | tier | scope | anchor | teaches | status"
        " | opened | recheck | used-by |\n"
        "| S001 | a | own-work | A | s | anc | t | mined | 2026-11-02"
        " | 90d | corpus/lessons/round-1.md |\n"
        "| S002 | b | own-work | A | s | anc | t | mined | 2026-11-02"
        " | 90d | corpus/lessons/round-1.md, reports/round-1/claims.md;"
        " SKILL.md |\n"
        "| S003 | c | docs | A | s | anc | t | queued | 2026-11-02"
        " | 90d | \u2014 |\n"
        "| S004 | d | docs | B | s | anc | t | queued | 2026-11-02"
        " | 90d | - |\n"
    )
    reg_v = parse_sources_registry(reg_txt_v)
    ok_reg = len(reg_v) == 4 \
        and reg_v[0][2] == ["corpus/lessons/round-1.md"] \
        and reg_v[1][2] == ["corpus/lessons/round-1.md",
                            "reports/round-1/claims.md", "SKILL.md"] \
        and reg_v[2][2] == [] and reg_v[3][2] == []
    if ok_reg:
        print("SWEEP_SELFTEST_SRC_PLACEHOLDER=ok (em-dash/hyphen skipped, "
              "4 pointers parsed)")
    else:
        print("SWEEP_SELFTEST_SRC_PLACEHOLDER=FAIL (reg=%s)" % (reg_v,))
        fails.append("used-by parse/placeholder drifted")
    def _rd(name):
        return {
            "corpus/lessons/round-1.md": "cites S001 and S002 here",
            "reports/round-1/claims.md": "no source ids in this body",
            "SKILL.md": "body without the id",
        }.get(name)
    n_r, n_s, n_c, mm_v, ab_v = used_by_accounting(reg_v, _rd)
    if (n_r, n_s, n_c) == (2, 4, 2) \
            and mm_v == [("S002", "reports/round-1/claims.md"),
                         ("S002", "SKILL.md")] and ab_v == []:
        print("SWEEP_SELFTEST_SRC_CITEBACK_VECTORS=ok (2 cited, 2 mismatch "
              "planted, 0 absent)")
    else:
        print("SWEEP_SELFTEST_SRC_CITEBACK_VECTORS=FAIL "
              "(%d/%d/%d %s %s)" % (n_r, n_s, n_c, mm_v, ab_v))
        fails.append("used-by cite-back vectors drifted")
    def _rd_absent(name):
        return {"corpus/lessons/round-1.md": "cites S001 and S002 here"}.get(name)
    _n2, _s2, _c2, _mm2, ab2 = used_by_accounting(reg_v, _rd_absent)
    if len(ab2) == 2:
        print("SWEEP_SELFTEST_SRC_ABSENT_VECTOR=ok (2 pointers absent)")
    else:
        print("SWEEP_SELFTEST_SRC_ABSENT_VECTOR=FAIL (%d)" % len(ab2))
        fails.append("used-by absent vector drifted")
    mn_r, mn_s, mn_c, mn_mm, mn_ab = used_by_accounting(reg_v, _rd,
                                                        enabled=False)
    if mn_mm == [] and mn_ab == [] and n_c == 2:
        print("SWEEP_SELFTEST_SRC_MUTANT_FLAGGED=ok (mutant=0 mismatch, "
              "vector=2)")
    else:
        print("SWEEP_SELFTEST_SRC_MUTANT_FLAGGED=FAIL")
        fails.append("used-by mutant agreed with the vector (vacuous)")
    if fails:
        # Attribution order matters: the change-6 mutant (bare classification
        # fully off) also fails the change-7 legs as a consequence, so the
        # bare-token class is attributed before the unmatched-absent class.
        if any("used-by" in f for f in fails):
            print("selftest: used-by accounting drifted (used-by class)")
        elif any("fleet" in f for f in fails):
            print("selftest: fleet-bare resolution drifted (fleet-bare class)")
        elif any("log-corpus" in f for f in fails):
            print("selftest: log-corpus collection drifted (log-corpus class)")
        elif any("bare" in f for f in fails):
            print("selftest: bare-filename classification drifted (bare-token class)")
        elif any("unmatched absent-file" in f or "unmatched-absent" in f
                 or "range/version" in f for f in fails):
            print("selftest: unmatched-absent recording drifted (unmatched-absent class)")
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
            print("usage: orphan_sweep7.py --lane <lane-dir> --fleet <fleet-root> "
                  "[--format full|summary] | --selftest", file=sys.stderr)
            return 64
        code, _ = run_sweep(args[1], args[3], fmt)
        return code
    print("usage: orphan_sweep7.py --lane <lane-dir> --fleet <fleet-root> "
          "[--format full|summary] | --selftest", file=sys.stderr)
    return 64


if __name__ == "__main__":
    raise SystemExit(main())
