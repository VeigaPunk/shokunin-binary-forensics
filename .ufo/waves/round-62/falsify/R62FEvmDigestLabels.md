GRADE: BROKEN — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09), digest/identity/provenance sentences; failed Q11
Seat: RevengerR61-2.R62FEvmDigestLabels (fresh falsify, not author/corrector). Date 2026-10-21.
Frozen revision: d97761952be256d145d298022de03091de91d358 (archived via `git -C …/revenger-shokunin archive` into /fast/scratch/hyaku/revenger-r62/R62FEvmDigestLabels/tree).
Candidate: git blob 3e58a91fa8aee579aff7f873ce55061ae8f92cdf; file sha256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e.
Extracted readout.py sha256 740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb. TMPDIR=<scratch>/tmp, cwd=/.

## Primary checks (exact outputs)
- `python3 -B readout.py <tree>` (Python 3.14.8): exit=0, stderr 0 bytes; `cmp out.txt printed.txt` → IDENTICAL (both sha256 aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf). Provenance block is exact for this revision.
- `git diff --stat a3498e25… d9776195… -- corpus/fixtures corpus/live` → empty: recorded-run base and frozen state read the same bytes.
- `git ls-remote https://github.com/ethereum/execution-specs 'refs/tags/v2.20.0*'` → `2004296f2ffcbcebcd00f41152d33e8dfda0922a refs/tags/v2.20.0^{}`: S028 commit pin matches tag (accessed 2026-10-21).
- 64-hex scan of all seven records: only `.evidence_id`, `.subject.digest.sha256`, `.normalized_result.artifact.sha256`, `.normalized_result.bytecode.sha256` (plus bytecode `.hex` false-positives in r22/r24). The readout scopes all three sha256 fields; evidence_id is labelled recorded/unaddressed (:144-146). No unscoped saved digest.
- Seven-record aggregates from the output: provider_version set {evmole@0.9.3}; (kind, deployment_authenticity, hardfork) set {(unknown, unknown, unknown)}; every subject/artifact scope matches a local byte string; decoded.hex == recorded.bytecode.hex for all seven.

## Finding 1 (fatal, Q11): r19 carrier format is asserted, not derived
- Entry :55-57: "r19's carrier is a 39-byte `0x`-prefixed ASCII hex file (`r19.carrier.bytes`, `r19.carrier.sha256`)". The cited fields print only `bytes`, `file`, `sha256` (output `carrier` keys = ['bytes','file','sha256']). Neither the `0x` prefix nor the trailing byte appears in any output field.
- Readout :362 and :366 decode with `carrier[2:-1]` — a hard-coded 2-byte header and 1-byte trailer, never checked or printed. Q11 (QUALITY.md:23): "Constants such as header offsets are derived, not assumed."
- Counterexample (archived copy only): r19 fixture rewritten to `zz60003560e01c63deadbeef14601057005b00!` → exit 0, stderr empty; r19 keys `decoded, instructions, instruction_opcode_counts, valid_jumpdest_offsets, raw_0x63_offsets, raw_0x5b_offsets, jumpi_with_preceding_push1, pattern, recorded, record, candidate_pairs_*` all UNCHANGED; other six lines and summary identical. Only `carrier.sha256` and subject/artifact scopes changed (→ `no_local_byte_string`).
- Observation: the actual file is `30 78 … 30 0a` (xxd: `0x60003560…005b00.`), so the value is correct. Inference: the digest-scope change detects that the carrier changed, but it cannot show the prefix is `0x` or the trailer is `\n`. A correct value without its claimed in-entry derivation fails Q11. The value is not labelled recorded either; `recorded.artifact.encoding=hex` is a producer label and does not establish a `0x` prefix.
- Smallest safe correction: print `carrier[:2]` and `carrier[-1:]` (or the full carrier hex) in the r19 case object, assert them before slicing, and cite those fields at :56. Alternatively, drop "`0x`-prefixed" from the prose and label the slice constants as recorded authoring premises.

## Finding 2 (nonfatal wording, Q11/Q09 inventory accuracy)
- :221 inventory row "pattern bytes and length" cites `summary.pattern_hex`; the 9 at :102 is in `summary.pattern_length` (printed 9), which is not cited.
- :241 one row/field (`r19.recorded.bytecode.kind`) is cited for three fields across seven records. Inference :134-135 says "each record's own `kind`, `deployment_authenticity` and `hardfork` fields are `unknown`". The output carries all 21 values (set above), but the entry's Q11 self-claim (:200, "names the field and the value for each claim") is false here.
- :239 row "bytes and encoding" gives only 39; the encoding value (`hex`) is uncited.
- :61-63 "all three digests name the same byte string" cites only `r21.digest_scopes.subject`. The `artifact`/`bytecode` scopes are printed but not inventoried. :65-75 "Each names its operation…" and :157/:199 "one recorded provider version" generalize over seven records while citing r19 fields only. All of these are supported by the output; the inventory is incomplete.
- :61-62 "the carrier file *is* the raw bytecode": for r21–r26 the readout sets `code = carrier` from the CASES constant `"raw"` (:304-307, :366), so the `carrier_and_decoded_same_byte_string` label follows by construction. The non-tautological support is recorded artifact/bytecode sha256 equal to sha(carrier). The premise should be labelled as the CASES/recorded `encoding=raw` label.
- :51 "(upstream)" glosses `raw_result` as upstream output. That holds only per the record's own `limitations[1]`, which is neither printed nor cited. Label it recorded or remove it.
- :22 "inert" has no derivation or source. "authored" is a recorded S031 label (SOURCES.md:45), which is acceptable.

## Held (no defect found)
- Q09: digests are claimed only for the bytes hashed. :131-135 and :159-162 explicitly deny provenance, completeness, origin, authenticity and custody. `authority` is "not read" as origin (:160-161), and no sentence defines `shipped-artifact` as a file class. The Q10 note's "shipped-artifact reverse-engineering overlap" (:178) is a domain label, not the `authority` field.
- `r19.record.sha256` is labelled "the record file's own digest" (:72-73), not a producer receipt. evidence_id is recorded, with no formula (:144-146).
- Carrier ≠ decoded for r19 is derived: `digest_scopes` = carrier_file_bytes_only/carrier_file_bytes_only/decoded_bytecode_bytes_only. Record↔fixture identity is by digest (:161-162). The record's `subject.local_path` points to /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/…, a different tree, so digest identity is the correct basis and the entry claims no path identity.
- Source-file pins (:31-43) are labelled "recorded source facts, not values this entry re-derives". Tag→commit verified above; line anchors are not re-opened by this seat.
- No generalization of authentication or completeness found: `discovery_completeness=unknown`, so an empty list is not read as absence (:141-143). The Provenance claim "exact, complete and untruncated" holds (cmp IDENTICAL).

## Observation / inference / unknown
- Observed: all command outputs above. Inferred: Finding 1 is a missing in-entry derivation (Q11 header-offset clause), not a wrong value.
- Unknown: S028 line anchors and quotes (left to opcode-source seats); C04 entry not reviewed; Q01–Q08, Q10, Q12, Q13 not independently audited beyond the digest/identity sentences.

VERDICT: BROKEN (Q11) — the `0x`-prefixed carrier claim and the `[2:-1]` header/trailer constants are assumed, not derived or labelled recorded. Recommend not admitting C09 at this hash until a focused re-review of the corrected bytes. The other digest/identity/provenance sentences hold, with the nonfatal Q11 inventory wording listed above.
Installs: none. Writes: this report, and scratch under /fast/scratch/hyaku/revenger-r62/R62FEvmDigestLabels/ (tree, mut copy, outputs). No repo, git or index mutation.
