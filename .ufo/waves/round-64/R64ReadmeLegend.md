# R64ReadmeLegend — C07 README flip draft (round 64)

Seat: R64ReadmeLegend (scribe). Lane root
`/home/vgpnk/Projects/shokunin/revenger-shokunin`. No git/jj mutation, no
commit/push; `corpus/README.md` was not edited.

## Deliverable

`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/readme-flip-draft.md`
(3040 bytes) contains, against the byte-exact source row
`| C07 | firmware images | — | — | frontier |` (README line 36, em dash U+2014):

1. **Post-admission row** (`frontier → held`), knowledge cell naming only
   `knowledge/round-64-firmware-region-byte-evidence.md` with a single-fixture
   scope parenthetical, work-evidence cell unchanged (`—`):
   `| C07 | firmware images | \`knowledge/round-64-firmware-region-byte-evidence.md\` (manual byte-derived readout of \`fixtures/firmware-r63/firmware-r63.bin\` only; no general firmware-format, extraction/execution, provider-completeness or authenticity claim) | — | held |`
2. **Falsification-fallback row** (`frontier → uncovered`), knowledge `—`, work
   evidence naming `fixtures/firmware-r63` and `live/runs/round-63`
   (`inspection.json` `inspect_firmware_regions`, `oracle_check.py`,
   `receipt.json`, `LEDGER.md`; observation layer only).
3. **Legend sentence**: the legend text needs no change — it defines the status
   tokens generically and contains nothing C07-specific, so both flips are pure
   data-token corrections.

Both rows keep the source row's five-cell shape
`| C07 | firmware images | <knowledge> | <work evidence> | <status> |`.

## Gates exercised (frozen counter, structural validation only)

Command shape (frozen script, cwd `/`, TMPDIR in lane scratch):
`TMPDIR=/tmp/revenger-r64-readme-legend/tmp python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py <tree>`

Rows were extracted from the draft file itself, injected into byte copies of the
live corpus (admission tree also got a simulated stub entry, since the real C1
candidate does not exist yet), then measured:

| tree | exit | K_HELD | K_ROW C07 | K_HELD_BACKED | STRICT | README_TOKEN_LEGEND_MISMATCH |
|---|---|---|---|---|---|---|
| `admit3` (row 1 + stub entry) | 0 | 8/14 (5.7) | held | 8/14 | 8/14 | 0 `rows=[]` |
| `fallback3` (row 2, no entry) | 0 | 7/14 (5.0) | uncovered | 7/14 | 7/14 | 0 `rows=[]` |
| `base-archive` (`git archive HEAD corpus`, no README edit) | 0 | 7/14 | frontier | 7/14 | 7/14 | 1 `rows=['C07']` |
| `pristine` (live tree, no README edit, 01:17:08 snapshot) | 1 | 7/14 | frontier | 7/14 | — | 1 `rows=['C07']` |

- Red-before values match `reports/round-64/measure-before.log`
  (`K_HELD_BACKED=7/14`, `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`,
  `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`, exit 0 on the base archive).
- Counter code paths confirmed: `K_HELD` = `\| held \|$`; `K_HELD_BACKED` reads
  `l.split("|")[3]`; `README_TOKEN_LEGEND_MISMATCH` reads `cols[-1]` and
  `cols[0]`; the draft rows satisfy all three.
- Logs: `/tmp/revenger-r64-readme-legend/{admit3,fallback3,base,pristine,admit,fallback,fallback2}.log`.

## Findings

1. **Transient C2 regression in the working tree — observed, then fixed by its
   owner before my final validation.** Against the pre-fix
   `corpus/verify_icon_languages.py` (mtime 01:17:08), the frozen counter printed
   `C2_RECEIPT_B_KILLED=1/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=1/2`, exit 1; the
   `git diff` showed the seat had **replaced** the existing
   `forged['command']+=' --forged'` control with the new stdout control, so
   mutant `b` survived (`verify_icon_languages.py b exit=0 pass`). The current
   file (mtime 01:18:25) keeps both controls (`b exit=1 killed :: AssertionError:
   r47: forged receipt command accepted`) and the counter now prints
   `C2_RECEIPT_B_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`,
   `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, exit 0 on both draft trees. Evidence for
   both states is preserved in `pristine.log` and `admit3.log`;
   `corpus/verify_multi_icon_states.py` was correct throughout (3 insertions
   after the command control). I notified `revenger-r64.R64C4LangPatch` and
   `revenger-r64`.
2. **Held-without-backing is invisible to K_HELD.** In my first (mis-indexed)
   validation pass the admission row was applied without the entry file:
   `K_HELD=8/14` but `K_HELD_BACKED=7/14`, exit 0. So the admission flip is only
   honest once the real entry lands; the final counter's `K_HELD_BACKED` (not
   `K_HELD`) is the label that catches a missing file. This was a harness
   mis-index in scratch, not a draft defect (`fallback2.log`).
3. **C1 candidate dependency.** `corpus/knowledge/round-64-firmware-region-byte-evidence.md`
   does not exist in the lane at draft time; admission-tree numbers above used a
   clearly-marked `/tmp` stub. The real entry must also avoid an
   `admission-status: rejected` marker in its first 2000 bytes or
   `K_HELD_BACKED_STRICT` will not count it.
4. **Adjacent stale prose, deliberately untouched.** README `## Frontier`
   (lines 63–66) still says the authored firmware fixture "is the next probe";
   after either flip that prose is stale. It is prose, not a coverage-map row,
   and the contract flips only the row, so the draft leaves it and flags the
   decision to L1.
5. **Legend.** No legend text change is required for either flip (row 3 of the
   deliverable).

## Touched surfaces

- Wrote: `.ufo/waves/round-64/readme-flip-draft.md`,
  `.ufo/waves/round-64/R64ReadmeLegend.md` (this report).
- Read-only: `corpus/README.md`, `reports/round-64/{claims.md,measure.py,measure-before.log}`,
  `corpus/fixtures/firmware-r63/*`, `corpus/live/runs/round-63/*`.
- Read-only git: `git archive HEAD corpus`, `git diff`, `git diff --stat` — no
  mutation, no commit, no push, no index/jj change. `git diff --stat` shows
  `corpus/README.md` untouched.
- Scratch: `/tmp/revenger-r64-readme-legend/` (corpus copies + logs), lane-owned;
  to be removed on landing.
- Installs/upgrades: none.

## Out of scope / limits

- No admission decision: this seat only drafts the flip; L1 integrates after the
  C1 admission order completes.
- My counter runs are on `/tmp` copies of the working tree, not the committed
  `git archive` tree the contract freezes for final evidence; they validate row
  shape and label movement, not round admission.
- No corpus candidate content was authored; no README row other than C07 was
  proposed; denominator (14 rows / 8 families) unchanged.
