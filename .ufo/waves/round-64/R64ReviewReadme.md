# R64ReviewReadme — C07 README flip draft review (round 64)

Seat: R64ReviewReadme (reviewer, independent leaf). Lane root
`/home/vgpnk/Projects/shokunin/revenger-shokunin`. No git/jj mutation; no
commit/push; `corpus/README.md` not edited; only
`.ufo/waves/round-64/R64ReviewReadme.md` written.

## Verdict: **PASS**

Draft reviewed: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/readme-flip-draft.md`
(3040 bytes, mtime 01:18). All four brief criteria hold at byte level, and the
admission-time gates are stated below as conditions on L1, not as draft
defects. Findings F1–F2 are gates that must be satisfied at integration; F3–F5
are advisory.

## Criteria

### 1. Post-admission row keeps exact column shape; changes only status + knowledge cell — PASS

Draft row 1:

```
| C07 | firmware images | `knowledge/round-64-firmware-region-byte-evidence.md` (manual byte-derived readout of `fixtures/firmware-r63/firmware-r63.bin` only; no general firmware-format, extraction/execution, provider-completeness or authenticity claim) | — | held |
```

Byte evidence against the live row (`corpus/README.md:36`,
`| C07 | firmware images | — | — | frontier |`, file 6200 bytes):

- draft's quoted source row `rows[0]` is byte-identical to the live C07 line — `True`.
- pipe split → 7 parts (empty|C07|surface|knowledge|work|status|empty) i.e. the
  header's five cells; cells are each `' '+strip()+' '` (single-space
  discipline) — `True`; line ends `| held |`; no trailing spaces.
- cell 1 (` C07 `) and cell 2 (` firmware images `) byte-identical to base — `True`.
- work-evidence cell byte-identical to base, `b' \xe2\x80\x94 '` (em dash
  U+2014) — `True` (brief: work cell unchanged).
- knowledge cell names exactly one entry:
  `knowledge/round-64-firmware-region-byte-evidence.md`, one occurrence, with
  the exact backticked spelling the counter regex
  `knowledge/[\w.-]+\.md` reads from `l.split("|")[3]`. The parenthetical's
  `fixtures/...` path does not match that regex (matches C06/C04 row style).
- status token cell `held`; whitespace/ASCII discipline: only non-ASCII char in
  the row is U+2014.
- replacing only line 36 with this row yields a 1-line diff (`2` +/- lines) —
  no other row or legend text carries a replacement in the draft.

### 2. Fallback uncovered row is legend-correct — PASS

Draft row 2:

```
| C07 | firmware images | — | `fixtures/firmware-r63` (`firmware-r63.bin`, `generator.py`, `truth.json`); `live/runs/round-63` (`inspection.json` `inspect_firmware_regions`, `oracle_check.py`, `receipt.json`, `LEDGER.md`; observation layer only) | uncovered |
```

- knowledge cell byte-identical to base ` — ` (`b' \xe2\x80\x94 '`) — `True`;
  status `uncovered`, the legend token defined as "work evidence exists but no
  admitted knowledge entry" (`corpus/README.md:21-24`).
- every cited work path exists in the lane: `fixtures/firmware-r63/firmware-r63.bin`
  (2048 B), `generator.py` (5532 B), `truth.json` (1933 B),
  `live/runs/round-63/{inspection.json, oracle_check.py, receipt.json, LEDGER.md}`;
  `inspection.json` carries `operation=inspect_firmware_regions`,
  `evidence_id`, non-null `normalized_result`.
- five-cell shape, single-space cells, no inner pipes, only U+2014 non-ASCII — `True`;
  1-line diff when substituted alone — `True`.
- the "observation layer only" qualifier keeps the record an observation, not a
  knowledge claim, matching claims.md scope.

### 3. No other row or the legend text touched — PASS

Programmatic check of the draft: exactly three `| C## ` lines (one quoted
source row, two replacement rows); no `Status: \`held\`` block, no legend
replacement text. Substitutions of either row into a corpus copy change line 36
only (line counts identical, all other lines equal). The `## Frontier` prose
(lines 63–66) is deliberately left alone and flagged to L1 — consistent with the
contract's "No other README row changes".

### 4. Cross-check against current C07 row character by character — PASS

Compared as bytes, not as rendered text: source row byte-equality `True`;
unchanged cells byte-equal (`b' \xe2\x80\x94 '` for the work cell in row 1 and
for the knowledge cell in row 2); status cells differ exactly
`frontier → held` / `frontier → uncovered`; the knowledge cell in row 1 starts
with the exact backticked entry name and mentions it once. Em dash is U+2014
(`b'\xe2\x80\x94'`) in all three rows, matching the live file.

## Independent frozen-counter receipts (actual draft rows, not the scribe's copies)

Method: `cp -a corpus` to lane-owned scratch; replace **only** line 36 with the
row extracted from the draft file; for the admission tree add a clearly-marked
`/tmp` stub at `corpus/knowledge/round-64-firmware-region-byte-evidence.md`
(the real entry does not exist in the lane); run
`TMPDIR=/tmp/revenger-r64-reviewreadme-tmp python3 -B reports/round-64/measure.py <TREE>`
from the lane root.

| tree | EXIT | K_HELD | K_ROW C07 | K_HELD_BACKED | STRICT | README_TOKEN_LEGEND_MISMATCH | F_COVERAGE | HOLDS_OK_V2 |
|---|---|---|---|---|---|---|---|---|
| admission row + stub entry | 0 | 8/14 (5.7) | held | 8/14 | 8/14 | 0 `rows=[]` | 5/8 | yes |
| fallback row, no entry | 0 | 7/14 (5.0) | uncovered | 7/14 | 7/14 | 0 `rows=[]` | 5/8 | yes |
| admission row, **no entry file** | 0 | 8/14 | held | **7/14** | 7/14 | 0 | — | — |

Red-before baseline reproduced from the committed receipt
`reports/round-64/measure-before.log`: `K_HELD=7/14`,
`K_HELD_BACKED=7/14`, `K_ROW C07 status=frontier`,
`README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`.

The probe trees are working-tree copies and already carry in-flight C2 script
edits, so `C4_RECEIPT_KILLED_ATTRIBUTED=2/2` in my logs is **not** evidence
about the README rows and is not used as such; the README-derived labels are
independent of those scripts.

## Findings by severity

**F1 — GATE (admission-time, not a draft defect).** The admission row is backed
only if `corpus/knowledge/round-64-firmware-region-byte-evidence.md` exists in
the same revision: with the entry present the probe prints
`K_HELD 8/14 / K_HELD_BACKED 8/14`; without it the row is held-but-unbacked
(`K_HELD 8/14`, `K_HELD_BACKED 7/14`) and the K target is not met. The entry
must also avoid an `admission-status: rejected` marker in its first 2000 bytes
or `K_HELD_BACKED_STRICT` will not count it (frozen `measure.py` lines 36–48).
L1 must land entry + row together; the README flip alone cannot move K.

**F2 — GATE (scope wording reconciliation).** The row's parenthetical cannot
yet be checked against the admitted entry's own wording: no candidate exists in
the lane (`corpus/knowledge/round-64*` absent), only `/tmp` stubs explicitly
marked "not a corpus candidate" (e.g. the 330-byte
`/tmp/revenger-r64-readme-legend/admit/.../round-64-firmware-region-byte-evidence.md`).
Round-63 finding F3 rule applies: if the landed entry's `coverage-map:` header
or `## Limitations` differs, the entry's wording wins verbatim. Separately, the
parenthetical omits the contract's "no real vendor image" clause; the
fixture-path-only framing covers it in effect, but L1 should confirm the landed
entry carries that disclaimer rather than relying on the row to imply it.

**F3 — ADVISORY (L1 decision, correctly left out of the draft).** After either
flip, `corpus/README.md` `## Frontier` (lines 63–66: "an authored known-truth
firmware fixture is the next probe") is stale. It is prose, not a coverage-map
row, and the contract flips only the row; the draft's explicit deferral is the
right call. Do not fold it into this flip; record it as follow-up debt.

**F4 — NIT (draft section (3)).** Section (3) says the legend "defines the four
status tokens" and then enumerates three (`held`, `uncovered`, `frontier`),
omitting `partial`; its `uncovered` paraphrase also drops the legend's
rejected-candidate parenthetical. No false claim about the legend and no
replacement legend text is proposed, so the deliverable sentence stands, but the
enumeration is incomplete as written.

**F5 — MINOR/CONDITIONAL (fallback knowledge cell).** If C1 falsifies and the
candidate is retained under `knowledge/` with `admission-status: rejected`, the
fallback row's `—` knowledge cell hides an existing knowledge file; C04 and C09
precedent names retained rejected candidates in that cell instead. This is
counter-safe either way (uncovered rows never enter `K_HELD`; the strict label
already refuses rejected-marked files). L1 owns the choice; no change needed if
nothing is retained under `knowledge/`.

## Residual risk and verification gaps

- **Entry wording** (F2) is unverifiable until the real candidate is authored
  and admitted; the row's parenthetical may need to be replaced with the
  entry's own scope sentence.
- **Admission decision** (Q01–Q13 quality) is out of this seat's scope; the
  counter measures existence only, and my receipts validate row shape/label
  movement, not admission.
- **Probe provenance**: my runs and the scribe's are working-tree copies, not
  the committed `git archive <commit> corpus` tree the contract freezes for
  final evidence. Final labels must be re-read on the committed archive.
- **Fallback validity** is conditional on C1 falsifying; both branches were
  measured, only one will be integrated.
- Text-level byte review was deliberate: the observable contract here is the
  frozen counter's line/regex parsing, and Markdown has no semantic server to
  consult; no LSP result is presented as proof.

## Bounds and tooling

- Wrote only this report. No edits to `corpus/README.md`, the draft, wave
  spec/registry, `MANIFEST.json`, fleet repo, sibling lanes, lane jj state or the
  Git index. No git/jj mutation, no commit/push.
- Scratch: `/tmp/revenger-r64-reviewreadme/` and
  `/tmp/revenger-r64-reviewreadme-tmp/` (lane-owned; remove on landing).
- Installs/upgrades: none (no network, no package transactions).
