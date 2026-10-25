# R69CriticC7Claim — C1's C7 conjunct (instrument hold)

**FALSIFIED** — with the pinned counter and the *unmodified* C7 gate, a v4 entry that embeds a
**corrupted derivation sha256 line** still reads `C7_V4_CLEAN=yes`, `HOLDS_OK_V6=yes`,
`C7_SELFTEST=pass`, exit `0`; the only change needed is **one leading space** on the `$` line
(builder-controlled entry bytes). Separately, the pinned counter cannot run at all once
`corpus/q15_tree_id_check.py` exists (`NameError: name 'run' is not defined`).

Axes touched: **calibration** (primary — both defects sit in the C7/Q15 instrument), **coverage**
(C1's `C7_V4_CLEAN=yes` conjunct carries no anti-drift force).

I did not edit the lane tree; all work is in `/tmp/revenger-r69-c7critic/` (deleted before return).
No V-label, marker-presence rule or gate source was proposed for change; the C7 L0 stays as it is.

## 1. Counter pin — MATCHES

```sh
sha256sum reports/round-69/measure.py            # bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377
grep -n bca74e6d reports/round-69/claims.md:6    # same 64 hex chars
```
`corpus/check_embedded_outputs.py` = `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`
(no pin exists for it; it is measured from the archived tree by the counter).
`reports/round-69/measure-before.log` = `e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29`.

Receipt is genuine and reproducible: `git archive 222a7a7 corpus | tar -x -C <tmp>` then
`python3 -B reports/round-69/measure.py <tmp>` reproduces `measure-before.log` **byte-identically**,
exit `0`.

## 2. A1 — mutation-free drift escape (the falsification)

Mechanism, `corpus/check_embedded_outputs.py:57`:
```python
if in_fence and line.startswith("$ "):     # column 0 only — an indented `$ cmd` is never a block
```
`evaluate` therefore silently skips the block (`checked_blocks` drops 17→16); nothing reports the
omission, so `problems=0` and `exit 0`.

Setup (scratch copy of `corpus/`; v4 entry bytes only):
1. replace the real derivation line `sha256 56b88bc4…c56f ResourceTypes.h` with `sha256 000…0 ResourceTypes.h`;
2. prefix the `$ python3 -B corpus/derive_axml_anchors.py` line with **one space**.

| tree | counter label | exit |
|---|---|---|
| same corruption, `$` at column 0 | `C7_V4_CLEAN=no` | 0 |
| same corruption, `$` indented by 1 space | **`C7_V4_CLEAN=yes`** | 0 |

Gate directly: `checked_blocks=17 problems=1` (col 0) vs `checked_blocks=16 problems=0` (indented).

Airtight variant — with the derive output made additive (plain `enum SYM : N` line plus a separate
`= 0x…` line, so the byte-frozen round-68 candidate is clean again and `HOLDS_OK_V6` can be `yes`):

| tree | C7_V4_CLEAN | HOLDS_OK_V6 | C7_SELFTEST | C7_RED_ON_R65 | MUTANT_ATTR | NEG_SPOOF_ATTR | exit |
|---|---|---|---|---|---|---|---|
| additive output, v4 untouched | yes | **yes** | pass | yes | 1/1 | 0/1 | 0 |
| additive output + corrupted sha256 + 1 space | **yes** | **yes** | pass | yes | 1/1 | 0/1 | 0 |
| additive output + corrupted sha256, col 0 | no | yes | pass | yes | 1/1 | 0/1 | 0 |

So `C7_V4_CLEAN=yes` (and the whole `HOLDS_OK_V6` aggregate) is satisfiable with a stale quoted
sha256 in the v4 entry — the predicate does **not** establish verbatim embedded output.

## 3. A2/A3 — the conjunct is vacuous without any mutation

Same unmodified gate, no indent:
- **A2** entry quoting **zero** output lines after every `$ cmd` → `checked_blocks=17 problems=0`, exit 0.
- **A3** entry quoting **1 of the 20** derivation lines → `checked_blocks=17 problems=0`, exit 0.
  (Drift is subset membership, `check_embedded_outputs.py:83-86` + `:105`; extra stdout lines, e.g.
  the additive-output variant's 28 lines, are invisible.)

Consequence for C1 item 2 ("re-embeds the new 20-line derivation output"): that sentence is not
covered by the C7 conjunct at all — only by the Q-seat review of item 11.

## 4. A4 — unconditional exit 1 / exit 0 (these ARE closed)

- always exit 1 → `C7_V4_CLEAN=no` → C1 predicate fails. Closed.
- always exit 0 on `--entry` → `C7_RED_ON_R65_CANDIDATE=no` → `HOLDS_OK_V5=no` → counter exit 1. Closed.
- non-python `$ cmd` → `exit 2 could-not-evaluate` (`:76`) → `C7_V4_CLEAN=no`. Closed (fails closed).

## 5. A5 — pinned counter is NOT evaluable on the tree it must measure (blocker)

`reports/round-69/measure.py:158` calls `run(...)`, which is defined at `:187` — i.e. **after** the
call, at module level. On any tree carrying `corpus/q15_tree_id_check.py`:

```
File ".../reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
```
→ exit `1`; `Q15_PRESENT=yes` prints, then **nothing else**: no
`Q15_SELFTEST`/`Q15_FALSE_KILLED`/`Q15_RESTATE_OK`, no `C7_*`, no `HOLDS_OK*`. The base tree has no checker,
so the `if q15_check.is_file():` branch is skipped and the before-log reproduces — which is exactly
why the receipt looks healthy.

Consequences, all on the frozen file whose sha256 equals the pin (so this is *not* a local edit):
1. `measure-after.log` cannot be produced by the pinned counter for any tree where C2's
   `Q15_PRESENT=yes` and the checker coexist → C1's "counter's exit code is 0" and C2's
   `Q15_SELFTEST=pass` are unreachable.
2. Any after-log carrying `Q15_*` **and** `C7_*`/`HOLDS_OK*` lines was not produced by the pinned
   sha256 — that is a counter substitution, i.e. the "counter edits" attack succeeds by necessity,
   not by choice. Treat such a log as false provenance until the file is re-pinned.

## 6. A6 — false provenance sentence in the frozen contract (D1 class, new instance)

`reports/round-69/claims.md:166`: "The counter's sha256 is pinned above **and in
`measure-before.log`**". `grep -c sha256 reports/round-69/measure-before.log` → `0`. The receipt
carries no sha256 token; the sentence is an identity asserted against contradicting bytes — the
same class D1/M46/M47 that Q15 is meant to catch, present in Q15's own claim surface.

## 7. Build-side finding that trips the claims' own void list

`C7_V3_CLEAN=no` on the final-shaped tree (q15 checker removed so the counter can run):

```
C7_V3_CLEAN=no   C7_V4_CLEAN=yes   HOLDS_OK=yes V2=yes V3=yes V4=yes V5=yes V6=no
K_HELD_BACKED=8/14  K_HELD_BACKED_STRICT=8/14  HOLDS_C2_V4=no  Q15_PRESENT=yes
```
Cause: `corpus/knowledge/round-68-apk-axml-byte-evidence.md` is byte-identical to `222a7a7`
(`ef7f0232edb74bae…` both sides), but the shared `corpus/derive_axml_anchors.py:124` now prints
`enum RES_XML_TYPE : 241 = 0x0003` where the round-68 entry quotes `enum RES_XML_TYPE : 241`
(7 drift lines, `checked_blocks=17 problems=7`). The void list says "`HOLDS_OK_V4`/`HOLDS_OK_V5`/
`HOLDS_OK_V6` not yes" → **void**, and it also collides with "the round-65, round-67 and round-68
candidates keep every byte" in spirit: the bytes are kept, but the instrument they were verified
against was reformatted.

## 8. Smallest safe corrections (no verdict changes, no V-label edits)

1. **Gate reachability (A1/A2/A3)** — the `$` line is the only block opener. Do not touch the
   marker or the V-labels; make omission *loud*: in `evaluate`, when a fenced block's body contains
   lines but no `$ ` opener was parsed at column 0, or when a parsed block has zero output lines,
   add `problems += [f"unchecked block entry:{lineno} ..."]`. Deterministic, ~6 lines, fails closed,
   keeps the frozen exit contract. (This is a gate source change — admissible only if the round
   re-pins; it is not a marker-presence replacement.)
2. **Counter (A5)** — do not edit the pinned file after measurement. Re-declare in a *new* claims
   revision before any after-run: move the `def run` block above the Q15 block (or hoist the Q15
   block below it), re-pin the sha256, and say in the receipt that the old pin certified a
   non-evaluable counter.
3. **Provenance (A6)** — drop "and in `measure-before.log`" from `claims.md:166`, or commit the pin
   into the receipt. Q15 must then be able to fail on this sentence; it currently cannot (it is
   prose in the claims file, not a scanned identity).
4. **r68 regression (A7)** — make the extension additive: emit the round-68-format line
   `enum {name} : {line}` unchanged, then a separate `enum {name} : {line} = {value}` line
   (`derive_axml_anchors.py:124`). Verified in scratch: `C7_V3_CLEAN=yes`, `C7_V4_CLEAN=yes`,
   `HOLDS_OK_V6=yes`, exit 0, round-68 bytes untouched, derivation grows to 28 lines — which then
   also exposes the subset hole (A3) but breaks nothing.

## 9. Supporting identities checked

- `corpus/derive_axml_anchors.py` = `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`
  = the sha pinned in the v4 entry's `source: S047` line. Match.
- v4 entry: `admission-status: candidate` (README not flipped) — consistent with build state.
- Real gate on the build bytes: `round-65 exit 1 problems 1`, `round-67 exit 0 problems 0`,
  `round-68 exit 1 problems 7`, `round-69 exit 0 problems 0 (17 blocks)`.

No host tools installed or upgraded; nothing required beyond python3 stdlib.
