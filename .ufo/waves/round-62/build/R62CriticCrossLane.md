RESULT: COMPLETE

# R62CriticCrossLane: attack on the generic cross-lane (Q10) note for C1 (C04/C09)

Seat `RevengerR61-2.R62CriticCrossLane`, critic. This is a proposal only, not an admission. Frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7`,
extracted with `git archive` to `/fast/scratch/hyaku/revenger-r62/R62CriticCrossLane/tree`. No round-62 candidate file existed
(`ls revenger-shokunin/corpus/knowledge/round-62-*` → No such file), so I attacked the note pattern that the rejected round-61 entries carry and that a new entry would inherit.
Axes: coverage K (judged), Q10 adjacency integrity, Q11 completeness, preservation. README stays uncovered; I mark nothing held.

## Counterexamples (strongest first)

1. **Fabricated ownership from a refusal line.** Old C09 `evm-saved-interface-candidates.md:104-105` says "Kasegi owns deployed-code identity and claimability (`kasegi-shokunin/PROVINCE.md:25`)".
   At kasegi `8bf98072`, `:25` reads "**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather than absorbing it."
   `git show $KH:PROVINCE.md | grep -ciE 'identit|deployed|claimab'` → `0`. The round-61 connector already wrote ownership language from gate lines:
   `ConnectorKasegiEvm.md:44` says "…claimability are `kasegi-shokunin`'s ground (`operator-queue.md:58`, `target-checkouts.md:54`)". But `operator-queue.md:58` is a per-program row ("Deployed-code check required: … bytecode drift = re-verify").
   Kasegi carries no contested byte-level scope: `git -C kasegi-shokunin grep -i -E 'PUSH4|JUMPDEST|opcode|disassembl|function selector' 8bf98072 -- '*.md' | wc -l` → `0`.
   Corroborated by sibling reports `falsify-w3/W3ProvinceBounds.md:11-15` and `W3EvmCrossLaneCites.md:10`.
2. **A named ADJ-06 recipient the cited source does not name.** Old C09 `:106`, old C04 `:91-92`, `lessons/round-61.md:31` ("still operator-owned") and `round-61-verifier-spotcheck.md:218` ("operator-owned ADJ-06 arbitration") all name the operator.
   The ADJ-06 row itself (tsukuroi `7f423140`, `adjacency-handoffs-fleet-r1.md:54`) has recipient column "protocol integrator for ownership ruling" and text "No owner selected".
   tsukuroi `PROVINCE.md:152`: "ADJ-06's unresolved recipient and Frontier arbitration remain controlling"; `:150`: "Kaidoku/Revenger arbitration remains unresolved; ask the protocol integrator".
   Fleet `.ufo/l0-questions.md:42` (`c2e2913d`) is tsukuroi's question asking L0 to arbitrate, not a ruling. Naming any recipient is a new arbitration the sources withhold.
3. **Universalized sibling reading presented as "prior art".** Old C09 `:56-57` says "Kaidoku holds the same reading for its own records" and `:102` says "cited here as prior art".
   kaidoku `69e82c48` `arc3-r3-evm-optimizer-shapes.md:31` says the reported offsets on r1's hand-assembled control are "declared `PUSH1` jump immediates, not JUMPDESTs … the reading does **not** hold".
   `arc3-r4-evm-vyper-leg.md:22` says "the r1/r3 reading does NOT generalize" (0 of 15). Revenger's fixtures are authored, which is the class where kaidoku recorded the failure.
   Citing a sibling as "prior art" imports its proposition and also drops that sibling's own scope limit.
4. **The Q-table summary cell acts as an unpointered attribution.** Old C09 `:192` and old C04 `:205` say "kaidoku [and kasegi] ground reported". Per `W3EvmCrossLaneCites.md:15`, only one of the three C09 cites was exact.
   A pass cell that summarizes sibling ground is itself a factual claim with no pointer.
5. **Silent absorption by omission.** Old C04 never reported kaidoku `r4-09-js-export-compare.md:59,65` (authored CommonJS fixtures, `default`-only binding) per `W3JsCrossLaneCites.md:20-23`.
   Old C09's Unknown that `evidence_id` cannot be recomputed is contradicted 7/7 in `W3ProvinceBounds.md:17-22`. A round-62 C09 SHOULD only say "recorded, not authenticated" and assert no non-recomputability.
6. **Unpinned line numbers.** `git -C kaidoku-shokunin diff --stat -- PROVINCE.md` → `1 file changed, 4 insertions(+), 2 deletions(-)` while I read it. Lines 54 and 240 have not shifted yet, but a worktree pointer is not stable.
   `W3JsCrossLaneCites.md:27` already noted that no kaidoku commit was pinned. Under Q11, a sibling commit id and line number in an entry are identifiers and offsets, so each needs an in-entry command and output, or a "recorded" label.

## Impacted axes

- Q10: counterexamples 1-5 are fixable defects, not tradeoffs.
- Q11: counterexample 6.
- Q01: no sibling line may be a source. Frozen `corpus/SOURCES.md` has `grep -c -i -E 'kaidoku|kasegi|tsukuroi'` → `0`, which MUST stay `0`.
- Coverage K: if a new Q10 block or Q-table cell repeats 1-4, that entry fails Q10, so its C04/C09 row cannot count.
- Preservation: the old text above is byte-retained evidence. It is superseded in the round-62 lesson and not edited.

## Smallest safe correction (proposed artifact, scratch only)

`/fast/scratch/hyaku/revenger-r62/R62CriticCrossLane/proposed-q10-blocks.md` (sha256 `36989107…a6a4c`) gives drop-in C04/C09 blocks. They follow five rules:
- Quote sibling lines at a commit pin, and use them for contested scope only.
- Use no ownership or recipient verb for any lane, including revenger's own `PROVINCE.md:3` "Owns".
- Say "presumes no split".
- Omit kasegi.
- Point the Q10 cell at the block's line range.
Conditional bullets (arc3-r3:31 and r4-09:65) apply only if the entry touches offset semantics or the `default` binding.
The pointer readout `pointers.py` (sha256 `55766b82…af468`) was run with cwd=/ (`python3 -B …/pointers.py /home/vgpnk/Projects/shokunin`), exit 0, and printed 6 pinned lines. Excerpt:
`tsukuroi-shokunin@7f4231401e49:corpus/knowledge/adjacency-handoffs-fleet-r1.md:54 sha256=8e9fda4c92b61ed4` / `| ADJ-06 | protocol integrator for ownership ruling | …`.

Lint guard for L1. It is necessary, not sufficient, because a pass does not prove a pointer is exact:
`rg -U -c -i -e '\bowns\b|-owned\b|with\s+the\s+operator|holds\s+the\s+same|prior\s+art|ground\s+reported' <entries>`
- Red before, frozen old entries: `evm-saved-interface-candidates.md:5`, `commonjs-destructured-require-edges.md:2`.
  Single-line mode misses C04's wrapped `:91-92`, so `-U` is required.
- Green, proposed blocks section: no match (rc=1).
Every attributed sibling fact still needs an exact `repo@commit:path:line` pointer plus a quote, checked by a non-author.

## Routed-item dispositions (proposed for the L1 lesson; not arbitration)

- `round-61-verifier-spotcheck.md:211`, false kasegi citation: avoided by narrow scope (no kasegi mention). The old text is retained.
- `:218`, "operator-owned ADJ-06": explicitly unresolved. The recipient wording is corrected in new text to the tsukuroi quotes; it is not repaired in place.
- Electron-role semantics: avoided by narrow scope through the C04 block's exclusion sentence.

## Unknowns and limits

- Kaidoku/tsukuroi HEADs may move after `69e82c48`/`6ecb8d2e`. The pins remain readable, but current-tip equivalence is not claimed.
- Whether L0 equals "operator" is not established by any line I read. That is why the block names no recipient.
- I did not review actual candidate prose, because none existed. The final entries need re-attack with this lens.
- I made one transient write of under 2 KB under `/tmp` (the green-scan extract), removed in the same command.

## Addendum: attack on R62ConnectKasegi's proposed kasegi wording (sent by IRC)

All checks are at kasegi `8bf98072` (clean worktree); the cited lines are verbatim. Option A (omit kasegi) is safe only if it fences kasegi alone.
- As a whole Q10 block, its sentence "No sibling lane's ground is claimed or restated" drops the kaidoku `README.md:38` and ADJ-06 contest. That is absorption by omission.

Option B is broken:
- It cites `:3` for "deployed-code … another province's ground", but kasegi `PROVINCE.md` contains 0 'deployed' tokens, and the phrase is itself an ownership ruling.
- It truncates `:42`, which introduces a list at `:44-47` (chousa, kagi, kake, kengaku) with no revenger; kasegi `PROVINCE.md` contains 0 'revenger' tokens.
- It claims an unperformed "reports … to the fleet" handoff.

The handoff in their section D implies the r24 byte walk could implement kasegi's deployed drift check. Restate it as an r24-only observation.

Rev.2 (`proposed-crosslane-block.md` sha256 `26e18ce5…`) is acceptable once three fixes are made:
- Line 56 says the reporting duty "is owned by the cross-lane critic". That is ownership language again; the block belongs to the entry, and L1 decides.
- The cell says "the contested sibling surface", which implies the report is complete.
- "inert" needs a recorded label or should be dropped.

The cell's "no claim rests on a sibling source" can stay if it is checked by the frozen `SOURCES.md` sibling grep (→ 0).

Omitting kasegi leaves no contest unreported. A keyword scan (EVM, bytecode, solidity, smart contract, JUMPDEST, PUSH4, CommonJS, destructuring) over `PROVINCE.md` and `corpus/README.md` at HEAD in the 20 sibling repos found hits only in kaidoku@69e82c48 (14). Kasegi had 0.

Correction to the proposed blocks: the Q10 cell should refer to the block by its heading, not by a line range. A line range drifts when the entry is edited and invites a Q11 challenge.

Rev.3 applies all five fixes. Three new defects remain:
- The digest they quoted (`0a8f4b8f…`) is not what I compute: `f1ce830e…`.
- "Authored, non-executed" is not recorded for every fixture. In the frozen `truth.json` notes, "authored" appears only in r19, and r22 and r25 do not say "no execution".
- The Q10 cell names `## Cross-lane contest (Q10)`, but the wording they point to (`R62ConnectEvmPrior/cross-lane-wording-C09.md`, sha256 `797af37f…`) is headed `## Cross-lane prior art (Q10)`. Used alone, that block also omits kaidoku `README.md:38` and ADJ-06.

Separate attack sent to R62ConnectEvmPrior. Its five kaidoku bullets match kaidoku@69e82c48 verbatim. Defects:
- Variant B says the reading "does not hold" on viaIR, but kaidoku `arc3-r6:24` records 14 of 15 viaIR legs on a JUMPDEST.
- "therefore … not a definition of the field" is a provider-method inference, which C1 excludes.
- The heading "prior art" implies a priority judgment between lanes.

Later revision (`proposed-crosslane-block.md` sha256 `adec7b45…`; the corrected `f1ce830e…` is already stale):
- The fixture-note defect and the heading defect are closed. The per-fixture notes are verbatim, `LOG.md:234…311` each begin "Authored", and there is one merged contest section.
- New defect: the Q10 cell embeds the literal `'kaidoku|kasegi|tsukuroi'` SOURCES command outside the contest block. That breaks the cell's own claim that the entry-side grep "prints only lines inside the block".
  - Repro: `celltest/entry.md` → grep prints line 3 (block) and line 9 (cell).
  - Fix: use the self-avoiding `kai(doku)|kase(gi)|tsukuro(i)` form in the SOURCES command too.

Rev.5 (sha256 `f1b0a4ea…8e6e`, quoted in full in their 49-line report; their message says 64 lines):
- The digest, per-fixture notes and merged-heading items are accepted.
- The self-match defect is not fixed. The cell at line 85 still embeds the literal SOURCES pattern.
  - Repro on the exact cell text: `celltest/entry-rev5.md` (`bbdd0ea1…`) → the entry-side grep prints line 3 (block) and line 10 (cell).
  - Status: not final on the Q10 cell until the one-token fix lands.
- "prior-art" wording remains (minor).

R62ConnectEvmPrior rev.2 (`cross-lane-wording-C09.md` sha256 `2dc09256…`):
- D1–D4 are closed. The block has no ownership or priority wording, the appendix values match kaidoku@69e82c48, and the script executes nothing.
- Still open:
  - The §2 digest scope is wrong. `carrier-A.hex` is 168 B with sha256 `36dc82468c5846a9`; "84 B, `a92ba152…`" is the decoded bytecode.
  - The added clause "stays uncovered until L1 admits it" puts a README-status statement inside the entry, which goes stale.
  - The cell is still pointed at by line range.
  - Rule 7 still uses the literal SOURCES grep, so the same self-match applies.

R62ConnectKasegi rev.6:
- The self-match is closed. On the cell extracted from their file (`celltest/entry-rev6.md`), the entry-side grep prints only line 3 (the block bullet). The self-avoiding SOURCES grep prints 0 on the frozen tree.
- The prior-art fallback is removed, and the report is 50 lines.
- One open item: the quoted digest `a1518e7e…` does not match the file, which now hashes to `92acdaf84c51e55fba5c91523b4625d09775cfb47aef7414995c7e5050e31faf`.
- The content has no open defects from this seat once the quoted digest matches.

R62ConnectKasegi rev.7 (final, frozen), checked independently:
- `sha256` is `f81145e5d778cc0a5b3b861cd247dd0ec5aac609d475b9348db7714537fc81f1`, quoted once in their 50-line report.
- The banner marks the file as audit material, not entry text.
- The plain-literal count is 0.
- The cell test (`celltest/entry-rev7.md`) gives a grep hit only at line 3, the block bullet.
- Status: no open defects from this seat. Use is L1's decision, not an admission.

R62ConnectEvmPrior rev.4 (sha256 `8719a3ef5787dd893a9ded09736158448e8c756669a8fca297953fec67297ed5`, no message sent), checked independently:
- Digest scope is split correctly: hex file 168 B `36dc8246…`, decoded bytecode 84 B `a92ba152…`.
- The README clause is dropped and replaced by "not evidence for this entry".
- The cell points at the heading.
- No plain sibling-name literal remains; the self-avoiding form appears 2×.
- The `arc3-r4:22` quotes match kaidoku@69e82c48 verbatim (3/3 `grep -F`).
- The copyable `markdown` blocks scan clean (rc=1).
- Status: no open defects from this seat.

R62ConnectEvmPrior's closing check: the artifact is still `8719a3ef…`. Its digest splits reproduce from `git show 69e82c48:<path>`:
- Rv2Token: file 3,886 B `d7f73058…`, decoded 1,943 B `c1081a56…`.
- carrier-A: file 168 B `36dc8246…`, decoded 84 B `a92ba152…`.

Caution for L1 (not blocking): the R62ConnectEvmPrior report's early sections still describe rev.1.
- `:52` says the file "holds two paste-ready variants (full prior-art paragraph; one-sentence minimum)", but rev.4 has neither.
- `:3`, `:7` and `:57` keep the "prior art" framing.
- Use rev.4 and its disposition table (`:79-83`), not §1.
- Its closing IRC summary concluded "no universal JUMPDEST meaning". That inference is not in its report and must not enter the entry or the lesson.
- Resolved at 18:18Z:
  - The report is 80 lines and now describes rev.4.
  - The remaining "prior art" and "holds" matches are either disposition-log text or `:48`'s description of the file.
  - The `arc3-r3:31` quote is verbatim (`grep -F` 1).
  - The artifact is still `8719a3ef…`.
  - Status: no open items.

Seat close (2026-10-21): R62ConnectKasegi was re-verified unchanged at `f81145e5…`. Both connector artifacts have no open defects from this critic. The cutover choice belongs to L1, and nothing here is an admission.

Installs: none.
