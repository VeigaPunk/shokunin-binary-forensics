GRADE: HOLDS — C1 coverage K hold inputs (corpus/live + corpus/fixtures byte identity) and holds, landed ab580698212258a55e43e9bb9bf6ac78c91eae2a

Seat RevengerR61-2.W3HoldInputsBytes (leaf; no delegation, no installs). Archives: `git archive --format=tar <commit> | tar -x` of cf02419276e5 (base), ab5806982122 (landed), plus 0b6ddf07f331, 0597e5336fd6, e0a4b0c4348e into /tmp/revenger-r61w3-W3HoldInputsBytes. Lane tree read-only; every run below in an extracted tree; no REA device, no bytecode/JavaScript execution, no chain, no credential read.

## Required harm check (OBSERVED, 2026-10-21)
1. `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --stat cf02419 ab58069 -- corpus/live corpus/fixtures` → no output, rc 0; `--name-status | wc -l` → 0.
2. Stronger than stat: `git rev-parse <c>:corpus/live` = `a35d30717a00250b0e8a884fd5ae402674609bea` at cf02419, e0a4b0c, 0b6ddf0, 0597e53 and ab58069; `:corpus/fixtures` = `c6287377454103866adea5b309850bf301279cc9` at all five. Identical tree objects ⇒ no modified, added, deleted or mode-changed path (inference from git tree identity, not from stat alone).
3. Independent sha256 of every file: 443 files (345 corpus/live, 98 corpus/fixtures) sorted and hashed in each archive; `diff base.hold.sha256 landed.hold.sha256` → identical.
4. The 29 files the two entries' `## Reproduce` blocks read (7 EVM fixture+truth+record triples, 6 JS fixture files, 2 JS records) hash identically: `diff inputs-base.sha256 inputs-landed.sha256` → empty.

## Holds (OBSERVED)
5. `python3 -B reports/round-61/measure.py /tmp/revenger-r61w3-W3HoldInputsBytes/base` → `K_HELD=4/14`, `K_HELD_BACKED=4/14`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, exit 0.
6. Same probe on landed → `K_HELD=6/14`, `K_HELD_BACKED=6/14`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, exit 0. No hold lost; the only corpus *code* changed is the two C2 verifier scripts, and both still pass their own self-tests on the landed tree.

## K admission inputs (OBSERVED)
7. README landed: 14 rows; status changes exactly C04/C09 `uncovered`→`held`; all 8 `knowledge/*.md` names resolve to files (probe's backed rule) ⇒ K_HELD_BACKED=6/14.
8. Both entry `## Reproduce` blocks extracted and run with cwd=landed: exit 0; stdout byte-identical to each `## Provenance` block (EVM 14 lines, JS 29 lines; `diff` empty); stderr 0 bytes. The Q11 values the entries cite for fixtures/records are executable on the held bytes, not asserted.
9. `git diff --numstat cf02419 ab58069 -- corpus/SOURCES.md` → `17 0`; S016–S027 all `opened 2026-10-21`; S016–S023, S026, S027 tier A and cited by the entries (S024 rejected-supersede, S025 tier C rejected; neither load-bearing). `--name-status` over `corpus/knowledge` shows only two `A` files — no existing entry edited.
10. Spot re-open of primary sources, access 2026-10-21 (URLs as recorded at `corpus/SOURCES.md:30-37`): S016 `instructions/__init__.py:55 EQ=0x14`, `:106 JUMPI=0x57`, `:109 JUMPDEST=0x5B`, `:125 PUSH4=0x63` and `runtime.py:29-30` PUSH-data sentence match; S017 PDF sha256 `d67c009c5d5a…77fa9` matches and §9.4.3 wording ("valid instruction boundaries … data portion of PUSH operations") matches; S018/S019/S020/S021/S022/S023 quotes found verbatim on the named pages (S023 line-wrapped in the HTML, wording exact).

## Non-falsifying observations (owned by sibling seats, not this item)
11. C09:99 kasegi `PROVINCE.md:25` anchor is that file's "Refuses" line, not the attributed scope; C09:88-90 `embedded_pattern_offsets [1, 9]` has no in-entry byte derivation (my own search: 9-byte pattern at 1..9, one occurrence); C04:39 says "a single exposed export" while each graph carries two `default`-named `exposes` edges. None of these changes the byte identity of any hold input; see sibling reports W3EvmCrossLaneCites, W3EvmR24SpanFix, W3JsLabelsDefault.

## Limits
- This item tests bytes and holds only; it does not re-adjudicate the entries' prose (other W3 seats) or C2 (separate claim).
- No producer was re-run (REA calls barred); identity is local bytes/digests, not producer origin (Q09 scope).

VERDICT: C1's hold inputs are bit-identical from claim base to landed and every hold passes; K_HELD_BACKED 4/14→6/14 is honest; the K-side harm conditions do not fire.

Installs: none.
