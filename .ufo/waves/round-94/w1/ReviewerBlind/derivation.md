# ReviewerBlind — pre-read derivation (round 94, C15 blind vote)

Written BEFORE opening `corpus/knowledge/round-72-tool-landscape.md` at rev
`060a8e87d6de6b31f91b58524ab0fcad88ae5431`. Basis: SOURCES registry rows
S054–S095 (`corpus/SOURCES.md`) only, plus the S498/S499 receipt bodies under
`.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/` (present: `S498.body` = REA
root README re-open; `S499.body` = REA `docs/installation.md` re-open). No
entry bytes, no r72/r74 lessons, no wave receipts other than those two bodies
were consulted for this section.

Registry supersession facts visible in the registry itself (scope/status cells
only): S062 is `rejected` ("REJECTED (r74 audit) … superseded by S431"); S058
is superseded in quote fidelity by S430 (bold markers around `jadx` in the raw
README); the live terminal rows for radare2/JADX are S431/S430 respectively.

## Sampled tool 1 — Ghidra (S055, mined, 2026-10-27, tier A)

- Declared role (predicted table row): static software reverse-engineering
  framework. Pinned anchor: "Capabilities include disassembly, assembly,
  decompilation, graphing, and scripting".
- Stated limitation: the row records NO output-quality caveat. What it carries
  is a scope boundary: "no installation or host capability claim"; teaches cell:
  "release prerequisites and security advisories must be checked separately".
- Boundary: README-only description — documentation scope, not a run receipt.
- REA-side (S498.body): Ghidra is one of four named native-analysis engines
  ("Native analysis can use an existing Hopper, Ghidra, IDA or Kuna
  installation", :67; provider table row "Native binaries … Hopper, Ghidra, IDA
  or Kuna", :197). Linux procps `ps` prerequisite for Ghidra launches (:73-76).
  S499.body: "Setup never installs Ghidra, Java, or Python" (:1192-1193) —
  setup saves verified paths for an existing Ghidra installation (:48-49).

## Sampled tool 2 — radare2 (S062 rejected by r74 audit; live row S431)

- Declared role per the pinned README sentence as CORRECTED by the registry
  (S431 anchor): "Today, r2 is a full-featured low-level command-line tool with
  support for scripting with the embedded Javascript interpreter or via
  r2pipe." Scope cell (S062/S431): "The repository's own CLI analysis, hex
  editing, debugging and scripting description; no claim of version-specific
  output".
- The r72-era row S062 quoted "Today, r2 is a full-featured low-level
  command-line hexadecimal editor" — the r74 audit found the phrase
  "command-line hexadecimal editor" belongs to the PRECEDING sentence (about
  the radare project's origin) and is not verbatim at the pinned revision; S062
  is `rejected` and S431 re-located the correct sentence at the same pinned
  commit `6ac96f50eafef46c1ac75a478a1460819968c66f`.
- Stated limitation/boundary: no version-specific output claim; "edits/debugging
  are not part of the static-only work performed in this round"; a broad
  command-line surface is documented.
- REA-side (S498.body): radare2 is NOT named in the re-opened README. For
  offline native-binary inspection REA names "caller-supplied GNU objdump and
  Rizin" (:237-239); Rizin (S069) is the fork lineage sibling, not radare2.

Blind prediction: a correctly re-grounded table row must NOT present r2 as a
"command-line hexadecimal editor" in the pinned-sentence slot; if the entry
still carries that phrase as S062's quoted sentence, it contradicts the
corrected registry state (S062 rejected, S431 verbatim) and is a finding, not
wording.

## Sampled tool 3 — JADX (S058; fidelity successor S430)

- Declared role (predicted row): decompiler for Android DEX/APK and Java
  bytecode outputs (README declaration "for DEX/APK and Java bytecode outputs").
- Stated limitation: "Please note that in most cases jadx can't decompile 100%
  of the code, so errors will occur." (S058 rendered-text form; S430 raw-README
  form adds `**` bold around jadx — fidelity-only difference, same sentence).
- Boundary: teaches cell — "recovered code is a hypothesis to check against the
  artifact and other evidence"; decompiled output is not original source.
- REA-side (S498.body): Android APKs route requires "Headless JADX and a full
  JDK on Linux/macOS/Windows x64" (:219); Linux procps prerequisite (:73-76).
  S499.body: `rea doctor --provider jadx` (:384); a provider missing
  `REA_JADX_MCP_JAR` keeps its own reason (:437-440).

## Sampled tool 4 — ILSpy (S061, mined)

- Declared role (predicted row): "ILSpy is the open-source, cross-platform .NET
  assembly browser and decompiler."; desktop and CLI/front-end roles are listed
  ("Decompiler Frontends" anchor).
- Stated limitation: no output-fidelity caveat is recorded in the row's anchor.
- Boundary: "not quality or host support testing"; teaches cell — "an output
  remains decompiled evidence rather than original source".
- REA-side (S498/S499 bodies): ILSpy is named NOWHERE in the re-opened REA
  README or installation docs; REA's .NET route is "None (static only)" (:218),
  i.e. built-in static inspection with no external .NET decompiler named.

## Sampled tool 5 — Frida (S060, mined)

- Declared role (predicted row): dynamic instrumentation toolkit — "Dynamic
  instrumentation toolkit for developers, reverse-engineers, and security
  researchers."; a runtime instrumentation surface with a published
  release-binary role.
- Stated limitation: no output-quality caveat recorded.
- Boundary: "no target activity or host installation"; teaches cell — "any use
  remains limited to an explicitly authorized local artifact/lifecycle, not a
  live target".
- REA-side (S499.body): Frida appears only as a transitive npm dependency
  ("a deprecation warning for `prebuild-install` from transitive native
  dependencies (such as Frida)", :28-30) and as an "optional native provider"
  whose readiness is NOT established by the CLI version verification (:541-542).
  S498.body names no Frida operation route.

## Q03/Q11 angle — what the table must NOT credit (derived from sources only)

A source-faithful tool-role table may state, for each of the five tools: the
declared role, the project's own stated limitation where one exists, and the
row's scope boundary. It must NOT credit:

1. radare2 "hexadecimal editing" as the pinned-sentence role (r74-corrected).
2. Any completeness/quality claim for Ghidra decompilation (S055 states none).
3. Any claim that jadx decompiles all code (S058/S430 say the opposite).
4. Any ILSpy output-quality or host-support claim (S061 excludes both).
5. Any Frida live-target or host-installation claim (S060 excludes both);
   and none of the five may be credited with a run receipt — every row is
   README/documentation scope.
