# SrcYellowPaperJumpdest — C1/C09 source opening (round 61)

Read-only seat `CloseChousa26.SrcYellowPaperJumpdest-10`, access 2026-10-21 (UTC 15:44). Scope: valid jump destinations and JUMPI semantics for C09. No lane/corpus edits; this report is the only file written.

## 1. Fetch and document identity

- URL: `https://ethereum.github.io/yellowpaper/paper.pdf`. `curl -sS -L -o /tmp/revenger-r61-yellowpaper.pdf -w 'HTTP %{http_code} size=%{size_download} type=%{content_type}'` → `HTTP 200 size=597589 type=application/pdf`; `curl -I -L` → `last-modified: Tue, 04 Feb 2025 14:03:41 GMT`, `etag: "67a21e3d-91e55"`.
- Pinned bytes: `sha256sum` → `d67c009c5d5a0542c8288aee3c4d470b3e2dbe6e664f72f00011543608477fa9` (597589 B). `pdfinfo`: 42 pages, `CreationDate/ModDate: Tue Feb 4 11:02:58 2025 -03`, `Producer: pdfTeX-1.40.16`.
- Title page (PDF p.1, `pdftotext -f 1 -l 1 -layout`): `ETHEREUM: A SECURE DECENTRALISED GENERALISED TRANSACTION LEDGER` / `SHANGHAI VERSION efc5f9a – 2025-02-04`. Only revision string on the page; every page footer repeats `SHANGHAI VERSION <n>`.
- Text extraction: `pdftotext` (poppler, pre-installed). Page renders: `pdftoppm -f N -l N -r 150 -png`; prose quotes below were also read on the rendered page. Poppler's text layer maps `≠` to `6=` and `∉` to `/ ∈`; the render shows the correct glyphs (p.15).

## 2. Section anchors

- §9.3 Execution Environment, p.14: `• I_b , the byte array that is the machine code to be executed.` (D is evaluated over this code array).
- §9.4.2 Exceptional Halting, eq. (158), p.15: the halt predicate `Z` includes the JUMP and JUMPI invalid-destination disjuncts.
- §9.4.3 Jump Destination Validity, eqs. (160)–(162), p.15: `D(c) ≡ D_J(c,0)`, the `D_J` recursion and `N`.
- Appendix H §H.2 Instruction Set: rows `0x56 JUMP`/`0x57 JUMPI` on p.35, `0x5b JUMPDEST` on p.36; §H.1 p.29 and Appendix G p.28 give `Gjumpdest = 1`.

## 3. Verbatim quotes (de-hyphenated line breaks only; word counts computed)

- Q1 (§9.4.3, p.15, 14 words): "We define this as any position in the code occupied by a JUMPDEST instruction." `python3` exact-substring match on the de-hyphenated page text → `match=True`.
- Q2 (§9.4.3, p.15, 19 words): "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations" — same sentence, substring of the verified 30-word sentence.
- Q3 (§9.4.3, p.15, 11 words; continuation of Q1/Q2's sentence): "and must appear within the explicitly defined portion of the code" — the sentence ends "(rather than in the implicitly defined STOP operations that trail it)." (p.15 render).
- Q4 (§H.2 row 0x5b, p.36, 7 words): "Mark a valid destination for jumps." (read on the p.36 render; row continues "This operation has no effect on machine state during execution.").

## 4. Equation transcription (verified against p.15 render; subscripts flattened)

- (158), §9.4.2, p.15: `(w = JUMP ∧ μ_s[0] ∉ D(I_b)) ∨ (w = JUMPI ∧ μ_s[1] ≠ 0 ∧ μ_s[0] ∉ D(I_b))` — JUMPI's invalid-destination halt is guarded by a nonzero test.
- (161), §9.4.3, p.15: `D_J(c,i) ≡ {} if i ⩾ ‖c‖; {i} ∪ D_J(c,N(i,c[i])) if c[i] = JUMPDEST; D_J(c,N(i,c[i])) otherwise`.
- (162), §9.4.3, p.15: `N(i,w) ≡ i + w − PUSH1 + 2 if w ∈ [PUSH1,PUSH32]; i + 1 otherwise` (skips the opcode plus w immediate bytes).
- §H.2 p.35: `0x56 JUMP 1 0` / `0x57 JUMPI 2 0` with `J_JUMPI(μ) ≡ μ_s[0] if μ_s[1] ≠ 0; μ_pc + 1 otherwise`; p.36: `0x5b JUMPDEST 0 0`.
- Appendices: `Gjumpdest 1` (p.28); `JUMP` in `W_mid`, `JUMPI` in `W_high` (p.29 section text) — gas only, no interface semantics.

## 5. What this source does NOT state (sweeps on `/tmp/revenger-r61-yp.txt`)

- No selector/ABI/dispatcher concept: `grep -ci selector` = 0, `dispatcher` = 0, `metadata` = 0; `grep -ci abi` = 4, all incidental English (`capability`, `ability`, `readability`, `Availability`), never the contract ABI. The PUSH4→selector link and selector→destination mapping are [INFERENCE], not paper statements.
- No printed `0x63`/`PUSH4` row: `grep -c 'PUSH4'` = 0, `grep -c '0x63'` = 0; `pdftotext -f 36 -raw | grep -oE '0x[0-9a-f]{2} PUSH[0-9]+'` → `0x5f PUSH0`, `0x60 PUSH1`, `0x61 PUSH2`, `0x7f PUSH32` only. The 4-byte width, δ=0, α=1 for 0x63 are family inferences from eq. (162) `w ∈ [PUSH1,PUSH32]` and the PUSH1/PUSH2/PUSH32 formulas.
- No reachability or disassembly notion: `grep -ci reachab` = 0, `disassembly` = 0, `dispatch` = 0, `jump table` = 0. `D_J` scans every `i < ‖c‖` and includes every boundary JUMPDEST whether or not any JUMP targets it; it is a candidate set, not the taken-target set.
- No section carve-outs: the scan has only the `i ⩾ ‖c‖ → ∅` bound and the boundary rule; it never excludes compiler metadata/CBOR trailers or data sections. [INFERENCE] under this definition a boundary-aligned `0x5b` in an appended metadata tail is in `D_J`, even if no dispatcher targets it.
- No client/fork coverage beyond Shanghai: title page pins `efc5f9a`; `grep -c EOF` = 0; no client-conformance claim.
- No obligation to validate a destination on JUMPI's not-taken path: eq. (158) requires `μ_s[1] ≠ 0` for the halt; `J_JUMPI` writes `μ_s[0]` only then.
- No statement that a JUMPDEST is a function entry; row 0x5b only marks a jump destination and has no machine-state effect.

## 6. C09 use (observation vs inference, for the entry author)

- Observation: to decide whether offset k is a valid destination, decode boundaries from offset 0 with eq. (162); a `0x5b` inside PUSH immediate data is not in `D_J`, and destinations must satisfy `k < len(code)`.
- Observation: `D_J` is defined over the whole code array, so valid-but-unreached JUMPDESTs are included; "candidate destination" must stay distinct from "taken destination", consistent with the saved records' `discovery_completeness: unknown` and `runtime_execution: not-performed` (`corpus/verify_evm_evidence.py:51-53`).
- [INFERENCE] the PUSH4 immediate equals code bytes at `pc+1..pc+4`, zero-padded past `‖I_b‖` ("The function c ensures the bytes default to zero if they extend past the limits.", §H.2 p.36) — the elided-PUSH4 derivation must be labeled inference.

## 7. Proposed SOURCES.md row (contract v1, 11 columns)

Merge with the Yellow Paper row already drafted in `.ufo/waves/round-61/build/ScribeSourcesRowsEvm.md` §4 (their provisional S017): same URL, one registry row only. L1 assigns the id; registry currently ends at S015.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016–S017 TBD (merge) | Ethereum Yellow Paper, Shanghai version efc5f9a (2025-02-04) — https://ethereum.github.io/yellowpaper/paper.pdf | spec | A | the paper's own valid-jump-destination definition and JUMP/JUMPI/JUMPDEST exceptional-halt semantics, Shanghai revision only | §9.3 p.14 (`I_b`); §9.4.2 eq. (158) p.15; §9.4.3 eqs. (160)–(162) p.15; App. H §H.2 rows 0x56/0x57 p.35 and 0x5b p.36; sha256 d67c009c…77fa9 | Only a JUMPDEST on an instruction boundary, never PUSH immediate data, inside `i < ‖code‖` is a valid jump destination, and an invalid JUMPI destination halts only when its test is nonzero. | queued (flip to mined when the C09 entry cites it) | 2026-10-21 | 180d | — |

Tier A holds only for that scope: not for client behavior, reachability, selector semantics, dispatcher shape, or post-Shanghai forks.

## 8. Gate lines for `corpus/lessons/round-61.md` (URL, access date, located quote)

- Yellow Paper — https://ethereum.github.io/yellowpaper/paper.pdf — accessed 2026-10-21 — "We define this as any position in the code occupied by a JUMPDEST instruction." (§9.4.3 Jump Destination Validity, PDF p.15)
- same URL/date — "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations" (§9.4.3, PDF p.15)
- same URL/date — "Mark a valid destination for jumps." (App. H §H.2, row 0x5b, PDF p.36)

Installs/updates: none; poppler (`pdftotext`, `pdfinfo`, `pdftoppm`) was already present, no pacman transaction (host pause respected). Files written: this report only. No git/jj mutation.

VERDICT: Yellow Paper Shanghai efc5f9a opened (HTTP 200, sha256 d67c009c…77fa9); D_J validity (boundary, PUSH-data exclusion, code-length bound) and the JUMPI nonzero-test halt guard are sourced with three located quotes, and the paper states no selector/dispatcher/reachability semantics — row merged with sibling S017, status queued.
