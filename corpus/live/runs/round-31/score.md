# Round 31 score contract: PE resource identity (pre-producer)

## Scope and oracle

This note defines scoring only; it does not score a round-31 parser result. The declared target is two RT_RCDATA resources (type ID 10), with identities `(type=10,name=2,language=1036)` and `(type=10,name=3,language=1033)`, distinct 15-byte payloads at distinct file offsets. Source of this claim: round-31 declaration in `.shokunin/revenger/LOG.md` (resource offsets proposed there: root 512, type directory 536, name dirs 568/592, data entries 616/632, payloads 672/704).

Construct the independent truth set from actual fixture bytes / a decoded source manifest—not from the REA output. For each truth occurrence, record the full identity tuple, data-entry location, payload file offset and length, and SHA-256 of exactly those payload bytes. Require two unique identity tuples and distinct payload ranges/digests as declared. Do not use name alone or payload digest alone as identity; matching must be one-to-one on the complete `(type,name,language)` tuple, then verify location/length/digest as attributes.

## Exact 2/2 scoring

Let `T` be the two oracle tuples and `R` the resource entries in the saved normalized result. A reported entry is a true positive only if its complete tuple matches exactly one still-unmatched member of `T`, and its payload file offset, length (=15), and SHA-256 equal that oracle member. Count each result row once; duplicate rows cannot match the same truth row twice.

- **Precision = TP / |R|**; require `|R|=2`, `TP=2`, hence 2/2. Any extra, malformed, duplicate, or identity-mismatched reported resource makes precision fail (e.g. 2 correct + 1 extra is 2/3, not 2/2).
- **Recall = TP / |T|**; require `|T|=2`, `TP=2`, hence 2/2. A missing, collapsed, or wrong-language/name/type entry makes recall fail.
- Overall identity pass requires both fractions 2/2 **and** exact payload-attribute checks for each matched tuple. Also require saved result coverage to say complete and resources count 2; partial/truncated/unknown coverage cannot establish 2/2 recall.

Report identity and payload attributes separately in the ledger. The declaration additionally requires independent source-byte decoding and a non-author review; absent either, do not admit the declared coverage claim even if the JSON appears to match.

## Reject / do-not-count conditions

Reject the 2/2 claim for any refusal or missing Evidence ID; non-PE32 input / wrong artifact SHA; incomplete coverage; extra or missing rows; duplicate tuple rows; tuple mismatch; wrong payload offset or length; payload hash mismatch; offsets that overlap or conflate the two distinct payloads; inability to derive the oracle independently; or reviewer disagreement. A matching tuple with wrong bytes is not an identity-and-payload true positive. Do not silently normalize ID-vs-name entries, language IDs, tuple order, or paths. Compare tuples order-independently, but retain per-entry locations for audit.

## Bounded evidence / receipts

Baseline receipt: `.shokunin/revenger/corpus/live/runs/round-30/inspection.json`, Evidence `ev_178f0cb2ef7b5e4f61e73e19f71cba354c44a337b998da07ee559cb93ede53df`, operation `inspect_pe_resources`, provider `rea-pe-resources` v1, normalized `format=pe32`, `coverage.status=complete`, `resources=1`. Its sole baseline tuple is `(10,2,1036)`, payload `[600,615)` (offset 600, length 15), SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`; locations: resource entry offsets 528/552/576, data-entry offset 584. Thus r30 is a one-resource schema example, not two-entry recall evidence.

Useful read-only receipt commands (after result exists):

```sh
python3 - <<'PY'
import json
p='.shokunin/revenger/corpus/live/runs/round-31/inspection.json'
d=json.load(open(p)); n=d['normalized_result']
print('evidence', d.get('evidence_id'), 'artifact', n['artifact']['sha256'])
print('format/coverage', n['format'], n['coverage'])
for r in n['resources']:
 print((r['type'],r['name'],r['language']), r['payload']['location'], r['payload']['sha256'])
PY
```

The tuple fields in this example should be extracted as `r['type']['id']`, `r['name']['id']`, `r['language']['id']` when each `kind` is `id`; do not assume names are IDs without checking `kind`. Baseline structure and values can be re-read without target execution via:

```sh
python3 -c "import json; d=json.load(open('.shokunin/revenger/corpus/live/runs/round-30/inspection.json'))['normalized_result']; print(d['directory'], d['directories'], d['resources'], d['coverage'])"
```

Boundary: this is a rubric for static PE resource-table identity only. It says nothing about payload interpretation, Windows loader behavior, execution, general parser correctness, producer authenticity, or native-session readiness. REA guidance names `inspect_pe_resources` as a portable static route; it explicitly treats opaque payloads as ranges/SHA-256. No parser outcome is asserted here.
