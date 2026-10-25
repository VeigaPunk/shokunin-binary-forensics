# Bounty triage report — sample-client 1.4.2

## Scope

Example Bounty Program, written policy at
https://bounty.example.test/policy#scope, authorization dated 2026-10-01. The
single program-provided artifact is in scope.

## Artifact identity

`artifacts/client.zip`, 866 bytes, program-provided.

sha256 `3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3`.

## Method

Static artifact analysis (`static-artifact-analysis`) and one offline fixture
(`offline-fixture`).

## Evidence

- E1 — artifact digest.
- E2 — member inventory.
- E3 — declared `config.json` fields.
- E4 — inference about a declared debug flag.
- E5 — the runtime effect, recorded as unknown.

## Reproduction

1. `sha256sum artifacts/client.zip`
2. `python3 -m zipfile -l artifacts/client.zip`
3. `python3 -c "import zipfile; print(zipfile.ZipFile('artifacts/client.zip').read('config.json').decode())"`

## Impact

- The telemetry endpoint accepts unauthenticated writes from any client.
- This proves full compromise of the reporting pipeline (E4).

## Limitations

One authored static artifact, read once. No runtime observation.

## Stop conditions

Not reviewed; a live test against the endpoint would settle the question.

## Disclosure

Program channel `security@example.test`, 90-day window per the program policy.
