# R73Source060 — round-73 source audit, row S060 (Frida)

Seat: R73Source060 (reviewer, godspeed). Assigned row only; no other source admission.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Read-only except this report and scratch.

## Registry row audited

`corpus/SOURCES.md:74` (11 cells, parsed):

- id: `S060`
- source: `Frida — https://github.com/frida/frida`
- class: `tool`; tier: `A`
- scope: "The repository's declared dynamic instrumentation purpose and published release-binary role; no target activity or host installation"
- located quote + locator: `README.md introduction, commit e598d053f4154fa78a26bb60d4f6cbc407ea387c, accessed 2026-10-27; "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers."`
- tier note: "Frida is described as a runtime instrumentation surface; any use remains limited to an explicitly authorized local artifact/lifecycle, not a live target"
- status: `mined`; verified 2026-10-27; disposition `on-release`; used-by `corpus/knowledge/round-72-tool-landscape.md`

## Lesson and entry wording (round 72)

- Lesson Gate (`corpus/lessons/round-72.md:19`): `| S060 | https://github.com/frida/frida | 2026-10-27 | README introduction: "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers." | ADMIT, tier A for declared dynamic-instrumentation purpose only; not a run or permission to use a target. |` — quote identical to registry row.
- Entry wording (`corpus/knowledge/round-72-tool-landscape.md:28`, "Need process instrumentation or debugging" row): "Frida S060; x64dbg S063; RAD Debugger S070 | Frida describes dynamic instrumentation. …" — bounded to the README's own claim; no execution/install claim. S060 appears nowhere else in the entry (single used-by site).

## Primary re-open (this seat, 2026-10-30)

- URL: `https://github.com/frida/frida` — pinned README fetched at `https://raw.githubusercontent.com/frida/frida/e598d053f4154fa78a26bb60d4f6cbc407ea387c/README.md`
- Network: success, HTTP 200, 1,931 bytes; no network or source failures.
- Pin existence cross-check: GitHub API `repos/frida/frida/commits/e598d053…` → HTTP 200, commit committer date 2026-03-23T14:45:43Z (observation: pin is a real commit).
- Fetched bytes sha256: `8478d48f61310d01be76702014de292852260f32cda695a64f8f86ab110b655b`.

## Verbatim quote comparison (markup normalization only)

- Registry/lesson quote (9 words, ≤25 ✓): "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers."
- Raw-byte substring of pinned README: **absent** — the README source wraps the line as `…and security\nresearchers.`.
- After whitespace/line-wrap normalization only: **PRESENT** (observation). This is markup normalization, not wording change; quote is verbatim.

## Located quote returned by this seat

> "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers."

- 9 words (≤25). Access date: **2026-10-30**. URL: `https://github.com/frida/frida` (README.md at commit `e598d053f4154fa78a26bb60d4f6cbc407ea387c`).

## Scope / tier / used-by / rejection-flip comparison

| dimension | row/lesson claim | re-opened source | match |
|---|---|---|---|
| scope | declared dynamic-instrumentation purpose + published release-binary role | README: "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers."; "Two ways to install / 1. Install from prebuilt binaries — This is the recommended way to get started."; "You may also download pre-built binaries … from Frida's releases page on GitHub." | ✓ verbatim-supported, no target activity/host install claimed |
| tier | A (primary repo README at pinned commit) | pinned commit verified real (API 200); README intro at that commit | ✓ |
| used-by | `round-72-tool-landscape.md` "Frida describes dynamic instrumentation" | README first sentence states exactly that | ✓ bounded, no overreach |
| rejection flip | none recorded (S060 is an ADMIT, not a rejection); no flip condition stated in row or lesson Gate | n/a | consistent — nothing to flip |

Freshness observation: current `main` README is byte-identical to the pinned README (diff empty, 2026-10-30) — no drift since the 2026-10-27 access; the row remains current.

## Disposition verdict

**AGREE** with the round-72 disposition: ADMIT, tier A, for the declared dynamic-instrumentation purpose only; not a run or permission to use a target. Quote verbatim (post line-wrap normalization), scope/tier/used-by all supported by the pinned primary; registry row, lesson Gate row, and entry wording are mutually consistent. No defect, no superseding row proposed for S060.

## S071/S082 note (context only, out of this seat's scope)

`corpus/lessons/round-72-verifier-spotcheck.md` routes two quote defects: S071 registry paraphrase and S082 misattributed quote. Per assignment, another seat owns those; this seat admits no other source and edits no old row. Observation: the candidate entry already carries an erratum naming superseding rows S427 (S071 verbatim "each one read and security-graded") and S428 (S082/S083 attribution fix) — a NEW-superseding-row structure consistent with the round-73 instruction, recorded as of round 72/23 wording. No action taken by this seat.

## Observation / inference / unknown

- Observation: quote present at pin after whitespace-only normalization; pin commit real; HEAD README identical to pin; lesson/row/entry texts mutually consistent.
- Inference: none needed — all row claims check directly against fetched bytes.
- Unknown: whether GitHub's rendered README view differs from raw markdown (irrelevant — the row cites README.md text, which was checked raw); behavioral/tool-readiness of Frida on any host is explicitly out of row scope and untested here.

## Bounds and tooling

- Reads: SOURCES.md:74; lessons/round-72.md:19; lessons/round-72-verifier-spotcheck.md; knowledge/round-72-tool-landscape.md; reports/round-73/{claims.md,candidate-pin.json,measure.py}; reports/round-72/ (listing). No writes to corpus/shared/sibling/fleet paths; no git/jj mutations; no installs (curl/python3 already present — no tool added this run).
- Scratch `/fast/scratch/hyaku/revenger-r73/R73Source060/` held fetched bytes + commit metadata; receipt hashes are quoted above and the scratch tree was removed after copying receipts into this report.
