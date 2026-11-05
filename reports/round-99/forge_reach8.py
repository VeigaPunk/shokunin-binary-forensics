#!/usr/bin/env python3
"""Round-99 forge-reach harness (calibration, C2 instrument).

One run drives the round-98 fresh holdout builder (build_fresh98.py, with the
L1 parity patch applied to a staged copy) over BOTH profiles and prints the
C2 battery for the twelve round-98 holdout vectors (six c02, six c14):

  c02: V01 hidden-dissent uppercase vote, V02 criterion-id-list n/a reason,
       E01 recheck with no command, E02 two-run clause count,
       E03 coverage-map header naming another row, R01 held row backed by an
       unadmitted candidate entry of another round
  c14: R01 suffix row outside the count, V01 placeholder PASS note,
       V02 FAIL under an out-of-range key, Q01 receipt span shift,
       O01 own-work pointer of another round, L01 fetch-log date vs receipt

A vector is *accepted* when the counter under test prints C1_VERDICT=pass on
the tree carrying that vector (frozen C2 predicate). Frozen v7 accepts 9/12
(development-set result); the v8 target is 0/12.

Builder handling (the committed builder is never edited or executed in place):
  * the working-tree builder and parity patch are checked against the blobs
    committed at FREEZE_REV and against pinned sha256 constants; any mismatch
    fails closed (exit 2).
  * each builder invocation runs a byte copy staged four directories below a
    per-run scratch root, so the builder's own `HERE.parents[5]` default stays
    evaluable; `--lane` is passed explicitly regardless.
  * the parity patch (one normal-diff `NaM,K` add hunk) is applied to the copy
    by a strict applier: anchor line verified, already-applied input refused,
    patched source must compile. The patch is not applied with `patch(1)`.
  * the c02 fixture root is created by the frozen v6 `_fixture` under a
    random `fx-<rand>/t/` directory; manifest keys strip that prefix (and fail
    closed if it is absent), so per-run randomness never reads as a difference.

Stub self-test: an always-pass stub counter must score 12/12 and an always-fail
stub 0/12 on the same built trees. "Same built trees" is enforced per profile:
the persisted honest tree (file sha256 manifest) and every vector's changed and
removed file set with the sha256 of each changed file must match across the
main run and both stub runs. A mismatch makes the stub self-test fail.

Output (one run, in this order):
  C2_VECTOR <profile>-<id> accepted|refused legs=<failing C1_ legs, or empty>
  C2_ACCEPTED=<n>/12
  C2_CONTROL_C02=<outcome>
  C2_CONTROL_C14=<outcome>
  C2_STUB_SELFTEST=ok|fail
  C2_REASON=<...>            printed whenever the verdict is not-met
  C2_VERDICT=met|not-met

met iff exactly 12 vectors were parsed, 0 accepted, both controls control-ok,
every vector produced a verdict, and the stub self-test is ok.
Exit 0 once the verdict is printed; exit 2 on usage or build error. Missing,
empty or inconsistent builder output is a build error (exit 2), never 0 accepted.

Usage:
  PYTHONUTF8=1 python3 -B reports/round-99/forge_reach8.py \
      --counter <counter.py> --work <scratch> [--lane <lane>]

Scratch: --work wins; otherwise $HYAKU_SCRATCH/forge8-work, otherwise
$TMPDIR/forge8-work. Nothing is written outside the resolved work root.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # never write __pycache__ into frozen dirs

HERE = Path(__file__).resolve().parent
LANE = HERE.parents[1]  # reports/round-99 -> lane root

FREEZE_REV = "7e6edd4db649f99c425daa46a91edbbd18a6e27c"
BUILDER_REL = ".ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py"
PATCH_REL = ".ufo/waves/round-98/w1/L1-holdout-v7/parity-patch.diff"
BUILDER_SHA256 = "82347899996e0394faec4c90efca0fc99ed12b4dbf5f4426c0e3b4ffe30b38cd"
PATCH_SHA256 = "1dfcb155d149dd2e8823a355be5b6f4dff8812a037ba460bf7b2788fd242572a"
PATCH_ANCHOR = "    assert (root / fx.ENTRY).is_file()"  # builder line 189
STAGE_DEPTH = 4
FIXTURE_PREFIX = re.compile(r"^fx-[A-Za-z0-9_]+/t/(.*)$")

PROFILES = ("c02", "c14")
N_VECTORS = 12
RUN_TIMEOUT_S = 900
OUTCOMES = {"ACCEPTED", "refused", "control-ok", "control-BROKEN", "NO-VERDICT", "built"}

STUB_PASS = "#!/usr/bin/env python3\nprint('C1_VERDICT=pass')\n"
STUB_FAIL = ("#!/usr/bin/env python3\nprint('C1_VERDICT=fail')\n"
             "print('C1_ADMITTED=fail')\n")

LEG_RE = re.compile(r"^C1_[A-Z0-9_]+$")
VEC_RE = re.compile(r"^C(\d+)-([A-Z]\d{2})-")


class ForgeError(Exception):
    """Usage or build error -> exit 2."""


# ---------------------------------------------------------------- pinning

def pinned_bytes(lane, rel, want_sha, what):
    """Working-tree bytes of a frozen file, checked against the blob committed
    at FREEZE_REV and against the pinned sha256."""
    p = lane / rel
    if not p.is_file():
        raise ForgeError(f"frozen {what} missing: {p}")
    data = p.read_bytes()
    r = subprocess.run(["git", "-C", str(lane), "cat-file", "blob", f"{FREEZE_REV}:{rel}"],
                       capture_output=True)
    if r.returncode:
        raise ForgeError(f"git cat-file {FREEZE_REV}:{rel} failed: {r.stderr[:200]!r}")
    committed = hashlib.sha256(r.stdout).hexdigest()
    if committed != want_sha:
        raise ForgeError(f"committed {what} sha256 {committed} != pinned {want_sha}")
    if hashlib.sha256(data).hexdigest() != committed:
        raise ForgeError(f"working-tree {what} differs from the committed blob")
    return data


# ---------------------------------------------------------------- patch

def apply_add_patch(src_text, patch_text):
    """Apply one normal-diff add hunk (`NaM` or `NaM,K` followed by `> ` lines).

    Strict: a single add command, hunk length matches the header, anchor line
    verified, already-patched input refused.
    """
    plines = patch_text.split("\n")
    m = re.match(r"^(\d+)a(\d+)(?:,(\d+))?$", plines[0])
    if not m:
        raise ForgeError(f"parity patch: unsupported first line {plines[0]!r}")
    anchor_no, first_new = int(m.group(1)), int(m.group(2))
    last_new = int(m.group(3)) if m.group(3) else first_new
    added = []
    for ln in plines[1:]:
        if ln == "":
            break
        if not ln.startswith("> "):
            raise ForgeError(f"parity patch: unsupported line {ln!r}")
        added.append(ln[2:])
    if len(added) != last_new - first_new + 1:
        raise ForgeError(f"parity patch: {len(added)} lines for header {plines[0]}")
    if first_new != anchor_no + 1:
        raise ForgeError(f"parity patch: add target {first_new} is not anchor+1")
    slines = src_text.split("\n")
    if len(slines) < anchor_no or slines[anchor_no - 1] != PATCH_ANCHOR:
        raise ForgeError(f"parity patch: anchor line {anchor_no} drifted")
    if slines[anchor_no:anchor_no + len(added)] == added:
        raise ForgeError("parity patch: already applied to the builder bytes")
    return "\n".join(slines[:anchor_no] + added + slines[anchor_no:])


def stage_builder(root, tag, builder_bytes, patch_text):
    """Write the patched builder copy under root/stage-<tag>/nest.../ and return it."""
    rel = Path(*(["nest"] * STAGE_DEPTH)) / "build_fresh98.py"
    staged = root / f"stage-{tag}" / rel
    staged.parent.mkdir(parents=True, exist_ok=True)
    patched = apply_add_patch(builder_bytes.decode("utf-8"), patch_text)
    try:
        compile(patched, str(staged), "exec")
    except SyntaxError as e:
        raise ForgeError(f"patched builder does not compile: {e}") from e
    staged.write_text(patched, encoding="utf-8", newline="")
    if len(staged.parents) <= 5:
        raise ForgeError("staged builder is too shallow for HERE.parents[5]")
    return staged


# ---------------------------------------------------------------- builder run

def run_builder(staged, counter, profile, run_dir, lane):
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "tmp").mkdir(exist_ok=True)
    (run_dir / "hyaku").mkdir(exist_ok=True)
    env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1",
               TMPDIR=str(run_dir / "tmp"), HYAKU_SCRATCH=str(run_dir / "hyaku"))
    cmd = [sys.executable, "-B", str(staged), "--counter", str(counter),
           "--profile", profile, "--work", str(run_dir), "--lane", str(lane)]
    try:
        r = subprocess.run(cmd, cwd=str(run_dir), env=env, capture_output=True,
                           text=True, encoding="utf-8", errors="replace",
                           timeout=RUN_TIMEOUT_S)
    except subprocess.TimeoutExpired as e:
        raise ForgeError(f"{profile}: builder timeout after {RUN_TIMEOUT_S}s") from e
    if r.returncode not in (0, 1):
        raise ForgeError(f"{profile}: builder rc={r.returncode}: {r.stderr.strip()[-300:]!r}")
    return r.stdout


def parse_run(stdout, profile):
    """Parse one builder run. Missing, empty or inconsistent output raises."""
    if not stdout.strip():
        raise ForgeError(f"{profile}: missing/empty builder output")
    rows, control, control_line, prof_line, acc_line = [], None, None, None, None
    for ln in stdout.splitlines():
        f = [c.strip() for c in ln.split(" | ")]
        if (len(f) == 8 and f[2].startswith("rc=") and f[4].startswith("K=")
                and f[3] in {"pass", "fail", "not-run"} and f[6] in {"pass", "fail"}
                and f[7] in OUTCOMES):
            name, cls, rc, verdict, kval, legs, expected, outcome = f
            legs = [] if legs == "-" else legs.split(",")
            for leg in legs:
                if not LEG_RE.match(leg):
                    raise ForgeError(f"{profile}: malformed leg {leg!r}")
            row = {"name": name, "class": cls, "rc": rc, "verdict": verdict,
                   "k": kval, "legs": legs, "expected": expected, "outcome": outcome}
            if name == "CONTROL-honest":
                if control is not None or expected != "pass":
                    raise ForgeError(f"{profile}: malformed control row")
                control = row
            else:
                vm = VEC_RE.match(name)
                if not vm or f"c{vm.group(1)}" != profile:
                    raise ForgeError(f"{profile}: unexpected vector row {name!r}")
                row["vid"] = vm.group(2)
                rows.append(row)
        elif ln.startswith("HOLDOUT98_PROFILE="):
            prof_line = ln
        elif ln.startswith("HOLDOUT98_CONTROL="):
            control_line = ln.split("=", 1)[1].strip()
        elif ln.startswith("HOLDOUT98 accepted="):
            acc_line = ln.split("=", 1)[1].strip()
    if control is None or control_line is None:
        raise ForgeError(f"{profile}: control row or HOLDOUT98_CONTROL line missing")
    if control_line != control["outcome"]:
        raise ForgeError(f"{profile}: control line {control_line} != row {control['outcome']}")
    if prof_line is None or not prof_line.startswith(f"HOLDOUT98_PROFILE={profile} "):
        raise ForgeError(f"{profile}: HOLDOUT98_PROFILE line missing or mismatched")
    if not rows:
        raise ForgeError(f"{profile}: zero vector rows (fail closed)")
    for row in rows:
        want = {"pass": "ACCEPTED", "fail": "refused"}.get(row["verdict"], "NO-VERDICT")
        if row["outcome"] != want:
            raise ForgeError(f"{profile}: {row['name']} outcome {row['outcome']} "
                             f"inconsistent with verdict {row['verdict']}")
    accepted = sum(1 for r in rows if r["outcome"] == "ACCEPTED")
    named = sum(1 for r in rows if r["expected"] == "fail")
    if acc_line != f"{accepted}/{named}":
        raise ForgeError(f"{profile}: builder summary {acc_line!r} != table {accepted}/{named}")
    return {"rows": rows, "control": control, "accepted": accepted}


# ---------------------------------------------------------------- fingerprints

def norm(rel, profile):
    """Tree-relative key. c02 trees sit under the v6 fixture's random `fx-<rand>/t/`
    root; strip it, and fail closed if a c02 path does not carry it."""
    if profile != "c02":
        return rel
    m = FIXTURE_PREFIX.match(rel)
    if not m:
        raise ForgeError(f"c02 path without the fixture root prefix: {rel!r}")
    return m.group(1)


def honest_manifest(run_dir, profile):
    """normalised rel path -> sha256 for every file of the persisted honest tree."""
    root = run_dir / profile / "honest"
    if not root.is_dir():
        raise ForgeError(f"{profile}: honest tree missing under {root}")
    out = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            rel = norm(str(p.relative_to(root)), profile)
            out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    if not out:
        raise ForgeError(f"{profile}: honest tree is empty")
    return out


def vector_fingerprint(staged, profile):
    """name -> (sorted changed (rel, sha256) pairs, sorted removed rels) for every
    vector the builder built. The builder deletes its vector trees, so this reads
    the copies it keeps under <staged dir>/vectors/<profile>/<variant>/<name>/."""
    base = staged.parent / "vectors" / profile
    variants = sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []
    if len(variants) != 1:
        raise ForgeError(f"{profile}: expected one vectors/<variant> dir, found {len(variants)}")
    out = {}
    for vdir in sorted(p for p in variants[0].iterdir() if p.is_dir()):
        meta = json.loads((vdir / "vector.json").read_text(encoding="utf-8"))
        changed = tuple(sorted(
            (rel, hashlib.sha256((vdir / "changed" / rel).read_bytes()).hexdigest())
            for rel in meta["changed"]))
        removed = tuple(sorted(ln for ln in (vdir / "removed.txt").read_text(encoding="utf-8").split("\n")
                               if ln.strip()))
        out[vdir.name] = (changed, removed)
    if not out:
        raise ForgeError(f"{profile}: no vector directories kept")
    return out


# ---------------------------------------------------------------- evaluate

def evaluate(counter, lane, work):
    builder_bytes = pinned_bytes(lane, BUILDER_REL, BUILDER_SHA256, "builder")
    patch_text = pinned_bytes(lane, PATCH_REL, PATCH_SHA256, "parity patch").decode("utf-8")
    root = work / "forge8"
    root.mkdir(parents=True, exist_ok=True)
    stubs = {"stub-pass": root / "stub-pass.py", "stub-fail": root / "stub-fail.py"}
    stubs["stub-pass"].write_text(STUB_PASS, encoding="utf-8")
    stubs["stub-fail"].write_text(STUB_FAIL, encoding="utf-8")

    main, fingerprints, reasons = {}, {}, []
    for profile in PROFILES:
        staged = stage_builder(root, f"main-{profile}", builder_bytes, patch_text)
        run_dir = root / f"run-main-{profile}"
        out = run_builder(staged, counter, profile, run_dir, lane)
        main[profile] = parse_run(out, profile)
        fingerprints[("main", profile)] = (honest_manifest(run_dir, profile),
                                           vector_fingerprint(staged, profile))
        for row in main[profile]["rows"]:
            state = "accepted" if row["outcome"] == "ACCEPTED" else "refused"
            print(f"C2_VECTOR {profile}-{row['vid']} {state} legs={','.join(row['legs'])}",
                  flush=True)
        if any(r["outcome"] == "NO-VERDICT" for r in main[profile]["rows"]):
            reasons.append(f"{profile}: counter printed no C1_VERDICT on some vector")

    stub_ok = True
    for profile in PROFILES:
        for tag in ("stub-pass", "stub-fail"):
            staged = stage_builder(root, f"{tag}-{profile}", builder_bytes, patch_text)
            run_dir = root / f"run-{tag}-{profile}"
            out = run_builder(staged, stubs[tag], profile, run_dir, lane)
            res = parse_run(out, profile)
            fingerprints[(tag, profile)] = (honest_manifest(run_dir, profile),
                                            vector_fingerprint(staged, profile))
            want = len(res["rows"]) if tag == "stub-pass" else 0
            if res["accepted"] != want:
                stub_ok = False
            if fingerprints[(tag, profile)] != fingerprints[("main", profile)]:
                stub_ok = False
                reasons.append(f"{profile}: built trees differ between main and {tag}")
    stub_total = sum(len(main[p]["rows"]) for p in PROFILES)
    if stub_total != N_VECTORS:
        stub_ok = False

    total = sum(len(main[p]["rows"]) for p in PROFILES)
    accepted = sum(main[p]["accepted"] for p in PROFILES)
    print(f"C2_ACCEPTED={accepted}/{N_VECTORS}", flush=True)
    for profile in PROFILES:
        print(f"C2_CONTROL_{profile.upper()}={main[profile]['control']['outcome']}", flush=True)
    print(f"C2_STUB_SELFTEST={'ok' if stub_ok else 'fail'}", flush=True)

    met = (total == N_VECTORS and accepted == 0 and stub_ok and not reasons
           and all(main[p]["control"]["outcome"] == "control-ok" for p in PROFILES))
    if total != N_VECTORS:
        reasons.append(f"expected {N_VECTORS} vectors, parsed {total}")
    if accepted != 0:
        reasons.append(f"counter accepts {accepted} of {total} vectors")
    for p in PROFILES:
        if main[p]["control"]["outcome"] != "control-ok":
            reasons.append(f"{p} control {main[p]['control']['outcome']}")
    if not stub_ok:
        reasons.append("stub self-test failed (stub-pass 12/12, stub-fail 0/12 on the same trees)")
    if not met:
        print(f"C2_REASON={'; '.join(reasons) or 'unspecified'}", flush=True)
    print(f"C2_VERDICT={'met' if met else 'not-met'}", flush=True)
    return 0


def main(argv):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--counter", type=Path, required=True)
    p.add_argument("--work", type=Path, default=None)
    p.add_argument("--lane", type=Path, default=LANE)
    args = p.parse_args(argv)
    try:
        counter = args.counter.resolve()
        if not counter.is_file():
            print(f"forge_reach8 error: counter not found: {counter}", file=sys.stderr)
            return 2
        lane = args.lane.resolve()
        if not (lane / "corpus").is_dir():
            print(f"forge_reach8 error: not a lane root: {lane}", file=sys.stderr)
            return 2
        if args.work is not None:
            work = args.work.expanduser().resolve()
        elif os.environ.get("HYAKU_SCRATCH"):
            work = Path(os.environ["HYAKU_SCRATCH"]).expanduser().resolve() / "forge8-work"
        elif os.environ.get("TMPDIR"):
            work = Path(os.environ["TMPDIR"]).expanduser().resolve() / "forge8-work"
        else:
            print("forge_reach8 error: no --work and neither HYAKU_SCRATCH nor TMPDIR",
                  file=sys.stderr)
            return 2
        work.mkdir(parents=True, exist_ok=True)
        return evaluate(counter, lane, work)
    except ForgeError as e:
        print(f"forge_reach8 error: {e}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 - any harness failure -> exit 2
        print(f"forge_reach8 error: {type(e).__name__}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
