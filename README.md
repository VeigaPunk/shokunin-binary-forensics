# shokunin-binary-forensics — revenger-shokunin

**Binary forensics under the evidence-ledger discipline.**

Revenger reverse-engineers shipped artifacts — native binaries,
managed assemblies, Electron/JavaScript packages, Android APKs,
archives, firmware, browser/Electron runtime evidence — using REA,
with every conclusion separated into observation, inference, and
unknown, and cited by Evidence ID.

This is a **shokunin lane** of the [shokunin fleet](https://github.com/VeigaPunk/shokunin).
Canonical name: `revenger-shokunin`. Rank: **shonen**.

## The craft

- Byte-oracle fixtures. A saved record is checked against pinned
  bytes, exact deltas, and a receipt command/hash.
- Forged-claim rejection: a relocated or tampered saved-record copy
  must fail closed.
- Evidence IDs are the currency. A conclusion without one is not
  held.
- The r55–r57 replay repair checks *this domain's* saved PE evidence
  ledger. It does not take ownership of generic harness gates, and
  it does not authenticate producer origin.

Kaidoku ([shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering))
owns the REA-on-Linux surface map. Shared shipped-artifact RE scope
is integrator-arbitrated; this lane does not absorb it.

## Province

Owns: reverse engineering of shipped artifacts with evidence-ledger
discipline.

**Refuses:** live-target execution beyond the declared target and
lifecycle; DRM circumvention or piracy facilitation; publishing
reversed code; asset rights claims; harness/evidence auditing;
game mechanics verification (game-dev-2d); narrative canon (lore).

Writes only this repository under the current interactive dispatch.
Historical `.shokunin/revenger/**` paths identify imported evidence,
not the current write scope.

See [`PROVINCE.md`](PROVINCE.md).

## What's in this repository

```
shokunin-binary-forensics/
├── PROVINCE.md
├── SHONEN.md
├── LOG.md
├── SCORECARD.md          includes the interactive-continuation section
├── reports/
│   └── round-1/          replay_scenarios.py + measurements
└── corpus/
    ├── verify_named_multi_icon_states.py
    ├── knowledge/
    └── fixtures/         authored PE32+ named-icon fixtures (r55–r57)
```

`SKILL.md` is not at repo root (shonen seed form). Start from
`PROVINCE.md` and the replay commands below.

## Saved named-icon ledger replay

From this lane's repository root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

This checks the authored r55–r57 PE32+ fixtures against their saved
normalized results, exact byte deltas, pinned Evidence IDs, and
receipt command/hash. `ROOT` locates the current corpus; `HIST` pins
the original producer path as recorded identity only. Moving this
checkout must not change `HIST`, rewrite saved records, or require
the historical directory to exist.

The output establishes bounded saved-record consistency, not
authenticated producer origin, a new REA analysis, PE execution, or
general parser correctness. The separate multi-image and
language-ledger relocation failures remain outside this repair.
Round evidence and counting commands live in `reports/round-1/`.

Run the isolated relocation/tamper acceptance battery with:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd/path contexts and six
individually forged saved-record copies, checking that original
inputs remain unchanged. Exit 0 means this bounded battery passed;
it does not admit a training round. The current interactive
continuation has a validated, undispatched 32-scope audit plan but
missing required global route bindings. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json`
and `SCORECARD.md`'s interactive-continuation section before
advancing a round. Permanent gate-registry and corpus-bar files
remain named debt, not implied by this command's existence. No
native judgment or completion receipt is claimed by these replay
commands.

This README does not include exploit procedures, payloads, or
unauthorized-access steps.

## How a round works

One axis-move. Lane identity:
`revenger-shokunin <revenger@shokunin.local>`.

## Fleet

[VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) ·
[kaidoku / shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering) ·
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin)
