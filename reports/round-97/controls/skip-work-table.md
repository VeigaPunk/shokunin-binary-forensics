# Skip-work controls — round 97 (paper table)

considerthese/2026-11-05.md proposal 1, implemented as a table. Each control
prints the counter verdict-line format (`C1_VERDICT=pass|fail`,
`C1_K_HELD_BACKED=n/15`) so the L1 can score them with the battery harness
unchanged. Controls live under `reports/round-97/controls/skip-work/`.

| control | claim | expected v6 verdict or count | reason | predicate it tests | observed value |
|---|---|---|---|---|---|
| S-A do-nothing: base archive (git archive 7d380ce corpus reports .ufo, copied to scratch) with no change | C1 | `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15` | Without the admission-status flip and the README/SOURCES changes, the C02 row is not held; K stays 8.0. | C1 do-nothing control (claims.md: a v6 that passes the base tree is wrong) | Observed v5: `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15`, only failing leg `C1_SOURCES=fail` — copied from `reports/round-97/controls/c1-do-nothing-v5.log` |
| S-B always-pass stub: `stub_always_pass.py` prints `C1_VERDICT=pass` / `C1_K_HELD_BACKED=13/15` with no legs | C2 (+ C1 claim line) | 19/19 accepted; would meet C2 target 0/19 only if inverted | The battery counts accepted deltas (counter prints `pass`); a stub that always passes is accepted on every vector, i.e. 19/19 accepted — the exact opposite of 0/19. Inverting the count (19/19 rejected) is not a gain. | C2 frozen predicate (claims.md §C2: delta accepted when counter prints `C1_VERDICT=pass`) | Observed: `C1_VERDICT=pass`, `C1_K_HELD_BACKED=13/15`, rc=0 |
| S-C always-fail stub: `stub_always_fail.py` prints `C1_VERDICT=fail` with no legs | C2 | 0/19 accepted | A refuse-everything counter rejects all 19 vectors, but it also rejects the landing tree (honest candidate), so the positive control fails and the battery's stub check rejects it. | C2 positive control (claims.md §C2: landing tree accepted by v6; blanket-refusing stub rejected by the battery's stub check) | Observed: `C1_VERDICT=fail`, rc=0 |
| S-D id-edited copy: base archive copy with candidate entry `admission-status: candidate -> admitted` (digest stays 2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923 under normalization), WITHOUT changing README C02 or any SOURCES used-by | C1 | `C1_VERDICT=fail`; failing legs `C1_C02_HELD`, `C1_ONLY_C02` | Flipping admission alone does not hold the coverage row: the README C02 cell still says `partial`, so only-C02 and held legs fail. Admission without the row move is not a gain. | C1 frozen predicate (claims.md §C1: C02 held only when every v5 leg passes AND the used-by exclusivity leg accepts the census form for a named-exactly-once entry) | Observed: (record only — flip applied in scratch, v6 not run per freeze order) |
| S-E hand-fit lookup table: table mapping the 19 vector NAMES to fail | C2 | Would reach 19/19 rejected if applied — must NOT be accepted | The frozen predicate is a rule about bytes, not names: a name-keyed lookup is not a counter over tree bytes, cannot reject a renamed/reserialized vector, and would not fail the positive control on the landing tree. | C2 frozen predicate (claims.md §C2: "a delta counts as accepted when the counter prints `C1_VERDICT=pass` on the tree carrying that delta") and C1 frozen predicate (claims.md §C1: "one sentence, same in the counter") | — |
| S-F count audit: `count_summary.py` reads `.ufo/waves/round-96/w1/CriticR96/receipts/summary.json`, prints accepted count and list | C2 | 14/19 accepted | The committed summary holds 14 `observed_verdict=pass` rows, not the 13 stated in the r96 SCORECARD/lesson — a recorded mismatch, counted from committed bytes. | C2 do-nothing control (claims.md §C2: frozen v5 accepts 14/19; the r96 text said 13, a recorded mismatch) | Observed: `accepted 14/19`, accepted_list FG01,FG02,FG03,FG04,FG05,FG06,FG07,FG08,FG09,FG10,FG11,FG12,FG15,FG19, rc=0 — logged to `reports/round-97/controls/c2-count-audit.log` |

## Why the battery cannot count S-B or S-E as gains

- S-B (always-pass): the battery counts `C1_VERDICT=pass` deltas as accepted. An
  always-pass stub gives 19/19 accepted, not 0/19. Reading its output backwards
  (19/19 rejected) inverts the frozen predicate and is not a gain.
- S-C (always-fail) fails the positive control (landing tree must be accepted),
  so the battery's stub check rejects it; 0/19 rejected without the positive
  control is not a gain (claims.md §C2).
- S-E (name lookup): the frozen predicate is a rule about bytes, not names
  (claims.md §C2, §C1). A name table does not examine tree bytes, does not
  transfer to byte-different vectors, and must not be accepted.
