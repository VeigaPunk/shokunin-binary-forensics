REJECT — the draft's numbers are true but three of them carry no derivation, and its central freshness sentence credits the lane's gate with re-running commands the landed gate refuses; per-entry gates fail on Q01/Q02/Q11/Q13 and the draft's own landing condition (offline snapshot) is unmet at 17ee7f8.

# Seat R70W2AssimGateB — assimilation gate, critic B

Target: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md`
(sha256 `2bbc89bec6a2f8b3b31a8c45d779cd466447ebeb0dc018d5700c62bd03b3e8ce`, 107 lines; NOT the C05 entry —
`corpus/knowledge/round-70-apk-axml-byte-evidence.md` at 17ee7f8 is `819efcb8…`, a different document).
Landed context read from commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`; gate/lint run from the lane root.
No file outside this report was written; scratch copies were `/tmp/revenger-r70-AssimGateB-*`.

## 1. What I re-derived and it holds (credit where due)

I re-ran every command the draft prints. All arithmetic reproduces; the defects below are provenance,
derivation and credit, not false numbers.

```
$ unblob --version
26.6.4
$ unblob --show-external-dependencies ; echo EXIT=$?
    ... 15 rows, ✓ on 7z debugfs lz4 simg2img zstd (5), ✗ on 10 ...
EXIT=1
```
Draft item 6 re-derived verbatim (`python3 -B -c` command from the draft, run at the lane root):
```
unblob_version 26.6.4
deps_exit 1
deps_rows 15
deps_found 5
deps_missing 10
```
Item 7 likewise: `deps_names 7z debugfs fsck.erofs jefferson lz4 lziprecover lzop partclone.restore sasquatch
sasquatch-v4be simg2img ubireader_extract_files ubireader_extract_images unar zstd` / `missing_names fsck.erofs
jefferson lziprecover lzop partclone.restore sasquatch sasquatch-v4be ubireader_extract_files
ubireader_extract_images unar` — identical to the draft. So **the host probe is real and is re-derived by me now,
not recorded prose**: unblob 26.6.4 IS installed (`~/.local/share/uv/tools/unblob`, mtime `2026-10-25 18:10:59`,
`uv-receipt.toml` present), exit 1, 15/5/10.

Item 1 (network, live) reproduces the pin exactly:
```
bytes 7580
lines 235
sha256 6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716
```
Items 2 and 3 reproduce exactly too: sections `[(20,'## Features'),(35,'## Installation'),(37,'### pip …'),
(91,'### From source')]`; quotes at 22/100/46/161; `named_families 11`, `apt_packages 11`,
`flag_occurrences 3`. Lines 5, 59, 97 are textually correct (`unblob --show-external-dependencies` at 59 and
`uv run unblob --show-external-dependencies` at 97; `78+ archive, compression, and file-system formats` at 5).

## 2. Failing criteria

### Q13 FAIL — the entry credits the lane's gate with a run the gate refuses (located defect D1)

Draft, Observation paragraph: "All commands are `python3` standard-library invocations with no shell
metacharacters, **so the embedded-output gate can re-run them by argv**." Landed gate, from the lane root:

```
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r70-AssimGateB-draft.md
could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure
GATE_EXIT=2
```
Cause, in the landed bytes: `corpus/check_embedded_outputs.py:75-84` `confined()` returns False whenever the
first non-`-B` argv token starts with `-`, and `:104` maps that to `(None,"",2)` → `evaluate` returns `None` →
exit 2. The gate's own self-test asserts this: `:245` `not confined(["python3","-c","print(1)"])`. **Zero of the
seven blocks are checked.** Mutant test (copy in /tmp, two output lines altered — the item-2 quote `78+`→`77+`
and the item-1 printed `sha256 6544d60f…`→`deadbeef…`):
```
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r70-AssimGateB-mut.md
could-not-evaluate: ...
MUT_GATE_EXIT=2
```
No drift reported, no detection. So the entry cites a verifier as guarding values whose check cannot even run —
exactly Q13's reject clause ("cites a verifier as guarding a value whose check survives deletion"), while the
entry's own Q13 row asserts "No verifier is credited for a clause its own run does not detect." The lint does
not catch this: `python3 -B corpus/lint_entry.py --entry <draft>` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0
LINT_HEADER=0`, `LINT_EXIT=0`.

### Q11 FAIL — three stated line numbers (and one quote) carry no command (D2)

Item 2's command prints sections `(20,35,37,91)` and quotes `(22,100,46,161)`. It does not print 5, 59 or 97.
Yet item 3 states "The same figure appears once more in the lede at **line 5** (`78+ archive, compression, and
file-system formats`)" and item 5 states the flag appears "as the command at **line 59** … at **line 97**". The
§Q-map Q11 row then claims these very numbers are among those that "carry … the command that derives it":
"line numbers 20, 22, 35, 37, 46, **59**, 91, **97**, 100, 161". Four values are typed by hand (5, 59, 97 and
the line-5 quote); they happen to be correct today, which is precisely Q11's reject clause ("a value is correct
when re-derived but the entry carries no derivation"). Same clause, second instance (D2b): Scope line 10 says
"no SWGDE row exists in `corpus/SOURCES.md`" — the landed registry holds **S003** (SWGDE Minimum Requirements for
Testing Tools, 18-Q-001-2.1, `spec`, tier A) at `corpus/SOURCES.md:17` and **S005** (SWGDE Best Practices for
Computer Forensic Acquisitions, 18-F-002, tier A) at `:19`; the retained package entry's claim 2 cites 18-F-002
and 18-F-003. The stated reason for dropping the package's claims 1-2 is false against the lane's own registry.

### Q01 + Q02 FAIL — the declared S-ids resolve to different documents at the landed tip (D3)

Draft `source:` lines declare **S048** = unblob upstream README and **S049** = own-work host probe, both marked
"PROVISIONAL until the L1 appends it". At `17ee7f8`, `corpus/SOURCES.md:62` is S048 = AOSP DEX format
specification (docs, A, scope: `header_item` fields of one authored `classes.dex`) and `:63` is S049 = REA
"Android application artifacts" reference (docs, A, route-scope sentences). Neither is tier A for the draft's
claims, and the ids are not free: `.ufo/waves/round-70/assimilation/staged-ids:2-5` stages S048-S051 and
`.ufo/waves/round-70/assimilation/collisions` already records `S047`, `S050`. Admitting the draft with its
header as written attaches load-bearing claims to rows that credit a different scope (Q01) and gives `source:`
anchors that do not resolve to the named source (Q02).

Secondary Q02 defect (D3b): the header points at items that hold no command. `recheck:` says "**item 4's**
command re-runs `unblob --version` and `unblob --show-external-dependencies`"; `verified-at:` says "**item 4-5**
ran the locally installed tool"; the S049 `source:` anchors say "the two commands and their full stdout are
**items 4 and 5**"; Scope says "(items 4 and 5)". Items 4 and 5 are prose claims ("Claim 4 retained", "Claim 5
retained"); the commands are items **6** and **7**, as the entry's own Q04/Q05 rows correctly say. A recheck line
that names a non-command item cannot be followed as written.

## 3. Freshness (my judged axis) — the draft's own landing condition is unmet

The draft's Limitation: "The bytes are **not** committed in this draft; landing requires
`corpus/snapshots/unblob-README.md` with the printed sha256 so items 2 and 3 re-derive offline."

```
$ git -C …/revenger-shokunin ls-tree 17ee7f8 corpus/snapshots/
100644 … APPNOTE.TXT
100644 … ResourceTypes.h
100644 … dex-format.html
100644 … rea-android-applications.md
```
No `unblob-README.md`. Combined with §2/Q13, the entry at the landed target is a record whose every value is
reachable only by network fetch plus a binary the author installed that day, and whose embedded blocks no
registered verifier can execute. That is a freshness regression against the lane's own C3 axis (an entry must
re-derive against pinned bytes), not a neutral omission.

## 4. Calibration conflict the entry does not reconcile (D5)

The draft discloses "The pre-existing `~/.local/bin/unblob` symlink, dated 13 October, was dangling before that
install, so the probe says nothing about the host's state at any earlier date." If true, two admitted records are
false and the entry does not say so: `corpus/README.md:73` ("the host has binwalk 3.1.0 and unblob 26.6.4") and
`corpus/knowledge/2026-10-12-rea-readiness-checklist.md:40` ("unblob 26.6.4 present … STALE → 3 of 4 present"),
plus the retained package entry's "Observed host state" ("`unblob --version` reports `26.6.4`"). The install
evidence supports the draft (uv tool dir mtime `2026-10-25 18:10:59`), so the older records are the stale side —
and a C07-deepening entry is exactly where that should be flagged. As written the entry leaves the conflict
silent.

## 5. Q decisions (Q01-Q15) on the draft bytes

| Q | decision | basis |
|---|---|---|
| Q01 | **FAIL** | D3: S048/S049 are, at 17ee7f8, rows tier A for other scopes; the claims' support does not exist. |
| Q02 | **FAIL** | D3/D3b: `source:` ids resolve to other documents; `recheck:`/`verified-at:`/Scope/S049-anchor name items 4-5, which hold no command. |
| Q03 | pass | expected values read from fetched bytes and from the tool's own report, not copied from the package entry (which explicitly did *not* run `--show-external-dependencies`). |
| Q04 | pass | tool, version as the tool prints it, function, and its own exit 1 / 15-5-10; re-derived by me. |
| Q05 | pass | no capability claim; the probe is the statement, with exit and full output. |
| Q06 | n/a | no fixture, no offset from intent. |
| Q07 | n/a | no parser-behavior prediction; the package→executable mapping is under Unknown. |
| Q08 | n/a | superseded by Q11. |
| Q09 | pass | item 1 states in place that the digest says nothing about earlier branch content or authorship. |
| Q10 | pass | scope held to one document/one date/one host; the "Python with Rust extensions" sentence is labeled as an inference about the description. |
| Q11 | **FAIL** | D2: lines 5, 59, 97 and the line-5 quote have no command, and the Q11 row claims they do; D2b: the "no SWGDE row" claim is false (`SOURCES.md:17`, `:19`). |
| Q12 | n/a | no rejected-source row is written; the drop is prose, and its stated ground is D2b. |
| Q13 | **FAIL** | D1: gate run = exit 2, zero blocks; two-line mutant undetected; the entry claims gate re-runnability. |
| Q14 | pass | only hex string is the 64-hex sha256 with no byte-count clause; `LINT_Q14=0`. |
| Q15 | pass | no git object id or tree identity stated; `LINT_Q15=0`. |

Verdict: **REJECT** (failing Q01, Q02, Q11, Q13), with freshness as an independent gate reason. The material is
good — the probe and the fetch both re-derive — so this is a fixable defect, not a rejected source.

## 6. Flip condition (smallest safe correction)

1. **Make the blocks gate-runnable and offline.** Commit `corpus/snapshots/unblob-README.md` at sha256
   `6544d60f…`; add two relative scripts (e.g. `corpus/read_unblob_readme.py` printing bytes/lines/sha256, the
   section+quote line numbers **including 5, 59, 97**, and the family/package/flag counts from the snapshot;
   `corpus/probe_unblob_deps.py` printing the version/exit/rows/names). Re-point items 1-3 to the snapshot and
   6-7 to the probe script. Acceptance: `python3 -B corpus/check_embedded_outputs.py --entry <entry>` exits **0**
   with ≥5 blocks checked, and a mutant of any quoted line or digest exits 1.
2. **Renumber** the source rows to a free, uncontested id at the landed tip (S048/S049 are taken; S050 is in
   `assimilation/collisions`) and open real `corpus/SOURCES.md` rows at tier A for exactly the scopes claimed.
3. **Fix the anchors:** items 6-7 (not 4-5) in `source:` S049, `recheck:`, `verified-at:` and Scope.
4. **Derive or delete** lines 5/59/97 and the line-5 quote (item 1 of the correction covers this).
5. **Correct the SWGDE sentence** — S003 and S005 exist; restate the drop on scope grounds (the package's
   SWGDE half is about custody documentation, not the unblob figures).
6. **Reconcile the host-state limitation** with `README.md:73` and
   `knowledge/2026-10-12-rea-readiness-checklist.md:40`: name them stale, or withdraw the dangling-symlink claim.

Until 1-6 land, this entry cannot clear the per-entry gates; a counter-only or lint-only reading
(`LINT_EXIT=0`) would admit it and is exactly the control the amendment was written to close.

## 7. Tooling record

No install or update was made by this seat. `unblob 26.6.4` already present at `/home/vgpnk/.local/bin/unblob`
(uv tool channel, installed 2026-10-25 18:10:59 by the wave-1 author, per `uv-receipt.toml`) — used read-only for
the re-probe. No pacman transaction. Scratch `/tmp/revenger-r70-AssimGateB*` removed before returning.
