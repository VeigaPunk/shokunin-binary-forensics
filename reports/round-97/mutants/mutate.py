#!/usr/bin/env python3
r"""Round-97 mutation harness for the C1 admission counter (stdlib only).

    python3 -B reports/round-97/mutants/mutate.py --counter <counter.py> --out <dir> \
        [--kill-tree <tree>] [--selftest] [--jobs N] [--label V5]

Writes into <dir>/mutants/:
  unmutated.py    the counter with LANE pinned: the baseline every mutant is diffed against
  <name>.py       one mutant per site: the baseline with exactly one edit
  manifest.json   (in <dir>) site table: name, class, function, line, leg(s), edit
Prints, per mutant: name, changed line (baseline numbering), leg(s), and the unified-diff hunk.

Mutant classes (each a single-token edit of a decision that feeds a C1_* leg):
  cmp     a comparison operator inverted: == <-> !=, in <-> not in, is <-> is not,
          < <-> >=, > <-> <=
  not     a boolean `not` deleted in a decision expression (`not X` -> `X`), including
          leg results such as `return (not fails)`
  if      an `if` test that is neither a comparison nor a `not` is negated: `not ` is
          prefixed; a BoolOp test is wrapped as `not (...)`
  d-host  the MutationR96 d-host edit: the host-allowlist sub-check of check_receipts is
          removed (its `if host not in HOST_ALLOWLIST:` line and the next fails.append line)

Scope: every top-level function of the counter except the archive materialiser, the CLI,
and the self-test fixture builders (their branches build fixtures, they decide no leg).

Lane pin: every file (baseline and mutants) replaces
    LANE = Path(__file__).resolve().parents[2]
with LANE = Path(<lane root>). Without it a copy under scratch resolves LANE to a
non-repo directory and base_readme's `git archive FREEZE_REV` fails. Identical for baseline
and mutants, so the pin is never the verdict difference.

Detectors (optional; each runs the mutant file itself):
  --kill-tree <tree>  `--tree <tree>`. KILLED when the verdict set (lines C1_<LEG>=pass|fail|n/m
                      and C1_VERDICT) or the exit code differs from the unmutated run on the
                      same tree. A timeout counts as killed (tag `timeout`).
  --selftest          the counter's frozen `--self-test`. KILLED when it does not print
                      SELFTEST_C1V<n>=pass with rc 0 (any counter version). The unmutated self-test must pass first.

Exit: 0 harness completed; 2 counter malformed (pin anchor / d-host anchor missing);
3 a requested detector's baseline did not reproduce.
"""
import argparse
import ast
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
PIN_OLD = "LANE = Path(__file__).resolve().parents[2]"
PIN_NEW = 'LANE = Path("{lane}")  # MUTATE: lane pinned (scratch copies)'
TIMEOUT = 300
EXCLUDE = {"materialize", "tar_extract", "main", "self_test", "_fixture", "_fixture_delta",
           "_set_row_cell", "_set_other_row_cell", "_vote"}
# leg-checking function -> the C1_* leg it decides; helpers inherit the legs of the checks
# that reach them; evaluate-level sites take the leg of the enclosing legs[...] assignment
CHECK_LEG = {
    "check_registry": "C1_REGISTRY",
    "check_votes": "C1_VOTES",
    "check_receipts": "C1_RECEIPTS",
    "check_pycache": "C1_PYCACHE",
    "check_admitted_union": "C1_ADMITTED_UNION",
    "check_sids": "C1_SIDS",
    "check_sources": "C1_SOURCES",
    "check_quotes": "C1_QUOTES",
    "check_embed_nonvacuous": "C1_EMBED_NONVACUOUS",
    "base_readme": "C1_ONLY_C02",
}
OP_CLS = {ast.Eq: "==", ast.NotEq: "!=", ast.In: "in", ast.NotIn: "not in",
          ast.Is: "is", ast.IsNot: "is not", ast.Lt: "<", ast.LtE: "<=",
          ast.Gt: ">", ast.GtE: ">="}
OP_INV = {"==": "!=", "!=": "==", "in": "not in", "not in": "in", "is": "is not",
          "is not": "is", "<": ">=", ">=": "<", ">": "<=", "<=": ">"}
OP_RE = re.compile(r"is\s+not|not\s+in|<=|>=|==|!=|<|>|\bin\b|\bis\b")
VERDICT_RE = re.compile(r"^(C1_[A-Z0-9_]+)=(pass|fail|\d+/\d+)$")
SELFTEST_PASS = re.compile(r"SELFTEST_C1V\d+=pass\b")


def pin(src, lane):
    if src.count(PIN_OLD) != 1:
        raise SystemExit(2)
    return src.replace(PIN_OLD, PIN_NEW.format(lane=lane), 1)


def line_table(src):
    lines = re.findall(r"[^\n]*\n|[^\n]+", src)
    starts, acc = [], 0
    for ln in lines:
        starts.append(acc)
        acc += len(ln)
    return lines, starts


def sites(pinned):
    tree = ast.parse(pinned)
    lines, starts = line_table(pinned)

    def off(lineno, bcol):
        # ast column offsets are UTF-8 byte offsets into the physical line
        ln = lines[lineno - 1]
        return starts[lineno - 1] + len(ln.encode("utf-8")[:bcol].decode("utf-8"))

    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name not in EXCLUDE]
    names = {f.name for f in funcs}
    direct = {}
    for f in funcs:
        direct[f.name] = {n.func.id for n in ast.walk(f)
                          if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                          and n.func.id in names} - {f.name}
    helper_legs = {}
    for fn, leg in CHECK_LEG.items():
        todo, seen = [fn], {fn}
        while todo:
            cur = todo.pop()
            helper_legs.setdefault(cur, set()).add(leg)
            for nxt in direct.get(cur, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
    # evaluate calls _raw_line only inside the C1_ONLY_C02 block
    helper_legs.setdefault("_raw_line", set()).add("C1_ONLY_C02")
    parents = {}
    for n in ast.walk(tree):
        for c in ast.iter_child_nodes(n):
            parents[c] = n
    evaluate = next(f for f in funcs if f.name == "evaluate")
    assigns = sorted(
        (n.lineno, n.targets[0].slice.value) for n in ast.walk(evaluate)
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript)
        and isinstance(n.targets[0].value, ast.Name) and n.targets[0].value.id == "legs"
        and isinstance(n.targets[0].slice, ast.Constant))

    def top_fn(node):
        cur = node
        while parents.get(cur) is not tree:
            cur = parents[cur]
        return cur.name if isinstance(cur, ast.FunctionDef) else "module"

    def legs_of(node):
        if top_fn(node) == "evaluate":
            cur = node
            while cur in parents:
                cur = parents[cur]
                if (isinstance(cur, ast.Assign) and isinstance(cur.targets[0], ast.Subscript)
                        and isinstance(cur.targets[0].value, ast.Name)
                        and cur.targets[0].value.id == "legs"):
                    return [cur.targets[0].slice.value]
            for lineno, key in assigns:
                if lineno >= node.lineno:
                    return [key]
            return ["UNATTRIBUTED"]
        return sorted(helper_legs.get(top_fn(node), set())) or ["UNATTRIBUTED"]

    def in_message(node):
        # a decision inside the message slot (`"ok" if X else ...`, element 1 of a return
        # tuple) selects WHY text only; it decides no leg, so it is not a mutation site
        cur = node
        while cur in parents:
            par = parents[cur]
            tup = parents.get(par)
            if isinstance(par, ast.IfExp) and isinstance(tup, ast.Tuple) \
                    and isinstance(parents.get(tup), ast.Return):
                return True
            cur = par
        return False

    excluded = []
    out = []
    for f in funcs:
        for n in ast.walk(f):
            if in_message(n):
                if isinstance(n, (ast.Compare, ast.UnaryOp, ast.If)):
                    excluded.append({"line": n.lineno, "fn": top_fn(n)})
                continue
            if isinstance(n, ast.Compare):
                comps = [n.left] + list(n.comparators)
                for i, op in enumerate(n.ops):
                    a, b = comps[i], comps[i + 1]
                    m = OP_RE.search(pinned, off(a.end_lineno, a.end_col_offset),
                                     off(b.lineno, b.col_offset))
                    tok = re.sub(r"\s+", " ", m.group(0)) if m else None
                    if tok != OP_CLS.get(type(op)):
                        raise SystemExit(f"operator site mismatch at line {n.lineno}")
                    out.append({"kind": "cmp", "line": n.lineno, "fn": top_fn(n),
                                "span": (m.start(), m.end()), "repl": OP_INV[tok],
                                "legs": legs_of(n), "desc": f"{tok} -> {OP_INV[tok]}"})
            elif isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.Not):
                st = off(n.lineno, n.col_offset)
                if pinned[st:st + 3] != "not":
                    raise SystemExit(f"not-site mismatch at line {n.lineno}")
                e = st + 3
                while pinned[e] in " \t":
                    e += 1
                out.append({"kind": "not", "line": n.lineno, "fn": top_fn(n),
                            "span": (st, e), "repl": "", "legs": legs_of(n),
                            "desc": "delete `not`"})
            elif isinstance(n, ast.If) and not isinstance(n.test, (ast.Compare, ast.UnaryOp)):
                t = n.test
                ts = off(t.lineno, t.col_offset)
                te = off(t.end_lineno, t.end_col_offset)
                if isinstance(t, ast.BoolOp):
                    out.append({"kind": "if", "line": n.lineno, "fn": top_fn(n),
                                "span": (ts, te), "repl": ("not (", ")"),
                                "legs": legs_of(n), "desc": "negate BoolOp test"})
                else:
                    out.append({"kind": "if", "line": n.lineno, "fn": top_fn(n),
                                "span": (ts, ts), "repl": "not ", "legs": legs_of(n),
                                "desc": "negate if test"})
    # d-host: MutationR96's edit (host allowlist sub-check removed, two lines)
    anchor = [i for i, ln in enumerate(lines)
              if re.match(r"^\s*if host not in HOST_ALLOWLIST:\s*$", ln)]
    if len(anchor) != 1 or 'fails.append(f"{sid}:host' not in lines[anchor[0] + 1]:
        raise SystemExit(2)
    i = anchor[0]
    out.append({"kind": "d-host", "line": i + 1, "fn": "check_receipts",
                "span": (starts[i], starts[i + 1] + len(lines[i + 1])), "repl": "",
                "legs": ["C1_RECEIPTS"],
                "desc": "host allowlist sub-check removed (MutationR96 d-host)"})
    out.sort(key=lambda x: (x["line"], x["span"]))
    return out, [k for _, k in assigns], excluded


def build(src, lane):
    pinned = pin(src, lane)
    found, leg_names, excluded = sites(pinned)
    mutants = []
    for idx, s in enumerate(found, 1):
        a, b = s["span"]
        rep = s["repl"]
        if isinstance(rep, tuple):
            text = pinned[:a] + rep[0] + pinned[a:b] + rep[1] + pinned[b:]
        else:
            text = pinned[:a] + rep + pinned[b:]
        name = "d-host" if s["kind"] == "d-host" else f"m{idx:03d}-{s['kind']}-{s['fn']}-L{s['line']}"
        mutants.append({"name": name, "text": text, "kind": s["kind"], "fn": s["fn"],
                        "line": s["line"], "legs": s["legs"], "desc": s["desc"]})
    return pinned, mutants, leg_names, excluded


def verdict_set(stdout):
    return sorted(ln for ln in stdout.splitlines() if VERDICT_RE.match(ln))


def c1_lines(stdout):
    return sorted(ln for ln in stdout.splitlines() if ln.startswith("C1_"))


def run(path, args, env, cwd):
    try:
        p = subprocess.run([sys.executable, "-B", str(path), *args], env=env, cwd=cwd,
                           capture_output=True, text=True, timeout=TIMEOUT)
        return {"rc": p.returncode, "out": p.stdout, "err": p.stderr, "timeout": False}
    except subprocess.TimeoutExpired as e:
        def s(x):
            return x.decode("utf-8", "replace") if isinstance(x, bytes) else (x or "")
        return {"rc": None, "out": s(e.stdout), "err": s(e.stderr), "timeout": True}


def kill_tree(mdir, names, tree, env, jobs):
    base = run(mdir / "unmutated.py", ["--tree", str(tree)], env, str(mdir))
    bvs = verdict_set(base["out"])

    def one(name):
        r = run(mdir / f"{name}.py", ["--tree", str(tree)], env, str(mdir))
        vs = verdict_set(r["out"])
        if r["timeout"]:
            why = "timeout"
        elif vs != bvs and r["rc"] != base["rc"]:
            why = "rc+verdict"
        elif vs != bvs:
            why = "verdict-set"
        elif r["rc"] != base["rc"]:
            why = "rc"
        else:
            why = None
        msg_only = why is None and c1_lines(r["out"]) != c1_lines(base["out"])
        return {"name": name, "rc": r["rc"], "killed": why is not None,
                "why": why or ("message-only" if msg_only else "survived"),
                "diff": sorted(set(vs) ^ set(bvs)) if why else []}

    with ThreadPoolExecutor(max_workers=jobs) as ex:
        results = list(ex.map(one, names))
    return {"base_rc": base["rc"], "base_verdicts": bvs, "results": results}


def selftest(mdir, names, env, jobs):
    base = run(mdir / "unmutated.py", ["--self-test"], env, str(mdir))
    if base["rc"] != 0 or not SELFTEST_PASS.search(base["out"]):
        raise SystemExit(3)

    def one(name):
        r = run(mdir / f"{name}.py", ["--self-test"], env, str(mdir))
        ok = (not r["timeout"]) and r["rc"] == 0 and bool(SELFTEST_PASS.search(r["out"]))
        fails = [ln for ln in r["out"].splitlines() if ln.startswith("SELFTEST FAIL:")]
        return {"name": name, "rc": r["rc"], "killed": not ok, "timeout": r["timeout"],
                "fail_lines": fails[:3]}

    with ThreadPoolExecutor(max_workers=jobs) as ex:
        results = list(ex.map(one, names))
    return {"base_rc": base["rc"], "results": results}


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--counter", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--kill-tree")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--label")
    a = ap.parse_args(argv)
    cpath = Path(a.counter)
    m = re.search(r"counter(\d+)", cpath.name)
    label = a.label or (f"V{m.group(1)}" if m else "VX")
    src = cpath.read_text(encoding="utf-8")
    out = Path(a.out)
    mdir = out / "mutants"
    mdir.mkdir(parents=True, exist_ok=True)
    pinned, mutants, leg_names, excluded = build(src, str(LANE))
    (mdir / "unmutated.py").write_text(pinned, encoding="utf-8")
    manifest = {"counter": str(cpath), "counter_sha256": hashlib.sha256(
        src.encode("utf-8")).hexdigest(), "lane_pin": str(LANE), "mutants": [],
        "excluded_msg": excluded}
    for mu in mutants:
        (mdir / f"{mu['name']}.py").write_text(mu["text"], encoding="utf-8")
        hunk = "".join(difflib.unified_diff(pinned.splitlines(True), mu["text"].splitlines(True),
                                            "unmutated", mu["name"], n=0))
        print(f"MUTANT {mu['name']} line={mu['line']} class={mu['kind']} fn={mu['fn']} "
              f"legs={','.join(mu['legs'])} edit={mu['desc']}")
        print(hunk, end="")
        manifest["mutants"].append({k: mu[k] for k in ("name", "kind", "fn", "line", "legs",
                                                      "desc")})
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    covered = {leg for mu in mutants for leg in mu["legs"]}
    for leg in dict.fromkeys(leg_names):
        if leg not in covered:
            print(f"NO_SITE leg={leg} (no comparison, if or not decides it)")
    print(f"EXCLUDED_MSG={len(excluded)} (WHY-text-only decisions; not leg sites): "
          + (",".join(f"L{x['line']}" for x in excluded) or "none"))
    print(f"MUTANTS_WRITTEN={len(mutants)} counter={cpath.name} label={label}")
    names = [mu["name"] for mu in mutants]
    env = dict(os.environ, PYTHONUTF8="1", HYAKU_SCRATCH=str(out / "hyaku"))
    (out / "hyaku").mkdir(parents=True, exist_ok=True)
    if a.kill_tree:
        kt = kill_tree(mdir, names, Path(a.kill_tree), env, a.jobs)
        for r in kt["results"]:
            print(f"KILL_TREE {r['name']} rc={r['rc']} killed={r['killed']} why={r['why']}"
                  f" diff={','.join(r['diff']) or '-'}")
        k = sum(1 for r in kt["results"] if r["killed"])
        print(f"BASE_TREE rc={kt['base_rc']} verdicts={len(kt['base_verdicts'])}")
        print(f"MUTANT_KILL_{label}={k}/{len(kt['results'])}")
        print("SURVIVORS_TREE=" + (",".join(r["name"] for r in kt["results"] if not r["killed"])
                                   or "none"))
    if a.selftest:
        st = selftest(mdir, names, env, a.jobs)
        for r in st["results"]:
            print(f"KILL_SELFTEST {r['name']} rc={r['rc']} killed={r['killed']} "
                  f"timeout={r['timeout']} first={' | '.join(r['fail_lines']) or '-'}")
        k = sum(1 for r in st["results"] if r["killed"])
        print(f"MUTANT_SELFTEST_{label}={k}/{len(st['results'])}")
        print("SURVIVORS_SELFTEST=" + (",".join(r["name"] for r in st["results"]
                                                if not r["killed"]) or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
