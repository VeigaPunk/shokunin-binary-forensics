# pe-route-sentinel — round 27

## Verdict: PASS

Lane proves REA PE resource route is distinct from EVM, ZIP, ELF-via-artifact-graph, and JS-graph routes.

## Evidence identity

- Path: `corpus/live/runs/round-27/inspection.json`
- `evidence_id`: `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef` (matches task)
- `operation`: **`inspect_pe_resources`** (exact string)
- Not: `inspect_evm_interface`, `inspect_artifact`, `inventory_artifact`, `analyze_javascript_application`, or any JS-graph op
- Provider: `rea-pe-resources` / "REA PE resource parser" v1
- Subject format: `pe`; normalized `format`: `pe32`; machine 332
- Normalized shape: PE resource directory tree (`directory`, `directories`, `resources` with type/name/language ids, payload RVA/locations) — PE-specific, not EVM functions/bytecode, not ZIP occurrences, not ELF open_binary probes

## Search hits (`inspect_pe_resources` / `inspect-pe-resources`)

Under `.shokunin/revenger` (excluding noise):

1. `corpus/verify_pe_resources.py` — requires `operation == "inspect_pe_resources"` and expected evidence id
2. `corpus/live/runs/round-27/inspection.json` — saved Evidence
3. `LOG.md` — mention
4. `__pycache__/verify_pe_resources.cpython-311.pyc` — bytecode of verifier

No hyphenated `inspect-pe-resources` string required in Evidence; saved op uses underscore form.

## Verifier path absent at baseline commit

Command:

`git cat-file -e f27b5f1a92af4f05081e7992925e30d621fff1c0:.shokunin/revenger/corpus/verify_pe_resources.py`

Result: **fail** (exit 128). Message: path exists on disk, but **not in** `f27b5f1a92af4f05081e7992925e30d621fff1c0`.

HEAD at check time was `f27b5f1` (`revenger r26: report controlled calibration and pause`). On-disk verifier is therefore **new relative to that baseline** (r27 PE route), not a rename of EVM/ZIP verifiers.

## Contrast with other routes (same tree)

| Route | Operation string | Typical provider | Fixture class |
|-------|------------------|------------------|---------------|
| PE resources (r27) | `inspect_pe_resources` | `rea-pe-resources` | `fixture.exe` / pe-r27 |
| EVM (r19–r26) | `inspect_evm_interface` | `evmole-interface` | `fixture.raw` / hex |
| ZIP / archive | `inspect_artifact` (+ `inventory_artifact`) | `rea-artifact-graph` | `fixture.zip` |
| ELF as graph root | `inspect_artifact` | `rea-artifact-graph` | checksum ELF |
| JS application | `analyze_javascript_application` (historical promotion notes) | JS graph | JS sources |

Dedicated verifiers:

- `verify_pe_resources.py` → PE op + PE expected id
- `verify_evm_evidence.py` → `inspect_evm_interface`
- `verify_saved_evidence.py` → ZIP `inspect_artifact`

## Conclusion

Saved r27 Evidence is a first-class **PE resource-table** REA operation with its own provider, schema, fixture, and verifier path that did not exist at `f27b5f1`. Route is not a relabel of EVM, ZIP, ELF graph, or JS-graph work.
