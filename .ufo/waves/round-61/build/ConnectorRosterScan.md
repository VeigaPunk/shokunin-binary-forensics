# ConnectorRosterScan — round 61: C04/C09 cross-lane contest (read-only)

Seat `CloseChousa26.ConnectorRosterScan-10`. Base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` (`git -C revenger-shokunin rev-parse HEAD`); `PROVINCE.md` sha256 `63acc3d0…` = tsukuroi OUT-009 anchor. No clone, no lane write.
Method: `grep -icE '(javascript|electron|\bnpm\b|\bevm\b|ethereum|bytecode|smart[ -]contract|commonjs)'` over all 21 local `*-shokunin/PROVINCE.md`; 3 files hit (19 lines), 18 zero. Adjacent variants (`asar|JS|solidity|webpack|PUSH[0-9]|JUMPDEST|EVMole`) scanned separately.
Roster mapping: `jq -r '.roster[] | [.id,.repo] | @tsv' MANIFEST.json` → id `revenger`→repo `shokunin-binary-forensics`, id `kaidoku`→repo `shokunin-reverse-engineering`; neither repo name is on disk (`ls -1d shokunin-*` → `ls: cannot access 'shokunin-*': No such file or directory`; `find /home/vgpnk/Projects -maxdepth 4 -type d -name 'shokunin-*'` → 34 hits, all `.ufo/waves` or scope dirs, no checkout); local trees are `revenger-shokunin/` and `kaidoku-shokunin/` (MANIFEST domain fields + tsukuroi OUT-008/009 anchors).
Contest rule: a hit contests when the planned entry would restate ground the hit claims as owned/held (C04 = Electron/JS package ownership or package-graph knowledge; C09 = EVM selector/JUMPDEST knowledge). `partial` = adjacent JS surface, not the entry's specific claim; `gov` = scope governance only.

| path:line | term | C04 | C09 | what the line claims |
|---|---|---|---|---|
| kaidoku-shokunin/PROVINCE.md:4 | JavaScript/Electron | contest | — | domain "Electron/ASAR/JavaScript bundles" |
| kaidoku-shokunin/PROVINCE.md:19 | npm | — | — | npx cache path 6.7.0 (tool provenance) |
| kaidoku-shokunin/PROVINCE.md:21 | npm | — | — | npx cache path 6.5.0 |
| kaidoku-shokunin/PROVINCE.md:45 | npm | — | — | `rea` CLI npx cache |
| kaidoku-shokunin/PROVINCE.md:49 | Electron/JavaScript | partial | — | held `analyze_javascript_application` on asar |
| kaidoku-shokunin/PROVINCE.md:52 | JavaScript | partial | — | `compare-javascript-export-shapes` CLI-held |
| kaidoku-shokunin/PROVINCE.md:53 | Electron | — | — | CDP runtime observation (C08) |
| kaidoku-shokunin/PROVINCE.md:54 | EVM | — | contest | EVM interface verb held; selector extraction |
| kaidoku-shokunin/PROVINCE.md:91 | EVM/bytecode | — | contest | selectors held, synthetic dispatcher r3-07 |
| kaidoku-shokunin/PROVINCE.md:124 | JavaScript | partial | — | wakaru JS source recovery held |
| kaidoku-shokunin/PROVINCE.md:127 | bytecode | — | — | `.jsc` V8 bytecode, not package graph |
| kaidoku-shokunin/PROVINCE.md:128 | JavaScript | — | — | runtime observation verbs (C08) |
| kaidoku-shokunin/PROVINCE.md:131 | JavaScript | partial | — | AppImage inner asar analyze-js-application |
| kaidoku-shokunin/PROVINCE.md:146 | bytecode | — | — | bytecode-to-source mapper frontier |
| kaidoku-shokunin/PROVINCE.md:160 | JavaScript | partial | — | export-shapes held (r4-09) |
| revenger-shokunin/PROVINCE.md:4 | JavaScript/Electron | own | — | own scope; basis for C04 entry |
| revenger-shokunin/PROVINCE.md:5 | Electron | — | — | own C08 runtime scope |
| tsukuroi-shokunin/PROVINCE.md:150 | Electron/JavaScript | contest (gov) | — | R20-OUT009: Kaidoku/Revenger arbitration unresolved |
| tsukuroi-shokunin/PROVINCE.md:152 | Electron/JavaScript | contest (gov) | — | "Electron/JavaScript packages" precise scope; "owns" superseded |

Adjacent-variant hits, none contesting C04/C09: game-dev-3d-shokunin/PROVINCE.md:7,17,68 (three.js runtime); kagi-shokunin/PROVINCE.md:30 (`fnm-nudge.js`); kake-shokunin/PROVINCE.md:23,57 (JS rendering for web crawl); tameshi-shokunin/PROVINCE.md:55,79 (`js-round-gate`, `js-sources-check` scripts); kaidoku-shokunin/PROVINCE.md:57 (`.node` addons), :135 (RISC-V), :151-152 (large asar mapping, C04 partial), :158 (JS+managed reconcile, C04 partial).

## Findings

F1 Lane-local "uncovered" is fleet-held. Revenger `corpus/README.md:30` (C04) and `:35` (C09) say `uncovered`; kaidoku `corpus/README.md:23` says `held — obsidian app.asar (launcher) + obsidian.asar (real app: 45 ipcMain ops); N-API taxonomy; .jsc bytecode loader identified`, and `:38` says `held — EVMole selectors recovered from a synthetic dispatcher (r3-07) and from real solc-0.8.37-compiled runtime carriers (arc3-r1)`.
F2 Half of C04 is already held. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-renderer-asar.md:79` heading `Entrypoint topology — package.json:main → index.js NOT-FOUND`; `:81` records `resolution_status: "not-found"`; `2026-10-13-asar-surface.md:15` records app.asar `"main": "main.js"`. The require-edge half is fleet-novel: `grep -rniE 'commonjs' corpus/knowledge/` → 2 incidental hits (bundler module nodes; CJS wrapper args); `grep -rnE 'require\(' corpus/knowledge/` → 9 hits, all tooling `node -e` or literal specifiers (`2026-10-13-r3-typora-signal.md:73`, `2026-10-13-r4-07-jsc-bytecode.md:78`), none a named-import edge.
F3 C09's core distinction is already held. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-evm-interface.md:151-154` erratum: "`bytecodeOffset` records the **JUMPDEST dispatch-target position**, not the PUSH4 comparison site." Fleet-novel C09 ground is revenger's r23–r26 authored negatives (bare PUSH4, PUSH32 decoy, shifted/invalid target, corrected target) and raw-vs-hex carrier identity; kaidoku's EVM entries cover solc/vyper carriers.
F4 Operative gate is Q10. Revenger `corpus/QUALITY.md:22` — "Cross-lane contested scope is reported, not absorbed." Neither sources draft reports the contest (`ScribeSourcesRowsJs.md` §5, `ScribeSourcesRowsEvm.md` §4 name no sibling lane), so both entries as planned would absorb contested scope.
F5 Governance binds current bytes. `tsukuroi-shokunin/PROVINCE.md:150` "Kaidoku/Revenger arbitration remains unresolved"; `:152` supersedes OUT-009's "Revenger owns" wording. Revenger `PROVINCE.md` sha256 `63acc3d033869f93f3e13da79e35023d86baa60b3f1d3b52861b019183b4b19f` equals the OUT-009 anchor.

## Proposal (one bounded move)

Evidence: F1–F5. Axes: coverage K integrity and Q10 conformance improve; calibration C2, replay and saved records untouched (disjoint files).
Move: make a `## Cross-lane contest (Q10)` block mandatory in both entries before gating — cite `kaidoku-shokunin/corpus/README.md:23`/`:38` and the exact sibling line, then state the delta. C04 novel: destructured-require named-import edge topology; C04 already held: `main` mapping (`r3-renderer-asar.md:79-81`) → cite as corroboration or drop the standalone claim. C09 novel: r23–r26 negatives and carrier identity; C09 already held: `bytecodeOffset` = JUMPDEST target (`r3-evm-interface.md:151-154`). No ownership language (tsukuroi `:150`).
Risks: (a) extra gate burden could delay the predicted 6/14 flip; (b) if C04 drops its `main` half, the entry narrows to edge topology and `ScribeSourcesRowsJs.md` §4 says the opened Node docs state nothing about destructuring — that half then fails Q01 unless a destructuring source is opened or the claim is demoted to unknown; (c) quoting sibling ground could propagate its errors — cite only its errata-checked lines.
Verification: `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` → 6/14 after both admit; `python3 -B reports/round-61/measure.py TREE` → `K_HELD` 6; each entry carries the Q10 block with a kaidoku path:line; `git diff e0a4b0c… -- corpus/live corpus/fixtures` empty.

VERDICT: C09 contests kaidoku's held EVM ground outright; C04 contests it on package `main` while its destructured-require edge topology is fleet-novel; tsukuroi R20-OUT009 is an unresolved governance contest on C04; report-only, no lane file changed.
