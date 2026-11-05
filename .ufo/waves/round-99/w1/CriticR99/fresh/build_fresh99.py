#!/usr/bin/env python3
"""CriticR99 fresh forgery holdout (round 99; C1 c14 and C2 c02 calibration).

Twelve new named forgeries, six per profile. None is one of the r96 FG01-FG20, r97 FR01-FR12 or
r98 holdout classes (c02 V01/V02/E01/E02/E03/R01; c14 R01/V01/V02/Q01/O01/L01).
  c02  fixture tree built by the frozen v6 maker (reports/round-97/c1_k_admit_counter6.py, read-only).
  c14  the lane commit given by --rev (default 9ddd38ac, Amendment B) with the landing edits:
       README C14 knowledge cell and status held, entry admission-status admitted, S505 queued with
       used-by em dash. Votes, registry and wave artifacts are SYNTHETIC fixture bytes written here.
Each profile carries one honest control (expected pass). Verdicts are data; a failing control is
reported, never hidden. Vector specs and trees live under --work; nothing is written to the lane tree.

Usage:
  python3 -B <this file> --counter <counter.py> --profile c02 --work <scratch> [--lane <root>] [--rev <commit>]
  python3 -B <this file> --counter <counter.py> --profile c14 --work <scratch> [--lane <root>] [--rev <commit>]
  add --build-only to build every tree and write vector specs without running any counter.
Prints one table row per vector, then HOLDOUT99_CONTROL=... and `HOLDOUT99 accepted=<n>/<m>`.
Exit 0 iff the honest control passed and every verdict was 0 or 1 (build-only: exit 0 iff built).
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
S506_SHA = "ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50"
S506_QUOTE = "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra."


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


def write_c14_votes(root, dval):
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
    # The v6 freeze (2875b9c) predates the saved round-96 record that the cited entry names; copy the
    # committed record bytes from the lane rev (never invented), as the v7 c02 fixture maker does.
    ar = subprocess.run(["git", "-C", str(LANE), "archive", "--format=tar", ARGS.rev,
                         "corpus/live/runs/round-96"], capture_output=True)
    if ar.returncode:
        raise SystemExit(f"git archive corpus/live/runs/round-96 failed: {ar.stderr[:200]!r}")
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


# ---------------------------------------------------------------- c02 forgeries (v6 fixture world)

def c02_pass_note_one_token(root):
    # N1: a PASS decision carried by a one-token note; the c02 profile does not read PASS notes
    p = root / fx.VOTES_DIR / "ReviewerGate.json"
    v = jrd(p)
    assert v["decisions"]["Q01"] == "PASS", v["decisions"]["Q01"]
    v["notes"]["Q01"] = "ok"
    jwr(p, v)


def c02_vote_omitted(root):
    # N2: a pinned reviewer's vote file deleted; two votes remain, meeting the two-vote floor
    p = root / fx.VOTES_DIR / "ReviewerBlind.json"
    assert p.is_file()
    p.unlink()


def c02_qmap_contradicts_votes(root):
    # N3: the entry's own Q-map claims PASS on Q07, which every seat marked n/a; votes re-bound
    p = root / fx.ENTRY
    t, n = re.subn(r"(?m)^\| Q07 \| n/a \|", "| Q07 | PASS |", rd(p), count=1)
    assert n == 1, n
    wr(p, t)
    rebind02(root)


def c02_evidence_id_edited(root):
    # N4: the saved record's Evidence ID in a derivation row replaced by another 64-hex identifier
    p = root / fx.ENTRY
    lines = rd(p).split("\n")
    hits = [i for i, ln in enumerate(lines) if "grep -m1 evidence_id" in ln]
    assert len(hits) == 1, len(hits)
    lines[hits[0]], n = re.subn(r"ev_[0-9a-f]{64}", "ev_" + "ab" * 32, lines[hits[0]])
    assert n == 1, n
    wr(p, "\n".join(lines))
    rebind02(root)


def c02_observation_limitations_cut(root):
    # N5: the observation/inference/unknown and limitations sections cut (admission procedure step 3)
    p = root / fx.ENTRY
    t = rd(p)
    a = t.find("## Observation, inference, unknown")
    b = t.find("## §Q-map")
    assert 0 < a < b, (a, b)
    wr(p, t[:a] + t[b:])
    rebind02(root)


def c02_surface_text_attests(root):
    # N6: the README C02 surface cell asserts a replication that no vote records; only the
    # knowledge cell is read by the counter
    sub_row(root / "corpus/README.md", "C02", 5,
            lambda c: [c[0], c[1] + " (replicated by two seats, both PASS on Q01 to Q11)", c[2], c[3], c[4]])


# ---------------------------------------------------------------- c14 forgeries (landing-candidate tree)

def c14_na_inflation(root):
    # N1: one reviewer marks ten PASS decisions n/a, each with a reason naming its own Q id; Q09 stays PASS
    p = root / VOTES14 / "ReviewerGate.json"
    v = jrd(p)
    for q in ("Q01", "Q02", "Q03", "Q04", "Q05", "Q06", "Q10", "Q11", "Q14", "Q16"):
        assert v["decisions"][q] == "PASS", (q, v["decisions"][q])
        v["decisions"][q] = "n/a"
        v["notes"][q] = f"{q} n/a: this seat judges the criterion outside its vote scope for this entry"
    jwr(p, v)


def c14_artifact_renamed_to_other_seat(root):
    # N2: CriticR98's audit copied to ReviewerBlind's own artifact path with the seat name substituted;
    # the copy names its own seat and the candidate digest, so the artifact rules are met
    src = root / WAVE14 / "w1/CriticR98/critic-audit.md"
    b = rd(src).replace("CriticR98", "ReviewerBlind").encode("utf-8")
    dst_rel = f"{WAVE14}/w1/ReviewerBlind/blind-evidence.md"
    (root / dst_rel).write_bytes(b)
    p = root / VOTES14 / "ReviewerBlind.json"
    v = jrd(p)
    v["artifact_sha256"] = hashlib.sha256(b).hexdigest()
    jwr(p, v)


def c14_derivation_count_edited(root):
    # N3: the client registration count row prints 15 where the record prints 14; no digest row touched
    p = root / ENTRY14
    t, n = re.subn(r"(?m)^(\| client registration count \| .* \| `)14(` \|)$", r"\g<1>15\2", rd(p))
    assert n == 1, n
    wr(p, t)
    resign14(root)


def c14_record_appended(root):
    # N4: the saved doctor record gains an appended rerun line; its digest prefix is re-derived
    rp = root / "corpus/live/runs/round-98/rea-doctor-r98.txt"
    new = rp.read_bytes() + b"rerun 2026-11-05: healthy: true\n"
    rp.write_bytes(new)
    prefix = hashlib.sha256(new).hexdigest()[:8]
    p = root / ENTRY14
    lines = rd(p).split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.startswith("| record file digests |")]
    assert len(hits) == 1, len(hits)
    lines[hits[0]], n = re.subn(r"`fb9a4824…`", f"`{prefix}…`", lines[hits[0]])
    assert n == 1, n
    wr(p, "\n".join(lines))
    resign14(root)


def c14_s506_body_rebuilt(root):
    # N5: the pinned S506 body replaced by a self-consistent body carrying the same quote; receipt,
    # fetch log and the entry's digest and length rows re-derived; votes re-bound
    body = ("REA connection and task recovery reference, re-fetched at the pinned revision.\n"
            "Doctor reports registration; this paragraph is part of the reference.\n"
            f"{S506_QUOTE}\n"
            "Further paragraphs of the reference follow in the original file.\n").encode("utf-8")
    (root / RECEIPTS14 / "raw/S506.body").write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()
    start = body.decode("utf-8").index(S506_QUOTE)
    rp = root / RECEIPTS14 / "S506.receipt.json"
    r = jrd(rp)
    r["fetch_sha256"] = sha
    r["length"] = len(body)
    r["span"] = {"start": start, "end": start + len(S506_QUOTE)}
    jwr(rp, r)
    fl = root / RECEIPTS14 / "fetch-log.md"
    wr(fl, rd(fl).replace(S506_SHA, sha))
    p = root / ENTRY14
    t = rd(p).replace(S506_SHA, sha)
    t, n = re.subn(r"(\| S506 body length \| .* \| `)16650(` \|)", lambda m: m.group(1) + str(len(body)) + m.group(2), t)
    assert n == 1, n
    wr(p, t)
    resign14(root)


def c14_s507_anchor_relabelled(root):
    # N6: the S507 anchor re-pointed to a true record line (the CLI version) with correct byte offsets;
    # the row's claim about healthy and failing checks is no longer anchored
    rel = "corpus/live/runs/round-98/rea-doctor-r98.txt"
    raw = (root / rel).read_bytes()
    lines = raw.split(b"\n")
    idx = next(i for i, l in enumerate(lines) if l.startswith(b"  cli_package_version:"))
    start = sum(len(l) + 1 for l in lines[:idx]) + 1
    seg = lines[idx]
    end = start + len(seg) - 1
    sub_row(root / "corpus/SOURCES.md", "S507", 11,
            lambda c: c[:5] + [f"`{rel}` line {idx + 1} (1-based bytes {start}-{end}): `{seg.decode('utf-8')}`; "
                               "record digests printed in the citing entry's derivation table"] + c[6:])


VECTORS = {
    "c02": [
        ("C02-N1-one-token-pass-note", "PASS decision carried by a one-token note",
         "ReviewerGate Q01 PASS note replaced by 'ok'; the c02 profile does not read PASS notes",
         c02_pass_note_one_token, "FAIL"),
        ("C02-N2-pinned-reviewer-vote-omitted", "pinned reviewer vote file deleted, two votes remain",
         "ReviewerBlind.json removed; registry still pins ReviewerBlind; the floor is two votes",
         c02_vote_omitted, "FAIL"),
        ("C02-N3-qmap-contradicts-votes", "entry Q-map claims PASS where every vote is n/a",
         "entry row Q07 n/a -> PASS; votes re-bound to the new digest; no vote changed",
         c02_qmap_contradicts_votes, "FAIL"),
        ("C02-N4-evidence-id-edited", "identifier in a derivation row replaced",
         "Evidence ID in the grep -m1 evidence_id row replaced by another 64-hex id; votes re-bound",
         c02_evidence_id_edited, "FAIL"),
        ("C02-N5-observation-limitations-cut", "observation/inference/unknown and limitations sections removed",
         "the two sections cut from the entry (admission procedure step 3); votes re-bound",
         c02_observation_limitations_cut, "FAIL"),
        ("C02-N6-surface-text-attests-replication", "README surface text asserts a replication no vote records",
         "README C02 surface cell gains '(replicated by two seats, both PASS on Q01 to Q11)'",
         c02_surface_text_attests, "FAIL"),
    ],
    "c14": [
        ("C14-N1-na-inflation", "one seat marks ten PASS decisions n/a with Q-id reasons",
         "ReviewerGate Q01-Q06, Q10, Q11, Q14, Q16 -> n/a, each reason names its Q id; Q09 stays PASS",
         c14_na_inflation, "FAIL"),
        ("C14-N2-artifact-renamed-to-other-seat", "another seat's audit renamed into this seat's artifact",
         "CriticR98 artifact copied to ReviewerBlind's own path with the seat name substituted; artifact sha re-signed",
         c14_artifact_renamed_to_other_seat, "FAIL"),
        ("C14-N3-derivation-count-edited", "derivation count row prints 15 where the record prints 14",
         "client registration count output cell 14 -> 15; no digest row touched; votes re-bound",
         c14_derivation_count_edited, "FAIL"),
        ("C14-N4-record-appended", "saved doctor record gains an appended rerun line",
         "rea-doctor-r98.txt appended with 'rerun ... healthy: true'; prefix row re-derived; votes re-bound",
         c14_record_appended, "FAIL"),
        ("C14-N5-s506-body-rebuilt", "pinned S506 body replaced by a self-consistent body",
         "S506.body, receipt, fetch-log line and entry digest/length rows re-derived; votes re-bound",
         c14_s506_body_rebuilt, "FAIL"),
        ("C14-N6-s507-anchor-relabelled", "S507 anchor re-pointed to a true line that does not carry the claim",
         "S507 anchor -> the cli_package_version line with correct byte offsets",
         c14_s507_anchor_relabelled, "FAIL"),
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
    cmd = [sys.executable, "-B", str(COUNTER), "--profile", PROFILE, "--tree", str(tree),
           "--work", str(WORK / "cw")]
    r = subprocess.run(cmd, cwd=str(WORK), capture_output=True, text=True, env=os.environ.copy())
    return r, cmd


def main():
    base = WORK / PROFILE
    base.mkdir(parents=True, exist_ok=True)
    if PROFILE == "c14":
        honest = base / "honest"
        d = build_c14_honest(honest)
        print(f"C14_LANDING_BUILT rev={ARGS.rev[:12]} entry_digest={d}")
    else:
        honest = build_c02_honest(base / "honest")
        print("C02_FIXTURE_BUILT source=frozen-v6 _fixture")
    hidx = manifest_of(honest)
    spec_dir = WORK / "vectors" / PROFILE
    if spec_dir.exists():
        shutil.rmtree(spec_dir)
    spec_dir.mkdir(parents=True)
    results, control_outcome, accepted, named = [], None, 0, 0
    entries = [("CONTROL-honest", "control", "none: honest tree, no delta", None, "pass")]
    entries += list(VECTORS[PROFILE])
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
        jwr(vdir / "vector.json", {"name": name, "profile": PROFILE, "class": cls, "mutation": desc,
                                   "expected": expected, "changed": changed, "removed": removed})
        rc, verdict, k, legs, outcome = None, "not-run", "-", [], "built"
        if COUNTER is not None and not ARGS.build_only:
            r, cmd = run_counter(tree)
            rc = r.returncode
            p = parse(r.stdout)
            verdict, k, legs = p["verdict"], p["k_held"], p["failing_legs"]
            wr(vdir / "counter.log", f"# rc={rc}\n# command: {' '.join(cmd[:-4])} --tree <tree>\n"
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
    jwr(WORK / f"results-{PROFILE}.json", results)
    if control_outcome is None and not ARGS.build_only:
        control_outcome = "control-BROKEN"
    print(f"HOLDOUT99_PROFILE={PROFILE} counter={COUNTER.name if COUNTER else 'none'} "
          f"build_only={ARGS.build_only}")
    if ARGS.build_only:
        print(f"HOLDOUT99_BUILD={'ok' if results else 'empty'} vectors={named}")
    else:
        print(f"HOLDOUT99_CONTROL={control_outcome}")
        print(f"HOLDOUT99 accepted={accepted}/{named}")
    sums = []
    for p in sorted((WORK / "vectors").rglob("*")):
        if p.is_file():
            sums.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(WORK)}")
    wr(WORK / f"MANIFEST-{PROFILE}.sha256", "\n".join(sums) + "\n")
    if ARGS.build_only:
        return 0
    ok = control_outcome == "control-ok" and all(x["rc"] in (0, 1) for x in results)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
