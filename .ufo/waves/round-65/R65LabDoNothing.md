PASS — do-nothing control meets no target (K 8/14, C05 frontier, C5 0/2, HOLDS_OK_V3=no); C2-only tree flips C5 0/2→2/2 with K fixed at 8/14; C1-only admission tree flips K 8/14→9/14 with C5 fixed at 0/2. Separability holds in both directions; all three probes exit 0.

Seat: R65LabDoNothing (do-nothing control / separability receipt), round 65 attempt 1 (hyaku).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

Pinned inputs (sha256):
- `reports/round-65/claims.md` = `b0b28105af0d284c262e7270b422cc2d408840f642b02322cbb59e5929b9cb47` (read in full before scoring)
- `reports/round-65/measure.py` = `8a2c69c4b0e9a799592c90f0e974ffee05556db5667d7b90ada58f92cf590304`
- `reports/round-65/measure-before.log` = `a91fc56385e8e0b26915d9da532b344237b0f83bcda2feba092c79f67887121f`
- base commit `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f` (`git cat-file -t` → `commit`)

## Probe command (byte-identical invocation for all three trees)

```
cd / && TMPDIR=/tmp/r65-lab-donothing/tmpN \
  python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py \
  /tmp/r65-lab-donothing/tN
```

Scratch root `/tmp/r65-lab-donothing` (disposable, outside the lane). Trees built per the frozen counting command:
`git -C <lane> archive 3eebcdd… corpus | tar -x -C <tree>`. No git/jj mutation was run; the only lane write is this report.

## T0 — do-nothing control (base archive, no claimed work)

Construction: `git archive 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f corpus | tar -x -C /tmp/r65-lab-donothing/t0` (489 files).
Output (log sha256 `a91fc56385e8e0b26915d9da532b344237b0f83bcda2feba092c79f67887121f`):

```
K_HELD=8/14 score=5.7
K_ROW C05 status=frontier
K_ROW C07 status=held
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
C5_CONTROL_PRESENT_verify_icon_languages.py=no
C5_CONTROL_PRESENT_verify_multi_icon_states.py=no
C5_CONTROL_PRESENT=0/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=0/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=no
EXIT=0
```

Receipt identity: `diff /tmp/r65-lab-donothing/t0.log reports/round-65/measure-before.log` → no output, `IDENTICAL_BYTES`. The base tree reproduces the frozen red-before receipt line-for-line, so it meets no target and the counter is deterministic on the base bytes.

## T1 — C2 only (base + the two C5 verifier controls, no C1 files)

Construction: T0 copy, then `git show 8214e4d:corpus/verify_icon_languages.py` and `…verify_multi_icon_states.py` into the tree. `diff -rq t0 t1` reports exactly those two files; no `corpus/fixtures/apk-r65/` and no `corpus/knowledge/round-65-apk-axml-byte-evidence.md` in t1 (checked: both `No such file or directory`). Patch shape (insertions only, 3 lines each):

```
verify_icon_languages.py:
+    forged_evidence=copy.deepcopy(receipt)
+    forged_evidence['evidence_id']='ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d'
+    require(not receipt_ok(forged_evidence,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt evidence accepted')
verify_multi_icon_states.py:
+    forged_evidence = copy.deepcopy(receipt)
+    forged_evidence['evidence_id'] = 'ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421'
+    require(not receipt_ok(forged_evidence, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt evidence accepted')
```

Hashes: languages `64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b`, multi `320bf24ce25c01abce4732f02e97954c9596c690807fbc48e03194c957055818`. Frozen mutant clause `receipt\['evidence_id'\]\s*==\s*evidence_id` matches exactly 1 time per patched script (grep -c → 1, 1), so the frozen mutation is well-defined on this tree.
Output (log sha256 `b3736823bbdf124174a1eb7cc02576035f8c94fa8a45fc84a89b1df2ddcc6718`):

```
K_HELD=8/14 score=5.7
K_ROW C05 status=frontier
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
C5_CONTROL_PRESENT_verify_icon_languages.py=yes
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
C5_CONTROL_PRESENT_verify_multi_icon_states.py=yes
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
EXIT=0
```

Both mutant tails end exactly in `forged receipt evidence accepted` (the frozen attribution marker), and the unmutated controls still pass. C2 alone moves only C5 and `HOLDS_OK_V3`; K and C05 do not move.

## T2 — C1 only (base + entry + fixture + SOURCES rows + the admission row)

Construction: T0 copy, then `git archive 8214e4d corpus/fixtures/apk-r65 corpus/knowledge/round-65-apk-axml-byte-evidence.md corpus/SOURCES.md | tar -x -C t2`; `diff -rq t0 t2` → `README.md`, `SOURCES.md` differ, `only in t2: fixtures/apk-r65`, `knowledge/round-65-apk-axml-byte-evidence.md`. SOURCES row count 37 → 41 (S038–S041, append-only; no `<` lines in the diff). Verifier bytes in t2 are the **base** bytes (`a2fd347e…` / `9345cb8c…`, identical to t0), i.e. no C5 control.
The C05 row was flipped in the scratch copy to the admitted form prescribed by the admission order (this is the one constructed element — see F4):

```
| C05 | Android packages (APK) | `knowledge/round-65-apk-axml-byte-evidence.md` (manual byte-derived AXML/container readout of `fixtures/apk-r65/fixture.apk` only; no install, signing, dex-validity, provider-completeness or authenticity claim) | `fixtures/apk-r65` | held |
```

Constructed README sha256 `ab5d7defe2c62bc31c4db5d14ace44f9993e55ed18a51f8466fa300ec8c9927b`; entry sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`; fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (matches the claimed 947-byte fixture).
Output (log sha256 `40e631e4d61d3471a09e6401b2b80ea4224918409c14be3108cbff779a7bcc98`):

```
K_HELD=9/14 score=6.4
K_ROW C05 status=held
K_ROW C07 status=held
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=9/14
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C5_CONTROL_PRESENT_verify_icon_languages.py=no
MUTANT verify_icon_languages.py c5 exit=0 pass :: PASS: 3/3 group-language states, ...
C5_CONTROL_PRESENT_verify_multi_icon_states.py=no
MUTANT verify_multi_icon_states.py c5 exit=0 pass :: PASS: 4/4 two-image states, ...
C5_CONTROL_PRESENT=0/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=0/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=no
EXIT=0
```

C1 alone moves K 8/14 → 9/14 with `K_HELD_BACKED`/`K_HELD_BACKED_STRICT` equal at 9/14, C05 frontier → held; C5 stays 0/2.

## Separability matrix (measured, not inferred)

| tree | contents | K_HELD | C05 | C5 attributed | HOLDS_OK_V3 | exit |
|---|---|---|---|---|---|---|
| T0 base | none of the claimed work | 8/14 | frontier | 0/2 | no | 0 |
| T1 C2-only | + 2 verifier controls | 8/14 | frontier | 2/2 | yes | 0 |
| T2 C1-only | + entry/fixture/SOURCES + held row | 9/14 | held | 0/2 | no | 0 |

Each claim moves its own frozen label and no other claim's label: C2 → `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` only; C1 → `K_HELD`/`K_ROW C05` only. The two claims are causally separable on the frozen counter.

## Findings / calibration notes

- **F1 — exit 0 is not a target signal.** The do-nothing tree exits 0 because the probe's exit code is round-63 `holds_ok` semantics (`measure.py` last line: `sys.exit(2 if not evaluable else 0 if holds_ok else 1)`), exactly as `claims.md` records for the red-before (`probe exit 0`). Round-end "exit 0" is necessary but proves nothing about C1/C2; only the labels do.
- **F2 — `HOLDS_OK_V3=yes` is blind to C1.** T1 prints `HOLDS_OK_V3=yes` while `K_HELD=8/14` and `C05 status=frontier`, because the frozen formula is `V3 = V2 ∧ C5 attributed==2 ∧ selftest`. This matches the contract (V3 is the C2 additive hold, not a K gate), but round-end acceptance must read `HOLDS_OK_V3=yes` **and** `K_HELD=9/14` **and** `K_ROW C05 status=held`; V3 alone cannot certify C1.
- **F3 — the K axis cannot distinguish a candidate entry from an admitted one.** At HEAD the entry still carries `admission-status: candidate` (line 12 of `corpus/knowledge/round-65-apk-axml-byte-evidence.md`), and the counter's strict scan only excludes entries containing `admission-status: rejected` (`measure.py` `rejected_marked`). My constructed T2 scored `K_HELD_BACKED_STRICT=9/14` with that candidate entry in place. Consequence: `K_HELD=9/14` is necessary but not sufficient for C1; admission remains the Q01–Q13 fresh-seat process gate, and the counter cannot detect an early/unauthorized flip. Non-blocking for the frozen contract, but it should be stated in the round record so a later reader does not read K=9/14 as an admission receipt.
- **F4 — T2 is a constructed tree, not a committed archive.** `git show 8214e4d:corpus/README.md` still has `| C05 | … | frontier |` (as does `5b4d29e`), so no committed tree carries C1 admission. The C1 separability receipt necessarily simulates L1's flip; it demonstrates counter separability only and is not a claim measurement. The C2-only tree T1, by contrast, uses committed verifier bytes from `8214e4d`.
- **F5 — transplant IDs are real and foreign, as claimed.** `ev_6e055332…` is the round-42 evidence ID (`corpus/live/runs/round-42/{LEDGER.md,inspection.raw.json,producer-receipt.json}`) and is transplanted into `verify_icon_languages.py`; `ev_8ed889836…` is the round-47 ID (`corpus/live/runs/round-47/…`) and is transplanted into `verify_multi_icon_states.py`. Cross-script transplant, matching `claims.md` C2; controls still pass unmutated, so the transplanted value differs from each script's own expected ID.

## Restoration / bounds

- All construction and mutation happened only in `/tmp/r65-lab-donothing/t{0,1,2}` and per-run `TMPDIR=/tmp/r65-lab-donothing/tmp{0,1,2}`; scratch trees are disposable and outside the lane. No lane file was modified; no `git`/`jj` mutation was executed. The only lane write is this report.
- No tool install or upgrade was needed (no pacman/uv/npx use).

## Pointers

- Frozen labels: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py` (K block :32-58, C5 block :258-295, exit :332), contract `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md`.
- C5 patch bytes: `git show 8214e4d:corpus/verify_icon_languages.py` / `…verify_multi_icon_states.py` (diff vs base: 3 insertions each).
- Entry status line: `corpus/knowledge/round-65-apk-axml-byte-evidence.md` `admission-status: candidate`.
- README row at HEAD: `git show 8214e4d:corpus/README.md` line 34 → `| C05 | Android packages (APK) | — | — | frontier |`.
- Scratch logs: `/tmp/r65-lab-donothing/{t0,t1,t2}.log` (sha256 above).
