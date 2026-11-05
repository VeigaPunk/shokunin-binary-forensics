#!/usr/bin/env python3
r"""Round-98 admission counter v7. Profiles c02 (v6 constants) and c14.

Carries v6 admission legs and eight named checks. Amendment A scopes used-by
checking to profile rows and PASS-note evidence requirements to c14; both
profiles prohibit Q09 n/a when the entry makes a digest claim. Only the L1
scores landing trees after the v7 freeze. Scratch honours --work and TMPDIR.
"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import urlparse

LANE = Path(__file__).resolve().parents[2]
import tempfile as _tfmod
SCRATCH = (Path(os.environ["HYAKU_SCRATCH"]) if os.environ.get("HYAKU_SCRATCH") else Path(_tfmod.gettempdir())) / "revenger-r98" / "c1v7"
WORK_ARG = None
ENTRY = "corpus/knowledge/round-96-native-analysis-sessions.md"
ENTRY_REL = "knowledge/round-96-native-analysis-sessions.md"
ROUND_DATE = "2026-11-05"
FREEZE_REV = "2875b9c9fa4cc15fd5a8ff991f04cdd0417bec97"
QS = [f"Q{i:02d}" for i in range(1, 18)]
TARGET_ROW = "C02"
HELD_TARGET = 13
NEW_ROW_IDS = ("S502", "S503", "S504")
RECEIPT_ROW_IDS = ("S502", "S503")
HOST_ALLOWLIST = frozenset({"raw.githubusercontent.com", "github.com"})
# sids the entry cites AS rejections (Q12): none this round
REJECTED_OK = frozenset()
WAVE_DIR = ".ufo/waves/round-96"
REGISTRY_REL = WAVE_DIR + "/w1/swarm-registry.json"
RECEIPTS_DIR = "reports/round-96/quote-receipts"
FETCH_LOG_REL = RECEIPTS_DIR + "/fetch-log.md"
VOTES_DIR = "reports/round-96/votes"
HEAD_WINDOW = 30
STATUS_ANY = re.compile(r"(?i)\s*admission-status\s*:")
PINNED_SEATS = {
    "ScoutReopen": "scout",
    "ScribeLesson": "scribe",
    "ExecSession": "executor",
    "ExecReceipts": "executor",
    "ExecBattery": "executor",
    "ExecFrozen": "executor",
    "ReviewerGate": "reviewer",
    "ReviewerBlind": "reviewer",
    "CriticR96": "critic",
    "MutationR96": "mutation-tester",
    "ConnectorOverlap": "connector",
    "SentinelScope": "sentinel",
}
VOTE_ROLES = ("reviewer", "critic")
ARCHIVE_PATHS = ["corpus", "reports/round-93", "reports/round-94",
                 "reports/round-95", "reports/round-96",
                 ".ufo/waves/round-95", ".ufo/waves/round-96"]


PROFILE = "c02"
FIXTURE_PATH = "corpus/fixtures/pe-r75-headless-smoke/fixture.exe"
GROUNDED_ROW_IDS = NEW_ROW_IDS
QUOTE_REFS = {"S502": "rea decompile <path> --file-offset=0x... --provider ghidra",
              "S503": "Use shipped-artifact or requested runtime evidence to explain features"}
_C02_CONSTANTS = {k: globals()[k] for k in (
    "ENTRY", "ENTRY_REL", "TARGET_ROW", "HELD_TARGET", "NEW_ROW_IDS",
    "RECEIPT_ROW_IDS", "VOTES_DIR", "RECEIPTS_DIR", "FETCH_LOG_REL", "WAVE_DIR",
    "REGISTRY_REL", "PINNED_SEATS", "FREEZE_REV", "ARCHIVE_PATHS", "FIXTURE_PATH",
    "GROUNDED_ROW_IDS", "QUOTE_REFS")}


def configure(profile):
    """Set all profile-bound constants together; imports retain c02 defaults."""
    global PROFILE
    if profile not in ("c02", "c14"):
        raise ValueError("unknown profile")
    globals().update(_C02_CONSTANTS)
    PROFILE = profile
    if profile == "c14":
        globals().update(
            ENTRY="corpus/knowledge/round-98-rea-host-readiness.md",
            ENTRY_REL="knowledge/round-98-rea-host-readiness.md",
            TARGET_ROW="C14", HELD_TARGET=14, NEW_ROW_IDS=("S506", "S507"),
            RECEIPT_ROW_IDS=("S506",), GROUNDED_ROW_IDS=("S505", "S506", "S507"),
            VOTES_DIR="reports/round-98/votes",
            RECEIPTS_DIR="reports/round-98/quote-receipts",
            FETCH_LOG_REL="reports/round-98/quote-receipts/fetch-log.md",
            WAVE_DIR=".ufo/waves/round-98",
            REGISTRY_REL=".ufo/waves/round-98/w1/swarm-registry.json",
            FREEZE_REV="9d49002a3804de48d365b7d32849ada06745d64f",
            FIXTURE_PATH="corpus/fixtures/archive-r2/fixture.zip",
            QUOTE_REFS={"S506": "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra."},
            ARCHIVE_PATHS=_C02_CONSTANTS["ARCHIVE_PATHS"] + [
                "reports/round-97", "reports/round-98", ".ufo/waves/round-97", ".ufo/waves/round-98"],
            PINNED_SEATS={
                "ExecCounterV7": "executor", "ExecHarness7": "executor", "ExecControls": "executor",
                "ScoutReopen": "scout", "ScribeLesson": "scribe", "ConnectorOverlap": "connector",
                "ReviewerClaims": "reviewer", "ReviewerGate": "reviewer", "ReviewerBlind": "reviewer",
                "CriticR98": "critic", "MutationR98": "mutation-tester", "SentinelScope": "sentinel"})


def strict_json(text):
    def hook(pairs):
        seen = set()
        for k, _ in pairs:
            if k in seen:
                raise ValueError(f"duplicate JSON key {k!r}")
            seen.add(k)
        return dict(pairs)
    return json.loads(text, object_pairs_hook=hook)


def digest(text):
    norm = re.sub(r"(?im)^\s*admission-status\s*:.*$", "admission-status: candidate", text)
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
    """Return the root dir holding corpus/, reports/round-96/, .ufo/waves/round-96/."""
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
            shutil.copytree(src, root / rel, symlinks=True)
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
    """Strict registry read: duplicate ids fail here, not downstream."""
    rows = {}
    src = root / "corpus/SOURCES.md"
    if not src.is_file():
        return rows
    for ln in src.read_text(encoding="utf-8").splitlines():
        if re.match(r"^ {0,3}\|[ \t]*S[0-9]{3,}[ \t]*\|", ln):
            c = cells(ln)
            if len(c) == 11:
                if c[0] in rows:
                    raise ValueError(f"duplicate registry row {c[0]}")
                rows[c[0]] = c
    return rows


def check_registry(root):
    """Own leg (M6 close): strict JSON, equals the pinned seat->role map."""
    p = root / REGISTRY_REL
    try:
        reg = strict_json(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return False, f"registry missing/strict-JSON-fail: {e}"
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


def na_reason_ok(reason):
    tokens = reason.split()
    return len(tokens) >= 6 and re.search(r"Q\d{2}", reason) is not None


def check_votes(root, want):
    """Accept votes only under the v4 rules; ANY malformed vote fails the leg outright."""
    votes_dir = root / VOTES_DIR
    if not votes_dir.is_dir():
        return False, "votes dir missing"
    accepted, artifacts, canonical = [], {}, {}
    for vf in sorted(votes_dir.glob("*.json")):
        try:
            v = strict_json(vf.read_text(encoding="utf-8"))
        except (ValueError, OSError) as e:
            return False, f"unreadable/strict-JSON-fail vote {vf.name}: {e}"
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
            if not na_reason_ok(reason):
                return False, (f"vote {seat} n/a reason for {q} fails vocabulary "
                               f"(>=6 tokens and a Q cross-reference): {reason!r}")
        if not any(ds[q] == "PASS" for q in QS):
            return False, f"vote {seat} has no PASS decision"
        apath = v.get("artifact_path")
        asha = v.get("artifact_sha256")
        own_dir = f"{WAVE_DIR}/w1/{seat}/"
        if not (isinstance(apath, str) and apath.startswith(own_dir)):
            return False, f"artifact_path outside the seat's own {own_dir}: {apath!r}"
        if ".." in Path(apath).parts:
            return False, f"artifact_path contains '..': {apath!r}"
        art = root / apath
        resolved = art.resolve()
        wave_root = (root / WAVE_DIR).resolve()
        if not resolved.is_relative_to(wave_root):
            return False, f"artifact resolves outside wave dir: {apath!r}"
        if art.is_symlink() or resolved.is_symlink():
            return False, f"artifact is a symlink: {apath!r}"
        try:
            if resolved.resolve() != resolved:
                pass
        except Exception:
            pass
        # reject any symlink component in the path itself
        cur = root
        for part in Path(apath).parts:
            cur = cur / part
            if cur.is_symlink():
                return False, f"artifact path contains a symlink component: {apath!r}"
        if not art.is_file():
            return False, f"artifact not a file: {apath!r}"
        own_resolved = (root / own_dir).resolve()
        if not resolved.is_relative_to(own_resolved):
            return False, f"artifact resolves outside its own seat dir: {apath!r}"
        b = art.read_bytes()
        if len(b) == 0 or not b.strip():
            return False, f"artifact empty: {apath!r}"
        if not (isinstance(asha, str) and hashlib.sha256(b).hexdigest() == asha):
            return False, f"artifact sha mismatch: {apath!r}"
        btxt = b.decode("utf-8", errors="replace")
        b_visible = re.sub(r"<!--.*?-->", "", btxt, flags=re.S)
        if b_visible.strip() == "":
            return False, f"artifact has no visible content after comment strip: {apath!r}"
        if str(seat) not in b_visible:
            return False, f"artifact does not name its seat {seat}: {apath!r}"
        if want not in b_visible:
            return False, f"artifact does not name the candidate digest: {apath!r}"
        if apath in artifacts or asha in artifacts.values():
            return False, f"artifact not distinct per seat: {apath!r}"
        canonical[cs] = seat
        artifacts[apath] = asha
        accepted.append(str(seat))
    if len(accepted) < 2:
        return False, f"only {len(accepted)} accepted votes"
    return True, ",".join(sorted(accepted))


def check_receipts(root):
    """H2 close: fetched_at / http_status / host allowlist / body re-hash / fetch log."""
    log_txt = ""
    fl = root / FETCH_LOG_REL
    if fl.is_file():
        log_txt = fl.read_text(encoding="utf-8", errors="replace")
    fails = []
    for sid in RECEIPT_ROW_IDS:
        rp = root / RECEIPTS_DIR / f"{sid}.receipt.json"
        try:
            r = strict_json(rp.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            fails.append(f"{sid}:receipt:{e}")
            continue
        if r.get("fetched_at") != ROUND_DATE:
            fails.append(f"{sid}:fetched_at:{r.get('fetched_at')!r}!={ROUND_DATE}")
        if r.get("http_status") != 200:
            fails.append(f"{sid}:http_status:{r.get('http_status')!r}")
        host = urlparse(str(r.get("fetch_url", ""))).hostname or ""
        if host not in HOST_ALLOWLIST:
            fails.append(f"{sid}:host:{host!r}")
        body_p = root / RECEIPTS_DIR / "raw" / f"{sid}.body"
        if not body_p.is_file():
            fails.append(f"{sid}:body-missing")
            continue
        if hashlib.sha256(body_p.read_bytes()).hexdigest() != r.get("fetch_sha256"):
            fails.append(f"{sid}:body-rehash-mismatch")
        line_has = any((sid in ln and str(r.get("fetch_sha256")) in ln
                        and ln.lstrip().startswith("-") and not ("S502" in ln and "S503" in ln))
                       for ln in log_txt.splitlines())
        if not line_has:
            fails.append(f"{sid}:fetch-log-line-missing")
        q = str(r.get("quote", ""))
        ref = QUOTE_REFS
        if ref[sid] not in q:
            fails.append(f"{sid}:quote-irrelevant")
    return (not fails), ("ok" if not fails else "; ".join(fails))


def collect_sid_tokens(text):
    return re.findall(r"\b[Ss]\s*\d{2,}[a-z]?\b", text)


def norm_sid(tok):
    t = re.sub(r"\s+", "", tok).upper()
    t = re.sub(r"[A-Z]$", "", t)
    return t


def check_sids(root, text):
    """M6c close: every widened S-token must normalise to a registry id."""
    try:
        rows = parse_sources(root)
    except ValueError as e:
        return False, f"registry-parse:{e}"
    fails = []
    for tok in sorted(set(collect_sid_tokens(text))):
        sid = norm_sid(tok)
        if sid not in rows:
            fails.append(f"{tok}:{sid}:unresolved")
    return (not fails), ("ok" if not fails else "; ".join(fails))


def check_sources(root, sids):
    try:
        rows = parse_sources(root)
    except ValueError as e:
        return False, f"registry-parse:{e}"
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
        if sid in RECEIPT_ROW_IDS:
            try:
                rec = json.loads((root / RECEIPTS_DIR / f"{sid}.receipt.json").read_text(encoding="utf-8"))
                if str(rec.get("fetch_url", "")) not in r[1]:
                    fails.append(f"{sid}:url-drift")
            except Exception:
                fails.append(f"{sid}:url-drift-noreceipt")
        ub = [x.strip() for x in r[10].split(",") if x.strip() and x.strip() != "\u2014"]
        ub_norm = [x[len("corpus/"):] if x.startswith("corpus/") else x for x in ub]
        if ub_norm != [ENTRY_REL]:
            fails.append(f"{sid}:usedby-exclusivity:{ub}")
    return (not fails), ("ok" if not fails else "; ".join(fails))


def check_quotes(root, sids):
    need = [s for s in RECEIPT_ROW_IDS if s in sids]
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
    """M7 carry-over plus the v4 widening: every `$ `-prompted line in ANY fence needs
    a non-blank output line after it; a `~~~` fence containing a `$ ` line is rejected."""
    bad = []
    for block in re.findall(r"```[^\n]*\n(.*?)```", text, re.S):
        lines = block.strip("\n").split("\n")
        for i, l in enumerate(lines):
            if l.lstrip().startswith("$") and not any(x.strip() for x in lines[i + 1:]):
                bad.append("```:" + l[:60])
    for block in re.findall(r"~~~[^\n]*\n(.*?)~~~", text, re.S):
        lines = block.split("\n")
        if any(l.lstrip().startswith("$") for l in lines):
            bad.append("~~~:" + lines[0][:60])
    return (not bad), ("ok" if not bad else "; ".join(bad))


def check_pycache(root):
    """M5t+M8 close: no __pycache__ or loose *.pyc under the round's surfaces or frozen hold dirs."""
    bad = []
    for rel in ARCHIVE_PATHS:
        base = root / rel
        if not base.is_dir():
            continue
        for p in base.rglob("__pycache__"):
            bad.append(str(p.relative_to(root)))
        for p in base.rglob("*.pyc"):
            bad.append(str(p.relative_to(root)))
    return (not bad), ("ok" if not bad else "; ".join(sorted(bad)[:4]))


def check_admitted_union(root):
    """A4 close: every knowledge file whose bytes carry an admitted admission-status
    line (wide case-insensitive anchor) must be named in the coverage-row knowledge
    union (cells 2 and 3). An unreferenced shadow entry fails here."""
    readme = (root / "corpus/README.md").read_text(encoding="utf-8").splitlines()
    union = set()
    for ln in readme:
        c = cells(ln)
        if len(c) == 5 and re.fullmatch(r"C\d{2}", c[0]):
            for cellx in (c[2], c[3]):
                for f in row_fileset(cellx):
                    union.add(f)
    bad = []
    kd = root / "corpus/knowledge"
    if kd.is_dir():
        for pf in sorted(x for x in kd.rglob("*") if x.is_file() and x.suffix.lower() == ".md"):
            t = pf.read_bytes().decode("utf-8", errors="replace")
            for ln in t.splitlines():
                if re.search(r"(?i)^\s*admission-status\s*:\s*admitted", ln):
                    rel = f"knowledge/{pf.name}"
                    if rel not in union:
                        bad.append(rel)
                    break
    return (not bad), ("ok" if not bad else "; ".join(sorted(bad)[:4]))


def row_fileset(cell):
    return re.findall(r"[\w./-]*knowledge/[\w.-]+\.md", cell)



HEADER_KEYS = ("source", "verified-at", "recheck", "coverage-map", "admission-status")


def result(fails):
    return not fails, "; ".join(fails) if fails else "ok"


def check_entry_bytes(root):
    try:
        raw = (root / ENTRY).read_bytes()
        raw.decode("utf-8", errors="strict")
    except (OSError, UnicodeError) as exc:
        return False, f"entry unreadable/strict UTF-8: {exc}"
    fails = []
    for mark, label in ((b"\xef\xbb\xbf", "BOM"), (b"\r", "CR"), (b"\x00", "NUL")):
        if mark in raw:
            fails.append(label)
    return result(fails)


def check_header_position(text):
    fails, leading, fence = [], [], None
    in_leading = True
    for i, line in enumerate(text.splitlines(), 1):
        fm = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fm:
            token = fm.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            in_leading = False
            continue
        hm = re.match(r"^\s*(source|verified-at|recheck|coverage-map|admission-status):", line)
        if hm:
            if fence:
                fails.append(f"line {i}: header inside fence")
            if not in_leading:
                fails.append(f"line {i}: header outside leading block")
            leading.append(hm.group(1))
        else:
            in_leading = False
    for key in HEADER_KEYS:
        if key not in leading:
            fails.append(f"missing leading {key}")
    return result(fails)


def check_verified_at(root, text, rows):
    dates = re.findall(r"(?m)^verified-at:\s*(\d{4}-\d{2}-\d{2})\b", text)
    fails = []
    if dates != [ROUND_DATE]:
        fails.append(f"verified-at={dates!r}, expected {ROUND_DATE}")
    for sid in NEW_ROW_IDS:
        if sid not in rows or rows[sid][8] != ROUND_DATE:
            fails.append(f"{sid}:opened differs from verified-at/ROUND_DATE")
    for sid in RECEIPT_ROW_IDS:
        try:
            receipt = strict_json((root / RECEIPTS_DIR / f"{sid}.receipt.json").read_text(encoding="utf-8"))
            if receipt.get("fetched_at") != ROUND_DATE:
                fails.append(f"{sid}:fetched_at differs from verified-at/ROUND_DATE")
        except (OSError, ValueError, AttributeError) as exc:
            fails.append(f"{sid}:receipt:{exc}")
    return result(fails)


def check_vote_notes(root, text):
    fails, notes_seen = [], {}
    files = sorted((root / VOTES_DIR).glob("*.json"))
    if not files:
        return False, "no votes"
    votes = []
    for vf in files:
        try:
            vote = strict_json(vf.read_text(encoding="utf-8"))
            decisions, notes = vote.get("decisions", {}), vote.get("notes", {})
            if not isinstance(decisions, dict) or not isinstance(notes, dict):
                raise ValueError("decisions/notes not objects")
            votes.append((vf.name, decisions, notes))
            for q, note in notes.items():
                if isinstance(note, str):
                    notes_seen.setdefault(note.strip(), []).append((vf.name, q))
        except (OSError, ValueError, AttributeError) as exc:
            fails.append(f"{vf.name}:invalid vote: {exc}")
    digest_claim = bool(re.search(r"\b[0-9a-fA-F]{64}\b", text))
    for seat, decisions, notes in votes:
        if digest_claim and decisions.get("Q09") == "n/a":
            fails.append(f"{seat}:Q09 n/a inapplicable: entry contains a 64-hex digest claim")
        if PROFILE != "c14":
            continue
        for q in QS:
            if decisions.get(q) != "PASS":
                continue
            note = notes.get(q, "")
            if not isinstance(note, str) or len(note.split()) < 6:
                fails.append(f"{seat}:{q}:PASS note needs >=6 tokens")
                continue
            if re.search(r"(?i)\bn/a\b|not applicable|no byte oracle|documentation.only|no .* exists", note):
                fails.append(f"{seat}:{q}:PASS note is n/a-style")
            if len(notes_seen.get(note.strip(), [])) != 1:
                fails.append(f"{seat}:{q}:PASS note shared verbatim")
    ok, why = result(fails)
    return ok, why if fails else "ok; Q09 applicability checked against 64-hex digest claims"


def tree_path(root, rel):
    """No absolute/parent/symlink escape may satisfy a corpus pointer."""
    path = root / rel
    if Path(rel).is_absolute() or ".." in Path(rel).parts or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"path outside tree: {rel}")
    return path


def path_nonempty(root, rel):
    if any(c in rel for c in "*?["):
        matches = list(root.glob(rel))
        return bool(matches) and all(path_nonempty(root, str(p.relative_to(root))) for p in matches)
    path = tree_path(root, rel)
    if path.is_file():
        return path.stat().st_size > 0
    if path.is_dir():
        return any(p.is_file() and p.stat().st_size > 0 for p in path.rglob("*"))
    return False


def check_ownwork_paths(root, text, rows):
    fails = []
    for sid in NEW_ROW_IDS:
        row = rows.get(sid)
        if row is None:
            fails.append(f"{sid}:missing row")
            continue
        if row[2] != "own-work" and "(own-work)" not in row[1]:
            continue
        paths = re.findall(r"`([^`]+)`", row[1])
        # v6's synthetic fixture uses an unquoted path; the frozen builder is unchanged.
        if not paths:
            paths = re.findall(r"corpus/(?:live/runs|fixtures)/[\w./*-]+", row[1])
        if not paths:
            fails.append(f"{sid}:no own-work source path")
        for rel in paths:
            try:
                if not path_nonempty(root, rel):
                    fails.append(f"{sid}:missing/empty {rel}")
            except (OSError, ValueError) as exc:
                fails.append(f"{sid}:{exc}")
    for rel in sorted(set(re.findall(r"corpus/(?:live/runs|fixtures)/[\w./*-]+", text))):
        try:
            if not path_nonempty(root, rel.rstrip(".,;")):
                fails.append(f"entry:missing/empty {rel}")
        except (OSError, ValueError) as exc:
            fails.append(f"entry:{exc}")
    return result(fails)


def check_quote_bytes(root, rows):
    fails, checked = [], []
    for sid in dict.fromkeys(NEW_ROW_IDS + GROUNDED_ROW_IDS):
        row = rows.get(sid)
        if not row or row[2] != "own-work":
            continue
        anchor = row[5]
        if "(1-based bytes" not in anchor:
            continue
        match = re.search(r"`([^`]+)`[^`]*\(1-based bytes (\d+)-(\d+)\):\s*(`[^`]*`(?:\s*/\s*`[^`]*`)*)", anchor)
        if not match:
            fails.append(f"{sid}:malformed byte anchor")
            continue
        rel, start, end, quoted = match.groups()
        checked.append(sid)
        a, b = int(start), int(end)
        try:
            body = tree_path(root, rel).read_bytes()
            expected = [seg.encode("utf-8") for seg in re.findall(r"`([^`]*)`", quoted)]
            actual = [seg for seg in body[a - 1:b].split(b"\n") if seg]
            if a < 1 or b < a or b > len(body) or actual != expected:
                fails.append(f"{sid}:{rel}:bytes {a}-{b} do not equal backticked segments")
        except (OSError, ValueError) as exc:
            fails.append(f"{sid}:{exc}")
    return result(fails) if fails else (True, "ok; checked byte anchors=" + ",".join(checked or ["none"]))


def check_usedby_grounded(root, rows=None):
    if rows is None:
        try:
            rows = parse_sources(root)
        except (OSError, ValueError) as exc:
            return False, str(exc)
    fails = []
    for sid in GROUNDED_ROW_IDS:
        row = rows.get(sid)
        if row is None:
            fails.append(f"{sid}:missing row")
            continue
        for rel in row_fileset(row[10]):
            rel = rel if rel.startswith("corpus/") else "corpus/" + rel
            try:
                entry = tree_path(root, rel).read_text(encoding="utf-8")
                if not re.search(r"\b" + re.escape(sid) + r"\b", entry):
                    fails.append(f"{sid} -> {rel}:entry does not cite row id")
            except (OSError, ValueError) as exc:
                fails.append(f"{sid} -> {rel}:{exc}")
    return result(fails)


def check_c14_digests(root, text):
    fails = []
    fixed = (FIXTURE_PATH, RECEIPTS_DIR + "/raw/S506.body")
    for rel in fixed:
        matching = [ln for ln in text.splitlines() if rel in ln and "sha256sum" in ln and ln.startswith("|")]
        try:
            sha = hashlib.sha256(tree_path(root, rel).read_bytes()).hexdigest()
            tokens = [tok.lower() for ln in matching for tok in re.findall(r"\b[0-9a-fA-F]{64}\b", ln)]
            if tokens != [sha]:
                fails.append(f"{rel}:recorded digest mismatch/missing")
        except (OSError, ValueError) as exc:
            fails.append(f"{rel}:{exc}")
    records = list((root / "corpus/live/runs/round-98").glob("*"))
    record_rows = "\n".join(ln for ln in text.splitlines() if ln.startswith("|") and "sha256sum corpus/live/runs/round-98/*" in ln)
    pairs = re.findall(r"`([0-9a-fA-F]{8})…`\s*\(([^)]+)\)", record_rows)
    recorded = {name: prefix for prefix, name in pairs}
    if len(recorded) != len(pairs) or not records:
        fails.append("record digest rows missing or duplicated")
    expected_names = set()
    for path in records:
        if path.is_file():
            expected_names.add(path.name)
            if recorded.get(path.name, "").lower() != hashlib.sha256(path.read_bytes()).hexdigest()[:8]:
                fails.append(f"{path.name}:record prefix mismatch/missing")
    if set(recorded) != expected_names:
        fails.append("record prefix names differ from record files")
    return result(fails)


def new_checks(root, text):
    try:
        rows = parse_sources(root)
    except (OSError, ValueError) as exc:
        rows = {}
    readme = (root / "corpus/README.md").read_text(encoding="utf-8")
    ids = [cells(ln)[0] for ln in readme.splitlines()
           if re.match(r"^ {0,3}\|\s*C\d+\s*\|", ln)]
    return {
        "C1_ROWSET": (ids == [f"C{i:02d}" for i in range(1, 16)], f"ordered ids={','.join(ids)}"),
        "C1_ENTRY_BYTES": check_entry_bytes(root),
        "C1_HEADER_POSITION": check_header_position(text),
        "C1_VERIFIED_AT": check_verified_at(root, text, rows),
        "C1_VOTE_NOTES": check_vote_notes(root, text),
        "C1_OWNWORK_PATHS": check_ownwork_paths(root, text, rows),
        "C1_QUOTE_BYTES": check_quote_bytes(root, rows),
        "C1_USEDBY_GROUNDED": check_usedby_grounded(root, rows),
    }


def evaluate(root):
    legs = {}
    readme = (root / "corpus/README.md").read_text(encoding="utf-8").splitlines()
    cov = [cells(l) for l in readme if re.match(r"^\|[ \t]*C[0-9]+ ", l) and len(cells(l)) == 5]
    legs["C1_ROWS_TOTAL"] = len(cov) == 15
    crow = next((r for r in cov if r[0] == TARGET_ROW), None)
    legs["C1_TARGET_HELD"] = bool(crow) and crow[4] == "held"
    fileset = row_fileset(crow[2]) if crow else []
    legs["C1_TARGET_CITES"] = (bool(crow) and fileset == [ENTRY_REL]
                            and (root / ENTRY).is_file())

    # C1_ONLY_TARGET: every other coverage row byte-identical to the frozen base.
    baserows = base_readme(root)
    diffs = []
    if baserows:
        for r in cov:
            if r[0] != TARGET_ROW and baserows.get(r[0]) != _raw_line(readme, r[0]):
                diffs.append(r[0])
        legs["C1_ONLY_TARGET"] = (not diffs and crow is not None
                               and baserows.get(TARGET_ROW) != _raw_line(readme, TARGET_ROW))
    else:
        legs["C1_ONLY_TARGET"] = False

    text = (root / ENTRY).read_bytes().decode("utf-8", errors="replace") if (root / ENTRY).is_file() else ""
    lines = text.splitlines()
    head = lines[:HEAD_WINDOW]
    st_idx = [i for i, l in enumerate(lines) if STATUS_ANY.search(l)]
    legs["C1_DERIV_TABLE"] = True
    legs["C1_ADMITTED_WS"] = True
    for i, l in enumerate(lines):
        if re.match(r"(?i)^\s*admission-status\s*:", l):
            lead = l[: len(l) - len(l.lstrip())]
            if lead and lead != " " * len(lead):
                legs["C1_ADMITTED_WS"] = False
            if "\u00a0" in l:
                legs["C1_ADMITTED_WS"] = False
            if "\t" in l.split(":", 1)[0]:
                legs["C1_ADMITTED_WS"] = False
    legs["C1_ADMITTED"] = (len(st_idx) == 1 and st_idx[0] < HEAD_WINDOW
                           and lines[st_idx[0]].strip().lower() == "admission-status: admitted")
    legs["C1_TRIO"] = all(any(l.startswith(k) for l in head)
                          for k in ("source:", "verified-at:", "recheck:"))

    want = digest(text) if text else None
    reg_ok, reg_why = check_registry(root)
    legs["C1_REGISTRY"] = reg_ok
    v_ok, v_why = check_votes(root, want)
    legs["C1_VOTES"] = v_ok
    r_ok, r_why = check_receipts(root)
    legs["C1_RECEIPTS"] = r_ok
    p_ok, p_why = check_pycache(root)
    legs["C1_PYCACHE"] = p_ok
    au_ok, au_why = check_admitted_union(root)
    legs["C1_ADMITTED_UNION"] = au_ok

    if (root / ENTRY).is_file():
        lint = run([sys.executable, "-B", "corpus/lint_entry.py", "--entry", ENTRY,
                    "--lane", str(LANE)], str(root))
        emb = run([sys.executable, "-B", "corpus/check_embedded_outputs.py",
                   "--entry", ENTRY], str(root))
        legs["C1_LINT"] = lint.returncode == 0
        print("C1_LINT_WHY=" + (lint.stdout + lint.stderr).strip().replace("\n", "; "))
        has_cmd_block = bool(re.search(r"```[^\n]*\n\$|~~~[^\n]*\n\$|```[^\n]*\n\s*\$", text, re.M))
        emb_ok = emb.returncode == 0 or (emb.returncode == 2
                                         and "could-not-evaluate" in (emb.stdout + emb.stderr)
                                         and not has_cmd_block)
        legs["C1_EMBEDDED"] = emb_ok
        nv_ok, nv_why = check_embed_nonvacuous(text)
        legs["C1_EMBED_NONVACUOUS"] = nv_ok
    else:
        legs["C1_LINT"] = legs["C1_EMBEDDED"] = legs["C1_EMBED_NONVACUOUS"] = False

    # FG15: derivation rows must be drawn from the pinned Q01-Q17 set only
    for _ln in text.splitlines():
        for _m in re.findall(r"\|\s*(Q\d+)", _ln):
            if _m not in QS:
                legs["C1_DERIV_TABLE"] = False
    # FG11 derivation-table honesty: any 64-hex token on a derivation row must equal the actual fixture sha if the row names that fixture path
    try:
        _fx = root / FIXTURE_PATH
        if _fx.is_file():
            _real = hashlib.sha256(_fx.read_bytes()).hexdigest()
            for _ln in text.splitlines():
                if FIXTURE_PATH in _ln and "sha256" in _ln:
                    for _tok in re.findall(r"[0-9a-fA-F]{64}", _ln):
                        if _tok.lower() != _real:
                            legs["C1_DERIV_TABLE"] = False
    except Exception:
        pass
    sid_tokens = collect_sid_tokens(text)
    sids = sorted(set(norm_sid(t) for t in sid_tokens))
    s_ok, s_why = check_sids(root, text)
    legs["C1_SIDS"] = s_ok
    src_ok, src_why = check_sources(root, sids)
    legs["C1_SOURCES"] = src_ok
    q_ok, q_why = check_quotes(root, sids)
    legs["C1_QUOTES"] = q_ok

    held_backed = 0
    for r in cov:
        files = row_fileset(r[2])
        if r[4] == "held" and files and all((root / "corpus" / f).is_file() for f in files):
            held_backed += 1
    legs["C1_K_HELD_BACKED"] = held_backed == HELD_TARGET

    print(f"C1_K_HELD_BACKED={held_backed}/{len(cov)}")
    print(f"C1_VOTES_WHY={v_why} digest={want}")
    print(f"C1_REGISTRY_WHY={reg_why}")
    print(f"C1_RECEIPTS_WHY={r_why}")
    print(f"C1_PYCACHE_WHY={p_why}")
    print(f"C1_SOURCE_IDS={','.join(sids) or 'none'}")
    print(f"C1_SIDS_WHY={s_why}")
    print(f"C1_SOURCES_WHY={src_why}")
    print(f"C1_QUOTES_WHY={q_why}")
    print(f"C1_ADMITTED_UNION_WHY={au_why}")
    print(f"C1_ONLY_TARGET_DIFFS={','.join(diffs) or 'none'}")
    for name, result in new_checks(root, text).items():
        passed, why = result
        legs[name] = passed
        print(f"{name}_WHY={why}")
    if PROFILE == "c14":
        deriv_ok, deriv_why = check_c14_digests(root, text)
        legs["C1_DERIV_TABLE"] = legs["C1_DERIV_TABLE"] and deriv_ok
        print(f"C1_DERIV_TABLE_WHY={deriv_why}")
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


NA_NOTE = ("no byte oracle or derived value exists in this documentation-only entry; "
           "see the Q03 and Q11 rows of the entry's own map")
NA_BY_Q = {
    "Q01": "tier-A rows S502 and S503 were opened this round with committed receipts, "
           "so the round-of-open rule holds; see also Q02",
}


def _fixture_c02(work):
    """Honest admission-shaped fixture built from the freeze archive + real entry bytes."""
    work = Path(tempfile.mkdtemp(prefix="fx-", dir=work))
    root, err = materialize(FREEZE_REV, None, work)
    if not root:
        raise SystemExit(f"fixture: {err}")
    # The c02 freeze predates the saved record cited by the real entry.
    # L1-approved fixture supplement: copy committed record bytes, never invent them.
    record_rel = "corpus/live/runs/round-96"
    shutil.copytree(LANE / record_rel, root / record_rel, dirs_exist_ok=True)
    entry = (LANE / ENTRY).read_text(encoding="utf-8")
    entry = re.sub(r"(?im)^\s*admission-status\s*:.*$", "admission-status: admitted",
                   entry, count=1)
    (root / ENTRY).write_text(entry, encoding="utf-8")
    want = digest(entry)
    out = []
    for ln in (root / "corpus/README.md").read_text(encoding="utf-8").splitlines():
        c = cells(ln)
        if len(c) == 5 and c[0] == TARGET_ROW:
            c[2] = ("`" + ENTRY_REL + "` (round-96 admission; REA's documented native routes "
                    "at the pinned revision plus one demonstrated session on this host, "
                    "2026-11-05)")
            c[4] = "held"
            ln = "| " + " | ".join(c) + " |"
        out.append(ln)
    (root / "corpus/README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    # receipts: synthetic bodies + receipts + fetch log under the allowlisted host
    rc = root / RECEIPTS_DIR
    (rc / "raw").mkdir(parents=True, exist_ok=True)
    bodies = {
        "S502": "REA native-and-artifacts reference at the pinned revision, re-opened "
                "2026-11-05. CLI `rea decompile <path> --file-offset=0x... --provider "
                "ghidra` resolves the source byte offset internally.\n",
        "S503": "REA skill SKILL.md at the pinned revision, re-opened 2026-11-05. Use "
                "shipped-artifact or requested runtime evidence to explain features, "
                "compare versions, decompile code, or guide a reconstruction.\n",
    }
    log_lines = ["# fetch log (fixture)", ""]
    for sid, quote in (("S502", "rea decompile <path> --file-offset=0x... --provider "
                             "ghidra` resolves the source byte offset internally"),
                       ("S503", "Use shipped-artifact or requested runtime evidence to "
                                "explain features, compare versions, decompile code, or "
                                "guide a reconstruction.")):
        body = bodies[sid]
        (rc / "raw" / f"{sid}.body").write_text(body, encoding="utf-8")
        sha = hashlib.sha256(body.encode()).hexdigest()
        url = f"https://raw.githubusercontent.com/morluto/rea/fixture/{sid}.md"
        i = body.index(quote)
        rec = {"schema": "revenger-quote-audit-v1", "sid": sid, "verdict": "verified",
               "fetch_url": url, "http_status": 200, "fetched_at": ROUND_DATE,
               "fetch_sha256": sha, "length": len(body.encode()), "quote": quote,
               "span": {"start": i, "end": i + len(quote)}}
        (rc / f"{sid}.receipt.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
        log_lines.append(f"- {sid} GET {url} -> HTTP 200, sha256 {sha}")
    (rc / "fetch-log.md").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    # SOURCES: append synthetic S502/S503/S504 mined rows (used-by = ENTRY_REL exactly)
    src = (root / "corpus/SOURCES.md").read_text(encoding="utf-8")
    add = []
    for sid, url, teaches in (
        ("S502", "https://raw.githubusercontent.com/morluto/rea/fixture/S502.md",
         "2026-11-05 open of the native-and-artifacts reference at the pinned revision: the pseudo-code route and its CLI decompile form"),
        ("S503", "https://raw.githubusercontent.com/morluto/rea/fixture/S503.md",
         "2026-11-05 open of the skill SKILL.md at the pinned revision: decompile code is among the declared shipped-artifact uses"),
        ("S504", "corpus/live/runs/round-96/ (own-work)",
         "2026-11-05 open of the saved session record: the rea decompile Evidence and the ghidra-headless receipt on the committed fixture"),
    ):
        add.append(f"| {sid} | rea native-route source — {url} | docs | A | {teaches} | "
                   f"file body or record at the named revision, opened {ROUND_DATE} | "
                   f'"the documented route and the demonstrated session agree" | '
                   f"mined | {ROUND_DATE} | on-release | {ENTRY_REL} |")
    (root / "corpus/SOURCES.md").write_text(src + "\n".join(add) + "\n", encoding="utf-8")
    # registry + wave artifacts + votes
    (root / REGISTRY_REL).parent.mkdir(parents=True, exist_ok=True)
    (root / REGISTRY_REL).write_text(json.dumps(
        {"members": {k: {"role": v} for k, v in PINNED_SEATS.items()}}, indent=1),
        encoding="utf-8")
    (root / VOTES_DIR).mkdir(parents=True, exist_ok=True)
    ds = {q: ("PASS" if q in ("Q01", "Q02", "Q09", "Q10") else "n/a") for q in QS}
    notes = {}
    for q in QS:
        notes[q] = NA_BY_Q[q] if q == "Q01" else NA_NOTE
    for seat, role, art in (("ReviewerGate", "reviewer", "gate-evidence.md"),
                            ("ReviewerBlind", "reviewer", "blind-evidence.md"),
                            ("CriticR96", "critic", "critic-evidence.md")):
        rel = f"{WAVE_DIR}/w1/{seat}/{art}"
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"seat evidence for {seat}\ncandidate {want}\n", encoding="utf-8")
        (root / VOTES_DIR / f"{seat}.json").write_text(json.dumps(
            _vote(seat, role, want, ds, notes, rel,
                  hashlib.sha256(p.read_bytes()).hexdigest())), encoding="utf-8")
    return root, want



def _fixture(work):
    """Honest development fixtures; never modifies the lane corpus or votes."""
    if PROFILE == "c02":
        return _fixture_c02(work)
    work = Path(tempfile.mkdtemp(prefix="fx-c14-", dir=work))
    root, err = materialize(FREEZE_REV, None, work)
    if root is None:
        raise ValueError(f"fixture: {err}")
    # Amendment B supplies the real entry Q-map; README baseline stays frozen.
    entry = (LANE / ENTRY).read_text(encoding="utf-8")
    entry = re.sub(r"(?im)^admission-status:.*$", "admission-status: admitted", entry)
    (root / ENTRY).write_text(entry, encoding="utf-8")
    want = digest(entry)
    readme = root / "corpus/README.md"
    out = []
    for line in readme.read_text(encoding="utf-8").splitlines():
        c = cells(line)
        if len(c) == 5 and c[0] == TARGET_ROW:
            c[2], c[4] = f"`{ENTRY_REL}` (development fixture)", "held"
            line = "| " + " | ".join(c) + " |"
        out.append(line)
    readme.write_text("\n".join(out) + "\n", encoding="utf-8")
    # Fixture correction of the known ungrounded S505 pair, not a lane edit.
    edit_source_row(root, "S505", lambda c: c[:7] + ["queued"] + c[8:10] + ["—"])
    registry = root / REGISTRY_REL
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(json.dumps({"members": {seat: {"role": role} for seat, role in PINNED_SEATS.items()}}), encoding="utf-8")
    vd = root / VOTES_DIR
    vd.mkdir(parents=True, exist_ok=True)
    for seat in ("ReviewerGate", "ReviewerBlind", "CriticR98"):
        artifact = f"{WAVE_DIR}/w1/{seat}/fixture-evidence.md"
        ap = root / artifact
        ap.parent.mkdir(parents=True, exist_ok=True)
        ap.write_text(f"{seat} fixture evidence\n{want}\n", encoding="utf-8")
        notes = {q: f"{seat} inspected {q} against saved readiness evidence and pinned source bytes" for q in QS}
        vote = _vote(seat, PINNED_SEATS[seat], want, {q: "PASS" for q in QS}, notes,
                     artifact, hashlib.sha256(ap.read_bytes()).hexdigest())
        (vd / f"{seat}.json").write_text(json.dumps(vote), encoding="utf-8")
    return root, want


def edit_source_row(root, sid, change):
    src = root / "corpus/SOURCES.md"
    lines = src.read_text(encoding="utf-8").splitlines()
    found = 0
    for i, line in enumerate(lines):
        c = cells(line)
        if len(c) == 11 and c[0] == sid:
            lines[i] = "| " + " | ".join(change(c)) + " |"
            found += 1
    if found != 1:
        raise ValueError(f"fixture row {sid}: hits={found}")
    src.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _new_delta(root, leg):
    ep = root / ENTRY
    text = ep.read_text(encoding="utf-8")
    if leg == "C1_ROWSET":
        readme = root / "corpus/README.md"
        lines = readme.read_text(encoding="utf-8").splitlines()
        donor = next(line for line in lines if cells(line)[0] == "C01")
        lines = [donor if cells(line)[0] == "C06" else line for line in lines]
        readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
    elif leg == "C1_ENTRY_BYTES":
        ep.write_bytes(b"\xef\xbb\xbf" + ep.read_bytes())
    elif leg == "C1_HEADER_POSITION":
        ep.write_text("```text\n" + text + "\n```\n", encoding="utf-8")
    elif leg == "C1_VERIFIED_AT":
        ep.write_text(text.replace("verified-at: " + ROUND_DATE, "verified-at: 2026-10-01", 1), encoding="utf-8")
    elif leg == "C1_VOTE_NOTES":
        vf = root / VOTES_DIR / "ReviewerGate.json"
        vote = strict_json(vf.read_text(encoding="utf-8"))
        vote["decisions"]["Q09"] = "n/a"
        vote["notes"]["Q09"] = NA_NOTE
        vf.write_text(json.dumps(vote), encoding="utf-8")
    elif leg == "C1_OWNWORK_PATHS":
        sid = "S504" if PROFILE == "c02" else "S507"
        edit_source_row(root, sid, lambda c: c[:1] + [c[1].replace("corpus/live/runs/", "corpus/live/runs/missing-development/")] + c[2:])
    elif leg == "C1_QUOTE_BYTES":
        sid = "S504" if PROFILE == "c02" else "S507"
        if PROFILE == "c02":
            rel = "corpus/live/runs/round-96/codeable-decompiled.c"
            def change(c):
                c[2] = "own-work"
                c[5] = f"`{rel}` (1-based bytes 1-1): `wrong`"
                return c
            edit_source_row(root, sid, change)
        else:
            edit_source_row(root, sid, lambda c: c[:5] + [c[5].replace("`healthy: false`", "`healthy: true`")] + c[6:])
    elif leg == "C1_USEDBY_GROUNDED":
        sid = "S502" if PROFILE == "c02" else "S506"
        edit_source_row(root, sid, lambda c: c[:10] + ["corpus/knowledge/missing-development.md"])
    elif leg.startswith("C1_DERIV_TABLE:"):
        kind = leg.split(":", 1)[1]
        rel = {"fixture": FIXTURE_PATH, "body": RECEIPTS_DIR + "/raw/S506.body",
               "record": "corpus/live/runs/round-98/rea-doctor-r98.txt"}[kind]
        p = root / rel
        p.write_bytes(p.read_bytes() + b"\nfixture digest mutation\n")
    else:
        raise ValueError(f"unknown new delta {leg}")
    return root


def _set_other_row_cell(root, cid, newcell):
    rl = root / "corpus/README.md"
    out = []
    for ln in rl.read_text(encoding="utf-8").splitlines():
        c = cells(ln)
        if len(c) == 5 and c[0] == cid:
            c[2] = newcell
            ln = "| " + " | ".join(c) + " |"
        out.append(ln)
    rl.write_text("\n".join(out) + "\n", encoding="utf-8")
    return root


def _fixture_delta(root, kind):
    """Apply one forged-class delta to an honest fixture copy."""
    ep = root / ENTRY
    text = ep.read_text(encoding="utf-8")
    votes = root / VOTES_DIR
    if kind == "H1-indent-dup-status":
        lines = text.splitlines(True)
        lines.insert(3, "  admission-status: rejected\n")
        text = "".join(lines)
    elif kind == "F10-dup-status-fenced":
        text += "\n```\nadmission-status: admitted\n```\n"
    elif kind == "V10-stale-fetched-at":
        for sid in RECEIPT_ROW_IDS:
            rp = root / RECEIPTS_DIR / f"{sid}.receipt.json"
            r = json.loads(rp.read_text())
            r["fetched_at"] = "2026-10-01"
            rp.write_text(json.dumps(r, indent=1))
        return root
    elif kind == "V27-fabricated-body-foreign-host":
        sid = "S502"
        body = ("REA is a cloud-hosted SaaS scanner with agent connectors for every "
                "binary format on the market, according to this fabricated text.\n")
        p = root / RECEIPTS_DIR / "raw" / f"{sid}.body"
        p.write_text(body, encoding="utf-8")
        quote = "cloud-hosted SaaS scanner with agent connectors"
        i = body.index(quote)
        rec = {"schema": "revenger-quote-audit-v1", "sid": sid, "verdict": "verified",
               "fetch_url": "https://dlang.org/fabricated", "http_status": 200,
               "fetched_at": ROUND_DATE,
               "fetch_sha256": hashlib.sha256(body.encode()).hexdigest(),
               "length": len(body.encode()), "quote": quote,
               "span": {"start": i, "end": i + len(quote)}}
        (root / RECEIPTS_DIR / f"{sid}.receipt.json").write_text(json.dumps(rec, indent=1))
        return root
    elif kind == "V07-legacy-path":
        return _set_row_cell(root, "`legacy/" + ENTRY_REL + "` (round-95 admission)")
    elif kind == "V08-entry-pending":
        return _set_row_cell(root, "`knowledge/seed.md` (census; `" + ENTRY_REL
                             + "` pending admission)")
    elif kind == "V03-dup-json-keys-registry":
        raw = (root / REGISTRY_REL).read_text(encoding="utf-8")
        # a literal duplicate "CriticR96" member: json.loads last-wins keeps the pinned
        # role, so only a strict reader rejects it
        injected = raw.replace('"members": {',
                               '"members": {\n    "CriticR96": {"role": "reviewer"},', 1)
        if injected == raw:
            raise SystemExit("V03 delta: members anchor not found")
        (root / REGISTRY_REL).write_text(injected, encoding="utf-8")
        return root
    elif kind == "V04-dup-json-keys-vote":
        v = json.loads((votes / "CriticR96.json").read_text())
        raw = ('{"seat": "CriticR96", "role": "reviewer", "role": "critic", '
               f'"candidate_sha256": "{v["candidate_sha256"]}", "decisions": '
               + json.dumps(v["decisions"]) + ', "notes": ' + json.dumps(v["notes"])
               + ', "artifact_path": ' + json.dumps(v["artifact_path"])
               + ', "artifact_sha256": ' + json.dumps(v["artifact_sha256"]) + '}')
        (votes / "CriticR96.json").write_text(raw)
        return root
    elif kind == "V19-sid-suffix-spaced":
        text = text.replace("## Observation, inference, unknown",
                            "Per S0999a and S 0999 the atlas approach generalizes.\n\n"
                            "## Observation, inference, unknown")
    elif kind == "F16-unresolved-body-sid":
        text = text.replace("## Observation, inference, unknown",
                            "Per S0999 the atlas approach generalizes.\n\n"
                            "## Observation, inference, unknown")
    elif kind == "V18-na-letter-flood":
        for f in sorted(votes.glob("*.json")):
            v = json.loads(f.read_text())
            v["notes"] = {q: "n" * 30 for q in QS}
            f.write_text(json.dumps(v))
        return root
    elif kind == "F17-vacuous-na":
        v = json.loads((votes / "ReviewerGate.json").read_text())
        v["decisions"]["Q03"] = "n/a"
        v["notes"]["Q03"] = "-"
        (votes / "ReviewerGate.json").write_text(json.dumps(v))
    elif kind == "M6-forged-registry-seat":
        reg = json.loads((root / REGISTRY_REL).read_text())
        reg["members"]["FabA"] = {"role": "critic"}
        (root / REGISTRY_REL).write_text(json.dumps(reg, indent=1))
        return root
    elif kind == "M5-pycache-planted":
        d = root / "corpus" / "__pycache__"
        d.mkdir(parents=True, exist_ok=True)
        (d / "audit_source_quotes.cpython-314.pyc").write_bytes(b"\x00fake")
        return root
    elif kind == "F20-foreign-artifact-dir":
        v = json.loads((votes / "ReviewerBlind.json").read_text())
        foreign = root / f"{WAVE_DIR}/w1/ReviewerGate/blind-evidence.md"
        b = f"seat evidence for ReviewerBlind\ncandidate {v['candidate_sha256']}\n".encode()
        foreign.write_bytes(b)
        v["artifact_path"] = f"{WAVE_DIR}/w1/ReviewerGate/blind-evidence.md"
        v["artifact_sha256"] = hashlib.sha256(b).hexdigest()
        (votes / "ReviewerBlind.json").write_text(json.dumps(v))
        old = root / f"{WAVE_DIR}/w1/ReviewerBlind/blind-evidence.md"
        if old.is_file():
            old.unlink()
        return root
    elif kind == "F12-case-dup-seat":
        v = json.loads((votes / "ReviewerGate.json").read_text())
        v["seat"] = "reviewergate"
        (votes / "reviewergate.json").write_text(json.dumps(v))
    elif kind == "F13-role-mismatch":
        v = json.loads((votes / "CriticR96.json").read_text())
        v["role"] = "reviewer"
        (votes / "CriticR96.json").write_text(json.dumps(v))
    elif kind == "F15-traversal":
        v = json.loads((votes / "ReviewerBlind.json").read_text())
        v["artifact_path"] = WAVE_DIR + "/w1/ReviewerBlind/../../../../corpus/SOURCES.md"
        (votes / "ReviewerBlind.json").write_text(json.dumps(v))
    elif kind == "F18-ws-output":
        text += "\n```sh\n$ python3 -B corpus/lint_entry.py --help\n   \n\t\n```\n"
    elif kind == "F18b-tilde-fence":
        text += "\n~~~sh\n$ python3 -B corpus/lint_entry.py --help\nfabricated output\n~~~\n"
    elif kind == "F19-stale-new-row":
        sl = root / "corpus/SOURCES.md"
        sl.write_text(sl.read_text(encoding="utf-8").replace(
            f'"the documented route and the demonstrated session agree" | mined | {ROUND_DATE} |',
            '"the documented route and the demonstrated session agree" | mined | 2026-11-04 |', 1),
            encoding="utf-8")
        return root
    elif kind == "A4-shadow-admitted":
        sh = root / "corpus/knowledge/shadow-r96-notes.md"
        sh.write_text("source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
                      "admission-status: admitted\n\n# Shadow entry (forgery)\n", encoding="utf-8")
        return root
    elif kind == "A3-usedby-extra":
        sl = root / "corpus/SOURCES.md"
        sl.write_text(sl.read_text(encoding="utf-8").replace(
            f'| on-release | {ENTRY_REL} |',
            f'| on-release | {ENTRY_REL}, corpus/lessons/round-96.md |', 1),
            encoding="utf-8")
        return root
    elif kind == "M8-pycache-frozen-dir":
        d = root / "reports/round-94" / "__pycache__"
        d.mkdir(parents=True, exist_ok=True)
        (d / "x.cpython-314.pyc").write_bytes(b"\x00fake")
        return root
    elif kind == "ROWS-total-extra-row":
        rl = root / "corpus/README.md"
        t = rl.read_text(encoding="utf-8")
        marker = t.index("| C15 |")
        line_end = t.index("\n", marker)
        t = t[:line_end + 1] + ("| C16 | forged extra surface | `knowledge/shadow-r96-notes.md` | — | frontier |\n") + t[line_end + 1:]
        rl.write_text(t, encoding="utf-8")
        return root
    elif kind == "TRIO-missing-recheck":
        text = re.sub(r"(?m)^recheck:.*\n?", "", text)
    elif kind == "LINT-qmap-missing-row":
        text = text.replace("| Q08 | n/a | Historical criterion superseded by Q11, applied below. |\n", "")
    elif kind == "EMBEDDED-fake-fence":
        text += "\n```sh\n$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-96-native-analysis-sessions.md --lane .\nLINT_QMAP=99\nLINT_RC=0\n```\n"
    elif kind == "QUOTES-mutated-body":
        bp = root / RECEIPTS_DIR / "raw" / "S502.body"
        b = bp.read_text(encoding="utf-8")
        bp.write_text("XX" + b, encoding="utf-8")
        return root
    elif kind == "KHELDBACK-broken-cell":
        return _set_other_row_cell(root, "C01", "`knowledge/nonexistent-r96.md` (broken backing)")
    elif kind == "DECOR-shadow-admitted":
        sh = root / "corpus/knowledge/shadow-r96-decorated.md"
        sh.write_text("source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
                      "admission-status: admitted (round-96 gate, two reviewer votes)\n\n"
                      "# Shadow entry (decorated admitted line)\n", encoding="utf-8")
        return root
    elif kind == "ONLY-C10-second-row":
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
    ep.write_text(text, encoding="utf-8")
    return root


def _set_row_cell(root, newcell):
    rl = root / "corpus/README.md"
    out = []
    for ln in rl.read_text(encoding="utf-8").splitlines():
        c = cells(ln)
        if len(c) == 5 and c[0] == TARGET_ROW:
            c[2] = newcell
            ln = "| " + " | ".join(c) + " |"
        out.append(ln)
    rl.write_text("\n".join(out) + "\n", encoding="utf-8")
    return root


EXPECT_FAIL = {
    "H1-indent-dup-status": "C1_ADMITTED",
    "F10-dup-status-fenced": "C1_ADMITTED",
    "V10-stale-fetched-at": "C1_RECEIPTS",
    "V27-fabricated-body-foreign-host": "C1_RECEIPTS",
    "V07-legacy-path": "C1_TARGET_CITES",
    "V08-entry-pending": "C1_TARGET_CITES",
    "V03-dup-json-keys-registry": "C1_REGISTRY",
    "V04-dup-json-keys-vote": "C1_VOTES",
    "V19-sid-suffix-spaced": "C1_SIDS",
    "F16-unresolved-body-sid": "C1_SIDS",
    "V18-na-letter-flood": "C1_VOTES",
    "F17-vacuous-na": "C1_VOTES",
    "M6-forged-registry-seat": "C1_REGISTRY",
    "M5-pycache-planted": "C1_PYCACHE",
    "F20-foreign-artifact-dir": "C1_VOTES",
    "F12-case-dup-seat": "C1_VOTES",
    "F13-role-mismatch": "C1_VOTES",
    "F15-traversal": "C1_VOTES",
    "F18-ws-output": "C1_EMBED_NONVACUOUS",
    "F18b-tilde-fence": "C1_EMBED_NONVACUOUS",
    "F19-stale-new-row": "C1_SOURCES",
    "ONLY-C10-second-row": "C1_ONLY_TARGET",
    # r95-routed closes (each a discriminating forged delta of its own)
    "A4-shadow-admitted": "C1_ADMITTED_UNION",
    "A3-usedby-extra": "C1_SOURCES",
    "M8-pycache-frozen-dir": "C1_PYCACHE",
    "ROWS-total-extra-row": "C1_ROWS_TOTAL",
    "TRIO-missing-recheck": "C1_TRIO",
    "LINT-qmap-missing-row": "C1_LINT",
    "EMBEDDED-fake-fence": "C1_EMBEDDED",
    "QUOTES-mutated-body": "C1_QUOTES",
    "KHELDBACK-broken-cell": "C1_K_HELD_BACKED",
    "DECOR-shadow-admitted": "C1_ADMITTED_UNION",
}


def self_test(receipts_dir=None, work_base=None):
    """Both honest profiles, inherited c02 deltas, eight new deltas per profile."""
    import contextlib
    import io
    base = Path(work_base) if work_base else SCRATCH
    base.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="c1v7-selftest-", dir=base))
    fails, total = [], 0
    new_legs = ("C1_ROWSET", "C1_ENTRY_BYTES", "C1_HEADER_POSITION", "C1_VERIFIED_AT",
                "C1_VOTE_NOTES", "C1_OWNWORK_PATHS", "C1_QUOTE_BYTES", "C1_USEDBY_GROUNDED")
    def exercise(profile, label, root, expected=None):
        nonlocal total
        total += 1
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            legs, ok = evaluate(root)
        passed = (ok if expected is None else not legs.get(expected, True) and not ok)
        if receipts_dir:
            rd = Path(receipts_dir)
            rd.mkdir(parents=True, exist_ok=True)
            (rd / f"{profile}-{label}.log").write_text(out.getvalue() + f"SELFTEST_CASE_RC={0 if ok else 1}\n", encoding="utf-8")
        if not passed:
            fails.append(f"{profile}:{label}: expected {expected or 'pass'}; failing=" +
                         ",".join(k for k, v in legs.items() if not v))
    try:
        for profile in ("c02", "c14"):
            configure(profile)
            root, _ = _fixture(work)
            exercise(profile, "honest", root)
            shutil.rmtree(root.parent)
            for leg in new_legs:
                root, _ = _fixture(work)
                _new_delta(root, leg)
                exercise(profile, leg, root, leg)
                shutil.rmtree(root.parent)
            if profile == "c02":
                for kind, expected in EXPECT_FAIL.items():
                    root, _ = _fixture(work)
                    _fixture_delta(root, kind)
                    exercise(profile, kind, root, expected)
                    shutil.rmtree(root.parent)
            if profile == "c14":
                for kind in ("fixture", "body", "record"):
                    root, _ = _fixture(work)
                    _new_delta(root, "C1_DERIV_TABLE:" + kind)
                    exercise(profile, "DERIV-" + kind, root, "C1_DERIV_TABLE")
                    shutil.rmtree(root.parent)
            dn_work = Path(tempfile.mkdtemp(prefix="dn-", dir=work))
            frozen, err = materialize(FREEZE_REV, None, dn_work)
            if frozen is None:
                fails.append(f"{profile}:do-nothing archive: {err}")
            else:
                exercise(profile, "do-nothing", frozen, "C1_TARGET_HELD")
            shutil.rmtree(dn_work)
        print(f"SELFTEST_C1V7={'OK' if not fails else 'FAIL'} legs={total}")
        for failure in fails:
            print("SELFTEST FAIL:", failure)
        return 0 if not fails else 1
    finally:
        configure("c02")
        shutil.rmtree(work, ignore_errors=True)


def main(argv):
    import argparse
    global WORK_ARG
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=("c02", "c14"))
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--tree", type=Path)
    parser.add_argument("--rev")
    parser.add_argument("--work", type=Path)
    parser.add_argument("--receipts-dir", type=Path)
    args = parser.parse_args(argv)
    WORK_ARG = args.work
    if args.self_test:
        return self_test(args.receipts_dir, args.work)
    if args.profile is None:
        parser.error("--profile is required unless --self-test is given")
    if bool(args.tree) == bool(args.rev):
        parser.error("exactly one of --tree or --rev is required")
    configure(args.profile)
    base = args.work if args.work else SCRATCH
    base.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="c1v7-run-", dir=base))
    try:
        root, err = materialize(args.rev, args.tree, work)
        if root is None:
            print(f"could-not-evaluate: {err}")
            print("C1_VERDICT=fail")
            return 1
        legs, ok = evaluate(root)
        return 0 if ok else 1
    except (OSError, ValueError) as exc:
        print(f"C1_INPUT_WHY={exc}")
        print("C1_VERDICT=fail")
        return 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
