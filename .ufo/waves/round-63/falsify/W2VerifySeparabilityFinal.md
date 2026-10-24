# W2VerifySeparabilityFinal — causal separability of C1/C2/C3 on committed bytes

Seat: `revenger-r63.W2VerifySeparabilityFinal` (leaf, no dispatch).
Assigned diff: committed tip `db55bd6488e24e956df5818ae34c2a043d7ddc12`, build state
`2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e`, frozen contract
`reports/round-63/claims.md`, frozen counter `reports/round-63/measure.py`,
red-before `reports/round-63/measure-before.log`.
Lane root for every command below: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Verdict

**Separability holds; no claim's counter moves with another claim's work.** The three
probes reproduce the pre-registered predictions exactly: A (C1 work only) → K 7/14,
F 4/8, C3 0/2; B (C2 work only) → F 5/8, K 6/14, C3 0/2; C (C3 work only) → C3 2/2,
K 6/14, F 4/8. All runs exit 0 with `HOLDS_OK=yes`, twice, byte-identically.

The claims are *separable*, not yet *admitted*: C1's README flip is still conditional
on fresh-seat Q01–Q13 decisions, and **no such named decision file exists in
`.ufo/waves/round-63/falsify/` at report time** (finding F1, blocker for admission —
not for separability). C2's F counter is presence-only and does not by itself establish
the byte-oracle agreement C2 requires (F2). C3's target is met on committed bytes and
each kill is attributed through the new in-script forged-receipt control, not a crash
(F3, attack log A7). One C3 side effect needs disclosure before admission: the patch
moves the named verifier's printed count `139 → 142`, so two committed round-58 quotes
no longer reproduce (F4, A9).

## Canonical runtime and frozen counter identity

| Item | Value |
|---|---|
| Counter SHA-256 | `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908` |
| Same at freeze commit `54ab973` | yes (`git show 54ab973:reports/round-63/measure.py \| sha256sum`) |
| Same at tip `db55bd6` | yes |
| Same on disk (invoked) | yes |
| Python | `Python 3.14.8` (`-B`, no bytecode writes) |
| Invocation | `python3 -B reports/round-63/measure.py <TREE>`, cwd = lane root |
| Script self-tests inside probe | `cwd=/` for mutant runs, `cwd=TREE` for the census (probe code, unchanged) |
| Target execution | none: no firmware payload run, no `npx rea-agents` call, no network |

One canonical runtime: the probe is invoked once from the lane repo and reads each
tree's own committed scripts. No shadow or patched copy of `measure.py` was used; the
SHA above is the only counter that produced every number in this report.

## Probe trees (built from `git archive`, single-claim deltas)

Scratch root `/tmp/revenger-r63-sep`, one directory per state, each containing `corpus/`:

```
S=/tmp/revenger-r63-sep
git -C <lane> archive HEAD      corpus | tar -x -C $S/tip      # db55bd6 bytes
git -C <lane> archive 55bcb6e   corpus | tar -x -C $S/base     # base bytes
A = tip − C2(record+fixture) − C3(two scripts→base) + C06 README flip   # C1 only
B = tip − C1(entry+README→base) − C3(two scripts→base)                  # C2 only
C = tip − C1(entry+README→base) − C2(record+fixture)                    # C3 only
D = tip + C06 README flip                                               # all claims
E1 = B + named-multi script only at tip                                 # per-script control
E2 = B + icon_states script only at tip                                 # per-script control
```

Blob identity of every claim-bearing file, `sha256` truncated to 12 hex chars
(`BASE` = `55bcb6e`, `TIP` = `db55bd6`; verified by `git show <rev>:<path> | sha256sum`):

| File | BASE | TIP | A | B | C | D |
|---|---|---|---|---|---|---|
| `corpus/verify_icon_states.py` | acbf47bbb49c | 7cbd931a3a8e | BASE | BASE | TIP | TIP |
| `corpus/verify_named_multi_icon_states.py` | b62441d5e1fa | a226bf73eaba | BASE | BASE | TIP | TIP |
| `corpus/README.md` | 7ccd8d4484db | 7ccd8d4484db | f583bd25ed7a | BASE | BASE | f583bd25ed7a |
| `corpus/knowledge/round-63-zip-central-directory-evidence.md` | absent | a0158e99d3fa | TIP | absent | absent | TIP |
| `corpus/live/runs/round-63/inspection.json` | absent | f69978355e28 | absent | TIP | absent | TIP |
| `corpus/live/runs/round-63/receipt.json` | absent | e930a549db16 | absent | TIP | absent | TIP |
| `corpus/fixtures/firmware-r63/truth.json` | absent | 9663f90b2b9f | absent | TIP | absent | TIP |
| `corpus/SOURCES.md` (build-level, not a claim input) | — | c075f900d461 | TIP | TIP | TIP | TIP |

- The README delta is exactly one line (`diff base A`):
  `35c35` → C06 status cell `partial` → `held` and knowledge cell
  `knowledge/2026-10-12-rea-readiness-checklist.md` (archive-tool row only) →
  `knowledge/round-63-zip-central-directory-evidence.md` (+ scope sentence).
  A and D READMEs are byte-identical (`cmp -s` clean).
- All nine files under `corpus/live/runs/round-63` + `corpus/fixtures/firmware-r63`
  hash identically in tip, B and D; only `stderr.txt` is 0 bytes (clean run;
  `stdout.raw` 3904 bytes, `LEDGER.md` 22502 bytes). The record's envelope:
  `operation=inspect_firmware_regions`, `evidence_id=ev_aae7529f…ed259`,
  `normalized_result` = `{coverage, engine, input_size: 2048, regions: 2}`,
  `locations=[{file-offset-range,0,2048}]`.
- Preservation check: all 443 files under `corpus/live` + `corpus/fixtures` outside
  `live/runs/round-63/*` and `fixtures/firmware-r63/*` hash identically in base, tip,
  A, B, C and D (pairwise `sha256sum` snapshots, all equal). The removal sets are
  directory removals only; no frozen byte was edited by any tree.

## Probe A — C1 work only (entry present + README flip)

`python3 -B reports/round-63/measure.py /tmp/revenger-r63-sep/A` → **exit 0**, output
SHA-256 `3b6e2a0ac5ace3eba2c2e6daffe3b8859f8edb0d1212c702273d64252338ec26`:

```
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=4/8 score=5.0
F_FAMILIES=['native-static', 'javascript', 'archives', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=0 pass :: PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

Readings: K moves 6→7 (score 4.3→5.0) on the C1 work alone; F stays 4/8; C3 stays 0/2.

## Probe B — C2 work only (firmware fixture + saved record)

`python3 -B reports/round-63/measure.py /tmp/revenger-r63-sep/B` → **exit 0**, output
SHA-256 `0f3379e97486d53ba6902e311bfa0ad9d1b94c411b9013dc5a1f23fd4317e0c5`:

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=0 pass :: PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

Readings: F moves 4→5 (5.0→6.2) on the C2 record alone, and the only new counter key is
`inspect_firmware_regions: 1`; K stays 6/14; C3 stays 0/2. Note `C2_CONTROLS_PASS`,
`C2_RECEIPT_B_KILLED`, `C2_D2_KILLED`, `C2_RECEIPT_B_KILLED_ATTRIBUTED` are all 2/2 in
*every* tree including base — those mutants use the round-47/round-42 receipts, so the
round-63 record moves only `F_COVERAGE`, never the C2 calibration holds.

## Probe C — C3 work only (both patched verifiers)

`python3 -B reports/round-63/measure.py /tmp/revenger-r63-sep/C` → **exit 0**, output
SHA-256 `97ba5f4b563478696c5a6f41de62be27ccb00efc5f8e120b4a66f365aa2ea017`:

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=4/8 score=5.0
F_FAMILIES=['native-static', 'javascript', 'archives', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

Readings: C3 0/2 → 2/2 on the C3 work alone; K stays 6/14; F stays 4/8.

## Control rows (what makes the three probes meaningful)

| State | K_HELD | K_ROW C06 | F_COVERAGE | C3 attributed | exit |
|---|---|---|---|---|---|
| base `55bcb6e` (red-before, `measure-before.log`) | 6/14 | partial | 4/8 | 0/2 | 0 |
| tip `db55bd6` (current commit, README *not* flipped) | 6/14 | partial | **5/8** | **2/2** | 0 |
| A — C1 only | **7/14** | **held** | 4/8 | 0/2 | 0 |
| B — C2 only | 6/14 | partial | **5/8** | 0/2 | 0 |
| C — C3 only | 6/14 | partial | 4/8 | **2/2** | 0 |
| D — all claims + flip | **7/14** | held | **5/8** | **2/2** | 0 |
| E1 — E2's complement: only named-multi patched | 6/14 | partial | 5/8 | **1/2** | 0 |
| E2 — only icon_states patched | 6/14 | partial | 5/8 | **1/2** | 0 |

- Tip output SHA-256 `cd071fb412c4380aef23407c7d9a1450e71c8b735421bede9a1d7d37e8a771cf`,
  D output SHA-256 `9a7799271647a06ab5d70ad9082a50542442951980e743dadf435c4759464513`.
- D shows the three targets are simultaneously reachable and additive: no claim's move
  suppresses another's. D's C3 mutant lines are identical to C's (142/139, r55/r36);
  D's F line is identical to B's; D's K line identical to A's.
- E1/E2 show the C3 counter is 1/2 per script, so 2/2 cannot come from one script.

## Attack log (each item names what it attacks)

- **A1 — does C1's K move without C2/C3 work?** Yes: A has the firmware record and both
  patched scripts removed (base blobs proven above) and K still hits 7/14, backed 7/14.
  Attacks: "K moves because round-63 also added live records".
- **A2 — does C2's F move without C1/C3 work?** Yes: B has no entry, no flip, base
  scripts, and F hits 5/8 with `inspect_firmware_regions: 1` as the only new key.
  Attacks: "F moves because README/C3 changed".
- **A3 — does C3's C2-style calibration ride on the new record?** No: C removes the
  round-63 record and `C2_*` stays 2/2; conversely the record's presence in B/D leaves
  `C3_*` untouched. Attacks: "receipt mutants share the new record".
- **A4 — is 2/2 a single-script artifact?** No: E1 and E2 each print 1/2; both scripts
  are required. Attacks: "one patched script earns both credits".
- **A5 — is the counter the frozen one?** Yes: `measure.py` SHA identical at freeze
  commit `54ab973`, at tip, and on disk; the invoked path is the lane's own file.
  Attacks: "counter drifted to fit the result".
- **A6 — are the trees really committed bytes?** Yes: per-file blob hashes (table above)
  show `BASE`/`TIP` identities for every claim-bearing file, and the only README delta
  is the single `35c35` line. Attacks: "hand-edited scratch favoured the claim".
- **A7 — are the C3 kills attributed or crashes?** Attributed: reproducing each frozen
  mutation with the probe's own regex (exactly one match per script, no
  `could-not-evaluate` line in any tree) gives single `AssertionError`s from the
  forged-receipt control:
  - named-multi: exit 1, last line `AssertionError: r55: forged receipt accepted`
    (raised at `if not ok: raise AssertionError(msg)` on the
    `req(not receipt_ok(forged, …), f'r{r}: forged receipt accepted')` control);
  - icon_states: exit 1, last line `AssertionError: r36: forged receipt accepted`
    (raised at `verify_icon_states.py:158`, the forged-receipt control).
  No syntax error, no unrelated assertion; red-before shows both mutants exit 0 on base.
  Peer `W2VerifyFixture.md:187` reports the same two messages independently.
  Attacks: "kill credited to an incidental crash".
- **A8 — can C2 and C3 messages cross-credit?** No: the C2 attributed counter requires
  `last.endswith("forged receipt command accepted")`; the C3 kills end with
  `forged receipt accepted` (no `command`), so a C3 kill cannot satisfy C2's check, and
  the C2 mutants are not run against the C3 scripts at all. Attacks: "one attribution
  counter launder the other".
- **A9 — does the C3 patch break an existing saved expectation?** It does change one
  quoted output, and no automated check covers it (corrects an earlier reading of this
  seat: `grep -rn "139 positive checks" corpus` *does* hit). The named verifier's count
  rises `139 → 142` because the frozen shape adds one `req(...)` control per round
  (r55, r56, r57): the diff from `55bcb6e` adds exactly one `req(` line (21 → 22
  occurrences) and the loop calls it three times; no other check changed. Two committed
  observation records quote the old line verbatim —
  `corpus/live/runs/round-58/LEDGER.md:4` (`… exit0 → PASS: 139 positive checks; …`) and
  `corpus/live/runs/round-58/reviewer.md:13`. Re-running that ledger command on tip
  prints `142`, so the quote no longer reproduces. Nothing automated depends on it: no
  verifier references `round-58` or asserts the PASS string (`grep -rn "round-58"
  corpus/verify_*.py` → no hit; `grep -rn "positive checks" corpus/verify_*.py` → only
  the `print` itself), and `HOLD_CALIBRATION=4/4` / `HOLD_REPLAY=10/10` hold in every
  tree. The round-63 lesson and ledger do not mention `142` (`grep -n "139\|142"` on
  `corpus/lessons/round-63.md` and `corpus/live/runs/round-63/LEDGER.md` → only unrelated
  hits), so the change is currently undisclosed. Attacks: "patch changed observable
  output in a way that invalidates a written expectation".
- **A9b — are the non-round-63 corpus bytes preserved?** Yes: every file under
  `corpus/live` and `corpus/fixtures` outside `live/runs/round-63/*` and
  `fixtures/firmware-r63/*` — 443 files — hashes identically in base, tip, A, B, C and D
  (`find … -print0 | sort -z | xargs -0 sha256sum` compared pairwise; all six snapshots
  identical). Attacks: "the claim was purchased by touching a frozen byte".
- **A10 — do the holds still pass on the final state?** Yes in A–D and tip: `HOLDS_OK=yes`,
  `FRESH_ROWS=18/18`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, exit 0. Attacks:
  "the claims were bought by weakening a hold".
- **A11 — is the measurement stable?** Two complete runs per state (A, B, C, tip, D),
  byte-identical outputs (diffs empty); the SHA-256 of each `*.final` output is printed
  above. Attacks: "the numbers are timing- or order-dependent".
- **A12 — no target execution / no model arguments.** The probe only runs the ten
  `corpus/verify_*.py --self-test` scripts and the mutants; the firmware fixture is not
  executed (it is not imported or run by any probe path). Attacks: "C2 was proved by
  executing the target".

## Findings by severity

- **F1 (blocker for C1 admission; not a separability defect).** No named fresh-seat
  Q01–Q13 pass decision existed under `.ufo/waves/round-63/falsify/` when this seat
  checked, before this report landed: the directory held `W2AttackProbeF.md`,
  `W2ReopenS032.md`, `W2ReopenS033.md`, `W2VerifyEntryRecheck.md`,
  `W2VerifyFixture.md`, `W2VerifyFreshness.md`, `W2VerifyFrozenFiles.md`,
  `swarm-registry.json`, and `grep -rn "Q01\|Q13" .ufo/waves/round-63/falsify/*.md`
  found only statements that Q01–Q13 are *other seats'* work or are not supplied. `claims.md` makes the README flip conditional on those decisions, and
  the milestone names them as required. Probe A/D therefore measure the *conditional*
  post-flip state, not an admitted state; L1 must not flip C06 on this report alone.
- **F2 (medium, overclaim guard).** `K_HELD`/`K_HELD_BACKED` are existence checks: the
  counter matches the status cell and verifies the named `knowledge/*.md` file exists;
  it never reads the entry. K 7/14 is necessary, never sufficient, for C1. Likewise
  `F_COVERAGE` counts records whose JSON has `evidence_id` and a non-null
  `normalized_result` and whose `operation` matches a family; it never compares a region
  to `truth.json`. F 5/8 alone does not establish C2's byte-oracle condition — the
  oracle-agreement receipt is a separate admission input (other seats). The same
  existence blindness makes K insensitive to the flip line's *variant*: keeping the old
  checklist citation beside the new entry (the draft's second form) would still print
  7/14 as long as the new entry is named and the file exists, so K cannot arbitrate
  between the two README forms.
- **F3 (low, calibration hygiene).** `C3_CONTROLS_PASS=2/2` is satisfied by the *base*
  scripts too (see `measure-before.log`): the "control" variant only requires the
  unmutated script to exit 0, so the control alone carries no discriminating signal.
  The discriminating evidence is mutant survival at base (0/2) versus attributed kills
  at tip (2/2), confirmed by A7. No action required if the contract is read that way,
  but the label should not be cited as proof the in-script control exists.
- **F4 (medium-low, undisclosed observable change from the C3 patch).** The named
  verifier now prints `142` positive checks instead of `139` (one new forged-receipt
  `req` per round r55–r57). Two committed records quote the old line verbatim —
  `corpus/live/runs/round-58/LEDGER.md:4` and `corpus/live/runs/round-58/reviewer.md:13` —
  and re-running their command on the tip prints `142`, so the quote no longer
  reproduces. The frozen void conditions forbid editing those two files ("changed
  `corpus/live` byte outside new round-63 paths"), so the repair cannot be a record
  edit; the round-63 receipt/ledger (or the lesson's `## Gate`) should disclose the
  count change and that the round-58 quote is a snapshot of the pre-patch script.
  No automated check depends on it (A9), and no hold moves. This is exactly the kind of
  observable-contract drift a falsify wave is for, and it is currently unmentioned in
  `corpus/lessons/round-63.md` and `corpus/live/runs/round-63/LEDGER.md`.
- **F5 (info, working-tree drift observed mid-run).** At final check the lane working
  tree shows peer edits `M corpus/lessons/round-63.md` (revision-trail sentence
  corrected against `R63SourceZipfileDocs §9c`) and `M corpus/SOURCES.md`, plus
  untracked `falsify/` artifacts and `falsify-spec.json`; at this seat's start only the
  five `.ufo/waves/round-63/build/*` files were modified. None is mine, and every tree
  came from `git archive db55bd6` (HEAD unchanged throughout). The frozen counter reads
  none of those two paths — its inputs are `corpus/README.md`, `corpus/live/runs/**/*.json`,
  `corpus/knowledge/seed.md`, the readiness checklist and the ten `verify_*.py` scripts —
  so the three counters here are insensitive to the edits; the C1 entry's SOURCES
  claims are an admission question, not a counter input. L1 still owes
  `reports/round-63/measure-after.log` on the final tip after committing them, per the
  routed round-62 debt.

## Residual risk

- The counterfactual "C3 absent" is defined here as reverting both scripts to `55bcb6e`
  blobs. If L1 instead intended "keep the helper refactor, drop only the new control",
  the C3 mutant would be blocked one step later and still be attributed by the same
  message — but that state was not measured.
- The C3 result depends on the probe's regex deleting exactly one conjunct per script;
  verified now (`findall` count 1, no `could-not-evaluate` printed, mutants syntactically
  valid under 3.14.8). A future reformat of those lines would make the probe exit 2,
  which the contract already treats as could-not-evaluate.
- `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` is a pre-existing hold (also at base), not new
  evidence for C2; only `F_COVERAGE` is the new C2 signal.
- Whether the `139 → 142` drift (F4) counts as a void depends on how the parent reads
  "unchanged scripts otherwise": the frozen fix shape mandates the extra control per
  script, so the count change is forced, but the two committed round-58 quotes are now
  irreproducible and cannot be edited under the same void conditions. This seat records
  it as disclosure-required, not as a counter failure.
- Saturation: this seat makes no saturation claim and did not evaluate fleet saturation;
  the counters are three separate criteria inputs (K, F, calibration) as
  `claims.md` pre-registers.

## Verification gaps

- Q01–Q13 content decisions for the C1 entry: not produced or judged here; none exist
  yet (F1). `W2VerifyEntryRecheck.md` re-runs the entry's own facts and finds no
  mismatch, which is evidence but not a Q-gate decision.
- Byte-oracle agreement for the C2 record: not re-checked here (F2); the record's
  envelope was only inspected for the fields F reads.
- `lsp` device: unavailable in this seat's toolset, so caller/definition checks for the
  mutated conjuncts were done by exact committed-blob inspection (`git show
  HEAD:corpus/verify_*.py`) rather than a language server. For a regex-driven mutation
  counter over two single-file scripts with no cross-file references, this is adequate;
  record it as the fallback, not semantic proof.
- No resume path exists in this lane, so `resume_continuity_v1` preflight rejection is
  not applicable to this assignment.

## Receipts and cleanup

- Tool installs/updates: none (no `uv`, `npx`, `cargo`, `npm`, or pacman transaction).
- Repo writes by this seat: only this report file. No `git`/`jj` mutation, no edit to
  wave spec/registry, `MANIFEST.json`, fleet files, sibling lanes, lane jj state or the
  lane Git index.
- Scratch: `/tmp/revenger-r63-sep` (five archive trees, two partial-patch trees, captured
  `.out`/`.final` logs, 41 MiB) was removed immediately after this report was written —
  the directory no longer exists. Every number it produced is quoted above with its
  output SHA-256, and the tree construction is documented in full so any probe can be
  re-derived from `git archive` in seconds. Sibling-seat scratch directories
  (`/tmp/revenger-r63-*` owned by other seats) were left untouched.
