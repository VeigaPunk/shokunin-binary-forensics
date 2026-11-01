# round-80 run ledger — sqlite family record through the current producer

One bounded, static, non-executing producer run, saved as producer-emitted bytes:

- fixture: `corpus/fixtures/sqlite-r80/fixture.db` (authored inert SQLite 3 database,
  page_size 4096, UTF-8, two ordinary tables `meta(k,v)` / `samples(id,name,score)`
  plus their two implicit unique indexes; generator `generator.py` byte-verifies its
  own premises — header magic/widths, page count, encoding code, and a page-1
  sqlite_master b-tree parse deriving every object's kind/table/root_page and stored
  CREATE sql — and regenerates byte-identically; truth pin `truth.json`, fixture
  sha256 `30703cce38a43ce7b01f4c3ba2a96d916da623ff79beb64e3c9b17ee5c8fbed8`). The
  database is an offline schema-inventory target: no code executes from it and the
  producer declares the source database and WAL are never opened by SQLite or
  modified. No real application data exists here (authored rows: 2 meta pairs,
  2 sample tuples).
- record: `inspection.json` = the exact stdout of
  `rea inspect-sqlite-database <fixture> --schema-scope database --format json`
  (rea 6.8.0, provider `sqlite`, SQLite 3.53.4 worker), stdout sha256
  `a9c190cd52ff96190a756338a48b81ddc4f07fc36db12ab41a6f512e5482b6b7`, exit 0, stderr
  empty; receipt in `receipt.json`.
- identity oracle: `python -B ../../fixtures/sqlite-r80/oracle_check.py
  ../../fixtures/sqlite-r80/truth.json inspection.json
  ../../fixtures/sqlite-r80/fixture.db` → `ORACLE OK (34/34 checks)`:
  operation `inspect_sqlite_database`, provider id `sqlite`, engine SQLite,
  database_encoding UTF-8 (byte-derived: header offset 56 == 1), artifact
  bytes 20480 == 5 × 4096 (byte-derived), wal null, schema scope database /
  completeness complete, tables {meta root 2, columns [k,v]; samples root 4,
  columns [id,name,score]} (root pages and column lists byte-derived from the
  page-1 sqlite_master parse and the stored CREATE sql), indexes
  {sqlite_autoindex_meta_1 → meta root 3; sqlite_autoindex_samples_1 → samples
  root 5} (byte-derived), views/triggers empty, rows null (not requested),
  confidence observed, authority shipped-artifact, evidence id form `ev_<64hex>`
  and distinct from both rehearsal records — the producer's own parser derived
  exactly the authored structure from the authored bytes.
- observation vs inference vs unknown: the record's structural fields are observations
  (producer-derived from committed bytes); that the F3 counter counts this family is a
  predicate evaluation (mapping revision frozen in `reports/round-80/claims.md` before
  the run); whether the closure judge accepts the family move as an honest coverage
  improvement is outside this ledger (unknown, adjudicated externally).
- Scope (Q10): this record grounds the `sqlite` family — bundled SQLite databases as
  shipped-artifact surfaces. It demonstrates schema-inventory reading of ONE authored
  fixture by ONE built-in provider version; it is not a claim about row sampling
  (rows unrequested), WAL pairs, encrypted databases, or general database forensics
  (the producer's own limitations exclude those from this profile).
- Scratch probes that informed this run (not evidence): the shape pre-probe is
  committed at `reports/round-80/preprobe-sqlite-shape.log` (refused iterations
  disclosed there: default YAML form refused for the r79 `--format json` discipline;
  a u16-vs-u32 header-width parse bug self-caught; an oracle check-id collision
  fixed).
