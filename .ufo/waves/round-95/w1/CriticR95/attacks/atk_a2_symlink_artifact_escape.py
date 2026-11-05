#!/usr/bin/env python3
"""Attack A2 (shape b): vote artifact placed inside the seat's own dir as a SYMLINK to a
file outside the wave dir. v4 materialize copies with symlinks=True (both --tree and the
tar layer behind --rev), so the symlink survives into the evaluated tree and only the
resolve()-based containment guard stands between it and acceptance.

Runs the frozen counter end-to-end with --tree, a direct check_votes probe, and a
tar_extract symlink-preservation probe standing in for the --rev materializer (a seat may
not run git write commands to plant a committed symlink in the lane, so the --rev path is
exercised at the extraction layer with the counter's own tar_extract class).
"""
import hashlib, importlib.util, io, json, os, subprocess, sys, tarfile
from pathlib import Path

SCRIPT = Path(__file__).resolve()
LANE = SCRIPT.parent
while not (LANE / "corpus").is_dir():
    LANE = LANE.parent
assert (LANE / "corpus").is_dir(), LANE
COUNTER = LANE / "reports/round-95/c1_k_admit_counter4.py"
_spec = importlib.util.spec_from_file_location("c1v4counter", COUNTER)
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

FREEZE = "6e0bf15fed58f357b7fa0c881371ac7616a116f7"


def failing_legs(stdout):
    return [ln.split("=", 1)[0] for ln in stdout.splitlines()
            if ln.startswith("C1_") and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]


def main():
    workroot = Path(sys.argv[1]).resolve()
    receipt_out = Path(sys.argv[2]).resolve()
    workroot.mkdir(parents=True, exist_ok=True)
    root, want = C._fixture(workroot)
    art = root / f"{C.WAVE_DIR}/w1/CriticR95/critic-evidence.md"
    assert art.is_file()
    outside = root / "corpus" / "outside-critic-evidence.md"
    outside.write_bytes(art.read_bytes())       # same bytes, outside the wave dir
    art.unlink()
    art.symlink_to(outside)
    assert art.is_symlink() and art.is_file()   # symlink-to-file still "is a file"

    # (1) direct leg probe on the fixture root
    dv_ok, dv_why = C.check_votes(root, want)

    # (2) end-to-end --tree run (materialize copytree symlinks=True)
    r = subprocess.run([sys.executable, "-B", str(COUNTER), "--tree", str(root)],
                       cwd=str(LANE), capture_output=True, text=True,
                       env={**os.environ, "HYAKU_SCRATCH": str(workroot)})
    legs = failing_legs(r.stdout)

    # (3) tar probe: --rev materializes via `git archive | tar -x` using tar_extract;
    #     prove a committed symlink survives extraction so the same resolve() guard applies.
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w") as tf:
        d = tarfile.TarInfo(".ufo/waves/round-95/w1/CriticR95")
        d.type = tarfile.DIRTYPE
        d.mode = 0o755
        tf.addfile(d)
        s = tarfile.TarInfo(".ufo/waves/round-95/w1/CriticR95/link.md")
        s.type = tarfile.SYMTYPE
        s.linkname = "../../../../../corpus/SOURCES.md"
        s.mode = 0o644
        tf.addfile(s)
    dest = workroot / "tar-probe"
    with C.tar_extract(buf.getvalue(), dest):
        pass
    link = dest / ".ufo/waves/round-95/w1/CriticR95/link.md"
    tar_symlink_preserved = link.is_symlink() and os.readlink(link) == "../../../../../corpus/SOURCES.md"

    # (4) --rev reachability: any committed symlinks under the wave dirs at the freeze tip?
    ls = subprocess.run(["git", "-C", str(LANE), "ls-tree", "-r", FREEZE, "--",
                         ".ufo/waves"], capture_output=True, text=True)
    modes = sorted({ln.split()[0] for ln in ls.stdout.splitlines() if ln.strip()})
    committed_symlinks = [m for m in modes if m.startswith("120000")]

    verdict = ("killed" if (r.returncode != 0 and "C1_VOTES" in legs and not dv_ok)
               else "SURVIVED")
    receipt = {
        "attack": "A2-symlink-artifact-escape",
        "shape": "(b) CriticR95 artifact is a symlink to corpus/outside-critic-evidence.md; --tree and --rev forms",
        "direct_check_votes": {"ok": dv_ok, "why": dv_why},
        "tree_rc": r.returncode,
        "tree_failing_legs": legs,
        "tar_probe": {"symlink_preserved": tar_symlink_preserved,
                      "extracted_link": str(link)},
        "rev_reachability": {
            "committed_symlink_modes_at_freeze_tip": committed_symlinks,
            "note": ("--rev end-to-end with a planted symlink is unreachable for a seat "
                     "without a git write (barred); the counter's --rev materializer is "
                     "git archive | tar_extract, and the tar probe shows symlinks survive "
                     "extraction, so the same resolve() containment guard applies."),
        },
        "rc": r.returncode, "verdict": verdict, "expected_leg": "C1_VOTES",
        "why": [ln for ln in r.stdout.splitlines() if ln.startswith("C1_VOTES=")],
        "counter_stdout": r.stdout,
        "counter_stderr": r.stderr[-400:],
        "fixture_root": str(root),
    }
    receipt_out.write_text(json.dumps(receipt, indent=1), encoding="utf-8")
    print(json.dumps({"receipt": str(receipt_out), "rc": r.returncode,
                      "verdict": verdict, "failing_legs": legs,
                      "direct_why": dv_why, "tar_symlink_preserved": tar_symlink_preserved}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
