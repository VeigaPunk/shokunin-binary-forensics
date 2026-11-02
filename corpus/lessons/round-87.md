# round-87 lesson — criterion N's mutation-killed attribution pair lands on the negctl harness itself

Round shape: fresh-start (r71/r72/r73 rejected closures re-read and
spot-checked; freshstart probes re-run fresh 2026-11-02). Base
`1306ec9ac32a4d4477cc15049c1d09e326ecac5a`; freeze `ea143a3a`
(claims + instruments + reds, committed before any landing or after-run);
landing `1fa086d3` (SKILL.md registry row + S473; 2 files, 12 insertions,
0 deletions); adjudication = this lesson's commit. ONE claim, calibration,
not exploratory, with counting commands. Non-author verification: pending
(the closure judge re-derives; this lesson records the self-gate only).

## Gate

### The claim

C1 calibration: criterion N's mutation-killed attribution pair lands on the
negctl harness itself (the routed r75-planned-(b) item, carried through
r75–r86), and the criterion-N instrument gets its registry row.

- Red (`reports/round-87/negctl-red.log`, over the frozen v1 bytes
  `eb5d1b54…3fad` = base bytes, never touched): the frozen counting
  instrument `reports/round-87/selftest_probe.sh` prints
  `NEG_SELFTEST_MODE_PRESENT=0/1`,
  `NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=0/2`, `NEG_USAGE_EXIT64=0/1`,
  exit 1; the v1 harness's own plain legs are green at the same bytes
  (`negctl-v1-baseline.log`, exit 0) — the harness works but cannot show
  it can fail. That contrast IS the routed debt.
- Fix: `reports/round-87/probe_negctl2.sh` (sha `d7027146…070d`, frozen at
  the freeze commit) — plain mode v1-identical (same fixtures, same legs,
  byte-identical value lines: `plain-equal.log` diff empty, both exits 0);
  `--selftest` hermetic (synthetic verdict vectors only: no fixture build,
  no probe run, no producer call; expected finding-ids
  `NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok`,
  `NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok`, `NEGCTL_SELFTEST_STALE_LOGIC=ok`,
  `NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok`, last line `NEGCTL_V2_SELFTEST=pass`);
  usage exit 64 declared. The pair: mutant A (`stale_flag_ok` blinded to
  `return 0`, exactly line 35, mutated sha `f70c0e9a…9a99`) dies exit 1
  attributed `selftest: stale-record verdict accepted a false-pass`;
  mutant B (attribution pattern relaxed to `.*`, exactly line 35, mutated
  sha `ec29099c…39cb`) dies exit 1 attributed `selftest: attribution guard
  accepted an unattributed kill`. Deterministic ST1→ST2 ordering gives
  each mutant its own message (mutant B's `[ "$1" = "1" ]` guard still
  rejects exit-0 inputs, so it passes ST1 and dies at ST2).
- Green (`negctl-green.log`, from the committed blob over the landing tip
  `1fa086d3`): `1/1 · 2/2 · 1/1`, exit 0. Mutations re-derived from the
  committed blob (`negctl-mutant-kill-after.log`): both one-line diffs at
  35c35, both shas match the claims pins, both deaths attributed.
- Registration: the SKILL.md §Gate registry gains the `probe_negctl2` row
  (7 → 8 rows, counting command
  `sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md | grep -cE '^\| name \|'`).
  The criterion-N instrument was never registered (v1, round 75) — the
  same gap the round-78 registration closed for R/G. Verdict map declares
  0/1/2/64 per PROTOCOL §Gate standard §Verdict; the self-test clause is
  satisfied with the two-evidences pair over committed input snapshots
  (v1 bytes red, v2 bytes green), naming the measured revisions.
- Axis boundary (honest): the criterion-N score itself stays 10.0 held
  (scored r75); the moved quantity is the instrument's self-conformance
  and its registry visibility — the same shape as the round-79
  receipt_probe2 registration, which moved no criterion score. Coverage,
  freshness, depth, operability, adjacency: unchanged (holds receipt;
  PROVINCE byte-unchanged; no knowledge byte).
- Holds: M 3/3 (10.00), F4 10/11 (9.09), A1v2 5/5 (10.00), A1 3/3
  (10.00), freshness 18/18, K 8/15 — all over the landing archive, all
  probe exits 0 (`holds-over-landing-archive.log`). No-harm: 12
  insertions, 0 deletions over freeze..landing; protected paths empty
  (`noharm-diff.txt`). Separability: archive of base + the two
  instruments only (no SKILL row, no S473) runs green identically with
  base-state markers (7 rows, no S473) — `c1-only.log`.

### New source row

- **S473** (own-work, tier A, opened 2026-11-02) — the criterion-N
  instrument-blindness evidence: the frozen v1 bytes +
  `negctl-v1-baseline.log` (legs green) + `negctl-red.log` (conformance
  red over the SAME bytes) + the routed-debt lineage. C1 rests on it
  (Q01: tier A for the claim's scope — the lane's own re-runnable gate
  output). Appended inside the Registry directly after S472; NF=13
  checked at landing (0 malformed, 0 duplicates; rows 472 → 473).
- Located quote grounding `teaches` (≤25 words, location, access date):
  "attribution pair on the negctl harness itself, or retire/split P2 at
  saturation" — SCORECARD.md, round-75 planned paragraph, re-read this
  round 2026-11-02 (verbatim; 13 words). This is the routed debt's own
  wording, unchanged from r75 through r86.

### Criteria mapping (self-gate, pending non-author verification)

Q01 pass (S473, tier A own-work, opened this round); Q02 n/a (no
knowledge entry; the claim is instrument + registration work — the S473
row carries the header contract); Q03 pass (expected values = the
claims.md pins, fixed before the landing); Q04 n/a (no tool-version
claim); Q05 n/a (no readiness claim; plain-mode host dependencies are
disclosed, not claimed); Q06 n/a (no fixture); Q07 pass (the mutants'
deaths were pre-registered as the pair's expected behavior with the
recipes and mutated-copy shas pinned in claims.md before the landing);
Q08/Q11 pass (every count carries its command — the two counting
commands live in claims.md and the receipts quote their own stdout);
Q09 pass (receipts claim only the bytes they hashed — the shas are
re-derived in the receipts themselves); Q10 pass (scoped to the
criterion-N instrument; no cross-family generalization); Q13 pass (the
counting instrument is credited only for the clauses its mutants show
it detects — both switches killed attributed); Q14/Q15/Q16 pass (no hex
runs; the one named revision `1fa086d3` is derived by the git commands
in the receipts; the probe's printed output is quoted, not described).

Spot-check: the non-author closure re-derives the red/green pair, both
mutant deaths, the plain-equal diff, and the registry count. No wave
surface was used or needed (this claim verifies from committed bytes on
this host).

### Census

Round start: sanctioned explicit-lane-dir form exit 0 (21 W01 + 10 W04,
zero E — `.ufo/waves/round-87/census-round-start-sanctioned.log`);
contract-literal form exit 2 (`.ufo/waves/round-87/census-round-start-literal.log`;
r74–r86 operator-side lineage, L0 r79 stands, routed around, nothing
assumed answered). Round end: receipts land with the adjudication
(`.ufo/waves/round-87/census-round-end-*.log`). Sources 472 → 473.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| loose-pattern counting (number-drift): the freshstart sentinel was first counted with a pattern re-derived from memory (`grep -ciE "unsupported"`) which prints 31 by counting limitation-text lines, against the registered metric (`grep -c "availability_code: unsupported_host"` = 7, the r85/r86 recorded value) | `reports/round-87/freshstart-probes.log` probes 3 vs 6 — both numbers present in the receipt; the prior receipts' value 7 is the registered constant | re-reading the prior receipt before citing (the 31 disagreed with the recorded 7 — the two-source cross-check habit) | probe 6 re-ran the registered pattern verbatim (7, unchanged sentinel); rule: paste the registered counting command from the prior receipt, never re-derive the pattern from memory; the receipt discloses the loose count as noise; mined |
| mutant-recipe over-escaping (fix-never-applied): the counting probe's first mutant B recipe embedded double-escaped backslashes (`\\\\^`), so sed never matched, the "mutant" ran unchanged, and the cmp-equal guard silently returned unkillable — the green would have been impossible to reach with the frozen bytes as written | `reports/round-87/mutants-prelanding.log` — mutant B section: no diff lines, `MUTB_EXIT=0` (the unapplied mutant passing its own selftest) | the preprobe habit (run every frozen recipe by hand BEFORE the freeze — the same measure-before-write that caught M33-class defects) | recipe corrected to single-escaping (`\\^` in the bash double-quoted string → `\^` in the sed BRE); the corrected application diffs exactly line 35 and dies attributed; the preprobe receipt keeps the failed first application on record; mined |
| command-substitution newline stripping (receipt-construction sha drift): the first `negctl-mutant-kill-after.log` draft built the blob copy via `printf '%s' "$(git show …)"` — `$(…)` strips the trailing newline, so v2.sh and both mutants hashed differently from the claims pins (`146c9c08…`/`6ff6751d…` vs pins `f70c0e9a…`/`ec29099c…`) | the mandated pin-vs-receipt sha check before landing (the shas printed in the first draft did not match claims.md) | the pin-verification habit (every receipt sha is compared against its pin before the receipt lands) | byte-preserving redirect (`git show … > file`) rebuilds the tree; the corrected receipt's three shas match the pins exactly; rule: never route committed bytes through `$(…)` when a hash will be pinned — redirect to a file; mined |
| grep-piped exit attribution (receipt-exit class, r85 tail-line signature on a new surface): the first `holds-over-landing-archive.log` recorded `M_EXIT=0` / `F4_EXIT=0` / `AG_EXIT=0` from the GREP's exit, not the probe's; the same first draft omitted the A1 hold entirely because `ag_probe2.py` prints only `A1V2_RECORDED` (the A1 criterion's instrument is the r82 `ag_probe.py`) | the first holds receipt (overwritten in place before landing — nothing committed); `reports/round-86/holds-over-landing-archive.log:70-80` (the r86 receipt's four-probe layout was the reference) | the r85 mined tail-line class + the r86 receipt's own structure as the two-source cross-check | receipt re-derived with exits captured into variables before any grep; the A1 leg appended from the committed r82 blob (`A1_RECORDED=3/3 score=10.00`, exit 0); all four probe exits now receipted truthfully; mined (recurrence of a known class, new signature) |
| transcription drift (`paste -sd:")"`): the counting probe's first draft carried a spurious quote after `-sd:` (mis-transcribed from the r79 instrument, whose line ends `-sd:)"`), producing a bash syntax error (unexpected EOF at line 73) | `bash -n reports/round-87/selftest_probe.sh` at the preprobe (SYNTAX exit 2) — caught before any receipt was built | the bash -n pre-check habit (syntax-check every new script before running it) | corrected to the r79 bytes; the r79 original itself was re-verified with `bash -n` (SYNTAX_OK) as the reference; rule: when copying a line from a committed instrument, copy the exact bytes (or diff the two files), never retype from a truncated view; mined |

## Routed forward

- Criterion R full extension to the legacy receipt-quoting rows (r76
  routed); criterion C repair (§9-ruled-out); criterion N is CLOSED this
  round (the routed pair landed; the criterion score stays 10.0 held).
- F android gate (`REA_JADX_MCP_JAR` + jadx PATH — re-probed fresh this
  round, still gated); K L0 r74 (re-read, unanswered) — coverage stays
  routed on documented unreachability, sentinel = the 7 unsupported_host
  groups (unchanged 2026-11-02).
- Census literal form (operator-side, lineage L0 r79); SHONEN box 1
  non-author re-confirmation (operator-side, now naming the r87 SKILL.md
  bytes — the registry row changed SKILL.md again).
- The criterion-instrument class question (whether every criterion probe
  of P's class takes a registry row) stays routed (r78 registry note);
  this round registered the criterion-N VERDICT instrument (gate-class
  like R/G), not a P-class probe.
- considerthese 2026-10-28 lesson-1 proposal (the claimed-coverage-set
  vs actual-compared-set checker) — considered, not adopted (consumers
  are the operator-blocked C05 surface); stays open for a future round.
- Plain-mode host dependencies of the negctl instrument (ghidra
  presence + the PROVINCE.md present-record block) are disclosed in the
  registry row; the plain receipts re-derive both ends each time they
  run (v1 baseline re-confirmed green 2026-11-02).
- treecommit repo-relative + file-exists + numstat-count rule (held:
  11/11 freeze, 2/2 landing).
