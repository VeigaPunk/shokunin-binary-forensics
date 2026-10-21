# Round 61 — scope the saved record, not the surface name (2026-10-21)

Hyaku round 61, attempt 1. Claim base `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97`;
pre-registration `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`
(`reports/round-61/claims.md`, amendments A1/A2 before any after-run). L1:
CloseChousa26 (reused idle agent; Main spawn job-capped). Bar: `corpus/QUALITY.md`
Q01–Q13. Build wave seat reports: `.ufo/waves/round-61/build/` (68 seats). These
L2 seats are the lane, not outside discernment.

## Principle

A row label such as "JavaScript/Electron packages" or "EVM bytecode
interfaces" invites a wider claim than a saved record supports. Both entries
admitted this round are scoped to what the records contain on the lane's own
authored fixtures; the surface name is not evidence. The EVM entry's strongest
content is a negative (r26: a valid static pattern behind an entry STOP was not
reported), and the JavaScript entry states outright that `electron-main` is a
label and the `main` edge is not separated from the `index.js` fallback.

## Spot-check intake (round-1 outside check)

Source: `corpus/lessons/round-1-verifier-spotcheck.md:12-17`.

| item | outside verdict | round-61 disposition |
|---|---|---|
| C11 admit | agree | no action |
| RFC 3227 reject (S008) | agree with reject, disagree with its record: §2.1 Order of Volatility is the very primitive its flip names | learned: superseding row S024 re-opened at §2.1 with a coherent flip; new criterion Q12 (M21). S008 is not edited (rule 2). |
| receipt-command mutation survivor | routed debt | C2 this round (M22, Q13) |
| SKILL.md absent | routed debt | still absent; not claimed this round |
| F03 verdict vs scout STALE | routed debt | not adjudicated this round; carried |
| kaidoku/revenger overlap (ADJ-06) | routed | still operator-owned; both new entries carry a `## Cross-lane contest (Q10)` block |

## Mistakes

| id | class | evidence | captured-by | fix shown able to fail |
|---|---|---|---|---|
| M21 | rejection record incoherent: S008's flip asks for "its volatility-ordering primitive", which RFC 3227 §2.1 already supplies, so the flip can never change the verdict; its anchor also omitted §2.1 | `corpus/SOURCES.md:22` (S008); `corpus/lessons/round-1-verifier-spotcheck.md:13`; re-opened §2.1 quote in `## Gate` below | Q12 (added this round; no criterion caught it before) | S024 supersedes S008 with a source-change or scope flip. Q12 rejects a flip that asks for content the row credits the source with; S008 itself fails Q12, S024 passes it. |
| M22 | self-test blind spot: a verifier clause had no in-script negative, so deleting it was invisible to the script's own run | `.ufo/waves/kaika-r1/mutation-post.md:15,21`; `reports/round-61/measure-before.log` (`C2_RECEIPT_B_KILLED=0/2`) | Q13 (added this round; no criterion caught it before) | in-memory forged-command control in both verifiers; the same mutant b now fails at the control (`C2_RECEIPT_B_KILLED_ATTRIBUTED` 0/2 before, 2/2 after; `reports/round-61/measure-after.log`) |
| M23 | committed conformance commands default to `HEAD`, which under jj colocation can name `@-` or an unbookmarked commit | `reports/round-1/scribe.md:42`; `LOG.md:318`; mechanism fleet `.ufo/waves/hyaku/jj-w1/reports/JjAuditRevenger.md:164-170` | none — process rule (like M03, M16), not corpus admission | use `git cat-file -e "$h^{commit}" && git merge-base --is-ancestor "$h" refs/heads/main`; seat `ScoutJjClassAIdioms` showed true 0, off-branch 1, missing 128, and that the audit's suggested jj revset `::<hash> & heads(bookmarks(main))` returns empty for a true ancestor |
| M24 | misroot: six build seats wrote their reports under the fleet root although the wave context named the absolute lane path | fleet `.ufo/waves/round-61/build/{ConnectorKasegiEvm,ExecJsOracleR3,ExecJsSavedEvidence,SimplifierReceiptControl,SrcEvmCodesScreen,SrcSolidityMetadataTail}.md` (now moved) | none — dispatch process | L1 misroot sweep: byte-exact copy to the lane path, `cmp`, delete the fleet copy; a seventh seat (ExecEvmOracleR24) self-corrected |
| M25 | fixture-field misread: the build seats and the C09 entry (at `0b6ddf0`) stated that `evm-r24/truth.json` `embedded_pattern_offsets` `[1, 9]` names two occurrences "inconsistent with the bytes"; it is the inclusive span of the one 9-byte occurrence (offsets 1–9), so the stated defect did not exist | `corpus/fixtures/evm-r24/fixture.raw` (pattern `63deadbeef14601057` found once, at 1, length 9); authoring note `LOG.md:289` ("occur only inside immediate offsets 1–9"); round-61 seats `ExecSelectorKeccak`, `ScribeEntryEvm`; first doubted by falsify seat `AuditR24Truth` (dead, no report; transcript only) | none — Q06 checks premises against bytes, not a reader's semantics for a truth field | entry `## Limitations` corrected by the replacement L1; check: for each byte-search occurrence compute `[start, start+len-1]` and compare with the truth list — it prints `[1, 9]` (match), while the two-occurrence reading needs a second match at 9, which the same search returns absent |

Classes this round 5; captured by a criterion 2 (Q12, Q13); `none` 3 (M23, M24 — process; M25).
Count: `awk -F'|' '/^\| M2[1-9] /{n++; if ($5 ~ /none/) z++} END{print n, n-z, z}' corpus/lessons/round-61.md`.

## Gate

### Sources opened this round (contract rule 1)

Access date 2026-10-21 for every row; quotes verbatim, at most 25 words.
L1 re-opened S016 (runtime.py, `instructions/__init__.py`), S017, S018, S019,
S020, S021, S023 and S024 and re-matched the quotes below against the fetched
bytes (Yellow Paper PDF SHA-256 `d67c009c…77fa9`).

- S016 https://raw.githubusercontent.com/ethereum/execution-specs/v2.20.0/src/ethereum/forks/osaka/vm/runtime.py — lines 29-30: "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes." Opener: `SrcExecSpecsOpcodes`.
- S017 https://ethereum.github.io/yellowpaper/paper.pdf — §9.4.3, p.15: "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations" Openers: `SrcYellowPaperJumpdest`, `ScribeSourcesRowsEvm`.
- S018 https://docs.soliditylang.org/en/v0.8.37/abi-spec.html — §Function Selector: "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function." Openers: `SrcSolidityAbiVersionPin`, `SrcSolidityAbiSelector`.
- S019 https://docs.soliditylang.org/en/latest/metadata.html — §Contract Metadata, para 1: "The compiler appends by default the IPFS hash of the metadata file to the end of the runtime bytecode" Opener: `SrcSolidityMetadataTail`.
- S020 https://nodejs.org/api/modules.html — "File modules": "If the exact filename is not found, then Node.js will attempt to load the required filename with the added extensions: .js, .json, and finally .node." Openers: `SrcNodeCjsRequire`, `ScribeSourcesRowsJs`.
- S021 https://nodejs.org/api/packages.html — `"main"`: "The "main" field defines the entry point of a package when imported by name via a node_modules lookup. Its value is a path." Openers: `SrcNodePackageMain`, `ScribeSourcesRowsJs`.
- S022 https://tc39.es/ecma262/ — §14.3.3.3 KeyedBindingInitialization, SingleNameBinding step 3: "Set value to ? GetV(value, propertyName)." Opener: `SrcEcmaDestructuring` (not re-opened by L1).
- S023 https://nodejs.org/api/esm.html — "CommonJS Namespaces": "The detection of named exports is based on common syntax patterns but does not always correctly detect named exports." Opener: `SrcNodeCjsLexer`.
- S024 https://www.rfc-editor.org/rfc/rfc3227.txt — §2.1 Order of Volatility: "When collecting evidence you should proceed from the volatile to the less volatile." Opener: `ScoutSpotcheckIntake`.
- S025 https://www.evm.codes/#5B — JUMPDEST notes: "Mark a valid destination for JUMP or JUMPI. This operation has no effect on machine state during execution." Opener: `SrcEvmCodesScreen` (not re-opened by L1).
- S026 `corpus/live/runs/round-26/inspection.json` — own-work: `"functions":[]` with `"runtime_execution":"not-performed"`.
- S027 `corpus/live/runs/20261012T164357Z/analysis.json` — own-work: `"resolution_context":"package-entrypoint"`.

Row changes old→new on pre-existing rows: none. S008 is superseded by the new
row S024 (rule 2), not edited.

### Admission decisions

Map statuses used for eligibility are those at `cf02419`.

| candidate | map row (status at `cf02419`) | decision | criteria |
|---|---|---|---|
| `knowledge/evm-saved-interface-candidates.md` | C09 (uncovered) | **admit** | Q01 S016/S017/S018/S019/S026; Q02 headers; Q03/Q06/Q11 `## Reproduce` re-run by L1, output identical; Q05 past tense; Q07 r25/r26 causes unknown; Q10 kaidoku prior art reported; Q13 EVM verifier not credited |
| `knowledge/commonjs-destructured-require-edges.md` | C04 (uncovered) | **admit** | Q01 S020/S021/S022/S023/S027; Q02 headers; Q03/Q06/Q11 block re-run by L1; Q04 comparison tool's 0/1 not credited; Q10 Electron/ASAR excluded, kaidoku ground reported; Q13 |
| "REA reports every statically valid PUSH4→JUMPDEST pattern" (registered C09 wording) | C09 | **reject** | Q07/Q10: falsified by saved r26 (`functions: []` with a valid destination at 17) |
| "r24 shows the provider excludes PUSH immediate data" | C09 | **reject** | Q07: confounded; the embedded target is not a JUMPDEST and the file has no 0x5B byte (`ExecEvmOracleR24`) |
| "fixture selectors are Keccak-derived" | C09 | **reject** | Q01/Q03: no `truth.json` declares a signature; S018 defines derivation (`ExecSelectorKeccak`) |
| "REA identifies the Electron main process" | C04 | **reject** | Q04/Q10: `electron-main` is a node-kind label; 0 Electron tokens in the fixtures |
| "the package `main` edge is discriminated from the `index.js` fallback" | C04 | **reject** | Q03/Q07: `main` is `index.js`, the documented fallback (S020); fixtures cannot separate them |
| Electron ASAR documentation as C04 support | C04 | **reject** (no row; `SOURCES.md` search log) | Q01 scope: the page says nothing about `require` destructuring or `main` (`SrcElectronAsarScreen`) |
| evm.codes as C09 support | C09 | **reject** (row S025, rejected) | Q01: community, never tier A; adds nothing beyond S016/S017 |

Admitted 2 (both on rows uncovered at `cf02419`); rejected 7.
Count: `awk -F'|' '/^\| (`knowledge|")/ || /^\| (Electron|evm\.codes)/ {d=$4; if (d ~ /admit/) a++; else if (d ~ /reject/) r++} END{print a, r}' corpus/lessons/round-61.md`.

### Outside spot-check

Not performed in-round. The orchestrator's non-author closure samples at least
one admit and one reject above; discernment stays `unchanged` until it lands.

## Gate — fresh-wave rejection erratum (2026-10-21)

This section supersedes the two admit decisions above; it does not erase
their history. The parent authorized a fresh validated 66-seat attack wave
against `ab580698` after the original 65-seat falsify wave died with the host.
Evidence: `.ufo/waves/round-61/falsify-w3-spec.json`, its dispatch/spawn
receipts, and `.ufo/waves/round-61/falsify-w3/` reports.

| candidate | final decision | failed criterion and counterexample |
|---|---|---|
| C04 `knowledge/commonjs-destructured-require-edges.md` | **reject** | Q11: Limitations claimed its block carried edge spans, but neither code nor Provenance printed any location/column fields (`W3JsOverclaimCritic.md`, corroborated by `W3JsSpecifierUnnamed.md`). Q13 also over-credited verifier clauses whose own run survived deletion (`W3QualityQ13Apply.md`). `W3JsElectronMainLabel.md` identified the unsupported neutral-name reading of the provider's inferred Electron role. |
| C09 `knowledge/evm-saved-interface-candidates.md` | **reject** | Q11: r24's PUSH32 count, raw 0x5B count, embedded target and pattern span were correct when independently checked but lacked in-entry derivations (`W3EvmR24Immediate.md`, corroborated by `W3EvmR24SpanFix.md`). `W3ProvinceBounds.md` and `W3EvmCrossLaneCites.md` also refuted the kasegi citation and found omitted sibling evidence. |

Both entries remain explicitly rejected evidence, not admitted knowledge.
C04/C09 return to `uncovered`; final admitted 0 of these 2 candidates,
rejected 2 (in addition to the seven earlier rejected propositions/sources).
Final K 4/14 (2.9), unchanged from the base and therefore C1 falsified by its
registered condition. C2's receipt-command kill stays 2/2; it does not rescue
C1 or make the whole round admitted.

Other fresh-wave findings remain in the reports, not silently repaired:
SOURCES search-log disposition/count defects (`W3SrcSearchLog.md`);
S019 anchor precision (`W3SrcContractCells.md`); Q12's weak successor-flip
branch (`W3QualityQ12Fail.md`); M25's imprecise attribution and capture
classification (`W3LessonMistakes.md`, `W3EvmR24SpanFix.md`); premature
README admission (`W3ClaimsAmendmentOrder.md`); and the K probe's file-existence
limit/non-target-status blind spot (`W3HoldProbeRerun.md`, `W3KProbeMutant.md`).
These are retained limitations, not fresh capabilities or admitted findings.

## Mistakes — fresh-wave addition

| id | class | evidence | captured-by | disposition shown able to fail |
|---|---|---|---|---|
| M26 | successful recheck output mistaken for complete derivation coverage | C04 block reproduced but printed no asserted spans; C09 reproduced but omitted r24 raw-count/span/target derivations; reports `W3JsOverclaimCritic.md`, `W3EvmR24Immediate.md` | Q11 (existing, admission failed to enforce it) | fresh reviewers applied the existing reject condition to factually correct but underived values; both candidates rejected and map flips rolled back, K 6/14 provisional → 4/14 final; no claimed repair |

The earlier M21–M25 count remains a historical five-row count; this appended
row is an additional mistake, not an alteration of that frozen census.

