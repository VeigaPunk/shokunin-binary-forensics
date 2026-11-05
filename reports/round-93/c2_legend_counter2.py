#!/usr/bin/env python3
"""Round-93 C2 v2 frozen counter (calibration): legend token vs saved records.

Successor of `reports/round-92/c2_legend_counter.py` (v1 bytes stay frozen at
commit 9402183a). The r92 critic's routed closes are frozen as legs here:

  C2_C08_TOKEN   exact-token leg: row C08 carries status `held` and cites
                 knowledge/round-93-browser-cdp-runtime-evidence.md, which
                 exists (v1 accepted `partial`, `held`+seed.md, trailing cells)
  C2_C08_RECORD  the saved round-77 record exists in the counted tree and its
                 sha256 equals the frozen pin (v1 passed when it was deleted)
  C2_ROWS_TOTAL  the coverage map keeps 15 rows parsed as exactly 5 cells
                 (a trailing cell drops the row here; v1 still counted 15)
  C2_NO_NEW      the legend probe flags no row at all (only C08 may move)
  C2_NO_UNBACKED K_HELD == K_HELD_BACKED (no held token without its file)
  C2_ONLY_C08    no row other than C08 changed its status cell vs the frozen
                 base revision

Probe execution (finding-5 close): the frozen probe `reports/round-66/measure.py`
is NEVER taken from a mutable tree. It is extracted by `git archive` from the
frozen PROBE_REV bytes into the counter's scratch dir and run with
`python3 -I -B` (isolated: script dir is the scratch copy, so a planted
shadow module in any working tree cannot be imported). If the probe emits no
labels the verdict is fail (exit 1), never pass.

Usage:
  c2_legend_counter2.py --rev REV     committed tree (archive of corpus)
  c2_legend_counter2.py --tree DIR    directory holding corpus/ (controls, battery)
  c2_legend_counter2.py --self-test   isolated fixtures, no network, no live-tree write

Prints C2_* lines and C2_VERDICT=pass|fail; exit 0 iff pass, 1 otherwise, 64 usage.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r93" / "c2v2"
PROBE_REV = "281a5bad66e844190a570cb35d257c6974749993"  # freeze base; probe bytes frozen here
PROBE_ARCHIVE_PATH = "reports/round-66/measure.py"
ENTRY = "corpus/knowledge/round-93-browser-cdp-runtime-evidence.md"
ENTRY_REL = "knowledge/round-93-browser-cdp-runtime-evidence.md"
RECORD = "corpus/live/runs/round-77/inspection.json"
RECORD_REL = "live/runs/round-77/inspection.json"
RECORD_SHA = "b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868"


def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]


def parse_map(readme_path):
    rows = []
    for ln in readme_path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^(\|)[ \t]*C[0-9]+ ", ln):
            c = cells(ln)
            rows.append((c[0] if c else "?", c))
    return rows


def run_probe(corpus_dir, work):
    probe_dir = work / "probe"
    ar = subprocess.run(["git", "-C", str(LANE), "archive", PROBE_REV, PROBE_ARCHIVE_PATH],
                        capture_output=True)
    if ar.returncode != 0:
        return None, f"probe-archive-failed {ar.stderr.decode()[:120]}"
    with tar_extract(ar.stdout, probe_dir):
        pass
    probe = probe_dir / PROBE_ARCHIVE_PATH
    if not probe.is_file():
        return None, "probe-missing-after-extract"
    tmp = work / "probe-tmp"
    tmp.mkdir(exist_ok=True)
    # measure.py takes the PARENT of the corpus dir (it reads TREE/corpus/...).
    pr = subprocess.run([sys.executable, "-I", "-B", str(probe), str(corpus_dir.parent)],
                        cwd=str(work), env={**os.environ, "TMPDIR": str(tmp)},
                        capture_output=True, text=True)
    out = pr.stdout + pr.stderr
    m = re.search(r"README_TOKEN_LEGEND_MISMATCH=(\d+) rows=(\[.*?\])", out)
    kh = re.search(r"^K_HELD=(\d+)/(\d+)", out, re.M)
    khb = re.search(r"^K_HELD_BACKED=(\d+)/(\d+)", out, re.M)
    if not (m and kh and khb):
        return None, f"probe-labels-missing probe_exit={pr.returncode}"
    import ast
    return {
        "rows": ast.literal_eval(m.group(2)),
        "held": int(kh.group(1)), "held_n": int(kh.group(2)),
        "backed": int(khb.group(1)), "backed_n": int(khb.group(2)),
        "exit": pr.returncode,
    }, None


class tar_extract:
    def __init__(self, data, dest):
        self.data, self.dest = data, dest

    def __enter__(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        subprocess.run(["tar", "-x", "-C", str(self.dest)], input=self.data, check=True)
        return self.dest

    def __exit__(self, *a):
        return False


def extract_corpus(rev, tree, work):
    d = work / "corpus"
    if rev:
        ar = subprocess.run(["git", "-C", str(LANE), "archive", rev, "corpus"],
                            capture_output=True)
        if ar.returncode != 0:
            return None, f"archive-failed {ar.stderr.decode()[:200]}"
        with tar_extract(ar.stdout, work):
            pass
        return work / "corpus", None
    shutil.copytree(tree / "corpus", d)
    return d, None


def base_statuses(work):
    ar = subprocess.run(["git", "-C", str(LANE), "archive", PROBE_REV, "corpus/README.md"],
                        capture_output=True)
    if ar.returncode != 0:
        return None
    with tar_extract(ar.stdout, work / "base") as _:
        pass
    return {rid: (c[4] if len(c) == 5 else "?") for rid, c in parse_map(work / "base" / "corpus" / "README.md")}


def evaluate(corpus_dir, work):
    labels, err = run_probe(corpus_dir, work)
    if labels is None:
        print(f"C2_VERDICT=fail reason={err}")
        return {}, False
    rows = parse_map(corpus_dir / "README.md")
    five = {rid: c for rid, c in rows if len(c) == 5}
    legs = {}
    legs["C2_ROWS_TOTAL"] = len(five) == 15 and len(rows) == 15
    c08 = five.get("C08")
    entry_ok = bool(c08) and ENTRY_REL in c08[2] and (corpus_dir / ENTRY_REL).is_file()
    legs["C2_C08_TOKEN"] = bool(c08) and c08[4] == "held" and entry_ok
    rec = corpus_dir / RECORD_REL
    legs["C2_C08_RECORD"] = rec.is_file() and hashlib.sha256(rec.read_bytes()).hexdigest() == RECORD_SHA
    legs["C2_NO_NEW"] = labels["rows"] == []
    legs["C2_NO_UNBACKED"] = labels["held"] == labels["backed"]
    base = base_statuses(work)
    if base is None:
        legs["C2_ONLY_C08"] = False
    else:
        moved = {rid for rid in base if (five.get(rid, ["", "", "", "", "?"]))[4] != base[rid]}
        legs["C2_ONLY_C08"] = moved <= {"C08"}
    print(f"C2_PROBE_EXIT={labels['exit']} (probe exit is not the claim verdict)")
    print(f"C2_LEGEND_MISMATCH={len(labels['rows'])} rows={labels['rows']}")
    print(f"C2_ROWS_FIVE_CELL={len(five)}/{len(rows)}")
    print(f"C2_K_HELD={labels['held']}/{labels['held_n']} C2_K_HELD_BACKED={labels['backed']}/{labels['backed_n']}")
    print(f"C2_C08_TOKEN={'pass' if legs['C2_C08_TOKEN'] else 'fail'} C2_C08_RECORD={'pass' if legs['C2_C08_RECORD'] else 'fail'}")
    ok = all(legs.values())
    for k, v in legs.items():
        print(f"{k}={'pass' if v else 'fail'}")
    print(f"C2_VERDICT={'pass' if ok else 'fail'}")
    return legs, ok


def self_test():
    """Isolated fixtures only; asserts exit codes and stable finding ids."""
    work = Path(tempfile.mkdtemp(prefix="c2v2-selftest-", dir=str(SCRATCH)))
    fails = []
    try:
        corpus = work / "corpus"
        rec_rel = RECORD_REL
        (corpus / "live/runs/round-77").mkdir(parents=True)
        rec_bytes = (LANE / RECORD).read_bytes()
        (corpus / rec_rel).write_bytes(rec_bytes)
        (corpus / ENTRY_REL).parent.mkdir(parents=True, exist_ok=True)
        (corpus / ENTRY_REL).write_text("stub entry for self-test\n")
        # start from the REAL base README and apply exactly the intended move:
        # C08 -> held citing the entry. Then back every held row's cited files so
        # NO_UNBACKED holds, isolating the legs under test.
        import tarfile, io
        ar = subprocess.run(["git", "-C", str(LANE), "archive", PROBE_REV, "corpus/README.md"],
                            capture_output=True, check=True)
        with tarfile.open(fileobj=io.BytesIO(ar.stdout)) as tf:
            base_readme = tf.extractfile("corpus/README.md").read().decode("utf-8")
        out_lines = []
        for ln in base_readme.splitlines():
            if re.match(r"^\|[ \t]*C08 ", ln):
                c = cells(ln)
                assert len(c) == 5, "base C08 row shape changed; counter fixture needs an update"
                c[2] = "`" + ENTRY_REL + "`"
                c[4] = "held"
                ln = "| " + " | ".join(c) + " |"
            out_lines.append(ln)
            m = re.match(r"^\|[ \t]*(C[0-9]+) ", ln)
            if m and ln.rstrip().endswith("| held |"):
                for p in re.findall(r"knowledge/[\w.-]+\.md", ln):
                    f = corpus / p
                    f.parent.mkdir(parents=True, exist_ok=True)
                    f.write_text("fixture stub\n")
        (corpus / "README.md").write_text("\n".join(out_lines) + "\n", encoding="utf-8")
        legs, ok = evaluate(corpus, work)
        if not legs.get("C2_C08_TOKEN") or not legs.get("C2_C08_RECORD") or not ok:
            fails.append("positive-fixture")
        # mutate the record -> C2_C08_RECORD must fail
        (corpus / rec_rel).write_bytes(rec_bytes[:-1] + b"x")
        legs2, ok2 = evaluate(corpus, work)
        if legs2.get("C2_C08_RECORD", True) or ok2:
            fails.append("record-sha-kill")
        # trailing-cell forgery -> ROWS_TOTAL must fail
        (corpus / rec_rel).write_bytes(rec_bytes)
        lines = (corpus / "README.md").read_text(encoding="utf-8").splitlines()
        for i, ln in enumerate(lines):
            if ln.startswith("| C08 "):
                lines[i] = ln + " extra |"
        (corpus / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        legs3, ok3 = evaluate(corpus, work)
        if legs3.get("C2_ROWS_TOTAL", True) or ok3:
            fails.append("trailing-cell-kill")
        print(f"SELFTEST_C2V2={'pass' if not fails else 'fail'} kills={'record-sha,trailing-cell'} cases={len(fails)}open")
        return (0 if not fails else 1)
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main(argv):
    if "--self-test" in argv:
        SCRATCH.mkdir(parents=True, exist_ok=True)
        return self_test()
    rev = tree = None
    i = 0
    while i < len(argv):
        if argv[i] == "--rev":
            rev = argv[i + 1]; i += 2
        elif argv[i] == "--tree":
            tree = Path(argv[i + 1]); i += 2
        else:
            print(__doc__, file=sys.stderr); return 64
    if bool(rev) == bool(tree):
        print(__doc__, file=sys.stderr); return 64
    SCRATCH.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="c2v2-", dir=str(SCRATCH)))
    try:
        corpus_dir, err = extract_corpus(rev, tree, work)
        if corpus_dir is None:
            print(f"C2_VERDICT=fail reason={err}")
            return 1
        _, ok = evaluate(corpus_dir, work)
        return 0 if ok else 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
