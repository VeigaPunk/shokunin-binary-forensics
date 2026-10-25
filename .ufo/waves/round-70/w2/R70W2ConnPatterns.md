PATTERNS-UNCOVERED: Asymmetric gate comparison, multi-run Q14 clauses, non-standard Q15 introducers, and prose-to-spec line drift slip mechanical detection.

# R70W2ConnPatterns — Cross-Claim & Cross-Round Pattern Scan (Wave 2 Falsify)

Seat: `R70W2ConnPatterns` · Role: connector · Date: 2026-10-25
Landed target commit: `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`
Base commit: `3f5edbc206351232a3d2d801334dd930499ccaf5`
Pre-registration: `dbacce212d798d1ec5bb59e03ff91d577eed0283`
Repository: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (read-only execution)

---

## 1. Executive Summary & Verdict

Verdict: **PATTERNS-UNCOVERED**

While the round-70 treatment changes and Amendment A1 have mechanized defenses against seven historical failure modes (header omission, §Q-map drops, embedded verbatim stdout drift, retained-candidate historical script drift, canonical self-assessment mismatches SM1–SM6, and do-nothing echo/mock counter bypasses), **four structural defect classes remain unmechanized or caught not at all**:
1. **Asymmetric verbatim check (Embedded line deletion immunity & flag degradation fallback)**: `corpus/check_embedded_outputs.py:140` verifies `embedded ⊆ stdout`. Silent deletion of embedded output lines or flag typos falling back to full dumps exit 0 with `problems=0`. Caught **NOT AT ALL** mechanically.
2. **Multi-hex-run / ASCII decode blind spots in Q14**: `corpus/lint_entry.py:83` drops multi-hex-run clauses (`len(runs) != 1`) and never verifies ASCII decoding. Caught **ONLY BY SEATS**.
3. **Non-standard Git object introducers in Q15**: `corpus/lint_entry.py:94` checks only a 5-word whitelist (`commit|base|tip|since|at`), missing unbackticked, cross-line, or non-whitelisted introducers (`tree`, `snapshot`, `object`). Caught **ONLY BY SEATS**.
4. **Prose line-number drift vs embedded spec-quote output**: Prose assertions citing spec lines (e.g. S038 line numbers) are not cross-checked against the embedded `--spec-quotes` stdout blocks. Caught **ONLY BY SEATS**.

---

## 2. Cross-Round & Cross-Claim Recurring Defect Classes

Below is the exhaustive census of recurring defect classes across rounds 65, 67, 68, 69, round-70 wave 1, and the three round-70 claims (C1 coverage, C2 calibration, C3 freshness).

| # | Defect Class | Historical Origin & Evidence | Landed v5.1 Entry, Lint, or Gate Disposition | What Catches It |
|---|---|---|---|---|
| **DC-01** | **Missing Header Keys (Q02, M18)** | Required keys (`source:`, `verified-at:`, `recheck:`, `coverage-map:`) omitted or misplaced in first 40 lines. | **MECHANICALLY CAUGHT** by `corpus/lint_entry.py` (`lint_header()`, lines 98–101). Tested clean on landed entry (`LINT_HEADER=0`). | `corpus/lint_entry.py` / `C1_LINT` |
| **DC-02** | **§Q-map Silent Dropping / Incomplete Rubric (r69 §Q-map regression)** | Round 69 v4 candidate silently dropped §Q-map from 13 rows to 8 rows while `QUALITY.md` held 15 criteria (`lessons/round-69.md:119`). | **MECHANICALLY CAUGHT** by `corpus/lint_entry.py` (`lint_qmap()`, lines 52–67). Requires every `| Qnn |` in `QUALITY.md` to have a non-empty decision cell. Landed entry has all 15 rows (`LINT_QMAP=0`). | `corpus/lint_entry.py` / `C1_LINT` |
| **DC-03** | **Embedded Output Verbatim Drift (M39, M45)** | Quoted command stdout lines inside fenced `$ <cmd>` blocks drifting from live script output (round-65 M39, round-67 C7). | **MECHANICALLY CAUGHT** by `corpus/check_embedded_outputs.py` (`parse_blocks()`, `run_cmd()`, `drift()`). Landed entry verified: 24 checked blocks, 0 problems (`C1_GATE=checked_blocks=24 problems=0 exit=0`). | `corpus/check_embedded_outputs.py` / `C1_GATE` |
| **DC-04** | **In-Place Script Drift Breaking Retained Candidates (Freshness Harm V6)** | Round 69 extended `corpus/derive_axml_anchors.py` in place, breaking embedded bare enum lines in the retained round-68 candidate (`C7_V3_CLEAN` went yes→no, problems=7; `round-69-verifier-spotcheck.md:88-95`). | **MECHANICALLY CAUGHT** by `corpus/check_embedded_outputs.py` (`load_pins()`, `apply_pin()`) via `corpus/embedded_output_pins.json` binding r68 to `derive_axml_anchors_r68.py` (sha256 `bce497d6...`). Verified `EMB_R68 problems=0`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`. | `corpus/check_embedded_outputs.py` / `C3` |
| **DC-05** | **Self-Assessment Metadata & Index Drift (SM1–SM6, V2, V7)** | Stale README index ranges (`Q01–Q13` vs Q15), unnamed top-level tools, stale SHONEN quoted digests/sizes (`39098 B`/`bfd92057`), lane-seat `[x]` verifiers, unresolvable SCORECARD commit citations (`e1d22caf`). | **MECHANICALLY CAUGHT** by `corpus/self_assessment_check.py` (`sm1` through `sm6`). Scores clean on landed commit (`SELF_MISMATCH=0 exit=0`, `SELF_MUTANTS_KILLED=6/6`, `A1_C2=yes`). | `corpus/self_assessment_check.py` / `C2` / `measure-a1.py` |
| **DC-06** | **Do-Nothing / Mock Counter Gaming (ControlAudit I, J, K)** | Round 70 Wave 1 `R70W1ControlAudit` proved that 17-block echo entries, mock 27-line checkers, and echo pins reached frozen `HOLDS_C1_V5`, `HOLDS_C2_V5`, `HOLDS_C3_V1` with zero real work. | **MECHANICALLY CAUGHT** by `reports/round-70/measure-a1.py` (A1_C1 requires >=17 distinct allowlisted script commands, all 15 readout lines, >=5 tier-A sources; A1_C2 requires base-vector match + 6 randomised variants; A1_C3 checks script digest and line count). | `reports/round-70/measure-a1.py` |
| **DC-07** | **Canonical Single-Hex Run Byte Count Mismatches (Q14, M47)** | Stating a byte count N on a single backticked hex run H where `len(H) != 2*N`, or stating a count on an ellipsis-truncated run (`4d616e69666573742d` = 9 bytes called "16-byte"). | **MECHANICALLY CAUGHT** by `corpus/lint_entry.py` (`lint_q14()`, lines 70–88) for single-run clauses outside fences. | `corpus/lint_entry.py` (`LINT_Q14`) |
| **DC-08** | **Canonical Stale Git Commit Citations (Q15, M48)** | Quoting an unresolvable 7–40 hex git commit ID introduced by `commit|base|tip|since|at` in prose. | **MECHANICALLY CAUGHT** by `corpus/lint_entry.py` (`lint_q15()`, lines 91–95). | `corpus/lint_entry.py` (`LINT_Q15`) |
| **DC-09** | **Asymmetric Verbatim Check: Embedded Output Line Deletion** | Deleting embedded stdout lines from a fenced block (`M2` in `R70W1GateMutants.md`). Because `drift()` only tests `line not in stdout_set`, any proper subset of stdout passes with 0 problems. | **NOT CAUGHT AT ALL** mechanically. The entry explicitly discloses this at line 310 ("Unguarded clauses, named: deleting an embedded output line is not detected..."). Neither gate nor lint checks embedded line counts per block. | **ONLY BY SEATS** (under Q13 rubric audit, if line counts are independently re-checked). |
| **DC-10** | **Asymmetric Verbatim Check: Flag Fallback Degradation** | Typo or corrupt argument in a script call (e.g. `readout.py --fakt archive`, `M5` in `R70W1GateMutants.md`). `readout.py:43` silently falls back to dumping all 15 facts. Gate sees all embedded lines in stdout superset and exits 0. | **NOT CAUGHT AT ALL** mechanically. Neither `check_embedded_outputs.py` nor `lint_entry.py` checks command arguments or flag validity. | **ONLY BY SEATS** (under Q11/Q13 command inspection). |
| **DC-11** | **Multi-Hex-Run Clauses & ASCII Decode Mismatches (Q14 G1/G4)** | Clauses containing >1 hex run (e.g. two separate headers) are skipped by `lint_q14` (`if len(runs) != 1: continue`). Hex runs whose decoded ASCII disagrees with stated ASCII (e.g. `4d616e69666573742d` vs `ManifestX`) are never decoded by the lint. | **NOT CAUGHT AT ALL** mechanically. Skipped by regex design in `lint_entry.py`. Landed v5.1 avoids backticked hex in prose to stay green, making `LINT_Q14=0` vacuous. | **ONLY BY SEATS** (under Q14 manual hex/ASCII decode). |
| **DC-12** | **Non-Standard Git Introducers & Cross-Line Hashes (Q15 G8/G9)** | Unresolvable git commit or tree IDs preceded by `tree`, `snapshot`, `object`, `derived from`, or split across line breaks. | **NOT CAUGHT AT ALL** mechanically. `lint_q15` strictly matches `\b(commit|base|tip|since|at)\s+`[0-9a-f]{7,40}``. | **ONLY BY SEATS** (under Q15 manual git rev-parse sweep). |
| **DC-13** | **Prose Line Citation vs Embedded Snapshot Output Drift** | Prose citing spec line numbers (e.g. "lines 237-253", "line 686") drifting from the actual snapshot lines printed by `--spec-quotes` or `derive_axml_anchors.py`. | **NOT CAUGHT AT ALL** mechanically. `check_embedded_outputs.py` checks block stdout, but does not parse preceding or following Markdown prose paragraphs. | **ONLY BY SEATS** (under Q04/Q11 cross-checking). |
| **DC-14** | **Literal Struct Widths & Hardcoded Constants Stated as Derived (Q04, Q11, M08, M20)** | Constants (such as APPNOTE 30/46/22 widths or AXML struct widths) present in Python dictionaries while entry prose implies they are derived from spec. | **CAUGHT ONLY BY SEATS**. In v5.1, explicitly repaired by labeling widths as "manually transcribed" and comparing them in `entry_checks.py --zip-layout` / `--axml-layout`. Neither lint nor gate can evaluate semantic truth of derivation labels. | **ONLY BY SEATS** (under Q04 and Q11). |
| **DC-15** | **Semantic Mismatch: Description vs Execution Path (Q07, M07, M12)** | Explanatory prose asserting a mechanism that code does not execute (e.g. r68/r69 entry line 91 asserting namespace resolution through start-namespace chunk, when readout executed `strings[ans]` on raw index 0). | **CAUGHT ONLY BY SEATS**. Mechanical tools evaluate command exit and string presence, not programmatic causation or semantic alignment. | **ONLY BY SEATS** (under Q07). |
| **DC-16** | **Unprobed Refusal Paths & Phantom Capabilities (Q05, M01, M19)** | Entry crediting a tool refusal path (e.g. "a missing or ambiguous symbol is exit 2") without an executable probe showing that refusal. | **CAUGHT ONLY BY SEATS**. If an entry includes unprobed capability sentences, lint and gate pass silently. (Repaired in v5.1 by stripping refusal claims and probing Exit 0 with `check=True` in `entry_checks.py --stdout-digest`). | **ONLY BY SEATS** (under Q05). |
| **DC-17** | **Overreaching Universal Claims & Format Generalization (Q10, M15)** | Presenting single-fixture observations as general ZIP/AXML/DEX parser specifications. | **CAUGHT ONLY BY SEATS**. No mechanical tool detects inductive overreach in natural language. | **ONLY BY SEATS** (under Q10). |

---

## 3. Vulnerability Analysis: What a Future Closure / Spot-Check Seat Will Cite

Based on the precedents established in `corpus/lessons/round-67-verifier-spotcheck.md`, `round-68-verifier-spotcheck.md`, and `round-69-verifier-spotcheck.md`, a future closure or spot-check seat (@m_flash, @m_swe, @m_kfc) will examine landed bytes against pre-registration declarations and committed receipts. The landed bytes at `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` expose the following checkable points:

### 3.1 Pre-Registration vs Landed Entry Divergence on Q15 / `c7b7cf98`
- **Location**: `reports/round-70/claims.md:35` vs `corpus/knowledge/round-70-apk-axml-byte-evidence.md:312` and `reports/round-70/claims-amendment-A1.md:47-49`.
- **Finding**: Pre-registration `claims.md:35` declared:
  > *"the `c7b7cf98` identity derived and a Q15 row"*
  In the landed v5.1 candidate entry, `c7b7cf98` does not appear anywhere (`grep -c c7b7cf98` = 0), and line 312 reads:
  > `| Q15 | pass | this entry states no git object id; identity statements are file digests printed by item 14. |`
- **Closure Citation Likelihood**: HIGH. Hyaku closure seats specifically cross-check every item in `claims.md` §Claims against the tip commit. Amendment A1 explicitly noted this divergence ("Deviation from the pre-registration prose (recorded, not a predicate change)"), which shields the lane from an unannounced substitution claim, but closure will record it as a documented deviation.

### 3.2 Explicitly Admitted Verification Asymmetry in Gate
- **Location**: `corpus/knowledge/round-70-apk-axml-byte-evidence.md:310` (§Q-map row Q13).
- **Finding**: The entry text explicitly concedes:
  > *"Unguarded clauses, named: deleting an embedded output line is not detected (the comparison is one-directional), and a command whose flag is corrupted still passes if its output is a superset of the embedded lines (the readout degrades an unknown flag to its full dump); the entry credits no verifier for either."*
- **Closure Citation Likelihood**: HIGH. Closure spot-checks re-evaluate the strength of admitted knowledge. While documenting the limitation satisfies Q13's admission procedure, a closure reviewer will cite that the gate `corpus/check_embedded_outputs.py` allows partial-output deletion without failing.

### 3.3 Vacuous Pre-Flight Lint Execution (`LINT_Q14=0`, `LINT_Q15=0`)
- **Location**: `corpus/lint_entry.py` run on `corpus/knowledge/round-70-apk-axml-byte-evidence.md`.
- **Finding**: `LINT_Q14=0` and `LINT_Q15=0` pass because the candidate entry stripped all backticked hex runs with byte counts from prose (item 10 describes the payload length in prose words without backticking the hex, and pin lines use coreutils format) and stripped all git object IDs.
- **Closure Citation Likelihood**: MEDIUM. Closure seats will note that `C1_LINT` passed due to prose avoidance rather than active verification of hex/commit facts.

### 3.4 SHONEN Promotion Box 1 Status
- **Location**: `SHONEN.md:5-16` vs `corpus/self_assessment_check.py` (SM3/SM4).
- **Finding**: Box 1 was corrected from `[x]` to `[~]` and stale digest strings removed to satisfy C2's SM3/SM4 checks (`SELF_MISMATCH=0`).
- **Closure Citation Likelihood**: LOW/NEUTRAL. Closure seats (e.g. r68 spot-check §1, r69 spot-check §1) have consistently held that SHONEN promotion is non-lane/operator duty. Transitioning box 1 to `[~]` with explicit explanation of lane attestation correctly aligns the repository with closure rules.

---

## 4. UFO-FSD Connector Synthesis: One Non-Obvious Move

### Evidence
1. **The Deletion-Immunity Gap**: `corpus/check_embedded_outputs.py:140` runs `problems += drift(lines, stdout_set, lineno)` where `drift` flags only lines present in `lines` but absent in `stdout_set`. In wave 1, `R70W1GateMutants` showed that mutant `M2` (deleting an embedded line) survived with exit 0.
2. **The Flag Degradation Gap**: `corpus/fixtures/apk-r65/readout.py:43` silently falls back to printing all 15 facts on unknown or mistyped flags (`--fakt`), which satisfies the subset check (`M5` in `R70W1GateMutants`).
3. **The Routed-Repair Ledger Need**: `considerthese/2026-10-25.md` proposal 1 ("Routed-repair carry-through check") notes that candidates repeatedly fail on sentences that were already routed in previous round spot-checks.

### Affected Axes
- **Calibration**: **Improves**. Closes the structural gap between claimed verbatim verification and actual one-directional subset tolerance.
- **Freshness**: **Neutral / Protected**. Does not alter any historical script pin or break retained candidate re-derivations.
- **Coverage**: **Neutral**. Does not alter C05 admission criteria or knowledge scope.
- **Operability**: **Improves**. Turns an admitted unguarded clause into a mechanical gate check without modifying the frozen line 140.

### Proposed Move
**Synthesize a Non-Intrusive Bidirectional Line-Count Guard beside the Frozen Gate Line.**
In `corpus/check_embedded_outputs.py`, without altering the frozen line:
```python
problems += drift(lines, stdout_set, lineno)
```
Add an adjacent block-level line-count check for single-command blocks:
```python
# Bidirectional verbatim check: if command is a single-fact readout, embedded line count must match stdout line count
stdout_lines = [l for l in proc.stdout.splitlines() if l.strip()]
if len(lines) != len(stdout_lines):
    problems.append(f"block line-count mismatch: embedded={len(lines)} stdout={len(stdout_lines)} at line {lineno}")
```
Simultaneously, add a strict-flag mode to fixture readouts (`readout.py`) so unrecognized flags exit non-zero (`SystemExit(2)`) rather than degrading to a full dump.

### Risks
1. *Breakage of Multi-Fact Output Truncation*: Some entries might intentionally embed only a snippet of a large command's stdout.
   *Mitigation*: Restrict the line-count equality check to commands marked `--fact <name>` or entries with single-output blocks, or make it an opt-in header directive `recheck-exact: yes`.
2. *Contract Freeze Violation*: Modifying line 140 in round 70 would violate C3's frozen kill rule.
   *Mitigation*: This move is proposed for Round 71 post-closure adoption; within round 70, the frozen lines are untouched.

### Verification
In scratch test:
1. Mutate `corpus/knowledge/round-70-apk-axml-byte-evidence.md` by deleting line 159 (`MATCH eocd.total_entries...`).
2. Run `check_embedded_outputs.py --entry <mutated>`.
3. Verify that `problems` increases from 0 to 1 with `block line-count mismatch: embedded=15 stdout=16`.
4. Mutate `--fact archive` to `--fakt archive`.
5. Verify that `readout.py` exits 2 and gate records `proc.returncode != 0`.

---

## 5. Conclusion

The round-70 landed candidate bytes, mechanical lints, and self-assessment tools make major advances on calibration and do-nothing control closure, but the pattern scan demonstrates that **mechanical coverage is not total**. Gate verification remains strictly one-directional, multi-run Q14 clauses and non-standard Q15 introducers slip through regex lints, and prose-to-code semantic consistency remains entirely dependent on seat-level audit. Thus, **PATTERNS-UNCOVERED** is the verified state of the repo's mechanical defenses.
