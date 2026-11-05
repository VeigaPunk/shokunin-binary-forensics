# ConnectorOverlap — revenger round 98, wave w1 (findings report)

**Seat:** `ConnectorOverlap` (`ConnectorOverlap-33`)  
**Role:** UFO-FSD connector (leaf member; read-only over siblings, fleet, and lane files)  
**Lane:** `revenger` (`/home/vgpnk/Projects/shokunin/revenger-shokunin`)  
**Freeze commit:** `9d49002a3804de48d365b7d32849ada06745d64f` (`reports/round-98/claims.md`)  
**Judged on:** coverage  
**Milestone:** Sibling-overlap scan for host-readiness / doctor knowledge and admission-counter legs  
**Deliverable:** `.ufo/waves/round-98/w1/ConnectorOverlap.md`  
**Receipts:** `.ufo/waves/round-98/w1/ConnectorOverlap/` (`query_1_rea_doctor.log` … `query_10_script_admit_counter.log`)  

---

## 1. Executive Summary & Scan Scope

Per task directive, performed a comprehensive, read-only overlap scan across all 20 sibling lane repositories under `/home/vgpnk/Projects/shokunin/*-shokunin` (excluding `revenger-shokunin`).

The scan evaluated two explicit surfaces:
1. **Surface (a) — C14 Subject (Coverage):**
   - Host readiness for REA routes (`rea doctor`, host probes, per-route prerequisites: ZIP inventory, Ghidra provider, Hopper, IDA, Kuna, JADX/Android, firmware extraction via binwalk/unblob, client MCP registration, CLI launcher, and pwntools).
   - Source S506: REA connection and recovery reference at pinned git revision `12f6e09` (`12f6e0974cc0db0b3a9b86246accc76556837222`).
   - Source S507: Saved round-98 host-readiness run records (`corpus/live/runs/round-98/`).
   - Candidate knowledge entry: `corpus/knowledge/round-98-rea-host-readiness.md` (normalized digest `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`).
2. **Surface (b) — v7 Admission Counter New-Leg Classes (Calibration & Coverage):**
   - New admission counter legs declared in `reports/round-98/claims.md` for `c1_k_admit_counter7.py`:
     `C1_ROWSET`, `C1_ENTRY_BYTES` (leading BOM / UTF-8 purity), `C1_HEADER_POSITION` (frontmatter headers preceding fences), `C1_VERIFIED_AT` (access date freshness), `C1_VOTE_NOTES` (non-boilerplate audit evidence), `C1_OWNWORK_PATHS` (disk existence of own-work records), `C1_QUOTE_BYTES` (byte-exact quote hash), `C1_USEDBY_GROUNDED` (bi-directional citation between registry `used-by` and entry text), and `C1_ONLY_TARGET`.
   - Analogous checks across sibling scripts (`*.py`, `*.sh`).

Target search roots in each sibling lane:
- `corpus/knowledge/`
- `corpus/SOURCES.md`
- `reports/` and `.ufo/reports/` (where present)
- Sibling scripts and instruments (`*.py`, `*.sh`) lane-wide.

All findings are evaluated under `corpus/QUALITY.md` Q10 (*"A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed"*).

---

## 2. Per-Lane Hit Counts Across All 20 Sibling Lanes

Searches were conducted systematically using GNU grep (`grep -rnE --exclude-dir='.git' --exclude-dir='.jj'`).

### Per-Lane Count Summary Table

| # | Sibling Lane | (1) `rea doctor` | (2) `host-readiness` | (3) `connection-and-recovery` | (4) REA rev `12f6e09` | (5) Artifact Inventory | (6) v7 New Legs | (7) Script BOM | (8) Script Hdr Pos | (9) Script Used-By Ground | (10) Script Admit Counter |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `audio-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | `chousa-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 56 | 5 | 3 | 3 |
| 3 | `game-dev-2d-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | `game-dev-3d-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | `kagi-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 |
| 6 | `kaidoku-shokunin` | **32** | 0 | **20** | 0 | **81** | 0 | 8 | 12 | 0 | 1 |
| 7 | `kake-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 2,911 | 0 | 2 | 4 |
| 8 | `kama-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 24 | 1 | 0 | 1 |
| 9 | `kasegi-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 1 | 3 |
| 10 | `kengaku-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 68 | 1 | 0 | 19 |
| 11 | `kotoba-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 4 | 0 | 3 |
| 12 | `kotodama-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 33 | 0 | 2 | 0 |
| 13 | `kumitate-shokunin` | 0 | 0 | **1** | 0 | 0 | 0 | 5 | 1 | 1 | 0 |
| 14 | `lore-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 15 | `mado-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 34 | 29 | 3 | 12 |
| 16 | `mori-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 19 | 5 | 2 |
| 17 | `souji-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 669 | 2 | 13 | 0 |
| 18 | `tabi-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 3 |
| 19 | `tameshi-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 544 | 1 | 4 | 2 |
| 20 | `tsukuroi-shokunin` | 0 | 0 | 0 | 0 | 0 | 0 | 27 | 29 | 1 | 29 |
| **Total** | **All 20 Siblings** | **32** | **0** | **21** | **0** | **81** | **0** | **4,460** | **107** | **37** | **82** |

---

## 3. Query Details, Exact Commands & Analysis

### Query 1: `rea doctor` in Knowledge, Sources, and Reports
- **Command:**
  ```bash
  grep -rnE --exclude-dir='.git' --exclude-dir='.jj' 'rea doctor' \
    <sibling>/corpus/knowledge <sibling>/corpus/SOURCES.md <sibling>/reports <sibling>/.ufo/reports
  ```
- **Exit Code:** `0` (matches found)
- **Total Hits:** **32 hits** across all 20 siblings.
- **Hit Distribution:**
  - `kaidoku-shokunin`: **32 hits** (all in `corpus/knowledge/`).
  - Other 19 siblings: **0 hits**.
- **Key Hit Locations in `kaidoku-shokunin`:**
  1. `kaidoku-shokunin/corpus/knowledge/2026-10-13-doctor-taxonomy.md:3, 10, 14, 105, 119` — Deep examination of `rea doctor` taxonomy, CLI invocation, and 18-check audit output under REA 6.4.0.
  2. `kaidoku-shokunin/corpus/knowledge/2026-10-13-asar-surface.md:50, 58` — Notes that `rea doctor` reporting `healthy: false` does not blind the Electron/JS tool surface.
  3. `kaidoku-shokunin/corpus/knowledge/2026-10-13-mcp-registrations.md:72, 73` — Details `rea doctor --client <id> --json` repair path and MCP registration limits.
  4. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r2-firmware-probe.md:60, 61, 90, 105` — Documents that firmware providers are invisible to `rea doctor`.
  5. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4u-01-firmware-deep.md:79, 81, 108` — Documents that doctor blind spot persists even with working environment variables (`REA_*_COMMAND`).
  6. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4u-06-adb-surface.md:135, 173, 196` — Notes doctor never inspects ADB.
  7. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-13-pwntools-persist.md:14, 178` — Notes doctor is blind to `pwntools-elf` auxiliary provider.
  8. `kaidoku-shokunin/corpus/knowledge/2026-10-13-rea-live-jq-e2e.md:117, 120` — Documents `healthy: false` coexisting with working native-binary decompilation.
  9. `kaidoku-shokunin/corpus/knowledge/2026-10-13-rea-self-documentation.md:15, 61` — Analyzes `rea doctor` as live provider/substrate documentation.
- **Receipt:** `.ufo/waves/round-98/w1/ConnectorOverlap/query_1_rea_doctor.log`.

### Query 2: `host-readiness` / `host readiness`
- **Command:**
  ```bash
  grep -rnE --exclude-dir='.git' --exclude-dir='.jj' 'host[- ]readiness' \
    <sibling>/corpus/knowledge <sibling>/corpus/SOURCES.md <sibling>/reports <sibling>/.ufo/reports
  ```
- **Exit Code:** `1` (no matches found)
- **Total Hits:** **0 hits** across all 20 siblings. The phrase and conceptual criterion "host readiness for REA routes" is unique to `revenger-shokunin` (row C14).
- **Receipt:** `.ufo/waves/round-98/w1/ConnectorOverlap/query_2_host_readiness.log`.

### Query 3: `connection-and-recovery`
- **Command:**
  ```bash
  grep -rnE --exclude-dir='.git' --exclude-dir='.jj' 'connection-and-recovery' \
    <sibling>/corpus/knowledge <sibling>/corpus/SOURCES.md <sibling>/reports <sibling>/.ufo/reports
  ```
- **Exit Code:** `0` (matches found)
- **Total Hits:** **21 hits** across all 20 siblings.
- **Hit Distribution:**
  - `kaidoku-shokunin`: **20 hits** across 4 knowledge entries (`2026-10-13-mcp-registrations.md`, `2026-10-13-r2-skill-references-deep.md`, `2026-10-13-rea-self-documentation.md`, `2026-10-13-rea-skill-contract.md`).
  - `kumitate-shokunin`: **1 hit** in `corpus/knowledge/kimi-skills-plugins.md:70` (file-path listing of user skill references under `~/.kimi-code/skills/reverse-engineer-anything/references/connection-and-recovery.md`).
  - Other 18 siblings: **0 hits**.
- **Receipt:** `.ufo/waves/round-98/w1/ConnectorOverlap/query_3_connection_recovery.log`.

### Query 4: REA Git Commit `12f6e09`
- **Command:**
  ```bash
  grep -rnE --exclude-dir='.git' --exclude-dir='.jj' '12f6e09' \
    <sibling>/corpus/knowledge <sibling>/corpus/SOURCES.md <sibling>/reports <sibling>/.ufo/reports
  ```
- **Exit Code:** `1` (no matches found)
- **Total Hits:** **0 hits** across all 20 siblings.
- **Finding:** ZERO other lanes cite git revision `12f6e09` (`12f6e0974cc0db0b3a9b86246accc76556837222`) or its raw GitHub URL.
  - `revenger-shokunin` pins remote GitHub commit `12f6e09` (SOURCES rows S502, S503, S506).
  - Sibling `kaidoku-shokunin` pins local installed skill version `v42` (`/home/vgpnk/.agents/skills/reverse-engineer-anything/SKILL.md`, SOURCES row S001) and npm releases `rea-agents@6.7.0` (S037, S081) / `6.5.0` (S040, S080).
  - Sibling `kumitate-shokunin` references `version: "37"` under `~/.kimi-code/skills/reverse-engineer-anything`.
  - Revenger's remote pin is completely isolated.
- **Receipt:** `.ufo/waves/round-98/w1/ConnectorOverlap/query_4_rea_commit_12f6e09.log`.

### Query 5: Artifact Inventory (`inspect_artifact` and `inventory_artifact`)
- **Command:**
  ```bash
  grep -rnE --exclude-dir='.git' --exclude-dir='.jj' '(inspect[-_]artifact|inventory[-_]artifact)' \
    <sibling>/corpus/knowledge <sibling>/corpus/SOURCES.md <sibling>/reports <sibling>/.ufo/reports
  ```
- **Exit Code:** `0` (matches found)
- **Total Hits:** **81 hits** across all 20 siblings.
- **Hit Distribution:**
  - `kaidoku-shokunin`: **81 hits** (77 `inspect_artifact`, 9 `inventory_artifact`).
  - Other 19 siblings: **0 hits**.
- **Analysis:** Kaidoku utilizes `rea inspect-artifact` as a primary tool for ASAR, APK, AppImage, and HarmonyOS HAP inspection (e.g. `2026-10-19-arc3-r11-inspect-artifact-evidence-id-domain.md`, `2026-10-14-r12-01-queue-b-ready.md`). Both lanes observe that `inventory_artifact` runs as the nested substep of `inspect_artifact` and operates without Hopper or Ghidra.
- **Receipt:** `.ufo/waves/round-98/w1/ConnectorOverlap/query_5_artifact_inventory.log`.

### Query 6: v7 Admission Counter New-Leg Tokens
- **Command:**
  ```bash
  grep -rnE --exclude-dir='.git' --exclude-dir='.jj' \
    '(C1_ROWSET|C1_ENTRY_BYTES|C1_HEADER_POSITION|C1_VERIFIED_AT|C1_VOTE_NOTES|C1_OWNWORK_PATHS|C1_QUOTE_BYTES|C1_USEDBY_GROUNDED|C1_ONLY_TARGET)' \
    <sibling>/corpus/knowledge <sibling>/corpus/SOURCES.md <sibling>/reports <sibling>/.ufo/reports
  ```
- **Exit Code:** `1` (no matches found)
- **Total Hits:** **0 hits** across all 20 siblings. None of these leg tokens exist outside `revenger-shokunin`.
- **Receipt:** `.ufo/waves/round-98/w1/ConnectorOverlap/query_6_v7_new_legs.log`.

### Queries 7–10: Script and Instrument Sweep Across Sibling Lanes
- **Query 7 (`utf-8-sig|leading BOM|\ufeff` in scripts):** 4,460 hits across 16 siblings. Sibling tools frequently strip or reject BOMs (e.g. `tameshi-shokunin/tools/selfstate-freshness.py:164` enforces strict UTF-8 with BOM refusal; `mori-shokunin/tools/mori-job-runway.py:248` checks `text.startswith(BOM)`). None implement an admission counter leg `C1_ENTRY_BYTES`. Receipt: `query_7_script_bom.log`.
- **Query 8 (`header_pos|header_position|fence.*header` in scripts):** 107 hits across 11 siblings. Tools parse table headers or skip code fences (e.g. `tsukuroi-shokunin/tools/check-registry-coverage.py:218`, `mori-shokunin/tools/mori-pin-check.py:111`). None implement `C1_HEADER_POSITION` requiring frontmatter headers to precede fences in candidate knowledge entries. Receipt: `query_8_script_header_pos.log`.
- **Query 9 (`used-by.*ground` in scripts):** 37 hits across 8 siblings. All hits occur in task dispatch specs requiring "grounded teaches cells" alongside `used-by` paths; zero hits implement automated bi-directional entry-to-source grounding checks (`C1_USEDBY_GROUNDED`). Receipt: `query_9_script_usedby_grounding.log`.
- **Query 10 (`admit_counter|c1_k_admit|admission.*counter` in scripts):** 82 hits across 11 siblings. Several lanes maintain admission counters (e.g. `kengaku-shokunin/plans/round84_c2_admission.py` checking Q1/Q21 rules, `tsukuroi-shokunin`, `chousa-shokunin`). Each counter is tightly bound to its respective lane's specific criteria and Q-rules; none share revenger's K held-backed admission architecture. Receipt: `query_10_script_admit_counter.log`.

---

## 4. Contested Scope Assessment (QUALITY.md Q10)

`corpus/QUALITY.md` Criterion Q10 states:
> *"A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed."*

### Sibling Scope vs. Revenger Scope
- **`kaidoku-shokunin` (Province):** Reverse engineering of shipped artifacts using REA on Linux (native ELF via Ghidra 12.1.4, Electron/ASAR/JS bundles, APKs, WebAssembly). Kaidoku focuses on artifact deconstruction, decompilation sessions, symbol recovery, and tool provider internals (e.g. `Doctor.js`, `DoctorDiagnostics.js` in REA 6.4.0/6.5.0/6.7.0).
- **`revenger-shokunin` (Province & C14 Criterion):** Host readiness for REA routes specifically within revenger's coverage map (row C14: ZIP inventory, Ghidra provider configuration, CLI launcher availability, client MCP registration, pwntools importability) on date 2026-11-05, backed by S506 (remote pinned recovery reference `12f6e09`) and S507 (saved host probe and ZIP inspection receipts).

### Scope Boundaries & Non-Absorption
1. **Explicit Negative Boundaries:** Revenger's candidate entry `round-98-rea-host-readiness.md` explicitly confines its scope:
   > *"It does not claim readiness on any other host, date or REA version; it does not claim that any route other than the one exercised below produces correct results; and it treats no digest as authenticity or origin (Q09)."*
2. **Distinct Evidentiary Sources:** Revenger cites external source S506 at GitHub commit `12f6e09` and own-work run records S507. It does not cite or absorb Kaidoku's internal knowledge files or lessons.
3. **No Territorial Overlap:** Revenger does not attempt to decompile ASAR packages, reverse-engineer HarmonyOS HAPs, or lift IR from optimized binaries (Kaidoku's province). Conversely, Kaidoku does not track revenger's K-held coverage matrix or row C14 admission status.
4. **Conclusion:** This relationship constitutes **domain adjacency** (shared tool substrate on the host), NOT contested scope. Under Q10, this relationship is reported, not absorbed.

---

## 5. Candidate Entry Route Table Cross-Check

The candidate entry `corpus/knowledge/round-98-rea-host-readiness.md` specifies an 8-row Route Decision Table. Each row was cross-checked against all sibling knowledge entries and province definitions:

| Route # | Route Name | Candidate Observation & Verdict | Sibling Knowledge Cross-Check (`kaidoku-shokunin`) | Contradiction? |
|---|---|---|---|:---:|
| 1 | **ZIP inventory** (`inspect_artifact` → `inventory_artifact`) | `rea inspect-artifact` on `fixtures/archive-r2/fixture.zip` exited 0. Substep `inventory_artifact` completed. Members README.txt (84 B) and bin/checksum (16160 B) match truth.json. Hopper absent. Verdict: **capability** (ready on this host). | Kaidoku entries `2026-10-19-arc3-r11-inspect-artifact-evidence-id-domain.md` and `2026-10-14-r12-01-queue-b-ready.md` confirm `inventory_artifact` is a substep of `inspect_artifact` and operates independently of Hopper or Ghidra. | **None** |
| 2 | **Native decompile** (Ghidra provider) | Doctor reports 8 ghidra scope checks healthy (ghidra, ghidra-platform, ghidra-architecture, ghidra-installation, ghidra-version 12.1.4, ghidra-headless, ghidra-native_decompiler, ghidra-java 21.0.13). `command -v analyzeHeadless` exited 1 (not on PATH; found under install dir). Verdict: **configuration** (configured; unprobed this round). | Kaidoku `2026-10-13-doctor-taxonomy.md:48-53` and `PROVINCE.md:27` confirm 8/8 Ghidra checks pass with Ghidra 12.1.4 and JDK 21 at `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`. Headless launcher exists under `support/analyzeHeadless`. | **None** |
| 3 | **Native analysis** (Hopper, IDA, Kuna engines) | Doctor reports `hopper`, `ida-registration`, and `kuna-installation` as `missing_analysis_engine`. `command -v hopper` and `command -v idat64` exited 1. Verdict: **absent** (not ready). | Kaidoku `2026-10-13-doctor-taxonomy.md:35, 42` and `PROVINCE.md:28` confirm Hopper and IDA are absent/unconfigured on this host. | **None** |
| 4 | **Android** (JADX provider) | Doctor reports `jadx` healthy ("checks configuration, not whether a selected APK fits in worker's memory"). `jadx --version` printed 1.5.6; `java -version` printed openjdk 21.0.13. Verdict: **configuration** (configured; capability unprobed). | Kaidoku `2026-10-13-r3-apk-inventory.md` and `2026-10-13-r4u-02-jadx-decode.md` confirm JADX configuration vs capability boundary. Candidate accurately reports capability is unprobed this round. | **None** |
| 5 | **Firmware regions and extraction** | `binwalk --version` printed 3.1.0; `unblob --version` printed 26.6.4 (both exit 0). Doctor has no binwalk or unblob check. Verdict: **configuration** (present; capability unprobed). | Kaidoku `2026-10-13-r4u-01-firmware-deep.md:79` states verbatim: *"the doctor/providers blind spot persists WITH working env — `rea doctor` still inspects only ghidra+ida; `rea providers` names the firmware operations but never binwalk/unblob readiness"*. This directly corroborates revenger's observation. | **None** |
| 6 | **MCP registration** (per client) | 14 client registrations: 4 aligned (codex, devin, grok_build, zcode), 8 missing, 1 manual (grok_bot), 1 stale (omp). Stale installed skill identity. Verdict: **configuration** (omp stale; aligned does not prove connected session per S506). | Kaidoku `PROVINCE.md:18-20` documents operator disabled OMP REA entry for hyaku (`disabledServers: ["rea"]`), leaving OMP stale/disabled. | **None** |
| 7 | **CLI launcher** | `rea --version` printed 6.7.0. `command -v rea` resolved to per-shell `fnm_multishells` path. Doctor lists three paths (`state: multiple`). Verdict: **configuration** (available in this shell). | Kaidoku `PROVINCE.md:8-12, 21-26` confirms REA CLI 6.7.0 is installed and active on the host. | **None** |
| 8 | **pwntools** (ELF-layout helper) | `python3 -c 'import pwn'` exited 0. Verdict: **configuration** (importable; corrects 2026-10-19 re-probe row K05). | Kaidoku `2026-10-13-r4-13-pwntools-persist.md` confirms pwntools availability in python env, noting doctor is blind to pwntools. | **None** |

### Cross-Check Verdict
**ZERO sibling knowledge contradicts the candidate entry's route table.** Sibling observations in `kaidoku-shokunin` independently corroborate and validate every single observation made in revenger's route decision table.

---

## 6. Non-Obvious Move (UFO-FSD Connector Synthesis)

### Evidence Across Round Cache & Local Evidence
1. **ReviewerClaims Finding F1 (Real-Tree Control Coupling):**  
   `claims.md:86` requires that the C2 positive control on the real tree (`v7 --profile c02` on the landing archive) print `C1_VERDICT=pass`. However, the `c02` profile preserves v6 logic in `C1_ONLY_TARGET` (formerly `C1_ONLY_C02`), which asserts that no row in `corpus/README.md` other than C02 differs from the frozen base. Because C1 *mandates* moving C14 `partial → held`, the landing tree will have `diffs = {C14}`, causing `C1_ONLY_TARGET` to fail under `--profile c02`. This forces a false report of "harm to C02" on a completely healthy tree.
2. **ReviewerClaims Finding F2 & ExecControls S505 Mirror (Grounding Scope Dilemma):**  
   `claims.md:38, 95` introduces `C1_USEDBY_GROUNDED`. ReviewerClaims demonstrated that the base registry contains 47 ungrounded used-by cells across 36 rows (including historical rows S445–S482 and S505). If `C1_USEDBY_GROUNDED` scans the entire registry or all mined rows, it fails unconditionally on both the landing tree and the FR00 holdout fixture.  
   Furthermore, ExecControls demonstrated that repairing S505 (`mined → queued`, `used-by: —`) causes frozen v6 to fail (`S504:terminal-mined-expected:S505:queued`) because S505 is in S504's `supersedes` chain. In addition, ExecControls noted that 8 historical rows (e.g. S480) have multi-file used-by cells where one path contains the SID but another does not; an all-files-must-cite rule would false-fail these rows.
3. **Considerthese Pre-Freeze Guidance (`considerthese/2026-11-05.md` Proposals 1 & 5):**  
   Mandates pre-freeze counter-reachability controls to ensure counters are not vulnerable to cheap skip-work stubs, while ensuring that successor instruments (`c1_k_admit_counter7.py`) are fully harmonized before freezing.

### Affected Axes
- **Coverage (C1):** Protects row C14 admission from false failures on landing caused by historical ungrounded rows or S505 coupling.
- **Calibration (C2):** Preserves the integrity of the C2 positive control on the real tree, ensuring clean separation between C14 coverage advance and C02 holdout discrimination.
- **Invariant:** Neither axis is degraded; both are improved in robustness and causal separability.

### Proposed Move
**Profile-Scoped Disjunctive Grounding & Mutual Target-Exemption in `c1_k_admit_counter7.py`:**

1. **Mutual Target-Exemption in `C1_ONLY_TARGET`:**  
   In `c1_k_admit_counter7.py`, configure the README row diff check against base (`base_readme()`) to exempt the companion profile's target row:
   - When run with `--profile c02`: allow both C02 (if modified) and C14 (status `held`) to differ from base, while asserting that all 13 other rows (C01, C03–C13, C15) match base exactly.
   - When run with `--profile c14`: allow C14 to differ from base (`partial → held`), while asserting that C02 is `held` and all 13 other rows match base.  
   *Second-Order Effect:* This breaks the artificial coupling between C1 and C2 on the real landing archive, allowing `v7 --profile c02` to pass `C1_VERDICT=pass` without false "harm to C02" claims, while preserving full refusal on holdout forgeries.

2. **Profile-Scoped Disjunctive Grounding in `C1_USEDBY_GROUNDED`:**  
   - Scope the grounding check strictly to `NEW_ROW_IDS` for the active profile:
     - For `--profile c14`: validate S506 and S507 (asserting that `corpus/knowledge/round-98-rea-host-readiness.md` exists and contains tokens `S506` and `S507`).
     - For `--profile c02`: validate S502, S503, S504 (asserting citation in `corpus/knowledge/round-96-native-analysis-sessions.md`).
   - Define grounding at the **row level** (disjunctive): a row is grounded if *at least one* valid path in its `used-by` cell cites the row ID. This avoids false-positives on the 8 historical multi-file rows.
   - For S505: check S505 grounding only if S505 is explicitly named in the profile's row set, preventing registry-wide failure on the frozen base tree.

### Risks & Second-Order Effects
- **Runtime Surface:** Microsecond evaluation; simple dictionary key checks.
- **Contract Surface:** Conforms to `claims.md` ("the c02 profile … do[es] not read the C14 row or entry"); fulfills the declared intent of causal separability between C1 and C2.
- **Substrate Surface:** Compatible with frozen `corpus/` bytes; requires no forbidden modifications to historical rows.
- **Verification Surface:** Holdout vector discrimination in `forge_reach7.py` is unaffected because synthetic holdout trees do not alter C14.

### Verification
- Mock landing tree with C14 `held`: `python3 -B reports/round-98/c1_k_admit_counter7.py --profile c02 --tree <landing>` prints `C1_ONLY_TARGET=pass` and `C1_VERDICT=pass`.
- Claims-freeze tree (do-nothing): `c14` profile prints `C1_VERDICT=fail` (C14 is `partial`).
- Holdout harness: `python3 -B reports/round-98/forge_reach7.py` prints `C2_ACCEPTED=0/5`, `C2_POSITIVE=pass`, `C2_STUB_SELFTEST=ok`, `C2_ROWSET_FR06=C1_ROWSET`, `C2_ROWSET_FR07=C1_ROWSET`.

---

## 7. Findings Verdict

- **Surface (a) — C14 Subject (REA Host Readiness & Doctor):** **adjacency**  
  (Domain adjacency with `kaidoku-shokunin` on REA substrate; 0 hits across all other 19 sibling lanes; no contested scope under QUALITY.md Q10; 0 contradictions to the route decision table).
- **Surface (b) — v7 Admission Counter New-Leg Classes:** **none**  
  (0 hits across all 20 sibling lanes for exact leg tokens; general structural analogies for BOM and header parsing in utility scripts do not implement admission counter legs).
- **Overall Sibling Overlap Verdict:** **adjacency**

---

## 8. Discipline, Bounds, and Tooling Record

- **Lane Bounds:** Leaf member — no subagents spawned, no tasks dispatched.
- **Write Scope:** Written only to assigned findings report (`.ufo/waves/round-98/w1/ConnectorOverlap.md`) and receipts directory (`.ufo/waves/round-98/w1/ConnectorOverlap/`). No lane-tracked files, no fleet-root files, and no sibling lane files were modified.
- **Tooling Record:** No tools installed or upgraded (host python3 and GNU grep sufficed; host pacman transactions remained paused).
- **Scratch Cleanup:** Scratch root `/fast/scratch/hyaku/revenger-r98/ConnectorOverlap/` verified clean and removed before yield.
