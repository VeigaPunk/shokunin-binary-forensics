# Curated sources to consider — revenger — batch 2 — 2026-11-03

**Status: unassimilated future reading after hyaku.** Source-candidate review only, not a training round, admission, readiness claim or change to the current plan. Public primary material checked on 2026-11-03 UTC. No candidate code or artifact was executed, no live target tested, no private artifact uploaded and no candidate implementation deployed.

## dnfile: raw CLR metadata versus interpreted resources

[Primary repository](https://github.com/malwarefrank/dnfile)

### Original summary

dnfile provides a readable static CLR metadata/resource implementation. Its design separates raw structures from interpreted attributes and intentionally salvages partially malformed input. The README distinguishes the full stream list from its last-metadata-table-stream shortcut, and raw resource bytes from parsed ResourceSet entries. This gives the managed-assembly province a narrower interpretation problem than batch-one object construction or archive comparison: what exactly did a convenience field omit or interpret?

### Exact source and license

- Version: Default-branch source snapshot `bde05f174e10cc3df72eee45ff7189c1d9e2a28b`, commit dated 2026-07-26T00:38:51Z; no release-to-commit equivalence claimed. HISTORY records 0.18.0, but this pin is a source snapshot, not a verified release tag.
- License: MIT, verified in the pinned repository's license text; retain notices for any later reuse.
- Reading links: [README.rst](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/README.rst) · [DESIGN.rst](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/DESIGN.rst) · [src/dnfile/stream.py](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/src/dnfile/stream.py) · [src/dnfile/mdtable.py](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/src/dnfile/mdtable.py) · [src/dnfile/resource.py](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/src/dnfile/resource.py) · [HISTORY.rst](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/HISTORY.rst) · [LICENSE](https://github.com/malwarefrank/dnfile/blob/bde05f174e10cc3df72eee45ff7189c1d9e2a28b/LICENSE)

### Proposed future review

After hyaku, draft a paper-only field map for an already authorized managed artifact: CLR directory, every metadata stream, ManifestResource row, resource container and entry. Read README “Quick Start”, DESIGN “Main”, `stream.py` `MetaDataTables`, `mdtable.py` `ManifestResourceRow`, and `resource.py` `ResourceSet`; consult HISTORY 0.18.0 and 0.15.0. Ask: does a count/hash describe all streams, raw bytes, or decoded entries? Preserve unknown and partial states.

### Caveats

Tolerant parsing is not full validity, complete coverage or runtime behavior. Dependencies have separate notices. Do not load the assembly, deserialize arbitrary objects, fetch sample binaries or execute parser code in this review.

### Novelty check

No dnfile/malwarefrank match in revenger inventory/full context. Existing dnlib/.NET material is related but a different implementation family. Kaidoku mentions dnfile as an installed tool; this is a new revenger source candidate, not a claim of global novelty or readiness.

## Boundary

Any later adoption requires normal independent review after hyaku. Recheck pins and applicable notices first. This note changes no corpus registry, skill, scorecard, training input, authorization or deployment state.
