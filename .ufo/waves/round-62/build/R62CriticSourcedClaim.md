RESULT: COMPLETE

# R62CriticSourcedClaim: source sufficiency for the new C04/C09 statements (critic, advisory)

Frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7`, extracted with `git archive` to
`/fast/scratch/hyaku/revenger-r62/R62CriticSourcedClaim/`. All reads were on that copy. No
fixture JS or bytecode was run, and no provider was called. The candidate drafts were absent
(`ls corpus/knowledge/round-62-*` returned ENOENT). So this review attacks the planned
statements (build-spec.json prompts for R62JsEntry and R62EvmEntry) against the saved bytes.
Exclusions with allowed rewordings: scratch `exclusions.md`. Probe `probe.py` (sha256
6c561288c9b554e72b289c9f6815c962138a58328f2f201bdc8b4504e06fb230) exited 0; `probe.stdout`
sha256 is 8089d862e0b60ecc4faf4c7d3ba10f1ff1fa153ca7dba8e6da77a78778dfdeab.

## Axis and rule
Axis: coverage (C1), constrained by Q01/Q04/Q07/Q09/Q10/Q11. S030/S031 are tier A only for
the content of the saved bytes. S028 covers only byte boundaries and S029 only language
semantics. None covers what a provider means, does or gets right. Unless an official
provider doc is opened and logged, each such statement must be omitted or labeled
recorded/Unknown. This is a disclosed exclusion, not a silent narrowing.

## Counterexamples (strongest first)
1. **The C04 1-based call span does not equal the saved location.** Probe:
   `js-r3 … 0based_start=28 end_exclusive=50 1based_start=29 end_inclusive=50` against
   saved start column 28, end column 50. js-r7-v2 gives 18/40 against 1-based 19/40.
   Reading the saved start as 1-based would begin at `' '`. "Matches" is false under 1-based
   columns; under any other convention it rests on an unopened REA convention.
   Impacted: Q01/Q04/Q11. Fix J1: print both conventions, state only the integer relation,
   leave the convention Unknown.
2. **No per-name spans exist.** Both named r3 edges have location `1:6–1:50`, which covers
   `"{ rot13, checksum } = require('./transform')"`. Impacted: Q10/Q11. Fix J2.
3. **The fixtures cannot tell `imported_name` from `local_name`.** They are equal on every
   edge because the source uses only shorthand bindings. No opened row defines the
   provider fields. Fix J3.
4. **The producer version is not in the record bytes.** `grep -c rea-agents` returned 0 on
   round-19 and round-24 `inspection.json` and both JS analysis records. The string occurs
   only in `round-24/LEDGER.md:5`, `20261012T164357Z/LEDGER.md:5` and `round-7/LEDGER.md:6`.
   JS provider.version is `"1"`. S026/S027 scope wording over-attributes, so S030/S031 must
   label the version as LEDGER-recorded. Impacted: Q09/Q11. Fix J9/E9.
5. **What C09 `bytecode_offset` means is provider-only.** In each of the 3 saved pairs the
   byte at the offset is `0x5b` and equals the PUSH1 immediate after PUSH4·EQ: r19/r21
   offset 16 (`14601057`), r22 offsets 30 (`14601e57`) and 32 (`14602057`). That equality
   is admissible. "Function entry/dispatch target" is unopened evmole semantics. Fix E1.
6. **"Dispatch" and "invalid jump" are execution semantics.** S028 opens only the opcode
   enum (`instructions/__init__.py`) and `runtime.py`. In r25 the byte at the PUSH1
   immediate 16 is `0x00` (hex `0060003560e01c63deadbeef14601057005b00`). "Reverts" or
   "compares calldata" needs control_flow/comparison sources. Fix E3: log the byte-pattern
   use of the frozen word "dispatch" as an explicit narrowing, or have L1 open those files
   and widen S028 with quotes.
7. **Empty outputs for r23–r26 have no admissible cause.** Raw and normalized `functions`
   are `[]`. Any "because STOP prefix / PUSH32 immediate" text is a Q07 provider cause.
   Quote only the record's own content: "Empty results do not prove the absence of callable
   dispatch." Fix E4.
8. **r19 digest scopes.** Carrier is 39 bytes (`b'0x60…5b00\n'`) and decoded is 18 bytes.
   carrier_sha equals subject and decoded_sha equals bytecode.sha256 (True/True). These
   equalities are admissible. "The provider decoded/hashed" is not, and the decode rule is
   the entry's own. Fix E6.

Further exclusions are listed with reasons in exclusions.md: J4–J8 and J10 for C04,
E2, E5, E7 and E8 for C09.

## Duplicate authority
S030 covers the same bytes as S027 and S031 the same as S026; S028/S016 and S029/S022
overlap the same way. Each new row must name its relation, either as a successor for the
round-62 opening or as a disjoint added scope. Otherwise census mined counts double one
authority. The `used-by` cells of S016–S027 point at rejected entries and are not support.

## Still admissible (the frozen scope is not shrunk)
- Equalities between saved strings and integers and the authored bytes.
- Instruction boundaries and valid-JUMPDEST sets under S028.
- Destructuring reads named properties of the call value, and §16.2.2 is a distinct
  production (S029). Both C04 and C09 remain viable under these exclusions; nothing here
  admits either.

## Unknowns
The candidate texts are unwritten, so whether they contain these statements is unverified.
REA/evmole conventions are unknown by design. I fetched no provider docs; opening them is an
L1 source-scope decision. README and C04/C09 statuses are untouched, no held flip is
proposed, and the rejected entries and round-61 reports were not edited.

Installs: none.
