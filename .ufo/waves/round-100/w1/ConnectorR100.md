# ConnectorR100 — sibling overlap: APK decoding capability and admission-counter leg patterns

Seat: ConnectorR100 (connector, leaf, read-only). Wave: round-100 w1. Lane: revenger (`/home/vgpnk/Projects/shokunin/revenger-shokunin`).
Paths below are relative to `/home/vgpnk/Projects/shokunin/` unless they begin with `revenger-shokunin/`. Fleet-root `.ufo/` paths are marked `[fleet]`.
Nothing was written outside this file. No command was run that mutates any lane, no git mutation, no tool installed.

## 0. Scope, method, limits

- Lanes: the 21 physical `*-shokunin` directories at the fleet root (listed by glob), against the roster table in `README.md` (13 rostered, 8 repository-link-only).
- Surfaces read: each lane's `PROVINCE.md`, `SKILL.md`, `README.md`, `corpus/` (where present) for APK/AXML/androguard/apktool/jadx terms; `tools/`, `scripts/`, `plans/`, `verifiers/`, `corpus/*.py` for admission/gate leg patterns.
- Fleet-wide grep was too noisy to use as evidence (`.ufo/` transcripts, snapshots, host package lists). Only lane-tracked surfaces and the `[fleet]` wave files cited below are evidence.
- Not covered: full bodies of most sibling counters (only grep-hit windows were read); lanes without a `tools/` or `scripts/` directory (kagi, kasegi, kumitate, lore, kotodama, mado scripts) were skipped by the path list; `.ufo/` of each lane was not scanned.

## 1. Who holds APK / AXML / decoder knowledge or capability

| Lane | Evidence | What it holds | Relation to revenger's new `apk-manifest-cross-decode` |
|---|---|---|---|
| revenger (self) | `revenger-shokunin/PROVINCE.md:3-4` | Owns "Android APKs" as shipped-artifact RE. | Owner of the proposed capability. |
| revenger (self) | `revenger-shokunin/corpus/README.md:52` | C05 "Android packages (APK)" row; `fixtures/apk-r65`; retained rejected candidates `round-65` … `round-70` entries. | C05 is still `uncovered` (`SCORECARD.md:466`, round-66 disposition). C2 scope boundary says C05 stays uncovered. |
| revenger (self) | `revenger-shokunin/corpus/SOURCES.md:52` (S038 AOSP ResourceTypes.h), `:57` (S043 REA Android reference), `:73` (S059 Apktool README), `:55` (S041 own-work apk-r65 bundle) | Spec and tool-scope sources for AXML and Apktool. | Source rows exist. The C2 row must cite round-100 opened sources (claims §C2); none exist yet at base. |
| revenger (self) | `revenger-shokunin/corpus/knowledge/round-71-apk-axml-byte-evidence.md:12` | Round-71 candidate `admission-status: rejected` (Q09, Q16). | Rejected AXML byte claims are revenger's own record. The C2 probe must not reuse their transcribed readouts. |
| kaidoku | `kaidoku-shokunin/PROVINCE.md:58` (APK surface, full), `:136` (Android deep analysis) | Routes APK inspection through REA providers: `inspect-android-package` (jadx-headless-mcp 0.7.1), `decode-android-resources` (apktool 3.0.3). | **Same surface, different route.** Kaidoku's apktool leg is REA-provider-mediated; revenger's probe calls `apktool d -s` and `androguard axml` directly. Overlap on the decoder-version axis, not on the gate. |
| kaidoku | `kaidoku-shokunin/SKILL.md:61` (Android APK route), `:76` (provider refusal keys `REA_JADX_MCP_JAR`, `REA_APKTOOL_COMMAND`) | Operator-facing routing and refusal table. | As above. |
| kaidoku | `kaidoku-shokunin/corpus/README.md:29` (`2026-10-13-r4u-02-jadx-decode`: decoded manifest on Godot APKs; apktool content-deterministic id) | Admitted knowledge on the Godot debug/release APKs. | Different artifacts (Godot templates). No authored-truth check. |
| kaidoku [fleet] | `.ufo/waves/kaidoku-r4u/02-jadx-decode.md:5-6` (apktool 3.0.3 provisioned via `REA_APKTOOL_COMMAND=/usr/bin/apktool`), `:48-54` (apktool `manifest` = full decoded XML) | Wave evidence behind the r4u-02 entry. | Shows the same apktool 3.0.3 binary on the same host that revenger's probe would call. |
| tsukuroi | `tsukuroi-shokunin/.ufo/waves/round-21/candidate/SKILL.md:100-102` (`android-apktool-bin` 3.0.3-1 is foreign, AUR-built); `tsukuroi-shokunin/corpus/knowledge/update-safety-v2.md:161` (`aur-local` row: `-Syu` reach none; rebuild from `~/.cache/yay`); `:175-176` (`apktool_3.0.3.jar` sha256 equals the PKGBUILD `sha256sums[0]`) | Host package provenance for the apktool binary. | **Coupling risk for revenger's decoder pin.** The apktool revenger's probe would run is the same AUR-local package; tsukuroi says no repo update path exists for it. Revenger's probe records the version line (claims §C2b) and should not assume a stable package. |
| tsukuroi | `tsukuroi-shokunin/corpus/knowledge/package-state-plane.md:59-60` (explicit-foreign trio, apktool + obsidian-cli `yay` caches) | Same provenance split. | As above. |
| tsukuroi | `tsukuroi-shokunin/corpus/knowledge/update-safety-v3.md:109` (row 1: `android-apktool-bin` `aur-local`, no measurable pending update) | Re-measured status. | As above. |
| kasegi | `kasegi-shokunin/corpus/knowledge/mission-control.md:148-150` ("signature-verified APK acquisition + smali-level deeplink trace, recorded as residual lead not-a-finding") | Bounty-side APK acquisition; not in kasegi PROVINCE. | Adjacency watch only: revenger's bounty route (`revenger-shokunin/PROVINCE.md:9-13`) gates artifact access by a written scope record. Not an overlap with the authored-fixture capability. |
| kengaku, kotoba, kumitate, chousa, mori, lore, audio, game-dev-2d, game-dev-3d, tabi, mado, kotodama, kagi | `PROVINCE.md` checked: no APK/AXML/androguard/apktool/jadx hits | — | None. |
| kake, kama, souji, tameshi | PROVINCE + corpus checked: no APK-decoder hits in the windows read | — | None found. |

## 2. Contested scope (flagged, not absorbed)

1. **Android APK ownership is double-declared.** Revenger owns "Android APKs" (`revenger-shokunin/PROVINCE.md:3-4`). Kaidoku owns the APK surface through REA (`kaidoku-shokunin/PROVINCE.md:58`, `:136`). Tsukuroi's ledger records the duplicate as unresolved: `tsukuroi-shokunin/PROVINCE.md:128-129` (OUT-008/009), and `:150` ("Kaidoku/Revenger arbitration remains unresolved; ask the protocol integrator before an internals handoff").
2. **A proposed split already exists and points apktool at kaidoku.** `[fleet] .ufo/waves/kaika-w1/connect-sources.md:124-125`: "specialize `kaidoku` for live Linux environment binary/package analysis (Ghidra, apktool, unblob) and `revenger` for cross-platform offline evidence ledger verification." The round-100 capability is offline, authored-fixture, and evidence-ledger shaped, so it fits revenger under that split. Its decoder leg is apktool, which that same proposal assigns to kaidoku. The contest is therefore live on the decoder axis.
3. **Revenger's own record flags the same contest.** `[fleet] .ufo/reports/round-69/revenger.md:177-179`: "No cross-domain bleed … `R69ConnectorOverlap`: CONTEST-NAMED (ADJ-06 still open at fleet `l0-questions.md:42`) … APK noun named but the byte ground unclaimed by any sibling". The C2 capability does not change this: it claims authored-truth byte agreement, not provider output.
4. **No sibling implements an authored-truth two-decoder check.** Kaidoku's Android checks go through REA providers; nothing in the lanes scanned compares androguard against apktool on an authored fixture (see §1 and the `.py` scan in §3, which found no androguard/apktool/AXML hits in any `tools/`, `plans/`, `verifiers/`, or `corpus/*.py` read).

## 3. Admission-counter / gate leg patterns in siblings (for the r99 holdout classes)

Revenger's frozen v8 (`revenger-shokunin/reports/round-99/c1_k_admit_counter8.py`) already implements the five classes named in the task. The table gives the file:line baseline in v8 and the sibling analogues.

| r99 holdout class | Revenger v8 (baseline) | Sibling analogue | Reuse note for ExecCounterV9 |
|---|---|---|---|
| PASS-note length | `check_vote_notes` `:612-648`; `len(note.split()) < 6` → `PASS note needs >=6 tokens` at `:640-641`; n/a-style regex `:643-644`; shared-verbatim `:645-646` | `kaidoku-shokunin/tools/round-99/self-assessment-audit.py:16-18` (map rows must keep ≥20 non-space characters; stricter than the stem recipe); label `:140-142` | v8 already has the floor. The sibling check is a text-cell floor, not a note floor. No sibling PASS-note n/a regex was found in `kengaku-shokunin/plans/` or `kotoba-shokunin/verifiers/`. |
| Pinned-seat vote presence | `PINNED_SEATS` `:41`; `check_registry` `:226-244` (strict JSON, equals pinned map, `:239-243`); `check_votes` seat-not-pinned `:266-267`, role mismatch `:271-273`, candidate sha `:276` | `kengaku-shokunin/plans/gate_timing_check.py:5-8` (committed seat registry is the identity check); `:346-347` (seat not in committed wave registry); `:348-349` (role allowlist); `:350-352` (candidate has no writer; **seat equals writer → self-review excluded**) | **Candidate leg not seen in v8.** Writer/self-review exclusion (`gate_timing_check.py:352`) is not among the `check_votes` lines I read (`revenger-shokunin/reports/round-99/c1_k_admit_counter8.py:252-276`). Whether v8 excludes self-review elsewhere was not verified. |
| Derivation re-run | `evaluate` derivation table `:1003`, `:1048-1062` (FG15 Q-set; FG11 fixture-sha match), `:1096-1099` (C14 digests) | `kengaku-shokunin/plans/attrib_calibration.py:306-307` (`rederive(block)` recomputes every stored line from its own rows), `:371`, `:382` (`_rederive_summary`), `:567`, `:577` (mismatch line `stored=… recomputed=…`); `kengaku-shokunin/plans/battery37/p910.py:28-32` (`_argv` adds `--rerun`), `:57-63` (M41 receipt-deleted branch of `c_rerun`); `kengaku-shokunin/plans/battery38/p10b.py:36-53` (accept fixture whose fresh probe output is byte-equal to its receipt; N15 mirror) | The sibling re-run pattern is "fresh probe output byte-equal to a committed receipt, plus a mirror accept fixture". Revenger's v8 derivation check is table-based, not run-based. The mirror-accept fixture is the reusable kill shape for "a re-run that reproduces must pass". |
| Pinned body digests | `digest()` `:136-138`; `check_c14_digests` `:751-` (fixed fixture and `S506.body` digests); `check_ownwork_paths` `:671-` | `kengaku-shokunin/plans/attrib_probe.py:157-158` (sha of the frozen block bytes), `:183-187` (pinned sha vs block; two reads, both must equal); `:541-543`, `:990-992` (instrument sha recorded in every receipt); `kengaku-shokunin/plans/attrib_calibration.py:497-499` (`P1_SHA256` frozen manifest), `:521-522` (`manifest_mismatches`) | Double-read stability (`attrib_probe.py:171-172`, `:186-187`) is a reusable pattern: it defeats a pin that changes between reads. v8 pins fixed paths only; a manifest-style pin (`attrib_calibration.py:497-499`) would cover a whole receipt set. |
| Anchor carries claim | `check_quote_bytes` `:701-725` (1-based byte-range quote check); `check_embed_nonvacuous` `:485-` | `kengaku-shokunin/plans/anchor_line_check.py:2-10` (a line-cited quote must sit on the line it cites), `:12-22` (three checks: line substring, range contains N, `(K words)` equals `len(quote.split())`), `:107-124` (`anchor_quotes`), `:210-220` (selftest fixtures); `kengaku-shokunin/plans/anchor_digest_check.py:9-13` (global digest set defect), `:15-22` (one token per named capture), `:66-67` (`anchor-unbound`), `:108-112` (erratum exemption must be row-scoped), `:125-126` (binding limit: locator and digest rewritten together) | Kengaku has the most developed "anchor carries claim" family. Two reusable ideas: exact word-count equality (not a minimum) and row-scoped digest binding. v8 has no equivalent row-scoped binding. |

Summary: v8 already covers PASS-note length, and most of pinned-seat and digest classes. Gaps against sibling practice are (a) writer/self-review exclusion among pinned seats, (b) double-read stability on pins, (c) a mirror-accept fixture for re-runs, (d) row-scoped digest binding. These are candidates for ExecCounterV9 only if the L1 accepts them as frozen legs; the lane's own claims freeze governs.

## 4. Pointer message to ExecCounterV9

Sent one short pointer list (see §3 for context). No other peer was messaged.

## 5. Adjacency verdict

**Revenger: UNCHANGED.**

Evidence:
- No sibling counter or gate implements an authored-truth two-decoder agreement check (§1, §2 item 4). So the new capability does not duplicate a sibling gate, and no sibling gate is weakened or displaced.
- No sibling artifact is changed by the probe, and the probe reads only `corpus/fixtures/apk-r65/` (claims §C2). Kaidoku's REA-routed apktool results are not consumed.
- The overlap that exists (APK ownership, `revenger-shokunin/PROVINCE.md:3-4` vs `kaidoku-shokunin/PROVINCE.md:58`; apktool binary provenance, `tsukuroi-shokunin/corpus/knowledge/update-safety-v2.md:161,175-176`) was already unresolved before this round (`tsukuroi-shokunin/PROVINCE.md:150`, `[fleet] .ufo/reports/round-69/revenger.md:177-179`). The capability neither resolves nor enlarges it. Per the instruction, nothing was absorbed.
- Revenger's gain is therefore not a sibling-verified improvement. It is a calibration of revenger's own decoder claim (claims §C2), which is outside this seat's adjacency measure.

Why not "improved": no sibling gate changed or was shown weaker. Why not "harmed": no sibling surface was written, displaced, or double-counted by a revenger claim.

## 6. Open questions for the L1

1. ADJ-06 arbitration (`[fleet] l0-questions.md:42`, cited by `.ufo/reports/round-69/revenger.md:177-179`): does the operator/integrator rule who owns Android decode before the round-100 capability row is added? The capability's apktool leg is the disputed ground (`[fleet] .ufo/waves/kaika-w1/connect-sources.md:124-125`).
2. Shared apktool binary: the probe's apktool leg resolves through PATH per the frozen contract. On this host that is the AUR-local `android-apktool-bin` package (tsukuroi, §1). Should the probe record the resolved absolute path and PKGBUILD digest, not only the version line?
3. Writer/self-review exclusion (§3, `gate_timing_check.py:352`): if ExecCounterV9 adopts it, it must be a new leg (v9 adds legs, never edits v8). Whether to adopt is the L1's decision under the frozen claims.

## 7. Verification of this file

Every factual claim above carries a path and line taken from a read or grep hit in this session. Line numbers were read from output; they were not re-derived by re-running checks. No check was run to verify a verdict. Revenger's frozen counters and probes were not executed.
