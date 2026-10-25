KILLED-ATTRIBUTED — the frozen mutant `problems += []  # mutant: verbatim comparison removed` at `corpus/check_embedded_outputs.py:105` is caught by the registered `--self-test` detector: exit 1, stderr empty, stdout exactly two lines, LAST line = `drifted entry output accepted` (the frozen attribution marker).

# R69MutC7Kill — frozen-mutant attack on the C7 gate (hold, not a claim)

seat: L1Revenger69.R69MutC7Kill · role: mutation tester · date 2026-10-25
lane: /home/vgpnk/Projects/shokunin/revenger-shokunin @ `35e12584d37434632fa06a6c2975ab55f29a8d3f`
("round-69: wave preparation — 64-seat v2 spec + builder, validated plan (exit 0), dispatch taskCall (64 tasks), swarm registry, slot acquire receipt (D2)")
scope: probe only. No claim scored, no gate flipped, lane tree not edited.

## Mutant (exactly as frozen)

- target: `corpus/check_embedded_outputs.py:105`
- pristine: `        problems += drift(lines, stdout_set, lineno)` (single occurrence; `grep -c` = 1)
- mutant:   `        problems += []  # mutant: verbatim comparison removed`
- applied to an isolated scratch copy `/tmp/revenger-r69-mutc7-cpTleW/corpus` (**not** the lane tree; write scope)
- diff of scratch vs lane is exactly that one line (`105c105`), nothing else.

## Hashes (before / mutated / restored)

| state | sha256 of `corpus/check_embedded_outputs.py` |
|---|---|
| pristine (lane bytes, also the scratch pre-state) | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` |
| mutated | `d67d9b121389e922f7a64fafb9bad08ba530691dc68ddb5759ae0d9535f5c2ba` |
| restored | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` (restored == pristine, `diff` empty) |
| lane tree after probe | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`; `git status --porcelain corpus/check_embedded_outputs.py` → empty output (exit 0) |

## Detector: `python3 -B corpus/check_embedded_outputs.py --self-test`, cwd = scratch tree root

### 1. Control on pristine bytes (red-before the mutation)

```
EXIT=0
--- stdout ---
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
--- stderr ---
(empty)
LAST_ENDS_WITH_MARKER=no
```
stdout sha256 `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d`.

### 2. Mutated bytes

```
EXIT=1
--- stdout ---
self-test: drifted entry not caught
drifted entry output accepted
--- stderr ---
(empty)
--- line count ---
2
LAST=[drifted entry output accepted]
LAST_ENDS_WITH_MARKER=yes
```
stdout sha256 `b815145160093708271ef7ea318f11d167481fbdee3656ac723792c266e5e5a1`.
Byte-exact stdout (`od -c`): `s e l f - t e s t :   d r i f t e d   e n t r y   n o t   c a u g h t \n d r i f t e d   e n t r y   o u t p u t   a c c e p t e d \n`

### 3. Restored bytes (repeat detector on the restored file)

```
EXIT=0
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
LAST_ENDS_WITH_MARKER=no
```
stdout sha256 `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d` — identical to leg 1.

## Attribution check

`corpus/check_embedded_outputs.py`:
- `:36` `MARKER = "drifted entry output accepted"`
- `:133` `require(problems is not None and checked == 1 and not problems, ...)` — the *clean*-entry require. Under the mutant this still passes (no `self-test: clean entry not clean` line appeared), so the failure is not this branch.
- `:135` `dproblems, dchecked = evaluate(drifted_entry, tmp)` → `problems is []` because the drift accumulation was removed; `:140` `caught = (... and dproblems ...)` → `False`.
- `:142-145` `if not caught: print("self-test: drifted entry not caught"); print(MARKER); sys.exit(1)` — the only printed branch.

So the kill is produced by the drifted-entry branch alone, and the marker is the LAST line of output (two-line stdout, marker second, trailing `\n`). This satisfies the frozen attribution predicate: **KILLED-ATTRIBUTED**, not merely "exited non-zero".

## Coverage finding (supplementary, bounded, same mutant)

The same mutation is **not** detected in `--entry` mode — the gate's verbatim comparison is behaviourally absent there and nothing else notices:
```
--- entry fixture (drifted.md) ---
$ python3 -B reader.py --fact a
{"fact": "a", "v": 9}
=== PRISTINE --entry ===
drift entry:3 embedded output line not in recheck stdout: {"fact": "a", "v": 9}
checked_blocks=1 problems=1
EXIT=1
=== MUTANT --entry ===
checked_blocks=1 problems=0
EXIT=0
```
`[INFERENCE]` Consequence for the C7 hold: the whole killing power against this mutant rests on the self-test's forged-control branch (`:140-145`), i.e. the same single branch whose shape the D5 C7-gameability item already questions. A future mutant that removes the drift accumulation *and* keeps `problems` non-empty by another route (e.g. appending a constant) would satisfy `dproblems` and survive every leg. This is a coverage observation only — it is not permission to change the frozen contract, and it does not alter this probe's verdict.

## Discipline

- No write to the lane tree, no sibling lane, no fleet root, no campaign tree; scratch only under `/tmp/revenger-r69-mutc7-*` (deleted before return).
- No mutating git/jj command; only `git status --porcelain <path>` and `git log -1` (read-only).
- No package install or upgrade performed (none needed; `python3` stdlib + coreutils only).
- Detector run count: 3 self-test runs (pristine, mutated, restored) + 2 `--entry` runs. No re-runs used to confirm a user-observed error.
