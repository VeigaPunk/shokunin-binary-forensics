# ConnectorOverlap — revenger round 97, attempt 1 (seat report)

**Seat:** `ConnectorOverlap` (`ConnectorOverlap-31`)  
**Role:** UFO-FSD connector (leaf member; read-only over siblings, fleet, and lane files)  
**Lane:** `revenger` (`/home/vgpnk/Projects/shokunin/revenger-shokunin`)  
**Freeze commit:** `3b4b4e5c1d123d5fc5337ad59015b4752366854a` (`reports/round-97/claims.md`)  
**Judged on:** coverage, calibration  
**Milestone:** Sibling-overlap scan for the round's surfaces (read-only)  
**Deliverable:** `.ufo/waves/round-97/w1/ConnectorOverlap.md`  
**Receipts:** `.ufo/waves/round-97/w1/ConnectorOverlap/` (`query_a.log`, `query_b.log`, `query_c.log`, `query_d.log`)  

---

## 1. Executive Summary & Scan Scope

Per task directive, performed a read-only overlap scan across all 20 sibling lane repositories (`/home/vgpnk/Projects/shokunin/*-shokunin` excluding `revenger-shokunin`) and the fleet waves tree (`/home/vgpnk/Projects/shokunin/.ufo/waves`).

Scanned surfaces correspond directly to revenger round 97's declared claims:
- **C1 (coverage):** Row C02 `partial -> held` through v6 admission counter (`c1_k_admit_counter6.py`), candidate knowledge entry `round-96-native-analysis-sessions.md`, vote-binding digest `2f7d4c1b...`, and `used-by` exclusivity against `corpus/SOURCES.md` rows S502/S503/S504 citing REA git commit `12f6e09`.
- **C2 (calibration):** Reach over 19 routed forgery vectors (FG01–FG20, FG17 absent) evaluated by `forge_reach6.py`.
- **Skip-work / Do-nothing controls:** Base tree `7d380ce` do-nothing control (`c1-do-nothing-v5.log`), v5 reach control (`c2-v5-reach-from-r96-receipts.txt`), and `considerthese/2026-11-05.md` proposal 1.

All findings are **reported, not absorbed** in accordance with `corpus/QUALITY.md` Q10 ("Cross-lane contested scope is reported, not absorbed").

---

## 2. Query (a): `admission-status` with `used-by` in scripts or counters (*.py, *.sh)

### Grep Execution & Counts
- **Command:**
  ```bash
  grep -rn --exclude-dir='.git' --include="*.py" --include="*.sh" "admission-status" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  *(Explicit paths over all 20 sibling lanes and fleet .ufo/waves, excluding revenger-shokunin)*
- **Exit Code:** `1`
- **Hit Count:** **0 hits** in scripts or counters (`*.py`, `*.sh`).
- **Scripts containing both `admission-status` AND `used-by`:** **0 hits** (exit code `1`).

### Context Check (All File Types)
A supplemental sweep for `admission-status` across all file types yielded **5 matches in 4 files** (exit code `0`):
1. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-92/w1/ConnectorScope/receipts/query-stale.txt:746` — text record of revenger r63 entry `admission-status: admitted`
2. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-92/w1/ConnectorScope/receipts/query-stale.txt:747` — text record of revenger r64 entry `admission-status: admitted`
3. `/home/vgpnk/Projects/shokunin/kengaku-shokunin/.ufo/waves/round-48/w1-results.json:226` — review json text
4. `/home/vgpnk/Projects/shokunin/kengaku-shokunin/.ufo/waves/round-74/w1/EntryFalsifyR74.md:3` — reviewer prompt text citing `admission-status`
5. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-9/d3/capability-draft.md:89` — note stating `SKILL.md carries no admission-status text for D3`

### Shared Surface with C1 / C2 & Disposition
- **Shared Surface:** C1 admission counter (`reports/round-97/c1_k_admit_counter6.py`) parses knowledge entry frontmatter `admission-status: candidate -> admitted` and cross-validates `used-by` exclusivity in `corpus/SOURCES.md`.
- **Finding:** No sibling lane possesses scripts or counters implementing `admission-status` inspection alongside `used-by`. The mechanism is unique to `revenger-shokunin`.
- **Disposition:** Reported; not absorbed (QUALITY.md Q10). Receipt: `.ufo/waves/round-97/w1/ConnectorOverlap/query_a.log`.

---

## 3. Query (b): `C1_K_HELD_BACKED` or `C1_VERDICT`

### Grep Execution & Counts
- **Command 1 (`C1_K_HELD_BACKED`):**
  ```bash
  grep -rn --exclude-dir='.git' "C1_K_HELD_BACKED" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `1` | **Hit count:** **0 hits**
- **Command 2 (`C1_VERDICT`):**
  ```bash
  grep -rn --exclude-dir='.git' "C1_VERDICT" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Hit count:** **23 matches in 18 files**
- **Combined Command (`C1_K_HELD_BACKED|C1_VERDICT`):**
  ```bash
  grep -rn --exclude-dir='.git' -E "C1_K_HELD_BACKED|C1_VERDICT" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Hit count:** **23 matches in 18 files**

### Complete List of Every Hit (path:line)
1. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-24/w1/SimplifyReplayPort.md:58`  
   `| C1_VERDICTS | measure_c1 | {"HOLD","STALE","UNVERIFIABLE"} |`
2. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-48/assimilation/validate/.ufo/waves/round-24/w1/SimplifyReplayPort.md:58`  
   `| C1_VERDICTS | measure_c1 | {"HOLD","STALE","UNVERIFIABLE"} |`
3. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-72/w1-results.json:46`  
   `verdict cells TIP_C1_VERDICT / TIP_C2_VERDICT`
4. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-72/w1/ScribeLesson.md:9`  
   `verdict cells are the L1's TIP_C1_VERDICT / TIP_C2_VERDICT placeholders.`
5. `/home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-72/w1/ScribeLesson.md:15`  
   `| TIP_C1_VERDICT |`
6. `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S04Report.md:46`  
   `- **C1 consistency/calibration — {{C1_VERDICT}}**`
7. `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80S04Report.md:85`  
   `C1_EXITS, C1_VERDICT — the runner's 01-tip-battery-dot.txt and`
8. `/home/vgpnk/Projects/shokunin/kumitate-shokunin/.ufo/waves/round-68/build/K68ScribeScorecard/scorecard-block.md:8`  
   `__TIP_RECEIPT__, __C1_VERDICT__, __C2_VERDICT__, __SELFTEST_N__, __ROWS_AT_M__, __GATES__.`
9. `/home/vgpnk/Projects/shokunin/kumitate-shokunin/.ufo/waves/round-68/build/K68ScribeScorecard/scorecard-block.md:26`  
   `Verdict by the frozen counter: **__C1_VERDICT__**.`
10. `/home/vgpnk/Projects/shokunin/kumitate-shokunin/.ufo/waves/round-68/w1-results.json:184`  
    `__TIP_RECEIPT__, __C1_VERDICT__, __C2_VERDICT__, __SELFTEST_N__, __ROWS_AT_M__, __GATES__`
11. `/home/vgpnk/Projects/shokunin/kumitate-shokunin/.ufo/waves/round-68/w1/K68ScribeScorecard.md:57`  
    `Unfilled tokens for the L1: __FREEZE_COMMIT__, __MEASURED_M__, __TIP_RECEIPT__, __C1_VERDICT__, __C2_VERDICT__...`
12. `/home/vgpnk/Projects/shokunin/mado-shokunin/.ufo/waves/round-17/drafts/ReportSkeleton.md:41`  
    `| C1 {{C1_AXIS}} | {{C1_BEFORE}} | {{C1_AFTER}} | {{C1_VERDICT}} |`
13. `/home/vgpnk/Projects/shokunin/souji-shokunin/.ufo/waves/round-23/w1/ScribeReport.md:230`  
    `| <C1_VERDICT> |`
14. `/home/vgpnk/Projects/shokunin/souji-shokunin/.ufo/waves/round-23/w1/ScribeReport.md:386`  
    `| <C1_AFTER_RC>, <C1_VERDICT>, <C1_COUNTER_VERDICT>, <C1_AXIS_MOVE>, <CAL_SCORE> | tip run + critic verdicts |`
15. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-49/w1-results.json:346`  
    `only <C1_VERDICT> and the misses paragraph change`
16. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-49/w1/R49ScribeScore.md:86`  
    `| **<C1_VERDICT>** | depth unchanged (ordinal 8...)`
17. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-49/w1/R49ScribeScore.md:120`  
    `verdicts_ok <C1_VERDICTS>`
18. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-49/w1/R49ScribeScore.md:161`  
    `only <C1_VERDICT> and the`
19. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-69/probes/K1Critic/critique.md:343`  
    `K1_ATTACKS=14 K1_FATAL=3 K1_C1_VERDICT=fails K1_C2_VERDICT=weakened`
20. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-69/w1-dispatch.json:242`  
    `FINAL: K1_ATTACKS=<n> K1_FATAL=<n> K1_C1_VERDICT=<stands|weakened|fails> K1_C2_VERDICT=<stands|weakened|fails>`
21. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-69/w1-results.json:70`  
    `"K1_C1_VERDICT": "fails"`
22. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-69/w1-spec.json:134`  
    `FINAL: K1_ATTACKS=<n> K1_FATAL=<n> K1_C1_VERDICT=<stands|weakened|fails> K1_C2_VERDICT=<stands|weakened|fails>`
23. `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-69/w1/K1Critic.md:20`  
    `K1_ATTACKS=14 K1_FATAL=3 K1_C1_VERDICT=fails K1_C2_VERDICT=weakened`

### Shared Surface with C1 / C2 & Disposition
- **Shared Surface:**
  - `C1_K_HELD_BACKED`: 0 hits outside revenger. Unique to revenger's coverage metric `12/15 -> 13/15`.
  - `C1_VERDICT`: Shared reporting token output by admission/verification counters (`C1_VERDICT=pass|fail`) used across 6 sibling lanes (kake, kotoba, kumitate, mado, souji, tsukuroi) as template placeholders and critic outputs.
- **Disposition:** Reported; not absorbed (QUALITY.md Q10). Receipt: `.ufo/waves/round-97/w1/ConnectorOverlap/query_b.log`.

---

## 4. Query (c): `skip-work` or `do-nothing`

### Grep Execution & Counts
- **Command 1 (`skip-work`):**
  ```bash
  grep -rn --exclude-dir='.git' --exclude-dir='.jj' "skip-work" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Total hits:** `7,105` (7,099 in sibling lanes + 6 in fleet waves)
- **Command 2 (`do-nothing`):**
  ```bash
  grep -rn --exclude-dir='.git' --exclude-dir='.jj' "do-nothing" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Total hits:** `38,278` (38,270 in sibling lanes + 8 in fleet waves)
- **Combined Command (`skip-work|do-nothing`):**
  ```bash
  grep -rn --exclude-dir='.git' --exclude-dir='.jj' -E "skip-work|do-nothing" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Total hits:** **45,278** (45,264 in sibling lanes + 14 in fleet waves)

### Complete List of Fleet Waves Hits (`/home/vgpnk/Projects/shokunin/.ufo/waves`)
1. `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-audit/members/KengakuIdentityAndTree.md:18`  
   `| Working tree clean apart from untracked plans/ | Agree | ... No assume-unchanged / skip-worktree. |`
2. `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-audit/members/FleetIdentityAudit.md:38`  
   `git ls-files -v has no skip-worktree (S) and no assume-unchanged (lowercase) flag`
3. `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-audit/members/KakeIdentityAndTree.md:29`  
   `| git -C kake-shokunin ls-files -v filtered to assume-unchanged / skip-worktree | 0 | empty |`
4. `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-audit/members/KakeIdentityAndTree.md:79`  
   `No assume-unchanged or skip-worktree bits. No ignored untracked residue.`
5. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/JjDocGitIndex.md:115`  
   `state (staged blobs, stage entries, assume-unchanged/skip-worktree flags) is discarded.`
6. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/JjDocGitIndex.md:193`  
   `- **Index flags are lost**: git update-index --skip-worktree b.txt (S b.txt) becomes H b.txt`
7. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/JjDocGitIndex.md:235`  
   `6. **Do not use index flags or sparse checkout in lanes.** skip-worktree / assume-unchanged are`
8. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/PHASE4.md:68`  
   `lane-addendum.md §9 now states: a target must be one a do-nothing control cannot reach (score the cheapest control with the frozen counter before building and commit the receipt)`
9. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/PHASE4.md:77`  
   `decisive causes over the five rejections — target reachable by a do-nothing control: kake r34, tsukuroi r30 (plus kumitate's proxy)`
10. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/PHASE4.md:89`  
    `C1 operability gate-mutants re-claimed under one frozen kill rule K43 (do-nothing control at round open SURVIVED 34/41, exit 1, committed before building...`
11. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/PHASE4.md:97`  
    `C1 operability (link-preview audit repair: 14/24 -> 24/24 sealed cases, target >= 22; do-nothing controls 7-14...`
12. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/PHASE4.md:125`  
    `Author: C1 operability (omp-census gate) does NOT verify (3 skip-work programs meet the frozen counter p44d 207/207 after the counted run...`
13. `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/PHASE4.md:127`  
    `C1 operability unprovable: p44b met by label-keyed controls (87/87); p44c and p44d replaced after seats scored; p44d met after data by 3 skip-work programs (kill rule 2).`
14. `/home/vgpnk/Projects/shokunin/.ufo/waves/round-41/w1/swarm-registry.legacy-wave-v1.json:213`  
    `"Attack the do-nothing control in /home/vgpnk/Projects/shokunin/chousa-shokunin: controls/base-gate-r41."`

### Per-Lane Count Breakdown Across 20 Sibling Lanes

| Sibling Lane Repo | `skip-work` Hits | `do-nothing` Hits | Combined Hits |
|:---|:---:|:---:|:---:|
| `audio-shokunin` | 0 | 1 | 1 |
| `chousa-shokunin` | 10 | 1,762 | 1,770 |
| `game-dev-2d-shokunin` | 0 | 0 | 0 |
| `game-dev-3d-shokunin` | 3 | 0 | 3 |
| `kagi-shokunin` | 6 | 205 | 211 |
| `kaidoku-shokunin` | 520 | 9,410 | 9,926 |
| `kake-shokunin` | 67 | 2,236 | 2,303 |
| `kama-shokunin` | 17 | 2,342 | 2,355 |
| `kasegi-shokunin` | 66 | 4,014 | 4,080 |
| `kengaku-shokunin` | 7 | 1,544 | 1,547 |
| `kotoba-shokunin` | 3 | 1,025 | 1,028 |
| `kotodama-shokunin` | 3 | 1,549 | 1,552 |
| `kumitate-shokunin` | 345 | 1,437 | 1,778 |
| `lore-shokunin` | 0 | 0 | 0 |
| `mado-shokunin` | 22 | 1,728 | 1,748 |
| `mori-shokunin` | 68 | 1,924 | 1,973 |
| `souji-shokunin` | 5,312 | 4,426 | 9,704 |
| `tabi-shokunin` | 489 | 2,242 | 2,719 |
| `tameshi-shokunin` | 34 | 1,252 | 1,286 |
| `tsukuroi-shokunin` | 127 | 1,173 | 1,280 |
| **Sibling Lanes Total** | **7,099** | **38,270** | **45,264** |
| **Fleet `.ufo/waves`** | **6** | **8** | **14** |
| **Grand Total** | **7,105** | **38,278** | **45,278** |

### Shared Surface with C1 / C2 & Disposition
- **Shared Surface:** Hyaku Addendum §9 mandates fleet-wide that "a target must be one a do-nothing control cannot reach". Revenger round 97 claims conform directly:
  - C1 do-nothing control (`claims.md:34`): base tree `7d380ce` under v6 scores `C1_VERDICT=fail` and `C1_K_HELD_BACKED=12/15` (`reports/round-97/controls/c1-do-nothing-v5.log`).
  - C2 do-nothing control (`claims.md:54`): frozen v5 counter accepts 14/19 routed forgeries (`reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt`).
- **Disposition:** Reported; not absorbed (QUALITY.md Q10). Receipt: `.ufo/waves/round-97/w1/ConnectorOverlap/query_c.log`.

---

## 5. Query (d): `12f6e09` or `native-and-artifacts.md` (other lanes citing the same REA revision)

### Grep Execution & Counts
- **Command 1 (`12f6e09`):**
  ```bash
  grep -rn --exclude-dir='.git' --exclude-dir='.jj' "12f6e09" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `1` | **Hit count:** **0 hits**
- **Command 2 (`native-and-artifacts.md`):**
  ```bash
  grep -rn --exclude-dir='.git' --exclude-dir='.jj' "native-and-artifacts.md" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Hit count:** **1,063 matches in 535 files**
- **Combined Command (`12f6e09|native-and-artifacts.md`):**
  ```bash
  grep -rn --exclude-dir='.git' --exclude-dir='.jj' -E "12f6e09|native-and-artifacts.md" \
    /home/vgpnk/Projects/shokunin/*-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/waves
  ```
  **Exit code:** `0` | **Hit count:** **1,063 matches in 535 files**

### Per-Lane Breakdown for `native-and-artifacts.md`
- `kaidoku-shokunin`: **500 files**
- `kumitate-shokunin`: **24 files**
- `tabi-shokunin`: **4 files**
- `kake-shokunin`: **1 file** (`query-stale.txt:736`)
- `souji-shokunin`: **1 file** (`fresh-120min.txt:747`)
- Fleet `.ufo/waves`: **5 files**

### Primary Finding on REA Revision Parity
- **ZERO other lanes cite git revision `12f6e09` (`12f6e0974cc0db0b3a9b86246accc76556837222`).**
- Cross-lane analysis of REA citations reveals sharp version segregation:
  - **`revenger-shokunin`:** Pins git commit `12f6e0974cc0db0b3a9b86246accc76556837222` from `https://raw.githubusercontent.com/morluto/rea/12f6e09.../references/native-and-artifacts.md` (SOURCES row S502, sha256 `c818ee34...`, 38,167 bytes).
  - **`kaidoku-shokunin`:** Pins **`v42`** referencing the local path `/home/vgpnk/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md` (SOURCES row S002, section `Recorded Linux crashes`).
  - **`kumitate-shokunin`:** Pins **`version: 37`** referencing `~/.kimi-code/skills/reverse-engineer-anything/references/native-and-artifacts.md` (`corpus/knowledge/kimi-skills-plugins.md:68`).
- **Shared Surface with C1:** Candidate entry `corpus/knowledge/round-96-native-analysis-sessions.md` cites S502 at commit `12f6e09`. While other lanes examine `native-and-artifacts.md`, none uses the remote GitHub commit `12f6e09`. Revenger's pin is completely isolated.
- **Disposition:** Reported; not absorbed (QUALITY.md Q10). Receipt: `.ufo/waves/round-97/w1/ConnectorOverlap/query_d.log`.

---

## 6. Non-Obvious Move (UFO-FSD Connector Synthesis)

### Evidence Across the Round Cache & Local Evidence
1. **Calibration Gap in C2 Harness (`ReviewerClaims.md` Finding 1):**  
   The frozen C2 counting command is `forge_reach6.py`, whose only declared target line is `C2_ACCEPTED=<n>/19` (target `0/19`). A trivial refuse-everything stub passes 0/19 accepted. While the claims prose references the positive control (honest candidate tree passes `C1_VERDICT=pass`), that positive control check is not embedded in the counting command's execution path.
2. **Coverage Row-Set Blind Spot in Admission Counter (`CriticR97.md` Vectors FR06 / FR07):**  
   CriticR97 demonstrated that `c1_k_admit_counter5.py` and `c1_k_admit_counter6.py` contain a subtle vulnerability in `check_coverage_rows`:
   - `C1_ROWS_TOTAL` checks `len(rows) == 15`.
   - `C1_ONLY_C02` iterates each row `r` present in the table, asserting that if `r[0] != "C02"`, it equals `base_rows[r[0]]`.
   - In FR06 and FR07, row C06 is overwritten with a duplicate copy of C01 (or C02). Because both instances of C01 equal `base_rows["C01"]`, `C1_ONLY_C02` passes! `len(rows)` remains 15! Row C06 is eliminated without detection, and K becomes 12 - 1 + 1 + 1 = 13/15.
3. **Considerthese Pre-Freeze Review (`considerthese/2026-11-05.md` Proposal 1):**  
   Proposal 1 mandates testing the cheapest skip-work controls (lookup table, refuse-everything stub, id-edited copy) before the round lands.

### Affected Axes
- **Calibration (C2):** Closes the vacuous refuse-everything counter vulnerability and defeats row-duplication / row-substitution forgeries (FR06/FR07).
- **Coverage (C1):** Guarantees that K held-row ground (`13/15`) strictly reflects the immutable, complete, ordered row set `C01..C15`, preventing coverage fabrication via row substitution.

### Proposed Move
**Hermetic Row-ID Set Bi-directionality & Positive-Control Binding in the v6 Admission & Harness Pipeline:**

1. **Bi-directional Row-ID Set Validation in `c1_k_admit_counter6.py`:**  
   Inside `check_coverage_rows` (under the existing `C1_ROWS_TOTAL` / `C1_ONLY_C02` leg, without creating new leg names or modifying the 18 frozen v5 leg interfaces), enforce exact ordered equality:
   ```python
   observed_ids = [r[0] for r in rows]
   if observed_ids != [f"C{i:02d}" for i in range(1, 16)]:
       return fail("C1_ROWS_TOTAL", f"coverage rows must be exactly C01..C15 in order; got {observed_ids}")
   ```
   This single check immediately kills CriticR97 vectors FR06 and FR07, ensuring that every canonical criterion C01–C15 is present exactly once.

2. **Positive-Control Harness Binding in `forge_reach6.py`:**  
   Require `forge_reach6.py` to evaluate the honest candidate fixture before scoring the 19 forgery vectors. The harness must assert `C1_VERDICT=pass` on the honest tree and emit:
   ```
   C2_POSITIVE=pass
   C2_ACCEPTED=0/19
   ```
   If a blanket-fail or refuse-everything counter is supplied, `C2_POSITIVE` fails (exit 1), preventing false zero-acceptance claims.

### Second-Order Effects & Risks
- **Runtime Surface:** List comparison is microsecond-scale; zero measurable performance overhead.
- **Contract Surface:** Does not alter `claims.md` frozen predicates; implements the declared intent ("passes every leg of the r96 v5 set" and "positive control: honest candidate accepted").
- **Substrate Surface:** Binds table parsing in `corpus/README.md` and harness evaluation in `forge_reach6.py`.
- **Risks & Mitigation:** Does not touch leg names; existing test suites expecting `C1_ROWS_TOTAL=pass` continue to pass on genuine trees while refusing FR06/FR07.

### Verification
- Red fixture with duplicated row (FR06 / FR07) triggers `C1_ROWS_TOTAL=fail`.
- Red refuse-everything stub fails `C2_POSITIVE=fail` with exit 1.
- Honest candidate tree passes with `C2_POSITIVE=pass`, `C2_ACCEPTED=0/19`, exit 0.

---

## 7. Discipline, Bounds, and Scratch Cleanup

- **Lane Bounds:** Leaf member — no subagents spawned, no tasks dispatched.
- **Write Scope:** Written only to assigned findings path (`.ufo/waves/round-97/w1/ConnectorOverlap.md`) and receipts directory (`.ufo/waves/round-97/w1/ConnectorOverlap/`). No lane-tracked files, no fleet-root files, and no sibling lane files were modified.
- **Scratch Cleanup:** Scratch root `/fast/scratch/hyaku/revenger-r97/ConnectorOverlap/` verified clean and removed before yield.
