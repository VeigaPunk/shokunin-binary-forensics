# R64LessonDraft — round-64 lesson draft

Seat `revenger-r64.R64LessonDraft` (scribe, leaf). Round 64 / attempt 1, lane
`revenger-shokunin`, claim base `666ea84b6be2eec2b0359f556ba2429fc9044c36`.
Absolute lane paths only; read-only work.

## Behavior

Drafted `corpus/lessons/round-64.md` at the brief's scratch path
**`/tmp/revenger-r64-lesson/round-64.md`** (17,852 bytes, 213 lines). L1 lands
it; this seat wrote nothing under `corpus/` and made no integration decision.

The draft carries, per brief:

- **Frontmatter** — `round: 64`, `date: 2026-10-24`, `author: revenger-r64`,
  `claims: [C1, C2]`, `contract: reports/round-64/claims.md`, `counter:
  reports/round-64/measure.py (frozen; sha256
  b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168)`, plus
  `lane`, `claim_base`, and `status: draft for L1 — build-wave evidence only;
  no admission is claimed by this file` (same guard line as round 63).
- **Red-before receipt** — the target-relevant lines of
  `reports/round-64/measure-before.log` quoted verbatim
  (`K_HELD=7/14 score=5.0`, `K_ROW C07 status=frontier`,
  `K_HELD_BACKED=7/14`, `K_HELD_BACKED_STRICT=7/14`, `SAVED_RECORDS=59`,
  `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `F_COVERAGE=5/8 score=6.2`,
  `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`,
  `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`,
  `HOLDS_OK_V2=no`), the four frozen C4 mutant lines proving red-before on the
  exact mutation, and a statement that the log is the do-nothing control.
- **`## Gate`** — fill blocks only: `S036_URL/HTTP/BYTES/SHA256/SNAPSHOT/
  PROVENANCE/QUOTES` and `S037_FIRMWARE_BIN/TRUTH_JSON/GENERATOR_PY/
  INSPECTION_JSON/RECEIPT_JSON/LEDGER_MD_SHA256`. Pinned S036 URL and its
  documented 404 fallback are recorded from brief `R64SourceReaGuide`; the
  quote-fill instruction requires ≤25-word verbatim quotes with snapshot line
  numbers covering route behavior, the binwalk 3.1.x / unblob 26.6.x
  requirement, and any entropy/signature-scan sentence.
- **`## Mistakes`** — M36 only, class *self-assessment drift*: token
  `frontier` vs legend “no knowledge and no saved record”; evidence
  `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']` committed in
  `reports/round-64/measure-before.log` at base `666ea84b`; captured-by
  **none** (no committed check; round-63 sightings were prose); fix = the
  registered label in `reports/round-64/measure.py`, shown able to fail at 1
  at base and required 0 at round end.
- **`## Routed debt`** — all seven `claims.md` inputs dispositioned plus the
  S036 id note: (1) later counter registers `K_HELD_BACKED_STRICT`,
  `README_TOKEN_LEGEND_MISMATCH`, `HOLDS_OK_V2`; (2) M35 → C2 with the frozen
  mutation/fix/endswith-attribution rule; (3) C07 repaired inside C1, flip
  either way; (4) transplant corollary owner named — 3-part binding-check
  shape (recomputed digests, `receipt.evidence_id == record.evidence_id ==`
  LEDGER ID, forged foreign-ID transplant control), Q09 disclaimers carried;
  (5) r58/59 `139` quotes stay unedited, **non-reproduction recorded** against
  the base log's `PASS: 142 positive checks`, re-derivation owner named;
  (6) freshness wording frozen in `claims.md`; (7) SHONEN box 1 checklist rule
  only, no verdict; (8) S036 first-use-wins, zipfile-docs note recorded as a
  note, not a reservation.
- Also included: `### Candidate status at draft time` (C1 candidate not
  landed; C2 working-tree controls observed), frozen admission order, quality
  criteria (Q01–Q13 unchanged, ten-verifier census), a one-line search-log
  placeholder, and `## Tooling`.

## Gates / checks run (read-only)

| check | command | outcome |
|---|---|---|
| frozen counter digest | `sha256sum reports/round-64/measure.py` | `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168` |
| contract digest | `sha256sum reports/round-64/claims.md` | `fdd7312e27d1b9c9180accb75fee4aed214c8fa938eb33444f02a82334f3cf3a` |
| red-before digest | `sha256sum reports/round-64/measure-before.log` | `8116b216d543984bfb60c6331defae43f384f5c94904658afb8997b8692a1003` |
| registry census | `awk -F'|' '/^\| S[0-9]/{n++} END{print n}' corpus/SOURCES.md` | `rows=35 last=S035` |
| S036 unused | `grep -c 'S036' corpus/SOURCES.md` | `0` (grep exit 1) |
| id rule | `grep -n -i 'id\|lead' .ufo/waves/kaika/SOURCES-CONTRACT-v1.md` | `:22` next unused, never reused; `:16` “a lead is not evidence and never a row” |
| C4 controls present | `grep -n 'forged receipt stdout accepted' corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py` | `verify_icon_languages.py:154`, `verify_multi_icon_states.py:153` |
| C4 red-before | `for f in corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py; do git show 666ea84b:$f \| grep -c 'forged receipt stdout accepted'; done` | `0` and `0` |
| working-tree state | `git status --porcelain -- corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py` | both `M` |
| draft structure | placeholder/pipe/section scan | 13 placeholders (7 S036, 6 S037) plus 1 search-log token; tables at 4/6/4 pipes; sections present |

`git show` and `git status` were the only git invocations; both read-only, no
mutation, no index write, no commit.

## Touched surfaces

- **Written:** `/tmp/revenger-r64-lesson/round-64.md` (scratch deliverable);
  this report `.ufo/waves/round-64/R64LessonDraft.md`.
- **Read only:** `reports/round-64/{claims.md,measure.py,measure-before.log}`,
  `corpus/SOURCES.md`, `corpus/README.md`, `corpus/lessons/round-63.md`,
  `corpus/lessons/round-63-verifier-spotcheck.md`,
  `.ufo/waves/round-63/{build/R63SourceZipfileDocs.md,falsify/routed-debt.md}`,
  `.ufo/waves/round-64/briefs/{R64LessonDraft.md,R64SourceReaGuide.md}`,
  `.ufo/waves/round-64/R64C4LangPatch.md`, `R64C4MultiPatch.md`, the two C4
  verifier scripts, and the S037 bundle files (hashing only).
- **Not touched:** nothing under `corpus/` was written; no `.ufo/waves` spec or
  registry file; no `MANIFEST.json`; no fleet/sibling lane; no jj state; no Git
  index.

## Out of scope (not claimed)

- Did not open S036 or any web source; did not fetch the REA guide.
- Did not run `reports/round-64/measure.py` or any verifier self-test; did not
  run the frozen mutants.
- Did not land the lesson, edit the README, append SOURCES rows, or adjudicate
  any claim.
- No outside spot-check, no quality-verdict.

## Findings

1. **S036 id conflict is resolvable and is recorded.** Round 63's D4 note says
   “A future zipfile-docs row takes **S036**”
   (`.ufo/waves/round-63/falsify/routed-debt.md:156`; origin
   `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:251-256`), while
   `reports/round-64/claims.md:41` opens S036 for the REA firmware guide. The
   contract gives no reservation mechanism: id = “the next unused; never
   reused” and “a lead is not evidence and never a row”
   (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:22,:16`). Registry ends at S035
   with 35 rows, so S036 is this round's by first use; the draft records the
   old note as a note, not a reservation, and names no future id.
2. **`measure-before.log` has no exit-code line.** The contract calls it a
   probe exit 0 receipt, but the file prints no `PROBE_EXIT`. The draft states
   this explicitly so a closure seat does not read the absence as a failed
   probe. All target lines quoted from it match the contract's numbers.
3. **C4 file state at draft time.** Both controls are in the working tree at
   the brief's frozen shape; base commit `666ea84b` has zero occurrences; both
   files show `M`. Seat reports diverge on execution: `R64C4LangPatch` ran
   `python3 -B corpus/verify_icon_languages.py --self-test` (exit 0, PASS line
   quoted); `R64C4MultiPatch` did **not** run its self-test (executor policy,
   parent owns post-integration verification). Attributed 2/2 is therefore
   still a final-gate measurement, and the draft says so.
4. **r58/59 count non-reproduction is evidenced, not asserted.** The base log
   prints `PASS: 142 positive checks; …` for `verify_named_multi_icon_states.py`,
   so a historical quote of 139 is stale at round 64; the draft records the
   quote as unedited history and names the re-derivation owner.
5. **S036 snapshot does not exist yet.** `.ufo/waves/round-64/source-snapshots/`
   is absent at draft time (directory listing empty), so the Gate fill blocks
   and `R64SourceReaGuide`/`R64ScribeGate` are hard dependencies for landing;
   the lesson is not landable with placeholders unfilled, and the draft says so
   in-line.
6. **Provisional S037 digests observed by this seat** (from the working tree at
   base, `sha256sum`; offered to the gate seat as a cross-check only — **not**
   Gate evidence, and deliberately left as placeholders in the draft):
   - `firmware-r63.bin` (2048 B) `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`
   - `truth.json` (1933 B) `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6`
   - `generator.py` `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4`
   - `round-63/inspection.json` (3904 B) `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`
   - `round-63/receipt.json` (492 B) `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d`
   - `round-63/LEDGER.md` (22671 B) `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6`
7. **M36 label mechanics verified in the frozen counter**, not inferred:
   `reports/round-64/measure.py:51-78` collects `operation` from every
   `corpus/live/runs/**/*.json` dict, intersects with the printed `ROW_OPS`
   map, and flags rows whose last cell is `frontier`. The base log prints the
   same `ROW_OPS` and `SAVED_RECORDS=59`, so the 1-at-base failure is
   reproducible by reading the committed receipt alone.
8. **Minor contract/brief divergence, reported verbatim:** the brief asks for
   “placeholders for S036/S036-quotes and S037 digests”; the draft keeps S037
   as placeholders even though this seat could compute them, because a landed
   lesson must not carry values that look like the gate seat's receipt. The
   computed values are in finding 6 above instead.
9. **No tool installs.** No `pacman` (host-wide pause honored), no `uv tool`,
   no npm, no binary download.

## Artifact paths

- Draft deliverable: `/tmp/revenger-r64-lesson/round-64.md`
- This report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64LessonDraft.md`
