# round-81 keyed-archive producer run — evidence ledger

- **Trigger**: round-81 C1 (coverage, F4 mapping revision) — the rea 6.8.0
  `rea-artifact-graph` provider reports `inspect_keyed_archive` `available: true`
  on this host (S457); the operation is in no F3 family set; an authored inert
  Foundation keyed archive makes the family's first real record manufacturable.
- **Action**: one bounded run, cwd = lane root:
  `rea inspect-keyed-archive corpus/fixtures/keyed-r81/fixture.plist --format json`
  (exact stdout saved as `inspection.json`, 3174 bytes, sha256
  `83fe4046ec51977b074e04e6cbee10e127be38a32a17bf32e14601fdde348fcf`;
  exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence `ev_6eb77fb0c3648cd34a7db9757bf2bd7709c30ffde0cbe0bc879de03002af4b73`
  (form `ev_<64hex>`), operation `inspect_keyed_archive`, provider
  `rea-artifact-graph`; `ORACLE OK (27/27 checks)` — every checked value derived
  from the built fixture bytes by `generator.py` (14/14 self-checks, regen
  byte-identical), never from the record (Q06).
- **Pointer**: `corpus/live/runs/round-81/{inspection.json, receipt.json,
  LEDGER.md, stderr.txt}`; fixture `corpus/fixtures/keyed-r81/`;
  oracle re-run over `git archive` bytes at adjudication.

## Q10 scope note

One authored inert 210-byte binary plist keyed archive; the producer's own
profile reads the object-reference graph (objects/roots/references) of that
snapshot. No class instantiation (the record's own limitation note: "Archive
classes are never instantiated"), no general keyed-archive format claim, no
NIB/storyboard or dylib-resolution claim (the family's other two operations
stay unrecorded), no encryption/WAL-style forensics scope.
