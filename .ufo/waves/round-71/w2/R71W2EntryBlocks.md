verdict: PASS-FLOOR — every one of the 24 embedded `$` command blocks in the v6 entry re-runs at tip and reprints its embedded output exactly (`checked_blocks=24 problems=0`, exit 0); an independent stricter comparator finds no missing, extra, reordered or duplicated line and no run-to-run drift. Gate floor met; this is not an admission and no Q decision is recorded here.

# R71W2EntryBlocks — v6 embedded-command re-run at final tip

Seat: `R71W2EntryBlocks` (leaf, executor, round-71 wave 2). Axes: coverage, operability. Scratch: `/fast/scratch/hyaku/revenger-r71/R71W2EntryBlocks/` (removed after this report was written; every receipt line below is copied from it).

## 1. Tip identity and measured bytes

```
$ git -C revenger-shokunin rev-parse HEAD
c6e284c6583fa3502754361f411b66646880ba02          # tree cfae4cfc2cc8348f86df9de2662e27afeca8f055
$ git -C revenger-shokunin rev-parse 4c1eeae^{tree}
b6f07f5af8cab9f91019a718024b1254d85ae6c1          # candidate/build commit named in the handoff
$ for c in 620849e 4c1eeae c6e284c; do git show $c:corpus/knowledge/round-71-apk-axml-byte-evidence.md | sha256sum; done
671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092  -   (620849e)
671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092  -   (4c1eeae)
671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092  -   (c6e284c)
$ git -C revenger-shokunin diff --exit-code -- corpus/knowledge/round-71-apk-axml-byte-evidence.md
(no output; exit 0 — working-tree entry == HEAD)
```

The entry file is byte-identical in the candidate commit, the freeze commit and the lane HEAD, so "final tip" is unambiguous for this surface. The freeze delta `4c1eeae..c6e284c` touches only `.ufo/waves/round-71/w2-{dispatch,spec}.json` and `w2/swarm-registry.json`; `4c1eeae` itself adds only two `sources-s05x/validate.log` lines. No `corpus/` file differs. All measurements below run in a `git archive HEAD` tree (`/fast/scratch/hyaku/revenger-r71/R71W2EntryBlocks/tree`), not the live working tree.

Tree state observed at measurement time (recorded, not touched): live working tree carries two uncommitted sibling edits outside my scope (` M corpus/SOURCES.md`, ` M corpus/lessons/round-71.md`) and untracked `corpus/__pycache__/`; none of them is the entry or a script the entry runs. Entry state in the measured tree: `admission-status: candidate` (line 12); README C05 row is `uncovered` with the v6 path in its knowledge column; the measured archive contains no `.ufo/waves/round-71/w2-votes/` directory.

## 2. Registered gate at tip (floor, not admission)

```
$ cd <tree> && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md
checked_blocks=24 problems=0
exit=0        stderr bytes=0
```

Same command from the live lane root also prints `checked_blocks=24 problems=0`, exit 0. `24` is the entry's full `$`-block count (see §3), and it is ≥ the frozen predicate's 17-block floor; the floor is satisfied, nothing more is inferred from it. Adjacent lint at the same tip (supplementary, not my verdict):

```
$ cd <tree> && python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
exit=0
```

## 3. Independent re-run: exact, not containment

The gate credits only the clause "every embedded line appears in the command's stdout" (`corpus/check_embedded_outputs.py:189-190` builds `set(stdout.splitlines())` and `:153-155` credits a line only by membership; one-directional). I re-implemented block parsing and comparison in `/fast/scratch/hyaku/revenger-r71/R71W2EntryBlocks/compare_blocks.py` (read-only over the tree) and scored three strengths per block plus a second run for determinism:

- S1 containment (the gate's clause), S2 ordered equality (`embedded == stdout`), S3 no extra stdout line (multiset).

```
$ python3 -B compare_blocks.py tree corpus/knowledge/round-71-apk-axml-byte-evidence.md
blocks 24   checked 24   problems {'S1': 0, 'S2': 0, 'S3': 0}
```

All 24 blocks: `rc=0`, `missing=0`, `extra=0`, `ordered_exact=True`, `deterministic=True` (byte-identical stdout and rc on two consecutive runs). Embedded and actual line counts are equal in every block, so multiplicity is exact too:

| entry line | item | command | emb/out lines | exact |
|---|---|---|---|---|
| 27 | 1 | `readout.py --fact archive` | 1/1 | yes |
| 34 | 2 | `readout.py --fact eocd` | 1/1 | yes |
| 36 | 2 | `entry_checks.py --eocd` | 1/1 | yes |
| 43 | 3 | `readout.py --fact member[AndroidManifest.xml]` | 1/1 | yes |
| 45 | 3 | `readout.py --fact member[classes.dex]` | 1/1 | yes |
| 47 | 3 | `readout.py --fact member[META-INF/MANIFEST.MF]` | 1/1 | yes |
| 58 | 4 | `readout.py --fact axml_chunk_table` | 1/1 | yes |
| 67 | 5 | `readout.py --fact spec_derived_struct_widths` | 1/1 | yes |
| 76 | 6 | `readout.py --fact axml_string_pool` | 1/1 | yes |
| 83 | 7 | `readout.py --fact axml_resource_map` | 1/1 | yes |
| 90 | 8 | `readout.py --fact axml_start_element` | 1/1 | yes |
| 92 | 8 | `readout.py --fact axml_start_namespace` | 1/1 | yes |
| 94 | 8 | `readout.py --fact axml_end_element` | 1/1 | yes |
| 96 | 8 | `readout.py --fact axml_end_namespace` | 1/1 | yes |
| 105 | 9 | `readout.py --fact dex_declared_header` | 1/1 | yes |
| 114 | 10 | `readout.py --fact jar_manifest` | 1/1 | yes |
| 123 | 11 | `derive_axml_anchors.py` | 20/20 | yes |
| 144 | 11 | `entry_checks.py --spec-quotes` | 6/6 | yes |
| 156 | 12 | `entry_checks.py --zip-layout` | 20/20 | yes |
| 182 | 13 | `entry_checks.py --oracle` | 34/34 | yes |
| 222 | 14 | `entry_checks.py --pins` | 10/10 | yes |
| 238 | 15 | `entry_checks.py --stdout-digest` | 1/1 | yes |
| 245 | 16 | `entry_checks.py --container` | 3/3 | yes |
| 254 | 17 | `entry_checks.py --axml-layout` | 24/24 | yes |

No command in the entry writes: file-manifest hash of the tree is identical before and after a full comparator pass (`670bbcd4…b3e5` both times, no new file). The extraction's only `__pycache__` is the tracked counter bytecode noted in §7.

## 4. Prose claims that rest on block output, checked against real stdout

- **Item 15:** `readout.py` full run → 15 stdout lines, `sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — equals the item-15 embedded line and the Reproduce claim ("Exit 0 and 15 stdout lines", rc 0).
- **Item 12:** `--zip-layout` → exactly 20 stdout lines; lines 16–18 are `APPNOTE 4.3.7` (heading 387, fields 389-399), `4.3.12` (511, 522-538), `4.3.16` (632, 634-646); lines 19–20 are `central.fixed_part` width 46 and `local.fixed_part` width 30. Matches the prose's positional statement.
- **Item 11:** `--spec-quotes` → 6 `MATCH <file>: first line <n>, folded phrase present=True: <phrase>` lines (1× `rea-android-applications.md`, 4× `dex-format.html`, 1× `ResourceTypes.h`), i.e. file + first-line number + phrase present + searched phrase, as S052 and item 11 state; the first `dex` line is `dex-format.html:5949`, not a raw snapshot line.
- **Item 14:** independent `sha256sum`/`stat` of the ten named files reproduces all ten digests and sizes verbatim (`fixture.apk 05d2280f…d03e 947`, `truth.json 27303bae…8173 2466`, `generator.py eaa9444c…7c1a 9599`, `readout.py 92e347c3…3976 11236`, `entry_checks.py 2d4f25f6…ab1f9 15062`, `derive_axml_anchors.py 74d4c0d9…83aa 4979`, `ResourceTypes.h 56b88bc4…c56f 86255`, `APPNOTE.TXT 0b993022…0cd6 174585`, `dex-format.html c0428612…d9f4 281157`, `rea-android-applications.md 412d9cb4…474c 1992`).
- **Item 4 vs item 5 arithmetic:** item 4's resource-map chunk (offset 204, size 44, headerSize 8) leaves 36 = 9×4, matching item 7's nine entries; item 5's printed `node_header_size` 16 with attrExt `ns` at `+16` (item 17) is the same literal item 8 uses. All three numbers come from the now-verified blocks.

## 5. Gate liveness at tip (mutants, scratch copies only)

Four single-line mutants of the entry, each in its own copy of the tip tree:

```
M1 one-character drift in item 1 ("bytes": 947 → 948)   -> drift entry:28 … ; checked_blocks=24 problems=1 ; rc=1   (killed)
M2 deleted one embedded --oracle MATCH line             -> checked_blocks=24 problems=0 ; rc=0                     (passes — known gap)
M3 appended "FABRICATED: gate must reject this line"    -> drift entry:249 … ; checked_blocks=24 problems=1 ; rc=1   (killed)
M4 swapped two embedded --zip-layout lines              -> checked_blocks=24 problems=0 ; rc=0                     (passes — order not checked)
```

So the gate is live and non-vacuous on these bytes (transcribed-line drift and fabricated extra lines are caught), while two drift classes are structurally invisible to it: a *deleted* embedded line and a *reordered* block. Both are already named as unguarded in the entry's Q13 row; §3's S2/S3 pass shows neither class is present in the landed bytes at this tip, but the gate itself would not have proven that.

## 6. Coverage of the entry's declared commands

36 fences (balanced); 24 `$ ` command blocks, all gated; zero `$ ` lines outside fences. One fenced region is not a gate block: the `Reproduce` fence at entry lines 320–322 declares `python3 -B corpus/fixtures/apk-r65/readout.py` under a ` ```sh ` fence with **no `$ ` prefix**, so the gate never runs it. Its prose claim ("Exit 0 and 15 stdout lines") is therefore backed only indirectly, through item 15's `--stdout-digest` (which runs the readout with `check=True`); I ran that command directly and it is exit 0 / 15 lines / digest `507d79f8…`, so there is no mismatch — the gap is coverage of *25 declared commands by a 24-block gate*, not drift. Adding `$ ` to that fence would close it; that is a source edit and out of scope for this wave.

## 7. Side observations (located, not repaired)

- `reports/round-71/__pycache__/measure.cpython-314.pyc` is **tracked** (`git ls-files` count 1 for `pycache`), added in `620849e`, and therefore present in the counter's measured archive. It is inert for these commands (all run as scripts with `-B`; `measure.py` runs by path), but a committed bytecode artifact of the counter sits inside the frozen measurement tree.
- `.gitignore` contains only `.ufo/interactive-sessions/`, so bytecode is not excluded generally; the working tree additionally holds untracked `corpus/__pycache__/` and `reports/round-70/__pycache__/`.

## 8. Limits of this finding

This seat measured embedded *command/output* correspondence and gate/lint operability at the tip. It did not adjudicate Q01–Q16, wrote no vote file, and did not run the full counter (the 120-second timeout leg belongs to other seats). Within the gate's one-directional, set-based contract the result is exact-order, exact-multiplicity and deterministic at this tip; `HOLDS_C1_V6` cannot be yes from these bytes alone (entry still `candidate`, README C05 `uncovered`, no committed `w2-votes/` in the measured archive). No source, report, README, counter or route file was modified by this seat.
