source: S048 — unblob upstream README (the project's own documentation) — https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md (docs, tier A for the project's own stated figures only; registry id S048 is the next unused after S047 and is PROVISIONAL until the L1 appends it) — scope: the three figures this entry quotes exactly as the project states them — its supported-format count with the format families it names, its runtime requirements, and its Ubuntu/Debian external-extractor install line together with the command it offers to verify that set; not extraction capability, not any handler's correctness, not the tool's behavior on any firmware image — anchors: every quote is located by item 2, which prints its line number and line text from the fetched bytes; the fetch digest is item 1
source: S049 — own-work host probe of one installed unblob, run by this entry's author on 2026-10-25 (own-work, tier A for that one run and that one host; registry id S049 is the next unused after S048 and is PROVISIONAL) — scope: the exit status and the dependency rows that `unblob --show-external-dependencies` printed for unblob 26.6.4 on this host at that date, as items 4 and 5 print them; not a statement about any other version, platform or earlier host state, and not evidence that any extraction works — anchor: the two commands and their full stdout are items 4 and 5
verified-at: 2026-10-25 (round-70 wave-1 build; items 1-3 fetched the document from branch `main` and item 4-5 ran the locally installed tool, each output pasted from the command printed above it; the fetch digest is pinned in item 1 so a later drift is visible rather than silent)
recheck: from the lane root, run item 1's command and require the printed sha256 to equal `6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716` before reading items 2 and 3 (a different digest means branch `main` moved and every quote must be re-located, not re-used); item 4's command re-runs `unblob --version` and `unblob --show-external-dependencies` and is credited only for the presence rows and exit status it prints on that host. At landing the fetched bytes should be committed as `corpus/snapshots/unblob-README.md` (same sha256) so items 2 and 3 read the snapshot offline, exactly as S032's snapshot serves the APK entry
coverage-map: C07 (`corpus/README.md`, firmware images — already `held`) — this is a DEEPENING of a held row, not a flip: it adds the upstream tool's own stated format count, runtime requirements and extractor dependency set to the ground C07 rests on. It does not add a fixture, does not run an extraction, and does not change any C07 status.
admission-status: candidate

# Unblob's own stated figures — format count, runtime requirements and external-extractor set — C07 deepening

Scope. One document, the unblob project's `README.md` on branch `main`, fetched once on 2026-10-25 (item 1), plus one probe of one locally installed unblob 26.6.4 on the same date (items 4 and 5). The analysis is **manual**: each quoted line is printed by a standard-library Python command that reads the fetched bytes; nothing is inferred from the project's website, its issue tracker or its source tree, and no extraction is run. Three claims are retained from the package entry `merge/revenger/knowledge/corpus/knowledge/digest-scope-versus-provenance-amendment-2026-10-23.md` — its claims 3, 4 and 5. Its claims 1 and 2 (the SWGDE document and the scope assignment) are **out of scope for this lane** and are not carried: no SWGDE row exists in `corpus/SOURCES.md` and none is opened here.

## Observation

Every numbered item is produced by the command printed above its output. All commands are `python3` standard-library invocations with no shell metacharacters, so the embedded-output gate can re-run them by argv.

1. The document is **7580 bytes** and **235 newline-terminated lines**, and its SHA-256 is `6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716`. The digest is claimed for these bytes only: it says nothing about what the branch held before or after the fetch, and nothing about who wrote them.

```
$ python3 -B -c "import hashlib,urllib.request as u;b=u.urlopen('https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md').read();print('bytes',len(b));print('lines',b.count(b'\n'));print('sha256',hashlib.sha256(b).hexdigest())"
bytes 7580
lines 235
sha256 6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716
```

2. The section headings that locate the three claims and the four quoted lines are printed with their 1-based line numbers. `## Features` is line 20, `## Installation` is line 35, its `### pip (recommended for most users)` subsection is line 37 and its `### From source` subsection is line 91.

```
$ python3 -B -c "import urllib.request as u;L=u.urlopen('https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md').read().decode().splitlines();print('sections',[(n,L[n-1]) for n in (20,35,37,91)]);print('quotes',[(n,L[n-1]) for n in (22,100,46,161)])"
sections [(20, '## Features'), (35, '## Installation'), (37, '### pip (recommended for most users)'), (91, '### From source')]
quotes [(22, '- **78+ supported formats** — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4, and many more. See the [full list](https://unblob.org/formats/).'), (100, 'Requires Python ≥ 3.10, [uv](https://docs.astral.sh/uv/), and a Rust toolchain (for the compiled extensions).'), (46, 'sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4'), (161, '  --show-external-dependencies    List required external tools and their status.')]
```

3. **Claim 3 retained — the format count is the project's own figure.** Under `## Features` (line 20), its first bullet (line 22) states `78+ supported formats — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4`. The same figure appears once more in the lede at line 5 (`78+ archive, compression, and file-system formats`). The bullet names **11** format families and ends `and many more`, so the named list is not the count and the count is not derived from the list.

```
$ python3 -B -c "import urllib.request as u;t=u.urlopen('https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md').read().decode();L=t.splitlines();fam=L[21].split('including ')[1].split(', and many more')[0].split(', ');print('named_families',len(fam));print('named_list',' '.join(fam));pk=L[45].split('apt install ')[1].split();print('apt_packages',len(pk));print('flag_occurrences',t.count('--show-external-dependencies'))"
named_families 11
named_list SquashFS JFFS2 UBI/UBIFS ext CPIO ZIP 7-Zip gzip XZ LZMA LZ4
apt_packages 11
flag_occurrences 3
```

4. **Claim 4 retained — the runtime requirement is Python with a Rust build requirement.** Under `### From source` (line 91), the subsection's last line (line 100) states `Requires Python ≥ 3.10, uv, and a Rust toolchain (for the compiled extensions)`. The document therefore declares the tool itself to be a Python program whose compiled extensions are built with Rust; it nowhere declares the tool to be written in Rust.

5. **Claim 5 retained — the external-extractor set and its verification command.** Under `### pip (recommended for most users)` (line 37), line 46 is `sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4` — **11** packages, item 3's `apt_packages`. The document offers `unblob --show-external-dependencies` as the way to verify the set: it appears 3 times (item 3's `flag_occurrences`), as the command at line 59, as `uv run unblob --show-external-dependencies` at line 97, and in the CLI reference at line 161 where it is described as `List required external tools and their status`.

6. **The offered command runs, and on this host it reports a set that is not satisfied.** The probe prints the tool's version, the report's exit status and its row counts; the exit status is **1**, the report lists **15** executables, **5** are found and **10** are missing.

```
$ python3 -B -c "import subprocess;v=subprocess.run(['unblob','--version'],capture_output=True,text=True);o=subprocess.run(['unblob','--show-external-dependencies'],capture_output=True,text=True);R=[l for l in o.stdout.splitlines() if l.startswith('    ')];print('unblob_version',v.stdout.strip());print('deps_exit',o.returncode);print('deps_rows',len(R));print('deps_found',sum(chr(0x2713) in l for l in R));print('deps_missing',sum(chr(0x2717) in l for l in R))"
unblob_version 26.6.4
deps_exit 1
deps_rows 15
deps_found 5
deps_missing 10
```

7. The 15 executable names the report requires and the 10 it did not find, printed from the same stdout:

```
$ python3 -B -c "import subprocess;o=subprocess.run(['unblob','--show-external-dependencies'],capture_output=True,text=True);R=[l.split()[0] for l in o.stdout.splitlines() if l.startswith('    ')];print('deps_names',' '.join(R));print('missing_names',' '.join(l.split()[0] for l in o.stdout.splitlines() if l.startswith('    ') and chr(0x2717) in l))"
deps_names 7z debugfs fsck.erofs jefferson lz4 lziprecover lzop partclone.restore sasquatch sasquatch-v4be simg2img ubireader_extract_files ubireader_extract_images unar zstd
missing_names fsck.erofs jefferson lziprecover lzop partclone.restore sasquatch sasquatch-v4be ubireader_extract_files ubireader_extract_images unar
```

## Inference

- The install line names **packages** and the report names **executables**; the two lists are different kinds and cannot be compared by string. Reading the report as "the README's list, verified" would be an unsupported step. What is supported is narrower: the README states an 11-package apt line, and the tool's own command states 15 required executables and their presence.
- Because line 100 requires a Rust toolchain only "for the compiled extensions", a description of unblob as a Rust implementation contradicts the project's own requirement line; the narrower statement — a Python tool with Rust compiled extensions — is what the bytes support. This is an inference about the *description*, not about the source tree, which this entry did not read.

## Unknown

- Which upstream package or Python distribution supplies `jefferson`, `partclone.restore`, `ubireader_extract_files` and `ubireader_extract_images` is **not derived here**; no package-manager query was run, and the README's apt line does not name them.
- Whether branch `main` held these bytes before or after 2026-10-25 is unknown: one fetch, no history read.
- Whether any of the stated 78+ formats is exercised by the lane's C07 fixture `corpus/fixtures/firmware-r63/firmware-r63.bin` is unknown: no extraction was run against it, and 10 of the 15 required executables are absent on this host.
- The package entry's claim 3 also supersedes two earlier figures (a Japanese OWASP FSTM translation's "30 以上" and a community "300+" figure). Neither has a row in this lane's `corpus/SOURCES.md`, so **no supersede statement is made in this entry**; only the upstream figure is claimed.

## Limitation

- One fetch of a moving branch. The digest pin in item 1 is what keeps this honest: a recheck that fetches different bytes fails the pin instead of silently re-basing the quotes. The bytes are **not** committed in this draft; landing requires `corpus/snapshots/unblob-README.md` with the printed sha256 so items 2 and 3 re-derive offline.
- The probe in items 6 and 7 ran on a tool **this entry's author installed on 2026-10-25** (`uv tool install --force unblob`, resolving `unblob==26.6.4`). The pre-existing `~/.local/bin/unblob` symlink, dated 13 October, was dangling before that install, so the probe says nothing about the host's state at any earlier date.
- The probe is a presence report, not a capability test: with 10 of 15 extractors missing, no statement is made about extraction quality, coverage or correctness on any image.
- Scope is one document and one host. Nothing here is generalized to another unblob version, another platform, or firmware formats in general.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | the load-bearing document claims rest on S048 (docs, tier A for the project's own stated figures, opened today by this seat, fetch digest item 1) and the probe on S049 (own-work, tier A for this one run, items 6-7). No tier-C row supports a claim, and no claim exceeds what the quoted line states. |
| Q02 | pass | the header carries `source:` for S048 and S049 with section and line anchors, `verified-at:` 2026-10-25, `recheck:` naming the digest pin and the probe, and `coverage-map:` naming C07. |
| Q03 | pass | the expected values are read from the fetched bytes by items 1-3, and the host figures are derived independently by running the tool's own report in items 6-7 rather than copied from the README's apt line. |
| Q04 | pass | the one tool claim names the tool, its version as the tool itself prints it (26.6.4), the function exercised (`--show-external-dependencies`) and scores its own exit 1 and its own 15 rows, 5 found and 10 missing. The install this seat performed is disclosed in the Limitation section, and no other tool is credited. |
| Q05 | pass | the capability-adjacent statement is the probe itself: command, date 2026-10-25, observed exit 1 and full output in items 6-7. No extraction capability is claimed anywhere, and the missing-extractor count is stated rather than glossed. |
| Q06 | n/a | no fixture premise exists: no fixture is built, no offset or size is stated from intent, and no producer is called. The inputs are one fetched document and one installed binary. |
| Q07 | n/a | no parser-behavior prediction is made. The package-to-executable mapping is listed under Unknown instead of being asserted as a cause. |
| Q08 | n/a | superseded by Q11 in `corpus/QUALITY.md`; the Q11 row carries the decision. |
| Q09 | pass | the fetch digest is claimed only for the bytes it hashed, and item 1 states in the same place that it establishes neither earlier branch content nor authorship. No digest is offered as origin, completeness or authenticity. |
| Q10 | pass | scope is one document at branch `main` on one date and one host probe of one version; the entry states it is not generalized to other versions, platforms or formats, and the C07 row's own scope is deepened rather than widened. |
| Q11 | pass | every number carries its command and output inside the entry: 7580 bytes, 235 lines, the digest, line numbers 20, 22, 35, 37, 46, 59, 91, 97, 100, 161, 11 named families, 11 apt packages, 3 flag occurrences, 15 report rows, 5 found, 10 missing, version 26.6.4 and exit 1. Nothing is cited only to prose. |
| Q12 | n/a | this entry writes no rejected-source row. The dropped SWGDE half and the dropped supersede framing are recorded in Scope and Unknown, not as a SOURCES row. |
| Q13 | pass | each recheck command is credited only for the lines it prints: the digest pin for the fetched bytes matching, the probe for the presence rows and exit status of that one host on that one date. No verifier is credited for a clause its own run does not detect. |
| Q14 | pass | no hex run in this entry carries a byte count in the same clause; the only hex string is the 64-hex-character fetch digest, which carries no length claim. |
| Q15 | pass | this entry states no git object id and no tree identity; branch `main` and the URL are not object ids, and the only identity stated is the fetch digest, derived in item 1. |

## Reproduce

From the lane root, items 1-3 need network access to `raw.githubusercontent.com`; items 6-7 need `unblob` on `PATH` (this host: `/home/vgpnk/.local/bin/unblob`, 26.6.4). Item 1's digest is the freshness gate for items 2-3: if it differs, the quotes must be re-located. Once `corpus/snapshots/unblob-README.md` is committed at landing, items 2 and 3 should be re-pointed to that path and stop needing the network, exactly as the APK entry reads `corpus/snapshots/ResourceTypes.h`.
