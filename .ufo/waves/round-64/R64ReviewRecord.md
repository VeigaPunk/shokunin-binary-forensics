# R64ReviewRecord — saved-record verification for C1 (round-63 REA firmware record)

Seat: `revenger-r64.R64ReviewRecord` (leaf, no dispatch). Lane tip observed:
`a3d063f29b93ad1f0b7eab78652c552685b84d89`, clean on `corpus/live` and `corpus/fixtures`.
Frozen contract: `reports/round-64/claims.md`; red-before: `reports/round-64/measure-before.log`.
Method: `.ufo/waves/round-63/falsify/W2VerifyC2Record.md` (round-63 re-derivation).
Deliverable with every command and its output: `.ufo/waves/round-64/review-record.md`.

**Verdict: record verified.** The Evidence ID in
`corpus/live/runs/round-63/inspection.json` re-derives to
`ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259` from the shipped
`rea-agents@6.5.0` package; `receipt.json` `stdout_sha256` binds `stdout.raw` bytes
(byte-identical to `inspection.json`, 3904 B) and `fixture_sha256` binds
`firmware-r63.bin` (2048 B). C1's evidence substrate is sound; the C1 **entry** was not
landed at verification time, so entry-level citation integrity is out of this seat's
reach (dependency finding, not a defect).

## Attacks run

### A1 — Evidence ID re-derivation, two independent paths → attacks "ID is producer-computed"

- Package-native: `parseEvidence(record)` (exported; internally recomputes
  `ev_ + digestCanonicalValue(semanticProjection(e), "Evidence")`,
  `dist/domain/evidence.js:135,156-182`) → **ACCEPT**, `evidence_id` equals the recorded
  ID. Wrong semantics or a wrong ID are rejected (mutations M1–M4 all `REJECT`).
- Independent: literal transcription of `semanticProjection` + package's exported
  `digestCanonicalValue` over the committed bytes → `ev_aae7529f…80ed259`, **exact match**
  (`RECOMPUTED == RECORDED`).
- Projection binds `subject.digest/format/architecture`, provider, profile,
  predicate/operation/parameters, `raw_result`, `normalized_result`, confidence, authority,
  environment, limitations, locations, links; excludes display `name`/`local_path`.
  `relationship_coverage` null → omitted, as the package does.

### A2 — `stdout_sha256` binds stdout bytes → attacks the receipt/stdout conjunct

- `sha256sum stdout.raw` = `f6997835…a71f9` = receipt `stdout_sha256` = SHA-256 of
  `inspection.json`; `cmp` → identical bytes; separate inodes (not the same file).
- Shape matches shipped serialization `` `${JSON.stringify(value)}\n` ``
  (`dist/cliOutput.js:129`): 3904 B, one newline, ends `0x0a`; saved `stderr.txt` 0 B
  (`e3b0c442…b855`); receipt `exit_code` 0.

### A3 — `fixture_sha256` binds the fixture → attacks the receipt/fixture conjunct

- `bdfe9f46…510be` agrees across four independent sources: fixture bytes on disk,
  receipt `fixture_sha256`, record `subject.digest.sha256`, `truth.json` `image.sha256`.
- Receipt command, record `parameters.path`, `subject.local_path` all name the same
  absolute fixture path; size 2048 = `normalized_result.input_size`;
  `receipt.evidence_id` = record ID.

### A4 — producer reproducibility and engine binding → corroboration beyond the receipt

- Fresh run of the pinned command (cached `rea-agents@6.5.0`, `REA_BINWALK_COMMAND=/usr/bin/binwalk`,
  scratch `TMPDIR`): exit 0, 3976 B stdout, 0 B stderr; fresh output accepted by
  `parseEvidence`; after excluding `evidence_id` and normalizing mkdtemp paths and
  provider UUIDs, **all fields equal** the committed record (regions, engine, input_size,
  coverage, locations, limitations). The only raw diff is the temp staging prefix inside
  `raw_result` — which is why the fresh ID differs
  (`ev_00f5ba29…426a24`); correct content-bound behavior, not drift.
- Live engine equality: `/usr/bin/binwalk` SHA-256
  `5fc19aac…40d6` = record `engine.executable_sha256`; `binwalk --version` →
  `binwalk 3.1.0` = `version_execution.stdout.text`. Route name mapping
  `inspectFirmwareRegions → "inspect-firmware-regions"` confirmed at `dist/cliCommandNames.js`.
- Oracle: `python3 -B corpus/live/runs/round-63/oracle_check.py` → `ORACLE OK`, exit 0;
  both reported zlib regions `offset=OK size=OK signature=OK decompressed_sha256=OK`;
  padding spans correctly `not-expected` under `coverage=signature_scan`.
- Independent `zlib.decompressobj` re-derivation: member lengths 79 and 90 are consumed
  exactly (`eof=True`, next byte `0x00`), decompressed digests equal truth
  (`a57184…df7b86`, `2d0d86…eeaba9`), the three padding spans (0/512, 591/433,
  1114/934) are all-zero and tile the image to 2048 B. The record's `reported_size`
  values are exact member boundaries, not provider guesses.

### A5 — provenance and census → attacks "was this record modified?"

- Added in `2a34e45`; `git log --diff-filter=M --` on `inspection.json`, `receipt.json`,
  `stdout.raw`, `firmware-r63.bin` → **empty**; working tree clean on both trees at tip.
  File SHA-256s match the LEDGER pins (receipt `e930a549…c6b94d` incl. its corrected
  note; stdout `f6997835…`; fixture `bdfe9f46…`).
- Exactly one saved record carries `operation=inspect_firmware_regions` with non-null
  `normalized_result` — `round-63/inspection.json` — satisfying the frozen counter's C07
  `ROW_OPS`/`firmware`-family predicate.
- Contract state at verification: `README.md:36` `| C07 | … | frontier |`;
  red-before `SAVED_RECORDS=59`, `K_ROW C07 status=frontier`,
  `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`. Stale token is genuine; K moves only on
  admission of the absent entry.

### A6 — receipt self-sufficiency (carried LOW recheck)

`env -u REA_BINWALK_COMMAND … npx -y rea-agents@6.5.0 inspect-firmware-regions <fixture>` →
exit 1, `capability_unavailable` "requires … an absolute REA_BINWALK_COMMAND path".
The needed engine is recorded in the record (`engine.executable_path`/version), not in the
receipt command. Unchanged from round-63 L2; no C1 field depends on it.

## Findings by severity

**HIGH — none. MEDIUM — none.**

**LOW**

1. **L1 (carried, reconfirmed):** receipt command is not a standalone replay recipe —
   `REA_BINWALK_COMMAND=/usr/bin/binwalk` is required by the route, exported globally on
   this host, and absent from `receipt.command`. Recovery is possible from the record's
   engine block. Cite as a reproduction affordance gap, not a binding failure.
2. **L2 (claim boundary):** the Evidence ID authenticates content self-consistency, not
   provenance. Controls M5/M6 (raw path / region size mutated, ID recomputed with the
   same package function) are **accepted** by `parseEvidence`. C1 must keep its
   "observation layer only" scope and must not cite the ID as cross-run identity: any
   re-run yields a different ID because `raw_result` embeds the temp staging path.
3. **L3 (dependency):** `corpus/knowledge/round-64-firmware-region-byte-evidence.md` was
   absent during verification (scribes draft under `/tmp/revenger-r64-*` by design). This
   seat verifies the record/receipt/fixture bindings feeding C1; the entry's citations
   and its Q01–Q13 decisions remain other seats' gates.

## Residual risk

- An assembled record whose ID is recomputed over fabricated semantics is accepted by
  the package parser (L2 controls). Authenticity here rests on fresh-producer structural
  equality (A4), the hash-matched live engine, and the fixture-scoped oracle — the
  LEDGER's disclosed U4.
- Oracle scope: this 2048-byte authored image, this binwalk 3.1.0 build, this route. It
  establishes nothing about firmware inspection generally (LEDGER I1/I5/U1–U3/U6 stand).
- Reported region sizes carry `size_basis=provider_reported_validation_unknown`; the
  oracle confirms them for this fixture only.

## Verification gaps

- Original 1.2966 s producer invocation is unreplayable; A4 is a fresh process under a
  scratch `TMPDIR`.
- Frozen counter not executed by this seat (measurement is another assignment); C07 row
  membership and red-before values are read from `measure.py` and the committed log.
- No `lsp` device mounted (`xd://lsp` absent; only `ast_edit`, `debug`), and these are
  JSON data artifacts with no server configuration — all semantic checks are byte
  re-derivation plus the shipped package's own parser, recorded as the substitute.
- C1 entry absent, so entry-level citation integrity unverified (L3).

## Tooling record

- No installs/upgrades/pacman (host pause respected). `npx -y rea-agents@6.5.0` resolved
  from the existing cache `~/.npm/_npx/ad9a3fdbcad992c6` (package version 6.5.0); one
  producer re-run + one clean-env failure probe.
- Scratch `/tmp/revenger-r64-review/` (three Node scripts, re-run outputs; ~50 KB),
  lane-owned; removal on L1 landing per contract.
- No git/jj mutation, no commit, no edit outside
  `.ufo/waves/round-64/review-record.md` and this report; lane index/lane state untouched.
