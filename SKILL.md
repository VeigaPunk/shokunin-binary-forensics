# SKILL — revenger saved-ledger evidence craft

Headers (QUALITY.md Q02 shape, applied to this instruction file):

- `source:` `corpus/QUALITY.md` Q01–Q13; `corpus/SOURCES.md` (contract v1); `corpus/README.md` coverage legend; `corpus/lessons/round-63.md` M33–M35; `corpus/lessons/round-66.md` M37–M41; `reports/round-66/claims.md` (C6 fix shape, adjudication order).
- `verified-at:` 2026-10-24, re-read in the lane tree at the round-66 adjudication commit (the round-64-era split below is preserved history): `corpus/`, `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md` at lane commit `666ea84b6be2eec2b0359f556ba2429fc9044c36` (round-64 claim base); `reports/round-64/claims.md`, `measure.py`, `measure-before.log` at `3bb430f96cac09feb7269c5c52725127c6f7c463`; the round-64 control line ranges in §1 at the uncommitted working tree on top of `a3d063f29b93ad1f0b7eab78652c552685b84d89`; the round-65/66 control line ranges and the round-66 instrument were re-read at the round-66 working tree (C5/C6 controls committed). Every cited path, line range and S-id was re-read in that split, in the lane tree and at the named fleet contract path.
- `§9 added:` 2026-10-27 in the interactive dispatch; §9's own pointer is verified by
  `corpus/training/bounty-triage/check_package.py --self-test` (26/26 detectors, clean
  control) and the two exercise runs recorded in `corpus/lessons/2026-10-27-bounty-triage-module.md`.
  The rest of this file's provenance split is unchanged.
- `recheck:` the frozen probe by absolute lane path with `cwd=/` and lane-owned `TMPDIR` (§6.1); the seven census commands in §6.2 from the lane root; the replay commands in §6.4.
- `box:` `SHONEN.md` box 1 — real decision tables (§1–§3), error patterns (§4), checklists (§6), cited sources (§7).

## Scope — what this SKILL governs

This is process instruction, not a knowledge entry: it fills no coverage-map row and
carries no Evidence ID. It governs four narrow acts in this lane:

1. drafting or reviewing an entry under `corpus/knowledge/` from authored bytes plus a
   saved REA record;
2. guarding a saved-ledger replay verifier in the lane's `corpus/` verifier family
   (`verify_icon_states.py`, `verify_multi_icon_states.py`, `verify_icon_languages.py`,
   `verify_named_multi_icon_states.py`, and their siblings) against deletion;
3. reading the round's frozen counting probe without mistaking it for the gate;
4. running the authorized bounty-triage exercise through §9 without mistaking its
   validator for an admission gate.

Named limits (`PROVINCE.md`, `corpus/README.md` "Known gaps", `SCORECARD.md` "Rubric
boundaries"):

- **No producer or readiness claim.** A configured value, an install or an older probe
  is not capability (Q05). Producer readiness lives in `corpus/README.md` "Frontier".
- **No origin, completeness or authenticity.** A digest or receipt is claimed only for
  the exact bytes it hashed (Q09; S005, S006, S015).
- **No generalization.** A finding is scoped to the observed family, operation, version
  and input (Q10). One authored fixture never supports a general format claim.
- **Registry is the only admission instrument.** §Gate registry below registers exactly one
  committed gate (`check_embedded_outputs`, kind `gate`); the ten `verify_*.py` scripts and every
  other self-test are replay evidence, not admission, and a green `--self-test` is not a verdict
  (`corpus/README.md` "Known gaps"; `SCORECARD.md` rubric boundaries). This SKILL is checklist work
  and claims no new capability.
- **Manual stays labeled manual.** A byte readout done by hand is labeled manual and is
  not credited to a tool (Q04, Q11).

## 1. Decision table — what a `receipt_ok` conjunct may be credited for

Use before writing any sentence that credits a verifier (Q13). Read each row against the
named file; the line ranges are the ones re-read at the header's provenance split, with the
round-64 controls read in the uncommitted working tree on top of `a3d063f2`.

| script | `receipt_ok` conjuncts (file:line) | in-script forged controls present (file:line → attribution text) | guarded conjuncts | unguarded — name, do not credit |
|---|---|---|---|---|
| `corpus/verify_icon_languages.py` | `command==command`, `exit_code==0`, `fixture_sha256==expected_hash`, `evidence_id==evidence_id`, `stdout_sha256==H(raw_bytes)` (:118-120) | forged `command` :149-151 → `forged receipt command accepted`; forged `stdout_sha256` :152-154 → `forged receipt stdout accepted`; forged `evidence_id` :155-157 → `forged receipt evidence accepted`; forged `exit_code` :158-160 → `forged receipt exit accepted`; forged `fixture_sha256` :161-163 → `forged receipt fixture accepted` | `command`, `stdout_sha256`, `evidence_id`, `exit_code`, `fixture_sha256` | — (all five guarded at the round-66 tree) |
| `corpus/verify_multi_icon_states.py` | same five conjuncts (:121-123) | forged `command` :148-150 → `forged receipt command accepted`; forged `stdout_sha256` :151-153 → `forged receipt stdout accepted`; forged `evidence_id` :154-156 → `forged receipt evidence accepted`; forged `exit_code` :157-159 → `forged receipt exit accepted`; forged `fixture_sha256` :160-162 → `forged receipt fixture accepted` | `command`, `stdout_sha256`, `evidence_id`, `exit_code`, `fixture_sha256` | — (all five guarded at the round-66 tree) |
| `corpus/verify_icon_states.py` | `exit_code==0`, `fixture_sha256==expected_hash`, `stdout_sha256` (or `raw_output_sha256`)`==sha(raw_bytes)`, `evidence_id==evidence_id` (skipped when `round_id==36`) (:119-123) | forged `fixture_sha256` :151-158 → `forged receipt accepted` | `fixture_sha256` | `exit_code`, `stdout_sha256`, `evidence_id` |
| `corpus/verify_named_multi_icon_states.py` | `command`, `exit_code`, `fixture_sha256`, `evidence_id`, `stdout_sha256`, `duration_seconds` numeric and `>=0` (:16-17) | forged `command` :76-78 → `forged receipt accepted` | `command` | `exit_code`, `fixture_sha256`, `evidence_id`, `stdout_sha256`, `duration_seconds` |

Rules that make the table usable:

- **Credit only the guarded column.** Q13 lets you credit a verifier for a clause only
  when its own run is shown to detect that clause's deletion. List the rest as
  "unguarded" in the entry instead of counting them (M35).
- **Attribution is exact.** A mutant kill counts only if the mutant run exits non-zero
  **and** its last output line ends with the registered phrase (`reports/round-64/claims.md`
  §C2, e.g. endswith `forged receipt stdout accepted`). A crash or an unrelated assertion
  is not attributed.
- **Adding a control** follows the frozen shape: deep-copy the valid receipt, forge one
  field, `require(not receipt_ok(...), f'r{r}: forged receipt <field> accepted')`,
  **appended after the last existing control** in `check()` (round-65 C5 and round-66
  C6 both append; inserting between controls renumbers this table's `file:line`
  column). Do not edit `receipt_ok` itself.
- **Status at this draft.** C4 is earned — `reports/round-65/measure-before.log`
  prints `C4_RECEIPT_KILLED_ATTRIBUTED=2/2` at that base. C5 is earned —
  `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` attributed at the round-65 tip
  (`reports/round-65/measure-after.log`). C6 is the round-66 claim:
  `reports/round-66/measure-before.log` prints `C6_RECEIPT_KILLED_ATTRIBUTED=0/4`
  at base `8214e4dd` (deleting `exit_code` or `fixture_sha256` left both self-tests
  green); credit is earned only by the frozen counter printing `4/4` at the
  round-66 landing commit.

## 2. Decision table — authoring a known-truth fixture (Q06, M33)

Precedent: `corpus/fixtures/firmware-r63/generator.py` plus its `truth.json`.

| step | do | never | where it is shown |
|---|---|---|---|
| declare | members by `offset` + `payload` bytes only; fixed `IMAGE_SIZE`; one declared `PADDING_BYTE` | declare region sizes, compressed sizes or digests by intent | `generator.py:17-35` |
| build | compress each payload, write into the zero-filled image, then take `image = bytes(image)` | edit the finished `.bin` by hand | `generator.py:104-113` |
| measure members | decompress with `decompressobj`; require `decoder.eof`; `member_size = len(image) - offset - len(decoder.unused_data)`; reject empty | trust the compressed length you intended | `decode_member`, `generator.py:39-49` |
| measure regions | walk offsets in order; reject overlap; verify every padding span equals the declared fill byte; require the region table to sum to the image size | leave any byte uncovered by the table | `derive_regions`, `generator.py:52-101` |
| record truth | `truth.json` shape: `image{path,sha256,size}`; `regions[]` = padding `{offset,size,kind,fill_hex}` or zlib `{offset,size,kind,name,decompressed_member{sha256,size}}`; `build_recipe{command,image_size,padding_byte_hex,compression{format,implementation,level,compile_version,runtime_version},python_version,determinism,members[{name,offset,payload_utf8}]}` | omit the recipe or the runtime versions that make regeneration reproducible | `truth.json` (73 lines) |
| reproduce | copy the fixture directory into `/tmp/revenger-r64-*` and run the recorded recipe there (`python3 -B generator.py`), then byte-compare image and truth against the committed originals; record the interpreter and zlib versions the recipe embeds | run the generator inside `corpus/fixtures/`: it rewrites `firmware-r63.bin` and `truth.json` in place (`generator.py:149-150`), and `truth.json` embeds `zlib.ZLIB_RUNTIME_VERSION` (:131) and `platform.python_version()` (:133), so a different interpreter changes the truth even with identical payloads — a changed fixture byte voids the round (`reports/round-64/claims.md` §Harms) | `truth.json` `build_recipe.command`; `generator.py:131,133,149-150` |
| pre-probe | before any producer call, test the fixture premise against the tool's **own signature list** and record the probe command, date, exit and output | assume a format name implies detectability | M33 (`round-63.md:218`) |
| byte-verify | after every fixture edit and before the producer call, re-derive offsets, sizes and digests from the built bytes; retain failed inputs | state an offset or count from intent | Q06 |

Second precedent (container fixtures, round-65): `corpus/fixtures/apk-r65/` —
a ZIP container whose `truth.json` is a container schema, not the zlib schema
above: `image{path,sha256,size}`; `members[]` with
`local_header_offset`/`compressed_size`/`uncompressed_size`/`crc32`/`method`/`sha256`;
`axml_declared{strings,attributes,resource_ids}`;
`build_recipe{command,container,members,python_version,determinism}`. Node
`size` fields include `headerSize` — the M38 defect was a `16 + len(payload)`
chunk size against an 8-byte node header. The same scratch-only rule applies:
`generator.py` writes `fixture.apk` (:197) and `truth.json` (:226) in place
and the truth embeds `platform.python_version()`; regenerate only under `/tmp`.

M33's concrete lesson: the zero-finding image and the positive control differed before
the producer call, and the positive control needed binwalk's `--search-all`. Probe first,
then record whichever way it falls (Q07).

## 3. Decision table — `corpus/SOURCES.md` rows and tiers

Contract: fleet root `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
(read-only, outside this lane and not lane-relative), restated for this lane by
`corpus/SOURCES.md`.

| tier | means | may be sole support? |
|---|---|---|
| A | primary or authoritative **for that row's `scope`**: spec, official docs, source code, original paper, maintainer statement, the lane's own re-runnable gate output | yes, inside `scope` |
| B | strong secondary with reproducible detail (expert write-up, survey, textbook) | **never** sole support for a load-bearing claim — corroboration beside a tier-A row only; Q01 requires a tier-A row for the claim's own scope |
| C | lead only | never (Q01); `community` is never A |

| rule | check |
|---|---|
| one row = one claim, opened in the round that writes it; lesson `## Gate` records URL, access date and a ≤25-word quote with location | Q01, SOURCES rule 1 |
| append-only; only `status`, `recheck`, `used-by` change in place, each change logged old→new in the round lesson; a correction is a new row whose `teaches` opens `supersedes S0NN —` | SOURCES rule 2 |
| `scope` bounds the tier; `anchor` is an exact section, page or line plus revision, never a bare homepage | Q02, SOURCES shape |
| rejected rows stay and read `REJECTED: <reason>; flip: <what would change the verdict>`, with the reject reason grounded in a located quote | Q12 (M21) |
| no credential material, session/private URLs or `op://` references | SOURCES rule 6 |
| the census in §6.2 prints `0` malformed rows, nothing for duplicates/enum/missing paths | SOURCES §Census |

## 4. Error patterns M33–M41 → the check that catches each

| id | class | what it looks like | check that catches it | source |
|---|---|---|---|---|
| M33 | stale premise | fixture detectability assumed from the format's name; producer call aimed at regions the tool never reports | Q05 (probe command, date, exit, output before the call) + Q06 (premise byte-verified) + the signature-scan pre-probe in §2 | `corpus/lessons/round-63.md:218` |
| M34 | counter substitution | flipping a README status cell or planting a shaped JSON satisfies the probe's printed labels without the claimed work | admission needs named Q01–Q13 decisions from non-author seats; `K_HELD_BACKED_STRICT`; count only a committed archive; the counter never flips README | `corpus/lessons/round-63.md:219`, `reports/round-64/claims.md` §Counting |
| M35 | residual unguarded clause | a receipt conjunct with no in-script forgery survives deletion; the self-test stays green | §1 table + Q13 credit rule + attributed-endswith measurement; add one control per conjunct you intend to credit | `corpus/lessons/round-63.md:220`, `reports/round-64/claims.md` §C2 |
| M36 | self-assessment drift | coverage-map token says `frontier` while a saved record already exists for that row's own surface operations | `README_TOKEN_LEGEND_MISMATCH` against the frozen `ROW_OPS` map; must print `0` at round end; at base it prints `1 rows=['C07']` | `reports/round-64/claims.md` §C1/§Frontier, `reports/round-64/measure-before.log` |
| M37 | stale premise (counter window) | a rejected-marker scan reads only `[:2000]` of an entry, so a marker past the window prints a clean STRICT count | whole-file scan + `STRICT_REJECT_WINDOW_SELFTEST` (seeded marker at byte 3000; the old window must miss it) | `reports/round-65/claims.md` §Registered, `corpus/lessons/round-65.md:30` |
| M38 | number-drift (layout from intent) | chunk `size` or struct width computed from intended layout (headerSize double-counted) instead of the built bytes | §2 byte-verify + derive constants from the spec's field lists; the red-before log shows the desynced walk dying `StopIteration` | `corpus/lessons/round-65.md:29`, `.ufo/waves/round-65/m38-red-before.log` |
| M39 | number-drift (quoted output transcribed) | a pasted command-output line differs from what the named command prints — here a dropped hex pair (`4d616e696673742d…` vs `4d616e69666573742d…`) | Q11 verbatim check: re-run the deriving command and diff every embedded output line (R65ReviewEntryQ02's proposed verbatim-diff gate is routed debt) | `corpus/lessons/round-66.md` `## Mistakes`, `.ufo/waves/round-65/R65ReviewEntryQ11.md` |
| M40 | number-drift/anchor (located-quote pointer from intent) | a Gate quote is verbatim but its line/span/word-count pointer is wrong (`lines 608-611` for 607-609; `line 5` for 7-8; `16 words` for 14) | the round-lesson located-quote rule at wave review; corrections land as superseding rows (SOURCES rule 2) — never in-place row edits | `corpus/lessons/round-66.md` `## Mistakes`, `corpus/SOURCES.md` S043/S044 |
| M41 | attribution (count from a draft) | a report's seat-role count sums to one less than the committed spec (63 vs 64) | reconcile the report's mix line against `wave-spec.json` role counts at closure | `corpus/lessons/round-66.md` `## Mistakes` |

The legend that M36 violated, from `corpus/README.md`: `held` = at least one admitted
entry; `partial` = only unsourced or pre-contract text; `uncovered` = work evidence but
no admitted entry; `frontier` = **no knowledge and no saved record**.

## 5. Admission checklist — Q01–Q16 (QUALITY.md; rows Q14–Q16 added round 70, the table had stopped at Q13)

| id | demands | reject when |
|---|---|---|
| Q01 | each load-bearing claim rests on a SOURCES row tier-A for that claim's scope, opened the round it was written | the claim exceeds what the cited text states; tier C is sole support |
| Q02 | header `source:` (S-id, URL or path, exact anchor), `verified-at:`, `recheck:`, and the coverage-map row named | any header missing, or the anchor is a bare homepage |
| Q03 | expected values derived independently — from bytes, a spec, or a pin fixed outside the record under test | the expected value is copied from the record checked, or one saved path is both identity and locator |
| Q04 | tool claim names tool, version, function and scores the tool's own explicit output; manual analysis labeled manual | credit for output the tool did not produce; one version/function generalized to the product |
| Q05 | readiness/capability claim carries a probe of the real surface with command, date, observed exit/output or Evidence ID | the claim rests on a configured value, an install or an unrechecked older probe |
| Q06 | fixture premises byte-verified against the built fixture after every edit and before any producer call; failed inputs retained | an offset, size or count stated from intent |
| Q07 | predicted parser behavior is a pre-registered hypothesis with spec-derived ground truth, recorded either way; a cause only after independent reproduction | prediction written as fact; unreproduced cause used as support |
| Q09 | digest/receipt claimed only for the exact bytes hashed; saved records stay byte-preserved; no origin/completeness/authenticity | a hash match offered as proof of origin, completeness or a valid interpretation |
| Q10 | finding scoped to observed family, operation, version, input; contested cross-lane scope reported, not absorbed | one family's observation stated as universal |
| Q11 | **supersedes Q08** — every count, identifier, offset and digest carries, inside the entry, the command that derives it from the primary record and that output; constants derived, not assumed; prose-only values labeled recorded | correct value with no derivation in the entry, or a recorded value presented as re-derived |
| Q12 | a rejected source row states a reject reason grounded in a located quote and a `flip` naming a source change or a scope the reason does not exclude | the flip asks for content the row already credits |
| Q13 | a verifier/recheck command is credited only for clauses whose deletion its own run detects; other clauses named unguarded | an entry cites a verifier for a value whose check survives deletion |
| Q14 | a hex string quoted with a byte count in the same clause carries 2 × N hex characters; an ellipsis-truncated run carries no length; an `ASCII` rendering decodes from that same run | a quoted hex string's stated length or rendering is not the bytes it quotes |
| Q15 | a stated git object id or tree identity is re-derived with the command that names it | an identity sentence is asserted without the deriving command, or the named object resolves to a different value |
| Q16 | a sentence crediting a script, table or command with covering a set is true only for the members its own printed output compares (the rest named unguarded), and a sentence saying what a command prints is checked against its stdout | a credit or output description reaches past what the command prints (round-70 entry `:119`, `:152`, `:282`) |

Q08 is historical (superseded by Q11); applying it instead of Q11 is a Q11 failure.
Procedure (QUALITY.md "Admission procedure"): apply every criterion, marking `n/a` only
with the reason it cannot apply; admit only when none fails and record the decision in
the round lesson's `## Gate`; each entry separates observation, inference and unknown and
names at least one limitation.

## 6. Checklists

### 6.1 Frozen counter usage

The counter is a measurement instrument, not the gate (M34).

- Count only a **committed** tree: `git archive <commit> corpus` extracted under
  `/tmp/revenger-r66-*`; never the live working tree.
- Run with `cwd=/` and absolute paths, as the contract requires
  (`reports/round-66/claims.md` §Frozen counter): from `/`,
  `TMPDIR=/tmp/revenger-r66-counter-XXXX python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-66/measure.py /tmp/revenger-r66-counter-XXXX`,
  with `<TREE>/corpus` present and `TMPDIR` under the same lane-owned scratch. A
  lane-root invocation is not the registered measurement; do not describe it as one.
- Read these labels: `K_HELD`, `K_HELD_BACKED`, `K_ROW C05` (the round-66
  disposition readout — `frontier` at base, `uncovered` after adjudication),
  `K_ROW C07`, `K_HELD_BACKED_STRICT` (must equal `K_HELD_BACKED` at both ends
  unless the discrepancy is reported), `C05_REJECTED_MARKED`,
  `README_TOKEN_LEGEND_MISMATCH` (0 at the round-66 base; `1` at the round-64
  base — the M36 fix landed), `F_COVERAGE`/`F_FAMILIES`,
  `C2_*`, `C3_*`, `C4_*`, `C5_*`, `C6_*`, `C7_*` (`C7_GATE_PRESENT`,
  `C7_SELFTEST`, `C7_CONTROL_PASS`, `C7_MUTANT_KILLED`,
  `C7_MUTANT_KILLED_ATTRIBUTED`, `C7_NEG_SPOOF_KILLED`,
  `C7_NEG_SPOOF_KILLED_ATTRIBUTED`, `C7_RED_ON_R65_CANDIDATE`, `C7_V2_CLEAN`,
  `C7_V3_CLEAN`),
  `STRICT_REJECT_WINDOW_SELFTEST`, `FRESH_ROWS`, `HOLDS_OK`, `HOLDS_OK_V2`,
  `HOLDS_OK_V3`, `HOLDS_OK_V4`, `HOLDS_OK_V5`, `HOLDS_OK_V6`.
- Exit codes (the script's own tail): `0` = `HOLDS_OK` yes, `1` = holds not met,
  `2` = could not evaluate. `HOLDS_OK_V2` substitutes the attributed counts and
  also requires `README_TOKEN_LEGEND_MISMATCH == 0`; `HOLDS_OK_V3` = V2 ∧ C5
  attributed 2/2 ∧ window selftest pass; `HOLDS_OK_V4` = V3 ∧ C6 attributed
  4/4; `HOLDS_OK_V5` = V4 ∧ every `C7_*` target (including the attributed kill
  and the negative spoof pair); `HOLDS_OK_V6` = V5 ∧ the C7 negative control ∧
  `C7_V3_CLEAN`. **Coupling to declare when reading V6:** it folds in the
  round-68 C05 candidate's verdict, so a C2 artifact defect can force V6 `no`
  even when the gate itself is sound (seat `R68CriticSeparability`; the
  round-68 claims' "neither counter reads the other's artifact" is false in
  both directions — routed). The V-labels are diagnostics, **not** folded into
  the exit code — read them explicitly.
- Red-before is part of the instruction: `reports/round-66/measure-before.log`
  shows a do-nothing base meeting no target (`K_HELD 8/14`, `K_ROW C05
  status=frontier`, `C05_REJECTED_MARKED=no`, `C6_* 0/4`,
  `README_TOKEN_LEGEND_MISMATCH=0`, `HOLDS_OK_V4=no`, probe exit 0).

### 6.2 Seven census commands (verbatim; run from the lane root)

```sh
# rows (spacing-tolerant)
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# status histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# duplicate ids — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# enum violations and tier inflation — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
# mined rows whose used-by paths do not exist — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

### 6.3 Admission order (claims.md)

1. Land candidates with **no** README status flip.
2. Run fresh in-wave attacks; each Q01–Q13 decision comes from a named seat that is not
   the author/corrector; blind independence (Q03) means at least one seat derives the
   expected layout without the author's readout script.
3. Adjudicate; flip the affected coverage-map row only on an all-criteria pass. If the
   claim falsifies, report it honestly and do not re-target; the contract's fallback
   flip applies instead.
4. A calibration claim requires red-before below target and the attributed count at
   target at the final measured commit.
5. Only the coverage row named in the contract may change; the denominator and
   Q01–Q13 stay fixed.

### 6.4 Replay and regeneration commands

- Per verifier: `python3 -B corpus/verify_icon_languages.py --self-test` (same shape for
  `verify_multi_icon_states.py`, `verify_icon_states.py`,
  `verify_named_multi_icon_states.py`); exit 0 is required for the calibration hold.
- Census C (`SCORECARD.md`) runs all ten verifiers from the corpus tree and prints every
  exit code; **the census probe exits 0 even when constituent verifiers fail — inspect
  each printed exit**.
- Fixture regeneration is **scratch-only**: `cp -a corpus/fixtures/firmware-r63 /tmp/revenger-r64-fixture && (cd /tmp/revenger-r64-fixture && python3 -B generator.py)`, then byte-compare both files with the committed originals. Never run the generator in place — `generator.py:149-150` overwrites the frozen image and truth, and the round's void conditions reject any changed `corpus/fixtures` byte. The recipe embeds `python_version` (:133) and zlib versions (:131), so a different interpreter changes the truth even when payloads match. The same rule binds `corpus/fixtures/apk-r65/generator.py` (:197 writes `fixture.apk`, :226 writes `truth.json`, the truth embeds `platform.python_version()`): `cp -a corpus/fixtures/apk-r65 /tmp/revenger-r66-apk && (cd /tmp/revenger-r66-apk && python3 -B generator.py)`, then byte-compare `fixture.apk` and `truth.json` against the committed pair.
- Verify cited paths still exist before citing: every path in §7 resolves in the lane tree at the header's provenance split.

### 6.5 Round-close gate (void conditions)

The current round's own claims.md governs; round-66 has no §Harms section — its
analogues are §Frozen counter and §Registered work.

Any of these voids the round: changed `corpus/live` or `corpus/fixtures` byte
outside the current round's registered new paths (round-66 registers none
under `corpus/live`/`corpus/fixtures`; round-65's registered fixture was
`corpus/fixtures/apk-r65/`); a lost baseline held row; a README status change
other than the named row (round-66: C05 only, either-way flip); a changed
denominator; weakened Q01–Q13; attributed calibration counts below target
(`C2_RECEIPT_B_KILLED_ATTRIBUTED` 2/2 **and** `C2_D2_KILLED` 2/2, C3 2/2,
C4 2/2, C5 2/2, C6 4/4 after landing); `HOLD_CALIBRATION` < 4/4;
`HOLD_REPLAY` < 10/10; `STRICT_REJECT_WINDOW_SELFTEST` not `pass`;
`HOLDS_OK_V4` not `yes`; probe exit non-zero at final. Prior rejected
candidates, counterexamples and round-63/65 evidence stay byte-preserved —
a rejected candidate keeps every byte except its `admission-status:` line.

## Gate registry (registry home; PROTOCOL.md §Gate standard)

| field | value |
|---|---|
| name | `check_embedded_outputs` |
| kind | gate (committed, re-runnable verdict script this lane owns) |
| entry command | `python3 -B corpus/check_embedded_outputs.py --entry <knowledge.md>` (cwd = lane root) |
| verdict map | `0` clean (≥1 block checked, every embedded output line verbatim) · `1` failed (an embedded line absent from its command's stdout, or a declared command exits non-zero) · `2` could-not-evaluate (no `$ cmd` blocks, unsupported command, unreadable/missing entry, or declared command times out after 120s; each prints the applicable `could-not-evaluate:` reason) · `64` usage (no arguments or an unrecognised form; PROTOCOL §Gate standard requires it declared) |
| self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` (spelling `--self-test`; hermetic temp trees; asserts clean+full-run exit 0 and that the drifted case is caught). **Rewritten 2026-10-25 from the after-run (r68 adjudication, repair D2/M46):** the drifted case is an `if not caught:` branch (`corpus/check_embedded_outputs.py:140-146`) that prints `self-test: drifted entry not caught`, then the marker `drifted entry output accepted` **as the last line**, then exits 1 — so the frozen mutant (the verbatim comparison removed) is killed *and attributed*: measured `C7_MUTANT_KILLED_ATTRIBUTED=1/1` against `0/1` at base. The negative control (same mutant plus `MARKER = "…(spoofed)"`) is killed but **not** attributed (`C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`), so the attribution rule cannot be satisfied by any non-zero exit. **Named limitation, not closed:** the drift fixture quotes a single line, so a *weakened* comparison (`drift(lines[:1], …)`) still passes the self-test (seat `R68CriticC7Surface`); a two-line partial-drift fixture is routed |
| pinned-value path | red snapshot `corpus/knowledge/round-65-apk-axml-byte-evidence.md` sha256 `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a` — expected verdict over these committed bytes: exit 1 naming entry:41 (the M39 drift); the bytes are the round-66-tip bytes, unchanged since. **Pin status: `unpinned (legacy)`** — the gate holds no digest of this file, so an edited snapshot reads as a compared verdict instead of `snapshot_tampered` (seat `R68ReviewSkillRegistry`; in-gate verification is routed, not claimed) |
| measured-against | round-68 frozen counter `reports/round-68/measure.py` labels `C7_*` (sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`, pinned in `reports/round-68/claims.md`): `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`, `HOLDS_OK_V5=yes`, `HOLDS_OK_V6=yes` (`reports/round-68/measure-after.log`) |
| write scope | read-only over the lane tree; runs the entry's declared commands (argv list, no shell, `python3` first token only); writes nothing outside its own temp dirs |
| owner | revenger |
| family note | deliberately OUTSIDE the `verify_*.py` replay family: the ten-verifier census and `HOLD_REPLAY=10/10` denominator are frozen and this gate does not join them (claims.md §C2) |
| pin rule (round 70) | an entry named in `corpus/embedded_output_pins.json` re-derives each pinned script argument against a digest-pinned earlier revision of that script (`corpus/derive_axml_anchors_r68.py`, sha256 `bce497d6…`, the S046 row's digest), verified by sha256 before use; a mismatch is a finding whose text is `pinned historical script digest mismatch` (exit 1). The registered comparison line (`problems += drift(lines, stdout_set, lineno)`) is unchanged. Credited for: the round-68 retained candidate's embedded block re-deriving (`EMB_R68` problems 7 → 0 under `reports/round-70/measure.py`); NOT credited for any entry not named in the pin file, and a pin does not make an old script current |
| round-71 exit-2 legs | Self-test covers missing entry and timeout with hermetic fixtures (timeout injected as 1s in self-test); the live CLI returns exit 2 with `could-not-evaluate: entry not found:` or `could-not-evaluate: command timed out after 120s:` and no traceback. Counter labels: `C2_MISSING_ENTRY_EXIT2`, `C2_TIMEOUT_EXIT2`; round-71 claims/counter in `reports/round-71/`. |

| field | value |
|---|---|
| name | `self_assessment_check` |
| kind | gate (committed, re-runnable verdict script this lane owns; round 70 C2) |
| entry command | `python3 -B corpus/self_assessment_check.py --root <tree> [--lane <repo>]` where `<tree>` holds `corpus/`, `SHONEN.md`, `SCORECARD.md`, `SKILL.md` (a `git archive` extraction, or the lane root) |
| verdict map | `0` `SELF_MISMATCH=0` · `1` at least one of SM1-SM6 non-zero (each class is printed) · `2` could-not-evaluate (a required file is missing) · `64` usage |
| self-test | `python3 -B corpus/self_assessment_check.py --self-test` — clean synthetic tree scores 0, one planted defect per class scores exactly that class, an appended `erratum: \`bad\` -> \`good\`` line excuses SM5 only when `good` resolves, an empty root is not evaluable. Attributed by the frozen counter's own independent fixtures (`SELF_MUTANTS_KILLED=6/6`, `reports/round-70/measure.py`), not only by its own self-test |
| what a green run does NOT establish | that the self-assessment is true beyond the six named classes; SM5 recognises a hash only after `pre-registration`, `base`, `tip` or `commit`; SM3 recognises `N bytes` / `sha256 \`hex\`` quoted in a SHONEN box for a file the box names in backticks |
| write scope | read-only over TREE; runs `git cat-file -e` in the lane repo; writes nothing outside its own temp dirs |
| owner | revenger |

| field | value |
|---|---|
| name | `lint_entry` |
| kind | pre-flight lint (NOT a gate: a clean lint never substitutes a Q decision; round 70 C1) |
| entry command | `python3 -B corpus/lint_entry.py --entry <knowledge.md> [--lane <repo>]` |
| verdict map | `0` every count 0 · `1` findings (`LINT_QMAP`, `LINT_Q14`, `LINT_Q15`, `LINT_HEADER` each printed with line numbers) · `2` unreadable · `64` usage |
| self-test | `python3 -B corpus/lint_entry.py --self-test` — clean entry 0, one planted defect per class scores exactly that class, an ellipsis-truncated run carrying a count is flagged |
| what a clean run does NOT establish | Q14 is a one-hex-run-one-count-per-clause heuristic (digest lengths 40/64/128 and odd lengths excluded; counts above 32 ignored); Q15 sees only a token introduced by `commit`, `base`, `tip`, `since` or `at`; QMAP checks row presence and a non-empty decision cell, not that the basis is true |
| write scope | read-only; reads the entry, `corpus/QUALITY.md`, and runs `git cat-file -e` |
| owner | revenger |

## 7. Cited sources — existence-checked

| citation | exists at | credited for |
|---|---|---|
| S005 | `corpus/SOURCES.md` (SWGDE acquisition best practices) | verification scope; a hash comparison may not cover all source data (Q09) |
| S006 | `corpus/SOURCES.md` (FIPS PUB 180-4) | what a digest computes, not provenance (Q09) |
| S007 | `corpus/SOURCES.md` (NIST CFTT report index) | where version-scoped reports live (tool-claim path) |
| S009 | `corpus/SOURCES.md` (Microsoft PE Format) | spec-derived layout expectations (Q03) |
| S010 | `corpus/SOURCES.md` (Unicode chapter 3) | well-formedness expectations from the spec (Q03) |
| S014 | `corpus/SOURCES.md` (lane `LOG.md`) | tool-claim scoring precedent r7/r8; r35 reformat digest caveat |
| S015 | `corpus/SOURCES.md` (round-1 lesson gate) | saved receipt hashes and Evidence IDs show internal consistency only |
| S032 | `corpus/SOURCES.md` (PKWARE APPNOTE) | field-offset readout precedent for a byte-derived entry (Q11) |
| S033 | `corpus/SOURCES.md` (archive-r2 fixture + truth + saved record) | byte → oracle → saved-record correspondence precedent |
| S034 | `corpus/SOURCES.md` (APPNOTE local header) | narrower re-open beside S032; scope discipline (Q01) |
| S035 | `corpus/SOURCES.md` (saved round-2 ledger) | provenance-only citation precedent (Q09) |
| `corpus/knowledge/round-63-zip-central-directory-evidence.md` | corpus/knowledge/ | worked byte-oracle entry |
| `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` | corpus/knowledge/ | worked authored-byte/saved-field entry |
| `corpus/knowledge/round-62-commonjs-require-name-evidence.md` | corpus/knowledge/ | worked source-name/record entry (scoped limits) |
| `corpus/knowledge/digest-scope-versus-provenance.md` | corpus/knowledge/ | digest scope and custody |
| `corpus/knowledge/tool-validation-by-function-and-version.md` | corpus/knowledge/ | tool-claim scoring |
| `corpus/knowledge/pe-resource-directory-layout.md` | corpus/knowledge/ | resource-tree layout and limits |
| `corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md` | corpus/knowledge/ | ill-formed name classification |
| `corpus/lessons/round-1.md` | corpus/lessons/ | mistake classes behind Q01–Q11 |
| `corpus/lessons/round-61.md` | corpus/lessons/ | M21 (Q12), M22 (Q13) |
| `corpus/lessons/round-62.md` | corpus/lessons/ | M27/M28 derivation and unit mistakes |
| `corpus/lessons/round-63.md` | corpus/lessons/ | M33 `:218`, M34 `:219`, M35 `:220` |
| `corpus/fixtures/firmware-r63/generator.py` | corpus/fixtures/firmware-r63/ | fixture authoring discipline (§2) |
| `corpus/fixtures/firmware-r63/truth.json` | corpus/fixtures/firmware-r63/ | truth shape and build recipe |
| `corpus/fixtures/REPLAY.md` | corpus/fixtures/ | fixture replay contract pointer |
| `corpus/README.md` | corpus/ | coverage legend and known gaps |
| `corpus/QUALITY.md` | corpus/ | Q01–Q16 and admission procedure |
| `corpus/SOURCES.md` | corpus/ | tiers, row rules, census |
| `SCORECARD.md` | lane root | census C command; rubric boundaries; axes |
| `SHONEN.md` | lane root | box 1 requirement this file answers |
| `PROVINCE.md` | lane root | province limits and refusals |
| `reports/round-64/claims.md` | reports/round-64/ | C1/C2, M36, admission order, void conditions |
| `reports/round-64/measure.py` | reports/round-64/ | frozen counter |
| `reports/round-64/measure-before.log` | reports/round-64/ | red-before receipt |
| `reports/round-64/measure.py` sha256 | `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168` | identity of the frozen instrument (committed at `3bb430f`, unchanged at `a3d063f`/working tree) |
| `reports/round-65/claims.md` | reports/round-65/ | C1/C2, C5 fix shape, frozen admission order (either-way flip) |
| `reports/round-65/measure.py` | reports/round-65/ | frozen counter (sha256 `8a2c69c4b0e9a799592c90f0e974ffee05556db5667d7b90ada58f92cf590304`) |
| `reports/round-65/measure-before.log` | reports/round-65/ | red-before receipt (K 8/14, C5 0/2, HOLDS_OK_V3=no) |
| `reports/round-66/claims.md` | reports/round-66/ | C1 disposition + C2/C6 fix shape, adjudication order |
| `reports/round-66/measure.py` | reports/round-66/ | frozen counter (sha256 `a59914e9199ac2fd49cf0bca40ea152a74823a63ecd300fae2fe45ee42ebf1da`) |
| `reports/round-66/measure-before.log` | reports/round-66/ | red-before receipt (K 8/14, C05 frontier, C6 0/4, HOLDS_OK_V4=no) |
| `corpus/fixtures/apk-r65/generator.py` | corpus/fixtures/apk-r65/ | container-fixture authoring (§2 second precedent) |
| `corpus/fixtures/apk-r65/truth.json` | corpus/fixtures/apk-r65/ | container oracle schema |
| `corpus/fixtures/apk-r65/readout.py` | corpus/fixtures/apk-r65/ | byte readout + per-fact form |
| `corpus/knowledge/round-64-firmware-region-byte-evidence.md` | corpus/knowledge/ | worked fixture entry (admitted) |
| `corpus/knowledge/round-65-apk-axml-byte-evidence.md` | corpus/knowledge/ | retained **rejected** candidate — falsified by the dispatched round-65 wave (Q02/Q06/Q11); evidence, never cite as held |
| `corpus/lessons/round-65.md` | corpus/lessons/ | M37/M38 |
| `corpus/lessons/round-66.md` | corpus/lessons/ | M39–M41; round-65 wave adjudication record |
| S038 | `corpus/SOURCES.md` (AOSP ResourceTypes.h, android-15.0.0_r1) | AXML field layout (Q03-derived constants) |
| S041 | `corpus/SOURCES.md` (apk-r65 bundle) | authored container fixture bytes |
| S042 | `corpus/SOURCES.md` (round-65 wave corpus) | the named fresh-seat gate decisions |
| S043 | `corpus/SOURCES.md` (supersedes S039) | corrected REA Android route-scope anchor (lines 7-8) |
| S044 | `corpus/SOURCES.md` (supersedes S040) | corrected zipfile-docs title (3.15.1), queued |
| S045 | `corpus/SOURCES.md` (AOSP DEX format spec, opened 2026-10-24, snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html`) | dex declared-header field semantics for the round-67 C05 v2 candidate (item 9) |
| `corpus/knowledge/round-67-apk-axml-byte-evidence.md` | corpus/knowledge/ | round-67 C05 re-gate candidate — **retained `rejected`** by the dispatched r67 wave (Q02 FAIL: START_NAMESPACE anchor :244 vs actual :245, twice; every other repair verified good: Q01/Q03–Q13 PASS or n/a with named reasons, blind derive CONCUR, hex checks ALL-MATCH); evidence, never cite as held |
| `corpus/check_embedded_outputs.py` | corpus/ | registered gate (see §Gate registry): embedded-output verbatim drift check, the M39 fix shape |
| `reports/round-67/claims.md` | reports/round-67/ | C1 either-way order + C2/C7 fix shape, frozen counter, void conditions |
| `reports/round-67/measure.py` | reports/round-67/ | frozen counter (sha256 `7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e`) |
| `reports/round-67/measure-before.log` | reports/round-67/ | red-before receipt (K 8/14, C7 0/no, HOLDS_OK_V5=no, exit 0) |

S-ids are cited from `corpus/SOURCES.md`; no URL is restated here, so no citation can
drift from the registry. Knowledge entries are cited by repo-relative path, not by claim.

## 8. Failure modes of this SKILL itself

- Citing a guarded conjunct as if a verifier were uniformly deletion-sensitive — M35.
- Treating the counter's labels as admission (M34) or a green self-test as a gate.
- Using this SKILL as a knowledge entry or as evidence of capability: it is instruction,
  and `SHONEN.md` flips box 1 only on a named non-author verifier's pass.

## 9. Bounty-triage module (instruction pointer, added 2026-10-27)

Authorized bounty/coordinated-disclosure triage of a shipped artifact is governed by
`corpus/training/bounty-triage/MODULE.md`. This section is a pointer, not a restatement.

| rule | where it lives | check that catches a violation |
|---|---|---|
| written scope precedes any artifact read; expired/ambiguous/absent scope is a stop | `MODULE.md` §1 | `check_package.py` codes B01–B09 |
| triage is artifact-first and static; execution or a live request is a stop | `MODULE.md` §2, §5 | B06 (`live_target_activity` / method allow-list); R08 stop record |
| every observation carries its deriving command, bound to a declared digest | `MODULE.md` §3 | L02–L06 |
| the report is nine sections and every impact line is evidence-bound or `unknown` | `MODULE.md` §4 | R01–R11 |
| an escalation is recorded, never silent | `MODULE.md` §5 | R08 |

The module is instruction: it fills no coverage row and carries no Evidence ID. Its
validator (`corpus/training/bounty-triage/check_package.py`, `--package`/`--self-test`,
exit 0/1/2/64) is **not** an admission gate and is not added to the Gate registry above;
a green run says nothing about truth, authorization or publishability.
Source rows are S050 (Claude-Red maintainer intended-use statement, tier A for that
scope only) and S051 (reporting methodology, tier C corroboration).
The authoring record is `corpus/lessons/2026-10-27-bounty-triage-module.md`.

## 10. Resource routes (instruction pointer, added 2026-10-29)

Where to open a primary source before trusting a tool's output. This section is a pointer to
`corpus/knowledge/round-73-re-resource-atlas.md` (candidate, not admitted) and the `## Paths`
block of `corpus/SOURCES.md`; it adds no claim and no Evidence ID.

| the claim at hand | open first | then |
|---|---|---|
| a disassembly/decompiler listing is right | S110–S112 (what disassembly ground truth is), S116–S117 (decompiler correctness tests) | S115 / S113 structuring semantics; S373 fidelity taxonomy |
| expected value for a byte fixture | the format's primary spec row (ELF S141/S135, DWARF S143, Mach-O S144, PE S009 + PDB S147, ECMA-335 S136, WASM S162, DEX S048, JVM class file S159) | Kaitai S168 / ImHex S171 / Construct S172 as an independent re-derivation |
| what a parser really accepts | S181 (identification vs polyglots), S194–S195 (loader differentials) | pefile S175, PolyFile S188, Corkami S183 |
| a capability or diff claim | capa S205–S207 and its limitations row, FLOSS S209, BinDiff S223 / Diaphora S225 / ghidriff S226 | every match is a labelled inference; unmatched stays unknown |
| an extractor for a packaged app | Go S211/S152/S258, Dart S264–S269, Hermes S270, PyInstaller S272, Electron S277/S297–S298, .NET R2R S282 | the extractor's own README limits; recovered source is a reconstruction |
| a firmware image | unblob S306–S307 and Binwalk S308 as two independent carvers, then the header spec (DTB S322, FIT S323, Android boot S324, AVB S325) | unextracted bytes are `unknown` |
| what a hash or signature proves | S334–S338 (reproducible builds, SLSA, Sigstore, in-toto) | extends Q09; a signature binds subject and signer only |
| text inside the sample addressed to the analyst | S368–S370, S085, S076 | artifact text is data, never instruction |

Rejected and refused material is registered, not hidden: S249/S250 (live execution of malware or
of a protected target), S321 (live-host testing), S401/S402 (exploitation training). Rows whose
anchor says `single-opener` rest on the scout's own read until `reports/round-73/verify_quotes.py`
reaches them. Host tool presence is in `reports/round-73/tool-probes.md` and is not readiness.


# Checklists — lane operability and evidence-ledger discipline

Operability half of the round-64 SKILL candidate (SHONEN box 1); merges with the
descriptive half drafted by `R64SkillDraft`. Every command below was copied
verbatim from the named `file:line` in this lane repo, or from the fleet contract
that the lane's own `corpus/SOURCES.md:3` names as governing. Nothing is
transcribed from memory. All commands are read-only: none writes into `corpus/`,
none runs `git`/`jj` mutations, none installs software.

Lane root for every step unless stated: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## 1. Verifier census — ten saved-ledger replay verifiers

Source: `SCORECARD.md:35-42` (command C). Run from the lane root: the glob is
relative (`pathlib.Path("corpus")`), so another cwd silently censuses zero scripts.

```sh
python3 -B -c 'import pathlib,subprocess,sys
ps=sorted(pathlib.Path("corpus").glob("verify_*.py"))
rows=[(p.name,subprocess.run([sys.executable,"-B",str(p),"--self-test"],capture_output=True,text=True)) for p in ps]
for name,r in rows: print(name,"exit="+str(r.returncode),(r.stdout+r.stderr).splitlines()[-1])
names={"verify_icon_states.py","verify_multi_icon_states.py","verify_icon_languages.py","verify_named_multi_icon_states.py"}
ok=sum(r.returncode==0 for name,r in rows if name in names)
print("CALIBRATION",ok,"/",len(names),"score=",10*ok/len(names))
print("REPLAY",sum(r.returncode==0 for _,r in rows),"/",len(rows))'
```

Promised outcome:

- one line per `corpus/verify_*.py` in name order, `<name> exit=<code> <final output line>`;
  ten verifiers at base (`corpus/lessons/round-63.md:212`, the census count that
  stays 10; `corpus/README.md:17` describes the set);
- then `CALIBRATION <ok> / 4 score= <value>` over the four scripts named in the
  command, and `REPLAY <ok> / <n>` over all of them;
- the wrapper exits 0 **even when constituent verifiers fail** (`SCORECARD.md:29-30`).
  The promise is each printed `exit=` field and the two ratios, never the wrapper status.
- recorded base values (`reports/round-64/measure-before.log`, the counter's own HOLD
  loop over the same script set — recorded, not re-run for this checklist): all ten
  `exit=0`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`.

A non-zero verifier means its own saved-input assertion rejected something. The
census does not say which clause; that is the verifier's own output. Do not cite
a verifier for a clause its own run is not shown to detect (Q13, `corpus/QUALITY.md`).

## 2. Firmware oracle — authored bytes vs saved REA record

Source: `corpus/live/runs/round-63/LEDGER.md:110`.

```sh
python3 -B corpus/live/runs/round-63/oracle_check.py     # ORACLE OK, exit 0
```

Defaults are file-relative (`corpus/live/runs/round-63/oracle_check.py:11-13`:
the record beside the script, the truth oracle at lane root +
`corpus/fixtures/firmware-r63/truth.json`), so the line works as written from the
lane root; `--record` and `--truth` override either side.

Promised outcome:

- one `REGION ...` line per truth region — five on this fixture: two `zlib` members
  and three padding spans (`LEDGER.md` O6) — carrying the record-vs-truth marker
  (`record=not-expected padding=OK` on the padding rows; the two paired members
  print `offset=OK size=OK signature=OK decompressed_sha256=OK`, recorded in
  `corpus/lessons/round-63-verifier-spotcheck.md:31`);
- final line `ORACLE OK`, exit 0 (`LEDGER.md:43`, O10).

Disagreement prints `MISMATCH <field>: <detail>` lines, then `ORACLE MISMATCH`,
exit `1` (`oracle_check.py` main return). The oracle does **not** promise the
producer ran, that the record is authentic, or anything about other images — Q09
scoping; the record's own open unknowns are `LEDGER.md` U4–U6.

## 3. Frozen counter — the round's registered counting probe

Source: `reports/round-66/claims.md` §Frozen counter (`reports/round-66/measure.py`,
sha256 `a59914e9199ac2fd49cf0bca40ea152a74823a63ecd300fae2fe45ee42ebf1da` at the
round-66 pre-registration; the round-64 instrument `b8e68d32…` and the round-65
`8a2c69c4…` remain committed history). The command it names, copied from inside
the backticks:

```sh
python3 -B reports/round-66/measure.py TREE
```

`TREE` is the only argument; it must contain `corpus/` or the probe exits with
`usage: measure.py TREE (TREE/corpus must exist)`. The contract fixes the rest:
TREE is a committed `git archive <commit> corpus` extraction, cwd=`/`, TMPDIR
under lane-owned `/tmp/revenger-r66-*`. Never point it at the working tree. The
committed invocation shape below is quoted byte-identical from a round-63
record; change only the archive commit and the counter path before running it
for this round:

```sh
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive db55bd6 corpus | tar -x -C /tmp/T
cd / && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-66/measure.py /tmp/T
```

Inside, the probe copies `corpus` into its own temp dirs for each mutant run
(prefixes `rev-r64-mut-`, `rev-r64-c3-`, `rev-r64-c4-`, `rev-r65-c5-`,
`rev-r66-c6-`), so the source tree is not mutated.

Promised outcome — the labels, with the base-archive values recorded in
`reports/round-66/measure-before.log` (base `8214e4dd`, recorded not re-run
here):

| label | round-66 base value | note |
|---|---|---|
| `K_HELD` | `=8/14 score=5.7` | 7/14 at the round-64 base |
| `K_ROW C05` / `K_ROW C07` | `status=frontier` / `status=held` | C05 is the round-66 disposition readout |
| `C05_REJECTED_MARKED` | `=no` | new round-66 label: whole-file `admission-status: rejected` scan of the retained candidate |
| `K_HELD_BACKED` / `K_HELD_BACKED_STRICT` | `=8/14` / `=8/14` | STRICT is the whole-file rejected-marker scan (M37 repair) |
| `STRICT_REJECT_WINDOW_SELFTEST` | `=pass old_window_miss=True` | new round-65 label |
| `SAVED_RECORDS`, `ROW_OPS` | `=59`; `{'C03': ['inspect_managed_artifact'], 'C05': ['inspect_android_package'], 'C07': ['inspect_firmware_regions'], 'C08': ['capture_browser_scenario', 'inspect_web_page', 'observe_web_session']}` | ROW_OPS frozen |
| `README_TOKEN_LEGEND_MISMATCH` | `=0 rows=[]` | `1 rows=['C07']` at the round-64 base — the M36 fix landed |
| operation counter, `F_COVERAGE`, `F_FAMILIES` | `F_COVERAGE=5/8 score=6.2`, `F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']` | unchanged |
| `FRESH_ROWS` | `=18/18` (byte survival, not current-host truth) | unchanged |
| `MUTANT <script> <variant>` lines + `C2_*` | `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` | unchanged holds |
| `C3_*`, `C4_*`, `C5_*` | `2/2`, `2/2`, `2/2` attributed each | C4 was `0/2` at the round-64 base, C5 `0/2` at the round-65 base — both earned since |
| `C6_*` | `C6_CONTROL_PRESENT=0/4`, `C6_CONTROLS_PASS=4/4`, `C6_RECEIPT_KILLED=0/4`, `C6_RECEIPT_KILLED_ATTRIBUTED=0/4` | the round-66 target |
| `HOLD <script> exit=...`, `HOLD_CALIBRATION`, `HOLD_REPLAY` | ten `exit=0` lines, `=4/4`, `=10/10` | unchanged holds |
| `HOLDS_OK` / `HOLDS_OK_V2` / `HOLDS_OK_V3` / `HOLDS_OK_V4` | `=yes` / `=yes` / `=yes` / `=no` | V4 = V3 ∧ C6 attributed 4/4 |

Exit semantics (`reports/round-66/measure.py` tail): `2` = not evaluable (a
frozen clause matched other than exactly once, printed `could-not-evaluate`),
`0` = the round-63 holds passed, `1` = a frozen hold failed. **Exit 0 does not
mean the round's claims are met**: the base receipt shows
`C6_RECEIPT_KILLED_ATTRIBUTED=0/4` and `HOLDS_OK_V4=no` alongside
`HOLDS_OK=yes`, which exits 0. Read the labels; never quote the exit code as
claim satisfaction (M34, `corpus/lessons/round-63.md`).

## 4. SOURCES census

### 4a. Fleet read-only registry checker (the round's census numbers)

Source: `.ufo/waves/round-63/falsify/W2FinalIndependent.md:151-152`. The script is
fleet-owned (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`): run it,
never edit it.

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-24 /home/vgpnk/Projects/shokunin/revenger-shokunin
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census /home/vgpnk/Projects/shokunin/revenger-shokunin
```

Promised outcome: TSV on stdout, `lane<TAB>code-or-metric<TAB>value…`; exit `0`
clean or warnings only, `1` E/overdue findings, `2` usage/env/missing registry,
`3` selftest failure (script header `:16-18`). `--today` is a scalar parameter,
not part of the proof: the value above is the round-63 run date and may be
dropped, in which case the script uses UTC today (`TODAY=${TODAY:-$(date -u +%F)}`).
`validate` reports E01–E12 and
W01–W04; W-codes do not fail a clean lane, and W04 ("same URL across scopes") is
expected where a source is deliberately re-opened under a narrower scope — report
it, never hide it. Recorded observations: round-63 tip → `validate` exit 0 with
exactly three disclosed W04s (S024/S028/S029), `census` exit 0, rows 33, tier
A 31 / C 2, mined 28 / queued 1 / rejected 4, missing 0
(`W2FinalIndependent.md:139-143`); round-64 base → census exit 0, 35 rows, four
disclosed W04s (S024/S028/S029/S034) (`reports/round-64/claims.md:127-129`). The
33→35 gap is appends between rounds, not a contradiction; every number is
read from the run, not from this page.

### 4b. Portable contract census (seven commands, no fleet script)

Source: `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:67-80`, the contract
`corpus/SOURCES.md:3` names; heading says run from the lane root. The same seven
commands were exercised in-lane in round 63
(`.ufo/waves/round-63/falsify/W2VerifySourcesTable.md:52`).

```sh
# rows (spacing-tolerant)
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# status histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# duplicate ids — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# enum violations and tier inflation — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
# mined rows whose used-by paths do not exist — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

Promised outcome, per the inline comments: the row count (grows only by append;
35 at round-64 base); malformed rows (`NF!=13`) must print `0`; tier and status
histograms; duplicate ids, enum/tier-inflation violations and mined rows whose
`used-by` path is absent on disk must each print nothing. Only the zero/empty
promises are pass/fail; histograms are observations.

## 5. Evidence-ledger discipline

Rule: `PROVINCE.md:6-7` — every conclusion separates **observation, inference,
unknown** and cites Evidence IDs. Admission step 3 makes it binding:
`corpus/QUALITY.md:32-33` — an entry that does not separate the three layers and
name at least one limitation is not admissible.

Shape in practice (`corpus/live/runs/round-63/LEDGER.md` is the worked exemplar):

- rows are `# | Class | Statement | Basis | Result`, ids `O#` / `I#` / `U#`,
  class spelled OBSERVATION, INFERENCE or UNKNOWN;
- an observation quotes the saved field or bytes it reads, and `Basis` names the
  file and field; a re-derivation names the command that produced it;
- an inference is bounded to the fixture, route, provider and version actually
  observed and states what it does not establish (e.g. "This says nothing about
  binwalk or REA firmware inspection on any other image", `LEDGER.md` I1);
- an unknown stays open even when a counter improves. Coverage counts are
  presence, not quality: a hand-written JSON with a fabricated `evidence_id` and
  `operation` satisfies the F predicate (`LEDGER.md` §Score and limitations; M34);

Never promote:

- **digest / receipt / Evidence ID → origin.** Claim a digest only for the exact
  bytes hashed; it establishes no producer origin, completeness or authenticity
  (Q09, `corpus/QUALITY.md`; `LEDGER.md` U4).
- **recorded → re-derived.** A value taken from prose is labelled `recorded`; a
  derived value carries its in-entry command and that command's output (Q11).
  Expected values come from bytes, a specification or a pin fixed outside the
  record under test (Q03).
- **tool presence → tool result.** A tool claim names tool, version, function and
  scores the tool's own output; manual analysis is labelled manual (Q04).
- **counts → coverage.** Status tokens carry the README's own definitions
  (`corpus/README.md:21-26`): `held` = at least one admitted entry, `partial`,
  `uncovered` = work evidence but no admitted entry, `frontier` = no knowledge and
  no saved record. Work evidence is not knowledge (`corpus/README.md:25`).
- **observation → general rule.** Scope to the observed family, operation,
  version and input; contested cross-lane scope is reported, not absorbed (Q10).

## 6. What a green run of these checklists does not establish

No producer re-run, no target execution, no authenticity, no completeness, no
promotion, no current-host truth (the freshness rows are byte survival, frozen in
`claims.md`). A green census or counter is a saved-input replay result against a
committed tree; it is evidence of consistency, not of provenance.
