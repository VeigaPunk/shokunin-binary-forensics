# Replay scenarios — fleet round-1 saved-ledger battery

Runner: `reports/round-1/replay_scenarios.py` (stdlib only, deterministic, no mocks).
It invokes the real named two-image PE saved-record verifier CLI
(`corpus/verify_named_multi_icon_states.py`) in a fresh subprocess per scenario.
Evidence-runner interface only — it is not production verifier scope and edits
no verifier, fixture, raw record or receipt.

## Usage (parent, after integration)

Acceptance (lane root):

    python3 -B reports/round-1/replay_scenarios.py

PASS shape: `POSITIVES met=3/3`, `EXPECTED_REJECTIONS met=6/6`,
`INPUTS met=9/9`, `VERIFIER_SCRIPT met=1/1`, `CLEANUP met=1/1`,
`RESULT PASS exit=0`. Any unmet acceptance prints an `ACCEPTANCE-MISS` line
with observed exit/diagnostic and exits nonzero — so if positives fail the run
fails clearly, per scenario.

Reproducible before measurement (optional; frozen baseline evidence at
baseline commit 286033c5 is already captured in `baseline.txt`): stage an
isolated archive of the baseline corpus, e.g.
`git archive 286033c5f2b1683fb538e86e15667709bb49b054 corpus | tar -x -C /tmp/baseline-r1`,
then `python3 -B reports/round-1/replay_scenarios.py --corpus /tmp/baseline-r1/corpus`.
Against the original verifier the three positives genuinely fail
(`AssertionError: r55 artifact`, exit 1) because the saved producer path is
compared with the relocated current location; the runner reports
`POSITIVES met=0/3` and `RESULT FAIL`. `--keep-temp` retains staged trees for
inspection instead of deleting them.

## Guarantees

- Originals never written: SHA-256 snapshots of the three `fixture.exe`,
  three `inspection.raw.json`, three `receipt.json` (the 9 inputs) plus the
  verifier script are emitted before and after all scenarios; the runner fails
  acceptance if any digest moves.
- All scenario executions and every forgery happen in fresh isolated temporary
  copies (`tempfile.mkdtemp`), removed afterwards; cleanup is verified and
  tallied.
- Machine-readable output: one JSON line per event (scenario verdicts include
  exit, diagnostic, forgery diff paths, expectations), plus plain tally lines.
- No producer rerun, no PE execution, no network; the verifier itself only
  parses bytes.

## Positives (verifier replay works after corpus move)

| id | shape | command shape | expect |
|----|-------|---------------|--------|
| P1 | lane-root CLI | `python3 -B corpus/verify_named_multi_icon_states.py` with CWD at the corpus's lane root | exit 0, last stdout line starts `PASS:` |
| P2 | unrelated CWD | same script by absolute path, CWD an unrelated temporary directory | exit 0, `PASS:` |
| P3 | relocated copy | minimal corpus closure (verifier + 3 fixtures + 3 raw + 3 receipts) staged under a directory containing spaces and non-ASCII (`replay 快照 ünïcode ✓`), invoked as `corpus/verify_named_multi_icon_states.py` from that staged lane-root equivalent | exit 0, `PASS:` |

## Expected rejections (isolated copies with one forged saved field)

| id | round | forgery (single declared field) | raw/receipt handling | expected exit | expected stable diagnostic |
|----|-------|--------------------------------|----------------------|---------------|----------------------------|
| N1 | 55 | `normalized_result.artifact.path` relabeled from the historical producer path to the relocated copy's own absolute fixture path | raw rewritten; receipt `stdout_sha256` regenerated only | 1 | `AssertionError: r55 artifact` |
| N2 | 55 | `receipt.command` relabeled to the relocated copy's fixture path (tool/version/format unchanged) | receipt only; raw and `stdout_sha256` untouched | 1 | `AssertionError: r55 receipt` |
| N3 | 56 | `icon_groups[0].images[1].candidate_resource_indices` `[]`→`[1]` | raw rewritten; `stdout_sha256` regenerated only | 1 | `AssertionError: r56 normalized result` |
| N4 | 57 | `icon_groups[0].images[1].size_matches` `False`→`True` | raw rewritten; `stdout_sha256` regenerated only | 1 | `AssertionError: r57 normalized result` |
| N5 | 55 | `resources[2].name.location.offset` `736`→`700` (the recorded `A😀B!` UTF-16 name, bytes unchanged) | raw rewritten; `stdout_sha256` regenerated only | 1 | `AssertionError: r55 normalized result` |
| N6 | 55 | `resources[2].entry_locations[0].offset` `536`→`520` (ancestor type-directory entry) | raw rewritten; `stdout_sha256` regenerated only | 1 | `AssertionError: r55 normalized result` |

Each prior value is asserted from the unchanged saved record before forging;
after forging, the runner re-reads both files from disk and fails itself
(scenario ERROR → unmet acceptance) unless the JSON diff is exactly the
declared field (plus `stdout_sha256` for raw mutations), unless both Evidence
IDs are untouched and mutually equal, and unless the receipt's
`stdout_sha256` still hashes the raw bytes as written.

## Why regenerate only `stdout_sha256`

The verifier's receipt check includes `receipt.stdout_sha256 == sha256(inspection.raw.json)`.
Mutating a saved report without regenerating that hash would leave an
incidental raw-hash inconsistency in the copy; the rejection could then be
attributed to hash drift instead of the claim being wrong. Regenerating only
that one field makes each forged copy internally consistent, so the only
remaining contradiction is semantic: the saved claim versus the byte-derived
decode (N3–N6) or versus the independently pinned historical identity (N1–N2).
A correct replay fix therefore rejects with the pre-existing semantic
diagnostics above, and the runner asserts those exact final diagnostic lines
and exit codes.

## Why relabel-to-relocated-copy for the path forgeries

The round-1 claim is that replay must not be achieved by laundering saved
identity. N1/N2 rewrite the recorded producer path and receipt command to the
location where the copy happens to live — precisely the "accept a path by
copying it out of the field under test" failure mode the brief forbids. If an
implementation "fixes" the baseline failure by comparing those fields against
the current script location instead of an independently pinned historical path,
N1/N2 pass acceptance wrongly is impossible: the verifier would accept the
forgery and the runner reports `ACCEPTANCE-MISS` on the expected rejection —
exposing the weakening.

## Authenticity limit (explicit)

Evidence IDs are never changed by the battery, and that is also its boundary.
These scenarios prove internal, semantic consistency: the saved normalized
result must agree with the SHA-256-identical fixture bytes as decoded from the
present corpus, receipt stdout hashes must agree with the raw bytes as stored,
and recorded producer paths/commands must match independently pinned
historical values. They do not prove producer authenticity: nothing external
attests that the pinned constants, the fixture bytes, or the whole consistent
raw+receipt pair were produced by `rea-agents@6.4.0`. An adversary with write
access to both files could keep every hash self-consistent while substituting
a byte-identical claim set; only source-integrity custody of the verifier's
pinned constants and of the corpus itself (out of replay scope) bounds that.
L2 review here is author-side evidence, not independent promotion or
outside-discernment verification.

## Observed vs inferred vs unknown

- Observed (data-only census of the present corpus): saved artifact paths and
  receipt commands carry the historical prefix
  `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus`; r55/r56/r57
  Evidence IDs match the verifier's pinned `EXPECT`; r56 image 1 candidates are
  `[]`, r57 image 1 `size_matches` is `False`; the UTF-16 name location is
  offset 736/bytes 12 and ancestor entry locations are 536/592/664 (8 bytes
  each); baseline pre-measurement: verifier exit 1, `AssertionError: r55
  artifact` (frozen in `baseline.txt`).
- Inferred (from the brief's fix contract): after integration the verifier
  compares historical identities to independently pinned values while reading
  fixture bytes from the present corpus, retaining the existing diagnostic
  message strings the negatives assert.
- Unknown (until parent integration): the fixed verifier's exact source; the
  battery's post-fix verdicts. The runner asserts only the existing stable
  strings — `PASS:` prefix on positives, listed `AssertionError: …` final
  lines on negatives — and no execution was performed during this wave.
