GRADE: BROKEN — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09 candidate), r19 hex-carrier / r21 raw-carrier identity and the three digest scopes; failed Q11

Seat RevengerR61-2.R62FEvmCarrier · fresh falsify, leaf, no dispatch · lane /home/vgpnk/Projects/shokunin/revenger-shokunin
Frozen revision d97761952be256d145d298022de03091de91d358 (`rev-parse ^{commit}` = same; HEAD = same) · candidate blob 3e58a91fa8aee579aff7f873ce55061ae8f92cdf · file sha256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e · claimbase 5bd4a90f… (read, not re-audited) · pre-reg a3498e25ad87bf756288812d0ea7c474b09433c7 · 2026-10-21 · Python 3.14.8, cwd=/, TMPDIR=<scratch>/tmp
Archive: `git -C …/revenger-shokunin archive d9776195…` → /fast/scratch/hyaku/revenger-r62/R62FEvmCarrier/root ; base tree a3498e25… → …/root_a3498e25.

## Observation 1 — r19 hex-carrier vs r21 raw carrier: sizes, full SHA-256, decoded bytes (independently re-derived, not via the entry's code)
`sha256sum` + my own script on the archived fixtures (`indep_check.py`, `mut/`), reading bytes directly:
- `corpus/fixtures/evm-r19/fixture.hex` = 39 B, sha256 `294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827`; xxd `3078 3630… 3030 3562 3030 0a` → `0x`-prefixed, newline-terminated ASCII hex.
- r19 decoded = 18 B `60003560e01c63deadbeef14601057005b00`, sha256 `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`.
- `corpus/fixtures/evm-r21/fixture.raw` = 18 B **raw** (no `0x`, no newline), sha256 `d1086bce…` — **byte-identical to r19's decoded bytes** (`r19 decoded == r21 carrier bytes: True`).
- Saved records (read directly): round-19 `subject.digest.sha256` = `294e6fd2…` (the 39-byte file), `normalized_result.artifact.sha256` = `294e6fd2…`, `.artifact.bytes` = 39, `.artifact.encoding` = "hex", `.bytecode.sha256` = `d1086bce…`, `.bytecode.bytes` = 18; round-21 subject/artifact/bytecode digests all = `d1086bce…`, artifact.bytes 18, encoding "raw".
The entry's inventory values for all of these (`r19.carrier.bytes` 39, `r19.carrier.sha256`, `r19.decoded.bytes` 18, `r19.decoded.sha256`, `r21.carrier.sha256` "(= r19 decoded)") match my independent values exactly.

## Observation 2 — every digest_scopes label re-derived against FIVE candidate byte strings (no disjunction can hide identity)
My own referent test (not the entry's `referent()`) classified each of the 21 saved digests against: carrier_file, decoded, hex-text-without-`0x`, uppercase-hex-text, and carrier-stripped-of-whitespace.
- r19: subject → **carrier_file only**; artifact → **carrier_file only**; bytecode → **decoded only**. The stripped 38-byte variant (no newline) did **not** match, so the referent is the exact 39-byte file including its trailing `\n`, not a prefix-stripped variant. No third string matched any digest.
- r21–r26: subject/artifact/bytecode → carrier == decoded, one and the same 18/34/7/35/19/19-byte string, three-way equal.
All 21 labels the entry prints match my classification exactly (`carrier_file_bytes_only` ×2, `decoded_bytecode_bytes_only` ×1 for r19; `carrier_and_decoded_same_byte_string` ×18 elsewhere). The round-61 F2 precedent (`in (sha(raw), sha(d))` hiding the referent) is **cured**: entry :324-332 is an exact-equality cascade with a `no_local_byte_string` fallback, and every digest resolves to exactly one referent. Q09 holds in my lane.

## Observation 3 — the Reproduce block and the Provenance stdout agree exactly, at both revisions
`readout.py` extracted from the entry's own ```python fence (131 lines), run on the frozen tree and on the a3498e25 base tree: exit 0, stderr 0 bytes, stdout **byte-identical** to the entry's `## Provenance` block (`cmp` clean, 15555 B, both trees). Re-run with `cwd=/`: still identical. `git diff --stat a3498e25… d9776195… -- corpus/fixtures corpus/live` → empty (recorded base and frozen state read the same bytes). All 35 `sha256` values in the printed stdout are 64 hex chars; all 7 `evidence_id` values 67 chars.

## Observation 4 — inventory/prose/output agreement, mechanically
67 inventory rows: every cited field resolves in the printed stdout and every stated value matches — **0 missing, 0 mismatches**. 60 distinct prose field citations: all resolve in the printed stdout, and all 60 have an Evidence-inventory row. (Tool: my own resolver over `run_out.txt` + the entry text; no corpus verifier used.)

## Observation 5 — DEFECT (fatal, Q11): the r19 carrier's `0x` framing is asserted, never derived
Entry :55-57: "r19's carrier is a 39-byte **`0x`-prefixed** ASCII hex file (`r19.carrier.bytes`, `r19.carrier.sha256`)". The cited fields print only `bytes`, `file`, `sha256` — no prefix, no trailer. The literal `0x` appears nowhere in the printed stdout except in opcode-count keys (`"0x0"`,`"0x14"`,…) and the selector string `"0xdeadbeef"`. The block hard-codes the framing: `carrier[2:-1]` at :362 and :366 — a 2-byte header and 1-byte trailer constant never asserted nor printed.
My own mutants on archived copies (`mut/`, `mut2/`), all exit 0 / stderr empty unless stated:
- prefix `0x`→`0X` (same length): r19 `decoded.hex` **unchanged**, all walk/count/scope fields unchanged except `carrier.sha256` and the two scope labels.
- prefix `0x`→`zz` (same length, non-hex): exit 0, `decoded.hex` **unchanged** — the block decodes a file whose prefix is not hex at all, because `[2:-1]` blindly drops two bytes.
- trailer `\n`→`!` (same length): exit 0, `decoded.hex` **unchanged**.
- trailer removed (38 B): exit 1, `ValueError: fromhex() arg must contain an even number of hexadecimal digits` — a crash, not a derivation of the trailer.
The value is TRUE (xxd above) but is carried by no printed field and no derivation; Q11 (QUALITY.md:23) rejects "a value is correct when re-derived but the entry carries no derivation", and names exactly this shape ("Constants such as header offsets are derived, not assumed"). This also falsifies the entry's own proposed Q11 basis at :200 ("Every claimed value is a field of the printed output").
Minimal correction (L1 only; I did not edit): print the carrier's first two and last byte in the r19 case object (e.g. `carrier.prefix` / `carrier.trailer` as byte reprs), assert them before slicing, and cite those fields at :56; or drop "`0x`-prefixed" from the prose and label the `[2:-1]` framing as a recorded authoring premise.

## Observation 6 — secondary, non-fatal: inventory rows name fields they do not cite (Q11 traceability)
:239 "r19 artifact bytes **and encoding**" cites `r19.recorded.artifact.bytes` = 39 only; the encoding value "hex" is printed at `r19.recorded.artifact.encoding` but uncited and uninventoried. :241 "r19 bytecode **kind / authenticity / hardfork**" cites `r19.recorded.bytecode.kind` = unknown only; I confirmed all 7 records have `deployment_authenticity` = unknown and `hardfork` = unknown, printed but uncited. :221 "pattern bytes **and length**" cites `summary.pattern_hex` only; the 9 is in `summary.pattern_length` (printed, uncited). :61-63 "all three digests name the same byte string" cites `r21.digest_scopes.subject` + `r21.carrier.sha256` only; `r21.digest_scopes.artifact` and `.bytecode` are printed but never cited/inventoried (0 hits in the file). All values are TRUE and printed — these are citation/traceability gaps, not wrong values.

## Observation 7 — Q13 no-guard boundary, re-verified in my lane
I re-ran the round-61 deletion sense on `corpus/verify_evm_evidence.py` (archived copy, restored byte-identical, sha256 8265a22f7be8df011cee319a332123a0bfcb011413839a31f602a037c15d0b49). Weakening one conjunct at a time — carrier digest, decoded digest, `artifact.sha256`, `bytecode.sha256`, `subject.digest.sha256`, candidate count, `decoded[target]==0x5b`, `runtime_execution` — leaves the script's own `--self-test` run at **exit 0 with "NEGATIVE REJECTED"** in all 8 cases: the deletions are undetected. The entry's :163-170 posture (no verifier credited; its own block not deletion-sensitive) is therefore correct for the digest-scope clauses.

## Inference
- [INFERENCE] The digest/identity substance of my lane is sound: the r19-vs-r21 byte relationship, all three digests' exact referents per case, and every label are independently re-derived and exact; nothing is hidden behind a disjunction, and no digest is claimed for bytes it did not hash (Q09 holds).
- [INFERENCE] Observation 5 is a missing in-entry derivation (Q11), not a wrong value and not a scope overreach: it cannot change any size, digest, scope label or byte string; it is the only asserted value in my lane with no printed field at all, and the block's hard-coded `[2:-1]` is exactly the assumed constant Q11 names.
- [INFERENCE] The Q13 boundary, the Provenance/base claims, and the inventory-to-output arithmetic are all sound as written.

## Unknown / not audited here
S028 line-anchor accuracy and the spec quotes (opcode-source seats); r22/r23/r24/r25/r26 prose specifics (R62FEvmR22Pairs, R62FEvmR23Empty, R62FEvmR24Span, R62FEvmR25R26); the general Q01–Q13 sweep (R62FEvmAllCriteria); Q13/guard credit and the readout-block deletion sensitivity (R62FEvmNoGuard); Q11 inventory completeness at large (R62FEvmQ11Inventory). The cause of the empty r23/r25/r26 pair lists stays unproved by design; I fitted no rule and assert no provider method, chain, execution or admission.

## Verification performed
Read-only: git rev-parse/archive/diff/ls-files; python3 3.14.8 stdlib only; sha256sum; xxd; grep/read of the entry and archived records. All code and mutation ran only on archived copies under /fast/scratch/hyaku/revenger-r62/R62FEvmCarrier/ (root, root_a3498e25, vtest, mut, mut2, del); the pristine archive and the lane tree are byte-unchanged (`git status --porcelain -- corpus/` empty; verifier restored to 8265a22f…; fixtures/records digests re-confirmed after every mutant). No bytecode executed, no chain/RPC, no producer called, no fixture JS, no build/lint/test, no git index/history mutation, no production edit.

VERDICT: BROKEN (Q11) on the r19 carrier format descriptor — the "`0x`-prefixed" claim has no in-entry derivation and the block assumes the `[2:-1]` framing; the minimal one-field correction above suffices. Everything else in my lane (r19/r21 sizes, full SHA-256s, decoded bytes, all 21 digest-scope labels, exact referents, no hidden disjunction, Provenance byte-identity, 67/67 inventory rows, 60/60 prose citations, Q13 non-credit) independently re-derives and HOLDS. Recommend not admitting C09 at this hash until the carrier framing is printed or the prefix claim is labelled recorded, then a focused non-author re-review.
Installs: none (no package installed or updated this run). Scratch: /fast/scratch/hyaku/revenger-r62/R62FEvmCarrier/.
