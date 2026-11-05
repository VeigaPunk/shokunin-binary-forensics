# ReviewerBlind — round 94 seat report (C15 blind-derivation vote)

Verdict: **entry matches the sources for all five sampled tools; mismatches: 0 beyond wording.** Vote cast (`vote.json`, 9 PASS / 8 n/a, every n/a reasoned ≥20 chars) bound to candidate digest `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`.

## What was done (blind order)

1. Derivation written BEFORE opening the entry, from `corpus/SOURCES.md` rows S054–S095 (scope/anchor/teaches cells) + the S498/S499 receipt bodies under `.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/` (both present). Full text: `.ufo/waves/round-94/w1/ReviewerBlind/derivation.md`.
2. Entry read once at `060a8e87d6de6b31f91b58524ab0fcad88ae5431` via read-only `git show`; not edited. Full diff + per-Q record: `.ufo/waves/round-94/w1/ReviewerBlind/evidence.md` (contains the digest; sha256 `c5200282ba10da5b526dad0512ccb0171dd07835842f2372f2ef5cd1debfd525` = `artifact_sha256` in `vote.json`).

## Findings

1. **No mismatch beyond wording (5/5 sampled tools).** Ghidra S055, radare2 S062, JADX S058, ILSpy S061, Frida S060: declared role, stated limitation, and boundary each match the entry's table rows.
2. **The r74-invalidated radare2 quote is absent.** The frozen entry never carries "command-line hexadecimal editor"; its paraphrase ("command-line binary analysis", "hex/format and scriptable inspection capabilities") is consistent with both the S062 scope cell and the corrected S431 pinned sentence. Same for the superseded dnSpyEx reordered quote and the bold-less jadx sentence: none reproduced.
3. **Wording-level observations (not defects):** (a) JADX limitation paraphrased "many cases" vs the source's "in most cases"; (b) Rizin grouped under "hex/format" though S069's cell says "framework/CLI surface" — Rizin is outside the assigned sample.
4. **Q03/Q11 angle clean.** No byte/semantic value is derived anywhere in the entry; the one prose date fact (dnSpyEx README "last revised in 2023") is traceable to S068's own teaches cell; no tool is credited with output the sources do not state; no run/installation credited anywhere (matches `verified-at`).
5. **Digest provenance.** Counter run at the freeze tip printed the digest and exited 1 as expected pre-landing (`C1_C15_HELD=fail`, `C1_VOTES=fail votes dir missing`, `C1_SOURCES=fail S498/S499 unresolved + new-row-missing` — the L1 lands those); cross-checked byte-identical against `ExecFrozen/freeze-state-digest.txt`.

## Residual risk / gaps

- The blind scope covers the five sampled tool rows plus a full-entry read for the credited-output angle; non-sampled rows (e.g. ImHex, Apktool, mitmproxy, papers) were checked only for the no-credited-output property, not row-by-row against their SOURCES cells.
- The r72-era rows the entry cites (S057/S058/S062/S066/S068/S094) are now rejected/superseded by r74 rows; the v3 gate's supersession-terminal semantics handle this, and the entry text itself is unaffected — recorded so the L1 does not mistake the observations in item 3 for admission blockers.
- Bounds: no lane file edited; no git/jj write commands; scratch `/fast/scratch/hyaku/revenger-r94/ReviewerBlind/` deleted before this report.
