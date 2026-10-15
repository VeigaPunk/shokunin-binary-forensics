# Round-1 input ledger — r55–r57 saved-record replay inputs

Machine-readable twin: `reports/round-1/input-ledger.json` (same SHA256 values).

## Boundary

- Measured: 2026-10-15, lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`, HEAD `286033c5f2b1683fb538e86e15667709bb49b054` (matches baseline commit).
- Independently pinned historical corpus root: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus` — from `reports/round-1/brief.md`, never extracted from a record under test. Every embedded historical path in the nine inputs equals this root plus `fixtures/pe-r{N}/fixture.exe`.
- Method: read-only census — SHA256, byte lengths, JSON field extraction, raw fixture byte diff. No tests, no producer call, no CLI-verifier acceptance run, no PE execution. `corpus/` was unmodified by this census (clean `git status` before and after; only `reports/round-1/input-ledger.{json,md}` written).
- Baseline failure context: `corpus/verify_named_multi_icon_states.py` line 67 compares the saved `normalized_result.artifact` (whose path field carries the historical root) against a locally derived path, producing the observed `AssertionError: r55 artifact`. Replay must therefore check historical identity against the pinned root above, and must never accept a path copied out of the field under test.

## The nine pinned inputs

| role | round | path (lane-relative) | bytes | SHA256 |
|---|---|---|---|---|
| fixture.exe | 55 | corpus/fixtures/pe-r55/fixture.exe | 1536 | 41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b |
| fixture.exe | 56 | corpus/fixtures/pe-r56/fixture.exe | 1536 | 911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b |
| fixture.exe | 57 | corpus/fixtures/pe-r57/fixture.exe | 1536 | 71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d |
| inspection.raw.json | 55 | corpus/live/runs/round-55/inspection.raw.json | 4850 | 54ffdeab7108895404efa01edb400c9bc32c36c4f85540babed2f5241137f860 |
| inspection.raw.json | 56 | corpus/live/runs/round-56/inspection.raw.json | 4852 | 59a95f9db16633b337fd058a6d1509c95687445af02d63bb3156309f1811bbe6 |
| inspection.raw.json | 57 | corpus/live/runs/round-57/inspection.raw.json | 4851 | 5c915ebdc4c79a6d98e3b9f374e6e2e67168a1c5b391487ac80bd8e199d34fc8 |
| receipt.json | 55 | corpus/live/runs/round-55/receipt.json | 495 | 1fffb03106c649cb2b1cdb92925347764d8e5546704986e67f57ae44b4bb9733 |
| receipt.json | 56 | corpus/live/runs/round-56/receipt.json | 495 | 1b2bcfe2323219b069b33c64259c9e052a26ef9264cb46b9c4d707ae164066ee |
| receipt.json | 57 | corpus/live/runs/round-57/receipt.json | 495 | ee2ec2875ebeeaa75c54acad671fcb488562051eeb3e17cb62d8a9338be67a91 |

## Per-round extracted identities

Expected receipt command pattern (recomputed from the historical path, not trusted from the string alone):
`npx -y rea-agents@6.4.0 inspect-pe-resources <historical artifact path> --format json` — each saved `receipt.command` matches this pattern exactly for its round.

### r55
- Evidence ID: `ev_db785aec4caaa20630a96a8a3b250ff3aae9c0fa454ff36abe4415725fa22e79` (identical in inspection and receipt)
- Historical artifact path: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe` (verbatim in `subject.local_path`, `parameters.path`, `normalized_result.artifact.path`, `locations[0].path`)
- Subject digest: `41c0132a…572b` = actual fixture bytes = `receipt.fixture_sha256` = `normalized_result.artifact.sha256`; artifact.bytes 1536 = actual length
- `receipt.stdout_sha256` = SHA256 of the actual inspection.raw.json bytes (`54ffdeab…f860`); exit_code 0, duration 0.6324599130020943 s
- Distinguishing observation (fully-resolved control): second `RT_GROUP_ICON` image `resource_id 2` → candidates `[1]`, same-language index `1`, `declared_bytes 48` equals RT_ICON payload length, `size_matches true`
- RT_GROUP_ICON payload: `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a`

### r56
- Evidence ID: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (inspection = receipt)
- Historical artifact path: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r56/fixture.exe` (same four verbatim fields)
- Subject digest: `911f96b3…e83b` = actual fixture bytes = `receipt.fixture_sha256` = artifact sha; 1536 bytes
- `receipt.stdout_sha256` = actual inspection bytes hash (`59a95f9d…bbe6`); exit_code 0, duration 0.6219461870205123 s
- Distinguishing observation (unresolved resource id): second image declares `resource_id 3`; no RT_ICON name 3 exists → candidates `[]`, same-language index `null`, `size_matches null`. Raw fixture bytes differ from r55 at exactly offset 928 (2→3), the group record's `resource_id` low byte.
- RT_GROUP_ICON payload: `672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d`

### r57
- Evidence ID: `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` (inspection = receipt)
- Historical artifact path: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r57/fixture.exe` (same four verbatim fields)
- Subject digest: `71d11fba…494d` = actual fixture bytes = `receipt.fixture_sha256` = artifact sha; 1536 bytes
- `receipt.stdout_sha256` = actual inspection bytes hash (`5c915ebd…4fc8`); exit_code 0, duration 0.6663579299929552 s
- Distinguishing observation (declared-size mismatch): second image resolves `resource_id 2` → candidate `[1]`, same-language index `1`, but `declared_bytes 47` ≠ RT_ICON payload length 48, `size_matches false`. Raw fixture bytes differ from r55 at exactly offset 924 (48→47), the group record's `declared_bytes` low byte.
- RT_GROUP_ICON payload: `78dc9a7dd2d08db459b2bf22958f72fd2d105b56f8c0a28e232a1864a299169c`

### Shared across all three rounds
- Operation `inspect_pe_resources`; provider `rea-pe-resources` ("REA PE resource parser" v1); format pe32-plus, machine 34404; coverage complete (8 examined entries, 3 resources).
- The two RT_ICON payload digests are identical across rounds: `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`, `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`. Only the RT_GROUP_ICON directory resource differs.
- Named group resource: type 14, name `A😀B!` (`utf16le_hex 41003dd800de42002100`, name entry at offset 736, 12 bytes), language 1033.

## Authentication status — observed vs inferred vs unknown

- **Observed:** all nine hashes/lengths above; every cross-consistency equality (receipt stdout ↔ inspection bytes, receipt fixture ↔ fixture bytes ↔ subject/artifact digests, Evidence ID agreement, embedded-path = pinned-root + suffix, command-pattern match, one-byte fixture deltas at the expected record fields).
- **Saved-record self-description, not authentication:** `confidence: "observed"` and `authority: "shipped-artifact"` are fields inside the data under replay. This ledger makes **no producer-authentication claim**: the `npx rea-agents@6.4.0` command was not executed, no engine install or provider readiness is asserted, and live-producer equivalence of these bytes is **unknown**. Replay validates byte-identity and internal consistency of saved records only.
- **Inferred (bounded, from verifier source `corpus/verify_named_multi_icon_states.py` lines 65–70, read-only):** the failure point is the artifact path comparison against a locally derived path; the two forged-claim targets are exactly the r56 candidate list and r57 `size_matches`, whose honest states this ledger pins.

## Runnable replay command (parent)

From the lane root (or a corpus copy with the `corpus/` prefix removed), pins all nine inputs and counts them:

```bash
python3 -B -c 'import hashlib,pathlib; [print(hashlib.sha256((q:=pathlib.Path(p)).read_bytes()).hexdigest(), q.stat().st_size, p) for p in ["corpus/fixtures/pe-r55/fixture.exe","corpus/fixtures/pe-r56/fixture.exe","corpus/fixtures/pe-r57/fixture.exe","corpus/live/runs/round-55/inspection.raw.json","corpus/live/runs/round-56/inspection.raw.json","corpus/live/runs/round-57/inspection.raw.json","corpus/live/runs/round-55/receipt.json","corpus/live/runs/round-56/receipt.json","corpus/live/runs/round-57/receipt.json"]]' | tee /tmp/input-ledger.sha; wc -l < /tmp/input-ledger.sha
```

Expected: `9` rows exactly, equal to the `replay.expected_rows` list in `input-ledger.json` (verified equal at authoring time). Diff parent output against that list; any byte change to any input fails closed.
