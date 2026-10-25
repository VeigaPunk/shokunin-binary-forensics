HOLD-INTACT — `corpus/live` and `corpus/fixtures` are byte-identical between base `f165908aaffcf14798de53405fe788986bd33ff9` and `refs/heads/main` (`4232235`): the required `--stat` is empty (0 bytes captured), both tree object ids match at both ends, all 456 blobs match one-for-one by object id, no commit in `base..main` touches those paths, and the working tree has zero modifications under `corpus/`. The 2702-line `corpus` diff is confined to 5 paths outside `live/`+`fixtures/`, each explained below.

Seat: R68FixtureHold (round 68, revenger-shokunin). Read-only: nothing outside this report was written. No tool installs or upgrades were needed (none performed).

## 1. Required hold command (verbatim)

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --stat \
    f165908aaffcf14798de53405fe788986bd33ff9 refs/heads/main -- corpus/live corpus/fixtures
EXIT=0
---LEN---
0
```
No output lines; the captured byte count of the command's output is **0**. The assertion "it must be EMPTY" holds.

## 2. Hold evidence beyond the empty `--stat`

Endpoint `--stat` alone can hide an add-then-delete round trip inside `base..main`, so the hold was re-established four independent ways.

| Check | Command | Result |
|---|---|---|
| Tree object ids, base vs main | `git rev-parse <base>:corpus/live <base>:corpus/fixtures main:corpus/live main:corpus/fixtures` | `74376f31ebae44d94ca904c3850bae4383496d5e` (live) and `865a4e8e9b03ad32df41f98f441bd63230c21c2d` (fixtures) at **both** ends — identical pairs |
| Blob enumeration, base vs main | `diff <(git ls-tree -r <base> -- corpus/live corpus/fixtures) <(git ls-tree -r main -- …)` on `<blob> <path>` | `IDENTICAL_ALL`; 456 entries at each end |
| Any intermediate commit touching them | `git log --oneline <base>..main -- corpus/live corpus/fixtures` | empty (no output) — no churn was reverted |
| Worktree state | `git status --porcelain -- corpus/live corpus/fixtures`; then `-- corpus` | empty; empty — no uncommitted or untracked change anywhere under `corpus/` |

The four fixture files the C2 entry cites are hash-equal across main-blob, base-blob and on-disk worktree:

```
fixture.apk    main=05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e base=05d2280f… same  disk=05d2280f…
truth.json     main=27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173 base=27303bae… same  disk=27303bae…
generator.py   main=eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a base=eaa9444c… same  disk=eaa9444c…
readout.py     main=92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976 base=92e347c3… same  disk=92e347c3…
```
`fixture.apk` `05d2280f…` and `readout.py` `92e347c3…` are exactly the digests the C05 candidate states at `corpus/knowledge/round-68-apk-axml-byte-evidence.md` lines 2-5 (S041 and `## Observation`), so the entry's fixture-byte claim is still true of the current tree, not just of round 65.

## 3. Required full-corpus diff (verbatim output)

```
$ git diff --stat f165908aaffcf14798de53405fe788986bd33ff9 refs/heads/main -- corpus
 corpus/SOURCES.md                                  |    3 +
 corpus/check_embedded_outputs.py                   |   29 +-
 corpus/derive_axml_anchors.py                      |  102 +
 .../knowledge/round-68-apk-axml-byte-evidence.md   |  215 ++
 corpus/snapshots/ResourceTypes.h                   | 2366 ++++++++++++++++++++
 5 files changed, 2702 insertions(+), 13 deletions(-)
```

`--name-status` on the same range (verbatim):

```
M	corpus/SOURCES.md
M	corpus/check_embedded_outputs.py
A	corpus/derive_axml_anchors.py
A	corpus/knowledge/round-68-apk-axml-byte-evidence.md
A	corpus/snapshots/ResourceTypes.h
```

There is **no `D` and no `R`** row: no corpus file was deleted or renamed, so the 13 deletions are intra-file removals inside `check_embedded_outputs.py` (16 insertions / 13 deletions for that file). Insertion arithmetic reconciles: 16 + 3 + 102 + 215 + 2366 = 2702.

### Every changed or added path, one line each

| # | Path | Status | Δ | Reason |
|---|---|---|---|---|
| 1 | `corpus/SOURCES.md` | M | +3 | Adds the `S046` registry row (own-work, tier A, opened 2026-10-24) for `corpus/derive_axml_anchors.py` plus the matching dated changelog bullet — the sourced row C2's anchor rests on. Diff hunks land at `@@ -58,6 +58,8 @@` (table) and `@@ -94,3 +96,4 @@` (changelog). |
| 2 | `corpus/check_embedded_outputs.py` | M | +16/-13 | C1/C7 attribution repair: docstring reclassifies the file from "Probe, not a registered gate" to a registered `kind gate` outside the `verify_*` family, documents `drifted entry output accepted` as the **last** output line of a failed run (round-67 M45 shadowing), and rewrites the drifted-entry self-test into a forged control where the marker is reachable as the killing line. |
| 3 | `corpus/derive_axml_anchors.py` | A | +102 | New read-only machine derivation of every S038 anchor line number from the pinned snapshot; pins the snapshot sha256 in-file and exits 2 on a missing/ambiguous symbol rather than printing an unverified line. |
| 4 | `corpus/knowledge/round-68-apk-axml-byte-evidence.md` | A | +215 | The C05 v3 candidate (`admission-status: candidate`): round-67 v2 with both `:244` anchors corrected to `:245`, item 11 replaced by the machine-derived 17-line table, Q-map present at `## §Q-map`. |
| 5 | `corpus/snapshots/ResourceTypes.h` | A | +2366 | Byte-exact copy of the lane pin `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` so the derivation runs from any `git archive corpus` tree. |

## 4. Freshness checks on the two added artifacts (grounds the "reason" column)

Snapshot identity, committed blob and disk:
```
$ git show refs/heads/main:corpus/snapshots/ResourceTypes.h | sha256sum   → 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
$ … | wc -c                                                              → 86255
$ sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h          → 56b88bc4…  (86255 bytes)
$ sha256sum corpus/snapshots/ResourceTypes.h                              → 56b88bc4…
```
Matches the pinned digest and byte count in the frozen contract exactly; the copy is not drifted and the working-tree file equals the committed blob.

Derivation script identity and safety:
```
$ git show refs/heads/main:corpus/derive_axml_anchors.py | sha256sum → bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249
$ sha256sum corpus/derive_axml_anchors.py                            → bce497d6…   (identical to the digest S046 states)
$ grep -nE 'write_text|\.write\(|open\(…["'\''](w|a|wb|x)' corpus/derive_axml_anchors.py → NO_WRITE_CALLS
$ python3 -B corpus/derive_axml_anchors.py                          → EXIT=0, 17 stdout lines
```
The 17 lines the script printed are byte-for-byte the block embedded at item 11 (lines 128-146 of the entry), including `enum RES_XML_START_NAMESPACE_TYPE : 245` and `enum RES_XML_RESOURCE_MAP_TYPE : 253`.

Snapshot bytes confirm the correction the entry narrates (read-only `sed` on the committed/disk file):
```
$ sed -n '244p;245p' corpus/snapshots/ResourceTypes.h
    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
```
So `:245` is correct and the round-67 `:244` was indeed one line early; every other derived line (`:239 :241 :246 :247 :248 :253`, structs `218/287/461/612/621/677/707`, attrExt `686/687`) also matches the file's actual line numbering (checked against `sed -n '238,254p'`).

Scope guards held: `corpus/README.md` is **not** in the diff (`git diff --name-only … -- corpus/README.md` → empty), so the C05 row at `corpus/README.md:34` still reads `uncovered` with the round-65 rejected candidate retained — the candidate did not flip its own coverage claim. Frozen counter digest also re-checked: `sha256sum reports/round-68/measure.py` → `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`, equal to the pre-registered digest in the contract.

## 5. Residual risk / notes for C2 and C7 reviewers (none affects the verdict)

1. **`generator.py` is in S041's artifact list but not digest-pinned in the candidate.** S041 cites three sha256s (fixture, truth.json, readout.py) while naming four files. Its actual digest is `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a` and it is unchanged base→main→disk, so no byte drift exists today; the gap is that the entry does not pin the fourth member it names. Low severity, but a reviewer applying a strict "every named artifact carries a digest" reading of Q11 will land on it.
2. **`:244` still appears as prose.** `grep -n ':244'` hits three places: `verified-at` (line 6), `admission-status` (line 9) and item 11's explanatory sentence ("line 244 is `RES_XML_FIRST_CHUNK_TYPE`"). All three describe the repair; none is a cited anchor (the S038 anchor line states `:245`). A mechanical grep-based spoof check that forbids the substring `:244` would false-positive here — the machine proof must be the script's output, not a substring search.
3. **Snapshot duplication is intentional, not drift.** `corpus/snapshots/ResourceTypes.h` duplicates 86255 bytes that live under `.ufo/`; since the counting command archives only `corpus`, the copy is what makes item 11 reproducible from the counted tree, and its digest pin closes the usual "second copy drifts" risk. The build commit also touches `.ufo/waves/round-68/build-r68.py` (outside `corpus`), which cannot reach the counter's tree.

## 6. Verification gaps (declared, not hidden)

- The entry's recheck claim that `corpus/fixtures/apk-r65/readout.py` prints 15 stdout lines hashing to `507d79f8…` was **not** re-executed here (out of the byte-hold scope, and it belongs to the C2 coverage seats). Only its byte identity to round 65 was verified.
- `lsp` was not used: the change set is two Markdown/Python-artifact paths plus a header snapshot with no caller graph, and the byte/digest questions are answered exactly by `git` object comparison. No semantic-index claim is made anywhere in this report.
- Time-boxed at ~12 minutes; no seat, subagent or peer was contacted or waited on.
