# revenger-shokunin — evidence ledger

Repo: `shokunin-binary-forensics`.

**Binary forensics under evidence-ledger discipline.** Reverse
engineering of shipped artifacts — native binaries, managed assemblies,
Electron/JS packages, APKs, archives, firmware — where every conclusion
separates observation, inference, and unknown, and cites Evidence IDs.

A **shokunin lane**: an expert agent for one domain, minted and trained
under the [shokunin skill](https://github.com/VeigaPunk/shokunin).
Rank: **shonen**. Promotion is a named non-author review of
[`SHONEN.md`](SHONEN.md), never self-attestation.

This lane answers: *does this saved record still match the bytes it
claims, under the Evidence IDs it pinned — and do forged copies fail
closed?*

Live REA analysis of a new target is
[kaidoku](https://github.com/VeigaPunk/shokunin-reverse-engineering).
This repo is the **ledger**: fixtures, verifiers, and the refusal to
treat a green replay as authenticated producer origin.

## Domain

From [`PROVINCE.md`](PROVINCE.md): shipped-artifact RE with an
evidence-ledger. Writes only this repository. Domain source checkouts
and sibling repos stay read-only. No live-target execution beyond the
declared target and lifecycle; no DRM circumvention; no publishing
reversed code.

The r55–r57 replay repair checks this domain's saved PE evidence
ledger. It does not take ownership of generic harness gates.

## What's here

| Path | Role |
|---|---|
| [`PROVINCE.md`](PROVINCE.md) | owned surfaces and write fence |
| [`corpus/fixtures/`](corpus/fixtures/) | authored PE/icon/language/checksum/duplicate fixtures |
| [`corpus/verify_*.py`](corpus/) | saved-record verifiers |
| [`reports/`](reports/) | verifier and adjudicator reports |
| [`SCORECARD.md`](SCORECARD.md) · [`LOG.md`](LOG.md) · [`SHONEN.md`](SHONEN.md) | axes, trail, promotion |

(`SKILL.md` is still in shonen seed form — the distilled tables live in
`corpus/` until promotion.)

## Saved named-icon ledger replay

From this repository root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

This checks the authored r55–r57 PE32+ fixtures against their saved
normalized results, exact byte deltas, pinned Evidence IDs, and receipt
command/hash. `ROOT` locates the current corpus; `HIST` pins the original
producer path as recorded identity only. Moving this checkout must not
change `HIST`, rewrite saved records, or require the historical directory
to exist.

The output establishes bounded saved-record consistency, **not**
authenticated producer origin, a new REA analysis, PE execution, or
general parser correctness. The separate multi-image and language-ledger
relocation failures remain outside this repair. Round evidence and
counting commands live in `reports/round-1/`.

Isolated relocation/tamper acceptance battery:

```sh
python3 -B reports/round-1/replay_scenarios.py
```

It exercises the real verifier in three cwd/path contexts and six
individually forged saved-record copies, checking that original inputs
remain unchanged. Exit 0 means this bounded battery passed; it does not
admit a training round.

The current interactive continuation has a validated, undispatched
32-scope audit plan but missing required global route bindings. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
`SCORECARD.md`'s interactive-continuation section before advancing a
round. Permanent gate-registry and corpus-bar files remain named debt,
not implied by this command's existence. No native judgment or
completion receipt is claimed by these replay commands.

## How a lane learns

Append-only corpus; every claim separates observation / inference /
unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme).
