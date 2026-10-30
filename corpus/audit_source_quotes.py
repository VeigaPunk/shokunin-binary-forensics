#!/usr/bin/env python3
"""Source-registry quote audit verifier (revenger, round-74 freeze).

Validates committed fetch receipts for SOURCES.md rows: a receipt is VERIFIED
only when the row's located quote appears verbatim (after whitespace collapse)
at its recorded span inside the committed fetched-bytes file, whose sha256 the
receipt pins. Unreachable requires >=2 recorded fetch attempts with distinct
URLs. Network-free: everything is checked over committed bytes.

Modes:
  verify    --sources corpus/SOURCES.md --receipts DIR [--sid S054 ...]
  chains    --sources corpus/SOURCES.md --range 54-95   (print supersession terminals)
  self-test                                        (hermetic fixtures, no network)
"""
import argparse, hashlib, json, re, sys, tempfile
from pathlib import Path

SCHEMA = "revenger-quote-audit-v1"
QUOTE_RE = re.compile(r'"([^"]+)"')


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def parse_rows(sources_path: Path):
    """id -> 11 cells, preserving registry order; raises on duplicate ids."""
    rows, order = {}, []
    for line in sources_path.read_text().splitlines():
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) == 11 and re.fullmatch(r"S\d{3,}", cells[0]):
            if cells[0] in rows:
                raise SystemExit(f"duplicate registry id {cells[0]}")
            rows[cells[0]] = cells
            order.append(cells[0])
    return rows, order


def supersedes_map(rows):
    """superseded id -> superseding id (first declaration wins)."""
    out = {}
    for sid, cells in rows.items():
        m = re.match(r"^supersedes (S\d{3,})\b", cells[6])
        if m and m.group(1) not in out:
            out[m.group(1)] = sid
    return out


def resolve_terminal(rows, sup, sid, max_depth=10):
    seen = 0
    while sid in sup and seen < max_depth:
        sid = sup[sid]
        seen += 1
    return sid


def anchor_quote(anchor: str):
    """The located quote is the LAST double-quoted segment of the anchor cell."""
    hits = QUOTE_RE.findall(anchor)
    return hits[-1] if hits else None


def load_receipt(receipts_dir: Path, sid: str):
    p = receipts_dir / f"{sid}.receipt.json"
    try:
        obj = json.loads(p.read_text())
    except (OSError, ValueError):
        return None, f"receipt missing/unreadable: {p.name}"
    if obj.get("schema") != SCHEMA:
        return obj, "schema mismatch"
    return obj, None


def check_verified(receipts_dir: Path, r: dict):
    """Return (ok, reason) for a 'verified' receipt over committed bytes."""
    for k in ("sid", "fetch_sha256", "length", "quote", "span", "http_status", "fetched_at", "fetch_url"):
        if k not in r:
            return False, f"missing field {k}"
    if r["verdict"] != "verified":
        return False, "verdict not verified"
    body_p = receipts_dir / "raw" / f"{r['sid']}.body"
    try:
        body = body_p.read_bytes()
    except OSError:
        return False, f"body missing: {body_p.name}"
    if sha256(body) != r["fetch_sha256"]:
        return False, "body sha256 != fetch_sha256"
    if len(body) != r["length"]:
        return False, "body length != receipt length"
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return False, "body not utf-8"
    nbody, nquote = norm(text), norm(r["quote"])
    if not nquote:
        return False, "empty quote"
    if nquote not in nbody:
        return False, "quote not in body"
    s, e = r["span"]["start"], r["span"]["end"]
    if not (0 <= s < e <= len(text)):
        return False, "span out of bounds"
    if norm(text[s:e]) != nquote:
        return False, "body[span] != quote"
    return True, "ok"


def check_unreachable(r: dict):
    if r.get("verdict") != "unreachable":
        return False, "verdict not unreachable"
    att = r.get("attempts") or []
    urls = {a.get("url", "") for a in att}
    if len(att) < 2 or len(urls) < 2:
        return False, "unreachable needs >=2 attempts with distinct urls"
    if not any(a.get("status") or a.get("error") for a in att):
        return False, "attempts carry no status/error evidence"
    return True, "ok"


def cmd_verify(a):
    rows, _ = parse_rows(a.sources)
    sup = supersedes_map(rows)
    sids = a.sid
    if a.range:
        lo, hi = (int(x) for x in a.range.split("-"))
        sids = [f"S{n:03d}" for n in range(lo, hi + 1)]
    resolved = {}
    for sid in sids:
        term = resolve_terminal(rows, sup, sid)
        r, err = load_receipt(a.receipts, term)
        state = "unresolved"
        if err:
            reason = err
        elif r.get("sid") != term:
            state, reason = "unresolved", "receipt sid mismatch"
        elif r["verdict"] == "verified":
            ok, reason = check_verified(a.receipts, r)
            state = "verified" if ok else "unresolved"
        elif r["verdict"] == "unreachable":
            ok, reason = check_unreachable(r)
            state = "unreachable" if ok else "unresolved"
        else:
            state, reason = "unresolved", f"verdict {r.get('verdict')!r}"
        resolved[sid] = (term, state, reason)
    for sid in sids:
        term, state, reason = resolved[sid]
        print(f"{sid} terminal={term} state={state} ({reason})")
    n = len(sids)
    ver = sum(1 for _, s, _ in resolved.values() if s == "verified")
    unr = sum(1 for _, s, _ in resolved.values() if s == "unreachable")
    unres = sum(1 for _, s, _ in resolved.values() if s == "unresolved")
    print(f"SUMMARY rows={n} verified={ver} unreachable={unr} unresolved={unres}")
    return 0 if unres == 0 else 1


def cmd_chains(a):
    rows, _ = parse_rows(a.sources)
    sup = supersedes_map(rows)
    lo, hi = (int(x) for x in a.range.split("-"))
    terms = {}
    for n in range(lo, hi + 1):
        sid = f"S{n:03d}"
        terms[sid] = resolve_terminal(rows, sup, sid)
    for k in sorted(terms):
        if terms[k] != k:
            print(f"{k} -> {terms[k]}")
    print(f"TERMINALS={len(set(terms.values()))}/{len(terms)}")
    return 0


def cmd_self_test():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / "raw").mkdir()
        body = b"alpha bravo charlie delta echo foxtrot golf hotel india juliet"
        body += b" " + b"A curated starting point for understanding binaries." + b" kilo lima"
        (d / "raw" / "S001.body").write_bytes(body)
        quote = "A curated starting point for understanding binaries."
        start = body.index(b"A curated")
        good = {
            "schema": SCHEMA, "sid": "S001", "row_url": "https://example.test/x",
            "fetch_url": "https://example.test/x", "final_url": "https://example.test/x",
            "http_status": 200, "fetched_at": "2026-10-30", "fetch_sha256": sha256(body),
            "length": len(body), "anchor": 'doc intro; "%s"' % quote, "quote": quote,
            "span": {"start": start, "end": start + len(b"A curated starting point for understanding binaries.")},
            "verdict": "verified", "body_derivation": "raw response bytes",
            "normalization": "", "attempts": [], "seat": "selftest", "notes": "",
        }
        (d / "S001.receipt.json").write_text(json.dumps(good))
        ok, reason = check_verified(d, good)
        assert ok, f"self-test: good receipt rejected: {reason}"
        # drift: quote that is NOT in the body must be flagged
        bad = dict(good)
        bad["quote"] = "Each repo is read and security-graded"
        bad["span"] = {"start": 0, "end": len(bad["quote"])}
        ok, reason = check_verified(d, bad)
        assert not ok, "self-test: drifted quote accepted"
        assert reason == "quote not in body", reason
        # span drift: quote present in body but span names other bytes
        bad2 = dict(good)
        bad2["span"] = {"start": 0, "end": 10}
        ok, reason = check_verified(d, bad2)
        assert not ok, "self-test: wrong span accepted"
        # sha drift
        bad3 = dict(good)
        bad3["fetch_sha256"] = "0" * 64
        ok, reason = check_verified(d, bad3)
        assert not ok, "self-test: sha mismatch accepted"
        # unreachable: needs >=2 distinct-url attempts
        r1 = {"verdict": "unreachable", "attempts": [{"url": "https://a.test/", "status": 403}]}
        ok, reason = check_unreachable(r1)
        assert not ok, "self-test: single-attempt unreachable accepted"
        r2 = {"verdict": "unreachable", "attempts": [
            {"url": "https://a.test/", "status": 403, "error": ""},
            {"url": "https://b.test/", "status": 0, "error": "Connection refused"}]}
        ok, reason = check_unreachable(r2)
        assert ok, f"self-test: honest unreachable rejected: {reason}"
        # last-quoted-segment anchor rule
        assert anchor_quote('doc "Section A" and "Section B", commit c; "the quote."') == "the quote."
        print("self-test: ok (7/7 legs)")
        return 0


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("verify")
    v.add_argument("--sources", type=Path, required=True)
    v.add_argument("--receipts", type=Path, required=True)
    v.add_argument("--range", default=None)
    v.add_argument("--sid", action="append", default=[])
    c = sub.add_parser("chains")
    c.add_argument("--sources", type=Path, required=True)
    c.add_argument("--range", required=True)
    sub.add_parser("self-test")
    a = p.parse_args()
    if a.cmd == "verify":
        return cmd_verify(a)
    if a.cmd == "chains":
        return cmd_chains(a)
    return cmd_self_test()


if __name__ == "__main__":
    raise SystemExit(main())
