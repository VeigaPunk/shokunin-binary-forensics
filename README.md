# shokunin-binary-forensics

Reverse engineering of shipped artifacts, under an evidence-ledger
discipline.

Lane id: **revenger-shokunin**. Rank: **shonen**. [`SHONEN.md`](SHONEN.md)
records that root `SKILL.md` is absent, and that the replay below is an
author-side fixture scope, not a promotion. There is no root `SKILL.md`
in this checkout. Decision tables live in `corpus/knowledge/` and
`corpus/lessons/`.

Fleet: [shokunin](https://github.com/VeigaPunk/shokunin). The live REA
surface map is maintained by
[shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering)
(kaidoku). This lane keeps the evidence ledger: observation, inference,
and unknown, each citing an Evidence ID.

## The question

> Which bytes support this conclusion, which Evidence ID points at them,
> and which saved record still matches those bytes?

Owned families, from `PROVINCE.md`: native binaries, managed assemblies,
Electron and JavaScript packages, Android APKs, archives, firmware, and
browser or Electron runtime evidence. Every conclusion separates
observation, inference, and unknown.

## Boundary

Live-target execution stays inside the declared target and lifecycle.
DRM circumvention, publishing reversed code, asset-rights claims, harness
auditing, game-mechanics verification, and narrative canon are outside
this province. Writes stay in this repository. Sibling repositories and
domain source checkouts are read-only. Historical `.shokunin/revenger/**`
paths identify imported evidence. They are not the current write scope.

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

Run the isolated relocation and tamper acceptance battery with:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd/path contexts and six
individually forged saved-record copies, checking that original inputs
remain unchanged. Exit 0 means this bounded battery passed. It does not
admit a training round. Before treating a replay as a round, read
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
`SCORECARD.md` under "Interactive continuation — fleet round-1 remains
unadmitted".

Sibling verifiers in `corpus/` cover narrower saved ledgers
(`verify_saved_evidence.py`, `verify_pe_resources.py`,
`verify_icon_states.py`, `verify_icon_languages.py`,
`verify_evm_evidence.py`, `verify_js_graph_delta.py`,
`verify_semantic_trace.py`, `verify_shape_evidence.py`,
`verify_multi_icon_states.py`). Each one is a bounded replay of its own
fixtures. None of them is a general parser proof.

## Map

| Path | What it is |
|---|---|
| [`PROVINCE.md`](PROVINCE.md) | owned artifact families and write scope |
| [`corpus/knowledge/`](corpus/knowledge/) | sourced ledger notes |
| [`corpus/fixtures/`](corpus/fixtures/) | authored fixtures, including the checksum and duplicate sets |
| [`reports/`](reports/) | verifier measurements |
| [`SHONEN.md`](SHONEN.md), [`SCORECARD.md`](SCORECARD.md), [`LOG.md`](LOG.md) | probation, verdicts, audit trail |
