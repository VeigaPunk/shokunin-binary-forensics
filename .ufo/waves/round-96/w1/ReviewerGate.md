# ReviewerGate — scoped findings (revenger round 96, attempt 1)

Reviewer seat, lane-internal vote, disclosed as such. Scope: gate audit of the candidate entry
`corpus/knowledge/round-96-native-analysis-sessions.md` against `corpus/QUALITY.md` Q01–Q17 and
`reports/round-96/claims.md` C1. Artifact: `.ufo/waves/round-96/w1/ReviewerGate/gate-evidence.md`
(sha256 `fee94694022733df24c0a0d3713d5ce16a1431cddbd40b032ba789fb73ae761b`); vote:
`.ufo/waves/round-96/w1/ReviewerGate/vote.json` (self-checked against the frozen counter's vote-leg
rules: pinned seat/role, digest equality, 17 decisions with ≥1 PASS, vocabulary-compliant n/a notes,
artifact in own dir naming seat + digest, sha match, strict JSON).

## Verdict

11 PASS (Q01 Q02 Q03 Q04 Q05 Q06 Q09 Q10 Q11 Q14 Q16), 6 n/a (Q07 Q08 Q12 Q13 Q15 Q17).
No decision disagrees with the entry's own §Q-map; every disagreement-shaped finding is recorded
below and none flips a decision. Vote: gate met on the candidate entry.

## Verification performed (all outputs matched)

- Digest: normalized candidate digest re-derived = `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`;
  working-tree entry bytes equal freeze-commit bytes (`git show ff767436f…:<entry>` sha equal to the file's sha).
- Derivation table re-run end to end: fixture sha256 `fe060de1…` (1024 B); regen via
  `gen_pe_r75.py` byte-identical (cmp clean); Evidence ID `ev_cc0b9d88…`; provider ghidra/Ghidra/12.1.4;
  `function_count=1`; entry line `/// FUNC entry @ 140001000`; body `undefined8 entry(void){ return 0x2a; }`;
  `INFO  REPORT` count 6; all four record digests match the table's prefixes.
- Fixture premise from bytes: `xxd -s 0x200 -l 16` → `b82a 0000 00c3` = `B82A000000C3` (2×6 hex chars ✓,
  decodes to `mov eax,0x2A; ret` ✓), matching `truth.json` — Q03/Q06 ground is outside the records under test.
- Receipt side: S502 body 38167 B sha `c818ee34…`, S503 body 35095 B sha `b5f17fd…`, both HTTP 200,
  `fetched_at 2026-11-05`, commit-pinned URLs, fetch-log lines present (including the honest 404 disclosure);
  quote anchors verified inside the committed bodies (S502 L425 file-offset sentence, L285 "Native targets",
  L418 "DOS MZ with Ghidra", L420 `inspect_native_load_image`; S503 frontmatter decompile clause verbatim).
- Non-author re-fetch this session: both raw URLs re-opened; sha256 equal to the committed bodies (c818ee34…, b5f17fd…).
- Doctor receipt: `healthy: false`, hopper `missing_analysis_engine`, IDA unconfigured, all eight named ghidra
  scope checks `ok: true` — exactly the entry's claim set, no more.
- Sequencing fact (not a defect): `corpus/SOURCES.md` has no S502/S503/S504 rows in the working tree; claims
  §Frontier appends them at landing, and the frozen receipts pin the bodies meanwhile; the counter's C1_SOURCES
  leg operates on `--rev <landing>`.

## Findings

- F1 (minor, non-blocking): derivation-table row "decompiled body" cites `codeable-decompiled.c` lines 6–10,
  but `// decompiled_ok=1 of 1` sits at line 13 — the locator under-covers the last quoted member; the value
  itself is correct and was re-verified. Flagged against Q11/Q16; no decision flips.
- F2 (observation): doctor receipt additionally shows `skill:identity` stale and several `config_drift`
  registrations — consistent with the entry's disclosed installed-copy (6.7.0-era) vs pinned-revision drift;
  no undisclosed claim.

## Bounds compliance

Writes: only `.ufo/waves/round-96/w1/ReviewerGate/{gate-evidence.md,vote.json}` and this file.
Scratch `/fast/scratch/hyaku/revenger-r96/ReviewerGate/` created and deleted before this report was finished;
all receipts are recorded here. All Python invocations used `python3 -B`. No lane files, no registry/state,
no git/jj write commands, no subagent dispatch, no hosts outside the task-named URLs touched.
