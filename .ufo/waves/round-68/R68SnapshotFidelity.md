# R68SnapshotFidelity — C2 snapshot-copy fidelity

**PASS** — `corpus/snapshots/ResourceTypes.h` is byte-identical to the pinned round-65 snapshot (sha256 `56b88bc4…c56f`, 86255 bytes, `cmp` exit 0), is tracked in the repository, matches the HEAD blob exactly, and the committed anchor derivation runs against it with exit 0 and 17 anchors reproducing the entry's cited line numbers including the repaired `:245`.

Seat: `L1Revenger68.R68SnapshotFidelity` (read-only leaf, no edits made). HEAD inspected: `4232235723cf8d4731a1e7e78ca098b8af953a57`.

## 1. Byte identity of the copy vs the pinned snapshot

```
$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
$ stat -c '%n %s' <both>        → 86255 / 86255
$ cmp <copy> <pinned>; echo $?  → (no output) cmp_exit=0
```

- Digests equal, sizes equal (86255 = the value pinned in `.ufo/waves/round-68/claims.md:110-111`), `cmp` reports no differing byte. **Byte-identical: yes.**
- Content is the real AOSP header, not a stub: 2366 lines, `/* Copyright (C) 2005 The Android Open Source Project … Apache License 2.0`, terminates `#endif // _LIBS_UTILS_RESOURCE_TYPES_H`.
- The pinned source `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` is itself tracked (`git ls-files` lists it, alongside `rea-android-applications.md` and `zipfile-docs.html`), is not ignored (`git check-ignore -v` exit 1), and has clean status — the pin is not a dirty/ignored local artifact.

## 2. Tracking state of the copy

```
$ git ls-files corpus/snapshots/            → corpus/snapshots/ResourceTypes.h
$ git status --porcelain -- corpus/snapshots/  → (empty), status_exit=0
$ git ls-files -s corpus/snapshots/ResourceTypes.h
100644 c2648909386ca3722c8a3bff98708505ab4f27a2 0	corpus/snapshots/ResourceTypes.h
$ git rev-parse HEAD:corpus/snapshots/ResourceTypes.h → c2648909386ca3722c8a3bff98708505ab4f27a2
$ git hash-object corpus/snapshots/ResourceTypes.h    → c2648909386ca3722c8a3bff98708505ab4f27a2
```

- **Tracked: yes**, at mode `100644`, no untracked/modified/staged state.
- Index blob = HEAD blob = worktree blob (`c264890…f27a2`), i.e. the thing committed *is* the thing measured on disk; no staged-but-uncommitted divergence.
- The **committed** bytes independently re-verified, not just the worktree:
  ```
  $ git cat-file -p HEAD:corpus/snapshots/ResourceTypes.h | sha256sum
  56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  -
  $ git cat-file -s HEAD:corpus/snapshots/ResourceTypes.h → 86255
  ```
  So the copy is byte-identical **as committed**, and the digest the entry cites at `corpus/knowledge/round-68-apk-axml-byte-evidence.md:129` / `:4`-item4 is the committed content, not a local accident.
- Reachable from a committed-tree extraction (the counter's input mode): `git archive HEAD corpus/snapshots/ResourceTypes.h | tar -t` lists `corpus/snapshots/ResourceTypes.h`. The copy survives `git archive`/clone and is not dependent on `.ufo/` being present.

## 3. Functional check — the copy actually serves the derivation (freshness)

`corpus/SOURCES.md:61` (S046) and the entry's item 11 claim the anchors are *machine-printed*, not transcribed. Verified:

```
$ sha256sum corpus/derive_axml_anchors.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249   ← matches S046's cited script sha256
$ grep -n 'SNAPSHOT_SHA256' corpus/derive_axml_anchors.py
33:SNAPSHOT_SHA256 = "56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f"
$ python3 -B corpus/derive_axml_anchors.py; echo $?
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
derive_exit=0
```

That is the complete 17-line output, verbatim.

- The script self-pins the same digest (`SNAPSHOT_SHA256`) and fails hard on mismatch, so the copy and the reader are bound to one value — a tampered or stale copy cannot silently pass.
- Independent corroboration by direct read of the copy: `sed -n '238,250p'` shows `RES_XML_START_NAMESPACE_TYPE` on **line 245** and `struct ResChunk_header` at **line 218**, i.e. the round-67 `:244`→`:245` repair is correct against these exact bytes.
- Every anchor printed matches the entry's cited line numbers (`:1`-line source row, `:129` embedded block). **Fresh, not stale.**

## 4. Findings that bear on C2 coverage (for the L1, not blockers)

1. **The frozen counter does not observe this copy.** `grep -n 'ResourceTypes\|snapshot\|56b88bc4' reports/round-68/measure.py` → no match (exit 1). `measure.py:45` still points `c05_cand` at `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, not the round-68 candidate. Consequence: the C05 predicate is computed off the *round-65* entry; neither the r68 candidate's presence nor this snapshot copy's byte-exactness is counter-observed. That is consistent with the frozen contract (measure.py is never edited post-registration), but it means item 4 of `claims.md:110-111` is currently attested **only** by manual verification such as this seat's, not by an automated gate.
2. The copy's guard is real but narrow: protection against divergence exists only *inside* `derive_axml_anchors.py` (digest pin → exit 2). Anything that regenerates `corpus/snapshots/ResourceTypes.h` without running the script leaves no trace in the counter.
3. No `.gitignore` interaction: `git check-ignore -v corpus/snapshots/ResourceTypes.h` exit 1, so the copy cannot be silently excluded by a future ignore rule of the `.ufo/` family.

## 5. Plain answers

- **Is the committed copy byte-identical to the pinned snapshot?** Yes. sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` on both sides, 86255 bytes on both sides, `cmp` exit 0, and the committed blob (`git cat-file -p HEAD:…`) hashes to the same digest at the same size.
- **Is it tracked in the repository?** Yes. `git ls-files corpus/snapshots/` returns it; `git status --porcelain -- corpus/snapshots/` is empty; index, HEAD and worktree blobs all agree at `c2648909386ca3722c8a3bff98708505ab4f27a2`; the path is included by `git archive HEAD`.

## 6. Retained evidence / risks

- Commands above were all executed in this seat with the outputs shown; nothing was inferred. Hashing done against the lane at HEAD `42322357…`, whose `corpus/snapshots/` also has ctime/mtime 2026-10-24 23:22 — consistent with the wave's build state, and irrelevant to fidelity given the blob-identity check.
- Residual risk: fidelity is correct **now** but is not counter-enforced (finding 4.1). If a later wave regenerates the copy, only `derive_axml_anchors.py` would notice.
- No installs or updates were performed (no tooling change to report). No files were edited; this report is the only write.
