#!/usr/bin/env python3
"""CriticR96 fresh-forgery battery against the frozen v5 counter.

Builds honest fixtures with the counter's own _fixture generator, applies one
fresh forged delta each (all outside the 31 frozen EXPECT_FAIL deltas), runs
python3 -B reports/round-96/c1_k_admit_counter5.py --tree <root>, and records
verdicts under receipts/.
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

SCRATCH = Path("/fast/scratch/hyaku/revenger-r96/CriticR96")
SCR = SCRATCH / "scr"
RECEIPTS = SCRATCH / "receipts"
os.environ["HYAKU_SCRATCH"] = str(SCR)
os.environ["PYTHONUTF8"] = "1"
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
COUNTER = LANE / "reports/round-96/c1_k_admit_counter5.py"
ENTRY = "corpus/knowledge/round-96-native-analysis-sessions.md"
WAVE_DIR = ".ufo/waves/round-96"
VOTES_DIR = WAVE_DIR + "/reports-void"  # unused; real one from module below

spec = importlib.util.spec_from_file_location("c1v5", COUNTER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
VOTES_DIR = mod.VOTES_DIR
SEATS = (("ReviewerGate", "reviewer", "gate-evidence.md"),
         ("ReviewerBlind", "reviewer", "blind-evidence.md"),
         ("CriticR96", "critic", "critic-evidence.md"))


def repin(root):
    """Re-pin the three votes to the current entry digest (forger owns the tree)."""
    text = (root / mod.ENTRY).read_text(encoding="utf-8")
    want = mod.digest(text)
    for seat, role, art in SEATS:
        rel = f"{WAVE_DIR}/w1/{seat}/{art}"
        p = root / rel
        p.write_text(f"seat evidence for {seat}\ncandidate {want}\n", encoding="utf-8")
        v = json.loads((root / VOTES_DIR / f"{seat}.json").read_text())
        v["candidate_sha256"] = want
        v["artifact_sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
        (root / VOTES_DIR / f"{seat}.json").write_text(json.dumps(v))
    return want


def run_counter(root):
    r = subprocess.run(["python3", "-B", str(COUNTER), "--tree", str(root)],
                       cwd=str(LANE), capture_output=True, text=True,
                       env=dict(os.environ))
    legs = [ln.split("=")[0] for ln in r.stdout.splitlines()
            if ln.startswith("C1_") and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln]
    verdict = "pass" if "C1_VERDICT=pass" in r.stdout else "fail"
    return r, verdict, legs


def entry_read(root):
    return (root / mod.ENTRY).read_text(encoding="utf-8")


def entry_write(root, text):
    (root / mod.ENTRY).write_text(text, encoding="utf-8")


# ---------------- fresh forgeries (none in the frozen 31-delta map) ----------

def fg01_shadow_decorated(root):
    sh = root / "corpus/knowledge/shadow-r96-decorated.md"
    sh.write_text("source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
                  "admission-status: admitted (round-96 gate, two reviewer votes)\n\n"
                  "# Shadow entry (decorated admitted line)\n", encoding="utf-8")


def fg02_shadow_nested(root):
    d = root / "corpus/knowledge/nested"
    d.mkdir(parents=True, exist_ok=True)
    (d / "shadow-r96-nested.md").write_text(
        "source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
        "admission-status: admitted\n\n# Shadow entry (nested dir)\n", encoding="utf-8")


def fg03_shadow_upper_ext(root):
    (root / "corpus/knowledge/shadow-r96-caps.MD").write_text(
        "source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
        "admission-status: admitted\n\n# Shadow entry (.MD ext)\n", encoding="utf-8")


def fg04_shadow_non_utf8(root):
    p = root / "corpus/knowledge/shadow-r96-latin1.md"
    p.write_bytes(b"source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
                  b"admission-status: admitted \xe9\n\n# Shadow entry (latin-1)\n")


def fg05_html_comment_artifact(root):
    text = entry_read(root)
    want = mod.digest(text)
    p = root / f"{WAVE_DIR}/w1/ReviewerGate/gate-evidence.md"
    p.write_text(f"<!-- wave round-96 evidence; seat ReviewerGate binds candidate "
                 f"{want}; all substantive content withheld -->\n", encoding="utf-8")
    v = json.loads((root / VOTES_DIR / "ReviewerGate.json").read_text())
    v["artifact_sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    (root / VOTES_DIR / "ReviewerGate.json").write_text(json.dumps(v))


def fg06_symlink_alias(root):
    text = entry_read(root)
    want = mod.digest(text)
    planted = root / f"{WAVE_DIR}/w1/ReviewerBlind/planted-shared.md"
    planted.write_text(f"shared wave evidence naming ReviewerGate and ReviewerBlind\n"
                       f"candidate {want}\n", encoding="utf-8")
    link = root / f"{WAVE_DIR}/w1/ReviewerGate/link.md"
    if link.exists() or link.is_symlink():
        link.unlink()
    os.symlink("../ReviewerBlind/planted-shared.md", link)
    v = json.loads((root / VOTES_DIR / "ReviewerGate.json").read_text())
    v["artifact_path"] = f"{WAVE_DIR}/w1/ReviewerGate/link.md"
    v["artifact_sha256"] = hashlib.sha256(planted.read_bytes()).hexdigest()
    (root / VOTES_DIR / "ReviewerGate.json").write_text(json.dumps(v))


def fg07_sid_double_space(root):
    text = entry_read(root)
    text += "\nPer S  0999 and s0888 the atlas approach generalizes.\n"
    entry_write(root, text)
    repin(root)


def fg08_loose_pyc(root):
    (root / "corpus" / "lint_entry_r96.pyc").write_bytes(b"\x00fake-loose-pyc")


def fg09_receipt_irrelevant_quote(root):
    rp = root / mod.RECEIPTS_DIR / "S502.receipt.json"
    r = json.loads(rp.read_text(encoding="utf-8"))
    body = (root / mod.RECEIPTS_DIR / "raw" / "S502.body").read_text(encoding="utf-8")
    quote = "REA native-and-artifacts reference at the pinned revision, re-opened 2026-11-05."
    i = body.index(quote)
    r["quote"] = quote
    r["span"] = {"start": i, "end": i + len(quote)}
    rp.write_text(json.dumps(r, indent=1), encoding="utf-8")


def fg10_sources_url_drift(root):
    sl = root / "corpus/SOURCES.md"
    t = sl.read_text(encoding="utf-8")
    old = "https://raw.githubusercontent.com/morluto/rea/fixture/S502.md"
    assert old in t
    sl.write_text(t.replace(old, "https://attacker.example/rea-native.md", 1),
                  encoding="utf-8")


def fg11_table_lie_fixture_swap(root):
    fx = root / "corpus/fixtures/pe-r75-headless-smoke/fixture.exe"
    b = bytearray(fx.read_bytes())
    b[600] ^= 0xFF
    fx.write_bytes(bytes(b))
    newsha = hashlib.sha256(bytes(b)).hexdigest()
    helper = root / "corpus/hash_fixture_r96.py"
    helper.write_text(
        'import hashlib\nprint("sha256: " + hashlib.sha256(open("corpus/fixtures/'
        'pe-r75-headless-smoke/fixture.exe", "rb").read()).hexdigest())\n',
        encoding="utf-8")
    text = entry_read(root)
    text += ("\n## Embedded re-derivation (self-consistent fence)\n\n"
             "```sh\n$ python3 -B corpus/hash_fixture_r96.py\n"
             f"sha256: {newsha}\n```\n")
    entry_write(root, text)  # derivation table keeps the STALE fe060de1... value
    repin(root)


def fg12_tab_status(root):
    text = entry_read(root)
    new = text.replace("admission-status: admitted", "\tadmission-status: admitted", 1)
    assert new != text
    entry_write(root, new)  # digest() normalizes the tab -> digest unchanged


def fg13_status_below_window(root):
    text = entry_read(root)
    lines = text.splitlines(True)
    idx = next(i for i, l in enumerate(lines)
               if re.match(r"(?i)^\s*admission-status\s*:", l))
    line = lines.pop(idx)
    lines.insert(40, line)
    entry_write(root, "".join(lines))
    repin(root)


def fg14_trio_shift(root):
    text = entry_read(root)
    lines = text.splitlines(True)
    idx = next(i for i, l in enumerate(lines) if l.startswith("recheck:"))
    line = lines.pop(idx)
    lines.insert(40, line)
    entry_write(root, "".join(lines))
    repin(root)


def fg15_qmap_extra_row(root):
    text = entry_read(root)
    text += "| Q18 | PASS | forged extra criterion row outside the pinned Q01-Q17 set |\n"
    entry_write(root, text)
    repin(root)


def fg16_nbsp_status(root):
    text = entry_read(root)
    new = text.replace("admission-status: admitted",
                       "admission-status:\u00a0admitted", 1)
    assert new != text
    entry_write(root, new)


def fg18_usedby_dot_slash(root):
    sl = root / "corpus/SOURCES.md"
    t = sl.read_text(encoding="utf-8")
    old = f"| on-release | {mod.ENTRY_REL} |"
    assert old in t
    sl.write_text(t.replace(old, f"| on-release | ./{mod.ENTRY_REL} |", 1),
                  encoding="utf-8")


def fg19_merged_fetch_log(root):
    fl = root / mod.FETCH_LOG_REL
    lines = fl.read_text(encoding="utf-8").splitlines()
    shas = [ln.split("sha256 ")[1].strip() for ln in lines if ln.startswith("- ")]
    fl.write_text("# fetch log (fixture)\n\n"
                  f"- S502 S503 GET batch -> HTTP 200, sha256 {shas[0]} {shas[1]}\n",
                  encoding="utf-8")


def fg20_prose_status_mention(root):
    text = entry_read(root)
    text += "\n(The admission-status: candidate normalization was re-derived this round.)\n"
    entry_write(root, text)
    repin(root)


FORGERIES = [
    ("FG01-shadow-decorated-admitted", fg01_shadow_decorated, "pass"),
    ("FG02-shadow-nested-dir", fg02_shadow_nested, "pass"),
    ("FG03-shadow-uppercase-ext", fg03_shadow_upper_ext, "pass"),
    ("FG04-shadow-non-utf8", fg04_shadow_non_utf8, "pass"),
    ("FG05-vote-html-comment-artifact", fg05_html_comment_artifact, "pass"),
    ("FG06-vote-symlink-alias", fg06_symlink_alias, "pass"),
    ("FG07-sid-double-space-evade", fg07_sid_double_space, "pass"),
    ("FG08-loose-pyc-file", fg08_loose_pyc, "pass"),
    ("FG09-receipt-quote-irrelevant", fg09_receipt_irrelevant_quote, "pass"),
    ("FG10-sources-url-drift", fg10_sources_url_drift, "pass"),
    ("FG11-table-lie-fixture-swap", fg11_table_lie_fixture_swap, "pass"),
    ("FG12-tab-status-digest-invariant", fg12_tab_status, "pass"),
    ("FG13-status-below-window", fg13_status_below_window, "fail:C1_ADMITTED"),
    ("FG14-trio-line-shift", fg14_trio_shift, "fail:C1_TRIO"),
    ("FG15-qmap-extra-row", fg15_qmap_extra_row, "pass"),
    ("FG16-nbsp-status-fork", fg16_nbsp_status, "fail:C1_ADMITTED"),
    ("FG18-usedby-dot-slash-alias", fg18_usedby_dot_slash, "fail:C1_SOURCES"),
    ("FG19-merged-fetch-log-line", fg19_merged_fetch_log, "pass"),
    ("FG20-prose-status-mention", fg20_prose_status_mention, "fail:C1_ADMITTED"),
]


def main():
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    SCR.mkdir(parents=True, exist_ok=True)
    work = SCRATCH / "fixtures"
    work.mkdir(exist_ok=True)
    summary = []
    for name, fn, expect in FORGERIES:
        root, want = mod._fixture(work)
        fn(root)
        r, verdict, legs = run_counter(root)
        exp_v, exp_leg = (expect.split(":") + [None])[:2] if ":" in expect else (expect, None)
        decided = (verdict == exp_v) and (exp_leg is None or exp_leg in legs)
        (RECEIPTS / f"{name}.log").write_text(r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr else ""),
                                              encoding="utf-8")
        rec = {"delta": name, "expected": expect, "observed_verdict": verdict,
               "observed_failing_legs": legs, "rc": r.returncode, "decided": decided,
               "digest": want}
        (RECEIPTS / f"{name}.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
        summary.append(rec)
        shutil.rmtree(root, ignore_errors=True)
        print(f"{name}: {verdict} rc={r.returncode} failing={legs or '-'} "
              f"decided={decided}")
    (RECEIPTS / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    bad = [s["delta"] for s in summary if not s["decided"]]
    print(f"BATTERY_DONE forgeries={len(summary)} undecided={len(bad)} {bad}")


if __name__ == "__main__":
    main()
