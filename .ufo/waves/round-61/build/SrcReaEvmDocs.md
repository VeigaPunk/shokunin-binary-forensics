# SrcReaEvmDocs — C09 source opening (read-only)

Seat CloseChousa26.SrcReaEvmDocs-10 · access date 2026-10-21 · lane repo /home/vgpnk/Projects/shokunin/revenger-shokunin untouched (no clone, no git/jj mutation); only this report written.

## 1. Installed REA skill — every EVM statement

- File /home/vgpnk/.agents/skills/reverse-engineer-anything/SKILL.md: frontmatter `version: "42"` (`:5`), `tool_count: 207` (`:6`), sha256 `fbcd39d6abe803cf7aa49c1880815bc8e22ba2af87a23681944f687bb7629eb1`; setup pins `rea-agents@6.7.0` (`:37,51,56`).
- The only EVM text is one bullet at `SKILL.md:158-166`; `grep -rniE 'inspect_evm_interface|\bevm\b' .../references --exclude='*backup*' --exclude='*.recovery'` exited 1 — no reference file states anything about EVM.
- `SKILL.md:159-161` verbatim: "treat selectors, argument strings and mutability as inferred candidates; this performs no chain lookup or target execution."
- `SKILL.md:165` verbatim: "Candidate coverage does not establish interface completeness."
- `SKILL.md:161-164` adds `detail: "summary"` and `parent_evidence_id`; that retained-view text is absent from the 6.4.0-tag guide (section 3) and was not exercised by r19-r26 (complete inline `inspection.json`).

## 2. Producer version of the saved r19-r26 records

- `rea-agents@6.4.0` appears once in each of `corpus/live/runs/round-19,21,22,23,24,25,26/LEDGER.md:5` (7 commands); `round-20/LEDGER.md:5-9` runs no producer call and reuses r19 Evidence `ev_0ad0097e…`. No file named `LOG` exists for these rounds; each holds `inspection.json`, `inspection.stderr`, `LEDGER.md`, `reviewer.md` (r20: LEDGER + reviewer only).
- `npm view rea-agents@6.4.0 version gitHead` → `version = '6.4.0'`, `gitHead = 'a56f7bb668ab23fec8d33f7af353ac7ed2fe1895'`, equal to tag `rea-agents-6.4.0`.
- `corpus/live/runs/round-19/inspection.json:1`: `"version":"evmole@0.9.3"`, `"evidence_kind":"inferred"`, `"discovery_completeness":"unknown"`, `"runtime_execution":"not-performed"`.

## 3. Source opened

- Opened https://raw.githubusercontent.com/morluto/rea/main/docs/evm-bytecode.md — HTTP 200, text/plain, 8511 bytes, sha256 `57d5af830bb67883cab98513ae043b56521378ce174d5b13036980ad1cfb7693`. Rendered https://github.com/morluto/rea/blob/main/docs/evm-bytecode.md — HTTP 200. No mirror or search snippet used.
- No in-page version or date. Revision: main blob `1e28542fb75447e1747dc5639354dea39583ae1b`; last modifying commit `48a683ac8c780786f0a2a71ab64aca5994087c00` (2026-10-13T13:55:30Z; `api.github.com/repos/morluto/rea/commits?path=docs/evm-bytecode.md`).
- Tag files: `rea-agents-6.4.0` HTTP 200, 4917 B, sha256 `2207858b9acd29ce46153bc29d407728983f4894f9db04a33dc2da62b32db553`; `rea-agents-6.7.0` HTTP 200, 8511 B, byte-identical to main (`diff -q` rc 0). Neither npm tarball ships the doc (`tar -tzf` found no `evm-bytecode`: 6.4.0 tgz sha256 `59eb1604…`, 6.7.0 `20958a66…`).
- Anchors: §Evidence semantics (tag-6.4.0 lines 42-48); §Selected interface delivery and retained views (main only, lines 76-95); §Resource and lifecycle limits.

## 4. Verbatim quotes (present at both 6.4.0 and main; tag-6.4.0 line numbers)

- Q1 §Evidence semantics 42-43 (14 words): "Selectors, argument strings and state mutability are inferences. Function names/signatures are not looked up." (source bolds `inferences`).
- Q2 §Evidence semantics 45-46 (18 words): "Runtime/init-code identity, deployed authenticity, hardfork and discovery completeness remain unknown. Empty candidates do not prove no callable interface."
- Q3 §Evidence semantics 47-48 (17 words): "Analysis is offline: no target runtime execution, implicit chain/RPC/explorer lookup, wallet action, transaction broadcast or network request."

## 5. Proposed SOURCES.md row (contract v1, 11 columns)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S018 (TBD) | Offline EVM bytecode (REA docs) — https://github.com/morluto/rea/blob/main/docs/evm-bytecode.md | docs | A | the declared output semantics and limits of `inspect_evm_interface` at rea-agents 6.4.0 and 6.7.0: selectors/arguments/mutability are inferences, discovery completeness unknown, no runtime execution or chain lookup | §Evidence semantics, bullets "Selectors…inferences", "Runtime/init-code…", "Analysis is offline…"; tag rea-agents-6.4.0 (a56f7bb) file sha256 2207858b…, tag rea-agents-6.7.0 (27dc42d) = main sha256 57d5af83…, opened 2026-10-21 | Names selector/argument/mutability output as inference with unknown discovery completeness and no execution, so a saved result supports candidates only. | queued | 2026-10-21 | on-release | — |

`queued` keeps the census safe (a `mined` row needs existing `used-by` paths); L1 flips it to `mined` with the C09 entry path and logs old→new.

## 6. What the source does NOT state

- No `PUSH4`, `JUMPDEST` or opcode term: `grep -niE 'push4|jumpdest'` on the 8511-B file exits 1. Selector discovery and destination pairing stay [INFERENCE] from authored fixture bytes (`corpus/live/runs/round-19/LEDGER.md:3`), not this row.
- Does not call `bytecode_offset` a JUMPDEST; only "Offsets are byte positions in decoded bytecode" (tag-6.4.0:37-38).
- No recall, precision, dataset or count; scope sentence only: "Initial real verification covers flat legacy bytecode on Linux x64 and unchanged bundled EVMole 0.9.3." (tag-6.4.0:20-21, 15 words).
- No npm-release mapping and no evidence-schema key names (`evidence_kind`, `discovery_completeness` are the saved record's keys, not doc keys).
- No deployed authenticity, hardfork, reachability or runtime behavior; explicitly no execution or chain lookup.
- 6.4.0 page lacks summary/retained-view delivery; do not cite it for `detail: "summary"`.

## 7. Gate lines (draft for corpus/lessons/round-61.md)

- S018 — https://github.com/morluto/rea/blob/main/docs/evm-bytecode.md — accessed 2026-10-21 — "Selectors, argument strings and state mutability are inferences. Function names/signatures are not looked up." (§Evidence semantics; tag rea-agents-6.4.0:42-43)
- S018 — same URL — accessed 2026-10-21 — "Runtime/init-code identity, deployed authenticity, hardfork and discovery completeness remain unknown. Empty candidates do not prove no callable interface." (§Evidence semantics; tag 6.4.0:45-46)
- S018 — same URL — accessed 2026-10-21 — "Analysis is offline: no target runtime execution, implicit chain/RPC/explorer lookup, wallet action, transaction broadcast or network request." (§Evidence semantics; tag 6.4.0:47-48)

## Unknowns

- Whether npm 6.7.0's build embeds the main-branch guide: npm returned no `gitHead` for 6.7.0; tag `rea-agents-6.7.0` = `27dc42d10249f0410904a75c0997842eb03b931c` (`git ls-remote`), doc identical to main. Tarball does not contain the doc.
- C04 is outside this seat's question; no JavaScript/Electron statement was assessed.

Installs/updates: none (no pacman, uv or npm install; `npm view`/curl reads only). No production edit.

VERDICT: The skill states one EVM bullet (SKILL.md:158-166) and the 6.4.0/6.7.0 REA guide confirms all three load-bearing limits (inferred selectors, unknown discovery completeness, no runtime execution); proposed tier-A row S018/TBD is ready for L1, while PUSH4/JUMPDEST mechanism remains unsupported by this source.
