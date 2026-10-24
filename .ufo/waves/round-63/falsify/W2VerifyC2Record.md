# W2VerifyC2Record — C2 coverage F, independent condition verification

Seat: revenger-r63.W2VerifyC2Record (leaf, no dispatch). Lane tip attacked:
`db55bd6488e24e956df5818ae34c2a043d7ddc12` (`round-63: C1 candidate entry …; README still partial`).
C2 artifacts were added in `2a34e45` and are unchanged at tip
(`git diff --stat 2a34e45 db55bd6 -- corpus/live/runs/round-63 corpus/fixtures/firmware-r63` empty;
`git log --diff-filter=M -- corpus/live/runs/round-63 corpus/fixtures/firmware-r63` empty;
`git status --porcelain` on both paths empty). Committed blobs re-hashed via `git show HEAD:` below.
Frozen contract: `reports/round-63/claims.md` §C2. Frozen counter: `reports/round-63/measure.py`.

**Verdict: C2 conditions (a), (b), (c) all MET on committed bytes.** Target `F_COVERAGE=5/8`
reproduced with the frozen counter on a `git archive HEAD corpus` tree. No condition located as unmet.

## Attacks run (each names its target)

### A1 — envelope carries evidence_id + operation + non-null normalized_result → attacks (a)

- `inspection.json` (3904 B, SHA-256 `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`)
  top-level keys include `evidence_id` = `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`,
  `operation` = `inspect_firmware_regions`, `predicate_type` = `rea.analysis`, and
  `normalized_result` present and non-null (keys exactly `coverage` `engine` `input_size` `regions`;
  `input_size` 2048, `coverage` `signature_scan`, two regions).
- Counter parity: `measure.py:43` counts a file iff `x.get("evidence_id")` is truthy **and**
  `x.get("normalized_result") is not None`, and keys the counter by the **top-level** `operation`.
  `inspection.json` satisfies exactly that predicate.
- Note (LOW, wording only): `normalized_result` itself carries no `operation` key — the operation is
  top-level. Under the strictest parse of claims.md ("normalized_result with operation == …") the
  nested field does not exist; under the counter's canonical reading (and the reading used by every
  other saved record, all of which carry top-level `operation`) the condition holds. Not a defect;
  the contract and counter agree, the phrase is ambiguous.

### A2 — receipt is a real-run receipt with digest/ID binding → attacks (b)

Re-read `receipt.json` field by field and re-hashed every file myself:

| Receipt field | Value | Independent check | Result |
|---|---|---|---|
| `command` | `npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json` | names `rea-agents@6.5.0` and `inspect-firmware-regions`; package cached at `~/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents` (`package.json` version `6.5.0`, `bin.rea-agents` → `scripts/rea.mjs`; `dist/cliCommandNames.js:67` maps `inspectFirmwareRegions` → `"inspect-firmware-regions"`) | OK |
| `exit_code` | `0` | re-run reproduces exit 0; stderr empty | OK |
| `fixture_sha256` | `bdfe9f46…510be` | `sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin` = `bdfe9f46…510be`; also equals `inspection.json` `subject.digest.sha256` and `truth.json` `image.sha256` | OK |
| `stdout_sha256` | `f6997835…a71f9` | `sha256sum stdout.raw` = `f6997835…a71f9`; `cmp stdout.raw inspection.json` → identical bytes; `sha256sum inspection.json` = `f6997835…a71f9` | OK |
| `evidence_id` | `ev_aae7529f…80ed259` | equals `inspection.json` `evidence_id` | OK |
| `stderr` | (separate file) `stderr.txt` 0 bytes, `e3b0c442…b855` | `wc -c` = 0 | OK |

Receipt blob at tip = `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d`
(matches LEDGER's cited digest); `inspection.json` blob at tip = `f6997835…`.

Real-run corroboration (beyond the receipt, because a receipt is self-consistent by construction):

1. **Producer identity recomputation.** Using the shipped 6.5.0 implementation
   (`dist/domain/evidence.js:182` `computeEvidenceId = ev_ + digestCanonicalValue(semanticProjection(evidence), "Evidence")`,
   `dist/domain/canonicalDigest.js` RFC-8785 canonical JSON over SHA-256), I recomputed the evidence ID
   from the committed record's own semantic fields (subject digest/format/architecture, provider,
   analysis_profile, predicate_type, operation, parameters, raw_result, normalized_result, confidence,
   authority, environment, limitations, locations, evidence_links; `relationship_coverage` omitted
   because null): **computed `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`
   == recorded ID**. Any post-hoc semantic edit (including `raw_result`) would break this binding.
2. **Independent producer re-run** of the exact command on the inert fixture (static inspection, no
   payload execution): exit 0, stdout 3904 bytes, stderr 0 bytes. The result differs from the committed
   record only in `evidence_id` (temp-path dependent), the mkdtemp temp-dir name
   (`/tmp/rea-firmware-7rPoLl/` — the shipped producer uses `PrivateRuntimeRoot.create({ prefix:
   "rea-firmware-" })`, `dist/cli-runtime/cli.js:15035`), and binwalk's random `provider_id` UUIDs. All regions,
   sizes, descriptions, confidence 250, engine block, `input_size`, `coverage`, `locations`,
   `limitations` are identical. The shipped CLI prints `${JSON.stringify(value)}\n`
   (`dist/cliOutput.js:129`), matching the saved stdout's single line + trailing `0x0a` (3904 B, `wc -l` 1).
3. **Fixture reproducibility.** Copied `generator.py` to `/tmp` scratch and ran `python3 -B generator.py`
   (host Python 3.14.8, zlib 1.3.2 — equal to `truth.json` `build_recipe`): reproduced
   `firmware-r63.bin` SHA-256 `bdfe9f46…510be` and `truth.json` byte-identically (`9663f90b…5e6`).

### A3 — oracle agreement and independent byte re-derivation → attacks (c)

- `python3 -B corpus/live/runs/round-63/oracle_check.py` (committed blob `d0dfd7a1…512`,
  matching LEDGER's cited checker digest) prints five `REGION` lines all `OK` and final line
  **`ORACLE OK`**, exit 0.
- Independent re-derivation from the fixture bytes (my own `zlib.decompressobj`, not the checker):
  image 2048 B / `bdfe9f46…`; member `image[512:591]` → `eof=True`, 0 unused bytes, 78 B,
  SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` (= truth
  `a57184…7b86`); member `image[1024:1114]` → `eof=True`, 0 unused bytes, 97 B, SHA-256
  `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` (= truth `2d0d86…aba9`).
  Byte immediately after each window is `0x00` (padding), so the reported sizes end exactly at the
  member boundary. Padding spans 0/512, 591/433, 1114/934 are all-zero, matching the three `padding`
  truth regions the record does not report (`coverage` = `signature_scan`); the record reports **no**
  padding/false-positive region.
- **Oracle sensitivity (control):** seven mutated copies of the record — offset 512→513, size 90→91,
  signature `zlib`→`gzip`, subject digest → 64 zeros, size 79→78, one region dropped, one extra
  fabricated zlib region appended — were each rejected with exit 1 and last line `ORACLE MISMATCH`
  (7/7). `ORACLE OK` is therefore not a hollow pass.
- Independent engine probe: `/usr/bin/binwalk` is 3.1.0 with SHA-256
  `5fc19aac1f357a66a47e8b20a8038a84cb93971cb5d331bd4503b02fcc0a40d6` — exactly the record's
  `normalized_result.engine.executable_sha256`. Re-running it on the fixture with the record's own args
  (`--quiet --search-all --threads 1`) yields exactly two `zlib` regions at offsets 512 (79 B) and 1024
  (90 B), confidence 250, with the same descriptions.
- Fresh-producer record also passes the oracle: `oracle_check.py --record <rerun.json>` → `ORACLE OK`,
  exit 0.

### A4 — F counter on committed tree → attacks the C2 target (F 5/8)

- `git archive HEAD corpus` → `/tmp/revenger-r63-w2c2/tree`; `cd /` and
  `TMPDIR=/tmp/revenger-r63-w2c2 python3 -B reports/round-63/measure.py <tree>`:
  **`F_COVERAGE=5/8 score=6.2`** (exact 6.25, printed to 1 dp), `F_FAMILIES=['native-static',
  'javascript', 'archives', 'firmware', 'evm']`; `HOLDS_OK=yes`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`,
  `C2_CONTROLS_PASS=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`,
  exit 0. `K_HELD=6/14`, `K_ROW C06 status=partial` (C1 untouched, as expected pre-admission).
- Census of counted records on that tree: exactly one file carries `operation` =
  `inspect_firmware_regions` — `corpus/live/runs/round-63/inspection.json`; `receipt.json` is **not**
  counted (no `normalized_result`). The F tick moves by exactly one and is attributable to this record.

## Findings by severity

**HIGH / MEDIUM: none.** No condition unmet; no contract, counter or preservation harm observed from
this seat's scope.

**LOW**

- `L1` (attacks (a) wording): `normalized_result` carries no `operation` key — the operation is
  top-level. Condition (a) holds under the frozen counter's predicate (`measure.py:43`), but the
  claims.md sentence "`normalized_result` with `operation == "inspect_firmware_regions"`" reads as a
  nested-field requirement it does not literally satisfy. Fix is wording in a future contract, not a
  byte change; the counter and all prior records use top-level `operation`.
- `L2` (attacks (b) reproducibility): the receipt's command line is not self-sufficient. With
  `REA_BINWALK_COMMAND` unset (`env -u REA_BINWALK_COMMAND … npx -y rea-agents@6.5.0
  inspect-firmware-regions <fixture> --format json`) the pinned producer exits **1** with
  `capability_unavailable` / "requires Linux and an absolute REA_BINWALK_COMMAND path to the
  caller-supplied tool" (`dist/firmware/FirmwareCommand.js:resolveFirmwareCommand`). The host currently
  exports `REA_BINWALK_COMMAND=/usr/bin/binwalk` globally, which is why the recorded invocation worked.
  The needed environment is recoverable from the record (`normalized_result.engine.executable_path`
  `/usr/bin/binwalk`, `provider.version` 3.1.0) and the LEDGER's binwalk row, but the receipt alone does
  not record it. This does not violate C2(b) as frozen (command, exit code, fixture SHA-256, stdout
  SHA-256, Evidence ID all present and correct); it is a reproduction affordance gap.

## Residual risk

- Authenticity of "one real run" is established by: evidence-ID recomputation from the shipped 6.5.0
  identity function (content-bound), a fresh producer run whose output equals the committed record
  except for random temp-dir/UUID/ID fields, CLI-exact stdout serialization, and an engine (binwalk
  3.1.0, executable hash-matched) that reproduces the exact two regions. It is **not** established by a
  third-party witness: a producer with the same code could compute the same ID for an assembled record.
  This is the LEDGER's own U4 and remains correctly disclosed.
- The oracle is fixture-scoped: agreement is proven for this authored image, this binwalk build and this
  route. It establishes nothing about firmware inspection generally (LEDGER I1/I5/U1–U3/U6 stand).
- Condition (c) is satisfied for the regions the record **reports** (2/2). The record reports no padding
  regions; the oracle's `record=not-expected` lines show that is consistent with `coverage` =
  `signature_scan`, not a missing-region defect.
- Preservation of `corpus/live`/`corpus/fixtures` bytes outside `round-63` paths is another seat's
  assignment; from this seat's reads, the C2 paths were added in `2a34e45` and never modified after add.

## Verification gaps

- I did not re-execute the original producer process; I re-ran the same pinned command and compared
  structure. The original 1.2966 s invocation cannot be replayed.
- I did not run the full `--self-test` corpus (outside C2); the frozen counter's own C3/hold lines were
  observed incidentally in the A4 run (`C3 2/2`, `HOLDS_OK=yes`).
- No `lsp` semantics applicable: this is JSON/artifact verification, not code-reference analysis; no
  language server answers `inspection.json`/`receipt.json`, so all checks are byte/oracle re-derivation
  by me (recorded here as the semantic-proof substitute).

## Tooling record

- No installs, no upgrades, no pacman (host pause respected). `npx -y rea-agents@6.5.0` resolved from
  the existing local cache `~/.npm/_npx/ad9a3fdbcad992c6` (version 6.5.0) — no registry fetch needed,
  one producer re-run, one clean-env failure probe.
- Scratch `/tmp/revenger-r63-w2c2/` (archive tree, rebuilt fixture, re-run outputs, mutants) removed
  after this report landed.
- Lane state untouched: no git/jj mutation, no commit, no edit outside this report path and `/tmp`.
