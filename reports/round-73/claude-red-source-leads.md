# Claude-Red-derived source leads (2026-10-29)

Curated leads only; not opened/admitted SOURCES rows. Keep S074 rejected; S050/S051 remain bounded sources. Each quote is a short source-origin quote (≤25 words); source refs are to the individual primary source, not the broad Claude-Red/offensive-checklist curriculum.

| Lead | URL | Exact quote (≤25 words) | Scope / transfer | Boundary |
|---|---|---|---|---|
| Crash triage: ASan | https://github.com/google/sanitizers/wiki/AddressSanitizer | “AddressSanitizer (ASan) is a fast memory error detector for C/C++.” | Interpret an ASan report as a crash observation; preserve location/error class and separate root-cause inference. | Own/authored fixtures only; report is not exploitability. |
| Crash triage: libFuzzer | https://llvm.org/docs/LibFuzzer.html | “LibFuzzer is an in-process, coverage-guided, evolutionary fuzzing engine.” | Produces reproducible crash inputs for artifact/parser analysis and corpus deduplication. | Fuzz only owned/authored targets; no third-party test campaigns. |
| Crash triage: AFL++ | https://aflplus.plus/ | “AFL++ is a security-oriented fuzzer” | Fuzzing as bounded instrumented input generation, then preserve corpus/crash inputs as evidence. | Not a license to target deployed software. |
| Fuzzing: LibAFL | https://github.com/AFLplusplus/LibAFL | “Advanced Fuzzing Library - Slot your own fuzzers together and extend their features using Rust.” | Lower-level reusable framework for constructing specific parser-fuzz research instruments. | Scope to local authored code and exact harness. |
| Fuzzing: Jackalope | https://github.com/googleprojectzero/Jackalope | “Jackalope is a customizable, distributed, coverage-guided fuzzer” | Windows binary fuzzing lead for future local authored-parser corpus only. | No live/vendor target execution. |
| Coverage/taint evidence: PolyTracker | https://github.com/trailofbits/polytracker | “track which bytes of an input file are operated on by which functions.” | High-signal bridge to byte-oriented evidence ledger: identify consumed input bytes, then distinguish runtime trace from semantic inference. | Instrumented execution only on owned test programs. |
| Crash corpus: Mesos | https://github.com/gamozolabs/mesos | “gather binary code coverage on all user-land Windows targets without need for source or recompilation” | Rare debugger-based coverage/crash-dump design; study how observations are generated. | Do not run against unowned targets; dynamic scope only. |
| Patch diff: ghidriff | https://github.com/clearbluejar/ghidriff | “find the added, deleted, and modified functions of two arbitrary binaries.” | Patch-diff observation as a way to select changed-function bytes for static review. | A diff is not root cause, vulnerability, or proof of behavior. |
| Patch diff: Diaphora | https://github.com/joxeankoret/diaphora | “Diaphora (διαφορά, Greek for 'difference') version 3.5 is the most advanced program diffing tool” | IDA plugin source for function/program diffing; useful as a workflow lead, not a superlative claim. | Quote is maintainer self-description; avoid repeating “most advanced” as fact. |
| Firmware static carve: Binwalk v3 | https://github.com/ReFirmLabs/binwalk | “Binwalk can identify, and optionally extract, files and data that have been embedded inside of other files.” | Firmware signature identification and carve planning; pair producer report with independent byte ranges. | Static authored images; extraction report does not establish authenticity or completeness. |
| Firmware static carve: unblob | https://github.com/onekey-sec/unblob | “unblob parses unknown binary blobs for 78+ archive, compression, and file-system formats, extracts their content recursively, and carves out unknown chunks.” | Recursive format/carve candidate for C07 firmware corpus, complementing current Binwalk readiness. | Treat nested files/ranges as producer observations; validate fixture bytes independently. |
| Firmware emulation literacy: Airbus QEMU internals | https://airbus-seclab.github.io/qemu_blog/ | “Creating a new machine” | Deep technical series on QEMU device/memory/execution internals, useful for understanding emulation boundaries when REA route is available. | Learning source only; no emulation claim or target interaction. |
| Mobile static scope: OWASP MASTG | https://github.com/OWASP/owasp-mastg | “The OWASP Mobile Application Security Testing Guide (MASTG) is a comprehensive manual for mobile app security testing and reverse engineering.” | Static mobile testing reference; use only static artifact-oriented portions for C05 curriculum. | The source covers more than revenger's static province; do not import live instrumentation techniques. |
| Mobile static artifacts: Apktool | https://github.com/iBotPeaches/Apktool | “A tool for reverse engineering Android apk files” | Decode APK resources/Smali for static inspection; compare output with APK bytes/spec. | Does not prove install validity, source recovery, or permission to modify. |
| Managed artifact taxonomy (if not already owned by another round-73 slice): .NET docs | https://learn.microsoft.com/en-us/dotnet/standard/assembly/ | “An assembly is a collection of types and resources that are built to work together” | Assemblies/metadata concepts supporting triage labels and declared-vs-recovered separation. | Binary-analysis ownership overlaps other round-73 slice; share lead only, don't duplicate row. |
| Mitigation state: PE load-config/CFG | https://learn.microsoft.com/en-us/windows/win32/debug/pe-format | “The Load Configuration Directory contains information about the image's security features.” | Static mitigation-presence fields as observations from PE metadata; use exact PE fields and fixture oracle. | Another slice owns PE format; avoid duplicate source row; no bypasses. |

## Claude-Red skill bridges (process patterns, not source rows)

- `offensive-crash-analysis`: reduce to crash-input → evidence fields → hypotheses; exclude exploitability assessment / PoC escalation.
- `offensive-fuzzing` and `offensive-fuzzing-course`: retain reproducible corpus, dedup and crash-preservation concepts; no live target.
- `offensive-mitigations` / `offensive-windows-mitigations`: retain static mitigation-*presence* inspection; exclude bypass instructions.
- `offensive-iot`: retain static firmware carving and file-system inventory; exclude physical access, bootloader access, credential discovery and runtime pivots.
- `offensive-mobile`: retain static APK/DEX/resource inspection only; exclude Frida/live-device and pinning bypass.
- `offensive-vuln-classes`: use class names as provisional labels/hypotheses only, not vulnerability findings.
- `offensive-bug-identification`: static triage ordering may inform workflow; exclude target recon and exploitation.
- `offensive-exploit-development`, `offensive-basic-exploitation`, `offensive-toctou`, `offensive-shellcode`, anti-forensics, EDR: route to kasegi; not revenger material.

## Prioritized shortlist for round author

1. **PolyTracker + ASan + libFuzzer** — most direct transfer to byte-level evidence / crash input traceability.
2. **Corkami PE + PolyTracker** — pair with binary-forensics slice if it needs static malformed-format fixtures; do not duplicate that lane's ownership.
3. **Binwalk + unblob** — C07 only if new authored firmware fixture is being studied; current known frontier already documents both tools.
4. **QEMU internals blog** — unusual, deep background; tier B/C learning source, not a source for runtime claims.
5. **MASTG/Apktool** — C05 only if C05 round is reopened; existing source set already includes MASTG and APK tooling, so likely no new row.
6. **ASan/libFuzzer/AFL++/Jackalope** — only if a future round adds an authored local parser harness; no need to add broad references without a concrete research claim.

All URLs were screened in this pass; project READMEs/pages were inspected for the short quotes above. Individual material is not yet admitted. Do not add generic S-IDs or quote unverified feature claims into SOURCES; round must reopen the selected source and record exact revision/anchor. No tools installed.