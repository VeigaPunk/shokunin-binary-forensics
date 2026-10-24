# R64ScoutHost — version-only host readiness

Date: 2026-10-24. Seat: `revenger-r64.R64ScoutHost`.

Axes: command success; firmware version-family agreement; source/environment provenance.

## Observed host commands

Concurrent Bash probes, cwd `/home/vgpnk/Projects/shokunin/revenger-shokunin`; each exit was explicitly captured with `&& printf 'exit=0\n'`. No command failed; stderr contained no diagnostics.

| Command | Version/banner | Exit | Flag |
|---|---|---:|---|
| `binwalk --version` | `binwalk 3.1.0` | 0 | holds: matches required 3.1.x and guide-verified 3.1.0 |
| `unblob --version` | `26.6.4` | 0 | holds: matches required 26.6.x and guide-verified 26.6.4 |
| `node --version` | `v24.21.0` | 0 | available; no Node version pin established by this firmware-guide comparison |
| `npx --version` | `11.19.0` | 0 | available; no npx version pin established by this firmware-guide comparison |

No STALE firmware version-family flag was observed. These are version-banner observations, not an end-to-end readiness claim.

## Source evidence and comparison

- Frozen scope: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:18-31` limits C07 to one authored fixture's byte/record correspondence, excluding extraction/execution and general firmware/provider claims.
- Read `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63ScoutFirmware.md:3-19,130-138`. It records historical Binwalk 3.1.0 and warns that its `main` guide snapshot is newer than the package that produced the 6.5.0 record. That snapshot is not treated as pinned evidence.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` was absent at lookup; no wait or dependency on another seat.
- Opened the official pinned guide directly: https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md (accessed 2026-10-24), lines 3-7: “REA accepts **Binwalk 3.1.x** for region inspection and **Unblob 26.6.x** for explicit extraction.” Its next sentence names parser-verified versions 3.1.0 and 26.6.4. Both observed host banners match exactly.
- Pinned guide lines 25-30 distinguish inspection/extraction prerequisites, require caller-supplied absolute tool paths and `prlimit`, and do not promise REA installation of providers. Its lines 83-87 warn that version equality does not attest build source revision. The local historical snapshot `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/source-snapshots/rea-firmware-guide.md:1-33` agrees on version families, but has additional later wording.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py:99-104` measures stored freshness-row survival, not current-host truth; the baseline `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log:11` reporting `FRESH_ROWS=18/18` is not substituted for these host observations.

## Environment distinction

An additional concurrent Eval-subprocess probe returned the same Binwalk/Unblob versions (all exits 0), but Node `v26.12.0` and npx `11.20.0` (both exits 0). Command-resolution observations explain the differing selections: Bash selected Node/npx under `/run/user/1000/fnm_multishells/5324_1792804850373/bin/`; Eval selected `/home/vgpnk/.local/share/mise/installs/node/latest/bin/`. Both selected `/usr/bin/binwalk` and `/home/vgpnk/.local/bin/unblob`. The table deliberately reports the requested host Bash environment; a single context-free Node/npx version would be misleading.

## Findings and remaining unknowns

- **Observed, high confidence:** all four requested commands exit 0 in host Bash; Binwalk/Unblob satisfy the pinned guide's stated version requirements. No provider-version staleness detected.
- **Inference, bounded:** the version component of the firmware provider prerequisites holds. This does not establish successful REA invocation or extraction readiness, and Unblob extraction is outside C1's claimed scope.
- **Not assessed by this version-only brief:** REA environment-variable configuration, `ps`/`prlimit`, extractor dependencies, source revision/authenticity, sandbox startup, and real-provider operation. Node/npx selection is environment-sensitive; compatibility beyond the observed version commands is not claimed.
- No LSP trace was applicable: no exported source contract or symbol was investigated. No source edits, Git/JJ commands, REA invocation, fixture scan/execution, installations, updates, or scratch artifacts.

Report: .ufo/waves/round-64/R64ScoutHost.md
