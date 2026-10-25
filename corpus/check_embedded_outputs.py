#!/usr/bin/env python3
"""Embedded-output verbatim gate (round-67 C7): catch quoted-output drift in a
knowledge entry before it is gated (M39 class — a transcribed command-output
line that the entry's own declared command does not print).

Registered gate (SKILL.md `## Gate registry`, kind `gate`): a committed,
re-runnable verdict script that can fail. It is deliberately OUTSIDE the
verify_* replay family: this file is
deliberately named outside the `verify_*.py` glob so the frozen ten-verifier
census and HOLD_REPLAY=10/10 denominator stay untouched (reports/round-67/
claims.md §C2). Registry row: SKILL.md §Gate registry (owner revenger).

Usage (cwd = lane root):
    python3 -B corpus/check_embedded_outputs.py --entry <knowledge.md>
        Re-parses every fenced block whose first line is `$ <command>`, runs
        that exact command (argv list, no shell), and requires every following
        output line to appear verbatim in the command's stdout.
        Exit 0 clean (>=1 block checked) · 1 drift found · 2 could-not-evaluate.
    python3 -B corpus/check_embedded_outputs.py --self-test
        Hermetic temp-tree cases plus the in-script forged control whose
        attributed failure marker is `drifted entry output accepted` — the
        marker is the last output line of a failed run (round-68 repair of the
        round-67 shadowing defect M45).

Read-only over the lane tree: it runs the entry's declared commands, which in
this corpus are standard-library readouts; it writes nothing outside its own
temp dirs.
"""
import hashlib
import json
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

MARKER = "drifted entry output accepted"
PIN_MARKER = "pinned historical script digest mismatch"
PINS_REL = "embedded_output_pins.json"


def require(cond, msg):
    if not cond:
        print(msg)
        sys.exit(1)


def parse_blocks(text):
    """Yield (command, output_lines, lineno) for each fenced `$ cmd` block."""
    blocks = []
    lines = text.splitlines()
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence and line.startswith("$ "):
            cmd = line[2:].strip()
            out = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith("$ ") and not lines[j].strip().startswith("```"):
                if lines[j].strip():
                    out.append((lines[j], j + 1))
                j += 1
            blocks.append((cmd, out, i + 1))
            i = j
            continue
        i += 1
    return blocks


def confined(argv, cwd):
    """Round-70 hardening (sentinel F1): the declared command may only be
    `python3 [-B] <relative script inside cwd> [args]` — no `-c`/`-m`, no absolute or
    `..` script path, no symlink leaving the tree."""
    rest = argv[1:]
    while rest and rest[0] == "-B":
        rest = rest[1:]
    if not rest or rest[0].startswith("-"):
        return False
    return inside(rest[0], cwd)


def inside(rel, cwd):
    p = Path(rel)
    if p.is_absolute() or ".." in p.parts:
        return False
    root = Path(cwd).resolve()
    try:
        return (root / p).resolve().relative_to(root) is not None and not (root / p).is_symlink()
    except ValueError:
        return False


def run_cmd(cmd, cwd):
    argv = shlex.split(cmd)
    if not argv:
        return None, "", 2
    if argv[0] not in ("python3", "python", sys.executable):
        return None, "", 2
    if not confined(argv, cwd):
        return None, "", 2
    proc = subprocess.run([sys.executable, "-B", *argv[1:]], cwd=str(cwd),
                          capture_output=True, text=True, timeout=120)
    return proc, proc.stdout, proc.returncode


def load_pins(entry_path):
    """Round-70 C3 (freshness): a retained entry whose embedded output was printed
    by an earlier revision of a script re-derives against that revision, pinned by
    sha256 in corpus/embedded_output_pins.json, never against the current script.
    Shape: {"<entry file name>": {"<script arg as written in the command>":
    {"use": "<repo-relative path of the pinned copy>", "sha256": "<hex>"}}}."""
    p = Path(__file__).resolve().parent / PINS_REL
    if not p.is_file():
        return {}
    return json.loads(p.read_text(encoding="utf-8")).get(Path(entry_path).name, {})


def apply_pin(cmd, pins, cwd, entry_text=None):
    """Return (command, problem). A pinned script is verified by digest before it
    replaces the script argument; a digest mismatch is a problem, not a fallback.
    Round-70 tightening (R70W1PinMut/PinCritic): the `use` path must stay inside cwd (no
    absolute path, no `..`, no symlink) and, when entry_text is given, the entry's own text
    must name the pinned digest in full — a pin is the entry declaring which script revision
    printed its output, never a free assignment."""
    argv = shlex.split(cmd)
    idx = next((i for i, a in enumerate(argv[1:], 1) if not a.startswith("-")), None)
    if idx is None or argv[idx] not in pins:
        return cmd, None
    pin = pins[argv[idx]]
    if not inside(pin["use"], cwd):
        return cmd, f"{PIN_MARKER}: {pin['use']} (path escapes the tree)"
    if entry_text is not None and pin["sha256"] not in entry_text:
        return cmd, f"{PIN_MARKER}: {pin['use']} (entry text does not name the pinned digest)"
    target = Path(cwd) / pin["use"]
    if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != pin["sha256"]:
        return cmd, f"{PIN_MARKER}: {pin['use']}"
    argv[idx] = pin["use"]
    return shlex.join(argv), None


def drift(lines, stdout_set, lineno):
    return [f"drift entry:{out_lineno} embedded output line not in recheck stdout: {l}"
            for l, out_lineno in lines if l not in stdout_set]


def evaluate(entry_path, cwd):
    """Entry mode. Returns (problems, blocks_checked) or (None, None) if the
    entry or a command could not be evaluated (exit 2)."""
    text = Path(entry_path).read_text(encoding="utf-8", errors="ignore")
    blocks = parse_blocks(text)
    if not blocks:
        return None, None
    problems = []
    checked = 0
    pins = load_pins(entry_path)
    used = set()
    for cmd, lines, lineno in blocks:
        pargv = shlex.split(cmd)
        pidx = next((i for i, a in enumerate(pargv[1:], 1) if not a.startswith("-")), None)
        if pidx is not None and pargv[pidx] in pins:
            used.add(pargv[pidx])
        cmd, pin_problem = apply_pin(cmd, pins, cwd, text)
        if pin_problem:
            problems.append(f"drift entry:{lineno} {pin_problem}")
            continue
        proc, stdout, rc = run_cmd(cmd, cwd)
        if proc is None:
            return None, None
        if rc != 0:
            problems.append(f"drift entry:{lineno} command exited {rc}: {cmd}")
            continue
        stdout_set = set(stdout.splitlines())
        problems += drift(lines, stdout_set, lineno)
        checked += 1
    for key in pins:
        if key not in used:
            problems.append(f"drift entry:0 unused pin for script argument {key}: no block of this entry runs it")
    return problems, checked


def _self_test(tmp):
    reader = tmp / "reader.py"
    reader.write_text(
        "import json,sys\n"
        "facts={'a': {'v': 1}, 'b': {'v': 2}}\n"
        "key = sys.argv[sys.argv.index('--fact')+1] if '--fact' in sys.argv else None\n"
        "rows = [facts[k] | {'fact': k} for k in (facts if key is None else [key])]\n"
        "[print(json.dumps(r, sort_keys=True)) for r in rows]\n", encoding="utf-8")
    clean_line = json.dumps({"fact": "a", "v": 1}, sort_keys=True)
    drifted_line = json.dumps({"fact": "a", "v": 9}, sort_keys=True)
    full_out = json.dumps({"fact": "a", "v": 1}, sort_keys=True) + "\n" + \
        json.dumps({"fact": "b", "v": 2}, sort_keys=True)
    clean_entry = (tmp / "clean.md")
    clean_entry.write_text(
        "```\n$ python3 -B reader.py --fact a\n" + clean_line + "\n```\n", encoding="utf-8")
    drifted_entry = (tmp / "drifted.md")
    drifted_entry.write_text(
        "```\n$ python3 -B reader.py --fact a\n" + drifted_line + "\n```\n", encoding="utf-8")
    full_entry = (tmp / "full.md")
    full_entry.write_text(
        "```\n$ python3 -B reader.py\n" + full_out + "\n```\n", encoding="utf-8")

    problems, checked = evaluate(clean_entry, tmp)
    require(problems is not None and checked == 1 and not problems,
            "self-test: clean entry not clean")
    dproblems, dchecked = evaluate(drifted_entry, tmp)
    # Forged control (round-68 repair of M45): the drifted case MUST be
    # caught. If the verbatim comparison is removed (or weakened) the branch
    # below is taken, and the attributed marker is the LAST output line, so
    # the kill is attributable to the marker and not to some earlier require.
    caught = (dproblems is not None and dchecked == 1 and dproblems
              and dproblems[0].startswith("drift entry:"))
    if not caught:
        print("self-test: drifted entry not caught")
        print(MARKER)
        sys.exit(1)
    fproblems, fchecked = evaluate(full_entry, tmp)
    require(fproblems is not None and fchecked == 1 and not fproblems,
            "self-test: full-run entry not clean")
    old = tmp / "old_reader.py"
    old.write_text("print('old')\n", encoding="utf-8")
    pins = {"reader.py": {"use": "old_reader.py", "sha256": hashlib.sha256(old.read_bytes()).hexdigest()}}
    pinned_cmd, pin_problem = apply_pin("python3 -B reader.py --fact a", pins, tmp)
    require(pin_problem is None and pinned_cmd.split()[2] == "old_reader.py",
            "self-test: a digest-verified pin did not replace the script argument")
    old.write_text("print('tampered')\n", encoding="utf-8")
    _, pin_problem = apply_pin("python3 -B reader.py --fact a", pins, tmp)
    if not (pin_problem and pin_problem.startswith(PIN_MARKER)):
        print("self-test: a tampered pinned script was accepted")
        print(PIN_MARKER + " not raised")
        sys.exit(1)
    old.write_text("print('old')\n", encoding="utf-8")
    require(apply_pin("python3 -B reader.py --fact a", pins, tmp, "text naming " + pins["reader.py"]["sha256"])[1] is None,
            "self-test: a pin whose digest the entry text names was refused")
    _, pin_problem = apply_pin("python3 -B reader.py --fact a", pins, tmp, "text that names no digest")
    require(pin_problem is not None and pin_problem.startswith(PIN_MARKER),
            "self-test: a pin the entry text does not name was accepted")
    (tmp / "link.py").symlink_to("/etc/hostname")
    require(confined(["python3", "-B", "reader.py", "--fact", "a"], tmp)
            and not confined(["python3", "-c", "print(1)"], tmp)
            and not confined(["python3", "-B", "-m", "json.tool"], tmp)
            and not confined(["python3", "-B", "/etc/passwd.py"], tmp)
            and not confined(["python3", "-B", "../x.py"], tmp)
            and not confined(["python3", "-B", "link.py"], tmp),
            "self-test: command confinement accepted or refused the wrong spelling")
    # wiring leg (R70W2GateConfinement: the predicate legs alone leave `run_cmd`'s call site unguarded):
    # an entry whose declared command is refused by confinement must come back could-not-evaluate
    hostile = tmp / "hostile.md"
    hostile.write_text("```\n$ python3 -B -c print(1)\n1\n```\n", encoding="utf-8")
    hproblems, hchecked = evaluate(hostile, tmp)
    require(hproblems is None and hchecked is None,
            "self-test: an entry declaring `python3 -c` was evaluated instead of refused")
    print("SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest and named by the entry, commands confined to relative scripts inside the tree and refused through evaluate()")


def main():
    args = sys.argv[1:]
    if args == ["--self-test"]:
        with tempfile.TemporaryDirectory(prefix="rev-r67-c7-selftest-") as d:
            _self_test(Path(d))
        sys.exit(0)
    if len(args) == 2 and args[0] == "--entry":
        problems, checked = evaluate(args[1], Path.cwd())
        if problems is None:
            print("could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure")
            sys.exit(2)
        for p in problems:
            print(p)
        print(f"checked_blocks={checked} problems={len(problems)}")
        sys.exit(0 if not problems else 1)
    print(__doc__)
    sys.exit(64)


if __name__ == "__main__":
    main()
