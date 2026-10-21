GRADE: HOLDS — C04 saved unnamed-call end-column visibility, this single mutation only
Frozen revision: `d97761952be256d145d298022de03091de91d358`.
Claimbase: `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration: `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Candidate: `corpus/knowledge/round-62-commonjs-require-name-evidence.md`.
Candidate SHA-256, before = after: `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`.
Axes: visible span drift; independent source/saved derivation; exact restoration. One assigned probe, no campaign.

## Mutant and expected detector
Scratch: `/fast/scratch/hyaku/revenger-r62/R62FMutantJsSpan/`; archive extracted into `tree/`.
Extraction: `/usr/bin/git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d97761952be256d145d298022de03091de91d358 | /usr/bin/tar -x -C /fast/scratch/hyaku/revenger-r62/R62FMutantJsSpan/tree`.
`git rev-parse --verify` printed the full frozen revision above.
Mutated only archived `corpus/live/runs/20261012T164357Z/analysis.json:1`.
Selected `normalized_result.graph.edges` edge ID: `jag_edge_b5c88eb64853f53cff70eaf288a3a9aca4c07f46d577d882da831cd3ca249757`.
Changed its `evidence.location.value.end.column`: **50 → 49**; source fixture and readout unchanged.
A literal-JSON AST replacement applied once to one file; an earlier malformed-metavariable preview was discarded without application.
Expected detector: the entry's unchanged complete readout plus manual source/saved provenance comparison, not an exit-code assertion.
Primary entry evidence: :24 (source call), :34 (saved unnamed span), :37 (equality claim), :129-150 (saved fields/slice), :166,179-180 (independent source-call derivation), :230 (saved stdout edge).
Extracted `readout.py` SHA-256: `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac`, matching entry :80.
All three phases ran exactly `/usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62FMutantJsSpan/readout.py /fast/scratch/hyaku/revenger-r62/R62FMutantJsSpan/tree`.
Each used cwd `/`, `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FMutantJsSpan/tmp`, 30-second timeout.

## Observation: actual outputs
| Phase | exit | stdout lines/bytes | stdout SHA-256 | stderr |
|---|---:|---|---|---|
| pristine | 0 | 25 / 7547 | `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` | empty |
| mutant | 0 | 25 / 7546 | `093951d1666171e1dc5696b1b41ddcb3fb5439b34bf8ae103e500afe94bbc777` | empty |
| restored | 0 | 25 / 7547 | `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` | empty |
Pristine and restored stdout both byte-equal the entry's complete declared stdout; baseline succeeded.
Only stdout lines 8 and 12 changed. Line 8 `record.sha256` changed as recorded below; `record.bytes` remained 193573.
Line 12 exact visible field changes:
- `location.end_column_0based_end_exclusive`: `50` → `49`.
- `location.span_1based_inclusive`: `[1,29,1,50]` → `[1,29,1,49]`.
- `location.span_text_from_fixture`: `"require('./transform')"` → `"require('./transform'"` (closing parenthesis lost).
Independent source stdout line 5 remained exactly:
`{"fixture":"js-r3","span":"require_call","offset_0based":28,"span_0based_end_exclusive":[28,50],"span_1based_inclusive":[29,50],"text":"require('./transform')"}`
Named-edge spans, both name-set deltas and all js-r7-v2 output remained unchanged.
Full actual stdout/stderr: scratch `pristine.stdout/.stderr`, `mutant.stdout/.stderr`, `restored.stdout/.stderr`; exact two-record diff: `pristine-mutant.diff`.

## Inference: manual Provenance diff
**Catches it.** The fixture-derived call still covers `[28,50)` and includes `)`, while the mutated saved location covers `[28,49)` and does not. These independently derived/read fields directly contradict the entry's item 11 equality when the mutant is supplied.
This is not merely output/digest inequality or token presence: :166 and :179-180 derive the source call from source text, while :136-148 read the saved columns and slice that source at those columns. Their actual printed spans/text disagree on the mutant and agree pristine/restored.
Verdict for the assigned manual detector: **KILLED**. An exit-code-only detector would **SURVIVE** (0/0/0); the readout does not automatically reject this mismatch.
Failed Q in the frozen target from this probe: none demonstrated. Q11's in-entry source/saved end-column derivations are present for this narrow claim; this is not an all-values/all-criteria admission audit.
Q13: **no clause-deletion-guard credit**; no verifier clause was deleted or tested, and entry :65 expressly disclaims that credit.

## Restoration evidence and unknowns
Saved-record SHA-256 pristine: `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452`.
Saved-record SHA-256 mutant: `43fc61fce71e39e3b6fad56be7e13fa71ab727223050a8553f4ffdbfdd71cbb7` (full-file digest emitted by unchanged readout, stdout line 8).
Saved-record SHA-256 restored: `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452` (`/usr/bin/sha256sum`).
Restoration ran in `finally`: frozen `git archive -- corpus/live/runs/20261012T164357Z/analysis.json`, then `/usr/bin/tar -x -C <scratch>/tree`; both exits 0, tar stderr empty.
A fresh frozen-archive member piped through `/usr/bin/cmp - <scratch>/tree/corpus/live/runs/20261012T164357Z/analysis.json` printed `restored_archive_cmp_exit=0`.
Fixture `index.js` SHA-256 before/after: `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7`; candidate/readout hashes also unchanged.
Tooling caveat: a capped `read :raw` response was not full-file bytes; its partial-text digest was discarded, not used above. Both tooling anomalies were reported through `xd://report_issue`.
Unknown/out of scope: other Q11 values, other mutants, runtime/provider correctness, ownership and admission. No fixture JS/EVM execution, provider calls, builds, linters, formatters, production edits or admission flips.
VERDICT: HOLDS for the assigned saved-call-span exposure; mutant killed by manual provenance comparison, exact input bytes restored. No correction warranted by this probe.
Installs/updates: none.
