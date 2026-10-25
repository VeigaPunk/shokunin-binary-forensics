# round-67 lesson — revenger

author: L1 revenger-r67 (attempt 1, Kimi fresh L1)
date: 2026-10-24
claims: C1 (coverage, lowest criterion K — the round-66 routed C05 re-gate: one new v2 candidate with exactly the routed text-level repairs, README flipped only on a fresh-seat Q01–Q13 all-pass), C2 (calibration, new criterion C7 — the embedded-output verbatim gate, the M39 fix shape)
claim base: fa0eb3eb33f22f56ebf066dea5440121a30d55a2 · pre-registration: reports/round-67/claims.md at d11f81dfb77ddf67365acfff1e0256207d65bc27 (frozen counter sha256 7933c060…bc07e + red-before in the same revision) · build: 7668510ffc49733daf023e40ff3300ef387ebde5

**Both claims FALSIFIED — honest stop, neither admission re-targeted.** C1: the v2 candidate was rejected by the wave's own named Q02 FAIL (one anchor off-by-one, twice — the M40 class recurring); C2: the frozen attributed-kill target is structurally unreachable (the marker control is shadowed dead code). The fail branches were executed as frozen; no acceptance condition was repaired after seats scored.

## Gate — assimilation posture (item 10, wave-4 quarantine-first)

This lane's first round under the 2026-10-24 assimilation directive adopts **nothing** from
`/home/vgpnk/Projects/shokuknow/merge/revenger/`. The register slice was re-derived at round
start: **26 data rows** (24 `payload-absent` + 2 fetch-failure prose rows S054/S099 — the
register's unchecked family), every line carrying an S-id (evidence
`.ufo/waves/round-67/assimilation/quarantine-slice` and `register-rows.json`). Id-collision
evidence (pre-append): `reg-ids` 44 (S001–S044), `staged-ids` 146 (S045–S190), `collisions` 0 —
then this round's own S045 row took the id the package's staged space starts at, so any later
adoption round renumbers the package **by document**, never arithmetically. The seat
`R67CriticAssim` audited exactly this posture and ruled **SOUND**. One register observation
passed to the campaign owner (not editable by this lane): the register's row for S099/S100 wraps
mid-row (`| \`revenger\` | 24 |` continuation line), and seat `R67QuarS099` found the staged
S099 row's anchors belong to a *different* URL (GitHub API REA commits) than the register row's
URL (developer.android.com apkanalyzer) — an id/URL cross-wiring in the package, named here for
the operator; the register file itself was never edited.

Per-row verdicts (each row hand-checked by a named wave seat; fetched-bytes evidence under
`.ufo/waves/round-67/quarantine/<id>/`):

| row | verdict | one-line reason (seat) |
|---|---|---|
| S053 | ABSENT (fabrication-class confirm) | all 3 quoted strings missing from the jadx v1.5.6 release JSON (200/14981 B) |
| S054 | UNVERIFIED-REACHABLE | prose-class row; fetch 200/0 redirects and all three staged anchors verified verbatim — adoptable-candidate later, nothing adopted now |
| S055 | PRESENT (register wrong) | quote occurs verbatim 3× in the ECMA-335 page bytes (offsets 2336/2802/3785) |
| S058 | ABSENT | all 3 strings missing from rea.tools/ja (200/61099 B) |
| S060 | ABSENT | quoted string missing from fetched HTML in raw/unescaped/tag-stripped/URL-encoded variants |
| S061 | PRESENT (register wrong) | string 1 verbatim at byte offset 875 (og:description) |
| S062 | ABSENT | all 3 missing from arXiv 2412.11539v1 (200) |
| S063 | ABSENT | all 3 missing (200/41461 B, sha pinned) |
| S064 | ABSENT | both missing in every rendering (200/41372 B) |
| S075 | ABSENT | all 3 missing from the fetched analysis.mjs bytes (200) |
| S081 | ABSENT | all 3 missing (200/494 B); near-miss: `source` field points at RFC 6238 appendix B |
| S083 | ABSENT | all 3 re-derived missing from the real 6,521,217-byte ApiDemos-debug.apk |
| S085 | UNREACHABLE | cited URL returns HTTP 404 on all 3 attempts (148687-B error body, sha pinned) — unreachable is not fabrication |
| S087 | ABSENT | genuine ECMA-335 6th-edition PDF fetched (sha pinned); quoted string missing everywhere |
| S089 | ABSENT | both strings fixed-string absent (200/63884 B) |
| S090 | PRESENT (register wrong) | quoted content verbatim in the cited PDF page 14, byte-identical except two pdftotext artifacts |
| S092 | ABSENT | both strings missing from raw and extracted text of the real 27-page PDF (sha pinned) |
| S093 | ABSENT | all 3 missing from the fetched 731467-B PDF; near-misses named for strings 1-2 |
| S094 | ABSENT | both missing from raw and every text rendering (200, real PDF) |
| S095 | ABSENT | both missing; no ILSpy/.NET content in the fetched document at all |
| S098 | ABSENT | all 3 missing from the 69784-B commit-list JSON |
| S099 | UNVERIFIED-REACHABLE | prose-class row; fetch 200/280121 B; the staged S099 row's anchors cite a different URL (GitHub API) than the register row's — package cross-wiring named above |
| S107 | PRESENT (register wrong) | quoted payload resolves verbatim to line 26 of the fetched generate.py once escapes are resolved |
| S108 | ABSENT | quoted line absent in all renderings; whitespace-differing near-miss named |
| S111 | ABSENT | all 3 absent verbatim, though each has a near-miss in the npm metadata (named) |
| S113 | ABSENT | all 3 missing; the fetch returns the jos.org.cn empty article-template page |

Tally: **4 PRESENT (register absence claims wrong) · 19 ABSENT (fabrication-class confirms) ·
1 UNREACHABLE · 2 UNVERIFIED-REACHABLE.** Admit/reject dispositions recorded for the non-author
closure to spot-check: the **rejects are the 19 ABSENT rows** (refuse — a row whose claimed quote
is in none of the checked renderings stays refused until its reason clears, Q12-shaped); the
**admit-candidates are the 4 PRESENT rows plus verified-anchor S054** (a later adoption round may
adopt them with the anchors these seats located — this round adopts none; wave-4 keeps adoption
closed). Sample re-verified by the L1: S055 (offsets quoted above), S054 (anchors in the fetched
bytes this L1 also fetched for S045), S085 (404 error body sha).

## Gate — source rows opened this round

- S045 — DEX format specification (AOSP) — https://source.android.com/docs/core/runtime/dex-format —
  opened 2026-10-24 by this L1 (fetch tool hit a redirect limit; `curl -sL --max-redirs 15`
  succeeded, 281157 bytes; snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256
  `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`). Located quote (≤25 words),
  "File layout" → `header_item` field table, checksum row: "adler32 checksum of the rest of the
  file (everything but magic and this field); used to detect file corruption" (18 words). Seat
  `R67ReviewSourcesS045` ruled the tier/scope/anchor **PASS**; `R67ScoutDexReopen` re-fetched
  independently — **STABLE** (only a per-request CSP nonce + one infrastructure line differ).
  The same fetched bytes are this lane's hand-check evidence for campaign register row S054.
  Status mined; used-by `corpus/knowledge/round-67-apk-axml-byte-evidence.md`.
- Re-opened from committed snapshots (no new fetch), for the v2 candidate's headers: S038
  (ResourceTypes.h — re-read at lines 237-253) and S043 (route-scope lines 7-8); access date
  2026-10-24. No prior row's status/recheck/used-by changed. Census: rows 44 → 45, exit 0 at
  round end; the same four disclosed W04s (S024/S028/S029/S034).

## Gate — admission decisions

- **C1 (C05 disposition): FALSIFIED — fail branch executed.** The wave's named fresh seats on the
  landed v2 bytes: Q01 PASS, **Q02 FAIL**, Q03–Q07 PASS, Q08 PASS (superseded-row check), Q09–Q11
  PASS, Q12/Q13 n/a with named reasons; blind `R67BlindDerive` CONCUR (zero divergences);
  `R67HexContainer`/`R67HexDex` ALL-MATCH/PASS; `R67CriticEntryDeps` NO-SILENT-DEPS;
  `R67RevengerLedger` HOLDS; outside-discernment `R67SpotcheckDiscern` S045-ADMIT-AGREE +
  R65-REJECT-AGREE. The single FAIL is **Q02** — the entry anchors `RES_XML_START_NAMESPACE_TYPE`
  at snapshot **:244** (entry:1 and :56) where the re-hashed pinned snapshot has it at **:245**
  (:244 is `RES_XML_FIRST_CHUNK_TYPE`); corroborated by `R67PointerAudit` FAIL and re-verified by
  this L1 against the committed snapshot (`sed -n '244,245p'`). Per the frozen kill rule
  (claims.md §C1): the README C05 row stays `uncovered` (no flip landed), the candidate is marked
  `admission-status: rejected` and retained (only that line changed from the adjudicated build
  state). Five of the six routed repairs verified good — the hex-pair fix, the S043 route anchor,
  the S045 dex row, the item-8 provenance, and the Q-map/pointer repairs all pass fresh attack;
  the repair set was incomplete by exactly one line number in two places.
- **C2 (C7 gate): FALSIFIED — structural attribution defect.** Every C7 conjunct verifies green
  except the frozen attribution: `C7_GATE_PRESENT=yes`, `C7_SELFTEST=pass`, `C7_CONTROL_PASS=1/1`,
  `C7_MUTANT_KILLED=1/1`, `C7_RED_ON_R65_CANDIDATE=yes` (exit 1 naming `drift entry:41`),
  `C7_V2_CLEAN=yes` — but `C7_MUTANT_KILLED_ATTRIBUTED=0/1`: the frozen mutant is killed (exit 1)
  by the self-test's earlier drifted-case require (`self-test: drifted entry not caught`), so the
  registered marker `drifted entry output accepted` can never be the killing line — the
  forged-control require at `check_embedded_outputs.py:141` is shadowed dead code. Seats:
  `R67MutC7Kill` FAIL (measured 0/1 under the counter's exact logic), `R67CriticC7Claim`
  FALSIFIED (replicated the counter's regex sub), `R67ReviewC7Gate` FAIL, `R67SimplifierGate`
  concurs; `R67MutC7Surface` adds the recorded limitation that pure reorderings/duplications of
  real stdout lines are false-clean under set-membership matching (2 of 3 forgeries). The
  `SKILL.md` Gate-registry row was corrected in the adjudication commit to describe the actual
  behavior (accuracy correction, not a re-target — the frozen predicate stands falsified);
  `HOLDS_OK_V5=no` at the final measurement is the honest signal of this falsification, and no
  prior hold regressed (`HOLDS_OK_V4=yes`).
- Claims-admission: **not admitted** — a round admits only when every claim verifies; both
  falsified claims are reported and stop here. Claims-critic seats: `R67CriticClaimsC1`
  NOT-FALSIFIED (the C1 shape itself was sound — the candidate failed on its bytes, not on the
  order), `R67CriticSeparability` SHARED-ARTIFACT-ACCEPTABLE (disclosed: C2's `C7_V2_CLEAN`
  conjunct reads C1's artifact file; C2's other conjuncts are self-standing).

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M44 | number-drift/anchor (the M40 class recurring in this lane's own repair work) | `corpus/knowledge/round-67-apk-axml-byte-evidence.md`:1 and :56 anchor `RES_XML_START_NAMESPACE_TYPE` at snapshot :244; the pinned snapshot (sha-verified by the seat) has it at :245 — caught by wave seat `R67ReviewEntryQ02` FAIL + `R67PointerAudit` FAIL, re-verified by this L1 (`sed -n '244,245p' .ufo/waves/round-65/source-snapshots/ResourceTypes.h`) | Q02 (the same criterion that killed the round-65 draft) + the pointer-audit seat; the author-side capture that should have prevented it: the build script hardcoded anchor text from intent instead of deriving each enum-symbol line programmatically from the snapshot | candidate rejected + retained; the repair is one line number in two places — routed to the next coverage round **with the fix shape: the entry builder must `grep -n` each symbol in the pinned snapshot and splice the actual line numbers** (a builder-derived anchor cannot drift) |
| M45 | landing (registered instrument carried a false attribution claim) | `corpus/check_embedded_outputs.py:141` forged-control `require(not ok(dproblems), MARKER)` unreachable behind the drifted-case require at :131-134 — `R67MutC7Kill` measured the frozen mutant exit 1 with last line `self-test: drifted entry not caught`; `R67CriticC7Claim` replicated the counter regex (`C7_MUTANT_KILLED_ATTRIBUTED=0/1`); `R67ReviewC7Gate` FAIL; `R67SimplifierGate` concurs | the C-pattern itself (C2–C6: a kill counts only with its registered endswith marker) — the counter's attribution check caught it exactly as designed, at wave time rather than at claim time | the gate stays (its drift detection and red-before are real and verified); the `SKILL.md` registry row corrected in the adjudication commit (accuracy); the reorder fix (make the drifted-case require carry the marker, or move the forged control ahead of it) is routed to the next calibration round and must re-pass the frozen-mutant attribution before any C7-resumption claim |

Round-shape note (recorded, not a numbered mistake): wave dispatch attempt 1 spawned all 64
seats and aborted every one at +51 s — the headless dispatcher session exited after the task call
returned and the runtime disposed its child jobs (`stopReason: aborted` / `session_exit: dispose`
in all 64 seat transcripts, zero reports, zero seat work). Attempt 2 re-dispatched the SAME
validated taskCall (no split, no seat replacement — no seat had started work) with a dispatcher
that holds the session open and polls until settlement: 64/64 reports in ~7.4 min, zero
job-level errors. Both attempts are committed as wave evidence (`dispatch-run.log`,
`dispatch-run-2.log`, `dispatch-start-attempt1.txt`, per-seat transcripts under the runtime
session dir).

## Routed forward (dispositions)

1. C05 re-gate, third pass (owner: next coverage round): fix entry:1/:56 (`:244` → `:245`) via a builder that derives symbol lines from the snapshot; every other Q decision already passed fresh this round — the candidate is one anchor away from a re-gate.
2. C7 attribution reorder (owner: next calibration round): make the forged-control marker the kill; re-run the frozen mutant attribution before claiming.
3. C7 set-membership surface (R67MutC7Surface): reorder/duplicate false-cleans — sequence-sensitive diff is the fix shape.
4. Sentinel findings (R67SentinelScope): seat containment is textual-only; the C7 gate runs entry-declared commands (python3-only, cwd lane-root) — an unsandboxed-exec surface to fence (named limitation; a command allowlist or path pin is the fix shape).
5. Carrier items unchanged: AST-bound mutation counter + label-spoof surface; generator conditional-symlink note; evidence-ID prongs (a)/(b)/(d) + injectivity registry; endswith-attribution asymmetry (now demonstrated concretely by M45); recheck-pin H1–H3; SHONEN box 1 `[x]` non-lane re-confirmation (`R67ReviewSkillRefresh` re-stated `[x]`-ready YES on the current bytes — lane-dispatched evidence only, the flip stays a non-lane duty); r58/59 PASS-count quotes; verbatim-output-diff gate now EXISTS as the C7 probe (its attribution defect is item 2).
6. Assimilation (item 10): adoption stays closed (wave-4). The 4 PRESENT rows + S054 are adoptable-candidates with located anchors; the S099/S100 package cross-wiring and the register's wrapped S099/S100 row are named for the operator/campaign owner.
7. Connector (R67ConnectorOverlap): CONTEST-NAMED — kaidoku holds provider decompile/signing/inventory ground for shipped Godot templates (PROVINCE.md:56, :242); revenger's C05 ground is a manual declared-header readout of one authored fixture; reported-not-absorbed, integrator to arbitrate (ADJ-06 unchanged).

## Round shape and receipts

ONE v2 wave (policy v2, band 64–128), exactly **64 seats**, validated (`ufo-swarm-wave.mjs plan`
exit 0, spawn 64, dispatch.calls 1) and dispatched **in-seat** as ONE batched OMP task call
carrying the validator's taskCall unchanged (attempt 1 aborted by the dispatcher exit, see above;
attempt 2 settled: `{"reports": 64, "settled": true, "jobs_with_errors": {}, "elapsed_min": 7.4}`).
Slot: `wave-slot.sh acquire` → `granted lane=revenger wave=r67-wave seats=64 live=28 cap=256`
(MemAvailable 15143 MB ≥ floor 6144); released after settlement. Roles (spec + registry):
scribe 19, reviewer 13, scout 11, critic 10, executor 5, mutation-tester 2, connector 1,
sentinel 1, simplifier 1, revenger 1 — **attack roles 25/64 = 39%** (reviewer+critic+mutation-tester).
§3 planner seat held by the L1 (mapping recorded per the orchestrator ruling; no planner role in
the validator payload). Dead seats: attempt 1 — 64 (all aborted, error `Request was aborted`,
no work done); attempt 2 — 0. Round total: 64 seats × 2 attempts = 128 spawned, 64 reported,
0 replacement seats. Residual call: none. Tool installs: none. No confirmed misroot (sentinel
sweep + L1 fleet-root sweep at round end).
