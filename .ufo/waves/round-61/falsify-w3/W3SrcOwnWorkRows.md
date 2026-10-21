GRADE: HOLDS — Own-work rows S026/S027 (tier-A legitimacy + lesson anchors/quotes)

Attack target: S026/S027 in corpus/SOURCES.md; anchors+quotes at
corpus/lessons/round-61.md:65-66; landed ab580698212258a55e43e9bb9bf6ac78c91eae2a
(extracted to /tmp/revenger-r61w3-W3SrcOwnWorkRows, verified against live tree:
diff -q SAME on SOURCES.md, round-61.md, both knowledge entries, README).
No live-target probing; no REA producer; read-only git/orchestration.

1) TIER-A LEGITIMACY — HOLDS.
CORPUS.md (fleet root) tier A = "primary or authoritative for that scope
(spec, official docs, source code, original paper, maintainer statement,
the lane's own re-runnable gate output)". For scope "what the saved record
contains", the saved record is the primary/authoritative source (the artifact
itself). This mirrors established precedent in the same registry: S013
(own-work, tier A, saved r59 REA record), S001/S014/S015 (own-work tier A).
Verified the observed scope is fixture-limited ("for fixtures evm-r19,
evm-r21..r26" / "js-r3, js-r7-v2"), not a general provider claim, so the A
is scoped correctly.

2) S026 SCOPE CHECK — accurate.
- Exactly 7 inspect_evm_interface records in corpus/live/runs: rounds 19,21,22,
  23,24,25,26 (grep -rl '"operation": *"inspect_evm_interface"' -> those 7
  files only). Round-20 has no inspection.json (ledger # Round 20 = verify pass).
- Record provider id "evmole-interface", version "evmole@0.9.3" in all 7
  (python readback). Subject.local_path matches fixtures evm-r19/evm-r21..r26.
- Anchor Evidence-ID prefixes match the files in order: r19 ev_0ad0097e,
  r21 ev_4810eda7, r22 ev_24fe0001, r23 ev_296e7ed7, r24 ev_50d5ffb1,
  r25 ev_23a9464b, r26 ev_482e41e6. All 7 present at SOURCES.md:40, in order.
- Record content matches entry observations: r19/r21 report selector
  0xdeadbeef@16; r22 0xaaaaaaaa@30 & 0xbbbbbbbb@32; r23-r26 functions=[],
  evidence_kind=inferred, discovery_completeness=unknown,
  runtime_execution=not-performed. Reproduce block output == entry Provenance
  (EVM: diff True; JS: diff True on archive).

3) S027 SCOPE CHECK — accurate.
- Both named files exist: 20261012T164357Z/analysis.json and round-7/
  v2-analysis.json; operations analyze_javascript_application; subjects
  js-r3/js-r7-v2; Evidence IDs ev_4a93276c… / ev_66f5dc7e… match exactly.
- "Two" is correct for these fixtures: other saved analyze_javascript_application
  records (round-12 v1/v2/v1-direct/v2-direct) are for shapes-r12 (subjects
  v1/v2, per-file shas df0badbf…/3f3521c6…), not js-r3/js-r7-v2.
- Per-file identity digests in the graphs match current fixture files
  (v1: index.js f7d8bf47…, transform.js cd9f3f63…, package.json 92ef8e3d…;
  v2: index.js b53d96d4…). Old checkout trees are byte-identical
  (diff -r IDENTICAL, both JS pairs and all 7 EVM fixtures).
- Subject *directory* digests (8eec9ffb…/696c2496…) were not reproducible by
  any of 9 candidate methods; entry honestly labels them "recorded, not
  re-derived; hashing method was not reproduced" (Q09-compliant).

4) LESSON QUOTES EXIST — HOLDS.
- round-61.md:65 (S026): `"functions":[]` and `"runtime_execution":
  "not-performed"` present byte-exact in round-26/inspection.json (offsets
  690, 1224, 1274).
- round-61.md:66 (S027): `"resolution_context":"package-entrypoint"` present
  byte-exact in 20261012T164357Z/analysis.json (3 occurrences).
- Section preamble provides access date (2026-10-21) and ≤25-word quotes.
- Used-by targets exist (both knowledge files, census clean, malformed=0,
  duplicate ids=0, no tier-inflation, mined used-by paths all exist).

PARTIAL/ANCILLARY NITS (do not break the verdict):
- SOURCES.md:40 anchor: "full IDs and file digests in the citing entry" —
  the entry carries full Evidence IDs (7) but file digests as 16-hex prefixes
  (file_sha256=e892dd18ff219f71 etc.), not full 64-hex; the derive command is
  present (Q11 ok), only "full … file digests" is loose wording.
- Scope cells attribute `rea-agents@6.4.0`, which lives in sibling LEDGERs
  (verified: rounds 19,21-26 and 20261012T164357Z/round-7 ledgers all cite
  rea-agents@6.4.0), not inside the inspection/analysis JSON (whose provider
  field is evmole@0.9.3 / JS version "1"). Supportable, but sourced indirectly.
- SOURCES.md:7-9 header says all row quotes are in lessons/round-1.md, but
  S016-S027 quotes are in lessons/round-61.md (reference drift in the header;
  does not affect existence of the checked quotes).
- Lesson quote strings occur multiple times in each JSON (functions:[] x2;
  resolution_context x3), so the quoted "location" is not unique within file —
  minor.

VERDICT: Own-work saved records S026/S027 are legitimately tier A for the
narrow "what the saved records report" scope (precedent S013; scope fixture-
limited; content independently re-derived and matching). Their anchors and the
quotes at corpus/lessons/round-61.md:65-66 exist verbatim in the named files on
ab58069. HOLDS, with the low-severity wording/drift nits above.

Installs: none.
