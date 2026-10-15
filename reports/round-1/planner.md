# Named saved-ledger replay: bounded planner report

## Evidence status and scope

This is source/data inspection and a proposed implementation skeleton, not execution evidence, a score award, admission, or a top-level round plan. No verifier, test, producer, PE executable, install, build, formatter, or CLI acceptance command was run. Only this report is written. The inherited brief, baseline, dispatch declaration, records, receipts, fixtures, SCORECARD and LOG are unchanged by this role. A dispatch declaration is intent, not proof of a live dispatch.

Observed below means read directly in source or saved data. Historical execution results are explicitly attributed to inherited reports; they were not reproduced. Predicted behavior is inference until the parent exercises it.

## Observations: exact mismatch and last-known-good contract

- `reports/round-1/brief.md:7-9` declares the single move: restore relocated r55-r57 replay while retaining historical identity and full byte-derived comparisons. `reports/round-1/baseline.txt:4-8,18` records the existing lane-root exit 1, `AssertionError: r55 artifact`. This supplied failure is ground truth, not a result rerun here.
- `corpus/verify_named_multi_icon_states.py:7` sets `ROOT=Path(__file__).resolve().parent`. At `:65`, fixture bytes and saved report/receipt bytes are read beneath that local corpus root. This is the correct relocation-independent read strategy.
- At `:67`, the saved artifact is compared with `dict(path=str(fixture), sha256=digest, bytes=len(d))`, but `fixture` is the relocated local read path. `compare_normalized` repeats the conflation at `:57-63`, especially `:58`. At `:69-70`, the expected historical receipt command also interpolates the relocated path. Fixing only the first assertion would leave the full normalized comparison and then the receipt comparison wrong. The forged-claim comparison at `:92` passes the same local path and must migrate with the comparator contract.
- `corpus/live/runs/round-55/inspection.raw.json:1` records the historical path `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe` in `normalized_result.artifact.path`, `subject.local_path`, `parameters.path`, and `locations[0].path`. The saved receipt's exact command is at `corpus/live/runs/round-55/receipt.json:2`. Its path is historical, not this checkout's corpus path. r56/r57 have the same historical prefix with their respective fixture suffixes (`inspection.raw.json:1`, `receipt.json:2` in each round folder).
- The existing enforced identity surface is explicit: fixed digest/Evidence ID pairs at verifier `:56`; local byte length/hash, operation, subject digest at `:66`; normalized artifact at `:67`; complete normalized equality at `:57-63,68`; receipt command/status/duration/Evidence ID/fixture hash/raw stdout hash at `:69-70`. The other envelope path fields are visible saved data, not currently independently asserted by this verifier. Do not describe this move as verification of the entire Evidence envelope.
- Last-known-good is historical and fixture-scoped: `LOG.md:697-705` records the repaired r58 contract and reported successful run, including rejection of an earlier implementation that omitted name metadata and copied saved ancestor locations. `corpus/live/runs/round-58/reviewer.md:7-16,35-48` records full normalized matches, byte-derived name/ancestor locations, exact deltas and four mutation rejections. These are inherited reports, not fresh or outside-discernment evidence for this round.

## Proposed task axes, limited to this move

1. **Calibration / portable saved-ledger repeatability:** local corpus relocation must not change the historical identity expected by the verifier. A pass must retain byte-derived semantics and rejection strength, not merely avoid `r55 artifact`.
2. **Mission coverage as an unchanged guardrail:** the move adds no producer record or artifact family. Preserve the declared 3/7 record-presence census; do not claim a new route.

Historical depth findings remain retained and unchanged; depth is not an active improvement axis here. No additional feature, parser policy, sibling-verifier repair, producer rerun or corpus rewrite is proposed.

## Pin-vs-local-read invariant and minimal skeleton

For round `r`, keep two distinct values:

```python
ROOT = Path(__file__).resolve().parent
RECORDED_ROOT = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
local_fixture = ROOT / f'fixtures/pe-r{r}/fixture.exe'
recorded_fixture = RECORDED_ROOT / f'fixtures/pe-r{r}/fixture.exe'
```

This is a proposed sketch, not an applied edit. The recorded root is a source-pinned historical identity, reviewed against the inherited records and brief; it is never taken from the report, receipt, environment, CWD, or current checkout. Do not resolve it, check its existence, or read fixture bytes there. Only `local_fixture` supplies bytes. Only `recorded_fixture` supplies the expected artifact path and exact historical command string.

Retain the current comparator and decoder design: rename the comparator's path argument to make its recorded-identity meaning explicit; build its expected artifact with that argument. Keep `actual == expected` for the complete normalized result and its limitations, rather than deleting/normalizing away `artifact.path` or copying any expected field from `actual`. Keep pinned digest/Evidence ID values and receipt raw-byte hashing unchanged. Update both the positive comparison caller and forged-claim caller to pass the recorded path. No compatibility shim or second comparison convention is needed.

### Ordered steps with evidence

| Step | Bounded action | Source evidence / later gate |
|---|---|---|
| 1 | Separate historical identity construction from local byte lookup, leaving `ROOT` local. | Verifier `:7,65`; brief `:7-9`; all three saved inspections `:1` and receipts `:2`. |
| 2 | Apply the recorded identity consistently to the artifact assertion, full-normalized comparator, receipt command and forged-claim comparator call. | Verifier `:57-70,86-95`. These are the four affected identity-bearing paths; keep byte decoding `:14-55` and checks `:66,70-85` intact. |
| 3 | Establish the representative r55 positive case below before interpreting the other states. | Existing pinned r55 pair `:56`, r55 JSON `:1`, receipt `:2-7`; parent must observe real relocated CLI behavior, not infer a pass from this sketch. |
| 4 | Generalize the same identity split through existing `EXPECT` iteration to r56/r57 and retain exact state/delta/forgery assertions. | Verifier `:75-95`; saved r56/r57 JSON `:1`; inherited r58 review `:35-48`. No independent per-round special case is needed. |
| 5 | Parent exercises the existing requested relocation and tamper gate after integration. | Brief `:24`: lane root, unrelated CWD, isolated copied corpus under a path containing spaces and non-ASCII; unchanged historical inputs; required forged fields rejected. This role executes none of these checks. |

## Representative r55 case, then r56-r57

**r55 data walk (observed saved values and source expectations):**

1. Read `ROOT/fixtures/pe-r55/fixture.exe` and `ROOT/live/runs/round-55/{inspection.raw.json,receipt.json}`. Current source `:65-66` expects 1536 fixture bytes and SHA-256 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`, with Evidence ID `ev_db785aec4caaa20630a96a8a3b250ff3aae9c0fa454ff36abe4415725fa22e79`. These match the saved JSON/receipt fields read here; this role did not recompute fixture hashes.
2. Compare the artifact against the historical r55 path above, the fixed digest, and local byte length. Construct the full expected normalized result from local decoded bytes plus that historical identity, retaining all fields and limitations.
3. Require the saved receipt command exactly as written at receipt `:2`: `npx -y rea-agents@6.4.0 inspect-pe-resources /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe --format json`. Its recorded stdout hash is `54ffdeab7108895404efa01edb400c9bc32c36c4f85540babed2f5241137f860` (`:5`); the verifier must still compare the receipt to the actual saved raw JSON bytes, not JSON reserialization.
4. Preserve one group at resource index 2, three resources, two ordered images; source `:71-82` requires `(1,[0],0,True)` then `(2,[1],1,True)`. Named group `A😀B!` retains raw UTF-16LE `41003dd800de42002100`, name location `(736,12)`, and byte-derived ancestor entries `(536,8),(592,8),(664,8)` (saved JSON `:1`; decoder `:25-41`; r58 review `:35`). A relocation pass that drops these comparisons is not this fix.

**Generalization:** r56/r57 change only the round suffix used to construct local and recorded paths; keep their separate existing pinned SHA/Evidence ID pairs (`:56`) and receipt hashes (`receipt.json:5` in each folder). Existing source `:76-85` requires:

| round | second image state `(id,candidates,same_language,size_matches)` | exact delta against r55 |
|---|---|---|
| r56 | `(3,[],None,None)` | `(offset 928, 2, 3)` |
| r57 | `(2,[1],1,False)`; declared 47 versus payload 48 bytes | `(offset 924, 48, 47)` |

The first image stays `(1,[0],0,True)` in both. Retain the in-memory r56 forged candidate `[1]` and r57 forged size `True` rejection paths (`:86-95`), passing the recorded identity to the same full comparator.

## Falsifier and verification boundary

The new claim is falsified if a correctly copied corpus fails solely because its current path/CWD differs, or if portability is obtained by accepting a forged historical artifact path or receipt command. It is also falsified if any required candidate, size, name-location or ancestor-location mutation is accepted, or historical inputs are rewritten. For an artifact-path challenge, refreshing the receipt's stdout hash for the mutated JSON must not make the forged historical path acceptable: the independent source pin must reject it. A hash mismatch alone would not demonstrate that path check. Receipt-command tampering must likewise fail even though the fixture and saved stdout remain unchanged.

The parent's requested real CLI runs in isolated copies must establish these results; mocks, a function-only happy path, or this source review are insufficient. Baseline file entries establish inherited measurements only. No current relocated success, mutation rejection, input-hash preservation, or live producer availability has been observed by this role.

## Bounded rubric assessment and scoring defects

- `SCORECARD.md:3-10` deliberately leaves all three imported scores unmeasured. Historical narrative and row counts are not pre-existing numeric scores. The new proxy is a newly declared rubric (`brief.md:13-16`), not a retroactive numerical interpretation of imported claims.
- Calibration's four-script denominator is explicitly enumerated at `brief.md:15`. The inherited census (`baseline.txt:13-23`) reports only `verify_icon_states.py` succeeding among those four, so its baseline arithmetic is `10 * 1/4 = 2.5`. The target arithmetic is `10 * 2/4 = 5.0` only if the parent observes the repaired script passing while the other results are retained. The broader inherited 7/10 becomes an expected 8/10, not an observed result here.
- **Measurement limitation:** the baseline census exercised lane-root commands, not all unrelated-CWD and relocated-copy cases. Thus 1/4 is observed inherited lane-root runnability, not already-demonstrated portability across the full new gate. Labeling it universally portable would overstate its evidence.
- Coverage is `10 * 3/7 = 4.29` rounded, with native-static, JavaScript and archives present (`baseline.txt:25-36`). It is unchanged by this move. The census code counts JSON with an Evidence ID and non-null normalized result and maps selected operation names; it does not inspect receipts/exit codes or authenticate origin. Calling that count **authenticated successful producer families** would be a scoring defect. The defensible meaning is saved successful-shaped record presence in seven declared buckets, not verified producer success or current runtime capability.
- The two proxy scales have different denominators and predicates. Calibration is numerically lowest under this declared rubric, not demonstrated to be the globally weakest RE competence. Counting one repaired script does not quantify test strength, producer authentication, or Unicode policy quality. The frozen four/seven denominators prevent choosing new denominators after results; do not broaden this task to improve their coverage.
- Imported calibration's narrative includes r58 but its last-change label remains r54 (`SCORECARD.md:10`), and its halt status is not represented there as clearly as in `LOG.md:716,721`. Treat those as imported summary limitations, not grounds to erase the halt or infer a new pass. This report makes no scorecard edit or award.

## Newly declared replay criterion versus halted r59 prediction

`LOG.md:707-711` declares and falsifies a different prediction: changing byte741 from `d8` to `00` must produce explicit malformed-Unicode refusal without successful Evidence. `:714-716` preserves that r59 instead returned successful Evidence `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db`, with raw `41003d0000de42002100` and an unpaired surrogate, while strict UTF-16LE rejects those bytes. Its expected refusal remains unmet; calibration was harmed relative to that declaration, not proven regressed versus a prior malformed-name baseline. `:721` retains the halt through r60.

This brief explicitly declares portable replay of the already-valid r55-r57 saved ledger as a new repeatability criterion (`brief.md:7,16`). It neither changes the malformed-name parser nor regrades r59. Keep the strict decoder at verifier `:35`; no permissive decoding, surrogate policy, r59 fixture admission, producer retry, or validity claim belongs in this move. A replay gain cannot cancel the recorded Unicode-refusal falsification.

## Assumptions, unknowns and hard blockers

- **Unverified continuity assumption:** the inherited baseline identifies commit `286033c5f2b1683fb538e86e15667709bb49b054`; this role did not inspect git state or independently prove unchanged historical bytes. The parent/input-ledger evidence must establish preservation. No prior live dispatch is assumed from `dispatch.json`.
- **Unknown until parent acceptance:** actual behavior after implementation under all requested locations and forged-record challenges. Source consistency predicts the small identity split resolves the relocation conflation; it is not execution proof.
- **Evidence boundary:** three authored PE32+ fixtures and saved-record internal consistency only. Receipt/hash agreement is not authentication of historical REA origin. General PE correctness, malformed Unicode policy, OS loading/rendering/fallback, native providers and runtime readiness remain unproven. This author-side planning review is not independent promotion/outside-discernment verification.
- **Hard blockers for the bounded skeleton:** none found in inspected inputs. Implementation and real acceptance evidence are outstanding obligations for their assigned owners, not reported successes or planner execution.

## Factual erratum — corrected current rubric and frozen baseline

This append supersedes the earlier advice to preserve 3/7 as the **current** coverage guardrail and the corresponding four/seven-denominator wording. The parent's live clarification at `reports/round-1/brief.md:26-30` corrects the inherited omission of already-recorded EVM evidence: the current fixed taxonomy is eight families, including `inspect_evm_interface`, with coverage **4/8 = 5.0/10 before and expected unchanged after**. The inherited 3/7 = 4.29 remains a historical measurement, not the current score. Calibration **1/4 = 2.5/10** remains the lowest bounded proxy. The saved-record-presence, non-authentication and non-readiness limitations still apply.

`reports/round-1/measured-before.json:3-4,7,12,15` now records the parent's baseline measurement from an isolated `git archive` of commit `286033c5f2b1683fb538e86e15667709bb49b054`, not merely the inherited lane-root census. Its retained output reports the same seven passing replay scripts, calibration 1/4 and the corrected coverage 4/8. This is newly read parent measurement evidence, not execution by this planner; it does not itself establish every later unrelated-CWD, copied-path or mutation acceptance case. No historical inputs or other report sections were edited by this append.
