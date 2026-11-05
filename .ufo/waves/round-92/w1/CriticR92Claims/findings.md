# CriticR92Claims — round-92 adversarial review (C1 K, C2 calibration)

Scope: read-only review of claims.md, both frozen counters, the controls, and the probe.
Lane HEAD 9402183; `git status -- reports corpus` clean. No frozen file edited. No git mutation. No install.
Reproduce everything: `python3 -B .ufo/waves/round-92/w1/CriticR92Claims/forge.py` (receipt: `forge-receipt.txt` beside it). Scratch is removed by the script.

## Ranked findings

**1. [High] C2 does not check the claimed token; any non-frontier C08 token passes.**
Claim: C08 `frontier -> uncovered`. Predicate: `C2_C08_CLEAR` only asks that C08 is absent from the probe's mismatch list (`reports/round-66/measure.py:92` flags only `frontier` rows). Receipt:
- C08 -> `partial` (no record claim): `C2_VERDICT=pass`
- C08 -> `held` citing existing `knowledge/seed.md`: `C2_VERDICT=pass` (K_HELD = K_HELD_BACKED = 9)
- C08 row with trailing cell `| frontier | note |` (probe reads `cols[-1]`="note"): `C2_VERDICT=pass`
- The intended `uncovered`: `C2_VERDICT=pass` (identical verdict, so the predicate cannot tell the real move from the cheap ones)
Pre-freeze controls do not catch this: `controls/run_controls.py` has no non-frontier, non-uncovered case, and the claim says the controls guard skip-work variants.
Close (frozen file, not edited): `reports/round-92/c2_legend_counter.py` needs a leg `C2_C08_TOKEN` that requires row C08 to have exactly 5 cells and status exactly `uncovered`; add `c2-partial`, `c2-held-seed` and `c2-trailing-cell` as fail controls to `run_controls.py`.

**2. [High] C2 is cleared by destroying the only C08 saved record.**
`corpus/live/runs/round-77/inspection.json` is the only saved record whose `operation` is in C08's ROW_OPS (`reports/round-66/measure.py:73-77`). Deleting it with the token still `frontier` gives `C2_VERDICT=pass` (`c2-del-r77`). The claim's "record exists" premise is therefore not enforced by the counter; the counter rewards removing evidence.
Close (frozen file): pin `sha256` of `corpus/live/runs/round-77/inspection.json` in `c2_legend_counter.py`, add leg `C2_C08_RECORD` (file present and digest matches), and require the token to be `uncovered` when it is present.

**3. [High] C1 passes on fabricated artifacts; all 12 legs pass on a full forgery.**
Forgery: a stub entry with `admission-status: admitted`, a fenced `$` block, an invented `S491` SOURCES row dated `2026-11-05` with `status mined`, a README C03 flip to `held`, and two votes from invented seats `ForgerA`/`ForgerB` whose `candidate_sha256` is the forged entry's digest. Receipt: `c1-forge-full` -> `C1_VOTES=pass C1_LINT=pass C1_EMBEDDED=pass C1_SOURCES=pass C1_VERDICT=pass`, exit 0.
The only legs that bite are sha binding (`c1-forge-badsha` fails `C1_VOTES`) and the presence of a fenced block (`c1-forge-noembed` fails `C1_EMBEDDED`). Every other leg is satisfied by editing text. The counter does not check that votes come from non-author seats (the claim's kill rule says it does; `c1_k_admit_counter.py` checks only distinct seat strings and `role`), nor that a vote is backed by a real review artifact.
Close (frozen file): require each vote to reference a `.ufo/waves/round-92/` artifact whose sha matches, check the seat against `.ufo/waves/round-92/w1/swarm-registry.json` and the entry author, and bind SOURCES `opened` dates to receipts. Until then `C1_VERDICT=pass` attests the text and sha only, not that non-author seats reviewed it.

**4. [High] C1 accepts `n/a` for every Q01–Q17.**
The vote test is `ds[q] in ("PASS", "n/a")` (c1 counter, votes loop). `c1-forge-allna` (17 × `n/a` in both votes) gives `C1_VOTES=pass`, `C1_VERDICT=pass`.
Close (frozen file): require PASS for all 17, or require an in-entry justification for each `n/a` and count `n/a` against a budget.

**5. [Medium] C2 probe is read from the lane working tree and imported from its own directory.**
`PROBE = LANE / "reports/round-66/measure.py"` (working tree, not the `--rev`), and Python puts the script's directory first on `sys.path`. A file `reports/round-66/tempfile.py` runs before the stdlib module and prints forged labels: `c2 shadow-probe -> C2_VERDICT=pass` with `C2_LEGEND_MISMATCH=0`. The cwd=`/` and TMPDIR handling is sound (cwd cannot shadow anything; TMPDIR is confined to the counter's scratch), so the gap is the probe source and import path, not the cwd. Currently clean: `git status -- reports corpus` empty at HEAD 9402183.
Close (frozen file): run the probe from `git archive REV reports/round-66`, or compare `git hash-object` of `measure.py` with the rev blob, and invoke with `python3 -I` (isolated mode, drops script dir from `sys.path`).

**6. [Medium] `C1_EMBEDDED` is vacuous for a fenced `$` block with zero output lines.**
`check_embedded_outputs.py` `drift()` iterates only the printed lines (lines 153–155), and `evaluate()` adds a checked block for any command that exits 0 (lines 189–191). A block `$ python3 -B corpus/lint_entry.py --self-test` with no output lines passes (`c1-forge-full` embeds exactly this). So the leg certifies that a command ran, not that any output was embedded.
Close (`corpus/check_embedded_outputs.py`, read by the frozen counter): require at least one output line per block, and require the counter to check a minimum line count.

**7. [Medium] `C1_SOURCES` trusts self-declared `mined` status and date.**
`r[7] != "mined" or r[8] != ROUND_DATE` reads two cells the author writes. Nothing ties `opened 2026-11-05` to a fetch or quote receipt (`corpus/audit_source_quotes.py` exists and is not called).
Close (frozen file): call `audit_source_quotes.py verify` on each S-row cited by the entry.

**8. [Low, calibration of the claims] The claims overstate what the predicates measure.**
claims.md says C2 "moves frontier -> uncovered" and C1 "entry is scoped to the observed fixtures"; neither predicate measures the token or the scope. The claim text should state that `C2_VERDICT=pass` attests "C08 not flagged", and that C1 attests "votes and sha bind to the committed text", not that the entry's content is correct.

**9. [Reviewed] Step 5, entry scope/source statements.** The entry landed late:
`corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` (707 lines, `admission-status: candidate`), READY at `.ufo/waves/round-92/w1/ScribeR92Entry/READY` with `sha256=2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6`, which I recomputed from the entry bytes with the admission-status line normalised — match. The bounded wait (40 × 30 s) had timed out before the scribe wrote anything; the verdict below is against the file as it stands at review time.

Verified by me: digest match; `lint_entry.py` exit 0 (QMAP/Q14/Q15/HEADER all 0); `check_embedded_outputs.py` exit 0, `checked_blocks=11 problems=0`; my own runs of the four oracle commands reproduce exits 0, stdout line counts 11/21/48/40 and summary lines `ORACLE OK (10/10|20/20|47/47|39/39 checks)`; `sha256sum` of both fixtures matches the entry (`25ece37d…`, `94429fa4…`); `git rev-parse 9402183a^{commit}` matches the `verified-at:` line; the locator lines `oracle_check.py:28` (data-directory read) and `:33` (`assert sig == 0x424A5342`) are exact; all seven S491 quotes plus the S493 row and both S494 quotes verify verbatim (whitespace-normalised) against the wave snapshots `ScoutR92Managed/snapshots/{ecma335-6th-edition.txt:14205,14221,14247,14317,14484,14761,14779; pe-format.txt:618-620; api-metadatarootbuilder.txt}`.

Statements that go beyond the located quotes/sources (all note-level; none a FAIL):
- `:224-226` and `:354` — "ECMA-335 §II.24.2.2 … lists the same five names" and "the records' `#GUID` spelling is the specification's spelling": the located §II.24.2.2 quote carries the count of stream kinds, not the names; the name list with `#GUID` casing sits in the section body (snapshot `ecma335-6th-edition.txt:14247-14253`), where I verified it. True, but it rests on the anchor section, not on a carried quote.
- `:399-400` — receipt details (`rea` 6.8.0, provider, exit 0, stderr 0 bytes, stdout digest) are prose-cited from `receipt.json` files and framed as recorded, but item 25's explicit "recorded" label covers only the digests. Q11-compliant in framing, worth a labelling tightening.
- `:378` / `:523` — the S491 version-string quote ends at the PDF line wrap ("…any conforming"), so the quoted requirement is a partial sentence; the entry only uses it to report the `v4.0.30319` divergence as unknown (`:376-379`), which is the honest handling.

Scope discipline is otherwise strict: the coverage-map line and items 15, 21–27 confine every claim to the two fixtures and four records, label every recorded value, and claim no producer readiness. Q-map: PASS on Q01–Q04, Q06, Q07, Q09–Q11, Q13–Q17; n/a on Q05, Q08 (superseded by Q11), Q12. Vote written to `reports/round-92/votes/CriticR92Claims.json`.

**10. [Info] K equality interacts with C2.** `C1_K_HELD_BACKED` requires exactly 9, and C2's `K_HELD == K_HELD_BACKED` does not require C08 to stay `frontier`. A C08 `held` token citing an existing file (finding 1) would push C1's K to 10 if C03 also landed, which C1 would then reject. It does not bypass C1 because `C1_C03_HELD` is still required. Note for the mutation seat.

**11. [Info] Working-tree changes not mine.** `SKILL.md` (+22/−1) is modified; `.gitignore` gained `__pycache__/`. Neither counter reads `SKILL.md`. `git check-ignore` on the vote, entry and SOURCES paths returns exit 1 (nothing ignored), so the L1's commit will include them.

## Summary
- C1: full forgery passes 12/12 legs (`c1-forge-full`); wrong sha and no-block variants fail as expected; all-`n/a` passes.
- C2: intended move passes; `partial`, `held`+seed, trailing-cell, round-77 deletion and probe shadow all pass. Base fails as expected.
- No frozen file edited; no git mutation; no installs; scratch removed by `forge.py`.
