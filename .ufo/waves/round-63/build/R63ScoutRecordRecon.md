# R63ScoutRecordRecon — C2 F dry-run

Scout only. Lane tree not modified. No tool install (pacman paused; none needed). Frozen predicate: `reports/round-63/measure.py` lines 36–53 (snapshot C6C4). Full `measure.py` was not executed (it also runs verifier self-tests). The F block was re-run by hand.

## Predicate (observed)

```python
counter = collections.Counter()
for p in sorted((TREE / "corpus/live/runs").rglob("*.json")):
    try:
        x = json.loads(p.read_bytes())
    except (ValueError, UnicodeError):
        continue
    if isinstance(x, dict) and x.get("evidence_id") and x.get("normalized_result") is not None:
        counter[x.get("operation", "unknown")] += 1
families = {
    "native-static": {"inspect_pe_resources"},
    "managed": {"inspect_managed_artifact"},
    "javascript": {"analyze_javascript_application"},
    "android": {"inspect_android_package"},
    "archives": {"inventory_artifact", "inspect_artifact"},
    "firmware": {"inspect_firmware_regions"},
    "browser-runtime": {"inspect_web_page", "capture_browser_scenario", "observe_web_session"},
    "evm": {"inspect_evm_interface"},
}
present = [k for k, v in families.items() if v.intersection(counter)]
```

A family is present iff at least one of its operation names has count ≥ 1. `F_FAMILIES` follows that dict's insertion order, not alphabetical order. `evidence_id` must be truthy (`""` fails). `normalized_result` must be non-None (missing key and JSON `null` both fail, because `.get` returns None). Parse errors are skipped (zero today). Non-JSON files are not read.

## (1) Today, before state — F 4/8

Walk of `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs` (104 `*.json`, 2,786,893 bytes). Output matches `reports/round-63/measure-before.log` lines 7–9:

```
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=4/8 score=5.0
F_FAMILIES=['native-static', 'javascript', 'archives', 'evm']
```

Opened by: `inspect_pe_resources` 30 → native-static; `analyze_javascript_application` 6 → javascript; `inspect_artifact` 4 → archives (`inventory_artifact` is 0); `inspect_evm_interface` 7 → evm.

Not opened: managed (`inspect_managed_artifact` 0), android (`inspect_android_package` 0), firmware (`inspect_firmware_regions` 0), browser-runtime (all three ops 0).

Counted but family-inert: `compare_application_versions` 1, `compare_javascript_export_shapes` 3, `extract_artifact` 2, `inspect_analysis_view` 1, `trace_application_feature` 2, `trace_javascript_semantics` 2.

Read 104, count 58, skip 46, parse errors 0. Not re-extracted from the base git archive; the printed histogram is identical to the frozen before log.

## (2) JSON files the counter reads

Every `corpus/live/runs/**/*.json`, sorted path order. Classification is the frozen gate, not the filename.

### Counted (58)

| rel | operation |
|---|---|
| 20261012T163909Z/artifact-inspection.json | inspect_artifact |
| 20261012T164246Z/artifact-inspection.json | inspect_artifact |
| 20261012T164357Z/analysis.json | analyze_javascript_application |
| round-10/extraction.json | extract_artifact |
| round-11/inner-inspection.json | inspect_artifact |
| round-11/outer-extraction.json | extract_artifact |
| round-11/outer-inspection.json | inspect_artifact |
| round-12/comparison-default.json | compare_javascript_export_shapes |
| round-12/comparison-direct.json | compare_javascript_export_shapes |
| round-12/comparison.json | compare_javascript_export_shapes |
| round-12/v1-analysis.json | analyze_javascript_application |
| round-12/v1-direct-analysis.json | analyze_javascript_application |
| round-12/v2-analysis.json | analyze_javascript_application |
| round-12/v2-direct-analysis.json | analyze_javascript_application |
| round-14/trace.json | trace_javascript_semantics |
| round-18/trace.json | trace_javascript_semantics |
| round-19/inspection.json | inspect_evm_interface |
| round-21/inspection.json | inspect_evm_interface |
| round-22/inspection.json | inspect_evm_interface |
| round-23/inspection.json | inspect_evm_interface |
| round-24/inspection.json | inspect_evm_interface |
| round-25/inspection.json | inspect_evm_interface |
| round-26/inspection.json | inspect_evm_interface |
| round-27/inspection.json | inspect_pe_resources |
| round-28/inspection.json | inspect_pe_resources |
| round-29/inspection.json | inspect_pe_resources |
| round-30/inspection.json | inspect_pe_resources |
| round-31/inspection.json | inspect_pe_resources |
| round-32/inspection.json | inspect_pe_resources |
| round-33/inspection.json | inspect_pe_resources |
| round-34/inspection.json | inspect_pe_resources |
| round-35/inspection.json | inspect_pe_resources |
| round-36/inspection.raw.json | inspect_pe_resources |
| round-37/inspection.raw.json | inspect_pe_resources |
| round-38/inspection.raw.json | inspect_pe_resources |
| round-39/inspection.raw.json | inspect_pe_resources |
| round-41/inspection.raw.json | inspect_pe_resources |
| round-42/inspection.raw.json | inspect_pe_resources |
| round-43/inspection.raw.json | inspect_pe_resources |
| round-44/inspection.raw.json | inspect_pe_resources |
| round-45/inspection.raw.json | inspect_pe_resources |
| round-47/inspection.raw.json | inspect_pe_resources |
| round-48/inspection.raw.json | inspect_pe_resources |
| round-49/inspection.raw.json | inspect_pe_resources |
| round-51/inspection.raw.json | inspect_pe_resources |
| round-52/inspection.raw.json | inspect_pe_resources |
| round-53/inspection.raw.json | inspect_pe_resources |
| round-54/inspection.raw.json | inspect_pe_resources |
| round-55/inspection.raw.json | inspect_pe_resources |
| round-56/inspection.raw.json | inspect_pe_resources |
| round-57/inspection.raw.json | inspect_pe_resources |
| round-59/devin-author/inspection.raw.json | inspect_pe_resources |
| round-59/inspection.stdout.json | inspect_pe_resources |
| round-6/view.json | inspect_analysis_view |
| round-7/comparison.json | compare_application_versions |
| round-7/v2-analysis.json | analyze_javascript_application |
| round-9/trace-exact.json | trace_application_feature |
| round-9/trace.json | trace_application_feature |

### Skipped (46) — read, not counted

25 objects missing `evidence_id`, `normalized_result`, and `operation`:

`20261012T163909Z/native-analyze.json`, `round-12/comparison-default-request.json`, `round-12/comparison-direct-request.json`, `round-12/comparison-request.json`, `round-14/trace-request.json`, `round-15/inspection.json`, `round-17/recovery.json`, `round-18/trace-request.json`, `round-31/attempt-invalid.json`, `round-33/producer-receipt.json`, `round-34/producer-receipt.json`, `round-35/attempt-invalid.json`, `round-35/producer-receipt.json`, `round-36/attempt-interval.json`, `round-36/attempt-overlap.json`, `round-36/producer-receipt.json`, `round-40/verifier-receipt.json`, `round-46/verifier-receipt.json`, `round-50/verifier-receipt.json`, `round-51/attempt-directory160.json`, `round-52/attempt-count.json`, `round-6/view-request.json`, `round-7/comparison-request.json`, `round-9/trace-exact-request.json`, `round-9/trace-request.json`.

21 objects with a truthy string `evidence_id` but no `normalized_result` key and no `operation` key (`.get("normalized_result") is None`, so the gate fails the same way an explicit null would):

`round-32/producer-receipt.json`, `round-37/producer-receipt.json`, `round-38/producer-receipt.json`, `round-39/producer-receipt.json`, `round-41/producer-receipt.json`, `round-42/producer-receipt.json`, `round-43/producer-receipt.json`, `round-44/producer-receipt.json`, `round-45/producer-receipt.json`, `round-47/producer-receipt.json`, `round-48/producer-receipt.json`, `round-49/producer-receipt.json`, `round-51/producer-receipt.json`, `round-52/producer-receipt.json`, `round-53/producer-receipt.json`, `round-54/producer-receipt.json`, `round-55/receipt.json`, `round-56/receipt.json`, `round-57/receipt.json`, `round-59/devin-author/receipt.json`, `round-59/receipt.json`.

## Hypothetical `round-63/inspection.json` — counted

Scratch only: copied the 104 JSON files to `/tmp/revenger-r63-scout-record/corpus/live/runs` (same relative paths). Baseline on that copy reprinted 4/8 and the same histogram. Then wrote only in scratch:

`corpus/live/runs/round-63/inspection.json`

```json
{"evidence_id": "r63-scout-synthetic", "operation": "inspect_firmware_regions", "normalized_result": {"regions": []}}
```

Re-run of the same loop:

```
inspect_firmware_regions: 1   (sole delta)
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
round-63/inspection.json COUNT
```

Confirmed: that shape is counted and opens `firmware`. It does not move any other family.

Same path, bytes replaced in scratch only (each left F at 4/8, file skipped):

- object without `evidence_id`, operation still `inspect_firmware_regions`, `normalized_result` `{}`
- `evidence_id` `""` (falsy)
- `normalized_result`: `null` with truthy `evidence_id` and the firmware operation

Lane check after the scratch write: `corpus/live/runs/round-63/inspection.json` does not exist.

This confirms the counter gate only. It does not satisfy C2: claims.md still requires a real `npx -y rea-agents@6.5.0 inspect-firmware-regions` receipt and byte-oracle agreement with `truth.json`. A hand-authored JSON would move the printed F number and still falsify the claim.

## (3) Leftovers

No `round-63` path under `corpus/live/runs` (rglob name and path check, repeated immediately before this report). No `round-63` directory. No race leftover observed. Top-level children run through `round-59` plus the three `20261012T*` dirs and loose review markdown; nothing named `round-63*`.

Scratch `/tmp/revenger-r63-scout-record` removed after this report.

## Confidence

High on the 4/8 print, the 104-file read set, the gate, and the scratch 5/8 result. Unresolved: byte-identity of today's JSON set versus the base `git archive` (histogram matches the before log; archive not re-extracted). Unresolved for C2 itself: fixture, real inspect run, and oracle agreement — out of this scout's scope.
