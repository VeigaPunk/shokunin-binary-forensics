# R63RevengerLedger — ledger-discipline review (round-63 build wave)

Seat: revenger-r63.R63RevengerLedger (revenger). Scope: PROVINCE.md evidence
discipline applied to `corpus/live/runs/round-63/LEDGER.md` +
`inspection.json` + `receipt.json` and the C06 candidate entry
(`/tmp/revenger-r63-entry/candidate.md`). Method: every reviewed digest
recomputed, the recheck command re-executed, and one forged-evidence scenario
actually constructed and executed against the round's checks. Tooling: none
installed (python3 stdlib, sha256sum, pre-existing unblob 26.6.4 at
`~/.local/bin`); scratch `/tmp/revenger-r63-ledger-forge` and
`/tmp/revenger-r63-ledger-unblob` used and removed.

## Verdict

**Discipline HOLDS** on all four review questions, with one minor located leak
(still present) and one constructed forged-evidence scenario the ledger cannot
flag by any committed check (its defense is the discipline itself, and the
ledger carries that defense correctly).

## Question-by-question findings

### 1. OBSERVATION / INFERENCE / UNKNOWN separation — HOLDS

- LEDGER.md (sha256 `cedc8f701350dfd0c2bcd09fcb36bca9f70f1a5bd61188e3f33c4429bac5f985`,
  22481 bytes, 119 lines): 23 classed rows (O1–O11, I1–I6, U1–U6), each with
  Basis and Result cells; scope statement names the class rule up front.
- Candidate: §Observation (items 1–17, each with command + printed output),
  §Inference (items 18–21, each tagged `[INFERENCE, scoped to …]`),
  §Unknown (22–26), §Limitations (27–35). No sentence mixes classes; inferences
  name their basis items; unknowns claim no output.

### 2. Q09 — digests and Evidence IDs — HOLDS (all recomputed)

- Receipt (recomputed): `fixture_sha256` `bdfe9f46…` = sha256 of
  `firmware-r63.bin` ✓; `stdout_sha256` `f6997835…` = sha256 of `stdout.raw` ✓
  and `stdout.raw` is **byte-identical to inspection.json** (3904 bytes), so the
  receipt transitively binds the record bytes; `evidence_id` receipt==record ✓;
  `stderr.txt` 0 bytes, sha `e3b0c442…` = sha256("") ✓.
- LEDGER-quoted digests all recomputed true: generator `4e5d5975…`, truth
  `9663f90b…`, receipt `e930a549…`, oracle_check `d0dfd7a1…` (current file;
  the ledger discloses it changed mid-round and cites it by path+behaviour),
  binwalk host binary `5fc19aac…` = envelope `engine.executable_sha256` ✓.
- Evidence IDs: `ev_aae7529f…` and the archive record's `ev_5cc39f35…` /
  `ev_cc681c2a…` are quoted only as **recorded fields of saved files**. I tested
  14 serializations of the archive record (whole file, pretty/sorted/compact,
  substep, evidence object, raw_result, …) — **no byte preimage exists in the
  corpus for either ID**; the derivation is provider-internal and opaque. No
  sentence in either artifact claims an Evidence ID hashes bytes, proves origin,
  or proves completeness. LEDGER U4 states the boundary verbatim ("does not
  authenticate that a producer ran… does not bind the Evidence ID to an external
  service"); candidate item 21 + limitation 30 ("Recorded, not authenticated")
  and item 14 do the same.

### 3. Provider origin / authenticity / completeness — no over-claim found

- LEDGER: provider fields quoted as envelope observations; I3 denies general
  provider length validity (`size_basis provider_reported_validation_unknown`,
  agreement "happened to be correct here"); U4 denies producer authentication;
  U5 declares truth.json same-lane-authored ("not third-party validation"); the
  score section states F cannot see realness, correctness, provider identity,
  authenticity or completeness.
- Candidate: item 14 marks Evidence IDs/provider/operation as recorded fields
  "does not establish who produced the record, that it is complete…"; item 20
  denies general correctness; unknowns 22–23 leave `executable`/`encrypted`/
  `hash_status` and record completeness open; limitation 31 credits the
  `rea-agents@6.4.0` run with nothing beyond the record's existence and literal
  fields.

### 4. Universal parser claims / single-fixture scope — HOLDS

- Candidate: item 18 ("not a general property of ZIP archives"), 27 ("It is not
  a ZIP parser"), 28 (no trailing-bytes claim — explicit), 29 (single fixture),
  33 (no ZIP64 / compression-semantics / provider claims; notes the fixture is
  non-ZIP64 in the bytes read), 35 (names the C06 grounds it does NOT cover:
  `nested-r11`, `duplicate-r15`).
- LEDGER: I1 ("says nothing about… any other image"), I5 (region set is
  engine-dependent — binwalk 2 regions vs unblob 0 chunks on the same image),
  U1 (refuses to transfer the L1 pre-probe into a claim), U6 (no device-level
  claim).

## Independent reproductions (evidence, not trust)

- Byte oracle, third derivation (mine): `zlib.decompress(image[512:591])` →
  78 bytes sha256 `a5718481…` == truth `decompressed_member.sha256` ✓;
  `image[1024:1114]` → 97 bytes sha256 `2d0d86aa…` == truth ✓. Record reports
  2/2 truth zlib regions; 3 padding regions unreported (all-zero spans verified;
  1880 zero bytes in the image).
- `oracle_check.py` control run: `ORACLE OK`, exit 0.
- LEDGER O11 unblob cross-check **reproduced**: whole 2048-byte image → 0
  ChunkReports, 0 extracted files; isolated `image[512:591]` → 1 zlib ChunkReport
  (start 0, end 79), `zlib.uncompressed` 78 bytes sha `a5718481…` == truth ✓.
- Candidate recheck **re-executed**: `readout.py` sha `c6b54ccc…` == quoted ✓,
  331 lines ✓, run against the repo root exits 0, prints exactly 17 lines, stdout
  sha256 `e112d409…` == the digest quoted in the entry's `recheck:` header ✓.
- Candidate source anchors recomputed: appnote snapshot `0b993022…` ✓,
  archive-r2 truth `7df773bf…` ✓, saved record `2fec924b…` ✓ (7692 bytes).
- My own central-directory readout matches every candidate value (EOCD@2942,
  counts 2, cd 114 @ 2828, member names/offsets/sizes/CRC-32 `b3df9ea7` /
  `72a557b1`, inflated digests, 0 trailing bytes; byte accounting
  0+2710+118+114+0+22+0 = 2964 ✓).

## Constructed forged-evidence scenario the ledger would FAIL to flag

**Evidence-ID transplant (executed on copies in `/tmp/revenger-r63-ledger-forge`; scratch removed).**
I replaced `ev_aae7529f…` consistently in inspection.json + the stdout.raw copy +
receipt.evidence_id with a **real foreign Evidence ID from another round's saved
record** (`ev_5cc39f35…`, the 20261012T164246Z archive record), then recomputed
`receipt.stdout_sha256`. Result:

- `fixture_sha256` still true; `stdout_sha256` still true; receipt==record ID
  equality still true; `oracle_check.py` on the forged record: **`ORACLE OK`,
  exit 0**.

Because the Evidence ID has no recomputable byte preimage (see §2), no committed
check distinguishes the genuine ID from a transplanted genuine ID. Residual gap:
`receipt.evidence_id == record.evidence_id` is observed only manually (LEDGER
row O9); `measure.py` and `oracle_check.py` never read the receipt or the ID.
**Corollary (ledger layer): nothing binds LEDGER.md to inspection.json** — the
receipt hashes stdout only, no ledger digest exists, so a fabricated ledger row
(a region the record never reported, citing a well-formed fabricated `ev_…`)
would be flagged by nothing in this round's artifacts. The working defenses,
both present in the artifacts: records are byte-preserved (any dispute
re-derives from inspection.json/oracle_check.py), and both artifacts explicitly
refuse to claim what the ID cannot prove (U4; candidate item 21, limitation 30).
This is exactly the Q09 boundary doing real work — keep it.

## Leaks located

- **L2 (present, minor):** `LEDGER.md` line 51 (U1, Other signatures): "This
  image contains only two zlib members and **zero padding**" — false against the
  bytes: truth.json declares and the fixture contains three all-zero padding
  spans (0–512, 591–1024, 1114–2048; 1880 zero bytes in the image), and O6 in
  the same document lists them. Rationale clause only; the row's UNKNOWN
  conclusion (no evidence about other signature families) is unaffected.
  Suggested one-word-class fix by the ledger author ("three zero-filled padding
  regions and no other signature kind").
- **L1 (found mid-round, already fixed in the final LEDGER):** an earlier draft
  rendered the receipt command as `…/corpus/live/../fixtures/…` while labelling
  it "verbatim from the receipt"; the final LEDGER (line 19, "REA command line
  (verbatim)") quotes the receipt `command` byte-verbatim — re-verified against
  current receipt.json bytes. No action needed; recorded for the audit trail.
- **Sequencing dependency (not a text defect):** `corpus/SOURCES.md` currently
  ends at S031 — the S032 and S034 rows the candidate cites are not yet
  appended. Q01/Q02 are only fully satisfiable after L1's round-63 SOURCES
  append; the candidate correctly marks both rows as opened/pending and proposes
  the S034 row text. The C06 admission must land after that append (and after
  the fresh-seat Q01–Q13 decisions, per claims.md).

## Notes for L1

- F-count context observed on the working tree (I6 of the LEDGER, confirmed by
  my read of measure.py's F block): `inspection.json` is the one new counted
  record (`receipt.json` has no `normalized_result` and is correctly not
  counted); the frozen `git archive` measurement and `measure-after.log` remain
  L1's to run.
- No Q01–Q13 criterion fails in either artifact on my reading; the candidate's
  self-check table matches mine (Q05/Q07/Q12/Q13 n/a with stated reasons,
  Q08 superseded by Q11).
