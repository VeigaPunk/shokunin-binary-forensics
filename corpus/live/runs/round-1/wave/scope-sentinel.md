# Scope sentinel — round 1 coverage

## Boundary assessment

**Conclusion:** The intended boundary is appropriately narrow: static analysis of the locally compiled checksum fixture only, with writes confined to the wave report. No live target, target execution, engine installation, or unrelated host setup is authorized. Existing evidence shows provider-neutral artifact inventory and an unavailable native-analysis provider; it does not show execution or semantic recovery.

## Concrete observations

- `.shokunin/revenger/LOG.md` Round 1 declaration states “No runtime target execution is authorized beyond fixture compilation; REA static inspection only” and limits each leaf worker to its individual report under `corpus/live/runs/round-1/wave/`. The scope-sentinel row assigns this fixture as its artifact.
- `PROVINCE.md` labels REA skill references and corpus as read-only sources, restricts writes to `.shokunin/revenger/**` and own reports, and refuses live-target execution beyond declared target/lifecycle.
- `corpus/fixtures/checksum-r1/checksum.c` is a local fixture source (checksum and ASCII rotation routines; `main` prints a transformed value and checksum). Reading source is static review; do not invoke the resulting program. `checksum` is the designated fixture artifact.
- `corpus/live/runs/20261012T163909Z/artifact-inspection.json`: Evidence `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c` records `inspect_artifact`, SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`, ELF, 16,160 bytes. Nested inventory Evidence `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` is from `rea-artifact-graph`; it inventories one file, zero edges, and explicitly says it does not execute or claim format-specific semantics. It recommends `open_binary` as a next probe, not as permission to broaden scope.
- `native-analyze.json` reports `provider_unavailable` for `current_document`: Ghidra not configured (`GHIDRA_INSTALL_DIR` absent), Hopper launcher missing, IDA not configured. This is a capability blocker, not a reason to install engines. Its stderr is empty.
- The REA skill’s `SKILL.md` says runtime requests execute the declared target and lifecycle and must not be broadened; its native guide states `inspect_binary_layout` is offline, while `observe_native_calls` launches a new process. Therefore any runtime route is out of scope here.

## Risks and guardrails

1. **Execution by accident:** invoking `checksum`, running it through a debugger, or using a runtime observation route would cross the stated boundary. Avoid all such actions.
2. **Scope creep from unavailable provider:** do not install/configure Ghidra, Hopper, IDA, Java, or other engines; the standing brief expressly bars setup beyond approved REA acquisition and unrelated installs, and this worker has no setup task. Report blocker as telemetry.
3. **Writes:** do not alter fixture, logs, shared evidence, environment configuration, or Git state. Only this report path is writable for this worker.
4. **Evidence overclaim:** artifact graph inventory is static format/container evidence, not proof of checksum behavior. Source inspection provides expected behavior by construction but is not an executed test. No Evidence ID here establishes function-level native findings or a scored precision result.
5. **Containment:** remain within `.shokunin/revenger` and only write the assigned report. No network access or unrelated target search is needed.

## Limits

This review was a read-only examination of the standing brief, lane files, fixture source, saved JSON/error records, and relevant REA instructions. I did not run the fixture, compiler, REA CLI, or setup diagnostics, and did not verify current tool registration. I cannot establish whether a particular analysis command would execute code beyond the documented routes; use only a route explicitly confirmed static and within the parent’s declared scope. The fixture’s provenance/build flags and any compilation-time side effects were not independently checked.
