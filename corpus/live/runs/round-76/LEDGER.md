# round-76 run ledger — managed family record through the current producer

One bounded, static, non-executing producer run, saved as producer-emitted bytes:

- fixture: `corpus/fixtures/managed-r76/fixture.dll` (authored inert minimal
  managed PE/CLI; generator `generator.py` byte-verifies its own premises and
  regenerates byte-identically; truth pin `truth.json` sha256
  `25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c`).
- record: `inspection.json` = the exact stdout of
  `rea inspect-managed-artifact <fixture> --format json` (rea 6.8.0, provider
  `rea-dotnet-static`), stdout sha256 `9da6800db9a8139f74edf51c72e06453422fed4172af89384595becc77b0c65c`,
  exit 0, stderr empty; receipt in `receipt.json`.
- identity oracle: `python -B ../../fixtures/managed-r76/oracle_check.py
  ../../fixtures/managed-r76/truth.json inspection.json
  ../../fixtures/managed-r76/fixture.dll` → `ORACLE OK (10/10 checks)`:
  operation `inspect_managed_artifact`, classification `managed`
  (metadata-only), module `r76-managed.dll`, assembly `r76-managed` `1.2.3.4`,
  all five stream names, subject digest == fixture sha256 — the producer's own
  parser derived exactly the authored identity from the authored bytes.
- observation vs inference vs unknown: the record's identity fields are
  observations (producer-derived from committed bytes); that the F counter
  counts this family is a predicate evaluation (counter bytes committed);
  whether the closure judge accepts the family move as an honest coverage
  improvement is outside this ledger (unknown, adjudicated externally).
- F is presence-only (routed debt, r63): this ledger's claim text is the gate —
  a real current-producer record on a real managed artifact, not a
  counter-only flip.

Scratch probes that informed this run (not evidence): android family gate
(`capability_unavailable`, needs caller-supplied `REA_JADX_MCP_JAR`),
firmware 6.8.0 route gate (Linux + caller-supplied `REA_BINWALK_COMMAND`),
browser family (needs caller-supplied CDP endpoint) — see
`corpus/lessons/round-76.md`.
