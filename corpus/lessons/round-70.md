# round 70 — revenger (hyaku run 7, fresh-start round)

Round 70 declared three claims on three axes (`reports/round-70/claims.md`, frozen at
`dbacce212d798d1ec5bb59e03ff91d577eed0283` against base `3f5edbc206351232a3d2d801334dd930499ccaf5`, counter
`reports/round-70/measure.py` sha256 `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`, tighten-only
amendment A1 `reports/round-70/claims-amendment-A1.md` with `measure-a1.py` sha256
`96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191`, declared before any wave-2 seat scored):

- **C1 — coverage (K, lowest criterion): C05 fifth pass → FALSIFIED — honest stop.** Wave-2 decisions on the landed v5.1 candidate
  (lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`): FAIL Q04 (`R70W2GateQ04`), FAIL Q11b (`R70W2GateQ11b`), FAIL Q13
  (`R70W2GateQ13`); PASS/n-a Q01, Q02, Q03, Q05, Q06, Q07, Q08, Q09, Q10, Q11a, Q12, Q14, Q15. Kill rule executed: README C05
  stays `uncovered`, `K_HELD_BACKED` 8/14 → 8/14, the entry header reads `admission-status: rejected` with every other byte kept
  (diff shows only line 11).
- **C2 — calibration: `SELF_MISMATCH` 9 → 0 with a checker shown able to fail → verified as declared** (`HOLDS_C2_V5=yes`,
  `A1_C2=yes`, `SELF_MUTANTS_KILLED=6/6`), with named limits below (the six classes are bounded detectors; SM3/SM4 read 0 because
  the overstating text was removed, not re-confirmed).
- **C3 — freshness: `EMB_R68` problems 7 → 0 via a digest-pinned historical script → verified as declared** (`HOLDS_C3_V1=yes`,
  `A1_C3=yes`, r65 still 1, entry bytes unchanged, tamper killed with the attributed text).
- Round is **not admitted** (C1 falsified); no axis is harmed (`HOLDS_OK_V7=yes`, `A1_*=yes`).

## Gate

### Source rows opened this round (CORPUS.md rule 1: URL or command, access date, located quote)

Every row the C1 entry cites was re-opened by this L1 or by a non-author scout this round; rows S048 and S049 are new.
Access date for all: **2026-10-25**.

- **S048 (new; supersedes S045's locator).** https://source.android.com/docs/core/runtime/dex-format, re-fetched by this L1
  at 21:28Z (281161 bytes, sha256 `d72efc551a4d69be6d29a3aebb4ea9fca67935832893ca2779c8e67a6e468598`; `diff` against the
  committed `corpus/snapshots/dex-format.html` shows two differing lines, a per-request CSP nonce and one devsite loader
  line, both outside every quoted phrase — also `R70W1OpenS045`). Located quote (live line 5949, table row `checksum` under
  "Items and related structures" → `header_item`): `adler32 checksum of the rest of the file (everything but magic and this field)`.
  Why a new row: S045 names "File layout" → `header_item` field table; the table is under "Items and related structures" and
  `ENDIAN_CONSTANT` (live line 5035) under "Bitfield, string, and constant definitions" (`R70W1OpenS045` D2, re-derived here).
- **S049 (new; supersedes S043's repo path).** https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md,
  re-fetched by this L1 at 21:28Z (1992 bytes, sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`,
  byte-identical to the committed snapshot). Located quote (lines 7-8): `Start with inspect_android_package on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.`
  Why a new row: S043's `source` cell names `skills/reverse-engineer-anything/references/android-applications.md`, which returns
  HTTP 404 at the tag; the file lives under `.agents/skills/` (`R70W1OpenS043` F1, byte-identical re-fetch by that seat).
- **S038 (re-opened).** `https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h`,
  live bytes byte-identical to `corpus/snapshots/ResourceTypes.h` (`R70W1OpenS038`, and the wave-2 re-open `R70W2QuoteS038`).
  Located quote (snapshot line 686): `Byte offset from the start of this structure where the attributes start`.
- **S032/S034 (re-opened).** https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT, fetched by this L1 and by
  `R70W1OpenS032` (174585 bytes, sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, byte-identical to
  `corpus/snapshots/APPNOTE.TXT`). Headings/fields located in the snapshot by `entry_checks.py --zip-layout`: §4.3.7 heading 387,
  fields 389-399; §4.3.12 heading 511, fields 522-538; §4.3.16 heading 632, fields 634-646. Located quote (line 399): `extra field length              2 bytes`.
- **S041, S047 (own-work, re-run).** Digests printed by `entry_checks.py --pins`; S047's 20-line output is item 11 of the entry.

Registry changes (append-only fields, logged old → new):

| row | field | old | new | reason |
|---|---|---|---|---|
| S048 | (new row) | — | `mined`, opened `2026-10-25`, `180d`, used-by the round-70 entry | supersedes S045 under rule 2 |
| S049 | (new row) | — | `mined`, opened `2026-10-25`, `on-release`, used-by the round-70 entry | supersedes S043 under rule 2 |
| S032 | used-by | `…round-63-zip-central-directory-evidence.md, corpus/lessons/round-63.md` | same + `corpus/knowledge/round-70-apk-axml-byte-evidence.md` | the entry cites it |
| S034 | used-by | `…round-63-zip-central-directory-evidence.md` | same + the round-70 entry | the entry cites it |
| S038 | used-by | `…round-65-apk-axml-byte-evidence.md` | same + the round-70 entry | the entry cites it |
| S041 | used-by | `…round-65-apk-axml-byte-evidence.md` | same + the round-70 entry | the entry cites it |
| S047 | used-by | `…round-69-apk-axml-byte-evidence.md` | same + the round-70 entry | the entry cites it |
| S043, S045 | (unchanged) | `queued`/`—` and `mined`/r67 entry | unchanged | superseded, not rejected; the round-70 entry cites S049/S048 |

`R70W1OpenS043` F2 also found S043 `queued` with `used-by` `—` although round-67/68/69 entries cite it; that is recorded here
and not repaired (append-only: only `status`/`recheck`/`used-by` change in place, and S043 is superseded by S049, which
carries the consumer).

Census before → after (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`; outputs committed as
`.ufo/waves/round-70/census-before.txt` and `census-after.txt`):

```
before: rows 47, four W04 (S024, S028, S029, S034), "revenger ok", CENSUS_EXIT=0
after:  rows 49 (+S048, +S049), five W04 (the four plus S048 vs S045 duplicate url, by design: a superseding row), "revenger ok", CENSUS_EXIT=0
```

### Admission decisions (QUALITY.md criteria Q01-Q15)

Decisions on `corpus/knowledge/round-70-apk-axml-byte-evidence.md` (landed v5.1, 24 embedded blocks, gate `checked_blocks=24 problems=0`,
lint 0/0/0/0 before Q16 was added): Q01 PASS (`R70W2GateQ01`), Q02 PASS, Q03 PASS (oracle AXML half labeled as the generator's declaration),
Q04 **FAIL**, Q05 PASS, Q06 PASS, Q07 PASS, Q08 n/a-PASS (superseded by Q11), Q09 PASS, Q10 PASS, Q11a PASS, Q11b **FAIL**,
Q12 n/a, Q13 **FAIL**, Q14 PASS, Q15 PASS (no git id stated).
- **Q04 FAIL** — entry `:119` says the `--spec-quotes` command "prints the raw line the phrase's first words start on"; it prints that
  line's number plus the searched phrase (`entry_checks.py:292`); `:152` says "the last three lines" of `--zip-layout` print the record
  positions; they are output lines 16-18 of 20.
- **Q11b FAIL** / **Q13 FAIL** — entry `:282` says the cited `readout.py:N` literals "are compared in items 12 and 17"; the UTF-8/sorted
  masks (`readout.py:166`), dex header reads (`:233-248`), `strings[ans]` (`:211`), `NO_INDEX` (`:22`) and the EOCD literal are compared
  nowhere, and falsifying a quote of three of them passes gate and lint (`checked_blocks=24 problems=0`); the Q13 row (`:310`) omits that clause.
- The kill rule was applied unchanged: each FAIL carries a located defect and the L1 did not claim any is absent. New criterion **Q16**
  (QUALITY.md) records the class (M53). The sixth pass is a four-sentence repair (`:119`, `:152`, `:282`, `:310`) plus the named residuals.
- Counter state at the final tip: `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`, `HOLDS_C1_V5=no` (also `C1_LINT` now reads `LINT_QMAP=1 ['Q16']`,
  because the rejected entry predates Q16 — recorded, not repaired).
- Separability: `R70W2SepC3` SEPARABLE; `R70W2SepC1` SEPARABLE only when C1's change set also appends one SCORECARD `K_HELD_BACKED 9/14` line (the frozen
  §Separability omits it); `R70W2SepC2`/`SepCritic` ENTANGLED in the admitted-C1 world (C1's flip alone moves SM6 0→1). C1 was not admitted, so no merged tip carries it.

## Item-10 assimilation (addendum section 10)

Theme: fixity and provenance / firmware-extractor upstream facts (package `merge/revenger/`, entry `digest-scope-versus-provenance-amendment-2026-10-23.md`
and `swgde-custody-authority-and-normative-scope.md`). **Adoption: none appended** — no entry cleared the per-entry gates; zero package rows or entries copied.
- Id guard (scratch committed under `.ufo/waves/round-70/assimilation/`): registry ids 47, staged ids 155, collisions at round start **1** (`S047`); live
  registry now collides 3 (S047/S048/S049); the guard was proven on an indented scratch row (`  | S050 |` → collisions 1; the column-zero-only pattern
  printed 0). Renumber map by document if the Unblob rows are adopted later: the staged Unblob rows S054/S099/S152 need none; colliding staged rows
  S047→S202, S048→S203, S049→S204 (`R70W2Quarantine`).
- Quarantine slice re-derived: 26 data rows. S099 and S054 hand-checked: **UNVERIFIED-REACHABLE** (the register recorded no quote; both sources fetch today), staged Unblob rows PRESENT
  verbatim (S054 release API 3/3; S099 README headers, feature line and install line).
- **REJECT** — the re-grounded Unblob draft (`.ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md`): `R70W2AssimGateA` REJECT (Q02 stale item cross-references, Q11 three
  values without derivation, one false registry sentence) and `R70W2AssimGateB` REJECT (Q01/Q02/Q11/Q13; its freshness sentence credits a gate that refuses `python3 -c`).
  Flip: fix the cross-references, derive the three values, ship an offline snapshot + gate-compatible commands, drop "authoritative".
- **REJECT** — package entry `swgde-custody-authority-and-normative-scope.md` as staged: wave-1 `R70W1AssimSwgde` REJECT-ADJACENT as written (its claim 2 rests on a premise the lane's bytes contradict).
- **ADMIT (scope only, no entry written)** — the narrowed SWGDE digest-scope claims bear on shipped-artifact evidence ledgers (`R70W2AssimScope` ADMIT; `R70W1AssimSwgde`
  in-scope for §13/§14 of 18-F-002 and §3/§4 of 18-F-003); flip to an entry: a draft that clears Q01-Q16. The two scope seats disagree on the staged text and agree on the narrowed claim.
- Wave-4 quarantine-first rule: the lane's earlier rounds satisfied it (r67, r69); this round adopted nothing, so `K` and the README map are untouched by assimilation.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M51 | reference-drift / attribution (a self-assessment record cites a hash that does not resolve and a command that does not run from the printed cwd) | `SCORECARD.md:557` cites pre-registration `e1d22caf`, which `git cat-file -e e1d22caf^{commit}` rejects (the commit is `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`); the round-69 C1 table printed `python3 -B reports/round-69/measure.py TREE`, which fails from the fleet root (`.ufo/waves/round-70/w1/R70W1MistakeSweep.md` §2-§3, `R70W1ErratumDraft.md` §2); both recorded by the round-69 spot-check as V2/V4 | **Q15** names the rule (a stated git id is re-derived) but is scoped to knowledge entries, so it never read SCORECARD or reports | `corpus/self_assessment_check.py` SM5 (the Q15 rule extended to SCORECARD citations) with an appended resolving erratum; shown able to fail: the checker's own self-test plants an unresolvable hash (SM5=1) and the counter's independent fixtures plant one per run (`SELF_MUTANTS_KILLED=6/6`, `A1_C2` randomised variants), and an unrelated resolving correction is not excused. The command half (V4) is named `named-unmeasured`: no tool checks a printed counting command |
| M52 | vacuous predicate / control (a frozen mechanical predicate reachable by a move that skips the claimed work) | `.ufo/waves/round-70/w1/R70W1ControlAudit.md` controls I, J, K: a 17-echo entry with `source: none` read `HOLDS_C1_V5=yes`; a 27-line checker keyed to the counter's own fixture literals over unrepaired bytes read `HOLDS_C2_V5=yes`; a pin pointing at an echo stub bypassed `EMB_PINNED_SCRIPT_IS_S046` | **none** before the wave: the pre-registration's control set (A-H, `reports/round-70/controls/`) tested the cheapest moves its author thought of, and §9's rule asks for the cheapest control, not the author's cheapest | amendment A1 (`reports/round-70/claims-amendment-A1.md`, `measure-a1.py`): distinct-command, readout-line, source-row, base-vector, randomised-variant and pin-binding conjuncts; shown able to fail: `controls/I-echo-entry-flip.log`, `J-fixture-shaped-checker.log`, `K-pin-to-echo-stub.log` read the frozen label `yes` (I, J) and the A1 label `no`, and the same conjuncts read `yes` on the real tree |
| M53 | prose-claim drift (hand-written claims about derived values) | the first v5 candidate (`aa1842f`) carried 11 prose defects found by wave-1 seats on bytes whose 22 embedded blocks all re-derived byte-for-byte: two wrong APPNOTE line ranges, a "five" flag list of six, an unprinted version tag, an unprinted `method 0`, "field by field" over 9 uncompared oracle fields, "every file" omitting the checker (`R70W1Citations`, `R70W1PreQ11Items1to8`, `R70W1Prose`) — the same class as r65-r69 (M39, M40/M44, M47, M49) | Q11 and Q14 (judgement-bound); `lint_entry.py` QMAP/Q14/Q15/HEADER saw none of them | the entry is generated from running commands (`build-entry.py`), the ranges and flag counts are printed by commands (`entry_checks.py --zip-layout`, `--container`, `--axml-layout`), and the gate/lint were hardened; shown able to fail: every entry_checks subcommand has a mutation that makes it print `MISMATCH` (`R70W1EntryChecksMut`, `R70W2EntryMutants`) |

Sweep that found M51's class once (`R70W1MistakeSweep`): `grep -n 'Pre-registration `' SCORECARD.md | …` followed by
`git cat-file -e <h>^{commit}` over every backticked 7-40 hex token in the Round 61+ sections — one instance (`e1d22caf`).

## considerthese (addendum section 10)

Latest file `considerthese/2026-10-25.md` (operator-authored; mined, never edited). Proposal 4 (Q-map completeness check) is
implemented as `corpus/lint_entry.py` QMAP — shown able to flag the round-69 entry's 7 missing rows
(`python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md` prints `LINT_QMAP=7`).
Proposal 2 (a change of approach: generate the entry's numbered items straight from readout stdout) is how the v5 entry is
built (`.ufo/waves/round-70/build-entry.py`). Proposal 1 (routed-repair carry-through) is wave-2 seat `R70W2ConnRoutedCarry`.
Proposals 3, 5 are not acted on. `considerthese/2026-10-24.md` proposal 3 (claim hit-rate ledger) lands below.

## Claim hit-rate ledger, lane rounds 61-69 (considerthese 2026-10-24 proposal 3)

Two independent derivations disagree on 2 of 18 rows, and the disagreement is the finding: the verdict depends on whether a claim is read by its round-end
SCORECARD cell or by its own frozen predicate. Wave-1 `R70W1ErratumDraft` §3: met=10, falsified=2, honest-stop=5, pending=1. Wave-2 `R70W2LedgerRederive`: met=11,
falsified=7 (5 honest-stop), pending=0 (r65 C1: pending vs falsified after the r66 adjudication; r66 C1: "order executed" met vs coverage candidate falsified). Both agree on rounds
67-69: one claim met of six (r68 C1), which `considerthese/2026-10-25.md` also states. A 100 % hit rate would be a calibration smell; the lane's is 11/18 by the stricter reading
of its own table, with every falsification executed as frozen. This ledger is `recorded` (two seat derivations, commands in their reports), not re-derived by the L1.

## Routed forward (not claims)

1. **C05 sixth pass (owner: next coverage round):** repair `:119`, `:152`, `:282`, `:310` of the v5.1 entry against the printed outputs (the four sentences, no value changes; the 24 blocks re-derive), add a Q16 row and the Q16-aware Q-map, name the unguarded literals (`readout.py:22,76,166,211,233-248`), and add an `--axml-layout`-style comparison for them if credit is wanted; append one SCORECARD `K_HELD_BACKED 9/14` line in the same revision as the README flip.
2. **Checker (C2) residuals:** every class SM1-SM6 has a still-open miss and (except SM2) a false positive (`R70W2CheckerClasses`); an env-override hybrid checker survives both counters (`R70W2CheckerMut`); SM3/SM4 read 0 vacuously on the landed tree. Not closed: an env-canary control and class tightenings.
3. **Gate residuals (base-identical):** a missing entry path exits 1 not 2, a command timeout exits 1 with a traceback (`R70W2GateReplay` F1/F2); one-directional comparison (deleting an embedded line, a superset-printing flag typo) stays unguarded and is named in the entry's Q13 row.
4. **Named-unmeasured self-assessment mismatches** (`R70W1SM5Sweep`): SCORECARD quoted file digests (F6) never re-derived; README `lessons/` enumeration fixed generically (F5); SHONEN box 4 README-parenthetical falsehood and the round-63 phantom seat name were corrected here by append/edit (F1, F2). PROVINCE.md pins `rea-agents@6.4.0` while records used 6.5.0 (`R70W2ShonenReview` F3).
5. **Fixture:** the dex `header_size` has no machine-checked expected value (`R70W2OraclePerturb` F1); attribute `ns_index` points at the prefix string, not the URI (`R70W1IndependentRead`) — stated in the entry's Limitations.
6. **Open L0s unchanged** (round-68 C7 behavioural legs; round-69 instrument-repair ruling). Round 70 built a new instrument instead of repairing the frozen one.
7. SHONEN box 1 stays `[~]`: a non-lane reviewer re-confirming the current SKILL.md bytes is operator-routed.

## Wave record

Shape: **two v1 waves, 85 seats** (policy band 32-64 each), dispatched through the inline handoff (`w1.ready`, `w2.ready`); no residual call; the L1 held the §3 planner seat
(data walk by connector `R70W1ConnLedger`). **Wave 1 (build / pre-gate), 40 seats, 0 dead:** reviewer 3 · critic 9 · executor 5 · mutation-tester 5 · scribe 4 · scout 8 · connector 3 ·
simplifier 1 · sentinel 1 · revenger 1; m_flash roles 21/40 = 52.5 %. **Wave 2 (falsify), 45 seats:** reviewer 11 · critic 13 · executor 10 · mutation-tester 3 · scout 4 · revenger 1 ·
sentinel 1 · connector 2; m_flash roles 25/45 = 55.6 %; attack share (reviewer/critic/mutation-tester/sentinel/revenger) 29/45 = 64 %. All 45 wave-2 seats returned (0 dead); `R70W2EntryMutants` reported UNNAMED-SURVIVORS: a forged block whose command is a different in-tree script that echoes fabricated lines passes the gate (`checked_blocks=25 problems=0`) — a further Q13 clause for the sixth pass to name. Wave-1 findings drove the v5.1 repairs, the checker/gate/lint hardening and amendment A1 before any wave-2 seat
scored. Tool installs by this L1: none (seat `R70W1IndependentRead` installed `androguard` 4.1.4 via `uv tool` and used `apktool` 3.0.3, already present). Misroot sweep: see the report.
