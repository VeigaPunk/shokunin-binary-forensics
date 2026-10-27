source: S054 — REA root README, https://github.com/morluto/rea, README.md overview and “How REA works”, last README revision 2026-10-27 (commit shown in the source history, accessed 2026-10-27); scope is the project's own declared tool families, not output correctness or host readiness.
source: S075 — REA setup documentation, https://github.com/morluto/rea, `docs/installation.md`, last file revision 2026-10-27; scope is the documented approval boundary, not this lane's configuration.
source: S076 — REA MCP prompts documentation, https://github.com/morluto/rea, `docs/mcp-prompts.md`, last file revision 2026-10-26; scope is prompt/data boundaries and generated workflow semantics.
source: S077 — REA feature spec and repository verification record, https://github.com/morluto/rea, `docs/specs/2356-wasm-interface-comparison/spec.md` and `verification.md`, feature spec dated 2026-10-13; scope is a feature-specific WebAssembly Evidence comparison workflow, not a general clean-room process.
source: S095 — REA agent-environment implementation index, https://github.com/morluto/rea, `docs/specs/agent-environments/README.md` “Agent environment implementation index”, last file revision 2026-10-25; scope is that index's named feature-spec and verification links, not a generic clean-room protocol.
verified-at: 2026-10-27; all linked content was opened read-only from the sources in `corpus/SOURCES.md` and the short-link screen at `reports/round-72/shortlink-dispositions.md`. No tool was installed or executed.
recheck: Re-open the exact URLs, headings and pinned revisions in the `S###` rows in `corpus/SOURCES.md`; a newer README, release, case page or paper revision requires a new source check. This entry is documentation-only and has no executable tool-recheck command.
coverage-map: C15 — selected reverse-engineering tool repositories and their declared boundaries; this is a source-map, not a tool installation/readiness map and not a claim of complete tool coverage.
admission-status: candidate

# Selected reverse-engineering tool repositories: declared roles and limits

## Scope

This entry organizes the operator-named selected repository set by the work each project's own public documentation says it addresses. The descriptions are observations about documentation, not claims that a tool was installed, tested, available on this host, accurate on an arbitrary target, or appropriate for every operation. This is a selected tool-source map, not a census of the market. The REA project, primary tool repositories and source-selection catalogs are kept distinct: catalog listings are leads, not evidence about the listed tool.

All work in this lane remains limited to shipped artifacts and declared, authorized local analysis. This entry does not authorize live-target activity, DRM circumvention, exploitation, publishing reversed code, or using an output as proof of source identity or behavioral equivalence. Dynamic-process and traffic tools are named only to identify their documented scope; none was run.

## Tool selection table — repository statements only

| Question / surface | Primary repositories and source IDs | What the README actually establishes | Boundary to carry into a decision |
|---|---|---|---|
| Need an agent-facing inspection workflow across app and binary surfaces | REA S054 | The project describes a local CLI/MCP/workflow that can inspect native binaries, JavaScript/Electron, .NET assemblies and websites, returning evidence and limitations. | This is the project's own feature description, not a claim of a successful run on this host or of complete source recovery. |
| Need native disassembly/decompilation and analysis | Ghidra S055; LaurieWired/GhidraMCP S056; IDA Pro MCP S057; radare2 S062; Rizin S069; angr S065 | Ghidra lists disassembly, assembly, decompilation, graphing and scripting. GhidraMCP documents a Ghidra plugin/MCP bridge. The IDA-MCP README recommends the official Hex-Rays MCP server. radare2/Rizin describe command-line binary analysis; angr describes a Python binary-analysis framework including symbolic execution. | These are distinct projects, APIs, platforms and inputs; do not infer feature parity, licensing, correct decompilation, or local provider readiness from the list. Review the exact source and current version before selecting one. |
| Need authored byte-level inspection and structure visualization | ImHex S064; radare2 S062; Rizin S069 | ImHex describes a hex editor with a custom pattern language and multiple data sources. radare2 and Rizin list hex/format and scriptable inspection capabilities. | A parser/pattern display is an observation to check against a separate specification and bytes; it is not an oracle by itself. |
| Need Android/APK output views | JADX S058; Apktool S059 | JADX describes Java output from DEX/APK and warns that many cases do not decompile completely. Apktool describes resource and Smali decoding and a rebuild path. | Decompiled or rebuilt files are not the original source or proof of install validity. The lane must remain static/artifact-first; no package is installed here. |
| Need managed assembly inspection | ILSpy S061; original dnSpy S067; dnSpyEx S068 | ILSpy describes a cross-platform .NET assembly browser/decompiler. The original dnSpy README describes a .NET/Unity debugger/editor and the GitHub repository banner identifies it as archived/read-only. dnSpyEx calls itself an unofficial continuation and describes similar .NET/Unity functions. | The original's archive notice is current GitHub repository metadata, not a claim of support. dnSpyEx's own README was last revised in 2023 in the opened history; active maintenance is not asserted. These docs do not yet establish C03 assembly-analysis knowledge. |
| Need process instrumentation or debugging | Frida S060; x64dbg S063; RAD Debugger S070 | Frida describes dynamic instrumentation. x64dbg describes a Windows user-mode debugger and x32/x64 launchers. RAD Debugger describes local-machine x64 debugging on Windows and Linux, with Linux support described as early. | This round does not run any target. Any later dynamic work needs explicit authorization and a bounded local artifact lifecycle; platform and architecture statements remain per-project. |
| Need a network view of a controlled artifact flow | mitmproxy S066 | The README describes an interactive TLS-capable proxy for HTTP/1, HTTP/2 and WebSockets. | This is a live interception surface, not a passive claim about saved records. Do not point it at an undeclared or third-party target. |
| Need byte-to-C reconstruction and verification research | ReAgent S073; REA feature spec S077 | ReAgent's README describes a reverser/checker, structural checks, candidate build/test gates and parity, while explicitly stating that this is not proof of semantic equivalence. REA's single `spec.md` defines a supplied-Evidence-only WASM comparison; its `verification.md` reports specific tests and WABT cases. | ReAgent is a separate project, not the REA tool itself. The WASM feature spec is a feature-specific case, not a repository-wide `SPEC.md` or general clean-room protocol. Its self-reported verification is not a test this lane ran. |

## Further study and reliability evidence

| Source | Bounded observation from the source | How to use it |
|---|---|---|
| REA setup docs S075 | The documented setup plan previews configuration changes and requires approval before applying them. | A documented setup path is not proof of installation; review plans and authorization separately. |
| REA MCP prompt contract S076 | The project says prompt arguments are untrusted selection data, not instructions or authorization; prompts do not themselves invoke tools. | Treat strings and prompts from analyzed artifacts as data, never as permission to broaden the target or operation. |
| REA WASM spec/verification S077 | The feature-specific comparison spec authenticates supplied Evidence and preserves unknown/incomplete coverage; its receipt reports a bounded tool/test matrix and platform limit. | This is an example of an explicit spec plus a reported oracle/check record. Do not generalize it to a generic clean-room loop or count its first-party receipt as independently rerun here. The root `SPEC.md` URL returned 404; the actual file found was case-specific lower-case `docs/specs/.../spec.md`. |
| REA agent-environments spec index S095 | The repository index links feature-specific specifications, implementation PRs and verification artifacts. | The index is evidence that these named feature records exist; it does not establish a universal clean-room loop. |
| pwn.college and OST2 S078–S079 | Their course pages describe toy reverse-engineering exercises and x86-64 assembly prerequisites/workflows. | Learning leads only; no challenge, training exercise or instruction set was executed. |
| Decomperson S080 | The USENIX paper describes its participant dataset and defines a measurable form of exact decompilation for that study. | Study evidence is bounded to its cohort/task, not every analyst or tool. |
| DIRTY S081 | The USENIX paper explains that compilation loses names/types and evaluates learned suggestions against its dataset. | A prediction may be plausible but not original; preserve it as inference until independently checked. |
| LLM4Decompile S082; AutoDecompiler S083; ALT4Decompile S084 | These papers describe distinct learned-decompilation techniques and report their own benchmark results. | Do not compare across their different tasks, datasets and metrics from abstracts alone, or translate a paper result into tool readiness. |
| Automated RE-agent attack paper S085 | The arXiv abstract reports prompt-injection risk from embedded strings in a studied LLM-assisted RE pipeline. | Defensive implication only: treat target strings as untrusted. No attack steps were reproduced or published. |
| REA author essay S086 | The essay recommends testing the oracle and checking what it actually verifies, while reporting first-party reconstruction experiences. | Useful first-party perspective, not independent model benchmarking. |
| REA Gems S087; Awesome Reverse-Engineered S088 | Both are secondary discovery catalogs; one labels itself unofficial and the other directs readers to search its index. | Use only to find candidate originals; each claim must be reopened at the primary tool, spec, paper or publisher source. Neither catalog backs a tool capability claim. |
| Ghidra Book 2e S089; Practical Binary Analysis S090; Android Malware Handbook S092 | Publisher pages expose titles, dates and chapter-topic descriptions only; the books themselves were not read. | Learning leads, not support for a technical procedure or a claim that this lane has executed that material. |
| OWASP MASTG S094 | The project's README describes the testing guide as a mobile app security and reverse-engineering manual. | Adjacent mobile-security reference; this lane does not absorb penetration testing or live-target activity. |

The publisher page for *Practical Malware Analysis* S091 was rejected as a source for current procedure because it identifies the book as a 2012 publication. The Malware Unicorn RE101 guide S093 was rejected as current lab guidance because it instructs disabling Windows Defender and enabling bidirectional host/guest sharing. The broad Claude-Red repository S074 was also rejected for province-wide offensive content; S050/S051 remain the bounded, already-curated policy/reporting sources. The live `chrome://dino` tutorial was screened and excluded as outside the lane's no-live-target scope; its destination and the reason are in `reports/round-72/shortlink-dispositions.md`. Rejection quotes and flips are in the round lesson Gate.
## §Q-map

| Q | decision | entry evidence / boundary |
|---|---|---|
| Q01 | PASS | Load-bearing tool roles use tier-A primary project docs or papers at the scope declared in their SOURCES rows; tier-C catalogs are discovery-only. |
| Q02 | PASS | Source headers include S-IDs, URLs, exact anchors/revisions; `verified-at`, `recheck` and `coverage-map` headers are present. |
| Q03 | n/a | No expected byte/semantic values are derived in this documentation map. |
| Q04 | PASS | No tool is credited with output from this lane; statements are explicitly the project's own README claims. |
| Q05 | n/a | No installation, provider readiness or capability-on-host claim is made. |
| Q06 | n/a | No fixture or producer analysis is claimed. |
| Q07 | n/a | No parser prediction is made. |
| Q08 | n/a | Historical criterion; superseded by Q11. |
| Q09 | PASS | No digest, provenance, origin, completeness or authenticity claim is made. |
| Q10 | PASS | Claims are per named project/paper and explicitly bounded; cross-lane game and bounty content is not absorbed. |
| Q11 | PASS | Project names and cited S-IDs are the only identifiers; page dates/versions are attributed to their source rows, not re-derived values. |
| Q12 | PASS | The rejected S074/S091/S093 sources have quoted reasons and source/scope flips in `corpus/SOURCES.md` and the lesson Gate; catalog rejections S071/S072 are similarly recorded. |
| Q13 | n/a | No verifier/recheck command is credited; S077 is a first-party report, explicitly not a test rerun by this lane. |
| Q14 | n/a | No hex string or byte count appears. |
| Q15 | PASS | No Git object or tree identity is asserted in the prose; revision locators are kept in the SOURCES registry. |
| Q16 | PASS | Each tool claim is restricted to the cited project's own documented output/scope; no claim reaches beyond the cited text. |

## Observation, inference, unknown

**Observation:** the cited READMEs, papers and course/publisher pages state the bounded tool roles and caveats in the tables. The source sweep and pinned source locations are recorded in `reports/round-72/shortlink-dispositions.md` and `corpus/SOURCES.md`.

**Inference:** a documentation-led tool inventory can map future static/local analysis choices without claiming tool execution. The cross-cutting safety rule is to validate generated/decompiled interpretations against a separate oracle and keep artifact-carried text untrusted.

**Unknown:** no tool was installed or run; the individual project claims were not behaviorally tested by this lane; the proprietary or commercial host prerequisites are not assessed; the REA spec example does not establish a generic clean-room workflow; and no conclusion is made about any actual game, binary, app, website or traffic target.

## Cross-domain note

The opened REA DX-Ball and TH04 case pages discuss game-specific reconstruction; those examples were not used to claim game-mechanics correctness or absorb game-dev ownership. The bounty-hunter request for the broad Claude-Red skills set is routed to kasegi only when that lane is formally dispatchable; this lane reuses the narrow S050/S051 screening and does not alter another lane's corpus.
