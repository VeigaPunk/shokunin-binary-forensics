# ReviewerClaimsR99 — findings on the frozen round-99 claims (7e6edd4)

Reviewed: `reports/round-99/claims.md` at 7e6edd4db649f99c425daa46a91edbbd18a6e27c, its controls,
frozen v7 (`reports/round-98/c1_k_admit_counter7.py`), the r98 builder
(`.ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py` + parity patch). All experiments on
scratch copies under `/fast/scratch/hyaku/revenger-r99/ReviewerClaimsR99/` (deleted after; receipts
copied to `w1/ReviewerClaimsR99/`). No frozen bytes edited; no counter run on any tree with C14 held.

## Findings

### F1 — BLOCKER (C1): the frozen leg set requires an S505 SOURCES correction the Surface-moved sentence does not declare
- **Claim sentences:** "that set is every v7 `c14` leg with the round-99 votes dir `reports/round-99/votes`, wave dir `.ufo/waves/round-99`, registry `.ufo/waves/round-99/w1/swarm-registry.json`, the round-99 pinned seats and `FREEZE_REV` = the claims-freeze commit, plus every new v8 leg." and "Surface moved: coverage-map row C14 (`corpus/README.md`): knowledge cell becomes exactly `knowledge/round-98-rea-host-readiness.md`, status `held`; the entry moves `admission-status: candidate → admitted` …".
- **Defect:** v7 c14's `C1_USEDBY_GROUNDED` checks `GROUNDED_ROW_IDS=("S505","S506","S507")`; the `S505` used-by cell (frozen, both 3d054a98 and 7e6edd4) is `corpus/knowledge/round-96-native-analysis-sessions.md`, and that entry contains no `S505` token (grep count 0 at 3d054a98 and 7e6edd4). The declared surface (README C14 row + entry admission-status line only) cannot fix this, so on the landing tree `C1_USEDBY_GROUNDED` fails and `C1_VERDICT=pass`/exit 0 is unreachable. Conversely, the only way to reach the target is a third landing edit the claims never declare — an undisclosed surface move.
- **Evidence:** `v7 --profile c14 --tree <claims-freeze archive copy>` → rc=1, `C1_USEDBY_GROUNDED_WHY=S505 -> corpus/knowledge/round-96-native-analysis-sessions.md:entry does not cite row id`. Same tree + the declared surface + S505 `mined→queued`, used-by `→—`: `C1_USEDBY_GROUNDED_WHY=ok`, `C1_K_HELD_BACKED=14/15` and only `C1_VOTES`/`C1_VOTE_NOTES` fail (exactly the legs r99 votes replace). Round-98 solved the identical problem by claims Amendment A2 (`reports/round-98/claims.md`: "The S505 correction is fixed at status `mined → queued` and used-by `… → —`"); the r99 claims inherited the leg but dropped the landing edit.
- **Minimal fix (L1, before the v8 freeze):** amend the C1 Surface-moved sentence to add the third landing edit — S505 row `mined → queued`, used-by `corpus/knowledge/round-96-native-analysis-sessions.md → —`, logged old→new (A2's exact correction; digest-neutral, entry bytes untouched, no re-vote). Alternative (weaker): re-scope c14r99's `C1_USEDBY_GROUNDED` to S506/S507 — but that departs from "every v7 `c14` leg".
- **Severity:** blocker for C1 as frozen; fixable by amendment before the v8 freeze.

### F2 — MEDIUM (C2): "the v7 round-98 constants, unchanged in v8" vs "every new v8 leg applies in all three profiles"
- **Claim sentence:** "… the counter run as `--profile c02` and `--profile c14` (the v7 round-98 constants, unchanged in v8)." — v8 contract: "Every new v8 leg applies in all three profiles unless the leg itself is profile-specific by design".
- **Defect:** on c02/c14 the executed leg set is not v7's: new profile-neutral legs run there too. Any new leg keyed on round-99 surfaces (r99 votes dir, wave dir, registry, freeze archive additions) fails the honest r98 control fixtures, which carry no round-99 surfaces → `control-BROKEN` → C2 unmet by the kill rule. Not a false-pass route (the kill rule catches it), but the two sentences are jointly satisfiable only if every non-profile-specific new leg accepts the honest r98 fixtures; nothing in the claims says so.
- **Minimal fix:** one sentence in the v8 counter/harness docstrings (and ideally an L1 note): new c02/c14-visible legs must be keyed on round-98-visible surfaces and must keep both honest r98 controls `control-ok`; r99-surface checks go into `c14r99`-only legs.
- **Severity:** medium (process trap; burns the C2 target as an honest kill if hit).

### F3 — LOW (C2): the recorded-run requirement does not force per-vector counter invocations
- **Claim sentence:** "one recorded run prints `C2_ACCEPTED=0/12`, `C2_CONTROL_C02=control-ok`, `C2_CONTROL_C14=control-ok` and `C2_STUB_SELFTEST=ok`".
- **Defect:** those four tokens alone do not prove the real counter ran on all twelve vector trees; the stub self-test validates counting semantics, not per-vector invocation. A harness that runs the counter on a subset and prints the tokens would satisfy the literal sentence.
- **Minimal fix:** require the recorded run to include the builder's per-vector lines (name | rc | verdict | K | failing legs | outcome) for all 12 vectors + both controls, as the frozen v7 receipts already do.
- **Severity:** low.

### F4 — INFORMATIONAL (C1): the S506 re-open receipt is never machine-checked
- **Claim sentence:** "C1 rests on S506 (re-opened this round at the pinned revision, … `quote-receipts/S506-reopen-r99.txt`)".
- **Defect:** none in the predicate — but note `RECEIPTS_DIR`/`FETCH_LOG_REL` are not in the c14r99 override list, so `C1_RECEIPTS` validates the r98 receipt under `reports/round-98/quote-receipts/`; the r99 re-open receipt is evidence for the claims file only. I re-verified it independently (below), so the duty is currently honest; nobody should expect the counter to police the re-open.
- **Severity:** informational.

## Do-nothing reachability (task item 1) — all refused, paste of rc
- C1 do-nothing (claims-freeze archive, v7 c14): rc=1, `C1_VERDICT=fail` (receipt `w1/ReviewerClaimsR99/v7-c14-donothing.log`).
- C1 reused r98 votes: refused inside the same run — `C1_VOTES_WHY=vote digest mismatch for CriticR98 digest=36cc6ac2…` (r98 votes carry 6d27c129…).
- C1 header-only flip (entry → admitted, nothing else): rc=1; failing `C1_TARGET_HELD`, `C1_TARGET_CITES`, `C1_VOTES`. Note the digest is invariant to the flip (v7 `digest()` normalizes admission-status lines), so votes would still match — the README legs are what refuse it.
- C1 junk-row control (README C14 status cell → held only): rc=1; failing `C1_TARGET_CITES`, `C1_ADMITTED`, `C1_VOTES`.
- C2 dropped vectors / control-BROKEN / stub counters / builder edits: builder inputs are pinned (c02 = frozen v6 `_fixture` from the r96 freeze archive + L1 round-96 record supplement; c14 = `git archive 1b76b4d` + three declared landing edits, digest asserted `6d27c129…`); kill rule covers control-BROKEN; stub self-test covers counting; residual = F3.

## Predicate/counter identity and coupling (task item 2)
- C1 predicate implementable as stated **except for F1**. Every other v7 c14 leg passes on the claims-freeze tree (do-nothing run: receipts, registry, deriv table, lint, quotes, sources, admitted-union, rows, entry bytes, header position, verified-at, ownwork, quote bytes, sids, pycache all `pass`).
- C2 predicate is the sentence the builder/harness counts: `parse()` reads `^C1_VERDICT=(\w+)$` — same sentence. ✓
- C1→C2 coupling: none through data. c02/c14 profiles keep v7 constants (r98 paths); the builder reads only pinned inputs (v6 `_fixture` at the r96 freeze; `1b76b4d` archive; lane `corpus/` bytes C1 never touches). The only coupling is the shared counter file — F2.
- C1 landing target is otherwise consistent: `HELD_TARGET=14` = printed `14/15`; `C1_ONLY_TARGET` compares against `FREEZE_REV`=7e6edd4's README, so flipping only the C14 row passes; `C1_ADMITTED` requires exactly one header line `admission-status: admitted` — matching "stated in the body, never in the header line" (the body must avoid a literal `admission-status:` line prefix; the current body has none).

## Factual ledger (task item 3) — every sentence checked
| Claim sentence | Result |
|---|---|
| Base K 13/15; C05 `uncovered`, C14 `partial` at 3d054a98 | MATCH (git show: 13 held rows; C05 uncovered; C14 partial) |
| base 3d054a98 is the r98 closure tip, parent of the freeze | MATCH (7e6edd4's parent is 3d054a9) |
| Lint `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0 | MATCH (re-run inside v7 leg on freeze copy: `C1_LINT=pass`, same four zeros) |
| Vote-binding digest `36cc6ac2cd37…948fce5` | MATCH (recomputed with v7 `digest()` on the frozen entry) |
| "Any entry edit other than the admission-status line invalidates the votes" | MATCH (v7 `digest()` normalizes only `admission-status` lines) |
| r99 candidate = r98 candidate + Q11/Q16/three-row fixes | MATCH (freeze diff = exactly those rows; entry at 3d054a98 digests to `6d27c129…` = Amendment C) |
| Q11 fix: old command prints 1, new prints 3 | MATCH (re-ran both greps on `rea-doctor-r98.txt`: 1 and 3) |
| Q16: 12.1.4 doctor-only; remaining versions probe-printed | MATCH (re-ran the six greps: 12.1.4 host-probes=0/doctor=17; 21.0.13 both=3; others probes≥1) |
| S506 re-open: pinned rev 12f6e09, http 200, 16650 bytes, sha `ce2d122b…`, byte-identical, quote count 1 | MATCH (re-fetched the URL live: http 200, 16650 bytes, sha `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`, cmp identical to committed body; receipt records quote_count=1) |
| S507 record hashes | MATCH (all three sha256s equal `controls/s507-reopen-r99.txt` and the entry's derivation rows) |
| Frozen v7 sha256 `59c9930a…` | MATCH (`59c9930ae864ce82…`; git blob `020a1471…` identical from 5d9b087 through 7e6edd4 — receipts' "v7 frozen 5d9b087" accurate) |
| v7 accepts 9/12 (c02 5/6, c14 4/6), both controls control-ok | MATCH (reproduced live: patched builder + v7 → c02 rc=0 `HOLDOUT98_CONTROL=control-ok` `accepted=5/6`; c14 rc=0 `control-ok` `accepted=4/6`) |
| Builder inputs: frozen v6 `_fixture` (c02), archive `1b76b4d` (c14), six vectors each | MATCH (`BASE_REV=1b76b4d…`, `fx._fixture`, `VECTORS` 6+6; digest asserted `6d27c129…`) |
| No-regression command shape: `forge_reach7.py --counter <v8> --profile c02` prints `C2_ACCEPTED=n/5` | MATCH (forge_reach7 accepts `--profile c02`, prints `C2_ACCEPTED=<n>/5` at line 232) |
| Vote key set = r98 `ReviewerBlind.json` keys | MATCH (`seat, role, candidate_sha256, decisions, notes, artifact_path, artifact_sha256`) |
| Q09 must not be n/a (entry carries 64-hex digests) | MATCH (entry contains 64-hex tokens; v7 `check_vote_notes` enforces it) |
| Census exit 0 at base | MATCH (`controls/census-round-start.log` ends `# rc=0 base=3d054a98…`) |
| Sourced docs exist (`corpus/lessons/round-98-verifier-spotcheck.md` §5, `critic-audit-6d27c129.md`) | MATCH (both present) |

**Verdict:** C2's frozen predicate, counting command, controls and kill rules are sound and reproduce (9/12 do-nothing confirmed live; separability from C1 holds). C1 as frozen is **not reachable** — F1 must be resolved by the L1 before the v8 freeze (amend the Surface-moved sentence to include the A2-style S505 correction, which is digest-neutral and needs no re-vote), or C1 dies as an honest miss.

Receipts copied to `.ufo/waves/round-99/w1/ReviewerClaimsR99/`: `v7-c14-donothing.log`, `v7-c14-junkrow.log`, `v7-c14-headerflip.log`, `v7-c14-landing-shape.log`, `c2repro-c02.log`, `c2repro-c14.log`, `s506-refetch.txt`.
