#!/usr/bin/env python3
r"""Round-99 mutation harness for the C1 admission counter (stdlib only).

    python3 -B reports/round-99/mutants/mutate8.py --counter <counter8.py> --out <dir> \
        [--base-counter reports/round-98/c1_k_admit_counter7.py] \
        [--prereg reports/round-99/mutants/mutants-r99.json] \
        [--kill-tree <tree>] [--selftest] [--jobs N] [--label V8] [--profile c02|c14|c14r99]

Port of reports/round-98/mutants/mutate7.py (routed defect 5 fixed, below), keeping the
v6 operator set (cmp / not / if / d-host) and the three new-leg operator classes
(del-leg / widen-re / drop-why). The v8 new legs are DERIVED, not hard-coded:
new_legs = leg names of the counter under test minus leg names of --base-counter (the
frozen v7 counter); without --base-counter the harness falls back to the eight v7 legs
(V7_NEW_LEGS). The optional --prereg file (reports/round-99/mutants/mutants-r99.json) is
the pre-registration: written BEFORE the harness first runs on the counter's bytes. It
lists (a) one del-leg target per new v8 leg and (b) explicit mut-const text edits for
the c14r99 profile constants (VOTES_DIR, REGISTRY_REL, FREEZE_REV, PINNED_SEATS). The
harness fails closed (exit 2) when a derived new leg is not registered, a registered
leg is absent from the counter or has no del-leg site, or a mut-const find-string does
not occur exactly once in the pinned source.

  del-leg   the `legs["<new leg>"] = ...` assignment in evaluate is deleted (or replaced
            by `pass` when it is the sole statement of an if arm): the leg is never decided
  widen-re  every str-literal re.match / re.fullmatch / re.search pattern inside a
            function attributed to a new leg is widened to `[\s\S]*` (accept anything);
            a pattern already equal to the widening is skipped as a no-op. re.sub /
            re.split / module-level re.compile names are out of scope (disclosed).
  drop-why  the statement emitting `<new leg>_WHY=` is deleted (pass under an if arm).
            Message-text only, so it is pre-registered as an expected survivor; it
            documents that WHY text is not instrumented by either detector.

The carried classes are unchanged from v6:
  cmp     a comparison operator inverted: == <-> !=, in <-> not in, is <-> is not,
          < <-> >=, > <-> <=
  not     a boolean `not` deleted in a decision expression
  if      an `if` test that is neither a comparison nor a `not` is negated
  d-host  the MutationR96 d-host edit: the host-allowlist sub-check of check_receipts is
          removed (its `if <x> not in <CONST>:` line and the following fails.append line
          carrying `:host`); exactly one such pair must exist.

Routed defect 5 (r98) fixed here: mutate7's self-test detector required the label
`SELFTEST_C1V<n>=pass`, but the v7/v8 counters print `SELFTEST_C1V<n>=OK|FAIL legs=<n>`
(v7 observed: `SELFTEST_C1V7=OK legs=55`, rc 0, while mutate7 exited 3). The baseline
therefore false-failed on a genuinely passing counter, and the mutant kill rule would
have marked every healthy mutant killed. mutate8 accepts `=OK` or `=pass` and treats
only `=FAIL` (or a nonzero rc / missing label) as failure; the baseline check now fails
exactly when the unmutated counter's self-test genuinely fails. When the counter source
supports `--work`, baseline and mutants are both invoked as
`--self-test --work <out>/st` (the recorded control invocation; identical on both sides
of the comparison, so never the verdict difference).

Leg attribution is derived from the counter source, not hard-coded: every function
reachable (transitively) from the RHS of a `legs["<LEG>"] = ...` assignment in evaluate
inherits that LEG, and a function with no such attribution inherits the LEG of the
evaluate block(s) that call it (the v6 `_raw_line` rule, generalized). On the frozen v6
counter this reproduces the r97 site table exactly (verified: same 140 sites, same legs
labels, same exclusions).

--profile is appended to the counter invocation of the --tree detector only when the
counter source contains the literal `--profile` flag (the v7 CLI contract). The operator
set is profile-independent; the profile choice changes only the constants the counter
configures. On v6 the new classes find no sites.

Scope: every top-level function of the counter except the archive materialiser, the CLI,
the self-test and the fixture builders (names materialize, tar_extract, main, self_test,
and any name starting _fixture, _set_, _vote, _stub, _delta).

Lane pin: every file (baseline and mutants) replaces
    LANE = Path(__file__).resolve().parents[2]
with LANE = Path(<lane root>), exactly as in v6/v5. Identical in baseline and mutants,
so the pin is never the verdict difference.

Detectors (optional; each runs the mutant file itself):
  --kill-tree <tree>  `--tree <tree>` (plus `--profile <p>` when supported). KILLED when
                      the verdict set (lines C1_<LEG>=pass|fail|n/m and C1_VERDICT) or the
                      exit code differs from the unmutated run on the same tree; a timeout
                      counts as killed (tag `timeout`); a WHY-text-only change is recorded
                      as `message-only`, not a kill.
  --selftest          the counter's frozen `--self-test`. KILLED when it does not print
                      SELFTEST_C1V<n>=OK (or =pass) with rc 0, or prints =FAIL. The
                      unmutated self-test must pass first (else exit 3).

Exit: 0 harness completed; 2 counter malformed (pin anchor / d-host anchor missing or
ambiguous, base-counter anchor missing, prereg mismatch); 3 the self-test baseline did
not reproduce (a genuine counter self-test failure).
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
EXCLUDE = {"materialize", "tar_extract", "main", "self_test"}
EXCLUDE_PREFIX = ("_fixture", "_set_", "_vote", "_stub", "_delta")
V7_NEW_LEGS = ["C1_ROWSET", "C1_ENTRY_BYTES", "C1_HEADER_POSITION", "C1_VERIFIED_AT",
               "C1_VOTE_NOTES", "C1_OWNWORK_PATHS", "C1_QUOTE_BYTES", "C1_USEDBY_GROUNDED"]
WIDEN = r"[\s\S]*"
OP_CLS = {ast.Eq: "==", ast.NotEq: "!=", ast.In: "in", ast.NotIn: "not in",
          ast.Is: "is", ast.IsNot: "is not", ast.Lt: "<", ast.LtE: "<=",
          ast.Gt: ">", ast.GtE: ">="}
OP_INV = {"==": "!=", "!=": "==", "in": "not in", "not in": "in", "is": "is not",
          "is not": "is", "<": ">=", ">=": "<", ">": "<=", "<=": ">"}
OP_RE = re.compile(r"is\s+not|not\s+in|<=|>=|==|!=|<|>|\bin\b|\bis\b")
VERDICT_RE = re.compile(r"^(C1_[A-Z0-9_]+)=(pass|fail|\d+/\d+)$")
SELFTEST_PASS = re.compile(r"SELFTEST_C1V\d+=(?:OK|pass)\b")
SELFTEST_FAIL = re.compile(r"SELFTEST_C1V\d+=FAIL\b")


def excluded_fn(name):
    return name in EXCLUDE or name.startswith(EXCLUDE_PREFIX)


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


def stmt_span(node, lines, starts):
    return (starts[node.lineno - 1],
            starts[node.end_lineno - 1] + len(lines[node.end_lineno - 1]))


def sites(pinned, new_legs):
    tree = ast.parse(pinned)
    lines, starts = line_table(pinned)

    def off(lineno, bcol):
        # ast column offsets are UTF-8 byte offsets into the physical line
        ln = lines[lineno - 1]
        return starts[lineno - 1] + len(ln.encode("utf-8")[:bcol].decode("utf-8"))

    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and not excluded_fn(n.name)]
    names = {f.name for f in funcs}
    direct = {}
    for f in funcs:
        direct[f.name] = {n.func.id for n in ast.walk(f)
                          if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                          and n.func.id in names} - {f.name}
    evaluate = next(f for f in funcs if f.name == "evaluate")
    assign_nodes = [n for n in ast.walk(evaluate)
                    if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript)
                    and isinstance(n.targets[0].value, ast.Name)
                    and n.targets[0].value.id == "legs"
                    and isinstance(n.targets[0].slice, ast.Constant)]
    assigns = sorted((n.lineno, n.targets[0].slice.value) for n in assign_nodes)
    parents = {}
    for n in ast.walk(tree):
        for c in ast.iter_child_nodes(n):
            parents[c] = n

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
                if id(cur) in dict_map:
                    for k, v in dict_map[id(cur)]:
                        if v.lineno <= node.lineno <= v.end_lineno:
                            return [k.value]
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

    # derived leg attribution: a LEG belongs to every included function called (directly
    # or through the call graph) in the statements that produce its verdict. v6's
    # legs["L"] = ok lines carry no calls (the check call sits in a preceding
    # tuple-unpack), so the names read by the RHS are traced backward through evaluate's
    # bindings to the calls that produced them (v6 hard-coded the resulting map).
    def reads(node):
        return {x.id for x in ast.walk(node)
                if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)}

    def calls_in(node):
        return {n.func.id for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id in names and n.func.id != "evaluate"}

    bindings = []
    for n in ast.walk(evaluate):
        if isinstance(n, ast.Assign):
            bindings.append((n, n.value, n.targets))
        elif isinstance(n, ast.AugAssign):
            bindings.append((n, n.value, [n.target]))
        elif isinstance(n, ast.For):
            bindings.append((n, n.iter, [n.target]))
    bindings.sort(key=lambda b: b[0].lineno)

    helper_legs = {}
    for a in assign_nodes:
        leg = a.targets[0].slice.value
        seeds = set(calls_in(a.value))
        work = set(reads(a.value))
        for node, val, tgts in reversed([b for b in bindings if b[0].lineno < a.lineno]):
            tnames = set()
            for t in tgts:
                if isinstance(t, ast.Name):
                    tnames.add(t.id)
                elif isinstance(t, (ast.Tuple, ast.List)):
                    tnames |= {e.id for e in t.elts if isinstance(e, ast.Name)}
            if tnames & work:
                work |= reads(val)
                seeds |= calls_in(val)
        todo, seen = list(seeds), set(seeds)
        while todo:
            cur = todo.pop()
            helper_legs.setdefault(cur, set()).add(leg)
            for nxt in direct.get(cur, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
    # dict-literal leg tables (v7 builds its new legs as {"C1_X": check_x(...)}): a
    # Constant key naming a C1_* leg attributes that leg to the call graph of its value
    dict_legs = []
    dict_map = {}
    for f in funcs:
        for n in ast.walk(f):
            if isinstance(n, ast.Dict):
                pairs = [(k, v) for k, v in zip(n.keys, n.values)
                         if isinstance(k, ast.Constant) and isinstance(k.value, str)
                         and re.match(r"C1_[A-Z0-9_]+$", str(k.value))]
                if pairs:
                    dict_legs.append(pairs)
                    dict_map[id(n)] = pairs
                    for k, v in pairs:
                        todo, seen = list(calls_in(v)), set(calls_in(v))
                        while todo:
                            cur = todo.pop()
                            helper_legs.setdefault(cur, set()).add(k.value)
                            for nxt in direct.get(cur, ()):
                                if nxt not in seen:
                                    seen.add(nxt)
                                    todo.append(nxt)
    # a function with no RHS attribution inherits the leg of the evaluate block(s) that
    # call it (the v6 `_raw_line` rule, generalized)
    for n in ast.walk(evaluate):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                and n.func.id in names and n.func.id != "evaluate" \
                and not helper_legs.get(n.func.id):
            helper_legs[n.func.id] = set(legs_of(n))

    out = []
    excluded = []
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
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and isinstance(n.func.value, ast.Name) and n.func.value.id == "re" \
                    and n.func.attr in ("match", "fullmatch", "search") and n.args:
                newls = sorted(set(helper_legs.get(f.name, set())) & set(new_legs))
                if not newls:
                    continue
                a0 = n.args[0]
                tok = (off(a0.lineno, a0.col_offset), off(a0.end_lineno, a0.end_col_offset))
                rep = 'r"' + WIDEN + '"'
                if pinned[tok[0]:tok[1]] == rep:
                    continue  # widening is a no-op on this pattern expression
                for leg in newls:
                    out.append({"kind": "widen-re", "line": n.lineno, "fn": f.name,
                                "span": tok, "repl": rep, "legs": [leg],
                                "desc": f"pattern widened to {WIDEN} ({leg})"})

    def del_site(stmt, legs, kind, desc):
        # delete the statement's physical lines; if it is the only statement of an if
        # arm, replace it by `pass` so the block stays syntactically valid
        par = parents.get(stmt)
        if isinstance(par, ast.If) and ((par.body and par.body[0] is stmt) or stmt in par.orelse):
            indent = re.match(r"[ \t]*", lines[stmt.lineno - 1]).group(0)
            out.append({"kind": kind, "line": stmt.lineno, "fn": top_fn(stmt),
                        "span": stmt_span(stmt, lines, starts), "repl": indent + "pass",
                        "legs": legs, "desc": desc + " (sole if-arm statement -> pass)"})
        else:
            out.append({"kind": kind, "line": stmt.lineno, "fn": top_fn(stmt),
                        "span": stmt_span(stmt, lines, starts), "repl": "",
                        "legs": legs, "desc": desc})

    for a in assign_nodes:
        leg = a.targets[0].slice.value
        if leg in new_legs:
            del_site(a, [leg], "del-leg",
                     f"legs[{leg!r}] assignment deleted (leg never decided)")

    stmt_spans = [(n, stmt_span(n, lines, starts)) for f in funcs for n in ast.walk(f)
                  if isinstance(n, ast.stmt)]
    by_span = {}
    for leg in new_legs:
        needle = leg + "_WHY"
        hits = [(n, sp) for n, sp in stmt_spans if needle in pinned[sp[0]:sp[1]]]
        inner = [(n, sp) for n, sp in hits
                 if not any(sp[0] <= osp[0] and osp[1] <= sp[1] and osp != sp
                            for _, osp in hits)]
        for n, sp in inner:
            by_span.setdefault(sp, (n, set()))[1].add(leg)
    # generic WHY loop (v7 prints f"{name}_WHY={why}" over the new-checks dict): one
    # statement decides the WHY text of every leg the loop's dict carries; the legs are
    # resolved through the loop iterable's call graph to its returned dict keys
    for f in funcs:
        for n in ast.walk(f):
            if not isinstance(n, ast.stmt):
                continue
            sp = stmt_span(n, lines, starts)
            seg = pinned[sp[0]:sp[1]]
            if "_WHY" not in seg:
                continue
            if any(k.value + "_WHY" in seg for pairs in dict_legs for k, _ in pairs):
                continue  # literal per-leg emission, already handled by the needles
            frm = None
            cur = n
            while cur in parents:
                cur = parents[cur]
                if isinstance(cur, ast.For):
                    frm = cur
                    break
            if frm is None:
                continue
            legs = set()
            by_name = {fd.name: fd for fd in funcs}
            for fname in calls_in(frm.iter):
                fnode = by_name.get(fname)
                if fnode is None:
                    continue
                for r in ast.walk(fnode):
                    if isinstance(r, ast.Return) and isinstance(r.value, ast.Dict):
                        for k, v in zip(r.value.keys, r.value.values):
                            if isinstance(k, ast.Constant) and isinstance(k.value, str) \
                                    and k.value in new_legs:
                                legs.add(k.value)
            if legs:
                by_span.setdefault(sp, (n, set()))[1].update(legs)
    # del-leg on dict-literal leg tables: delete the physical lines of the entry (key
    # through the end of its value line, trailing comma included) so the leg is never
    # decided
    for pairs in dict_legs:
        for k, v in pairs:
            if k.value in new_legs:
                a = off(k.lineno, k.col_offset)
                b = starts[v.end_lineno - 1] + len(lines[v.end_lineno - 1])
                out.append({"kind": "del-leg", "line": k.lineno, "fn": top_fn(k),
                            "span": (a, b), "repl": "", "legs": [k.value],
                            "desc": f"checks-dict entry {k.value!r} deleted "
                                    f"(leg never decided)"})
    for sp in sorted(by_span):
        n, legs = by_span[sp]
        del_site(n, sorted(legs), "drop-why",
                 "WHY-emitting statement deleted (message-only by construction)")

    # d-host: MutationR96's edit (host allowlist sub-check removed, two lines). The
    # anchor is broadened to any `if <name> not in <CONST>:` followed by a fails.append
    # carrying `:host`; it must still match exactly one pair.
    anchor = [i for i, ln in enumerate(lines)
              if re.match(r"^\s*if \w+ not in [A-Z][A-Z0-9_]*:\s*$", ln)]
    anchor = [i for i in anchor
              if i + 1 < len(lines) and "fails.append" in lines[i + 1]
              and ":host" in lines[i + 1]]
    if len(anchor) != 1:
        raise SystemExit(2)
    i = anchor[0]
    out.append({"kind": "d-host", "line": i + 1, "fn": "check_receipts",
                "span": (starts[i], starts[i + 1] + len(lines[i + 1])), "repl": "",
                "legs": ["C1_RECEIPTS"],
                "desc": "host allowlist sub-check removed (MutationR96 d-host)"})
    all_legs = sorted({k for _, k in assigns}
                      | {k.value for pairs in dict_legs for k, _ in pairs})
    out.sort(key=lambda x: (x["line"], x["span"]))
    return out, [k for _, k in assigns], excluded, all_legs


def build(src, lane, new_legs):
    pinned = pin(src, lane)
    found, leg_names, excluded, all_legs = sites(pinned, new_legs)
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
    return pinned, mutants, leg_names, excluded, all_legs


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


def kill_tree(mdir, names, tree, env, jobs, extra_args):
    base = run(mdir / "unmutated.py", [*extra_args, "--tree", str(tree)], env, str(mdir))
    bvs = verdict_set(base["out"])

    def one(name):
        r = run(mdir / f"{name}.py", [*extra_args, "--tree", str(tree)], env, str(mdir))
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


def selftest(mdir, names, env, jobs, work_arg=None):
    # routed defect 5 fix: the label is `SELFTEST_C1V<n>=OK|FAIL legs=<n>` on v7/v8;
    # mutate7 required `=pass` and false-failed the baseline (see docstring).
    args = ["--self-test"] + (["--work", str(work_arg)] if work_arg is not None else [])
    base = run(mdir / "unmutated.py", args, env, str(mdir))
    base_label = next((ln for ln in base["out"].splitlines()
                       if ln.startswith("SELFTEST_C1V")), "-")
    if base["rc"] != 0 or not SELFTEST_PASS.search(base["out"]) \
            or SELFTEST_FAIL.search(base["out"]):
        raise SystemExit(3)

    def one(name):
        r = run(mdir / f"{name}.py", args, env, str(mdir))
        ok = ((not r["timeout"]) and r["rc"] == 0
              and bool(SELFTEST_PASS.search(r["out"]))
              and not SELFTEST_FAIL.search(r["out"]))
        fails = [ln for ln in r["out"].splitlines() if ln.startswith("SELFTEST FAIL:")]
        return {"name": name, "rc": r["rc"], "killed": not ok, "timeout": r["timeout"],
                "fail_lines": fails[:3]}

    with ThreadPoolExecutor(max_workers=jobs) as ex:
        results = list(ex.map(one, names))
    return {"base_rc": base["rc"], "base_label": base_label, "results": results}


def fail2(msg):
    print(msg, file=sys.stderr)
    raise SystemExit(2)


def all_legs_of(src, lane):
    return sites(pin(src, lane), [])[3]


def load_prereg(path, pinned, mutants, new_legs, all_legs):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    consts, legs = [], []
    for m in data.get("mutants", []):
        mid = m.get("id", "?")
        cls = m.get("class")
        if cls == "mut-const":
            f = m["find"]
            n = pinned.count(f)
            if n != 1:
                fail2(f"PREREG_FAIL {mid}: find-string occurs {n} times (need exactly 1)")
            consts.append({"id": mid, "find": f, "replace": m["replace"],
                           "legs": m.get("legs", []), "desc": m.get("desc", cls)})
        elif cls == "del-leg":
            if m["leg"] not in all_legs:
                fail2(f"PREREG_FAIL {mid}: leg {m['leg']} absent from counter")
            if not any(mu["kind"] == "del-leg" and m["leg"] in mu["legs"]
                       for mu in mutants):
                fail2(f"PREREG_FAIL {mid}: no del-leg site derived for {m['leg']}")
            legs.append(m["leg"])
        else:
            fail2(f"PREREG_FAIL {mid}: unknown class {cls!r}")
    unreg = [l for l in new_legs if l not in legs]
    if unreg:
        fail2("PREREG_FAIL derived new legs not registered: " + ",".join(unreg))
    return consts, legs, data.get("sha256_at_prereg")


def kill_by_class(results, kind_of):
    byc = {}
    for r in results:
        d = byc.setdefault(kind_of.get(r["name"], "?"), [0, 0])
        d[0] += 1 if r["killed"] else 0
        d[1] += 1
    return " ".join(f"{k}={v[0]}/{v[1]}" for k, v in sorted(byc.items())) or "none"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--counter", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--kill-tree")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--label")
    ap.add_argument("--profile", choices=["c02", "c14", "c14r99"], default="c02")
    ap.add_argument("--base-counter", default="reports/round-98/c1_k_admit_counter7.py")
    ap.add_argument("--prereg")
    a = ap.parse_args(argv)
    cpath = Path(a.counter)
    m = re.search(r"counter(\d+)", cpath.name)
    label = a.label or (f"V{m.group(1)}" if m else "VX")
    src = cpath.read_text(encoding="utf-8")
    out = Path(a.out)
    mdir = out / "mutants"
    mdir.mkdir(parents=True, exist_ok=True)
    base_info = None
    new_legs = list(V7_NEW_LEGS)
    if a.base_counter:
        bpath = Path(a.base_counter)
        if not bpath.is_absolute():
            bpath = LANE / bpath
        if not bpath.exists():
            fail2(f"BASE_COUNTER missing: {bpath}")
        bsrc = bpath.read_text(encoding="utf-8")
        base_info = {"path": str(bpath), "sha256": hashlib.sha256(
            bsrc.encode("utf-8")).hexdigest()}
        new_legs = sorted(set(all_legs_of(src, str(LANE)))
                          - set(all_legs_of(bsrc, str(LANE))))
    pinned, mutants, leg_names, excluded, all_legs = build(src, str(LANE), new_legs)
    prereg_consts, prereg_legs, prereg_sha = [], [], None
    prereg_path = Path(a.prereg) if a.prereg else None
    if prereg_path is not None:
        prereg_consts, prereg_legs, prereg_sha = load_prereg(
            prereg_path, pinned, mutants, new_legs, all_legs)
        for c in prereg_consts:
            text = pinned.replace(c["find"], c["replace"], 1)
            line = pinned[: pinned.index(c["find"])].count("\n") + 1
            mutants.append({"name": f"prereg-{c['id']}", "text": text,
                            "kind": "mut-const", "fn": "configure", "line": line,
                            "legs": c["legs"], "desc": c["desc"]})
    (mdir / "unmutated.py").write_text(pinned, encoding="utf-8")
    manifest = {"counter": str(cpath), "counter_sha256": hashlib.sha256(
        src.encode("utf-8")).hexdigest(), "lane_pin": str(LANE), "profile": a.profile,
        "new_legs": list(new_legs), "base_counter": base_info,
        "mutants": [], "excluded_msg": excluded}
    if prereg_path is not None:
        manifest["prereg"] = {"path": str(prereg_path), "sha256_at_prereg": prereg_sha,
                              "mut_const": [c["id"] for c in prereg_consts],
                              "del_legs": list(prereg_legs)}
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
    for leg in new_legs:
        d = sum(1 for mu in mutants if mu["kind"] == "del-leg" and leg in mu["legs"])
        w = sum(1 for mu in mutants if mu["kind"] == "widen-re" and leg in mu["legs"])
        y = sum(1 for mu in mutants if mu["kind"] == "drop-why" and leg in mu["legs"])
        if d == 0 and w == 0 and y == 0 and leg not in covered:
            print(f"NEWLEG {leg} absent-from-counter")
        else:
            print(f"NEWLEG {leg} del-leg={d} widen-re={w} drop-why={y}")
    print(f"EXCLUDED_MSG={len(excluded)} (WHY-text-only decisions; not leg sites): "
          + (",".join(f"L{x['line']}" for x in excluded) or "none"))
    print(f"MUTANTS_WRITTEN={len(mutants)} counter={cpath.name} label={label}")
    print(f"NEW_LEGS_DERIVED={','.join(new_legs) or 'none'}")
    if prereg_path is not None:
        print(f"PREREG_OK consts={len(prereg_consts)} del_legs={len(prereg_legs)} "
              f"file={prereg_path}")
    names = [mu["name"] for mu in mutants]
    kind_of = {mu["name"]: mu["kind"] for mu in mutants}
    env = dict(os.environ, PYTHONUTF8="1", HYAKU_SCRATCH=str(out / "hyaku"))
    (out / "hyaku").mkdir(parents=True, exist_ok=True)
    if a.kill_tree:
        tree = Path(a.kill_tree)
        supports_profile = ('"--profile"' in src) or ("'--profile'" in src)
        extra = ["--profile", a.profile] if supports_profile else []
        kt = kill_tree(mdir, names, tree, env, a.jobs, extra)
        for r in kt["results"]:
            print(f"KILL_TREE {r['name']} rc={r['rc']} killed={r['killed']} why={r['why']}"
                  f" diff={','.join(r['diff']) or '-'}")
        k = sum(1 for r in kt["results"] if r["killed"])
        print(f"BASE_TREE rc={kt['base_rc']} verdicts={len(kt['base_verdicts'])}")
        print(f"MUTANT_KILL_{label}={k}/{len(kt['results'])}")
        print("KILLBY_TREE " + kill_by_class(kt["results"], kind_of))
        print("SURVIVORS_TREE=" + (",".join(r["name"] for r in kt["results"] if not r["killed"])
                                   or "none"))
    if a.selftest:
        supports_work = ('"--work"' in src) or ("'--work'" in src)
        work_arg = None
        if supports_work:
            work_arg = out / "st"
            work_arg.mkdir(parents=True, exist_ok=True)
        st = selftest(mdir, names, env, a.jobs, work_arg)
        print(f"BASE_SELFTEST rc={st['base_rc']} label={st['base_label']}")
        for r in st["results"]:
            print(f"KILL_SELFTEST {r['name']} rc={r['rc']} killed={r['killed']} "
                  f"timeout={r['timeout']} first={' | '.join(r['fail_lines']) or '-'}")
        k = sum(1 for r in st["results"] if r["killed"])
        print(f"MUTANT_SELFTEST_{label}={k}/{len(st['results'])}")
        print("KILLBY_SELFTEST " + kill_by_class(st["results"], kind_of))
        print("SURVIVORS_SELFTEST=" + (",".join(r["name"] for r in st["results"]
                                                if not r["killed"]) or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
