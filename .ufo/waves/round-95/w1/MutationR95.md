# MutationR95 — seat report (revenger round-95, w1)

Per-leg mutant audit of the frozen v4 counter
(`reports/round-95/c1_k_admit_counter4.py` @ `6e0bf15fed58f357b7fa0c881371ac7616a116f7`).
Full detail, anchor table and verbatim self-test tails:
`.ufo/waves/round-95/w1/MutationR95/mutants.md` + `receipts/` (17 leg logs + baseline).

## Result: 11 KILLED / 6 SURVIVED (baseline `SELFTEST_C1V4=pass legs=24`, rc=0, green before any mutant ran)

KILLED: C1_C10_HELD (via the do-nothing control), C1_C10_CITES (V07/V08),
C1_ONLY_C10 (ONLY-C10-second-row), C1_ADMITTED (H1/F10), C1_REGISTRY (V03 +
M6-forged-registry-seat), C1_VOTES (V04/V18/F17/F20/F12/F13/F15), C1_RECEIPTS
(V10/V27), C1_PYCACHE (M5), C1_EMBED_NONVACUOUS (F18/F18b), C1_SIDS (V19/F16),
C1_SOURCES (F19).

SURVIVED (coverage findings — no isolating forged delta exists for these legs;
route to r96, frozen bytes untouched): C1_ROWS_TOTAL, C1_TRIO, C1_LINT,
C1_EMBEDDED, C1_QUOTES, C1_K_HELD_BACKED.

## Headline: the M6 close holds — C1_REGISTRY mutant DIES on v4

```
rc=1
SELFTEST_C1V4=fail legs=24
SELFTEST FAIL: V03-dup-json-keys-registry: expected fail on C1_REGISTRY, got rc=0 failing=[]
SELFTEST FAIL: M6-forged-registry-seat: expected fail on C1_REGISTRY, got rc=0 failing=[]
```

The r94 finding was that the registry check had no own leg, so the drop-the-gate
mutant survived. v4 splits `C1_REGISTRY` out and the same mutation is now
self-test-fatal on both registry-class vectors. This supports C2's
`MUTANT_V4_REGISTRY_KILLED` predicate from the mutation side.

## Notes for the integrator

- Method: scratch clone of the lane at the freeze commit (clone toplevel asserted;
  `LANE` resolves inside the clone, so the counter's git reads never touch the real
  lane), one line per leg mutated to constant pass, `--self-test` per mutant with
  `HYAKU_SCRATCH` pointed into my scratch. Every Python call `python3 -B`.
- Killed legs with `got rc=0 failing=[]` (REGISTRY, VOTES×7, RECEIPTS×2, PYCACHE,
  SOURCES) are load-bearing with zero redundancy: muting them lets the forged tree
  pass the WHOLE counter.
- The remaining killed legs die on the per-leg `EXPECT_FAIL` assertion even though
  the overall verdict would still fail elsewhere (entry-byte deltas shift the
  normalized digest and trip `C1_VOTES` binding). The leg assertion is load-bearing,
  not cosmetic.
- `C1_C10_HELD` is the only leg backstopped by the do-nothing control.
- Restoration evidence: lane counter sha256 `fbbec26c…` and lane entry sha256
  `476edc36…` identical before/after the whole run; mutants lived only in
  `/fast/scratch/hyaku/revenger-r95/MutationR95/` (deleted at exit, receipts copied
  to the wave dir first). No lane file edited; no votes/claims bytes touched.
