import difflib, hashlib, os, re, shutil, subprocess, sys
from pathlib import Path
S = Path("/fast/scratch/hyaku/revenger-r90/MutR90SM6")
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
SRC = LANE / "corpus/self_assessment_check2.py"
BAT = LANE / "reports/round-90/sm6_battery.py"
OUT = LANE / ".ufo/waves/round-90/w1/MutR90SM6"
TREE = S / "tree"
work = S / "check2.py"
pristine = SRC.read_bytes()
H0 = hashlib.sha256(pristine).hexdigest()

M = [
 ("M1_drop_denominator", "int(num) == held and int(den) == len(rows)", "int(num) == held"),
 ("M2_drop_numerator", "int(num) == held and int(den) == len(rows)", "int(den) == len(rows)"),
 ("M3_left_side", "num, den = (n1, d1) if n1 else (n0, d0)", "num, den = (n0, d0)"),
 ("M4_drop_paren_score", r'r"(?:\s*(?:\(\s*[0-9.]+\s*\))?\s*(?:→|->)\s*(\d+)/(\d+))?", head)', r'r"(?:\s*(?:→|->)\s*(\d+)/(\d+))?", head)'),
 ("M5_count_all_pipe_C_rows", r're.match(r"^\| C[0-9]+ ", l)', r're.match(r"^\| C", l)'),
 ("M6a_first_statement", "n0, d0, n1, d1 = stmts[-1]", "n0, d0, n1, d1 = stmts[0]"),
 ("M6b_first_K_line", 'head = last[-1].split("K_HELD_BACKED_STRICT")[0]', 'head = last[0].split("K_HELD_BACKED_STRICT")[0]'),
 ("M7_drop_STRICT_split", 'head = last[-1].split("K_HELD_BACKED_STRICT")[0]', 'head = last[-1]'),
 ("M8a_no_statement_returns_0", "    if not stmts:\n        return 1", "    if not stmts:\n        return 0"),
 ("M8b_no_K_line_returns_0", "    if not last:\n        return 1", "    if not last:\n        return 0"),
 ("M9_held_unanchored", r're.search(r"\|\s*held\s*\|\s*$", l)', r'"held" in l'),
]

env = dict(os.environ, TMPDIR=str(S), PYTHONDONTWRITEBYTECODE="1")
def run(impl):
    b = subprocess.run([sys.executable, "-B", str(BAT), "--impl", str(impl), "--real", str(TREE)], capture_output=True, text=True, env=env, cwd=S)
    t = subprocess.run([sys.executable, "-B", str(impl), "--self-test"], capture_output=True, text=True, env=env, cwd=S)
    return b, t

def summ(b, t):
    mis = re.search(r"SM6_MISCLASS=\S+", b.stdout)
    bad = [l.split()[1] for l in b.stdout.splitlines() if l.endswith("MISCLASS")]
    return (mis.group(0) if mis else "NO-OUTPUT") + f" exit={b.returncode}" + (f" [{','.join(bad)}]" if bad else ""), \
           f"exit={t.returncode} " + ((t.stdout.strip().splitlines() or [t.stderr.strip()[-200:]])[0][:160])

log = []
def leg(name, data):
    work.write_bytes(data)
    h = hashlib.sha256(work.read_bytes()).hexdigest()
    b, t = run(work)
    (OUT / f"{name}.battery.log").write_text(b.stdout + b.stderr)
    (OUT / f"{name}.selftest.log").write_text(t.stdout + t.stderr)
    return h, b, t

OUT.mkdir(parents=True, exist_ok=True)
h, b, t = leg("pristine", pristine)
log.append(("pristine", h, *summ(b, t)))
base_ok = b.returncode == 0 and t.returncode == 0
rows = []
for name, old, new in M:
    s = pristine.decode()
    assert s.count(old) == 1, (name, s.count(old))
    ms = s.replace(old, new)
    diff = "".join(difflib.unified_diff(s.splitlines(True), ms.splitlines(True), "a/corpus/self_assessment_check2.py", "b/corpus/self_assessment_check2.py"))
    (OUT / f"{name}.diff").write_text(diff)
    hm, b, t = leg(name, ms.encode())
    bs, ts = summ(b, t)
    bk, tk = b.returncode != 0, t.returncode != 0
    verdict = ("inconclusive" if not base_ok else "killed" if (bk or tk) else "SURVIVED")
    by = "+".join(x for x, k in (("battery", bk), ("selftest", tk)) if k) or "-"
    work.write_bytes(pristine)
    hr = hashlib.sha256(work.read_bytes()).hexdigest()
    rows.append((name, hm, bs, ts, verdict, by, hr == H0))
h, b, t = leg("restored", pristine)
log.append(("restored", h, *summ(b, t)))
src_after = hashlib.sha256(SRC.read_bytes()).hexdigest()
print("PRISTINE_SHA", H0, "SRC_AFTER", src_after)
for r in log: print("CTRL", *r, sep=" | ")
for r in rows: print("MUT", *r, sep=" | ")
