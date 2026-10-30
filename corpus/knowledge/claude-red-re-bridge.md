source: S050 — Claude-Red `SECURITY.md` (https://raw.githubusercontent.com/SnailSploit/Claude-Red/main/SECURITY.md), `## Intended Use` and `## Scope`; S051 — `offensive-reporting` (https://raw.githubusercontent.com/SnailSploit/Claude-Red/main/Skills/utility/offensive-reporting/SKILL.md), `## Quick Workflow` / `## Report Structure (Standard)`; REA/format/fuzzing leads in `reports/round-73/claude-red-source-leads.md` remain unopened registry candidates.
verified-at: 2026-10-29 — source scope checked against the local Claude-Red checkout and existing S050/S051 snapshots; other lead URLs screened, not admitted.
recheck: Re-open selected source in a gated round, pin version/commit and exact quote; recheck exact individual skills/primary source anchors before making any load-bearing claim.
coverage-map: C12/C15 (method/source map only; does not fill an uncovered technical coverage row).
admission-status: candidate

# Claude-Red ↔ revenger: province-safe bridge

## Scope

A proposal for using Claude-Red as a **workflow-shape donor**, not as an RE authority or a new library of operational methods. The broad Claude-Red collection remains rejected as a revenger source (S074); S050 is a policy source and S051 is a tier-C reporting lead. For a technical RE claim, select and open the relevant specification, project documentation, authored fixture or tool output independently.

Revenger owns static analysis of shipped artifacts and specifically bounded, authorized local evidence. The useful connection is the discipline of structuring a triage: preserve an input, record output, name an error/class hypothesis, compare with independent evidence, mark unknowns, and communicate bounded findings. It does **not** authorize fuzzing third-party targets, exploit construction, payload development, live device or process access, mitigation bypass, C2, anti-forensics, or vulnerability disclosure outside an explicit program channel.

## Safe method-transfer table

| Claude-Red area | Keep as a workflow prompt | Independent technical evidence needed | Exclude / route elsewhere |
|---|---|---|---|
| Crash analysis | Preserve crash input and exact analyzer/debugger output; separate observed fault fields from root-cause hypotheses; deduplicate only with a stated key. | ASan/GDB/WinDbg documentation for a precise output interpretation; the input bytes; bounded, authored local fixture; independent byte/static analysis. | Exploitability ranking, exploit PoC, weaponization, debugging a third-party target. |
| Fuzzing | On authored test code, retain harness identity, corpus seed, tool/version, run limits and crash artifact; turn each crash into a falsifiable parser hypothesis. | Fuzzer primary docs, harness source, fixture hash and generated crash input, exact local command/output. | Fuzzing undeclared targets, service endpoints, vendor products or production devices. |
| Mitigations | Treat metadata bits as a static *presence indication*; record the exact field and binary version. | Format/OS primary documentation for the field; byte-derived field value; authored fixture control. | Bypass instructions, exploit chains, runtime probing of unowned systems. |
| Firmware/IoT | Limit to a caller-supplied firmware file: identify candidate offsets/types, recursively inventory extracts, retain the tool report and byte ranges. | REA route docs and exact Binwalk/Unblob versions; authored image and independent byte oracle. | PCB inspection, UART/JTAG, credentials, bootloader drops, network pivots, executing extracted files. |
| Mobile | Static APK member/manifest/DEX/resource inventory; note a decompiler's unknowns instead of treating output as source. | AOSP format references and byte-derived fields; static tool output on a local authored APK. | Installing or instrumenting real apps/devices, Frida hooks, pinning bypass, backend interaction. |
| Vulnerability classes | Use taxonomy names only as provisional labels for a static pattern, never as findings by themselves. | A primary spec or source for the exact behavior; independent reproduction on an authored fixture is required before cause claims. | CVE exploitation procedure, attack chains, unsourced severity/impact assertions. |
| Report structure | Keep sections for scope, artifact identity, method, observations, inference, unknowns, impact and disclosure. S051 is corroborative only. | The lane's Q01–Q16 and validator/gate; each report observation must bind to its own evidence. | Replacing lane gates with Claude-Red checklist; publishing or disclosing outside program channels. |

## Resource shortlist

The unopened source leads and exact short quotes are kept in `reports/round-73/claude-red-source-leads.md`, to prevent an unadmitted candidate from being mistaken for corpus knowledge. Highest signal for a future local parser-analysis round:

1. **PolyTracker** — tracks which input bytes are operated on by which functions; directly bridges fuzz/crash triage with byte-level provenance.
2. **AddressSanitizer + libFuzzer** — useful only with authored/local code and retained reproducer inputs; documentation does not establish tool correctness or cause.
3. **Corkami's PE reality notes** — malformed PE loader behavior fixtures; coordinate with the binary-forensics source owner rather than duplicating format rows.
4. **Binwalk + Unblob** — firmware carve/extract scope for a byte-authored C07 fixture; the lane already has a firmware route and tool readiness material.
5. **Airbus QEMU internals blog** — uncommon emulation internals learning source; not evidence of emulation output or REA readiness.
6. **OWASP MASTG / Apktool** — static mobile learning leads, but likely redundant with existing S058/S059/S094 and the Android spec set.

The lead list flags cross-slice overlap: binary-format primaries, managed assembly, patch-diff tools, emulators and C05/C07 tool sources should be admitted by the corresponding round-73 owner, not duplicated here.

## Observation, inference, unknown

**Observation:** The lane's registry contains S050 (Claude-Red policy) and S051 (reporting skill, tier C); S074 rejects the entire offensive collection as exceeding the RE province. Claude-Red skills include crash triage, fuzzing, mitigation taxonomy, firmware and mobile workflow material.

**Inference:** A narrow translation of method discipline—especially crash-input preservation, output-vs-cause separation and report evidence hygiene—can improve artifact-first triage without adopting offensive execution workflows.

**Unknown:** This candidate admits no new source claim, does not test any fuzzer/parser/tool, does not demonstrate that a given mitigation bit has runtime effect, and does not establish the correctness of any Claude-Red skill. All resource leads must be reopened by a gated round and independently checked.

## Q-map (proposal only)

- Q01: **not yet passed** — new sources must be opened/entered in round and technical claims supported by tier-A scoped sources.
- Q02: **not yet passed** — the final source anchors and recheck command are round-dependent.
- Q03/Q04/Q05/Q06/Q07/Q08/Q09/Q10/Q11/Q12/Q13/Q14/Q15/Q16: no technical finding or tool output is claimed here; round gate must assess each criterion against the finalized entry.

## Boundary

No installation or runtime analysis was performed. This document is a candidate workflow map only; it is not a training instruction for exploitation, an authorization record, or an admission to `corpus/knowledge/`.