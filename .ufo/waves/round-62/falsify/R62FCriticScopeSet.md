GRADE: BROKEN — C04 `corpus/knowledge/round-62-commonjs-require-name-evidence.md` (C09 `round-62-evm-dispatch-byte-evidence.md`: PARTIAL)
Seat R62FCriticScopeSet (fresh critic; not author or corrector). Scope-set attack on both candidates against frozen claim scope. No repair, no admission.

## Frozen target
- revision `d97761952be256d145d298022de03091de91d358` (`git rev-parse …^{commit}` → same); claimbase 5bd4a90f…, pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7.
- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d9776195… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FCriticScopeSet/tree` (cwd=/), exit 0.
- sha256: C04 entry `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; C09 entry `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`; claims.md `41cc8b73…6c02`; lesson round-62 `cf0339eb…49d6ae`.

## Excluded-scope census (observation)
Excluded by claims.md:19-26: main/Electron role, runtime loading, export binding, package resolution, provider internals/method, chain, callable-interface completeness, present capability, saved-ID authentication, whole edge-set delta.
- C04: `main` and Electron appear only as disclaimers (entry:10). The only Electron mention is the README row label on the coverage-map line (entry:6; README:33). Export binding is disclaimed (items 16 and 19). Edge-set delta is disclaimed (items 15 and 25, plus the stdout note). Evidence IDs and provider fields are labelled recorded (item 6). `resolved_path` and the target-node kind/identity in items 8-9 are bare saved literals and are not interpreted as resolution. No reintroduction found.
- C09: callability is disclaimed via `discovery_completeness=unknown` (entry:141-143). Chain/RPC/producer are disclaimed (entry:25-29). Evidence IDs are recorded and not authenticated (entry:144-146). No present capability is claimed (Q05). Exception: F4 below.

## Findings
F1 [C04, actual contradiction, material] entry:64 (limitation 26): "The one network access this round was the read-only opening of the public ECMA-262 page for the S029 row".
  Evidence against, all at the frozen tree:
  - `.ufo/waves/round-62/build/R62SourceEcma.md:13-19` logs three fetched tc39 documents: the single page plus the multipage `ecmascript-language-statements-and-declarations.html` and `ecmascript-language-scripts-and-modules.html`, each with its own sha256.
  - `corpus/SOURCES.md:67`: "two guessed short-form mirror URLs returned 404".
  - `corpus/SOURCES.md:66` and lesson:63-65: S028 was opened this round from raw.githubusercontent, with "tag/ref/commit API responses".
  - The author's own plan, `R62JsEntry.md:25`, carries the same false count.
  Inference: the count "one" has no derivation and is false. Fails Q11 (a count carried without derivation, and wrong), and the entry's no-network scope statement is inaccurate.
  Smallest correction: limit the sentence to the readout ("the readout touched no network"), or state the round's opens with their ledger pointers (R62SourceEcma.md:12-19, SOURCES.md:66-67).
F2 [C04, missing requirement] entry:1 and entry:248 assert the S029 single-page SHA-256 `06db92a8…7d7f`.
  - No in-entry command derives it.
  - It carries no explicit "recorded" label. Contrast C09's entry:31-36, which labels its S028 values "recorded source facts".
  - `rg 06db92a8 R62JsEntry.md` → no match; the value originates in R62SourceEcma.md:15.
  Fails Q11: "A value cited only to prose is labeled recorded"; the lesson requires review of headers too (lesson:98-99). "cited here as the existing row" is not the required label.
  Smallest correction: label the digest (and the October 16 2026 draft identity) "recorded from R62SourceEcma.md:13-15, not re-derived".
F3 [C04, nonfatal wording] entry:68 presents a paraphrase as a quotation: "ADJ-06 sibling arbitration: operator-owned and unresolved; …". The lesson (lesson:29) is a table row: `| ADJ-06 sibling arbitration | Operator-owned and unresolved; …`. Correction: quote verbatim, or mark it as a paraphrase.
F4 [C09, provider-internals characterization, nonfatal] entry:50-51: "the raw (upstream) and normalized lists".
  - "upstream" asserts the data path from evmole to the adapter.
  - Nothing in the readout prints that label, and the entry cites no source for it.
  - The basis exists only in record `limitations[1]` ("Upstream may also report terminal metadata… retained in raw_result"). That index lies outside the S031 anchor, which covers `subject.digest`, `normalized_result.bytecode`/`.functions` and `limitations[4]` (SOURCES.md:45).
  - S031 scope excludes "provider semantics".
  Correction: delete "(upstream)", or label it as recorded with its record pointer.
F5 [C09, nonfatal wording] entry:101 and the Q03 row (entry:192) say the pattern is "derived from the files' own bytes". The code derives it from r19 only (entry:362, `derive_pattern(bytes.fromhex(r19[2:-1]…))`) and then searches the other files for it. Correction: write "derived from r19's bytes".
F6 [C09, Q11 candidate, for the C09 all-criteria seat] The `0x` prefix asserted at entry:56 is never printed.
  - The hex decode strips assumed constants `[2:-1]` (entry:362, entry:366).
  - My read shows the file is 39 bytes, starts with `b'0x'` and ends with `b'\n'`, so the value is correct. However, Q11 says "Constants such as header offsets are derived, not assumed".
  - The only in-entry support is that the decoded sha256 equals the saved bytecode sha256, which is output equality.
  Correction: print `carrier[:2]` and `carrier[-1:]` in the readout.
F7 [C09, nonfatal] entry:147-148 assert that the saved records carry `dispatch`, argument and state-mutability labels. The readout does not print these fields (I observed them in round-19 `normalized_result.functions`). Correction: label them recorded, or print the field names.
F8 [C04, nonfatal wording] entry:37 says "The column base is not assumed — it is shown".
  - The readout itself labels the raw saved `column` values as `start_column_0based` and `end_column_0based_end_exclusive` (entry:144-145) and slices under that convention.
  - The alternative 1-based slice (" { rot13, …") is never printed.
  - The evidence that remains is the coincidence of the saved columns with syntactic offsets. That is inference, not a shown base.
  Correction: move it to Inference, or print the alternative-convention readback.

## Checks run (observation)
- C04's embedded code and stdout blocks, hashed from the entry: python `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac` (129 lines) and stdout `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` (25 lines). Both equal the claimed values. This is output equality only and is not Q11 credit.
- js-r3 graph relations at the frozen tree: `['contains','exposes','imports','loads','maps_to']`. No non-`imports` edge mentions `require`, so the scoping to `imports` hides no require edge (bounded to js-r3).
- No fixture JavaScript or EVM was executed. No REA, network, provider or verifier was used.

## Unknown
- Whether the S029 clause text "Set value to ? GetV(value, propertyName)." matches the Oct 16 draft verbatim. Not re-opened by this seat; the source seats own it.
- Whether L1 treats F1 as admission-voiding or as correctable within the round (claims.md:47-50 permits correction plus focused re-review).

VERDICT: C04 BROKEN under Q11 (F1 false count of network accesses; F2 unlabelled source digest), plus nonfatal F3 and F8. C09 PARTIAL: no excluded scope reintroduced beyond F4's unlabelled "upstream"; F5-F7 are wording or derivation gaps, and F6 is routed to the C09 all-criteria seat as a Q11 candidate.
Installs: none.
