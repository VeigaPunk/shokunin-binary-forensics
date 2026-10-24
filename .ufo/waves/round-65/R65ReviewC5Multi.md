PASS — every patch-shape check holds for `corpus/verify_multi_icon_states.py` at HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` against base `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f`, and the frozen C5 mutant is attributed (exit 1, last line ends `forged receipt evidence accepted`) while base+mutant exits 0.

Seat: R65ReviewC5Multi (read-only leaf). Artifacts read: `reports/round-65/claims.md` (frozen contract), `.ufo/waves/round-65/wave-spec.json` entries `R65ReviewC5Lang`/`R65ReviewC5Multi` (twin checklist), lane git bytes. No production edits; no tool installs (nothing needed; `python3` present).

## Axes (godspeed)
- calibration (my judgment axis): C5 evidence-id transplant guard shape and attribution.
- invariances: base-vs-HEAD minimality, `receipt_ok` byte-identity, no dependent breakage.

## Per-check verdicts

| # | Check (twin brief + frozen contract §C2) | Verdict | Evidence |
|---|---|---|---|
| 1 | Insertions only | PASS | `git diff --numstat 3eebcdd7..HEAD -- corpus/verify_multi_icon_states.py` → `3 0`; one hunk only: `git diff -U0 … \| grep -c '^@@'` → `1`; patch is `@@ -153,0 +154,3 @@ def check(round_id):` (pure insert). |
| 2 | Exactly one new control | PASS | The 3 inserted lines at `corpus/verify_multi_icon_states.py:154-156` are one control: `forged_evidence = copy.deepcopy(receipt)` / `forged_evidence['evidence_id'] = 'ev_8ed8…4421'` / `require(not receipt_ok(forged_evidence, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt evidence accepted')`. No other insertion anywhere in the file. |
| 3 | Placed after the forged-stdout control | PASS | Insertion offset `+153,0` → new lines 154-156, immediately after the pre-existing forged-stdout require at `corpus/verify_multi_icon_states.py:153`; forged-command control at `:150`; both retained (diff has 0 deletions). Function order in `check()`: genuine receipt (`:147`) → forged command (`:150`) → forged stdout (`:153`) → forged evidence (`:154-156`) → `return data, report, decoded, state` (`:157`). |
| 4 | `receipt_ok` untouched | PASS | `git diff 3eebcdd7..HEAD -- corpus/verify_multi_icon_states.py` shows no hunk touching `receipt_ok`; direct comparison of lines 121-124 base vs HEAD: `diff <(git show 3eebcdd7:corpus/verify_multi_icon_states.py \| sed -n '121,124p') <(sed -n '121,124p' corpus/verify_multi_icon_states.py)` → empty (`receipt_ok_identical=yes`). Blob hashes: base `f0db71c791007298e5be386cd992ea766dfd3eaa` → HEAD `de8cc2bd0a5b410180c05b18c4092d600e85fc46` (only the 3 lines differ). |
| 5 | Transplanted ID equals `corpus/live/runs/round-47/`'s saved evidence_id | PASS | Script literal `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421` (67 chars = `ev_` + 64 hex). Programmatic equality: `== corpus/live/runs/round-47/producer-receipt.json` `evidence_id` → `True`; `== corpus/live/runs/round-47/inspection.raw.json` `evidence_id` → `True`. Also equals `corpus/verify_icon_languages.py` `EXPECTED[47]` ID (`in languages EXPECTED[47]: True`, cf. `corpus/verify_icon_languages.py:108`), matching claims.md's "the languages script's round-47 ID". **Foreign to the multi script**: `False` containment in multi's own `EXPECTED` (`corpus/verify_multi_icon_states.py:106-119` = r42 `ev_6e0553…`, r43 `ev_c9f912…`, r44 `ev_7915751…`, r45 `ev_4949e5…`), and it is a real saved receipt ID, not a synthetic hash. |
| 6 | Message ends `forged receipt evidence accepted` | PASS | `corpus/verify_multi_icon_states.py:156` message `f'r{round_id}: forged receipt evidence accepted'`; only occurrence of the marker in the file (`grep -c` → `1`), so the counter's `C5_CONTROL_PRESENT` anti-spoof substring cannot be satisfied by a comment. |

## End-to-end behavior (executed, not inferred)

Fresh archive of HEAD into `/tmp` scratch, run from `/`:

```
git archive HEAD corpus | tar -x -C $T
python3 -B $T/corpus/verify_multi_icon_states.py
→ PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
  rc=0
```

Frozen mutation, applied with `reports/round-65/measure.py`'s own `mutate_c5` logic (regex `receipt\['evidence_id'\]\s*==\s*evidence_id`, `clause_hits=1`, connector `and` removed, `deleted=1`; resulting `receipt_ok` compiles and reads `… expected_hash and receipt['stdout_sha256']==H(raw_bytes))`):

```
python3 -B $W/corpus/verify_multi_icon_states.py   # mutant
→ rc=1
→ AssertionError: r42: forged receipt evidence accepted
  last_line_ends_marker=1
```

Red-before on the base tree (same mutant, control absent):

```
grep 'forged receipt evidence accepted' base script → base_has_marker= False
base+mutant → rc=0
→ PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
```

Frozen counter reproduces the C2 after-state on the HEAD archive (`TMPDIR=$T python3 -B reports/round-65/measure.py $T`, from `/`; `measure_rc=0`):

```
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
C5_CONTROL_PRESENT_verify_icon_languages.py=yes
C5_CONTROL_PRESENT_verify_multi_icon_states.py=yes
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLDS_OK_V3=yes
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, …
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
```

Matching red-before receipt `reports/round-65/measure-before.log`: `C5_CONTROL_PRESENT=0/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK_V3=no`.

## Invariants / dependents checked

- The multi script is self-contained: `root = Path(__file__).resolve().parent` (`:8`), `HIST` used only for path strings (`:9-10`); the control reads no external run directory, so the guard cannot break if `corpus/live/runs/round-47/` is later moved. No runtime dependency on the literal's provenance.
- No executable depends on the script's line numbers or hash: repo-wide grep for `verify_multi_icon_states` finds only prose/history (`corpus/knowledge/digest-scope-versus-provenance.md:151-156` counts `receipt['command']` occurrences — still 1 at `:122`, unchanged; `corpus/lessons/round-64.md:59-60,142` cite `:150`/`:153`, both unchanged because the insertion starts at `:154`). No test or script hashes the verifier.
- Control executes for all four rounds (`rows={r:check(r) for r in EXPECTED}`, `:160` for r42-45), so the guard is live code, not dead.
- Script bytes at the receipt's measured revision are identical to HEAD: `git diff --stat 6f1761a9..HEAD -- corpus/verify_multi_icon_states.py` → empty; blob `de8cc2bd…` both ends.
- Scope note (not a defect): at HEAD the counter prints `K_HELD=8/14`, `K_ROW C05 status=frontier` — correct for this wave stage, since the README flip is L1's admission step per claims.md "Admission order" §3; my seat judges only C2's script patch.

## Residual risk

1. Under the mutant, the failure aborts at r42, so rounds 43-45's copies of the control never execute in the killed run. Attribution therefore rests on one round; the frozen kill rule accepts a single attributed kill, and unmutated all four rounds exercise it. No action needed.
2. The guard is syntactic: it proves `receipt_ok` rejects a mismatched `evidence_id` literal, not that an Evidence ID is cryptographically bound to a receipt. claims.md already fences this — prongs (a)/(b) and the injectivity registry remain future-round debt.
3. `C5_CONTROL_PRESENT` is a substring test; the current tree contains the marker exactly once (the require line), and a no-op transplant would fail `C5_CONTROLS_PASS` (a same-ID deep copy makes `receipt_ok` true and the assertion fails), so this tree is not spoofable — but the anti-spoof property is emergent from tree bytes, not structurally enforced by the counter.
4. The "real foreign" property is re-derivable only while `corpus/live/runs/round-47/` or `EXPECTED[47]` persists; both currently do.

## Verification gaps

- The twin seat `R65ReviewC5Lang`'s report had not landed in `.ufo/waves/round-65/` at review time, so I took the checklist from the authoritative wave-spec entries (`R65ReviewC5Lang` prompt: insertions only / exactly one control / after forged-stdout / `receipt_ok` untouched / ID equality / message suffix) rather than from its output.
- No `lsp` device is exposed to this seat (tool set: read/bash/edit/eval/glob/grep/task/wait/web_search/write/yield), so no server-backed `references`/`diagnostics` pass was possible; I substituted execution-level evidence (unmutated exit 0, mutant exit 1 with marker, base+mutant exit 0, frozen counter 2/2) which is stronger than textual reference resolution for this artifact. Recorded as tooling unavailability, not as absence of defects.
- I did not re-run the rest of the C1 lane (fixture/entry/admission) — out of this seat's scope.

Report: .ufo/waves/round-65/R65ReviewC5Multi.md
