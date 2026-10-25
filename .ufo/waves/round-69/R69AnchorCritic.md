DEFECT — the derivation is sound on the pinned bytes, but the registered gate pins only the fenced block; the exact prose/frontmatter channel that falsified rounds 65/67 (M40/M44) passes it (gate exit 0 on the M44 bytes reconstructed).

# R69AnchorCritic — attack on the anchor derivation (round 69)

Scope: `corpus/derive_axml_anchors.py` (sha256 `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`, matches S047 at `corpus/SOURCES.md:61`), `corpus/check_embedded_outputs.py`, `corpus/knowledge/round-69-apk-axml-byte-evidence.md` item 11. Nothing edited; all mutants were scratch copies under `/tmp/revenger-r69-*` (deleted).

Axes attacked: **coverage** (is the anchor class actually captured?) and **calibration** (does the capture have a shown-able-to-fail property on the class it names?). Lane verdict codes only.

## Independent ground truth for the claimed numbers

```
$ python3 -B corpus/derive_axml_anchors.py    # cwd = lane root
exit 0, 20 lines; sha256 line = 56b88bc4…c56f
enum block open : 237 · RES_XML_TYPE : 241 = 0x0003 · RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100 · RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180 · enum block close : 263
$ sed -n '236,264p' corpus/snapshots/ResourceTypes.h     # 237 == "enum {", 263 == "};", 245 == RES_XML_START_NAMESPACE_TYPE
$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4…c56f  both
```

Every number the entry states is in the 20-line set: header anchors (218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263), item 8 (677, 686, 687), item 11 (= the block). So the *current* bytes are consistent; what follows is about what the capture would catch.

## (1) Can the script print a line it did not find?

For the four `find_unique` families (7 structs, 8 enums, comment, field): **no** — `derive_axml_anchors.py:74-80` returns only an index of a predicate hit and exits 2 on zero/multiple hits. Mutation m1 (value moved to the next line, so the declaration no longer matches `name + " "`): `derive_axml_anchors.py: enum RES_XML_START_NAMESPACE_TYPE: not found`, **EXIT=2**. Fail-closed.

Two paths print a number the script did **not** find, both at exit 0:

1. **The close bound is arithmetic, not searched.** `:97` `return i + 1, i + 1 + len(span) + 1` — `close_line` is computed from the length of the span, so if the block's `};` does not satisfy the exact `l.strip() == "};"` test at `:93`, the loop runs to the *next* exact `};` anywhere below. Mutation m2 (line 263 → `};  // end of chunk-type enum`, everything else identical, digest re-pinned in the scratch copy): **EXIT=0**, printed `enum block close : 350` — a line number that is not the block's close, silently, with success.
2. **The value channel is not fail-closed.** `:123` `value = m.group(1) if m else "?"` — a matched enum line with no `= 0x…,` prints `= ?` and exits 0. Item 11's sentence only promises refusal for a "missing or ambiguous symbol", so this is a narrow over-generalisation rather than a false claim, but the `?` is non-numeric and would flow into the entry's block as an accepted line.

## (2) Does the output pin the PROSE numbers, or only the block? — **only the block. This is the defect.**

`check_embedded_outputs.py` reads only fenced blocks (`parse_blocks:44-68` — `in_fence` is toggled by a line starting with a triple backtick, and a `$ ` line is only a command *inside* a fence), runs each `$ cmd`, and requires each embedded output line to be a member of stdout (`drift()` at `:83-85`). Nothing in it, and nothing else in the tree, reads a line number out of entry prose. This is structural, not incidental: no prose byte is ever handed to the comparison, so the blindness survives any repair of the counter's definition order (cross-finding below).

```
# edit A — item 11 prose only (entry:153), "RES_XML_START_NAMESPACE_TYPE is line **245**" -> **244**
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-anchor2/prose.md
checked_blocks=17 problems=0        EXIT=0        <-- not caught

# edit B — frontmatter only (entry:1), "**\`:245\`**" -> "\`:244\`" — this reconstructs M44's bytes
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-anchor/frontmatter.md
checked_blocks=17 problems=0        EXIT=0        <-- not caught

# control — the same edit inside the fenced block (entry:143)
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-anchor2/blk.md
drift entry:143 embedded output line not in recheck stdout: enum RES_XML_START_NAMESPACE_TYPE : 244 = 0x0100
checked_blocks=17 problems=1        EXIT=1        <-- caught
```

The class is not hypothetical: `corpus/lessons/round-67.md:126` records M44 as "`corpus/knowledge/round-67-apk-axml-byte-evidence.md`:1 **and :56** anchor `RES_XML_START_NAMESPACE_TYPE` at snapshot :244" — both sites are prose/frontmatter, i.e. precisely the channel the v4 capture leaves unpinned. Edit B above is that defect re-injected, and the registered gate is green on it. `C7_V4_CLEAN` is therefore not a control for the M40/M44 class; it is a control for a channel that never drifted, while the entry's item 11 credits it with the class ("no spec line number in this entry is transcribed by hand", `entry:127`; credit sentence, `entry:153`).

Q13 is the criterion that names this test ("credited only for the clauses whose deletion its own run is shown to detect"). Deletion test on the credited clause: change the prose value, keep the block, the credited command's run is unchanged → the clause is unguarded and is not *named* as unguarded. On the literal reading that is a Q13 hit on the v4 bytes, which C1's kill rule routes to `admission-status: rejected`. A permissive reading ("the number :245 *is* printed somewhere") survives — so this is a one-sentence fix, not an unsalvageable claim:

**Smallest safe correction.** Two additive moves, neither touching the frozen C7 instrument or the counter: (a) item 11 names the prose occurrences (`entry:1`, `entry:153`) as hand-typed restatements *not* detected by the gate and guarded instead by the wave's `R69AnchorDerive`/Q02 seats — which the wave already dispatches (`.ufo/waves/round-69/build-wave-spec.py:156` requires "extract EVERY line number … in the `source:` header anchor list, items 4/8/11 prose"); or (b) add one `$ python3 -c` block to the entry that scans its own bytes for `:NNN`/`line NNN` and prints the sorted set, so the gate compares it verbatim (the gate permits only python3 argv, `run_cmd:72-80`, so a shell `grep` block would be skipped — use python). (a) is the round-safe form.

Secondary, same channel: the gate is **one-way containment** (`:85` `if l not in stdout_set`) with no count and no order check, so embedded lines may be deleted freely.

```
# edit C — delete the "enum block close : 263" line from the fenced block, prose still states :263
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-anchor/subset.md
checked_blocks=17 problems=0        EXIT=0
```

The entry's "the 20-line stdout below … is the complete set" (`entry:127`) is thus an unenforced cardinality; the credit can shrink below the prose's stated numbers and stay green. Same fix ((a) wording, or a `problems += []`-free strictness leg is out of scope this round since the C7 instrument is frozen).

## (3) Can the snapshot copy drift without any check failing? — the *copy* no; the *source* and the *script identity* yes.

```
# D — one byte flipped in corpus/snapshots/ResourceTypes.h (a comment)
$ python3 -B corpus/check_embedded_outputs.py --entry $PWD/corpus/knowledge/round-69-apk-axml-byte-evidence.md
drift entry:130 command exited 2: python3 -B corpus/derive_axml_anchors.py
checked_blocks=16 problems=1        EXIT=1        <-- caught (derive_axml_anchors.py:107 digest guard)
```

The derivation input is pinned end-to-end: `:40` digest + `:107` hard error + the gate's `rc != 0` branch (`:101`). Good.

But two adjacent identities are **asserted in prose and never re-derived**:

```
# E — script edited (one comment line appended): sha256 74d4c0d9… -> 5a149af0…, snapshot untouched
$ python3 -B corpus/check_embedded_outputs.py --entry $PWD/corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0        EXIT=0        <-- entry:6 / S047's "script sha256 74d4c0d9…" is now false, nothing fails
```

- `entry:6` and `corpus/SOURCES.md:61` (S047) assert the script's sha256 and "20 output lines"; no check compares them to disk. A script edit that preserves the 20 lines (comment, refactor, different search order) is invisible, and the registry row silently lies. Q15 does not cover it: its text is "a stated **git object id or tree identity**" (`corpus/QUALITY.md:27`) — a file sha256 is neither. Round-safe fix: name it unguarded, or add `$ python3 -c` hash line(s) for script+snapshot to the entry so the gate re-derives them.
- The round-65 source snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` is read by nothing (`grep -rn source-snapshots` finds only prose citations; `derive_axml_anchors.py:20` mentions it in a docstring). The "byte-exact copy of the pinned snapshot" sentence is a one-time human comparison; either file may change and every check stays green. Currently equal (`56b88bc4…` both), so it is true today, unguarded tomorrow.

## (4) Enum-block bound logic when the file has other `enum {`/`};` lines

The snapshot has 30 `enum {` lines (163, 237, 354, 400, 474, …) and 38 exact `};` lines. `enum_block_bounds` (`:83-98`) scans **all** `enum {` lines and picks the first whose body (up to the first exact `};`) contains a line starting with `RES_NULL_TYPE`; the real block's 237-263 selection is correct because `RES_NULL_TYPE` occurs exactly once, at `:238`. Other blocks are skipped cleanly; a truncated body without `RES_NULL_TYPE` is skipped, not mis-reported. So: correct on these bytes, but **two latent weaknesses, both reachable only with a snapshot whose digest collides with the pin, i.e. not reachable at rest**:

- **No ambiguity check on block identity.** Unlike `find_unique`, multiple qualifying blocks are not rejected. Mutation m3 (a decoy `enum { RES_NULL_TYPE = 0x0000, RES_DECOY_TYPE = 0x0999, };` inserted just above line 237): **EXIT=0**, printed `enum block open : 237` / `enum block close : 240` — the decoy's bounds — while the 8 enum symbol lines still came from the real block (now shifted to 241/245/249…), i.e. an internally inconsistent table printed as success.
- **Line-format dependence** of the close test (m2 above, close 350). `RES_NULL_TYPE` is a proxy for the chunk-type enum, not an identity check; a structural check (also require `RES_XML_LAST_CHUNK_TYPE`/`RES_TABLE_STAGED_ALIAS_TYPE` inside, or require exactly one qualifying block) would cost three lines.

## Cross-finding 2 — claims C2's control paragraph names a state its own receipt contradicts

`reports/round-69/claims.md:137-140` ("**Red-before (committed history).** On the base tree: … `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes`") is internally inconsistent. Base tree = `222a7a7` (claims.md:4), and:

```
$ git cat-file -e 222a7a7:corpus/q15_tree_id_check.py
fatal: path 'corpus/q15_tree_id_check.py' exists on disk, but not in '222a7a7'   exit 128
$ git log --oneline -- corpus/q15_tree_id_check.py
e1d22ca round-69: pre-registration — claims …, frozen counter measure.py, Q15 checker, red-before receipt
$ grep -n Q15 reports/round-69/measure-before.log
22:Q15_PRESENT=no / 23:Q15_SELFTEST=n/a (no checker) / 24:Q15_FALSE_KILLED=n/a (no checker) / 25:Q15_RESTATE_OK=n/a (no checker)
```

Precise scope, so a fix does not over-claim: `pass`/`yes` are *not* impossible states — they are the states of the claims revision `e1d22ca` (checker present, `cat-file exit=0`), not of the base tree the same paragraph and the same receipt name. The defect is site confusion plus a missing receipt: **no committed counter run has ever printed `Q15_SELFTEST=pass`**, because the only trees that carry the checker are the ones where the counter dies at `measure.py:158` (cross-finding below) before reaching that print. So C2's red-before is evidenced for `Q15_PRESENT=no`/`Q15_RESTATE_OK=n/a` only; the two "pass" labels have no receipt on any tree. Positive receipt (re-run by this seat, `R69CounterIntegrity` concurring):

```
$ git grep -n "Q15_SELFTEST=pass" -- .
corpus/q15_tree_id_check.py:75:    print("Q15_SELFTEST=pass (true sentence verified; false sentence killed)")
reports/round-69/claims.md:130:- `Q15_SELFTEST=pass` (the committed checker's own true/false fixtures behave)
reports/round-69/claims.md:138:criterion row), `Q15_RESTATE_OK=n/a` (no round-69 lesson), `Q15_SELFTEST=pass`
$ grep -c 'Q15_SELFTEST=pass' reports/round-69/measure.py      -> 0
$ grep -n 'Q15_SELFTEST' reports/round-69/measure.py          -> :160 f-string expression, :180 "n/a (no checker)"
$ grep -rn '^Q15_SELFTEST=' reports/round-69/                 -> measure-before.log:23 = n/a (no checker)
```

i.e. the only hits are the checker's own print, two prose sentences, and an f-string in `measure.py:160` whose emitted `pass` form is unreachable while the call above it raises. The sole emitted `Q15_SELFTEST=` line in the repo is the `n/a`. (Correction to a detail in the peer report: `measure.py:160` is *not* a literal grep hit — `grep -c` = 0; it matches `Q15_SELFTEST` only.) Frozen text, so this is an L0/re-declaration matter, not an edit.

## Cross-finding (not my judgment to make; reported with receipt to `R69CounterIntegrity`)

`reports/round-69/measure.py` (sha matches the pin `bca74e6d…`) is **not runnable on any tree that contains `corpus/q15_tree_id_check.py`**: `run(...)` is called at module level at `:158` but `def run` is at `:187`.

```
$ git archive HEAD corpus | tar -x -C /tmp/…/base        # HEAD = 35e12584
$ cd / && TMPDIR=/tmp/revenger-r69-counter-A python3 -B …/reports/round-69/measure.py /tmp/…/base
… Q15_PRESENT=yes
Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined          (python exit 1)
```

Exit 1 is the counter's "a hold failed" code (0 = holds, 2 = not evaluable), so the crash is indistinguishable from a red hold, and the claims' "the counter's exit code is 0" branch is unreachable once the checker lands. `reports/round-69/measure-before.log:23-25` never hit `:158` because the base tree `222a7a7` had no checker (`Q15_SELFTEST=n/a (no checker)`) — the red-before receipt could not have exposed it. Also note the consequences for this attack: running the counter on a prose-edited tree gave byte-identical output to the unedited tree, but only because both crash at the same line; the (2) verdict rests on the gate's own exit codes above, not on the counter.

## Verdict and the one-line correction

- Derivation **CLEAN** on the pinned bytes: every stated number is printed, the input is digest-pinned, failures are exit 2, ties are rejected.
- Captured class **DEFECT**: the gate pins the fenced block and nothing else, so the M40/M44 prose/frontmatter channel survives it at exit 0 (edits A and B), and the block's own cardinality can shrink at exit 0 (edit C). The entry credits the derivation with a coverage it does not enforce (`entry:127`).
- Latent only (unreachable under the snapshot pin, still worth three lines): close-bound arithmetic at `:97` and the unchecked `RES_NULL_TYPE` block identity at `:89-98`.
- Registry identity unguarded: `entry:6`/S047 script sha256 and the "20 output lines" count are not re-derived (edit E), and the round-65 source snapshot is not compared to the copy by anything.
- Smallest safe correction: item 11 names the prose restatements as unguarded-by-gate (guarded by the wave's `R69AnchorDerive`/Q02 seats) and, if the round will afford it, one python `$` block that prints the entry's own `:NNN` set plus `sha256sum`-equivalent digests of script and snapshot, so the existing gate re-derives the whole chain verbatim.

Tool installs: none (no package manager used; host pacman paused respected). Scratch: `/tmp/revenger-r69-anchor*`, `/tmp/revenger-r69-counter-{A,B}` — deleted before return.
