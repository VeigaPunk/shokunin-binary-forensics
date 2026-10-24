# W2ClaimsAdmission — committed-byte admission attack

Reviewer: `revenger-r63.W2ClaimsAdmission`, independent falsify leaf; neither candidate author nor corrector. This is adversarial evidence and a recommendation, not canonical judgment or admission.

## Scope and axes

- **Coverage K / C1**, **coverage F / C2**, **calibration / C3**. Cross-cutting risks: reviewer identity, false provenance, preservation and freshness.
- Pinned lane tip: `db55bd6488e24e956df5818ae34c2a043d7ddc12` (candidate integration immediately after build `2a34e455…`). All evaluated corpus/report/build bytes came from `git archive` of that exact commit, extracted under `/tmp/revenger-r63-claims-admission-AxwTeF` (T below), not the mutable checkout. Baseline B = T/base, extracted from `55bcb6e1aeb4d42923a4e98db6580f67142b41ac corpus`.
- Frozen counter SHA-256 independently recomputed: `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`. Frozen claims SHA-256: `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31`.

## Findings at a glance

| Attacked claim | Adversarial result on pinned bytes | Smallest safe correction / retained boundary |
|---|---|---|
| C1 | **FALSIFIED as an admitted 7/14 claim at this tip.** Actual K is 6/14, no final-byte fresh-seat pass decisions are committed, and Q11 has a directly false printed command result. Q01 also has a registry-scope mismatch. | Correct the count; resolve the source-row scope using append-only rules; obtain named fresh non-author/non-corrector decisions on corrected exact bytes before L1 flips C06. |
| C2 | **NOT-FALSIFIED under the frozen claim.** F is 5/8; committed receipt and run/cache attestations corroborate the run; every reported region independently matches the byte oracle. | Preserve the distinction between receipted/corroborated execution and authenticated producer origin. Repair the ledger's receipt-hash typo without rewriting saved record bytes. |
| C3 | **NOT-FALSIFIED.** Both frozen mutants exit 1 with the last line containing `forged receipt`, both controls exit 0, and the patches actually implement the contracted data-forgery controls. | Retain narrow credit for the two frozen conjuncts; do not promote 2/2 to protection of every receipt field. |

## C1 — two concrete gate defects, plus absent admission decisions

### C1.1 — Q11: the entry prints a command result that is not its result

Object: `corpus/knowledge/round-63-zip-central-directory-evidence.md`, 80126 bytes, 709 lines, SHA-256 `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53`.

Entry lines 284–306 label the block **“command and exact output”**. Lines 291–292 contain:

```text
$ printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w
8
```

I executed that exact counting operation independently, exit 0:

```text
7
```

The seven tokens are `local`, `file`, `header`, `signature`, `4`, `bytes`, `(0x04034b50)`. I independently reran all ten quote counts using `wc -w`; the other nine agree. All ten quotes are verbatim substrings of the whitespace-normalized committed APPNOTE snapshot and remain ≤25 words. This therefore does **not** falsify the quotation-length ceiling or the ZIP arithmetic; it falsifies the entry's exact-output/count evidence under Q11. The author's Q11 pass at line 707 cannot cure a false recorded result.

**Impacted axes:** C1 admission integrity and K; calibration of command/output claims. **Smallest correction:** replace this displayed `8` with independently observed `7`, then review the corrected entry identity. This is a fixable defect, not an acceptable no-harm tradeoff or grounds to weaken Q11.

### C1.2 — Q01: the corrected entry outruns the actual S032 row's registered scope

`corpus/SOURCES.md:46` grants S032 tier A for **central-directory file header and EOCD field layout**, with anchors §4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10–12, §4.4.16, §4.4.21–22. It does **not** include §4.3.7 or local-file-header field layout. Its “local-header offset” means the central-directory field pointing at a local header, not the local header's own field layout.

The corrected entry, however, derives the local fixed length 30 and local name/extra offsets 26/28 from §4.3.7 (lines 67, 360–364, 468–475), quotes that section (645–646), and says the row covers **three** fixed records (655, 697). The document itself supports these facts: I reopened the primary URL and §4.3.7 shows exactly that layout. The defect is the mismatch between registered tier-A scope and the entry's claimed scope, not an invented ZIP fact.

**Impacted axes:** C1/Q01 and source authority. **Smallest safe correction:** make the local-header layout rest on an actually registered, opened, correctly scoped tier-A row. SOURCES:6–8 allows only `status`, `recheck`, `used-by` changes in place; if S032's scope is immutable, append a next-free, narrowly scoped §4.3.7 re-open row and update the entry's local-layout citations rather than silently rewriting S032 or treating the entry's self-check as a second authority.

### C1.3 — named fresh Q-pass decisions for the committed entry: none

- Author: **`revenger-r63.R63EntryC06`**, identified in `build/R63EntryC06.md:3`. Its self-check is explicitly not admission authority (:146–149).
- Sole integrating/correcting seat: **`revenger-r63`**, per frozen claims:8 and this wave's assignment. Integration is not independent review.
- Existing fresh non-author build reviewer: **`revenger-r63.R63ReviewC06Q`**, `build/R63ReviewC06Q.md:3–6`. Its pass reviews the **older draft** SHA-256 `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e`, 672 lines, not the pinned entry `a0158e99…`, 709 lines. Its Q01 pass is conditional on then-unlanded rows; it cites S034, before renumbering/corrections. Its blanket Q11 pass also preceded the H1–H7 corrections documented by `R63CriticCounts`.
- The committed archive has **no `.ufo/waves/round-63/falsify/` directory**. The lesson Gate remains a draft: `corpus/lessons/round-63.md:10,154–177`; no final-byte named all-Q pass decisions are recorded. A live seat roster is not a pass decision.

Thus there is no legitimate set of names to credit with fresh all-Q approval of these committed bytes. Q11 is still failing, and Q01 requires resolution. I found no independent numerical counterexample to Q03/Q04/Q06/Q09/Q10; Q05/Q07 are expressly inapplicable to this manual saved-byte comparison, Q08 is superseded, Q12 cites no rejected row, and Q13 claims no deletion-sensitive guard credit. None of those observations is an all-Q admission.

The counter independently prints `K_HELD=6/14`, `K_HELD_BACKED=6/14`, `K_ROW C06 status=partial`. Keeping README partial is **correct pre-wave ordering**, not itself misconduct. Nevertheless, a final C1 success claim on this pinned tip would fail both numeric and substantive admission conditions. Do not substitute the old build review or a status-only flip for the missing decisions.

### C1 — independent reproductions and source reopening

I reopened both appended rows: S032's primary URL <https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT> at the relevant layouts/meanings, and S033's fixture bytes, oracle, saved record and ledger. Their independently recomputed hashes match the entry. The APPNOTE snapshot is 174585 bytes, SHA-256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`.

I executed the complete embedded readout from the committed entry in an isolated Python namespace over T. Script: 328 lines, SHA-256 `94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac`. Result: 17 lines, SHA-256 `02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4`, byte-identical to its displayed stdout. Independent `wc` calls confirm script/stdout/snapshot counts 328/17/174585. Correct reproduction of those observations does not make the separate wrong quote-count output true.

## C2 — real-run and every-region attacks

### C2.1 — execution provenance attack: strongest residual, not a demonstrated forgery

Committed `receipt.json` names the required `npx -y rea-agents@6.5.0 inspect-firmware-regions … --format json`, exit 0, duration 1.296587134, fixture/stdout hashes and matching Evidence ID. `build/R63FirmwareRun.md:7–18` is the producer seat's exactly-one-run attestation. `build/R63ReviewFirmware.md:22,38` records an independent cache check for `rea-agents` 6.5.0; `build/R63ScoutFirmware.md:3` identifies cached package path `~/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents` and its `package.json` version 6.5.0.

I independently recomputed:

```text
fixture:   2048 bytes bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
stdout:    3904 bytes f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9
inspection:3904 bytes f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9
receipt:    492 bytes e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d
stderr:       0 bytes e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Evidence ID: ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
```

Fixture hash = receipt = subject digest = truth image digest; stdout hash = receipt = inspection; Evidence ID receipt = inspection. The raw provider report and normalized result both contain the same two zlib offsets/sizes. Operation is `inspect_firmware_regions`, provider is binwalk 3.1.0, coverage is `signature_scan`.

**Residual:** committed bytes contain reports of cache inspection, not the cached package bytes or an independently authenticated process transcript. Cache presence corroborates availability/version, not occurrence of the specific invocation; rehashable stdout/receipt pairs do not authenticate origin. I did not reach outside committed evidence and pretend to reopen that live cache. The frozen claim requires a real receipted run, not third-party authenticated provenance; the committed producer and independent cache attestations plus coherent envelope give no affirmative counterexample to that requirement. **NOT-FALSIFIED**, not “producer origin proven.”

**Fixable metadata defect:** LEDGER:26 prints the receipt digest ending `…c6b94b`, whereas the actual committed receipt hashes to `…c6b94d` above. Correct the ledger pointer; the receipt's own contracted fields and their byte bindings are intact. This typo does not turn the reported regions into mismatches.

### C2.2 — EVERY reported region, not one selected example

I ran the committed `oracle_check.py` from cwd `/`: exit 0, `ORACLE OK`. Separately, I iterated **every normalized region**, matched the `(offset, reported_size, signature)` tuple to exactly one truth member, and decompressed that exact reported byte window with a fresh `zlib.decompressobj`.

| Reported region | Offset / compressed size | Plain bytes | Independently computed plain SHA-256 | Truth agreement |
|---|---:|---:|---|---|
| 1, zlib | 512 / 79 | 78 | `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` | all fields match |
| 2, zlib | 1024 / 90 | 97 | `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` | all fields match |

Both decoders reach EOF with zero unused data and zero unconsumed tail. There are exactly two reported regions; no unexamined third region. Truth's other three regions are padding, independently checked by the committed oracle; C2 quantifies over what the record reports, not every padding span. No extraction occurred in the record, so these hashes are checker-side decompressions, **not** hashes falsely attributed to producer extraction output. F independently prints **5/8**, including `firmware`.

**Strongest residual:** a correct two-region zlib signature scan of an inert authored image is not firmware extraction completeness, real-device capability, or a general engine claim. Those limitations are already explicit and cannot be promoted into new credit, but they do not falsify the frozen family-record criterion.

## C3 — attribution versus crash attack

I reran the frozen counter against the committed archive, which independently constructs fresh corpus copies and deletes exactly the registered conjunct once per script. Results:

```text
verify_named_multi_icon_states.py control exit=0
verify_named_multi_icon_states.py c3 exit=1
last: AssertionError: r55: forged receipt accepted
verify_icon_states.py control exit=0
verify_icon_states.py c3 exit=1
last: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
```

I compared both patched files against their baseline bytes. Named's helper preserves the entire former receipt expression; lines 76–79 deep-copy the receipt, append ` --forged` to its command, require rejection, then check the genuine receipt. Icon's helper preserves the original assertions **including `round_id != 36`**; lines 151–158 deep-copy the receipt, forge the fixture hash, and raise the attributed message if accepted. These are actual forged-data controls, not source-string canaries. Both observed last lines contain `forged receipt`; neither kill is a syntax error, missing-file error or unrelated assertion. **NOT-FALSIFIED.**

**Strongest residual:** the stdout-digest clauses have no equivalent new in-script control. The committed `build/R63MutC3.md:174–205` reports surviving stdout-clause deletion/double-forgery probes, and lesson M35 names that debt. I did not independently rerun those supplementary mutants; this is committed prior evidence, not my new test result. It cannot falsify the two explicitly frozen mutants. Smallest safe action is narrow C3 credit and retained unguarded-field disclosure, not expanding this round's claim or changing its mutation.

## Counting receipts, holds and final dependency

Independently executed, cwd `/`:

```text
env TMPDIR=T python3 -B T/reports/round-63/measure.py T
env TMPDIR=T python3 -B T/reports/round-63/measure.py B
```

Both commands exited 0. T/B denote the absolute scratch paths stated above, not checkout-relative locations.

| Printed label | Baseline B | Pinned tip T |
|---|---:|---:|
| K_HELD / K_HELD_BACKED | 6/14 / 6/14 | 6/14 / 6/14 |
| K_ROW C06 | partial | partial |
| F_COVERAGE | 4/8 | 5/8 |
| FRESH_ROWS | 18/18 | 18/18 |
| C2_CONTROLS_PASS | 2/2 | 2/2 |
| C2_RECEIPT_B_KILLED / attributed | 2/2 / 2/2 | 2/2 / 2/2 |
| C2_D2_KILLED | 2/2 | 2/2 |
| C3_CONTROLS_PASS | 2/2 | 2/2 |
| C3_RECEIPT_KILLED_ATTRIBUTED | 0/2 | 2/2 |
| HOLD_CALIBRATION / HOLD_REPLAY | 4/4 / 10/10 | 4/4 / 10/10 |
| HOLDS_OK | yes | yes |

The current run's `F_FAMILIES` is `['native-static', 'javascript', 'archives', 'firmware', 'evm']`. Both earlier receipt-command mutants remain attributed (`r47` and `r42`: `forged receipt command accepted`). `HOLDS_OK=yes` is not an admission result and does not require a K improvement.

Additional independent byte comparison: all **443** baseline live/fixture files are identical; nine added live/fixture paths are entirely within `fixtures/firmware-r63/` and `live/runs/round-63/`; QUALITY bytes are identical to baseline. Registry row count is 33. These checks reveal no axis harm, but do not waive C1's defects.

**Final receipt dependency attacking all three final success claims:** `reports/round-63/measure-after.log` is absent from the pinned committed archive. Claims:129–132 requires the final on-tip re-verification receipt beside the final report. Its absence is expected at candidate dispatch but forbids treating this candidate snapshot or my scratch run as the completed final landing. L1 must land the final named decisions, adjudication and actual final committed-tree receipt; this leaf neither waits for them nor fabricates them.

## Tooling and boundaries

Read `/home/vgpnk/.omp/agent/RULES.md` and `skill://godspeed`. No installation or update, no pacman, no npx producer re-run, no model arguments, no target execution, no canonical judge/runtime invocation, no git/jj mutation. Only this assigned report was written in the lane. Independent commands used preinstalled Git, tar, Python standard library, printf and wc. Scratch T is removed after report landing. No source, fixture, saved record, verifier, registry, spec, index or config was edited.

## Corrected-byte re-review — `aaa046326d92ba983f3ae99341438c9b8509a6cc`

Re-review requested by L1 after the first findings. This appendix evaluates the corrected committed candidate, not the old failed bytes. Archive extracted at `/tmp/revenger-r63-claims-readmit-CTmXyV` (T2). Independently computed entry SHA-256 is exactly `285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1`, 734 lines.

**C1 adversarial result: still FALSIFIED as an all-Q admitted claim on these bytes.** The original count and registered-scope defects are genuinely corrected; I do not retain those obsolete objections. However, the corrected entry still carries an underived source-file byte count under Q11, an inconsistent source-count sentence, and unresolved citation-template tokens. These are bounded, fixable defects, not a license to weaken the unchanged gate.

### Corrections that survive this attack

- Independently executed all ten displayed quote-count operations using `wc -w`: actual/displayed counts are `7,21,7,10,8,23,24,20,23,12`; every one matches. The prior `8` versus `7` defect is closed at corrected lines 312–313.
- Reopened new S034's actual registered scope and APPNOTE §4.3.7 both at the primary URL and the committed snapshot (lines 387–399). It covers the local-header layout used by the candidate. S032 stays scoped to central-directory/EOCD fields. Reopened S035's actual ledger bytes; SHA-256 `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`. The old Q01 scope objections are closed by the new registered rows; I found no new unsupported ZIP field-layout claim.
- Executed the complete corrected embedded readout over T2: 17 stdout lines, SHA-256 `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5`, byte-identical to the displayed full stdout. Script SHA-256 `8dbefe4dae2fd170d4bd658c4d1111e66a15b266687fe586e385d9aab74c367f`, 329 lines. Independent `wc` operations confirm those counts.
- The new zipfile-snapshot measurement matches: 139782 bytes, SHA-256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`. APPNOTE remains 174585 bytes with the original pinned digest. Its first five CR-stripped lines exactly match the new version/status/date output. Those prior metadata gaps are closed.

### C1-R1 — Q11: S035's `3959 bytes` has no in-entry derivation/output

Corrected entry line 4 and line 681 assert the ledger's **3959-byte** size. That number is correct: I independently ran

```text
wc -c /tmp/revenger-r63-claims-readmit-CTmXyV/corpus/live/runs/20261012T164246Z/LEDGER.md
3959 /tmp/revenger-r63-claims-readmit-CTmXyV/corpus/live/runs/20261012T164246Z/LEDGER.md
```

But **no such byte-count derivation and output exists inside the entry**. Its ledger commands at lines 37–38 and 42–46 hash the file; they do not measure its length. All `3959` occurrences are in S035 source prose/row text, not measurement output. The embedded readout has zero references to the ledger and its 17 output lines contain no `3959`. Nor is this byte count explicitly qualified as a value recorded from the registry instead of a measured file property. The primary ledger itself contains no assertion of its own byte length.

This is exactly Q11's frozen rejection case: “a value is correct when re-derived but the entry carries no derivation.” The new inventory's distinction between recorded producer attribution and derived measurements does not turn an uncited byte length into a printed measurement. **Impacted axes:** C1/Q11 and source-identity calibration. **Smallest correction:** add `wc -c corpus/live/runs/20261012T164246Z/LEDGER.md` and its actual `3959 …/LEDGER.md` output in-entry, or remove that unneeded size claim everywhere it appears.

### C1-R2 — source-count inconsistency and unresolved correction scaffolding

- Corrected line **682** still says **“No third source is cited.”** The entry's own headers and Sources section cite **S032, S034, S033, S035**. My independent header enumeration returns those four ids; Q02's own table at line 723 also explicitly says “four rows.” APPNOTE's two scope rows are one document, not independent corroboration, but that does not make the unqualified “No third source” sentence true of the cited registry sources. Smallest correction: delete that stale sentence while retaining the grounded zipfile-exclusion explanation; do not invent another source-count convention retrospectively.
- Corrected line **680** contains literal unresolved references **`{{R:spec_offsets}}`, `{{R:local_member_1}}`, `{{R:local_member_2}}`** and draft “Proposed registry row text for L1” despite the rows having landed. Those three strings are not observation ids, commands or resolvable anchors in the entry. They obstruct the source-to-observation audit the correction is supposed to close. Smallest correction: replace them with the real item/fact references (item 5 / `spec_derived_field_offsets`, item 8 / `member_local[bin/checksum]`, item 9 / `member_local[README.txt]`), and remove obsolete row-proposal scaffolding without changing the committed source rows.

R1 is the decisive remaining Q11 rejection. R2 supplies additional local evidence that the corrected candidate is not yet a finished all-Q entry; it is not a claim that the reproduced ZIP values are wrong.

### Current committed admission and counter receipts

I reran the frozen counter on T2, cwd `/`, `TMPDIR=T2`: exit 0; `K_HELD=6/14`, `K_HELD_BACKED=6/14`, `K_ROW C06 status=partial`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`; all earlier C2 control/kill/attribution labels remain `2/2`; `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`; `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`. C3's actual last lines remain `AssertionError: r55: forged receipt accepted` and `AssertionError: r36: forged receipt accepted`, not crashes.

Registry count is now 35. As committed at this pin, no falsify-report directory or `measure-after.log` is present; the lesson still distinguishes draft candidate evidence from later fresh admission decisions. Thus **no named final-byte all-Q pass seats can be credited from this archive**. The original named build reviewer `revenger-r63.R63ReviewC06Q` still reviewed a different draft; the author/corrector identities remain as recorded above. Correctly retaining README `partial` is expected pre-admission ordering, but does not meet the final 7/14 claim.

**C2 and C3 remain NOT-FALSIFIED.** The corrected commit fixes the ledger receipt-pin typo; the producer envelope, fixture/oracle and the two verifiers are not changed by this correction. The current counter independently retains F 5/8 and attributed C3 2/2. Their strongest residual attacks remain unauthenticated producer origin and the specifically disclosed unguarded stdout-digest conjuncts; neither is silently converted into a new requirement.

No installs, producer re-run, target execution, judge/runtime invocation or lane-state mutation. Only this named report is appended. T2 scratch is removed after this appendix lands.

Final exact-hash re-review, commit `3af3acbab51ab38c929d6d81524e07ded70dec44`, entry SHA-256 `4ece6cfb980f834b6dcf5fe2fc9bf4de8436a3f50ea5081d829182b5e6d8027c`: **NOT-FALSIFIED as the corrected candidate, not final admission**. Independent ledger `wc -c` = 3959 and SHA-256 = `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`; the new in-entry derivation closes R1. All ten quote counts reproduce, no unresolved template tokens remain, and the 17-line readout again byte-matches SHA-256 `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5`.
Strongest residual attack: line 680 calls its embedded S034 draft “Registry row as landed” but quotes status `queued` / used-by `—`, whereas actual SOURCES S034 is `mined` / used-by the candidate path. The load-bearing layout and actual registered authority agree; this stale documentary copy is not evidence against the ZIP derivation. Smallest safe correction: remove the redundant copied draft or quote the actual landed row, without rewriting immutable registry cells.
Frozen counter independently rerun from cwd `/` on the pinned archive: exit 0, K 6/14 (correctly still partial), F 5/8, C3 controls/attributed kills 2/2, freshness 18/18, calibration 4/4, replay 10/10, all earlier C2 labels 2/2, `HOLDS_OK=yes`. No final K admission or fresh-seat decisions are inferred from these numbers; C2/C3 remain NOT-FALSIFIED. Only this report was appended; final scratch `/tmp/revenger-r63-claims-final-37BJCL` is removed after landing, with no installs or producer/target execution.

Transition check, commit `34cfa2435a424541d09a95c88cbdca2eb9ebe33b`, independently verified entry SHA-256 `854e33d78034e8d53ca68e813cab2394a1bc9a38770c9b47ee1bf0dc07a1a0d7`: **NOT-FALSIFIED stands for the corrected candidate, not final admission**. The embedded script is unchanged; its independently rerun 17-line stdout again matches `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5`, and all ten quote counts reproduce.
Residual documentary discrepancy is only partly closed: both copied rows now say `mined`, but contrary to the transition note, their copied `used-by` cells still say `—`; actual S034/S035 both name `corpus/knowledge/round-63-zip-central-directory-evidence.md`. Remove the redundant draft copies or reproduce the actual rows; this does not supply a new counterexample to the load-bearing ZIP derivation.
Frozen counter on this exact committed archive again exits 0: K 6/14 partial, F 5/8, C3 controls/attributed kills 2/2, freshness 18/18, calibration 4/4, replay 10/10, all earlier C2 labels 2/2, `HOLDS_OK=yes`. No final admission inferred; no installs or target/producer execution; owned scratch `/tmp/revenger-r63-claims-transition-xApYUd` removed after this append.
