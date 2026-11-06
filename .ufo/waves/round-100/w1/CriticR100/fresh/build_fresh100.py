#!/usr/bin/env python3
"""CriticR100 fresh forgery holdout (round 100; C1 calibration on new classes).

Eight new named forgeries, four per profile, plus one honest control per profile. None is one of the
r96 FG01-FG20, r97 FR01-FR12, r98 holdout (c02 V01/V02/E01/E02/E03/R01; c14 R01/V01/V02/Q01/O01/L01)
or r99 holdout (c02 N1-N6; c14 N1-N6) classes.
  c02  fixture tree built by the frozen v6 maker (reports/round-97/c1_k_admit_counter6.py, read-only),
       with the round-96 record bytes copied from the lane rev (never invented).
  c14  the lane commit given by --rev (default 9ddd38ac) with the landing edits: README C14 knowledge
       cell and status held, entry admission-status admitted, S505 queued with used-by em dash. Votes,
       registry and wave artifacts are SYNTHETIC fixture bytes written here (disclosed).
Verdicts are data. Vector specs and trees live under --work; nothing is written to the lane tree.

Usage:
  python3 -B <this file> --counter <counter.py> --profile c02 --work <scratch> [--lane <root>] [--rev <commit>]
  python3 -B <this file> --counter <counter.py> --profile c14 --work <scratch> [--lane <root>] [--rev <commit>]
  add --build-only to build every tree and write vector specs without running any counter.
Prints one row per vector, then HOLDOUT100_CONTROL=... and `HOLDOUT100 accepted=<n>/<m>`.
A verdict is ACCEPTED only when the counter exits 0 AND prints exactly one C1_VERDICT=pass that agrees
with the failing-leg lines; REFUSED only when it exits 1 AND prints exactly one C1_VERDICT=fail that
agrees; anything else is NO-VERDICT (counted as neither). Exit 0 iff the honest control passed and no
vector is NO-VERDICT (build-only: exit 0 iff built).
"""
import argparse, hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--counter", default=None)
ap.add_argument("--profile", choices=["c02", "c14"], default="c02")
ap.add_argument("--work", required=True)
ap.add_argument("--lane", default=str(HERE.parents[5]))
ap.add_argument("--rev", default="9ddd38ac8baef67d689ac36fa233aaaef35b1703")
ap.add_argument("--build-only", action="store_true")
ARGS = ap.parse_args()
LANE = Path(ARGS.lane).resolve()
WORK = Path(ARGS.work).resolve()
PROFILE = ARGS.profile
if not ARGS.build_only and not ARGS.counter:
    sys.exit("usage: --counter <path> is required unless --build-only")
COUNTER = Path(ARGS.counter).resolve() if ARGS.counter else None
WORK.mkdir(parents=True, exist_ok=True)
for _sub in ("tmp", "hyaku", "cw", "vectors"):
    (WORK / _sub).mkdir(exist_ok=True)
os.environ["TMPDIR"] = str(WORK / "tmp")
os.environ["HYAKU_SCRATCH"] = str(WORK / "hyaku")
os.environ["PYTHONUTF8"] = "1"
sys.dont_write_bytecode = True

_FIX = LANE / "reports/round-97/c1_k_admit_counter6.py"
_spec = importlib.util.spec_from_file_location("c1v6_fixture_maker", _FIX)
fx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fx)

ROUND_DATE = "2026-11-05"
QS = [f"Q{i:02d}" for i in range(1, 18)]
PASS_QS14 = ("Q01", "Q02", "Q03", "Q04", "Q05", "Q06", "Q09", "Q10", "Q11", "Q14", "Q16")
ENTRY14 = "corpus/knowledge/round-98-rea-host-readiness.md"
WAVE14 = ".ufo/waves/round-98"
VOTES14 = "reports/round-98/votes"
RECEIPTS14 = "reports/round-98/quote-receipts"
REGISTRY14 = WAVE14 + "/w1/swarm-registry.json"
PIN14 = {"ExecCounterV7": "executor", "ExecHarness7": "executor", "ExecControls": "executor",
         "ScoutReopen": "scout", "ScribeLesson": "scribe", "ConnectorOverlap": "connector",
         "ReviewerClaims": "reviewer", "ReviewerGate": "reviewer", "ReviewerBlind": "reviewer",
         "CriticR98": "critic", "MutationR98": "mutation-tester", "SentinelScope": "sentinel"}
SEATS14 = (("ReviewerGate", "reviewer", "gate-evidence.md"),
           ("ReviewerBlind", "reviewer", "blind-evidence.md"),
           ("CriticR98", "critic", "critic-audit.md"))
R96_RECORD = "corpus/live/runs/round-96"
R96_RECEIPTS = "reports/round-96/quote-receipts"


# ---------------------------------------------------------------- helpers

def rd(p):
    return p.read_text(encoding="utf-8")


def wr(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def jwr(p, obj):
    wr(p, json.dumps(obj, indent=1, ensure_ascii=False))


def jrd(p):
    return fx.strict_json(rd(p))


def cells(line):
    return fx.cells(line)


def digest(text):
    return fx.digest(text)


def sub_row(path, rowid, ncells, fn):
    lines = rd(path).split("\n")
    hits = [i for i, ln in enumerate(lines)
            if re.match(r"^\s{0,3}\|", ln) and len(cells(ln)) == ncells and cells(ln)[0] == rowid]
    assert len(hits) == 1, (str(path), rowid, len(hits))
    lines[hits[0]] = "| " + " | ".join(fn(cells(lines[hits[0]]))) + " |"
    wr(path, "\n".join(lines))


def write_c14_votes(root, dval, note_fn=None):
    """Synthetic c14 votes, registry and wave artifacts bound to digest dval (no seat audit)."""
    for seat, role, art in SEATS14:
        rel = f"{WAVE14}/w1/{seat}/{art}"
        body = (f"seat evidence for {seat}\ncandidate {dval}\n"
                f"fixture artifact built by CriticR98 for the holdout, not a seat audit\n")
        wr(root / rel, body)
        ds = {q: ("PASS" if q in PASS_QS14 else "n/a") for q in QS}
        notes = {}
        for q in QS:
            if ds[q] == "PASS":
                notes[q] = f"{seat} fixture decision for {q}: checked against the built tree bytes, not a seat audit"
            else:
                notes[q] = (f"{seat} fixture n/a for {q}: the fixture entry carries no content that this "
                            f"criterion reads")
        jwr(root / VOTES14 / f"{seat}.json", {
            "seat": seat, "role": role, "candidate_sha256": dval, "decisions": ds,
            "notes": notes, "artifact_path": rel,
            "artifact_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest()})
    jwr(root / REGISTRY14, {"members": {k: {"role": v} for k, v in PIN14.items()}})


def resign14(root):
    """Re-bind the c14 synthetic votes to the entry's current digest after an entry edit."""
    d = digest(rd(root / ENTRY14))
    write_c14_votes(root, d)
    return d


def build_c14_honest(dest):
    dest.mkdir(parents=True)
    ar = subprocess.run(["git", "-C", str(LANE), "archive", "--format=tar", ARGS.rev], capture_output=True)
    if ar.returncode:
        raise SystemExit(f"git archive {ARGS.rev} failed: {ar.stderr[:200]!r}")
    subprocess.run(["tar", "-x", "-C", str(dest)], input=ar.stdout, check=True)
    sub_row(dest / "corpus/README.md", "C14", 5,
            lambda c: [c[0], c[1], "`knowledge/round-98-rea-host-readiness.md`", c[3], "held"])
    text, n = re.subn(r"(?im)^[ \t]*admission-status[ \t]*:.*$", "admission-status: admitted",
                      rd(dest / ENTRY14), count=1)
    assert n == 1, n
    wr(dest / ENTRY14, text)
    sub_row(dest / "corpus/SOURCES.md", "S505", 11,
            lambda c: c[:7] + ["queued"] + c[8:10] + ["\u2014"])
    d = digest(text)
    write_c14_votes(dest, d)
    return d


def build_c02_honest(base):
    base.mkdir(parents=True, exist_ok=True)
    root, _want = fx._fixture(base)
    assert (root / fx.ENTRY).is_file()
    # The v6 freeze predates the saved round-96 record the entry names; copy the committed bytes from
    # the lane rev (never invented), as the r99 builder and the v7 c02 maker do.
    ar = subprocess.run(["git", "-C", str(LANE), "archive", "--format=tar", ARGS.rev, R96_RECORD],
                        capture_output=True)
    if ar.returncode:
        raise SystemExit(f"git archive {R96_RECORD} failed: {ar.stderr[:200]!r}")
    subprocess.run(["tar", "-x", "-C", str(root)], input=ar.stdout, check=True)
    return root


def rebind02(root):
    """Re-sign the v6 fixture's votes (and their artifacts) to the entry's current digest."""
    new = digest(rd(root / fx.ENTRY))
    for vf in sorted((root / fx.VOTES_DIR).glob("*.json")):
        v = jrd(vf)
        art = root / v["artifact_path"]
        b = rd(art).replace(v["candidate_sha256"], new).encode("utf-8")
        art.write_bytes(b)
        v["candidate_sha256"] = new
        v["artifact_sha256"] = hashlib.sha256(b).hexdigest()
        jwr(vf, v)


def one(text, pattern, what):
    hits = re.findall(pattern, text)
    assert len(hits) == 1, (what, len(hits))


# ---------------------------------------------------------------- c02 forgeries (v6 fixture world)

def c02_recheck_listing_only(root):
    # P1: the recheck header names a directory listing; it names no comparison that re-verifies a digest
    p = root / fx.ENTRY
    t = rd(p)
    one(t, r"(?m)^recheck: .*$", "recheck line")
    t, n = re.subn(r"(?m)^recheck: .*$",
                   "recheck: `ls corpus/live/runs/round-96/` lists the saved record files", t, count=1)
    assert n == 1, n
    wr(p, t)
    rebind02(root)


def c02_source_header_main_pin(root):
    # P2: the S502 source header's URL pins the moving branch `main`; the trailing commit text, the
    # SOURCES row and the receipt keep the pinned commit 12f6e09
    p = root / fx.ENTRY
    t = rd(p)
    t, n = re.subn(r"(https://raw\.githubusercontent\.com/morluto/rea/)12f6e0974cc0db0b3a9b86246accc76556837222"
                   r"(/\.agents/skills/reverse-engineer-anything/references/native-and-artifacts\.md)",
                   r"\1main\2", t, count=1)
    assert n == 1, n
    wr(p, t)
    rebind02(root)


def c02_fetchlog_404_receipt_200(root):
    # P3: the fetch log records S502 as HTTP 404 while the receipt the lane wrote keeps http_status 200
    fl = root / R96_RECEIPTS / "fetch-log.md"
    lines = rd(fl).split("\n")
    hits = [i for i, ln in enumerate(lines) if "S502" in ln and " GET " in ln and "HTTP 200" in ln]
    assert len(hits) == 1, hits
    lines[hits[0]] = lines[hits[0]].replace("HTTP 200", "HTTP 404")
    wr(fl, "\n".join(lines))


def c02_record_edited_digest_stale(root):
    # P4: the saved decompiled output is overwritten by a later run that returns 0x2b; the entry's derivation
    # table (decompiled body row) and the record-digest row are left as written
    p = root / R96_RECORD / "codeable-decompiled.c"
    t = rd(p)
    assert t.count("return 0x2a;") == 1, t.count("return 0x2a;")
    wr(p, t.replace("return 0x2a;", "return 0x2b;"))


# ---------------------------------------------------------------- c14 forgeries (landing-candidate tree)

def c14_templated_pass_notes(root):
    # P1: every PASS note of the three seats is one template with the seat name and the Q id substituted;
    # each note is distinct verbatim, so the verbatim-distinctness rule is met
    for seat, _role, _art in SEATS14:
        p = root / VOTES14 / f"{seat}.json"
        v = jrd(p)
        for q in QS:
            if v["decisions"][q] == "PASS":
                v["notes"][q] = (f"{seat} checked {q} against the saved readiness record bytes and found "
                                 f"no discrepancy with the entry text")
        jwr(p, v)


def c14_pass_note_out_of_scope(root):
    # P2: a PASS decision on Q14 whose own note says the criterion is outside the seat's scope and that
    # nothing was checked; the note carries no n/a-style token
    p = root / VOTES14 / "ReviewerGate.json"
    v = jrd(p)
    assert v["decisions"]["Q14"] == "PASS", v["decisions"]["Q14"]
    v["notes"]["Q14"] = ("Q14 falls outside this seat's scope: no clause in the entry carries a hex run "
                         "with a byte count, so nothing was checked")
    jwr(p, v)


def c14_pass_note_other_criterion(root):
    # P3: the note recorded for Q06 is carried under the key Q05 (copy-paste); the note stays distinct
    # verbatim, has at least six tokens and names a different Q id than its key
    p = root / VOTES14 / "ReviewerBlind.json"
    v = jrd(p)
    assert v["decisions"]["Q05"] == "PASS", v["decisions"]["Q05"]
    v["notes"]["Q05"] = ("ReviewerBlind decision on Q06 carried under Q05: checked against the built tree "
                         "bytes, not a seat audit")
    jwr(p, v)


def c14_record_digest_prefixes_transposed(root):
    # P4: in the record-file digest row the prefixes of host-probes-r98.txt and rea-doctor-r98.txt are
    # swapped; the row still names both files and the votes are re-bound to the edited entry
    p = root / ENTRY14
    lines = rd(p).split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.startswith("| record file digests |")]
    assert len(hits) == 1, len(hits)
    ln = lines[hits[0]]
    a = re.search(r"`([0-9a-f]{8})…` \(host-probes-r98\.txt\)", ln)
    b = re.search(r"`([0-9a-f]{8})…` \(rea-doctor-r98\.txt\)", ln)
    assert a and b, (a, b)
    pa, pb = a.group(1), b.group(1)
    assert pa != pb, (pa, pb)
    new = ln.replace(f"`{pa}…` (host-probes-r98.txt)", f"`{pb}…` (host-probes-r98.txt)")
    new = new.replace(f"`{pb}…` (rea-doctor-r98.txt)", f"`{pa}…` (rea-doctor-r98.txt)")
    assert new != ln
    lines[hits[0]] = new
    wr(p, "\n".join(lines))
    resign14(root)


VECTORS = {
    "c02": [
        ("C02-P1-recheck-listing-only", "recheck header names a directory listing, not a re-verification",
         "recheck line replaced by `ls corpus/live/runs/round-96/`; votes re-bound to the new digest",
         c02_recheck_listing_only, "FAIL"),
        ("C02-P2-source-header-main-pin", "source header URL pins a moving branch, SOURCES row keeps the commit",
         "S502 header URL commit replaced by `main`; trailing commit text, SOURCES row and receipt untouched",
         c02_source_header_main_pin, "FAIL"),
        ("C02-P3-fetchlog-404-receipt-200", "fetch log says HTTP 404 for S502, receipt says 200",
         "fetch-log S502 line HTTP 200 -> HTTP 404; receipt and body untouched",
         c02_fetchlog_404_receipt_200, "FAIL"),
        ("C02-P4-record-overwritten-digest-stale", "saved decompiled output changed after the entry was written",
         "codeable-decompiled.c `return 0x2a;` -> `return 0x2b;`; entry and digest rows untouched",
         c02_record_edited_digest_stale, "FAIL"),
    ],
    "c14": [
        ("C14-P1-templated-pass-notes", "three seats' PASS notes are one template with name and Q id swapped",
         "every PASS note of ReviewerGate, ReviewerBlind, CriticR98 rewritten to one template; votes unchanged otherwise",
         c14_templated_pass_notes, "FAIL"),
        ("C14-P2-pass-note-out-of-scope", "PASS decision whose note says the criterion is out of scope",
         "ReviewerGate Q14 stays PASS; note replaced by an out-of-scope, nothing-checked sentence",
         c14_pass_note_out_of_scope, "FAIL"),
        ("C14-P3-pass-note-other-criterion", "PASS note under Q05 names Q06 (copy-paste)",
         "ReviewerBlind Q05 note replaced by the Q06 decision text; Q05 stays PASS",
         c14_pass_note_other_criterion, "FAIL"),
        ("C14-P4-record-digest-prefixes-transposed", "two record-file digest prefixes swapped in the derivation row",
         "host-probes and rea-doctor prefixes swapped in the record digest row; votes re-bound",
         c14_record_digest_prefixes_transposed, "FAIL"),
    ],
}


# ---------------------------------------------------------------- run

def manifest_of(root):
    out = {}
    for p in root.rglob("*"):
        if p.is_file() and not p.is_symlink():
            out[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def classify(rc, out, expected):
    """Strict verdict: exactly one C1_VERDICT line, consistent with rc and the failing-leg lines."""
    verdicts = re.findall(r"^C1_VERDICT=(\w+)$", out, re.M)
    legs = [x for x in re.findall(r"^(C1_[A-Z0-9_]+)=fail$", out, re.M) if x != "C1_VERDICT"]
    k = re.findall(r"^C1_K_HELD_BACKED=(\d+/\d+)$", out, re.M)
    v = verdicts[0] if len(verdicts) == 1 else "none"
    consistent = (len(verdicts) == 1 and v in ("pass", "fail")
                  and ((v == "pass") == (rc == 0)) and ((v == "pass") == (not legs)))
    if expected == "pass":
        outcome = "control-ok" if consistent and v == "pass" else "control-BROKEN"
    elif consistent and v == "pass":
        outcome = "ACCEPTED"
    elif consistent and v == "fail":
        outcome = "refused"
    else:
        outcome = "NO-VERDICT"
    return {"verdict": v, "k_held": k[0] if k else "none", "failing_legs": legs, "outcome": outcome}


def run_counter(tree):
    cmd = [sys.executable, "-B", str(COUNTER), "--profile", PROFILE, "--tree", str(tree),
           "--work", str(WORK / "cw")]
    r = subprocess.run(cmd, cwd=str(WORK), capture_output=True, text=True, env=os.environ.copy())
    return r, cmd


def main():
    base = WORK / PROFILE
    shutil.rmtree(base, ignore_errors=True)
    base.mkdir(parents=True, exist_ok=True)
    if PROFILE == "c14":
        honest = base / "honest"
        d = build_c14_honest(honest)
        print(f"C14_LANDING_BUILT rev={ARGS.rev[:12]} entry_digest={d}")
    else:
        honest = build_c02_honest(base / "honest")
        print("C02_FIXTURE_BUILT source=frozen-v6 _fixture + round-96 record from rev")
    hidx = manifest_of(honest)
    spec_dir = WORK / "vectors" / PROFILE
    if spec_dir.exists():
        shutil.rmtree(spec_dir)
    spec_dir.mkdir(parents=True)
    results, control_outcome, accepted, named, no_verdict = [], None, 0, 0, 0
    entries = [("CONTROL-honest", "control", "none: honest tree, no delta", None, "pass")]
    entries += list(VECTORS[PROFILE])
    for name, cls, desc, fn, expected0 in entries:
        expected = expected0.lower()
        vdir = spec_dir / name
        vdir.mkdir()
        tree = base / "trees" / name
        if tree.exists():
            shutil.rmtree(tree)
        shutil.copytree(honest, tree, symlinks=True)
        if fn:
            fn(tree)
        tidx = manifest_of(tree)
        changed = sorted(r for r in tidx if hidx.get(r) != tidx[r])
        removed = sorted(r for r in hidx if r not in tidx)
        for rel in changed:
            dst = vdir / "changed" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(tree / rel, dst)
        wr(vdir / "removed.txt", "\n".join(removed) + ("\n" if removed else ""))
        jwr(vdir / "vector.json", {"name": name, "profile": PROFILE, "class": cls, "mutation": desc,
                                   "expected": expected, "changed": changed, "removed": removed})
        rc, verdict, k, legs, outcome = None, "not-run", "-", [], "built"
        if COUNTER is not None and not ARGS.build_only:
            r, cmd = run_counter(tree)
            rc = r.returncode
            c = classify(rc, r.stdout, expected)
            verdict, k, legs, outcome = c["verdict"], c["k_held"], c["failing_legs"], c["outcome"]
            wr(vdir / "counter.log", f"# rc={rc}\n# command: {' '.join(cmd[:-4])} --tree <tree>\n"
                                     + r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr.strip() else ""))
            if expected == "pass":
                control_outcome = outcome
            else:
                named += 1
                accepted += outcome == "ACCEPTED"
                no_verdict += outcome == "NO-VERDICT"
        elif expected == "fail":
            named += 1
        results.append({"name": name, "class": cls, "desc": desc, "expected": expected, "rc": rc,
                        "verdict": verdict, "k_held": k, "failing_legs": legs, "outcome": outcome,
                        "changed": changed, "removed": removed})
        shutil.rmtree(tree, ignore_errors=True)
        print(f"{name} | {cls} | rc={rc} | {verdict} | K={k} | {','.join(legs) or '-'} | {expected} | {outcome}")
    jwr(WORK / f"results-{PROFILE}.json", results)
    if control_outcome is None and not ARGS.build_only:
        control_outcome = "control-BROKEN"
    print(f"HOLDOUT100_PROFILE={PROFILE} counter={COUNTER.name if COUNTER else 'none'} "
          f"build_only={ARGS.build_only}")
    if ARGS.build_only:
        print(f"HOLDOUT100_BUILD={'ok' if results else 'empty'} vectors={named}")
    else:
        print(f"HOLDOUT100_CONTROL={control_outcome}")
        print(f"HOLDOUT100 accepted={accepted}/{named}")
        print(f"HOLDOUT100_NO_VERDICT={no_verdict}")
    sums = []
    for p in sorted((WORK / "vectors").rglob("*")):
        if p.is_file():
            sums.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(WORK)}")
    wr(WORK / f"MANIFEST-{PROFILE}.sha256", "\n".join(sums) + "\n")
    if ARGS.build_only:
        return 0
    ok = control_outcome == "control-ok" and no_verdict == 0
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
