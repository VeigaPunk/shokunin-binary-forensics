# R70W2Quarantine — quarantine hand-check (addendum §10) + id-collision guard

**First-line verdict:** Register rows S054/S099 are **UNVERIFIED-REACHABLE** (both cited sources fetch HTTP 200 today; the register recorded **no quote** for either — that is the `unverifiable-unreachable` class, not fabrication); staged Unblob rows verify **PRESENT** verbatim on their anchors (S054 release API 3/3; S099 README headers/feature line/install line), with two sentence-level near-miss quotes inside citing entries; id-collision guard: **archived snapshot collisions = 1 (S047), live registry collisions = 3 (S047/S048/S049)**; renumber map for the Unblob rows = **identity** (S054/S099/S152 need no renumber), colliding staged rows → S047→S202, S048→S203, S049→S204.

---

## 0. Method and independence

- Primary sources only: the frozen register `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` (READ-ONLY), the lane's derived slice `.ufo/waves/round-70/assimilation/quarantine-slice`, the lane registry `corpus/SOURCES.md`, and the merge package `/home/vgpnk/Projects/shokuknow/merge/revenger/` (SOURCES.append.md, knowledge entries, ID-REMAP.md). All fetches executed by me today (2026-10-25) with `curl -sL --max-redirs 15`; bytes saved under `/tmp/revenger-r70-quarantine/` (deleted before return).
- No edits to any lane/campaign file. No tools installed (curl + python3 stdlib only).
- The wave-1 report (`.ufo/waves/round-70/w1/R70W1AssimUnblob.md`) was **not** read before these verdicts were formed; the grep fragments of it surfaced only as cross-check material afterward (its D1 claim "both fetch HTTP 200 and the three quotes verify" is compared below).

## 1. Slice identification

The slice (26 lines) is the revenger-lane projection of the register: 24 `payload-absent` rows + 2 prose/fetch-failure rows `S054`/`S099` (slice:25-26), whose register text is exactly *"the cited source could not be fetched, so no quote was checked"* — i.e., the register's **never-checked** section (register lines 359-360), **not** the payload-absent section. These rows therefore carry **no quote** in the register.

Register rows:
- S054 (revenger r1) → cited source `https://source.android.com/docs/core/runtime/dex-format` — never-checked, no quote.
- S099 (revenger r3) → cited source `https://developer.android.com/tools/apkanalyzer` — never-checked, no quote.

"Any other Unblob row": the slice contains no further Unblob row. In the **staged** space (SOURCES.append.md), the Unblob rows are staged **S054** (Unblob release 26.6.4 API, line 14), staged **S099** (unblob README tier A, line 59) and staged **S152** (Unblob project README tier B, line 112); staged S069 (REA `FirmwareRelease.ts`) pins Unblob versions but is a REA code row. ID-REMAP.md confirms staged ids S047–S201 (lane registry ended at S046 at packaging; first staged id S047).

## 2. Per-row verdicts (fetch today)

| row | cited source (register) | fetch today | register quote | verdict |
|---|---|---|---|---|
| S054 (revenger r1) | https://source.android.com/docs/core/runtime/dex-format | **HTTP 200**, 281157 B, sha256 `183c0a9b21d736a2e4230c3bfc164f7300af9a1abe526ee7e924ee3dc97f3e3d` | none recorded | **UNVERIFIED-REACHABLE** (fetchable; nothing ever checked) |
| S099 (revenger r3) | https://developer.android.com/tools/apkanalyzer | **HTTP 200**, 280117 B, sha256 `a6e6250ef8bf048af8f48042271de250e5292490b3dfebf5f106620835fbe7b5` | none recorded | **UNVERIFIED-REACHABLE** |

Neither row is PRESENT or ABSENT: there is no quote on record to locate. The slice's "could not be fetched" classification is **false as of today** — both sources are fetchable. (Both fetched pages also contain the anchors other staged rows use: the dex-format page contains the title "Dalvik executable format" [reg_s054.bin, 2 hits]; the apkanalyzer page contains "apkanalyzer" [reg_s099.bin, 3 hits].)

## 3. Staged Unblob rows (what the candidate entries cite) — verified against today's bytes

**Staged S054 — Unblob release 26.6.4 API** (`https://api.github.com/repos/onekey-sec/unblob/releases?per_page=10`; fetched 200, 74527 B, sha256 `63ecb211b65b8bae07a616949068f18b771223fef23da6ebefed7d6826013f7a`):
- `"tag_name": "26.6.4"` ✓
- `"published_at": "2026-06-04T08:52:43Z"` ✓
- asset `unblob-26.6.4-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl` digest `sha256:0fc16e9c7dc92fcf86b8b61475700c9dd16e1dddacf34467574ea965a5d3584e` ✓ (entry's full digest matches byte-for-byte)
- Verdict: **PRESENT** (3/3 anchors verbatim).

**Staged S099 / S152 — unblob README** (`https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md`; fetched 200, 7580 B, sha256 `6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716`):
- `## Features` header ✓; `## Installation` header ✓ (2 hits)
- `**Accurate, fast, and easy-to-use extraction suite for binary blobs.**` ✓ verbatim
- `**78+ supported formats** — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4, and many more.` ✓ verbatim
- `Verify that all extractors are available: unblob --show-external-dependencies` ✓ (3 hits)
- install line `sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4` ✓ verbatim
- Verdict: **PRESENT** on the staged row anchors.

**Near-miss flags in citing-entry sentences (do not change the row verdicts; matter to adoption-time quoting):**
1. `digest-scope-versus-provenance-amendment-2026-10-23.md:43-44` quotes upstream as "Requires Python ≥ 3.10, uv, and a Rust toolchain (for the compiled extensions)". Today's bytes read `Requires Python ≥ 3.10, [uv](https://docs.astral.sh/uv/), and a Rust toolchain (for the compiled extensions).` — the markdown link around "uv" is omitted → **not byte-verbatim** (semantically identical).
2. `firmware-gate-is-reas-own-rule-and-the-host-matches-it-2026-10-24.md:41-43` says Unblob's README "says it parses unknown binary blobs for archive, compression and file-system formats, extracts their content recursively and carves unknown chunks". Today's bytes read `unblob parses unknown binary blobs for **78+ archive, compression, and file-system formats**, extracts their content recursively, and carves out unknown chunks.` — "carves out" vs "carves", bold `**78+` wrapper, punctuation → **near-miss, not verbatim** (the entry flags this as "says", i.e. a description, but the quoted span is not exact).

Wave-1 D1 ("both fetch HTTP 200 and the three quotes verify") is **confirmed on fetchability and on the staged-row anchors**; the "three quotes verify" needs the near-miss qualification above.

## 4. Id-collision guard replay (as in `assimilation/`)

Method (round-67 precedent, R67CriticAssim): registry ids = rows of `corpus/SOURCES.md`; staged ids = merge-package ids (`SOURCES.append.md`); collisions = `comm -12 <(sort reg-ids) <(sort staged-ids)`.

**Archived snapshot (`.ufo/waves/round-70/assimilation/`):**
- `reg-ids`: 47 lines S001–S047 · `staged-ids`: 155 lines S047–S201 · `collisions`: {S047} → **count 1** (recomputed: `comm -12` → 1). `guard-reg-ids` = S050, `guard-collisions` = S050.

**Live re-run (registry now ends at S049):**
- Live registry from `corpus/SOURCES.md` registry rows: 49 ids **S001–S049** (staged-ids identical to the archived list, verified by diff).
- `comm -12` → **{S047, S048, S049}** → **count 3**. The archived `reg-ids` is stale by exactly S048/S049 (diff: only `> S048`, `> S049` added), i.e. it was captured before the round-70 S048/S049 mint (SOURCES.md rows S048/S049 dated 2026-10-25).

**Renumber map** (by-document obligation; must avoid both the registry block S001–S049 and the staged block S047–S201; first free ids above the staged max S201 are S202+):

| staged id | staged row (document) | collision? | new id |
|---|---|---|---|
| S047 | REA `docs/firmware-analysis.md` (round1) | yes (lane S047 = AXML anchor derivation, own-work) | **S202** |
| S048 | REA `docs/managed-code-analysis.md` (round1) | yes (lane S048 = DEX spec AOSP) | **S203** |
| S049 | REA `docs/android-analysis.md` (round1) | yes (lane S049 = REA android-applications ref) | **S204** |
| **S054** | **Unblob release 26.6.4 API (round1)** | **no** (S054 > S049) | **S054 (identity)** |
| **S099** | **unblob README (round3)** | **no** | **S099 (identity)** |
| **S152** | **Unblob project README (round8)** | **no** | **S152 (identity)** |

Collision count to report: **3** (live). The Unblob rows need no renumber — the identity map holds for all three.

**Caveat:** if, instead of renumbering the staged collisions, the lane mints a *new* registration row for Unblob before appending, the next registry id would be **S050**, which collides with staged S050 (REA `src/android/JadxRelease.ts`); then staged S050 → S205 (or the Unblob row takes an id above S201).

## 5. Evidence pointers

- Register rows: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:359-360` (never-checked section, S054/S099).
- Slice: `.ufo/waves/round-70/assimilation/quarantine-slice:25-26`.
- Staged rows: `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md:14` (S054), `:59` (S099), `:112` (S152), `:7-9` (S047-S049); `lanes/revenger/ID-REMAP.md:5-8`.
- Lane registry end: `corpus/SOURCES.md:62-63` (S048/S049 rows; registry 49 rows).
- Guard files: `.ufo/waves/round-70/assimilation/{reg-ids,staged-ids,collisions,guard-reg-ids,guard-collisions}`; live recompute outputs in scratch (deleted): live-collisions.txt = {S047,S048,S049}.
- Fetches today (all HTTP 200): dex-format 281157 B sha256 `183c0a9b…`; apkanalyzer 280117 B sha256 `a6e6250e…`; unblob releases API 74527 B sha256 `63ecb211…`; unblob README 7580 B sha256 `6544d60f…`.
- Entry near-misses: `digest-scope-versus-provenance-amendment-2026-10-23.md:43-44`; `firmware-gate-is-reas-own-rule-and-the-host-matches-it-2026-10-24.md:41-43`.

## 6. Summary

- **S054 (register)**: UNVERIFIED-REACHABLE — fetchable today, no quote ever recorded. Staged S054 (Unblob release): **PRESENT**, 3/3 anchors verbatim.
- **S099 (register)**: UNVERIFIED-REACHABLE — fetchable today, no quote ever recorded. Staged S099/S152 (unblob README): **PRESENT** on row anchors; two entry sentence-quotes are near-misses (flagged).
- **No other Unblob row** exists in the slice.
- **Id-collision guard**: archived 1 (S047); live 3 (S047/S048/S049). **Renumber map: Unblob rows identity (S054/S099/S152); staged S047→S202, S048→S203, S049→S204.**
