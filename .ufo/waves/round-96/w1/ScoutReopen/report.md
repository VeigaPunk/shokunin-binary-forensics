# ScoutReopen — round 96, attempt 1 — scoped findings

Seat: `ScoutReopen` (role `scout`, registry `.ufo/waves/round-96/w1/swarm-registry.json`).
Scope: re-open the frozen S502/S503 receipts and the S504 record. Read-only seat: no lane file
was created, edited or deleted; the only writes are this report and the wave-dir copy named by
the `Report:` trailer. No vote is written by this seat (the frozen vote-file shape is scoped to
ReviewerGate / ReviewerBlind / CriticR96).

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Scratch (created, used, **deleted** before yield): `/fast/scratch/hyaku/revenger-r96/ScoutReopen/`
Every Python invocation in this seat used `python3 -B`. No `__pycache__` / `.pyc` exists under
`corpus/`, `reports/round-93..96/`, `.ufo/waves/round-95..96/` (checked; empty result).
No tools were installed. No network beyond the two named raw.githubusercontent.com URLs.

---

## 0. Summary

| # | Check | Result |
|---|---|---|
| 1 | S502/S503 receipt sha256 vs committed body | **MATCH** (both) |
| 1 | S502 quote at receipt span | **EXACT MATCH** on the receipt's own offset basis (see §1.3 — the span is a *character* offset, not a byte offset) |
| 1 | S503 quote at receipt span | **EXACT MATCH** (both bases agree) |
| 2 | S502 pinned body vs installed `native-and-artifacts.md` | **DRIFTED** — 38167 B vs 18911 B; first differing byte **43** |
| 2 | S503 pinned body vs installed `SKILL.md` | **DRIFTED** — 35095 B vs 23437 B; first differing byte **152** |
| 3 | `grep -m1 evidence_id` prints `ev_cc0b9d88…282ffefe` | **MATCH** (exact) |
| 3 | Evidence `normalized_result` vs `codeable-decompiled.c` lines 6–10 | **EXACT after strip**; byte-exact only against lines **5–12** (see §3.3) |
| 3 | Four record-file digests vs entry derivation table | **ALL FOUR PREFIXES MATCH** |
| 4 | Fixture regen vs committed `fixture.exe` | **BYTE-IDENTICAL** (`cmp` rc 0) |
| + | Candidate digest re-derived from lane root | **MATCHES** `2f7d4c1b…d776d923` (3 ways) |
| + | Working-tree entry bytes == freeze-commit bytes | **IDENTICAL** |
| + | Non-author independent re-fetch of both pinned URLs | **HTTP 200, sha256 equal to committed bodies** |

No defect found that invalidates a claim. Three observations worth a reviewer's attention are
recorded in §5 — none of them falsifies a claim; they are precision notes about *how* the
receipt/derivation wording is worded.

---

## 1. S502 / S503 receipts re-opened

### 1.1 Committed body re-hash vs `fetch_sha256`

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-96/quote-receipts
$ sha256sum raw/S502.body raw/S503.body
c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24  raw/S502.body
b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc  raw/S503.body
$ wc -c raw/S502.body raw/S503.body
38167 raw/S502.body
35095 raw/S503.body
```

| sid | receipt `fetch_sha256` | recomputed | sha match | receipt `length` | body bytes | len match |
|---|---|---|---|---|---|---|
| S502 | `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24` | `c818ee34…3cc24` | **True** | 38167 | 38167 | **True** |
| S503 | `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc` | `b5f17fdf…96ccc` | **True** | 35095 | 35095 | **True** |

Both receipts also carry `http_status: 200`, `fetched_at: "2026-11-05"`, and a
`fetch_url` whose host is `raw.githubusercontent.com` (inside the frozen
`HOST_ALLOWLIST = {"raw.githubusercontent.com", "github.com"}`).
Both fetch-log lines are present and carry sid + sha256:

```
$ grep -c "S502.*c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24" …/fetch-log.md
1
$ grep -c "S503.*b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc" …/fetch-log.md
1
```

### 1.2 Quote located at the receipt's span

| sid | span | len(span) | len(quote) | bytes at span == quote bytes | decoded-text[s:e] == quote | verdict |
|---|---|---|---|---|---|---|
| S502 | 26309–26411 | 102 | 102 | **False** | **True** | EXACT (on the receipt's basis) |
| S503 | 257–389 | 132 | 132 | **True** | **True** | EXACT (both bases) |

### 1.3 S502 — the span is a CHARACTER offset; this is not a mismatch

This is the one thing a byte-level re-checker can trip over, so it is spelled out.

S502's body is **not** pure ASCII (38167 bytes decode to 38165 characters). It contains one
non-ASCII character: U+2013 EN DASH at **character index 11420** (3 UTF-8 bytes). Because that
character precedes the quote, the quote's *byte* index (26311) is 2 greater than its *character*
index (26309).

```
quote char index in decoded text : 26309
quote byte index in raw bytes    : 26311
receipt span                    : 26309..26411
EXACT char-span match (text[s:e] == quote)      : True
EXACT byte-span match (data[s:e] == quote bytes) : False
```

The receipt's span `26309..26411` is exactly the quote's **character** range, and
`text[26309:26411] == quote` holds byte-for-byte on the decoded text. The frozen verifier
`corpus/audit_source_quotes.py` reads the body with `body.decode("utf-8")` and then slices the
**string** (`text[s:e]`, `corpus/audit_source_quotes.py:103-107`), so the receipt's basis is the
basis the verifier uses. The receipt is internally correct.

Confirmation that this is the lane's established convention rather than an r96 slip — the same
char/byte divergence already exists in earlier frozen rounds, and the verifier accepts them:

| sid | round | body bytes | non-ascii bytes | char_exact | byte_exact | norm_exact | sha_ok |
|---|---|---|---|---|---|---|---|
| S496 | 93 | 35462 | 15 | False | False | True | True |
| S497 | 93 | 69577 | 145 | True | True | True | True |
| S498 | 94 | 30064 | 247 | True | **False** | True | True |
| S499 | 94 | 115812 | 9 | True | True | True | True |
| S500 | 95 | 17010 | 0 | True | True | True | True |
| S501 | 95 | 18784 | 0 | True | True | True | True |
| **S502** | **96** | **38167** | **3** | **True** | **False** | **True** | **True** |
| **S503** | **96** | **35095** | **3** | **True** | **True** | **True** | **True** |

The frozen verifier run over the committed bytes:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ PYTHONUTF8=1 python3 -B corpus/audit_source_quotes.py verify \
    --sources corpus/SOURCES.md --receipts reports/round-96/quote-receipts --sid S502 --sid S503
S502 terminal=S502 state=verified (ok)
S503 terminal=S503 state=verified (ok)
SUMMARY rows=2 verified=2 unreachable=0 unresolved=0
EXIT=0
```

### 1.4 Quote anchor sections exist in the pinned bodies

- **S502** quote (`rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source
  byte offset internally) sits at body line 425, inside the section `## DOS MZ with Ghidra`
  (body line 418). The entry's route-table row cites exactly that section. The same section also
  contains `procedure_pseudo_code` and `inspect_native_load_image` as the entry describes.
  The other cited section, `## Native targets`, exists at body line 285 and contains the
  "focused search, procedure, or function tools" and "addresses and recovered pseudocode are
  analysis observations, not original source" language the entry paraphrases.
- **S503** quote sits inside the YAML frontmatter `description:` value (body lines 1–7), which is
  what the entry claims ("frontmatter description").
- Both quotes are ≤ 25 words (S502 = 12, S503 = 17), satisfying the round's quote-length rule.

### 1.5 Independent non-author re-fetch (network to the two named URLs)

```
$ for f in "references/native-and-artifacts.md:S502" "SKILL.md:S503"; do … curl … done
S502 http=200 bytes=38167 sha=c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24
S503 http=200 bytes=35095 sha=b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc

$ cmp refetch-S502.body …/reports/round-96/quote-receipts/raw/S502.body   -> byte-identical
$ cmp refetch-S503.body …/reports/round-96/quote-receipts/raw/S503.body   -> byte-identical
```

The fetch-log's disclosed 404 probe also reproduces:

```
$ curl -o /dev/null -w "http=%{http_code}\n" \
    https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/cli-command-map.md
http=404
```

---

## 2. Installed-copy drift (pinned body vs `~/.agents/skills/reverse-engineer-anything/`)

| sid | pinned body | installed copy | pinned bytes | installed bytes | byte-identical? | first differing byte offset |
|---|---|---|---|---|---|---|
| S502 | `reports/round-96/quote-receipts/raw/S502.body` | `references/native-and-artifacts.md` | 38167 | 18911 | **No** | **43** |
| S503 | `reports/round-96/quote-receipts/raw/S503.body` | `SKILL.md` | 35095 | 23437 | **No** | **152** |

Byte context at the first divergence:

```
S502  offset 43:  pinned 0x46 ('F')   installed 0x23 ('#')
  pinned    [0:133]: b'# Native, managed, and packaged artifacts\n\nFor release comparisons, export `list_procedures` Evidence from each target before\nclosing'
  installed [0:133]: b'# Native, managed, and packaged artifacts\n\n## Go build metadata\n\nUse `inspect_go_binary` for an explicit local ELF, PE or thin Mach-O'

S503  offset 152: pinned 0x2c (',')   installed 0x2e ('.')
  pinned    [62:242]: b'…of web applications from a live instance or a capture. Use shipped-artifact or requested runtime evidence…'
  installed [62:242]: b'…of web applications from a live instance. Use shipped-artifact or requested runtime evidence…'
```

Both installed copies are the **older, shorter** 6.7.0-era checkout; the pinned bodies are the
`12f6e0974cc0db0b3a9b86246accc76556837222` revision. The drift is real and material
(19256 B and 11658 B shorter respectively).

Supporting detail for the entry's "installed 6.7.0-era" wording:

```
$ rea --version
6.7.0
$ sed -n '5,6p' ~/.agents/skills/reverse-engineer-anything/SKILL.md
  version: "42"
  tool_count: 207
```

The installed `SKILL.md` declares `metadata.version: "42"`, not `6.7.0`; `6.7.0` is the
`rea-agents` CLI release the file pins (`npx -y rea-agents@6.7.0`), and `~/.agents/skills/
reverse-engineer-anything/HOST-CONTRACT.md:41` states "REA release: `rea-agents@6.7.0`,
skill v42, 207 tools." The pinned S503 body is a **skill v49** document (`metadata: version: "49"`,
`tool_count` absent, frontmatter description ending "…from a live instance or a capture." vs the
installed "…from a live instance."). The entry's phrase "the installed 6.7.0-era skill copy" is
therefore accurate as a release descriptor and matches S002's registry row, which itself names
"setup commands naming `rea-agents@6.7.0` (lines 37-56)" — all re-derive.

Both quotes happen to still be present in the installed copies (S502's at installed byte 9103,
S503's at installed byte 154), but the pinned bytes are what the rows cite, and the entry
discloses the drift in its Unknown section. Nothing here is load-bearing for the claim: the
claim rests on the pinned revision, which is independently re-fetched and re-hashed above.

---

## 3. S504 record check

### 3.1 `evidence_id`

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ grep -m1 evidence_id corpus/live/runs/round-96/rea-decompile.raw.txt
evidence_id: ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe
EXIT=0
```

**Matches** the value named in the claims and in the entry's derivation table, exactly.

### 3.2 Record-file digests vs the entry's "record file digests" row

```
$ sha256sum corpus/live/runs/round-96/*
d717b49156faa1a627a5577a35ab7c158b103bd6adf31ee7ab5428abae3afc9d  codeable-decompiled.c
6ce217fa48a0b4426e55de550b29f6d259abbe3c89fa8dd603265708d033f0f6  ghidra-headless-r96.log
2fba7fbfc4439cacc0991e1c22e9ac74cbba526e2980ae791289cd2d1df07b41  rea-decompile.raw.txt
6a1d18c3497f3d4560c581906184aa96f6f71188ab491d9a75d937df65cdc80f  rea-doctor-r96.txt
```

| file | entry prefix | actual sha256 | prefix match |
|---|---|---|---|
| `codeable-decompiled.c` | `d717b491…` | `d717b49156faa1a627a5577a35ab7c158b103bd6adf31ee7ab5428abae3afc9d` | **True** |
| `ghidra-headless-r96.log` | `6ce217fa…` | `6ce217fa48a0b4426e55de550b29f6d259abbe3c89fa8dd603265708d033f0f6` | **True** |
| `rea-decompile.raw.txt` | `2fba7fbf…` | `2fba7fbfc4439cacc0991e1c22e9ac74cbba526e2980ae791289cd2d1df07b41` | **True** |
| `rea-doctor-r96.txt` | `6a1d18c3…` | `6a1d18c3497f3d4560c581906184aa96f6f71188ab491d9a75d937df65cdc80f` | **True** |

The derivation table's command `sha256sum corpus/live/runs/round-96/*` re-derives exactly four
files and their digests; the entry's abbreviated prefixes are the true leading 8 hex chars of
each. **All four match.**

### 3.3 Evidence `normalized_result` vs `codeable-decompiled.c` lines 6–10

The Evidence's `normalized_result` (YAML double-quoted scalar, escape-decoded) is:

```
'\nundefined8 entry(void)\n\n{\n  return 0x2a;\n}\n\n'
```

The `.c` file, with line numbers:

```
 1: program_name=fixture.exe
 2: image_base=140000000
 3: function_count=1
 4: // ==== FUNC entry @ 140001000 ====
 5: (blank)
 6: undefined8 entry(void)
 7: (blank)
 8: {
 9:   return 0x2a;
10: }
11: (blank)
12: (blank)
13: (blank)
14: // decompiled_ok=1 of 1
```

| comparison | result |
|---|---|
| `normalized_result` == lines 6–10 joined | **False** (the scalar carries a leading `\n` and trailing `\n\n`) |
| `normalized_result.strip()` == lines 6–10 joined (stripped) | **True** |
| `normalized_result` == lines **5–12** joined | **True** (exact, byte-for-byte) |

So: **the content is an exact match**; the byte-exact line range is 5–12, and 6–10 is its
interior, equal after stripping the surrounding newlines. This is explained by the producer: the
committed round-75 postScript `reports/round-75/rev75_dump.java` writes
`fh.println(res.getDecompiledFunction().getC())`, and Ghidra's `getC()` returns the function
text with a leading and trailing newline — exactly the `\n…\n\n` the Evidence scalar carries.
The two records therefore agree on the decompiled body.

### 3.4 Other derivation-table rows re-derived

| entry row | command | re-derived output | match |
|---|---|---|---|
| Evidence ID | `grep -m1 evidence_id …/rea-decompile.raw.txt` | `evidence_id: ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe` | **yes** |
| CLI provider line | `grep -A3 "^provider:" …/rea-decompile.raw.txt` | `provider:` / `id: ghidra` / `name: Ghidra` / `version: 12.1.4` | **yes** |
| headless function count | `sed -n 3p …/codeable-decompiled.c` | `function_count=1` | **yes** |
| headless entry line | `sed -n 4p …/codeable-decompiled.c` | `// ==== FUNC entry @ 140001000 ====` | **yes** |
| headless receipt | `grep -c "INFO  REPORT" …/ghidra-headless-r96.log` | `6` (lines 45, 93, 94, 98, 100, 101 — input-files, analysis, script, post-analysis, save, import) | **yes** |

### 3.5 Fixture premise and doctor receipt

- `corpus/fixtures/pe-r75-headless-smoke/fixture.exe` — 1024 bytes,
  sha256 `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72` — **matches** the
  entry's `fixture sha256` row and `truth.json`'s `sha256`.
- PE structure re-derived from the bytes: `MZ` at 0x00, `e_lfanew` = 0x80, `PE\0\0`,
  machine `0x8664` (x86_64), optional-header magic `0x20b` (PE32+), `AddressOfEntryPoint` RVA
  `0x1000`, `ImageBase` `0x140000000`, entry VA `0x140001000`, one section `.text`
  (vaddr `0x1000`, rawptr `0x200`, rawsize `0x200`), entry point file offset `0x200` with bytes
  `B82A000000C3` — **exactly** the entry's `B82A000000C3` (= `mov eax, 0x2A; ret`), matching
  `truth.json`'s `entry_bytes_hex`, `entry_file_offset: "0x200"` and
  `expected_ghidra_function: "entry @ 140001000"`.
- `rea doctor` re-run on this host: **exit 1**, `healthy: false`, `environment_healthy: false`;
  ghidra scope all healthy (`ghidra`, `ghidra-platform: linux`, `ghidra-architecture: x64`,
  `ghidra-installation`, `ghidra-version: 12.1.4`, `ghidra-headless`,
  `ghidra-native_decompiler`, `ghidra-java: 21.0.13`), `hopper` scope
  `ok: false / classification: missing_analysis_engine`. This **reproduces** the committed
  `rea-doctor-r96.txt` and the entry's statement that the doctor observed exit 1 with a healthy
  ghidra scope and an absent Hopper engine.
- The headless log records `SCRIPT: /fast/scratch/…/rev75_dump.java` and
  `REV75_DUMP wrote …: 1 functions, 1 decompiled`; the committed postScript is
  `reports/round-75/rev75_dump.java` (tracked by git), and its output format matches the
  committed `.c` file exactly (`program_name` / `image_base` / `function_count` /
  `// ==== FUNC … ====` / body / `// decompiled_ok=N of M`), consistent with the entry's
  "committed round-75 Java postScript" wording.

---

## 4. Fixture regen premise (item 4)

```
$ cd /fast/scratch/hyaku/revenger-r96/ScoutReopen
$ PYTHONUTF8=1 python3 -B \
    /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/pe-r75-headless-smoke/gen_pe_r75.py \
    /fast/scratch/hyaku/revenger-r96/ScoutReopen/regen.exe
wrote /fast/scratch/hyaku/revenger-r96/ScoutReopen/regen.exe (1024 bytes)
GEN_EXIT=0

$ cmp /fast/scratch/hyaku/revenger-r96/ScoutReopen/regen.exe \
      /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/pe-r75-headless-smoke/fixture.exe
CMP_EXIT=0

$ sha256sum regen.exe …/pe-r75-headless-smoke/fixture.exe
fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72  regen.exe
fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72  …/pe-r75-headless-smoke/fixture.exe
```

**Byte-identical** (`cmp` rc 0, identical sha256, identical 1024-byte size). The generator
re-derives its own declared premises with `assert`s before writing (machine, magic, entry RVA,
image base, `.text` VA/rawptr/rawsize, `mov eax,0x2A`, `ret`, total size), so the regen is
deterministic and self-verifying. The entry's "regen byte-identity" row re-derives exactly:
"wrote …fixture-regen.exe (1024 bytes)", then no output and exit 0.

---

## 5. Candidate digest and freeze-commit binding

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin

# (a) normalized candidate digest, per the task's stated recipe
$ PYTHONUTF8=1 python3 -B -c "import hashlib,re;t=open('corpus/knowledge/round-96-native-analysis-sessions.md',encoding='utf-8').read();n=re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t);print(hashlib.sha256(n.encode('utf-8')).hexdigest())"
2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923

# (b) working-tree bytes
$ sha256sum corpus/knowledge/round-96-native-analysis-sessions.md
2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923  corpus/knowledge/round-96-native-analysis-sessions.md

# (c) freeze-commit bytes
$ git show ff767436feed32cf2f4074f05f938f8cea98e69a:corpus/knowledge/round-96-native-analysis-sessions.md | sha256sum
2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923  -
```

All three agree with the frozen vote-binding digest
`2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`.
Working-tree bytes == freeze-commit bytes (the entry currently reads
`admission-status: candidate`, so the raw file sha and the normalized sha coincide today; the
normalization makes the digest invariant to the admission flip).

Read-only git commands only (`git show`, `git ls-files`, `git log`); no git/jj write was issued.

---

## 6. Observations for the reviewers (no claim invalidated)

These are **precision notes**, not defects. None changes a predicate, a counter, a control
receipt or a kill rule; the frozen bytes stay frozen.

**O1 — S502's `span` is a character offset, and the receipt schema does not say so.**
`S502.receipt.json` pins `span: {start: 26309, end: 26411}`, which is the quote's range in
*decoded characters*; its *byte* range is 26311–26413 because a U+2013 at character 11420 sits
before it. The frozen verifier slices decoded text, so the receipt passes — and the identical
char/byte divergence already exists in the frozen r93 S496 and r94 S498 receipts. A future
reviewer doing a naive byte slice will read this as a mismatch. Worth a one-line note in the
entry's `recheck` cell ("span is a character offset into the UTF-8-decoded body") so a later
re-checker does not misread it. Confidence: high (byte- and char-level evidence in §1.3).

**O2 — the entry's "decompiled body" derivation row cites `lines 6–10` but its recorded output
includes a marker from line 14.**
The row reads: "`corpus/live/runs/round-96/codeable-decompiled.c` lines 6–10 | `undefined8
entry(void)` … `{` … `return 0x2a;` … `}` and `// decompiled_ok=1 of 1`". Lines 6–10 are
`undefined8 entry(void)` / blank / `{` / `  return 0x2a;` / `}` — the `// decompiled_ok=1 of 1`
marker is on **line 14**. The marker value is real and present in the file; only the cited line
range is narrower than the output quoted. This is a one-cell wording nit inside the candidate
entry (which the digest binds), so it is a reviewer's/connector's call whether to note it in the
lesson; it is not a claim failure — §3.3 shows the Evidence and the `.c` file agree on the
decompiled body. Confidence: high.

**O3 — `normalized_result` matches lines 5–12 exactly, 6–10 after stripping.**
Directly parallel to O2 and worth stating so the two are not conflated: the Evidence scalar
`'\nundefined8 entry(void)\n\n{\n  return 0x2a;\n}\n\n'` equals the joined lines **5–12**
byte-for-byte and equals lines 6–10 only after `.strip()`. The producer explains it —
`rev75_dump.java` prints Ghidra's `getC()`, which carries leading/trailing newlines. So the
strict answer to "exact match against lines 6-10?" is **no at byte level, yes in content**.

**O4 — the committed headless log and the entry's regen row name `/fast/scratch/…` paths.**
`corpus/live/runs/round-96/ghidra-headless-r96.log` embeds
`/fast/scratch/hyaku/revenger-r96/l1/{ghidra-proj/rev96cap, rev75_dump.java,
codeable-decompiled.c}` (6 lines), and the entry's "regen byte-identity" row names
`/fast/scratch/hyaku/revenger-r96/l1/fixture-regen.exe`. These are *records of where the run
happened*, not hardcoded dependencies of a committed instrument — the L1's scratch is reaped
after the round, so a re-checker must substitute their own scratch path (as this seat did; the
regen re-derived byte-identically). Contrast the r94 lesson M1 / r95 lesson M1 pattern, which
was about a committed *instrument* hardcoding a reaped scratch path; no such defect appears
here. The one genuine hardcoded-scratch dependency in this round's committed instrument is
`reports/round-96/c1_k_admit_counter5.py:33`
(`SCRATCH = …/revenger-r96/c1v5`), which the counter itself provisions with
`SCRATCH.mkdir(parents=True, exist_ok=True)` before use (lines 905, 962) — the r95 M1 fix is
carried. Confidence: medium-high.

**O5 — `corpus/SOURCES.md` does not yet carry S502/S503/S504.**
The registry's newest row is S501; the three new rows are appended **at landing** by the L1
(the frozen claims' Frontier step says exactly that: "S502, S503 and S504 appended at landing").
The frozen counter's `C1_SOURCES` leg reads those rows and requires each to be `mined`, tier `A`,
opened `2026-11-05`, cite-back to the entry, and be used-by-exclusive to it — so that leg cannot
pass against the current pre-landing tree, and the counter is designed to be run against the
landing revision (`--rev <landing>`). This is expected pre-landing state, not a defect; it does
mean a reviewer must not read the counter's pre-landing verdict as the C1 predicate. The
`C1_QUOTES` leg, which is the one this seat's scope bears on, was exercised directly against
the committed bytes and passes (§1.3).

---

## 7. Bounds compliance

- Wrote only: `.ufo/waves/round-96/w1/ScoutReopen/report.md` and the wave-dir copy at
  `.ufo/waves/round-96/w1/ScoutReopen.md` (the path named by the `Report:` trailer). No lane
  file (`corpus/`, `reports/`, SCORECARD, LOG, SKILL, README, PROVINCE, QUALITY, claims) was
  created, edited or deleted; the frozen claims, the r93/r94/r95 instruments and the r96 counter
  and battery are untouched.
- Scratch `/fast/scratch/hyaku/revenger-r96/ScoutReopen/` created with `mkdir -p`, used with
  explicit absolute paths, and **deleted** before this yield. No committed file hardcodes `/tmp`;
  the only `/tmp` mention in this seat's output is quoted from a frozen r91 lesson.
- Every Python invocation used `python3 -B`. Verified after the fact: no `__pycache__` or
  `.pyc` under `corpus/`, `reports/round-93..96/`, `.ufo/waves/round-95..96/`.
- Git: read-only (`git show`, `git ls-files`, `git log`) — no write command in this lane or
  anywhere. Fleet root, sibling lanes, `.ufo/state`, `.ufo/watchdog.log` and
  `/home/vgpnk/Projects/shokuknow` untouched. One stray scratch script accidentally written to
  the fleet root early in the seat was deleted immediately (`rm -f
  /home/vgpnk/Projects/shokunin/revanger_tmp.py`); the fleet root listing was re-checked and
  shows no new file. Disclosed for the sentinel's audit.
- Network limited to the two named `raw.githubusercontent.com/morluto/rea` URLs (plus the
  disclosed 404 probe on the same host/path family named in the fetch log). No other network.
- No subagent dispatched (leaf member; no spawns). No `agent://all`.
- Nothing installed; no sudo; no sysctl mutation.

## 8. Confidence and remaining unknowns

**High confidence:** receipt↔body sha256 equality for S502 and S503; quote location and exactness
at the receipt spans (S502 on the character basis the frozen verifier uses); the four
record-file digests; the `evidence_id`; the fixture sha256, PE structure, entry bytes and
byte-identical regen; the candidate digest and the working-tree/freeze-commit byte equality;
the independent re-fetch equality of both pinned bodies.

**Medium confidence / explicitly unresolved:** the exact line range a future re-checker should
cite for the decompiled body (5–12 byte-exact vs 6–10 stripped — O3); whether the reviewer
wants the char-vs-byte span basis stated in the entry's `recheck` cell (O1) and the derivation
row's line range corrected (O2). Both are wording-level and inside the candidate entry the
digest binds, so they are the L1's/reviewers' call, not this seat's — this seat does not edit
lane files.

**Not verifiable from committed bytes:** the doctor receipt's own `exit 1` was re-observed by
re-running `rea doctor` on this host (rc 1, healthy: false, ghidra scope healthy, hopper
missing) rather than being read out of the receipt, which records content, not the exit status.
The Ghidra-headless session was likewise not re-run here (it would need the reaped scratch tree
and an hours-scale analyzeHeadless invocation); its evidence is the committed log's six
`INFO  REPORT` lines plus the byte-exact agreement between the postScript's output format and
the committed `.c` file. Whether the Evidence ID is stable across re-runs remains open, as the
entry itself records.
