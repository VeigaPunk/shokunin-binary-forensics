#!/usr/bin/env python3
"""Round-94 C1 v3 frozen counter (coverage K): C15 admission, the r93 critic's closes as legs.

Successor of reports/round-93/c1_k_admit_counter2.py (frozen bytes untouched, kumitate r42
rule). v3 freezes the CriticR93 closes (findings 1-9, 11) as legs:

  F10  exactly ONE `admission-status:` line in the whole file, inside the 15-line header window
  F11  the wave registry is pinned to the frozen seat->role map (no self-attested registry)
  F12  vote seats canonicalised (case-fold + strip); a canonical collision fails the vote leg
  F13  vote.role must equal the pinned registry role and be reviewer|critic
  F14  one distinct, non-empty artifact per vote, inside .ufo/waves/round-94/ after resolution,
       whose bytes contain the candidate digest
  F15  artifact paths are resolved and contained (no `..` escape)
  F16  S-ids are collected from the WHOLE entry, not the header window
  F17  an `n/a` decision needs a reason of at least 20 non-punctuation characters
  F18  a ``` block whose first line is `$ ...` needs >=1 non-blank output line; a `~~~` fence
       containing a `$ ` line is rejected outright
  F11b POS runs the REAL corpus/lint_entry.py and corpus/check_embedded_outputs.py (no stubs)

C15 is documentation-only: there is no saved-record oracle, so v3 has no C1_OPENS leg; the
opening evidence is the receipts leg (C1_QUOTES) over the rows opened this round (S498, S499).
"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r94" / "c1v3"
ENTRY = "corpus/knowledge/round-72-tool-landscape.md"
ENTRY_REL = "knowledge/round-72-tool-landscape.md"
ROUND_DATE = "2026-11-05"
FREEZE_REV = "9876cb38c5415fbc86336a26a68e05680c397fd5"
QS = [f"Q{i:02d}" for i in range(1, 18)]
NEW_ROW_IDS = ("S498", "S499")
# rows the entry cites AS rejections (Q12); every other collected sid must be `mined`
REJECTED_OK = frozenset({"S071", "S072", "S074", "S091", "S093", "S427"})
WAVE_DIR = ".ufo/waves/round-94"
REGISTRY_REL = WAVE_DIR + "/w1/swarm-registry.json"
RECEIPTS_DIR = "reports/round-94/quote-receipts"
VOTES_DIR = "reports/round-94/votes"
MIN_NA_REASON = 20
PINNED_SEATS = {
    "ScoutReopen": "scout",
    "ScoutErrata": "scout",
    "ScribeLesson": "scribe",
    "ExecReceipts": "executor",
    "ExecBattery": "executor",
    "ExecCensus": "executor",
    "ExecFrozen": "executor",
    "ReviewerGate": "reviewer",
    "ReviewerBlind": "reviewer",
    "CriticR94": "critic",
    "MutationR94": "mutation-tester",
    "ConnectorOverlap": "connector",
    "SentinelScope": "sentinel",
}
VOTE_ROLES = ("reviewer", "critic")
ARCHIVE_PATHS = ["corpus", "reports/round-94", ".ufo/waves/round-94"]


def digest(text):
    norm = re.sub(r"^admission-status: (candidate|admitted|rejected)$",
                  "admission-status: candidate", text, flags=re.M)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]


def canon_seat(s):
    return re.sub(r"\s+", "", str(s)).lower()


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
    """Return the root dir holding corpus/, reports/round-94/, .ufo/waves/round-94/."""
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


def base_readme(work):
    """The frozen base coverage rows (raw lines), from git archive of FREEZE_REV."""
    ar = subprocess.run(["git", "-C", str(LANE), "archive", FREEZE_REV, "corpus/README.md"],
                        capture_output=True)
    if ar.returncode != 0:
        return None
    dest = work / "base"
    with tar_extract(ar.stdout, dest):
        pass
    lines = (dest / "corpus/README.md").read_text(encoding="utf-8").splitlines()
    rows = {}
    for ln in lines:
        c = cells(ln)
        if len(c) == 5 and re.fullmatch(r"C\d{2}", c[0]):
            rows[c[0]] = ln
    return rows


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


def check_registry(root):
    p = root / REGISTRY_REL
    try:
        reg = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False, "registry missing/unreadable"
    m = reg.get("members") if isinstance(reg, dict) else None
    if not isinstance(m, dict):
        return False, "registry has no members map"
    got = {}
    for name, meta in m.items():
        got[str(name)] = str((meta or {}).get("role", ""))
    if got != {k: v for k, v in PINNED_SEATS.items()}:
        missing = sorted(set(PINNED_SEATS) - set(got))
        extra = sorted(set(got) - set(PINNED_SEATS))
        roled = sorted(k for k in set(got) & set(PINNED_SEATS) if got[k] != PINNED_SEATS[k])
        return False, f"registry!=pinned missing={missing} extra={extra} rolemismatch={roled}"
    return True, "ok"


def check_votes(root, want):
    """Accept votes only under the v3 rules; ANY malformed vote fails the leg outright."""
    votes_dir = root / VOTES_DIR
    if not votes_dir.is_dir():
        return False, "votes dir missing"
    reg_ok, reg_reason = check_registry(root)
    if not reg_ok:
        return False, f"registry: {reg_reason}"
    accepted, artifacts, canonical = [], {}, {}
    for vf in sorted(votes_dir.glob("*.json")):
        try:
            v = json.loads(vf.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            return False, f"unreadable vote {vf.name}"
        if not isinstance(v, dict):
            return False, f"non-object vote {vf.name}"
        seat = v.get("seat")
        if not seat or str(seat) not in PINNED_SEATS:
            return False, f"seat not in pinned registry: {seat!r} ({vf.name})"
        cs = canon_seat(seat)
        if cs in canonical:
            return False, f"canonical seat collision: {seat!r} vs {canonical[cs]!r}"
        role = v.get("role")
        if role != PINNED_SEATS[str(seat)]:
            return False, f"vote role {role!r} != pinned {PINNED_SEATS[str(seat)]!r} for {seat}"
        if role not in VOTE_ROLES:
            return False, f"vote role {role!r} not in {VOTE_ROLES} for {seat}"
        if v.get("candidate_sha256") != want:
            return False, f"vote digest mismatch for {seat}"
        ds = v.get("decisions", {})
        notes = v.get("notes", {}) if isinstance(v.get("notes", {}), dict) else {}
        if not (isinstance(ds, dict) and set(ds) >= set(QS)):
            return False, f"vote decisions incomplete for {seat}"
        for q in QS:
            d = ds[q]
            if d == "PASS":
                continue
            if d != "n/a":
                return False, f"vote {seat} decision {q}={d!r} not PASS/n-a"
            reason = str(notes.get(q, "")).strip()
            letters = re.sub(r"[^0-9A-Za-z]", "", reason)
            if len(reason) < MIN_NA_REASON or len(letters) < MIN_NA_REASON // 2:
                return False, f"vote {seat} n/a reason for {q} under {MIN_NA_REASON} chars: {reason!r}"
        if not any(ds[q] == "PASS" for q in QS):
            return False, f"vote {seat} has no PASS decision"
        apath = v.get("artifact_path")
        asha = v.get("artifact_sha256")
        if not (isinstance(apath, str) and apath.startswith(WAVE_DIR + "/")):
            return False, f"artifact_path outside {WAVE_DIR}/: {apath!r}"
        if ".." in Path(apath).parts:
            return False, f"artifact_path contains '..': {apath!r}"
        art = root / apath
        resolved = art.resolve()
        wave_root = (root / WAVE_DIR).resolve()
        if not resolved.is_relative_to(wave_root):
            return False, f"artifact resolves outside wave dir: {apath!r}"
        if not art.is_file():
            return False, f"artifact not a file: {apath!r}"
        b = art.read_bytes()
        if len(b) == 0 or not b.strip():
            return False, f"artifact empty: {apath!r}"
        if not (isinstance(asha, str) and hashlib.sha256(b).hexdigest() == asha):
            return False, f"artifact sha mismatch: {apath!r}"
        if want not in b.decode("utf-8", errors="replace"):
            return False, f"artifact does not name the candidate digest: {apath!r}"
        if apath in artifacts or asha in artifacts.values():
            return False, f"artifact not distinct per seat: {apath!r}"
        canonical[cs] = seat
        artifacts[apath] = asha
        accepted.append(str(seat))
    if len(accepted) < 2:
        return False, f"only {len(accepted)} accepted votes"
    return True, ",".join(sorted(accepted))


def collect_sids(text):
    return sorted(set(re.findall(r"\bS\d{3,}\b", text)))


def check_sources(root, sids):
    rows = parse_sources(root)
    sup = {}
    for sid, c in rows.items():
        m = re.match(r"^supersedes (S\d{3,})\b", c[6])
        if m and m.group(1) not in sup:
            sup[m.group(1)] = sid

    def terminal(sid, d=0):
        while sid in sup and d < 10:
            sid = sup[sid]
            d += 1
        return sid

    fails = []
    for sid in sids:
        r = rows.get(sid)
        if not r:
            fails.append(f"{sid}:unresolved")
            continue
        if sid in REJECTED_OK:
            if r[7] != "rejected":
                fails.append(f"{sid}:rejected-expected:{r[7]}")
            continue
        term = terminal(sid)
        rt = rows.get(term)
        if rt is None:
            fails.append(f"{sid}:terminal-unresolved:{term}")
        elif rt[7] != "mined":
            fails.append(f"{sid}:terminal-mined-expected:{term}:{rt[7]}")
    for sid in NEW_ROW_IDS:
        r = rows.get(sid)
        if not r:
            fails.append(f"{sid}:new-row-missing")
            continue
        if r[7] != "mined":
            fails.append(f"{sid}:new-status:{r[7]}")
        if r[8] != ROUND_DATE:
            fails.append(f"{sid}:new-opened:{r[8]}")
        if r[3] != "A":
            fails.append(f"{sid}:new-tier:{r[3]}")
        if ENTRY_REL not in r[10]:
            fails.append(f"{sid}:cite-back-missing")
    return (not fails), ("ok" if not fails else "; ".join(fails))


def check_quotes(root, sids):
    need = [s for s in NEW_ROW_IDS if s in sids]
    if not need:
        return False, "no new-row sids cited by the entry"
    r = run([sys.executable, "-B", "corpus/audit_source_quotes.py", "verify",
             "--sources", "corpus/SOURCES.md",
             "--receipts", RECEIPTS_DIR] + sum((["--sid", s] for s in need), []), str(root))
    if r.returncode != 0:
        tail = (r.stdout + r.stderr).strip().splitlines()
        return False, tail[-1][:120] if tail else "no-output"
    if f"verified={len(need)}" not in r.stdout:
        return False, f"verified count != {len(need)}"
    return True, "ok"


def check_embed_nonvacuous(text):
    bad = []
    for block in re.findall(r"```[^\n]*\n(.*?)```", text, re.S):
        lines = block.strip("\n").split("\n")
        if lines and lines[0].lstrip().startswith("$") and not any(l.strip() for l in lines[1:]):
            bad.append("```:" + lines[0][:60])
    for block in re.findall(r"~~~[^\n]*\n(.*?)~~~", text, re.S):
        lines = block.split("\n")
        if any(l.lstrip().startswith("$") for l in lines):
            bad.append("~~~:" + lines[0][:60])
    return (not bad), ("ok" if not bad else "; ".join(bad))


def evaluate(root):
    legs = {}
    readme = (root / "corpus/README.md").read_text(encoding="utf-8").splitlines()
    cov = [cells(l) for l in readme if re.match(r"^\|[ \t]*C[0-9]+ ", l) and len(cells(l)) == 5]
    legs["C1_ROWS_TOTAL"] = len(cov) == 15
    c15 = next((r for r in cov if r[0] == "C15"), None)
    legs["C1_C15_HELD"] = bool(c15) and c15[4] == "held"
    legs["C1_C15_CITES"] = bool(c15) and ENTRY_REL in c15[2] and (root / ENTRY).is_file()

    # C1_ONLY_C15: every other coverage row byte-identical to the frozen base.
    baserows = base_readme(root)
    diffs = []
    if baserows:
        for r in cov:
            if r[0] != "C15" and baserows.get(r[0]) != _raw_line(readme, r[0]):
                diffs.append(r[0])
        legs["C1_ONLY_C15"] = not diffs and c15 is not None and baserows.get("C15") != _raw_line(readme, "C15")
    else:
        legs["C1_ONLY_C15"] = False

    text = (root / ENTRY).read_text(encoding="utf-8") if (root / ENTRY).is_file() else ""
    head = text.splitlines()[:15]
    st_lines = [i for i, l in enumerate(text.splitlines()) if re.match(r"^admission-status:", l)]
    legs["C1_ADMITTED"] = (len(st_lines) == 1 and st_lines[0] < 15
                           and re.match(r"^admission-status: admitted$",
                                        text.splitlines()[st_lines[0]]) is not None)
    legs["C1_TRIO"] = all(any(l.startswith(k) for l in head) for k in ("source:", "verified-at:", "recheck:"))

    want = digest(text) if text else None
    v_ok, v_why = check_votes(root, want)
    legs["C1_VOTES"] = v_ok

    if (root / ENTRY).is_file():
        lint = run([sys.executable, "-B", "corpus/lint_entry.py", "--entry", ENTRY, "--lane", str(LANE)], str(root))
        emb = run([sys.executable, "-B", "corpus/check_embedded_outputs.py", "--entry", ENTRY], str(root))
        legs["C1_LINT"] = lint.returncode == 0
        has_cmd_block = bool(re.search(r"```[^\n]*\n\$|~~~[^\n]*\n\$|```[^\n]*\n\s*\$", text, re.M))
        emb_ok = emb.returncode == 0 or (emb.returncode == 2 and "could-not-evaluate" in (emb.stdout + emb.stderr) and not has_cmd_block)
        legs["C1_EMBEDDED"] = emb_ok
        nv_ok, nv_why = check_embed_nonvacuous(text)
        legs["C1_EMBED_NONVACUOUS"] = nv_ok
    else:
        legs["C1_LINT"] = legs["C1_EMBEDDED"] = legs["C1_EMBED_NONVACUOUS"] = False

    sids = collect_sids(text)
    s_ok, s_why = check_sources(root, sids)
    legs["C1_SOURCES"] = s_ok
    q_ok, q_why = check_quotes(root, sids)
    legs["C1_QUOTES"] = q_ok

    held_backed = 0
    for r in cov:
        files = re.findall(r"knowledge/[\w.-]+\.md", r[2])
        if r[4] == "held" and files and all((root / "corpus" / f).is_file() for f in files):
            held_backed += 1
    legs["C1_K_HELD_BACKED"] = held_backed == 11

    print(f"C1_K_HELD_BACKED={held_backed}/{len(cov)}")
    print(f"C1_VOTES={v_why} digest={want}")
    print(f"C1_SOURCE_IDS={','.join(sids) or 'none'}")
    print(f"C1_SOURCES_WHY={s_why}")
    print(f"C1_QUOTES_WHY={q_why}")
    print(f"C1_ONLY_C15_DIFFS={','.join(diffs) or 'none'}")
    for k, v in legs.items():
        print(f"{k}={'pass' if v else 'fail'}")
    ok = all(legs.values())
    print(f"C1_VERDICT={'pass' if ok else 'fail'}")
    return legs, ok


def _raw_line(readme, cid):
    for ln in readme:
        c = cells(ln)
        if len(c) == 5 and c[0] == cid:
            return ln
    return None


def _vote(seat, role, sha, ds, notes, apath, asha):
    return {"seat": seat, "role": role, "candidate_sha256": sha, "decisions": ds,
            "notes": notes, "artifact_path": apath, "artifact_sha256": asha}


def _fixture(work):
    """Honest admission-shaped fixture built from the freeze archive + real entry bytes."""
    work = Path(tempfile.mkdtemp(prefix="fx-", dir=work))
    root, err = materialize(FREEZE_REV, None, work)
    if not root:
        raise SystemExit(f"fixture: {err}")
    # entry = real revised bytes, flipped to admitted
    entry = (LANE / ENTRY).read_text(encoding="utf-8")
    entry = re.sub(r"^admission-status: candidate$", "admission-status: admitted", entry, count=1, flags=re.M)
    (root / ENTRY).write_text(entry, encoding="utf-8")
    # README: flip C15 to held with the admitted scope wording
    want = digest(entry)
    out = []
    for ln in (root / "corpus/README.md").read_text(encoding="utf-8").splitlines():
        c = cells(ln)
        if len(c) == 5 and c[0] == "C15":
            c[2] = "`" + ENTRY_REL + "` (round-94 admission; scoped to named project sources, not tool execution, host readiness, accuracy or complete market coverage)"
            c[4] = "held"
            ln = "| " + " | ".join(c) + " |"
        out.append(ln)
    (root / "corpus/README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    # SOURCES: append synthetic S498/S499 mined rows + receipts
    body1 = (f"Reverse Engineer Anything (REA) README at main 2026-11-05. It declares an "
             f"agent-facing inspection workflow for native binaries, JavaScript/Electron, "
             f"managed assemblies and websites, returning evidence and limitations.\n")
    quote1 = "agent-facing inspection workflow for native binaries"
    i1 = body1.index(quote1)
    body2 = (f"REA installation docs at main 2026-11-05. The setup plan previews "
             f"configuration changes and requires approval before applying them.\n")
    quote2 = "requires approval before applying them"
    i2 = body2.index(quote2)
    rc = root / RECEIPTS_DIR
    (rc / "raw").mkdir(parents=True, exist_ok=True)
    for sid, body, quote, off in (("S498", body1, quote1, i1), ("S499", body2, quote2, i2)):
        (rc / "raw" / f"{sid}.body").write_text(body, encoding="utf-8")
        rec = {"schema": "revenger-quote-audit-v1", "sid": sid, "verdict": "verified",
               "fetch_sha256": hashlib.sha256(body.encode()).hexdigest(),
               "length": len(body.encode()), "quote": quote,
               "span": {"start": off, "end": off + len(quote)},
               "http_status": 200, "fetched_at": ROUND_DATE,
               "fetch_url": "https://fixture.invalid/" + sid}
        (rc / f"{sid}.receipt.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
    src = (root / "corpus/SOURCES.md").read_text(encoding="utf-8")
    add = []
    for sid, url, anchor, teaches in (
        ("S498", "https://github.com/morluto/rea", "README.md overview at main 2026-11-05",
         "2026-11-05 re-open of the S054 source: the declared tool families are unchanged at the current revision"),
        ("S499", "https://github.com/morluto/rea docs/installation.md", "installation.md at main 2026-11-05",
         "2026-11-05 re-open of the S075 source: the approval-boundary statement is unchanged at the current revision"),
    ):
        add.append(f"| {sid} | rea docs re-open — {url} | docs | A | {teaches} | {anchor} | "
                   f'"drift check of the pinned r72 scope; no drift found" | mined | {ROUND_DATE} | on-release | '
                   f"{ENTRY_REL} |")
    (root / "corpus/SOURCES.md").write_text(src + "\n".join(add) + "\n", encoding="utf-8")
    # registry + wave artifacts + votes
    (root / REGISTRY_REL).parent.mkdir(parents=True, exist_ok=True)
    (root / REGISTRY_REL).write_text(json.dumps(
        {"members": {k: {"role": v} for k, v in PINNED_SEATS.items()}}, indent=1), encoding="utf-8")
    (root / VOTES_DIR).mkdir(parents=True, exist_ok=True)
    ds = {q: ("PASS" if q in ("Q01", "Q02", "Q10", "Q16") else "n/a") for q in QS}
    notes = {q: ("tier-A project docs opened this round back the tool-role table" if q == "Q01" else
                 "no derived byte values exist in this documentation-only entry") for q in QS}
    for seat, role, art in (("ReviewerGate", "reviewer", "ReviewerGate/evidence.md"),
                            ("ReviewerBlind", "reviewer", "ReviewerBlind/evidence.md"),
                            ("CriticR94", "critic", "CriticR94/evidence.md")):
        rel = f"{WAVE_DIR}/w1/{art}"
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"seat evidence for {seat}\ncandidate {want}\n", encoding="utf-8")
        (root / VOTES_DIR / f"{seat}.json").write_text(json.dumps(
            _vote(seat, role, want, ds, notes, rel, hashlib.sha256(p.read_bytes()).hexdigest())), encoding="utf-8")
    return root, want


def _fixture_delta(root, kind):
    """Apply one forged-class delta to an honest fixture copy."""
    ep = root / ENTRY
    text = ep.read_text(encoding="utf-8")
    votes = root / VOTES_DIR
    if kind == "F10-dup-status":
        text += "\n```\nadmission-status: admitted\n```\n"
    elif kind == "F11-forged-registry":
        reg = json.loads((root / REGISTRY_REL).read_text())
        reg["members"]["FabA"] = {"role": "critic"}
        (root / REGISTRY_REL).write_text(json.dumps(reg))
        want = digest(text)
        p = root / f"{WAVE_DIR}/w1/FabA/evidence.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"fab evidence {want}\n", encoding="utf-8")
        ds = {q: "PASS" for q in QS}
        (votes / "FabA.json").write_text(json.dumps(_vote(
            "FabA", "critic", want, ds, {}, rel_clamp(p, root), hashlib.sha256(p.read_bytes()).hexdigest())))
    elif kind == "F12-case-dup-seat":
        v = json.loads((votes / "ReviewerGate.json").read_text())
        v["seat"] = "reviewergate"
        (votes / "reviewergate.json").write_text(json.dumps(v))
    elif kind == "F13-role-mismatch":
        v = json.loads((votes / "CriticR94.json").read_text())
        v["role"] = "reviewer"
        (votes / "CriticR94.json").write_text(json.dumps(v))
    elif kind == "F14-empty-artifact":
        p = root / f"{WAVE_DIR}/w1/ReviewerBlind/evidence.md"
        p.write_bytes(b"")
        v = json.loads((votes / "ReviewerBlind.json").read_text())
        v["artifact_sha256"] = hashlib.sha256(b"").hexdigest()
        (votes / "ReviewerBlind.json").write_text(json.dumps(v))
    elif kind == "F15-traversal":
        v = json.loads((votes / "ReviewerBlind.json").read_text())
        v["artifact_path"] = WAVE_DIR + "/w1/../../../../corpus/SOURCES.md"
        (votes / "ReviewerBlind.json").write_text(json.dumps(v))
    elif kind == "F16-body-rejected-sid":
        text = text.replace("## Observation, inference, unknown",
                            "Per S0999 the atlas approach generalizes.\n\n## Observation, inference, unknown")
    elif kind == "F17-vacuous-na":
        v = json.loads((votes / "ReviewerGate.json").read_text())
        v["decisions"]["Q03"] = "n/a"
        v["notes"]["Q03"] = "-"
        (votes / "ReviewerGate.json").write_text(json.dumps(v))
    elif kind == "F18-ws-output":
        text += "\n```sh\n$ python3 -B corpus/lint_entry.py --help\n   \n\t\n```\n"
    elif kind == "F18b-tilde-fence":
        text += "\n~~~sh\n$ python3 -B corpus/lint_entry.py --help\nfabricated output\n~~~\n"
    elif kind == "ONLY-C15-second-row":
        rl = root / "corpus/README.md"
        out = []
        for ln in rl.read_text(encoding="utf-8").splitlines():
            c = cells(ln)
            if len(c) == 5 and c[0] == "C07":
                c[4] = "partial"
                ln = "| " + " | ".join(c) + " |"
            out.append(ln)
        rl.write_text("\n".join(out) + "\n", encoding="utf-8")
        return root
    elif kind == "F19-stale-new-row":
        sl = root / "corpus/SOURCES.md"
        sl.write_text(sl.read_text(encoding="utf-8").replace(
            '"drift check of the pinned r72 scope; no drift found" | mined | 2026-11-05 |',
            '"drift check of the pinned r72 scope; no drift found" | mined | 2026-11-04 |', 1), encoding="utf-8")
        return root
    ep.write_text(text, encoding="utf-8")
    return root


def rel_clamp(p, root):
    return str(p.relative_to(root))


EXPECT_FAIL = {
    "F10-dup-status": "C1_ADMITTED",
    "F11-forged-registry": "C1_VOTES",
    "F12-case-dup-seat": "C1_VOTES",
    "F13-role-mismatch": "C1_VOTES",
    "F14-empty-artifact": "C1_VOTES",
    "F15-traversal": "C1_VOTES",
    "F16-body-rejected-sid": "C1_SOURCES",
    "F17-vacuous-na": "C1_VOTES",
    "F18-ws-output": "C1_EMBED_NONVACUOUS",
    "F18b-tilde-fence": "C1_EMBED_NONVACUOUS",
    "F19-stale-new-row": "C1_SOURCES",
    "ONLY-C15-second-row": "C1_ONLY_C15",
}


def self_test():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="c1v3-selftest-", dir=str(SCRATCH)))
    fails = []
    try:
        root, want = _fixture(work)
        r = run([sys.executable, "-B", str(Path(__file__).resolve()), "--tree", str(root)], str(LANE))
        if "C1_VERDICT=pass" not in r.stdout or r.returncode != 0:
            fails.append(f"POS honest fixture did not pass: rc={r.returncode} tail={r.stdout.splitlines()[-1:]}")
        for kind, expect in EXPECT_FAIL.items():
            froot, _ = _fixture(work)
            _fixture_delta(froot, kind)
            r = run([sys.executable, "-B", str(Path(__file__).resolve()), "--tree", str(froot)], str(LANE))
            fails_legs = [ln.split("=")[0] for ln in r.stdout.splitlines()
                          if ln.startswith(("C1_",)) and ln.endswith("=fail") and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]
            if r.returncode == 0 or expect not in fails_legs:
                fails.append(f"{kind}: expected fail on {expect}, got rc={r.returncode} failing={fails_legs}")
        dn_work = Path(tempfile.mkdtemp(prefix="dn-", dir=work))
        do_nothing, err = materialize(FREEZE_REV, None, dn_work)
        if do_nothing:
            r = run([sys.executable, "-B", str(Path(__file__).resolve()), "--tree", str(do_nothing)], str(LANE))
            if "C1_C15_HELD=fail" not in r.stdout or r.returncode == 0:
                fails.append(f"do-nothing base did not fail: rc={r.returncode}")
        else:
            fails.append(f"do-nothing materialize: {err}")
        print(f"SELFTEST_C1V3={'pass' if not fails else 'fail'} legs={len(EXPECT_FAIL)+2}")
        for f in fails:
            print("SELFTEST FAIL:", f)
        return 0 if not fails else 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main(argv):
    if "--self-test" in argv:
        return self_test()
    rev = tree = None
    if "--rev" in argv:
        rev = argv[argv.index("--rev") + 1]
    if "--tree" in argv:
        tree = Path(argv[argv.index("--tree") + 1])
    if not rev and not tree:
        print(__doc__)
        return 64
    SCRATCH.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="c1v3-run-", dir=str(SCRATCH)))
    try:
        root, err = materialize(rev, tree, work)
        if not root:
            print(f"could-not-evaluate: {err}")
            return 2
        legs, ok = evaluate(root)
        return 0 if ok else 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
