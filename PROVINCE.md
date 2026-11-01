# revenger province

Owns: reverse engineering of shipped artifacts — native binaries, managed
assemblies, Electron/JavaScript packages, Android APKs, archives, firmware,
browser/Electron runtime evidence — using the REA skill and its toolset,
with an evidence-ledger discipline: every conclusion separates observation,
inference, and unknown, and cites Evidence IDs.

Bounty and coordinated-disclosure triage enters only through
`corpus/training/bounty-triage/MODULE.md`: a written scope record gates access
to the artifact, triage stays static and artifact-first, and live-target
activity, exploitation, third-party testing and disclosure outside the program
channel remain outside this province.

Sources (read-only):
- REA skill: ~/.agents/skills/reverse-engineer-anything/ (SKILL.md +
  references/; instructions only — server registration and engines are the
  lane's readiness domain) [absent on this host, 2026-10-31 — the packaged
  `rea` CLI below is the available REA surface here]
- REA package: `rea` CLI when installed, else `npx -y rea-agents@6.5.0`
  within authorized scope (setup never installs unrelated software);
  installed on this host at 6.8.0 (`rea --version` exit 0, 2026-10-31)
- Host engines as they become available (caller-supplied per REA: Ghidra,
  IDA, JADX, Binwalk/Unblob, pwntools) — census in corpus/knowledge/seed.md
  [absent on this host, 2026-10-31: ghidra / analyzeHeadless — PATH probe]
  [absent on this host, 2026-10-31: ida / ida64 — PATH probe]
  [absent on this host, 2026-10-31: jadx — PATH probe]
  [absent on this host, 2026-10-31: binwalk / unblob — PATH probe]
  [absent on this host, 2026-10-31: pwntools — `python -c "import pwn"` fails]
- Demand context: ~/Projects/gamez/research/ (incl. decomp/recomp interest)
  [absent on this host, 2026-10-31 — no ~/Projects tree exists]

Refuses: live-target execution beyond the declared target and lifecycle
(REA runtime discipline); DRM circumvention or piracy facilitation;
publishing reversed code; asset rights claims (art-east-asian-design);
harness/evidence auditing (harness-integrity, gate-evidence, rlm-dispatch);
game mechanics verification (game-dev-2d); narrative canon (lore).

Writes only this lane repository — `fleet/shokunin-binary-forensics` in the
campaign workspace, branch `main` (the historical name `revenger-shokunin/`
identifies imported evidence and prior-host paths) — under the current
interactive dispatch. Reports, continuation evidence and L0 requests stay in its own
`.ufo/`; the fleet integrator alone copies them to shared ledgers/report paths.
Domain source checkouts, shared fleet state and sibling repositories remain
read-only. No push, global routing changes or substrate/package remediation.
Historical `.shokunin/revenger/**` paths identify imported evidence, not the
current write scope. The r55–r57 replay repair checks this domain's saved
PE evidence ledger; it does not take ownership of generic harness gates.
