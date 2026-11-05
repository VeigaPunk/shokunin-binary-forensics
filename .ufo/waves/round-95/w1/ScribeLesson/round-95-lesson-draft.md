# Round 95 lesson — DRAFT for the L1 (scribe seat `ScribeLesson`, wave `revenger-r95-w1`, attempt 1)

Drafted by the `ScribeLesson` seat, read-only over the lane. Every path below is relative to the
lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Freeze
`6e0bf15fed58f357b7fa0c881371ac7616a116f7` (claims, v4 counter, battery4, controls, the
superseding candidate entry, the S500/S501 receipts) — all frozen bytes, unedited by this seat.
Base `cb5c26f73c99af268bc71e9f7417bfd7e7738d83` (round-94 adjudication tip).

**Scribe's own scope note.** This seat writes only inside
`.ufo/waves/round-95/w1/ScribeLesson/` and its scratch
`/fast/scratch/hyaku/revenger-r95/ScribeLesson/` (deleted on exit). It edited no lane file, ran no
git/jj write command, and installed nothing. Where a number in this draft comes from a landing
tree that is still uncommitted, the draft says so and names the command that produces it; the
L1 re-derives at landing.

## Gate

### Candidates CONSIDERED this round for the coverage-K move

Three candidates were considered. One admitted, two rejected. The rejects are recorded with
reasons and flip conditions so the non-author closure has at least one reject to sample
(the round-94 spot-check defect C-a).

#### (a) ADMISSION candidate — the superseding entry `knowledge/round-95-evidence-ledger-discipline.md` (coverage-map row C10)

- **What it is.** A NEW entry file that supersedes the round-74-rejected candidate
  `knowledge/2026-10-29-rea-evidence-ledger-discipline.md`. The superseded file's bytes are
  unchanged and its `admission-status` still reads `rejected` (sha256
  `fee514ccbd2986de9828a729ccd029fdcd2f9da6498b49af6fb9bdfe23d232de`, identical to the freeze
  commit's blob) — the CORPUS corrections rule (new entries, never rewrites) was honoured in
  both directions: the old candidate is not reopened, the new one is a different file.
- **What the decision rests on.**
  1. **Two source rows opened THIS round (S500, S501), receipts frozen pre-data.** Both are
     `mined`, tier A, `opened 2026-11-05`, with `used-by` pointing at this entry. Their bodies
     and receipt JSONs were committed at the FREEZE commit (`git ls-tree -r 6e0bf15` lists
     `reports/round-95/quote-receipts/{S500.receipt.json,S501.receipt.json,fetch-log.md,raw/S500.body,raw/S501.body}`),
     so the opening evidence predates every seat's vote.
     - **S500** — REA Evidence schema, drift check of **S098**,
       `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts`,
       HTTP 200, 17010 B, sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`.
       Located quote (11 words, ≤25), body span `[3149,3223)`: *"Source authority vocabulary
       owned by Evidence and reused by its consumers."* — re-hash, span and quote verified
       byte-exactly by this seat and by the `ScoutReopen` re-fetch.
     - **S501** — REA EvidenceLedger, drift check of **S096**,
       `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts`,
       HTTP 200, 18784 B, sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`.
       Located quote (7 words, ≤25), body span `[2136,2198)`: *"Record evidence idempotently;
       conflicting content is rejected."*
     - `corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts
       reports/round-95/quote-receipts --sid S500 --sid S501` → `SUMMARY rows=2 verified=2
       unreachable=0 unresolved=0`, exit 0 (re-run by this seat over the scratch tree).
     - The **fetch log** `reports/round-95/quote-receipts/fetch-log.md` names both sids with both
       sha256 values — the frozen `C1_RECEIPTS` leg's log-naming requirement.
  2. **Drift-check verdict: no drift on the two re-verified rows.** The S500/S501 re-opens
     confirm the S098 confidence enum (`observed`/`derived`/`inferred`) and authority vocabulary,
     and the S096 `record` idempotency + conflicting-content rejection, are unchanged at REA
     revision `12f6e09`. No older scope cell is corrected, so neither S096 nor S098 is
     superseded — their `status` stays `mined` and their anchors stay as filed.
  3. **A Q-map with a decision for every QUALITY.md criterion.** The entry carries its own
     `## §Q-map` with a row for each of Q01–Q17 (PASS / n/a + reason). It is documentation-only:
     no REA run, no tool output, no saved-record oracle. The `Q04`/`Q10` rows state the scoping
     limits; `Q09` states that no digest is offered as origin/authenticity.
  4. **Votes pending at drafting time.** The vote-binding digest is
     `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` (recipe in the wave
     context, run from the lane root; identical to the raw file sha256 today because the entry's
     only `admission-status:` line, at line 21 inside the 30-line header window, already reads
     `admission-status: candidate`, so the normaliser is the identity transform).
     - **The digest is flip-invariant, and the L1 must know why.** Measured over the freeze bytes:
       normalising the status line yields the SAME digest whether it reads `candidate` or
       `admitted` (`476edc36…` both ways), while the raw sha256 of the flipped file differs
       (`c70259fc…`). So the L1's single admission-status flip does **not** re-open the digest and
       does **not** force a vote re-bind — **provided the flip is the only byte changed**. Any
       other byte change in the entry re-opens the digest and all votes must be re-bound (the
       r93 M1 procedure). This is the same finding the r94 scribe recorded, re-confirmed on this
       round's bytes.
     - Two votes were filed in the wave at the time of this draft, both binding the digest above:
       `ReviewerGate` (reviewer) PASS 8 / n-a 9; `ReviewerBlind` (reviewer) PASS 7 / n-a 10.
       `CriticR95` (critic) had not yet filed. The frozen `C1_VOTES` leg needs **≥2 accepted
       votes**; the third vote is the lane's own to land.
     - Each filed vote's artifact is a distinct, non-empty file inside its own seat dir, naming
       both its seat and the digest: `ReviewerGate/evidence.md`
       (sha256 `ce1f94eb3d037cc2555f265c6c1e37f8a25b600c59c9918c290cfe5a57133890`) and
       `ReviewerBlind/derivation.md`
       (sha256 `62e125f38c898c82341f75964c6c60d4b1c296f5b1c5d319a371f9fa5dcd3a19`). This seat
       re-checked the second value against the file on disk: it matches.
  5. **The coverage row moves `partial` → `held`.** The C10 row's knowledge-file set must be
     EXACTLY `[knowledge/round-95-evidence-ledger-discipline.md]` under the frozen `C1_C10_CITES`
     leg. Verified over the landing-tree copy: `row_fileset` parses to that one file and no
     other, and every other coverage row is byte-identical to the frozen base (`C1_ONLY_C10=none`).

#### (b) REJECTED — a seventh C05 Android candidate (round-95 K-move on the APK row)

- **Reason.** Six rejected C05 candidates are already on record — `round-65`, `round-67`,
  `round-68`, `round-69`, `round-70`, `round-71` APK/AXML byte-evidence candidates, each filed
  with `admission-status: rejected` and a located Q-failure (Q02/Q06/Q11 anchor drift at r65;
  Q02 anchor precision at r67; Q04/Q05/Q07/Q11 at r68; Q05/Q07/Q08/Q11/Q14 at r69; Q04/Q11b/Q13
  at r70; Q09/Q16 at r71). **No new sourced APK byte-evidence was opened this round**: the only
  rows opened are S500 and S501, both REA TypeScript sources, neither an APK/AXML source. A
  seventh candidate would therefore repeat a known failure against the same primary sources
  rather than rest on new bytes.
- **Flip.** A newly opened primary source carrying located AXML byte-level rules that the Q-map
  can cite without prose credit to a script — i.e. new sourced byte evidence, not another
  re-gate of the same records.

#### (c) REJECTED — re-admitting the 2026-10-29 C10 candidate in place

- **Reason.** The CORPUS corrections rule (**new entries, never rewrites**; `CORPUS.md` §Files
  the path writes) plus the round-74 frozen kill rule, which set that candidate's status to
  `rejected` because the required multi-seat Q review could not run on that round's host — a
  dispatch-surface fact, not a quality finding against its content. Re-admitting it in place would
  be exactly the rewrite the rule forbids, and would discard the superseding entry's own
  §Supersession section and the two 2026-11-05 drift-check re-opens.
- **Flip.** None needed. The supersession entry (a) covers the ground: it carries the candidate's
  ledger-layer table, qualification rule and boundaries byte-wise, adds the S500/S501 drift-check
  re-opens folded into the two rows they re-verify, and adds the §Q-map. The rejected file stays
  byte-preserved as the record of why the round-74 review could not run.

#### Q17 note for the Q-map

Q17 (QUALITY.md) asks that, **when an adjudication relocates a cited artifact**, every citation of
the old path is swept in the same commit, and that a filed entry gains an appended dated
correction naming the old and the new path. This round's disposition, stated for the entry's own
`## §Q-map` Q17 row (which the entry marks `n/a`):

- **No artifact was relocated.** The 2026-10-29 candidate stays at
  `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md`, byte-preserved (sha256
  `fee514cc…`, verified identical to the freeze blob). The new entry is a NEW file at a NEW
  path. There is no old path to sweep, so Q17's sweep clause has no object here — the entry's
  `n/a` is correct.
- **The sweep check was nevertheless run** over the landing tree, read-only:
  `PYTHONUTF8=1 python3 -B reports/round-90/source_path_check.py --root .` →
  `SOURCE_PATH_ROWS=501`, `SOURCE_PATH_ROWS_CHECKED=40`, `SOURCE_PATH_MALFORMED=0`,
  `SOURCE_PATH_DEAD=0`, `SOURCE_PATH_EXCUSED=1` (S481 excused by S486), exit 0.
- **One stale cross-candidate pointer is disclosed, not fixed here** (it is a candidate file, not
  an admitted one, and it does not make a path dead): `corpus/knowledge/round-73-re-resource-atlas.md:434`
  still describes `knowledge/2026-10-29-rea-evidence-ledger-discipline.md` as the *C10 candidate*.
  After this round's admission that description is out of date. Because the atlas is
  `admission-status: candidate` and the correction rule forbids in-place rewrites of filed bytes,
  the honest fix is an appended dated correction in the atlas (or its admitting round's lesson),
  not an edit of that line. **Route to the round that admits the atlas; do not edit it here.**
  (The `C10` row in `corpus/README.md` no longer points at the 2026-10-29 file, so no coverage row
  mis-cites it.)
- **The `seed.md` back-reference is intentionally left alone.** `corpus/knowledge/seed.md:4`
  declares `coverage-map: C02, C10, C12, C14` and still exists as the pre-contract C10 reminder;
  the new entry's Limitations section says so explicitly (*"Seed.md's C10 note remains the
  pre-contract reminder; this entry is the sourced expansion"*). The frozen `C1_C10_CITES` leg
  requires the C10 row's knowledge-file set to be exactly the one admitted file, so `seed.md`
  cannot stay in that cell; the entry keeps the pointer in prose where it belongs.

### Gate verdicts the L1 must record from the frozen instruments

- **C1 (coverage K, `partial` → `held`)** — predicate `C1_VERDICT=pass` from
  `PYTHONUTF8=1 python3 -B reports/round-95/c1_k_admit_counter4.py --rev <landing>`.
- **C2 (calibration)** — predicate `BATTERY4_VERDICT=pass` from
  `PYTHONUTF8=1 python3 -B reports/round-95/forge_battery4.py --stage full`.
- Both predicates, the counters, the control receipts and the kill rules are FROZEN bytes
  (`reports/round-95/claims.md`, `c1_k_admit_counter4.py`, `forge_battery4.py`). Nothing in this
  draft proposes a change to any of them.

## Mistakes

Mined; class · evidence pointer · captured-by · fix. Seven rows; the found-none sweep was not
needed.

| id | class | evidence pointer | captured-by | fix (shown able to fail) |
|---|---|---|---|---|
| **M1** | **reaped-scratch dependency in a committed frozen instrument (r94 M1 class, recurrence).** The frozen `reports/round-94/forge_battery3.py --stage full` mkdtemps under its own `SCRATCH` constant (`/fast/scratch/hyaku/revenger-r94/battery3`) without creating that root. With the root reaped, the stage dies with `FileNotFoundError` from `tempfile.mkdtemp` **before any verdict line prints**, so the run looks like a crash, not a failure. | `reports/round-95/forge_battery4.py` HOLD leg: `Path(b3.SCRATCH).mkdir(parents=True, exist_ok=True)` before re-running the frozen r94 battery. **Reproduced by this seat** on a lane-shaped copy of the frozen file with the `SCRATCH` constant pointed at a non-existent root: `FileNotFoundError: [Errno 2] No such file or directory: '…/full-y91uti3c'` at `tempfile.mkdtemp` (receipt `ScribeLesson/battery3-repro-SCRATCH-redirected.py`, the copy is byte-identical to the frozen file except the one `SCRATCH` constant). | **none** — the frozen r94 bytes are not editable mid-round (kumitate r42 rule); the defect is inside a frozen instrument, so it is closed by provisioning around it, not by an edit. | the successor runner (`forge_battery4.py`) **pre-creates the frozen battery's own scratch root** before re-running it; the r94 M1 fix had only provisioned the red-v2 stage's dirs, not the full stage's root. **Able to fail:** the HOLD leg prints `HOLD_R94_BATTERY=pass` only when the re-run actually prints `BATTERY3_VERDICT=pass`; with the root absent the leg would print `HOLD_R94_BATTERY=fail` (`controls/battery4-full-at-freeze.log` carries the green line). **Route for a later freeze:** a committed instrument must create the root it mkdtemps under, or the runner must provision it — the rule is not yet written into the counter/battery contract. |
| **M2** | **helper-only registry gate (r94 M6 recurrence, in the successor's own first draft).** The first v4 draft carried `C1_REGISTRY` as its own leg, but the first V03 duplicate-key delta built the registry JSON in Python, so `json.loads` collapsed the duplicate key before the strict reader ever saw it — the delta never reached the gate it was meant to exercise. | the counter's own strict reader (`strict_json`, `c1_k_admit_counter4.py:80-90`) against `json.loads`; the failure is visible as `SELFTEST_C1V4=fail` with `V03-dup-json-keys-registry: expected fail on C1_REGISTRY, got rc=0 failing=[]`. | the self-test itself (the first run failed; the frozen `controls/selftest-c1v4.log` carries the green `SELFTEST_C1V4=pass legs=24`). | the delta now injects a **literal duplicate member into the raw registry text**, so the strict reader sees it. **Able to fail:** the pre-fix run printed `fail`; the same mutant is now self-test-fatal on v3 (`MUTANT_V3_REGISTRY_SURVIVES=pass`) and fatal on v4 (`MUTANT_V4_REGISTRY_KILLED=pass`) — the r94 finding that the registry check had no own leg is closed by the leg split, not by the delta. |
| **M3** | **red-stage fixture shape mismatch (a body-editing delta moves the digest the fixture's votes are bound to).** The first red-v3 run blocked H1 and V19 with `rc=1`: the delta edits the entry body, which moves the candidate digest, so the fixture's votes no longer bind and the vector is blocked for the wrong reason. | `reports/round-95/controls/battery4-red-v3.log` (final: `V3_REACH_NEW=10/10`) against the first run (`V3_REACH_NEW=8/10`, `RED_V3_VERDICT=fail`). | the red stage itself (`RED_V3_VERDICT=fail` on the first run — it failed closed rather than passing). | the `rebind_v3` helper applies the r93 M1 procedure (candidate digest, artifact bytes and artifact sha256 move together) for body-editing deltas only. **Able to fail:** the `RED_V3_VERDICT` line flips `fail` → `pass` on that change, and the reach count `8/10` → `10/10`. |
| **M4** | **the v3 counter's registry mutant survives its own self-test (r94 M6, shown as a survivor on the frozen bytes).** A code mutant that drops the v3 registry gate keeps `SELFTEST_C1V3=pass` — the r94 finding, reproduced on the frozen bytes. | `reports/round-95/controls/battery4-red-v3.log`: `MUTANT_V3_REGISTRY_SURVIVES=pass` (the committed `MutationR94` `C1_REGISTRY` SURVIVED finding, re-derived). | **none** — the frozen v3 bytes are not editable; the survivor is the point of the red-before. | v4 splits the check into its own `C1_REGISTRY` leg; the same mutant now **dies** on v4 (`MUTANT_V4_REGISTRY_KILLED=pass`, `controls/battery4-full-at-freeze.log`). **Able to fail:** the mutation seat's own run of the v4 mutant prints `SELFTEST_C1V4=fail` with `V03-dup-json-keys-registry: expected fail on C1_REGISTRY, got rc=0 failing=[]` and `M6-forged-registry-seat:` likewise. |
| **M5** | **a revision mislabel in the SKILL.md registry note.** The first registry row said the v4 counter was "frozen at `cb5c26f`"; `cb5c26f` is the **BASE** (`FREEZE_REV`, the round-94 tip), and the freeze commit that carries the frozen bytes is `6e0bf15`. `claims.md` itself was right. | `SKILL.md` registry row for `c1_k_admit_counter4` (label corrected before landing); `reports/round-95/claims.md` header names base `cb5c26f` and the freeze commit in its Carry-in paragraph. | **none** — a prose label, not a predicate; caught by reading the two identifiers side by side. | the label now names the base revision only. **Able to fail:** `git rev-parse cb5c26f` prints the round-94 tip, `git rev-parse 6e0bf15` prints the freeze commit — the two hashes are not interchangeable. **No counter or claim byte changed.** |
| **M6** | **a SOURCES row written without its closing pipe, caught by the census.** The S500/S501 rows were appended with a `used-by` cell and **no trailing `|`**, so each row parsed as 10 fields instead of 11. | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` before the fix: `E01 S500 fields=10`, `E01 S501 fields=10`, exit 1; the same census on the settled file: exit 0, `ok`. The `ExecCensus` seat captured the red run as `census-validate-run1-transient.tsv` (rc 1) and the settled run as `census-validate.tsv` (rc 0). | the census itself (E01) and, independently, this seat's malformed-row awk (`NF!=13` → 2 rows before the fix, 0 after). | the closing pipe appended; census rc 0. **Able to fail:** the E01 codes are the census's own `fields=` count — a row without the trailing `|` reads `fields=10` and a well-formed row reads `fields=11`. **Note the interaction with M7:** the transient red run was observed *while* another writer was editing `corpus/SOURCES.md`, so a re-run on the settled file is what a census receipt must cite. |
| **M7** | **the C10 coverage cell named extra `knowledge/*.md` paths.** The first README C10 cell cited `knowledge/seed.md` and the superseded 2026-10-29 candidate in addition to the admitted entry; the frozen `C1_C10_CITES` leg requires the cell's knowledge-file set to EQUAL exactly `[knowledge/round-95-evidence-ledger-discipline.md]`. | `row_fileset` in `reports/round-95/c1_k_admit_counter4.py` (the leg the claim names); on the pre-trim cell the set had three members. | the frozen leg itself, read before landing (the counter's `C1_C10_CITES` would have failed the whole leg). | the cell trimmed to the admitted entry alone; `C1_C10_CITES=pass` and `C1_ONLY_C10=none` on the landing-tree copy. **Able to fail:** the leg compares the parsed set for **equality**, so an extra path fails it as surely as a missing one. **This is the same shape as the r94 C1_C15_CITES→C1_C10_CITES close (critic H3)**, applied to the row this round moves. |

**Found-none sweep:** not needed — seven mined.

**Open items this seat observed but did not mine into the table** (each is a residual of a frozen
counter or a foreign-lane artifact, so each is routed rather than fixed):

- **Residual A — the frozen `C1_PYCACHE` leg covers only three of the lane's Python surfaces.**
  `check_pycache` scans `corpus`, `reports/round-95` and `.ufo/waves/round-95`. It does not scan
  `reports/round-93` or `reports/round-94`, and a stale
  `reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc` (46897 B, mtime
  2026-11-05 14:23:14 — i.e. before any seat spawned) sits there now, written by an
  `importlib.util.spec_from_file_location` + `exec_module` of the frozen r94 counter **without
  `-B`**. This seat reproduced the mechanism exactly: importing the frozen file by path without
  `-B` writes `reports/round-94/__pycache__`; with `-B` it writes nothing. The frozen r93/r94
  instrument dirs are the two places a frozen counter is most likely to be imported by a
  successor, so they are the two places the `-B` rule most needs to be checked. **Route: extend
  the `C1_PYCACHE` surface list to the frozen instrument dirs in the next successor freeze, and
  have the L1 delete this residue before landing** (it is gitignored, so tracked bytes are
  unaffected, and the `C1_PYCACHE` leg cannot see it — the leg is green on a dirty dir).
- **Residual B — the vote-binding digest is not a byte-identity witness.** The digest normaliser
  replaces every `^\s*admission-status\s*:.*$` line, so two entries that differ **only** in
  whitespace around the status line normalise to the same digest. Measured on the freeze bytes:
  a file whose status line is indented `  admission-status: admitted` and one whose status line
  is column-0 `admission-status: admitted` are **different bytes** (`sha256` differs) but
  produce the **same** vote digest `476edc36…`. The frozen `C1_ADMITTED` leg accepts the indented
  form too (its `STATUS_ANY` anchor is `\s*admission-status\s*:` counted case-insensitively over
  the whole file, and `lines[st_idx[0]].strip().lower()` is compared to
  `"admission-status: admitted"`). A second status line anywhere in the file is still caught
  (verified: a body-line `admission-status: rejected` makes `C1_ADMITTED=fail`), so this is a
  narrow whitespace alias, not a duplicate-status hole. **Route: the digest should be paired with
  a raw-bytes sha256 of the entry in a successor freeze, so the binding is byte-exact.**
  The disclosure belongs in the lesson because the vote binding is presented as byte-bound.
- **Residual C — the L1's landed `corpus/lessons/round-95.md` differs from this seat's scratch
  copy at the M5 row** (the landed row names the SKILL.md registry note; the scratch copy's row
  named the claims header). The scratch copy was a byte copy of the lane taken at 14:38:11 — it
  is the L1's file that is the later edit. **Not a defect in the lesson's substance**; recorded
  so the L1 knows the draft it finalises from is this file, not the scratch copy.

## Frontier and census

### Exact census commands

The fleet driver, from the fleet root (the L1 runs it; the seat ran it read-only):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
```

The seven lane census commands, verbatim from `SKILL.md` §6.2, run **from the lane root**:

```sh
# rows (spacing-tolerant)
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# status histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# duplicate ids — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# enum violations and tier inflation — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
# mined rows whose used-by paths do not exist — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

### Where the before/after logs live

| log | path | content |
|---|---|---|
| **census BEFORE** | `reports/round-95/controls/census-round-start.log` (committed at the freeze) | the fleet driver's round-start run: exit 0, the `ok` line for `corpus/SOURCES.md`, 21 × W01 and 13 × W04 warnings, 0 E-codes. **This log carries no row count** — the claims' "rows 499" is the freeze-commit registry size, which the seven-command run derives separately. |
| **census AFTER** | `reports/round-95/controls/census-round-end.log` — **not yet written at drafting time**; the L1 writes it at landing | the same driver command on the landed tree: exit 0, 0 E, and the seven-command numbers below. |
| **seven-command census (this seat's receipt)** | `.ufo/waves/round-95/w1/ScribeLesson/census-seven-settled.log` | the settled landing-tree numbers (below), run 2026-11-05T14:51:27-03:00 from the lane root. |

### Numbers

| figure | before (freeze `6e0bf15`) | after (landing tree, S500/S501 appended) |
|---|---|---|
| registry rows | **499** | **501** |
| tier histogram | `A=450 B=21 C=28` | `A=452 B=21 C=28` |
| status histogram | `mined=463 queued=16 rejected=20` | `mined=465 queued=16 rejected=20` |
| malformed rows (NF≠13) | 0 | **0** |
| duplicate ids | none | none |
| enum / tier-inflation violations | none | none |
| mined rows with a missing `used-by` path | none | none |
| fleet driver | exit 0, 21 W01 + 13 W04, 0 E | exit 0, 21 W01 + 13 W04, 0 E |
| coverage row advanced | C10 `partial` | C10 **`held`** |
| `K_HELD_BACKED` | 11/15 | **12/15** |

- **Rows added this round:** S500, S501 (tier A, `mined`, opened 2026-11-05, `used-by`
  `corpus/knowledge/round-95-evidence-ledger-discipline.md`).
- **Rows touched old→new (15 rows, `used-by` cell only — the one mutable cell besides `status`
  and `recheck`):** S002 and S096–S109 each gain the round-95 entry alongside the path they
  already listed; **no** `status`, `tier`, `opened` or `recheck` cell changed. Verified by
  cell-by-cell diff of the freeze blob against the working tree (15 rows, field index 10 only).
- **Sourced claim (§2b.4):** C1 rests on S500 and S501, both opened this round.
- **One mistake mined into `corpus/lessons/round-95.md` `## Mistakes`** — the mined set above
  (M1–M7); the round's own claims name the M1-class reaped-scratch defect as the expected
  candidate, and the others were found in this round's own artifacts.

## Assimilation

**Assimilation: none.** The frozen §10 id-collision check was re-run this round, read-only, over
the landed registry and the staged package:

```sh
S=/home/vgpnk/Projects/shokuknow
A=/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-95/w1/ScribeLesson; mkdir -p "$A"
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md \
  | grep -oE 'S[0-9]+' | sort > "$A/reg-ids"
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' "$S/merge/revenger/SOURCES.append.md" \
  | grep -oE 'S[0-9]+' | sort > "$A/staged-ids"
comm -12 "$A/reg-ids" "$A/staged-ids" > "$A/collisions"   # nonempty -> renumber in scratch
```

**Expected: none — and the measured result is none adopted.**

| file | lines | sha256 |
|---|---|---|
| `reg-ids` | **501** | `3778e0b352b7f33b9c8bbfe697a1cdc37049e095e33abb14ab05dd86922e0290` |
| `staged-ids` | **155** | `18ff151052c7ea13e03cd0e12e48f42158d31b79d1bd4e6fb62f9b95404e2631` |
| `collisions` | **155** | `18ff151052c7ea13e03cd0e12e48f42158d31b79d1bd4e6fb62f9b95404e2631` |

`collisions` is byte-identical to `staged-ids`: **every one of the 155 staged ids already exists
in the lane registry**, so nothing in the package is adoptable under the collision rule. The
`ExecCensus` seat measured the same three files independently in
`.ufo/waves/round-95/w1/ExecCensus/assimilation/` with identical counts and identical `collisions`
sha256. The L0 question `revenger | round-91` stays unanswered; the wave-4 quarantine-first duty
is not re-run this round (it was performed in round 92 for all 26 rows).

## considerthese

**Proposal 1 of `considerthese/2026-11-05.md` is ADOPTED as this round's practice.**

- **Citation:** `considerthese/2026-11-05.md`, dated **2026-11-05**, proposal 1 — *"Counter-reachability
  review of each new `claims.md`, written before the round lands. For every frozen predicate, I
  write the cheapest skip-work control I can think of (lookup table, stub that prints the pass
  line, id-edited copy, no-work base) and check whether the round's `controls/` directory already
  has it."*
- **What adoption means here:** the controls were designed and executed **before the freeze**, not
  after the data existed. The round's `claims.md` was frozen at `6e0bf15` together with its
  controls, in one commit.
- **Evidence (the receipt set):** `reports/round-95/controls/` — five files, all committed at the
  freeze commit:
  | file | what it attests |
  |---|---|
  | `c1v4-do-nothing.log` | the **no-work base** fails: `C1_C10_HELD=fail`, `C1_VERDICT=fail`, exit 1 (14 of 17 legs fail on the base). |
  | `selftest-c1v4.log` | the counter's own self-test: `SELFTEST_C1V4=pass legs=24`, exit 0 — the positive fixture plus 22 forged deltas each failing on its frozen expected leg. |
  | `battery4-red-v3.log` | the **red-before**: the frozen v3 counter reaches all 10 TREE vectors (`V3_REACH_NEW=10/10`) and the registry mutant **survives** v3 (`MUTANT_V3_REGISTRY_SURVIVES=pass`), `RED_V3_VERDICT=pass`. |
  | `battery4-full-at-freeze.log` | the **after**: `V4_KILLS=10/10`, `MUTANT_V4_REGISTRY_KILLED=pass`, `POS_C1V4=pass`, `DO_NOTHING_C1V4=fail-as-required`, `HOLD_R94_BATTERY=pass`, `BATTERY4_VERDICT=pass`, exit 0. |
  | `census-round-start.log` | the fleet census at round start: exit 0, `ok`, 0 E-codes. |
  - **and this round's own M2**: the self-test caught a helper-only delta **before the freeze**
    (`SELFTEST_C1V4=fail` on the first run) — the proposal's reachability review working on a
    real class, not just on a paper table.
- **Proposal 2 (frozen-counter validity rate) was re-measured but NOT adopted.** The
  `ConnectorOverlap` seat extended it over the r94–r95 window
  (`.ufo/waves/round-95/w1/ConnectorOverlap/measurement-r95.tsv`): the r94–r95 rows are counted
  **1 each** under the headline reading (both carry an open claim-level caveat), running
  **12 of 12 = 100 %**; the sibling reading (the r93 caveat applied to r94 too) gives **8 of 12 =
  67 %**. The r95 rows are `pending` and counted 0. **Not adopted as a criterion:** a criterion
  needs its own frozen predicate, and this lane's bar does not admit a criterion from a
  measurement it has not frozen. **Recorded as the baseline.**

### The adoption's honest limits (from the same seat's inventory, `ConnectorOverlap/connector.md`)

The proposal names four skip-work control classes. Measured against this round's committed
receipts: the **no-work base** is PRESENT; the **id-edited copy** is PARTIAL (id-shape and
row-count mutants are receipted in the self-test, but 12 of the 22 deltas have only the
aggregate `pass` line, not per-delta output); the **stub that prints the pass line** and the
**lookup table fitted to the fixtures** are **ABSENT** — no committed receipt shows either is
killed. A fifth class the proposal names in its "today" paragraph — a hand-written entry copy
with a correct digest but non-independent votes — is **ABSENT**, and remains the disclosed
residual of the lane-internal vote (defect 6 of this round's claims). **Adoption is recorded as
adoption of the practice, with its coverage stated; it is not a claim that the control set is
complete.**
