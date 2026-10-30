#!/usr/bin/env python3
"""Round-74 frozen quote-audit counter; network-free over a committed archive.

Claim C2 predicate (frozen before any seat fetch): every required registry row
resolves to a receipt whose verdict is `verified` (quote verbatim at its recorded
span in the committed fetched bytes, sha256-bound) or `unreachable` (>=2 distinct
fetch attempts with status/error evidence), and the S071 historical drift quote
must stay absent from the S427 body (negative control).
"""
import argparse, hashlib, json, re, sys
from pathlib import Path

RANGE = list(range(54, 96))                    # S054..S095, the round-72 registry block
MANUAL = [115, 130, 131, 343, 379, 380, 381, 398, 400]  # verify_quotes.log MANUAL rows
AUDIT = ".ufo/waves/round-74/quote-audit"
SCHEMA = "revenger-quote-audit-v1"
S071_HISTORICAL_QUOTE = "Each repo is read and security-graded"
MIN_VERIFIED = 40


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def parse_rows(path):
    rows = {}
    for line in path.read_text().splitlines():
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) == 11 and re.fullmatch(r"S\d{3,}", cells[0]):
            if cells[0] in rows:
                print("could-not-evaluate: duplicate registry id"); raise SystemExit(2)
            rows[cells[0]] = cells
    return rows


def sup_map(rows):
    out = {}
    for sid, cells in rows.items():
        m = re.match(r"^supersedes (S\d{3,})\b", cells[6])
        if m and m.group(1) not in out:
            out[m.group(1)] = sid
    return out


def terminal(rows, sup, sid):
    for _ in range(10):
        if sid in sup:
            sid = sup[sid]
    return sid


def eval_sid(t, rows, sup, sid):
    term = terminal(rows, sup, sid)
    rp = t / AUDIT / f"{term}.receipt.json"
    try:
        r = json.loads(rp.read_text())
    except (OSError, ValueError):
        return term, "unresolved", "receipt missing/unreadable"
    if r.get("schema") != SCHEMA or r.get("sid") != term:
        return term, "unresolved", "schema/sid mismatch"
    if r.get("verdict") == "verified":
        need = ("fetch_sha256", "length", "quote", "span", "http_status", "fetched_at", "fetch_url")
        if any(k not in r for k in need):
            return term, "unresolved", "missing receipt fields"
        bp = t / AUDIT / "raw" / f"{term}.body"
        try:
            body = bp.read_bytes()
        except OSError:
            return term, "unresolved", "body missing"
        if hashlib.sha256(body).hexdigest() != r["fetch_sha256"] or len(body) != r["length"]:
            return term, "unresolved", "body digest/length mismatch"
        try:
            text = body.decode("utf-8")
        except UnicodeDecodeError:
            return term, "unresolved", "body not utf-8"
        nq, nb = norm(r["quote"]), norm(text)
        s, e = r["span"]["start"], r["span"]["end"]
        if not nq or nq not in nb or not (0 <= s < e <= len(text)) or norm(text[s:e]) != nq:
            return term, "unresolved", "quote/span check failed"
        return term, "verified", "ok"
    if r.get("verdict") == "unreachable":
        att = r.get("attempts") or []
        if len(att) >= 2 and len({a.get("url", "") for a in att}) >= 2 and \
                any(a.get("status") or a.get("error") for a in att):
            return term, "unreachable", "ok"
        return term, "unresolved", "unreachable evidence insufficient"
    return term, "unresolved", f"verdict {r.get('verdict')!r}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("tree", type=Path)
    a = p.parse_args()
    t = a.tree
    if not (t / "corpus/SOURCES.md").is_file():
        print("could-not-evaluate: missing corpus inputs")
        return 2
    rows = parse_rows(t / "corpus/SOURCES.md")
    sup = sup_map(rows)
    states = {}
    for n in RANGE:
        term, st, why = eval_sid(t, rows, sup, f"S{n:03d}")
        states[f"S{n:03d}"] = (term, st, why)
    mstates = {}
    for n in MANUAL:
        term, st, why = eval_sid(t, rows, sup, f"S{n:03d}")
        mstates[f"S{n:03d}"] = (term, st, why)

    def count(st_map):
        v = sum(1 for _, s, _ in st_map.values() if s == "verified")
        u = sum(1 for _, s, _ in st_map.values() if s == "unreachable")
        x = sum(1 for _, s, _ in st_map.values() if s == "unresolved")
        return v, u, x

    rv, ru, rx = count(states)
    mv, mu, mx = count(mstates)
    terms = {sid: tr for sid, (tr, _, _) in states.items()}
    nterm = len(set(terms.values()))

    neg = "n/a (S427 receipt not verified)"
    s427_state = states.get("S071", ("", "", ""))[1]  # S071's terminal is S427
    if s427_state == "verified":
        try:
            body = (t / AUDIT / "raw/S427.body").read_bytes()
            nb = norm(body.decode("utf-8"))
            neg = "fail (historical S071 quote present)" if norm(S071_HISTORICAL_QUOTE) in nb \
                else "pass"
        except (OSError, UnicodeDecodeError):
            neg = "n/a (S427 body unreadable)"

    target = (rx == 0 and mx == 0 and (rv + mv) >= MIN_VERIFIED and neg == "pass")
    print(f"QA_RANGE_ROWS={len(RANGE)} QA_TERMINALS={nterm}/{len(RANGE)}")
    print(f"QA_VERIFIED={rv}/42 QA_UNREACHABLE={ru}/42 QA_UNRESOLVED={rx}/42")
    print(f"QA_MANUAL_VERIFIED={mv}/9 QA_MANUAL_UNREACHABLE={mu}/9 QA_MANUAL_UNRESOLVED={mx}/9")
    print(f"QA_VERIFIED_TOTAL={rv + mv}/51 (target >= {MIN_VERIFIED})")
    for sid, (tr, st, why) in sorted(states.items()):
        if st == "unresolved":
            print(f"QA_UNRESOLVED_ROW {sid} terminal={tr} why={why}")
    for sid, (tr, st, why) in sorted(mstates.items()):
        if st == "unresolved":
            print(f"QA_MANUAL_UNRESOLVED_ROW {sid} terminal={tr} why={why}")
    print(f"QA_NEGCTRL={neg}")
    print(f"QA_TARGET={'yes' if target else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
