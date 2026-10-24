# R63CriticClaims — frozen-contract attack

## Review conclusion

**Verdict: SOUND as a conjunctive claim-and-admission contract, not as a counter-only gate.** A cheap tree can print all three target numbers without doing the claimed substantive work. It cannot satisfy the frozen claim text: the independent admission, real-run/oracle, and frozen-fix requirements explicitly reject that tree. Treating printed targets or `HOLDS_OK=yes` as admission would introduce an enforcement hole the contract does not authorize. This is a scoped critic finding, not a canonical judgment or admission.

Axes examined: **coverage K**, **coverage F**, **calibration C3**; cross-cutting **provenance**, **causal separability**, and **preservation/freshness holds**. These are review dimensions, not replacements for the frozen criteria.

### Evidence key

All line references below resolve through these absolute paths:

- **C:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/claims.md` (frozen contract, supplied freeze commit `54ab973c021cc62ca65dcbe2cbfabe3235d5ee38`).
- **P:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure.py`.
- **B:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure-before.log`.
- **R:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md` (coverage row and known-gaps text read before integration).
- **E:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/2026-10-12-rea-readiness-checklist.md`.
- **Q:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md`.
- **S:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/SCORECARD.md`.
- **N:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_named_multi_icon_states.py` (original receipt conjunct observed at initial read, line 72).
- **I:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_states.py` (original receipt block observed at initial read, lines 142–146; another assigned seat subsequently changed this working-tree file).

## 1. Do-nothing control: what it proves, and what it does not

The literal unchanged-base control is adequate to show the starting tree misses all three targets: **B:4–6** records K `6/14`, **B:8–9** F `4/8`, and **B:21–26** C3 `0/2`. **B:37–40** simultaneously records the holds green and probe exit 0. Thus exit 0 was never a claim-pass verdict, even at registration. This review uses that committed receipt; it did not rerun it.

The stronger adversarial question has a different answer: **yes, labels can be made green without substantive claimed work**. The following is a compact four-file counterexample specification, not an applied tree or an executed result.

### K: status-only promotion already has an existing backing file

**P:32–34 does require actual files to exist.** It extracts `knowledge/[\w.-]+\.md` only from the knowledge cell, requires at least one match, and applies `is_file()` to every matched path. A held C06 pointing exclusively to a nonexistent new entry would not increase `K_HELD_BACKED`.

But the stronger premise “no NEW entry means a README flip fails backing” is false. **R:35** already points C06 at `knowledge/2026-10-12-rea-readiness-checklist.md`. That file exists (**E:1–18**); **R:54–57** explicitly says this older entry has not been re-gated. Keeping that existing reference and changing only C06's terminal status from `partial` to `held` satisfies the backing predicate. **[INFERENCE from P:26–34 and R:30–43]** This yields `K_HELD=7/14` and `K_HELD_BACKED=7/14` without creating the round-63 candidate. The regex checks existence, not newness, candidate identity, derivations, or admission.

**Contract barrier:** **C:21** requires “one newly admitted entry”; **C:38–41** requires “named fresh-seat Q01–Q13 pass decisions from reviewers other than the candidate author/corrector” and says “the K probe measures existence, never quality.” The status-only tree fails those requirements. An existing ungated checklist cannot become the specified new entry by relabeling its row.

**Impacted axes:** K coverage, provenance, admission independence. **Smallest safe correction:** retain the existing two-part gate: verify the exact new candidate and its fresh decisions before the sole integrator flips C06; never use `K_HELD_BACKED` as a substitute. Do not rewrite the frozen counter this round.

### F: invented Evidence ID and empty normalized result are counted

In the hypothetical new file
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/not-a-run.json`, place:

```json
{"evidence_id":"invented","operation":"inspect_firmware_regions","normalized_result":{}}
```

**P:38–50** accepts any dictionary with a truthy `evidence_id`, non-null `normalized_result`, and the recognized top-level operation. It checks no Evidence-ID format, producer receipt, command execution, fixture, result schema, or oracle. The recursive scan is not itself restricted to the round-63 directory. **[INFERENCE]** That JSON adds the previously absent firmware family and prints `F_COVERAGE=5/8`; no fixture or producer run is needed for this printed value. A JSON `false` normalized result would also pass the `is not None` predicate.

**It does not satisfy the claim text.** The decisive quote is **C:45–50**: F advances “**iff**” the saved record “**is the output of one real `npx -y rea-agents@6.5.0 inspect-firmware-regions <path>` run (receipt committed with command, exit code, fixture SHA-256, stdout SHA-256, Evidence ID)”. **C:50–55** additionally requires byte-oracle agreement and committed generator plus `truth.json`. **C:105–108** repeats that the F count requires the byte-oracle agreement receipt. A fabricated record, even paired with a fabricated internally consistent hash receipt, does not make a real run happen. **Q:21 (Q09)** separately forbids treating matching hashes as proof of producer origin.

**Impacted axes:** F coverage and false provenance. **Smallest safe correction:** before crediting F, resolve the actual run receipt to its saved stdout and authored fixture, verify the digests/Evidence ID and enumerate every reported region against truth. Report F presence and the real-run/oracle decision separately. The counter is only the presence half.

### C3: source-presence canaries can counterfeit attribution

For a counting-only spoof of the original two scripts, insert one top-level assertion before each script's main invocation, retaining all existing logic:

Named script:

```python
assert ("receipt[" + "'command']==command") in Path(__file__).read_text(), 'forged receipt'
```

Icon-states script:

```python
assert ("receipt[" + "'fixture_sha256'] == expected_hash") in Path(__file__).read_text(), 'forged receipt'
```

Both original scripts already import `Path`. Splitting the string keeps the assertion from adding another textual mutant match. The original conjunct remains the sole match; after the frozen deletion its assembled text is absent. **[INFERENCE from P:125–164 and the original N/I receipt sites]** Controls retain their original behavior; each mutant instead ends with `AssertionError: forged receipt`, meeting the probe's nonzero-plus-last-line-substring attribution test. That can print `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` without a `receipt_ok` helper or a deep-copied forged receipt. This tests source text, not rejection of receipt data.

**Contract barrier:** **C:77–88** mandates the specific helper refactor, preservation of every existing conjunct (including the round-36 exemption), the specified deep-copy field forgeries, and all existing saved-input assertions. The canaries omit those required changes. Substring attribution alone is not the frozen fix.

**Impacted axes:** calibration, causal attribution, preservation of old assertions. **Smallest safe correction:** review the final diff against the frozen fix sentences as well as reading the attributed tally. Reject source-inspection canaries or unconditional error-message substitutes; no change to the frozen mutation or matching rule is authorized.

### Combined cheap tree

**[INFERENCE, NOT RUN]** The C06 status-only change, one new JSON file, and one canary line in each of the two original verifiers constitute a four-file tree that can print K `7/14`, F `5/8`, and C3 `2/2` while omitting the new knowledge entry, firmware fixture/real producer call/oracle receipt, and specified receipt controls. Existing replay inputs need not change. This demonstrates a counter-only false positive, **not a contract-valid improvement**: each component violates an explicit independent condition above. No such tree was created or executed by this critic.

## 2. Falsifiability of each frozen target

| Claim | Independently falsifiable condition | Counter boundary |
|---|---|---|
| C1 / K | K remaining `6/14` falsifies numerically (**C:21–22**). No specified new admitted entry, a failed Q criterion, or missing fresh non-author decisions also prevents admission even if raw K reaches 7. | **P:24–34** exposes row status/backing only; it does not decide quality. |
| C2 / F | F remaining `4/8` falsifies (**C:45–52**). An invented output, missing real pinned-version run/receipt, absent committed fixture oracle, or any reported-region mismatch fails the conjunctive target even if F prints 5. | **P:36–53** measures family presence only. |
| C3 / calibration | Final attributed kills must be `2/2` with passing controls and the frozen fix. `0/2` or `1/2` misses the target; a crash/unrelated last line is not an attributed kill (**C:69–88**). A non-unique mutation site makes the probe could-not-evaluate (**P:131–139,149–154,183**), not a pass. | The phrase test is narrower than proving the required data-forgery control; final code review remains necessary. |

One scope limit must stay explicit: **C:50–52** quantifies over regions the record reports, not over all truth members, and does not expressly demand a nonempty region list. Empty output makes that comparison vacuous. This is a bounded **record-presence/soundness**, not completeness or detection-recall, criterion; **S:21–24,132,138–140** supports that distinction. It still requires the real run and the authored fixture. Do not promote an empty result into a capability or complete-detection claim. If nonempty/all-member detection were intended instead, that would require a new pre-registration, not a post-hoc strengthening here.

## 3. Separability and overlap

The K/F split is not invented for round 63: **S:132–140** records the two criteria and the reason. Their parsed scoring inputs are disjoint: README status plus referenced knowledge-file existence for K (**P:25–34**), versus JSON dictionaries under saved runs for F (**P:38–50**). They share an archive root, not a counted datum.

- C1 uses an already-saved archive record as observation material; archives are already present in **B:9**. Admitting its manual knowledge entry need not add any family or change F.
- C2 adds a firmware saved record under a new round-63 path. C07's README status must remain unchanged (**C:113–115**), so F can move without K.
- C3 changes the two named verifier programs, not the README or a saved-record JSON. Its controls consume old, byte-preserved fixtures/receipts, so its attributed tally can improve without either coverage claim landing.
- The same old archive evidence supports C1's comparison and existing replay holds; that is shared evidence, not a second family gain. Likewise C3's passing controls overlap the calibration/replay holds and must not be counted as another improvement.

There is a label hazard, not a causal dependency: new **claim C2** means firmware/F, whereas printed **`C2_*`** labels are the inherited round-61 calibration holds (**C:95–98; P:72–122**). The firmware claim is not established by `C2_CONTROLS_PASS` or `C2_RECEIPT_B_KILLED_ATTRIBUTED`. Qualify claims by criterion/printed label in the final report. K and F remain two declared coverage subcriteria, not evidence of two unrelated general-domain competencies or saturation.

## 4. Universal obligations not certified by the counter

The frozen counter never claims to certify all these obligations. They must remain explicit final review items; a green `HOLDS_OK` does not discharge them.

| Frozen obligation | What the probe actually checks / omits | Smallest safe final check |
|---|---|---|
| Every old `corpus/live` / `corpus/fixtures` byte outside new round-63 paths is unchanged; prior rejected material and round-62 evidence stay preserved (**C:113–119**). | It runs selected saved-input assertions, not an all-path baseline digest comparison. An unused historical file can change without being read. | Resolve the independently owned preservation manifest against the frozen base and delivered tree, with only the precise new paths excluded. |
| No lost baseline held identity, only C06 status may change, denominator remains 14 (**C:114–115**). | Rows and held rows are counted from text; unique row identities and baseline statuses are not compared. The row denominator is dynamic. `K_ROW C06` is printed, not asserted. | Compare the full 14-row identity/status map and candidate reference to baseline. The family denominator **is** fixed at eight by **P:45–49**, assuming the frozen probe stays unchanged. |
| Q01–Q13 never weaken; every load-bearing source/derivation and fresh independent pass decision exists; flip follows decisions (**C:33–41,105–106,115**). | No `QUALITY.md`, lesson Gate, source registry, reviewer identity, or admission order is inspected. | Preserve the quality bar and resolve the named final-candidate decisions plus located sources/derivations. |
| Preserve every receipt conjunct, the round-36 exemption, every existing saved-input assertion, and exactly ten verifier scripts (**C:77–88**). | Mutation matching checks one textual site; self-tests prove only what still executes. Replay denominator is `len(results)` (**P:166–180**), not an asserted 10. | Review the two receipt refactors and the complete named verifier census/diff. Do not accept a smaller all-green census. |
| Existing **attributed** C2 kills remain `2/2` (**C:116–117**). | `attributed_b` is printed (**P:116,122**) but absent from `holds_ok` (**P:179–181**), which uses raw `killed_b` instead. d2 `2/2` is enforced. | Require the separate printed `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` label; exit 0 alone is insufficient. |
| Freshness remains the existing stored-row proxy. | **P:55–60,181** requires 18 matching rows, not their identities or present-day truth. | Keep the proxy's bounded meaning; do not infer a new live-host re-verification. |
| Count on the committed archive using the frozen probe; preserve the older probe pin; commit final-tip re-verification and frontier/census evidence (**C:92–98,124–132**). | TREE is only checked for a `corpus/` directory. The probe cannot prove its input's commit provenance, its own immutability, final report/log landing, source opening, or M33 lesson completion. | Integrator records the immutable measured revision, frozen-probe identity, final receipt, source census and lesson pointers separately. |
| No firmware payload execution, real vendor image, extra extraction, host-route/config or unauthorized repository mutations (**C:53–61,134–142**, assignment). | A corpus snapshot cannot attest all historical host actions. | Retain the actual inert-fixture generation/run receipts and scoped integration records; do not infer operational safety from output labels. |

The most consequential operational mistake would be to conflate **`HOLDS_OK`**, the three printed target values, and the complete claim contract. **P:179–183** deliberately does not require a K/F/C3 improvement; the red-before receipt already demonstrates this. The safe correction is the existing conjunctive final review, not a new authority, a weakened universal clause, an altered frozen counter, or a re-targeted claim.

## Review method and limits

Read the frozen contract, counter and red-before receipt first, then the located coverage/backing, original receipt sites, scorecard split and quality bar. A read of the icon verifier showed a peer-owned working-tree update during the review; the canary analysis above is explicitly against the originally observed receipt block and is not a review of the final patch. This report does not assert final candidate quality or final tree preservation.

No shell commands, counter runs, tests, mutants, target payloads, producer calls, or other judgment runtime were invoked. All proposed false-positive outputs are marked **[INFERENCE]**. No production file, registry/spec, Git/jj state, or host configuration was modified. Tool installs/updates: **none**. Only this assigned findings report was written.
