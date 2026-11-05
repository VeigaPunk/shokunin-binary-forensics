# Round 94 — drift verdicts for the S498 / S499 re-opens (seat ScoutReopen)

Seat: `ScoutReopen`. Date of the checks: 2026-11-05. Read-only drift check of two
already-registered sources (S054, S075) to produce the two new source rows S498 and
S499 that the frozen C1 claim rests on. No lane file was read-modified; no tool was
executed against REA.

## What was fetched (byte-exact, both HTTP 200, no fallback needed)

| sid | URL used | status | bytes | sha256 of body |
|---|---|---|---|---|
| S498 | `https://raw.githubusercontent.com/morluto/rea/main/README.md` | 200 | 30064 | `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba` |
| S499 | `https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md` | 200 | 115812 | `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267` |

Both `main`-branch raw URLs returned 200 on the first attempt, so the documented
fallback (GitHub API / github.com README page) was not needed. Each body was fetched
a second time and hashed identically (`raw/README.recheck.md`,
`raw/installation.recheck.md` in scratch) — the fetch is reproducible.

`main` at fetch time = commit `fe677f6cf9853fb12490dfb8ef23ccae3a551049`
(2026-11-05T10:38:12Z, GitHub commits API).

The bodies are committed under this wave dir:
`.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/S498.body` and `.../raw/S499.body`,
with receipts `.../receipts/S498.receipt.json` and `.../receipts/S499.receipt.json`
(schema `revenger-quote-audit-v1`).

## Baseline for the comparison

The comparison baseline is the pinned revision both old rows cite —
commit `0cd7ef456bf960da265e04b341e82a24b1e377d5` (2026-10-27), fetched here read-only
from the same raw host:

| file | pinned sha256 / bytes | current sha256 / bytes |
|---|---|---|
| `README.md` | `783d630690c5169122965ae3a00b7714e7c9f83b9328afe3649e95cca70636a5` / 29447 | `cb5b40c…b6ba` / 30064 |
| `docs/installation.md` | `c4a16fa00f39d08267098dc56c688a008cc6455a0dc3024baf333b95770003ac` / 105202 | `f05249e6…2267` / 115812 |

Both pinned sha256 values equal the ones recorded in the round-74 receipts
(`.ufo/waves/round-74/quote-audit/S054.receipt.json`, `…/S075.receipt.json`), so the
baseline is the same byte set the old rows were verified against.

## Row verdicts

### S498 (re-open of S054) — verdict: `no-drift`

S054's scope cell: *"The repository's own declared REA scope across binary,
application and runtime inspection; not capability, host readiness, tool accuracy or
completeness"*. The current README's declared tool-family scope is unchanged.

Located evidence:

- **Scope sentence, byte-identical.** `README.md:65` (current) reads
  *"REA connects your agent to tools for inspecting native binaries, JavaScript and
  Electron apps, .NET assemblies, and websites. You can also use the same tools from
  your terminal. Analysis runs locally, and results include the evidence and
  limitations behind each conclusion."* — the first sentence is byte-identical to the
  S054 anchor quote and to the pinned `README.md:63`; the "evidence and limitations"
  exclusion is still present in the same sentence.
- **Family table, unchanged.** The "What you can analyze" table has 38 `Target` rows
  in both revisions and the `Target` column is byte-identical row-for-row (diff of the
  two `^| ` blocks differs on exactly one line, the "Native binaries" *provider*
  cell). The runtime-inspection rows the scope cell names — `Desktop installations`,
  `Process behavior`, `Recorded Linux crashes` — are present in both.
- **Section structure, unchanged.** `grep '^#'` over the two READMEs is empty-diff:
  the same headings, including `## How REA works` (current `:176`, pinned `:171`),
  the section the old row's anchor names.

**Adjacent change inside the native-binary family (scope-neutral, recorded not
hidden):** the declared *engine* set for the "Native binaries" family gained `Kuna` —
`README.md:197` (current) reads `Hopper, Ghidra, IDA or Kuna; …` where the pinned
`README.md:192` read `Hopper, Ghidra or IDA; …`; the overview paragraph at
`README.md:67` likewise now reads "an existing Hopper, Ghidra, IDA or Kuna
installation"; and the FAQ heading changed from "Do I need Hopper, Ghidra or IDA?"
(pinned `:344`) to "Do I need a native analysis engine?" (current `:349`). This is a
provider addition inside an unchanged family, not a change of the declared family set,
and it does not weaken the scope cell: the README still declares only what its own
text declares and still carries the "evidence and limitations" wording. It does not
contradict any claim in the re-grounded entry, which never enumerates REA's native
engines.

Conclusion: the S054 scope cell still describes the current README's declared
tool-family scope. Verdict `no-drift`, with the engine-set addition noted above for
the L1.

### S499 (re-open of S075) — verdict: `no-drift`

S075's scope cell: *"The project's setup preview and approval statements only; not
evidence of installation or readiness on this host"*. The installation docs' approval
statements are unchanged in the located instance, and the approval boundary still
stands.

Located evidence:

- **Approval statement, byte-identical and at the same place.**
  `docs/installation.md:4` (current) reads *"Setup previews configuration changes and
  asks for approval before applying them."* — byte-identical to the S075 anchor quote
  and to the pinned `docs/installation.md:4`, same character span `107..187`.
- **Anchor headings still present.** `# Installation and setup` and
  `## Review setup changes` (current `:36`, pinned `:36`); the full heading list of
  the two revisions is empty-diff (same twelve `##` headings), so no approval section
  was renamed or removed.
- **Approval boundary still gates writes.** `docs/installation.md:1192` — "Setup never
  installs Ghidra, Java, or Python. It preserves verified …" (pinned `:1097`, same
  wording); the write-then-verify ordering is unchanged.

**Adjacent additions around the approval statements (scope-neutral, recorded not
hidden):** the current revision adds approval-adjacent detail that the pinned revision
did not have — a documented unattended-approval path (`docs/installation.md:707`
"To approve Hopper installation without prompts, run `rea setup --yes --install-hopper`",
which is the pre-existing `--yes --install-hopper` route restated as an approval
instruction; the flag itself already existed at pinned `:151`, `:754`, `:769`), a
pre-approval macOS-version check (`docs/installation.md:736` "cannot confirm support
before approval. Setup compares this Mac's version with the release metadata's
`deployment_target` before downloading the DMG"), a dry-run approval path
(`docs/installation.md:401` "…`rea setup --client <client-id> --skill=false --dry-run`
from that terminal and approve it to record the settings"), and a new "Readiness
check" table (`docs/installation.md:381`) whose `One analysis engine` row now also
lists `jadx` and `kuna`. Every one of these is still an *approval* statement — the
approval boundary is strengthened or restated, never bypassed: `--yes` is the
operator's own pre-granted approval and it already existed in the pinned revision.
Nothing in the current revision claims installation or readiness on this host.

Conclusion: the S075 scope cell still describes the current installation docs'
approval statements. Verdict `no-drift`, with the additions above noted for the L1.

## Summary

| sid | source re-opened | baseline | verdict | the located evidence |
|---|---|---|---|---|
| S498 | REA root `README.md` (main, 2026-11-05) | S054 @ `0cd7ef45` | `no-drift` | `README.md:65` (scope sentence byte-identical); 38/38 `Target` rows identical |
| S499 | REA `docs/installation.md` (main, 2026-11-05) | S075 @ `0cd7ef45` | `no-drift` | `docs/installation.md:4` (approval statement byte-identical, span 107..187) |

Both re-opens are `verified` under `corpus/audit_source_quotes.py` over the committed
bytes: `S498 terminal=S498 state=verified (ok)` / `S499 terminal=S499 state=verified
(ok)`, `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`, exit 0.
