# shokunin-binary-forensics — revenger-shokunin

**Reverse engineering of shipped artifacts under an evidence-ledger
discipline.** Every conclusion separates observation, inference, and
unknown, and cites Evidence IDs. Byte-oracle fixtures. Forged-claim
rejection controls.

This is a [shokunin](https://github.com/VeigaPunk/shokunin) lane. Rank:
shonen. Canonical lane name: `revenger-shokunin`. REA tooling is the
instrument; the ledger is the craft.

Revenger owns shipped-artifact RE with evidence IDs. Kaidoku
([shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering))
also declares shipped-artifact RE on this host. Shared scope is
integrator-owned — this lane does not absorb it. Game-mechanics
verification is
[game-dev-2d](https://github.com/VeigaPunk/shokunin-godot-2d). Narrative
canon is [lore](https://github.com/VeigaPunk/shokunin-world-bible).

## Province

**Owns:** reverse engineering of shipped artifacts — native binaries,
managed assemblies, Electron / JavaScript packages, Android APKs,
archives, firmware, browser / Electron runtime evidence — using the REA
skill and its toolset, with Evidence IDs on every conclusion. The
r55–r57 replay repair checks this domain's saved PE evidence ledger.

**Refuses:** live-target execution beyond the declared target and
lifecycle; DRM circumvention or piracy facilitation; publishing
reversed code; asset rights claims; harness / evidence auditing; game
mechanics verification; narrative canon.

Writes only this repository. Domain source checkouts, shared fleet
state, and sibling repositories remain read-only. Historical
`.shokunin/revenger/**` paths identify imported evidence, not the
current write scope. Full boundary: [`PROVINCE.md`](PROVINCE.md).

## Start here

1. [`PROVINCE.md`](PROVINCE.md) — owned artifact classes and the live-target fence.
2. [`corpus/`](corpus/) — saved-ledger verifiers and fixtures.
3. [`reports/round-1/`](reports/round-1/) — relocation / tamper battery.
4. [`SHONEN.md`](SHONEN.md) — promotion checklist.

This lane is still in shonen seed form: distilled `SKILL.md` lives in
the corpus until promotion.

## Saved named-icon ledger replay

From this lane's repository root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

This checks the authored r55–r57 PE32+ fixtures against their saved
normalized results, exact byte deltas, pinned Evidence IDs, and receipt
command / hash. `ROOT` locates the current corpus; `HIST` pins the
original producer path as recorded identity only. Moving this checkout
must not change `HIST`, rewrite saved records, or require the
historical directory to exist.

The output establishes bounded saved-record consistency, not
authenticated producer origin, a new REA analysis, PE execution, or
general parser correctness. The separate multi-image and
language-ledger relocation failures remain outside this repair. Round
evidence and counting commands live in `reports/round-1/`.

Run the isolated relocation / tamper acceptance battery with:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd / path contexts and six
individually forged saved-record copies, checking that original inputs
remain unchanged. Exit 0 means this bounded battery passed; it does not
admit a training round. The current interactive continuation has a
validated, undispatched 32-scope audit plan but missing required global
route bindings. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
`SCORECARD.md`'s interactive-continuation section before advancing a
round. Permanent gate-registry and corpus-bar files remain named debt,
not implied by this command's existence. No native judgment or
completion receipt is claimed by these replay commands.

Sibling verifiers in `corpus/` (`verify_saved_evidence.py`,
`verify_pe_resources.py`, `verify_icon_states.py`,
`verify_js_graph_delta.py`, `verify_evm_evidence.py`, …) are the same
kind of bound: each names what it proves and what it does not.

## What's in the repo

```
shokunin-binary-forensics/
├── PROVINCE.md       domain boundary + write scope
├── SHONEN.md         promotion checklist
├── LOG.md            append-only audit trail
├── SCORECARD.md      axis verdicts
├── reports/          including round-1 replay_scenarios.py
└── corpus/           ledger verifiers, fixtures, knowledge/, lessons/
```

Protocol: append-only corpus; every claim separates observation /
inference / unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme) for how a lane
learns.
