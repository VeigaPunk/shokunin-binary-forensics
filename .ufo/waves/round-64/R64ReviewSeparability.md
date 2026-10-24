# R64ReviewSeparability — C1/C2 causal separability on the frozen round-64 counter

Seat: revenger-r64.R64ReviewSeparability (reviewer; independent leaf). Date 2026-10-24.
Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. No git/jj mutation was run
(`git status`, `git log`, `git show`, `git diff`, `git archive` reads only). Nothing was
written in the lane except this report; all trees live under `/tmp/revenger-r64-sep/`.

## Verdict

Separability **holds** on the frozen counter: C1 (entry + C07 flip) moves only the five
coverage labels; C2 (the two 3-line verifier patches) moves only
`C4_RECEIPT_KILLED_ATTRIBUTED`; neither moves the other's labels, and only the two together
give `HOLDS_OK_V2=yes`. Two defects sit outside the claims themselves: **the brief's tree
(a) is unsatisfiable as written** (the entry file alone moves nothing; 8/14 requires the
C07 row flip), and **`K_HELD_BACKED_STRICT`'s rejected-marker test is blind to the actual
candidate draft**, whose `admission-status:` header is at byte 4155 of a 2000-byte scan
window. Neither falsifies C1 or C2; both change what may honestly be claimed.

## Frozen inputs (verified byte-identical, no tampering)

| artifact | sha256 | check |
|---|---|---|
| `reports/round-64/measure.py` | `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168` | equals `git show 3bb430f:` blob; worktree == HEAD |
| `reports/round-64/claims.md` | `fdd7312e27d1b9c9180accb75fee4aed214c8fa938eb33444f02a82334f3cf3a` | equals `3bb430f:` blob |
| `reports/round-64/measure-before.log` | `8116b216d543984bfb60c6331defae43f384f5c94904658afb8997b8692a1003` | equals `3bb430f:` blob |

Base tree: `git -C <lane> archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus |
tar -x -C <tree>` (486 archive files == 486 extracted). `git diff --stat 666ea84 a3d063f --
corpus/` is empty, so base-commit corpus == HEAD corpus; the only corpus mutation in the
working tree is `M corpus/verify_icon_languages.py` + `M corpus/verify_multi_icon_states.py`
(the C2 patches).

## Trees built under `/tmp/revenger-r64-sep/` and results

Counter invocation (identical for every tree, cwd `/`, lane-owned TMPDIR):
`TMPDIR=/tmp/revenger-r64-sep/tmp/<tree> python3 -B <lane>/reports/round-64/measure.py
/tmp/revenger-r64-sep/<tree>`. Logs: `/tmp/revenger-r64-sep/<tree>.log`. Every run exited
**0** — exit is driven by round-63 `HOLDS_OK`, not V2 (finding 5) — so labels, not status,
is the evidence. 17 counter runs over 19 trees (the two `real_*` trees are byte-identical
copies used only for an identity check).

| # | tree | contents | K_HELD | K_ROW C07 | K_HELD_BACKED | STRICT | MISMATCH | C4_ATTRIB | HOLDS_OK | V2 |
|---|---|---|---|---|---|---|---|---|---|---|
| c | `neither` | base archive only | 7/14 | frontier | 7/14 | 7/14 | 1 | 0/2 | yes | no |
| a-literal | `entry_only_raw` | + stand-in entry, **README untouched** | 7/14 | frontier | 7/14 | 7/14 | 1 | 0/2 | yes | no |
| a-literal-real | `draft_entry_only` | + **real candidate draft**, README untouched | 7/14 | frontier | 7/14 | 7/14 | 1 | 0/2 | yes | no |
| a-corrected | `entry_admitted` | + stand-in entry + C07 flip citing it | **8/14** | **held** | **8/14** | **8/14** | **0** | 0/2 | yes | no |
| a-corrected-real | `draft_admitted` | + real draft + C07 flip citing it | **8/14** | **held** | **8/14** | **8/14** | **0** | 0/2 | yes | no |
| b | `patch_only` (= `real_patch`) | only the two C4 patches | 7/14 | frontier | 7/14 | 7/14 | 1 | **2/2** | yes | no |
| a+b-real | `draft_admitted_patch` (`draft_admitted` + patches) | real draft + flip + patches | 8/14 | held | 8/14 | 8/14 | 0 | 2/2 | yes | **yes** |
| live | `live_asis` | copy of lane working-tree corpus at review time (entry + patches, README still `frontier`) | 7/14 | frontier | 7/14 | 7/14 | 1 | 2/2 | yes | no |
| live+flip | `live_admitted` | `live_asis` + C07 flip citing the integrated entry | 8/14 | held | 8/14 | 8/14 | 0 | 2/2 | yes | **yes** |
| d1 | `token_only` | C07 flipped `held`, **no citation, no entry** | 8/14 | held | 7/14 | 7/14 | 0 | 0/2 | yes | no |
| d2 | `uncovered` | C07 flipped `uncovered` only (fallback) | 7/14 | uncovered | 7/14 | 7/14 | 0 | 0/2 | yes | no |
| d3 | `strict_early` | stand-in marked `rejected` at byte 31 | 8/14 | held | 8/14 | **7/14** | 0 | 0/2 | yes | no |
| d4 | `strict_late` | stand-in marked `rejected` at byte 3406 | 8/14 | held | 8/14 | **8/14** | 0 | 0/2 | yes | no |
| d5 | `draft_rejected_prefix` | **real draft**, `rejected` at byte 0 | 8/14 | held | 8/14 | **7/14** | 0 | 0/2 | yes | no |
| d6 | `draft_rejected_natural` | **real draft**, `candidate`→`rejected` at byte 4155 | 8/14 | held | 8/14 | **8/14** | 0 | 0/2 | yes | no |
| d7 | `fallback_plus_patch` | `uncovered` flip + both patches | 7/14 | uncovered | 7/14 | 7/14 | 0 | 2/2 | yes | **yes** |

Base reproduction: every non-MUTANT/non-HOLD line of `neither.log` diffs **empty** against
`reports/round-64/measure-before.log` (7/14 backed, strict 7/14, mismatch 1 `['C07']`, C4
0/2, C2/C3 2/2, HOLD 4/4 and 10/10, FRESH 18/18, F 5/8, SAVED_RECORDS 59). `draft_entry_only`
diffs empty against `neither` on all labels — **the entry file's presence, and its real
content, change no printed label** until the README row flips.

## Tree construction

- **C2 patch.** Authored from the frozen fix shape, then proven **byte-identical (sha256) to
  the current lane working-tree files**: `corpus/verify_icon_languages.py`
  `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3`,
  `corpus/verify_multi_icon_states.py`
  `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e`; `diff -r` of
  `patch_only` vs `real_patch` and `both` vs `real_both` is clean. One control line per file
  (`grep -c` = 1). Inserted after the existing forged-command control in `check(...)`:

```diff
@@ verify_icon_languages.py:151
+    forged_stdout=copy.deepcopy(receipt)
+    forged_stdout['stdout_sha256']=H(b'')
+    require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
@@ verify_multi_icon_states.py:150
+    forged_stdout = copy.deepcopy(receipt)
+    forged_stdout['stdout_sha256'] = H(b'')
+    require(not receipt_ok(forged_stdout, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt stdout accepted')
```

- **C1 entry.** The scribe draft was located at `/tmp/revenger-r64-entry/candidate.md`
  (48,440 bytes, sha256 `0a3730a1a03b19ef134930a8eb180147be8b6e503fbd7040fdd7617eafed0a22`,
  header `admission-status: candidate`), copied **unmodified** to
  `corpus/knowledge/round-64-firmware-region-byte-evidence.md` in the draft trees. The
  stand-in trees use a 410-byte zero-claim placeholder that says it is not an evidence entry.
  In `*_admitted*` trees the README delta is exactly one line (`diff -u` shows only C07),
  citing that single path, work evidence `fixtures/firmware-r63` +
  `live/runs/round-63/inspection.json`, status `held`. The flip simulates L1's final
  integration step; the draft itself says "the README C07 status flip belongs to L1".

### Attribution evidence (the point of C2)

Base: `MUTANT verify_icon_languages.py c4 exit=0 pass` and `MUTANT verify_multi_icon_states.py
c4 exit=0 pass` (0/2). With the real patch:

```
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
```

Both kills end with the registered endswith string and are produced by the new control only:
the forged copy changes `stdout_sha256` alone, the genuine-receipt check still passes, and the
earlier forged-command control does not fire. Neighbouring labels are unchanged by the patch
in every patched tree: `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`,
`C2_D2_KILLED=2/2`, `C3_* =2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`,
`FRESH_ROWS=18/18`, `F_COVERAGE=5/8`, `SAVED_RECORDS=59`; C2 mutant b still ends
`forged receipt command accepted`, so attribution stays distinct per conjunct.

## Findings

**1. MEDIUM — brief tree (a) is unsatisfiable as written.** The brief asks for "only the C07
candidate entry file (no verifier patch, README untouched) — expect K_HELD_BACKED 8/14".
`K_HELD_BACKED` iterates `held` rows only (`measure.py:28-34`, regex `\| held \|$`), and all
seven held rows are already backed at base. A file cannot add a held row: both
`entry_only_raw` (stand-in) and `draft_entry_only` (real draft) print exactly the base
labels — zero diff — so the observed value is 7/14, never 8/14. With the README flip
(`entry_admitted`, `draft_admitted`) the labels move exactly as the contract predicts
(8/14 backed, C07 held, strict 8/14, mismatch 0, C4 0/2). A seat executing the brief
literally will log a false failure; adjudication should define (a) as entry file + C07 row
flip citing it, or restate the literal expectation as 7/14.

**2. MEDIUM — the rejected-marker guard is inert for the actual candidate.** `rejected_marked()`
tests only `read_text(...)[:2000]` (`measure.py:38-41`). The real candidate's header block
(`source:` ×2, `verified-at:`, `recheck:`, `coverage-map:`) is long and its
`admission-status:` line sits at **byte 4155**. With the row `held` and the draft's marker
changed from `candidate` to `rejected` in place, the counter prints
`K_HELD_BACKED=8/14` and `K_HELD_BACKED_STRICT=8/14` (`draft_rejected_natural`) — no
discrepancy, so a rejected entry still backs the row. Prefixing the same marker at byte 0
(`draft_rejected_prefix`) correctly yields strict 7/14 vs backed 8/14. This is not contrived:
the natural layout of a sourced entry pushes `admission-status:` past 2 KB, and this is the
only named mechanism for excluding rejected entries from K backing. Fix: scan the whole file
(or the whole header block) for the marker. Until then, L1 must not present strict==backed
as evidence that the C07 entry is not rejected.

**3. LOW — `K_HELD`/score is token-gameable; only `K_HELD_BACKED` is admission evidence.**
`token_only` flips C07 to `held` with a `—` knowledge column and no entry: the counter prints
`K_HELD=8/14 score=5.7` and `README_TOKEN_LEGEND_MISMATCH=0` while `K_HELD_BACKED=7/14`.
The score line and the mismatch label therefore cannot be quoted as C1 evidence; adjudicate
C1 on `K_HELD_BACKED=8/14` + `K_ROW C07 status=held` + the cited file present (SCORECARD:199
already uses the backed label; this is reporting hygiene, not a contract change).

**4. LOW — `HOLDS_OK_V2=yes` does not imply C1 admission.** `fallback_plus_patch` (C07 flipped
to `uncovered`, both patches) prints K 7/14, C4 2/2, mismatch 0, `HOLDS_OK_V2=yes`. That is
contract-consistent (the fallback flip is authorized and clears M36), but the round-end green
V2 gate can be reached with C1 falsified; only the K labels discriminate the branches.

**5. INFO — probe exit code encodes neither claim.** `measure.py:273` exits on round-63
`holds_ok` only; it omits `c4_attributed` and `len(mismatch)`. Base and patched runs both exit
0 while C4 is 0/2 vs 2/2. "probe exit 0" is not admission evidence (consistent with
`measure-before.log`, which is exit 0 at C4 0/2).

**6. DEPENDENCY (updated, resolved in content) — the draft exists but is not integrated.**
`/tmp/revenger-r64-entry/candidate.md` (sha256 `0a3730a1…`, `admission-status: candidate` at
byte 4155) is the scribe artifact; no
`corpus/knowledge/round-64-firmware-region-byte-evidence.md` exists at HEAD `a3d063f` or in
the lane working tree, and the README C07 row is still `frontier`. The entry exists only in
scratch, so the "real" end state is not yet legally constructible; the `draft_*` trees use the
draft verbatim to remove content as a variable. Transfer to the integrated artifact is
conditional on: (i) the file landing at exactly
`corpus/knowledge/round-64-firmware-region-byte-evidence.md`; (ii) the C07 row citing that
path in the knowledge column and ending `| held |` (trailing space or a second cited
`knowledge/*.md` path that does not exist drops backed to 7/14); (iii) no other README row
changing (denominator stays 14). Q01–Q13 admission quality was not assessed here.

**7. INFO — the C2 half is already in the working tree and matches the frozen shape.** The two
modified files are byte-identical to the independently authored patch; no other corpus file is
modified; the verifier census stays at 10 (`HOLD_REPLAY=10/10`).

## Integration checks for the committed end state

`K_HELD=8/14 score=5.7`; `K_ROW C07 status=held`; `K_HELD_BACKED=8/14`;
`K_HELD_BACKED_STRICT=8/14`; `README_TOKEN_LEGEND_MISMATCH=0 rows=[]`;
`C4_CONTROLS_PASS=2/2`; `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`; `HOLD_CALIBRATION=4/4`;
`HOLD_REPLAY=10/10`; `FRESH_ROWS=18/18`; `F_COVERAGE=5/8`; `SAVED_RECORDS=59`;
`HOLDS_OK=yes`; `HOLDS_OK_V2=yes`; exit 0. Do not cite `HOLDS_OK_V2` or exit 0 alone
(findings 4, 5), and do not cite strict==backed as a rejection check until finding 2 is fixed.

## Residual risk

- Within these two scripts, the `evidence_id`, `fixture_sha256` and `exit_code` conjuncts of
  `receipt_ok` still lack in-script forged controls (the new control covers `stdout_sha256`
  only; C3's clauses live in different scripts). No claim covers them; same M35 argument.
- The control pins `H(b'')`. If a future `inspection.raw.json` were empty, the forged value
  would equal the genuine one and the control would fail spuriously; all current raw records
  are non-empty JSON, so this is latent.
- `README_TOKEN_LEGEND_MISMATCH` moves on either C07 flip, so it cannot date or attribute the
  flip; the round report must name the branch taken (held vs uncovered).

## Verification gaps

- No integrated end state exists (finding 6); the flip in the `*_admitted*` trees is a
  reviewer simulation of L1's step, and the draft content itself was used only as an
  existence/citation artifact, not reviewed for evidence quality (other seats' Q01–Q13 scope).
- No `lsp` server was used: the affected "callers" are two self-test scripts and a frozen
  single-file Python counter, both read end-to-end; definition/reference queries would add
  nothing beyond those full-text reads.
- Runs are fast (1.1–1.7 s each; one self-test measured at 22 ms), so no timing truncation.

## Tooling

No installs or upgrades (host pacman pause respected; no uv/npx/official-binary downloads).
Scratch: `/tmp/revenger-r64-sep/` — base archive copy, 17 trees, 15 counter logs, per-tree
TMPDIR under `/tmp/revenger-r64-sep/tmp/`; lane-owned, remove on landing.
