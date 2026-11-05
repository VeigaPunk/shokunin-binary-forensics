#!/usr/bin/env python3
"""CriticR94 attack driver: forgeries beyond the frozen twelve, run against the v3 counter.

Every attempt builds an honest admission-shaped fixture with the counter's own _fixture()
(freeze archive + real entry bytes), applies one mutation, and runs the counter in one of
two modes:
  rev   the landing path: the fixture is committed into a scratch git repo (objects borrowed
        read-only via alternates from the lane so FREEZE_REV resolves) and the counter runs
        `--rev <commit>`, which is how `--rev <landing>` reads symlinks and files.
  tree  the harness path: `--tree <dir>` (shutil.copytree dereferences symlinks).
Prints one line per attempt: NAME: rc=<rc> verdict=<pass|fail> failing=<legs>
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

S = Path("/fast/scratch/hyaku/revenger-r94/CriticR94")
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
COUNTER = LANE / "reports/round-94/c1_k_admit_counter3.py"
OUT = LANE / ".ufo/waves/round-94/w1/CriticR94/receipts"
os.environ["HYAKU_SCRATCH"] = str(S / "hs")
spec = importlib.util.spec_from_file_location("c1v3", str(COUNTER))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

ENTRY = m.ENTRY
WAVE = m.WAVE_DIR + "/w1"
PINNED = m.PINNED_SEATS
README = "corpus/README.md"
SOURCES = "corpus/SOURCES.md"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_vote(root, seat):
    return json.loads((root / m.VOTES_DIR / f"{seat}.json").read_text(encoding="utf-8"))


def save_vote(root, seat, v):
    (root / m.VOTES_DIR / f"{seat}.json").write_text(json.dumps(v), encoding="utf-8")


def set_artifact(root, seat, body, path=None):
    v = load_vote(root, seat)
    ap = root / (path or v["artifact_path"])
    if ap.is_symlink():
        ap.unlink()
    ap.parent.mkdir(parents=True, exist_ok=True)
    data = body.encode("utf-8") if isinstance(body, str) else body
    ap.write_bytes(data)
    v["artifact_sha256"] = sha(data)
    if path:
        v["artifact_path"] = path
    save_vote(root, seat, v)


def resign(root):
    """Re-bind every honest vote to the entry's current normalised digest (attacker can always do this)."""
    want = m.digest((root / ENTRY).read_text(encoding="utf-8"))
    for seat in ("ReviewerGate", "ReviewerBlind", "CriticR94"):
        v = load_vote(root, seat)
        ap = root / v["artifact_path"]
        if ap.is_symlink():
            continue
        set_artifact(root, seat, f"seat evidence for {seat}\ncandidate {want}\n")
        v = load_vote(root, seat)
        v["candidate_sha256"] = want
        save_vote(root, seat, v)
    return want


def edit_entry(root, fn):
    p = root / ENTRY
    t = p.read_text(encoding="utf-8")
    t2 = fn(t)
    assert t2 != t, "entry edit was a no-op"
    p.write_text(t2, encoding="utf-8")


def edit_cell(root, rel, cid, idx, fn):
    p = root / rel
    out, hit = [], False
    for ln in p.read_text(encoding="utf-8").splitlines():
        c = m.cells(ln)
        if len(c) == 5 and c[0] == cid:
            c[idx] = fn(c[idx])
            ln = "| " + " | ".join(c) + " |"
            hit = True
        out.append(ln)
    assert hit, cid
    p.write_text("\n".join(out) + "\n", encoding="utf-8")


def append(root, rel, text):
    p = root / rel
    p.write_text(p.read_text(encoding="utf-8") + text, encoding="utf-8")


SRC_ROW = ("| {sid} | {title} | community | C | {teach} | {anchor} | {col6} | {status} | "
           "2026-10-27 | 90d | {used} |\n")


# ---------------------------------------------------------------- attacks
def a_vote_symlink_sibling(root):
    """Vote artifact is a symlink to another seat's evidence file (sha copied from the target)."""
    resign(root)
    gt = root / WAVE / "ReviewerGate/evidence.md"
    bl = root / WAVE / "ReviewerBlind/evidence.md"
    bl.unlink()
    os.symlink(gt, bl)
    v = load_vote(root, "ReviewerBlind")
    v["artifact_sha256"] = sha(gt.read_bytes())
    save_vote(root, "ReviewerBlind", v)


def a_vote_symlink_outside(root):
    """Vote artifact is a symlink to a digest-bearing file OUTSIDE the wave dir."""
    want = resign(root)
    out = root.parent / "outside-evidence.md"
    out.write_text(f"seat evidence for ReviewerBlind\ncandidate {want}\n", encoding="utf-8")
    bl = root / WAVE / "ReviewerBlind/evidence.md"
    bl.unlink()
    os.symlink(out, bl)
    v = load_vote(root, "ReviewerBlind")
    v["artifact_sha256"] = sha(out.read_bytes())
    save_vote(root, "ReviewerBlind", v)


def a_registry_dup_key(root):
    """Registry JSON with a duplicate seat key: the visible first value is reviewer, the last wins."""
    members = ", ".join(f'"{k}": {{"role": "{v}"}}' for k, v in PINNED.items())
    txt = '{"members": {"CriticR94": {"role": "reviewer"}, ' + members + "}}"
    (root / m.REGISTRY_REL).write_text(txt, encoding="utf-8")


def a_vote_dup_role_key(root):
    """Vote JSON with a duplicate role key: visible 'reviewer' first, parser keeps the last 'critic'."""
    resign(root)
    s = json.dumps(load_vote(root, "CriticR94"))
    s2 = s.replace('"role": "critic"', '"role": "reviewer", "role": "critic"', 1)
    assert s2 != s
    (root / m.VOTES_DIR / "CriticR94.json").write_text(s2, encoding="utf-8")


def a_qmap_empty_cell(root):
    """Entry Q-map decision cell empty for Q05."""
    edit_entry(root, lambda t: t.replace("| Q05 | n/a |", "| Q05 |  |", 1))
    resign(root)


def a_qmap_contradicts_votes(root):
    """Entry Q-map says FAIL for Q02 while every vote says PASS."""
    edit_entry(root, lambda t: t.replace("| Q02 | PASS |", "| Q02 | FAIL |", 1))
    resign(root)


def a_c15_legacy_path(root):
    """C15 cell names legacy/knowledge/round-72-... (a path that does not exist)."""
    edit_cell(root, README, "C15", 2,
              lambda c: c.replace("`knowledge/round-72", "`legacy/knowledge/round-72", 1))


def a_c15_entry_pending(root):
    """C15 cell's backing file is seed.md; the entry is only named as 'pending admission'."""
    edit_cell(root, README, "C15", 2,
              lambda c: "`knowledge/seed.md` (census; `knowledge/round-72-tool-landscape.md` pending admission)")


def a_receipt_span_reversed(root):
    """S498 receipt span end < start."""
    p = root / m.RECEIPTS_DIR / "S498.receipt.json"
    r = json.loads(p.read_text(encoding="utf-8"))
    r["span"] = {"start": r["span"]["end"], "end": r["span"]["start"]}
    p.write_text(json.dumps(r), encoding="utf-8")


def a_receipt_stale_fetch(root):
    """S498/S499 receipts claim fetched_at 2026-10-01 (rows say opened 2026-11-05)."""
    for sid in ("S498", "S499"):
        p = root / m.RECEIPTS_DIR / f"{sid}.receipt.json"
        r = json.loads(p.read_text(encoding="utf-8"))
        r["fetched_at"] = "2026-10-01"
        p.write_text(json.dumps(r), encoding="utf-8")


def a_vote_seat_scout_role(root):
    """ScoutReopen (pinned role scout) votes with role scout."""
    resign(root)
    base = load_vote(root, "CriticR94")
    want = m.digest((root / ENTRY).read_text(encoding="utf-8"))
    body = f"seat evidence for ScoutReopen\ncandidate {want}\n"
    art = f"{WAVE}/ScoutReopen/evidence.md"
    (root / art).parent.mkdir(parents=True, exist_ok=True)
    (root / art).write_text(body, encoding="utf-8")
    v = dict(base, seat="ScoutReopen", role="scout", artifact_path=art, artifact_sha256=sha(body.encode()))
    save_vote(root, "ScoutReopen", v)


def a_vote_canonical_dup(root):
    """Two votes for the same exact seat ReviewerGate in two files (ReviewerGate.b.json sorts first)."""
    resign(root)
    v = load_vote(root, "ReviewerGate")
    want = m.digest((root / ENTRY).read_text(encoding="utf-8"))
    art = f"{WAVE}/ReviewerGate/evidence-b.md"
    body = f"seat evidence for ReviewerGate (second file)\ncandidate {want}\n"
    (root / art).write_text(body, encoding="utf-8")
    v2 = dict(v, artifact_path=art, artifact_sha256=sha(body.encode()))
    (root / m.VOTES_DIR / "ReviewerGate.b.json").write_text(json.dumps(v2), encoding="utf-8")


def a_vote_seat_case_variant(root):
    """Seat spelled reviewergate in its own file: not a pinned name, fails by exact pin."""
    resign(root)
    v = load_vote(root, "ReviewerGate")
    want = m.digest((root / ENTRY).read_text(encoding="utf-8"))
    art = f"{WAVE}/ReviewerGate/evidence-lc.md"
    body = f"seat evidence for reviewergate\ncandidate {want}\n"
    (root / art).write_text(body, encoding="utf-8")
    v2 = dict(v, seat="reviewergate", artifact_path=art, artifact_sha256=sha(body.encode()))
    (root / m.VOTES_DIR / "reviewergate.json").write_text(json.dumps(v2), encoding="utf-8")


def a_indented_dup_status(root):
    """Header line 3 says `  admission-status: rejected` (indented); the real line 11 says admitted."""
    def f(t):
        lines = t.split("\n")
        lines.insert(2, "  admission-status: rejected")
        return "\n".join(lines)
    edit_entry(root, f)
    resign(root)


def a_status_on_line_16(root):
    """The single admitted status moved to line 16 (index 15): outside the header window."""
    def f(t):
        lines = t.split("\n")
        i = next(k for k, l in enumerate(lines) if l.startswith("admission-status:"))
        del lines[i]
        lines.insert(15, "admission-status: admitted")
        return "\n".join(lines)
    edit_entry(root, f)
    resign(root)


def a_s427_renamed_mined(root):
    """S427 (REJECTED_OK, cited in the body) status renamed rejected -> mined."""
    p = root / SOURCES
    out = []
    for ln in p.read_text(encoding="utf-8").split("\n"):
        if ln.startswith("| S427 |"):
            assert "| rejected | 2026-10-30" in ln
            ln = ln.replace("| rejected | 2026-10-30", "| mined | 2026-10-30", 1)
        out.append(ln)
    p.write_text("\n".join(out), encoding="utf-8")


def a_artifact_digest_only(root):
    """Artifacts are only the digest (CriticR94) and whitespace around the digest (ReviewerBlind)."""
    want = resign(root)
    set_artifact(root, "CriticR94", want + "\n")
    set_artifact(root, "ReviewerBlind", "   \n" + want + "\n\n   \n")


def a_na_twenty_letters(root):
    """ReviewerGate's n/a reasons are twenty copies of one letter."""
    resign(root)
    v = load_vote(root, "ReviewerGate")
    for q, d in v["decisions"].items():
        if d == "n/a":
            v["notes"][q] = "n" * 20
    save_vote(root, "ReviewerGate", v)


def a_cite_suffix_unresolved(root):
    """Body cites S0999a (suffix) and 'S 0999' (space): neither matches \\bS\\d{3,}\\b."""
    edit_entry(root, lambda t: t.replace(
        "## Observation, inference, unknown",
        "Per S0999a the atlas approach generalizes; S 0999 is a second form.\n\n## Observation, inference, unknown", 1))
    resign(root)


def a_dup_source_row_last_wins(root):
    """S900 first declared rejected, then re-declared mined; the entry cites S900."""
    rows = (SRC_ROW.format(sid="S900", title="fixture rejected row", teach="rejected fixture",
                           anchor="fixture anchor", col6='"x"', status="rejected", used="knowledge/seed.md")
            + SRC_ROW.format(sid="S900", title="fixture mined row", teach="mined fixture",
                             anchor="fixture anchor", col6='"x"', status="mined", used="knowledge/seed.md"))
    append(root, SOURCES, rows)
    edit_entry(root, lambda t: t.replace("## Observation, inference, unknown",
                                         "Per S900 the approach is tested.\n\n## Observation, inference, unknown", 1))
    resign(root)


def a_fabricated_supersession_terminal(root):
    """S900 is a rejected row; S901 (mined, no receipt) claims supersedes S900; the entry cites S900."""
    rows = (SRC_ROW.format(sid="S900", title="fixture rejected row", teach="rejected fixture",
                           anchor="fixture anchor", col6='"x"', status="rejected", used="knowledge/seed.md")
            + SRC_ROW.format(sid="S901", title="fixture terminal", teach="fixture terminal row",
                             anchor="fixture anchor", col6="supersedes S900 — fixture", status="mined",
                             used="knowledge/seed.md"))
    append(root, SOURCES, rows)
    edit_entry(root, lambda t: t.replace("## Observation, inference, unknown",
                                         "Per S900 the approach is tested.\n\n## Observation, inference, unknown", 1))
    resign(root)


def a_embed_prefix_vacuous(root):
    """A $ command that is NOT the first line of its fence, with no output: vacuous, unchecked."""
    append(root, ENTRY, "\n```sh\necho header\n$ python3 -B corpus/lint_entry.py --self-test\n\n```\n")
    resign(root)


def a_embed_unprompted_transcript(root):
    """A fenced transcript with a % prompt and fabricated output: no $-block, so no check runs."""
    append(root, ENTRY, "\n```text\n% python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-72-tool-landscape.md\nLINT_QMAP=9 fabricated\n```\n")
    resign(root)


def a_trio_inside_html_comment(root):
    """The header trio keys are present (lines 7-10) but sit inside an HTML comment."""
    def f(t):
        lines = t.split("\n")
        lines.insert(7, "<!--")
        lines.insert(11, "-->")
        return "\n".join(lines)
    edit_entry(root, f)
    resign(root)


def a_registry_as_artifact_digest_key(root):
    """ReviewerBlind's artifact is the wave registry, with the digest in an ignored top-level key."""
    want = m.digest((root / ENTRY).read_text(encoding="utf-8"))
    reg = json.loads((root / m.REGISTRY_REL).read_text(encoding="utf-8"))
    reg["candidate"] = want
    (root / m.REGISTRY_REL).write_text(json.dumps(reg), encoding="utf-8")
    v = load_vote(root, "ReviewerBlind")
    v["artifact_path"] = m.REGISTRY_REL
    v["artifact_sha256"] = sha((root / m.REGISTRY_REL).read_bytes())
    save_vote(root, "ReviewerBlind", v)


def a_control_second_row_moved(root):
    edit_cell(root, README, "C07", 4, lambda c: "partial")


def a_control_c15_duplicate_row(root):
    append(root, README, "\n| C15 | duplicate | `knowledge/round-72-tool-landscape.md` | `x` | held |\n")


def a_quality_row_removed_with_qmap(root):
    """The lint criterion list is read from the tree's corpus/QUALITY.md (not pinned): drop Q05 there
    and drop the Q05 Q-map row from the entry. Lint sees no missing criterion; votes still carry Q05."""
    q = root / "corpus/QUALITY.md"
    lines = [l for l in q.read_text(encoding="utf-8").split("\n") if not l.startswith("| Q05 |")]
    q.write_text("\n".join(lines), encoding="utf-8")
    edit_entry(root, lambda t: "\n".join(l for l in t.split("\n") if not l.startswith("| Q05 |")))
    resign(root)


def a_self_consistent_fabricated_body(root):
    """S498's raw body is replaced by invented REA text; fetch_sha256, length, quote and span are
    recomputed so the receipt is internally consistent. Nothing ties the body to the network."""
    body = "REA is a cloud-hosted SaaS scanner that uploads your binaries to its servers.\n"
    quote = "a cloud-hosted SaaS scanner"
    bp = root / m.RECEIPTS_DIR / "raw" / "S498.body"
    bp.write_bytes(body.encode("utf-8"))
    p = root / m.RECEIPTS_DIR / "S498.receipt.json"
    r = json.loads(p.read_text(encoding="utf-8"))
    off = body.index(quote)
    r.update(fetch_sha256=sha(body.encode()), length=len(body.encode()), quote=quote,
             span={"start": off, "end": off + len(quote)})
    p.write_text(json.dumps(r), encoding="utf-8")


def a_honest_author_self_vote(root):
    """Control and residual: ReviewerGate is treated as the entry author. The counter has no author field."""
    return


ATTACKS = [
    # name, fn, modes, expectation (recorded for the findings table, not used by the verdict)
    ("V01-vote-symlink-sibling", a_vote_symlink_sibling, ("rev", "tree"), "fail C1_VOTES (distinct)"),
    ("V02-vote-symlink-outside", a_vote_symlink_outside, ("rev", "tree"), "fail C1_VOTES (containment) in rev; tree dereferences"),
    ("V03-registry-dup-key", a_registry_dup_key, ("rev",), "pass (last-wins json)"),
    ("V04-vote-dup-role-key", a_vote_dup_role_key, ("rev",), "pass (last-wins json)"),
    ("V05-qmap-empty-cell", a_qmap_empty_cell, ("rev",), "fail C1_LINT"),
    ("V06-qmap-contradicts-votes", a_qmap_contradicts_votes, ("rev",), "pass (no Q-map vs vote cross-check)"),
    ("V07-c15-legacy-path", a_c15_legacy_path, ("rev",), "pass (substring cite; findall hits real entry)"),
    ("V08-c15-entry-pending", a_c15_entry_pending, ("rev",), "pass (cite = substring; backing = seed.md)"),
    ("V09-receipt-span-reversed", a_receipt_span_reversed, ("rev",), "fail C1_QUOTES"),
    ("V10-receipt-stale-fetch", a_receipt_stale_fetch, ("rev",), "pass (fetched_at unchecked)"),
    ("V11-vote-seat-scout-role", a_vote_seat_scout_role, ("rev",), "fail C1_VOTES (role)"),
    ("V12-vote-canonical-dup", a_vote_canonical_dup, ("rev",), "fail C1_VOTES (collision)"),
    ("V13-vote-seat-case-variant", a_vote_seat_case_variant, ("rev",), "fail C1_VOTES (pin)"),
    ("V14-indented-dup-status", a_indented_dup_status, ("rev",), "pass (anchor ^admission-status)"),
    ("V15-status-on-line-16", a_status_on_line_16, ("rev",), "fail C1_ADMITTED"),
    ("V16-s427-renamed-mined", a_s427_renamed_mined, ("rev",), "fail C1_SOURCES"),
    ("V17-artifact-digest-only", a_artifact_digest_only, ("rev",), "pass (substring binding)"),
    ("V18-na-twenty-letters", a_na_twenty_letters, ("rev",), "pass (length, not content)"),
    ("V19-cite-suffix-unresolved", a_cite_suffix_unresolved, ("rev",), "pass (regex misses suffix/space)"),
    ("V20-dup-sources-row", a_dup_source_row_last_wins, ("rev",), "C1_SOURCES pass, C1_QUOTES fail (incidental)"),
    ("V21-fabricated-supersession", a_fabricated_supersession_terminal, ("rev",), "pass (terminal self-declared)"),
    ("V22-embed-prefix-vacuous", a_embed_prefix_vacuous, ("rev",), "pass (first-line-only nonvacuous)"),
    ("V23-embed-unprompted-transcript", a_embed_unprompted_transcript, ("rev",), "pass ($-only scope)"),
    ("V24-trio-in-html-comment", a_trio_inside_html_comment, ("rev",), "pass (presence check)"),
    ("V25-registry-as-artifact-digest-key", a_registry_as_artifact_digest_key, ("rev",), "pass"),
    ("C01-control-second-row-moved", a_control_second_row_moved, ("rev",), "fail C1_ONLY_C15"),
    ("C02-control-c15-duplicate-row", a_control_c15_duplicate_row, ("rev",), "fail C1_ROWS_TOTAL"),
    ("V26-quality-row-removed-with-qmap", a_quality_row_removed_with_qmap, ("rev",), "pass (criterion list is tree-supplied)"),
    ("V27-self-consistent-fabricated-body", a_self_consistent_fabricated_body, ("rev",), "pass (quote leg is internal consistency)"),
    ("H00-honest-author-self-vote-residual", a_honest_author_self_vote, ("rev", "tree"), "pass (no author concept)"),
]


def frozen_kills():
    """Independent re-run of the frozen twelve (CriticR94 cross-check of V3_KILLS) in tree mode."""
    kills = 0
    for kind, expect in sorted(m.EXPECT_FAIL.items()):
        work = Path(tempfile.mkdtemp(prefix=f"frozen-{kind}-", dir=S / "work"))
        root, _ = m._fixture(work)
        m._fixture_delta(root, kind)
        r = run_counter("tree", root, "frozen")
        failing = [ln.split("=")[0] for ln in r.stdout.splitlines() if re.match(r"^C1_\w+=fail$", ln)]
        hit = r.returncode != 0 and expect in failing
        kills += hit
        print(f"FROZEN-{kind}: rc={r.returncode} expected={expect} {'KILLED' if hit else 'SURVIVED'} failing={','.join(failing) or 'none'}", flush=True)
        shutil.rmtree(work, ignore_errors=True)
    print(f"FROZEN_KILLS_CRITICR94={kills}/{len(m.EXPECT_FAIL)}", flush=True)


# ---------------------------------------------------------------- harness
def make_rev(root, name):
    fx = S / "fx" / name
    if fx.exists():
        shutil.rmtree(fx)
    fx.mkdir(parents=True)
    git = ["git", "-C", str(fx)]
    subprocess.run(["git", "init", "-q", str(fx)], check=True)
    top = subprocess.run(git + ["rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    assert Path(top).resolve() == fx.resolve(), f"toplevel mismatch {top}"
    alt = fx / ".git/objects/info"
    alt.mkdir(parents=True, exist_ok=True)
    (alt / "alternates").write_text(str(LANE / ".git/objects") + "\n", encoding="utf-8")
    for rel in m.ARCHIVE_PATHS:
        src = root / rel
        if src.is_dir():
            shutil.copytree(src, fx / rel, symlinks=True)
    (fx / "reports/round-94").mkdir(parents=True, exist_ok=True)
    shutil.copy2(COUNTER, fx / "reports/round-94/c1_k_admit_counter3.py")
    subprocess.run(git + ["add", "-A"], check=True)
    subprocess.run(git + ["-c", "user.name=CriticR94", "-c", "user.email=critic@scratch.invalid",
                          "commit", "-q", "-m", f"fixture {name}"], check=True)
    sha_ = subprocess.run(git + ["rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return fx, sha_


def run_counter(mode, root, name):
    env = dict(os.environ, HYAKU_SCRATCH=str(S / "hs"), PYTHONUTF8="1")
    if mode == "rev":
        fx, rev = make_rev(root, name)
        cmd = [sys.executable, "-B", str(fx / "reports/round-94/c1_k_admit_counter3.py"), "--rev", rev]
    else:
        cmd = [sys.executable, "-B", str(COUNTER), "--tree", str(root)]
    return subprocess.run(cmd, cwd=str(S), capture_output=True, text=True, env=env)


def attempt(name, fn, mode, expect):
    work = Path(tempfile.mkdtemp(prefix=f"{name}-", dir=S / "work"))
    root, _ = m._fixture(work)
    fn(root)
    tag = f"{name}.{mode}"
    r = run_counter(mode, root, tag.replace(".", "_"))
    failing = [ln.split("=")[0] for ln in r.stdout.splitlines() if re.match(r"^C1_\w+=fail$", ln)]
    verdict = "pass" if r.returncode == 0 and "C1_VERDICT=pass" in r.stdout else "fail"
    line = f"{tag}: rc={r.returncode} verdict={verdict} failing={','.join(failing) or 'none'}"
    print(line, flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{tag}.txt").write_text(
        f"# {tag}\n# expectation: {expect}\n# rc={r.returncode} verdict={verdict} failing={','.join(failing) or 'none'}\n"
        f"# ---- stdout ----\n{r.stdout}# ---- stderr ----\n{r.stderr}", encoding="utf-8")
    shutil.rmtree(work, ignore_errors=True)
    return verdict, failing


def main(argv):
    S.mkdir(parents=True, exist_ok=True)
    (S / "work").mkdir(parents=True, exist_ok=True)
    only = argv[0] if argv else None
    if only == "frozen":
        frozen_kills()
        return 0
    for name, fn, modes, expect in ATTACKS:
        if only and not name.startswith(only):
            continue
        for mode in modes:
            attempt(name, fn, mode, expect)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
