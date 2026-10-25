# Evidence ledger — sample-client 1.4.2

Artifact: `artifacts/client.zip`, program-provided, 866 bytes.

| id | artifact_sha256 | layer | statement | command |
|---|---|---|---|---|
| E1 | 3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3 | observation | The program-provided artifact hashes to the digest declared in `scope.json`. | `sha256sum artifacts/client.zip` |
| E2 | 3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3 | observation | The archive holds four members — README.txt, config.json, main.js, package.json — all stored without compression. | `python3 -m zipfile -l artifacts/client.zip` |
| E3 | 3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3 | observation | `config.json` declares `"debug": true` and `"telemetry_endpoint": "https://telemetry.example.test/collect"`. | `python3 -c "import zipfile; print(zipfile.ZipFile('artifacts/client.zip').read('config.json').decode())"` |
| E4 | 3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3 | inference | A default-true debug flag beside a telemetry endpoint may change what a build reports; the artifact declares the fields, not their runtime effect. | — |
| E5 | 3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3 | unknown | Whether the endpoint is reachable, authenticated, or part of production behavior. Not tested. | — |
