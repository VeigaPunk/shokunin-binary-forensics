# R64SnapshotManifest

## Files changed
- `.ufo/waves/round-64/snapshot-manifest.json` — SHA-256 and byte size for all 13 requested frozen inputs.
- `.ufo/waves/round-64/R64SnapshotManifest.md` — this report.

## Behavior and retained evidence
- Manifest records base commit `666ea84b6be2eec2b0359f556ba2429fc9044c36` and hashes/size for the three round-64 report inputs, all three files in `corpus/fixtures/firmware-r63/`, the five named round-63 live-run inputs, and both named verifier scripts.
- The three `reports/round-64/` inputs are absent from the base commit, so their current round-preparation files were hashed. The ten `corpus/` inputs were hashed from the frozen base commit objects, avoiding concurrent working-tree changes.
- The two verifier files' working-tree sizes were 10,147 and 10,398 bytes versus base sizes 10,058 and 10,172 bytes respectively when checked; the manifest therefore captures their base versions. No run-record or receipt values were displayed; these inputs were treated as opaque bytes for hashing.
- No tools were installed. No tests, builds, or formatters were run.

## Risks / blockers
- The live verifier scripts were already modified relative to the frozen base when inspected. Their base-commit digests are retained intentionally; landing-time comparison must account for the authorized script edits.
- No other blocker observed.

Report: .ufo/waves/round-64/R64SnapshotManifest.md
