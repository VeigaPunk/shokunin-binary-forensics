# Round 40 non-author LEAF review — bounded PASS

**Verdict:** PASS for four saved, fixture-scoped icon-reference states. I read the verifier, the round 36–39 PE fixtures and saved Evidence/receipts, and prior review ledgers. The verifier decodes the PE bytes rather than taking `truth.json` or saved `normalized_result` as its oracle. It independently derives the PE32 machine and resource data-directory mapping; traverses all ID-only resource directories and their entries; reads the two leaf data records, payload locations and hashes; parses the group icon entry; and computes matching icon candidates, same-language selection, and declared-size agreement. It compares each derived `format`, `machine`, `directory`, `directories`, `resources`, `icon_groups`, and `coverage` value against the corresponding saved Evidence field, plus artifact byte count and SHA-256. All four fixture SHA-256 values, Evidence IDs, receipt exit codes, and retained stdout hashes are checked. This supports agreement for **all those parsed/reportable fields**, not every field in the Evidence envelope.

**Exact command**, from `/home/vgpnk/Projects/prymeagnt/revenger`:

```sh
python3 .shokunin/revenger/corpus/verify_icon_states.py
```

**Exact stdout** (exit code **0**; trailing newline):

```text
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
```

The four independently byte-derived state tuples `(group image ID, declared size, icon language, candidate indices, same-language index, size_matches)` are:

| Round | State | Interpretation |
| --- | --- | --- |
| 36 | `(1, 48, 1033, (0,), 0, True)` | Same-language candidate; size agrees. |
| 37 | `(2, 48, 1033, (), None, None)` | Image ID absent; no candidate or size comparison. |
| 38 | `(1, 47, 1033, (0,), 0, False)` | Candidate exists; declared size disagrees with its 48-byte payload. |
| 39 | `(1, 48, 1036, (0,), None, None)` | Candidate exists but differs from group language 1033; no same-language size comparison. |

The verifier compares each fixture to round 36 byte-for-byte and finds exactly one differing byte in each control: round 37 offset 850 `01→02` (group image ID); round 38 offset 846 `30→2f` (declared image bytes); round 39 offset 608 `09→0c` (RT_ICON language 1033→1036). All are 1024 bytes. The four tuples are distinct. Its in-memory forged round 37 Evidence changes `candidate_resource_indices` from `[]` to `[0]` and is rejected by comparing the changed `icon_groups` to a fresh decode of the unchanged fixture. The `except AssertionError` also catches a hypothetical parser assertion, but the same round 37 parser already succeeded in `check_saved`; this does not affect rejection on these fixed bytes.

**Limits/shortcomings:** `normalized_result['limitations']` and the remaining Evidence envelope (`raw_result`, provider/authority/confidence/environment/locations etc.) are not byte-derived or compared by this verifier; calling the check “all reported fields” without this qualification would overstate it. Receipt SHA agreement and fixed Evidence IDs establish internal consistency, not authentication of REA execution, its version, or who produced the JSON. The parser assumes one PE32 `.rsrc` section, 224-byte optional header, numeric resource IDs, three directory levels and well-formed saved fixtures. It checks a tree walk and basic bounds but does not establish full arbitrary-PE validity (for example, no resource-range overlap or virtual-size validation). The matched `coverage.status` is copied as a fixed `complete` label for this walked fixture, not proof of general completeness. The forged-candidate test covers one in-memory negative claim only, not adversarial variants or independently replayed REA. No PE execution, icon-image decoding, Windows language fallback/loading/rendering, or REA rerun was performed.
