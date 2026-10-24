# R63ScoutFirmware — C2 / M33 recon

Seat `revenger-r63.R63ScoutFirmware`. No installs. No pacman. `binwalk` 3.1.0 was already at `/usr/bin/binwalk` (package `binwalk 3.1.0-1`). `npx -y rea-agents@6.5.0` resolved to the existing cache `~/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents` (`package.json` version `6.5.0`). Scratch `/tmp/revenger-r63-scout-fw` removed after this report. Nothing under `corpus/` was written. The guide snapshot is a lead, not a `SOURCES.md` row.

## 1. Firmware guide snapshot

| field | value |
|---|---|
| blob URL | https://github.com/morluto/rea/blob/main/docs/firmware-analysis.md |
| raw URL fetched | https://raw.githubusercontent.com/morluto/rea/main/docs/firmware-analysis.md |
| access date | 2026-10-23 |
| HTTP | 200, `text/plain; charset=utf-8` |
| bytes | 15474 |
| sha256 | `d4a25c8569b37c3d030431333db08fc459af54a163af7815b4505cce2f16a898` |
| latest commit touching that path | `15450643f7502114c4f0755416f97b8f0b358b69` at `2026-10-23T19:00:09Z` |

Byte-exact copy: `.ufo/waves/round-63/source-snapshots/rea-firmware-guide.md` (same sha256). Not a registry row. `main` is newer than pinned `rea-agents@6.5.0`; use the package schema in §3, not the guide's later wording, for the saved record.

Guide facts that bear on C2 (lead only): inspection is Binwalk 3.1.x, parser verified against 3.1.0; `REA_BINWALK_COMMAND` must be an absolute path; REA does not install Binwalk; region offsets are original-file bytes; `reported_size` preserves Binwalk's size; `size_basis=provider_reported_validation_unknown`; a signature is not a validated partition; inspection does not extract and does not execute. REA's own fixture generator (`scripts/fixtures/firmware/generate.py` on `main`) builds gzip+USTAR, not uImage, and it compiles a host C probe — out of scope here; this round's fixture must stay inert and unexecuted.

## 2. M33 red-before (independent binwalk 3.1.0)

Banner on every run: **85 file signatures**. Default scan reports **187 magic patterns**. `--search-all` (`-a`) reports **196**. `binwalk -L` lists `gzip`, `uimage`, and `zlib` as `Built-in`. There is no local signature file and no cache: `~/.config/binwalk`, `~/.cache/binwalk`, and `/usr/share/binwalk` are absent. Package files are the binary plus `/usr/share/licenses/binwalk/`. Upstream source is not checked out. Tag `v3.1.0` of `ReFirmLabs/binwalk` (read, not executed):

- `src/magic.rs`: `gzip` `short: false`, magic `1f 8b 08`; `uimage` `short: false`, magic `27 05 19 56`; `zlib` `short: true` with the comment that a 2-byte magic matches only at the start of a file. `--search-all` is what lifts that restriction (187 vs 196 patterns).
- `src/signatures/zlib.rs`: magics `78 9c`, `78 da`, `78 5e` only. Size is the dry-run inflate length. `78 01` is not a magic (a 55-byte stored-block stream with that header was not reported).
- `src/structures/uimage.rs`: `UIMAGE_HEADER_SIZE = 64`. Parse is big-endian and requires a known OS, CPU, image type, and compression, then header CRC32 over the 64-byte header with the CRC field zeroed.
- `src/extractors/uimage.rs`: after the header parses, the data CRC32 must match or the signature is rejected. Reported size is header + data size.

### 2a. 1056-byte magic header — zero findings (requested construction)

`struct.pack('>I', 0x27051956) + 1052 zero bytes`. 1056 bytes. sha256 `b4e9f53c88b4c5a593ac6df61ae35f89e5b432cf454bde0f7167475f91164347`.

Default and `-a`, exit 0, JSON `file_map: []`:

```text
Analyzed 1 file for 85 file signatures (187 magic patterns) in 1.0 milliseconds
Analyzed 1 file for 85 file signatures (196 magic patterns) in 1.0 milliseconds
```

Same zero `file_map` for a 64-byte header with Linux/ARM/kernel/none enums but `header_crc=0` and `data_crc=0` plus a 992-byte zero payload (sha256 `352628200bf330818027f9cc18ae47330968fb71f92a133b9753b5634bcac136`).

### 2b. Qualifier — a CRC-valid uImage of the same length is detected

Not the requested zero-finding image. Header CRC and data CRC both valid, 64 + 992 = 1056, name `probe`, load/entry `0x80000000`. sha256 `c6f1d06581f18938326f7100fc72277795bfc41e26cc6ffa0eba5bec1286d5dd`. Default scan (no `-a`), exit 0:

```text
0  0x0  uImage firmware image, header size: 64 bytes, data size: 992 bytes, compression: none, CPU: ARM, OS: Linux, image type: OS Kernel Image, load address: 0x80000000, entry point: 0x80000000, creation time: 1970-01-01 00:00:00, image name: "probe"
Analyzed 1 file for 85 file signatures (187 magic patterns)
```

JSON: `offset 0`, `size 1056`, `name "uimage"`, `confidence 250`. So "uImage is absent from the 85" is false. "This magic-only 1056-byte image produces zero findings" is true. M33's stale premise is the unverified assumption, not a missing signature. `[INFERENCE]` L1's pre-probe image failed header and/or data CRC (or the OS/CPU/type enums); that matches the zero-finding result, not an absent signature.

### 2c. zlib at offset 512, reported size 55, name `zlib`

Stream: `zlib.compress(bytes(range(47)), 6)`. 55 bytes, header `78 9c`, sha256 `23d0cd96fbe5f590eceadf574251c46e9f6dc8bfdbd93b541e140a3b4e034956`. Image: 512 zero bytes + that stream (567 bytes). Image sha256 `33fe9d07609592e267b409c47fa12df79360eb545df5715fc336a7e91c056912`.

Default scan: exit 0, **zero hits** (short magic, not at offset 0).

`--search-all`: exit 0, one hit.

```text
512  0x200  Zlib compressed file, total size: 55 bytes
Analyzed 1 file for 85 file signatures (196 magic patterns)
```

JSON: `offset 512`, `size 55`, `name "zlib"`, `confidence 250`, `description "Zlib compressed file, total size: 55 bytes"`. Levels 2 and 7 of the same 47-byte sequence also compressed to 55 bytes and reported the same way. This is the M33 positive control, and it requires `--search-all`. REA 6.5.0 already passes that flag (§3).

gzip is the contrasting short=false control: `gzip.compress(b'hello firmware', mtime=0)` (34 bytes, magic `1f 8b 08`) at offset 512 is reported by the **default** scan as `offset 512`, `size 34`, `name "gzip"`.

### 2d. Scanner resume (observed, not a source reading of the loop)

- Two zlib members, `--search-all`: both reported, `offset 512 size 55 name zlib` and `offset 583 size 28 name zlib`. The scan does not stop at the first hit.
- Default scan of that same file: zero hits (both are off-origin short magics).
- CRC-valid uImage covering bytes 0..1056 with the same 55-byte zlib planted at file offset 512 (sha256 `a054d488326959372de4b5943f057b8c3f0b7b4adf7b72842cbdd697062f4533`): default and `-a` both report **only** `offset 0 size 1056 name uimage`. The inner zlib is not a second row.
- Magic-only 1056-byte image with that zlib at 512: default zero hits; `-a` reports only the zlib at 512 (the uImage magic does not consume the span when CRC/enums fail).

`[INFERENCE]` a hit's reported span is not also emitted as an inner signature. A fixture that needs the zlib row must not wrap it in a CRC-valid uImage that covers those bytes.

## 3. `inspect-firmware-regions` envelope (rea-agents 6.5.0)

Commands run: `npx -y rea-agents@6.5.0 --help` (exit 0, 17408 bytes), `--llms` (exit 0, 17217 bytes), `inspect-firmware-regions --help` (exit 0), `inspect-firmware-regions --schema` (exit 0). No firmware file was passed to REA. No target execution.

`--llms` is a command table, not a field schema. The row is:

```text
| `rea inspect-firmware-regions <path>` | Inspect firmware signature candidates without extracting them |
```

`--help` lists the same command. `inspect-firmware-regions --help`:

```text
Usage: rea inspect-firmware-regions <path>
  path  Local firmware path; never executed
```

`--schema` prints the **input** only:

```yaml
args:
  type: object
  properties:
    path:
      type: string
      minLength: 1
      description: Local firmware path; never executed
  required[1]: path
  additionalProperties: false
```

It does not print `evidence_id` / `normalized_result`. Those live in the package.

CLI default format is `toon` (`dist/cliOutput.js` `let format = "toon"`). `--format json` and `--json` select JSON. `--full-output` defaults false. The F counter (`reports/round-63/measure.py`) `json.loads` every `corpus/live/runs/**/*.json` and counts a file only when the value is a dict, `evidence_id` is truthy, and `normalized_result is not None`. It then counts `operation` (missing → `"unknown"`). Family `firmware` matches only `inspect_firmware_regions`. A toon stdout saved as `.json` does not count. `[INFERENCE]` the file that should be saved is the Evidence object from `--format json`, not the toon transcript. This seat did not run the command, so the exact stdout bytes are unverified.

Evidence object (`dist/domain/evidence.js`, `evidenceBaseSchema`, strict) keys a saved record carries:

`evidence_id` (`ev_` + digest), `subject`, `provider`, `analysis_profile`, `predicate_type`, `operation`, `parameters`, `raw_result`, `normalized_result`, `confidence` (`observed`|`derived`|`inferred`), `authority`, `environment`, `limitations`, `relationship_coverage`, `locations`, `evidence_links`.

Counter-necessary subset: truthy `evidence_id`, `normalized_result` not null, `operation` exactly `inspect_firmware_regions` (underscore). The CLI spelling `inspect-firmware-regions` does not match the family set.

`normalized_result` for this operation (`dist/domain/firmware/firmwareAnalysis.js` in 6.5.0, strict):

- `engine`: `name`, `version`, `executable_path`, `executable_sha256`, `source_revision` (must be null), `worker_count` (must be 1)
- `input_size` (int ≥ 0)
- `coverage`: literal `signature_scan`
- `regions[]`: `provider_id`, `offset`, `reported_size`, `signature`, `description`, `reported_confidence` (int 0..255), `size_basis` literal `provider_reported_validation_unknown`

There is no `size` field and no decompressed SHA-256. `FirmwareReports.js` copies Binwalk `hit.size` → `reported_size`, `hit.name` → `signature`, `hit.id` → `provider_id`, `hit.confidence` → `reported_confidence`. `provider_id` is the producer UUID (changes per run; the guide says compare hashes and ranges, not that id).

`FirmwareProvider.js` invokes, and only this invocation:

```text
binwalk --quiet --search-all --threads 1 --log <private report.json> <copied input>
```

That is why a zlib at offset 512 is visible to REA even though a default `binwalk` scan misses it. The tool contract text in this package: "Binwalk 3.1.x (verified with 3.1.0). Returns offsets, reported lengths, descriptions and raw confidence values. Length validation and runtime addresses remain unknown. No extraction or target execution."

`main` at the guide commit adds `firmwareExecutionBudgetSchema` onto the result. That is **not** in the 6.5.0 schema this counter will parse. Do not require those extra keys of a 6.5.0 record.

C2 clause (c) asks the record's regions to match `truth.json` on offset, size, and for extractable members the decompressed SHA-256. Against this schema, offset maps to `regions[].offset` and size maps to `regions[].reported_size` (not `size`). The decompressed SHA-256 is not a field of `inspect_firmware_regions`. `[INFERENCE]` that digest has to be computed from the fixture bytes by the oracle, unless the seat also saves an `extract_firmware` record (that operation does carry file `sha256`, but it is a different `operation` and would not by itself flip `firmware`). Inspection does not extract.

## Unknowns

- Exact L1 pre-probe bytes were not in the tree. §2a and §2c reproduce the claimed results (zero uImage findings; zlib offset 512 / size 55 / name zlib) without claiming byte-identity with L1's files.
- CLI stdout shape of a real `inspect-firmware-regions --format json` run was not captured (no REA invocation on a fixture). Schema above is from the 6.5.0 package, not from a saved Evidence file.
- Whether `--full-output` wraps extra keys around the Evidence object was not executed. Default is off; the counter needs the Evidence dict at the JSON root.
