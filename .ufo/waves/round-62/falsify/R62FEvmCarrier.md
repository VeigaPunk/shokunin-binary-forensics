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

---

# Focused rereview — corrected candidate (L1 request), revision 47511b213bf556022869fa104a4bda9d7c9a3b95

Seat RevengerR61-2.R62FEvmCarrier · same lane, archived scratch only · no repair, no admission, no production/git edit.
Frozen revision 47511b213bf556022869fa104a4bda9d7c9a3b95 (rev-parse ^{commit} confirmed; HEAD = same) · C09 blob 63dbc34b387bfad4a51fd00c14a43d3433113bc2 · C09 file sha256 **35ad7d93936f31e02eae9431df6185f31d0c38b079579586ab2fce15b80f2e4d** (L1-supplied; matches the extracted file exactly). Archive: `git -C …/revenger-shokunin archive 47511b21…` → …/R62FEvmCarrier/root_r475. `git diff --name-only d9776195… 47511b21… -- corpus/fixtures corpus/live` → empty: fixtures and saved records byte-identical to my original target.

GRADE: PARTIAL — the Q11 defect I reported is CURED (carrier framing now derived, printed and mutation-refused); one NEW non-asserted defect remains in the replacement machinery (`template_enclosing_instruction` for r19), plus the same non-fatal inventory/pointer gaps.

## Observation 1 — my original Q11 finding is cured: framing derived from bytes, printed, and mutation-refused
New `decode_carrier()` (entry :386-405) derives the framing from the carrier's own bytes: it prints `carrier_form` (`ascii_hex_text` for r19, `raw_bytes` for the other six), `carrier_prefix_bytes` `[48,120]`/`carrier_prefix_hex` `3078`, `carrier_trailer_bytes` `[10]`/`carrier_trailer_hex` `0a`, `decode_body_slice` `[2,38]`, and `decode_checks` {ascii_prefix_is_0x:true, body_is_even_length_hex:true, trailer_is_lf:true}. The only remaining literal slice is `body = raw[2:-1]` (:399) — now guarded by the three checks, not assumed. Independently confirmed from bytes: len 39, prefix b'0x' (`3078`), trailer b'\n' (`0a`), body 36 chars, even, all hex → 18 decoded bytes; `raw[2:len(raw)-1]` = `[2,38]`, matching the printed slice. Prose :54-62 now cites these fields; no "`0x`-prefixed" claim rests on an unprinted constant. Inventory rows :250-260 name each field.

## Observation 2 — the zz-prefix mutation is now refused, and every framing mutation is visible
Archived-copy mutants of the corrected block (cwd=/, TMPDIR=<scratch>/tmp; original restored, digest re-confirmed):
| mutant | exit | stderr | outcome |
|---|---|---|---|
| prefix `0x`→`zz` | 1 | 726 B | REFUSED `ValueError: r19 has no PUSH4 and JUMPI instruction pair` (the `zz` carrier is not hex text, so it is not decoded as hex) |
| prefix `0x`→`0X` | 1 | 726 B | REFUSED, same ValueError |
| trailer `\n`→`!` | 1 | 739 B | REFUSED `ValueError: hex-text carrier has no trailing newline: b'b00!'` |
| trailer removed (38 B) | 1 | 739 B | REFUSED `ValueError: hex-text carrier has no trailing newline: b'5b00'` |
| body odd length | 1 | 743 B | REFUSED `ValueError: hex-text carrier body is not an even-length hex string` |
| non-hex body char | 1 | 743 B | REFUSED, same ValueError |
| body uppercased | 0 | 0 B | accepted; `decoded.hex` unchanged (uppercase hex is the same value), only `carrier.sha256` and the two subject/artifact scopes change → correctly surfaced |
Every mutation is now either refused or visibly different; none passes silently with unchanged derived fields. This is the defect I reported, cured.

## Observation 3 — digest referents unchanged, and still exactly classified
The corrected output's 21 `digest_scopes` labels are byte-identical to the d9776195 output (carrier sha, decoded sha/bytes and all scopes compared per case: identical). Re-classified with my own independent referent test over five candidate byte strings (carrier_file, decoded, hex_text_no_0x, hex_text_upper, carrier_stripped): **all 21 agree** — r19 subject/artifact `carrier_file_bytes_only`, r19 bytecode `decoded_bytecode_bytes_only`, the other 18 `carrier_and_decoded_same_byte_string`. The 39-byte stripped variant still does not match r19's subject/artifact digests, so the referent remains the exact 39-byte file including its trailing `\n`. Round-61 F2 (a disjunction hiding the referent) stays cured. r19 carrier 39 B/`294e6fd2…`, decoded 18 B/`d1086bce…`, r21 carrier 18 B raw/`d1086bce…` = r19 decoded bytes — unchanged and re-verified.

## Observation 4 — provenance, inventory, prose, and source/encoding pointers
- Reproduce block re-extracted from the corrected entry (190 lines) and run: exit 0, stderr 0, stdout **byte-identical** to the corrected `## Provenance` block; also byte-identical on the base tree a3498e25…
- Inventory re-audited mechanically: **95 rows, 0 real mismatches** (the single flag is my comparator reading the unquoted hex `3078` as a number vs the printed string "3078" — the entry's own table convention for every hex row: `63deadbeef14601057`, `294e6fd2…`, `0a`). **82 prose field citations, all resolve in the printed output and all have an inventory row.**
- Source pointer resolves: the header now cites **S028** (opcode values), **S031** (authored fixtures + decoded bytes) and **S026** (the seven saved records) — all three exist in `corpus/SOURCES.md` at this revision, tier A, no rejected row cited; S026's citing-files cell now names this entry (that is the only SOURCES.md row change, +1 cell).
- Encoding pointer resolves: `r19.recorded.artifact.encoding` = `hex` (:273) and `summary.distinct_artifact_encoding_values` = `["hex","raw"]` (:249), both printed and inventoried; all eight `summary.distinct_*` aggregates match my independent recomputation over the seven saved records exactly (evidence_kind inferred; discovery_completeness unknown; runtime_execution not-performed; provider_version evmole@0.9.3; bytecode kind/hardfork/deployment_authenticity unknown; artifact encodings hex+raw).
- S026's row text "full IDs and file digests in the citing entry" holds: all seven `evidence_id` values and all seven record-file digests appear in the entry's Provenance stdout.

## Observation 5 — NEW DEFECT (non-fatal, Q11 traceability; r19 printed field is wrong but unasserted)
Entry :449-450 computes `template_enclosing_instruction=[[o, op] for o, op, im in ins if o <= po < o + 1 + len(im)]`. `im` is the immediate's **hex string**, so `len(im)` is twice its byte length; the extent test therefore spans twice the real instruction. Verified independently:
- r19 (`po`=12): the entry prints `[[6, 99], [12, 96]]`; the correct byte extent is `[[12, 96]]`. The PUSH4 at offset 6 has a 4-byte immediate (bytes 7–10) and does **not** enclose byte 12. The printed r19 object is internally inconsistent: `template_push1_byte_offset`=12 with `template_push1_byte_is_instruction_opcode`=true (byte 12 IS the PUSH1 opcode at offset 12) while the same object lists the PUSH4 at 6 as enclosing it.
- r24 (`po`=7): unaffected — `[[0, 127]]` is correct under both the buggy and the byte-extent rule (PUSH32's 32-byte immediate spans 1–32).
Severity: the wrong value is printed in the r19 Provenance line but is **not** asserted in the prose and has **no** inventory row (only r24's `[[0,127]]` is asserted, :121-122 and :316, and it is correct). It touches no digest scope, no carrier framing, no r24 target. Minimal correction (L1 only): use the byte length, `len(im)//2`, at :450 — or drop the field, since no claim rests on it.

## Observation 6 — residual non-fatal inventory gaps (unchanged class)
Only r19's `evidence_id` and record digest are named in the inventory; the other six records' ids and digests appear in the Provenance stdout but have no inventory row (S026's row points at the entry as a whole, so the pointer itself resolves). Two inventory labels still name more than the single field they cite: "raw and normalized pair counts equal" (cites `summary.raw_and_normalized_pair_counts_equal` = true — the label is a sentence, the value is a boolean, fine) and "template bytes and length" (cites `summary.template_hex`; the length 9 has its own row `summary.template_length` = 9 at :241, so this is now covered).

## Inference
- [INFERENCE] The Q11 failure I reported (the "`0x`-prefixed" claim asserted with an unprinted, assumed `[2:-1]` framing) is cured on the merits: the framing is now derived from the bytes, printed in five named fields plus three boolean checks, and any deviation is refused with a non-zero exit. My lane's central question — exact digest referents with no disjunction hiding identity — still HOLDS on all 21 digests.
- [INFERENCE] The new `template_enclosing_instruction` defect is real but currently unasserted: it is a wrong value in a printed line, not a wrong claim, so it is a traceability/derivation defect (Q11-adjacent) rather than the "correct value with no derivation" shape of the original finding. It should be corrected, but on its own it does not falsify any prose sentence, any digest scope, or any coverage claim.
- [INFERENCE] Q13 posture unchanged and correct: no verifier credited, own block explicitly not deletion-sensitive, and my earlier 8/8 verifier conjunct-deletion result (undetected) stands.

## Unknown / not audited here
Still outside my lane: S028 line-anchor accuracy and spec quotes (opcode-source seats); r22/r23/r25/r26 prose specifics; the general Q01–Q13 sweep; Q13/guard credit; Q11 inventory completeness at large; the C04 sibling entry. No provider method, chain, execution or admission is asserted anywhere by me.

## Verification performed
Read-only git (rev-parse, archive, diff, ls-files); python3 3.14.8 stdlib; sha256sum; grep/read. All runs and mutations on archived copies only, under /fast/scratch/hyaku/revenger-r62/R62FEvmCarrier/ (root_r475, m475, plus the earlier root/root_a3498e25/vtest/mut/mut2/del). Pristine archive and lane tree byte-unchanged; every mutated fixture restored and its digest re-confirmed (294e6fd2…); verifier restored to 8265a22f…. No bytecode executed, no chain/RPC, no producer called, no fixture JS, no build/lint/test, no git index/history mutation, no production edit, no repair to the entry.

VERDICT: PARTIAL on 47511b21… / C09 sha256 35ad7d93…. My reported Q11 defect is CURED and independently verified (framing derived, printed, zz-prefix and every framing mutant refused or visibly different; all 21 digest referents unchanged and exactly classified; 95/95 inventory rows and 82/82 prose citations resolve; S028/S031/S026 and the encoding pointers resolve). One new non-fatal defect: r19's printed `template_enclosing_instruction` `[[6,99],[12,96]]` is wrong (`len(im)` counts hex characters, not bytes; correct = `[[12,96]]`) — unasserted, no prose sentence or digest scope depends on it; minimal fix `len(im)//2` at :450. Recommend: correct :450, then admit; the C09 coverage substance (carrier/decoded identity, digest scopes, r24 span/target) is verified sound on this revision.
Installs: none (no package installed or updated this run).

---

# Addendum — observed in-progress working-tree correction (uncommitted), sha256 e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196

Seat RevengerR61-2.R62FEvmCarrier · observation only, read-only snapshot · HEAD still 47511b213bf556022869fa104a4bda9d7c9a3b95, so this is **not** the frozen revision I was asked to review and I issue no verdict on it.

While finishing, the lane working tree moved ahead of HEAD: `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` is modified (index 63dbc34→324a7ff) and `corpus/lessons/round-62.md` is modified. I did not make these edits (my only write is this report; `git status --porcelain -- corpus/` shows these two as modified by another seat). I snapshotted the file read-only to …/R62FEvmCarrier/wt/entry_wt.md and verified the snapshot only.

Observed in that snapshot (sha256 e7bf76aa…, an uncommitted intermediate, not a frozen target):
- **My Observation 5 finding is corrected there**: the block now uses `len(im) // 2` and r19 prints `template_enclosing_instruction` = **[[12,96]]** (was [[6,99],[12,96]] at 47511b21) — the byte-extent-correct value I derived; r24 stays [[0,127]]. A new field `template_push1_template_index` = 6 is printed for both r19 and r24, and the prose now distinguishes "at r24 file offset 7 — template index 6".
- The entry also adds r19's enclosing instruction to the inventory, plus carrier-form/decode-slice rows for r21–r26 and template occurrence rows for r19/r21/r22/r23/r25/r26.
- Verified on the snapshot: the worktree's own Reproduce block run against the frozen r475 tree → exit 0, stderr 0, stdout **byte-identical** to its own printed Provenance block; **116 inventory rows / 0 mismatches**; **84 prose citations, all resolve and all inventoried**; all 21 digest scopes still match my independent five-candidate referent classifier.
- The source header also gains the exact S028 URL and file:line anchors, and Q01 is now "pass, pending final review".

Caveat for L1: this is a work-in-progress file, not a committed revision; my PARTIAL verdict stands against the frozen 47511b21 / 35ad7d93… hash I was asked to review. If the next frozen revision carries the `len(im) // 2` change plus the added rows, the Observation 5 defect is cured and the lane's substance (carrier/decoded identity, all 21 digest referents, r24 span/target) is verified sound — but that must be confirmed against a committed hash, not against a moving working tree.

VERDICT ADDENDUM: no new verdict on an uncommitted intermediate. My frozen-target verdict (PARTIAL on 47511b21 / 35ad7d93…) is unchanged and stands as recorded above.
Installs: none.

---

# Exact-hash independent re-review of the corrected candidate — sha256 e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196

Seat RevengerR61-2.R62FEvmCarrier · fresh non-author seat (not the corrector) · read-only verification · no repair, no admission, no production/git edit.
Target: `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` at working-tree sha256 **e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196**, the hash recorded in `.ufo/waves/round-62/falsify/unit-correction.json` as `candidate_sha256` (prior revision 47511b213bf556022869fa104a4bda9d7c9a3b95 / prior candidate 35ad7d93936f31e02eae9431df6185f31d0c38b079579586ab2fce15b80f2e4d). The ledger's `admission` field requires "exact-hash independent re-review"; this section supplies it for my lane. NOTE: at the time of this review the file is a **working-tree state, not yet a committed revision** — HEAD is still 47511b21…; my earlier Addendum (sha256 e7bf76aa…) observed the same bytes. I verified a fresh copy taken from the live file (…/fin/entry.md, sha256 e7bf76aa…) and the earlier snapshot independently; both hash identically.

GRADE: HOLDS (for this lane) — the M28 defect is corrected at the recorded hash and nothing else in my lane regressed.

## Observation 1 — the ledger's red-before is cleared, expected-after achieved
Ledger: `finding` = "template_enclosing_instruction used hex-character length as byte extent"; `minimal_fix` = "len(im) -> len(im)//2"; `red_before` = "r19 enclosing template PUSH1 byte: [[6,99],[12,96]] incorrectly includes earlier PUSH4"; `expected_after` = "r19 [[12,96]], r24 [[0,127]]; same primary input bytes".
Verified on e7bf76aa…: the block's extent expression is now `if o <= po < o + 1 + len(im) // 2` (entry :479), and the printed output gives r19 `template_enclosing_instruction` = **[[12,96]]** and r24 = **[[0,127]]** — exactly the ledger's expected_after. The red-before `[[6,99],…]` no longer appears for r19. Primary input bytes unchanged: r19 carrier still 39 B / `294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827`, decoded 18 B / `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`, r21 carrier 18 B raw / `d1086bce…`, and `r19 decoded == r21 carrier bytes` still True.

## Observation 2 — provenance reproduces at this exact hash
The Reproduce block re-extracted fresh from the live file (…/fin/readout.py) and run against the frozen tree with unmodified fixtures/records (cwd=/, TMPDIR=<scratch>/tmp): exit 0, stderr 0 bytes, stdout **byte-identical** to this hash's own printed `## Provenance` block (cmp clean). The Provenance stdout is therefore exact and untruncated for e7bf76aa…, and the entry's `## Evidence inventory` is synchronized with it.

## Observation 3 — inventory and prose resolve completely at this hash
**116 inventory rows, 0 mismatches** — every cited field resolves in the printed output and every stated value matches (my comparator reads the table's unquoted hex as a string, the entry's own convention). **84 prose field citations: all resolve in the printed output, all have an Evidence-inventory row.** The newly added rows resolve too: r19's `template_enclosing_instruction` = [[12,96]], `template_push1_byte_offset` = 12, `template_push1_byte_is_instruction_opcode` = true, the new `r24.template.template_push1_template_index` = 6, and the added carrier-form / decode-body-slice rows for r21–r26 (raw_bytes, slice [0,length]).

## Observation 4 — all 21 digest referents unchanged and exactly classified
Re-classified with my own independent referent test over five candidate byte strings (carrier_file, decoded, hex_text_no_0x, hex_text_upper, carrier_stripped): **all 21 agree with the printed labels** — r19 subject/artifact `carrier_file_bytes_only`, r19 bytecode `decoded_bytecode_bytes_only`, the other 18 `carrier_and_decoded_same_byte_string`. The 39-byte stripped variant still does not match r19's subject/artifact digests, so each referent remains the exact byte string named. No disjunction hides an identity; round-61 F2 stays cured. The r19/r21 byte identity and all full SHA-256 values are unchanged from my earlier reviews.

## Observation 5 — framing-mutation regression on this exact hash (cure survives the new edit)
Mutants of the r19 carrier against the e7bf76aa… block (archived copies; original restored and digest re-confirmed `294e6fd2…`):
| mutant | exit | stdout | stderr | outcome |
|---|---|---|---|---|
| prefix `0x`→`zz` | 1 | 0 B | 723 B | REFUSED `ValueError: r19 has no PUSH4 and JUMPI instruction pair` |
| prefix `0x`→`0X` | 1 | 0 B | 723 B | REFUSED, same |
| trailer `\n`→`!` | 1 | 0 B | 736 B | REFUSED `ValueError: hex-text carrier has no trailing newline: b'b00!'` |
| trailer removed (38 B) | 1 | 0 B | 736 B | REFUSED `ValueError: hex-text carrier has no trailing newline: b'5b00'` |
| body odd length | 1 | 0 B | 740 B | REFUSED `ValueError: hex-text carrier body is not an even-length hex string` |
| non-hex body char | 1 | 0 B | 740 B | REFUSED, same |
| body uppercased | 0 | 19682 B | 0 B | accepted; same decoded value, carrier digest and scopes visibly change |
Every framing mutation is refused or visibly different; none passes silently with unchanged derived fields. The Q11 cure from my first finding is intact at this hash.

## Observation 6 — source and encoding pointers at this hash
The source header now carries the exact S028 URL plus file:line anchors and names S031 and S026; all three rows exist in `corpus/SOURCES.md` (tier A, no rejected row cited). Encoding pointers resolve: `r19.recorded.artifact.encoding` = hex and `summary.distinct_artifact_encoding_values` = ["hex","raw"], both printed and inventoried; all eight `summary.distinct_*` aggregates match my independent recomputation over the seven saved records.

## Inference
- [INFERENCE] The M28 defect is genuinely fixed at the recorded hash, by the exact minimal fix named in the ledger, with the primary input bytes unchanged and the red-before cleared. The r19 enclosing-instruction value is now the byte-extent-correct [[12,96]], and it no longer contradicts the adjacent `template_push1_byte_is_instruction_opcode` = true in the same printed object.
- [INFERENCE] My lane's substantive C09 claims — carrier/decoded identity for r19 vs r21, and the exact referent of each of the 21 saved digests — are verified sound at e7bf76aa…, with no disjunction and no scope drift; the earlier carrier-framing cure still holds under regression.
- [INFERENCE] Because this hash is not yet committed, my HOLD is conditional on the file being committed unchanged: if the bytes that reach the next commit differ from e7bf76aa…, the HOLD must be re-checked against the committed hash.
- [INFERENCE] The remaining non-fatal gaps I noted earlier (only r19's evidence_id and record digest have inventory rows, though all seven appear in the Provenance stdout) are unchanged in class and remain non-material for my lane.

## Unknown / not audited here
Still outside my lane: S028 line-anchor accuracy and the spec quotes themselves (opcode-source seats); r22/r23/r25/r26 prose specifics; the general Q01–Q13 sweep; Q13/guard credit; Q11 inventory completeness at large; the C04 sibling entry. I assert no provider method, chain, execution or admission.

## Verification performed
Read-only: git rev-parse/log/diff/status; python3 3.14.8 stdlib; sha256sum. The candidate was copied read-only to …/fin/ and …/wt/ (both sha256 e7bf76aa…) and every run and mutation used archived copies under /fast/scratch/hyaku/revenger-r62/R62FEvmCarrier/ (root_r475, fin, fin_mut, wt + earlier root, root_a3498e25, vtest, mut, mut2, del, m475). Pristine archive byte-unchanged (root_r475 still holds 35ad7d93…, the committed 47511b21… version); every mutated fixture restored and its digest re-confirmed (294e6fd2…). No bytecode executed, no chain/RPC, no producer called, no fixture JS, no build/lint/test, no git index/history mutation, no production edit, no repair to the entry — my only write is this report.

VERDICT: HOLDS for my lane at sha256 e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196 — M28 corrected exactly as the ledger specifies (r19 [[12,96]], r24 [[0,127]]), provenance byte-identical, 116/116 inventory rows and 84/84 prose citations resolve, all 21 digest referents unchanged and exactly classified, framing mutations still refused. Conditional on these bytes being committed unchanged; no admission claimed, no repair made.
Installs: none (no package installed or updated this run).

---

# FINAL FROZEN VERDICT — committed revision 8e2f082d405fc130fc1e8523a0763672289f287a

Seat RevengerR61-2.R62FEvmCarrier · fresh non-author seat · exact-hash confirmation of the committed bytes · no repair, no admission, no production/git edit.
Committed revision **8e2f082d405fc130fc1e8523a0763672289f287a** ("round-62: correct hex-character versus byte extent; preserve exact-hash reviews and M28 before admission"). C09 file `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`, git blob **324a7ffe8173066a7bf96b94a18c482247100866**, file sha256 **e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196**.

## Confirmation that the committed bytes ARE the bytes I reviewed
- `git show HEAD:corpus/knowledge/round-62-evm-dispatch-byte-evidence.md | sha256sum` → `e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196`, equal to the hash I reviewed.
- `cmp` of the committed blob against my reviewed copy …/fin/entry.md → **byte-identical** (no difference). Working tree == HEAD for this file (same sha256; `git status --porcelain -- corpus/` empty).
- Independent archive of the commit (…/root_8e2f/) yields the same file sha256 `e7bf76aa…`.
- Primary inputs unchanged by the commit: `diff -rq` over `corpus/fixtures` → identical; all seven saved records `corpus/live/runs/round-{19,21,22,23,24,25,26}/inspection.json` byte-identical to the tree I verified against.

## Verdict for this lane (C09 carrier / digest-scope / referent lane) — no probe re-run needed
All findings below were established on these exact bytes and are carried forward unchanged; per the L1 instruction no probe was re-run, and none needed to be, because the committed bytes are byte-identical to the reviewed ones.
1. **Original Q11 defect (BROKEN at d9776195…): CURED.** Carrier framing is derived from the carrier's own bytes and printed (`carrier_form` ascii_hex_text, prefix `[48,120]`/`3078`, trailer `[10]`/`0a`, `decode_body_slice` `[2,38]`, three passing `decode_checks`); the residual literal slice `raw[2:-1]` is guarded by those checks. Every framing mutant I ran is refused (exit 1, stdout 0 B, explicit ValueError) or visibly different — prefix `0x`→`zz`, prefix `0x`→`0X`, trailer `\n`→`!`, trailer removed, odd-length body, non-hex body char; uppercased body accepted with the same decoded value and visibly changed carrier digest/scopes. No framing mutation passes silently with unchanged derived fields.
2. **M28 unit defect (PARTIAL at 47511b21…): CURED at the committed hash.** The extent expression is `len(im) // 2`; printed r19 `template_enclosing_instruction` = **[[12,96]]** (red-before `[[6,99],[12,96]]` cleared) and r24 = **[[0,127]]**, matching the ledger's `expected_after` in `.ufo/waves/round-62/falsify/unit-correction.json`. Primary input bytes unchanged: r19 carrier 39 B / `294e6fd2…`, decoded 18 B / `d1086bce…`, r21 carrier 18 B raw / `d1086bce…`, and `r19 decoded == r21 carrier bytes` still True.
3. **Digest referents and identity: HOLDS.** All 21 `digest_scopes` labels match my independent five-candidate referent classifier (carrier_file, decoded, hex_text_no_0x, hex_text_upper, carrier_stripped): r19 subject/artifact `carrier_file_bytes_only`, r19 bytecode `decoded_bytecode_bytes_only`, the other 18 `carrier_and_decoded_same_byte_string`. The stripped 39-byte variant still does not match r19's subject/artifact digests, so each referent names the exact byte string; no disjunction hides an identity; round-61 F2 stays cured.
4. **Prose / code / output / inventory agreement: HOLDS.** The entry's Reproduce block (re-extracted from these bytes) run against the committed tree → exit 0, stderr 0, stdout byte-identical to this hash's own printed `## Provenance`; **116 inventory rows / 0 mismatches**; **84 prose field citations, all resolving in the printed output and all carrying an Evidence-inventory row**; source pointer S028 (with exact URL and file:line anchors) / S031 / S026 all present in `corpus/SOURCES.md` (tier A, no rejected row cited), and the encoding pointers (`r19.recorded.artifact.encoding` = hex, `summary.distinct_artifact_encoding_values` = ["hex","raw"]) resolve; all eight `summary.distinct_*` aggregates match my independent recomputation over the seven saved records.
5. **Residual, non-material, unchanged in class:** only r19's `evidence_id` and record digest have inventory rows (all seven appear in the Provenance stdout, and S026's row points at the entry as a whole). No prose sentence, digest scope, or coverage claim depends on it.

## Admission status observed (recorded, not flipped by me)
At this commit `corpus/README.md` C09 still reads status "— (round-61 candidate rejected; see lessons/round-61.md)" with the row's last cell `uncovered`, and the README does not yet name `round-62-evm-dispatch-byte-evidence.md`; the entry's own header still reads `admission-status: candidate`. No held flip, no admission and no README edit was made by me, and I assert none.

VERDICT: **HOLDS** for this lane at committed revision **8e2f082d405fc130fc1e8523a0763672289f287a**, C09 file sha256 **e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196**, blob 324a7ffe8173066a7bf96b94a18c482247100866. My original BROKEN finding (d9776195…, Q11 carrier framing) and the subsequent PARTIAL finding (47511b21…, M28 unit extent) are both CURED at this exact committed hash, with no regression in my lane; the one residual gap is a non-material inventory-completeness item. This is a lane verdict and a recommendation, not an admission — L1 adjudicates, and the C04 sibling's own exact-hash review remains outside my scope.
Installs: none (no package installed or updated this run).
