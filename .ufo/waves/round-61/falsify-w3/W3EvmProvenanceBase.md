GRADE: PARTIAL — C09 `verified-at` names base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (corpus/knowledge/evm-saved-interface-candidates.md:2); the Reproduce output is byte-identical at every base I ran, but the named commit cannot be the base at which this entry was verified (the file, its source rows and its quality rows do not exist there).

Seat RevengerR61-2.W3EvmProvenanceBase. Extracted archives (never the live tree; no git/jj mutation, no bytecode executed, no REA call, no RPC):
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar <c> | tar -x -C /tmp/revenger-r61w3-W3EvmProvenanceBase/<c>` for cf02419, e0a4b0c, 0b6ddf07, ab580698.

## F1 — the requested reproduction holds exactly (observation)
Block extracted from the ab580698 entry (`## Reproduce`, sha256 `9c64f619c6d74931b17196f7dee7e439c2d42d2853343ad01bd3c327e4eccfeb`; the block at 0b6ddf07 is byte-identical — same sha — so equality below is not a coincidence of one tree). Run with `python3 -B` from each tree root:

| tree | exit | stderr | sha256 of stdout |
|---|---|---|---|
| cf02419 (claim base) | 0 | empty | `0480a2f78af46082b6cb82f51a6816965fef4b0e3f86cbda6e1bb8a38c722d49` |
| e0a4b0c (named base) | 0 | empty | `0480a2f78af46082b6cb82f51a6816965fef4b0e3f86cbda6e1bb8a38c722d49` |
| 0b6ddf07 | 0 | empty | `0480a2f78af46082b6cb82f51a6816965fef4b0e3f86cbda6e1bb8a38c722d49` |
| ab580698 (landed) | 0 | empty | `0480a2f78af46082b6cb82f51a6816965fef4b0e3f86cbda6e1bb8a38c722d49` |

The `## Provenance` text block of the ab580698 entry, extracted verbatim, hashes to the same `0480a2f7…` and compares byte-identical to the observed stdout (python `prov==obs: True`). Root cause of the invariance: `git archive <c> corpus/fixtures corpus/live | tar -xO | sha256sum` = `8b46fecfd15e0d01e0c96564a0cf234964229e174bc1aced11f8d0f9b1deead1` at cf02419, e0a4b0c, 0b6ddf07, 0597e53 and ab580698 — the block's inputs never moved. No value in the entry is contradicted by this attack.

## F2 — `verified-at` names a commit where the entry and its own supports do not exist (defect, naming only)
- `git cat-file -e e0a4b0c:corpus/knowledge/evm-saved-interface-candidates.md` → fatal: path does not exist in 'e0a4b0c'. The entry first landed at 0b6ddf0 (`git log --oneline -- corpus/knowledge/evm-saved-interface-candidates.md` → 0597e53, 0b6ddf0) and its current text landed at 0597e53 (`git diff 0b6ddf07 ab580698 -- …` = the `embedded_pattern_offsets` sentence only).
- At e0a4b0c, `corpus/SOURCES.md` has rows S001–S015 only (`git show e0a4b0c:corpus/SOURCES.md | grep -o '^| S0[0-9][0-9]'` → S001…S015); the entry's `source:` header (line 1) cites S016–S019 and S026, which exist only from 0b6ddf0 (`git log -S'| S026 |' -- corpus/SOURCES.md` → 0b6ddf0).
- At e0a4b0c, `corpus/QUALITY.md` has Q01–Q11 only (`git show e0a4b0c:corpus/QUALITY.md | grep -o '^| Q[0-9][0-9]'` → Q01…Q11); the entry's QUALITY table (lines 178–190) cites Q12 and Q13, added in 0b6ddf0 (`git log -S'| Q13 |' -- corpus/QUALITY.md` → 0b6ddf0).
- Terminology conflict with the lane's own documents: claims.md:6 calls cf02419 the "Claim base" and corpus/lessons/round-61.md:3-4 calls e0a4b0c the "pre-registration" commit. The entry calls e0a4b0c the "lane base" — a third label for it. Same wording in the sibling C04 entry (commonjs-destructured-require-edges.md:2), so this is a lane-wide convention, not a C09-specific slip.
- Fix: `verified-at` should name 0597e5336fd67654c974fcb05f73353f44d868b9 (the commit carrying the entry's current text) or the landed ab580698212258a55e43e9bb9bf6ac78c91eae2a; e0a4b0c may remain as the base the fixture/record bytes were read at, which is exactly what the invariant in F1 supports.

## F3 — one statement in the current text has no in-entry derivation (observation, cross-seat)
Entry lines 88-90 state that `evm-r24/truth.json` `embedded_pattern_offsets` `[1, 9]` is "the inclusive byte span of the one 9-byte pattern occurrence (offsets 1–9, authoring note `LOG.md:289`)". The `## Reproduce` block does not derive that: it prints only `raw_0x63=[1]` for r24 and never searches the 9-byte pattern `63deadbeef14601057`. The derivation lives outside the entry — reports/round-61/measure-after.log (`R24_SPAN [[1, 9]]`), .ufo/waves/round-61/build/ScribeEntryEvm.md step 3, LOG.md:289 ("occur only inside immediate offsets 1–9") and LOG.md:805. I confirmed the fact independently (pattern occurs once, at offset 1, length 9 → inclusive span 1..9; `git show ab58069:LOG.md | sed -n '289p'` matches), so no overstatement — but under QUALITY.md Q11 the offsets 1–9 are cited to prose and should be labelled recorded or carried by an in-entry command.

## Residual risk / verification gaps
- I did not re-run `reports/round-61/measure.py` (out of scope) nor any REA producer; the provider-version and `functions: []` claims rest on the saved records, which I did read (r19 provider `evmole-interface`/`evmole@0.9.3`; all seven `evidence_id` values match the entry's list; `rea-agents@6.4.0` appears in the seven LEDGER.md files, not in any inspection.json).
- The e0a4b0c run executed the ab580698 block text (that commit has no entry); the block text is identical at 0b6ddf07 and ab580698, so no variant was exercised.
- Not decided here: whether the sibling C04 header needs the same correction (same wording, line 2).

VERDICT: The reproduction half of the attack fails — the Reproduce output is byte-identical (sha256 0480a2f7…, exit 0, empty stderr) at cf02419, e0a4b0c, 0b6ddf07 and ab580698 and equals the Provenance block exactly, so no entry value is falsified; but `verified-at` naming e0a4b0c is stale/incomplete (the entry, S016–S026 and Q12/Q13 do not exist at that commit) and should name 0597e53 or ab58069.

Installs: none (stdlib `python3 -B`, `curl`, `git archive` only; no pacman/uv/npm action taken).
