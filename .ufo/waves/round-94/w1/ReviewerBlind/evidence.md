# ReviewerBlind — evidence and vote record (round 94, C15 blind-derivation vote)

- Seat: `ReviewerBlind` (pinned registry role: `reviewer`, `swarm-registry.json`)
- Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
- Frozen entry rev: `060a8e87d6de6b31f91b58524ab0fcad88ae5431`
- Candidate digest (vote-bound): `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`
- Digest provenance: `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431` printed `C1_VOTES=votes dir missing digest=01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3` (exit 1 — expected at the freeze tip: the C15 row is not yet flipped and the live SOURCES.md does not yet carry S498/S499, so `C1_C15_HELD=fail`, `C1_VOTES=fail(votes dir missing)`, `C1_SOURCES=fail S498/S499 unresolved+new-row-missing`). Cross-checked byte-identical against `.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`.

## Method (blind order, as assigned)

1. Derivation written FIRST, from `corpus/SOURCES.md` rows S054–S095 (scope/anchor/teaches cells only) plus the two S498/S499 receipt bodies under `.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/` (`S498.body` = REA root README re-open, `S499.body` = REA `docs/installation.md` re-open; both present). Preserved verbatim at `derivation.md` in this directory; written before any entry byte was opened.
2. Entry then read once via `git show 060a8e87d6de6b31f91b58524ab0fcad88ae5431:corpus/knowledge/round-72-tool-landscape.md` (read-only). The entry was NOT edited.

## 1. Blind derivation (summary; full text in `derivation.md`)

| Tool | Declared role (predicted) | Stated limitation (predicted) | Boundary (predicted) |
|---|---|---|---|
| Ghidra S055 | static SRE framework: disassembly, assembly, decompilation, graphing, scripting | none on output; row carries only scope | README-only documentation scope; no installation/host capability claim; prerequisites and advisories checked separately |
| radare2 S062 (rejected r74; terminal S431) | full-featured low-level command-line tool with scripting (embedded JS interpreter / r2pipe) — the corrected pinned sentence | no version-specific output claim | repo's own CLI analysis/hex-editing/debugging/scripting description; edits/debugging outside this round's static-only work; r2 must NOT be quoted as "command-line hexadecimal editor" |
| JADX S058 (fidelity terminal S430) | Java source output from DEX/APK and Java bytecode | "in most cases jadx can't decompile 100% of the code, so errors will occur." | recovered code is a hypothesis to check against the artifact; not original source |
| ILSpy S061 | open-source cross-platform .NET assembly browser and decompiler; desktop + CLI frontends | none recorded on output fidelity | not quality or host support testing; decompiled evidence ≠ original source |
| Frida S060 | dynamic instrumentation toolkit for developers, reverse-engineers, security researchers; release-binary role | none on output | no target activity or host installation; any use limited to an explicitly authorized local artifact/lifecycle, never a live target |

REA-side receipt facts (S498/S499 bodies): Ghidra = one of four named native-analysis engines (Hopper/Ghidra/IDA/Kuna), never installed by setup; JADX = required provider of the Android APK route (headless JADX + full JDK; Linux procps prerequisite); radare2 NOT named (GNU objdump and Rizin are the named offline native-binary helpers); ILSpy named nowhere (.NET route is "None (static only)"); Frida appears only as a transitive npm dependency warning and as an optional native provider whose readiness the CLI check does not establish.

## 2. Diff: derivation vs the frozen entry's table rows

| Tool | Entry row (frozen bytes) | Verdict |
|---|---|---|
| Ghidra | "Ghidra lists disassembly, assembly, decompilation, graphing and scripting"; boundary: "do not infer feature parity, licensing, correct decompilation, or local provider readiness"; "Review the exact source and current version before selecting one." | MATCH — role, limitation-absence and boundary all as derived. Source anchor says "Capabilities include …" (non-exhaustive); the entry's "lists" phrasing stays faithful. |
| radare2 | Row 2: "radare2/Rizin describe command-line binary analysis"; row 3: "radare2 and Rizin list hex/format and scriptable inspection capabilities." | MATCH — critically, the entry does NOT carry the invalidated "command-line hexadecimal editor" quote anywhere; its generic paraphrase is consistent with both the S062 scope cell and the corrected S431 pinned sentence. |
| JADX | "JADX describes Java output from DEX/APK and warns that many cases do not decompile completely."; boundary: "Decompiled or rebuilt files are not the original source or proof of install validity." | MATCH — wording-level note: source says "in most cases", entry paraphrase says "many cases". The warning is preserved; nothing beyond the source is credited. |
| ILSpy | "ILSpy describes a cross-platform .NET assembly browser/decompiler."; row boundary adds "These docs do not yet establish C03 assembly-analysis knowledge." | MATCH — role exact; boundary cell of that row focuses on the dnSpy/dnSpyEx archive/maintenance caveats; the ILSpy-specific "decompiled evidence, not original source" limit is carried by the entry's Scope section ("not using an output as proof of source identity"). |
| Frida | "Frida describes dynamic instrumentation."; boundary: "This round does not run any target. Any later dynamic work needs explicit authorization and a bounded local artifact lifecycle; platform and architecture statements remain per-project." | MATCH — role, limitation-absence and no-live-target boundary exactly as derived. |

**Mismatch count: 0 beyond wording.** Two wording-level observations, neither a credited output:
1. JADX "many cases" (entry) vs "in most cases" (S058/S430 raw sentence) — paraphrase slightly weakens the frequency; the caveat and its direction are preserved.
2. Rizin is grouped with radare2 under "hex/format and scriptable inspection capabilities" (row 3); S069's own cell names a "framework/CLI surface" without the literal words "hex editing". Rizin is outside my assigned five-sample; recorded as an observation only.

Supersession note: the entry cites the r72-era rows S057/S058/S062/S066/S068/S094, which the r74 quote audit later rejected for fidelity and superseded (S429/S430/S431/S433/S434/S438). The frozen entry's table text reproduces NONE of the invalidated quotes (checked for "command-line hexadecimal editor", the reordered dnSpyEx sentence, and the bold-less jadx sentence — all absent; the entry paraphrases), so its substance survives the corrections, and each cited sid reaches a `mined` terminal row in the live registry — consistent with the v3 gate's supersession-terminal semantics. The r73 erratum section (S427/S428) is present and, per the frozen claim, must stay byte-identical at landing.

## 3. Per-Q spot-check — Q03/Q11 angle ("does the table credit any output the sources do not state?")

- Q03 angle: the entry derives no expected byte/semantic value anywhere (verified by full read of the frozen bytes: every table cell is a documentation-scope statement; no command output, no hex, no counts). The entry's own `n/a` on Q03 is honest.
- Q11 angle: identifiers in prose are project names + S-IDs only. The one date-like fact in prose, "dnSpyEx's own README was last revised in 2023 in the opened history", is traceable to S068's own teaches cell ("no claim of active maintenance is made because the README revision is from 2023") — attributed, not re-derived. No page version/date is re-derived for any of the five sampled tools.
- No output is credited beyond the sources for any of the five sampled tools; on full-entry read, no row credits a run, an installation, or a lane-observed result (matches the `verified-at` line: "No tool was installed or executed.").

## 4. Vote decisions (recorded in `vote.json`)

| Q | Vote | Basis (this seat's verification) |
|---|---|---|
| Q01 | PASS | Load-bearing tool roles rest on tier-A primary project docs/papers at their declared scope (S054–S070 all tier A); tier-C catalogs S071/S072/S087/S088 appear only as discovery leads; verified per-row for the five sampled tools. |
| Q02 | PASS | Header block carries source S-IDs with URLs and anchors/revisions, plus `verified-at`, `recheck`, `coverage-map` and `admission-status` lines. |
| Q03 | n/a | Documentation-only map; verified across the full frozen bytes that no expected byte/semantic value is derived, so the criterion has no object to check here. |
| Q04 | PASS | Every cell attributes statements to the project's own documentation ("describes/lists/reports"); no tool is credited with output produced by this lane; verified per-row for the five sampled tools. |
| Q05 | n/a | No installation, provider-readiness or capability-on-host claim appears; the Scope section and `verified-at` line explicitly bar and deny it. |
| Q06 | n/a | No fixture or producer analysis is claimed in any section of the frozen entry. |
| Q07 | n/a | No parser prediction is made; the table states documentation scope and defers displayed interpretations to separate oracles. |
| Q08 | n/a | Historical criterion; this entry's map supersedes it with Q11, so there is no independent Q08 object to vote. |
| Q09 | PASS | No digest, provenance, origin, completeness or authenticity claim is made; the dnSpy archive banner is treated as repository metadata, not support. |
| Q10 | PASS | Claims are per named project/paper and bounded; the coverage-map line explicitly disclaims complete tool coverage and tool installation/readiness; no cross-lane content absorbed. |
| Q11 | PASS | Project names and S-IDs are the only prose identifiers; the dnSpyEx 2023 fact is attributed to S068's row; no page date/version is re-derived for the sampled tools. |
| Q12 | PASS | Rejection dispositions verified against live SOURCES.md rows: S091 ("February 2012, 800 pp." quoted, dated-procedure flip), S093 ("Disable Windows Defender" quote, safety-conflict flip), S071/S072 (catalog-evidence flips), S074 (province-content flip) — all carry quoted reasons and scope flips; the erratum section records S427/S428 supersessions. |
| Q13 | n/a | No verifier or recheck command is credited as rerun by this lane; the `recheck` header names registry re-open only and S077 is labeled first-party, not rerun here. |
| Q14 | n/a | No hex string or byte count appears anywhere in the frozen entry bytes (verified by full read). |
| Q15 | PASS | No Git object or tree identity is asserted in the prose (the header names commits only as "shown in the source history"); revision locators stay in the SOURCES registry. |
| Q16 | PASS | Each tool claim is restricted to the cited project's own documented output/scope with an explicit boundary cell; verified per-row for the five sampled tools. |
| Q17 | n/a | No sentence credits a script, table or command with covering a set; no command output is embedded or re-derived in the entry. |

9 PASS / 8 n/a; every n/a carries a ≥20-character reason (see `vote.json`).

## 5. Artifact binding

- This file (`evidence.md`) is the vote artifact: non-empty, seat-distinct, inside `.ufo/waves/round-94/w1/ReviewerBlind/`, and contains the candidate digest `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`.
- `artifact_sha256` in `vote.json` is the SHA-256 of this file's bytes, computed after this write.
- Bounds honored: no lane file edited; no git write command; reads only (claims, SOURCES.md, S498/S499 receipt bodies, swarm-registry.json, frozen entry via `git show`, ExecFrozen freeze-state digest file). Scratch dir `/fast/scratch/hyaku/revenger-r94/ReviewerBlind/` was created for the session and is deleted before yielding; no output depended on it (all artifacts written directly here).
