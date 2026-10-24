# R64SourcesRows — S036/S037 registry-row draft

Seat: scribe. Round 64 (revenger), attempt hyaku. Leaf seat: no blocking on peers.
Deliverable: `.ufo/waves/round-64/sources-rows-draft.md` — two rows (S036, S037) per
`SOURCES-CONTRACT-v1.md`; status left `queued` for L1. No corpus edit, no commit, no
git/jj mutation, no installs.

## 1. Behaviour

1. Read the frozen inputs: `reports/round-64/claims.md`, `reports/round-64/measure.py`,
   `reports/round-64/measure-before.log`, the fleet contract
   `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, and the
   registry shape in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`
   (11 columns, NF=13 in `awk -F'|'`, no `|` inside cells).
2. Took S036 facts from the already-opened snapshot supplied by seat `R64SourceReaGuide`
   (`.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` and
   `rea-firmware-guide.provenance.json`) — the seat did the fetch; this seat did not
   re-fetch and did not rerun any provider.
3. Computed S037 sha256s **from the claim base commit**
   `666ea84b6be2eec2b0359f556ba2429fc9044c36` with
   `git show <base>:<path> | sha256sum`, then re-checked the working tree with
   `sha256sum`; all six values are identical at base and in the working tree.
4. Read the three JSON records (read-only) to ground the S037 `teaches` sentence:
   image is 2048 bytes; `receipt.fixture_sha256` = `truth.json.image.sha256` =
   `inspection.json.subject.digest.sha256` = `bdfe9f46…8510be`;
   `receipt.stdout_sha256` = file sha256 of `inspection.json` (`f6997835…aa71f9`);
   `truth.json.regions` has 5 entries, 2 of kind `zlib` at offsets 512 and 1024;
   `inspection.json.provider` = binwalk 3.1.0, `operation` = `inspect_firmware_regions`,
   normalized regions 512/1024 with `reported_size` 79/90 and
   `size_basis=provider_reported_validation_unknown`.
5. Wrote the two rows in the draft, with the contract's header and separator line plus a
   short provenance note. No `|` inside any cell.
6. Ran the contract's mechanical census checks against the draft (not against
   `corpus/SOURCES.md`, which this seat did not edit).

## 2. Draft content (summary)

- **S036** — kind `docs`, tier `A` scoped to **route-scope sentences only** (what
  `inspect-firmware-regions` returns and bounds per `rea-agents-6.5.0`); anchor pins tag
  `rea-agents-6.5.0` (`refs/tags/rea-agents-6.5.0` → commit
  `3b79af28e80785afce9f5998d8f03289402a1847`, blob
  `152819177f8dce2124dea2a6a541e701cee227ed`), headings "Firmware analysis",
  "Caller-supplied tools", "CLI and MCP" with "### Interpret the results", "Resource and
  lifecycle policy", "Verification", route text lines 56-124, snapshot 213 lines /
  10695 bytes / sha256 `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`.
  Source URL cited is the pinned-tag raw URL used for the snapshot. Status `queued`,
  opened `2026-10-24`, recheck `on-release`, used-by the new C07 entry.
- **S037** — own-work bundle of all six paths the brief names (fixture bytes, truth
  oracle, generator, saved inspection record, receipt, LEDGER); tier `A` for byte/record
  correspondence only; anchor carries every file sha256 and byte count **at the claim
  base commit** `666ea84b6be2eec2b0359f556ba2429fc9044c36`. Status `queued`, opened
  `2026-10-24`, recheck `on-release`, used-by the new C07 entry plus
  `corpus/lessons/round-64.md`.

| file | bytes | sha256 (base = working tree) |
|---|---|---|
| `corpus/fixtures/firmware-r63/firmware-r63.bin` | 2048 | `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` |
| `corpus/fixtures/firmware-r63/truth.json` | 1933 | `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` |
| `corpus/fixtures/firmware-r63/generator.py` | 5532 | `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` |
| `corpus/live/runs/round-63/inspection.json` | 3904 | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` |
| `corpus/live/runs/round-63/receipt.json` | 492 | `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` |
| `corpus/live/runs/round-63/LEDGER.md` | 22671 | `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6` |

## 3. Gates

| Gate | Command | Result |
|---|---|---|
| Row count in draft | `awk -F'\|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {print $2, NF}'` | 2 rows (`S036`, `S037`), `NF=13` each — PASS |
| Malformed rows | contract v1 `NF!=13` check | `malformed 0` — PASS |
| Enum / tier-inflation check | contract v1 `tier !~ /^[ABC]$/`, `status`, `kind` checks | no output — PASS |
| No pipe inside cells | column count 13 on both rows | PASS |
| S036 snapshot integrity | `sha256sum` + `wc -l -c` on `rea-firmware-guide.md` | `e422b481…3609`, `213 10695` — matches provenance — PASS |
| S037 base digests | `git show 666ea84b:<path> \| sha256sum` vs working-tree `sha256sum` | six of six identical — PASS |
| Base is ancestor of lane HEAD | `git merge-base --is-ancestor` | `a3d063f…` HEAD, base ancestor — PASS (read-only git) |
| Draft content hash at hand-off | `sha256sum sources-rows-draft.md` | `6e66fd3e078088fedcc0816fbf2e52262e0a644036014eaef3b7092387ba3d20` |

## 4. Findings

1. **Tag vs main drift is real and the draft cites the tag only.** The round-64
   provenance records `main` at 15474 bytes / `d4a25c85…a898`; the tag snapshot is
   10695 bytes / `e422b481…3609`. My S036 anchor, source URL and teaches use the tag
   snapshot; the round-63 `main` copy is not cited anywhere.
2. **No entropy text in the pinned guide.** The S036 `scope` and `teaches` therefore
   make no entropy claim: they cover Evidence fields, byte offsets in the original
   firmware, provider-reported sizes and the separately configured Binwalk prerequisite.
   This matches the `R64SourceReaGuide` finding (`grep -c -i entropy` = 0) and the
   reviewer's mechanical fact.
3. **S037 digests in this draft agree with the independent Gate-quote draft.**
   `.ufo/waves/round-64/gate-quotes.md` (seat `R64ScribeGate`) lists the same four
   primary digests plus `generator.py` and `LEDGER.md`; all six match my base-commit
   computation exactly.
4. **Base anchor is not the lane HEAD.** HEAD is `a3d063f29b93ad1f0b7eab78652c552685b84d89`
   (round-64 pre-registration commits); the claim base `666ea84b…` is an ancestor, so
   anchoring S037 at the claim base is possible and was done; the six files are
   byte-identical in the working tree.
5. **Landing precondition for the `queued → mined` flip.** Contract census treats a
   `mined` row's `used-by` paths as required-existing. Both rows are `queued` now, and
   their `used-by` names the not-yet-landed
   `corpus/knowledge/round-64-firmware-region-byte-evidence.md` (both) and
   `corpus/lessons/round-64.md` (S037). L1 must flip to `mined` only once those files
   exist; if the C07 entry is not admitted, the rows should stay `queued` (or carry
   `used-by —`) rather than cite a missing path.
6. **S037 `used-by` includes the lesson per the brief.** The lesson must contain the
   literal `S036`/`S037` mentions for the citation to be honest; `gate-quotes.md` already
   carries the old→new flip log this round needs, but the lesson file itself is a
   separate seat's deliverable.
7. **Id-space is S036/S037 by first actual use.** `scout-sources.md` found 35 rows
   (S001–S035), no S036/S037 row, and no reservation power for an unopened lead; the
   draft respects that.

## 5. Out of scope / untouched

- `corpus/SOURCES.md` not edited; no registry append, no status flip, no `used-by` edit.
- `corpus/README.md`, knowledge entries, lessons, fixtures, saved records untouched.
- No git/jj mutation, no commit, no push; the only git commands run were read-only
  (`rev-parse`, `status`, `log`, `merge-base`, `show` piped to `sha256sum`).
- No `.ufo/waves` spec/registry edit; the draft and this report are the only wave paths
  written.
- No provider rerun and no verification run: `inspection.json` fields were read, never
  regenerated.
- No installs or upgrades (pacman paused host-wide; nothing needed).

## 6. Artifact paths

- Draft: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/sources-rows-draft.md`
- This report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64SourcesRows.md`
- S036 snapshot: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`
- S036 provenance: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json`
- Independent quote/Gate draft: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/gate-quotes.md`
- Id-space recon: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-sources.md`

Report: .ufo/waves/round-64/R64SourcesRows.md
