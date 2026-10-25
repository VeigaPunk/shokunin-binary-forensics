#!/usr/bin/env python3
"""Embedded-output verbatim gate (round-67 C7): catch quoted-output drift in a
knowledge entry before it is gated (M39 class — a transcribed command-output
line that the entry's own declared command does not print).

Probe, not a registered gate of the verify_* replay family: this file is
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
        attributed failure marker is `drifted entry output accepted`.

Read-only over the lane tree: it runs the entry's declared commands, which in
this corpus are standard-library readouts; it writes nothing outside its own
temp dirs.
"""
import json
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

MARKER = "drifted entry output accepted"


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


def run_cmd(cmd, cwd):
    argv = shlex.split(cmd)
    if not argv:
        return None, "", 2
    if argv[0] not in ("python3", "python", sys.executable):
        return None, "", 2
    proc = subprocess.run([sys.executable, "-B", *argv[1:]], cwd=str(cwd),
                          capture_output=True, text=True, timeout=120)
    return proc, proc.stdout, proc.returncode


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
    for cmd, lines, lineno in blocks:
        proc, stdout, rc = run_cmd(cmd, cwd)
        if proc is None:
            return None, None
        if rc != 0:
            problems.append(f"drift entry:{lineno} command exited {rc}: {cmd}")
            continue
        stdout_set = set(stdout.splitlines())
        problems += drift(lines, stdout_set, lineno)
        checked += 1
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
    require(dproblems is not None and dchecked == 1 and dproblems
            and dproblems[0].startswith("drift entry:"),
            "self-test: drifted entry not caught")
    fproblems, fchecked = evaluate(full_entry, tmp)
    require(fproblems is not None and fchecked == 1 and not fproblems,
            "self-test: full-run entry not clean")
    # In-script forged control: the drifted case MUST be caught. If the
    # verbatim comparison is removed (or weakened), this fires with the
    # attributed marker as the last output line.
    require(not ok(dproblems), MARKER)
    print("SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired")


def ok(problems):
    return not problems


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
