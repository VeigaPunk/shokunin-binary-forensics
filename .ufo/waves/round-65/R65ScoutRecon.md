CLEAN — state map complete: rounds 62–64 landings, round-65 claims, and routed-debt dispositions traced to file:line.

# Round-state map for the round-65 v2 wave (64 seats, build-and-attack)

Seat: R65ScoutRecon (scout, read-only). All paths relative to `/home/vgpnk/Projects/shokunin/revenger-shokunin/` unless absolute. Sources: `LOG.md:786-903`, `SCORECARD.md:187-454`, `reports/round-65/claims.md` (full), `reports/round-65/measure-before.log`, `corpus/lessons/round-64.md:178-281`.

## 1. What rounds 62–64 landed

| round | wave shape | coverage K | calibration | other landings | pointers |
|---|---|---|---|---|---|
| 62 | 64 build + 64 fresh-attack, two correction rounds, 128/200 seats | **4/14 → 6/14**: C04 `round-62-commonjs-require-name-evidence.md` + C09 `round-62-evm-dispatch-byte-evidence.md` admitted only after named fresh-seat exact-hash re-reviews; README flipped at admission revision `0651c7c6` | C2 receipt-command guard held 2/2 (not re-claimed) | sources 27→31; M27/M28 mined (missing derivation, byte/hex units); K probe reaffirmed as existence-only, not the gate (M34) | `SCORECARD.md:261-296`; `LOG.md:819-857`; `reports/round-62/measure-after.log` |
| 63 | 32 build + 32 falsify, zero dead | **6/14 → 7/14**: C06 `round-63-zip-central-directory-evidence.md` (partial→held) | **C3 0/2 → 2/2**: forged-receipt controls in `verify_named_multi_icon_states.py` + `verify_icon_states.py` (`r55:`/`r36: forged receipt accepted`) | **F 4/8 → 5/8**: authored fixture `corpus/fixtures/firmware-r63/` + real `inspect-firmware-regions` run, Evidence `ev_aae7529f…`, `ORACLE OK`; sources 31→35; M33–M35 mined | `SCORECARD.md:303-351`; `LOG.md:859-873` |
| 64 | ONE v2 wave of exactly 64 seats, one task call; one dead seat (R64CriticC4, provider flag) | **7/14 → 8/14**: C07 `round-64-firmware-region-byte-evidence.md` (sha256 `9bf21e50…e0ebf`) admitted after Q09/Q11 FAIL → author corrections → all-criteria pass; README C07 frontier→held same revision as Gate | **C4 0/2 → 2/2**: forged-stdout controls in `verify_icon_languages.py` + `verify_multi_icon_states.py` (6 insertions/0 deletions; `forged receipt stdout accepted`) | M36 legend mismatch repaired (`README_TOKEN_LEGEND_MISMATCH` 1→0); `HOLDS_OK_V2` no→yes; SKILL.md landed (SHONEN box 1 `[x]` by lane seat — see carried debt); sources 35→37 | `SCORECARD.md:367-422`; `LOG.md:875-888`; `corpus/lessons/round-64.md:216-281` |

Calibration chain to date (receipt-identity conjunct family, one new guard per round): **C2** command (r61) → **C3** forged receipt on the other two scripts (r63) → **C4** `stdout_sha256` (r64) → **C5** `evidence_id` (r65, this round). The `exit_code`/`fixture_sha256` conjuncts still lack in-script forged controls — `SCORECARD.md:452` names them as next-round candidates.

## 2. What round 65 claims (frozen: `reports/round-65/claims.md`, base `3eebcdd7`, counter `reports/round-65/measure.py`)

- **C1 — coverage K, 8/14 → 9/14** (`claims.md:19-30`): exactly one independently gated admitted entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md` over authored fixture `corpus/fixtures/apk-r65/` (binary-AXML manifest + declared-header dex + jar manifest; 947 B sha256 `05d2280f…`), covering README row **C05 (Android packages)**. 8/14 falsifies. README C05 flips **either way** at round end: `frontier → held` naming only the new entry on all-criteria Q01–Q13 admission by named fresh non-author seats; `frontier → uncovered` on falsification. Entry scope is manual byte readout only — Q10 fence, no install/signing/dex-validity/authenticity claim.
- **C2 — calibration, new criterion C5, 0/2 → 2/2** (`claims.md:32-52`): one in-script forged-evidence control per script in `verify_icon_languages.py` (transplants multi's real round-42 id `ev_6e055332…2dc3d`) and `verify_multi_icon_states.py` (transplants languages' real round-47 id `ev_8ed88983…e8d4421`), both ids real in `corpus/live/runs/`. Frozen kill rule: delete the `receipt['evidence_id']==evidence_id` conjunct (one regex match per script); attributed iff mutant exit non-zero **and** last output line ends `forged receipt evidence accepted`. Insertions only; `receipt_ok` untouched. Anti-spoof: `C5_CONTROL_PRESENT` greps landed script bytes for the attribution string (`claims.md:87-90`).
- **Registered counter repair (not scored)** (`claims.md:54-65`): STRICT rejected-marker scan widened from `[:2000]` to whole file + additive `STRICT_REJECT_WINDOW_SELFTEST`; `HOLDS_OK_V2` formula frozen; `HOLDS_OK_V3` = V2 ∧ C5==2 ∧ selftest=pass. Must not move current counts (both retained rejected markers sit < byte 2000).
- **Admission order** (`claims.md:111-123`): candidates land without flip → this wave's named fresh-seat Q decisions + C5 attribution + separability/counter-spoof attacks → L1 adjudicates and flips → final measure on committed archive needs `HOLDS_OK_V3=yes`, exit 0.
- **Separability** (`claims.md:107-108`): C1 touches corpus knowledge/SOURCES/README only; C2 touches the two verifier scripts only; probe lines independent.

## 3. Routed debt — what round 65 pays vs carries

**Addressed this round:**
- **STRICT scan window (routed by R64ReviewSeparability)** — r64's `rejected_marked` scanned only the first 2000 bytes; the admitted C07 entry's marker sits at byte 4155 (`SCORECARD.md:416-419`). R65 registers the whole-file scan + self-test as M37 (pre-registered, `claims.md:55-62`); red-before already prints `STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True` (`measure-before.log:6`).
- **Evidence-ID transplant corollary, prong (c)** — round-63 debt owned to "a future calibration round": (a) recompute record/stdout/receipt digests, (b) bind `receipt.evidence_id == record.evidence_id == LEDGER` line, (c) in-script control transplanting a real foreign ID with recomputed digests (`corpus/lessons/round-64.md:200`). C5 seeds **prong (c) only** (`claims.md:50-52`); the r63 transplant passed the byte oracle, so digests alone cannot catch it — the cross-bind prongs are the load-bearing remainder.

**Carried forward (explicitly dispositioned, not claimed):**
- Evidence-ID prongs **(a),(b) + injectivity registry** → future round, owner named in `corpus/lessons/round-65.md` (`claims.md:51-52`, `SCORECARD.md:454`).
- **AST-bound mutation counter** → future-counter debt (r64 critics reproduced decoy trees meeting numeric targets; the Q-gate is the defense) (`claims.md:141-143`, `SCORECARD.md:454`).
- **Recheck-pin scope holes H1–H3** (recheck doesn't read entry prose; compression.level not byte-derivable; Evidence ID not echoed) (`claims.md:144`, `SCORECARD.md:454`).
- **SHONEN box 1** → reported `[~]` this round: the r64 verifier is a lane seat; only a fresh non-lane reviewer may write `[x]` (`claims.md:138-141`, `SCORECARD.md:454`).
- **r58/59 139→142 PASS-count quotes** → not triggered (r65 doesn't touch the two named/icon-states verifiers); owner rule restated in the lesson (`claims.md:145-147`).
- **`## Frontier` C05 prose refresh** → must land with the row flip in the same revision (`SCORECARD.md:454`).
- `FRESH_ROWS` remains the frozen byte-survival hold (`claims.md:148`).

## 4. Build state this wave attacks (per L1, `LOG.md:894-903`, `SCORECARD.md:429-452`)

Committed at `c7b7cf98ddeecbd5464e47396f224e6384b78905`: fixture `corpus/fixtures/apk-r65/` (regen byte-identical, Python 3.14.8); candidate entry (admission-status: candidate; 15 readout facts, stdout sha256 `507d79f8…`); SOURCES S038–S041 (S038 AOSP `ResourceTypes.h` @ android-15.0.0_r1 mined; S039 REA android guide @ rea-agents-6.5.0 mined; S040 CPython zipfile docs queued — resolves the r63 lead; S041 own-work bundle); C5 controls 3 insertions/0 deletions each; lesson with M38 mined (layout-from-intent, red-before `.ufo/waves/round-65/m38-red-before.log`) and M37 pre-registered. README C05 **not flipped**; SCORECARD records C2 as verified at the candidate commit but C1 as **pending** — the flip and K move require this wave's fresh-seat decisions.

Red-before receipt (`measure-before.log` over base `3eebcdd7`): `K_HELD=8/14`, `K_ROW C05 status=frontier`, `C5_CONTROL_PRESENT=0/2`, both c5 mutants `exit=0 pass` (lines 38/41), `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK_V3=no`, holds all green, probe exit 0. L1 dry-run of the flip on scratch: `K_HELD=K_HELD_BACKED=STRICT=9/14` (6.4), `MISMATCH=0`, `HOLDS_OK_V3=yes` (`LOG.md:896` — L1 claim, not an admission).

## 5. Orientation notes for the wave

- The K probe counts existence/status only; admission is the named-seat Q01–Q13 gate (r61 M34 lesson; `lessons/round-64.md:160-164`). A printed `K_HELD=9/14` without the Q-gate is not evidence for C1.
- Fresh seats must be non-author/non-corrector of the C05 entry and correctors of the C5 patches (`claims.md:115-118`; r62 discipline `LOG.md:832`).
- C5 attribution is endswith-strict: a mutant crashing with any other final line is killed but **not attributed** (`claims.md:46-49`); r64's attribution-integrity precedent (R64MutProbe rejected loose messages, `lessons/round-64.md:218-220`) applies.
- Either C05 flip lands at round end — `held` only names the new entry; `uncovered` on falsification; no third status, no other row changes (`claims.md:26-27`, `claims.md:118-121`).

Remaining unknowns: none blocking — the C5 patch bytes, entry bytes, and wave spec are committed for the attack seats to verify on their own; this seat verified contract/ledger state only.

Tooling: none installed or upgraded (read-only recon; existing `read`/`bash` utilities only). No git/jj mutations; nothing written outside this report.
