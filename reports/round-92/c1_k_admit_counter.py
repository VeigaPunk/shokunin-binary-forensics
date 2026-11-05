#!/usr/bin/env python3
"""Round-92 C1 frozen counter (coverage K): C03 admission, strict.

Claim: coverage-map row C03 (managed (.NET/CLI) assemblies) moves frontier -> held
on the strength of ONE admitted knowledge entry, and K_HELD_BACKED moves 8/15 -> 9/15.
The legacy counter (reports/round-73/measure.py logic, reproduced below) only checks
that a held row's knowledge file exists, which a stub satisfies. This counter adds
the admission legs a stub cannot satisfy:

  C1_ROWS_TOTAL   coverage map keeps 15 rows
  C1_C03_HELD     row C03 status is `held`
  C1_C03_CITES    row C03 cites knowledge/round-92-managed-assembly-metadata-evidence.md and it exists
  C1_ADMITTED     the entry carries `admission-status: admitted`
  C1_TRIO         `source:`, `verified-at:`, `recheck:` appear in the first 15 lines
  C1_VOTES        >=2 vote files in reports/round-92/votes/ from DISTINCT seats, role reviewer|critic,
                  candidate_sha256 == sha256 of the entry with its admission-status line normalised,
                  decisions for Q01..Q17 each PASS or n/a
  C1_LINT         corpus/lint_entry.py --entry <entry> exits 0
  C1_EMBEDDED     corpus/check_embedded_outputs.py --entry <entry> exits 0
  C1_SOURCES      every S### id in the entry header is a SOURCES row with status mined,
                  used-by naming the entry, and opened 2026-11-05 (opened this round)
  C1_K_HELD_BACKED  held rows whose knowledge file exists == 9 (legacy measure, target 9/15)

Usage:
  c1_k_admit_counter.py --rev REV     committed tree (git archive of corpus/ + reports/round-92/)
  c1_k_admit_counter.py --tree DIR    directory holding corpus/ and reports/round-92/ (controls)
Exit 0 iff C1_VERDICT=pass; 1 otherwise; 64 usage.
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
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r92" / "c1"
ENTRY = "corpus/knowledge/round-92-managed-assembly-metadata-evidence.md"
ROUND_DATE = "2026-11-05"
QS = [f"Q{i:02d}" for i in range(1, 18)]


def digest(text):
    norm = re.sub(r"^admission-status: (candidate|admitted|rejected)$",
                  "admission-status: candidate", text, flags=re.M)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def main(argv):
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
    d = Path(tempfile.mkdtemp(prefix="c1-", dir=str(SCRATCH)))
    try:
        if rev:
            ar = subprocess.run(["git", "-C", str(LANE), "archive", rev, "corpus", "reports/round-92"],
                                capture_output=True)
            if ar.returncode != 0:
                print("C1_VERDICT=fail reason=archive-failed")
                return 1
            subprocess.run(["tar", "-x", "-C", str(d)], input=ar.stdout, check=True)
        else:
            shutil.copytree(tree / "corpus", d / "corpus")
            if (tree / "reports/round-92").is_dir():
                shutil.copytree(tree / "reports/round-92", d / "reports/round-92")

        legs = {}
        readme = (d / "corpus/README.md").read_text(encoding="utf-8").splitlines()
        cov = [cells(l) for l in readme if re.match(r"^\| C[0-9]+ ", l) and len(cells(l)) == 5]
        legs["C1_ROWS_TOTAL"] = len(cov) == 15
        c03 = next((r for r in cov if r[0] == "C03"), None)
        legs["C1_C03_HELD"] = bool(c03) and c03[4] == "held"
        legs["C1_C03_CITES"] = bool(c03) and ENTRY.removeprefix("corpus/") in c03[2] and (d / ENTRY).is_file()

        text = (d / ENTRY).read_text(encoding="utf-8") if (d / ENTRY).is_file() else ""
        head = text.splitlines()[:15]
        legs["C1_ADMITTED"] = bool(re.search(r"^admission-status: admitted$", text, re.M))
        legs["C1_TRIO"] = all(any(l.startswith(k) for l in head) for k in ("source:", "verified-at:", "recheck:"))

        want = digest(text) if text else None
        votes_ok = []
        seen = set()
        for vf in sorted((d / "reports/round-92/votes").glob("*.json")) if (d / "reports/round-92/votes").is_dir() else []:
            try:
                v = json.loads(vf.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                continue
            ds = v.get("decisions", {}) if isinstance(v, dict) else {}
            good = (isinstance(v, dict) and v.get("seat") and v["seat"] not in seen
                    and v.get("role") in ("reviewer", "critic")
                    and v.get("candidate_sha256") == want
                    and set(ds) >= set(QS)
                    and all(ds[q] in ("PASS", "n/a") for q in QS))
            if good:
                seen.add(v["seat"])
                votes_ok.append(v["seat"])
        legs["C1_VOTES"] = len(votes_ok) >= 2

        if (d / ENTRY).is_file():
            lint = run([sys.executable, "-B", "corpus/lint_entry.py", "--entry", ENTRY, "--lane", str(LANE)], d)
            emb = run([sys.executable, "-B", "corpus/check_embedded_outputs.py", "--entry", ENTRY], d)
            legs["C1_LINT"] = lint.returncode == 0
            legs["C1_EMBEDDED"] = emb.returncode == 0
        else:
            legs["C1_LINT"] = legs["C1_EMBEDDED"] = False

        s_ids = sorted(set(re.findall(r"\bS\d{3,}\b", "\n".join(head))))
        rows = {}
        for ln in (d / "corpus/SOURCES.md").read_text(encoding="utf-8").splitlines():
            if re.match(r"^ {0,3}\|[ \t]*S[0-9]{3,}[ \t]*\|", ln):
                c = cells(ln)
                if len(c) == 11:
                    rows[c[0]] = c
        src_ok = bool(s_ids)
        for sid in s_ids:
            r = rows.get(sid)
            if not r or r[7] != "mined" or r[8] != ROUND_DATE or ENTRY not in r[10]:
                src_ok = False
        legs["C1_SOURCES"] = src_ok

        held_backed = 0
        for r in cov:
            files = re.findall(r"knowledge/[\w.-]+\.md", r[2])
            if r[4] == "held" and files and all((d / "corpus" / f).is_file() for f in files):
                held_backed += 1
        legs["C1_K_HELD_BACKED"] = held_backed == 9

        print(f"C1_K_HELD_BACKED={held_backed}/{len(cov)}")
        print(f"C1_VOTE_SEATS={','.join(votes_ok) or 'none'} digest={want}")
        print(f"C1_SOURCE_IDS={','.join(s_ids) or 'none'}")
        for k, v in legs.items():
            print(f"{k}={'pass' if v else 'fail'}")
        ok = all(legs.values())
        print(f"C1_VERDICT={'pass' if ok else 'fail'}")
        return 0 if ok else 1
    finally:
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
