# round-84 corrections — r83 non-author closure routed defects (status-neutral; addressed first, append-only, no in-place rewrite)

Base `54a36bca7bc52d528026ca28beb51f4cab98fa69` (r83 tip + the r83
verifier spot-check). The r83 non-author closure
(`corpus/lessons/round-83-verifier-spotcheck.md`, "Routed defects")
routed three status-neutral defects to round 84. All three are
dispositioned here; none is a round claim.

## Correction 1 — short-form sha pin drift (routed defect 2)

The five r83 prose surfaces pin the abbreviated suffix
`f520f8d6…9701` for `reports/round-83/orphan_sweep4.py`:

1. the round-83 report (fleet root `.ufo/reports/round-83/revenger.md:53`,
   orchestrator-committed; corrected here by pointer, not rewrite);
2. `corpus/lessons/round-83.md:125` (Gate, C2 chain);
3. `corpus/lessons/round-83.md:186` (Mistakes, CRLF-mutant row);
4. `SCORECARD.md:1183` (round-83 C2 row);
5. `LOG.md:1178` (round-83 claims bullet).

The committed blob is
`f520f8d69875d1ca83eb8daeddbffecb5f471bf5f5e6aba43bd97029fc2ea701`
(suffix `…c2ea701`, not `…9701`). The freeze-time FULL-sha pin in
`reports/round-83/claims.md` (§ Frozen sha256 pins) is correct and
governs; v3's `af64b4c5…b8748` and ag_probe's `22be124b…a08a5` short
pins verify as printed. Deriving command (run 2026-11-02 at base
`54a36bca`, worktree == HEAD blob, both print the same full sha):

```
sha256sum reports/round-83/orphan_sweep4.py
git show HEAD:reports/round-83/orphan_sweep4.py | sha256sum
```

Fix: this entry is the correction; the five surfaces are NOT rewritten
(append-only discipline). Every r84 surface pins the full sha.

## Correction 2 — census receipt pointer (routed defect 3)

`reports/round-83/census-after.log:23` names
`census-round-start-sanctioned2.log` (the r83 round-start sanctioned
re-run, exit 0) — never committed. The killed first attempt's output IS
committed (`.ufo/waves/round-83/census-round-start-sanctioned.log`:
false exit 1 with a clean `ok` output — r83 lesson Mistakes row 6). The
sanctioned2 bytes are gone with the r83 scratch (deleted at round end
per the contract). Disposition: the pointer is corrected by this entry
(census-after.log is not rewritten); the value it pinned (sanctioned
explicit-lane-dir form, exit 0, 31 W = 21 W01 + 10 W04, zero E) is
independently settled three ways:

1. the committed killed-run receipt's output body (identical W/E
   composition, verdict `ok`);
2. the r83 non-author verifier's independent re-run (exit 0, recorded in
   `corpus/lessons/round-83-verifier-spotcheck.md` § census);
3. this round's own round-start re-run, committed at
   `.ufo/waves/round-84/census-round-start-sanctioned.log` (exit 0,
   21 W01 + 10 W04, zero E — the same disclosed classes).

## Correction 3 — the unlanded cited receipt (routed defect 1)

`reports/round-83/v4-postlanding-recon.log` — cited by five surfaces
(the r83 report ×2, `corpus/lessons/round-83.md`, `SCORECARD.md`,
`LOG.md`), absent from the committed tree AND the worktree — is
regenerated from committed bytes only and lands in this commit. The
regeneration is fully disclosed in the receipt's own header (recon
recipe, instrument blob sha, basis movement); the load-bearing values
the five surfaces cite (`LANDABLE_ORPHANS=0`, exit 0, over the minimal
reconstruction with HEAD = `60693f2`) reproduce. Byte-verification of
the seven reconstruction receipts:
`.ufo/waves/round-84/carryin-byteverify.log` (7/7 MATCH; short shas
match the r83 lesson's pins).
