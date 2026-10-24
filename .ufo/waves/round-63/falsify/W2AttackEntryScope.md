# W2AttackEntryScope — C1 Q10 and frozen scope

Reviewer: `revenger-r63.W2AttackEntryScope` (independent falsify leaf).

**Scoped verdict: scope CLEAN; Q10 pass recommendation.** No universal ZIP/parser/provider finding, affirmative trailing-bytes finding, or ZIP64-present claim was found. Observation/Inference/Unknown separation and named limitations are present. This is not admission, an all-Q pass, or a C1/K counter decision. A separate, reproducible Q11 transcript defect is reported below.

## Axes and immutable evidence

- Attacked axis: **coverage, C1/K (C06), specifically Q10 and the frozen claim boundary**. Quality/provenance are holds, not permission to weaken the entry. No calibration or freshness improvement is claimed by this leaf.
- Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
- Reviewed committed tip: `db55bd6488e24e956df5818ae34c2a043d7ddc12` (candidate/source/lesson integration immediately after the stated build commit).
- `E` below means `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-63-zip-central-directory-evidence.md`.
- `C` means `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/claims.md`.
- The relevant files were extracted with `git archive db55bd6488e24e956df5818ae34c2a043d7ddc12` into leaf-owned scratch. SHA-256 equality between the archive and the opened lane files was observed for E, C, QUALITY, SOURCES and the APPNOTE snapshot. Thus the findings concern committed bytes, not an uncommitted candidate.
- E SHA-256: `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53`.
- C SHA-256: `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31`.
- Canonical criterion: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:22`; admission separation/limitation requirement: `:32-33`.
- Frozen boundary: C:23-31, especially “correspondence for this one fixture” and the four exclusions. No contract, quality criterion, source registry or candidate was edited.

## Located attacks

| Item / attacked claim | Strongest local counterexample attempted | Evidence and result | Smallest safe correction |
|---|---|---|---|
| S1 — C1/Q10, universal ZIP or general-parser scope | Promote the readout's successful parse and exact member-name sets to a statement about all ZIPs or general parsers. | E:10 explicitly denies being a ZIP parser or inventory tool. E:189-193 scope each inference to the named archive/oracle/record; E:189 says this is not a general property of ZIP archives. E:211-213 refuse generalization to other implementations, archive families, providers or versions. The “All values MUST…” sentence at E:654 is a located specification quotation about field byte order, not a universal empirical provider finding. **No scope violation found.** | None for Q10. |
| S2 — C1/Q10 and frozen provider-accuracy/completeness/authenticity exclusions | The saved record says `normalized_result.coverage.status = "complete-within-substeps"`, retains one observation and reports zero omitted observations; the two expected member names also appear. This is the strongest local bait for silently promoting agreement into complete or authentic inventory. | E:155 labels provider/Evidence-ID metadata recorded, not authenticated. E:163-175 label executable/encrypted/hash-status values recorded. E:193 explicitly refuses completeness, general correctness and authenticity. E:195 denies provenance/authenticity from digest matches; E:199-205 keep field correctness and completeness unknown. E:215 repeats the provenance limit. **The stronger saved-record declaration is not adopted by the entry.** | None for this scope attack; do not replace the unknowns with the saved record's self-description. |
| S3 — C1 frozen exclusion of trailing-bytes claims | Treat the end-relative EOCD position (22) or a quotation of the saved inventory limitation as proof of absent trailing bytes or as a tested producer boundary. | E:49 and E:57 report this fixture's EOCD/CD positions. E:201 attributes “bytes after the central directory are not occurrences” to the saved record's own limitations, then says the entry “neither confirms nor denies that boundary.” E:193 also says that stated limitation is not tested; E:211 claims nothing about undescribed regions. **No affirmative trailing-byte presence/absence, completeness or producer-policy result is asserted.** | None. Keep the attribution and explicit non-confirmation together. |
| S4 — C1 frozen scope, ZIP64-present claim | Infer ZIP64 support or presence from the specification's ZIP64 discussion or the script's field decoding. | E:221 explicitly puts ZIP64 outside scope and says its records are not read; E:655 excludes ZIP64 support from S032's use. The script at E:339-628 reads ordinary LFH/CD/EOCD fields and no ZIP64 record. No positive ZIP64-present statement was located. **No scope violation found.** | None. No ZIP64 support or absence theorem should be added. |
| S5 — C1 admission procedure, epistemic separation | Treat a recorded producer/library string as independently demonstrated behavior, or present member agreement as an observed universal. | Observation starts at E:12; the recorded-provenance note at E:143-149 explicitly relies on the build string for no value. Inference starts at E:187 and items 17-20 name their observational bases. Unknown starts at E:197 and preserves untested flags, completeness and behavior. **Separation is present; recorded facts are not promoted to authenticated origins.** | None for the assigned separation check. |
| S6 — C1 admission procedure, named limitation and scope granularity | Inflate this single-fixture contribution into all of C06's fixture grounds. | “Single fixture” at E:213 is an explicit named limitation. “Recorded, not authenticated” at E:215 is another. E:5 and E:225 say nested-r11 and duplicate-r15 are not examined. E:706 declares no cross-lane ownership or other lane's file as supporting evidence; this leaf makes no external lane-overlap finding. **The required named limitation is present.** | None for the assigned limitation check. C06 admission remains outside this leaf's authority. |

## Fresh reproduction and source reopening

Both new source rows were reopened at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:46-47`.

- S032: reopened the [official APPNOTE URL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), sections 4.3.7, 4.3.12 and 4.3.16, and the committed snapshot's byte-order, CRC, local-offset and count anchors. The snapshot SHA-256 is `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`.
- S033: reopened the authored truth JSON, saved record and ledger; the archive itself was read as bytes by the reproduced readout. The saved `complete-within-substeps` and limitation fields were inspected directly, not inferred from entry prose.

The committed Code fence was saved verbatim to scratch `readout.py` and run against the immutable archived inputs with `python3 -B .../readout.py ...` from `/`:

- Exit **0**, empty stderr, **17 stdout lines**; stdout equals the committed full output block byte-for-byte.
- stdout SHA-256: `02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4`.
- script: **328 lines**, SHA-256 `94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac`.
- `wc -c` snapshot: **174585 bytes**.
- Re-derived EOCD offset **2942**, CD offset **2828**, CD size **114**, parsed entries **2**, both EOCD entry counts **2**; saved occurrence paths `[".","README.txt","bin/checksum"]`.
- All ten quoted `wc -w` counts were rerun, in entry command order: **7, 21, 7, 10, 8, 23, 24, 20, 23, 12**. Each remains within 25 words, but one committed count is wrong (below).

No firmware or archive member was executed; no producer was invoked. No frozen K/F/C3 counter result or overall wave pass is asserted by this scoped leaf.

## F1 — separate C1/Q11 factual-transcript counterexample

**Location: E:291-292.** The committed entry shows:

```text
$ printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w
8
```

I ran that exact pipeline and observed **7**, not 8. This is a concrete command/output disagreement, not an inference or an over-25-word quote. It does **not** falsify the scope-clean finding above, but it is an independently reproduced defect in C1's claimed in-entry factual transcript, for the Q11 seat and canonical adjudication.

- Impacted axis: **coverage K via C1's Q11 quality gate**; no direct F or C3 effect.
- Smallest safe correction: replace only the displayed `8` at E:292 with `7`; retain the quote, derivation and unchanged criterion. No source or frozen-contract rewrite is needed.
- The evidence was sent to `revenger-r63.W2AttackEntryQ11` for its assigned review. This leaf did not modify or integrate the candidate.

## Tooling and boundary

Read `/home/vgpnk/.omp/agent/RULES.md` before tooling use. **No installs or updates**; no pacman transaction. Existing tools observed: Python **3.14.8**, Git **2.56.0**. Only this named report and leaf-owned `/tmp/revenger-r63-W2AttackEntryScope-db55bd6` scratch were written. Scratch is removed after this report lands. C2 and C3 are separate assigned wave slices, not decisions made here.
