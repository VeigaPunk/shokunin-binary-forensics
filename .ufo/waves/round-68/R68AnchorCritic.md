DEFECT — the derivation itself is a genuine, byte-driven capture (not a tautology, and it cannot print a line it did not find), but the repair is only half landed: every spec line number in the entry's **prose** — including the header anchor that Q02 adjudicates — is still hand-transcribed, unguarded, and a `:245`→`:244` edit there (the exact M40/M44 mistake that falsified r65 and r67) passes the registered gate rc=0; item 11's own sentence "no spec line number in this entry is transcribed by hand" is therefore false, and lines 237/244 are values cited only to prose that Q11 requires labelled recorded.

scope: read-only attack on `corpus/derive_axml_anchors.py`, item 11 of `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, `corpus/snapshots/ResourceTypes.h` and the registered gate `corpus/check_embedded_outputs.py`. Nothing edited; all experiments on scratch copies under `/tmp/r68-anchor-critic.1717020/`. Tooling: no installs/upgrades (existing `python3` 3.x stdlib, `git`, `awk`).

Axes attacked: **provenance** (is item 11 a capture or a transcription?) · **regression coverage** (does the registered gate cover the site that killed the last two rounds?) · **input integrity** (can the snapshot copy drift silently?).

---

## (1) Can the derivation print a line number it did not find in the bytes? — **NO**

Trace (`corpus/derive_axml_anchors.py:69-110`): bytes ← `Path(__file__).resolve().parent / "snapshots/ResourceTypes.h"` (cwd-independent) → sha256 vs hardcoded pin (`:85-89`) → `text.splitlines()` (`:91`) → per symbol `find_unique` (`:74-81`) which returns `hits[0]` only when `len(hits)==1`, else `fail()` → `sys.exit(2)` (`:70-72`). There is no literal number anywhere in the script; every printed integer is `enumerate` index + 1 over the snapshot's own lines.

Proved by construction, not by reading — three doctored snapshots + re-pinned copies at `/tmp/r68-anchor-critic.1717020/t{1,2,3}`:

```
--- A shifted+5: exit=0 :: ['enum RES_XML_START_NAMESPACE_TYPE : 250'] field attributeStart : 692
--- B symbol deleted: exit=2 :: ['derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: not found']
--- C symbol duplicated: exit=2 :: ['derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: ambiguous (2 hits at [245, 246])']
```

A (+5 inserted lines at file top) prints **250**: the output follows the bytes, so it is a real capture and not a replay of intent. B and C close the "invent a number" and "pick one of several" paths.

Residual limits, none of them a defect today:
- `raw.decode("utf-8", errors="replace")` (`:90`) is lossy, and `str.splitlines()` splits on more than `\n` (`\v`, `\f`, `\r`, `\x1c-\x1e`, `\x85`, U+2028/9). If the snapshot ever contained one, the printed number would disagree with `grep -n`/`wc -l`. **Not live**: `wc -l` = 2366, `splitlines()` = 2366, newline count = 2366, and the separator scan is empty (`separator bytes present: {}`, `\r` count 0).
- The output prints the number but not the matched line's content, so it cannot show *which* line it matched. Spot-checked the non-enum matches: `218 struct ResChunk_header`, `287 struct Res_value`, `677 struct ResXMLTree_attrExt`, `686 // Byte offset from the start of this structure where the attributes start.`, `687 uint16_t attributeStart;`, `707 struct ResXMLTree_attribute` — all are the real declarations/comment, and every enum predicate uses `startswith(symbol + " ")`, which does not collide with `RES_XML_FIRST_CHUNK_TYPE`. Non-defect, but it is why finding (3)+(2) matter: the only self-evidencing artefact is a list of integers.

Result of the real run (`cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py`): exit 0, **17 lines**, sha256 of stdout `b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831`; every number correct against the bytes (e.g. `:245` is `RES_XML_START_NAMESPACE_TYPE      = 0x0100,`).

## (2) Does it pin the entry's PROSE numbers, or only the embedded block? — **ONLY THE BLOCK**

The gate parses fenced `$ cmd` blocks and only those (`check_embedded_outputs.py:52-76`, `:96-116`); prose outside a fence is never read. Its registry row says so by design: `SKILL.md:267` — "`1` failed (drift: an embedded output line the entry's own command does not print)". So `C7_V3_CLEAN=yes` is a statement about blocks, not about the entry.

Receipts — scratch copies of the entry, gate run from the lane root (so relative command resolution is identical to the counter's `run(TREE, C7_GATE_REL, "--entry", ...)` at `reports/round-68/measure.py:440-445`):

| scratch variant | edit | rc | output |
|---|---|---|---|
| `baseline.md` | none | **0** | `checked_blocks=17 problems=0` |
| `header244.md` | line 1 `source:` `RES_XML_START_NAMESPACE_TYPE` **:245** → **:244** | **0** | `checked_blocks=17 problems=0` |
| `prose_item4.md` | line 57 `start/end namespace :245/:246` → `:244/:246` | **0** | `checked_blocks=17 problems=0` |
| `prose_item8.md` | line 82 `(line 677)` → `(line 676)` | **0** | `checked_blocks=17 problems=0` |
| `prose344.md` | line 148 `is line **245**; line 244 is …` → `**244** … 245` | **0** | `checked_blocks=17 problems=0` |
| `block244.md` | embedded table `enum RES_XML_START_NAMESPACE_TYPE : 245` → `:244` | **1** | `drift entry:139 embedded output line not in recheck stdout: enum RES_XML_START_NAMESPACE_TYPE : 244` |

`header244.md` is the decisive counterexample: after the edit the entry contains **both** `** :244**` (line 1) and `enum RES_XML_START_NAMESPACE_TYPE : 245` (line 139) — self-contradictory — and the registered gate reports clean, so the counter's `C7_V3_CLEAN` stays `yes` and C2's frozen predicate is satisfied by a document asserting the r66/r67-falsified anchor. This is the same mistake class (M40/M44) the repair was routed to eliminate, in the same location (`corpus/lessons/round-67.md:126` records the r67 candidate failing at ":1 and :56").

Consequences, stated precisely:
- **D1 (false self-description).** Line 125: "Every S038 line number this entry states is printed by a committed derivation script … **no spec line number in this entry is transcribed by hand**." Every spec number in prose is a hand-transcribed duplicate of a derived value: line 1 (218, 239, 241, 245, 246, 247, 248, 253, 461, 677, 686, 687, 707), line 57 (239, 245-248, 253), line 82 (677, 686, 687), line 148 (245, 237-253, 244). Line 148's second clause — "the derivation above is the capture that makes it mechanical" — is true of the block and false of the prose it sits in. Lines 6 and 9 (`:244` referring to the r67 draft) and line 68 (`readout.py:166`) are historical/code pointers, not spec anchors — not defects.
- **D2 (uncovered regression surface).** The gate + counter combination cannot detect a prose regression at any of those sites (table above). The mechanical capture does not cover the site Q02 adjudicates (`QUALITY.md:14`, "`source:` … exact anchor") — it covers only the restatement of it.
- **D3 (two values cited only to prose).** Not printed by item 11's command: **237** (lower bound of "lines 237-253" at lines 57, 148, 157) and **244** (its *content*, line 148). Both are **true** — `awk` on the snapshot gives `237 enum {`, `244 RES_XML_FIRST_CHUNK_TYPE = 0x0100,`, `245 RES_XML_START_NAMESPACE_TYPE = 0x0100,`. `QUALITY.md:23` (Q11) requires: "A value cited only to prose is labeled recorded, not re-derived"; neither is labelled. This matters more than usual because 244 and 245 carry the **same enum value** `0x0100`, so no byte value can disambiguate them — only the symbol name at the line does.
- Verified clean inside the block: the embedded 17 lines equal the current stdout **exactly**, in order (`block == stdout exactly: True`, 17/17, nothing missing) — so the block is not a subset or a forgery; the 17-line count in `SOURCES.md:61` and entry line 4 is accurate.

**Gate-scope finding (attribution, not an entry edit).** The gate pins output *text*, not provenance. A scratch entry whose single derivation block is `$ python3 -B /tmp/.../fake_derive.py`, where that script prints a hand-written table with the **wrong** anchor (245→244) and reads no bytes at all, returns:

```
=== spoof_cmd (fake derivation, wrong anchor 244, no bytes read) rc=0
checked_blocks=17 problems=0
```

and nothing pins `corpus/derive_axml_anchors.py`'s digest in the check path (`grep -n 'derive\|anchor' reports/round-68/measure.py` → no hits). So `C7_V3_CLEAN=yes` must be read as "the embedded lines match the stdout of the named command", never as "the anchors were machine-derived". The real guarantee is: committed script + digest pin inside it + a reviewer reading it. Settlement wording should not exceed that.

## (3) Can `corpus/snapshots/ResourceTypes.h` drift from the upstream pinned snapshot with no check failing? — **YES, in the coordinated direction only**

Today the invariant holds by bytes, not by check:
```
56b88bc4…c56f  corpus/snapshots/ResourceTypes.h
56b88bc4…c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
86255 / 86255 bytes · CMP_IDENTICAL · both tracked (git ls-files), neither ignored
```
and the script runs from a corpus-only tree (`git archive HEAD corpus` → `/tmp/…/tree`, which contains no `.ufo`): derive exit 0, gate rc=0, `checked_blocks=17 problems=0` — so claims.md C2 item 4 ("runs from any corpus tree") is verified.

Drift, per direction:

- **Copy drifts, pin untouched → caught hard.** One byte flipped at offset 100 in the scratch tree: gate rc=**1**, `drift entry:128 command exited 2: python3 -B corpus/derive_axml_anchors.py` (the digest guard at `derive_axml_anchors.py:87-89` fires before any search).
- **Copy + pin + block drift together → nothing fails.** Mutated the copy, updated `SNAPSHOT_SHA256` in the script, and updated only the block's `sha256 …` line:
```
checked_blocks=17 problems=0        gate_rc=0
b103194b…   (the mutated copy)
56b88bc4…   (the upstream pinned original, unchanged)
```
So the copy can be non-identical to the "pinned snapshot" it claims to be byte-exact with, and every registered check stays green. Structural reason, not a coding bug: the pin is a constant in the same commit, and the measured surface is `git archive <commit> corpus`, which **excludes `.ufo/`** — no check in `corpus/` or `reports/` reads `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` (only the derive script's docstring mentions it, `derive_axml_anchors.py:14`).

Assessment: **not a live drift** (equality verified now, both files in-repo, three coordinated edits would be visible in any diff) — but the "byte-exact copy of the pinned snapshot" is a one-shot prose-asserted fact, not a re-runnable check. One sentence in §Limitations should say so, so no seat treats the copy-vs-original equality as re-checked.

## Impacted axes and owners

- **C2 / Q11** — cannot be an unqualified PASS on the derived-not-transcribed clause: D1 (the assertion is false) and D3 (237, 244 unlabelled) are exactly Q11's fail conditions (`QUALITY.md:23`: "a value is correct when re-derived but the entry carries no derivation, or a recorded value is presented as re-derived"). Seats: `R68ReviewEntryQ11`, `R68ReviewEntryQ02`.
- **C2 / Q02** — passes today (header `:245` is correct), but the gate does not protect that site (D2). `R68ReviewEntryQ02` should audit the header against item 11 explicitly, since the mechanical capture cannot.
- **S046 row** — the 17-line count and script digest are accurate as written (`SOURCES.md:61`, entry line 4); the gap is that the row sells "the machine derivation of every … line number the entry cites", which the entry does not currently meet for 237/244 and for every prose restatement. `R68ReviewSourcesS046`.
- **Snapshot fidelity** — `R68SnapshotFidelity` should record copy↔original as verified-once via sha/`cmp`, not as a checked invariant.
- **Settlement wording** — `C7_V3_CLEAN` is a text-match label (spoof proof above); do not narrate it as provenance.

## Smallest safe correction (ordered; none harms an axis)

1. **Prose-only, zero new machinery (smallest).** Remove the duplicated spec numbers from lines 1, 57, 82, 148 — name the symbol and point at item 11 instead — and label **237** and **244** at line 148 as *recorded* (the derivation does not print them). This makes line 125's assertion TRUE, deletes the surface where M40/M44 has now twice survived, and keeps Q02's "exact anchor" (S038 row + symbol name + item 11's derived line). The disambiguating sentence at line 148 must survive in some form — it is what stops a future author re-writing `:244` — so keep "line 245 is `RES_XML_START_NAMESPACE_TYPE`; `RES_XML_FIRST_CHUNK_TYPE` is the preceding line and carries the same value `0x0100`", which is byte-checkable and now labelled recorded.
2. **Preferred if budget allows.** Add 2–3 lines to the derive output that print *content*, not just numbers (`neighbor 244 RES_XML_FIRST_CHUNK_TYPE`, `block-open 237 enum {`, `block-close 253 RES_XML_RESOURCE_MAP_TYPE`), then quote them verbatim in item 11 — 237 and 244 become gate-pinned and the capture becomes self-evidencing. **Three coupled updates are required or the gate turns red**: the entry's block (item 11), the derive-script sha256 at `SOURCES.md:61` and entry line 4, and the "17 output lines" count in both places. `checked_blocks` stays 17 (the gate counts blocks, not lines) and no frozen C2 label pins the line count.
3. **AVOID.** Extending the gate to cross-check prose anchors against a derived table: new machinery, couples the gate to one entry's shape, and Q13 ("no automatic checker introduced") is the criterion this lane has been trained on. Not needed for the two fixes above.

## Things verified clean (so the L1 does not re-open them)

- Item 11 verbose block is a faithful capture: 17/17 lines, exact, ordered; reproducible from a corpus-only tree at HEAD `4232235`.
- The derivation cannot fabricate a line number (shift/delete/duplicate tests) and is not a tautology (shift prints 250).
- All 15 prose spec numbers are correct against the bytes *today*; the defect is coverage and labelling, not present wrongness.
- Build state is committed: `git cat-file -e HEAD:{corpus/derive_axml_anchors.py,corpus/snapshots/ResourceTypes.h,corpus/knowledge/round-68-apk-axml-byte-evidence.md}` all present; HEAD `4232235723cf…` "round-68: build — C7 gate attribution repair".
- Observation only, not mine to touch: an untracked `corpus/__pycache__/` exists in the lane (`git status --porcelain corpus/`); it is excluded by `git archive`, so it cannot reach the measured tree.
