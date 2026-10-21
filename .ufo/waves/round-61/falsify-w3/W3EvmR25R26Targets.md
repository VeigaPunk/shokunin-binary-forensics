GRADE: PARTIAL — C09 Observation 3, r25/r26 hypothesis (core facts HOLD; wording and sourcing defects F1–F6)
Seat W3EvmR25R26Targets · base ab580698212258a55e43e9bb9bf6ac78c91eae2a (git archive → /tmp/revenger-r61w3-W3EvmR25R26Targets/base) · checks 2026-10-21 · no REA call, no EVM execution, no chain access · scratch only under /tmp.

HOLDS (re-derived)
H1 Byte diff: `cmp -l` evm-r25 vs evm-r26 = one byte, offset 14, 0x10→0x11 (sha256 2d87a4e2…f8f7 / ebe2d675…8e97). truth.json changed_offset 14, 10→11 agrees. `git diff cf02419..ab580698` over evm-r25/r26 and live/runs/round-25/26: empty.
H2 Decode (own decoder and pyevmasm 0.2.3 agree). r25: 0:STOP 1:PUSH1 3:CALLDATALOAD 4:PUSH1 e0 6:SHR 7:PUSH4 deadbeef 12:EQ 13:PUSH1 10 15:JUMPI 16:STOP 17:JUMPDEST 18:STOP. r26: identical except 13:PUSH1 11. Target 16 = 0x00 (not a JUMPDEST); target 17 = 0x5b, a valid destination in both.
H3 Records: r25/r26 inspection.json have functions [], evidence_kind inferred, discovery_completeness unknown, runtime_execution not-performed, subject.digest = fixture sha256, bytecode.hex = fixture bytes; evidence_id values equal the entry's; file sha256 prefixes 4f677a20…, bf2b2337… equal Provenance.
H4 Reproduce block extracted, `python3 -B` from base: exit 0; stdout vs Provenance block IDENTICAL (14 lines).
H5 Pinned provider, two bindings (evmole==0.9.3 Python; evmole@0.9.3 npm): r19 deadbeef@16, r21 same, r22 aaaaaaaa@30 + bbbbbbbb@32, r23–r26 []. Both match the saved records exactly.
H6 Sources: S016 runtime.py (v2.20.0, 69 lines; https://raw.githubusercontent.com/ethereum/execution-specs/v2.20.0/src/ethereum/forks/osaka/vm/runtime.py): lines 22–69 are a linear whole-code scan; lines 29–30 quote verbatim ("The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes."). instructions/__init__.py lines 55, 106, 109, 125 = EQ 0x14, JUMPI 0x57, JUMPDEST 0x5B, PUSH4 0x63, exact. S017 (https://ethereum.github.io/yellowpaper/paper.pdf, efc5f9a, 2025-02-04; sha256 d67c009c… matches row): p.15 "rather than sitting in the data portion of PUSH operations" (pdftotext splits "boundaries").
H7 LOG.md:300 (r25 = STOP prepended to r19) and :312 (r26 one-byte delta) agree with the bytes; r19 == r25[1:] byte-identical.

DEFECTS
F1 PARTIAL, line 35: "a PUSH4/EQ/JUMPI whose target 16" omits the PUSH1 at 13 that pushes the target (line 53 includes it). Line 53's arrow chain reads as flow, but 17 is reached only by the jump.
F2 PARTIAL, lines 20–21 and the r25/r26 text: STOP (0x00) and PUSH1 (0x60) carry "entry STOP" and "target 16 is a STOP", but are uncited. S016 is cited only at 55/106/109/125; STOP is at :104 and PUSH1 at :122 (verified). The S016 row's "teaches" omits both. Values correct; Q01/Q11 citation gap.
F3 PARTIAL, BROKEN on its literal reading, lines 65–66 (Unknown): "the scan stops at the first STOP". Line 21 defines "its valid-destination scan". Read that way it predicts [] for r19 (JUMPDEST 16 lies after the first STOP at 15), but the record reports deadbeef@16; it also misses r21, r22 and P1. The rule that fits all eight is "the dispatch JUMPI precedes the first STOP" (build ExecEvmOracleR25.md:33, "L"). Under the harm rule (an entry that overstates its evidence voids admission) the literal reading is disqualifying until L is named.
F4 PARTIAL, lines 65–66: "only code reachable from pc 0 is considered" (rule C, static PUSH+JUMP targets followed) is refuted by P2 (below) under both bindings: it predicts deadbeef@17, the provider returns []. "Neither is validated; no fixture separates them" stays true, since P2 is not a lane fixture, but the probe belongs in the entry.
F5 PARTIAL, lines 53–55 and lesson round-61.md:79: the "registered C09 wording" is not traceable. claims.md has no "statically valid" or "every…pattern" prediction (grep). Four wordings circulate: entry :55 "The provider reports every statically valid selector/JUMPDEST pattern"; lesson :79 "REA reports every statically valid PUSH4→JUMPDEST pattern" (labelled registered); build ExecEvmOracleR26.md:47 F1 "REA reports every valid static PUSH4→JUMPDEST candidate"; falsify spec "every statically valid pattern is reported". The falsification holds (rule W below); the Q07 registration trace does not.
F6 nit, line 2: verified-at still names e0a4b0c; commit 0597e53 changed the body (lines 85–93) without refreshing line 2. The Reproduce block still reproduces identically; header only.

RULE FIT (my implementation; 7 saved records + scratch P1, P2)
rule | r19 r21 r22 | r23–r26 | P1 | P2
W whole-code valid JUMPDEST | fit | misses r26 only | fit | MISS (predicts @17)
A literal valid-destination scan stops at STOP | MISS | fit | MISS | fit
L dispatch JUMPI before first STOP | fit | fit | fit | fit
C reachable from pc 0, static jumps followed | fit | fit | fit | MISS (predicts @17)
Only L fits all eight.

SCRATCH PROBES (not lane evidence; not admissible without a declared round)
P1 = build proposal, sha256 121ddb5e…457c2 (verified): r26 with byte 0 STOP→JUMPDEST → deadbeef@17 (Python and npm). The pc-0 STOP is the operative difference for this provider.
P2 = build proposal, sha256 e7e09812…2424e (verified), `6006560000005b63deadbeef14601157005b00` → [] (Python and npm). For the pinned provider this separates L from C.

INSTALLS (tool · version · channel · reason)
- uv 0.13.0: already present, not installed by this seat. `uv venv` in scratch resolved CPython 3.15.0 (uv-managed; prior presence unverified).
- evmole 0.9.3 and pyevmasm 0.2.3: `uv pip install` into scratch venv (PyPI); provider reproduction and independent disassembly.
- evmole@0.9.3: `npm install` into a scratch dir (npm registry); the JS binding named in the record limitations.
- No pacman, system package, or service change.

VERDICT: r25/r26 facts HOLD on bytes, decode, records and both provider bindings; F3 is BROKEN on its literal reading, and F1, F2, F4–F6 need wording or citation fixes before the entry's Unknown can be called accurate.
