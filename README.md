# shokunin-binary-forensics — revenger

Shipped-artifact reverse engineering under an evidence ledger: observation, inference, and unknown stay separate, and conclusions cite Evidence IDs (`PROVINCE.md`).

**Rank:** `SHONEN.md` is a promotion checklist. Its boxes are `[ ]` or `[~]` (author-side; no outside verifier). That is not a promotion.

**Owns:** native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware, and browser/Electron runtime evidence, using the REA skill, written only in this repository (`PROVINCE.md`).

**Refuses:** live-target execution beyond a declared target and lifecycle; DRM circumvention; publishing reversed code; asset-rights claims; harness auditing; game-mechanics verification; narrative canon (`PROVINCE.md`).

## Start here

`SHONEN.md` cites `README.md:24-41`. Those lines are unchanged below. The replay checks saved records. It does not execute a PE or admit a round.

## Neighbors

Game-mechanics verification stays with game-dev-2d. Narrative canon stays with lore. Harness auditing is refused (`PROVINCE.md`).

## Map

Root files: `PROVINCE.md`, `SHONEN.md`, `LOG.md`, `SCORECARD.md`, `corpus/`, `reports/`, `.ufo/`. There is no `SKILL.md` (`SHONEN.md`).

`corpus/` holds `fixtures/`, `knowledge/`, `lessons/`, `live/`, and the `verify_*.py` checkers. Fleet protocol: https://github.com/VeigaPunk/shokunin
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
