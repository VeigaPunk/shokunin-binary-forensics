RESULT: COMPLETE

Axes: C1 coverage K (C09 surface only); EVM readout safety and path confinement. This is not an admission judgment. The frozen base remains C09 uncovered (`corpus/README.md:38`); the new round-62 EVM candidate is not in the frozen archive, so this reviews the planned boundaries against prior code, not a draft.

Severity: MEDIUM, conditional path-boundary hazard; no exploit or outside-root read observed.
Exploit path: a readout that treats saved `subject.local_path` / normalized `artifact.path` as a filesystem locator can escape the archive. Frozen r24 record stores `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r24/fixture.raw` (`corpus/live/runs/round-24/inspection.json:1`). A runner invoked from a wrong CWD can also redirect the prior relative `corpus/...` paths; a symlink under those paths could escape unless rejected. These are conditional risks, not behavior observed in the old walker.
Impact: accidental or record-directed reads outside approved scratch can substitute mutable bytes for the frozen fixture and launder provenance; an untrusted saved path could direct broader local reads. No target bytes were executed, no provider/chain call was made, and no path from the JSON was dereferenced.

Evidence:
- Extracted `a3498e25ad87bf756288812d0ea7c474b09433c7` with `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive <revision> | tar -x -C /fast/scratch/hyaku/revenger-r62/R62SafeEvmReadout`; all inspection below used that archive. Frozen claims `reports/round-62/claims.md:22-34,45-51,73-77` require no producer/chain claims, no pre-credit, and keep C09 uncovered pending admission.
- Prior reproduced block `corpus/knowledge/evm-saved-interface-candidates.md:110-144` is inspected only as code-safety precedent, not factual support: fixed case table; `read_bytes`, `bytes.fromhex`, JSON load and print; manual PUSH-immediate skip; no EVM execution, `eval`/`exec`, subprocess or provider invocation. It uses CWD-relative `Path('corpus/...')` without a resolved-root/symlink guard, and its hex branch blindly slices `[2:-1]`. The prior verifier is likewise read-only Python/JSON/hash logic (`corpus/verify_evm_evidence.py:1-25,63-78`); it was not run.
- Bounded read-only check: `python3 -B /fast/scratch/hyaku/revenger-r62/R62SafeEvmReadout/safe_input_audit.py` (cwd `/fast/scratch/hyaku/revenger-r62/R62SafeEvmReadout`; helper lines 6-28,30-69). Output:
```text
root=/fast/scratch/hyaku/revenger-r62/R62SafeEvmReadout
fixed_cases=(19, 21, 22, 23, 24, 25, 26) paths_checked=21 all_regular_nonsymlink_under_root=yes
r24_raw_bytes=35 sha256=b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93
r24_instruction_starts=[(0, '0x7f'), (33, '0x50'), (34, '0x0')] count=3
r24_pattern_bytes=9 starts=[1] inclusive_spans=[[1, 9]]
r24_saved_id=ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e normalized_functions=0
r24_saved_subject_path_recorded_only=/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r24/fixture.raw
r24_saved_record_sha256=ec9e147db2b042f4d991816fa2a02fe95373de31956730fd1eb4cce5763742cd
```
  This bounded script read the pattern field from frozen `truth.json`; its output is safety/boundary evidence, not the new entry's independent Q03/Q11 derivation. Instruction starts are byte-walk output; `[1,9]` is the search result for that truth-provided pattern, not an independently pinned expected value. The `0x10` in the pattern is an immediate-data byte, not a validated dispatch target. Do not repeat the prior two-occurrence misread.

Smallest remediation for the entry writer:
1. Run only from the frozen archive root in its seat scratch; assert the canonical root/CWD. Keep a closed `{19: fixture.hex, 21..26: fixture.raw}` allowlist and fixed `round-N/inspection.json` names; no user paths, globbing, or CWD fallback.
2. For every relative input reject absolute paths, `..`, symlinks and non-regular files; resolve strictly, require containment under the archive root, and bound file size before JSON/hex decoding. Never open paths from saved JSON fields; compare those fields as data only. Treat Evidence IDs as recorded, not authenticated.
3. Validate r19's exact ASCII `0x`/newline hex carrier before decoding; do not silently strip arbitrary bytes or accept whitespace. Keep raw carrier digest/size separate from decoded-byte digest/size. Bounds-check PUSH immediates; emit raw-byte and instruction counts separately (`r24`: 35 vs 3) and label the r24 embedded `0x10` as data, not a destination.
4. Keep the readout standard-library-only and read/print-only. No `eval`/`exec`, EVM runtime, subprocess, REA invocation, network/RPC, or writes outside the seat scratch. Any saved helper script stays in `/fast/scratch/hyaku/revenger-r62/R62SafeEvmReadout/`.

No source row, gate, README status, candidate entry, or production artifact changed. No tier-A source was opened or claimed by this safety-only slice; no admission or producer/authenticity/runtime claim is made.

Installs/updates: none.
