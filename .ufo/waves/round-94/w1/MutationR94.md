# MutationR94 — round-94 attempt-1 scoped findings (mutation probe, C2 support)

One-per-leg mutation probe of the frozen v3 counter
`reports/round-94/c1_k_admit_counter3.py` (sha256
`de2815be742737cb66ffc5249aa61b25173cec138b8e4b958eb2e171175d799e`, byte-identical
before/after — frozen bytes untouched). Full detail: per-leg diffs, deciding runs and
logs in `.ufo/waves/round-94/w1/MutationR94/mutants.md` and
`.ufo/waves/round-94/w1/MutationR94/logs/`.

**Verdicts: 12 KILLED / 2 SURVIVED / 0 EQUIVALENT over the 14 legs.**

## Baseline (detector sanity)

- Real shipped `--self-test` of the pristine frozen path: `SELFTEST_C1V3=pass legs=14`, rc 0
  (matches the frozen control receipt on this host today).
- Honest admission-shaped fixture (built by the ORIGINAL module's `_fixture`):
  `C1_VERDICT=pass`, candidate digest `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`.
- Frozen `--rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431` run prints the SAME digest and
  `C1_VERDICT=fail` at the freeze tip — the vote-binding digest cross-check holds.

## Load-bearing map (what the kills prove)

- **Verdict-load-bearing legs (forgery passes outright when disabled):**
  - `C1_VOTES` — F11 forged-registry, F12 case-dup seat, F13 role mismatch, F14 empty
    artifact, F15 traversal, F17 vacuous n/a ALL pass with `C1_VERDICT=pass` when the leg
    is forced true. Six of the frozen twelve rest on this single leg.
  - `C1_SOURCES` — F19 stale-new-row passes outright: SOURCES.md is not digest-bound and
    no other leg reads it. (F16 body-sid stays rejected via the vote-digest backstop.)
- **Honest-path-load-bearing legs** (honest fixture flips when broken): C1_ROWS_TOTAL,
  C1_C15_HELD (also inverts the do-nothing control), C1_C15_CITES, C1_TRIO, C1_LINT,
  C1_EMBEDDED (the exit-2 no-`$`-blocks clause is load-bearing for the docs-only entry),
  C1_K_HELD_BACKED.
- **Diagnostic deepening over the digest-binding vote backstop** (mutant caught by the
  frozen leg-specific detector assertion while the class stays verdict-rejected):
  C1_ADMITTED (F10 dup-status changes the normalized bytes — values canonicalized, count
  not — so votes reject on digest mismatch), C1_ONLY_C15 (second-row move caught by
  K_HELD_BACKED only because the frozen class moves a held row; a non-held-row move has
  no backstop), C1_EMBED_NONVACUOUS (F18b caught by votes + EMBEDDED's `has_cmd_block`
  clause).

## Survivors — coverage findings (r95 candidates, per the claims' routing rule)

1. **C1_REGISTRY** (`if not reg_ok: return` gate dropped from `check_votes`): self-test
   fully green. F11 is still caught independently by the pinned-seat vote subcheck
   (defense-in-depth; failure reason shifts to `seat not in pinned registry: 'FabA'`).
   Gap: a **registry-only forgery** (members map altered, votes all from pinned seats)
   has no frozen class, passes v3 under the mutant, and the dropped gate is its only
   enforcement point. No frozen test kills the gate's removal.
2. **C1_QUOTES** (`legs["C1_QUOTES"] = True`): self-test fully green; do-nothing still
   fails overall (only the `C1_QUOTES=pass` line changes). Gap: **no forged-receipt
   class** (stale `fetched_at`, quote-not-in-body, wrong `fetch_sha256`/span). The leg
   does real honest-path work (fails on the base tree) but the battery never forges
   receipts, so nothing kills its removal.

Neither survivor is an exploitable hole in the frozen twelve; both are unrouted forgery
shapes with receipts in `logs/`, routable to r95 without touching frozen bytes.

## Bounds compliance

Writes confined to `.ufo/waves/round-94/w1/MutationR94/` + scratch
(`/fast/scratch/hyaku/revenger-r94/MutationR94`, deleted on exit, receipts copied first).
No lane file, no git/jj write, no sibling dir, no sysctl, no sudo, no installs, no
subagent, no network. Mutants existed only in scratch. Restoration: `cmp` clean,
sha256 above; frozen self-test still green after the probe.
