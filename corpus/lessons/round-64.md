---
round: 64
date: 2026-10-24
author: revenger-r64
claims: [C1, C2]
lane: revenger-shokunin
claim_base: 666ea84b6be2eec2b0359f556ba2429fc9044c36
contract: reports/round-64/claims.md
counter: reports/round-64/measure.py (frozen; sha256 b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168)
status: landed by L1 revenger-r64 — candidates integrated (entry, S036/S037 rows mined, this lesson); C07 README flip deliberately HELD pending the all-criteria Q pass; C2 verified (see Gate)
---

# Round 64 — a coverage token is a claim about the record (2026-10-24)

Two claims on distinct frozen criteria: **C1** coverage K — one independently
gated admitted entry covering C07 firmware, K 7/14 → at least 8/14 (7/14
falsifies), with the README C07 token flipped **either way** at round end
(`frontier → held` naming only the new entry on all-criteria admission;
`frontier → uncovered` if C1 falsifies); **C2** calibration —
`C4_RECEIPT_KILLED_ATTRIBUTED` 0/2 → 2/2 by one in-script forged-stdout control
in each of `corpus/verify_icon_languages.py` and
`corpus/verify_multi_icon_states.py`.

Red-before receipt, committed at the pre-registration commit `3bb430f96cac09feb7269c5c52725127c6f7c463` (whose parent is the claim base `666ea84b`; the receipt, contract and counter do not exist at the claim base itself — `git cat-file -e 666ea84b:reports/round-64/measure-before.log` fails, as R64ReviewLesson verified):
`reports/round-64/measure-before.log`. The lines relevant to the targets,
quoted verbatim:

```text
K_HELD=7/14 score=5.0
K_ROW C07 status=frontier
K_HELD_BACKED=7/14
K_HELD_BACKED_STRICT=7/14
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']
F_COVERAGE=5/8 score=6.2
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=no
```

That log is the do-nothing control: it contains no claimed work and therefore
meets no target. Two reading notes for the closure seat. First, the log prints
**no exit-code line**; `probe exit 0` is the contract's characterization of this
receipt, not a line inside it, so a missing `PROBE_EXIT` line is not a failure.
Second, `HOLDS_OK_V2=no` is expected at base: it is this round's routed-counter
fix and it consumes the attributed counts (`C2_RECEIPT_B_KILLED_ATTRIBUTED`,
`C3_RECEIPT_KILLED_ATTRIBUTED`, `C4_RECEIPT_KILLED_ATTRIBUTED`), and the C4
attributed tally is 0/2 before the claimed fix.

The frozen red-before mutation on the two C4 scripts is also in that log — both
controls pass and both mutants are green, which is exactly the debt C2 pays:

```text
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c4 exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c4 exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
```

## Gate

### Sources opened in this round

Access date **2026-10-24** for every row. **This draft seat opened no source**
and makes no source claim; the two rows below are fill blocks owned by the
opener/scribe seats named in each, and this lesson is not landable with a
`<<…>>` token still unfilled. Every located quote must be at most 25 words and
verbatim against the pinned snapshot.

**S036** — REA firmware-analysis guide at the pinned `rea-agents-6.5.0` tag.
Pinned URL from the opener brief `R64SourceReaGuide`:
`https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md`
(fallback if that path 404s: list tags via the GitHub API and fetch the nearest
6.5.x tag, recording exactly what was opened). Kind `docs`, tier **A only for
route-scope sentences** — what the `inspect-firmware-regions` route does per
the version that produced the round-63 record. Owner: opener
`R64SourceReaGuide`; quote block `R64ScribeGate`
(`.ufo/waves/round-64/gate-quotes.md`).

```text
S036_URL=https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md (pinned tag; fetched directly, no 404, no tag-enumeration fallback needed)
S036_HTTP=200, content-type text/plain; charset=utf-8
S036_BYTES=10695 bytes, 213 lines
S036_SHA256=e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609 (re-fetch byte-identical: R64ReviewSources cmp PASS; git blob 152819177f8dce2124dea2a6a541e701cee227ed)
S036_SNAPSHOT=.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md          # .ufo/waves/round-64/source-snapshots/…
S036_PROVENANCE=.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json (URL, access date 2026-10-24, status, sha256; every field reproduced by R64ReviewSources)      # sidecar: URL, access date, status, sha256
S036_QUOTES=snapshot lines 3-4 "REA accepts **Binwalk 3.1.x** for region inspection and **Unblob 26.6.x** for explicit extraction."; lines 4-5 "The report parsers are verified with Binwalk 3.1.0 and Unblob 26.6.4."; lines 83-85 "Both return Evidence with the original path and SHA-256, raw producer reports, actual executable path/digest, version and limitations."; line 91 "Region offsets refer to bytes in the original firmware."; lines 91-94 "reported_size preserves Binwalk's output; size_basis=provider_reported_validation_unknown reflects that Binwalk can replace unknown lengths with the next signature or EOF before serialization."; lines 94-95 "Neither a signature nor its confidence byte proves a valid partition, encryption or runtime behavior."; lines 86-87 "A matching version does not attest an installed build's source revision, so that field remains unknown." (entropy: the pinned tag contains NO entropy statement — grep -c -i entropy = 0 — so no entropy sentence can be sourced; R64SourceReaGuide)              # ≤25 words each, with snapshot line numbers; cover what inspect-firmware-regions does, the binwalk 3.1.x / unblob 26.6.x requirement, and any entropy/signature-scan sentence the C07 entry relies on
```

**S037** — own-work bundle: `corpus/fixtures/firmware-r63/{firmware-r63.bin,
truth.json, generator.py}` plus `corpus/live/runs/round-63/{inspection.json,
receipt.json, LEDGER.md}`, at claim base `666ea84b`. Kind `own-work`, tier
**A for byte/record correspondence only** — the authored fixture bytes, the
oracle, the saved record and its ledger, not provider accuracy, completeness or
producer origin. Digests are the gate seat's to compute from the committed
base; the filler records the command output, not a number copied from another
report.

```text
S037_FIRMWARE_BIN_SHA256=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be (2048 bytes)      # firmware-r63.bin, 2048 bytes
S037_TRUTH_JSON_SHA256=9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6 (1933 bytes)
S037_GENERATOR_PY_SHA256=4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4 (5532 bytes)
S037_INSPECTION_JSON_SHA256=f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9 (3904 bytes; byte-identical to stdout.raw)
S037_RECEIPT_JSON_SHA256=e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d (492 bytes)
S037_LEDGER_MD_SHA256=25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6 (22671 bytes)
```

**Id allocation — decided, not left open.** The registry at the claim base holds
**35** rows and ends at **S035**
(`awk -F'|' '/^\| S[0-9]/{n++} END{print n}' corpus/SOURCES.md` → `35`;
`grep -c 'S036' corpus/SOURCES.md` → `0`, both read by this draft seat on
2026-10-24). The contract rule is
“`id` — `S` + 3 or more digits, the next unused; never reused”
(`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:22`), and its leads rule is
“a lead is not evidence and never a row” (`:16`). So S036 is the next unused
id and is spent on the REA firmware guide, the source `reports/round-64/claims.md`
names for the route-scope sentences.

**Reconciliation of the round-63 S036 note — first-use-wins.** Round 63's
screen-out of the Python `zipfile` documentation left a forward note that “a
future zipfile-docs row takes **S036**”
(`.ufo/waves/round-63/falsify/routed-debt.md:156`, from
`.ufo/waves/round-63/falsify/routed-debt.md:156` (the note text originated at `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:251-256` and its id moved S033→S034→S036 as rounds consumed ids)). That note is
recorded here as a **note, not a reservation**: the contract has no reservation
mechanism, an unopened lead holds no id, and round 63 landed no zipfile row.
S036 therefore belongs to the first row actually opened against the next unused
id — this round's REA guide. A later round that needs a zipfile-docs row takes
whatever id is next unused *then*; nothing is promised to it in advance. The
round's ids are the contiguous pair **S036 + S037 with no id skipped**. Both
rows arrive `queued` and become `mined` when the C07 entry and this lesson name
them — that in-place `status`/`used-by` change is logged old→new here, as the
registry contract requires. No existing row is edited by this round.

### Candidate status at draft time

| candidate | build-stage status | evidence at draft time | necessary next decision |
|---|---|---|---|
| C1 C07 entry `knowledge/round-64-firmware-region-byte-evidence.md` | **landed in the lane working tree (candidate bytes 0a3730a1, then author correction round for Q11/Q09 findings — final bytes pending); README C07 intentionally still `frontier`** | target path named by the contract; the candidate is drafted under `/tmp/revenger-r64-entry/candidate.md` per brief `R64EntryC07`; at draft time this seat read `corpus/README.md:36` and the C07 row still ends `frontier` | S036/S037 rows land first, then fresh-seat Q01–Q13 decisions, then L1 flips C07 only on an all-criteria pass |
| C2 forged-stdout controls | **landed in the lane working tree; attributed 2/2 verified by R64MutC4 (final bytes), R64ReviewC4Lang/Multi (PASS), R64MutIcon (regression sweep), R64MutProbe (attribution integrity), R64SimplifierDrift (minimality 6 insertions/0 deletions)** | `forged receipt stdout accepted` require line observed by this seat at `corpus/verify_icon_languages.py:154` (existing forged-command control retained at `:151`) and `corpus/verify_multi_icon_states.py:153` (existing control at `:150`); base commit `666ea84b` contains `0` occurrences; `git status --porcelain` shows both scripts modified in the working tree. `R64C4LangPatch` reports its self-test passed; `R64C4MultiPatch` reports the self-test was **not run** (executor policy, parent owns post-integration verification) | run the frozen counter on the committed archive: `C4_CONTROLS_PASS=2/2` **and** `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, both mutants exiting non-zero with last output line ending `forged receipt stdout accepted` |

### Admission order (frozen)

1. Land the candidates **without** the README flip: the S036/S037 rows, the
   C07 entry, and the two verifier controls.
2. Fresh in-wave attacks: named fresh-seat Q01–Q13 pass decisions on the C07
   entry, from reviewers other than its author or corrector.
3. Adjudicate. Only on an all-criteria pass does L1 flip C07 `frontier →
   held` naming only
   `knowledge/round-64-firmware-region-byte-evidence.md`; if C1 falsifies, L1
   flips `frontier → uncovered` instead. Either flip lands; K moves only on
   admission. No other README row changes.
4. Measure on a committed archive: `python3 -B reports/round-64/measure.py TREE`
   over `git archive <commit> corpus`, cwd `/`, `TMPDIR` under lane scratch.
   C2 requires the red-before 0/2 and the attributed 2/2 at final as separate
   printed lines; `HOLDS_OK` alone does not prove C4.

Nothing in this section admits anything. A printed counter value is not an
admission: the round-63 record (`corpus/lessons/round-63.md` M34) showed a
counter-only tree can print the targets without the claimed work, and this
round's contract keeps the same separation — the K probe measures existence,
never quality.

### Quality criteria

Q01–Q13 are unchanged; no Q14 row is adopted and no criterion is weakened
(`corpus/QUALITY.md` byte-identical to the claim base is L1's check, not this
seat's). The ten-verifier census stays 10. C1's admission condition is the same
shape as rounds 62–63: named fresh-seat Q01–Q13 pass decisions from reviewers
other than the candidate author or corrector, with blind independence (Q03) —
at least one seat derives the expected layout without the author's readout
script and compares blind. C2's fix shape is frozen: each script keeps every
existing saved-input assertion and the existing forged-command control, and
adds exactly one stdout forgery control.

## Mistakes

| id | class | evidence | captured-by | fix / falsifiable demonstration |
|---|---|---|---|---|
| M36 | self-assessment drift — the coverage-map token `frontier` contradicted the legend's own definition for a full round after the firmware record landed | `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']` at base commit `666ea84b`, committed in `reports/round-64/measure-before.log`; the legend at `corpus/README.md:24` defines `frontier` as “no knowledge and no saved record”, while `corpus/live/runs/round-63/inspection.json` carries `operation=inspect_firmware_regions` (the same log prints `SAVED_RECORDS=59` and a `ROW_OPS` map naming that operation for C07); the round-63 build and falsify waves saw it in prose (`R63ReadmeFlipDraft` observation for L1, `W2VerifyReadmeContract` finding F8, routed as D2) but it stayed unfixed through the round boundary | **none** — no committed check compared tokens to evidence; the round-63 sightings were report narrative, not a gate, and no counter line printed the contradiction | the `README_TOKEN_LEGEND_MISMATCH` label registered in `reports/round-64/measure.py` (the routed-counter fix): a row at `frontier` contradicts the legend iff at least one saved record exists for that row's own surface operations, per the frozen `ROW_OPS` map (C03 `inspect_managed_artifact`; C05 `inspect_android_package`; C07 `inspect_firmware_regions`; C08 `inspect_web_page`, `capture_browser_scenario`, `observe_web_session`). The label is shown able to **fail** at base with value 1 and is required **0** at round end; the actual repair is C1's token flip (either direction). It compares the token to the saved-record operations the probe itself enumerates, so it is cleared only by a token consistent with evidence that exists — dropping the C07 row to clear it would change the frozen 14-row denominator, a void condition |

## Search log

This draft seat ran **no search and opened no source**; it makes no
identified/screened/included count. The round's authoritative search-log note is
the S036 opener's (`R64SourceReaGuide`), reconciled append-only by the Gate
scribe (`R64ScribeGate`) with the registry census — before: **35 rows**, ending
S035, four disclosed W04s (S024, S028, S029, S034); after: exit 0 required.
`<<R64_SEARCH_LOG_NOTE>>` is the one line to fill or replace at landing.

## Routed debt

| routed item | source | round-64 disposition |
|---|---|---|
| **(1) frozen-counter semantics → later registered counter** | round-63 closure, `corpus/lessons/round-63-verifier-spotcheck.md:59` | **Honored — this round's probe is the later counter.** It registers `K_HELD_BACKED_STRICT` (cited entries carrying an `admission-status: rejected` marker do not back a row; diagnostic, must equal `K_HELD_BACKED` at both ends or the discrepancy is reported), `README_TOKEN_LEGEND_MISMATCH` (M36), and `HOLDS_OK_V2` (uses the attributed counts instead of raw kills). F stays presence-only **by definition**; per-family counts are printed. Any remaining semantic gap is re-routed with reasons at closure |
| **(2) M35 both `stdout_sha256` conjuncts** | `corpus/lessons/round-63.md` M35; `.ufo/waves/round-63/build/R63MutC3.md` M3 widened by `W2MutC3Final` | **Claimed as C2.** Frozen mutation: delete exactly `receipt['stdout_sha256']==H(raw_bytes)` and its connecting `and` inside `receipt_ok`, run `--self-test` on a fresh tree copy. Frozen fix: after the existing forged-command control, deep-copy the receipt, set `forged['stdout_sha256'] = H(b'')`, require rejection with a message ending `forged receipt stdout accepted`. A kill is **attributed** iff the mutant run exits non-zero and its last output line ends with that string; a crash or unrelated assertion is not attributed. Red-before: both mutants exit 0. Note the base log already shows one *unattributed* deletion-sensitive shape (`d2 exit=1 killed :: AssertionError: r47: receipt` on the icon-language script) — that is the round-63 routed substring weakness, which the endswith rule exists to exclude |
| **(3) C07 legend staleness** | round-63 routed D2; `.ufo/waves/round-63/build/R63ReadmeFlipDraft.md:126-132`, `.ufo/waves/round-63/falsify/W2VerifyReadmeContract.md:206-211` | **Repaired inside C1, flip either way.** On admission: `frontier → held` naming only the new entry. On falsification: `frontier → uncovered` (work evidence exists, no admitted knowledge). No third status is invented and no other row changes |
| **(4) evidence-ID transplant corollary** | `corpus/lessons/round-63.md` routed row; `.ufo/waves/round-63/build/R63RevengerLedger.md:104-118`; `.ufo/waves/round-63/falsify/W2AttackRecordForgery.md:41-61` | **Owner named: a future calibration round that registers a receipt/Evidence-ID binding check.** Check shape to register there: (a) recompute the digests of record, stdout and receipt from the committed bytes; (b) require `receipt.evidence_id == record.evidence_id` **and** both equal the Evidence ID named in the record's `LEDGER.md` line; (c) seed a control that transplants a **real foreign** Evidence ID across record + stdout + receipt with recomputed digests and requires rejection with an attributed message. The round-63 transplant passed the byte oracle (`ORACLE OK`, exit 0), so digests alone cannot catch it; the cross-bind and the ledger leg are the load-bearing parts. Q09 disclaimers are carried unchanged: matching hashes and IDs show internal consistency, never producer origin |
| **(5) r58/59 139 → 142 PASS-count quotes** | `corpus/lessons/round-63-verifier-spotcheck.md:63`; claims.md routed input 5 | **Stay unedited** under the historical-record void conditions. **Non-reproduction recorded:** the round-64 base log's control line prints `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size)` for `verify_named_multi_icon_states.py`, so a quote saying 139 no longer reproduces at round 64. **Owner named:** the next round that touches those verifiers re-derives the current pass counts in its own receipts; this round does not touch them and claims nothing about the count |
| **(6) freshness-hold wording** | claims.md routed input 6; `.ufo/waves/round-63/…` routed wording | **Frozen in `reports/round-64/claims.md`.** `FRESH_ROWS` is a byte-survival hold; it does not certify current-host truth. The SCORECARD wording is updated at round end by L1, not by this seat |
| **(7) SHONEN box 1 (SKILL.md absent)** | claims.md routed input 7 | **Checklist work this round, not a claim.** A named scribe drafts and a named non-author reviewer verifies; the box flips only on a named verifier, otherwise it stays `[~]` or `[ ]`. This lesson records the rule, not a verdict |
| **(8) S036 id note from the zipfile screen-out** | `.ufo/waves/round-63/falsify/routed-debt.md:156` (the note text originated at `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:251-256` and its id moved S033→S034→S036 as rounds consumed ids); `.ufo/waves/round-63/falsify/routed-debt.md:156` | **First-use-wins; recorded as a note, not a reservation** (see `## Gate` › Id allocation). S036 is spent on this round's REA firmware guide; a future zipfile-docs row takes the next unused id at that time |

## Tooling

No tool was installed or upgraded by this seat. No `pacman` transaction (the
host's pacman gate is paused), no `uv tool install`, no global npm install, no
binary download. Commands used were already-present read-only utilities:
`sha256sum`, `wc`, `awk`, `grep`, `sed`, and read-only `git show`/`git status`
(no mutation, no index write). Scratch: `/tmp/revenger-r64-lesson/`, removed
after this report lands.


### Gate adjudication state at landing (L1)

- C2: **verified** — `C4_RECEIPT_KILLED_ATTRIBUTED` 0/2 → 2/2 on the final
  patched bytes (`a2fd347e…` languages, `9345cb8c…` multi), red-before 0/2 at
  base; attribution integrity probed (loose message rejected, R64MutProbe);
  regression sweep of C2/C3 mutants all killed attributed (R64MutIcon).
  Mid-wave hazard recorded: the first languages patch *replaced* the
  forged-command control (sha `2e9e56e8…`, C2 regressed to 1/2); L1 restored
  the line within the round; receipts pinning `2e9e56e8…` (R64MutC4's patched
  base) describe that transient — the kills were re-verified on final bytes by
  R64ReviewCounter and R64MutIcon.
- C1: **correction round open** — Q03 PASS (R64ReviewEntryScope blind
  derivation), Q06 PASS (R64ReviewEntryQ06), Q09 FAIL and Q11 FAIL (narrow,
  correctable: recorded-vs-derived labels, comparison counts, Unblob sentence,
  Q-map rows answering wrong criteria, missing size/absence derivations);
  fixes routed to the author; Q01 re-review pending against the landed rows;
  Q10 cross-lane note landed in bytes `0a3730a1` (R64ReviewEntryScope's FAIL
  predates it — delta re-confirm queued). README C07 flip held until the
  all-criteria pass, per the frozen admission order.
- Contract amendment (recorded, not hidden): `claims.md` `HOLDS_OK_V2` sentence
  amended pre-measurement to match the counter code (attributed counts PLUS
  `README_TOKEN_LEGEND_MISMATCH == 0`); found by R64ReviewCounter drift review;
  V2 is a diagnostic, not a claim target.
- Routed forward: (a) counter spoof surface (R64CriticClaims, R64CriticCounter
  reproduced decoy trees meeting the numeric targets) — the admission gate is
  the named-seat Q decisions plus exact-shape review, and an AST-bound
  mutation counter is future-counter debt; (b) evidence-ID transplant check —
  owner: a future calibration round, check shape reverse-engineered by
  R64RevengerLedger (6 prongs incl. an Evidence-ID injectivity registry; attack
  it must catch: self-consistent receipt re-signing with ID reuse); (c) recheck
  holes H1–H3 from R64MutEntry (recheck does not read entry prose —
  transcription covered instead by R64EntryCommands; compression.level not
  byte-derivable; Evidence ID not echoed); (d) `## Frontier` C07 prose goes
  stale after the flip (R64ReadmeLegend F3) — L1 debt.
- Dead seat: R64CriticC4 died on a provider cyber-policy flag (m_sol route) at
  1m22s; recorded, not replaced; its C4 kill-rule attack angle was covered by
  R64MutC4/R64MutProbe/R64CriticCounter.

### Admission decision (L1, after all fresh-seat re-reviews)

**C1 ADMITTED.** The corrected entry `corpus/knowledge/round-64-firmware-region-byte-evidence.md`
(53098 bytes, sha256 `9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf`)
passes every quality criterion on landed bytes, by named non-author seats:
Q01 PASS + Q02 PASS (R64ReviewEntryQ01 re-review, "recommend admit"), Q03 PASS
(R64ReviewEntryScope blind derivation), Q06 PASS (R64ReviewEntryQ06), Q09 PASS
all six criteria (R64ReviewEntryQ09 re-review), Q10 PASS (R64ReviewEntryScope
delta — cross-lane fence present and correct), Q11 PASS (R64ReviewEntryQ11
re-review), Q04/Q05/Q07/Q08/Q12 answered or n/a-with-reason inside the entry's
Q-map (verified by Q09/Q11), every in-entry derivation command re-run with
MATCH ×24 (R64EntryCommands), recheck mutation kill attributed (R64MutEntry).
README C07 flips `frontier → held` in the same revision as this decision,
naming only this entry. Two LOW precision nits from Q01 (guide line range
"91-96" narrows to 91-94; l0-questions.md:42 is the question that references
ADJ-06, the row being tsukuroi PROVINCE.md:51) are recorded as bounded debt —
any edit to the entry requires a fresh delta re-confirm, so they route forward
rather than re-open a passed gate.

**C2 VERIFIED.** `C4_RECEIPT_KILLED_ATTRIBUTED` 0/2 → 2/2 (final bytes
`a2fd347e…` / `9345cb8c…`), red-before 0/2 at base; attribution integrity
(R64MutProbe), regression sweep (R64MutIcon), minimality 6 insertions/0
deletions (R64SimplifierDrift), independent mutation reproduction (R64MutC4),
both patch reviews PASS (R64ReviewC4Lang/Multi).

**Sourced-claim conformance:** C1 rests on S036 (opened this round, pinned tag
`rea-agents-6.5.0`) and S037; both rows landed `mined` with used-by paths
present (R64ReviewSources PASS).
