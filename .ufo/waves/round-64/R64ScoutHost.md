# R64ScoutHost

Axes: command success, version-family agreement, provenance fidelity.

**Observed host Bash results (all exit 0):** `binwalk --version` → `binwalk 3.1.0`; `unblob --version` → `26.6.4`; `node --version` → `v24.21.0`; `npx --version` → `11.19.0`.

**Holds, high confidence:** Binwalk and Unblob exactly match the pinned REA 6.5.0 guide's verified versions, within its required 3.1.x / 26.6.x families. No firmware version-family STALE flag. Node/npx are available; this comparison establishes no Node/npx compatibility pin.

**Provenance:** read `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63ScoutFirmware.md`; the requested round-64 guide snapshot was absent. Opened the official pinned guide directly instead: https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md (2026-10-24), especially lines 3-7 and 18-30. The historical round-63 snapshot was explicitly `main`, not pinned 6.5.0.

**Environment finding:** Eval's alternate PATH selected Node `v26.12.0` / npx `11.20.0` (both exit 0), whereas Bash selected the fnm versions above; Binwalk/Unblob were identical. Do not quote a context-free Node/npx version.

**Boundaries:** version checks alone do not establish configured REA execution, extraction, sandbox, dependency, or build-authenticity readiness. No REA operation or fixture execution; no source edits, Git/JJ commands, installs/updates, or scratch artifacts. LSP not applicable to this command/document-only investigation.

Full command exits, source paths, and remaining unknowns: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-host.md`.

Report: .ufo/waves/round-64/R64ScoutHost.md
