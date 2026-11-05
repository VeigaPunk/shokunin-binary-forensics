# ScribeR92Entry — round 92, C1 knowledge entry and SOURCES rows

Seat: `ScribeR92Entry` (scribe, wave 1). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Date: 2026-11-05. Lane commit at freeze: `9402183a9492428fa0064d250746c62a0a2d9ca5`.

## What I produced

| path | role |
|---|---|
| `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` | the C1 candidate entry (50408 bytes, `admission-status: candidate`) |
| `.ufo/waves/round-92/w1/ScribeR92Entry/SOURCES.append.md` | four SOURCES rows S491–S491…S494 for the L1 to append |
| `.ufo/waves/round-92/w1/ScribeR92Entry/READY` | the counter's digest line, written last |
| `.ufo/waves/round-92/w1/ScribeR92Entry.md` | this report |

No other lane file was written. `corpus/SOURCES.md`, `corpus/README.md`, `SKILL.md`, `SCORECARD.md`,
`LOG.md`, `corpus/lessons/*`, `MANIFEST.json` and everything under `reports/round-92/` are untouched by
me; `SKILL.md` and `.gitignore` were already modified in the working tree by another seat before I
started (`git status` at my first command showed them modified).

## Checks run (both from the lane root, entry as committed in the tree)

```
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-92-managed-assembly-metadata-evidence.md --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
exit=0
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-92-managed-assembly-metadata-evidence.md
checked_blocks=11 problems=0
exit=0
```

11 embedded `$ cmd` blocks, all re-run by the gate with zero drift: the r76 oracle (11 stdout lines),
the r85 artifact oracle (21), the r85 members oracle (48) and the r85 boundaries oracle (40), each
printed verbatim with its own command line.

## The entry's shape

Header lines first, in the required order: `source:` (four registry rows S491–S494 with URL and
anchor, then a separate `source:` line for the own-work record paths, which are not registry rows),
`verified-at:` (lane commit `9402183a` and 2026-11-05), `recheck:` (one runnable command and the
stdout line it must end with), `coverage-map: C03`, `admission-status: candidate`.

Body: `## 1. Observation` (items 1–9, each with the command's own stdout), `## 2. Inference`
(10–14, each scoped and each with its basis), `## 3. Unknown` (15–20), `## 4. Limitations` (21–27,
including the three the task named: no general .NET claim, no producer-readiness claim,
fixture-scoped), `## 5. Provenance (Q11)` (a per-statement table naming the stdout line and the
expectation side for each), `## §Q-map` (all seventeen Q rows, decision cell non-empty),
`## Sources`, `## Reproduce`.

## Sources

I used only the sources ScoutR92Managed marked usable, in its listed order, so the ids are
S491 (ECMA-335 6th ed.) → S492 (ECMA-335 5th ed.) → S493 (PE Format) → S494 (MetadataRootBuilder
API). Each row is 11 columns in the registry order, `status` `mined`, `opened` `2026-11-05`,
`recheck` `180d`, `used-by` exactly `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md`,
and no cell contains a `|` (verified by a parse that re-splits each row and checks 11 cells and the
three fixed values).

I re-opened all four sources myself with `curl` into my scratch dir (HTTP 200 each; the two PDFs
rendered with `pdftotext -layout`) and located each quote in the fetched text before using it. The
scout's own snapshots were used as a second, independent copy of the same text; each quote was
whitespace-normalised and confirmed present in both copies. Seven quotes are used, all ≤25 words:
the root signature, the five-stream sentence and the Rows-array sentence at both editions; the PE
Format CLR-runtime-header row; the MetadataRootBuilder stream-set sentence and "The metadata
version."; plus two ECMA-335 clauses the records exercise — §II.25.3.3.1's
"COMIMAGE_FLAGS_ILONLY 0x00000001 Shall be 1." and §II.25.3.3's "16 4 Flags Flags describing this
runtime image." (the second is what makes 512 + 16 = 528, the record's second evidence offset).

## The one judgement call worth flagging for review

The two oracle scripts print one line per check with the value the script read and an `OK`/`FAIL`
verdict; the expected value is printed only on a failure. The entry therefore states, for every
check it leans on, **which side the comparison is on**: a value the script re-derived from the
fixture bytes, a value fixed outside the record under test (the authored premise file's pin or its
pre-registered hypothesis block), or a literal in the script. That mapping is item 24's table, one
row per run, with the check names partitioned so a name appears in one column and no other. Two
checks are called out separately because their printed value and their expectation sit on opposite
sides: the r76 `fixture.sha256==truth` line prints the script's own digest of the fixture bytes and
compares it with the premise file's pin, while the r76 `subject.sha256` line prints the record's
field and compares it with that same byte-derived digest; and `m0.anchor0` is mixed (literal offset
and opcode, byte-derived token) and is named in neither column. The §5 table points to item 24 rather
than repeating the mapping, so the two cannot drift apart.

## Digest and the counter

The entry's raw bytes hash to `2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6`,
which is also the digest the counter computes after it normalises the `admission-status` line — I
checked that the digest is identical with the line set to `candidate` and with it set to `admitted`,
so the L1's admission flip does not move the bytes the reviewers vote on. `READY` holds exactly that
one line, written via `READY.tmp` + `mv`.

I ran the frozen counter over a scratch tree holding the committed `corpus/` plus my entry and my
four appended SOURCES rows, to see which legs my seat can affect:

```
$ python3 -B reports/round-92/c1_k_admit_counter.py --tree <scratch-tree>
C1_K_HELD_BACKED=8/15
C1_SOURCE_IDS=S491,S492,S493,S494
C1_ROWS_TOTAL=pass
C1_C03_HELD=fail
C1_C03_CITES=fail
C1_ADMITTED=fail
C1_TRIO=pass
C1_VOTES=fail
C1_LINT=pass
C1_EMBEDDED=pass
C1_SOURCES=pass
C1_K_HELD_BACKED=fail
C1_VERDICT=fail
```

The legs that still fail are not mine to close: `C1_C03_HELD`, `C1_C03_CITES` and `C1_K_HELD_BACKED`
need the L1's README C03 row flipped to `held` and naming this entry, `C1_ADMITTED` needs the
`admission-status: admitted` line, and `C1_VOTES` needs two reviewer/critic votes on this digest.
`C1_LINT`, `C1_EMBEDDED`, `C1_SOURCES` and `C1_TRIO` pass. (The first counter run in this scratch
tree reported `C1_LINT=fail`; that was my simulation's fault — the counter resolves `LANE` from its
own location, so running it from a copy outside the lane made `--lane` point at the copy and the
git-resolution leg fail. Re-running it from the lane root gave `C1_LINT=pass`. The real landing run
uses `--rev`, so this artifact cannot occur.)

## Notes and limits

- No producer was invoked; the four records are read as saved bytes. The entry says so and makes no
  readiness claim.
- No tool was installed, upgraded or removed this round; `curl` and `pdftotext` were already present.
  The host-wide `pacman` pause was respected: no `pacman`, `uv`, `npx` or `~/.local/bin` operation.
- The recorded-file digests (`stdout_sha256`, `stdout_bytes` in the four `receipt.json` files) are
  labelled **recorded** in the entry; no command in it re-hashes a saved record.
- Scratch under `$HYAKU_SCRATCH/revenger-r92/ScribeR92Entry/` (fetches, oracle stdout captures, the
  builder script and the counter simulation tree) was deleted before this report was written.
