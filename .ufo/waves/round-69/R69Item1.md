MATCH — the `--fact archive` line embedded in the v4 entry (`corpus/knowledge/round-69-apk-axml-byte-evidence.md:27`, repeated at `:200`) is byte-identical to the live re-derivation (exit 0, 159 stdout bytes, sha256 `983053887fddc48b26095f18f94e24351b801f0fadad7414edb004768d07315c` on both sides); every one of the four fields agrees and the accompanying prose sentence asserts nothing the output does not support.

# R69Item1 — per-item re-derivation: the archive digest/size fact

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (base `222a7a7`). Read-only seat: nothing edited, no git-mutating command run, no package installed.
Axes: **coverage** (a Q11-shaped leg of the C05 v4 re-gate: is this cited block re-derivable on the v4 bytes?) and **depth** (field-by-field, prose-vs-output, and byte-freeze attribution).

## 1. Command and actual output

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
EXIT_CODE=0
```

- stdout: 159 bytes (one line + `\n`), sha256 `983053887fddc48b26095f18f94e24351b801f0fadad7414edb004768d07315c`
- stderr: 0 bytes
- determinism: three consecutive runs → `1` distinct stdout (`sort -u | wc -l` = 1)
- cwd-independence: identical stdout from `/tmp` (absolute invocation) and from `/home/vgpnk/Projects/shokunin` (relative invocation), both exit 0 — the fixture is resolved script-relatively (`readout.py:20-21`: `ROOT = Path(__file__).resolve().parent`; `APK = ROOT / "fixture.apk"`).

Independent size check of the file the script reads: `stat -c '%s' corpus/fixtures/apk-r65/fixture.apk` → `947`.

## 2. The entry's block

Entry: `corpus/knowledge/round-69-apk-axml-byte-evidence.md` (215 lines, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`).

Block, `:25-:28` (`:raw`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
```

- **Embedded line = `:27`**; command line = `:26`; the second, full-invocation copy of the same line is **`:200`** (under `:199` `$ python3 -B corpus/fixtures/apk-r65/readout.py`).
- `diff` actual-stdout vs `sed -n '27p'` → empty (`BYTE_IDENTICAL=yes`); both sides sha256 `983053887f…` (identical digest).
- `diff` actual-stdout vs `sed -n '200p'` → empty (`LINE200_IDENTICAL=yes`); full-invocation first line also identical, and the full run re-derives the entry's own receipt at `:194` exactly: exit 0, **15** stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (actual `sha256sum` of the captured full stdout = same value).

## 3. Field-by-field verdict (actual vs embedded)

| field | actual output value | embedded `:27` value | verdict |
|---|---|---|---|
| `fact` | `"archive"` | `"archive"` | MATCH — is the selector echo, consistent with `--fact archive` (`readout.py:43` sets `ONLY`, `readout.py:27-30` filters on `fact != ONLY`) and with the command at `:26` |
| `bytes` | `947` | `947` | MATCH — and independently equal to `len(apk)` (`readout.py:45`), to `stat` size 947, and to the prose's bold **947 bytes** |
| `path` | `"corpus/fixtures/apk-r65/fixture.apk"` | `"corpus/fixtures/apk-r65/fixture.apk"` | MATCH (string equality); see caveat A below — the value is an emit-site literal (`readout.py:45`), not a derived field |
| `sha256` | `"05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"` | same 64 hex chars | MATCH — recomputed live by `hashlib.sha256(apk).hexdigest()` over the bytes read at `readout.py:44`; also equals the S041 anchor at `:7` (`fixture sha256 05d2280f… (947 bytes)`) |
| key set / order / types | `bytes`(int), `fact`(str), `path`(str), `sha256`(str), alphabetical | identical, alphabetical | MATCH — `json.dumps(..., sort_keys=True)` (`readout.py:30`), so no extra, missing, reordered or retyped field; 159 bytes on both sides leaves no room for a hidden difference |

**Mismatched fields: none (0 of 4).**

Caveat A (advisory, non-blocking, not a mismatch): the `path` field is a hardcoded literal at the emit site (`readout.py:45`), not a value derived from the file actually opened (`APK = ROOT / "fixture.apk"`). The label is **true** — `ROOT` resolves to `…/corpus/fixtures/apk-r65` and the file read is exactly that path — and the cwd tests above show the label is not silently reflecting the caller's cwd. It only becomes a Q11 concern if a future revision cites `path` as evidence of location *resolution*; the present prose does not.

## 4. Prose judgement — the sentence that claims this fact (`:23`, raw)

> `1. The archive is **947 bytes** with SHA-256 \`05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e\`, read from the file's bytes.`

- "**947 bytes**" ← `"bytes": 947` (and `len(apk)` at `readout.py:45`): supported.
- "SHA-256 `05d2280f…`" ← `"sha256": "05d2280f…"` (recomputed at `readout.py:46`): supported.
- "read from the file's bytes" ← `apk = APK.read_bytes()` (`readout.py:44`), then `len()`/`hashlib` over that same object; the mechanism is in-entry verifiable because the entry pins this exact script by sha256 (`:19` and `:196`: `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`) and the live file's sha256 equals it: supported.
- Nothing else is asserted: no universal quantifier ("every line"/"only"), no comparison to another archive, no producer/parser behaviour, no git object id, no claim about the whole readout (that is item 1's own fact only; the 15-line/`507d79f8…` receipt is stated separately at `:194` and separately re-derived above).

**Does the prose state anything the output does not support? No.** The one thing the output alone does not show — that the two numbers were *read from bytes* rather than echoed — is carried by the sha-pinned script the entry cites, and re-verified here; it is not an overstatement of the output.

Adjacent Q15 exposure: none. The block states no git object id / tree identity, so the round-69 Q15 criterion (`corpus/QUALITY.md:27`) has no leg on this fact; the digest is a content digest re-derivable from the working tree.

## 5. Byte-freeze attribution (void-condition check, read-only)

The round-69 claims declare `corpus/fixtures` bytes frozen. Observed, all identical:

- worktree blob `git hash-object corpus/fixtures/apk-r65/fixture.apk` → `b62216a955a4b130b67b7f8d35806abf07be92fa`
- `git rev-parse c7b7cf9:corpus/fixtures/apk-r65/fixture.apk` → `b62216a955a4b130b67b7f8d35806abf07be92fa` (round-65 claim tree)
- `git rev-parse 222a7a7:corpus/fixtures/apk-r65/fixture.apk` → `b62216a955a4b130b67b7f8d35806abf07be92fa` (round-69 base)
- readout script: `git rev-parse c7b7cf9:…/readout.py` = `git hash-object …/readout.py` = `0fcb1d859b3fcebad600ad5bc141cc0c0dd35bc8`
- `git status --porcelain corpus/fixtures/apk-r65/ corpus/knowledge/round-69-apk-axml-byte-evidence.md` → empty (no uncommitted drift in the fact's surface)
- only commit touching the fixture: `c7b7cf9 round-65: candidates — apk-r65 fixture+readout, …`

So the 947/frozen-digest agreement is not an accident of a locally modified working tree.

## 6. Axis contribution

- **coverage**: one Q11-leg of the C05 v4 re-gate resolves PASS on the v4 bytes for the archive fact — the cited command exists in-entry, runs, exits 0, and its output is the cited one. This is one seat's leg only; the C05 row flip still depends on the rest of the wave (this seat does not adjudicate C1).
- **depth**: the block survives the stronger checks beyond string equality — determinism (3 runs), stderr emptiness, cwd-invariance of the command, script-sha pinning, cross-commit blob identity, and the whole-invocation receipt at `:194`/`:200`.

## 7. Risks / blockers

- None blocking. No dependency on another seat was needed; nothing was missing.
- Advisory (caveat A above): `readout.py:45`'s `path=` literal is the only non-derived field in this output. Not a defect of this block; a future Q11 audit of the *path* line specifically should read it as a label, not a derivation.
- Not scored by this seat: any other fact block, the C05 row flip, README state, the counter run. Scope was this one fact.
- Cleanup: `/tmp/revenger-r69-item1-*.txt` scratch removed; no tool installs (none needed, so no tool/version/channel line applies).
