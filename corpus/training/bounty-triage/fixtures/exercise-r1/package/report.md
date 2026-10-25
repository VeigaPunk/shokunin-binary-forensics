# Bounty triage report — sample-client 1.4.2

## Scope

Example Bounty Program, written policy at
https://bounty.example.test/policy#scope, authorization dated 2026-10-01 and
valid through 2026-12-31. The single program-provided artifact is in scope.

## Artifact identity

`artifacts/client.zip`, 866 bytes, program-provided.

sha256 `3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3`.

## Method

Static artifact analysis (`static-artifact-analysis`) and one offline fixture
(`offline-fixture`). No live-target activity and no execution of the artifact
were performed or needed.

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

No network access is required; all three commands read the package copy.

## Impact

- The artifact declares `"debug": true` and a telemetry endpoint string (E3); the
  runtime effect of either field is unknown (E5).
- Impact beyond the artifact's own bytes is unknown (E5).

## Limitations

One authored static artifact, read once. No runtime observation, no endpoint
testing, and no claim about the vendor's production behavior.

## Stop conditions

None triggered: no live testing was requested or needed, and no credential or
personal data was encountered.

## Disclosure

Program channel `security@example.test`, 90-day window per the program policy.
