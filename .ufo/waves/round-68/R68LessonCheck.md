REQUIREMENTS-STATE — (1) round 68 must mine the **landing/registry-drift** class: the authoritative registry row `SKILL.md:268` still asserts the pre-repair "can never fire" limitation that the landed r68 gate removed; its fix only counts if the lesson carries the committed negative-spoof control as the falsifier. (2) The S045 word count **is still uncorrected** in committed bytes at `corpus/lessons/round-67.md:75` ("18 words"; actual 19); the correction must land as a superseding row in `corpus/lessons/round-68.md`, never in place.

seat: L1Revenger68.R68LessonCheck · lane: /home/vgpnk/Projects/shokunin/revenger-shokunin · HEAD at read: `4232235` (build) · read-only seat, nothing edited outside this file · no tool installs

## Read set (absolute paths)

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/claims.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-67.md` (M44 `:126`, M45 `:127`, S045 `:75`, Routed forward `:155-161`)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-67-verifier-spotcheck.md:225-245` (routed defects D1–D4)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-66.md:53` (M40 row: the correction rule precedent)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md:118`, `:135`, `:264-270`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py:100-170`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py:455-528`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure-before.log`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/snapshots/ResourceTypes.h`, `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/derive_axml_anchors.py`, `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:59,61,99`

## Answer 1 — the mistake class round 68 must mine

**Class.** *Landing / registry drift* — a registered instrument's authoritative description is not re-derived from the landed instrument bytes after a repair, so the registry asserts a limitation the fix removed. This is M45's surface **inverted**: r67's row claimed a positive capability the gate did not have; r68's row claims a negative one the gate no longer has. Same instrument, same registry, one repair apart.

**Evidence pointer (committed, resolvable).**

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
git show HEAD:SKILL.md | sed -n '268p'
```

Actual committed bytes (HEAD `4232235`; `sha256sum SKILL.md` = `9ece37809c842f5471dcf08a43842b285fb73a5222b1f4532b4e4234a3a04fc6`, byte-identical to the worktree, `git status --porcelain SKILL.md` empty):

> `| self-test | ... **correction 2026-10-24 (r67 adjudication):** the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and can never fire — seats `R67ReviewC7Gate`/`R67MutC7Kill`/`R67CriticC7Claim`; recorded limitation, reorder fix routed) |`

Against the landed instrument, `corpus/check_embedded_outputs.py:141-146`:

```
    if not caught:
        print("self-test: drifted entry not caught")
        print(MARKER)
        sys.exit(1)
```

`MARKER = "drifted entry output accepted"` at `:36`; frozen mutant removes `problems += drift(...)` in `evaluate` (`:88` def, `:105` call), so `caught` is False, the marker is printed **last**, then exit 1 — i.e. the row's "can never fire" is false on the bytes this round committed. Corroboration that the row was not re-derived: `git diff --stat f165908..4232235` lists 9 paths and **SKILL.md is not one of them**; the last commit touching it is `712ef61` (r67 adjudication).

**Captured-by.** The r67 spot-check's routed defect 2 — "Registry kind/description inconsistent with the landed text" (`corpus/lessons/round-67-verifier-spotcheck.md:228-233`), carried in `reports/round-68/claims.md` §Registered as D2. Note the honest gap: **no wave seat this round re-read `SKILL.md:268`** (the roster has no registry seat); the lesson must attribute the capture to this seat's read (`R68LessonCheck`) or to a hygiene seat, not invent a seat.

**Fix.** Rewrite the `self-test` field of `SKILL.md:268` from the measured after-run: drop the shadowing/limitation clause, state the frozen-mutant kill is the drifted-case branch with `MARKER` as its last output line, and bind the wording to the two measured controls.

**Falsifier — the evidence pointer the lesson MUST carry (a fix only counts once shown able to fail).** The corrected row may only claim attributed kills if the attribution rule can still refuse. The committed artifact for that is the negative-spoof control in the final measured log:

- `reports/round-68/measure-after.log` (must exist and be committed with the after-run — **it does not exist at HEAD**, `ls reports/round-68/` = `claims.md`, `measure-before.log`, `measure.py`) reading:
  `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`;
- mechanism, `reports/round-68/measure.py:460-467` — spoof substitution on the unique clause `MARKER = "drifted entry output accepted"` (verified unique: regex match count 1; the only other occurrence at `:21` is docstring prose, not the assignment) — and `:492`, `c7_neg_attributed += rc != 0 and last.endswith(C7_MARKER)`.

Why that is the falsifier and not decoration: if the repair had made attribution "any non-zero exit", the spoofed mutant would read `C7_NEG_SPOOF_KILLED_ATTRIBUTED=1/1` and the corrected registry row's claim would be false. The row's text is therefore falsifiable by a committed control.

**Caveat the lesson must state (or the row is overstated).** The neg pair reads **identically** on the base tree — `reports/round-68/measure-before.log`: `C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1` — so it falsifies the *attribution rule*, not the before→after delta. The delta artifact remains `C7_MUTANT_KILLED_ATTRIBUTED=0/1` (before) → `1/1` (after). Citing the neg pair alone as "the fix works" would be a false claim.

**Conditional alternative (state only if it fires).** If the wave's Q02 seat returns FAIL on the v3 bytes, the mined class flips to the M40/M44 anchor class, and its falsifier is already committed: `corpus/derive_axml_anchors.py` exits 2 on a missing/ambiguous symbol. My re-run on the landed bytes is clean, so the v3 entry is currently anchor-clean from this seat's view:

```
$ python3 -B corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
...
struct ResXMLTree_attrExt : 677
...
enum RES_XML_START_NAMESPACE_TYPE : 245
...
comment attributeStart : 686
field attributeStart : 687
exit=0
```

17 lines, byte-identical to the entry's item-11 block (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:130-147`); snapshot anchors verified directly (`sed -n '243,246p'` → `:244` is `RES_XML_FIRST_CHUNK_TYPE`, `:245` is `RES_XML_START_NAMESPACE_TYPE`; `:686` comment / `:687` `uint16_t attributeStart;`); `corpus/snapshots/ResourceTypes.h` and `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` both hash `56b88bc4…`.

## Answer 2 — the round-67 S045 word count (still uncorrected)

**Still uncorrected in the committed bytes — yes.** `git show HEAD:corpus/lessons/round-67.md | sed -n '70,80p'` prints, at committed line 75:

```
  file (everything but magic and this field); used to detect file corruption" (18 words). Seat
```

**Actual count is 19** by whitespace split of the quoted text (`adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption`):

```
$ python3 -c "q='adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption'; print(len(q.split()))"
19
```

Both 18 and 19 are ≤ 25, so the row stays conformant; the field is checkable and wrong. Everything else already states it correctly: `corpus/lessons/round-67-verifier-spotcheck.md:234` ("The lesson says 18 words; the quote is 19 words"), and `corpus/SOURCES.md:59` carries the checksum quote **without any word-count field**, so no SOURCES row is affected.

**Exactly where the correction must land.**

1. As a **superseding / errata row in `corpus/lessons/round-68.md` `## Mistakes`** (the file does not exist at HEAD — `git ls-tree --name-only HEAD corpus/lessons/` ends at `round-67-verifier-spotcheck.md` / `round-67.md`), whose evidence pointer cites `corpus/lessons/round-67.md:75` and states 19 words. Rule: `SKILL.md:135` (M40 row) — "corrections land as superseding rows (SOURCES rule 2) — **never in-place row edits**"; `SKILL.md:118` (SOURCES rule 2) — append-only, a correction is a new row. Precedent: `corpus/lessons/round-66.md:53` M40 — "the r65 lesson stays immutable history".
2. Logged in the round-68 report's sources/gate section, per `reports/round-68/claims.md` §Registered ("The round-67 routed defects D1–D4 … the S045 quote word count … are carried as repairs in this round's report and lesson").

**Must NOT be edited:** `corpus/lessons/round-67.md:75` (closed-round lesson bytes stay byte-preserved) and `corpus/SOURCES.md:59` (no word-count field to fix).

## Coverage / calibration state observed (read-only, not scored by this seat)

- `corpus/README.md:34` C05 row status = `uncovered`; knowledge column still names the retained **round-65** candidate. README not flipped — consistent with claims §C2 delta 5.
- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:9` `admission-status: candidate`; `:1/:2/:3/:4` source header carries S038/S043/S045/S046.
- `reports/round-68/measure-before.log` reproduces every red value claims.md declares: `K_HELD_BACKED=8/14`, `K_ROW C05 status=uncovered`, `C05_SINGLE_V3=no`, `HOLDS_C2_V3=no`, `C7_V3_CLEAN=n/a (no v3 file)`, `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, `HOLDS_OK_V5=no`, `HOLDS_OK_V6=no`, counter exit 0.
- Gate repair is reachable-by-construction for the frozen mutant (marker is the last printed line on the `caught is False` branch); the measurement of that is the mutant seats' charge, not this seat's.

## Out of scope / limits

- No `reports/round-68/measure-after.log`, no `corpus/lessons/round-68.md`, no round-68 report at HEAD: **the mined row and the S045 erratum are both still unlanded**, and the Answer-1 falsifier (neg-spoof pair) exists committed only for the base tree.
- This seat did not run the counter, the mutant, or the Q01–Q13 wave seats; no claim is upgraded from unobserved to observed. Anchor/derivation checks above are this seat's own read-only runs on committed bytes.
- No subagent dispatch, no git/jj mutation, no write outside this report. Tool installs: none.

Report: `.ufo/waves/round-68/R68LessonCheck.md`
