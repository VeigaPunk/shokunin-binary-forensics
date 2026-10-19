# Sibling Overlap and Connection Scan — kaika-r1

**Author:** `RevConnector` (L2 UFO-FSD connector)  
**Date:** 2026-10-19  
**Worktree:** `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin`  
**Target:** Sibling overlap, contested boundaries, and evidence-id reconciliation for round-1 planned knowledge entries.

---

## 1. Sibling Overlap Table

| Planned Topic / Surface | Sibling Path:Line | Overlap Kind | Recommendation |
|---|---|---|---|
| **(a) Tool validation by function and version** (SWGDE 18-Q-001, NIST CFTT) → map row C12 | Siblings: None (`corpus/`, `SKILL.md`, `PROVINCE.md`).<br>Fleet reference: `fleet-ledger/.ufo/waves/kaika-w1/revenger-art.md:39,74,101` | **none** | **cite** — Revenger owns C12 tool validation against known truth; cite SWGDE 18-Q-001-2.1 and NIST CFTT report methodology. |
| **(b) Digest scope vs. provenance** (FIPS 180-4, SWGDE acquisition verification) → map row C13 | `kotodama-shokunin/corpus/knowledge/verification/generated-artifact-roundtrip-verification.md:15`<br>Fleet reference: `fleet-ledger/.ufo/waves/kaika-w1/revenger-art.md:43,65,106` | **same source** (FIPS 180-4);<br>**none** (SWGDE acquisition verification) | **cite** — Cite FIPS 180-4 for cryptographic hash specification and SWGDE 17-F-002-2.1 for acquisition verification limits. Differentiate from Kotodama's roundtrip determinism use. |
| **(c) PE `.rsrc` resource directory layout** (Microsoft PE format spec) → map row C01 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r2-pe-e2e-proof.md:45,100`<br>`kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-pe-arm64.md:24`<br>`kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-12-godot-arm64-scale.md:29,68`<br>`game-dev-2d-shokunin/corpus/live/r101-ver11/scratch/freshB/out/fixture.pck:1` | **contested scope** (Kaidoku PE inspection vs. Revenger format oracle);<br>**none** (GameDev2D Godot RSRC magic) | **report to integrator** / **cite** — Report the shared shipped-artifact PE boundary to protocol integrator per ADJ-06; cite Microsoft PE spec for internal 3-level tree layout (`IMAGE_RESOURCE_DIRECTORY`). |
| **(d) UTF-16 unpaired surrogates** (Unicode Standard ch.3) and REA acceptance of `A=\ude00B!` (r59) → map row C11 | `audio-shokunin/corpus/live/r62-boundary/src/decode.c:928`<br>`kaidoku-shokunin` MCP tool descriptors (`annotate_native_function`, `inspect_managed_members`)<br>Fleet reference: `fleet-ledger/.ufo/waves/kaika-w1/revenger-state.md:69,99` | **same source** (Unicode D800..DFFF range);<br>**none** (no sibling knowledge entry covers PE name surrogate acceptance) | **cite** — Cite Unicode Standard 18.0.0 ch. 3 (D71–D91) for ill-formed isolated surrogates; cite revenger historical Evidence `ev_8ab30e10…` for REA non-refusal behavior. |
| **Contested Province: Shipped-artifact RE** | `kaidoku-shokunin/PROVINCE.md:3-7`<br>`tsukuroi-shokunin/PROVINCE.md:42`<br>`tsukuroi-shokunin/corpus/knowledge/adjacency-handoffs-fleet-r1.md:54`<br>Fleet: `.ufo/l0-questions.md:42` | **contested scope** | **report to integrator** — Tsukuroi filed ADJ-06 regarding unresolved Kaidoku/Revenger ownership of shipped-artifact RE. Must not unilaterally absorb. |
| **Evidence-ID Identity: Universal vs. Family-scoped** | `kaidoku-shokunin/SKILL.md:331-335`<br>`kaidoku-shokunin/corpus/QUALITY.md:25` (rule 15)<br>`kaidoku-shokunin/corpus/knowledge/2026-10-14-r9-02-queue-a-ops-2.md:146-169`<br>Fleet: `MANIFEST.json:2782` | **same claim / contradiction** | **defer / cite correction** — Kaidoku disproved the universal `f(content, path, params)` claim; Revenger's uncorrected text in `LOG.md:720` and `SCORECARD.md:135` should be superseded in C10/C13 entries. |

---

## 2. Absence Claims and Exact Grep Sweep Commands

All absence claims below were executed across all sibling checkouts and worktrees (`/home/vgpnk/Projects/shokunin/*-shokunin/` and `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin/`):

1. **SWGDE Absence in Siblings:**
   - **Command:**
     ```sh
     grep -rn -i "SWGDE" /home/vgpnk/Projects/shokunin/*-shokunin/{corpus,SKILL.md,PROVINCE.md} /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin/{corpus,SKILL.md,PROVINCE.md} 2>/dev/null | grep -v "revenger-shokunin"
     ```
   - **Result:** Exit 1 (0 matches). Zero sibling holds or cites SWGDE forensic documents. Only Revenger references SWGDE (`corpus/README.md:61` and fleet `revenger-art.md`).

2. **CFTT Absence in Siblings:**
   - **Command:**
     ```sh
     grep -rn -i "CFTT" /home/vgpnk/Projects/shokunin/*-shokunin/{corpus,SKILL.md,PROVINCE.md} /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin/{corpus,SKILL.md,PROVINCE.md} 2>/dev/null | grep -v "revenger-shokunin"
     ```
   - **Result:** Exit 1 (0 matches). No sibling corpus or skill mentions NIST Computer Forensic Tool Testing (CFTT).

3. **PE Format Specification (`pe-format`) Absence in Siblings:**
   - **Command:**
     ```sh
     grep -rn -i "pe-format" /home/vgpnk/Projects/shokunin/*-shokunin/{corpus,SKILL.md,PROVINCE.md} /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin/{corpus,SKILL.md,PROVINCE.md} 2>/dev/null | grep -v "revenger-shokunin"
     ```
   - **Result:** Exit 1 (0 matches). No sibling cites the Microsoft PE/COFF specification URL or doc identifier.

4. **Unicode Surrogate Knowledge Entry Absence in Siblings:**
   - **Command:**
     ```sh
     grep -rn -i "surrogate" /home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge/ /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin/corpus/knowledge/ 2>/dev/null | grep -v "revenger-shokunin"
     ```
   - **Result:** Exit 1 (0 matches). Sibling occurrences are restricted to C source parsing in audio (`decode.c:928`), Godot binary export strings in game-dev-2d, and REA tool help schemas in Kaidoku receipts. No sibling has authored a knowledge entry on UTF-16 surrogates in artifact metadata or parser acceptance/refusal boundaries.

5. **Sibling `corpus/SOURCES.md` Absence:**
   - **Command:**
     ```sh
     ls -d /home/vgpnk/Projects/shokunin/*-shokunin/corpus/SOURCES.md /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin/corpus/SOURCES.md 2>/dev/null
     ```
   - **Result:** Exit 1 (0 files found). `corpus/SOURCES.md` is a contract v1 introduction in fleet round kaika (`SOURCES-CONTRACT-v1.md`); no sibling worktree currently carries a committed `SOURCES.md`.

---

## 3. Contested Scope Analysis: Shipped-Artifact RE and Tsukuroi ADJ-06

1. **The Shared Domain Declaration:**
   - `revenger-shokunin/PROVINCE.md:3`: `Domain: reverse engineering of shipped artifacts under an evidence-ledger discipline`.
   - `kaidoku-shokunin/PROVINCE.md:3`: `Domain: reverse engineering of shipped artifacts with REA on this Linux host`.
   Both lanes declare the core domain of reverse engineering shipped artifacts using REA.

2. **The Adjudication Filing (ADJ-06):**
   - Tsukuroi identified this overlap during fleet round-1 and filed an unresolved handoff in `tsukuroi-shokunin/PROVINCE.md:42`:
     > "ADJ-06 | Driver/firmware/package mechanism requires shipped-artifact reverse engineering beyond health inventory ... protocol integrator — kaidoku/revenger ownership unresolved ... Request an ownership ruling before any RE work; do not invoke a target or forward raw cores | `../kaidoku-shokunin/PROVINCE.md:3-6,88-100`; `../revenger-shokunin/PROVINCE.md:3-7,19-25`"
   - Corroborated by `tsukuroi-shokunin/corpus/knowledge/adjacency-handoffs-fleet-r1.md:54` and fleet question `.ufo/l0-questions.md:42`.

3. **Demarcation Recommendation:**
   - **Revenger's Ground:** Internal byte-level artifact structure and byte oracles (e.g. PE `.rsrc` directory tree layout, section table alignment, UTF-16 LE encoding edge cases, icon group structures, forged-claim rejection gates, and forensic ledger standards).
   - **Kaidoku's Ground:** REA server operations, external provider binding and lifecycle (Ghidra headless timeouts/memory caps, wakaru execution limits, pwntools persistence, EVM/ASAR tool paging, and provider comparison).
   - **Action:** Report the ADJ-06 line to the protocol integrator; do not attempt to absorb general binary RE without an integrator ruling.

---

## 4. Evidence-ID Identity: Kaidoku Adjudication vs. Revenger Phrasing

1. **Kaidoku's Luna-Round-3 Adjudication (`MANIFEST.json:2782`):**
   - Kaidoku removed the false universal rule `"evidence ids are f(content, path, params)"` from its active surface (`SKILL.md:331-335`, `corpus/QUALITY.md:25` rule 15).
   - Primary evidence showed:
     - For `analyze`, `inspect`, and `analyze_function` (Ghidra provider), the ID hashes analysis content and parameters; it does **not** hash path. Identical bytes at two different paths yield identical `evidence_id` (`corpus/knowledge/2026-10-14-r9-02-queue-a-ops-2.md:146-169`).
     - For the `revenger-verifier` family (`inspect-pe-resources`, `inspect-evidence-bundle`), the semantic projection embeds `parameters.path` or `local_path`, making the ID **path-sensitive**.
     - Jadx is per-run (mints fresh temp paths).
     - Apktool is deterministic.

2. **Revenger's Uncorrected Historical Phrasing:**
   - In `LOG.md:720` (round 60):
     `DISCOVERED: evidence_id is path-sensitive (same bytes elsewhere → ev_50038b96…) — ev = f(content, path, params).`
   - In `SCORECARD.md:135` (planned section):
     `evidence_id confirmed path-sensitive (content+path+params)`
   - **Status:** Uncorrected. Revenger has preserved this universal formulation from its imported round 60.

3. **Reconciliation Recommendation:**
   - Leave `LOG.md:720` untouched as an immutable, append-only historical record.
   - For C10 (evidence-ledger discipline) and C13 (digest scope vs provenance), adopt the **family-scoped** rule: state explicitly that path-sensitivity is a property of the `inspect-pe-resources` semantic projection, not a universal law of all REA tools.

---

## 5. Candidate Sibling `SOURCES.md` Rows to Cross-Reference

While sibling checkouts have not yet committed `corpus/SOURCES.md`, the fleet ledger retains candidate rows opened in sibling ART dossiers (`.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/`) that Revenger can cross-reference:

1. **From `kaidoku-art.md`:**
   - `S028` (LIEF, PE Support Enhancements: ARM64EC/ARM64X — `https://lief.re/blog/2025-02-16-arm64ec-pe-support/`): Authoritative tier A reference on PE dynamic relocations, CHPE metadata, and exception-directory structure; relevant to Revenger's C01 PE format frontier.
   - `S022` (Electron ASAR Integrity — `https://www.electronjs.org/docs/latest/tutorial/asar-integrity`): Tier A documentation on ASAR header integrity and SHA-256 block hash verification; relevant to C04/C13.
   - `S020` (Electron Fuses — `https://www.electronjs.org/docs/latest/tutorial/fuses`): Authoritative wire format and sentinel byte decoding; relevant to C04.

2. **From `chousa-art.md`:**
   - `S010` (Cited but Not Verified: Parsing and Evaluating Source Attribution — `https://arxiv.org/html/2605.06635v1`): Distinguishes URL access from topical relevance and factual support; reinforces Revenger's C13 provenance discipline.
   - `S026` (Cochrane MECIR C52-C60: Assessing Risk of Bias — `https://www.cochrane.org/authors/handbooks-and-manuals/mecir-manual/...`): Authoritative standard on independent duplicate judgments; grounds Revenger's non-author review gate.

3. **From `tameshi-art.md`:**
   - `S002` (Mutation Testing Report Schema — `https://raw.githubusercontent.com/stryker-mutator/.../mutation-testing-report-schema.json`): Cross-tool report schema with explicit status enums; model for structured evidence ledgers.
   - `S012` (Oracles That Cannot Fail — `https://arxiv.org/abs/2608.17214`): Formulates state-anchored oracle failure modes; directly relevant to Revenger's C12 calibration strategy and byte-oracle verification.
   - `S028` (Bazel Test Encyclopedia — `https://bazel.build/reference/test-encyclopedia`): Normative hermetic test contract; reinforces Revenger's fixture replay isolation.

---

## 6. Proposed Move: UFO-FSD Synthesis

### Evidence
- Revenger's planned entries C12 (SWGDE/CFTT) and C13 (FIPS 180-4 / provenance) address evidence-ledger discipline and tool calibration (`corpus/README.md:37-38`).
- Kaidoku adjudicated that `evidence_id` identity is verb-family-specific (`MANIFEST.json:2782`, `QUALITY.md:25`), while Revenger retains the superseded universal claim `ev = f(content, path, params)` in `LOG.md:720` and `SCORECARD.md:135`.
- Tsukuroi ADJ-06 remains an active unresolved question at the protocol level (`.ufo/l0-questions.md:42`).

### Affected Axes
- **Coverage (+):** Incorporates C10/C13 domain knowledge on evidence-ledger identity domains.
- **Calibration (+):** Aligns Revenger's evidence-ledger claims with empirical multi-lane ground truth, eliminating false universal claims.
- **Freshness / Depth (0):** Leaves existing verifiers and historical records intact without regressions.

### Proposed Move
When admitting `corpus/knowledge/digest-scope-versus-provenance.md` (C13) and formulating the future C10 evidence-ledger entry, explicitly specify the **family-scoped evidence-id domain**:
1. Declare that for `inspect-pe-resources`, `evidence_id` is path-sensitive because `parameters.path` is included in the semantic projection.
2. Formally recognize Kaidoku's finding that `analyze_function` / Ghidra native analysis is content+params-keyed.
3. In `SCORECARD.md`'s planned section, annotate the historical r60 entry with a pointer to the family-scoped correction, without rewriting append-only `LOG.md`.

### Risks
- *Risk:* Over-extending Revenger's scope into Kaidoku's analysis tools.
- *Mitigation:* Revenger tests and claims path-sensitivity only over its own PE fixture tools (`inspect-pe-resources`); cites Kaidoku's `2026-10-14-r9-02-queue-a-ops-2.md` as external evidence for the wider verb family.

### Verification
- Census of `f(content, path, params)` in active text:
  ```sh
  grep -n "f(content, path, params)" corpus/README.md corpus/QUALITY.md corpus/knowledge/*.md
  ```
  Must yield 0 hits in new knowledge entries.
- Verification that all four verifiers reject path forgeries while maintaining byte-level determinism.
