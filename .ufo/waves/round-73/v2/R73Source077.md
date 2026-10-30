# R73Source077 — S077 source audit (round-73, wave v2)

Seat: R73Source077 (critic, leaf — no subagent dispatch). Assignment: reopen SOURCES.md row S077,
compare located quote VERBATIM, scope, tier, used-by, rejection flip. Report only this row.
Lane root: /home/vgpnk/Projects/shokunin/revenger-shokunin.

## Verdict

**AGREE with source disposition.** S077 stands as written: tier A, `mined`, 2026-10-27, on-release,
used-by `corpus/knowledge/round-72-tool-landscape.md`. No quote defect found → **no superseding row
proposed** (append-only supersession is reserved for the routed S071/S082 defects; S077 is not flagged
in `corpus/lessons/round-72-verifier-spotcheck.md` and my independent reopen confirms it).

## Located quote (verbatim, 14 words ≤ 25)

> "Exact static equality is not runtime compatibility, ABI compatibility, linking success or source identity."

- Access date (this seat): 2026-10-30. Original access recorded in row: 2026-10-27.
- URL: https://github.com/morluto/rea/tree/0cd7ef456bf960da265e04b341e82a24b1e377d5/docs/specs/2356-wasm-interface-comparison
  (raw files re-fetched at the pin: `.../spec.md`, `.../verification.md`, both HTTP 200).

## Evidence

### 1. Pin and path [observation]

- GitHub API: commit `0cd7ef456bf960da265e04b341e82a24b1e377d5` exists in `morluto/rea`,
  committer date 2026-10-27T17:13:17Z. Directory listing at that ref for
  `docs/specs/2356-wasm-interface-comparison/` returns `plan.md`, `spec.md`, `tasks.md`, `verification.md`.
- Pinned raw fetches (2026-10-30): `spec.md` 3538 B HTTP 200; `verification.md` 2702 B HTTP 200.
  A commit-pinned tree is immutable, so 2026-10-27 and 2026-10-30 accesses return identical bytes.
- Local checkout `~/.local/share/rea` (read-only, HEAD `12f6e09`) does NOT contain the pinned
  object — verification therefore rests on the network reopen, not the local tree.

### 2. Quote verbatim [observation]

`spec.md` section `## Comparison contract`, final sentence (byte-identical after markup
normalization; file is plain Markdown, no transformation needed):

    Report unknown coverage and explicit limitations. Exact static equality is not
    runtime compatibility, ABI compatibility, linking success or source identity.

Corroborating variant in `verification.md` `## Scope and measurement limits`:
"Static equality is not runtime compatibility." — consistent, shorter; the row's quote uses the
full form, which lives in `spec.md`. No conflict.

### 3. Cited sections [observation]

- `spec.md`: headings `## Comparison contract` and `## Authority and overlap` both present. ✓
- `verification.md`: heading `## Scope and measurement limits` present ✓; "Real WABT" appears as
  the lead of a verification bullet ("- Real WABT 1.0.42 comparison through compiled CLI and stdio
  MCP passed: ..."), not as a section heading (the file's headings are `## Independent review` and
  `## Scope and measurement limits`). The row's `"Real WABT"` is a passage locator, not a heading
  citation; it locates real content verbatim. Minor notation nuance, not a quote defect.

### 4. Scope and tier [observation]

- Row scope: "One feature-specific WASM Evidence-comparison contract and the repository's own
  verification record at the pinned REA tree; not a repo-wide clean-room protocol or independent
  re-run by this lane." Supported by source text: "This is a derived workflow within existing WABT
  inspection authority, not a new provider"; the spec is feature issue #2356, comparing "two exact
  authenticated `inspect_wasm_artifact` Evidence inputs"; `verification.md` is a first-party receipt
  ("Verified base: a2d8b94...", "8 files / 56 tests passed", "Real-tool verification covers macOS
  arm64 only; Linux/Windows remain unverified").
- Tier A agree: first-party spec plus first-party verification receipt at an immutable commit,
  honestly scoped to the feature; limitations cell ("limits comparison to authenticated supplied
  evidence and preserves unknowns; ... first-party reported verification, not a test this lane
  ran") is directly supported ("Authenticate Evidence before projection", "Unsupported type/proposal
  forms remain unknown ...").

### 5. Used-by [observation]

`corpus/knowledge/round-72-tool-landscape.md` cites S077 at lines 4, 30, 38, 67 with matching
scope language ("feature-specific ... not a repository-wide SPEC.md or general clean-room protocol";
"its first-party receipt as independently rerun here" — explicitly not). The C10 candidate
`corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md` does not cite S077 (grep empty);
S077 is outside the S096–S109 C10 source set — consistent with the frozen claim.

### 6. Rejection flip [observation]

None. Admission is tier A with explicit limitation language; no rejected source is promoted, and
no admitted scope is silently broadened. The round-72 lesson (`corpus/lessons/round-72.md` row 36)
carries the same verbatim quote and the same tier-A-with-limits decision; the row, the lesson, and
the used-by entry agree.

## Network / source failures

None. Both pinned raw URLs and the GitHub API responded HTTP 200 on 2026-10-30.

## Tooling record

No installs or updates performed; pacman pause honored. Used pre-existing host tools only:
curl 8.x (official Arch package, already installed) and git (already installed) for network reopen
and API checks. No writes outside this report and scratch
`/fast/scratch/hyaku/revenger-r73/R73Source077/` (fetched `spec.md`, `verification.md`, `s077row.txt`;
scratch removed after receipts copied here).
