# shokunin-binary-forensics

**Shipped-artifact reverse engineering under an evidence ledger —
observation, inference, and unknown, each named.**

Lane name: **revenger-shokunin**. A **shokunin lane** minted and trained
under the [shokunin](https://github.com/VeigaPunk/shokunin) skill.

**Wiki:** [lane overview](https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/shokunin-binary-forensics?branch=main)

## Domain

From `PROVINCE.md`: native binaries, managed assemblies,
Electron/JavaScript packages, Android APKs, archives, firmware,
browser/Electron runtime evidence — using the REA skill and toolset.
Every conclusion separates observation, inference, and unknown, and
cites Evidence IDs.

The r55–r57 replay repair checks this domain's saved PE evidence ledger.
It does not take ownership of generic harness gates.

## What it refuses

Live-target execution beyond the declared target and lifecycle; DRM
circumvention or piracy facilitation; publishing reversed code; asset
rights claims; harness/evidence auditing; game-mechanics verification
([game-dev-2d](https://github.com/VeigaPunk/shokunin-godot-2d));
narrative canon ([lore](https://github.com/VeigaPunk/shokunin-world-bible)).

Writes only this repository. Sibling repos and domain source trees are
read-only. Historical `.shokunin/revenger/**` paths identify imported
evidence, not the current write scope.

Host REA / Ghidra surface maps are maintained by
[kaidoku](https://github.com/VeigaPunk/shokunin-reverse-engineering)
and do not rebase this lane's frozen receipt commands.

## In this repository

```
PROVINCE.md     evidence-ledger fence
SHONEN.md  SCORECARD.md  LOG.md
corpus/
  fixtures/     checksum-r1, duplicate-r15, …
  knowledge/    lessons/
  live/
  verify_named_multi_icon_states.py
  verify_multi_icon_states.py
  verify_icon_states.py
  verify_icon_languages.py
  verify_pe_resources.py
  verify_saved_evidence.py
  verify_shape_evidence.py
  verify_semantic_trace.py
  verify_js_graph_delta.py
  verify_evm_evidence.py
reports/
  round-1/replay_scenarios.py
```

This lane is still in shonen seed form — distilled `SKILL.md` is absent;
the corpus and verifiers are the craft record.

## Replay the named-icon ledger

From this repository root:

```sh
python3 -B corpus/verify_named_multi_icon_states.py
```

This checks the authored r55–r57 PE32+ fixtures against their saved
normalized results, exact byte deltas, pinned Evidence IDs, and receipt
command/hash. `ROOT` locates the current corpus; `HIST` pins the
original producer path as recorded identity only. Moving this checkout
must not change `HIST`, rewrite saved records, or require the historical
directory to exist.

The output establishes bounded saved-record consistency, not
authenticated producer origin, a new REA analysis, PE execution, or
general parser correctness. The separate multi-image and language-ledger
relocation failures remain outside this repair.

```sh
python3 -B reports/round-1/replay_scenarios.py
```

Exercises the real verifier in three cwd/path contexts and six
individually forged saved-record copies, checking that original inputs
remain unchanged. Exit 0 means this bounded battery passed; it does not
admit a training round. See
`.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json` and
`SCORECARD.md`'s interactive-continuation section before advancing a
round. Permanent gate-registry and corpus-bar files remain named debt.
No native judgment or completion receipt is claimed by these replay
commands.

## How a lane learns

Append-only corpus; every claim separates observation / inference /
unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme).
