# Round 56 independent receipt review

## Commands / independent checks

Read-only Python byte checks (no producer rerun, target execution, or REA invocation):

```python
raw = Path(".shokunin/revenger/corpus/live/runs/round-56/inspection.raw.json").read_bytes()
receipt = json.loads(Path(".shokunin/revenger/corpus/live/runs/round-56/receipt.json").read_text())
inspection = json.loads(raw)
fixture = Path(".shokunin/revenger/corpus/fixtures/pe-r56/fixture.exe").read_bytes()
source = Path(".shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe").read_bytes()
sha256(raw); sha256(fixture); sha256(source)
```

Observed output:
- `sha256(raw)` = `59a95f9db16633b337fd058a6d1509c95687445af02d63bb3156309f1811bbe6`; equals receipt `stdout_sha256`.
- fixture r56: 1536 bytes, SHA-256 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`.
- fixture r55: 1536 bytes, SHA-256 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`.
- Direct byte comparison: files differ only at offset 928; byte changes 2 -> 3.
- `truth.json` declares r55 source hash and r56 hash above, size 1536, changed offset `[928]`; declarations match these independently calculated hashes/bytes.
- Evidence ID in inspection and receipt is identical: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a`.
- Inspection subject digest, receipt `fixture_sha256`, truth `sha256`, and actual r56 fixture SHA-256 all match.
- Receipt states command `npx -y rea-agents@6.4.0 inspect-pe-resources ...`, exit code 0, duration 0.6219461870205123s.

## Observation / inference / unknown

**Observation:** Saved JSON parses. Its computed byte hash matches the receipt's claimed stdout hash. The Evidence ID and fixture digest fields agree across receipt and saved inspection; independently hashing the supplied r56 bytes confirms the digest. The r55/r56 fixture comparison supports the truth file's single-byte mutation description. Evidence ID: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a`.

**Inference:** The saved receipt and saved inspection are internally consistent with one another and with the currently supplied fixture/truth bytes. The saved normalized result reports PE32+ resource inventory, three resources, complete coverage, and icon-group candidate relationships; these are claims in the saved record, not independently rerun analysis.

**Unknown / authentication limit:** These checks do not authenticate who produced either file, prove the stated command actually ran, establish stdout provenance, or cryptographically bind the Evidence ID to the JSON. No signature, trusted external log, or independent REA run was checked. Matching hashes demonstrate byte equality only against the local files and claims inspected. No executable was run.

## Verdict

**PASS: internal consistency checks. NOT AUTHENTICATED: producer/origin.** Do not treat this review as independent validation of the analysis findings or producer provenance.
