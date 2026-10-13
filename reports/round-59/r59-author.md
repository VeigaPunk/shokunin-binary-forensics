# r59 author report — named type key coverage extension (host: devin)

## Scope decision
The r59 LOG entry halted the **calibration** axis (malformed-UTF-16 refusal
prediction falsified; halt pending a newly declared criterion or operator
ruling). This leg deliberately does **not** re-tread that claim. Chosen route:
a distinct fixture-perturbation class on the **coverage** axis — a new
top-level *named* resource type key (`kind:"name"` at type level), a key kind
never scored in any prior authored fixture (all roots had `named_entries=0`).

## What ran (host: devin)
1. Authored `corpus/fixtures/pe-r59d/` via `build_fixture.py` (stdlib,
   deterministic): reuses r55 header bytes [0:512], sets resource-directory
   size field @220 = 320, emits root dir (named=1, id=2: `REVTEST`, 3, 14),
   name dirs, four language dirs, four data entries, name strings, payloads.
   r55 icon1/icon2/group payload bytes are reused byte-identical.
2. `npx -y rea-agents@6.4.0 inspect-pe-resources
   /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r59d/fixture.exe
   --format json` → exit 0, empty stderr, one producer call only.
3. `python3 .shokunin/revenger/corpus/live/runs/round-59/devin-author/verify.py`
   → exit 0, `PASS: 22 positive checks; 3/3 forged claims rejected`.

## Byte-exact evidence
- Fixture `corpus/fixtures/pe-r59d/fixture.exe`: SHA-256
  `99bebcf14c462075e63d6504c97a45267063f33e05f215c1235f89d666b5c0f3`, 1536 B.
  Source r55 SHA `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`.
- Evidence `ev_8efa2368e77f5370b305faea34e37042cb405f7c3583ed6b6c6ea7ba2dab6038`;
  saved stdout SHA `e04b14ef31ffb66e3534cbc6b008544076972a236249c86982b53c0720cc936e`;
  receipt/stdout/stderr in `corpus/live/runs/round-59/devin-author/`.
- Leaves 4/4 precision & recall (index 0 = named type `REVTEST`/id1/lang1033,
  payload @968/23 B sha `d069b384…91da6`; 1,2 = RT_ICON ids1/2 @832/@880/48 B,
  digests equal r55's; 3 = RT_GROUP_ICON `A😀B!` @928/34 B, digest equal r55's).
- Directories 7/7 byte-derived incl. root @512/40 (named1/id2); all
  entry_locations and name strings (REVTEST @812/16, `41003dd800de42002100`
  group name @800/12) match.
- icon_groups[0]: resource_index 3; images → candidates [[1],[2]],
  same-language [1,2], size_matches [true,true]; 2/2 links, zero false links —
  the opaque named-type leaf is never an icon candidate.
- coverage field: `complete`, examined_entries 11, resources 4.
- Forged claims rejected 3/3: REVTEST leaf as icon candidate; numeric type-id
  24 claim for the leaf; forged payload digest.

## Per-axis verdict claim
- coverage **improved**: first scored named type key at type level; first
  root `named_entries=1`; three-type root {name, 3, 14} byte-exact.
- depth **unchanged**: same three-level tree and group-relation semantics.
- calibration **unchanged** (guardrail): no validity/refusal claim made; the
  halted axis is untouched. Byte-oracle discipline retained.
- No axis regressed; claim is fixture-scoped only.

## UNKNOWNs
Named keys combined with arbitrary ids, malformed/overlong/duplicate names,
Windows loader behavior, icon decode/rendering, producer authentication,
native disassembler readiness, arbitrary/malformed PE correctness, whether REA
bounds-checks name strings beyond directory size.

## Boundaries
Author-run oracle, not independent review — a non-author reviewer lane remains
open. No commits, nothing outside `.shokunin/revenger/`, no existing
fixture/verifier modified, no verdicts marked in LOG/SCORECARD.
