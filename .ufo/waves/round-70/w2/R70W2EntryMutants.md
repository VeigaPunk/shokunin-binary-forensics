UNNAMED-SURVIVORS — one survivor class is not named in the entry's Q13 row: a forged lookalike derivation block whose command is a *different in-tree script* that echoes the fabricated lines passes the gate (`checked_blocks=25 problems=0`); M4/M5b survive but are named in Q13, and M5a is detected while contradicting Q13's parenthetical mechanism.

# R70W2EntryMutants — mutation probe of the landed C05 v5.1 candidate + its derivation scripts

Seat: R70W2EntryMutants (wave 2, falsify). Target bytes: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`,
entry `corpus/knowledge/round-70-apk-axml-byte-evidence.md` (sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`,
byte-identical to `git show 17ee7f8:corpus/knowledge/round-70-apk-axml-byte-evidence.md | sha256sum`).
Detector: `corpus/check_embedded_outputs.py` (sha256 `5f42415bd4124cf916ecfd9b745d030254a29d299afbe8061a89b784e0d9e879`),
run as `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` from a tree root.
I did not read `.ufo/waves/round-70/w1/`; no subagents; no writes outside my report file and `/tmp/revenger-r70-R70W2EntryMutants*`.

## Baseline (pristine, before and after)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
checked_blocks=24 problems=0        EXIT=0
```

Ran identically at start and after all mutants (see Restoration). A baseline failure would have been inconclusive; it did not occur.

## Entry mutants (each on a fresh copy of the whole corpus tree; scripts pristine)

| id | mutation (landed entry line) | gate result | verdict |
|---|---|---|---|
| M1 | one digit in embedded JSON, `entry:27` `"bytes": 947` → `946` | exit 1: `drift entry:27 embedded output line not in recheck stdout: {"bytes": 946, …}`, `checked_blocks=24 problems=1` | DETECTED |
| M2 | hex swap in `payload_first16_hex`, `entry:43` `…01001c00c4…` → `…0100c100c4…` | exit 1: `drift entry:43 embedded output line not in recheck stdout: {… "payload_first16_hex": "03000800a00100000100c100c4000000" …}`, problems=1 | DETECTED |
| M3 | `MATCH`→`MISMATCH` in item 12, `entry:175` | exit 1: `drift entry:175 embedded output line not in recheck stdout: MISMATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True`, problems=1 | DETECTED |
| M4 | delete the only embedded output line of item 1 (`entry:27`) | exit 0: `checked_blocks=24 problems=0` | SURVIVED — **named** in Q13 ("deleting an embedded output line is not detected (the comparison is one-directional)") |
| M5a | flag value corrupted: `entry:26` `--fact archive` → `--fact zrchivx` | probe: `readout.py --fact zrchivx` → **0 stdout lines, exit 0**; gate exit 1: `drift entry:27 … not in recheck stdout: {"bytes": 947, …}`, problems=1 | DETECTED — **contradicts Q13's parenthetical** (below) |
| M5b | `--fact` qualifier dropped: `entry:26` → `$ python3 -B corpus/fixtures/apk-r65/readout.py` | probe: full 15-line dump (superset); gate exit 0: `checked_blocks=24 problems=0` | SURVIVED — **named** in Q13 ("a command whose flag is corrupted still passes if its output is a superset of the embedded lines") |
| M6 | add an output line item 16 does not print (`entry:248`) | exit 1: `drift entry:248 embedded output line not in recheck stdout: MATCH forged-member.txt: …`, problems=1 | DETECTED |
| M7 | forged 18th item: lookalike block `$ python3 -B corpus/fixtures/apk-r65/echo18.py` + 3 fabricated `MATCH` lines, inserted before `entry:280`; `echo18.py` created inside the tree printing exactly those lines | exit 0: `checked_blocks=25 problems=0` | **SURVIVED — NOT named in Q13** |
| M8 | item-14 digest of readout.py, `entry:225` final hex char `…8c13976` → `…8c13977` | exit 1: `drift entry:225 embedded output line not in recheck stdout: sha256 92e347c3…813977 11236 bytes corpus/fixtures/apk-r65/readout.py`, problems=1 | DETECTED |

Driver bug, disclosed: my first M8 attempt replaced `"813976"`→`"813977"`, a substring that does not occur in the digest (`…eef8c13976`), so bytes were unchanged and the pass was meaningless; redone with a verified non-no-op replacement (`sub()` now asserts the new string is present and the text changed). M8-redo is the row above.

## The M7 finding (the unnamed survivor)

The gate's confinement (`check_embedded_outputs.py:79-103`, `confined()`/`inside()`) allows any `python3 [-B] <relative script inside the tree>` — including a script that is not a derivation script. A forged block whose command is an in-tree echo that prints the fabricated lines satisfies the one-directional clause exactly, and the gate passes the whole entry:

```
$ python3 -B corpus/fixtures/apk-r65/echo18.py        (probe, exit 0)
MATCH forged.axml.attribute[3].data: readout=8 oracle=8
MATCH forged.dex.header_size: readout=112 oracle=112
MATCH forged.image.size: readout=947 oracle=947

$ gate on the M7 tree
checked_blocks=25 problems=0        EXIT=0
```

Q13 (`entry:310`) names exactly two unguarded clauses: (1) deleting an embedded output line; (2) a corrupted-flag command whose output is a superset. A whole forged lookalike block backed by a foreign in-tree script is neither. Fairness note: Q13's credit sentence ("credited only for the clause that every embedded line appears in its command's stdout") is not overclaimed by the echo — the fabricated lines do appear in the echo's stdout — but the "Unguarded clauses, named" list reads as exhaustive and does not name this class. The A1 counter (`measure-a1.py`, per claims-amendment-A1.md) requires ≥17 distinct commands each being a readout.py / entry_checks.py / derive_axml_anchors.py script, so the A1 label would reject a foreign echo command in the *counter's* tally; the gap is at the gate level that Q13 credits. This is a coverage finding against the Q13 row's named list, not permission to change the contract.

## The M5a finding (Q13's parenthetical misdescribes the landed readout)

Q13 (`entry:310`) states: "(the readout degrades an unknown flag to its full dump)". Against the landed bytes this is false: `readout.py:43` sets `ONLY = sys.argv[sys.argv.index("--fact") + 1]` and `emit()` (`readout.py:26-29`) filters out every fact whose name differs, so an unknown fact value prints **nothing** (probe: `--fact zrchivx` → 0 lines, exit 0) and the gate **detects** the corrupted-value mutant (M5a, drift entry:27). The real superset path is *omitting* the qualifier entirely (M5b: `readout.py` with no `--fact` prints all 15 facts). The named class ("superset passes") is real and survives as claimed, but the mechanism sentence in the Q13 basis is inaccurate prose at a located pointer (`entry:310` vs `readout.py:43,26-29`). Flagging it as a Q13-decision input for the wave; the class-level guard claim stands.

## Script / fixture / snapshot mutants (pristine entry; one file mutated per fresh tree)

| id | mutation | affected subcommand (probe) | gate result | verdict |
|---|---|---|---|---|
| S1 | `entry_checks.py:57` transcribed width `("extra_length", 2)]` → `3)]` (LOCAL_HEADER sum 30→31) | `entry_checks.py --zip-layout` → exit 1, `local fixed part: 31 bytes …`, `MISMATCH local.fixed_part: spec width 31, …` | exit 1: `drift entry:155 command exited 1: … --zip-layout` + `drift entry:226 … not in recheck stdout` (item-14 digest of entry_checks.py also drifts) | DETECTED |
| S2 | `readout.py:103` literal `lh_off + 30:lh_off + 30 + lh_name_len` → `lh_off + 31:…` | `entry_checks.py --zip-layout` still prints `MATCH local.fixed_part … present=True` (a second `lh_off + 30` literal remains at `readout.py:105`, so item 12's literal check alone does not catch it) — but the mutated slice breaks the walk | exit 1: `drift entry:26 command exited 1: … readout.py --fact archive` + `drift entry:253 command exited 1: … --axml-layout` | DETECTED (via exit-code check, not the literal check) |
| S3 | `fixture.apk` one payload byte flipped (offset 49, `0x03`→`0x02`) | `readout.py --fact archive` → new sha256 `528038ed140a8181…`, then `AssertionError: not a RES_XML_TYPE document`, exit 1 | exit 1: `drift entry:26 command exited 1` + `drift entry:253 command exited 1` | DETECTED |
| S4 | `snapshots/ResourceTypes.h:686` phrase `…start of this structure where…` → `structurx` | `derive_axml_anchors.py` → exit 2: `derive_axml_anchors: snapshot digest 99bc0995ddb4bf41… != pinned 56b88bc4a34a9cf4…` | exit 1: `drift entry:122 command exited 2: … derive_axml_anchors.py` + `drift entry:228 … not in recheck stdout: sha256 56b88bc4…` | DETECTED |

S2 nuance: item 12's literal check (`MATCH local.fixed_part: … `lh_off + 30` present=True`) survives a one-literal mutation because the readout carries the same literal twice (`readout.py:103` slice and `:105` payload offset); detection came from the readout crashing (exit 1), which the gate attributes as `command exited 1`. A narrower mutation that changes only one occurrence and does not crash would be needed to test the literal check itself; the assigned probe is as stated.

## Verdict basis

- Survivors: M4, M5b (both explicitly named in Q13's "Unguarded clauses, named") and **M7 (not named)**.
- All other mutants (M1, M2, M3, M5a, M6, M8, S1, S2, S3, S4) killed by the gate with attributed `drift entry:<line>` output.
- Per the tasking's rule ("the entry may NOT claim to guard what survives"), the entry's Q13 row claims no guard for M7's class and therefore does not overclaim — but its named list is incomplete, so the verdict is UNNAMED-SURVIVORS with the single survivor class: *forged lookalike block whose command is a foreign in-tree script that echoes the fabricated lines*.

## Restoration evidence

- Every mutant was applied to a fresh copy under `/tmp/revenger-r70-R70W2EntryMutants/mM*/` and `sS*/`; the pristine seed and the lane repo were never written by me (no mutating git/jj command run anywhere; all lane access was `git show`/`git archive` read-only).
- Mid-run, an external actor deleted `/tmp/revenger-r70-R70W2EntryMutants` (only sibling `R70W2GateQ11a` remained); all results above were already captured in the transcript. I re-derived the pristine tree from `git archive 17ee7f8 corpus` and re-verified: entry sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31` == landed blob hash; `check_embedded_outputs.py` `5f42415bd4124cf916ecfd9b745d030254a29d299afbe8061a89b784e0d9e879`; `readout.py` `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`; `entry_checks.py` `2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9`; `fixture.apk` `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`; `truth.json` `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`; `ResourceTypes.h` `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`; `derive_axml_anchors.py` `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa` — all identical to the pre-mutation inventory, and the baseline re-run on the rebuilt seed is `checked_blocks=24 problems=0`, EXIT=0.
- Driver's own before/after hash check on the pristine seed (before the wipe): `pristine_unchanged: true` for all seven tracked files.
- No packages installed or updated (pacman paused; Python 3 stdlib only). Scratch deleted before returning.
