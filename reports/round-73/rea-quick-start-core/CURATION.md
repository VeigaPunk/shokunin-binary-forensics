> **Id note (2026-10-29, post-merge):** this pack's provisional ids S096–S108 were merged by REVENGER_SHOKUNIN into `corpus/SOURCES.md` as **S415–S426** (BinKit deduped — pcoderef already S132). Read every `S0xx` here via `reports/round-73/source-id-map.tsv` col2 `rea-quick-start:<old>`. Do not reuse S110–S122.

# REA quick-start core — curated sources for revenger corpus

Agent: `REA_quick_start_core` · opened 2026-10-29 · lane head `abe4276` · local REA checkout `12f6e09` (`rea-agents` package 6.7.0; npm latest 6.8.0).

Purpose: give revenger a ready-to-admit quick-start study path that connects
REA (morluto/rea) setup → first Evidence-backed investigation → calibration
against known-truth corpora, without trespassing on EvidenceLedger depth
(`REA_EvidenceLedger_impl`) or Claude-Red / binary-forensics slices.

Corpus gaps this pack targets: **C14** (host readiness), **C10** (evidence
discipline at the entry surface), **C02** (native sessions as readiness, not
provider method), **C04** (first JS/Electron investigation loop), and a
frontier bridge into **C12/C15** (tool/corpus validation).

Already admitted nearby rows (do not re-add): S001–S002 (host/skill), S075
(installation.md), S076 (mcp-prompts), S077/S095 (agent-env / WASM specs),
S078–S089 (courses/papers/catalogs from round 72).

## Axes (godspeed)

1. **Authority** — prefer REA first-party docs and pinned local skill files.
2. **Actionability** — each source unlocks a concrete next command or falsifier.
3. **Obscurity with leverage** — keep sources that change how claims are checked
   (p-code provenance, injected facts, compiler-variation corpora), not listicles.
4. **Non-harm** — no offensive procedure; no MCP re-enable on this CLI-first host.

## Recommended study path

`host contract → skill/CLI map → connection recovery → Evidence surface →
first JS analyze → mcp-contracts identity rules → native provider readiness →
p-code/scripting practice → known-truth corpora`

Concrete order (proposed Path for SOURCES.md once rows land):

```
REA quick-start core —
  S002 (skill declaration) → HOST-CONTRACT (this host) → cli-command-map →
  connection-and-recovery → evidence-workflows → cli.md →
  javascript-application-workflows → mcp-contracts →
  River Loop p-code PoC → GhidraSnippets → Ghidra P-Code Reference →
  BinKit → AUTOFACTS → Assemblage
```

## Tier-A opens (admit these)

### A1. Host CLI-first contract (own-work / docs)

| field | value |
|---|---|
| source | Host REA CLI-first contract — `~/.agents/skills/reverse-engineer-anything/HOST-CONTRACT.md` |
| kind / tier / scope | docs · A · this host's intentional MCP-off / CLI-on policy only |
| anchor | "The rule" + "State as of this writing"; sha256 `ab36b310…b58fe` |
| teaches | On this machine REA is CLI-first by operator choice; absent MCP tools are not a fault to "fix" with `setup`. |
| quote (≤25w) | "REA runs CLI-first on this host. The MCP server is off, deliberately." |
| why | S002 alone is incomplete: the installed `SKILL.md` was patched for CLI-first and doctor reports intentional `skill:identity` drift. |

Companion: `references/cli-command-map.md` (sha256 `83c4ec63…f32e48`) — maps MCP names to kebab CLI; generated from `rea-agents@6.7.0 --llms`.

### A2. Connection and task recovery

| field | value |
|---|---|
| source | REA skill reference — connection-and-recovery — local `references/connection-and-recovery.md` (upstream skill) |
| kind / tier | docs · A |
| scope | observed connection/approval/provider blockers and next steps; not general readiness |
| anchor | table row "No REA tools in the active session"; sha256 `a33760c8…66a2b1` |
| teaches | A skill install alone does not register MCP; diagnose with scoped `rea doctor --client … --json`. |
| quote | "A skill installation alone does not register MCP." |

### A3. Evidence workflows (entry surface)

| field | value |
|---|---|
| source | REA skill reference — evidence-workflows — local `references/evidence-workflows.md` |
| kind / tier | docs · A |
| scope | how agents read Evidence, page views, and when comparisons are allowed |
| anchor | opening + `verify_reconstruction` bullet; sha256 `2bdee98a…d5ab80` |
| teaches | Cite `evidence_id`; preserve limitations/coverage/unknowns; `verify_reconstruction` only covers declared comparable claims. |
| quote | "Evidence-producing tools return the complete Evidence record directly in MCP" |
| handoff | Deeper obligation-ledger / export semantics → `REA_EvidenceLedger_impl`. |

### A4. CLI Evidence contract

| field | value |
|---|---|
| source | REA CLI and Evidence — local checkout `docs/cli.md` @ `12f6e09` |
| kind / tier | docs · A |
| scope | CLI as same Evidence engine as MCP; save-then-project pattern |
| anchor | "CLI and Evidence" / "Run a command"; sha256 `fad0e2b6…ce92e6` |
| teaches | Each CLI invocation is a separate process; large JS Evidence must be saved and projected via `inspect-analysis-view`. |
| quote | "Each CLI invocation is a separate process; save results when you want to use them in a later command." |

### A5. First investigation loop (JS/Electron)

| field | value |
|---|---|
| source | REA JavaScript application workflows — `docs/javascript-application-workflows.md` @ `12f6e09` |
| kind / tier | docs · A |
| scope | authenticated Application Graph traces/comparisons; no native provider |
| anchor | opening paragraphs; sha256 `b2ea1ca7…da40cd` |
| teaches | Trace/compare tools consume completed `analyze_javascript_application` Evidence; they do not re-read the artifact or execute it. |
| quote | "REA derives a complete reachable feature trace from one authenticated JavaScript Application Graph" |

First command on this host (authorized targets only):

```bash
rea analyze-javascript-application /absolute/path/to/app --json > app-evidence.json
```

### A6. MCP runtime contracts (identity / paging)

| field | value |
|---|---|
| source | REA MCP runtime contracts — `docs/mcp-contracts.md` @ `12f6e09` |
| kind / tier | docs · A |
| scope | Evidence record fields, retained dossiers, coverage, integrity mismatch |
| anchor | "## Tool results"; sha256 `83596680…9a6655` (89832 bytes) |
| teaches | Read `structuredContent.normalized_result` + `evidence_id`; `analyze_function` defaults to summary Evidence whose parent holds the dossier. |
| quote | "Evidence-producing tools return the complete canonical Evidence record in both text and structured content." |

### A7. Obscure lever — River Loop p-code malloc provenance

| field | value |
|---|---|
| source | Working With Ghidra's P-Code To Identify Vulnerable Function Calls — https://riverloopsecurity.com/blog/2019/05/pcode/ |
| kind / tier | talk/docs · B (worked PoC with script+binary+source+output; not a vuln detector) |
| scope | backward p-code tracing of `malloc` size provenance as a reproducible method example |
| anchor | 2019-05-11 article; snapshot sha256 `a90a95ee…40ea70` |
| teaches | Lift to p-code, then follow `varnode` defs across calls; a PoC that finds provenance is not proof of exploitability. |
| quote | "My script leverages Ghidra's “p-code” intermediate representation to trace inputs to the malloc through functions and interprocedural calls." |
| why obscure+high leverage | Rarely in awesome-lists; supplies the exact script/test-binary/source/output loop REA agents need for native calibration once Ghidra is available. |

### A8. GhidraSnippets (API cookbook)

| field | value |
|---|---|
| source | HackOvert/GhidraSnippets — https://github.com/HackOvert/GhidraSnippets |
| kind / tier | code · B |
| scope | Flat Program / Flat Decompiler / Complex API examples only |
| anchor | README lede; commit oid observed in GitHub page `9bcd718e8958387ff5695194b83a52df4e0a3de7`; README sha256 `acf6c479…09c7f6` |
| teaches | Start on Flat APIs; leave Flat APIs when slicing/varnodes demand the Complex API. |
| quote | "There are three primary APIs covered here, the Flat Program API, the Flat Decompiler API, and everything else (\"Complex API\")." |

### A9. Ghidra P-Code Reference Manual

| field | value |
|---|---|
| source | NSA Ghidra P-Code Reference Manual — `GhidraDocs/languages/html/pcoderef.html` at tag `Ghidra_11.3.2_build` |
| kind / tier | docs · A |
| scope | processor-independent p-code operation semantics at that tag |
| anchor | title + "Last updated March 2, 2023"; sha256 `496b96e8…ed62d84` |
| teaches | Look up what a p-code op means instead of inferring from decompiled C. |
| quote | "P-Code Reference Manual" / "Last updated March 2, 2023" |

### A10. BinKit 2.0 (compiler-variation corpus)

| field | value |
|---|---|
| source | SoftSec-KAIST/BinKit — https://github.com/SoftSec-KAIST/BinKit |
| kind / tier | dataset · A (for its own stated BCSA benchmark counts) |
| scope | binary-similarity benchmark with declared arch/opt/compiler matrix |
| anchor | README "BinKit 2.0"; sha256 `586957cc…c979fb` |
| teaches | 1,904 compiler-option combinations / 371,928 binaries is the project's declared matrix for similarity survival tests — not REA accuracy. |
| quote | "The current dataset includes 1,904 distinct combinations of compiler options of 8 architectures, 6 optimization levels, and 23 compilers. It includes 371,928 binaries." |

### A11. AUTOFACTS (injected-fact ground truth)

| field | value |
|---|---|
| source | Towards Automatically Generating a Sound and Complete Dataset for Evaluating Static Analysis Tools — https://purs3lab.github.io/files/autofacts.pdf |
| kind / tier | paper · A |
| scope | synthetic fact injection into real programs; 29×72=2,088 binaries as authors state |
| anchor | Abstract; PDF sha256 `27f2fae4…03bcc9` |
| teaches | Evaluate analyzers on recovering known injected values at program points — problem-independent of the downstream RE task. |
| quote | "Our approach involves the injection of synthetic “facts” into a set of open-source programs, consisting of new variables and their possible values." |

### A12. Assemblage (source-connected corpus generator)

| field | value |
|---|---|
| source | Assemblage-Dataset/Assemblage — https://github.com/Assemblage-Dataset/Assemblage |
| kind / tier | dataset/code · A (for its own generator description) |
| scope | crawl/build/archive pipelines with function-level metadata |
| anchor | README lede; sha256 `473397f1…886d67b4` |
| teaches | Large labeled binaries with DWARF/PDB-style metadata are a different ground truth than AUTOFACTS injected facts or BinKit similarity pairs. |
| quote | "archives the resulting binaries with rich, function-level metadata — producing labeled training data for machine-learning approaches to binary analysis" |

## Tier-C / reject / park

| candidate | verdict | reason |
|---|---|---|
| Forks / mirrors of morluto/rea (`Nowng/rea-mcp`, `minibeta/morluto-rea`, …) | REJECT | Official distribution is `morluto/rea` + `rea-agents` npm + `rea.tools` (REA README IMPORTANT note). |
| Awesome-RE listicles as sole support | REJECT as tier A | Catalogs are discoverability only (matches S071/S072/S088 discipline). |
| Practical Reverse Engineering (Dang et al.) | LEAD (book) | Architecture foundation; contents not opened this pass. Pair later with A7–A9. |
| clearbluejar callgraph/pyhidra walkthrough | LEAD | Useful pipeline article; not opened byte-exact this pass. |
| `docs/reconstruction-obligation-ledgers.md` | DEFER | Owned by EvidenceLedger slice; CLI already exposes `build-reconstruction-obligation-ledger`. |
| Re-running `rea setup --client` on this host | NEVER | Violates HOST-CONTRACT; harms axis 4. |

## Search log (PRISMA-lite)

- **Question:** which opened sources make a shokunin-grade REA quick-start (setup → first Evidence → calibration) without duplicating round-72 catalog rows or ledger-impl depth?
- **Where:** local `~/.local/share/rea` @ `12f6e09`, local skill tree, `rea.tools`/`morluto/rea` docs, River Loop blog, HackOvert/GhidraSnippets, SoftSec-KAIST/BinKit, AUTOFACTS PDF, Assemblage README, Ghidra `pcoderef.html` @ `Ghidra_11.3.2_build`.
- **Date:** 2026-10-29.
- **Identified 18 / screened 16 / included 12 proposed rows (A1–A12) / excluded 6** (forks, awesome-lists as A, Practical RE unopened, clearbluejar unopened, obligation-ledgers deferred, setup-reenable refused).
- **Stop:** every quick-start claim has a local sha256 snapshot under `source-snapshots/`; obscure calibration trio (BinKit/AUTOFACTS/Assemblage) distinguishes three non-interchangeable ground truths.
- **Installs this agent:** none.

## Snapshots

All opened bytes and `SHA256SUMS` live in
`reports/round-73/rea-quick-start-core/source-snapshots/`.

## Suggested first knowledge entries (after SOURCES admit)

1. `knowledge/rea-cli-first-host-contract.md` — C14 correction of S002/readiness checklist against HOST-CONTRACT + doctor expected drift.
2. `knowledge/rea-first-js-evidence-loop.md` — C04/C10: analyze → save → `inspect-analysis-view` → cite `evidence_id` (fixture-bound).
3. `knowledge/rea-native-pcode-calibration-path.md` — C02/C12: River Loop PoC + GhidraSnippets + pcoderef as the method to validate native provider outputs once Ghidra is wired.

## Peer boundaries

- `REA_EvidenceLedger_impl` — export/import bundles, obligation ledgers, reconstruction coverage.
- `CLAUDE_RED_SKILLS` — offensive-skill technique library (already S050/S051 for bounty boundary).
- `SHOKUNIN_BINARY_FORENSICS` / `REVENGER_SHOKUNIN` — lane/repo layout; this pack only drops files under `reports/round-73/rea-quick-start-core/`.
- `KIMI_SHOKUNIN_INSTALL` — plugin install path; orthogonal.
