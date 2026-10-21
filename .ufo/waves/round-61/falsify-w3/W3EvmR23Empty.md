GRADE: HOLDS — C09 Observation 3, r23 (bare PUSH4 c0ffee00 negative: functions [], no JUMPI/JUMPDEST); adjacent PARTIAL at Observation 5, lines 43-45
Target: landed ab580698212258a55e43e9bb9bf6ac78c91eae2a (rev-parse confirmed), extracted to /tmp/revenger-r61w3-W3EvmR23Empty. r23 also checked at claim base cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 and verified-at base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (git archive into scratch). Entry: corpus/knowledge/evm-saved-interface-candidates.md; Observation 3 = lines 32-37.

1. Bytes, decoded by me with my own opcode names (PUSHn consumes n immediate bytes) — HOLDS
- corpus/fixtures/evm-r23/fixture.raw = `63 c0 ff ee 00 50 00` (7 B); sha256 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a = truth.json raw_sha256.
- Walk: 0 PUSH4 c0ffee00 · 5 POP · 6 STOP. Raw-byte scan of all 7 bytes: 0x57 absent, 0x5b absent, 0x14 absent.
- So "no JUMPI, no JUMPDEST" holds without the PUSH-data exclusion rule: no 0x5b byte exists at all. truth.json (push4_opcode_offset 0, push4_immediate c0ffee00, opcodes [PUSH4,POP,STOP], comparison_or_jump false) agrees.

2. Opcode values from sources outside the lane, re-opened 2026-10-21 — HOLDS
- execution-specs tag v2.20.0, src/ethereum/forks/osaka/vm/instructions/__init__.py (fetched, 367 lines, sha256 49dd6155c7560811…5b63724): EQ=0x14 L55, STOP=0x00 L104, JUMPI=0x57 L106, JUMPDEST=0x5B L109, POP=0x50 L118, PUSH4=0x63 L125. S016's cited lines 55/106/109/125 match exactly.
- Yellow Paper, SHANGHAI VERSION efc5f9a – 2025-02-04 (https://ethereum.github.io/yellowpaper/paper.pdf; 597589 B; sha256 d67c009c…8477fa9 = S017's pinned digest). pdftotext -layout Appendix H rows: "0x00 STOP", "0x50 POP", "0x57 JUMPI", "0x5b JUMPDEST", "0x61 PUSH2 … 2-byte", "0x7f PUSH32 … 32-byte". The PUSH4 row is elided; its 4-byte immediate follows from that family pattern [INFERENCE].
- §9.4.3 text, PDF p.15 (extracted lines 1233-1234), quoted: "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations" (19 words; accessed 2026-10-21).

3. Saved record corpus/live/runs/round-23/inspection.json (3923 B; sha256 ce9fe51536af461e…aac2af) — HOLDS on every field Observation 3 reads
- evidence_id ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201 = the entry's r23 ID (full 64 hex).
- subject.digest, artifact.sha256, bytecode.sha256 = fixture sha; artifact and bytecode bytes 7; bytecode.hex 63c0ffee005000 = fixture bytes.
- raw_result = {"functions": []} (its only key; no hidden candidate); normalized_result.functions = [].
- evidence_kind inferred; discovery_completeness unknown; runtime_execution not-performed; provider evmole-interface / evmole@0.9.3.
- inspection.stderr 0 B (sha e3b0c44298fc1c14…52b855); diagnostics.stderr "".

4. Entry's Reproduce block, run as written (extracted from the archived entry; python3 -B; cwd = extracted root; exit 0) — HOLDS
- stdout is 14 lines, byte-exact match to the ```text Provenance block. The r23 lines reproduce:
  r23 bytes=7 sha256=8047ddff11234c2d push4=[(0, 'c0ffee00')] raw_0x63=[0] jumpi(at,dest,valid)=[] jumpdest=[] entry_op=0x63
     saved ev_296e7ed723c7356b file_sha256=ce9fe51536af461e functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True

5. Harm test (changed saved record or fixture) — none found
- fixture.raw, truth.json, inspection.json, inspection.stderr, LEDGER.md and reviewer.md are byte-identical (diff -r) at cf02419, e0a4b0c, ab580698 and in the live lane tree. Read-only: sha256sum and diff only; no git status, index or jj write.

6. Observation 3 wording, lines 32-37: "r23 (`PUSH4 c0ffee00`, POP, STOP; no JUMPI, no JUMPDEST) … all report `functions: []`" — accurate for r23. It asserts no cause for r23. No overstatement in this clause.

PARTIAL (adjacent; Observation 5, not the target) — entry lines 43-45: "…so `deadbeef`, `aaaaaaaa`, `bbbbbbbb` and `c0ffee00` are test constants, not derived selectors."
- The conclusion is supported by the authoring record, which lines 41-45 do not cite: LOG.md:273 (r23 CLAIM: "author inert raw bytecode with `PUSH4 c0ffee00; POP; STOP`"); truth.json r23 note "Inert negative fixture; no dispatch syntax, execution or ABI claim."
- The cited route does not carry it. "No fixture declares a signature" (lines 41-42) does not establish non-derivation. The cited seat report calls its keccak(signature)[:4] test "VACUOUS" against these bytes (ExecSelectorKeccak.md:9). Lines 43-45 restate the S018 row's conditional (SOURCES.md:32) and leave its antecedent "authored constant" uncited.
- Fix: cite LOG.md:272-273 and the truth.json note for authorship. Not BROKEN: nothing contradicts the sentence.

Side note (not a finding against the entry)
- ExecEvmOracleR23.md:44 opcode line numbers (STOP L103, JUMPI L105, JUMPDEST L108, PUSH4 L124) come from execution-specs HEAD 921c0796, Cancun file, sha 6803bc7d… (ExecEvmOracleR22.md:29). They are not the S016 tag. The entry cites the v2.20.0 lines, which check out. The opcode values are the same.

Not run: no REA producer call; no bytecode execution; no keccak preimage test; evidence_id not recomputed (the entry says recorded only).
Installs: none. Used pre-present curl, /usr/bin/pdftotext (poppler), python3.
Scratch: /tmp/revenger-r61w3-W3EvmR23Empty (reproduce_c09_r61w3.py, spec/, base-cf02419/, base-e0a4b0c/).

VERDICT: Observation 3's r23 clause HOLDS (bytes, saved record, Reproduce output, cross-commit identity, external opcode values). One PARTIAL derivation gap sits at Observation 5, lines 43-45 (c0ffee00 "not derived").
