# R71W1GateQ13Q16 — Q13/Q16 pre-gate verification of the round-71 v6 candidate

PASS with two minor pre-gate repairs recommended — the required unguarded classes are named and reproduce live, the four frozen round-70 prose repairs land as registered, and no overcredit was found beyond two located prose slips (a dangling lessons pointer in the S052 row and an incomplete flag enumeration in the recheck header).

Scope: read-only. No lane writes (`git status --porcelain corpus/` empty after all probes; lane entry sha256 `778af93bac4cca16f8ad38e2af3cb4fd984a2054c65ad4dcba513f1f392ea3bf` identical before and after). All probes ran on a copy of `corpus/` under scratch; scratch deleted before return. No packages installed (Python 3 stdlib only; pacman pause respected).

## Targets and evidence

- v6 candidate: `corpus/knowledge/round-71-apk-axml-byte-evidence.md` (324 lines; sha256 above; `admission-status: candidate` at entry:12, README C05 unflipped — correct candidate state).
- Gate: `corpus/check_embedded_outputs.py` (sha256 `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8` — differs from round-70's `5f4241…` because C2's `CannotEvaluate`/exit-2 rework is in; expected, not a defect here).
- Inputs read: `reports/round-71/claims.md`, `reports/round-71/pre-registration.txt`, `corpus/QUALITY.md:25,28` (Q13, Q16), `.ufo/waves/round-70/w2/R70W2EntryMutants.md`, gate source, v6 entry.

### Baseline (scratch copy of the current candidate)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md
checked_blocks=24 problems=0        EXIT=0
```

Meets the frozen C1 gate floor (≥17 checked blocks, zero problems). Item-14 pins consistent: `readout.py` `92e347c3…8c13976`, `entry_checks.py` `2d4f25f6…29b1f9` match the entry's item-14 output.

### The three unguarded classes reproduce live (all exit 0 = SURVIVED)

| probe | mutation on scratch copy | gate result |
|---|---|---|
| FORGE (R70 M7 class) | lookalike block `$ python3 -B corpus/fixtures/apk-r65/echo71.py` + 2 fabricated `MATCH` lines, `echo71.py` created in-tree | `checked_blocks=25 problems=0`, EXIT=0 |
| ONEWAY (R70 M4 class) | delete item 1's embedded archive line (entry:28) | `checked_blocks=24 problems=0`, EXIT=0 |
| SUPERSET (R70 M5b class) | item 1 command `--fact archive` dropped → full 15-line dump | `checked_blocks=24 problems=0`, EXIT=0 |

Sanity control (same copy discipline): mutating one embedded byte (`"bytes": 947`→`946`) is DETECTED — `drift entry:28 embedded output line not in recheck stdout: {"bytes": 946, …}`, `problems=1`, EXIT=1. The three survivals are specific, not a degenerate always-pass gate.

Gate mechanism confirming why: `evaluate()` builds `stdout_set` and calls `drift(lines, stdout_set, lineno)` (`corpus/check_embedded_outputs.py:188-189`, `:153-155`) — embedded lines must appear in the declared command's stdout; extra stdout lines and missing embedded lines are unconstrained; `confined()`/`inside()` (`:79-100`) admit any in-tree script, so a foreign echo script satisfies the one-directional clause exactly.

### All three classes are named unguarded in the v6 Q13 row (entry:311)

> "**Unguarded clauses, named:** deleting an embedded output line is not detected (one-directional comparison); a corrupted flag whose output is a superset passes; and a forged block whose command is a different in-tree script that prints fabricated lines verbatim passes (the gate compares only the declared command's stdout; R70W2EntryMutants). The entry credits no verifier for these clauses."

Exact match to the frozen claims requirement ("Q13 must also name the surviving forged-block case (a different in-tree script prints fabricated lines)") and to R70W2EntryMutants' survivor classes M4, M5b, M7. The R70 M5a defect is repaired: the false parenthetical "(the readout degrades an unknown flag to its full dump)" is gone (`grep "degrades\|full dump"` → no match); the surviving sentence now states the accurate superset mechanism.

### The four frozen round-70 prose repairs verified against command stdout

1. **Item 11 (entry:120)** — describes `--spec-quotes` as printing "the snapshot file, the line number its first words start on, and the searched phrase itself". Verified: `--spec-quotes` prints exactly 6 MATCH lines in that shape (1 REA + 4 dex + 1 ResourceTypes = the 1+1+4 phrases item 11 names), e.g. `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;` — no raw snapshot line. The "complete set" claim for the derivation also holds: `derive_axml_anchors.py` prints 20 lines; the embedded item-11 block carries those same 20.
2. **Item 12 (entry:153)** — "output lines 16-18 of 20 print where each record layout sits in the snapshot … while the last two lines compare the central and local fixed-part widths". Verified against actual stdout: `--zip-layout` prints exactly 20 lines; line 16 = `MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399`, 17 = 4.3.12, 18 = 4.3.16; lines 19-20 = `MATCH central.fixed_part …` / `MATCH local.fixed_part …`.
3. **Observation (entry:283)** — literal-comparison credit bounded to items 12/17 and exactly five locators-only citations named: `readout.py:22`, `:76`, `:166`, `:211`, `:233-248` — matching the frozen list byte for byte. Cross-checked every `readout.py:N` citation in the entry (`:51-58`, `:76`, `:105`, `:155-168`, `:166`, `:203`, `:211`, `:233-248`, `:22`): each is either covered by item-12/17 printed literals or named locators-only.
4. **Q13** — see above.

### Overcredit sweep — no defect found in these checks

- item 2: "prints the four bytes at the offset it finds" ↔ `eocd signature bytes at offset 925: 504b0506 (4 bytes)` ✓
- item 14: "ten files under `corpus/`" ↔ `--pins` prints 10 sha256 lines ✓
- item 16: "every record" ↔ 3 records printed (all members of this fixture) ✓
- item 4 enum-value prose ↔ all six stated hex values printed as enum lines by item 11 ✓
- Reproduce "Exit 0 and 15 stdout lines" ↔ item 15 prints `readout stdout: 15 lines, sha256 507d79f8…` ✓
- item 13 bounds: keys-not-compared and generator-declaration scoping present; "One line per compared field, every line printed" ✓ (32 MATCH lines all printed)

## Findings (pre-gate repair recommendations)

1. **[minor, located] Dangling lessons pointer in the S052 source row (entry:8).** The row's anchor ends "…and recorded in `corpus/lessons/round-71.md` `## Gate`", but `corpus/lessons/round-71.md` does not exist — `corpus/lessons/` holds `round-1` … `round-70` only. The embedded-output gate does not check prose pointers, so nothing fires today; at admission the anchor would name a nonexistent file. Recommend: either create the round-71 lesson before adjudication (the claims already plan a lesson for proposal-1 mining) or drop the lessons clause from the S052 anchor.
2. **[minor, located] Recheck header omits item 15's flag (entry:10).** "the `entry_checks.py` flags named in items 2, 11-14 and 16-17" — item 15 runs `entry_checks.py --stdout-digest`, so the enumeration should include it (e.g. "items 2 and 11-17"). `Reproduce` (entry:323) already lists all eight flags correctly; only the header enumeration is incomplete.

## Residual risk / verification gaps

- Probes ran on a scratch copy of `corpus/`, not on a future lane tip; a wave-2 seat must re-run the baseline on the final measured tip (cheap: one gate invocation).
- I verified Q13/Q16 surfaces only; C1 coverage-K bookkeeping (README flip, vote files), C2 exit-2 classification and the counter are other seats' assignments, untouched here.
- The Observation's locator bound for `readout.py:105` (item 3's payload-offset formula) is covered only partially by item 12's printed literals (`lh_off + 30` and the `lh_off + 26/28` reads); judged defensible under the sentence's "compared only where items 12 and 17 print them" wording, flagged here for completeness, not as a defect.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W1GateQ13Q16/` deleted after this report was written.
