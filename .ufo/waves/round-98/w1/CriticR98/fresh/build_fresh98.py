#!/usr/bin/env python3
"""CriticR98 fresh forgery holdout (round 98, C1 c14 and C2 c02 calibration). Not r96 FG01-FG20, not r97 FR01-FR12.

Twelve new named forgeries, six per profile, each delta applied to a fully built tree:
  c02  the round-96-era fixture tree built by the frozen v6 fixture maker (C02 held, round-96 entry).
  c14  the lane commit 1b76b4d archive (Amendment C candidate, digest 6d27c129...) plus the landing
       edits the claims describe: README C14 knowledge cell and status held, entry admission-status
       admitted, S505 status queued and used-by em dash. Votes, the wave registry and wave artifacts
       are SYNTHETIC fixture bytes written here (not the seats' votes; they carry no evidence).
Each profile carries one honest control (expected pass).

The fixture maker is the frozen v6 module (reports/round-97/c1_k_admit_counter6.py), imported
read-only with bytecode writing off. The counter under test is run only through --counter.

Usage:
  python3 -B <this file> --work <scratch>                                  # build only, frozen-v6 c02 set needs --counter
  python3 -B <this file> --counter reports/round-97/c1_k_admit_counter6.py --work <scratch>   # frozen v6, c02 set, no profile flag
  python3 -B <this file> --counter <v7> --profile c02 --work <scratch>     # L1, after the v7 freeze
  python3 -B <this file> --counter <v7> --profile c14 --work <scratch>
  add --build-only to build every tree and write vector specs without running any counter.

Writes beside this file: vectors/<profile>/<NAME>/{changed/,removed.txt,vector.json},
results-<profile>.json and MANIFEST.sha256 (sha256 of the builder and every vector spec and overlay).
Exit 0 iff every tree was built, the honest control passed and every verdict was 0 or 1
(build-only: exit 0 iff every tree was built). Verdicts are data; a failing control is reported, not hidden.
"""
import argparse, hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--counter", default=None)
ap.add_argument("--profile", choices=["c02", "c14"], default=None)
ap.add_argument("--c14-variant", choices=["candidate"], default="candidate")
ap.add_argument("--work", required=True)
ap.add_argument("--lane", default=str(HERE.parents[5]))
ap.add_argument("--build-only", action="store_true")
ARGS = ap.parse_args()
LANE = Path(ARGS.lane).resolve()
WORK = Path(ARGS.work).resolve()
PROFILE = ARGS.profile or "c02"
if not ARGS.build_only and not ARGS.counter:
    sys.exit("usage: --counter <path> is required unless --build-only")
COUNTER = Path(ARGS.counter).resolve() if ARGS.counter else None
WORK.mkdir(parents=True, exist_ok=True)
for _sub in ("tmp", "hyaku", "cw"):
    (WORK / _sub).mkdir(exist_ok=True)
os.environ["TMPDIR"] = str(WORK / "tmp")
os.environ["HYAKU_SCRATCH"] = str(WORK / "hyaku")
os.environ["PYTHONUTF8"] = "1"
sys.dont_write_bytecode = True

_FIX = LANE / "reports/round-97/c1_k_admit_counter6.py"
_spec = importlib.util.spec_from_file_location("c1v6_fixture_maker", _FIX)
fx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fx)

BASE_REV = "1b76b4d18be824baa52b9c4c141b6a26138a2b6f"
ROUND_DATE = "2026-11-05"
QS = [f"Q{i:02d}" for i in range(1, 18)]
PASS_QS = ("Q01", "Q02", "Q03", "Q04", "Q05", "Q06", "Q09", "Q10", "Q11", "Q14", "Q16")
ENTRY14 = "corpus/knowledge/round-98-rea-host-readiness.md"
ENTRY14_REL = "knowledge/round-98-rea-host-readiness.md"
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
CANDIDATE_DIGEST = "6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f"


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


def sub_row(path, rowid, ncells, fn):
    lines = rd(path).split("\n")
    hits = [i for i, ln in enumerate(lines)
            if re.match(r"^\s{0,3}\|", ln) and len(cells(ln)) == ncells and cells(ln)[0] == rowid]
    assert len(hits) == 1, (str(path), rowid, len(hits))
    lines[hits[0]] = "| " + " | ".join(fn(cells(lines[hits[0]]))) + " |"
    wr(path, "\n".join(lines))


def git_show(rel):
    r = subprocess.run(["git", "-C", str(LANE), "show", f"{BASE_REV}:{rel}"], capture_output=True)
    if r.returncode:
        raise SystemExit(f"git show {rel}: {r.stderr[:200]!r}")
    return r.stdout


def digest(text):
    return fx.digest(text)


def rebind02(root):
    """Re-sign the v6 fixture's votes to the entry's new digest (same rule as the r97 builder)."""
    new = digest(rd(root / fx.ENTRY))
    for vf in sorted((root / fx.VOTES_DIR).glob("*.json")):
        v = jrd(vf)
        art = root / v["artifact_path"]
        b = rd(art).replace(v["candidate_sha256"], new).encode("utf-8")
        art.write_bytes(b)
        v["candidate_sha256"] = new
        v["artifact_sha256"] = hashlib.sha256(b).hexdigest()
        jwr(vf, v)




def decisions14(seat):
    ds = {q: ("PASS" if q in PASS_QS else "n/a") for q in QS}
    notes = {}
    for q in QS:
        if ds[q] == "PASS":
            notes[q] = f"{seat} fixture decision for {q}: checked against the built tree bytes, not a seat audit"
        else:
            notes[q] = (f"{seat} fixture n/a for {q}: the fixture entry carries no content that this "
                        f"criterion reads")
    return ds, notes


def write_c14_round98(root, digest_value):
    for seat, role, art in SEATS14:
        rel = f"{WAVE14}/w1/{seat}/{art}"
        body = (f"seat evidence for {seat}\ncandidate {digest_value}\n"
                f"fixture artifact built by CriticR98 for the holdout, not a seat audit\n")
        wr(root / rel, body)
        ds, notes = decisions14(seat)
        jwr(root / VOTES14 / f"{seat}.json", {
            "seat": seat, "role": role, "candidate_sha256": digest_value, "decisions": ds,
            "notes": notes, "artifact_path": rel,
            "artifact_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest()})
    jwr(root / REGISTRY14, {"members": {k: {"role": v} for k, v in PIN14.items()}})


def build_c14_honest(dest, variant):
    dest.mkdir(parents=True)
    ar = subprocess.run(["git", "-C", str(LANE), "archive", "--format=tar", BASE_REV], capture_output=True)
    if ar.returncode:
        raise SystemExit("git archive of the claims freeze failed")
    subprocess.run(["tar", "-x", "-C", str(dest)], input=ar.stdout, check=True)
    # landing edit 1: README C14 knowledge cell and status
    sub_row(dest / "corpus/README.md", "C14", 5,
            lambda c: [c[0], c[1], "`knowledge/round-98-rea-host-readiness.md`", c[3], "held"])
    # landing edit 2: entry admission-status line only
    ep = dest / ENTRY14
    text, n = re.subn(r"(?im)^[ \t]*admission-status[ \t]*:.*$", "admission-status: admitted", rd(ep), count=1)
    assert n == 1, n
    wr(ep, text)
    # landing edit 3: S505 correction (status queued, used-by em dash)
    sub_row(dest / "corpus/SOURCES.md", "S505", 11,
            lambda c: c[:7] + ["queued"] + c[8:10] + ["\u2014"])
    d = digest(text)
    if variant == "candidate":
        assert d == CANDIDATE_DIGEST, d
    write_c14_round98(dest, d)
    return d


def build_c02_honest(base):
    base.mkdir(parents=True, exist_ok=True)
    root, _want = fx._fixture(base)
    assert (root / fx.ENTRY).is_file()
    return root


# ---------------------------------------------------------------- c02 deltas (frozen-v6 fixture world)

def d02_hidden_dissent_vote(root):
    # V01: a FAIL vote saved under an upper-case extension; the v6 glob is "*.json", so it is never read
    v = jrd(root / fx.VOTES_DIR / "ReviewerBlind.json")
    v["decisions"]["Q05"] = "FAIL"
    v["notes"]["Q05"] = "dissent saved by the blind seat: the probe line lacks its command"
    jwr(root / fx.VOTES_DIR / "ReviewerBlind.JSON", v)


def d02_qid_list_na(root):
    # V02: n/a reason made only of criterion ids; passes the >=6 tokens and names-a-Q-id test
    v = jrd(root / fx.VOTES_DIR / "ReviewerGate.json")
    assert v["decisions"]["Q07"] == "n/a"
    v["notes"]["Q07"] = "see Q01 Q02 Q03 Q04 Q05 Q06 for the reason"
    jwr(root / fx.VOTES_DIR / "ReviewerGate.json", v)


def d02_recheck_none(root):
    # E01: recheck header present but names no re-verifying command; votes re-bound
    p = root / fx.ENTRY
    t, n = re.subn(r"(?m)^recheck:.*$", "recheck: none", rd(p), count=1)
    assert n == 1
    wr(p, t)
    rebind02(root)


def d02_two_run_clause_count(root):
    # E02: two hex runs in one clause; the wrong count (3 bytes for 2 bytes) is not checked by Q14 lint
    p = root / fx.ENTRY
    t = rd(p)
    line = ("The payload `B82A000000C3` (6 bytes) and its tail `0102` (3 bytes) are quoted from the "
            "committed fixture.\n\n")
    i = t.index("## §Q-map")
    wr(p, t[:i] + line + t[i:])
    rebind02(root)


def d02_coverage_map_other_row(root):
    # E03: coverage-map header names C05 while C02's README cell cites this entry
    p = root / fx.ENTRY
    t, n = re.subn(r"(?m)^coverage-map: C02", "coverage-map: C05", rd(p), count=1)
    assert n == 1
    wr(p, t)
    rebind02(root)


def d02_candidate_backs_held_c06(root):
    # R01: held C06 row cites an unadmitted (candidate) entry of another round; K counts file existence
    (root / ENTRY14).parent.mkdir(parents=True, exist_ok=True)
    (root / ENTRY14).write_bytes(git_show(ENTRY14))
    sub_row(root / "corpus/README.md", "C06", 5,
            lambda c: [c[0], c[1], "`knowledge/round-98-rea-host-readiness.md`", c[3], c[4]])


# ---------------------------------------------------------------- c14 deltas (landing tree)

def d14_suffix_row_hidden(root):
    # R01: a held coverage row whose id carries a letter suffix; the cov regex (C[0-9]+ ) does not count it
    p = root / "corpus/README.md"
    lines = rd(p).split("\n")
    i = next(i for i, ln in enumerate(lines) if re.match(r"^\|\s*C14\s", ln))
    lines.insert(i + 1, "| C14a | host readiness duplicate for REA routes | "
                        "`knowledge/round-98-rea-host-readiness.md` | \u2014 | held |")
    wr(p, "\n".join(lines))


def d14_placeholder_pass_note(root):
    # V01: a PASS decision whose note is a one-word placeholder
    v = jrd(root / VOTES14 / "ReviewerGate.json")
    assert v["decisions"]["Q09"] == "PASS"
    v["notes"]["Q09"] = "ok"
    jwr(root / VOTES14 / "ReviewerGate.json", v)


def d14_fail_under_extra_key(root):
    # V02: a FAIL recorded under a decision key outside Q01-Q17
    v = jrd(root / VOTES14 / "ReviewerBlind.json")
    v["decisions"]["Q18"] = "FAIL"
    v["notes"]["Q18"] = "fixture dissent recorded under a key outside the criterion list"
    jwr(root / VOTES14 / "ReviewerBlind.json", v)


def d14_receipt_span_shift(root):
    # Q01: S506 receipt span moved one byte; the quote text is intact in the body, the span names other bytes
    p = root / RECEIPTS14 / "S506.receipt.json"
    r = jrd(p)
    r["span"] = {"start": r["span"]["start"] + 1, "end": r["span"]["end"] + 1}
    jwr(p, r)


def d14_ownwork_foreign_round(root):
    # O01: S507 own-work pointer re-pointed to an existing round-96 record; the entry still cites round-98 files
    sub_row(root / "corpus/SOURCES.md", "S507", 11,
            lambda c: [c[0], c[1].replace("corpus/live/runs/round-98/", "corpus/live/runs/round-96/")] + c[2:])


def d14_fetchlog_date(root):
    # L01: fetch-log header date moved to 2026-11-04; the S506 receipt still says fetched_at 2026-11-05
    p = root / RECEIPTS14 / "fetch-log.md"
    t = rd(p)
    assert ROUND_DATE in t.split("\n")[0]
    wr(p, t.replace(ROUND_DATE, "2026-11-04", 1))


VECTORS = {
    "c02": [
        ("C02-V01-hidden-dissent-uppercase-vote", "vote file outside the *.json glob hides a FAIL vote",
         "ReviewerBlind.JSON (upper-case extension) copies ReviewerBlind with Q05 FAIL; canonical file unchanged",
         d02_hidden_dissent_vote, "FAIL"),
        ("C02-V02-qid-list-as-na-reason", "n/a reason made of criterion ids only",
         "ReviewerGate Q07 n/a note 'see Q01 Q02 Q03 Q04 Q05 Q06 for the reason' (6+ tokens, names a Q id)",
         d02_qid_list_na, "FAIL"),
        ("C02-E01-recheck-names-no-command", "recheck header with no re-verifying command",
         "entry recheck line -> 'recheck: none'; votes re-bound to the new digest",
         d02_recheck_none, "FAIL"),
        ("C02-E02-two-run-clause-count", "Q14 count wrong in a clause carrying two hex runs",
         "prose clause with `B82A000000C3` (6 bytes) and `0102` (3 bytes); lint skips two-run clauses; re-bound",
         d02_two_run_clause_count, "FAIL"),
        ("C02-E03-coverage-map-other-row", "coverage-map header names a row other than the citing row",
         "entry coverage-map C02 -> C05 while README C02 cites the entry; re-bound",
         d02_coverage_map_other_row, "FAIL"),
        ("C02-R01-held-row-backed-by-candidate", "held row backed by an unadmitted entry of another round",
         "README C06 knowledge cell -> the round-98 candidate (copied into the tree); K counts existence only",
         d02_candidate_backs_held_c06, "FAIL"),
    ],
    "c14": [
        ("C14-R01-suffix-row-outside-count", "coverage row id with a letter suffix, invisible to the count",
         "extra held row 'C14a' inserted after C14, same knowledge file; cov regex C[0-9]+ skips it",
         d14_suffix_row_hidden, "FAIL"),
        ("C14-V01-placeholder-pass-note", "PASS decision with a one-word placeholder note",
         "ReviewerGate Q09 PASS with note 'ok'",
         d14_placeholder_pass_note, "FAIL"),
        ("C14-V02-fail-under-extra-key", "FAIL recorded under an out-of-range decision key",
         "ReviewerBlind decisions gains Q18 FAIL with a note",
         d14_fail_under_extra_key, "FAIL"),
        ("C14-Q01-receipt-span-shift", "receipt span names bytes beside the quote",
         "S506 receipt span start/end +1 (quote text still in the body)",
         d14_receipt_span_shift, "FAIL"),
        ("C14-O01-ownwork-pointer-foreign-round", "own-work pointer names an existing record of another round",
         "S507 source cell corpus/live/runs/round-98/ -> corpus/live/runs/round-96/ (exists); entry unchanged",
         d14_ownwork_foreign_round, "FAIL"),
        ("C14-L01-fetchlog-date-vs-receipt", "fetch-log header date disagrees with the receipt fetched_at",
         "reports/round-98/quote-receipts/fetch-log.md header 2026-11-05 -> 2026-11-04; receipt unchanged",
         d14_fetchlog_date, "FAIL"),
    ],
}


# ---------------------------------------------------------------- run

def manifest_of(root):
    out = {}
    for p in root.rglob("*"):
        if p.is_file() and not p.is_symlink():
            out[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def parse(out):
    m = re.search(r"^C1_VERDICT=(\w+)$", out, re.M)
    k = re.search(r"^C1_K_HELD_BACKED=(\d+/\d+)$", out, re.M)
    return {"verdict": m.group(1) if m else "none",
            "k_held": k.group(1) if k else "none",
            "failing_legs": re.findall(r"^(C1_[A-Z0-9_]+)=fail$", out, re.M)}


def run_counter(tree):
    cmd = [sys.executable, "-B", str(COUNTER), "--tree", str(tree), "--work", str(WORK / "cw")]
    if ARGS.profile:
        cmd += ["--profile", ARGS.profile]
    r = subprocess.run(cmd, cwd=str(WORK), capture_output=True, text=True,
                       env=os.environ.copy())
    return r, cmd


def main():
    base = WORK / PROFILE
    base.mkdir(parents=True, exist_ok=True)
    if PROFILE == "c14":
        honest = base / "honest"
        d = build_c14_honest(honest, ARGS.c14_variant)
        print(f"C14_LANDING_BUILT variant={ARGS.c14_variant} entry_digest={d}")
    else:
        honest = build_c02_honest(base / "honest")
        print("C02_FIXTURE_BUILT source=frozen-v6 _fixture")
    hidx = manifest_of(honest)
    VARIANT = ARGS.c14_variant if PROFILE == "c14" else "fixture"
    spec_dir = HERE / "vectors" / PROFILE / VARIANT
    if spec_dir.exists():
        shutil.rmtree(spec_dir)
    spec_dir.mkdir(parents=True)
    results, control_outcome, accepted, named = [], None, 0, 0
    entries = [("CONTROL-honest", "control", "none: honest tree, no delta", None, "pass")]
    entries += [(n, c, m, f, e) for (n, c, m, f, e) in VECTORS[PROFILE]]
    for name, cls, desc, fn, expected in entries:
        expected = expected.lower()
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
        jwr(vdir / "vector.json", {"name": name, "profile": PROFILE,
                                   "variant": ARGS.c14_variant if PROFILE == "c14" else "fixture",
                                   "class": cls, "mutation": desc, "expected": expected,
                                   "changed": changed, "removed": removed})
        rc, verdict, k, legs, outcome = None, "not-run", "-", [], "built"
        if COUNTER is not None and not ARGS.build_only:
            r, cmd = run_counter(tree)
            rc = r.returncode
            p = parse(r.stdout)
            verdict, k, legs = p["verdict"], p["k_held"], p["failing_legs"]
            wr(vdir / "counter.log", f"# rc={rc}\n# command: {' '.join(cmd[:-2])} --tree <tree>\n"
                                     + r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr.strip() else ""))
            if expected == "pass":
                outcome = "control-ok" if verdict == "pass" else "control-BROKEN"
                control_outcome = outcome
            else:
                named += 1
                if verdict == "pass":
                    outcome = "ACCEPTED"
                    accepted += 1
                elif verdict == "fail":
                    outcome = "refused"
                else:
                    outcome = "NO-VERDICT"
        elif expected == "fail":
            named += 1
        results.append({"name": name, "class": cls, "expected": expected, "rc": rc, "verdict": verdict,
                        "k_held": k, "failing_legs": legs, "outcome": outcome, "changed": changed,
                        "removed": removed})
        shutil.rmtree(tree, ignore_errors=True)
        print(f"{name} | {cls} | rc={rc} | {verdict} | K={k} | {','.join(legs) or '-'} | {expected} | {outcome}")
    jwr(HERE / f"results-{PROFILE}-{VARIANT}.json", results)
    if control_outcome is None and not ARGS.build_only:
        control_outcome = "control-BROKEN"
    print(f"HOLDOUT98_PROFILE={PROFILE} variant={ARGS.c14_variant if PROFILE == 'c14' else 'fixture'} "
          f"counter={COUNTER.name if COUNTER else 'none'} build_only={ARGS.build_only}")
    if ARGS.build_only:
        print(f"HOLDOUT98_BUILD={'ok' if results else 'empty'} vectors={named}")
    else:
        print(f"HOLDOUT98_CONTROL={control_outcome}")
        print(f"HOLDOUT98 accepted={accepted}/{named}")
    sums = []
    for p in sorted(HERE.rglob("*")):
        if p.is_file() and p.name != "MANIFEST.sha256" and "__pycache__" not in p.parts:
            sums.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(HERE)}")
    wr(HERE / "MANIFEST.sha256", "\n".join(sums) + "\n")
    if ARGS.build_only:
        return 0
    ok = control_outcome == "control-ok" and all(x["rc"] in (0, 1) for x in results)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
