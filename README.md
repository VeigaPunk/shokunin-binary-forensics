# shokunin-binary-forensics

A **shokunin lane** — an expert agent for one domain, minted and trained
under the [shokunin skill](https://github.com/VeigaPunk/shokunin).

**Domain:** Reverse engineering of shipped artifacts under the evidence-ledger discipline — byte-oracle fixtures, Evidence IDs, forged-claim rejection controls.

**Wiki:** [Devin wiki](https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/shokunin-binary-forensics?branch=main)

## What's here

- `SKILL.md` — the distilled expertise: decision tables, error patterns,
  checklists (absent on lanes still in shonen seed form — see `corpus/`)
- `PROVINCE.md` — the owned domain boundary and refusals
- `corpus/` — the craft record: `knowledge/` (sourced, verifiable),
  `lessons/` (per-round), `QUALITY.md` (the admission bar)
- `LOG.md` — the round-by-round audit trail · `SCORECARD.md` — axis
  verdicts · `SHONEN.md` — promotion checklist (deleted on promotion)
- `reports/` — verifier and adjudicator reports

Protocol: append-only corpus; every claim separates observation /
inference / unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme) for how a lane
learns.

## Saved named-icon ledger replay

From this lane's repository root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

This checks the authored r55–r57 PE32+ fixtures against their saved normalized
results, exact byte deltas, pinned Evidence IDs, and receipt command/hash.
`ROOT` locates the current corpus; `HIST` pins the original producer path as
recorded identity only. Moving this checkout must not change `HIST`, rewrite
saved records, or require the historical directory to exist.

The output establishes bounded saved-record consistency, not authenticated
producer origin, a new REA analysis, PE execution, or general parser correctness.
The separate multi-image and language-ledger relocation failures remain outside
this repair. Round evidence and counting commands live in `reports/round-1/`.

Run the isolated relocation/tamper acceptance battery with:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd/path contexts and six individually
forged saved-record copies, checking that original inputs remain unchanged.
Exit 0 means this bounded battery passed; it does not admit a training round.
The current interactive continuation has a validated, undispatched 32-scope
audit plan but missing required global route bindings. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
`SCORECARD.md`'s interactive-continuation section before advancing a round.
Permanent gate-registry and corpus-bar files remain named debt, not implied
by this command's existence. No native judgment or completion receipt is
claimed by these replay commands.
