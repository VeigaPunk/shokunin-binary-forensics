# shokunin-binary-forensics

Reverse engineering of shipped artifacts, under an evidence-ledger
discipline. Every conclusion separates observation, inference, and
unknown, and cites an Evidence ID.

The lane id is `revenger`. Rank is shonen. There is no root `SKILL.md`;
`LOG.md` records that absence as contract debt, not as a file this page
can point you at. The working surface is `PROVINCE.md`, the verifiers
in `corpus/`, and `reports/`.

## The job

`PROVINCE.md` owns native binaries, managed assemblies,
Electron and JavaScript packages, Android APKs, archives, firmware, and
browser or Electron runtime evidence, using the REA skill and its
toolset. The REA skill path and the `npx -y rea-agents@6.4.0` fallback
are named there, along with the host-engine census.

The lane refuses live-target execution beyond the declared target and
lifecycle, DRM circumvention, publishing reversed code, asset-rights
claims, harness auditing as a separate discipline, game-mechanics
verification, and narrative canon. Writes stay in this repository.
Domain checkouts, shared fleet state, and sibling repositories are
read-only. Historical `.shokunin/revenger/**` paths identify imported
evidence. They are not the current write scope.

Kaidoku ([shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering))
is the sibling that owns the REA-on-this-host province, including the
Ghidra provider and the client pin table. This lane owns the
evidence-ledger replay of shipped artifacts. The r55–r57 repair checks
this domain's saved PE evidence ledger. It does not take ownership of
generic harness gates.

## Replay the saved named-icon ledger

From this repository's root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

That checks the authored r55–r57 PE32+ fixtures against their saved
normalized results, exact byte deltas, pinned Evidence IDs, and the
receipt command and hash. `ROOT` locates the current corpus. `HIST`
pins the original producer path as recorded identity only. Moving this
checkout must not change `HIST`, rewrite saved records, or require the
historical directory to exist.

The output establishes bounded saved-record consistency. It does not
establish authenticated producer origin, a new REA analysis, PE
execution, or general parser correctness. The separate multi-image and
language-ledger relocation failures remain outside this repair. Round
evidence and counting commands live in `reports/round-1/`.

The isolated relocation and tamper battery:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd/path contexts and six
individually forged saved-record copies, and checks that original inputs
stay unchanged. Exit 0 means this bounded battery passed. It does not
admit a training round.

Other verifiers in `corpus/` cover saved evidence, PE resources, icon
states, JS graph delta, semantic trace, shape evidence, and EVM
evidence. Each script's docstring is its contract. A green run of one
of them does not license a claim the docstring refuses.

The interactive continuation recorded a validated, undispatched 32-scope
audit plan and missing required global route bindings. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
the interactive-continuation section of `SCORECARD.md` before advancing
a round. Gate-registry and corpus-bar files (`corpus/QUALITY.md`,
`corpus/README.md`) remain named debt. These replay commands do not
close it.

## Read this first

1. [`PROVINCE.md`](PROVINCE.md) — owns, refuses, write scope.
2. [`corpus/verify_named_multi_icon_states.py`](corpus/verify_named_multi_icon_states.py) — the saved-ledger replay.
3. [`reports/round-1/`](reports/round-1) — counting commands and `replay_scenarios.py`.
4. [`SHONEN.md`](SHONEN.md) — the promotion checklist. Still present.

## On disk

| Path | Role |
|---|---|
| `PROVINCE.md` | Boundary. |
| `corpus/verify_*.py` | Saved-ledger verifiers. |
| `corpus/fixtures/` | Authored fixtures, including the PE r59 builder. |
| `corpus/live/` | Preserved round runs. |
| `reports/` | Verifier reports and the replay battery. |
| `SCORECARD.md`, `LOG.md` | Axis verdicts and the audit trail. |
| `SHONEN.md` | Promotion checklist. |

## Fleet

Protocol and roster: [shokunin](https://github.com/VeigaPunk/shokunin).
Roster id `revenger`, rank **shonen**.
