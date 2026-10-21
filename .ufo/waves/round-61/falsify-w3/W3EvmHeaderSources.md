GRADE: HOLDS — C09 header `source:` line and Q02 fields (corpus/knowledge/evm-saved-interface-candidates.md:1-4)

Attack target: every S-id on the entry's `source:` line (S026, S016, S017, S018, S019) — existence, opened-in-round-61, tier A for the scope used — plus `verified-at:`/`recheck:`/`coverage-map:` against QUALITY Q02. Landed ab580698212258a55e43e9bb9bf6ac78c91eae2a; archive extracted to /tmp/revenger-r61w3-W3EvmHeaderSources. No REA producer call, no bytecode execution.

OBSERVED — existence, tier, round-61 opening (all five pass)
- Rows exist and are tier A, `opened` 2026-10-21, `status` mined, `used-by` names this entry: SOURCES.md:30 (S016), :31 (S017), :32 (S018), :33 (S019), :40 (S026). Parsed columns: `tier=A status=mined opened=2026-10-21 used-by=corpus/knowledge/evm-saved-interface-candidates.md` for each.
- Round-61 opening is recorded under `### Sources opened this round` (lessons/round-61.md:48), with per-row anchors/quotes at :55 S016, :56 S017, :57 S018, :58 S019, :65 S026; access date 2026-10-21. So each cited row was opened in the writing round, as Q01 requires.

OBSERVED — tier A for the scope actually used, anchor by anchor
- S016: `git ls-remote https://github.com/ethereum/execution-specs 'refs/tags/v2.20.0^{}'` → `2004296f2ffcbcebcd00f41152d33e8dfda0922a`, matching the row's commit anchor. Fetched `.../osaka/vm/instructions/__init__.py` (367 lines) at that tag: line 55 `EQ = 0x14`, 106 `JUMPI = 0x57`, 109 `JUMPDEST = 0x5B`, 125 `PUSH4 = 0x63`. Fetched `.../osaka/vm/runtime.py` (69 lines): 22 `def get_valid_jump_destinations(...)`, 29-30 the PUSH-N exclusion sentence verbatim, 60 the PUSH skip, 69 end. Header's “`instructions/__init__.py` lines 55, 106, 109, 125 and `runtime.py` lines 22-69” is exact, not merely plausible.
- S017: fetched PDF SHA-256 `d67c009c5d5a0542c8288aee3c4d470b3e2dbe6e664f72f00011543608477fa9` = the row's recorded digest. Title page line 2: “SHANGHAI VERSION efc5f9a – 2025-02-04”. Page 15 carries §9.4.3, eq. (160), (161), (162) and the quoted sentence “All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations”. Header's “§9.4.3 eqs. (160)-(162), p.15” is exact.
- S018: fetched `https://docs.soliditylang.org/en/v0.8.37/abi-spec.html`, title “Contract ABI Specification — Solidity 0.8.37-develop documentation”; §Function Selector states the first-four-bytes-of-Keccak-256 rule the entry uses. Version pin matches `v0.8.37`.
- S019: fetched `https://docs.soliditylang.org/en/latest/metadata.html`, title “Solidity 0.8.38-develop documentation”; section “Encoding of the Metadata Hash in the Bytecode” present and says the compiler by default appends the IPFS hash to the end of the bytecode (CBOR fields listed). Matches the row scope (“placement of the CBOR metadata tail”).
- S026: all seven `corpus/live/runs/round-{19,21,22,23,24,25,26}/inspection.json` parse with `operation: inspect_evm_interface` and `provider: evmole-interface evmole@0.9.3`; Evidence IDs equal the full IDs printed in the entry; no round-20 record exists. Header's “rounds 19 and 21–26” is exact.

OBSERVED — Q02 fields (entry lines 1-4)
- `source:` present with S-id + tag/section/line anchors; no bare homepage. `verified-at:` carries both date (2026-10-21) and commit. `recheck:` names a runnable command. `coverage-map: C09` matches the README row that names this entry (corpus/README.md:35, status `held`).
- The recheck command works: I extracted the entry's `## Reproduce` block and ran `python3 -B repro.py` from the ab58069 archive root — exit 0, output byte-identical to the entry's `## Provenance` (`PROV_EQ_RUN: True`), including all seven fixture digests, selectors, offsets and saved `evidence_id` prefixes.
- `verified-at` names pre-registration base e0a4b0c4348ef1fade46539f520e94fa140c4d8a, an ancestor of ab58069 (`merge-base --is-ancestor` → 0). At that commit the entry file does not yet exist (git diff e0a4b0c..ab58069 shows it as a 189-line new file), but the header's claim is confined to re-deriving fixture bytes and saved records; I ran the same block in an e0a4b0c archive and got byte-identical output (`BASE_IDENTICAL`), so the sentence is true, not an overstatement. Q02 only requires a date or commit.
- Harm check: `git diff --stat cf02419..ab58069 -- corpus/fixtures corpus/live` is empty; no changed saved record or fixture underlies this header.

INFERENCE
- Since all five anchors re-resolve to the cited bytes/pages and Q02's two reject conditions (missing header, bare homepage) are absent, the `source:` line and Q02 fields meet the pre-registered condition for C09.

UNKNOWN
- Whether S018's `/en/v0.8.37/` section is byte-identical to `/en/latest/` (a SOURCES-row aside, not stated by the entry); not needed for this header item and not tested.
- S002 is cited in the body (current REA release), not on the `source:` line; outside this assigned attack, so not graded here.

VERDICT: HOLDS — all five header S-ids exist, were opened 2026-10-21 in round 61, are tier A for the scopes used, every line/equation/section anchor re-resolves, and the four Q02 headers recheck reproducibly.
Installs: none (system python3, curl, git, pdftotext already present).
