# ConnectorKasegiEvm — does a C09 EVM interface entry overlap kasegi's ground? (read-only)

Seat `CloseChousa26.ConnectorKasegiEvm-10` · base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` · 2026-10-21

## Axes named

C1 coverage K (the judged axis), C2 calibration (must not move), Q10 cross-lane scoping, C13 provenance (adjacency must not leak).

## Answer

No method overlap; one real ground overlap, at a single proposition. Both lanes speak about smart-contract artifacts but own different layers: kasegi owns the *claim/package* layer, revenger C09 would own the *byte-offset* layer. Kasegi holds **zero** opcode-level knowledge.

- `grep -rn -iE 'PUSH4|JUMPDEST|opcode|disassembl|selector candidate|function selector|4-byte' --include='*.md' /home/vgpnk/Projects/shokunin/kasegi-shokunin` → **0 lines** (observed). Kasegi's smart-contract hits are three, all claim-layer: `corpus/knowledge/target-checkouts.md:54`, `corpus/knowledge/intake-surface.md:22`, `corpus/knowledge/claim-anatomy-sample.md:44`.
- Kasegi owns deploy-identity and claimability: `kasegi-shokunin/corpus/knowledge/operator-queue.md:58` — "Deployed-code check required: diamond facets must match source-pinned review (repo HEAD `4e80daa`); bytecode drift = re-verify". And `corpus/knowledge/target-checkouts.md:54` — "When auditing a web3/smart-contract claim, check `pin` by hand and re-derive the commit against the upstream remote". Deployed-vs-source identity is a *gate*, not an instrument.
- Kasegi's own boundary: `kasegi-shokunin/PROVINCE.md:25` — "**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather than absorbing it." Its `Owns` is `PROVINCE.md:24` (program rules, scopes, claim packages).
- Revenger's side is byte-scoped and self-limiting: `corpus/fixtures/evm-r19/truth.json` note — "Inert authored bytecode, no ABI signature claim or execution; dispatch-like comparison only". `corpus/verify_evm_evidence.py:60-63` requires `evidence_kind=="inferred"`, `confidence=="inferred"`, `discovery_completeness=="unknown"`, `runtime_execution=="not-performed"`.

**Contested proposition (the only one):** any sentence claiming the contract *has* a function `<selector>` / *exposes* N functions. That is a deployed-artifact claim in kasegi's layer; revenger's record (inferred, completeness unknown, no execution) cannot support it. Kasegi already carries the upper gate too: `corpus/knowledge/ufo-archive-2026.md:78` — gamma-deposit "vuln proven by local-EVM PoC" was still `NOT-SUBMITTABLE` because the deployed asset was "verified FIRST-HAND fixed". Byte-level observation never reaches claimability.

**Second-order effect (the non-obvious part).** Kasegi's Beanstalk gate names no instrument. Revenger's fixture family is that instrument's counter-example, byte-verified:

    r19 pattern@6 63deadbeef14601057        r24 opcode@0 0x7f imm_len 32
    r24 pattern@1 63deadbeef14601057 == r19@6: True
    r24 tail 5000 (POP,STOP)                r19 dest16 0x5b  jumpop14 0x57

The identical 9 bytes `63deadbeef14601057` are dispatch-like in `evm-r19` and inert data inside a PUSH32 immediate in `evm-r24` (`truth.json`: `executable_push4_count: 0`; `corpus/verify_evm_evidence.py:40-46`). A raw-hex grep for selector bytes — the obvious way to implement "bytecode drift = re-verify" — returns a false positive on r24. A second, stronger counter-example for the same gate: **pattern + a valid JUMPDEST destination is still not a candidate** (r26, below). So kasegi's gate cannot be instrumented by either byte pattern or pattern-plus-destination.

## Correction (peer refutation, `ExecEvmOracleR25`, verified here)

My first draft of claim 1 asserted a *sufficient* rule and mis-named `0x57` as `JUMP`; both errors are refuted by saved records. `0x57` is **JUMPI**, and the shape is not sufficient:

    r25 bytes=19 hex=0060003560e01c63deadbeef14601057005b00  [14]=0x10 [15]=0x57 [16]=0x00 [17]=0x5b  saved_functions=[]
    r26 bytes=19 hex=0060003560e01c63deadbeef14601157005b00  [14]=0x11 [15]=0x57 [16]=0x00 [17]=0x5b  saved_functions=[]

`r26` carries the identical 9-byte shape with operand `0x11`=17 landing on a real `JUMPDEST` (`[17]=0x5b`) and the saved record is still empty, normalized and raw (`corpus/live/runs/round-26/inspection.json`). So *pattern-only* fails at r25/r26 and *pattern + valid JUMPDEST* fails at r26 — see `revenger-shokunin/.ufo/waves/round-61/build/ExecEvmOracleR25.md` §5 cross-table, columns B `F/T/T/T` and A `F/F/T/T` (66 lines, sha256 `f7c3cd58…16e24e7d`, final 2026-10-21; supersedes `c540e609…` and `db44b120…`). Its §5 labels the two unrun rows "P1 (not run, §6)" / "P2 (not run, §6)" and §6 heads them "never cite as results" — they must not be cited as fixtures or outcomes. Scratch filenames stay `f1-`/`f3-` by design: the cross-table script and §6's recorded sha256s bind those names.

## Proposed move (one bounded)

Invert the C09 entry so its first falsifiable claim is a **refuted-rule** statement, then report both counter-examples to kasegi instead of absorbing their layer. Drop-in wording:

1. **Claim 1 (refutation, not rule).** "PUSH4 immediate + `0x14` + `0x57` (JUMPI) + a destination byte of `0x5b` is the shape on which this family's only saved candidates occur (r19/r21/r22); it is **not sufficient** — r26 has that exact shape with a valid JUMPDEST destination 17 and an empty saved record. Pattern-only is refuted by r25 and r26; pattern-plus-valid-JUMPDEST is refuted by r26. The acceptance rule is not established." This is the entry's load-bearing claim and it is falsifiable against a saved record. It is also **durable across P1/P2**: any outcome narrows the suppressor but cannot restore a sufficient rule, so the claim needs no revision when those unrun proposals are later executed.
2. **Discriminator (claim 2).** "The same bytes `63deadbeef14601057` are dispatch-like at `evm-r19` offset 6 and inert data at `evm-r24` offset 1 (inside a 32-byte PUSH32 immediate, `executable_push4_count: 0`); an interface claim must name the instruction-stream position, never the raw pattern." Carries its derivation inline (Q11): the four-line `python3 -c` above. Unaffected by the refutation — r24 is a saved empty in every rule column.
3. **Scope sentence.** "…is an interface candidate *shape in a supplied byte string*, read by linear sweep from the declared entry — not a deployed-contract function, ABI signature, reachability result or claimability observation. The 4-byte immediates are authored constants with no signature preimage, so no function name or ABI signature is implied."
4. **Report-not-absorb note.** "Deployed-bytecode identity versus source pins, program scope and claimability are `kasegi-shokunin`'s ground (`corpus/knowledge/operator-queue.md:58`, `target-checkouts.md:54`); this entry supplies only the byte-level candidate shape and reports the r24 (PUSH-immediate) and r26 (valid-JUMPDEST-empty) counter-examples to that lane rather than editing it."
5. **No absorption either direction:** revenger's `corpus/SOURCES.md` must not cite kasegi claim-package facts as tier-A for a byte claim (Q01), and kasegi will not host fixture methodology under its Q6 documentation-only rule (`kasegi-shokunin/corpus/QUALITY.md:26`).

## Risks

- **Q01 depends on L1 merging a source row.** `grep -cE '^\| S[0-9]+ ' corpus/SOURCES.md` → `15`; no EVM/opcode row exists on disk (`grep -in 'evm\|bytecode\|opcode\|yellow' corpus/SOURCES.md` → 0 lines). Two round-61 drafts propose rows: `ScribeSourcesRowsEvm.md:33` (Yellow Paper Shanghai `efc5f9a`, mined, App. H row 0x5b) and `SrcExecSpecsOpcodes.md:62` (execution-specs `v2.20.0` Osaka, queued, `instructions/__init__.py:55,106,109,125`). Also note the Yellow Paper's Appendix H **elides the PUSH4 row** (`ScribeEntryEvm.md` "Peer-reported source constraints"), so PUSH4 = 0x63 needs the execution-specs row; the paper alone leaves Q01 short for that constant. Unmerged rows = entry rejected, K stays 4/14.
- **Overread risk if the scope sentence is placed as a footnote.** Put it first; the phrase "interface candidate" is what a claim assembler would lift.
- **Do not let the cross-lane note become a citation.** Citing kasegi's `operator-queue.md:58` for a byte claim is exactly the Q01 scope failure; the note is a handoff, not support.
- **Two proposed rows sit at different forks.** `ScribeSourcesRowsEvm.md:33` pins the Yellow Paper to **Shanghai** `efc5f9a` and scopes it to "the valid-jump-destination set … only" (anchor §9.4.3 + App. H row `0x5b`); `SrcExecSpecsOpcodes.md:62` pins execution-specs to **Osaka** `v2.20.0`. Only `0x5b` is cross-covered; `0x14/0x57/0x63` rest on the Osaka row alone. The entry must declare that split (and that it uses no post-Shanghai opcode) or a critic reads a fork mix as a Q10 over-generalization. **Correction to my earlier claim:** the byte walk does *not* independently source `PUSH4=0x63` — it presupposes `PUSH_n = 0x5f+n`, the very table row that is unsourced (`ScribeEntryEvm.md:90`). It is a fixture consistency check, not a second source; the paper elides the row.
- **Selector vacuity is the one sentence most likely to be lifted into a kasegi claim.** Saved records carry `dispatch:"abi"`, but no signature name (`corpus/live/runs/round-19/LEDGER.md:7` lists it UNKNOWN) and the fixture constants `deadbeef/aaaaaaaa/bbbbbbbb/c0ffee00` are authored, not Keccak-derived (`ExecSelectorKeccak.md:9`); `keccak(signature)[:4]` is vacuous against these bytes. An entry that leaves "selector" unqualified invites "the contract exposes `deadbeef`" — precisely the deployed-interface proposition kasegi owns.
- **Falsifier-label collision (resolved 2026-10-21).** `ScribeEntryEvm.md:198-201` now reads `S-F1…S-F4` (observed saved-record falsifiers) and `ExecEvmOracleR25.md` §6 now reads `P1/P2` (unrun proposals, "never cite as results"); both relabels verified in place. My report's earlier F-label references are superseded.
- C2 untouched: this move writes only `corpus/knowledge/`, `corpus/README.md`, `corpus/SOURCES.md`, lesson.

## Verification

- `python3 -c "import pathlib;d=bytes.fromhex(pathlib.Path('corpus/fixtures/evm-r19/fixture.hex').read_bytes()[2:-1].decode());r=pathlib.Path('corpus/fixtures/evm-r24/fixture.raw').read_bytes();print(d[6:15].hex(),r[1:10].hex(),r[1:10]==d[6:15],hex(d[16]),r[0])"` → `63deadbeef14601057 63deadbeef14601057 True 0x5b 127` (r19 vs r24).
- `python3 -B -c "import json,pathlib;[print(r,pathlib.Path(f'corpus/fixtures/evm-r{r}/fixture.raw').read_bytes()[14:18].hex(),json.loads(pathlib.Path(f'corpus/live/runs/round-{r}/inspection.json').read_text())['raw_result']['functions']) for r in (25,26)]"` → `25 1057005b []`, `26 1157005b []` (r26 operand 0x11→17 on a real JUMPDEST, still empty).
- `python3 corpus/verify_evm_evidence.py --self-test` → `POSITIVE …` + `NEGATIVE REJECTED …` (unchanged; no fixture edit).
- `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` → `4` now (matches `measure-before.log`); `6` only if both C04 and C09 admit.
- kasegi paths above resolve today: `test -e` each of `PROVINCE.md`, `corpus/knowledge/operator-queue.md`, `corpus/knowledge/target-checkouts.md`, `corpus/knowledge/ufo-archive-2026.md`, `corpus/knowledge/intake-surface.md`, `corpus/knowledge/claim-anatomy-sample.md`.
- `git diff e0a4b0c -- corpus/fixtures corpus/live` → empty (hold set of C2).

VERDICT: Overlap is one proposition, not a method — keep C09 byte-scoped; its first claim must be the refutation pair (r25/r26 kill pattern-only and pattern+valid-JUMPDEST; acceptance rule unestablished), with the r19/r24 same-bytes discriminator second; report both counter-examples to kasegi and never cite kasegi for a byte claim; the PUSH4=0x63 constant needs the execution-specs row because Yellow Paper Appendix H elides it.

Installs: none.
