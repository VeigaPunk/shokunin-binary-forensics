PASS — corpus/verify_icon_languages.py C5 patch is insertion-only (3+/0-), exactly one new forged-evidence control immediately after the forged-stdout control, receipt_ok byte-identical, transplanted ID is the real round-42 evidence_id, message ends `forged receipt evidence accepted`; frozen mutant is killed and attributed (exit 1, last line ends with the marker). No blocking defect.

# Scope

- Lane: patch-shape review of `corpus/verify_icon_languages.py` only (sibling `corpus/verify_multi_icon_states.py` diff inspected for symmetry, not scored here).
- Base: `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f`; reviewed revision: `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (working tree clean, `git status --porcelain` empty).
- File hashes: `verify_icon_languages.py` = `64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b`; base = `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3`.
- Contract read first: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` (frozen C2 fix shape, mutant regex, attribution predicate).
- Tooling installed this seat: none (nothing needed; no pacman/uv/npx invocation).

# Check results (per brief)

**1. Insertions only — PASS.**
```
git diff --numstat 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f HEAD -- corpus/verify_icon_languages.py
3	0	corpus/verify_icon_languages.py
```
Zero deleted lines; whole-tree diff for the file is `1 file changed, 3 insertions(+), 0 deletions(-)`. No whitespace/EOL churn elsewhere in the file.

**2. Exactly one new control — PASS.**
Three added lines (`forged_evidence=copy.deepcopy(receipt)`, id assignment, `require(not receipt_ok(...), ...)`) form one control. Marker string count in the file is exactly 1 (`forged receipt evidence accepted`), so no duplicated control; `copy` was already imported at base (`import copy`, line 5) and is unchanged, so no import churn.

**3. Placement immediately after the forged-stdout control — PASS.**
```
grep -n "forged receipt (command|stdout|evidence) accepted" corpus/verify_icon_languages.py
151: require(not receipt_ok(forged,...),        f'r{r}: forged receipt command accepted')
154: require(not receipt_ok(forged_stdout,...), f'r{r}: forged receipt stdout accepted')
157: require(not receipt_ok(forged_evidence,...), f'r{r}: forged receipt evidence accepted')
```
New control is the line group 155–157, directly after 153–154, before `return data,record,decoded` (158). All pre-existing saved-input assertions (lines 127–150) untouched.

**4. `receipt_ok` untouched — PASS.**
```
diff <(git show BASE:corpus/verify_icon_languages.py | sed -n '118,120p') <(sed -n '118,120p' corpus/verify_icon_languages.py)
RECEIPT_OK_IDENTICAL
```
Body still `receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes)`; the guard conjunct is present exactly once, so the frozen mutant regex has exactly one match (verified: `mutant_regex_matches: 1`).

**5. Transplanted ID equals round-42 saved evidence_id — PASS.**
Control literal: `ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d`, occurring once in the file.
```
corpus/live/runs/round-42/producer-receipt.json:6: "evidence_id": "ev_6e055332...dc3d"
corpus/live/runs/round-42/inspection.raw.json:1: {"evidence_id":"ev_6e055332...dc3d", ...}
EQUAL: True    (control literal == producer-receipt['evidence_id'])
r42_raw_id_matches: True
```
It is a **real foreign** ID relative to this script: this script's EXPECTED ids are `ev_8ed889…4421` (r47), `ev_6fbaf2…f4b` (r48), `ev_01789…ec0` (r49); the transplanted ID appears in the sibling `corpus/verify_multi_icon_states.py:108` as that script's r42 row, matching claims.md's provenance sentence.

**6. Message ends `forged receipt evidence accepted` — PASS.**
Line 157 literal: `f'r{r}: forged receipt evidence accepted'` (no trailing punctuation, so the counter predicate `last.endswith(C5_MARKER)` matches; `C5_MARKER = "forged receipt evidence accepted"` at `reports/round-65/measure.py:263`, and `run()` at measure.py takes `(stdout+stderr).strip().splitlines()[-1]`).

# Kill-attribution reproduction (read-only scratch, /tmp/r65rev-lang)

Unmutated copy, mirroring the counter's invocation (`--self-test`, cwd = tree root):
```
python3 -B corpus/verify_icon_languages.py --self-test   -> exit=0
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
```
Frozen mutant: remove `receipt['evidence_id']==evidence_id` plus its connecting `and` (regex `receipt\['evidence_id'\]\s*==\s*evidence_id`, 1 match, removed with `re.subn(..., count=1)`):
```
python3 -B corpus/verify_icon_languages_mut.py --self-test -> exit=1
last line: AssertionError: r47: forged receipt evidence accepted
endswith('forged receipt evidence accepted') = True
```
So the kill is attributed by the frozen predicate, and it is non-vacuous: the genuine `require(receipt_ok(receipt,...))` at line 150 pins that the receipt passes every conjunct before the control mutates one field, hence the assertion can only fire because the evidence-id conjunct is gone. Red-before cross-check: control string count in the base blob is `0` (`git show BASE:... | grep -c` → 0), matching `C5_CONTROL_PRESENT=0/2` in reports/round-65/measure-before.log.

After-log cross-check (committed measurement, not re-run by me): `reports/round-65/measure-after.log:42-45` prints `C5_CONTROL_PRESENT=2/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=2/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, consistent with the landed bytes I reviewed.

# Findings by severity

Critical / High: none.

**Low — control proves presence, not binding direction.** A semantically equivalent rewrite `evidence_id==receipt['evidence_id']` would survive both the control and the frozen mutant regex (regex requires `receipt['evidence_id']` on the left). This is inside the claim's frozen fix shape ("delete exactly the conjunct", exactly-one-match regex) and is therefore not a deviation from C2; it is a residual of the text/AST-scan spoof surface already carried as future-counter debt in claims.md §Routed inputs #2.

**Low — maintenance coupling on the literal ID.** The transplanted literal is also `EXPECTED[42]` in the sibling script. If `verify_icon_languages.py` ever gains round 42 in its own EXPECTED table, the control would assert `not receipt_ok` on a receipt carrying the genuine `eid` and break the self-test loudly (fail-closed, acceptable) — no silent-pass path.

**Informational (outside my patch-shape lane, for Main/C1 seats).** At reviewed tip `8214e4d` the committed after-log still prints `K_HELD=8/14` and `K_ROW C05 status=frontier` (`reports/round-65/measure-after.log:1-2`); the frozen C1 after-state (9/14, held) requires the post-admission README flip and a re-measurement at the final tip. Nothing in the C2 patch I reviewed affects those lines.

# Residual risk

- My attribution reproduction used the same regex the counter uses, applied by hand; the counter's own `mutate_c5` fallback also accepts `<clause>\s+and\s+`, which would delete the trailing `and` after the final conjunct — that path cannot apply here because the evidence conjunct is not last (stdout conjunct follows it), and the first pattern matched. Not exercised beyond the primary pattern.
- The self-test exercises only rows 47–49; the control runs per row, so three independent opportunities to fire, all covered by the mutant run (fails at r47 first).

# Verification gaps

- **LSP unavailable:** `xd://lsp` is not mounted ("No such tool: xd://lsp. Mounted devices: ast_edit, debug"), so no semantic `references`/`definition`/`diagnostics` pass was possible. Evidence above is `git diff`/`git show` byte comparison plus direct execution, not grep-as-semantic-proof; the script is self-contained (no cross-file callers of `receipt_ok`), so caller impact is limited to the two call sites inside `check()`.
- Scratch tree left at `/tmp/r65rev-lang` (outside the lane and outside /home/vgpnk/Projects/shokunin); no lane file was modified. Wrote only this report.

# Verdict

PASS — all six brief checks hold on committed bytes; C5 patch is attributable under the frozen kill rule. Recommendation only; admission is L1's.
