# R69DeriveCritic — the anchor derivation's failure behaviour

**FAILS-OPEN** — the derivation refuses a snapshot whose *bytes* drifted (exit 2) but the
system it lives in (pinned digest in the same editable file + entry output + snapshot all
from the measured tree + a subset-only gate) will print and certify any set of anchor line
numbers, including 20 wrong ones, with exit 0. Two internal paths also print anchors they
did not uniquely find. Additionally the frozen counter crashes before printing any C7/Q15
label, so `C7_V4_CLEAN` cannot be observed at the after state at all.

Axes attacked: **coverage (C1 / C05 v4 anchors)**, **calibration (C2 / Q15 + D1-class prose)**,
**D5 (counter)**.

Read-only work. Nothing written outside this file and `/tmp/revenger-r69-derive` (deleted at
return). No tools installed; no package manager used.

## 1. Objects under test (digests observed)

```
$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h \
            .ufo/waves/round-65/source-snapshots/ResourceTypes.h
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h   (86255 B)
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
```

Pinned anchors in the real snapshot (the round-65 copy, cross-checked):
`:218 struct ResChunk_header`, `:237 enum {`, `:238 RES_NULL_TYPE`, `:244 RES_XML_FIRST_CHUNK_TYPE = 0x0100`,
`:253 RES_XML_RESOURCE_MAP_TYPE = 0x0180`, `:263 };` — exactly one `RES_NULL_TYPE` in the file
(`grep -n RES_NULL_TYPE` → only `238`), so `enum_block_bounds` resolves the right block today
by luck of uniqueness, not by check.

Baseline run in a scratch copy is 20 lines, exit 0, and matches the v4 entry block verbatim
(`struct ResChunk_header : 218` … `field attributeStart : 687`).

## 2. The three required corruptions (scratch copies only)

Scratch layout: `cp corpus/derive_axml_anchors.py` + `cp corpus/snapshots/ResourceTypes.h`
into `/tmp/revenger-r69-derive/<case>/`, script at the root, snapshot under `snapshots/`
(script resolves `Path(__file__).parent / SNAPSHOT_REL`, `derive_axml_anchors.py:103`).

| # | Corruption | Observed digest | Output | Exit |
|---|---|---|---|---|
| 1 | truncate snapshot to 20000 B | `92f7dca8…3548a` | `derive_axml_anchors: snapshot digest 92f7dca8… != pinned 56b88bc4…` | **2** |
| 2 | flip 1 byte inside `RES_XML_FIRST_CHUNK_TYPE`, size unchanged 86255 | `ef835532…24bf7` | same digest message | **2** |
| 3 | duplicate `struct Res_value` (86272 B) | `9d872c85…3a5d0` | same digest message | **2** |
| 3′ | case 3 **plus** the pin rewritten to the new digest (author-level co-edit) | `9d872c85…3a5d0` | `derive_axml_anchors: struct Res_value: ambiguous (2 hits at [287, 288])` | **2** |
| 3″ | duplicate the whole `enum {`…`};` block, pin co-updated | `04c567489…c86d3` | `derive_axml_anchors: enum RES_STRING_POOL_TYPE: ambiguous (2 hits at [239, 266])` | **2** |
| D | snapshot deleted | — | `derive_axml_anchors: snapshot missing: …` | **2** |

Reading: all three required corruptions fail **closed**, but they fail at the *digest pin*, not
at the anchor logic — `derive_axml_anchors.py:107-108` runs before any line is searched, so the
ambiguity/missing branches at `:74-81` are unreachable on a plain corrupted copy. The
ambiguity machinery is real (3′, 3″) but only reachable by a tree that also rewrote the pin —
i.e. by an author, which is precisely the threat model that matters (see §4).

## 3. Does it refuse to print a line it did not find? **No — two counterexamples**

Docstring claim (`derive_axml_anchors.py:29-33`): *"the script never prints a line number it did
not find"*. True for symbols; **false** for the two line classes added in round 69 (the ones
C1 depends on for the "repair" story).

**(a) Enum-block bounds — no uniqueness check at all.** `enum_block_bounds` (`:83-98`) loops the
`enum {` candidates and `return`s the first whose body contains `RES_NULL_TYPE`; it never counts
matches, never asserts `open < each emitted enum line < close`. Inserting a decoy block before
the real one and co-updating the pin:

```
$ python3 -B derive_axml_anchors.py       # scratch, decoy block inserted at 238
sha256 c6699651c621b04143cc4ef6308768bd811f632cca5b4104abb92950d8b1a573 ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 292
enum block open : 238
enum RES_STRING_POOL_TYPE : 244 = 0x0001
enum RES_XML_TYPE : 246 = 0x0003
enum RES_XML_RESOURCE_MAP_TYPE : 258 = 0x0180
enum block close : 241
...
EXIT=0
```

`open 238 / close 241` are the **decoy's** bounds; the block the cited enums actually live in is
242–268. The output is self-contradictory (`close : 241` while a cited enum sits at `:258`) and
still exits 0. This is exactly the class that killed the round-65/67/68 candidates — a transcribed
range — now producible by the tool that is supposed to prevent it.

**(b) Enum values — silent `?` degradation.** `:122-123` is `value = m.group(1) if m else "?"`.
Changing one cited enum's initializer to a non-`0x…,` form and co-updating the pin:

```
$ python3 -B derive_axml_anchors.py
enum RES_XML_FIRST_CHUNK_TYPE : 244 = ?
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
EXIT=0
```

A value the script did not find is printed as if derived, and the gate (§4) accepts the `?`
verbatim because it re-runs the same command. Latent rather than active on the pinned bytes
(all eight cited values parse), but it is a one-byte corruption away from emitting a fabricated
"derived" value.

Correctly closed: a cited symbol absent from the bytes → `: not found`, exit 2; a symbol present
only in a non-initializer position (e.g. `FIRST_CHUNK_CODE = RES_XML_FIRST_CHUNK_TYPE,` at :734)
does **not** create false ambiguity, because the predicate is anchored `startswith(name + " ")`
on the stripped line (`:119-121`). That part of the design is sound.

## 4. Can a corrupted `corpus/snapshots/` copy make the v4 anchors wrong while the gate passes? **Yes.**

The gate checks **reproducibility only**, never the anchors, and every input it needs is inside
the tree being measured:

- The counter invokes it with `cwd = TREE`: `measure.py:446` (`--self-test`), `:470/:482/:490`
  (`--entry corpus/knowledge/round-6{5,7,8,9}-…md`), and `TREE` is the `git archive <commit> corpus`
  extraction (claims §Frozen counter). So entry bytes, snapshot bytes and the digest pin are
  **one tree, one author**.
- `evaluate` (`check_embedded_outputs.py:88-108`) runs the embedded `$ …` command, requires
  `rc == 0`, then keeps the embedded lines that are **absent** from stdout (`drift`, `:83-86`).
  It is a drift check, not a fidelity check: nothing compares the snapshot, the printed line
  numbers, or the printed digest to AOSP or to any out-of-tree pin.
- The only fidelity link is the literal at `derive_axml_anchors.py:40`, in the same file the
  corruptor can rewrite.

**(A) corrupted snapshot + repinned pin, entry untouched — gate (correctly) red:**

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
drift entry:132 embedded output line not in recheck stdout: struct ResChunk_header : 218
... (20 lines) ...
checked_blocks=17 problems=20                                              GATE_EXIT=1
```

**(B) same tree, entry block updated to the corrupted output — gate (wrongly) green:**

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0                                               GATE_EXIT=0
```

The accepted entry now states, with the gate's blessing:

```
sha256 64739e929c91e2574c39b318a140d6a9d5b6d8ce571b67b883346aaf26a8f441 ResourceTypes.h
struct ResChunk_header : 221          # real :218
struct Res_value : 290                # real :287
enum block open : 240                 # real :237
enum RES_XML_FIRST_CHUNK_TYPE : 247 = 0x0100   # real :244
enum RES_XML_RESOURCE_MAP_TYPE : 256 = 0x0180  # real :253
enum block close : 266                # real :263
```

**All 20 anchors are false**, the printed digest is not the AOSP digest, and the entry's own
line 6 still says `snapshot sha256 56b88bc4…` — an in-document contradiction that no registered
checker reads. Derivation exit 0 in that tree too.

**(C) subset hole.** On a pristine tree, deleting 19 of the 20 embedded derivation lines and
keeping only the sha256 line still yields `checked_blocks=17 problems=0`, exit 0. The gate cannot
enforce claims §C1 item 2 ("bounds its credit to exactly the numbers the command prints") or the
"20 lines" claim in S047/`SOURCES.md:61`; a one-line embed is C7-clean.

So: the gate certifies *"this tree's command prints these lines"*, not *"these anchor numbers are
true of the pinned AOSP bytes"*. The threat is not a stray corrupt byte (exit 2, caught) but a
tree-coherent edit — snapshot + pin + entry — which is the shape every self-consistent
transcription defect takes.

## 5. Blocking side finding — the frozen counter cannot print `C7_V4_CLEAN` (or `Q15_*`)

On a **pristine** extraction of the tip (`git archive 35e1258 corpus`), with the frozen counter
(sha256 `bca74e6d…`, identical at `e1d22ca`, `da02261`, `35e1258` and the worktree):

```
$ cd / && TMPDIR=… python3 -B …/reports/round-69/measure.py <pristine-tree>
…
FRESH_ROWS=18/18
Q15_PRESENT=yes
Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
EXIT=1
```

`measure.py:158/163/172` call `run()`; `def run` is at `:187`. Top-level execution reaches the
Q15 block first whenever `TREE/corpus/q15_tree_id_check.py` exists (`:157`) — which is the state
C2 requires. Consequences:

- `C7_V4_CLEAN`, `C7_SELFTEST`, `Q15_SELFTEST`, `Q15_FALSE_KILLED`, `Q15_RESTATE_OK`,
  `HOLDS_OK_V*`, `HOLD_CALIBRATION` are **never printed** at the after state; the run dies at
  log line 25/26.
- Exit is **1**, not the contract's `2 = not evaluable` (claims §Frozen counter). A reader of the
  exit code alone would read "a hold failed", and the claims' void condition "counter exit
  non-zero at final" fires on an artefact defect rather than a measured regression.
- The red-before receipt survives **only** because the base tree has no checker:
  `git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → `fatal: … not in '222a7a7'` (exit 128),
  so `:157` is false and the block prints `n/a (no checker)` (`measure-before.log:23-25`).
- That makes claims.md:137-139 — *"On the base tree: … `Q15_SELFTEST=pass` and
  `Q15_FALSE_KILLED=yes`"* — **false against the receipt it names** (`measure-before.log:23-25`
  says `n/a (no checker)`). A D1/M46-class sentence, asserted in the same round that claims to
  close D1, in the same file that froze the counter.

I flag this as a finding on my axis because it invalidates the only label that could have
carried my §4 result: whatever the derivation does, the registered counter cannot certify
`C7_V4_CLEAN=yes` at the final tree.

## 6. Impacted axes

| Axis | Impact |
|---|---|
| **coverage / C1** | The v4 anchors' credit rests on derivation + gate that cannot distinguish a corrupted snapshot from the pinned one once the pin is co-edited. `C7_V4_CLEAN=yes` is unreachable (§5), so C1's frozen predicate cannot be satisfied as written. |
| **calibration / C2** | Q15 is the right class (identity re-derived by the command that names it) — but the counter that must print `Q15_*` crashes, the red-before sentence contradicts its own receipt, and Q15 covers *git tree ids* only; the same defect class on *file digests* (this report) is uncovered. |
| **D5 / counter** | `run` call-before-def at `:158`; uncaught exception exits 1 instead of 2; C7/Q15 blocks unreachable. |

## 7. Smallest safe corrections

Ordered by size; each is independently sufficient for one hole.

1. **Derivation, fail-closed (3 lines, author-editable, no instrument change).** In
   `enum_block_bounds`, collect all candidate blocks and `fail("enum block: ambiguous (N blocks)")`
   unless exactly one; after building `out`, assert `open_line < every cited enum line < close_line`
   and `fail` otherwise. Replace `value = m.group(1) if m else "?"` with
   `if m is None: fail(f"enum {name}: no 0x value on :{line}")`.
2. **Counter, mechanism (2 lines).** Move `def run` (currently `:187`) above the Q15 block, and
   wrap the top level so an uncaught exception exits **2** (not evaluable) rather than 1 —
   otherwise a crash is indistinguishable from a failed hold and trips the void condition for the
   wrong reason. Because the counter is frozen at `bca74e6d…` and "never edited after this
   revision", the honest disposition for **this** round is to report C1/C2 **FALSIFIED** under
   their own kill rules and land this as the next round's repair, not to patch the frozen artefact
   mid-measurement.
3. **Out-of-tree fidelity leg (the Q15 shape, applied to file digests).** The counter already holds
   `LANE` (`measure.py:30`) and reads outside the measured tree for Q15's `git rev-parse`. Add:
   `sha256(TREE/corpus/snapshots/ResourceTypes.h) == sha256(LANE/.ufo/waves/round-65/source-snapshots/ResourceTypes.h)`
   **and** `==` the digest printed in the entry's `source:` header. This closes §4(B) without
   trusting the in-tree pin, and §4(B) is exactly the case where the in-tree pin and the block
   agree but the header does not.
4. **Coverage claim, mechanically checkable.** Assert the v4 derivation block has exactly 20 lines
   when the gate reports clean (closes §4(C)); the gate's `drift` is a subset test by construction
   (`:83-86,105`) and should not be widened globally — other blocks legitimately quote a subset of
   a full run.

## 8. Scope / limits

- All corruption was on `/tmp/revenger-r69-derive/*` copies; the lane tree, `corpus/` and
  `.ufo/` were read only. No mutating git/jj command was run (`git archive`, `git show`,
  `git cat-file -e`, `git log` only).
- The round-69 v4 entry's *content* (readout/oracle claims) is out of my brief; I attacked only
  the failure behaviour of the derivation, the gate that re-checks it, and the counter path that
  carries the label.
- `/tmp/revenger-r69-derive` and `/tmp/revenger-r69-counter-XXXX` removed before return.
