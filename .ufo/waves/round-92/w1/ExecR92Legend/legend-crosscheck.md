# ExecR92Legend — independent cross-check of the C2 legend numbers and the C08 evidence

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, HEAD at check time =
`9402183a9492428fa0064d250746c62a0a2d9ca5` (the freeze commit). All read-only;
writes confined to this wave dir and scratch.

## 1. Saved records over the six surface operations

Method: every `*.json` under `corpus/live/runs/` (135 files) parsed; **78** carry a
truthy top-level `operation` — exactly the frozen probe's `SAVED_RECORDS=78` on the
same committed tree (0 parse failures). Eight records carry one of the six ops in
scope (`inspect_managed_artifact`, `inspect_managed_members`,
`inspect_managed_native_boundaries`, `inspect_web_page`,
`capture_browser_scenario`, `observe_web_session`):

| # | record (`corpus/live/runs/`) | operation | sibling receipt | receipt `exit_code` | receipt oracle result |
|---|---|---|---|---|---|
| 1 | `round-76/inspection.json` | `inspect_managed_artifact` | `receipt.json` present | 0 | none in receipt (no `oracle` key; receipt carries producer command, `fixture_sha256`/`stdout_sha256`, `evidence_id`, run_date 2026-11-01) |
| 2 | `round-77/inspection.json` | `inspect_web_page` | `receipt.json` present | 0 | none in receipt (no `oracle` key; receipt notes state the oracle verdict is re-derived from committed bytes, not stored in the receipt) |
| 3 | `round-85/inspect-managed-artifact/inspection.json` | `inspect_managed_artifact` | `receipt.json` present | 0 | `ORACLE OK (20/20 checks)` |
| 4 | `round-85/inspect-managed-artifact/receipt.json` | `inspect_managed_artifact` | — (is itself a receipt) | 0 | `ORACLE OK (20/20 checks)` |
| 5 | `round-85/inspect-managed-members/inspection.json` | `inspect_managed_members` | `receipt.json` present | 0 | `ORACLE OK (47/47 checks)` |
| 6 | `round-85/inspect-managed-members/receipt.json` | `inspect_managed_members` | — (is itself a receipt) | 0 | `ORACLE OK (47/47 checks)` |
| 7 | `round-85/inspect-managed-native-boundaries/inspection.json` | `inspect_managed_native_boundaries` | `receipt.json` present | 0 | `ORACLE OK (39/39 checks)` |
| 8 | `round-85/inspect-managed-native-boundaries/receipt.json` | `inspect_managed_native_boundaries` | — (is itself a receipt) | 0 | `ORACLE OK (39/39 checks)` |

Notes.

- `capture_browser_scenario` and `observe_web_session`: **zero** saved records.
- The three round-85 receipts carry a top-level `operation`, so the probe counts
  them as saved records too (each appears once inside `SAVED_RECORDS=78`).
- Probe `ROW_OPS` maps `C03 → {inspect_managed_artifact}` and
  `C08 → {inspect_web_page, capture_browser_scenario, observe_web_session}`;
  `round-77/target-listing.json`'s `list_browser_targets` is in neither set, so the
  C08 flag rests solely on `round-77/inspection.json`.

## 2. C08 — work evidence or rejected candidate?

Observed on `corpus/live/runs/round-77/inspection.json` and `target-listing.json`:

- No `rejected` field/marker and no quarantine marker anywhere in the round-77
  directory (byte-level scan for `admission-status`, `rejected`, `quarantin`:
  **0 hits**).
- Both records carry `confidence="observed"`, `authority="external-service"`,
  an `evidence_id`, `provider.id="rea-cdp-browser"`, and a populated
  `normalized_result` (browser product Chrome/156.0.8078.74, target
  `http://127.0.0.1:8477/index.html`, capture window timestamps).
- Sibling `receipt.json`: `exit_code=0`, `stderr_bytes=0`, fixture and stdout
  sha256 recorded, run_date 2026-11-01.

**Verdict: work evidence.** These are saved producer runs with passing receipts;
they are not rejected candidates (no rejection marker exists) and not quarantined
material. They have never been through an admission gate, so they are also not
admitted knowledge. No admitted knowledge entry covers the browser surface: the
coverage map's C08 knowledge cell is `—`, and the only `corpus/knowledge/` files
matching browser/CDP terms are census/roadmap context in `seed.md` (no
browser mention at all) and `admission-status: candidate` files
(`round-72-tool-landscape.md`, `round-73-re-resource-atlas.md`,
`claude-red-re-bridge.md`). Under the README legend ("`uncovered` — work evidence
exists but no admitted knowledge entry"; "`frontier` — no knowledge and no saved
record"), C08's `frontier` token is wrong **because the saved record exists**; the
legend-correct token is `uncovered`.

## 3. Frozen probe reproduced independently of the counter

Command (per seat spec): `git -C <lane> archive HEAD corpus | tar -x -C
$S/probe-tree`, then `cd / && TMPDIR=$S/tmp python3 -B
reports/round-66/measure.py $S/probe-tree` (probe exit 1 = base `holds_ok` false,
expected on the do-nothing tree and not a claim verdict). Verbatim lines:

```
K_HELD=8/15 score=5.3
K_HELD_BACKED=8/15
README_TOKEN_LEGEND_MISMATCH=2 rows=['C03', 'C08']
```

Corroborating context from the same run: `K_HELD_BACKED_STRICT=8/15`,
`SAVED_RECORDS=78`, `F_COVERAGE=8/8 score=10.0`, `HOLD_CALIBRATION=4/4`,
`HOLD_REPLAY=10/10`.

## 4. Frozen counter verbatim (`c2_legend_counter.py --rev HEAD`)

```
C2_PROBE_EXIT=1 (probe exit is not the claim verdict)
C2_LEGEND_MISMATCH=2 rows=['C03', 'C08']
C2_ROWS_COUNT=15
C2_K_HELD=8/15 C2_K_HELD_BACKED=8/15
C2_ROWS_TOTAL=pass
C2_C08_CLEAR=fail
C2_NO_NEW=fail
C2_NO_UNBACKED=pass
C2_VERDICT=fail
```

Counter exit 1. This is the do-nothing base state recorded in
`controls/c2-do-nothing.log`; the pass verdict is the post-landing state the L1
runs after the C08 row moves.

## 5. Agreement and per-row verdicts

- **Agreement:** the independent probe and the frozen counter report identical
  mismatch rows (`['C03', 'C08']`) and identical held counts (`8/15`,
  `8/15`). No disagreement, nothing to attribute.
- **Row C03** — legend-correct token on the committed tree: **`uncovered`**
  (work evidence exists: `corpus/live/runs/round-76/inspection.json`,
  `corpus/live/runs/round-85/inspect-managed-{artifact,members,native-boundaries}/inspection.json`,
  fixtures `corpus/fixtures/managed-r76`, `managed-r85`; no admitted knowledge
  entry — the knowledge cell is `—` and every managed-mentioning knowledge file
  is census context or `admission-status: candidate`). `frontier` is wrong now;
  `held` becomes correct **only** if the round-92 C1 entry lands admitted and the
  row cites it (C1's move, gated by `c1_k_admit_counter.py`).
- **Row C08** — legend-correct token: **`uncovered`** (work evidence exists:
  `corpus/live/runs/round-77/inspection.json` + `receipt.json`, fixture
  `corpus/fixtures/browser-r77`; no admitted knowledge entry, none claimed this
  round). `frontier` is the legend mismatch the C2 move repairs.

## Defects

None found in the frozen counter or the probe. `c2_legend_counter.py`'s internal
archive/probe run matches my independent reproduction byte-for-legend; the
`K_HELD` regexes cannot collide with `K_HELD_BACKED`; `C2_ROWS_COUNT` = 15 over
the committed README. Note (not a defect): the counter's scratch lives under
`$HYAKU_SCRATCH/revenger-r92/c2/` by its own frozen code — outside my seat
scratch, left in place.
