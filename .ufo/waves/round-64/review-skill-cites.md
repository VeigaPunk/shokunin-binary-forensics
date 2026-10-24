# R64ReviewSkillCites — citation existence sweep of the SKILL candidate

**Seat:** `revenger-r64.R64ReviewSkillCites` (reviewer, calibration axis)
**Candidate swept:** `/tmp/revenger-r64-skill/SKILL.md` — 264 lines, 23,106 bytes,
mtime 2026-10-24 01:20. Earlier probes of the assigned path (before 01:17) returned
"not found"; the first landed draft is what this sweep covers.
**Method:** mechanical extraction (sweep tool at
`/tmp/revenger-r64-cites/sweep.py`, JSON output `/tmp/revenger-r64-cites/sweep-out.json`)
plus manual anchor verification of every load-bearing line range, hash and
section heading the candidate cites. Nothing was edited; read-only throughout.

## 1. Extraction summary

| kind | count | verdict |
|---|---|---|
| backticked repo paths (incl. globs) | 90 cite-events | 75 `exists`, 5 `exists-via-prefix` (corpus/wave-relative), 1 `exists-ambiguous` (`corpus/verify_*.py` → all 10 verifiers), 9 `unresolved-basename` (fixture-local names, informational), **0 PHANTOM** |
| URLs | 0 | none cited — candidate deliberately restates no URL (§7 note) |
| S-ids | 15 cite-events | all `registered` in `corpus/SOURCES.md`: S005, S006, S007, S009, S010, S014, S015, S032, S033, S034, S035 (+ prose repeats). None rejected-status; **0 PHANTOM** |

Unresolved basenames are `generator.py`/`truth.json`/`README.txt`/`readout.py`-style
fixture-local or wave-local names, not repo-path claims; none reads as a missing
repo file.

## 2. Phantom or stale citations found

### F1 — `README.md` anchor mislocation (2 lines)
- `SKILL.md:26` — "Producer readiness lives in `README.md` "Frontier"."
- `SKILL.md:32` — "(`README.md` "Known gaps"; `SCORECARD.md` rubric boundaries)."

Evidence: bare `README.md` resolves at lane root
(`/home/vgpnk/Projects/shokunin/revenger-shokunin/README.md`), which contains no
"Frontier" and no "Known gaps" section (its headings: "What's here", "Saved
named-icon ledger replay"). Both sections exist only in `corpus/README.md:50`
(`## Known gaps`) and `corpus/README.md:59` (`## Frontier`). `SKILL.md:24` cites
the same sections correctly as `corpus/README.md`; the bare basename elsewhere
is the stale/mislocated form. Severity: medium — a literal reader lands on a file
where the anchor does not exist.

### F2 — `verify_multi_icon_states.py` control anchors off by one (`SKILL.md` §1 row 2)
Candidate claims `forged command :149-151`, `forged stdout_sha256 :152-154`.
Actual working-tree lines: forged-command control `:148-150`, forged-stdout
control `:151-153` (`sed -n 148,153p`; independently recorded by
`.ufo/waves/round-64/R64C4MultiPatch.md` "new three-line control at lines
151–153"). The attributed phrases (`forged receipt command accepted`,
`forged receipt stdout accepted`) are correct. Severity: low — cited lines are
real control lines but off by one; fixes: `:148-150` / `:151-153`.

### F3 — "at this SKILL's base" overclaims (`SKILL.md:8`, §7 measure.py row)
`verified-at:` says "Every file, line range and S-id cited below was re-read in
the lane tree at that base" (`666ea84b`), and §7 lists `reports/round-64/`
claims/measure/measure-before **plus a sha256** under "identity of the frozen
instrument at this base". `git cat-file -e 666ea84b:reports/round-64/claims.md`
fails for all three: they are committed after the claim base (pre-registration
commit). The §1 table also cites "the round-64 C4 patch in the working tree" —
correctly disclosed, but it means §1 anchors are working-tree, not base.
Severity: low-medium — the base-commit clause is false for the round-64
artifacts; the honest fix is "at base plus the round-64 working-tree artifacts
named below".

### F4 — minor stale anchors (informational)
- `generator.py:149-150` (writes `firmware-r63.bin`/`truth.json` in place):
  verified exact at 149-150.
- `decode_member :39-49`, `derive_regions :52-101`, `MEMBERS/IMAGE_SIZE :17-35`,
  `build :104-113`, `ZLIB_RUNTIME_VERSION :131`, `python_version :133`,
  `truth.json` 73 lines — all verified exact.
- `verify_icon_states.py` conjunct range cited `:119-123`: `receipt_ok` def at
  `:119`, `evidence_id` assert at `:123` — exact; forged `fixture_sha256`
  control `:151-158` and phrase `forged receipt accepted` — verified.
- `verify_named_multi_icon_states.py` conjuncts `:16-17`, forged command
  `:76-78` phrase `forged receipt accepted` — verified.

## 3. Verified-consistent claims (selected)

- §1 conjunct tables and guarded/unguarded columns match all four verifiers;
  attribution phrases match file bytes; `R64C4MultiPatch.md` citation at `:64`
  is accurate ("the requested self-test was not run … parent owns
  post-integration verification" verbatim).
- §6.2 seven census commands run verbatim from the lane root; outputs match the
  SKILL's claims: rows `35`, malformed `0`, tier `A=33 C=2`, status
  `mined=30 queued=1 rejected=4`, no duplicate ids, no enum violations, no
  missing mined `used-by` paths.
- §6.1 exit-code semantics verified against `reports/round-64/measure.py` tail:
  `sys.exit(2 if not evaluable else 0 if holds_ok else 1)`; `HOLDS_OK_V2` is
  printed, not folded into the exit code (uses attributed counts incl.
  `C4_RECEIPT_KILLED_ATTRIBUTED`, `len(mismatch)==0`).
- `reports/round-64/measure.py` sha256
  `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168` verified.
- `measure-before.log` prints `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`,
  `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `K_HELD_BACKED=7/14` — as cited.
- §7 knowledge/lessons paths all exist at base commit `666ea84b` (`git cat-file -e`
  on all 22 repo paths — OK); `corpus/fixtures/REPLAY.md` exists; ten
  `corpus/verify_*.py` = 10 (census count claim).
- `truth.json` keys verified: `image{path,sha256,size}`, padding
  `{offset,size,kind,fill_hex}`, zlib `{offset,size,kind,name,decompressed_member
  {sha256,size}}`, `build_recipe` fields incl. `compression{format,
  implementation,level,compile_version,runtime_version}` and `members[{name,
  offset,payload_utf8}]` — candidate's shape description is accurate.
- Fleet contract `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
  exists; rule numbers cited (1 row-a-claim, 2 append-only/supersedes, 6
  credential ban, §Census) all verified at the cited text.

## 4. Residual risk / verification gaps

- **Tier-B gloss (§3 table).** SKILL renders tier B as "strong secondary … only
  where Q01's scope test passes"; contract says B = "strong secondary …" and Q01
  says each load-bearing claim rests on a row "tier A for that claim's scope",
  tier C never sole support. A literal reader could credit a B row where Q01
  demands A. Existence-wise all cited sources exist; this is a wording risk, not
  a phantom.
- **`cwd=/` contract nuance.** `claims.md` freezes invocation cwd as `/`; the
  SKILL says "from the lane root". The relative counter path requires the lane
  root in practice (my census ran so); flagging the doc-level deviation only.
- **Queued row S007** is cited for "where version-scoped reports live" — the row
  exists (status `queued`), but its scope was never mined; citing it in the
  existence table is safe, but §7's "credited for" gloss should not be promoted
  to load-bearing until the row is mined.
- **M36 source is the contract, not a landed lesson.** `corpus/lessons/
  round-64.md` is not yet committed (draft at `/tmp/revenger-r64-lesson/
  round-64.md:182`); the candidate correctly cites `reports/round-64/claims.md`
  §131 for the M36 row, so no phantom — but the id's canonical lesson record is
  still in-flight.
- **No executable command cited with a wrong argv.** All census/replay commands
  verified verbatim; `--self-test` accepted by the ten verifiers (argv plumbing
  present in all; `grep -c self.test` on the four named scripts = 0 because they
  use `sys.argv[1]`/`argv[1:]`-style dispatch — flag plumbing confirmed by the
  counter's own census run, which invokes all ten with `--self-test`).

## 5. Verdict

Zero phantom citations; two stale/mislocated anchors (F1 medium, F2 low), one
overclaimed base-commit clause (F3 low-medium), tier-B gloss risk (residual).
No URL citations to validate (candidate restates none — self-consistent).
SHONEN box 1 checklists/tables/cited-sources requirement is met on the citation
axis; admission remains a named non-author verifier's call.

Tooling: no installs. Sweep tool retained at `/tmp/revenger-r64-cites/sweep.py`
with output `/tmp/revenger-r64-cites/sweep-out.json` (lane scratch, removed on
landing per round rules).

Report: .ufo/waves/round-64/R64ReviewSkillCites.md
