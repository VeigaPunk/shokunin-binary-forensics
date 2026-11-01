#!/usr/bin/env python
"""generator.py - builds the round-80 inert SQLite fixture and derives every
oracle-checked fact from the BUILT bytes (Q03/Q06: the record is checked
against byte-derived truth, never the reverse).

The fixture is a small SQLite 3 database (page_size 4096, UTF-8 encoding)
with two ordinary tables and their two implicit unique indexes:

    meta   (k TEXT PRIMARY KEY, v TEXT NOT NULL)     rows: 2
    samples(id INTEGER PRIMARY KEY, name TEXT UNIQUE, score REAL)  rows: 2

It is built by the Python stdlib sqlite3 module; the build is deterministic
(same library build + same statements => byte-identical file, asserted by the
regen mode). The database is inert: no code executes from it, the producer
declares the source database is never opened by SQLite or modified, and the
fixture is authored bytes on disk - an offline schema-inventory target.

Modes:
  python generator.py            # build fixture.db + truth.json + self-check
  python generator.py regen      # rebuild to regen-check.db, byte-compare

The self-check parses the built bytes directly:
  - file header: magic (0..16), page_size (u16@16), page_count (u32@28),
    text encoding (u32@56: 1=UTF-8), file size == page_size * page_count
  - page-1 table b-tree (sqlite_master, leaf type 13): cell pointer array,
    varint payload/rowid, record header serial types -> every schema object's
    (kind, tbl_name, rootpage) and stored CREATE sql text
  - column names derived from the stored CREATE TABLE sql (top-level comma
    split, constraint keywords skipped)

Every value written to truth.json is printed by the self-check from the built
bytes before truth.json is written. No value is copied from any producer
record.
"""
import hashlib
import json
import pathlib
import struct
import sys

PAGE_SIZE = 4096
CREATE_STMTS = [
    "CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT NOT NULL)",
    "CREATE TABLE samples (id INTEGER PRIMARY KEY, name TEXT UNIQUE, score REAL)",
]
META_ROWS = [("format", "revenger-sqlite-r80"), ("tables", "2")]
SAMPLE_ROWS = [(1, "alpha", 1.5), (2, "beta", 2.5)]

CONSTRAINT_KEYWORDS = {"PRIMARY", "UNIQUE", "CHECK", "FOREIGN", "CONSTRAINT"}


def build(path: pathlib.Path) -> None:
    import sqlite3

    if path.exists():
        path.unlink()
    c = sqlite3.connect(str(path))
    try:
        c.execute("PRAGMA page_size=%d" % PAGE_SIZE)
        c.execute(CREATE_STMTS[0])
        c.executemany("INSERT INTO meta (k, v) VALUES (?, ?)", META_ROWS)
        c.execute(CREATE_STMTS[1])
        c.executemany("INSERT INTO samples (id, name, score) VALUES (?, ?, ?)", SAMPLE_ROWS)
        c.commit()
    finally:
        c.close()


def u16(b, o):
    return struct.unpack(">H", b[o : o + 2])[0]


def u32(b, o):
    return struct.unpack(">I", b[o : o + 4])[0]


def varint(b, o):
    n = 0
    for i in range(9):
        c = b[o + i]
        if i == 8:
            return (n << 8) | c, o + 9
        n = (n << 7) | (c & 0x7F)
        if not c & 0x80:
            return n, o + i + 1
    raise ValueError("unreachable")


def serial_len(t):
    if t in (0, 8, 9):
        return 0
    if 1 <= t <= 4:
        return t
    if t == 5:
        return 6
    if t in (6, 7):
        return 8
    if t >= 13 and t % 2 == 1:
        return (t - 13) // 2
    if t >= 12:
        return (t - 12) // 2
    raise ValueError("serial type %d" % t)


def parse_sqlite_master(b):
    """Parse the page-1 table b-tree; return {name: (kind, tbl_name, rootpage, sql)}."""
    if b[:16] != b"SQLite format 3\x00":
        raise AssertionError("magic mismatch")
    page_type = b[100]
    assert page_type == 13, "page 1 expected to be a leaf table b-tree, got %d" % page_type
    ncells = u16(b, 103)
    cpa = 108
    found = {}
    for i in range(ncells):
        off = u16(b, cpa + 2 * i)
        plen, o = varint(b, off)
        _rowid, o = varint(b, o)
        payload = b[o : o + plen]
        hlen, ho = varint(payload, 0)
        types = []
        while ho < hlen:
            t, ho = varint(payload, ho)
            types.append(t)
        vals, vo = [], hlen
        for t in types:
            ln = serial_len(t)
            raw = payload[vo : vo + ln]
            vo += ln
            if t >= 13 and t % 2 == 1:
                vals.append(raw.decode("utf-8"))
            elif t == 0:
                vals.append(None)
            elif 1 <= t <= 6:
                vals.append(int.from_bytes(raw, "big", signed=True))
            else:
                vals.append(raw)
        kind, name, tbl, rootpage, sql = vals[0], vals[1], vals[2], vals[3], vals[4]
        found[name] = (kind, tbl, rootpage, sql)
    return found


def columns_from_create(sql):
    """Derive column names from a stored CREATE TABLE statement."""
    body = sql[sql.index("(") + 1 : sql.rindex(")")]
    parts, depth, cur = [], 0, ""
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    names = []
    for p in parts:
        tok = p.strip().split()[0].strip('"`[]')
        if tok.upper() in CONSTRAINT_KEYWORDS:
            continue
        names.append(tok)
    return names


def derive(db_path: pathlib.Path) -> dict:
    b = db_path.read_bytes()
    magic_ok = b[:16] == b"SQLite format 3\x00"
    assert magic_ok, "fixture magic mismatch"
    page_size = u16(b, 16)
    if page_size == 1:
        page_size = 65536
    page_count = u32(b, 28)
    encoding_code = u32(b, 56)
    assert page_size == PAGE_SIZE, "page_size %d != %d" % (page_size, PAGE_SIZE)
    assert len(b) == page_size * page_count, "size %d != %d*%d" % (len(b), page_size, page_count)
    assert encoding_code == 1, "encoding %d != 1 (UTF-8)" % encoding_code
    objs = parse_sqlite_master(b)
    truth = {
        "fixture_name": db_path.name,
        "fixture_sha256": hashlib.sha256(b).hexdigest(),
        "file_size": len(b),
        "page_size": page_size,
        "page_count": page_count,
        "encoding_code": encoding_code,
        "encoding_name": "UTF-8",
        "magic_ok": magic_ok,
        "objects": {},
        "views_expected": [],
        "triggers_expected": [],
    }
    for name, (kind, tbl, rootpage, sql) in sorted(objs.items()):
        entry = {"kind": kind, "table": tbl, "root_page": rootpage}
        if kind == "table":
            assert sql and sql.replace("\n", " ").startswith("CREATE TABLE"), name
            cols = columns_from_create(sql)
            entry["columns"] = cols
            entry["column_count"] = len(cols)
            entry["without_rowid"] = "WITHOUT ROWID" in sql.upper()
            entry["strict"] = "STRICT" in sql.upper()
            # byte-verify the authored statement really is stored in the built bytes
            assert sql.encode("utf-8") in b, "CREATE text not found in built bytes: %s" % name
        truth["objects"][name] = entry
        print("derived %s: kind=%s table=%s root_page=%d cols=%s" % (name, kind, tbl, rootpage, entry.get("columns")))
    print("derived fixture_sha256=%s file_size=%d page_size=%d page_count=%d encoding=%s" % (
        truth["fixture_sha256"], truth["file_size"], truth["page_size"], truth["page_count"], truth["encoding_name"]))
    return truth


def main() -> int:
    here = pathlib.Path(__file__).resolve().parent
    if len(sys.argv) == 2 and sys.argv[1] == "regen":
        build(here / "regen-check.db")
        a = (here / "fixture.db").read_bytes()
        c = (here / "regen-check.db").read_bytes()
        (here / "regen-check.db").unlink()
        if a != c:
            print("REGEN: DIFFER (%d vs %d bytes)" % (len(a), len(c)), file=sys.stderr)
            return 1
        print("REGEN: byte-identical (%d bytes)" % len(a))
        return 0
    if len(sys.argv) != 1:
        print("usage: generator.py [regen]", file=sys.stderr)
        return 2
    db = here / "fixture.db"
    build(db)
    truth = derive(db)
    (here / "truth.json").write_text(json.dumps(truth, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("truth.json written (%d objects)" % len(truth["objects"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
