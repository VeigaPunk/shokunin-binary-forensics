# R64CriticSkill — three material sentence-level findings

## Scope and axes

Reviewed `/tmp/revenger-r64-skill/SKILL.md`, all 268 lines, SHA-256
`29172a6e9982cffabe12a8ec9ac0309bebc951dc86c16b099c826c15c5989f10`.
Line references below bind to that snapshot, not later revisions.

Review axes: truth/provenance, scope/admission fidelity, and literal-execution safety.
Round impacts: coverage-K admission integrity, freshness/provenance, and the frozen
byte-preservation holds. This report changes no axes, scores, admission decisions,
or frozen counter.

The initial missing-candidate report is superseded: the candidate was absent on
the first direct read, then its author notified this seat that it existed.
The following review was performed after that notification, without waiting.

## 1. False verification provenance

**Weak sentence — candidate line 6:**

> Every file, line range and S-id cited below was re-read in the lane tree at that base.

The named base is `666ea84b6be2eec2b0359f556ba2429fc9044c36`.

**Counterexample/evidence.** The candidate itself cites the round-64 contract.
This read-only object lookup:

```sh
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin cat-file -e 666ea84b6be2eec2b0359f556ba2429fc9044c36:reports/round-64/claims.md
```

exited **128**, reporting:

```text
fatal: path 'reports/round-64/claims.md' exists on disk, but not in '666ea84b6be2eec2b0359f556ba2429fc9044c36'
```

Thus at least one cited file cannot have been read at the claimed base.
Candidate lines 40-41 separately acknowledge working-tree C4 patches, which also
cannot be flattened into an all-at-base verification claim. The frozen
`reports/round-64/measure-before.log:28-33` records the base stdout mutants
surviving and `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`.

**Concrete harm.** A fresh agent following the header would attribute the
round-64 contract and patch-sensitive table to a reproducible base snapshot that
does not contain the former and must not be credited with the latter's result.
The provenance claim already fails independently of any future measurement;
it is not merely a stale line-number concern.

**Impacted axes.** Truth/provenance and freshness; indirectly coverage/calibration
evidence attribution. No counter result is changed or inferred here.

**Smallest safe correction.** Separate the historical base identity from the
actual inspection snapshot: cite the real committed identity for round-64
artifacts, and identify any uncommitted patch-dependent claims as working-tree
observations with their own exact content identities. Remove the universal
“every ... at that base” assertion rather than inventing a replacement commit.

## 2. Regeneration instruction overwrites protected evidence

**Weak sentence — candidate lines 207-208:**

> Fixture regeneration: `cd corpus/fixtures/firmware-r63 && python3 -B generator.py`,
> then re-derive and compare bytes; a byte change invalidates every derived value.

Candidate line 79 repeats the instruction to run the recipe in the fixture directory.

**Counterexample/evidence.** In
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py`:

- lines 14-16 bind both output paths to the resolved script directory;
- lines 130-133 put the current zlib and Python versions into generated truth;
- lines 149-150 unconditionally write both `firmware-r63.bin` and `truth.json`.

The existing
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json:5-9,26`
records zlib `1.3.2` and Python `3.14.8`.
The frozen
`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:115-123`
voids changes to old fixture/live bytes and requires round-63 evidence preserved.

**Concrete literal-execution counterexample [INFERENCE, not executed].**
A fresh agent with Python `3.14.9` follows the stated command. Even if compression
produces an identical image, the generator writes `python_version: 3.14.9` over
the protected `truth.json` before the comparison. This violates the preservation
hold and destroys the original on-disk oracle being compared. The same issue
can arise from a zlib-version change. This finding does not assert that the
current host has either differing version.

**Impacted axes.** Literal-execution safety and frozen byte-preservation holds;
coverage-K evidence identity is also at risk.

**Smallest safe correction.** Regenerate only from a physical copy of the fixture
directory under `/tmp/revenger-r64-*`, then compare the scratch outputs against
the untouched originals. Merely changing cwd is insufficient because the
generator uses `Path(__file__).resolve().parent`. Keep the original bytes even
on mismatch; do not refresh their truth metadata to match the new runtime.

## 3. Tier-B shortcut creates a second admission authority

**Weak sentence — candidate line 96, tier-B “may be sole support?” cell:**

> only where Q01's scope test passes

**Counterexample/evidence.**
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:13`
requires **each load-bearing claim** to rest on a row that is **tier A for that
claim's scope**, not merely a source that discusses the right scope.
The source contract at
`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-30`
distinguishes B (strong secondary) from A, and lines 52-55 explicitly leave
admission in QUALITY.md rather than creating a second method. Candidate
line 125 correctly repeats the tier-A requirement, so the candidate is internally
contradictory as well.

**Concrete literal-execution counterexample [INFERENCE, not an actual admission].**
An entry's only support for a load-bearing format-layout claim is an opened,
located, reproducible expert write-up classified B. The claim exactly matches
that row's scope. The §3 decision table permits sole support; Q01 still fails
because no scoped tier-A support exists. A fresh agent using the advertised
decision table could therefore admit or recommend a coverage entry under a
weakened bar.

**Impacted axes.** Scope/admission fidelity and coverage-K quality; this is an
unsupported admission route, not a disagreement about the source's usefulness.

**Smallest safe correction.** Change the B cell to “No, not for a load-bearing
claim under this lane's Q01; supplementary support only.” Keep the tier
definition and QUALITY.md's scoped-A requirement unchanged.

## Sweep, disposition, and bounds

The sweep read the entire candidate and cross-checked the frozen claims/counter/
red-before receipt, QUALITY.md, SOURCES.md and its frozen source contract,
SHONEN.md, PROVINCE.md, SCORECARD.md, the fixture generator/truth, and the
icon-state/named-icon receipt implementations. This is not an assertion that
every source URL, cited entry, or operational command was independently replayed.

All three findings are fixable instruction defects, not a tradeoff requiring an
axis sacrifice. They provide no clean non-author verification for SHONEN `[x]`.
No formal judge, admission, integration, or promotion decision is made here.

Only this authorized report was edited. The Git command above was read-only.
No tests, producer/replay runs, generator execution, other runtime, git/jj
mutations, production edits, or tool installations were performed.

## Focused follow-up on corrected candidate

After the author reported corrections, inspected the changed provenance,
fixture-reproduction, tier, and execution sections of candidate SHA-256
`23e61e722947baf893bac00e858d59547bd98f46ada5151910fc10d39d558c9f`.
This was a focused correction check, not another complete review.

- The header now separates the baseline, round-64 contract commit, and
  uncommitted controls. The new contract identity
  `3bb430f96cac09feb7269c5c52725127c6f7c463:reports/round-64/claims.md`
  exists: the corresponding read-only `git cat-file -e` lookup exited 0.
- Both reproduction instructions now require a scratch copy and explicitly
  prohibit regenerating the frozen originals in place.
- Tier B now explicitly cannot be sole support for a load-bearing claim.

These textual changes address the three original counterexamples; their
historical evidence above remains bound to the original hash.

### Remaining frozen-invocation mismatch

**Sentence:** corrected candidate lines 152-154 still say “Invoke from the lane
root exactly as frozen” before the relative probe command.

**Evidence:** the actual frozen contract,
`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:84-86`,
requires **cwd=/**. Lane-root invocation is not the registered invocation.

**Counterexample/harm:** a fresh agent following the instruction literally can
produce a lane-root receipt but cannot truthfully present it as the specified
cwd=/ measurement. This is a procedural evidence-fidelity defect; no differing
counter output or cwd-sensitive failure is asserted.

**Impacted axes:** provenance and calibration-measurement reproducibility.

**Smallest safe correction:** require cwd=/ and name the frozen probe by its
absolute lane path, with absolute TREE and lane-owned TMPDIR, rather than
claiming that lane-root invocation is frozen. No probe execution is needed to
repair the instruction. This finding was sent to the author; no corrected
follow-on hash is covered by this report, and no clean-review decision is made.

## Final targeted correction check

Confirmed candidate SHA-256
`b3b0af1d8d3d65f0246ee30e580d36c93b21998629d587772d9f43f83fabba5a`
with a direct hash, and read its header plus §6.1.
Lines 7 and 153-157 now explicitly require cwd=/, absolute probe/tree paths,
and lane-owned TMPDIR, and reject presenting lane-root invocation as registered.
The remaining invocation counterexample is addressed in the instruction text.

All findings raised by this seat have corresponding textual corrections in
the reviewed revisions. This closes the assigned attack; it is not a full
re-review of the final candidate or an admission, checklist-pass, judge,
integration, promotion, or executed-counter decision. No tests or counter runs
were performed.

Report: .ufo/waves/round-64/R64CriticSkill.md
