RESULT: COMPLETE

# R62ConnectEvmPrior — kaidoku EVM recorded observations and cross-lane wording for the C09 candidate

Lane: read-only cross-lane connector. No kaidoku/revenger corpus file, index or history touched; no fixture JS, no bytecode execution, no REA producer, no chain/RPC. Artifact: `/fast/scratch/hyaku/revenger-r62/R62ConnectEvmPrior/cross-lane-wording-C09.md` rev.4, sha256 `8719a3ef5787dd893a9ded09736158448e8c756669a8fca297953fec67297ed5` (accepted by the cross-lane critic; cutover is L1's).

## 1. Kaidoku's recorded EVM observations (read-only)

Pinned at `kaidoku-shokunin` @ `69e82c48be5614ce96f7c1c32445fe61c4870630`; the five EVM entries below are byte-identical between that commit and the worktree, so path:line is stable. Last-touch commits: r3 interface `999ce123f87020869e592fa409e24310d22fabf2`; arc3-r1/r3/r4 `58c3db7bc3992eead810983f94a104fea6343f6a`; arc3-r6 `2fba56fe7d54cfb94ca9332c11cea81667b3b289`; arc3-r8 `53fcf0caca7255f730fe1a1f17aefd00203a2978`.

| kaidoku-shokunin path | line | recorded content |
|---|---|---|
| `corpus/knowledge/2026-10-13-r3-evm-interface.md` | 151-155 | r4 erratum: `bytecodeOffset` records the JUMPDEST dispatch-target position, not the PUSH4 site; carrier 3 offsets 62/68/74 sit at jump destinations |
| `corpus/knowledge/2026-10-19-arc3-r1-evm-real-solc.md` | 17, 23 | real solc-0.8.37: offsets 89/137/167/215/263 and all KdxToken offsets land on byte `0x5b` |
| `corpus/knowledge/2026-10-19-arc3-r3-evm-optimizer-shapes.md` | 31 | hand-assembled 84-byte carrier: offsets 38/48/58 are the declared `PUSH1` jump immediates; `0x5b` bytes at 40/50/60, two bytes later; "the reading is scoped to solc-convention carriers" |
| `corpus/knowledge/2026-10-19-arc3-r4-evm-vyper-leg.md` | 22 | 0 of 15 offsets land on a JUMPDEST (each `push4_pc + 11`); "on the solc carriers the offsets **are** JUMPDESTs"; corpus text asserting "offsets land on JUMPDESTs" "carries a solc-convention scope" |
| `corpus/knowledge/2026-10-19-arc3-r6-viair-dispatch-shape.md` | 24 | 14/15 land on a JUMPDEST; the 15th is `push4_pc + 10`, neither JUMPDEST nor PUSH2 target |
| `corpus/knowledge/2026-10-19-arc3-r8-vyper-optimizer-dispatch-shapes.md` | 14 | all eight reported offsets equal the shared value 65 (`0x41` DUP1), not the handler targets |

The round-61 rejected revenger entry carried one of these lines only (frozen tree line 101 cites `2026-10-13-r3-evm-interface.md:151-153`); the others were not carried over.

## 2. My byte re-derivation (read-only, nothing executed)

Script `…/kaidoku_offset_conventions.py`, output `…/kaidoku_offset_conventions.out` (scratch `/fast/scratch/hyaku/revenger-r62/R62ConnectEvmPrior/`).

```
$ python3 -B kaidoku_offset_conventions.py
carrier-A (…/arc3-loop1-round1/claims/c1/CR-1/evidence/carrier-A.hex)
  hex file: 168 B sha256=36dc82468c5846a93273970483253e63f5b0bef673f0bd355d3c41db01b9b3d2
  decoded:  84 B sha256=a92ba15225aaddccff5c0c67fff18c6c13b86be3bc91c07527681fbf500f6f7b
  push4_sites=[(7,'a9059cbb'),(17,'70a08231'),(27,'095ea7b3'),(70,'deadbeef'),(77,'ffffffff')]
  jumpi=(at,target,target_is_jumpdest)=[(15,38,False),(25,48,False),(35,58,False)]  jumpdest_pcs=[40,50,60]
  claimed_offset 38: byte=0x80 is_jumpdest=False is_push1_jumpi_target=True is_push2_target=False
  claimed_offset 48: byte=0x00 is_jumpdest=False is_push1_jumpi_target=True is_push2_target=False
  claimed_offset 58: byte=0x00 is_jumpdest=False is_push1_jumpi_target=True is_push2_target=False
Rv2Token.runtime (…/arc3-loop1-round1/claims/c1/RV-2/Rv2Token.runtime.hex)
  hex file: 3886 B sha256=d7f73058e2d9fb2563bf96b2f26902f233530de027a7943185e15bfdc4e1048f
  decoded:  1943 B sha256=c1081a565869b50387211b25afaf3768294aa774c35845bc3a8c0b12cfe15e74
  claimed_offset 89/137/167/215/263: byte=0x5b is_jumpdest=True is_push1_jumpi_target=False is_push2_target=True
```

Digest domains are separate (Q09): the 84 B / `a92ba152…` and 1,943 B / `c1081a56…` values are the **decoded** bytecodes; the 168 B / `36dc8246…` and 3,886 B / `d7f73058…` values are the hex container files. Both carriers are tracked in kaidoku and present at `69e82c48`, so a citation pins them with `git -C kaidoku-shokunin show 69e82c48:<path>` rather than a worktree path.

Reading (my walk only): the same authored dispatch shape (`PUSH4 sel; EQ; PUSH1/PUSH2 dst; JUMPI`) has a reported offset landing on a JUMPDEST on the compiled carrier (Rv2Token 5/5) and one not landing on a JUMPDEST on the hand-assembled carrier (carrier-A 3/3: offsets are the declared `PUSH1` immediates, `0x5b` two bytes later). Kaidoku's corresponding statements are its own recorded lines (listed in §1, labelled recorded); this lane adds no claim about what the provider's field means (see D2).

## 3. Proposed artifact (cross-lane wording)

rev.4 holds one merged `## Cross-lane contest (Q10)` block (the cross-lane critic's block plus one non-transfer sentence), a non-block appendix of further recorded kaidoku observations, and nine rules: (1) never write "the offset is the JUMPDEST" unqualified — state the convention observed on the entry's own fixtures, with its own in-entry derivation; (2) label kaidoku numbers as recorded, not re-derived (Q11); (3) keep a no-new-claim scope clause (no claim about kaidoku's carriers/compilers/providers/probes; no provider-method, chain/RPC or present-capability claim); (4) do not cite the round-61 rejected revenger entry as support; (5) `kaidoku-shokunin/PROVINCE.md:54` is kaidoku's EVM surface row (positional encoding, held selector recovery), not offset semantics — line 54 identical at HEAD and worktree (worktree edit is at the file tail, ~292); (6) no ownership or recipient verb for any lane; (7) both sibling-name checks in the self-avoiding form only; (8) every count inside the block printed by the entry or labelled recorded; (9) sibling files pinned by commit, with container and decoded digest domains stated separately. Rev.1's "two paste-ready variants (full prior-art paragraph; one-sentence minimum)" is superseded by rev.4 — see §6.

## 4. Frozen-C1 fit and non-claims

- Frozen revenger tree extracted read-only to `…/frozen` from `a3498e25ad87bf756288812d0ea7c474b09433c7`: `corpus/README.md` shows **C04 and C09 uncovered**, 4 `| held |` rows, denominator 14 unchanged. No README row touched; nothing here marks README held.
- No new gate, no promotion, no producer/authenticity/Electron-role claim. This lane supplies cross-lane wording plus its own byte re-derivation of kaidoku's retained carriers only; it does not restate the rejected entry's claims and supplies none of the C09 candidate's own counts/offsets/digests — those must be derived inside the new entry with command and output under unchanged Q11.

## 5. Unknowns (honest)

- kaidoku's r3 carrier-3 bytes (`/tmp/evm-carrier-3.*`, deleted by that lane) are not retained in the kaidoku repo, so "offsets 62/68/74 sit at jump destinations" is recorded-only here; the carrier-A and Rv2Token halves were re-derived from retained bytes. kaidoku's arc3-r4 / arc3-r6 / arc3-r8 carriers were not re-walked (recorded only); their carrier bytes were not found on this host's retained paths. kaidoku's `PROVINCE.md` and `corpus/SOURCES.md` are modified in that worktree (unrelated round-24 tail edits); only `PROVINCE.md:54` was used, unchanged.

## 6. Post-review corrections (artifact rev.1 → rev.4)

Artifact hashes retained: rev.1 `797af37f…`, rev.2 `2dc09256…`, rev.3 (superseded), rev.4 `8719a3ef5787dd893a9ded09736158448e8c756669a8fca297953fec67297ed5`.
- **D1** (`R62CriticCrossLane`) viaIR overstated → **corrected**: dropped from entry-facing wording; appendix states "holds on 14 of 15 viaIR legs (recorded)".
- **D2** (critic) "not a definition of the field" was a provider-method inference → **corrected**: clause removed; the entry states only the convention it observes on its own fixtures.
- **D3** (critic) heading/prior-art framing → **corrected**: block is `## Cross-lane contest (Q10)`; no priority/ownership wording.
- **D4** (critic) too many quoted sibling numbers → **corrected (narrow scope)**: one optional kaidoku bullet in the block; wider list demoted to an appendix, values labelled recorded.
- **M1** (`R62ConnectKasegi` rev.5) one merged block with all three content kinds → **corrected**: map row + non-transfer sentence, ADJ-06 quotations, optional kaidoku bullet.
- **M2** (kasegi rev.5) two checks credited narrowly → **corrected**: rule 7 (no sibling source row, sibling names confined to the block).
- **D5** (kasegi rev.6) plain-form SOURCES check self-matches if copied into the cell → **corrected**: self-avoiding form only; probe on the frozen tree: plain literal → plain `1` / avoiding `1`; self-avoiding literal → `0`/`0` (`…/probe/{plain_cell.txt,avoid_cell.txt}`); SOURCES count `0`.
- **D6** (kasegi rev.6) "the seven authored fixtures" is a count → **corrected**: rule 8.
- **D7** (critic) digest scope mixed container and decoded bytes; worktree path → **corrected**: both domains stated, path pinned by commit (both carriers tracked and present at `69e82c48`).
- **D8** (critic) "which stays uncovered until L1 admits it" was a README-status statement → **corrected**: clause dropped; the sentence now reads "That status is kaidoku's own map status; it is not evidence for this entry and does not apply to revenger's C09 row."
- **D9** (critic) Q10 cell pointing at a drifting line range → **corrected**: points at the heading; L1 may substitute the final range at cutover.
- **D10** (critic) rule 7 carried the plain pattern literal → **corrected**: self-avoiding form only.
- **M3** (critic, minor) appendix paraphrase → **corrected**: `arc3-r4-evm-vyper-leg.md:22` quoted verbatim, `arc3-r3-evm-optimizer-shapes.md:31` cited for "scoped to solc-convention carriers".
- **D11** (critic, report side) §1/§3 still described superseded rev.1 → **corrected in place**: title and §1 heading reworded; §3 describes rev.4; §2's closing paragraph now cites kaidoku's pinned lines.
- **D12** (critic) lane chat phrasing "no universal JUMPDEST meaning" is a field inference (my own D2) → **corrected**: kept out of this report, the artifact and peer messages; the safe form states only what kaidoku records, labelled recorded, at the pinned lines.

Unresolved (L1's call, not mine): which artifact the entry writer cuts over from — the critic's `proposed-q10-blocks.md` block or my rev.4 block with the one added non-transfer sentence — and whether the entry embeds the critic's pointer readout script or labels each sibling value "recorded, not re-derived". The critic reports rev.4 accepted with no open defects; that is a wording verdict, not an admission. My lane supplies wording and the kaidoku recorded-observation grounding only — no revenger-side fact, no admission, no README change.

Installs: none. No tool installed or updated by this lane.
