# Round-64 C1 record ↔ truth correspondence

## Scope

Compared the saved observation record at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json`, its saved stdout at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw`, receipt at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json`, and authored fixture oracle at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json`. `inspection.json` and `stdout.raw` are byte-identical (command output below); the “record” column therefore gives their shared values. Values are compared as their stored JSON scalar values; absent record fields are explicitly not comparable, not inferred matches.

## Field-level correspondence

| Field | Record source/value (`inspection.json` = `stdout.raw`) | Truth source/value | Receipt source/value | Record ↔ truth byte-for-byte |
|---|---|---|---|---|
| operation | `inspection.json.operation` / `stdout.raw.operation` = `inspect_firmware_regions` | no operation field | `receipt.json.command` = `npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json` | No truth operation field; not comparable. Receipt command denotes this operation but is a distinct string/representation. |
| evidence_id | `inspection.json.evidence_id` / `stdout.raw.evidence_id` = `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259` | no evidence ID field | `receipt.json.evidence_id` = `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259` | No truth field; not comparable. Record and receipt values are exactly equal. |
| subject SHA-256 | `inspection.json.subject.digest.sha256` / `stdout.raw.subject.digest.sha256` = `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | `truth.json.image.sha256` = `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | `receipt.json.fixture_sha256` = `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | Yes — exact string match across record, truth, and receipt. |
| subject/input size | `inspection.json.normalized_result.input_size` / `stdout.raw.normalized_result.input_size` = `2048` | `truth.json.image.size` = `2048` | no size field | Yes — exact numeric value match. |
| region 0 offset | record has no corresponding region (the first recorded region is at offset 512) | `truth.json.regions[0].offset` = `0` | no region field | No record field; not comparable. |
| region 0 size | record has no corresponding region | `truth.json.regions[0].size` = `512` | no region field | No record field; not comparable. |
| region 0 kind | record has no corresponding region | `truth.json.regions[0].kind` = `padding` | no region field | No record field; not comparable. |
| region 0 decompressed-member SHA-256 | record has no corresponding region/member field | `truth.json.regions[0].decompressed_member` is absent | no member field | Not applicable (no truth member digest and no record field). |
| region 1 offset | `inspection.json.normalized_result.regions[0].offset` / `stdout.raw.normalized_result.regions[0].offset` = `512` | `truth.json.regions[1].offset` = `512` | no region field | Yes — exact numeric value match. |
| region 1 size | `inspection.json.normalized_result.regions[0].reported_size` / `stdout.raw.normalized_result.regions[0].reported_size` = `79` | `truth.json.regions[1].size` = `79` | no region field | Yes — exact numeric value match. |
| region 1 kind | `inspection.json.normalized_result.regions[0].signature` / `stdout.raw.normalized_result.regions[0].signature` = `zlib` | `truth.json.regions[1].kind` = `zlib` | no region field | Yes — exact string match. |
| region 1 decompressed-member SHA-256 | no record member-digest field | `truth.json.regions[1].decompressed_member.sha256` = `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` | no member field | No record-side digest; not comparable. |
| region 2 offset | record has no corresponding region | `truth.json.regions[2].offset` = `591` | no region field | No record field; not comparable. |
| region 2 size | record has no corresponding region | `truth.json.regions[2].size` = `433` | no region field | No record field; not comparable. |
| region 2 kind | record has no corresponding region | `truth.json.regions[2].kind` = `padding` | no region field | No record field; not comparable. |
| region 2 decompressed-member SHA-256 | record has no corresponding region/member field | `truth.json.regions[2].decompressed_member` is absent | no member field | Not applicable (no truth member digest and no record field). |
| region 3 offset | `inspection.json.normalized_result.regions[1].offset` / `stdout.raw.normalized_result.regions[1].offset` = `1024` | `truth.json.regions[3].offset` = `1024` | no region field | Yes — exact numeric value match. |
| region 3 size | `inspection.json.normalized_result.regions[1].reported_size` / `stdout.raw.normalized_result.regions[1].reported_size` = `90` | `truth.json.regions[3].size` = `90` | no region field | Yes — exact numeric value match. |
| region 3 kind | `inspection.json.normalized_result.regions[1].signature` / `stdout.raw.normalized_result.regions[1].signature` = `zlib` | `truth.json.regions[3].kind` = `zlib` | no region field | Yes — exact string match. |
| region 3 decompressed-member SHA-256 | no record member-digest field | `truth.json.regions[3].decompressed_member.sha256` = `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` | no member field | No record-side digest; not comparable. |
| region 4 offset | record has no corresponding region | `truth.json.regions[4].offset` = `1114` | no region field | No record field; not comparable. |
| region 4 size | record has no corresponding region | `truth.json.regions[4].size` = `934` | no region field | No record field; not comparable. |
| region 4 kind | record has no corresponding region | `truth.json.regions[4].kind` = `padding` | no region field | No record field; not comparable. |
| region 4 decompressed-member SHA-256 | record has no corresponding region/member field | `truth.json.regions[4].decompressed_member` is absent | no member field | Not applicable (no truth member digest and no record field). |

The saved record reports exactly two zlib signatures at `(offset=512, size=79)` and `(offset=1024, size=90)`; both reported fields match the corresponding truth entries. Truth describes three intervening/surrounding padding regions that are not emitted in the record. The two decompressed member digests are present in truth only, not in the record. This is a correspondence readout, not evidence that the observation record is a complete byte-layout description.

## Exact commands run and outputs

The following read-only shell commands extracted the fields above and checked the saved artifacts. The receipt's `command` value shown in the table is historical receipt data; it was not re-executed for this readout.

### 1. Inspection record

Command:
```sh
jq -c '{operation,evidence_id,subject_sha256:.subject.digest.sha256,input_size:.normalized_result.input_size,regions:[.normalized_result.regions[]|{offset,size:.reported_size,kind:.signature}]}' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json
```
Output:
```json
{"operation":"inspect_firmware_regions","evidence_id":"ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259","subject_sha256":"bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be","input_size":2048,"regions":[{"offset":512,"size":79,"kind":"zlib"},{"offset":1024,"size":90,"kind":"zlib"}]}
```

### 2. Saved stdout record

Command:
```sh
jq -c '{operation,evidence_id,subject_sha256:.subject.digest.sha256,input_size:.normalized_result.input_size,regions:[.normalized_result.regions[]|{offset,size:.reported_size,kind:.signature}]}' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw
```
Output:
```json
{"operation":"inspect_firmware_regions","evidence_id":"ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259","subject_sha256":"bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be","input_size":2048,"regions":[{"offset":512,"size":79,"kind":"zlib"},{"offset":1024,"size":90,"kind":"zlib"}]}
```

### 3. Fixture truth

Command:
```sh
jq -c '{image_sha256:.image.sha256,image_size:.image.size,regions:[.regions[]|{offset,size,kind,decompressed_member_sha256:.decompressed_member.sha256}]}' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json
```
Output:
```json
{"image_sha256":"bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be","image_size":2048,"regions":[{"offset":0,"size":512,"kind":"padding","decompressed_member_sha256":null},{"offset":512,"size":79,"kind":"zlib","decompressed_member_sha256":"a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86"},{"offset":591,"size":433,"kind":"padding","decompressed_member_sha256":null},{"offset":1024,"size":90,"kind":"zlib","decompressed_member_sha256":"2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9"},{"offset":1114,"size":934,"kind":"padding","decompressed_member_sha256":null}]}
```

### 4. Receipt binding fields

Command:
```sh
jq -c '{command,exit_code,fixture_sha256,stdout_sha256,evidence_id}' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json
```
Output:
```json
{"command":"npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json","exit_code":0,"fixture_sha256":"bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be","stdout_sha256":"f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9","evidence_id":"ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259"}
```

### 5. Exact saved-record comparison

Command:
```sh
cmp -s /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw && printf 'inspection.json and stdout.raw: byte-identical\n'
```
Output:
```text
inspection.json and stdout.raw: byte-identical
```

### 6. Saved stdout and fixture hashes

Command:
```sh
sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
```
Output:
```text
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
```
