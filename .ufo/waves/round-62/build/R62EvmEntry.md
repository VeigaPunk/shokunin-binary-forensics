RESULT: COMPLETE

# R62EvmEntry — round-62 C09 candidate entry (revised narrow form, draft only)

Seat `RevengerR61-2.R62EvmEntry` (leaf). Frozen revision
`a3498e25ad87bf756288812d0ea7c474b09433c7` (tree
`f53a42f2eb5baa9fa999f8bcf2b7e8145d2309c7`), extracted read-only via
`git -C …/revenger-shokunin archive a3498e25… | tar -x -C
/fast/scratch/hyaku/revenger-r62/R62EvmEntry/frozen`; all execution ran on that
copy or on scratch files, cwd=/ for the recorded run. The complete draft entry
is a separate scratch file, per the report line budget.

**Proposed entry (draft, scratch only):**
`/fast/scratch/hyaku/revenger-r62/R62EvmEntry/candidate.md` — 450 lines, 42839
bytes, SHA-256
`2003e39936f2191d26402056d499e86f459346c73002a1039249efe437ccf6fe`.
Intended landing path `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`
is **not** written by this seat; L1 integrates it.

**Revised to the L1 integration directive.** The earlier 1448-line draft with a
second pointer script is superseded. The candidate now has **one** stdlib
readout, `readout.py` (131 lines, SHA-256
`740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb`), which takes
**only the archive root** as its argument, reads no specification file, no
sibling git object, no verifier and no ledger, executes no bytecode, and prints
one compact JSON object per case plus one summary object (8 stdout lines, SHA-256
`aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf`). The
`pointers.py` script and its output are deleted from the scratch directory. The
entry is 449 lines with a 67-row sentence→output inventory whose every value is
read back out of the recorded JSON by the builder, so the table cannot drift
from the output.

**What the entry now contains, and what it dropped.** It keeps the full SHA-256
of every carrier file, decoded byte string and saved record; the per-case
digest scope labels (which exact byte string each of the subject, artifact and
bytecode digests covers — `carrier_file_bytes_only`,
`decoded_bytecode_bytes_only`, `carrier_and_decoded_same_byte_string`); the
recorded metadata and identifiers (operation, provider id/name/version,
evidence id, authority, confidence, predicate type, the three flags, artifact
and bytecode fields); the full instruction tuples (offset, opcode, immediate
bytes) with opcode counts; the JUMPDEST set on instruction boundaries; the raw
`0x63` and `0x5b` byte offsets; and for r24 the pattern occurrence count (1),
its start ([1]) and inclusive span ([[1, 9]]), the embedded PUSH1 opcode and
operand offsets (7, 8) and operand value (16), the embedded target offset (16),
the byte there (0x00) and that it is not a raw `0x5b` byte. The six competing
count sets are gone: only `total_cases` (7), `reported_candidate_observations`
(4) and `distinct_candidate_pairs` (3) remain, kept apart, with
`raw_and_normalized_pair_counts_equal` alongside. The cross-lane note now says
only that ADJ-06 remains unresolved and that no citation from the rejected
round-61 candidate is reused, citing this round's own
`corpus/lessons/round-62.md` and `.ufo/waves/round-62/build/R62DebtExistingFiles.md`
rather than any new outside claim. The opcode byte values and the
valid-jump-destination rule are documented as recorded source facts from S028
under a `## Source facts (recorded)` section, not re-derived and not executed.
No post-hoc rule fit, no cause, no signature claim, no `truth.json` reading, no
verifier introspection and no guard credit anywhere in the file; Q13 is answered
by naming every clause unguarded. The `## Q01-Q13 decisions` table is labelled
as the author's proposed readings, not self-admission. No Q14 is proposed.

**Commands and exits** (all stderr empty). `git archive a3498e25… | tar -x -C
…/frozen` → 0. `curl -sS -m 60` for the two `execution-specs` files at tag
v2.20.0 and for the GitHub tag/commit metadata → 0. `python3 -B readout.py
frozen > readout_stdout.txt 2> readout_stderr.txt` → **exit 0**, 8 stdout lines,
empty stderr. `python3 -B build_entry.py` → 0. **Final reproduce:** the
`## Reproduce` block was extracted from the finished `candidate.md` into
`extracted_readout.py` and run against the frozen copy → **exit 0**, empty
stderr, stdout **byte-identical** to the recorded
`readout_stdout.txt` (both SHA-256
`aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf`); a second
run of `readout.py` produced the identical digest, so the output is
deterministic. A run with the wrong root fails loudly with `FileNotFoundError`
rather than emitting partial output.

**Residual defects fixed at L1's instruction (prose only, output unchanged).**
The malformed sentence at old line 138 is now "proposes **no** rule that would
produce it, and asserts no cause". The compiled-bytecode bullet no longer
asserts absence ("None of these appears in these seven files") and now states
that those features are outside this entry's claim and are not examined here.
`authority` is now "recorded and is **not read** as origin, custody or
authenticity", and the `local_path` claim — the field is not printed by the
readout — is deleted. The `evidence_id` bullet now says this entry does not
address, recompute or authenticate the recorded identifiers and claims no
formula for them. The inference bullet is scoped to "each non-empty saved
result in this sample (r19, r21, r22)" and notes that the other four records
report no pair, so no offset is available there. The `## Source facts (recorded)`
section now also quotes the constants the walk uses that S028 anchors —
`STOP = 0x00` (:104), `POP = 0x50` (:118), `PUSH0 = 0x5F` (:121),
`PUSH1 = 0x60` (:122), `PUSH32 = 0x7F` (:153) — all inside L1's S028 anchor
ranges `:104-109`, `:118` and `:121-153`. These are prose-only edits: the
embedded code and stdout are unchanged, and a confirmation run of `readout.py`
against the frozen copy exited 0 with empty stderr and produced the same
`aff3efda2…` digest.

**Mechanical checks over the finished entry.** The embedded code equals
`readout.py` and the embedded stdout equals the recorded file (both byte-equal);
all 67 inventory rows' pointers resolve to the recorded JSON and every printed
value equals the JSON's value (**0 mismatches**); no truncated digest appears
(anywhere in the file; the digests are the full 64-hex values printed by the
readout); and the strings `kasegi`, "every statically valid", "post-hoc",
"37 single", the rejected round-61 entry's filename, `truth.json`, `local_path`
and "file-class label" are all **0 occurrences**.

**Preservation and non-claims.** `git status --porcelain` shows only
`?? .ufo/waves/round-62/` (other seats' reports); `git diff --stat a3498e25 --
corpus/` is empty, so no fixture, saved record, README or SOURCES byte changed;
`corpus/README.md:33` (C04) and `:38` (C09) still read `uncovered`; no row
flipped, no held token added, no admission, gate or promotion claimed, prior
rejected candidates byte-preserved.

**Risks / unknowns (honest).** S028 and S031 are reserved ids; if L1 does not
write those rows from the recorded source facts printed in the entry, the Q01
basis cell fails on a missing row, not on a missing derivation. The offset
convention is stated only for these seven authored fixtures. The provider id,
version, evidence id, authority and confidence are recorded fields of the saved
files, not authenticated; no present producer capability is claimed. The
readout is a manual comparison against the saved records and is **not** claimed
to be deletion-sensitive; no mutant run over it was performed, and
`corpus/verify_evm_evidence.py` is credited for no clause. The census
constraint measured earlier still binds L1: an S031 `used-by` path that does not
exist at validate time produces `E11` and exit 1, so the entry file and the row
must land together.

**Proposed changes.** None applied to the lane tree. The only proposed change
is the new file `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`, to
be created by L1 from `candidate.md` verbatim at the digest recorded above.

Installs / updates: **none**. No pacman, uv, cargo or npm transaction; no
service restart. Tools: `git` (read-only), `curl` (read-only fetch of two public
specification files and GitHub tag metadata), `python3` 3.14.8 stdlib only.
