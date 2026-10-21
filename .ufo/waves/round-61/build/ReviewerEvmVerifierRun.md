# ReviewerEvmVerifierRun — round 61 C09 verifier run (read-only)

Seat CloseChousa26.ReviewerEvmVerifierRun-10 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (commit, `git cat-file -t`).
Tree: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive e0a4b0c4348ef1fade46539f520e94fa140c4d8a corpus | tar -x -C /tmp/revenger-r61-ReviewerEvmVerifierRun-base`. Sweep scratch: /tmp/revenger-r61-ReviewerEvmVerifierRun-mut. Lane not written. No REA producer, no bytecode executed (byte indexing only), no subagents. The tmp copy has 0 `__pycache__` dirs.
Versions: Python 3.14.8, git 2.56.0 (pre-existing). Installs: none.
sha256: verify_evm_evidence.py 8265a22f7be8df011cee319a332123a0bfcb011413839a31f602a037c15d0b49; live/runs/round-19/inspection.json e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948 (4175 B).

## 1. Self-test (command and output, verbatim)
$ python3 -B /tmp/revenger-r61-ReviewerEvmVerifierRun-base/corpus/verify_evm_evidence.py --self-test; echo EXIT=$?
POSITIVE ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 1/1 selector candidate and two digests; destination 16 != PUSH4 6; inferred only
NEGATIVE REJECTED candidate destination mismatch
EXIT=0

Coverage, from source:
- verify_evm_evidence.py:10 FIXTURE = fixtures/evm-r19; :11 EVIDENCE = live/runs/round-19/inspection.json; :12 EXPECTED_ID = ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42. One fixture, one record, no loop or argument: evm-r19 ONLY.
- :21 reads fixture.hex; r21–r26 hold fixture.raw + truth.json only. verify() pointed at each of r21..r26 → FileNotFoundError at :21 (fixture.hex), 6/6.
- :60 is a literal string, so the POSITIVE text is not computed; the checks are :23–59.
- Read-only hash check: r19 carrier and decoded sha256 match truth.json; r21–r26 raw sha256 and size match truth.json (6/6).

## 2. Guard reach (29 in-process mutants + baseline)
Method: importlib load of the script from the tmp copy; v.FIXTURE repointed to scratch dirs under /tmp/revenger-r61-ReviewerEvmVerifierRun-mut; v.verify(mutant). Nothing written into the copy.
- Baseline (saved r19) ACCEPTED. Rejected 28/29: identity :26–29, :41–45; selector :30–35; saved-Evidence :37–40; count :47–48; destination :51–56 (the self-test negative at :68 maps to ev:destination_eq_PUSH4(6)); inference limits :57–59.
- Accepted: rs:consistent_selector_swap (selector changed in bytes, truth and Evidence together). No independent selector oracle: self-consistency only.

## 3. C09 statements vs a recheck based on this script
Statements enumerated from claims.md C1 (C09 wording) and fixture/record notes. Guard for r21–r26 = NONE in every row.
S1 PUSH4 immediate in EQ/PUSH1/JUMPI shape = inferred selector candidate. r19: :30–35, :51–52; PUSH4→PUSH3, EQ→LT, PUSH1→PUSH2, JUMPI→JUMP REJECTED. Saved: r21 same; r22 two; r23–r26 none.
S2 destination = PUSH1 operand = JUMPDEST. r19: :54–55; operand→17, JUMPDEST→STOP, dest=PUSH4(6) REJECTED. r22 not guarded: :54 `immediate+9` = 17, but static operand@14 = 30 and byte@30 = 0x5b.
S3 exactly one candidate per fixture. r19: :47–48 only. Rule rejects zero-candidate records (r23–r26 negatives cannot be expressed) and fails saved r22 (two candidates).
S4 inferred / discovery unknown / runtime not-performed. r19: :57–59; four mutants REJECTED. Saved r21–r26 show the same values (observed, unchecked).
S5 carrier + decoded identity (sha256, size, hex encoding). r19: :21–29, :41–45; identity mutants REJECTED. r21–r26 hashes match truth.json but are unchecked; r21 raw == r19 decoded (True).
S6 bare PUSH4, no comparison or jump → no candidate (r23 63c0ffee005000 → saved []). Unguarded.
S7 opcode-like bytes inside PUSH32 data are not code (r24: 63deadbeef14601057 at bytes 1–9 of PUSH32@0 → saved []). Unguarded.
S8 operand naming a non-JUMPDEST gives no destination (r25: operand 16 → STOP@16 → saved []; cause confounded, round-25 LEDGER line 5). Unguarded; nearest r19 analogue rs:JUMPDEST_to_STOP@16 REJECTED, not run on r25 bytes.
S9 valid JUMPDEST operand gives a candidate (r26: operand 17 → JUMPDEST@17 → saved []). Unguarded; unconditional form falsified by saved r26 (F2).
S10 raw/hex carrier parity for identical bytes (r21 = r19 → same 0xdeadbeef@16). Unguarded.
S11 two branches, each selector with its own destination (r22: 0xaaaaaaaa→30, 0xbbbbbbbb→32, match truth). Unguarded; r19 rules cannot express two candidates.
S12 ABI / dispatch / payable / arguments (r19 functions[0]: dispatch "abi", inferred_state_mutability "payable", inferred_arguments ""). Unguarded; never read; selector swap accepted. Not claimable: r25/r26 limitations[2] says "not verified ABI signatures or names. Empty results do not prove the absence of callable dispatch."
Net: a recheck based on this script guards S1–S5 for r19 only, S6–S12 for no fixture, and nothing for r21–r26.

## 4. First falsifiers (saved REA output + static bytes)
F1 "one candidate per dispatch fixture" and "destination = immediate+9": live/runs/round-22/inspection.json has two candidates (0xaaaaaaaa→30, 0xbbbbbbbb→32); immediate+9 = 17 and 27.
F2 "valid JUMPDEST dispatch ⇒ reported candidate": live/runs/round-26/inspection.json (ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090) has operand 17 = JUMPDEST and functions=[] raw and normalized. Cause unknown; round-26 LEDGER line 5: correcting the operand "did not change this saved result".
F3 "PUSH4 or dispatch-looking bytes ⇒ candidate": round-23 (ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201) and round-24 (ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e) both functions=[]. REA holds this; the verifier cannot assert it.

## 5. Consequences for admission (L1 decides; not decided here)
- corpus/README.md:35 (C09 row) lists verify_evm_evidence.py beside evm-r19 and evm-r21…evm-r26; the script covers evm-r19 only. A C09 entry must not name it as the recheck for r21–r26 (Q02 `recheck:`; Q08/Q11 re-derivation).
- Unconditional forms of S2/S3 (F1) and S9 (F2) must not be admitted; scope them to saved REA output.
- S6–S12 are admissible only as labeled observations of saved records, not as verifier-guarded statements.

Disclosure: after this report was written, one `git -C <lane> status --porcelain -- .ufo/waves/round-61/build` ran in the lane (read intent); git may refresh its index stat cache. No content was written in the lane.
VERDICT: self-test passes (EXIT=0; ev_0ad0097eb137…6f42) but covers only fixtures/evm-r19 and round-19 Evidence; a recheck based on it guards no r21–r26 statement, and saved r22 and r26 falsify the one-candidate, immediate+9, and valid-destination forms.
Installs: none (Python 3.14.8 and git 2.56.0 pre-existing).
