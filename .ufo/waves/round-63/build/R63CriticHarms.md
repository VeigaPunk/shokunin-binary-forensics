# R63CriticHarms — build-state guard pre-check

Reviewer: `revenger-r63.R63CriticHarms`. Round 63, attempt 1 only.

Axes protected: **coverage** (K/F evidence and coverage-map identity), **calibration** (receipt/replay census and unchanged quality gates), **freshness** (preserved evidence), and **operability** (reproducible guard checks). This is a scoped working-tree observation during the concurrent build, not a claim/admission verdict or final committed-tree measurement.

Read the frozen contract `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/claims.md`, especially lines 111–120, the frozen counter `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure.py`, and the existing red-before receipt `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure-before.log`. Comparison base: `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`.

## Per-guard results

| Guard | Result | Observed evidence |
|---|---|---|
| 1. Preservation manifest exists and covers live + fixtures | **CHECKABLE** | `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/preservation-base.sha256` exists and has 455 records: 443 baseline live/fixtures records, followed by 12 supplemental references. The base Git tree independently counts 443 live/fixtures paths. A baseline-path-to-manifest membership comparison returned no missing paths. Its capture receipt reports 345 live and 98 fixture files, an initially clean live/fixtures status, and reconciliation against the base. |
| 2. README unchanged before fresh gate decisions | **CHECKABLE** | The requested `git diff --stat 55bcb6e` check for README returned no output. No premature README change was observed by this check. |
| 3. Q01–Q13 unchanged | **CHECKABLE** | The requested full `git diff 55bcb6e` check for QUALITY returned no output. The whole file was unchanged, not merely selected Q rows. |
| 4. Exactly ten verifier files; no additions/deletions | **CHECKABLE** | The absolute-path `glob` for `corpus/verify_*.py` returned ten files. All ten names also exist at the base. Git's additions/deletions check and its file-summary check returned no output. This checks identity as well as the count. |
| 5. Frozen measure.py digest | **CHECKABLE** | `sha256sum` returned exactly `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`. |

Preservation capture/provenance receipt: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63Preservation.md`, especially lines 5–16. I inspected the completed manifest and independently checked its baseline path coverage; I did not rerun all 443 stored digest comparisons.

Additional boundary observations: the tracked live/fixtures diff against the base was empty. The separate untracked-path census listed only these eight files, all within the two authorized new round-63 directories:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stderr.txt`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw`

## Executed read-only check evidence

Each command below completed with the stated output; no payload or verifier was executed.

```sh
# Empty output:
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --stat 55bcb6e -- corpus/README.md
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff 55bcb6e -- corpus/QUALITY.md
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --name-status --diff-filter=AD 55bcb6e -- 'corpus/verify_*.py'
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --summary 55bcb6e -- 'corpus/verify_*.py'
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --name-status 55bcb6e -- corpus/live corpus/fixtures

# 443:
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin ls-tree -r --name-only 55bcb6e -- corpus/live corpus/fixtures | wc -l

# Empty output means every baseline path has a manifest record:
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin ls-tree -r --name-only 55bcb6e -- corpus/live corpus/fixtures | sort | join --nocheck-order -1 1 -2 2 -v 1 - /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/preservation-base.sha256

# 455 records:
wc -l /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/preservation-base.sha256

# Exactly the eight allowed paths listed above:
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin ls-files --others -- corpus/live corpus/fixtures

# Expected frozen SHA-256:
sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure.py
```

The current verifier roster came from the file-structure tool's absolute pattern `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_*.py`; its ten names match the ten baseline names and manifest supplemental rows 444–453.

## Counterexamples and smallest safe correction

- **Hash-only preservation is incomplete.** [INFERENCE] Adding a file outside the two authorized new directories would leave every stored baseline hash unchanged. The separate tracked-delta and untracked-path checks above close that blind spot for this observed build state. Keep both baseline-byte verification and a complete path-delta/allowlist comparison at final admission; never treat manifest existence alone as a preservation pass. Impact: coverage provenance, freshness, calibration.
- **Count-only replay is incomplete.** [INFERENCE] A one-out/one-in verifier replacement can preserve a count of ten. The frozen counter discovers scripts dynamically at lines 167–178 and compares replay successes to `len(results)` at lines 179–181, not a fixed ten-name baseline. The identity checks above therefore matter; retain them rather than changing the frozen counter. Impact: calibration and replay operability.
- **Do not apply the entire 455-record manifest as an unconditional hold.** Its final 12 rows include the deliberately changed C3 verifiers and later-authorized README/SOURCES changes. The immutable byte check must use the 443 live/fixtures baseline records, while the other records remain comparison references. Blanket acceptance of all manifest mismatches would hide real harms; blanket rejection would reject authorized work. This distinction is already documented by the preservation owner.

These are fixable guard-composition risks, not evidence of an observed triggered void in the five requested checks, and not permission to trade harms for claimed improvements. The frozen counter's `HOLDS_OK` is not a universal harms certificate. This review does not establish the final numerical holds, all baseline held-row identities, firmware byte-oracle agreement, or fresh Q01–Q13 admission decisions. L1's final committed-tree checks remain authoritative; the README check here is explicitly before its authorized C06 flip.

Tooling: read `/home/vgpnk/.omp/agent/RULES.md`; no tools installed or updated, no pacman transactions, no runtime/judge invocation, no fixture execution, and no builds/tests/linters/formatters run. Only this assigned report was written; no scratch files created.
