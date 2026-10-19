# Fleet round-1 lesson — preserve identity, relocate reads

Round: current fleet round 1, interactive continuation of interrupted work; not a renumbering of imported r1–r60.
Sources: `LOG.md` sections “Fleet round-1 declaration”, “implementation smoke”, and “interactive continuation”; work commit `7c3ce197341b0babe0046b1d9cbb59f1ba43f54e`; `.ufo/waves/fleet-round-1-interactive/local-acceptance.json`; `reports/round-1/reviewer.md:12-41`.

## Principle and boundary

A saved PE Evidence artifact path is historical identity, not an input locator for a relocated corpus. The existing named two-image ledger now reads bytes via its own `__file__`-relative `ROOT` while checking artifact and receipt-command identity against an independently fixed `HIST`. Copying the expected path out of the saved field, or rewriting history to the current checkout, would launder the field under test.

This is a demonstrated property only of authored r55–r57 saved normalized records and their checked receipts. It does not authenticate the historical REA producer, exercise a PE loader, validate arbitrary PE files, or reverse the falsified r59 malformed-Unicode refusal claim. The envelope's `parameters.path` and `locations` are not comprehensively checked by this verifier; they are not part of the six claimed rejection cases.

## Gate

- Candidate: admit a narrow observation that the named ledger can replay unchanged saved inputs after relocation while retaining its checked historical identities. **Locally accepted as round evidence only**: real verifier passes in three contexts, six isolated semantic/path forgeries reject with expected findings and exit 1, and all nine source inputs match baseline/work/current SHA-256. Command: `python3 -B reports/round-1/replay_scenarios.py`, observed exit 0; full stdout/stderr and input revision hashes in `.ufo/waves/fleet-round-1-interactive/local-acceptance.json`.
- Candidate: count the predecessor's nine-member batch, a validated/rendered plan, or a live interactive process as a verified completed round. **Rejected**: the operator requires a complete authorized routed width-32 native task batch. Canonical plan exit 0 produced 32 distinct scopes, but the executed route assessment exits 2 and dispatch count is zero. Evidence: `.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json`.
- Candidate: equate saved receipt hashes or Evidence IDs with authenticated producer origin/native readiness. **Rejected**: these checks establish internal consistency only; no producer was called. The exact boundary is exercised against saved records, not a running target.
- Candidate: claim the language/multi-image ledgers are repaired, the Evidence envelope is wholly authenticated, or r59 refusal now passes. **Rejected**: these are outside the single change and remain named gaps; no unrelated known failing check or r59 producer was rerun.
- Corpus admission: **no new `knowledge/` entry admitted**. `corpus/QUALITY.md` is absent; do not invent a quality bar or use this author-side lesson as a promotion/independence substitute.
- Outside spot-check: **not performed**. The inherited specialist reports are author-side, and no new specialist was dispatched through unauthorized routes. A non-author must independently sample at least one admit and one reject before discernment can improve.

## Outcomes and next action

Calibration improved locally for the replay criterion; coverage remained the same fixed four of eight selected saved-record families (command and exact outputs in `coverage-remeasurement.json` beside the acceptance evidence). Expansion unchanged; quality improved only for re-verification; discernment unchanged.

The round remains unadmitted. Operator-owned global role bindings must supply reviewer/critic/sentinel `@m_grok`, scribe `@m_composer`, connector `@m_antigravity` with `@m_zfl` fallback. A fresh interactive continuation then revalidates and dispatches the complete canonical 32-scope payload, preserving the same round and owned work. Missing lane craft/quality/index/registry files need a separately declared sourced restoration and outside spot-check; they are explicit debt, not silently filled with generic advice.

## Mistakes — kaika continuation (2026-10-19)

Mined from this lane's rejected, halted, honest-stop and corrected rounds plus
errata. Pointers are lane-root paths at base `8bbcb4e`; `MANIFEST.json` is the
fleet root's. `captured-by` names the `corpus/QUALITY.md` criterion this round
adds for the class, or `none` with the reason it is not a corpus-admission
criterion. Before this section, 0 classes were captured by any criterion
(`corpus/QUALITY.md` absent at `8bbcb4e`).

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M01 | readiness taken for a pass: CLI acquired, native session never opened | `LOG.md:26-30`; `corpus/lessons/2026-10-12-r1-provider-gap.md:3` | Q05 | readiness is a probe against the real surface with its exit or Evidence ID; acquisition or configuration is not capability |
| M02 | manual difference reading offered where the tool's explicit output was the claim (r7, 0/1 explicit relationships) | `LOG.md:97-100` | Q04 | score the tool's own output; label manual analysis separately |
| M03 | an unsupported or failed route invites an identical retry (r15 path collision, r17 Wakaru unavailable) | `LOG.md:189-192`, `LOG.md:211-214` | none — round-process halt rule kept in `LOG.md`, not an admission criterion | halt the route; resume only with changed input or a newly declared route |
| M04 | fixture premise stale after a byte shift: copied jump operand still pointed at the old offset (r25) | `LOG.md:299-300` | Q06 | after any byte-shifting edit, re-derive every absolute operand and offset before stating the premise |
| M05 | declared construction constant wrong: 160-byte directory (r51), unchanged entry counts (r52) | `LOG.md:614`, `LOG.md:625` | Q06 | byte-verify constants against the built fixture before the producer call; retain the failed input |
| M06 | first verifier substituted saved `entry_locations` for byte-derived values (r58) | `LOG.md:700-703` | Q03 | expected values come from bytes or an independent pin, never from the record under test |
| M07 | predicted refusal of an unpaired UTF-16 surrogate name falsified: REA accepted `A=\ude00B!` (r59) | `LOG.md:711-716`; `corpus/live/runs/round-59/reviewer.md:5,7` | Q07 | a predicted parser behavior is a hypothesis with spec-derived ground truth, classified either way |
| M08 | author count 7/7 directories; non-author byte oracle found 8/8 (r60) | `LOG.md:720` | Q08 | counts carry their command; a non-author byte-derived count supersedes author prose |
| M09 | ledger carried a wrong seed ID until the reviewer caught it (r18) | `LOG.md:224` | Q08 | identifiers are checked against the request record by command before commit |
| M10 | byte-offset role mislabeled: 556 is the name child-directory pointer, not a data-entry pointer (r30) | `LOG.md:383` | Q08 | an offset's role cites the decoded structure, not memory |
| M11 | saved JSON reformatted, so its SHA no longer matched the receipt's raw-output SHA (r35) | `LOG.md:458` | Q09 | keep saved records byte-preserved; a digest binds only the bytes hashed |
| M12 | a refusal's stated interval cause was not independently reproduced (r36); correctly kept out of claims | `LOG.md:475` | Q07 | claim a cause only after independent reproduction |
| M13 | receipt hashes or Evidence IDs nearly read as producer origin or native readiness | `corpus/lessons/round-1.md:16`; `LOG.md:704` | Q09 | a receipt shows internal consistency, not who produced the bytes |
| M14 | historical saved artifact path used as the input locator, so relocated replays failed (`r42`, `r47`, `r55: artifact`) | `corpus/lessons/round-1.md:8`; `reports/round-1/baseline.txt:14,17-18`; `SCORECARD.md:9,20-21` | Q03 | pin historical identity independently (`HIST`); read bytes via the current root (`ROOT`) |
| M15 | one verifier family's observation generalized to "evidence ids are f(content, path, params)"; kaidoku adjudicated it family-scoped (analyze/inspect are content+params keyed) | `LOG.md:720`; `SCORECARD.md:135`; `MANIFEST.json:2782` | Q10 | scope a finding to the observed family, operation, version and fixture; the correction is appended to `LOG.md` this round |
| M16 | a plan or a nine-role batch nearly counted as a completed round | `corpus/lessons/round-1.md:15` | none — protocol round-admission rule, not corpus admission | a round completes only with landed, measured, reported work |
| M17 | W1 ART research asserted 25/25 sources tier A, with count commands that return 0 on the committed dossier (it holds no `S###` table rows), and relied on ISO catalog abstracts in place of the standards | fleet repo `.ufo/waves/kaika-w1/revenger-art.md:21-24,45` at `5b471e4` | Q01 | tier per scope: an abstract is primary only for what it states; a count must reproduce on the committed artifact |
| M18 | knowledge entries admitted without `source:`, `verified-at:` and `recheck:` headers (2/2 entries) | `corpus/knowledge/seed.md:1-3`; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:1-3` | Q02 | every entry opens with the three headers and its coverage-map row |
| M19 | readiness facts left without a recheck went stale: node, npm, REA skill version and tool count, REA package pin, MCP registration, jadx/binwalk/unblob presence (8 of 13 probe-able facts) | `corpus/knowledge/seed.md:5,8-12`; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:8-12`; re-probe `.ufo/waves/kaika-r1/scout-freshness.md` | Q05 | each host fact carries `verified-at:` and a recheck command; re-probe before relying on it |

Classes 19; captured by a criterion 17; `none` 2 (M03, M16 — process rules).
Count: `awk -F'|' '/^\| M[0-9]+ /{n++; if ($5 ~ /none/) z++} END{print n, n-z, z}' corpus/lessons/round-1.md`.

## Gate — kaika continuation (2026-10-19)

Bar: `corpus/QUALITY.md` Q01–Q10 (committed before any entry landed, `a7acc20`).
Map statuses used for expansion eligibility are those frozen at `a7acc20`.

### Sources opened this round (contract rule 1)

Access date 2026-10-19 for every row. Quotes ≤25 words, verbatim.

- S001 `.ufo/waves/kaika-r1/scout-freshness.md` — own-work; table row 7: "server key `rea`, package `rea-agents@6.5.0`".
- S002 `~/.agents/skills/reverse-engineer-anything/SKILL.md` — frontmatter: `version: "42"`, `tool_count: 207`; line 37: "`npx -y rea-agents@6.7.0 doctor --client codex --json`".
- S003 https://www.swgde.org/wp-content/uploads/2024/04/2024-03-07-SWGDE-Minimum-Requirements-for-Testing-Tools-Used-in-Digital-and-Multimedia-Forensics-18-Q-001-2.1.pdf — §4 General Discussion: "This document bases its testing baseline recommendations on the function of the tool, not on the tool origin."
- S004 https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt/cftt-general-0 — "Methodology Overview", first paragraph: "The testing methodology developed by NIST is functionality driven."
- S005 https://swgde.org/wp-content/uploads/2025/09/2025-08-05-Best-Practices-for-Computer-Forensic-Acquisitions-17-F-002-2.1.pdf — §8 Verification and Preview: "The process of verification might not verify all data as read from the subject media."
- S006 https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf — Announcement §3 Explanation: "This Standard specifies secure hash algorithms - SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256 -".
- S007 https://www.dhs.gov/science-and-technology/nist-cftt-reports — body under "CFTT Reports": "Reports, organized by tool category, can be accessed and downloaded via the links below."
- S008 https://www.rfc-editor.org/rfc/rfc3227.txt — Abstract: "The purpose of this document is to provide System Administrators with guidelines on the collection and archiving of evidence".
- S009 https://learn.microsoft.com/en-us/windows/win32/debug/pe-format — "The .rsrc Section": "Resources are indexed by a multiple-level binary-sorted tree structure."
- S010 https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/ — §3.9.2, under D91: "isolated UTF-16 code units in the range D800..DFFF are ill-formed."
- S011 https://docs.python.org/3/library/codecs.html — Error Handlers table, surrogatepass row: "Allow encoding and decoding surrogate code point (U+D800 - U+DFFF) as normal code point."
- S012 https://en.wikipedia.org/wiki/Portable_Executable — lede: "The PE format supports storing the data required to load and start an operating system process".
- S013 `corpus/live/runs/round-59/inspection.stdout.json` — own-work; `normalized_result.resources[2].name`: `"name": "A=\ude00B!"`, `utf16le_hex` `41003d0000de42002100`.
- S014 `LOG.md:99` — own-work: "`items[]` does not explicitly identify removed named `checksum` import".

Openers: S003–S008 L2 `ExecForensicKnowledge`; S009–S012 L2 `ExecFormatKnowledge`;
S001 L2 `RevScout`; S002, S013, S014 L1. L1 re-opened S003, S005, S006 and S010 and
re-matched the quotes above against the fetched text. Row status changes old→new: none
(every row is new).

### Admission decisions

| candidate | map row (status at `a7acc20`) | decision | criteria |
|---|---|---|---|
| `knowledge/pe-resource-directory-layout.md` | C01 (uncovered) | **admit** | Q01 S009/S010/S013; Q02 headers; Q03/Q06/Q08 `## Reproduce` re-run by L1, output matches; Q05/Q07 n/a with reason |
| `knowledge/utf16-unpaired-surrogates-in-resource-names.md` | C11 (uncovered) | **admit after correction** | L1 gate caught a Q08 failure: the code units were stated as `<0041 003D 0000 DE00 0021>`; bytes give `<0041 003D DE00 0042 0021>` (command now in the entry). Corrected before admission |
| `knowledge/tool-validation-by-function-and-version.md` | C12 (partial) | **admit after correction** | L1 gate caught a Q01/Q08 anchor error: the function-of-the-tool quote is SWGDE §4, not §2 (re-opened PDF). Corrected; §5.3.3 named in the inference |
| `knowledge/digest-scope-versus-provenance.md` | C13 (partial) | **admit after correction** | L1 gate caught a Q08 misstatement: the hash≠origin rejection is a gate decision, not one of the six replay forgeries. Corrected |
| ART candidate `custody-transfer-ledger` (fleet `.ufo/waves/kaika-w1/revenger-art.md:53-60`) | none (frontier, adjacent) | **reject** | Q10: physical custody-transfer records are adjacent to this province's shipped-artifact ledgers; kept on `README.md` `## Frontier`; flip: a lane ledger needs transfer records |
| ART candidate `reproducible-finding-ledger` (ISO/IEC 27042 abstract, `revenger-art.md:80-87`) | C10 (partial) | **reject** | Q01: the only source is a catalog abstract and iso.org returned HTTP 403 this round; nothing tier A opened |
| ART candidate `long-term-fixity-evidence-records` (RFC 4998, `revenger-art.md:89-96`) | C13 (partial) | **reject** | Q01: RFC 4998 was not opened this round; the dossier itself says admit only if long-term archival is a lane need, and none is shown |
| universal rule "evidence ids are f(content, path, params)" (`LOG.md:720`) | C10 (partial) | **reject** | Q10: one family's observation; kaidoku adjudicated identity family-scoped (fleet `MANIFEST.json:2782`). Correction appended to `LOG.md` |

Admitted 4 (2 on uncovered rows, 2 on partial rows); rejected 4.
Count: `awk -F'|' '/^\| `knowledge|^\| ART|^\| universal/ {d=$4; if (d ~ /admit/) a++; else if (d ~ /reject/) r++} END{print a, r}' corpus/lessons/round-1.md`.

### Outside spot-check

Not performed in-round. The reviewer and critic L2s are the lane, not outside
discernment (`LEARNING.md` §Discernment is checked from outside). The
orchestrator's non-author spot-check (≥1 admit, ≥1 reject, ≥3 SOURCES rows
re-opened) is pending; discernment stays `unchanged` until it lands.

### Post-landing re-gate (critic L2 `RevCritic2-2`, `.ufo/waves/kaika-r1/critic-post.md`)

The lane's critic recommended demoting all four admits: every stated value was
true when re-derived, but four entries did not carry the derivation itself
(Q06/Q08). L1 agreed and fixed each before commit, then re-gated:

- C01 — `## Reproduce` hard-coded data-directory offset 216 and `.rsrc` base 512 → now derived from `e_lfanew`, optional-header magic and the section table; output re-run and matching.
- C11 — "differs at exactly offset 741" lacked its diff → full-file byte-diff command added (`1536 1536 [(741, '0xd8', '0x0')]`); the Python decode is labeled a manual reproduction on 3.14.7, separate from the cited 3.15.0 docs.
- C12 — the r7 0/1 score was cited to LOG prose → command over the saved `comparison.json` added (`15 0`); r8 1/1 cites the verifier's own output line.
- C13 — `recheck:` replayed r55–r57, not r35 → r35-specific re-hash plus receipt read; the receipt value is labeled receipt-reported; claim 3 marked a case-scoped inference and its gate source registered as S015 (`teaches` quote: lesson `:16` "these checks establish internal consistency only; no producer was called").

Re-gate: 4 admitted, 4 rejected (the critic agreed with all four rejects).
Critic's sampled re-opens S004, S009, S011: quotes verbatim, tiers honest.

### Mistake learned in this gate

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M20 | L1 gate applied Q08 to the values (re-derived and correct) instead of to the entry, so hard-coded constants and prose-cited counts passed | `.ufo/waves/kaika-r1/critic-post.md:9-12` | Q11 | the entry itself must carry each derivation; Q11 supersedes Q08 |

Mistake classes now 20; captured by a criterion 18; `none` 2 — same command as above.

## Post-review fixes (orchestrator adjudication, 2026-10-19)

Appended; rows above are not rewritten.

- SOURCES `recheck` changes, in place per contract rule 2 (census `validate` flagged E09, because rejected rows still need a date or cadence):
  - S008 `recheck` `—` → `on-release`. The flip condition depends on a successor RFC or BCP superseding RFC 3227.
  - S012 `recheck` `—` → `180d`. The flip condition depends on the article gaining a resource-tree section.
- Q11 applied to the four admitted entries: each now ends with an appended `## Provenance (Q11, appended 2026-10-19)` block. The block carries the command for every stated value and that command's observed output, including the web quotes re-matched by `curl` against S003–S006 and S010. Diffs are pure appends; `git diff | grep -c '^-[^-]'` returned 0 per entry.
- M14 pointer correction. The row cites `SCORECARD.md:9,20-21`, which is off by one and was stale after this round.
  - At `8bbcb4e` the failing-ledger sentence is `SCORECARD.md:19-20` ("The language and numeric multi-image verifiers still fail at their original artifact-path assertions"). `:9` is the r55 1/4 → 2/4 row.
  - Both lines describe the pre-C1 state, superseded by the kaika axes table (`SCORECARD.md:121-144`, `19b3174`).
  - Corrected evidence for M14: `reports/round-1/baseline.txt:14,17-18`; `SCORECARD.md:9,19-20` at `8bbcb4e`.
- C3 measure label, per adjudication: the freshness proxy counts **stored assertions re-verified** (flagged or confirmed against the live host). It does not count unique-fact currency.
