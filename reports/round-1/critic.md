# Fleet round-1 critic — relocated saved-ledger replay

## Review boundary and evidence status

Read-only source review of `reports/round-1/brief.md`, `baseline.txt`, `SCORECARD.md`, `SHONEN.md`, `LOG.md:696–721`, the targeted verifier, historical r55–r57 receipts, r55 saved Evidence, and the EVM counterexample below. Sole authored file: this report. No verifier, acceptance command, producer, fixture, build, lint, test, formatter, or other runtime was executed. Baseline execution results below are **recorded observations in the inherited baseline**, not independently reproduced observations by this critic. This L2 review is author-side evidence, not outside discernment or promotion verification.

The verifier references below describe the source snapshot read for review: `corpus/verify_named_multi_icon_states.py:1–97`, before any integration repair. They are not an assessment of an unseen final patch.

Impacted axes: calibration (honest bounded claims and historical identity checks), coverage (taxonomy and denominator), and the historical depth guardrail (no new semantic finding). Runnable saved-record portability is the selected calibration **proxy**, not the full meaning of calibration (`../AXES.md:9–16`).

## 1. “Calibration is lowest” is conditional, and coverage omits an observed family

**Observed sources.** `SCORECARD.md:3–10` explicitly leaves all three scores unmeasured without a quality rubric. `brief.md:13–16` then declares seven-family coverage and four-script repeatability proxies. The inherited baseline records coverage 3/7 and calibration 1/4, and lists seven `inspect_evm_interface` records (`baseline.txt:25–34`). Its family mapping has no EVM bucket (`baseline.txt:31`). EVM is not hypothetical: `corpus/live/runs/round-22/inspection.json:1` records `inspect_evm_interface`, and `round-22/reviewer.md:18–26` describes bounded static selector/destination evidence. `SCORECARD.md:8–10` already cites EVM depth, coverage and calibration work.

**Counterclaim.** “Coverage is 3/7 across the domain's artifact families” hides an already-observed surface. The command's reported 3/7 is faithful to its selected seven buckets, but those buckets are incomplete. Neither that fraction nor a comparison with script counts independently establishes the globally weakest expertise axis. The different proxy units and equal weighting are declared conventions, not an empirically calibrated common competence scale.

**Smallest safe correction.** Keep `baseline.txt` immutable as historical evidence. Explicitly correct the current proxy to **eight selected route families including EVM**, with **4/8 = 5.0 both before and after**; explain why this differs from the inherited 3/7 = 4.29. This is a census/rubric correction, not a second functional move or newly acquired coverage. If retaining the original number for historical comparison, label it “incomplete seven-family proxy,” never exhaustive coverage. Eight selected buckets are still not proof of exhaustive domain coverage.

**Required wording:** “Under the newly declared bounded proxies, calibration starts at 1/4 = 2.5, lower than corrected selected-family saved-record presence at 4/8 = 5.0. Coverage is unchanged by this move. The inherited 3/7 omitted the already-recorded EVM family.”

The corrected denominator does **not** falsify the selected move: 2.5 remains below 5.0. The fixable defect is the omitted surface and unqualified ranking, not the choice to repair this verifier. A post-repair 2/4 = 5.0 would tie the corrected coverage proxy; it would not establish saturation.

## 2. One bounded move is not “fix all verifier failures” or overall competence

**Observed sources.** `baseline.txt:13–23` records 7/10 runnable verifiers; the failing scripts are language, multi-image and named multi-image ledgers. Of the four selected PE cross-record scripts, only `verify_icon_states.py` passes. `brief.md:15` explicitly permits changing only the named verifier and predicts 2/4 and 8/10. `../MISSION.md:38–46` and `../AXES.md:25–39` require one verifiable axis-move, not universal repair.

**Strong counterexample.** Even if the named ledger succeeds after relocation, the two other pre-existing failed PE ledgers remain. Therefore “relocated corpus replay restored,” “all historical ledgers portable,” or “calibration fixed” would be false as general claims. Conversely, leaving those failures named and unchanged is not itself a defect in this deliberately bounded repair.

**Smallest safe correction.** Change only the named ledger's local-versus-historical path handling; keep the other failures visible. State the expected arithmetic conditionally until the parent's real acceptance results exist. Do not convert 1/4→2/4 into “50% overall RE competence,” nor treat 8/10 as an independent second measurement of the same magnitude: these are overlapping script inventories. Script exits are fixture-scoped outcomes, not statistically independent competence samples.

**Required wording:** “This restores relocation-safe replay for the existing r55–r57 named two-image ledger only. If acceptance succeeds, selected ledger repeatability changes 1/4→2/4 and the broader existing-verifier census 7/10→8/10; two other relocation failures remain. No new RE route, semantic depth, general parser validity or runtime capability is established.”

Historical depth may be retained as wrong-fit for this lane's active assignment (`brief.md:13`), but “saturated” would require evidence not supplied by a path repair. `SCORECARD.md:13` currently says no axes are retired; any current-axis change must preserve the distinction between historical evidence and newly declared scoring.

## 3. Relocation must not make the record its own historical identity oracle

**Observed defect.** In the reviewed verifier, `ROOT` is the current script directory (`:7`), local bytes are read through it (`:65`), and that same current fixture path is required in the saved artifact (`:58`, `:67–68`) and saved command (`:69–70`). The r55 receipt instead records the historical corpus path (`corpus/live/runs/round-55/receipt.json:2`); r56 and r57 receipts do likewise. The inherited failure is `AssertionError: r55 artifact` (`baseline.txt:4–8`). Thus relocation changes the expected saved identity even when the saved record itself is unchanged.

**Strongest static counterexample to an unsafe repair.** Consider a forged copy whose normalized artifact path is replaced by `/tmp/forged/fixture.exe`, whose receipt command is rewritten to that same path, and whose receipt stdout hash is recomputed over the forged JSON. Fixture bytes, fixture digest, normalized resource tree and hard-coded Evidence ID can all remain unchanged. If a repair obtains its expected historical path from the artifact under test, or merely cross-compares the saved command against that untrusted path, these alterations become self-consistent. The saved Evidence ID equality check does not recompute path-sensitive identity. This is an **inferred acceptance failure of that unsafe design**, not an executed mutation result and not a claim that the final patch uses it.

**Smallest safe correction.** Separate two authorities explicitly:

- Current `ROOT` determines where fixture bytes and saved files are read.
- One independently pinned historical corpus root determines the expected original artifact path and the complete original receipt command for each r55–r57 record: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus` plus the fixed fixture suffix.

Never derive that historical expectation from a saved field under test, the current CWD, or a newly relocated path. Never rewrite inputs or manufacture new Evidence IDs. Preserve pinned fixture digests and Evidence IDs (`:56`, `:66`), byte-derived complete normalized equality (`:25–55`, `:57–63`), exact deltas (`:83–85`), receipt fields and stdout hash (`:69–70`), and candidate/size mutation rejection (`:86–95`). `LOG.md:700–704` already documents why substituting saved ancestor locations for decoded locations is unsound; do not reintroduce that shortcut.

Parent acceptance must actually challenge historic artifact path and receipt command independently, as well as candidate, size, UTF-16 name location and ancestor location, while keeping the existing inputs unchanged (`brief.md:24`). No such result is asserted by this review. A command-only mutant need not change stdout, so retaining exact command equality matters independently of the stdout-hash check.

**Existing limit, not extra repair scope.** The read source checks the subject digest, but does not separately assert every historical path-bearing envelope field, such as `subject.local_path`, `parameters.path`, and `locations` (`:66–70`; r55 `inspection.raw.json:1`). Do not describe the bounded repair as complete authentication of every Evidence-envelope field. The required preserved baseline authority is the pinned normalized artifact identity plus exact receipt command and existing checks; a broader envelope validator is not silently part of this move.

## 4. Saved hash consistency cannot authenticate the historical producer

**Counterclaim and evidence.** A person able to write a saved report and receipt can compute a matching SHA-256 and copy the expected Evidence ID. In the verifier, `receipt['stdout_sha256'] == H(raw)` checks consistency of those local files (`:70`), not a signature, independent trusted execution record, or origin attestation. The r57 historical review explicitly distinguishes this boundary (`corpus/live/runs/round-57/receipt-review.md:12–18`); `LOG.md:704–705` says historical origin cannot be authenticated by saved receipt hashes. Path-sensitive Evidence identity is also recorded in `LOG.md:720`, not a license to regenerate identity after relocation.

**Smallest safe correction / required wording:** “Fixture bytes, saved normalized results, pinned historical artifact path, Evidence IDs and receipt command/hash are internally consistent under the bounded checks. Historical producer identity, execution time and trusted origin remain unauthenticated. No producer rerun or provider readiness is asserted.”

False provenance would be a substantive contract violation, not a harmless terminology tradeoff for the canonical Rust judge to overlook.

## 5. The r59 validity/refusal criterion remains falsified and halted

**Observed sources.** `LOG.md:707–708` declared refusal of a malformed surrogate name with no successful Evidence ID. `:711` records success instead; `:714–716` preserve the one-byte cause, unpaired surrogate, successful saved Evidence, unmet prediction, and halted validity/refusal progression. `:719–721` explicitly left that halted calibration criterion untouched in r60. `brief.md:16` declares a different repeatability criterion and forbids regrading r59.

**Strong counterexample.** All three valid-name r55–r57 records may replay perfectly while the r59 malformed-name producer still succeeds rather than refusing. Those facts are compatible. Improving replay therefore cannot restore the falsified Unicode-validity prediction, resolve the parser gap, or justify silently changing what “calibration improved” historically meant. The verifier's strict local UTF-16 decoding (`:35`) is not proof that the producer refused r59.

**Smallest safe correction / required wording:** “Fleet round-1 measures a newly declared saved-ledger repeatability criterion only. Historical r59 remains unmet and halted for the malformed-name validity/refusal expectation; no regrade, policy ruling, producer fix or general calibration recovery is claimed.”

An unqualified green calibration row that erases this distinction would be false provenance of improvement. Preserving the historical failure while declaring this separate proxy is the bounded, fixable alternative.

## 6. Same-lane reviews are not promotion authority

**Observed sources.** `SHONEN.md:3–6` bounds historical checks to named evidence and fixture scopes. `:8` explicitly withholds rank promotion and native readiness, reserves the operator-owned roster decision, and disclaims manifest/global-rank changes. `brief.md:22` classifies these subagents as author-side evidence. Existing SHONEN checkboxes do not become newly verified by this round's path repair.

**Counterclaim.** A nine-role same-lane batch, a non-author report, or passing local saved-ledger replay cannot itself establish outside discernment, independent promotion verification, authenticated producer provenance, or arbitrary-target expertise. Role diversity and reviewer labels do not supply those missing authorities.

**Required wording:** “L2 reports are author-side review evidence for this bounded change. They do not grant promotion, substitute for an independent outside verifier, change global rank, or establish producer/native runtime readiness.”

## Bounded safe conclusion

The source supports a narrow local/historical-path separation as the relevant repair; it does not yet prove final acceptance. Retain the exact historical identity and byte-derived comparison authorities, correct the omitted EVM census transparently without claiming a coverage gain, and report only the parent's subsequently observed acceptance outcomes. A successful result can support improved portability of this one existing saved-record ledger under a declared proxy, with historical depth and coverage unchanged and r59's separate failure preserved.

**Unproven assumptions / unknowns:** final patch and direct CLI outcomes; portability under unrelated CWD and spaced/non-ASCII copies; actual negative-mutation outcomes after integration; unchanged-input hashes after integration; arbitrary PE correctness; producer origin; current provider/runtime availability; exhaustive domain coverage; independence/promotion authority. None is filled in by this critic's source review. The canonical judge, not this L2 report, owns any admission or tradeoff decision.

## Integration clarification observed during review

After the critique above, the parent added `brief.md:26–28`, explicitly adopting the fixed eight-family proxy, preserving the inherited 3/7 measurement, and stating 4/8 = 5.0 before with coverage expected unchanged. This addresses the census-wording defect in the brief; it is not an executed recount, a coverage gain, or evidence that any verifier acceptance has completed. The other boundary and wording requirements above still apply to the integrated scorecard, log and final report.
