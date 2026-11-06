# ExecApkProbe findings — round-100 wave w1

## Deliverable

`reports/round-100/cap_apk_probe.py` — sha256
`b2c9d189e75c582b06ce5636af17267869e70965c13d33ced10f501a03f2c71a`, 17.3 KB,
`python3 -m py_compile` clean. BUILT sent to RevengerR100 (after the
L1-requested pre-freeze cwd fix); bytes final, no post-BUILT edits.

## Contract conformance (claims.md §C2)

Invocation: `PYTHONUTF8=1 python3 -B reports/round-100/cap_apk_probe.py
--fixture corpus/fixtures/apk-r65 --work <scratch>` (from lane root). stdout
carries exactly the seven contract lines in order (CAP_FIXTURE_SHA, two
CAP_DECODER version lines, CAP_ANDROGUARD, CAP_APKTOOL, CAP_TAMPER_DETECTED,
CAP_APK_VERDICT last); diagnostics to stderr. rc 0 pass / 1 fail / 2 usage or
missing decoder. A fixture-sha mismatch does not short-circuit: every leg
runs, verdict fails. Decoders resolve via PATH with `--androguard`/`--apktool`
overrides. Scratch: `--work` > `$HYAKU_SCRATCH` > TMPDIR (mkdtemp); created
scratch removed on exit. Every decoder subprocess (`androguard axml`,
`apktool d`, both `--version` calls) runs with `cwd=<probe scratch dir>` so
androguard's `androguard.log` lands in scratch and dies with it; probe()
resolves `--fixture` to an absolute path first (`Path(args.fixture).resolve()`)
because the decoders' relative APK argument must survive their changed cwd.
Verified: `git -C <lane> status --porcelain` identical before/after the
genuine lane-root run and the full battery — the probe leaves no file in the
lane.

## Truth values (never hardcoded)

Derived in-probe from truth.json `axml_declared`: attribute `name_idx`
indexes `strings` for the field name; `data_type` 3 (TYPE_STRING) takes the
value from `strings[raw_value_idx]`; other types (16 = TYPE_INT_DEC) render
`data` in decimal. Result: package=`com.example.r65`, versionCode=`1`,
versionName=`1.0`. `CAP_FIXTURE_SHA` compares sha256(fixture.apk) against
truth.json `image.sha256` = `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`.

## Decoders and the namespace quirk

- androguard 4.1.4: argv `[androguard, axml, <apk>]`, XML from stdout;
  version from `[androguard, --version]` first stdout line
  ("androguard, version 4.1.4").
- apktool 3.0.3: argv `[apktool, d, -f, -s, -o, <scratch>/apktool-out, <apk>]`,
  reads `<outdir>/AndroidManifest.xml`; version from
  `[apktool, --version]` ("3.0.3").

Quirk (recorded as instructed): the fixture's attribute records carry
`ns_idx=0`, i.e. the namespace slot holds string 0, which is the *prefix*
string "android", not the URI at index 1. Both decoders therefore render the
attribute namespace as a prefix bound to URI "android" — androguard as
`xmlns:ns0="android"` with `ns0:versionCode`, apktool as `xmlns:n0="android"`
with `n0:versionCode`. The probe parses with ElementTree and matches attribute
*local names* (strips `{uri}`), so the prefix is irrelevant; this quirk is
also documented in the probe's `manifest_attrs` docstring.

## Tamper leg (method and exact offsets)

`bump_last()` derives a same-length different value from the truth versionName
("1.0" -> "1.1"; last digit incremented). The string pool is UTF-8
(flags 0x100 read from the pool chunk header at manifest offset 24); short
entries are `[u8 utf16len][u8 utf8len][utf8][NUL]`, so the pattern is
`03 03 31 2E 30 00`, occurring exactly once at **member offset 198**
(AndroidManifest.xml), i.e. **file offset 246** in fixture.apk (local header
at offset 0, 30 fixed bytes + 18-byte name). Replacement `03 03 31 2E 31 00`
is byte-identical in length, so ZIP_STORED sizes and offsets stay valid. The
CRC-32 of the patched member (zlib.crc32) is written into the local header at
`header_offset+14` (offset 14) and into the central-directory entry at
`entry+16`, located by scanning `PK\x01\x02` signatures and matching the
stored name (assert exactly one entry patched). The copy is verified with
`zipfile.ZipFile(...).testzip() is None` before decoding. Both decoders must
then report versionName == "1.1" AND != truth "1.0"; a truth-echoing decoder
fails the leg (observed with shims). UTF-16 pool input is also handled
(`[u16 len][u16 len][utf-16-le][u16 NUL]`) per the task note.

## Observed results (builder self-checks; dev only, not scoring)

Exact commands and rc values are in `probe-dev.log` beside this file:

1. Genuine fixture: `CAP_APK_VERDICT=pass`, rc=0, all seven lines pass.
2. Truth-echoing PATH shims for both decoders (control ii shape):
   CAP_ANDROGUARD=pass, CAP_APKTOOL=pass, CAP_TAMPER_DETECTED=fail,
   verdict fail, rc=1.
3. Flipped fixture copy with original truth.json (control iii shape):
   CAP_FIXTURE_SHA=fail, CAP_APK_VERDICT=fail, rc=1, zero probe-side
   tracebacks.
4. Missing decoder (empty PATH): rc=2 with verdict fail.

No C1/C2 target run was executed and nothing was scored; all runs were
builder development self-checks on `corpus/fixtures/apk-r65` in scratch.

## Bugs found during development (fixed before final bytes)

1. String-pool flags were read at pool+20 (stringsStart) instead of pool+16
   (flags), so the UTF-8 flag was missed and the pool pattern never matched.
2. The flipped-fixture control crashed the probe with an uncaught
   BadZipFile when tamper_leg() read the corrupt member; zip reads are now
   guarded and contract lines print incrementally.
3. L1-requested pre-freeze fix: androguard writes `androguard.log` into its
   cwd, so all decoder subprocesses now run with `cwd=<probe scratch>`;
   the naive fix broke relative `--fixture` (decoders resolved the APK
   against their new cwd), so the probe also resolves the fixture path to
   absolute. Lane cleanliness verified with `git status --porcelain`
   before/after.

## Observations / risks

- On the corrupted (control iii) fixture the two real decoders disagree:
  apktool 3.0.3 still reported all three truth values (it evidently prefers
  the raw string-pool value over the flipped typed data), androguard 4.1.4
  rendered the flipped INT_DEC as `?00000001`. A shim that mimics "real
  apktool behaviour" would still be caught by the tamper leg (versionName
  pool value), and the sha leg fails regardless — but anyone writing stricter
  controls should know the decoder legs do not both fail on this shape.
- The tamper patch assumes short pool entries (both length fields < 0x80 for
  UTF-8, < 0x8000 for UTF-16); the probe refuses anything else instead of
  guessing.
- apktool's framework cache under ~/.local/share/apktool was touched by the
  real decoder runs — allowed by the wave rules.
- No tools installed or upgraded this session (both decoders already present);
  nothing to record under the tooling rule.
- Scratch root /fast/scratch/hyaku/revenger-r100/ExecApkProbe removed before
  yield; receipts copied to `probe-dev.log` in this wave dir.
