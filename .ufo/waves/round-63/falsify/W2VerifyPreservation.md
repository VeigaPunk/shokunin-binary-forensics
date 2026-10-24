# W2VerifyPreservation — corpus/live + corpus/fixtures byte preservation

## Scope, axes, and result

Reviewer: `revenger-r63.W2VerifyPreservation` (independent leaf). Primary axis: **calibration** of the preservation guard — does the committed tree actually preserve every baseline byte, and does it admit only the declared additions? Preserved observation axes: C1 knowledge bytes (not reviewed here), C2 record envelope (adjacent observation only), C3 script delta scope (scope check only, no C3 verdict).

**Result: PASS. No BROKEN condition, no unauthorized modification, no unexpected addition.**

- All **443/443** baseline `corpus/live` + `corpus/fixtures` paths are byte-identical to the requested baseline `55bcb6e`, verified twice: (a) manifest check, and (b) an independent `git archive 55bcb6e` extraction compared raw file-by-file, bypassing the manifest entirely.
- Exactly **9 additions**, all and only under `corpus/fixtures/firmware-r63/` (3) and `corpus/live/runs/round-63/` (6). No deletions, no renames, no untracked files, no `__pycache__`/`.pyc`.
- `corpus/verify_*.py` count is **exactly 10**; exactly the **two** C3 targets differ from `55bcb6e`, and the eight others are byte-identical. The two diffs are the C3 receipt-guard refactor + forged-receipt control only.
- The three non-identical rows in `preservation-base.sha256` (both C3 scripts + `corpus/SOURCES.md`) are exactly the three declared carve-outs; nothing else in the manifest deviates.

## Committed inputs

- Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, tip `db55bd6488e24e956df5818ae34c2a043d7ddc12` (`git rev-parse HEAD`), read-only inspection only.
- Baseline: `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`; confirmed ancestor of HEAD (`git merge-base --is-ancestor` → true).
- Manifest: `.ufo/waves/round-63/build/preservation-base.sha256`, sha256 `2f462c31e948eddaec4737c49bc85f52c2a82773289a04d0dddc858cd8e377b6`, 455 rows. Blob at HEAD and at `2a34e45` both `fae74c5622e7ea74c280efa0bf57f6cc20ff1e55`; working copy clean (`git diff --stat HEAD --` empty).
- Manifest composition (matches `build/R63Preservation.md`): rows 1–443 = sorted `find corpus/live corpus/fixtures | sort | xargs sha256sum` capture; rows 444–455 = 10 verifiers + `corpus/README.md` + `corpus/SOURCES.md`.
- Manifest first-443 path set vs `git ls-tree -r --name-only 55bcb6e -- corpus/live corpus/fixtures`: identical (`diff` empty).
- Capture-claim coherence: `git diff --name-status 55bcb6e 54ab973 -- corpus/live corpus/fixtures` is empty, so the requested baseline and the capture HEAD had identical live/fixtures bytes; the manifest's row anchoring is not a mixed-state artifact.
- Tools: system `sha256sum`, `git`, `find`, `comm`, `diff` only. **No installs, no updates, no pacman transaction, no target execution, no model arguments, no config edits.** Scratch: `/tmp/r63-*` only.

## Evidence

### 1. Guard rows — `sha256sum -c` against the committed manifest

```
$ sha256sum -c .ufo/waves/round-63/build/preservation-base.sha256
corpus/verify_icon_states.py: FAILED
corpus/verify_named_multi_icon_states.py: FAILED
corpus/SOURCES.md: FAILED
sha256sum: WARNING: 3 computed checksum(s) did NOT match
```

452 OK / 3 FAILED. The 452 OK comprise all 443 live/fixtures holds plus 9 of the 12 supplemental rows (`corpus/README.md` + 8 untouched verifiers).

### 2. Independent proof — raw bytes vs extracted `55bcb6e` (manifest bypassed)

```
$ git archive 55bcb6e corpus/live corpus/fixtures | tar -x -C /tmp/r63-pres-verify
# extracted tree: 443 files; manifest first-443 rows: 0 mismatches (sha256sum -c)
# current tree minus the 9 declared additions: 443 files
$ diff <(sort extracted) <(sort current-minus-additions)
→ identical, exit 0  ⇒ ALL_443_BYTE_IDENTICAL
```

This closes the "poisoned manifest" attack: the manifest's 443 rows are not merely self-consistent, they equal the baseline commit's blobs, and the working tree equals those same bytes.

### 3. Additions — exactly the two allowed prefixes

`git diff --name-status 55bcb6e HEAD -- corpus/live corpus/fixtures` → 9 lines, all `A`:

```
A corpus/fixtures/firmware-r63/firmware-r63.bin
A corpus/fixtures/firmware-r63/generator.py
A corpus/fixtures/firmware-r63/truth.json
A corpus/live/runs/round-63/LEDGER.md
A corpus/live/runs/round-63/inspection.json
A corpus/live/runs/round-63/oracle_check.py
A corpus/live/runs/round-63/receipt.json
A corpus/live/runs/round-63/stderr.txt
A corpus/live/runs/round-63/stdout.raw
```

Tracked file counts: `55bcb6e` = 443, HEAD = 452, working tree (`find`) = 452. `git status --porcelain --untracked-files=all corpus/` reports no `??` entries. Full corpus diff since baseline contains only the 9 `A` rows plus `M corpus/SOURCES.md`, `M corpus/verify_icon_states.py`, `M corpus/verify_named_multi_icon_states.py`, `A corpus/knowledge/round-63-zip-central-directory-evidence.md`, `A corpus/lessons/round-63.md` — i.e. no deletion, rename, or hidden addition anywhere in `corpus/`.

### 4. Verifier deck — 10 scripts, exactly 2 differ from baseline

Per-file `git show 55bcb6e:<path> | sha256sum` vs working file:

| Script | vs 55bcb6e |
|---|---|
| verify_evm_evidence.py | SAME |
| verify_icon_languages.py | SAME |
| **verify_icon_states.py** | **DIFF** `acbf47bb…` → `7cbd931a…` |
| verify_js_graph_delta.py | SAME |
| verify_multi_icon_states.py | SAME |
| **verify_named_multi_icon_states.py** | **DIFF** `b62441d5…` → `a226bf73…` |
| verify_pe_resources.py | SAME |
| verify_saved_evidence.py | SAME |
| verify_semantic_trace.py | SAME |
| verify_shape_evidence.py | SAME |

Diff scope: `verify_icon_states.py` +20/−4 (extracts `receipt_ok(...)`, adds deep-copied forged-`fixture_sha256` control raising `forged receipt accepted`); `verify_named_multi_icon_states.py` +9/−1 (same `receipt_ok` extraction + forged-receipt `req`). No other logic touched in the shown hunks. No non-`.py` `verify_*` file exists at `corpus/` root.

### 5. Declared carve-outs (the only 3 manifest deviations)

| Row | Base digest | Current | Authorization |
|---|---|---|---|
| `corpus/verify_icon_states.py` | `acbf47bb…` (= `55bcb6e` blob) | `7cbd931a…` | C3 patch, `build/R63C3IconPatch.md` |
| `corpus/verify_named_multi_icon_states.py` | `b62441d5…` (= `55bcb6e` blob) | `a226bf73…` | C3 patch, `build/R63C3NamedPatch.md` |
| `corpus/SOURCES.md` | `e517ec93…` (= `55bcb6e` blob) | `c075f900…` | S032/S033 rows, +4/−0 pure append, lands in the pre-wave integration commit |

`corpus/README.md` is byte-identical to baseline (`7ccd8d44…`), consistent with "README stays partial until this wave's pass decisions."

## Findings

**Blocking / BROKEN:** none.

1. **Info — literal target wording vs declared carve-outs.** "Every base file must be byte-identical" cannot be satisfied literally without also failing C3 (2 scripts) and the S032/S033 rows, both of which the wave itself requires. The build note declares the 12 supplemental rows non-unconditional holds and the 443 live/fixtures rows unconditional. Under that declared split the guard is green: **443/443 holds, 9/12 supplemental holds, 3/12 authorized changes**. Any reader applying the literal sentence to the supplemental rows would mis-flag authorized work; the manifest is a mixed-scope document and should be read with `R63Preservation.md` §"Base-state reconciliation and guard scope".
2. **Low — manifest scope gap.** `corpus/QUALITY.md`, `corpus/knowledge/**`, and `corpus/lessons/**` are in no byte guard. `QUALITY.md` was separately checked against baseline and is identical (`811ebf73…` both), but knowledge/lessons protection rests entirely on C1's own review, not on this manifest. Recommend a follow-on base that covers all of `corpus/`.
3. **Low — worktree is dirty outside my guard.** `git status --porcelain corpus/` → ` M corpus/lessons/round-63.md` (1 insertion, 6 deletions; committed `ce7b47e8…` vs worktree `3d6f643c…`), an in-progress sentence correction of the rev1/rev2 attribution. It is outside `corpus/live`/`corpus/fixtures` so preservation is unaffected, but the tip's committed lesson bytes do not equal the working file — relevant to `W2VerifyLessonGate` and to the integration commit.
4. **Info — adjacent C2 observation, not a verdict.** `corpus/live/runs/round-63/inspection.json` and `stdout.raw` are byte-identical (`f6997835…`), and `receipt.json`'s `stdout_sha256` matches both while its `fixture_sha256` (`bdfe9f46…`) matches the committed `firmware-r63.bin`. The envelope is internally hash-consistent; whether the bytes are genuine producer output or a copy of the saved record is `W2AttackOracle`'s call, not decided here. `stderr.txt` is 0 bytes.

## Residual risk

- The guard proves bytes, not provenance: a run artifact committed whole (as here) can still be forged consistently. That is C2's oracle problem; preservation cannot detect it.
- The 12 supplemental rows are unguarded by design; future waves could alter README/SOURCES/8 verifiers silently. For *this* wave the delta is fully pinned by the `55bcb6e..HEAD` corpus diff above (only the 3 authorized files).
- No execution of verifiers, oracle, or fixtures was performed (no target execution permitted), so no runtime claim is made about the C3 scripts' self-tests.

## Verification gaps

- `lsp` not applicable: the object of proof is file-byte identity, not symbols or references; no server consulted and none needed.
- Manifest row ordering was validated as a set against `git ls-tree`; the capture's exact byte ordering of rows 1–443 was not re-derived (`find|sort` reproducibility was not re-run against `55bcb6e`'s checkout, only against the extracted archive, which is equivalent for content).
- The dirty `corpus/lessons/round-63.md` was observed mid-wave; its final bytes will differ from what is recorded here and belong to the lesson seat.
