GRADE: PARTIAL — C09 Unknown 1 ("two post-hoc rules fit all seven outputs; no fixture separates them"), landed ab580698212258a55e43e9bb9bf6ac78c91eae2a

Seat: RevengerR61-2.W3EvmTwoRulesFit. Extract: `git archive --format=tar ab580698…` (read-only; tar sha256 c774b23e31657f93c3818cc51eaf6cf53e287819805bdf2534f4ca9f880cab24) → /tmp/revenger-r61w3-W3EvmTwoRulesFit/landed. Script: /tmp/revenger-r61w3-W3EvmTwoRulesFit/two_rules.py (stdlib, Python 3.14.8; static byte walk + JSON read; no bytecode executed; no chain, no REA producer). Run from archive root: `python3 -B two_rules.py`, exit 0.

## Matrix (independent code; compared with saved `normalized_result.functions`, 7 fixtures)
- S1 = reachable from pc 0, with resolved PUSH1-dest JUMP/JUMPI edges ("only code reachable from pc 0").
- S2 = linear scan from pc 0, stopping before the first STOP ("scan stops at first STOP").
- S3 = fallthrough-only reach (control).
- V1 = JUMPDEST validity over the whole code. V2 = JUMPDEST validity restricted to the scanned/reached code.

| rule | V1 whole-code | V2 scope-restricted |
|---|---|---|
| S1 | 7/7 | 7/7 |
| S2 | 7/7 | 4/7 (r19, r21, r22 return [] vs saved 0xdeadbeef@16; 0xaaaaaaaa@30, 0xbbbbbbbb@32) |
| S3 | 7/7 | 4/7 (same three) |

Separating fixtures, S1 vs S2: V1 none; V2 r19, r21, r22 (only because S2-V2 is wrong there).
Third rival G (pc-0 STOP gate, then one whole-code scan) also gives 7/7. The entry names two rules only.

## Findings
F1 PARTIAL — evm-saved-interface-candidates.md:65-66 (the "Two post-hoc rules" bullet).
- Under V1 both rules fit 7/7. V1 is the convention the entry's own Reproduce uses (line 123: `valid = [i for i, op, _ in ins if op == 0x5b]` over the whole `ins`).
- The bullet never names V1. Under a uniform restriction (V2), rule B fails: r19 and r21 have JUMPDEST 16 after the first STOP at 15; r22 has JUMPDESTs 30 and 32 after the first STOP at 26.
- Observation 1 (lines 20-21) names S016's "valid-destination scan". Re-opened S016 (read-only, accessed 2026-10-21): https://raw.githubusercontent.com/ethereum/execution-specs/v2.20.0/src/ethereum/forks/osaka/vm/runtime.py, `get_valid_jump_destinations`, body `while pc < ulen(code):` with no STOP exit. Docstring, verbatim: "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes." So under the entry's own term, the scan does not stop at STOP.
- Rule B holds only if "stops at the first STOP" governs candidate enumeration (PUSH4→EQ→PUSH1→JUMPI) and not JUMPDEST validity. The bullet does not say so. Not BROKEN, because that reading fits 7/7. Not HOLDS, because the unqualified reading fails 3/7.
- Fix: name V1 in lines 65-66 and scope rule B to candidate enumeration.

F2 HOLDS under V1 — "no fixture separates them" (line 67). Structural reason: every candidate in the seven is either wholly before the first STOP (r19, r21: PUSH4@6 before STOP@15; r22: PUSH4@7 and @17 before STOP@26) or behind a pc-0 STOP (r25, r26: PUSH4@7; both rules return []). r23 has no EQ. r24's only 0x63 (offset 1) is PUSH32 data, with no PUSH4 instruction. A separating shape needs a candidate reached by a resolved jump past a STOP; none of the seven has one. Under V2 the claim fails for r19, r21, r22, but there rule B is also wrong.

F3 HOLDS (supporting) — no truth.json separates the rules. Each file declares offsets, digests or opcodes only. r25 truth.json: `"note": "... No runtime reachability claim."`

F4 scratch-only hypothetical (NOT a lane fixture, NOT admitted): bytes 600456005b63deadbeef14600f57005b. S1 → [(0xdeadbeef, 15)]; S2 → []; S3 → []. The Unknown is real, and the seven cannot test it. This is consistent with the entry's Limitations.

F5 PARTIAL — adjacent, outside the assigned item, for L1. Entry line 40: "each record's subject digest equals the fixture bytes' SHA-256." For r19, the saved subject digest 294e6fd2e041… is the SHA-256 of fixture.hex as text. It equals r19 truth.json `carrier_sha256`. The 18 decoded bytes hash to d1086bce… (`decoded_sha256` in truth.json, and the Provenance `sha256=` at line 146). Reproduce line 137 tests `in (sha(raw), sha(d))`, so Provenance line 147 `subject_eq_bytes=True` does not say which digest matched. That is true for the carrier file and false for the decoded bytes that Observation 2 (lines 25-26) calls "the same 18 decoded bytes." r21 subject = d1086bce (decoded); r22–r26 subjects are decoded-bytes digests (checked by script).

Observation: r25 and r26 are emptied by the same mechanism under both rules (pc-0 STOP). The bullet's two rules are not two independent explanations for r25/r26; the "why" rests on the entry STOP.

Not re-opened: S017 (Yellow Paper). I relied on the lane row SOURCES.md:31 ("the set is a whole-code candidate set, not reachability") and on re-opened S016.

Installs: none. Tools used: Python 3.14.8 (pre-existing), git archive (read-only), `read` for the S016 URL.

VERDICT: Unknown 1 survives under the whole-code JUMPDEST convention (both rules 7/7, zero separating fixtures), but the bullet at lines 65-66 omits that convention, and its literal rule-B reading fails 3/7 → PARTIAL. Adjacent F5 (line 40) is PARTIAL.
