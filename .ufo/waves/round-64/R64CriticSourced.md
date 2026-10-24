# R64CriticSourced — sourced-claim dependency attack

## Axes

Coverage K / expansion (C1 admission), depth (correct interpretation of region-size fields), and calibration (honest source dependency and provenance). No C2 mutation or calibration measurement was run.

## Finding: required entry unavailable; deletion result unestablished

The source-removal attack cannot be executed against an absent entry. Both designated entry locations returned `Path ... not found` when read:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md`
- `/tmp/revenger-r64-entry/candidate.md`

The second location was discovered in the round dispatch artifact, not inferred. The independent-leaf instruction requires recording this dependency rather than waiting for its author. I therefore did not invent an entry, create a substitute mutant, or infer that S036 is decorative. No scratch deletion was performed and no sourced-claim/admission verdict is supplied.

## Counterexample pressure and local evidence

1. `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:41-49` confines S036 to version-scoped route semantics and S037 to byte/record correspondence. Fixture offsets, lengths and content digests alone therefore do not demonstrate a need for S036.
2. `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:68` supplies a direct local precedent: the REA JavaScript guide was excluded because it was “useful for record semantics but not load-bearing for any entry sentence.” Merely adding a guide citation to frontmatter would reproduce that problem.
3. The same registry's firmware search note at `:75` says the byte oracle settled the firmware agreement and excluded the then-opened guide. Its current registry ends at S035 (`:49`); the newly required S036/S037 rows were not present in that read. This is a current dependency observation, not a claim about final integration.
4. The designated local guide snapshot exists at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`. Its `Interpret the results` section (`:91-95`) states that `reported_size` preserves Binwalk output, that unknown lengths can be replaced by the next signature or EOF, and that signatures/confidence do not prove valid partitions. I read that text; I did not independently establish the snapshot's upstream tag or digest.
5. `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:13,16,21-23` requires scope-correct support, tool/function/version attribution, byte-limited digest claims and in-entry derivations. A documentation citation must not become authority for independently derived fixture values or producer authenticity.

## Exact sentence that could require S036

Proposed wording, **not observed in a draft**:

> For this route, Binwalk can replace an unknown length with the next signature or EOF before serialization; therefore agreement with the byte-derived member lengths below does not establish that `reported_size` denotes independently validated partition extents.

The first clause needs the guide's route semantics; a fixture, truth file and saved JSON literals cannot establish that general field behavior. The second clause makes that dependency relevant to interpreting C1's comparison rather than an unrelated documentation ornament. It must remain version-scoped to the pinned guide and supported by the actual comparison. Whether the candidate contains this or an equivalent load-bearing sentence is **unobserved: no candidate was available**.

## Smallest safe correction

Supply the actual finished candidate plus the opened S036 row/located Gate quote, then remove S036 support from a private copy and identify the exact comparison interpretation that loses its only support. If every substantive C1 sentence remains independently supported by S037, the registered S036 dependency is still unestablished; a source-list citation alone does not repair it. A narrowly sourced interpretation boundary such as the sentence above can address the defect without claiming extraction, execution, authenticity, completeness, or a new capability. Do not report this seat as an executed deletion attack or an all-criteria admission decision.

## Scope / tooling

Read-only review apart from this assigned report. No production edits, runtime invocation, git/jj mutation, measurement rerun, install/update, or scratch artifact creation. Missing prerequisites: the actual candidate and its final source-row linkage. This is a fixable evidence dependency, not an established axis tradeoff; canonical judgment remains with its assigned judge.

Report: .ufo/waves/round-64/R64CriticSourced.md
