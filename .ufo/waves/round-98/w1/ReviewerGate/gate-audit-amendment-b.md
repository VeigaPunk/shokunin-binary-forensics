# ReviewerGate — gate-audit-amendment-b.md (revenger round 98, wave w1)

Seat: **ReviewerGate** (role: reviewer). Candidate re-audited after
**Amendment B** (lane commit `0146c0a`, diff base `cf8a9d4`):
`corpus/knowledge/round-98-rea-host-readiness.md`.

Normalized vote-binding digest, recomputed by me with the v6 `digest()` rule
(entry text with every `admission-status` line normalized to
`admission-status: candidate`; the file's only such line already reads
`admission-status: candidate`):

```
raw sha256 = digest() = 73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7
```

Equal to the Amendment B digest named by the L1. My prior vote (digest
`1ea9260c…`) is superseded and kept by the L1 in
`.ufo/waves/round-98/w1/superseded-votes-digest-1ea9260c/`.

## What Amendment B changed (verified from `git diff cf8a9d4 0146c0a -- <entry>`)

1. **Route-table clause reworded** (ZIP inventory row): "Hopper was absent
   during this run." → "Doctor reported Hopper missing the same day (record
   1)." — the new wording claims only what the record shows: the doctor record
   (record 1 of the entry's list = `rea-doctor-r98.txt`) reports
   `hopper` `missing_analysis_engine`, and both records are dated 2026-11-05
   (file mtimes 17:46/17:47; digests unchanged: `fb9a4824…` doctor,
   `c373f656…` inspect — re-run byte-equal).
2. **Observation clause reworded**: "at a time when doctor reported Hopper
   missing" → "on the same day that doctor reported Hopper missing" — honest
   weakening; the saved records do not establish sub-day ordering, and the new
   sentence no longer claims it.
3. **Derivation table gained 3 rows** (all re-run by me from the lane root;
   every recorded output matches):
   - ghidra scope checks healthy:
     `sed -n '/^scope_checks/,/^informational_checks/p' …rea-doctor-r98.txt | grep -A1 '^  - name: ghidra' | grep -c '    ok: true'`
     → `8` (of 8 ghidra-named scope checks; matches my per-block parse of the
     24 checks).
   - installation paths: `grep -c '^    paths\[3\]: ' …rea-doctor-r98.txt`
     → `1` and `grep -c '^    state: multiple' …rea-doctor-r98.txt` → `1`
     (the record line carries the three `fnm_multishells` paths, consistent
     with the CLI-launcher row's "three such installation paths").
   - S506 body length: `wc -c < reports/round-98/quote-receipts/raw/S506.body`
     → `16650` (digest row now carries no length clause, so Q14's
     hex-with-byte-count shape stays absent).
4. **`## §Q-map` appended**: a 17-row table mapping every Q id to a decision
   and the entry evidence/boundary.

Unchanged and still verified from my first audit (bytes identical in this
diff): both `source:` lines with exact anchors, `verified-at: 2026-11-05`,
`recheck:`, `coverage-map: C14`, `admission-status: candidate`; S506 body
digest `ce2d122b…` and its byte-identical re-fetch (HTTP 200, 2026-11-05);
all other derivation rows (11/13 scope checks, 10/11/3 classes, 14
registration pairs, CLI 6.7.0, `ev_0ef6c8…`, `status: completed`, sizes
2964/84/16160, fixture digest `857989f5…`, record digests `94eaa6ff…`
`fb9a4824…` `c373f656…`); truth.json round-2 pinning (`5c9fb20`).

## §Q-map cross-check (my independent decisions vs the entry's map)

| Q | entry's §Q-map | my decision | agree |
|---|---|---|---|
| Q01 | PASS | PASS | yes |
| Q02 | PASS | PASS | yes |
| Q03 | PASS | PASS | yes |
| Q04 | PASS | PASS | yes |
| Q05 | PASS | PASS | yes |
| Q06 | n/a | n/a | yes |
| Q07 | n/a | n/a | yes |
| Q08 | n/a | n/a | yes |
| Q09 | PASS | PASS | yes |
| Q10 | PASS | PASS | yes |
| Q11 | PASS | PASS | yes |
| Q12 | n/a | n/a | yes |
| Q13 | n/a | n/a | yes |
| Q14 | n/a | n/a | yes |
| Q15 | n/a | n/a | yes |
| Q16 | PASS | PASS | yes |
| Q17 | n/a | n/a | yes |

The entry's §Q-map agrees with my independent audit on all 17 decisions; zero
criteria fail. The Amendment B hunks introduce no new unsupported claim: both
reworded clauses narrow what is asserted, and each new derivation row carries
its command and recorded output (Q11/Q16 duties re-checked on the new rows).

## Remaining uncertainties

- Unchanged from the superseded audit: the S507 registry-row anchor's
  "1-based bytes 1-41" for the doctor's first two lines measures 42 bytes
  1-based-inclusive (the dispatch's own `head -c 41` recipe matches the
  stated count). Anchor-only, not load-bearing in the entry text; not gateable
  under any Q id. Not affected by Amendment B.

## Tooling

No tools installed or upgraded. Everything ran on host python3/git/coreutils
over committed bytes plus one read-only HTTP GET of the pinned S506 URL. No
writes outside my wave dir, the vote file, my findings file and scratch
`/fast/scratch/hyaku/revenger-r98/ReviewerGate/`.
