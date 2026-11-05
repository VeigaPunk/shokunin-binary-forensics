#!/usr/bin/env python3
"""Round-100 forge-reach harness (calibration, C1 instrument).

One run stages the frozen round-99 fresh holdout builder (build_fresh99.py, sha256 pinned) and
drives it over BOTH profiles against the counter under test, then prints the C1 battery for the
twelve round-99 holdout vectors (six c02 N1-N6, six c14 N1-N6):

  R100_VECTOR <name> accepted|refused legs=<failing C1_ legs>   x12, c02 then c14
  R100_ACCEPTED=<n>/12
  R100_CONTROL_C02=control-ok|control-bad
  R100_CONTROL_C14=control-ok|control-bad
  R100_STUB_SELFTEST=ok|bad
  R100_REASON=<...>        printed whenever the verdict is not-met
  R100_VERDICT=met|not-met

A vector is *accepted* when the counter under test prints C1_VERDICT=pass on that vector's tree.
Fail closed: a vector whose builder row is missing, duplicated, or does not carry a clean refusal
(verdict fail and outcome refused) counts as accepted and is named in R100_REASON. Never as refused.
A builder run that times out, crashes or prints nothing leaves every one of its rows missing, so
those vectors count as accepted.

met iff all of: 0 of 12 accepted; both honest controls control-ok; stub self-test ok.

Stub self-test (per profile, on the same built trees as the main run):
  stub-pass (prints C1_VERDICT=pass for every tree): every vector accepted with a clean row, control-ok;
  stub-fail (prints C1_VERDICT=fail for every tree): every vector refused, control-bad;
  the honest tree and every vector's changed and removed file set, with the sha256 of each changed
  file, must match the main run for both stubs. A mismatch makes the self-test bad.

Exit: 0 iff met; 1 iff not-met; 2 on usage or pin error (builder sha256 mismatch, missing counter,
missing lane, no work root).

Usage:
  PYTHONUTF8=1 python3 -B reports/round-100/forge_reach9.py \
      --counter <counter.py> --work <scratch> [--lane <lane>]

Scratch: --work wins; otherwise $HYAKU_SCRATCH/forge9-work, otherwise $TMPDIR/forge9-work.
Everything is written under <work>/forge9/ and nothing is written to the lane tree.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # never write __pycache__ into frozen dirs

HERE = Path(__file__).resolve().parent
LANE = HERE.parents[1]  # reports/round-100 -> lane root

BUILDER_REL = ".ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py"
BUILDER_SHA256 = "22dddf3d683719c38772f7f65716196f2eabd641e8368791e9575430e79984ec"
STAGE_DEPTH = 4  # builder's own default lane is HERE.parents[5]; --lane is always passed anyway

PROFILES = ("c02", "c14")
VECTORS = {
    "c02": ("C02-N1-one-token-pass-note",
            "C02-N2-pinned-reviewer-vote-omitted",
            "C02-N3-qmap-contradicts-votes",
            "C02-N4-evidence-id-edited",
            "C02-N5-observation-limitations-cut",
            "C02-N6-surface-text-attests-replication"),
    "c14": ("C14-N1-na-inflation",
            "C14-N2-artifact-renamed-to-other-seat",
            "C14-N3-derivation-count-edited",
            "C14-N4-record-appended",
            "C14-N5-s506-body-rebuilt",
            "C14-N6-s507-anchor-relabelled"),
}
N_VECTORS = 12
CONTROL_NAME = "CONTROL-honest"
RUN_TIMEOUT_S = 1800
LEG_RE = re.compile(r"^C1_[A-Z0-9_]+$")

STUB_PASS = "#!/usr/bin/env python3\nprint('C1_VERDICT=pass')\n"
STUB_FAIL = "#!/usr/bin/env python3\nprint('C1_VERDICT=fail')\n"


class ForgeError(Exception):
    """Usage or pin error -> exit 2."""


# ---------------------------------------------------------------- pinning

def sha256(data):
    return hashlib.sha256(data).hexdigest()


def pinned_builder(lane):
    """Working-tree bytes of the frozen builder; any sha256 mismatch fails closed (exit 2)."""
    p = lane / BUILDER_REL
    if not p.is_file():
        raise ForgeError(f"frozen builder missing: {p}")
    data = p.read_bytes()
    got = sha256(data)
    if got != BUILDER_SHA256:
        raise ForgeError(f"builder sha256 {got} != pinned {BUILDER_SHA256}")
    return data


def stage_builder(root, tag, data):
    """Write a byte copy of the builder under root/stage-<tag>/nest.../ and return its path."""
    rel = Path(*(["nest"] * STAGE_DEPTH)) / "build_fresh99.py"
    staged = root / f"stage-{tag}" / rel
    staged.parent.mkdir(parents=True, exist_ok=True)
    staged.write_bytes(data)
    if len(staged.parents) <= 5:
        raise ForgeError("staged builder is too shallow for HERE.parents[5]")
    if sha256(staged.read_bytes()) != BUILDER_SHA256:
        raise ForgeError("staged builder copy drifted from the pinned sha256")
    return staged


# ---------------------------------------------------------------- builder run

def run_builder(staged, counter, profile, run_dir, lane):
    """Run the staged builder once. Returns (stdout, note); a failed run yields empty stdout."""
    shutil.rmtree(run_dir, ignore_errors=True)  # the builder's c14 honest build is not re-runnable
    (run_dir / "tmp").mkdir(parents=True)
    (run_dir / "hyaku").mkdir(parents=True)
    env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1",
               TMPDIR=str(run_dir / "tmp"), HYAKU_SCRATCH=str(run_dir / "hyaku"))
    cmd = [sys.executable, "-B", str(staged), "--counter", str(counter),
           "--profile", profile, "--work", str(run_dir), "--lane", str(lane)]
    try:
        r = subprocess.run(cmd, cwd=str(run_dir), env=env, capture_output=True,
                           text=True, encoding="utf-8", errors="replace",
                           timeout=RUN_TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return "", f"{profile}: builder timeout after {RUN_TIMEOUT_S}s"
    err = r.stderr.strip()[-300:]
    if r.returncode not in (0, 1):
        return r.stdout, f"{profile}: builder rc={r.returncode}: {err!r}"
    if err:
        return r.stdout, f"{profile}: builder stderr: {err!r}"
    return r.stdout, ""


def parse_rows(stdout):
    """Table rows `name | class | rc= | verdict | K= | legs | expected | outcome`, plus the
    HOLDOUT99_CONTROL and `HOLDOUT99 accepted=` summary lines. Never raises: bad rows are simply
    absent, which the caller counts as accepted."""
    rows, dups = {}, set()
    control_line = summary = None
    for ln in stdout.splitlines():
        f = [c.strip() for c in ln.split(" | ")]
        if len(f) == 8 and f[2].startswith("rc=") and f[4].startswith("K="):
            name, _cls, rc, verdict, kval, legs, expected, outcome = f
            if name in rows:
                dups.add(name)
            rows[name] = {"rc": rc, "verdict": verdict, "k": kval,
                          "legs": [] if legs in ("", "-") else legs.split(","),
                          "expected": expected, "outcome": outcome}
        elif ln.startswith("HOLDOUT99_CONTROL="):
            control_line = ln.split("=", 1)[1].strip()
        elif ln.startswith("HOLDOUT99 accepted="):
            summary = ln.split("=", 1)[1].strip()
    return rows, dups, control_line, summary


def classify(name, rows, dups):
    """-> (state, legs, note). state is accepted or refused; note is empty only for a clean row."""
    if name in dups:
        return "accepted", "", f"duplicate builder row {name}"
    row = rows.get(name)
    if row is None:
        return "accepted", "", f"missing builder row {name}"
    # the builder's leg column lists every `C1_*=fail` line; C1_VERDICT is the verdict, not a leg
    leg_list = [leg for leg in row["legs"] if leg != "C1_VERDICT"]
    bad = [leg for leg in leg_list if not LEG_RE.match(leg)]
    legs = ",".join(leg_list)
    if bad:
        return "accepted", legs, f"malformed legs {bad!r} in row {name}"
    if row["expected"] != "fail":
        return "accepted", legs, f"row {name} expected={row['expected']}"
    if row["verdict"] == "fail" and row["outcome"] == "refused":
        return "refused", legs, ""
    if row["verdict"] == "pass" and row["outcome"] == "ACCEPTED":
        return "accepted", legs, ""
    return "accepted", legs, (f"unclean row {name}: verdict={row['verdict']} "
                              f"outcome={row['outcome']}")


# ---------------------------------------------------------------- fingerprints


def fingerprint(run_dir, profile):
    """(honest manifest, per-vector (changed, removed)) for one builder run. Raises on a
    missing or inconsistent tree; the caller records None, which never matches."""
    honest = run_dir / profile / "honest"
    root = honest
    if profile == "c02":
        # the v6 fixture writes its tree under a random fx-<rand>/t; the builder keys on that t/
        cands = sorted(p for p in honest.glob("fx-*/t") if p.is_dir())
        if len(cands) != 1:
            raise ForgeError(f"{profile}: expected one fx-*/t fixture root, found {len(cands)}")
        root = cands[0]
    if not root.is_dir():
        raise ForgeError(f"{profile}: honest tree missing under {root}")
    man = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            man[str(p.relative_to(root))] = sha256(p.read_bytes())
    if not man:
        raise ForgeError(f"{profile}: honest tree is empty")
    vecs = {}
    for name in VECTORS[profile]:
        vdir = run_dir / "vectors" / profile / name
        meta = json.loads((vdir / "vector.json").read_text(encoding="utf-8"))
        changed = tuple(sorted(
            (rel, sha256((vdir / "changed" / rel).read_bytes()))
            for rel in meta["changed"]))
        removed = tuple(sorted(ln
                               for ln in (vdir / "removed.txt").read_text(encoding="utf-8").split("\n")
                               if ln.strip()))
        vecs[name] = (changed, removed)
    return man, vecs


# ---------------------------------------------------------------- one profile

def run_one(root, tag, profile, counter, lane, builder_bytes):
    """Stage, run and parse the builder for one profile and one counter."""
    staged = stage_builder(root, f"{tag}-{profile}", builder_bytes)
    run_dir = root / f"run-{tag}-{profile}"
    out, note = run_builder(staged, counter, profile, run_dir, lane)
    rows, dups, control_line, summary = parse_rows(out)
    notes = [note] if note else []

    vecs = []
    for name in VECTORS[profile]:
        state, legs, vnote = classify(name, rows, dups)
        vecs.append({"name": name, "state": state, "legs": legs, "note": vnote})

    ctl = rows.get(CONTROL_NAME)
    ctl_ok = (ctl is not None and CONTROL_NAME not in dups and ctl["verdict"] == "pass"
              and ctl["outcome"] == "control-ok" and control_line == "control-ok")
    if ctl is None:
        notes.append(f"{profile}: missing control row {CONTROL_NAME}")
    elif not ctl_ok:
        notes.append(f"{profile}: control row verdict={ctl['verdict']} outcome={ctl['outcome']} "
                     f"line={control_line!r}")
    accepted_rows = sum(1 for name in VECTORS[profile]
                        if rows.get(name, {}).get("outcome") == "ACCEPTED")
    want_summary = f"{accepted_rows}/{len(VECTORS[profile])}"
    if summary is None:
        notes.append(f"{profile}: summary line HOLDOUT99 accepted= missing")
    elif summary != want_summary:
        notes.append(f"{profile}: summary {summary!r} != table {want_summary}")
    unknown = sorted(n for n in rows if n not in VECTORS[profile] and n != CONTROL_NAME)
    if unknown:
        notes.append(f"{profile}: unexpected builder rows {unknown}")

    try:
        fp = fingerprint(run_dir, profile)
    except Exception as e:  # noqa: BLE001 - any fingerprint failure fails the stub check
        fp = None
        notes.append(f"{profile}: {tag} tree fingerprint failed: {type(e).__name__}: {e}")

    return {"vecs": vecs, "control": "control-ok" if ctl_ok else "control-bad",
            "fp": fp, "notes": notes}


# ---------------------------------------------------------------- evaluate

def resolve_work(arg):
    if arg is not None:
        return arg.expanduser().resolve()
    if os.environ.get("HYAKU_SCRATCH"):
        return Path(os.environ["HYAKU_SCRATCH"]).expanduser().resolve() / "forge9-work"
    if os.environ.get("TMPDIR"):
        return Path(os.environ["TMPDIR"]).expanduser().resolve() / "forge9-work"
    raise ForgeError("no --work and neither HYAKU_SCRATCH nor TMPDIR is set")


def evaluate(counter, lane, work):
    builder_bytes = pinned_builder(lane)
    root = work / "forge9"
    shutil.rmtree(root, ignore_errors=True)
    stubs = root / "stubs"
    stubs.mkdir(parents=True)
    stub_paths = {"stub-pass": stubs / "stub-pass.py", "stub-fail": stubs / "stub-fail.py"}
    stub_paths["stub-pass"].write_text(STUB_PASS, encoding="utf-8")
    stub_paths["stub-fail"].write_text(STUB_FAIL, encoding="utf-8")

    reasons = []
    main = {}
    for profile in PROFILES:
        main[profile] = run_one(root, "main", profile, counter, lane, builder_bytes)
        reasons.extend(main[profile]["notes"])
        for v in main[profile]["vecs"]:
            if v["note"]:
                reasons.append(v["note"])

    total = sum(len(main[p]["vecs"]) for p in PROFILES)
    accepted = sum(1 for p in PROFILES for v in main[p]["vecs"] if v["state"] == "accepted")
    for p in PROFILES:
        for v in main[p]["vecs"]:
            print(f"R100_VECTOR {v['name']} {v['state']} legs={v['legs']}", flush=True)
    print(f"R100_ACCEPTED={accepted}/{N_VECTORS}", flush=True)
    for p in PROFILES:
        print(f"R100_CONTROL_{p.upper()}={main[p]['control']}", flush=True)

    stub_ok = True
    for profile in PROFILES:
        for tag in ("stub-pass", "stub-fail"):
            s = run_one(root, tag, profile, stub_paths[tag], lane, builder_bytes)
            reasons.extend(f"[{tag}] {n}" for n in s["notes"])
            if tag == "stub-pass":
                clean = all(v["state"] == "accepted" and not v["note"] for v in s["vecs"])
                good = clean and s["control"] == "control-ok"
            else:
                clean = all(v["state"] == "refused" and not v["note"] for v in s["vecs"])
                good = clean and s["control"] == "control-bad"
            same = s["fp"] is not None and main[profile]["fp"] is not None \
                and s["fp"] == main[profile]["fp"]
            if not good:
                stub_ok = False
                reasons.append(f"stub self-test {tag} {profile}: expected all "
                               f"{'accept with control-ok' if tag == 'stub-pass' else 'refuse with control-bad'}"
                               f", got control={s['control']} "
                               f"states={[v['state'] for v in s['vecs']]}")
            if not same:
                stub_ok = False
                reasons.append(f"stub self-test {tag} {profile}: built trees differ from the main run")
    print(f"R100_STUB_SELFTEST={'ok' if stub_ok else 'bad'}", flush=True)

    ctl_ok = all(main[p]["control"] == "control-ok" for p in PROFILES)
    met = total == N_VECTORS and accepted == 0 and ctl_ok and stub_ok
    if accepted:
        named = [v["name"] for p in PROFILES for v in main[p]["vecs"] if v["state"] == "accepted"]
        reasons.insert(0, f"counter accepts {accepted} of {N_VECTORS} vectors: {', '.join(named)}")
    for p in PROFILES:
        if main[p]["control"] != "control-ok":
            reasons.insert(0, f"{p} honest control {main[p]['control']}")
    if not stub_ok:
        reasons.insert(0, "stub self-test bad")
    if not met:
        for r in reasons:
            print(f"R100_REASON={r}", flush=True)
    print(f"R100_VERDICT={'met' if met else 'not-met'}", flush=True)
    return 0 if met else 1


def main(argv):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--counter", type=Path, required=True)
    p.add_argument("--work", type=Path, default=None)
    p.add_argument("--lane", type=Path, default=LANE)
    args = p.parse_args(argv)
    try:
        counter = args.counter.expanduser().resolve()
        if not counter.is_file():
            print(f"forge_reach9 error: counter not found: {counter}", file=sys.stderr)
            return 2
        lane = args.lane.expanduser().resolve()
        if not (lane / "corpus").is_dir():
            print(f"forge_reach9 error: not a lane root: {lane}", file=sys.stderr)
            return 2
        work = resolve_work(args.work)
        work.mkdir(parents=True, exist_ok=True)
        return evaluate(counter, lane, work)
    except ForgeError as e:
        print(f"forge_reach9 error: {e}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 - any harness failure -> exit 2
        print(f"forge_reach9 error: {type(e).__name__}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
