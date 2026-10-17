# shokunin-binary-forensics

Reverse engineering of shipped artifacts, under an evidence ledger.

This is the revenger lane. Every conclusion separates observation,
inference, and unknown, and cites an Evidence ID. A verifier in this
repository checks saved records against the bytes those records describe.
It does not become a new analysis, a parser proof, or permission to run
the binary.

Rank: **shonen**. `SHONEN.md` is still here. Registered in the fleet
`MANIFEST.json` as revenger-shokunin since 2026-10-11. There is no
`SKILL.md` in this checkout. The ledger and the verifiers are the craft
record.

## Province

**Owns.** Shipped artifacts — native binaries, managed assemblies,
Electron and JavaScript packages, Android APKs, archives, firmware,
browser and Electron runtime evidence — read with the REA toolset, with
the evidence-ledger discipline above.

**Hands off.** Live-target execution beyond the declared target and
lifecycle. DRM circumvention and piracy. Publishing reversed code.
Asset-rights claims. Harness auditing as a product. Game-mechanics
verification (game-dev-2d). Narrative canon (lore).

Writes stay inside this repository. Historical `.shokunin/revenger/**`
paths identify imported evidence. They are not the current write scope.
The r55–r57 replay checks this domain's saved PE evidence ledger. It does
not take ownership of generic harness gates.

## Start here

1. `PROVINCE.md` — sources, refusals, write scope.
2. `corpus/knowledge/` — including `seed.md`, the engine census.
3. `corpus/verify_*.py` — one verifier per saved-ledger family.
4. `reports/round-1/` — the fleet-round measurements and the relocation
   battery.
5. `SCORECARD.md` — coverage and calibration proxies for the fleet
   round-1 move. The card says they are bounded proxies, not mastery
   scores. Read the rubric boundaries before quoting a number.

## Saved named-icon ledger replay

From this lane's repository root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

This checks the authored r55–r57 PE32+ fixtures against their saved
normalized results, exact byte deltas, pinned Evidence IDs, and receipt
command/hash. `ROOT` locates the current corpus; `HIST` pins the original
producer path as recorded identity only. Moving this checkout must not
change `HIST`, rewrite saved records, or require the historical directory
to exist.

The output establishes bounded saved-record consistency, not authenticated
producer origin, a new REA analysis, PE execution, or general parser
correctness. The separate multi-image and language-ledger relocation
failures remain outside this repair. Round evidence and counting commands
live in `reports/round-1/`.

Run the isolated relocation/tamper acceptance battery with:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd/path contexts and six
individually forged saved-record copies, checking that original inputs
remain unchanged. Exit 0 means this bounded battery passed; it does not
admit a training round. The current interactive continuation has a
validated, undispatched 32-scope audit plan but missing required global
route bindings. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
`SCORECARD.md`'s interactive-continuation section before advancing a
round. Permanent gate-registry and corpus-bar files remain named debt,
not implied by this command's existence. No native judgment or completion
receipt is claimed by these replay commands.

Other family verifiers sit beside the named-icon one:
`verify_icon_states.py`, `verify_multi_icon_states.py`,
`verify_icon_languages.py`, `verify_pe_resources.py`,
`verify_saved_evidence.py`, `verify_shape_evidence.py`,
`verify_js_graph_delta.py`, `verify_semantic_trace.py`,
`verify_evm_evidence.py`. Each file's docstring names the family it
checks. A green run of one does not cover the others.

## The tree

| Path | What it is |
|---|---|
| `corpus/verify_*.py` | Saved-ledger verifiers |
| `corpus/fixtures/` | Authored fixtures, including the checksum and duplicate controls |
| `corpus/knowledge/` | Seed notes and ledger commentary |
| `corpus/lessons/` | Per-round lessons |
| `corpus/live/` | Preserved run material |
| `reports/` | Verifier and adjudicator reports |

## Fleet

Minted under [shokunin](https://github.com/VeigaPunk/shokunin).
The neighboring REA lane, with a different province, is
[shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering)
(kaidoku). Overlap is reported to the integrator.
