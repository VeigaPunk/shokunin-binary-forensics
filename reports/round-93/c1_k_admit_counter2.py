#!/usr/bin/env python3
"""Round-93 C1 v2 frozen counter (coverage K): C08 admission, strict + provenance.

Successor of `reports/round-92/c1_k_admit_counter.py` (v1 bytes stay frozen at
commit 9402183a). Claim: coverage-map row C08 (browser/Electron runtime evidence)
moves `uncovered` -> `held` on the strength of ONE admitted knowledge entry
derived from the lane's saved round-77 CDP record, and K_HELD_BACKED moves
9/15 -> 10/15. The r92 critic's routed closes are frozen as legs here:

  C1_VOTES (strict)   every vote carries:
                      - seat in the wave registry (.ufo/waves/round-93/w1/swarm-registry.json)
                      - role reviewer|critic, distinct seats
                      - candidate_sha256 == digest of the entry bytes
                        (admission-status line normalised)
                      - decisions for Q01..Q17, each `PASS` or `n/a` WITH a
                        nonempty per-Q reason in `notes`; at least one PASS
                        (the all-`n/a` forgery class is dead)
                      - artifact_path naming a file that exists in the counted
                        tree under .ufo/waves/round-93/ and artifact_sha256
                        equal to its sha256 (the vote is bound to wave bytes)
  C1_SOURCES          every header S-id is a mined registry row, opened
                      2026-11-05 (this round), used-by naming the entry
  C1_QUOTES           every EXTERNAL (http) header row verifies through
                      corpus/audit_source_quotes.py verify over committed
                      fetch receipts (reports/round-93/quote-receipts/)
  C1_OPENS            reports/round-93/opens.json re-derives: the counter re-runs
                      the round-77 oracle over the archived record bytes (exit 0,
                      tail ORACLE OK (17/17 checks)), re-hashes the archived
                      record (frozen pin) and both fixture files, and compares
                      them with the receipt's committed values

Carried from v1 (unchanged semantics): C1_ROWS_TOTAL (15 rows x 5 cells),
C1_C08_HELD, C1_C08_CITES, C1_ADMITTED, C1_TRIO, C1_LINT, C1_EMBEDDED,
C1_K_HELD_BACKED == 10. New counter-level guard from the r92 critic finding 6:
C1_EMBED_NONVACUOUS (a fenced `$ command` block must embed >=1 output line).

Usage:
  c1_k_admit_counter2.py --rev REV     committed tree (archive of corpus, reports/round-93, .ufo/waves/round-93)
  c1_k_admit_counter2.py --tree DIR    directory holding those paths (controls, battery)
  c1_k_admit_counter2.py --self-test   isolated fixtures, no network, no live-tree write

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
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r93" / "c1v2"
ENTRY = "corpus/knowledge/round-93-browser-cdp-runtime-evidence.md"
ENTRY_REL = "knowledge/round-93-browser-cdp-runtime-evidence.md"
ROUND_DATE = "2026-11-05"
QS = [f"Q{i:02d}" for i in range(1, 18)]
RECORD_REL = "live/runs/round-77/inspection.json"
RECORD_SHA = "b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868"
ORACLE_TAIL = "ORACLE OK (17/17 checks)"
FIXTURE_SHAS = {
    "index.html": "46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45",
    "app.js": "fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593",
}
ARCHIVE_PATHS = ["corpus", "reports/round-93", ".ufo/waves/round-93"]


def digest(text):
    norm = re.sub(r"^admission-status: (candidate|admitted|rejected)$",
                  "admission-status: candidate", text, flags=re.M)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


class tar_extract:
    def __init__(self, data, dest):
        self.data, self.dest = data, dest

    def __enter__(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        subprocess.run(["tar", "-x", "-C", str(self.dest)], input=self.data, check=True)
        return self.dest

    def __exit__(self, *a):
        return False


def materialize(rev, tree, work):
    """Return the root dir holding corpus/, reports/round-93/, .ufo/waves/round-93/."""
    root = work / "t"
    root.mkdir()
    if rev:
        for rel in ARCHIVE_PATHS:
            exists = subprocess.run(["git", "-C", str(LANE), "cat-file", "-e",
                                     f"{rev}:{rel}"], capture_output=True).returncode == 0
            if not exists:
                continue
            ar = subprocess.run(["git", "-C", str(LANE), "archive", rev, rel],
                                capture_output=True)
            if ar.returncode != 0:
                return None, f"archive-failed {rel} {ar.stderr[:200]}"
            with tar_extract(ar.stdout, root):
                pass
        if not (root / "corpus").is_dir():
            return None, "archive-failed corpus"
        return root, None
    for rel in ARCHIVE_PATHS:
        src = tree / rel
        if src.is_dir():
            shutil.copytree(src, root / rel)
    return root, None


def parse_sources(root):
    rows = {}
    src = root / "corpus/SOURCES.md"
    if not src.is_file():
        return rows
    for ln in src.read_text(encoding="utf-8").splitlines():
        if re.match(r"^ {0,3}\|[ \t]*S[0-9]{3,}[ \t]*\|", ln):
            c = cells(ln)
            if len(c) == 11:
                rows[c[0]] = c
    return rows


def load_registry(root):
    p = root / ".ufo/waves/round-93/w1/swarm-registry.json"
    try:
        reg = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    m = reg.get("members") if isinstance(reg, dict) else None
    return set(m.keys()) if isinstance(m, dict) else None


def check_votes(root, want):
    votes_dir = root / "reports/round-93/votes"
    members = load_registry(root)
    good, seen = [], set()
    for vf in sorted(votes_dir.glob("*.json")) if votes_dir.is_dir() else []:
        try:
            v = json.loads(vf.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if not isinstance(v, dict):
            continue
        ds = v.get("decisions", {})
        notes = v.get("notes", {}) if isinstance(v.get("notes", {}), dict) else {}
        seat = v.get("seat")
        sha = v.get("artifact_sha256")
        apath = v.get("artifact_path")
        dec_ok = (isinstance(ds, dict) and set(ds) >= set(QS)
                  and all(ds[q] == "PASS" or (ds[q] == "n/a" and str(notes.get(q, "")).strip())
                          for q in QS)
                  and any(ds[q] == "PASS" for q in QS))
        art = root / apath if isinstance(apath, str) and apath else None
        art_ok = (art is not None and str(apath).startswith(".ufo/waves/round-93/")
                  and art.is_file()
                  and isinstance(sha, str)
                  and hashlib.sha256(art.read_bytes()).hexdigest() == sha)
        ok = (seat and seat not in seen
              and v.get("role") in ("reviewer", "critic")
              and v.get("candidate_sha256") == want
              and dec_ok and art_ok
              and members is not None and seat in members)
        if ok:
            seen.add(seat)
            good.append(seat)
    return good


def check_opens(root):
    p = root / "reports/round-93/opens.json"
    try:
        o = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False, "opens missing/unreadable"
    rec = root / "corpus" / RECORD_REL
    if not rec.is_file() or hashlib.sha256(rec.read_bytes()).hexdigest() != RECORD_SHA:
        return False, "record pin mismatch"
    if o.get("record_sha256") != RECORD_SHA:
        return False, "opens record_sha256 mismatch"
    if str(o.get("oracle_tail", "")).strip() != ORACLE_TAIL:
        return False, "opens oracle_tail mismatch"
    fx = o.get("fixture_shas", {})
    for name, want in FIXTURE_SHAS.items():
        f = root / "corpus/fixtures/browser-r77" / name
        if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest() != want:
            return False, f"fixture {name} missing or sha mismatch"
        if fx.get(name) != want:
            return False, f"opens fixture_shas[{name}] mismatch"
    r = run([sys.executable, "-B", "corpus/fixtures/browser-r77/oracle_check.py",
             "corpus/fixtures/browser-r77/truth.json", "corpus/" + RECORD_REL], str(root))
    tail = (r.stdout + r.stderr).strip().splitlines()
    if r.returncode != 0 or not tail or tail[-1].strip() != ORACLE_TAIL:
        return False, f"oracle rerun rc={r.returncode} tail={tail[-1] if tail else 'none'!r}"
    return True, "ok"


def check_quotes(root, sids):
    rows = parse_sources(root)
    ext = []
    for sid in sids:
        r = rows.get(sid)
        if r and "http" in r[1]:
            ext.append(sid)
    if not ext:
        return True, "no external header rows cited"
    fails = []
    for sid in ext:
        r = run([sys.executable, "-B", "corpus/audit_source_quotes.py", "verify",
                 "--sources", "corpus/SOURCES.md",
                 "--receipts", "reports/round-93/quote-receipts",
                 "--sid", sid], str(root))
        if r.returncode != 0:
            fails.append(f"{sid}:{(r.stdout + r.stderr).strip().splitlines()[-1][:80] if (r.stdout + r.stderr).strip() else 'no-output'}")
    return (not fails), ("ok" if not fails else "; ".join(fails))


def evaluate(root):
    legs = {}
    readme = (root / "corpus/README.md").read_text(encoding="utf-8").splitlines()
    cov = [cells(l) for l in readme if re.match(r"^\|[ \t]*C[0-9]+ ", l) and len(cells(l)) == 5]
    legs["C1_ROWS_TOTAL"] = len(cov) == 15
    c08 = next((r for r in cov if r[0] == "C08"), None)
    legs["C1_C08_HELD"] = bool(c08) and c08[4] == "held"
    legs["C1_C08_CITES"] = bool(c08) and ENTRY_REL in c08[2] and (root / ENTRY).is_file()

    text = (root / ENTRY).read_text(encoding="utf-8") if (root / ENTRY).is_file() else ""
    head = text.splitlines()[:15]
    legs["C1_ADMITTED"] = bool(re.search(r"^admission-status: admitted$", text, re.M))
    legs["C1_TRIO"] = all(any(l.startswith(k) for l in head) for k in ("source:", "verified-at:", "recheck:"))

    want = digest(text) if text else None
    votes_ok = check_votes(root, want)
    legs["C1_VOTES"] = len(votes_ok) >= 2

    if (root / ENTRY).is_file():
        lint = run([sys.executable, "-B", "corpus/lint_entry.py", "--entry", ENTRY, "--lane", str(LANE)], str(root))
        emb = run([sys.executable, "-B", "corpus/check_embedded_outputs.py", "--entry", ENTRY], str(root))
        legs["C1_LINT"] = lint.returncode == 0
        legs["C1_EMBEDDED"] = emb.returncode == 0
        # r92 critic finding 6 close (counter-level): a fenced block whose first
        # line is a `$ command` must carry at least one output line.
        vacuous = []
        for block in re.findall(r"```[^\n]*\n(.*?)```", text, re.S):
            lines = block.strip("\n").split("\n")
            if lines and lines[0].lstrip().startswith("$") and len(lines) < 2:
                vacuous.append(lines[0][:60])
        legs["C1_EMBED_NONVACUOUS"] = not vacuous
    else:
        legs["C1_LINT"] = legs["C1_EMBEDDED"] = legs["C1_EMBED_NONVACUOUS"] = False

    s_ids = sorted(set(re.findall(r"\bS\d{3,}\b", "\n".join(head))))
    rows = parse_sources(root)
    src_ok = bool(s_ids)
    for sid in s_ids:
        r = rows.get(sid)
        if not r or r[7] != "mined" or r[8] != ROUND_DATE or ENTRY not in r[10]:
            src_ok = False
    legs["C1_SOURCES"] = src_ok

    q_ok, q_reason = check_quotes(root, s_ids)
    legs["C1_QUOTES"] = q_ok
    o_ok, _ = check_opens(root)
    legs["C1_OPENS"] = o_ok

    held_backed = 0
    for r in cov:
        files = re.findall(r"knowledge/[\w.-]+\.md", r[2])
        if r[4] == "held" and files and all((root / "corpus" / f).is_file() for f in files):
            held_backed += 1
    legs["C1_K_HELD_BACKED"] = held_backed == 10

    print(f"C1_K_HELD_BACKED={held_backed}/{len(cov)}")
    print(f"C1_VOTE_SEATS={','.join(votes_ok) or 'none'} digest={want}")
    print(f"C1_SOURCE_IDS={','.join(s_ids) or 'none'} C1_QUOTES={'ok' if q_ok else q_reason}")
    for k, v in legs.items():
        print(f"{k}={'pass' if v else 'fail'}")
    ok = all(legs.values())
    print(f"C1_VERDICT={'pass' if ok else 'fail'}")
    return legs, ok


def _vote(seat, role, sha, ds, notes, apath, asha):
    return {"seat": seat, "role": role, "candidate_sha256": sha, "decisions": ds,
            "notes": notes, "artifact_path": apath, "artifact_sha256": asha}


def self_test():
    """Isolated fixtures only; asserts exit codes and stable finding ids."""
    work = Path(tempfile.mkdtemp(prefix="c1v2-selftest-", dir=str(SCRATCH)))
    fails = []
    try:
        root = work / "t"
        corpus = root / "corpus"
        for rel in ("knowledge", "live/runs/round-77", "fixtures/browser-r77"):
            (corpus / rel).mkdir(parents=True)
        (root / "reports/round-93/votes").mkdir(parents=True)
        (root / ".ufo/waves/round-93/w1").mkdir(parents=True)
        (root / "reports/round-93/quote-receipts").mkdir(parents=True)
        # corpus material
        for name, want in FIXTURE_SHAS.items():
            (corpus / "fixtures/browser-r77" / name).write_text(name + "-bytes\n")
        # the ORACLE leg needs the real record bytes; copy them read-only
        rec_bytes = (LANE / "corpus" / RECORD_REL).read_bytes()
        (corpus / RECORD_REL).write_bytes(rec_bytes)
        for orel in ("corpus/fixtures/browser-r77/oracle_check.py",
                     "corpus/fixtures/browser-r77/truth.json",
                     "corpus/fixtures/browser-r77/index.html",
                     "corpus/fixtures/browser-r77/app.js"):
            dst = root / orel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(LANE / orel, dst)
        (corpus / "knowledge/pe-resource-directory-layout.md").write_text("x\n")
        import tarfile, io
        ar = subprocess.run(["git", "-C", str(LANE), "archive",
                             "281a5bad66e844190a570cb35d257c6974749993", "corpus/README.md"],
                            capture_output=True, check=True)
        with tarfile.open(fileobj=io.BytesIO(ar.stdout)) as tf:
            base_readme = tf.extractfile("corpus/README.md").read().decode("utf-8")
        out_lines = []
        for ln in base_readme.splitlines():
            if re.match(r"^\|[ \t]*C08 ", ln):
                c = cells(ln)
                c[2] = "`" + ENTRY_REL + "`"
                c[4] = "held"
                ln = "| " + " | ".join(c) + " |"
            out_lines.append(ln)
            if ln.rstrip().endswith("| held |"):
                for p in re.findall(r"knowledge/[\w.-]+\.md", ln):
                    f = corpus / p
                    f.parent.mkdir(parents=True, exist_ok=True)
                    if not f.exists():
                        f.write_text("fixture stub\n")
        (corpus / "README.md").write_text("\n".join(out_lines) + "\n", encoding="utf-8")
        # entry with trio, admitted, header source rows
        header = (f"source: S495 — round-77 record (own-work, tier A, opened 2026-11-05)\n"
                  f"verified-at: 2026-11-05\nrecheck: oracle tail {ORACLE_TAIL}\n"
                  "coverage-map: C08\nadmission-status: admitted\n\n# Entry\n")
        (corpus / ENTRY_REL).write_text(header)
        # registry + wave artifacts
        art_rel = ".ufo/waves/round-93/w1/SeatA/evidence.md"
        art2_rel = ".ufo/waves/round-93/w1/SeatB/evidence.md"
        (root / art_rel).parent.mkdir(parents=True, exist_ok=True)
        (root / art2_rel).parent.mkdir(parents=True, exist_ok=True)
        (root / art_rel).write_text("seat A evidence\n")
        (root / art2_rel).write_text("seat B evidence\n")
        reg = {"members": {"SeatA": {"role": "reviewer"}, "SeatB": {"role": "critic"}}}
        (root / ".ufo/waves/round-93/w1/swarm-registry.json").write_text(json.dumps(reg))
        # opens receipt
        opens = {"record_sha256": RECORD_SHA, "oracle_tail": ORACLE_TAIL,
                 "fixture_shas": dict(FIXTURE_SHAS)}
        (root / "reports/round-93/opens.json").write_text(json.dumps(opens))
        # sources rows appended
        rows = [
            "| S495 | round-77 record corpus/live/runs/round-77 (own-work, tier A, opened 2026-11-05) | own-work | A | record identity | opened 2026-11-05 oracle 17/17 | The saved record's identity facts re-derive | mined | 2026-11-05 | 180d | " + ENTRY + " |",
        ]
        sources = root / "corpus/SOURCES.md"
        text = sources.read_text(encoding="utf-8") if sources.exists() else "# SOURCES\n## Registry\n"
        sources.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")
        # lint/embedded: run against a permissive stub? They are real lane tools;
        # the fixture entry is too thin for lint_entry -> provide minimal fake
        # tools on PATH? No: copy the real tools is out of scope; the self-test
        # asserts the vote/sources/opens legs, so neutralize lint/embedded by
        # planting minimal stand-ins inside the fixture corpus.
        (corpus / "lint_entry.py").write_text(
            "import sys\nsys.exit(0)\n")
        (corpus / "check_embedded_outputs.py").write_text(
            "import sys\nsys.exit(0)\n")
        text_entry = (corpus / ENTRY_REL).read_text(encoding="utf-8")
        want = digest(text_entry)

        def write_vote(name, v):
            (root / "reports/round-93/votes" / f"{name}.json").write_text(json.dumps(v))

        all_pass = {q: "PASS" for q in QS}
        good_a = _vote("SeatA", "reviewer", want, all_pass, {q: "clean" for q in QS},
                       art_rel, hashlib.sha256((root / art_rel).read_bytes()).hexdigest())
        good_b = _vote("SeatB", "critic", want, all_pass, {q: "clean" for q in QS},
                       art2_rel, hashlib.sha256((root / art2_rel).read_bytes()).hexdigest())
        write_vote("GoodA", good_a)
        write_vote("GoodB", good_b)
        legs, ok = evaluate(root)
        if not ok or not legs.get("C1_VOTES") or not legs.get("C1_SOURCES") or not legs.get("C1_OPENS"):
            fails.append("positive-fixture:" + ",".join(k for k, v in legs.items() if not v))

        def reset_votes():
            for f in (root / "reports/round-93/votes").glob("*.json"):
                f.unlink()

        # kill 1: seat not in the wave registry
        reset_votes()
        bad = dict(good_a); bad["seat"] = "FabricatedSeat"
        write_vote("BadReg", bad)
        write_vote("GoodB2", good_b)
        legs, ok = evaluate(root)
        if legs.get("C1_VOTES", True):
            fails.append("registry-kill")
        # kill 2: artifact sha mismatch
        reset_votes()
        bad = dict(good_a); bad["artifact_sha256"] = "0" * 64
        write_vote("BadSha", bad)
        write_vote("GoodB3", good_b)
        legs, ok = evaluate(root)
        if legs.get("C1_VOTES", True):
            fails.append("artifact-sha-kill")
        # kill 3: all-n/a decisions
        reset_votes()
        na = {q: "n/a" for q in QS}
        bad = _vote("SeatA", "reviewer", want, na, {q: "reason" for q in QS},
                    art_rel, hashlib.sha256((root / art_rel).read_bytes()).hexdigest())
        write_vote("AllNa", bad)
        write_vote("GoodB4", good_b)
        legs, ok = evaluate(root)
        if legs.get("C1_VOTES", True):
            fails.append("all-na-kill")
        # kill 4: n/a without a reason
        reset_votes()
        ds = {q: "PASS" for q in QS}; ds["Q17"] = "n/a"
        notes = {q: "clean" for q in QS}; notes["Q17"] = ""
        bad = _vote("SeatA", "reviewer", want, ds, notes,
                    art_rel, hashlib.sha256((root / art_rel).read_bytes()).hexdigest())
        write_vote("NaNoReason", bad)
        write_vote("GoodB5", good_b)
        legs, ok = evaluate(root)
        if legs.get("C1_VOTES", True):
            fails.append("na-reason-kill")
        print(f"SELFTEST_C1V2={'pass' if not fails else 'fail'} "
              f"kills=registry,artifact-sha,all-na,na-reason cases={';'.join(fails) or 'none'}")
        return 0 if not fails else 1
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
    work = Path(tempfile.mkdtemp(prefix="c1v2-", dir=str(SCRATCH)))
    try:
        root, err = materialize(rev, tree, work)
        if root is None:
            print(f"C1_VERDICT=fail reason={err}")
            return 1
        _, ok = evaluate(root)
        return 0 if ok else 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
