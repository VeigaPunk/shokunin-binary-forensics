FAIL — Q13 on the landed candidate (`17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, entry sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`): `corpus/knowledge/round-70-apk-axml-byte-evidence.md:282` credits items 12 and 17 with comparing "the literals they [the `readout.py:N` citations] concern", but at least five of the ten cited literals are in neither command's closed comparison table, and a falsified quote of three of them (`entry:39`, `entry:72`, `entry:86`) passes the entry's entire verification suite — `checked_blocks=24 problems=0`, `LINT_*=0`. The Q13 row (`entry:310`) names two unguarded clauses and not this one.

## Evidence base (no lane byte written or mutated)

- Target read from the landed commit only: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md | sha256sum` → `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`.
- Scratch tree: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-R70W2GateQ13`.
- Frozen scripts in the extraction match the entry's item-14 pins: `readout.py` `92e347c3…c13976`, `entry_checks.py` `2d4f25f6…29b1f9`, `derive_axml_anchors.py` `74d4c0d9…a83aa`.
- Baseline, from the scratch root: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0` (exit 0).
- Independent bidirectional re-derivation of every block (own parser, not the gate's): **24/24 blocks, `extra=0 missing=0`, all `rc=0`** — every embedded line is reproduced exactly and no command prints anything the entry omits (so item 11's "the output below is the complete set", `entry:119`, holds on these bytes: 20 printed lines = 20 embedded).

## What the Q13 row gets right — mutation matrix (all on scratch copies)

| mutant | mutation | observed | verdict |
|---|---|---|---|
| M1 | delete embedded line `MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399` (`entry:171`) | `checked_blocks=24 problems=0`, exit 0 | undetected — **matches** the row's named clause "deleting an embedded output line is not detected (the comparison is one-directional)" |
| M2 | corrupt a flag whose output is a superset: `--fact eocd` → `--facts eocd` (`entry:33`) | `checked_blocks=24 problems=0`, exit 0; `readout.py --facts eocd` prints the 15-line full dump | undetected — **matches** the row's named clause "(the readout degrades an unknown flag to its full dump)" |
| M3 | edit one `MATCH` line: `MATCH central.local_header_offset: spec offset 42,` → `spec offset 43,` (`entry:165`) | `drift entry:165 embedded output line not in recheck stdout: MATCH central.local_header_offset: spec offset 43, readout.py literal \`u32(apk, cursor + 42)\` present=True` / `checked_blocks=24 problems=1`, exit 1 | detected — **matches** the credit "the `MATCH`/`MISMATCH` lines are credited only for the comparisons each prints" |
| M4 | reorder two embedded lines (`entry:174`/`:175`) | `checked_blocks=24 problems=0`, exit 0 | undetected; *not* named, but the credited clause is set membership ("every embedded line appears in its command's stdout", `entry:9`), so no credit is over-broad — advisory only |
| M5 | corrupt a flag *value*: `--fact eocd` → `--fact eoc` | `drift entry:34 embedded output line not in recheck stdout: {"cd_end_equals_eocd_offset": true, …}`, `problems=1` | detected — the row's clause is correctly qualified ("… **if its output is a superset**") |
| M6 | exit-status probe (Q05-row credit, checked because it is a verifier credit): scratch `readout.py` exits 7 only on the full dump | `drift entry:181 command exited 1: … --oracle` / `drift entry:225 … sha256 92e347c3… readout.py` / `drift entry:237 command exited 1: … --stdout-digest` / `problems=3`, exit 1 | detected — the `Reproduce: Exit 0` credit at `entry:302` is real |

So the row's two *named* unguarded clauses and its bounded `MATCH` credit are accurate on these bytes. The FAIL is not about them.

## The defect — `entry:282` over-credits items 12 and 17

Exact text (`entry:282`, Observation bullet): "… the `readout.py:N` line citations are source locators checked by reading the file, **and the literals they concern are compared in items 12 and 17**."

What items 12 and 17 actually compare is a closed list, not the citation set:
- `corpus/fixtures/apk-r65/entry_checks.py:67-80` (`READOUT_USES`), `:199-215` (`AXML_USES`), `:219-249` (`axml_layout` literal templates) — twelve ZIP offsets, five string-pool offsets, seven attrExt offsets, six attribute offsets, plus `cursor + 46` / `lh_off + 30`.
- The cited literals absent from both tables (`grep -c` over `entry_checks.py`): `strings[ans]` → **0**, `flags & 0x100` → **0**, `NO_INDEX` → **0**, `u32(dex` → **0**; `b"PK\x05\x06"` occurs only as entry_checks' *own* signature search (`entry_checks.py:118`, `:255`), never as a compared literal. So at least `readout.py:76`, `:166`, `:211`, `:22` and `:233-248` — five of the ten citations — are not compared in items 12 or 17, and the formula texts at `:105` and `:203` are only compared through their components.

Demonstration that the clause is unguarded end to end — falsify the entry's quote of a cited literal, then run the entry's own two registered checks on the copy:

1. `entry:39` (`readout.py:105`): `` `payload_offset = local_header_offset + 30 + name_length + extra_length` `` → `` `… + 999 + …` `` (source line is `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`).
2. `entry:72` (`readout.py:166`): `` `flags & 0x100` `` → `` `flags & 0x200` ``.
3. `entry:86` (`readout.py:211`): `` `strings[ans]` `` → `` `strings[ans + 1]` ``.

Observed for each (same bytes otherwise):

```
$ python3 -B corpus/check_embedded_outputs.py --entry m7.md
checked_blocks=24 problems=0          # gate_exit=0
$ python3 -B corpus/lint_entry.py --entry m7.md
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0                          # lint_exit=0
```

(m6 and m8 are identical: `problems=0`, all four `LINT_*=0`.) No command in the entry reads the entry's prose against `readout.py`, and items 12/17 read only their tables, so a false quote of a cited literal survives the whole suite. That is the M22 class Q13 exists for (`corpus/lessons/round-61.md:38`: "a verifier clause had no in-script negative, so deleting it was invisible to the script's own run") — here the *credit* is present and the negative is absent.

The entry's own Q11 row (`entry:308`) states the honest version ("`readout.py:N` citations are labeled source locators"); `entry:282` contradicts it, and the Q13 row (`entry:310`) does not name the gap.

**Smallest safe correction** (two edits, no value changes):

- `entry:282`, replace the trailing clause with: "the `readout.py:N` line citations are source locators checked by reading the file; only the field-offset literals that items 12 and 17 print are machine-compared (the `u16`/`u32` offsets, `cursor + 46`, `lh_off + 30`, and the `base`/`aoff` offsets). The remaining cited literals — `b"PK\x05\x06"` at `readout.py:76`, the `payload_offset` expression at `:105`, `flags & 0x100` at `:166`, the `aoff` expression at `:203`, `strings[ans]` at `:211`, `NO_INDEX` at `:22` and the dex-header reads at `:233-248` — are **unguarded** by those two commands: a false quote of any of them changes no output of items 12 or 17, and the embedded-output gate does not compare entry prose with the script (the script's own bytes are pinned in item 14, but the entry's quote of them is not)."
- `entry:310`, extend the named-unguarded list with: "a false quote of a cited `readout.py:N` literal outside items 12/17's printed comparisons is not detected by any command in this entry."

## Adjacent defect (not my criterion — for the Q11 seat, not a Q13 basis)

`entry:152` says "the last three lines print where each record layout sits in the snapshot". In `entry_checks.py --zip-layout` the three APPNOTE lines are output lines **16-18 of 20**; the last three are `APPNOTE 4.3.16`, `central.fixed_part`, `local.fixed_part`:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | nl -ba | sed -n '16,20p'
    16  MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
    17  MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
    18  MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
    19  MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
    20  MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
```

## Wave-1 cross-check (consulted after the verdict above was formed)

`.ufo/waves/round-70/w1/R70W1PreQ04Q13.md` scored Q13 PASS on the earlier bytes `aa1842fac199…` (22 blocks). Its mutant **M-G** (`+ 30 +` → `+ 999 +` in item-3 prose) produced exactly the survivor I reproduce at `entry:39`, and wave 1 set it aside: "gate exit 0 — prose is outside the credited clause, and the entry does not credit the gate for it". On the landed bytes that premise no longer holds: `entry:282` does credit items 12/17 with comparing the cited literals, so the survivor is now inside a credited clause. My verdict was reached from the landed bytes before this file was opened; it is not derived from it.

## Scope, tools, cleanup

- Decision on Q13 only; no other criterion judged, no lane file read as a target from the working tree, no mutation outside `/tmp`.
- Tools installed/upgraded: none (Python 3 stdlib + existing `git`/`tar` only; pacman paused and untouched).
- Scratch `/tmp/revenger-r70-R70W2GateQ13` deleted before return.

## Kill-rule consequence (recorded, not decided by this seat)

Per `reports/round-70/claims.md` §C1 kill rule, this FAIL carries a located defect (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:282`, with the commands and outputs above): the C05 row stays `uncovered`, the header becomes `admission-status: rejected`, and C1 is falsified — honest stop — unless the L1 shows by command that the cited defect is absent from the landed bytes and a second fresh reviewer concurs in writing.
