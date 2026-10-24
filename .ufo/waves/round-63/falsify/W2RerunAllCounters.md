# W2RerunAllCounters — round-63 falsify wave (attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Leaf seat: no dispatch, no git/jj mutation,
no lane edits; all writes are this report plus `/tmp/revenger-r63-*` scratch (removed on landing).

- **Attacked bytes:** lane tip `db55bd6488e24e956df5818ae34c2a043d7ddc12` (`main` == `HEAD`;
  integration commit immediately after build `2a34e455`).  `git rev-parse main` returned
  `db55bd6488e24e956df5818ae34c2a043d7ddc12`.
- **Frozen contract:** `reports/round-63/claims.md`; **frozen counter:** `reports/round-63/measure.py`;
  **red-before:** `reports/round-63/measure-before.log`.  All three are `A` (added at freeze commit
  `54ab973`); `git diff 54ab973 db55bd6 -- reports/round-63/` is **empty** — none was edited after
  the freeze.
- **LSP:** no `lsp` device is mounted in this session (`xd://lsp` → "No such tool … Mounted devices:
  ast_edit, debug").  Every caller/definition check below is therefore text/execution based, not
  semantic-server based; this is recorded as a tooling gap, not as absence of references.
- **Time-box:** partial by design; every claim attacked at least once on committed bytes.

## 1. Command and verbatim transcript

```
$ TIP=$(git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse main)
$ rm -rf /tmp/revenger-r63-w2rerun && mkdir -p /tmp/revenger-r63-w2rerun
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive "$TIP" corpus | tar -x -C /tmp/revenger-r63-w2rerun
$ cd / && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure.py /tmp/revenger-r63-w2rerun
```

Every printed line, verbatim (tip `db55bd6`):

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
PROBE_EXIT=0
```

Red-before re-run (same counter, `git archive 55bcb6e corpus` at `/tmp/revenger-r63-w2base`,
`cd /`), key lines — reproduces `measure-before.log` exactly:

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
F_COVERAGE=4/8 score=5.0
F_FAMILIES=['native-static', 'javascript', 'archives', 'evm']
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
BASE_PROBE_EXIT=0
```

## 2. Brief expectation vs printed lines

| Label | Brief expectation | Printed at tip | Verdict |
|---|---|---|---|
| `K_HELD` | (7/14 implied) | `K_HELD=6/14 score=4.3` | **D1** |
| `K_ROW C06` | `held` | `K_ROW C06 status=partial` | **D1** |
| `K_HELD_BACKED` | `7/14` | `K_HELD_BACKED=6/14` | **D1** |
| `F_COVERAGE` | `5/8` with firmware | `F_COVERAGE=5/8 score=6.2`, `F_FAMILIES=[… 'firmware' …]` | MATCH |
| `C3_RECEIPT_KILLED_ATTRIBUTED` | `2/2` | `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` | MATCH |
| C2 controls / b / d2 / attributed | 2/2 each | `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` | MATCH |
| Calibration / replay | 4/4, 10/10 | `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10` | MATCH |
| Freshness | 18/18 | `FRESH_ROWS=18/18` | MATCH |
| Holds / exit | `yes`, 0 | `HOLDS_OK=yes`, `PROBE_EXIT=0` | MATCH |

`D1` is not a C2/C3 phenomenon and is **not evidence of substantive falsification**; it is the
frozen admission order working as written (see §3.4).  It is still a literal deviation from the
brief's expected line list and must be recorded as such.

## 3. C1 — coverage K: `corpus/knowledge/round-63-zip-central-directory-evidence.md`

### 3.1 Committed state and README

- Entry present at the tip, 709 lines, header lines 1–6 carry two `source:` rows (S032 spec,
  S033 own-work), `verified-at:` 2026-10-23 with base commit, `recheck:` with stdout digest
  `02b0f495…`, `coverage-map: C06` (line 5) and `admission-status: candidate` (line 6).
- `git diff 55bcb6e db55bd6 -- corpus/README.md` is **empty**; C06 row still ends `| partial |`.
  This matches `claims.md` "README C06 flips `partial → held` only after those decisions land" and
  lesson `corpus/lessons/round-63.md:157-172` (admission order step 1: land without the flip).

### 3.2 Recheck reproduced

Extracted the `### Code` block (doc lines 311–640, `readout.py`) to `/tmp/readout-r63.py`
(sha256 `94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac`) and ran
`python3 -B /tmp/readout-r63.py <lane root>` from `/tmp`:

- exit 0, stderr empty, **17 lines**;
- `sha256sum` of stdout = `02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4`
  — **exactly the digest the entry claims**. The recheck is real and reproducible.

### 3.3 Independent byte derivation (my own parser, not the entry's script)

Own `struct`/`zlib` walk of `corpus/fixtures/archive-r2/fixture.zip` (2964 B,
sha256 `857989f5…`):

- EOCD at 2942, 22 B from end, sig `0x06054b50`, disks 0/0, entries on disk 2, total 2,
  CD size 114, CD offset 2828, comment length 0.  Counts read at EOCD+8 and EOCD+10.
- CD records at 2828 and 2886: `bin/checksum` (crc `b3df9ea7` = 3017776807, csize 2668,
  usize 16160, reloff 0, nlen 12, method 8, flags 0) and `README.txt` (crc `72a557b1` =
  1923438513, csize 78, usize 84, reloff 2710, nlen 10, method 8, flags 0); `crc` read at
  header+16 and `reloff` at header+42 agree with the parsed struct fields; CD ends exactly at 2942.
- Local payload offsets 42 and 2750; inflated 16160 and 84 bytes; CRC-32 recomputed equals the CD
  field for both; payload sha256 `f5ba0697…` / `7d8f6a8d…` equal `truth.json` member digests and
  sizes/compressed sizes; member name sets agree exactly.
- Spec anchors verified against the pinned snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt`
  (sha256 `0b993022…`, matches the S032 row): §4.3.7 is "Local file header" at snapshot line 387
  with the field order summing to 30/14/18/22/26/28; §4.3.12 CD header at line 522; §4.3.16 EOCD at
  line 634. The entry's derived offsets (crc@16, reloff@42, entries@8/10) are correct by construction.

All nine located quotes in `corpus/lessons/round-63.md:48-62` are verbatim substrings of the
whitespace-normalized snapshot, with word counts 7, 21, 7, 8, 23, 24, 23, 12, 20 — each ≤25.

### 3.4 Saved-record correspondence (items 13–16)

`corpus/live/runs/20261012T164246Z/artifact-inspection.json` at tip: **7692 bytes**, sha256
`2fec924b…`; top-level Evidence ID `ev_5cc39f…`, `operation=inspect_artifact`, provider
`rea-artifact-graph`/`1`, subject sha256 = archive digest, nested inventory Evidence ID
`ev_cc681c2a…` present, **3 occurrences**: `.` (2964), `README.txt` (84/78), `bin/checksum`
(16160/2668), node sha256 equal the inflated digests, `executable` false/true, `encrypted` false,
`hash_status` verified. Exactly as item 13–16 state. Source row `corpus/SOURCES.md:46` (S032,
`spec`, tier A, opened 2026-10-23, 6.3.10, snapshot digest) and `:47` (S033, own-work, tier A,
fixture/truth/record digests) reproduce on disk. `corpus/SOURCES.md` diff base..tip is +4 lines,
0 deletions.

### 3.5 Flip simulation (scratch only; lane untouched)

On `/tmp/revenger-r63-w2flip` (a fresh `git archive` of the tip) I applied the **compliant** flip
(step 3 of the lesson: status `held` **and** the knowledge cell naming the entry) and ran the same
frozen counter, cwd `/`:

```
flipped row: | C06 | archives (ZIP inventory) | `knowledge/round-63-zip-central-directory-evidence.md` (central-directory byte readout for `archive-r2` only) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | held |
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
F_COVERAGE=5/8 score=6.2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
FLIP_PROBE_EXIT=0
```

**Therefore:** the C1 numeric target (K 7/14) is reachable with exactly the admitted entry and no
other change — but only after the flip.  A **status-only** flip also prints `K_HELD=7/14
K_HELD_BACKED=7/14` (reproduced with the probe's exact K expressions on a scratch README): the K
counter measures presence, not quality.  That is already disclosed by the lesson's M34
(`corpus/lessons/round-63.md:194`); the gate must remain the entry + fresh decisions, never the
number.

## 4. C2 — coverage F: `corpus/live/runs/round-63/`

Envelope and receipt (all values re-derived by me):

- `inspection.json` 3904 B, sha256 `f6997835…`, **byte-identical to `stdout.raw`**; `stderr.txt`
  0 B; `receipt.json` 492 B sha256 `e930a549…`, `exit_code 0`, `fixture_sha256 bdfe9f46…` == image
  sha256, `stdout_sha256 f6997835…` == stdout/record sha256, `evidence_id ev_aae7529f…` == record's,
  `duration_seconds 1.296587134`.
- Record: `operation=inspect_firmware_regions`, `predicate_type=rea.analysis`,
  `authority=shipped-artifact`, provider/engine `binwalk` 3.1.0, `coverage=signature_scan`,
  `input_size=2048`, exactly 2 regions, `raw_result` carries the actual engine invocation and
  `extractions {}`; 5 limitations present.  Host `/usr/bin/binwalk` sha256
  `5fc19aac…` equals the envelope's `engine.executable_sha256`; `binwalk --version` prints 3.1.0
  (version probe only — no target execution).
- Byte oracle, re-derived from bytes (not from the record): region @512 size 79 and @1024 size 90
  inflate to 78 B sha `a5718481…` and 97 B sha `2d0d86aa…` — equal to `truth.json`
  `decompressed_member`; the three padding spans (0/512, 591/433, 1114/934) are all-zero; image
  sha256/size equal `truth.json`.  `oracle_check.py` run on the extracted tree exits 0, prints five
  `REGION … OK` lines and `ORACLE OK`.  **2/2 regions, 6/6 fields.**
- F counting: `inspect_firmware_regions` count = 1; only `round-63/inspection.json` is counted
  (`receipt.json` has no `normalized_result`); families become
  `['native-static','javascript','archives','firmware','evm']` = 5/8.

Residual: execution provenance is envelope-internal (the record's own U4 says so).  I did not
re-run the producer (no target execution; `npx` would also be a producer call).  The strongest
independent corroboration available without running it is the host binwalk byte-identity plus
byte-identical stdout/record.

## 5. C3 — calibration: attributed forged-receipt kill

Causal chain, verified on the final files:

- `corpus/verify_named_multi_icon_states.py:17` `receipt_ok` begins
  `receipt['command']==command and …`; the in-script control at `:76-78` deep-copies the receipt,
  sets `forged['command'] += ' --forged'`, and requires `not receipt_ok(forged, …)` with message
  `f'r{r}: forged receipt accepted'`.  The frozen mutant deletes exactly that conjunct; the probe
  prints `MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted`.
- `corpus/verify_icon_states.py:120` `assert receipt['exit_code'] == 0 and receipt['fixture_sha256'] == expected_hash`;
  the `round_id != 36` exemption (`:122`) is preserved byte-for-byte; control at `:153-158` forges
  `fixture_sha256 = '0'*64`, catches `AssertionError`, else raises `forged receipt accepted`.
  Probe: `MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted`.
- Both clauses match exactly once (no `could-not-evaluate`); controls pass 2/2 in both the tip run
  and the red-before run; red-before `C3_RECEIPT_KILLED_ATTRIBUTED=0/2` reproduces the committed
  log, so the 0→2 delta is real.
- Patch review: `git diff 55bcb6e db55bd6` on the two verifiers moves the existing conjunct chains
  into `receipt_ok` unchanged and **adds** the controls; no assertion is deleted or weakened.
  Named-script positive checks rose 139 → 142 (the three new control checks).  Census stays 10
  (`HOLD_REPLAY=10/10`), calibration 4/4.
- Disclosed limit (lesson M35, `round-63.md:195`): the `stdout_sha256` conjunct in
  `verify_icon_states.py` remains unguarded by an in-script control.  The claim credits only the
  two frozen clauses; no overclaim (Q13 honored, entry limitation 32, §Q13 at doc line 687).

## 6. Preservation and frozen holds

- `git diff --name-status 55bcb6e db55bd6 -- corpus/live corpus/fixtures`: only **additions** under
  `corpus/fixtures/firmware-r63/` (3 files) and `corpus/live/runs/round-63/` (6 files); no `M`/`D`.
- Non-add changes overall: `M corpus/SOURCES.md` (+4 lines, appends S032/S033, 0 deletions),
  `M corpus/verify_icon_states.py`, `M corpus/verify_named_multi_icon_states.py` (the C3 patch).
  All other changes are `A` under `.ufo/waves/round-63/` and the round-63 corpus paths.
- `corpus/QUALITY.md`, `corpus/README.md`, `reports/round-63/claims.md`, `measure.py`,
  `measure-before.log` unchanged after the freeze; round-61 probe untouched (`reports/` diff = only
  the three round-63 additions).  Ten-verifier census 10; denominator 14/8 unchanged.

## 7. Findings by severity

### D1 (HIGH, brief deviation — not substantive falsification)

`K_HELD_BACKED=6/14`, `K_ROW C06 status=partial` at the tip, versus the brief's expected
`7/14`/`held`.  Cause: the README flip is L1's and must follow this wave's fresh-seat decisions
(`claims.md` "Counting and admission order"; lesson `round-63.md:157-172`); README is byte-identical
base..tip.  Consequence to state plainly at adjudication: **the committed tip alone prints 6/14,
and `claims.md` says 6/14 falsifies C1** — so the round MUST land the flip (both status cell and
the knowledge cell, as simulated in §3.5) before the final `measure-after.log`, or C1 is falsified
on the frozen counter.  With that flip the same probe prints exactly `K_HELD=7/14`,
`K_HELD_BACKED=7/14`, `C06 held`, exit 0.

### F1 (LOW, contract prose inconsistency)

Lesson `round-63.md:164-166` requires the flip to name the entry "in the same commit as the entry
file".  The entry is already committed at `db55bd6`; the flip must come after decisions, so it
cannot be the same commit.  The counter does not require this (it only checks that cited knowledge
files exist).  Recommend rewording to "the measured tree must contain the entry and the row must
cite it", and not treating the sentence as an admission precondition.

### F2 (LOW, disclosed id reassignment)

`claims.md` pre-registered S033 as "Python zipfile docs … if used".  The landed S033
(`SOURCES.md:47`) is the own-work archive-r2 row; the zipfile docs were screened and excluded with
no row.  Disclosed at `round-63.md:83-140` and doc line 2.  No claim rests on zipfile behaviour
(`grep -c 'import zipfile'` = 0 in the entry's Code block; the build copy also uses
`struct`/`zlib`/`binascii`), so Q12 owes no reject reason (no rejected row) and Q01/Q02 hold.  Flag
only because the frozen contract's parenthetical id meaning changed.

### F3 (LOW, quote-evidence thinness)

The lesson's located-quote set has no §4.3.7 quote, while the entry derives local-header offsets
from §4.3.7 (doc item 5, snapshot line 387).  The row names the anchor and its scope covers the
local file header, so Q01/Q02 are satisfied; adding one §4.3.7 quote would make the quote evidence
uniform across the three record types.

### F4 (INFO, stale build artifact)

`.ufo/waves/round-63/build/zip-readout.py` (sha256 `c4b9b9f7…`) differs from the entry's `###
Code` block (sha256 `94f502cd…`); the build scratch predates the H1–H7/N1–N3 corrections.  Recheck
integrity is unaffected: the Code block itself reproduces the claimed 17-line stdout digest.

### F5 (INFO, counter semantics confirmed)

A status-only C06 flip prints `K_HELD=7/14 K_HELD_BACKED=7/14` (probe's exact K expressions,
scratch README), and a hand-written JSON with `evidence_id` + `operation` + `normalized_result`
would satisfy F.  This is the lesson's own M34 (`round-63.md:194`); I confirm it, and confirm that
the actual evidence (entry + byte readouts; receipt + oracle) is present, so the numbers are backed
by work here — but the counter alone must not be read as admission.

## 8. Residual risk and verification gaps

1. C1's K number is post-flip only.  If the round closes on this tip, the frozen counter's C1
   reading is 6/14 = falsified.  The substantive entry checks (Q01–Q13 evidence, byte derivation,
   recheck digest) all pass under my reading.
2. My Q01–Q13 judgements are one seat's recommendations, not admission (ROLE: verdict is a
   recommendation; L1 adjudicates).
3. C2 producer execution is not independently provable without re-running the producer (refused by
   rule); the envelope is internally consistent, stdout/record byte-identical, and the host binwalk
   bytes match the envelope, but origin/time remain UNKNOWN (record's own U4).
4. The firmware `truth.json` is author-authored (record's U5); my recomputation is independent of
   the truth file but both come from the same lane.  No third-party validation.
5. C3 attribution covers exactly the two frozen clauses; `stdout_sha256` (icon_states) stays
   unguarded (M35, disclosed).  No other conjunct was mutated in this run.
6. No LSP server was available, so no semantic references/definition/diagnostics results exist;
   these scripts are self-test entrypoints with no in-repo importers (checked by text).
7. The producer duration (1.296 s) and Evidence ID are accepted as recorded, not reproduced.

## 9. Named fresh-seat Q01–Q13 recommendations for the C1 entry (recommendation, not admission)

I am neither author nor corrector of the entry.  Decisions below are mine, each backed by an
artifact I executed or re-derived in this run.

| Q | Recommendation | Evidence |
|---|---|---|
| Q01 | pass | S032 is a `spec` row tier A for the three record layouts, opened 2026-10-23, snapshot digest reproduced; S033 own-work tier A with all four digests reproduced; no claim rests on another row |
| Q02 | pass | header lines 1–6: two `source:` rows with URL/paths and exact section/file anchors, `verified-at:` with base commit, `recheck:` reproduced (17 lines, digest `02b0f495…`), `coverage-map: C06` line 5 |
| Q03 | pass | expected values derived from bytes/spec arithmetic; `truth.json` and the saved record are only compared (items 10–16), never used to derive |
| Q04 | pass | manual analysis labelled (item 29); no tool credited; run ledger's `rea-agents@6.4.0` (checked on disk) credited only with the record's existence |
| Q05 | n/a | no readiness/capability claim; saved file read in past tense |
| Q06 | pass | fixture length/sha from bytes and base-commit identity block (items 1–2); failure inputs none |
| Q07 | n/a | no predicted parser behaviour; offsets are arithmetic from the spec field tables |
| Q08 | superseded by Q11 | stated in the doc's own table |
| Q09 | pass | each digest binds its own bytes (items 1, 8, 9, 13, 20); no origin/completeness/authenticity claim (items 20, 28) |
| Q10 | pass | scope is one archive/oracle/record, one provider id+version, one operation; no cross-lane absorption |
| Q11 | pass | §Sentence-to-output inventory (doc 659–687) plus per-item command+output; the whole 17-line stdout is reproducible byte-for-byte |
| Q12 | n/a | no rejected source row; zipfile docs excluded without a row, no claim on its behavior |
| Q13 | pass | no guard credit; §Q13 (line 687) and limitation 32; no verifier cited as guarding a value |

## 10. Tooling and cleanup

No installs, no pacman, no `npx`, no producer/target execution.  Used: `git` (read-only), GNU
tar/sha256sum/diff, `python3` 3.14.8 (`struct`, `zlib` 1.3.2, `hashlib`, `json`), `binwalk --version`
(version probe only).  Scratch: `/tmp/revenger-r63-w2rerun`, `/tmp/revenger-r63-w2flip`,
`/tmp/revenger-r63-w2status`, `/tmp/revenger-r63-w2base`, `/tmp/readout-r63.py`, `.out`, `.err` —
removed after this report landed.

**Bottom line (recommendation):** C2 holds (F 5/8, byte-oracle 2/2, envelope consistent); C3 holds
(red-before 0/2 reproduced; attributed 2/2 with genuine in-script controls; controls 2/2); C1 is
substantively supported (recheck digest exact, independent byte derivation 2/2 members, saved-record
correspondence exact, quotes ≤25 words and verbatim) but its counter line at the committed tip is
`K_HELD_BACKED=6/14`, so the flip required by the frozen order must land before the final
`measure-after.log` — otherwise the frozen counter falsifies C1 at 6/14.
