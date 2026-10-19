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
