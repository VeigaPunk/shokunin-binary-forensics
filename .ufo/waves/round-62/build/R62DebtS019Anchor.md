RESULT: COMPLETE

Seat `RevengerR61-2.R62DebtS019Anchor` (round-62 build, leaf). Scope: re-open the
Solidity metadata page, locate the intro-paragraph vs Encoding-section anchoring
mismatch behind `W3SrcContractCells.md` F1, and propose (not apply) retain-old-debt
vs a lawful correction row. Frozen `a3498e25ad87bf756288812d0ea7c474b09433c7`
extracted read-only to `/fast/scratch/hyaku/revenger-r62/R62DebtS019Anchor/archive`;
no production/corpus/fixture/README/lesson byte written, no admission claimed, README uncovered.

## Opens (2026-10-21 18:03Z, HTTP/2 200, curl, read-only)

```text
/en/latest/metadata.html   38117 B  last-modified 2026-09-29 13:01:07 GMT  sha256 3407a364bf99c6a0b85bedc83d71afb4252fcef76bad8eeb5d5d9eca04c9ba64
/en/v0.8.37/metadata.html  37987 B  last-modified 2026-09-10 06:40:16 GMT  sha256 017ee271f129aeb290082c112a57b674bab9cc1f5d5629e43ec239760ca410ad
titles "Solidity 0.8.38-develop documentation" / "Solidity 0.8.37-develop documentation"; headers+bodies in web/
```
No JS, bytecode, fixture, producer, chain/RPC or service was run.

## Derived mismatch

Command: `python3 -B s019_anchor_readout.py` -> `s019_anchor_readout.out` (57 lines,
exit 0; script sha256 `39ff7d1f…10d33`).

- `corpus/SOURCES.md:33` (frozen) `anchor` = "§Encoding of the Metadata Hash in the
  Bytecode; page … last-modified 2026-09-29"; `scope` = "placement of the CBOR
  metadata tail that solc appends to runtime bytecode by default"; `teaches` =
  "Compiled runtime bytecode normally ends in non-code metadata bytes…".
- Output: whole page contains `runtime` once; intro blocks containing `runtime` = 1;
  Encoding blocks containing `runtime` = 0 (same in v0.8.37); Encoding blocks
  containing `CBOR` = 3, `end of the bytecode` = 2, `deployed bytecode` = 1.
- Runtime paragraph is zero-based index 3 of the 10 `<p>` blocks in §Contract
  Metadata — first paragraph after the two-item list, not the section's first;
  round-61 Gate's label "§Contract Metadata, para 1" (`corpus/lessons/round-61.md:58`)
  is therefore not a safe locator either.
- Exact sentences: intro "The compiler appends by default the IPFS hash of the
  metadata file to the end of the runtime bytecode (not necessarily the creation
  bytecode)…" (19 words); §Encoding: "Because we might support other ways to
  retrieve the metadata file in the future, this information is stored CBOR-encoded."
  (19 words), then "The last two bytes in the bytecode indicate the length…".
- Cross-version: three load-bearing paragraphs byte-identical between `/en/latest/`
  and `/en/v0.8.37/` (raw `<p>` spans: 564 B `618306e5…`, 390 B `1b183a54…`,
  389 B `12199700…`); page unchanged since round 61 (38117 B, 2026-09-29), so the
  defect existed when the row was written.

Finding: the explicit `runtime` term and the not-necessarily-creation caveat are
grounded only by the §Contract Metadata intro paragraph; `CBOR` appears only in
§Encoding (its one `deployed bytecode` occurrence is the --no-cbor-metadata skip
sentence). Neither section alone grounds the cell; W3's F1 reproduces exactly. The
minimal fix is an anchor naming both sections, or dropping one half of the claim.

## Disposition for L1 (row not written)

- **Option R — retain old debt (recommended).** No `SOURCES.md` change; record
  entry-level `avoided-by-narrow-scope` (the round-62 EVM entry excludes the
  CBOR/compiler generalization, so no admissible sentence rests on S019) plus
  registry-level `explicitly unresolved`. Rule 2 forbids editing the anchor in
  place, and a correction row with no consumer would be `queued`/`used-by —`,
  i.e. inert churn plus a W04 duplicate-URL warning (S024/S008 precedent).
- **Option C — lawful correction row.** Pre-drafted 11-cell row in
  `…/S019-correction-proposal.md` (validated: 11 cells, `teaches` opens
  `supersedes S019 —`): anchor both sections, pin `/en/v0.8.37/`, status `queued`,
  `used-by —`; id `S032` only if reserved S028–S031 land (L1 renumbers). Old S019
  stays `mined`/unedited; log one 19-word quote; do not cite it for the EVM entry.
- Decision rule: no metadata-tail sentence in the integrated EVM entry -> Option R;
  a sentence citing S019 -> delete it (preferred, matches the registered scope) or
  apply Option C and have the entry open the page itself.

## Unknowns

- `…/round-62-evm-dispatch-byte-evidence.md` absent from frozen archive and live
  tree; "excludes CBOR/compiler generalization" is assigned scope, not observed text.
- `/en/latest/` can move (S019 `recheck: on-release`); the v0.8.37 pin is
  content-identical today but L1 owns it. No census run; W04 is precedent only.

Proposed artifacts (scratch, no production edit): `/fast/scratch/hyaku/revenger-r62/
R62DebtS019Anchor/{s019_anchor_readout.py, s019_anchor_readout.out,
S019-correction-proposal.md, web/*}`. Prior rejected candidates, round-61
reports/counterexamples, verifier lesson, README/map/holds untouched.

Installs or updates: none.
