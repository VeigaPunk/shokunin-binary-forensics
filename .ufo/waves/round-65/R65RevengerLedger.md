# R65RevengerLedger — ledger-discipline reversal: prong (c) landed, prongs (a)/(b)/(d) attacked on the landed `receipt_ok`

**NOT-FALSIFIED** — the landed C5 control (prong c, real foreign ID) fires exactly as frozen on the landed bytes; every receipt-only transplant variant of prongs (a)/(b)/(d) is equally caught by the same conjunct, so the control is sound; the residual uncaught surface is real but is precisely the round-63/64 routed 6-prong check's territory, whose owner is named at umbrella level — with one divergence recorded (§5: the round-65 lesson omits the routed-forward row that claims.md promises, and attack name (d) appears in no lesson). No verifier was edited.

## 1. Harness (read-only, landed bytes)

Modules loaded from the landed tree with `importlib` (module name ≠ `__main__`, so `main()` never ran; no file I/O at module level); all receipts/records read read-only from `corpus/live/runs/`; forgeries on `copy.deepcopy` copies in scratch only. Script: `/tmp/revenger-r65-ledger/prongs.py` (sha256 `eda611d830d0d6f5987d9b48f4c658ff7b74a34e930cac63baec99542989624c`), full output `/tmp/revenger-r65-ledger/prongs.out` (sha256 `cbe7f7d664261120fa48609dd68d88f30baeee30e1690cd4c7ac7ce865005f27`, 1494 bytes). Harness sanity: `A0 baseline honest r47 pair: receipt_ok=True` — the predicate accepts the honest pair, so every "caught/uncaught" below is measured against a working oracle.

Targets: `corpus/verify_icon_languages.py` (receipt_ok `:118-120`, evidence conjunct `:120`; record-side pin `require(record['evidence_id']==eid …)` `:132`; C5 control `:155-157`) and `corpus/verify_multi_icon_states.py` (receipt_ok `:121-123`, conjunct `:123`; record pin `:135`; C5 control `:154-156`). Frozen C5 mutant regex `receipt\['evidence_id'\]\s*==\s*evidence_id` matches exactly once per script (`grep -cE` → 1 and 1), so the kill rule is well-formed on the landed bytes.

## 2. Prong battery — actual output

```
H(raw47)=e12ff95b78b57fde… H(raw42)=7163c758c776f8aa… distinct=True
languages C5 foreign id == multi r42 EXPECTED id: True
fresh id: ev_2e2ca092808f7c8843794e2f4c004e328beadd31389afe8c40bbebdb42579485
A0 baseline honest r47 pair: receipt_ok=True (harness sanity, must be True)
caught (receipt_ok=False) — A1 prong(a) same-run sibling id (r48), receipt-only
UNCAUGHT (receipt_ok=True) — A2 prong(a) both-sides consistent transplant (checker handed r48 eid): pairwise-blind: no registry consulted
caught (receipt_ok=False) — B1 prong(b) injectively fresh id, receipt-only
UNCAUGHT (receipt_ok=True) — B2 prong(b) fresh id, self-consistent pair: fresh id never greps in corpus
caught (receipt_ok=False) — D1 prong(d) cross-record stdout digest, receipt-only
UNCAUGHT (receipt_ok=True) — D2 honest id + stdout re-signed over FORGED record bytes: selected 1→0 flipped
caught (receipt_ok=False) — D2b same forged record bytes vs HONEST stored receipt
caught (receipt_ok=False) — D3 r47 receipt paired with r42 record bytes
caught (receipt_ok=False) — A1' multi r43 receipt with r42 sibling id
caught (receipt_ok=False) — B1' multi fresh id
UNCAUGHT (receipt_ok=True) — D2' multi re-signed honest id over forged record bytes
```

Prong definitions used: (a) same-run = a real ID from the same script's sibling round (r47 receipt ↔ r48's `ev_6fbaf25d…`, symmetric r43 ↔ r42); (b) fresh = well-formed `ev_`+64-hex never recorded (grep of the whole corpus for the session's fresh ID returned zero lines); (d) cross-record stdout binding = the receipt's `stdout_sha256` set to `H()` of another run's record bytes (r47 receipt ↔ r42 bytes) and, in the load-bearing form, re-signed over a locally forged record.

## 3. What is caught — and why the control's "real foreign" choice adds no coverage

Receipt-only transplants of all three prongs are caught (`A1`, `B1`, `D1`, plus symmetric `A1'`, `B1'`), because every one of them changes exactly the field the C4/C5 conjunct family pins: `receipt['evidence_id']==evidence_id` (`verify_icon_languages.py:120`, `verify_multi_icon_states.py:123`) or `receipt['stdout_sha256']==H(raw_bytes)` (same lines). D1 is caught by the stdout conjunct against this round's own `H(raw_bytes)`; D2b proves the receipt-vs-record catch is nothing deeper than that equality (honest stored receipt vs forged record bytes → False). The landed C5 control's transplant is a member of the same equivalence class as A1/B1: **any** deviation of `receipt['evidence_id']` from the EXPECTED constant fires the conjunct. The "real foreign" property (prong c) earns its keep only as provenance discipline for the control itself (the ID demonstrably exists in saved bytes, §4) — it does not add detection coverage over a fresh-ID control. That is not a defect of the landed round-65 fix; it is the honest boundary of what one in-script conjunct control can measure.

## 4. Registry reality of the two control IDs

`ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d` (languages control) is multi script r42's EXPECTED ID — verified byte-true (`…==eid42 → True`) and present in `corpus/live/runs/round-42/{LEDGER.md, inspection.raw.json, producer-receipt.json}`. `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421` (multi control) is languages r47's ID, present in `corpus/live/runs/round-47/{LEDGER.md, inspection.raw.json, producer-receipt.json}`. Each ID also appears as **prose** in other rounds' verifier LEDGERs (`round-46/LEDGER.md:4` and `round-55/result-review.md:28` cite the r42 ID; `round-50/LEDGER.md:4` cites the r47 ID) — cross-run prose mentions, not record-level ID reuse (rounds 46/50 have no `inspection.raw.json`; their records are verifier receipts). No injectivity violation exists in the record registry today, but this prose spread is exactly why the routed prong-4 spec must scope "the ID named in **that run's** LEDGER row", not any-ID-mentioned-anywhere.

## 5. Residual uncaught surface (structural, demonstrated)

`receipt_ok` is a pure pairwise predicate over `(receipt, command, expected_hash, evidence_id, raw_bytes)`: it consults no registry, no other record, no LEDGER. Therefore every attack where the attacker owns the pairing passes it:

- **A2** — consistent same-run transplant across record+receipt with the checker handed the forged `evidence_id`: True.
- **B2** — injectively fresh ID on a self-consistent pair: True.
- **D2/D2'** — honest ID kept, `stdout_sha256` re-signed over locally forged record bytes (r47 selection flipped 1→0; r43 image[1] selection → None): True on both scripts. R64RevengerLedger §6 named this attack ("self-consistent receipt re-signing with ID reuse") as INFERENCE; it is now **executed against the landed bytes** — the receipt_ok family cannot see it, and inside `check()` the only thing that fires is the independent `decoded`-vs-record comparison, not the receipt chain.

In-script mitigations that do exist: the hardcoded `EXPECTED` constants pin each round's ID (`verify_icon_languages.py:107-111`, `verify_multi_icon_states.py:105-115`) and the record-side `require(record['evidence_id']==eid …)` (`:132` / `:135`) catches record-side transplants in the two covered scripts — but both are just more recorded strings in the same file, and coverage is thin: `receipt_ok` exists in **four** verifiers (`verify_icon_languages.py:118`, `verify_multi_icon_states.py:121`, `verify_icon_states.py:119`, `verify_named_multi_icon_states.py:16`) while the C5 evidence-conjunct control family scores only the two. The routed 6-prong check over the whole `corpus/live/runs` tree (R64RevengerLedger §6 items 1-6: partition, R→S, R→F, X→ID, injectivity registry, attribution) remains unimplemented in any committed checker — grep finds no such tree-level probe in `reports/round-65/measure.py` (its C5 block only runs the two scripts' self-tests with the frozen mutant). The residual surface of §5 is real and open.

## 6. Owner naming — does the routed check name owners for (a), (b), (d)?

- **Umbrella owner: YES.** `corpus/lessons/round-64.md` routed row 4: "Owner named: a future calibration round that registers a receipt/Evidence-ID binding check", with the 6-prong shape and the named attack at `round-64.md:244-245` ("6 prongs incl. an Evidence-ID injectivity registry; attack it must catch: self-consistent receipt re-signing with ID reuse"). Round-65's landed C5 is that row's prong (c).
- **Per-prong in round-65's own lesson: NO — divergence.** `reports/round-65/claims.md` (frozen) states "prongs (a),(b) and the injectivity registry remain future-round debt (owner named in the lesson)", but `corpus/lessons/round-65.md` "## Routed forward" carries only five items (SHONEN box `[~]`, AST-bound mutation counter, recheck holes H1-H3, r58/59 quotes, freshness wording) — **no evidence-ID transplant row at all**. The promised owner sentence exists only in round-64's lesson, not the lesson of the round that claims to name it.
- **Prong (d) as an attack name: NO owner, no name.** `grep -in "cross-record|same-run"` over `corpus/lessons/*.md` returns zero rows; "injectiv" appears only at `round-64.md:244`. Cross-record stdout binding is covered only implicitly by the umbrella owner via check-shape items 2 (R→S digest recompute) and 5 (injectivity); nowhere is it named as an attack to catch, and claims.md's residual-debt sentence names (a),(b)+registry but not (d).

Mapping for the owner round: (a) same-run ID → prong 4 (X→ID chain) + prong 5 (injectivity); (b) fresh ID → prong 4 (the weaker catch: "no honest LEDGER row binds it", R64RevengerLedger §6); (d) cross-record stdout binding → prong 2 (R→S) + prong 5; A2/B2/D2-class forgeries → prong 5 alone, plus prong 3's bytes-side falsification.

## 7. Verdict rationale and bounds conformance

The assigned attack surface was "is the landed prong-(c) discipline reversible, and are (a)/(b)/(d) still uncaught?" — answer: the landed control behaves exactly as its frozen contract requires (fires on real-foreign transplant, attribution string present, mutant regex single-match); receipt-only (a)/(b)/(d) are NOT uncaught (the brief's premise narrows: they fall to the same conjunct); the genuinely uncaught forms are the attacker-owns-the-pairing variants (A2/B2/D2), demonstrated live, and those are owned — at umbrella level only — by the round-64 routed row. Verdict NOT-FALSIFIED: nothing observed contradicts the frozen C2 claim's contract; the recorded divergences (§5 coverage thinness, §6 lesson routed-row omission, (d) unnamed) are residual-surface findings for L1, not falsifications of C1/C2. No verifier edited; no repo byte outside this report written; scratch confined to `/tmp/revenger-r65-ledger/` (kept for reproduction; safe to remove after landing). Installs: none — no pacman, no uv/npm, no binaries; tools used were already-present `python3`, `grep`, `sha256sum`, `wc`.
